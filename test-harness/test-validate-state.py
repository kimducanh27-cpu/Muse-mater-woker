#!/usr/bin/env python3
"""Two-sided test evidence for test-harness/validate-state.py.

Tests:
  1. Valid sample against fixtures/probe-11/product/app-flow/APP_FLOW.md -> PASS (exit 0)
  2. Planted failure type 1: Matrix invalid screen, placeholder state, invalid source -> FAIL (exit 1)
  3. Planted failure type 2: Non-recoverable state without valid DEC- ID -> FAIL (exit 1)
  4. Planted failure type 3: Lexical boundary violations (component, color, hex, dimension) -> FAIL (exit 1)
  5. Planted failure type 4: Coverage check totals mismatch -> FAIL (exit 1)
"""

import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "test-harness" / "validate-state.py"
APP_FLOW = REPO / "fixtures" / "probe-11" / "product" / "app-flow" / "APP_FLOW.md"

VALID_SAMPLE = """# 03 — State Experience

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> One row per screen × state that applies to that screen, projected from the frozen Process 04 state matrix.

## Rules for this artifact

- The state space belongs to Process 04. This artifact may not add a state. A genuinely missing state is a Change Request to Process 04.
- Every row states what the user **sees**, **understands** and **can do** — three different things. "Shows an error" fails all three.
- Every failure-bearing state needs a recovery affordance, or an approved decision that says there is none and why.
- No component names, no colour, no wording. Message intent belongs to artifact 04.

## Projection rule

A state applies to a screen when the frozen Process 04 matrix marks it applicable, or when the screen's transition set can produce it. Record the source of the projection:

| Projection source | Meaning |
|---|---|
| `P04-MATRIX` | The Process 04 matrix names this screen for this state |
| `P04-TRANSITION` | A transition into this screen can produce this state |
| `P04-EXPLICIT-EXCLUSION` | Process 04 excluded this state; the rationale must be quoted |

## Matrix

| Screen ID | State ID | Source | User sees | User understands | User can do | Recovery affordance | Pattern |
|---|---|---|---|---|---|---|---|
| `SCREEN-01` | `STATE-EMPTY` | `P04-MATRIX` | Empty workspace indicator and creation prompt | No existing drafts are saved | Initiate creation of a new draft | Inline creation trigger | `PAT-01` |
| `SCREEN-01` | `STATE-LOADING` | `P04-MATRIX` | Progress representation | Draft inventory is being retrieved | Wait or cancel retrieval | Cancellation affordance | `PAT-02` |
| `SCREEN-01` | `STATE-POPULATED` | `P04-MATRIX` | Chronological list of saved drafts | Available drafts ready for selection | Select a draft or initiate a new one | Navigation to editor | `PAT-01` |
| `SCREEN-02` | `STATE-DEFAULT` | `P04-MATRIX` | Editable content area with current content | Content ready for modification | Enter text or navigate away | Auto-preservation | `PAT-03` |
| `SCREEN-02` | `STATE-SAVING` | `P04-MATRIX` | Save activity indication | Changes are currently writing to store | Continue typing or await completion | Background queuing | `PAT-02` |
| `SCREEN-02` | `STATE-SAVED` | `P04-MATRIX` | Timestamped confirmation indicator | All edits persisted safely | Continue editing or leave screen | Retain current draft | `PAT-03` |
| `SCREEN-02` | `STATE-SAVE-FAILED` | `P04-MATRIX` | Unsaved indicator and failure context | Edits held in memory but not stored | Retry save or export current changes | Retry mechanism | `PAT-04` |

## Non-recoverable states — explicit register

States where recovery is genuinely impossible or out of scope. Each needs an approved decision; silence is a defect.

| Screen ID | State ID | Why recovery is impossible | Decision ID |
|---|---|---|---|
| None | | | |

## Coverage check — required at the end of the artifact

| Screen ID | States applicable in P04 | Rows present | Missing |
|---|---|---|---|
| `SCREEN-01` | 3 | 3 | none |
| `SCREEN-02` | 4 | 4 | none |

**Totals.** Applicable screen-state pairs: 7. Rows present: 7. Non-recoverable states with a decision: 0. Rows for states not in Process 04: 0 (any non-zero value blocks Gate 2).
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
        print("OK: Valid sample passed.\n")

    # 1b. Valid sample with non-recoverable state and DEC- ID
    print("--- Test 1b: Valid sample with approved non-recoverable state ---")
    valid_with_nonrec = VALID_SAMPLE.replace(
        "| None | | | |",
        "| `SCREEN-02` | `STATE-SAVE-FAILED` | Offline permanent media failure | `DEC-01` |",
    ).replace(
        "Non-recoverable states with a decision: 0.",
        "Non-recoverable states with a decision: 1.",
    )
    rc, out = run_validator(valid_with_nonrec)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 0 or "PASS" not in out:
        print("FAIL: Expected rc=0 with PASS for valid non-recoverable state")
        all_ok = False
    else:
        print("OK: Valid sample with approved DEC-01 passed.\n")

    # 2. Planted failure 1: Matrix row defects
    print("--- Test 2: Planted failure 1 (Matrix row defects) ---")
    bad_matrix = VALID_SAMPLE.replace(
        "| `SCREEN-01` | `STATE-EMPTY` | `P04-MATRIX` | Empty workspace indicator and creation prompt | No existing drafts are saved | Initiate creation of a new draft | Inline creation trigger | `PAT-01` |",
        "| `SCREEN-99` | `STATE-…` | `P04-INVENTED` | Empty workspace indicator | No drafts | Create draft | Trigger | `PAT-01` |",
    )
    rc, out = run_validator(bad_matrix)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    expected_matches = [
        "screen 'SCREEN-99' is not in the frozen flow inventory",
        "placeholder or empty State ID 'STATE-…'",
        "invalid source 'P04-INVENTED'",
    ]
    for em in expected_matches:
        if em not in out:
            print(f"FAIL: Missing expected error: {em}")
            all_ok = False
        else:
            print(f"OK: Caught: {em}")
    print()

    # 3. Planted failure 2: Non-recoverable state missing Decision ID
    print("--- Test 3: Planted failure 2 (Non-recoverable state without DEC- ID) ---")
    bad_non_rec = VALID_SAMPLE.replace(
        "| None | | | |",
        "| `SCREEN-02` | `STATE-SAVE-FAILED` | Storage hardware destroyed | PENDING |",
    )
    rc, out = run_validator(bad_non_rec)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    expected = "missing or invalid Decision ID ('PENDING')"
    if expected not in out:
        print(f"FAIL: Missing expected error: {expected}")
        all_ok = False
    else:
        print(f"OK: Caught: {expected}")
    print()

    # 4. Planted failure 3: Lexical boundary violations
    print("--- Test 4: Planted failure 3 (Boundary: component, color, hex, dimension) ---")
    bad_boundary = VALID_SAMPLE.replace(
        "Chronological list of saved drafts",
        "Chronological list of a card with red button of 16px and border #ff0000",
    )
    rc, out = run_validator(bad_boundary)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    boundary_matches = [
        "matched component 'card'",
        "matched component 'button'",
        "matched color 'red'",
        "matched hex color '#ff0000'",
        "matched dimension '16px'",
    ]
    for bm in boundary_matches:
        if bm not in out:
            print(f"FAIL: Missing expected boundary error: {bm}")
            all_ok = False
        else:
            print(f"OK: Caught: {bm}")
    print()

    # 5. Planted failure 4: Coverage check totals mismatch
    print("--- Test 5: Planted failure 4 (Coverage totals mismatch) ---")
    bad_totals = VALID_SAMPLE.replace(
        "**Totals.** Applicable screen-state pairs: 7. Rows present: 7. Non-recoverable states with a decision: 0. Rows for states not in Process 04: 0 (any non-zero value blocks Gate 2).",
        "**Totals.** Applicable screen-state pairs: 99. Rows present: 1. Non-recoverable states with a decision: 5. Rows for states not in Process 04: 2 (any non-zero value blocks Gate 2).",
    )
    rc, out = run_validator(bad_totals)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    totals_matches = [
        "coverage check totals: 'Applicable screen-state pairs' is 99, expected 7 from Process 04",
        "coverage check totals: 'Rows present' is 1, expected 7 (actual rows in Matrix)",
        "coverage check totals: 'Non-recoverable states with a decision' is 5, expected 0",
        "coverage check totals: 'Rows for states not in Process 04' is 2, expected 0 (blocks Gate 2)",
    ]
    for tm in totals_matches:
        if tm not in out:
            print(f"FAIL: Missing expected totals error: {tm}")
            all_ok = False
        else:
            print(f"OK: Caught: {tm}")
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
