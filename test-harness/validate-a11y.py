#!/usr/bin/env python3
"""Validate a Process 05 artifact 05 (Accessibility Requirements).

Checks the rules the template states and prose cannot enforce:
  1. Target conformance: standard is WCAG 2.2, level is valid WCAG level (A, AA, AAA),
     and non-empty Decision ID (DEC-...).
  2. Per-screen requirements: every screen in the frozen app-flow inventory has
     exactly one row. Keyboard reachable is REQUIRED or N/A. Focus order intent
     and Announcement intent are non-empty.
  3. Boundary checks: no UI component names (via validate-ux-model banned list),
     NO hex colors (#[0-9a-fA-F]{3,8}), NO token references, NO px/dp raw dimensions.
  4. Coverage check: table agrees with inventory count and row counts, confirms
     target level recorded with decision ID, and verifies 0 tokens/colors/dimensions.

Usage: python test-harness/validate-a11y.py <artifact-05> <app-flow>
Exit:  0 = PASS, 1 = FAIL, 2 = cannot evaluate
"""

import importlib.util
import pathlib
import re
import sys

# Reuse the audit helpers rather than copying them.
_spec = importlib.util.spec_from_file_location(
    "vum", pathlib.Path(__file__).resolve().parent / "validate-ux-model.py"
)
_vum = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vum)

INVENTORY_ROW = re.compile(r"^\|\s*`?(SCREEN-[A-Za-z0-9-]+)`?\s*\|", re.M)
SCREEN_ROW = re.compile(r"^\|\s*`?(SCREEN-[A-Za-z0-9-]+)`?\s*\|(.+)$", re.M)

HEX_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}(?![0-9a-fA-F_-])")
TOKEN_PATTERN = re.compile(
    r"\b(?:sys|ref|comp|md\.sys|md\.ref|md\.comp)\.[a-zA-Z0-9_.-]+"
    r"|\b(?:color|elevation|motion|space|type)\.[a-zA-Z0-9_.-]+"
    r"|\bvar\(--[a-zA-Z0-9_-]+\)"
    r"|\btoken\([^\)]+\)",
    re.IGNORECASE,
)
DIMENSION_PATTERN = re.compile(r"\b\d+(?:\.\d+)?\s*(?:px|dp|sp|pt)\b", re.IGNORECASE)

