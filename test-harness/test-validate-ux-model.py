#!/usr/bin/env python3
"""Two-sided test evidence for test-harness/validate-ux-model.py.

Tests:
  1. Valid sample against fixtures/probe-11 -> PASS (exit 0)
  2. Planted failure 1: Screen set mismatch -> FAIL (exit 1)
  3. Planted failure 2: Primary action missing / empty -> FAIL (exit 1)
  4. Planted failure 3: Missing subsection per screen / structural line > 100 -> FAIL (exit 1)
  5. Planted failure 4: Boundary violations (component, hex, color, token, dimension) -> FAIL (exit 1)
  6. Planted failure 5: Coverage table missing / incomplete -> FAIL (exit 1)
  7. CLI argument check -> exit 2
"""

import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "test-harness" / "validate-ux-model.py"
APP_FLOW = REPO / "fixtures" / "probe-11" / "product" / "app-flow" / "APP_FLOW.md"
VALID_UX_MODEL = REPO / "fixtures" / "probe-11" / "product" / "ux-design" / "01_SCREEN_UX_MODEL.md"


def run_validator(art_path: pathlib.Path, flow_path: pathlib.Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(art_path), str(flow_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return proc.returncode, proc.stdout + proc.stderr


def run_validator_text(art_text: str, flow_path: pathlib.Path = APP_FLOW) -> tuple[int, str]:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
        f.write(art_text)
        tmp_path = pathlib.Path(f.name)
    try:
        return run_validator(tmp_path, flow_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def test_suite() -> bool:
    all_ok = True
    valid_text = VALID_UX_MODEL.read_text(encoding="utf-8")

    # 1. Valid sample
    print("--- Test 1: Valid sample ---")
    rc, out = run_validator(VALID_UX_MODEL, APP_FLOW)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 0 or "PASS" not in out:
        print("FAIL: Expected rc=0 with PASS")
        all_ok = False
    else:
        print("OK: Valid sample passed.")
    print()

    # 2. Planted failure 1: Screen set mismatch
    print("--- Test 2: Planted failure 1 (Screen set mismatch) ---")
    bad_screens = valid_text.replace("## SCREEN-02 — Draft editor", "## SCREEN-99 — Unknown screen")
    rc, out = run_validator_text(bad_screens)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "screen SCREEN-02 exists in the frozen flow but has no entry" not in out:
        print("FAIL: Expected screen mismatch error")
        all_ok = False
    else:
        print("OK: Caught screen set mismatch")
    print()

    # 3. Planted failure 2: Primary action empty
    print("--- Test 3: Planted failure 2 (Primary action empty) ---")
    bad_action = valid_text.replace("| Primary action | Open a draft |", "| Primary action | none |")
    rc, out = run_validator_text(bad_action)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "primary action is empty" not in out:
        print("FAIL: Expected empty primary action error")
        all_ok = False
    else:
        print("OK: Caught empty primary action")
    print()

    # 4. Planted failure 3: Missing subsection per screen & line length > 100
    print("--- Test 4: Planted failure 3 (Missing section and structural line > 100) ---")
    bad_structure = valid_text.replace(
        "### Information hierarchy",
        "### Dropped hierarchy",
    ).replace(
        "+------------------------------------------+",
        "+" + "-" * 110 + "+",
    )
    rc, out = run_validator_text(bad_structure)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "missing required section '### Information hierarchy'" not in out or "exceeds 100 characters" not in out:
        print("FAIL: Expected subsection and line length errors")
        all_ok = False
    else:
        print("OK: Caught missing section and structural line length > 100")
    print()

    # 5. Planted failure 4: Boundary violations
    print("--- Test 5: Planted failure 4 (Boundary violations) ---")
    bad_boundary = valid_text.replace(
        "See all saved drafts and choose which one to open",
        "See all saved drafts and click button #ff0000 with red border of 16px and token sys.color.primary",
    )
    rc, out = run_validator_text(bad_boundary)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "matched component 'button'" not in out or "matched hex color '#ff0000'" not in out or "matched color 'red'" not in out or "matched dimension '16px'" not in out:
        print("FAIL: Expected boundary violations")
        all_ok = False
    else:
        print("OK: Caught all boundary violations")
    print()

    # 6. Planted failure 5: Coverage table missing screen
    print("--- Test 6: Planted failure 5 (Coverage table missing screen) ---")
    bad_cov = valid_text.replace("| `SCREEN-02` | yes | Save the draft | `CAP-01` | 4 (default, saving, saved, save-failed) |", "")
    rc, out = run_validator_text(bad_cov)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "coverage table: missing screen SCREEN-02" not in out:
        print("FAIL: Expected coverage table missing screen error")
        all_ok = False
    else:
        print("OK: Caught coverage table defect")
    print()

    # 7. CLI missing arguments
    print("--- Test 7: CLI argument check ---")
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
