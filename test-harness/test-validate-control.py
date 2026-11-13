#!/usr/bin/env python3
"""Two-sided test evidence for test-harness/validate-control.py.

Tests:
  1. Valid sample against fixtures/probe-11/product/ux-design/00_UX_CONTROL.md -> PASS (exit 0)
  2. Planted failure 1: Gate approved but approved_state_seq is null or missing event -> FAIL (exit 1)
  3. Planted failure 2: Missing decision_log file on disk (fail closed) -> FAIL (exit 1)
  4. Planted failure 3: Event key contract mismatch (missing required key, extra key) -> FAIL (exit 1)
  5. Planted failure 4: Lifecycle status inconsistent -> FAIL (exit 1)
  6. CLI argument check -> exit 2
"""

import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "test-harness" / "validate-control.py"
PROBE11_CONTROL = REPO / "fixtures" / "probe-11" / "product" / "ux-design" / "00_UX_CONTROL.md"


def run_validator(ctrl_path: pathlib.Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ctrl_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return proc.returncode, proc.stdout + proc.stderr


def run_validator_text(text: str, working_dir: pathlib.Path = PROBE11_CONTROL.parent) -> tuple[int, str]:
    tmp_path = working_dir / "temp_control_test.md"
    try:
        tmp_path.write_text(text, encoding="utf-8")
        return run_validator(tmp_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def test_suite() -> bool:
    all_ok = True
    base_text = PROBE11_CONTROL.read_text(encoding="utf-8")

    # 1. Valid sample
    print("--- Test 1: Valid sample ---")
    rc, out = run_validator(PROBE11_CONTROL)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 0 or "PASS" not in out:
        print("FAIL: Expected rc=0 with PASS")
        all_ok = False
    else:
        print("OK: Valid sample passed.")
    print()

    # 2. Planted failure 1: Gate approved but approved_state_seq is null or missing matching event
    print("--- Test 2: Planted failure 1 (Approved gate with null/unmatched state_seq) ---")
    bad_gate = base_text.replace(
        "approved_state_seq: 1",
        "approved_state_seq: null",
    )
    rc, out = run_validator_text(bad_gate)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "gate_1 status is APPROVED but approved_state_seq is None" not in out:
        print("FAIL: Expected gate approved_state_seq is None error")
        all_ok = False
    else:
        print("OK: Caught null approved_state_seq error")
    print()

    # 3. Planted failure 2: Missing decision_log file on disk
    print("--- Test 3: Planted failure 2 (Decision log missing on disk) ---")
    bad_dl_path = base_text.replace(
        "path: product/ux-design/08_DECISION_LOG.md",
        "path: product/ux-design/NONEXISTENT_DECISION_LOG.md",
    )
    rc, out = run_validator_text(bad_dl_path)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "decision log not found on disk" not in out:
        print("FAIL: Expected decision log not found on disk error")
        all_ok = False
    else:
        print("OK: Caught missing decision log file")
    print()

    # 4. Planted failure 3: Event key contract mismatch
    print("--- Test 4: Planted failure 3 (Event key contract mismatch) ---")
    bad_event = base_text.replace(
        "exact_user_command: APPROVE SCREEN UX MODEL",
        "bogus_command_key: APPROVE SCREEN UX MODEL",
    )
    rc, out = run_validator_text(bad_event)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "missing key 'exact_user_command'" not in out or "extra key 'bogus_command_key'" not in out:
        print("FAIL: Expected missing key and extra key errors")
        all_ok = False
    else:
        print("OK: Caught event key contract mismatch")
    print()

    # 5. Planted failure 4: Lifecycle status inconsistent
    print("--- Test 5: Planted failure 4 (Lifecycle status inconsistent) ---")
    bad_lifecycle = base_text.replace(
        "lifecycle_status: DRAFT",
        "lifecycle_status: FROZEN",
    )
    rc, out = run_validator_text(bad_lifecycle)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "lifecycle_status FROZEN requires gate_3 APPROVED" not in out:
        print("FAIL: Expected lifecycle inconsistency error")
        all_ok = False
    else:
        print("OK: Caught lifecycle inconsistency")
    print()

    # 6. CLI argument check
    print("--- Test 6: CLI argument check ---")
    proc = subprocess.run([sys.executable, str(VALIDATOR)], capture_output=True, text=True)
    if proc.returncode != 2:
        print(f"FAIL: Expected rc=2, got {proc.returncode}")
        all_ok = False
    else:
        print("OK: CLI argument check passed.")
    print()

    if all_ok:
        print("ALL TESTS PASSED: Two-sided verification complete.")
        return True
    else:
        print("SOME TESTS FAILED.")
        return False


if __name__ == "__main__":
    success = test_suite()
    sys.exit(0 if success else 1)