VALID_WCAG_LEVELS = {"A", "AA", "AAA"}


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def section(art: str, heading: str) -> str:
    """Return the body of one `## heading` section, and nothing after it."""
    m = re.search(rf"^##\s+{re.escape(heading)}.*$", art, re.M | re.IGNORECASE)
    if not m:
        return ""
    i = m.start()
    next_m = re.search(r"^##\s+", art[m.end() :], re.M)
    if not next_m:
        return art[i:]
    return art[i : m.end() + next_m.start()]


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2

    art_path, flow_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    for p in (art_path, flow_path):
        if not p.exists():
            print(f"FAIL  not found: {p}")
            return 2

    art = art_path.read_text(encoding="utf-8")
    flow = flow_path.read_text(encoding="utf-8")
    known_screens = {m.group(1) for m in INVENTORY_ROW.finditer(flow)}

    if not known_screens:
        print("FAIL  no screens found in frozen app-flow")
        return 2

    failures: list[str] = []

    # 1. Target conformance
    tc_text = section(art, "Target conformance")
    target_level = ""
    decision_id = ""
    if not tc_text:
        failures.append("missing 'Target conformance' section")
    else:
        tc_fields: dict[str, str] = {}
        for line in tc_text.splitlines():
            line = line.strip()
            if not line.startswith("|") or "---" in line or "| Field |" in line:
                continue
            c = cells(line)
            if len(c) >= 2:
                tc_fields[c[0].strip().lower()] = c[1].strip()

        # Check Standard
        standard = tc_fields.get("standard", "")
        if not standard:
            failures.append("Target conformance missing 'Standard'")
        elif standard.strip("`").strip().upper() != "WCAG 2.2":
            failures.append(f"Target conformance standard is {standard!r}, expected 'WCAG 2.2'")

        # Check Level
        level_raw = tc_fields.get("level", "")
        if not level_raw:
            failures.append("Target conformance missing 'Level'")
        else:
            level_clean = level_raw.strip("`").strip()
            m_level = re.match(r"^`?(A|AA|AAA)`?(?:\s|$)", level_clean, re.I)
            if not m_level or "record the actual decision" in level_clean.lower():
                failures.append(
                    f"Target conformance level is {level_raw!r}, expected 'A', 'AA', or 'AAA' without placeholder text"
                )
            else:
                target_level = m_level.group(1).upper()

        # Check Decision ID
        decision_raw = tc_fields.get("decision id", "")
        if not decision_raw:
            failures.append("Target conformance missing 'Decision ID'")
        else:
            dec_clean = decision_raw.strip("`").strip()
            m_dec = re.search(r"\bDEC-[A-Za-z0-9-]+\b", dec_clean)
            if not m_dec or "…" in dec_clean or "..." in dec_clean:
                failures.append(
                    f"Target conformance Decision ID is {decision_raw!r}, expected non-empty 'DEC-...'"
                )
            else:
                decision_id = m_dec.group(0)

    # 2. Per-screen requirements
    ps_text = section(art, "Per-screen requirements")
    screen_rows: dict[str, list[str]] = {}
    if not ps_text:
        failures.append("missing 'Per-screen requirements' section")
    else:
        if re.search(r"^\|\s*`?SCREEN-[….]+", ps_text, re.M):
            failures.append("Per-screen requirements contains unedited template placeholder row 'SCREEN-…'")

        for m in SCREEN_ROW.finditer(ps_text):
            sid = m.group(1)
            rest = m.group(2)
            if sid in screen_rows:
                failures.append(f"screen {sid} appears multiple times in per-screen requirements")
            row_cells = cells("|" + rest)
            screen_rows[sid] = row_cells

            kb = row_cells[0].strip("`").strip().upper() if len(row_cells) > 0 else ""
            if kb not in ("REQUIRED", "N/A"):
                failures.append(
                    f"{sid}: Keyboard reachable is {row_cells[0] if row_cells else ''!r}, expected REQUIRED or N/A"
                )

            focus_order = row_cells[1].strip() if len(row_cells) > 1 else ""
            if not focus_order or focus_order.lower() in (
                "ordered list of what receives focus, in sequence",
                "todo",
                "none",
                "-",
                "—",
            ):
                failures.append(f"{sid}: Focus order intent is empty")

            announcement = row_cells[2].strip() if len(row_cells) > 2 else ""
            if not announcement or announcement.lower() in (
                "what must be announced on state change, and when",
                "todo",
                "none",
                "-",
                "—",
            ):
                failures.append(f"{sid}: Announcement intent is empty")

        for sid in sorted(known_screens - set(screen_rows)):
            failures.append(f"screen {sid} exists in the frozen flow but has no requirements row")
        for sid in sorted(set(screen_rows) - known_screens):
            failures.append(f"screen {sid} has a requirements row but does not exist in the frozen flow")

    # 3. Boundary checks
    body = _vum.mask_workflow_tabs(_vum.strip_fences(_vum.strip_rule_block(art)))

    # Component names
    for term in _vum.BANNED:
        for hit in re.finditer(rf"\b{re.escape(term)}\b", body, re.IGNORECASE):
            line_no = body[: hit.start()].count("\n") + 1
            failures.append(
                f"boundary: line ~{line_no} matched banned component {term!r} — \"{_vum.sentence_at(body, hit.start())}\""
            )

    # Hex colors
    for hit in HEX_COLOR.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} hex color {hit.group(0)!r} — \"{_vum.sentence_at(body, hit.start())}\""
        )

    # Token references
    for hit in TOKEN_PATTERN.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} token reference {hit.group(0)!r} — \"{_vum.sentence_at(body, hit.start())}\""
        )

    # Raw dimensions
    for hit in DIMENSION_PATTERN.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} raw dimension {hit.group(0)!r} — \"{_vum.sentence_at(body, hit.start())}\""
        )

    # 4. Coverage check
    cc_text = section(art, "Coverage check")
    if not cc_text:
        failures.append("missing the Coverage check table")
    else:
        cc_rows: dict[str, str] = {}
        for line in cc_text.splitlines():
            line = line.strip()
            if not line.startswith("|") or "---" in line or "| Check |" in line:
                continue
            c = cells(line)
            if len(c) >= 2:
                cc_rows[c[0].strip().lower()] = c[1].strip()

        # Screens in source
        screens_in_source_val = None
        for k, v in cc_rows.items():
            if "screens in source" in k:
                screens_in_source_val = v
                break

        if screens_in_source_val is None:
            failures.append("Coverage check missing 'Screens in source'")
        else:
            m = re.search(r"\d+", screens_in_source_val)
            if not m:
                failures.append(
                    f"Coverage check 'Screens in source' is {screens_in_source_val!r}, expected integer {len(known_screens)}"
                )
            else:
                cnt = int(m.group(0))
                if cnt != len(known_screens):
                    failures.append(f"Coverage check 'Screens in source' is {cnt}, expected {len(known_screens)}")

        # Screens with a requirements row
        screens_with_reqs_val = None
        for k, v in cc_rows.items():
            if "screens with a requirements row" in k:
                screens_with_reqs_val = v
                break

        if screens_with_reqs_val is None:
            failures.append("Coverage check missing 'Screens with a requirements row'")
        else:
            m = re.search(r"\d+", screens_with_reqs_val)
            if not m:
                failures.append(
                    f"Coverage check 'Screens with a requirements row' is {screens_with_reqs_val!r}, expected integer {len(screen_rows)}"
                )
            else:
                cnt = int(m.group(0))
                if cnt != len(screen_rows):
                    failures.append(
                        f"Coverage check 'Screens with a requirements row' is {cnt}, expected {len(screen_rows)}"
                    )

        # Target level recorded with a decision ID
        target_level_dec_val = None
        for k, v in cc_rows.items():
            if "target level" in k:
                target_level_dec_val = v
                break

        if target_level_dec_val is None:
            failures.append("Coverage check missing 'Target level recorded with a decision ID'")
        else:
            ans = target_level_dec_val.strip("`").strip().lower()
            if ans != "yes":
                failures.append(
                    f"Coverage check 'Target level recorded with a decision ID' is {target_level_dec_val!r}, expected 'yes'"
                )

        # Any token, colour or size value present in this artifact
        any_token_val = None
        for k, v in cc_rows.items():
            if "any token" in k:
                any_token_val = v
                break

        if any_token_val is None:
            failures.append(
                "Coverage check missing 'Any token, colour or size value present in this artifact'"
            )
        else:
            ans = any_token_val.strip("`").strip()
            if ans not in ("0", "must be 0", "0 (none)"):
                failures.append(
                    f"Coverage check 'Any token, colour or size value present in this artifact' is {any_token_val!r}, expected '0'"
                )

    for f in failures:
        print(f"FAIL  {f}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    print(
        f"PASS  {len(screen_rows)} screen(s) covered, WCAG {target_level or 'conformance'} with {decision_id or 'decision'}, boundary clean"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
