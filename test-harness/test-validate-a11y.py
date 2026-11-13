#!/usr/bin/env python3
"""Two-sided test suite for test-harness/validate-a11y.py.

Verifies:
  1. Valid sample returns PASS (exit code 0).
  2. Planted failure type 1 (Target Conformance defects) returns FAIL (exit code 1) with exact error messages.
  3. Planted failure type 2 (Per-screen requirements defects) returns FAIL (exit code 1) with exact error messages.
  4. Planted failure type 3 (Boundary violations) returns FAIL (exit code 1) with exact error messages.
  5. Planted failure type 4 (Coverage check table mismatches) returns FAIL (exit code 1) with exact error messages.
  6. CLI errors (missing files / missing args) return exit code 2.
"""

import pathlib
import subprocess
import sys
import tempfile

VALID_FLOW = """# App Flow — probe fixture

> SIMULATED — NOT ELIGIBLE DOWNSTREAM

## Screen inventory

| SCREEN ID | Name | Serves |
|---|---|---|
| `SCREEN-01` | Draft list | `CAP-01` |
| `SCREEN-02` | Draft editor | `CAP-01` |
"""

VALID_A11Y = """# 05 — Accessibility Requirements

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> Requirements only. Process 06 supplies the tokens and components that satisfy them; Process 08 measures conformance. This artifact must not choose a colour, size or token.

## Target conformance

| Field | Value |
|---|---|
| Standard | WCAG 2.2 |
| Level | AA |
| Decision ID | DEC-05 |
| Scope | All screens in the frozen Process 04 inventory |
| Out of scope | Stated explicitly, with rationale |

The target level is a decision, not a default. It is recorded here and in the Decision Log because it changes the audit checklist and the number of findings in Process 08.

## Per-screen requirements

| Screen ID | Keyboard reachable | Focus order intent | Announcement intent | Minimum target size | Motion constraint | Notes |
|---|---|---|---|---|---|---|
| `SCREEN-01` | REQUIRED | Primary action, then items in reverse order | Status change announced when list reloads | Must meet touch target requirements | Respect reduced motion preference | None |
| `SCREEN-02` | REQUIRED | Title, then content area, then primary action | Save confirmation announced immediately | Must meet touch target requirements | None | None |

**Focus order intent** is a sequence of *things*, not elements: "primary action, then the list, then the escape hatch". Process 06 and 07 translate it into real focus targets.

**Announcement intent** states what must be conveyed non-visually when a state changes — for example "the user must be told that the save failed and that their draft is intact". It does not name an ARIA attribute.

## Requirements that apply to every screen

| Requirement | Statement | Verified by |
|---|---|---|
| Text alternatives | Every non-text element that carries meaning has a stated alternative intent | Process 07 composition |
| Colour independence | No state may be conveyed by colour alone | Process 06 tokens + Process 08 audit |
| Focus visibility | Every focusable element must be visibly distinguishable | Process 06 + Process 08 |
| Timing | No interaction may require a response faster than the user can read the message | Process 05 review |
| Error identification | Every error names what failed and what to do | Artifact 04 message intent |

## Known constraints inherited from upstream

| Constraint | Source | Consequence |
|---|---|---|
| None | Product Definition constraint | None |

## Coverage check — required at the end of the artifact

| Check | Result |
|---|---|
| Screens in source | 2 |
| Screens with a requirements row | 2 |
| Target level recorded with a decision ID | yes |
| Any token, colour or size value present in this artifact | 0 |
"""


