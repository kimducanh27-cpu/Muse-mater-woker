#!/usr/bin/env python3
"""Two-sided test evidence for test-harness/validate-copy.py.

Tests:
  1. Valid sample against fixtures/probe-11/product/app-flow/APP_FLOW.md -> PASS (exit 0)
  2. Planted failure type 1: Content requirements defects (unknown screen, empty element, invalid req/opt) -> FAIL (exit 1)
  3. Planted failure type 2: Message intent register defects (placeholder MSG-…, placeholder state, empty job/tone/imply) -> FAIL (exit 1)
  4. Planted failure type 3: Boundary violations (component, hex color, color name, token, dimension) -> FAIL (exit 1)
  5. Planted failure type 4: Coverage check mismatches (count discrepancy, missing screen) -> FAIL (exit 1)
  6. Missing CLI arguments -> exit 2
"""

import pathlib
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "test-harness" / "validate-copy.py"
APP_FLOW = REPO / "fixtures" / "probe-11" / "product" / "app-flow" / "APP_FLOW.md"

VALID_SAMPLE = """# 04 — Content and Copy Intent

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> What content each screen requires, and the intent of each message. **Never final wording.** Final strings are composed in Process 07 against real layout constraints.

## Rules for this artifact

- Intent, not copy. "Tell the user the payment failed and that no money moved" is intent. "Payment failed. You have not been charged." is Process 07's job.
- Every message states its **job**: what the user must understand or do after reading it.
- Every message states its **tone constraint** and its **prohibited implication**. A failure message must not imply data loss when none occurred; a destructive confirmation must not imply reversibility.
- Character budgets are set in Process 07, not here. Do not guess a length.
- No placeholder that could be mistaken for approved copy.

## Content requirements by screen

| Screen ID | Content element | Required or optional | Source of truth | Notes |
|---|---|---|---|---|
| `SCREEN-01` | Workspace title and description | REQUIRED | User configuration | Identifies current draft collection |
| `SCREEN-01` | Draft inventory list items | REQUIRED | Local storage index | Chronological listing |
| `SCREEN-01` | Filter and sort options | OPTIONAL | Client state | Secondary filtering |
| `SCREEN-02` | Document headline input area | REQUIRED | Active draft data | Single-line editable field |
| `SCREEN-02` | Document narrative body editor | REQUIRED | Active draft data | Multi-line text body |
| `SCREEN-02` | Last saved status indicator | REQUIRED | Persistence store receipt | Relative or absolute timestamp |

## Message intent register

| Message ID | Screen ID | State ID | Trigger | Job of the message | Tone constraint | Must not imply |
|---|---|---|---|---|---|---|
| `MSG-01` | `SCREEN-01` | `STATE-EMPTY` | Empty collection retrieved | Guide user to initiate their first draft creation | Encouraging, straightforward | Must not imply that drafts were lost or deleted |
| `MSG-02` | `SCREEN-01` | `STATE-LOADING` | Draft retrieval in progress | Clarify that local storage is being accessed | Neutral, informative | Must not imply system stall or network failure |
| `MSG-03` | `SCREEN-02` | `STATE-SAVING` | Draft persistence initiated | Reassure user that edits are writing to disk | Subtle, unhurried | Must not imply user must halt interaction |
| `MSG-04` | `SCREEN-02` | `STATE-SAVE-FAILED` | Storage write error | Alert user to failure and prompt explicit retry | Direct, calm | Must not imply edits have been discarded from memory |

## Content that must never be shown

| Content | Why prohibited | Scope |
|---|---|---|
| Raw filesystem stack traces | Confuses user and leaks implementation internals | All screens |
| Internal storage row identifiers | Irrelevant to user draft tracking | All screens |

## Coverage check — required at the end of the artifact

| Screen ID | Required content elements | Message intents defined | States with a message | States with no message, and why |
|---|---|---|---|---|
| `SCREEN-01` | 2 | 2 | 2 | Populated state uses self-evident list items |
| `SCREEN-02` | 3 | 2 | 2 | Default and saved states use inline indicators |

Every failure-bearing state in artifact 03 must have at least one message intent, or an approved decision stating that the state is silent by design.
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

    # 2. Planted failure 1: Content requirements defects
    print("--- Test 2: Planted failure 1 (Content requirements defects) ---")
    bad_req = VALID_SAMPLE.replace(
        "| `SCREEN-01` | Workspace title and description | REQUIRED | User configuration | Identifies current draft collection |",
        "| `SCREEN-99` | | MANDATORY | User configuration | Invalid row |",
    )
    rc, out = run_validator(bad_req)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    expected_matches = [
        "screen 'SCREEN-99' is not in the frozen flow inventory",
        "'Content element' is empty or placeholder",
        "'Required or optional' is 'MANDATORY', expected REQUIRED or OPTIONAL",
    ]
    for em in expected_matches:
        if em not in out:
            print(f"FAIL: Missing expected error: {em}")
            all_ok = False
        else:
            print(f"OK: Caught: {em}")
    print()

    # 3. Planted failure 2: Message intent register defects
    print("--- Test 3: Planted failure 2 (Message intent register defects) ---")
    bad_msg = VALID_SAMPLE.replace(
        "| `MSG-01` | `SCREEN-01` | `STATE-EMPTY` | Empty collection retrieved | Guide user to initiate their first draft creation | Encouraging, straightforward | Must not imply that drafts were lost or deleted |",
        "| `MSG-…` | `SCREEN-01` | `STATE-…` | Empty collection retrieved | | | |",
    )
    rc, out = run_validator(bad_msg)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    expected_matches = [
        "placeholder or empty Message ID 'MSG-…'",
        "placeholder or empty State ID 'STATE-…'",
        "'Job of the message' is empty or placeholder",
        "'Tone constraint' is empty or placeholder",
        "'Must not imply' is empty or placeholder",
    ]
    for em in expected_matches:
        if em not in out:
            print(f"FAIL: Missing expected error: {em}")
            all_ok = False
        else:
            print(f"OK: Caught: {em}")
    print()

    # 4. Planted failure 3: Boundary violations
    print("--- Test 4: Planted failure 3 (Boundary violations) ---")
    bad_boundary = VALID_SAMPLE.replace(
        "Single-line editable field",
        "Single-line modal field with green border #00FF00 of 24px and token sys.color.primary",
    )
    rc, out = run_validator(bad_boundary)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    boundary_matches = [
        "matched component 'modal'",
        "matched color 'green'",
        "matched hex color '#00FF00'",
        "matched dimension '24px'",
        "matched token reference 'sys.color.primary'",
    ]
    for bm in boundary_matches:
        if bm not in out:
            print(f"FAIL: Missing expected boundary error: {bm}")
            all_ok = False
        else:
            print(f"OK: Caught: {bm}")
    print()

    # 5. Planted failure 4: Coverage check mismatches
    print("--- Test 5: Planted failure 4 (Coverage check mismatches) ---")
    bad_cov = VALID_SAMPLE.replace(
        "| `SCREEN-01` | 2 | 2 | 2 | Populated state uses self-evident list items |\n| `SCREEN-02` | 3 | 2 | 2 | Default and saved states use inline indicators |",
        "| `SCREEN-01` | 99 | 1 | 0 | Mismatch row |",
    )
    rc, out = run_validator(bad_cov)
    print(f"Exit code: {rc}")
    print(f"Output:\n{out.strip()}\n")
    if rc != 1:
        print("FAIL: Expected rc=1")
        all_ok = False
    cov_matches = [
        "SCREEN-01 claims 99 required content elements, expected 2",
        "SCREEN-01 claims 1 message intents defined, expected 2",
        "SCREEN-01 claims 0 states with a message, expected 2",
        "screen SCREEN-02 is missing from coverage check table",
    ]
    for cm in cov_matches:
        if cm not in out:
            print(f"FAIL: Missing expected coverage error: {cm}")
            all_ok = False
        else:
            print(f"OK: Caught: {cm}")
    print()

    # 6. CLI argument error
    print("--- Test 6: CLI missing arguments ---")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        capture_output=True,
        text=True,
    )
    print(f"Exit code: {proc.returncode}")
    if proc.returncode != 2:
        print("FAIL: Expected exit code 2 on missing args")
        all_ok = False
    else:
        print("OK: CLI argument check returned 2.\n")

    if all_ok:
        print("ALL TESTS PASSED: Two-sided verification complete.")
        return True
    else:
        print("SOME TESTS FAILED.")
        return False


if __name__ == "__main__":
    success = test_suite()
    sys.exit(0 if success else 1)
