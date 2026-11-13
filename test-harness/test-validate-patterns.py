#!/usr/bin/env python3
"""Two-sided test evidence for test-harness/validate-patterns.py.

Tests:
  1. Valid sample against fixtures/probe-11/product/app-flow/APP_FLOW.md -> PASS (exit 0)
  2. Planted failure 1: Empty pattern register -> FAIL (exit 1)
  3. Planted failure 2: Missing mandatory register columns -> FAIL (exit 1)
  4. Planted failure 3: Detail section missing / subsection missing -> FAIL (exit 1)
  5. Planted failure 4: Uncited pattern without reservation DEC- ID / unknown screen citation -> FAIL (exit 1)
  6. Planted failure 5: Citation check count mismatch -> FAIL (exit 1)
  7. Planted failure 6: Boundary violations (component, hex, color, token, dimension) -> FAIL (exit 1)
  8. CLI argument check -> exit 2
"""

import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "test-harness" / "validate-patterns.py"
APP_FLOW = REPO / "fixtures" / "probe-11" / "product" / "app-flow" / "APP_FLOW.md"

VALID_SAMPLE = """# 02 — Interaction Pattern Library

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> Patterns are defined here once, then cited by ID.

## Rules for this artifact

- Every pattern has a stable `PAT-<NN>` ID and is defined before first use.
- "When not to use" is mandatory. A pattern without a refusal condition is a habit, not a decision.
- A pattern states the failure it prevents. If it prevents nothing, delete it.
- Patterns describe behaviour, not appearance. No component names, no animation curves, no colour.

## Pattern register

| Pattern ID | Name | When to use | When not to use | Failure it prevents | Used by screens |
|---|---|---|---|---|---|
| `PAT-01` | Selection navigation | The user must choose one item from a list to open | When items can only be viewed in place | Accidental entry into unwanted items | `SCREEN-01` |
| `PAT-02` | Automatic preservation | The user modifies content and expects it to be preserved | When changes require explicit confirmation | Unsaved data loss on navigation away | `SCREEN-02` |

## Pattern detail — `PAT-01`

**Behaviour.** The user selects a list row and the detail opens.

**Preconditions.** A list of saved drafts is displayed.

**Recovery.** The user can navigate back to the list.

**Refusal condition.** Do not use when items cannot be navigated into.

**Cited by.** `SCREEN-01`

---

## Pattern detail — `PAT-02`

**Behaviour.** As edits occur, state is saved automatically.

**Preconditions.** An open draft in the editor.

**Recovery.** Retry save affordance if write fails.

**Refusal condition.** Do not use where changes require explicit confirmation.

**Cited by.** `SCREEN-02`

---

## Reserved patterns

Patterns defined but not yet cited.

| Pattern ID | Reason reserved | Decision ID |
|---|---|---|

## Citation check — required at the end of the artifact

| Pattern ID | Cited by count | Status |
|---|---|---|
| `PAT-01` | 1 | CITED |
| `PAT-02` | 1 | CITED |
"""


def run_validator(art_text: str) -> tuple[int, str]:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f:
        f.write(art_text)
        tmp_path = pathlib.Path(f.name)
    try:
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), str(tmp_path), str(APP_FLOW)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return proc.returncode, proc.stdout + proc.stderr
    finally:
        tmp_path.unlink(missing_ok=True)


def test_suite() -> bool:
    all_ok = True

    # 1. Valid sample
    print("--- Test 1: Valid sample ---")
    rc, out = run_validator(VALID_SAMPLE)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 0 or "PASS" not in out:
        print("FAIL: Expected rc=0 with PASS")
        all_ok = False
    else:
        print("OK: Valid sample passed.")
    print()

    # 2. Planted failure 1: Empty pattern register
    print("--- Test 2: Planted failure 1 (Empty register) ---")
    bad_empty = VALID_SAMPLE.replace(
        "| `PAT-01` | Selection navigation | The user must choose one item from a list to open | When items can only be viewed in place | Accidental entry into unwanted items | `SCREEN-01` |\n| `PAT-02` | Automatic preservation | The user modifies content and expects it to be preserved | When changes require explicit confirmation | Unsaved data loss on navigation away | `SCREEN-02` |",
        "",
    )
    rc, out = run_validator(bad_empty)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "pattern register is empty" not in out:
        print("FAIL: Expected empty pattern register error")
        all_ok = False
    else:
        print("OK: Caught empty pattern register")
    print()

    # 3. Planted failure 2: Missing mandatory register columns
    print("--- Test 3: Planted failure 2 (Empty register columns) ---")
    bad_cols = VALID_SAMPLE.replace(
        "| `PAT-01` | Selection navigation | The user must choose one item from a list to open | When items can only be viewed in place | Accidental entry into unwanted items | `SCREEN-01` |",
        "| `PAT-01` | - | - | - | - | `SCREEN-01` |",
    )
    rc, out = run_validator(bad_cols)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "'Name' is empty" not in out or "'When to use' is empty" not in out:
        print("FAIL: Expected empty column errors")
        all_ok = False
    else:
        print("OK: Caught empty register columns")
    print()

    # 4. Planted failure 3: Detail section missing / subsection missing
    print("--- Test 4: Planted failure 3 (Detail / subsection defects) ---")
    bad_sub = VALID_SAMPLE.replace("**Refusal condition.**", "**Dropped refusal.**")
    rc, out = run_validator(bad_sub)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "missing subsection 'Refusal condition'" not in out:
        print("FAIL: Expected missing subsection error")
        all_ok = False
    else:
        print("OK: Caught missing subsection")
    print()

    # 5. Planted failure 4: Unknown screen citation
    print("--- Test 5: Planted failure 4 (Cites unknown screen) ---")
    bad_citation = VALID_SAMPLE.replace("`SCREEN-01`", "`SCREEN-99`")
    rc, out = run_validator(bad_citation)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "cites SCREEN-99, which is not in the frozen flow" not in out:
        print("FAIL: Expected unknown screen citation error")
        all_ok = False
    else:
        print("OK: Caught unknown screen citation")
    print()

    # 6. Planted failure 5: Citation check count mismatch
    print("--- Test 6: Planted failure 5 (Citation count mismatch) ---")
    bad_count = VALID_SAMPLE.replace("| `PAT-01` | 1 | CITED |", "| `PAT-01` | 99 | CITED |")
    rc, out = run_validator(bad_count)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "claims count 99, expected 1" not in out:
        print("FAIL: Expected citation check count mismatch error")
        all_ok = False
    else:
        print("OK: Caught citation count mismatch")
    print()

    # 7. Planted failure 6: Boundary violations
    print("--- Test 7: Planted failure 6 (Boundary violations) ---")
    bad_boundary = VALID_SAMPLE.replace(
        "The user selects a list row and the detail opens.",
        "The user clicks a button #FF0000 with red border of 16px and token sys.color.primary.",
    )
    rc, out = run_validator(bad_boundary)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1 or "matched component 'button'" not in out or "matched hex color '#FF0000'" not in out or "matched color 'red'" not in out:
        print("FAIL: Expected boundary violations")
        all_ok = False
    else:
        print("OK: Caught all boundary violations")
    print()

    # 8. CLI argument check
    print("--- Test 8: CLI argument check ---")
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