def run_validator(art_path: pathlib.Path, flow_path: pathlib.Path) -> subprocess.CompletedProcess:
    validator = pathlib.Path(__file__).resolve().parent / "validate-a11y.py"
    return subprocess.run(
        [sys.executable, str(validator), str(art_path), str(flow_path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_suite() -> int:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = pathlib.Path(tmpdir)
        flow_path = root / "APP_FLOW.md"
        flow_path.write_text(VALID_FLOW, encoding="utf-8")

        test_count = 0
        pass_count = 0

        # --- Test 1: Valid sample PASS ---
        test_count += 1
        valid_art = root / "VALID_05.md"
        valid_art.write_text(VALID_A11Y, encoding="utf-8")
        res = run_validator(valid_art, flow_path)
        print("=== TEST 1: Valid Sample ===")
        print(f"Exit code: {res.returncode}")
        print(f"Output:\n{res.stdout}")
        assert res.returncode == 0, f"Expected 0, got {res.returncode}"
        assert "PASS" in res.stdout
        assert "2 screen(s) covered" in res.stdout
        pass_count += 1

        # --- Test 2: Planted Failure Type 1: Target Conformance defects ---
        test_count += 1
        tc_fail_text = VALID_A11Y.replace(
            "| Standard | WCAG 2.2 |", "| Standard | WCAG 2.1 |"
        ).replace(
            "| Level | AA |", "| Level | `AA` (record the actual decision; do not assume) |"
        ).replace(
            "| Decision ID | DEC-05 |", "| Decision ID | `DEC-…` |"
        )
        tc_art = root / "FAIL_TC_05.md"
        tc_art.write_text(tc_fail_text, encoding="utf-8")
        res = run_validator(tc_art, flow_path)
        print("=== TEST 2: Planted Failure Type 1 (Target Conformance) ===")
        print(f"Exit code: {res.returncode}")
        print(f"Output:\n{res.stdout}")
        assert res.returncode == 1, f"Expected 1, got {res.returncode}"
        assert "FAIL  Target conformance standard is 'WCAG 2.1', expected 'WCAG 2.2'" in res.stdout
        assert "FAIL  Target conformance level is '`AA` (record the actual decision; do not assume)', expected 'A', 'AA', or 'AAA' without placeholder text" in res.stdout
        assert "FAIL  Target conformance Decision ID is '`DEC-…`', expected non-empty 'DEC-...'" in res.stdout
        pass_count += 1

        # --- Test 3: Planted Failure Type 2: Per-screen requirements defects ---
        test_count += 1
        ps_fail_text = VALID_A11Y.replace(
            "| `SCREEN-01` | REQUIRED | Primary action, then items in reverse order | Status change announced when list reloads | Must meet touch target requirements | Respect reduced motion preference | None |",
            "| `SCREEN-01` | OPTIONAL |  |  | Must meet touch target requirements | Respect reduced motion preference | None |",
        ).replace(
            "| `SCREEN-02` | REQUIRED | Title, then content area, then primary action | Save confirmation announced immediately | Must meet touch target requirements | None | None |",
            "| `SCREEN-99` | REQUIRED | Some focus | Some announcement | Must meet touch target requirements | None | None |",
        )
        ps_art = root / "FAIL_PS_05.md"
        ps_art.write_text(ps_fail_text, encoding="utf-8")
        res = run_validator(ps_art, flow_path)
        print("=== TEST 3: Planted Failure Type 2 (Per-screen requirements) ===")
        print(f"Exit code: {res.returncode}")
        print(f"Output:\n{res.stdout}")
        assert res.returncode == 1, f"Expected 1, got {res.returncode}"
        assert "FAIL  SCREEN-01: Keyboard reachable is 'OPTIONAL', expected REQUIRED or N/A" in res.stdout
        assert "FAIL  SCREEN-01: Focus order intent is empty" in res.stdout
        assert "FAIL  SCREEN-01: Announcement intent is empty" in res.stdout
        assert "FAIL  screen SCREEN-02 exists in the frozen flow but has no requirements row" in res.stdout
        assert "FAIL  screen SCREEN-99 has a requirements row but does not exist in the frozen flow" in res.stdout
        pass_count += 1

        # --- Test 4: Planted Failure Type 3: Boundary violations ---
        test_count += 1
        bound_fail_text = VALID_A11Y.replace(
            "Primary action, then items in reverse order",
            "Click button to open dialog",
        ).replace(
            "Save confirmation announced immediately",
            "Color set to #FFFFFF with token sys.color.action.primary and size 48dp",
        )
        bound_art = root / "FAIL_BOUND_05.md"
        bound_art.write_text(bound_fail_text, encoding="utf-8")
        res = run_validator(bound_art, flow_path)
        print("=== TEST 4: Planted Failure Type 3 (Boundary violations) ===")
        print(f"Exit code: {res.returncode}")
        print(f"Output:\n{res.stdout}")
        assert res.returncode == 1, f"Expected 1, got {res.returncode}"
        assert "matched banned component 'button'" in res.stdout
        assert "matched banned component 'dialog'" in res.stdout
        assert "hex color '#FFFFFF'" in res.stdout
        assert "token reference 'sys.color.action.primary'" in res.stdout
        assert "raw dimension '48dp'" in res.stdout
        pass_count += 1

        # --- Test 5: Planted Failure Type 4: Coverage check mismatches ---
        test_count += 1
        cc_fail_text = VALID_A11Y.replace(
            "| Screens in source | 2 |", "| Screens in source | 99 |"
        ).replace(
            "| Screens with a requirements row | 2 |", "| Screens with a requirements row | 0 |"
        ).replace(
            "| Target level recorded with a decision ID | yes |", "| Target level recorded with a decision ID | no |"
        ).replace(
            "| Any token, colour or size value present in this artifact | 0 |", "| Any token, colour or size value present in this artifact | 3 |"
        )
        cc_art = root / "FAIL_CC_05.md"
        cc_art.write_text(cc_fail_text, encoding="utf-8")
        res = run_validator(cc_art, flow_path)
        print("=== TEST 5: Planted Failure Type 4 (Coverage check table mismatches) ===")
        print(f"Exit code: {res.returncode}")
        print(f"Output:\n{res.stdout}")
        assert res.returncode == 1, f"Expected 1, got {res.returncode}"
        assert "FAIL  Coverage check 'Screens in source' is 99, expected 2" in res.stdout
        assert "FAIL  Coverage check 'Screens with a requirements row' is 0, expected 2" in res.stdout
        assert "FAIL  Coverage check 'Target level recorded with a decision ID' is 'no', expected 'yes'" in res.stdout
        assert "FAIL  Coverage check 'Any token, colour or size value present in this artifact' is '3', expected '0'" in res.stdout
        pass_count += 1

        # --- Test 6: CLI error handling (exit code 2) ---
        test_count += 1
        res = subprocess.run(
            [sys.executable, str(pathlib.Path(__file__).resolve().parent / "validate-a11y.py")],
            capture_output=True,
            text=True,
        )
        assert res.returncode == 2, f"Expected 2, got {res.returncode}"
        pass_count += 1

        print(f"\nALL {pass_count}/{test_count} TESTS PASSED.")
        return 0


if __name__ == "__main__":
    sys.exit(test_suite())
