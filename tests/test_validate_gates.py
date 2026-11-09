import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate-gates.py"


class GateValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.run_dir = Path(self.temp.name)
        (self.run_dir / "evidence").mkdir()
        for name in (
            "security-secrets.log", "security-deps.log", "security-static.log",
            "security-auth.log", "security-network.log", "security-build.log", "regression.log",
            "review-vision.log", "review-code.log",
        ):
            (self.run_dir / "evidence" / name).write_text("PASS\n", encoding="utf-8")
        self.write("manifest.json", {
            "schema_version": "1.0", "run_id": "run-001", "candidate_sha": "abc123",
            "phase": 3, "platforms_required": ["web", "android"],
        })
        self.write("security-review.json", {
            "run_id": "run-001", "candidate_sha": "abc123", "status": "PASS",
            "fresh_context": True, "reviewer_role": "security-reviewer",
            "read_only": True, "modified_paths": [], "findings": [],
            "checks": {
                "secret_scanning": self.check("security-secrets.log", "secret scanner"),
                "dependency_vulnerabilities": self.check("security-deps.log", "dependency audit"),
                "static_security": self.check("security-static.log", "static security scan"),
                "authorization": self.check("security-auth.log", "resource authorization tests"),
                "network_boundaries": self.check("security-network.log", "network boundary tests"),
                "build_release_configuration": self.check("security-build.log", "build and release configuration audit"),
            },
        })
        platforms = {}
        for platform in ("web", "android"):
            platforms[platform] = {
                name: self.check("regression.log", f"{platform} {name}")
                for name in ("build", "typecheck", "lint", "unit_tests", "state_matrix",
                             "e2e", "visual_snapshot", "responsive_platform")
            }
        self.write("regression.json", {
            "run_id": "run-001", "candidate_sha": "abc123", "status": "PASS",
            "checks": {"component_immutability": self.check("regression.log", "component freeze check")},
            "platforms": platforms,
        })
        self.write("independent-review.json", {
            "run_id": "run-001", "candidate_sha": "abc123", "status": "PASS",
            "fresh_context": True, "read_only": True, "modified_paths": [],
            "reviewers": {
                "vision_ux": {"status": "PASS", "command": "fresh vision audit", "evidence": "evidence/review-vision.log", "exit_code": 0},
                "code_architecture": {"status": "PASS", "command": "fresh code audit", "evidence": "evidence/review-code.log", "exit_code": 0},
            },
        })

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, value):
        (self.run_dir / name).write_text(json.dumps(value), encoding="utf-8")

    @staticmethod
    def check(file, command):
        return {"status": "PASS", "tool": "test-tool", "command": command, "exit_code": 0, "evidence": f"evidence/{file}"}

    def run_validator(self):
        return subprocess.run([sys.executable, str(SCRIPT), "--run-dir", str(self.run_dir)],
                              capture_output=True, text=True, check=False)

    def test_complete_evidence_bundle_passes(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads((self.run_dir / "gate-result.json").read_text())
        self.assertEqual(payload["status"], "PASS")
        self.assertTrue(payload["merge_eligible"])

    def test_missing_security_report_fails_closed(self):
        (self.run_dir / "security-review.json").unlink()
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(json.loads((self.run_dir / "gate-result.json").read_text())["status"], "BLOCKED")

    def test_security_veto_cannot_be_overridden(self):
        report = json.loads((self.run_dir / "security-review.json").read_text())
        report["status"] = "ARBITRATION"
        self.write("security-review.json", report)
        result = self.run_validator()
        payload = json.loads((self.run_dir / "gate-result.json").read_text())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(payload["status"], "ARBITRATION")
        self.assertFalse(payload["merge_eligible"])

    def test_security_reviewer_must_be_read_only(self):
        report = json.loads((self.run_dir / "security-review.json").read_text())
        report["read_only"] = False
        report["modified_paths"] = ["src/auth.ts"]
        self.write("security-review.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_security_report_requires_role_and_scanner_tool_ids(self):
        report = json.loads((self.run_dir / "security-review.json").read_text())
        report["reviewer_role"] = "worker"
        report["checks"]["secret_scanning"].pop("tool")
        self.write("security-review.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_phase2_requires_frozen_phase1_inputs(self):
        manifest = json.loads((self.run_dir / "manifest.json").read_text())
        manifest["phase"] = 2
        self.write("manifest.json", manifest)
        report = json.loads((self.run_dir / "regression.json").read_text())
        report["checks"] = {"frozen_input_immutability": self.check("regression.log", "phase 1 freeze check")}
        self.write("regression.json", report)
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_phase3_component_immutability_blocks(self):
        report = json.loads((self.run_dir / "regression.json").read_text())
        report["checks"] = {}
        self.write("regression.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_stale_candidate_sha_is_rejected(self):
        report = json.loads((self.run_dir / "regression.json").read_text())
        report["candidate_sha"] = "old-sha"
        self.write("regression.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_missing_android_regression_blocks(self):
        report = json.loads((self.run_dir / "regression.json").read_text())
        del report["platforms"]["android"]["responsive_platform"]
        self.write("regression.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_failed_check_blocks(self):
        report = json.loads((self.run_dir / "regression.json").read_text())
        report["platforms"]["web"]["e2e"]["status"] = "FAIL"
        self.write("regression.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_missing_evidence_file_blocks(self):
        report = json.loads((self.run_dir / "security-review.json").read_text())
        report["checks"]["secret_scanning"]["evidence"] = "evidence/missing.log"
        self.write("security-review.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_unresolved_security_finding_fails(self):
        report = json.loads((self.run_dir / "security-review.json").read_text())
        report["findings"] = [{"id": "SEC-1", "status": "OPEN"}]
        self.write("security-review.json", report)
        self.assertNotEqual(self.run_validator().returncode, 0)

    def test_arbitration_in_independent_review_is_not_pass(self):
        report = json.loads((self.run_dir / "independent-review.json").read_text())
        report["reviewers"]["code_architecture"]["status"] = "ARBITRATION"
        self.write("independent-review.json", report)
        result = self.run_validator()
        payload = json.loads((self.run_dir / "gate-result.json").read_text())
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(payload["status"], "ARBITRATION")


if __name__ == "__main__":
    unittest.main()
