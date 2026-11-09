#!/usr/bin/env python3
"""Fail-closed validator for Muse Phase 2/3 evidence bundles.

Validates that mandatory gate reports are present, current, successful,
read-only where required, and backed by evidence files. It does not execute or
re-interpret the scanners/tests named in those reports.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any

PASS = "PASS"
FAIL = "FAIL"
BLOCKED = "BLOCKED"
ARBITRATION = "ARBITRATION"
FLAKY = "FLAKY"
VALID_STATES = {PASS, FAIL, BLOCKED, ARBITRATION, FLAKY, "NOT_APPLICABLE"}
SECURITY_CHECKS = (
    "secret_scanning",
    "dependency_vulnerabilities",
    "static_security",
    "authorization",
    "network_boundaries",
    "build_release_configuration",
)
PLATFORM_CHECKS = (
    "build",
    "typecheck",
    "lint",
    "unit_tests",
    "state_matrix",
    "e2e",
    "visual_snapshot",
    "responsive_platform",
)


class GateValidation:
    def __init__(self, run_dir: Path) -> None:
        self.run_dir = run_dir.resolve()
        self.issues: list[tuple[str, str]] = []
        self.manifest: dict[str, Any] = {}

    def add(self, state: str, message: str) -> None:
        self.issues.append((state, message))

    def load(self, filename: str) -> dict[str, Any] | None:
        path = self.run_dir / filename
        if not path.is_file():
            self.add(BLOCKED, f"missing mandatory artifact: {filename}")
            return None
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.add(BLOCKED, f"cannot read {filename}: {exc}")
            return None
        if not isinstance(value, dict):
            self.add(BLOCKED, f"{filename} must contain a JSON object")
            return None
        return value

    def identity(self, artifact: dict[str, Any], name: str) -> None:
        for key in ("run_id", "candidate_sha"):
            expected = self.manifest.get(key)
            actual = artifact.get(key)
            if not isinstance(actual, str) or not actual.strip():
                self.add(BLOCKED, f"{name}.{key} is missing")
            elif actual != expected:
                self.add(FAIL, f"stale {name}: {key} does not match manifest")

    def evidence(self, record: Any, label: str, allow_na: bool = False, require_tool: bool = False) -> None:
        if not isinstance(record, dict):
            self.add(BLOCKED, f"{label} result must be an object")
            return
        state = record.get("status")
        if state not in VALID_STATES:
            self.add(BLOCKED, f"{label} has missing/unknown status")
            return
        if state == "NOT_APPLICABLE":
            if not allow_na:
                self.add(FAIL, f"{label} may not be marked NOT_APPLICABLE")
                return
            if not isinstance(record.get("reason"), str) or not record["reason"].strip():
                self.add(BLOCKED, f"{label} NOT_APPLICABLE requires a reason")
            self.evidence_file(record, label)
            return
        if state != PASS:
            next_state = state if state in {FAIL, BLOCKED, ARBITRATION, FLAKY} else BLOCKED
            self.add(next_state, f"{label} status is {state}")
            return
        if not isinstance(record.get("command"), str) or not record["command"].strip():
            self.add(BLOCKED, f"{label} is missing the executed command")
        if require_tool and (not isinstance(record.get("tool"), str) or not record["tool"].strip()):
            self.add(BLOCKED, f"{label} is missing the scanner/test tool identifier")
        if record.get("exit_code") != 0:
            self.add(FAIL, f"{label} did not report exit_code 0")
        self.evidence_file(record, label)

    def evidence_file(self, record: dict[str, Any], label: str) -> None:
        evidence = record.get("evidence")
        if not isinstance(evidence, str) or not evidence.strip():
            self.add(BLOCKED, f"{label} is missing evidence path")
            return
        rel = PurePosixPath(evidence)
        if rel.is_absolute() or ".." in rel.parts:
            self.add(FAIL, f"{label} evidence path must stay inside the run directory")
            return
        path = self.run_dir.joinpath(*rel.parts)
        try:
            path.resolve().relative_to(self.run_dir)
        except ValueError:
            self.add(FAIL, f"{label} evidence path escapes the run directory")
            return
        if not path.is_file() or path.stat().st_size == 0:
            self.add(BLOCKED, f"{label} evidence file is missing or empty: {evidence}")

    def run(self) -> dict[str, Any]:
        manifest = self.load("manifest.json")
        if manifest is None:
            return self.result()
        self.manifest = manifest
        if manifest.get("schema_version") != "1.0":
            self.add(BLOCKED, "manifest schema_version must be 1.0")
        if manifest.get("phase") not in (2, 3):
            self.add(BLOCKED, "manifest.phase must be 2 or 3")
        for key in ("run_id", "candidate_sha"):
            if not isinstance(manifest.get(key), str) or not manifest[key].strip():
                self.add(BLOCKED, f"manifest.{key} is required")

        platforms = manifest.get("platforms_required")
        if not isinstance(platforms, list) or not platforms:
            self.add(BLOCKED, "manifest.platforms_required must be a non-empty list")
            platforms = []
        elif (any(p not in ("web", "android") for p in platforms)
              or len(set(platforms)) != len(platforms)):
            self.add(BLOCKED, "manifest.platforms_required must contain unique web/android values")
            platforms = []

        security = self.load("security-review.json")
        if security is not None:
            self.identity(security, "security-review.json")
            if security.get("status") != PASS:
                state = security.get("status")
                next_state = state if state in {FAIL, BLOCKED, ARBITRATION, FLAKY} else BLOCKED
                self.add(next_state, f"security reviewer gate is {state}; Master arbitration cannot override it")
            if security.get("fresh_context") is not True:
                self.add(BLOCKED, "security reviewer must use fresh context")
            if security.get("reviewer_role") != "security-reviewer":
                self.add(BLOCKED, "security reviewer role must be security-reviewer")
            if security.get("read_only") is not True or security.get("modified_paths") != []:
                self.add(FAIL, "security reviewer must be read-only and report zero modified paths")
            checks = security.get("checks")
            if not isinstance(checks, dict):
                self.add(BLOCKED, "security-review.json.checks must be an object")
            else:
                for name in SECURITY_CHECKS:
                    if name not in checks:
                        self.add(BLOCKED, f"security review missing check: {name}")
                    else:
                        self.evidence(
                            checks[name],
                            f"security.{name}",
                            allow_na=name in {"authorization", "network_boundaries"},
                            require_tool=True,
                        )
            findings = security.get("findings")
            if not isinstance(findings, list):
                self.add(BLOCKED, "security-review.json.findings must be an array")
            elif any(not isinstance(item, dict) or item.get("status") != "RESOLVED"
                     for item in findings):
                self.add(FAIL, "security review contains an unresolved or malformed finding")

        regression = self.load("regression.json")
        if regression is not None:
            self.identity(regression, "regression.json")
            if regression.get("status") != PASS:
                state = regression.get("status")
                next_state = state if state in {FAIL, BLOCKED, ARBITRATION, FLAKY} else BLOCKED
                self.add(next_state, f"full regression gate is {state}")
            checks = regression.get("checks")
            immutable_check = "frozen_input_immutability" if manifest.get("phase") == 2 else "component_immutability"
            if not isinstance(checks, dict) or immutable_check not in checks:
                self.add(BLOCKED, f"regression.checks.{immutable_check} is required")
            else:
                self.evidence(checks[immutable_check], f"regression.{immutable_check}")
            platform_results = regression.get("platforms")
            if not isinstance(platform_results, dict):
                self.add(BLOCKED, "regression.platforms must be an object")
            else:
                for platform in platforms:
                    if platform not in platform_results or not isinstance(platform_results[platform], dict):
                        self.add(BLOCKED, f"regression missing required platform: {platform}")
                        continue
                    for check in PLATFORM_CHECKS:
                        record = platform_results[platform].get(check)
                        if record is None:
                            self.add(BLOCKED, f"regression.{platform} missing check: {check}")
                        else:
                            self.evidence(record, f"regression.{platform}.{check}")

        review = self.load("independent-review.json")
        if review is not None:
            self.identity(review, "independent-review.json")
            if review.get("status") != PASS:
                state = review.get("status")
                next_state = state if state in {FAIL, BLOCKED, ARBITRATION, FLAKY} else BLOCKED
                self.add(next_state, f"independent review gate is {state}")
            if review.get("fresh_context") is not True:
                self.add(BLOCKED, "independent reviewers must use fresh context")
            if review.get("read_only") is not True or review.get("modified_paths") != []:
                self.add(FAIL, "independent reviewers must be read-only and report zero modified paths")
            reviewers = review.get("reviewers")
            if not isinstance(reviewers, dict):
                self.add(BLOCKED, "independent-review.json.reviewers must be an object")
            else:
                for name in ("vision_ux", "code_architecture"):
                    record = reviewers.get(name)
                    if not isinstance(record, dict):
                        self.add(BLOCKED, f"independent review missing reviewer: {name}")
                    elif record.get("status") != PASS:
                        state = record.get("status")
                        next_state = state if state in {FAIL, BLOCKED, ARBITRATION, FLAKY} else BLOCKED
                        self.add(next_state, f"independent reviewer {name} is {state}")
                    else:
                        self.evidence(record, f"review.{name}")

        return self.result()

    def result(self) -> dict[str, Any]:
        states = {state for state, _ in self.issues}
        if not states:
            status = PASS
        elif FAIL in states:
            status = FAIL
        elif ARBITRATION in states:
            status = ARBITRATION
        elif FLAKY in states:
            status = FLAKY
        else:
            status = BLOCKED
        return {
            "schema_version": "1.0",
            "run_id": self.manifest.get("run_id"),
            "candidate_sha": self.manifest.get("candidate_sha"),
            "status": status,
            "merge_eligible": status == PASS,
            "issues": [{"state": state, "message": message} for state, message in self.issues],
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, type=Path,
                        help="Evidence directory containing manifest.json and gate reports")
    args = parser.parse_args()
    if not args.run_dir.is_dir():
        print(f"[BLOCKED] evidence directory does not exist: {args.run_dir}", file=sys.stderr)
        return 2
    validator = GateValidation(args.run_dir)
    result = validator.run()
    output = validator.run_dir / "gate-result.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["merge_eligible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
