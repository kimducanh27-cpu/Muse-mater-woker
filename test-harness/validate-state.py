#!/usr/bin/env python3
"""Validate a Process 05 artifact 03 (State Experience).

Checks the rules the template states and prose cannot enforce:
  1. Every row in the Matrix has a valid Screen ID (from the frozen app-flow
     inventory), a valid State ID, and Source in (P04-MATRIX, P04-TRANSITION,
     P04-EXPLICIT-EXCLUSION).
  2. Every row states what the user sees, understands and can do.
  3. Every non-recoverable state in the explicit register has an approved
     Decision ID matching DEC-.
  4. The boundary holds: no component names, no visual/color values, no raw dimensions
     (via validate-ux-model audit_boundary).
  5. The Coverage check table and totals match actual rows and the Process 04
     matrix count, and state sets match P04 exactly (no unauthorized states).

Usage: python test-harness/validate-state.py <artifact-03> <app-flow>
Exit:  0 = PASS, 1 = FAIL, 2 = cannot evaluate
"""

import importlib.util
import pathlib
import re
import sys

# Reuse the audit helpers from validate-ux-model.py
_spec = importlib.util.spec_from_file_location(
    "vum", pathlib.Path(__file__).resolve().parent / "validate-ux-model.py"
)
_vum = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vum)

ALLOWED_SOURCES = {"P04-MATRIX", "P04-TRANSITION", "P04-EXPLICIT-EXCLUSION"}


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def normalize_state_name(s: str) -> str:
    s = s.strip().upper()
    if s.startswith("STATE-"):
        s = s[6:]
    return s


def section(art: str, heading: str) -> str:
    """Return the body of one `## heading` section, and nothing after it."""
    m = re.search(rf"^##\s+{re.escape(heading)}[^\n]*$", art, re.M | re.IGNORECASE)
    if not m:
        return ""
    start = m.start()
    m2 = re.search(r"\n##\s+", art[m.end():])
    return art[start : m.end() + m2.start()] if m2 else art[start:]


def table_rows(sec_text: str) -> list[list[str]]:
    """Extract table rows, ignoring header and separator rows."""
    rows = []
    for line in sec_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        c = [cell.strip().strip("`") for cell in cells(line)]
        if not c or not c[0]:
            continue
        if c[0].startswith("-"):
            continue
        first = c[0].lower()
        if first in ("screen id", "screen", "screen_id", "id", "projection source"):
            continue
        rows.append(c)
    return rows


def parse_p04_state_matrix(flow: str) -> dict[str, list[str]]:
    """Parse screen -> list of applicable states from Process 04 app flow."""
    sec = section(flow, "State matrix") or section(flow, "State and exception matrix")
    if not sec:
        return {}
    result: dict[str, list[str]] = {}
    for line in sec.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        c = [cell.strip().strip("`") for cell in cells(line)]
        if not c or not c[0]:
            continue
        if c[0].startswith("-") or c[0].lower() in ("id", "screen id", "screen/flow/node"):
            continue

        # Format A: col 0 is SCREEN ID, col 1 is comma-separated states
        if re.match(r"^SCREEN-[A-Za-z0-9-]+$", c[0]):
            sid = c[0]
            states = [s.strip() for s in c[1].split(",") if s.strip()] if len(c) > 1 else []
            result.setdefault(sid, []).extend(states)
        # Format B: col 1 is SCREEN ID, col 0 or 2 is state
        elif len(c) > 1 and re.match(r"^SCREEN-[A-Za-z0-9-]+$", c[1]):
            sid = c[1]
            state = c[0] if c[0] else (c[2] if len(c) > 2 else "")
            if state:
                result.setdefault(sid, []).append(state)
    return result


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

    known_screens = _vum.get_flow_screens(flow)
    p04_states = parse_p04_state_matrix(flow)
    p04_matrix_count = sum(len(v) for v in p04_states.values())

    failures: list[str] = []

    # 1. Parse and validate Matrix section
    matrix_sec = section(art, "Matrix")
    if not matrix_sec:
        failures.append("missing the Matrix section")
        matrix_rows = []
    else:
        raw_rows = table_rows(matrix_sec)
        matrix_rows = []
        seen_pairs: set[tuple[str, str]] = set()

        for idx, row in enumerate(raw_rows, start=1):
            if len(row) < 3:
                failures.append(f"matrix row {idx}: too few columns ({len(row)}), expected at least 7")
                continue

            sid = row[0]
            state_id = row[1]
            source = row[2]
            sees = row[3] if len(row) > 3 else ""
            understands = row[4] if len(row) > 4 else ""
            can_do = row[5] if len(row) > 5 else ""

            # Validate Screen ID
            if not sid or not re.fullmatch(r"SCREEN-[A-Za-z0-9-]+", sid):
                failures.append(f"matrix row {idx}: invalid Screen ID {sid!r}")
            elif sid not in known_screens:
                failures.append(f"matrix row {idx}: screen {sid!r} is not in the frozen flow inventory")

            # Validate State ID
            if not state_id or state_id in ("STATE-…", "STATE-...") or "…" in state_id or "..." in state_id:
                failures.append(f"matrix row {idx}: placeholder or empty State ID {state_id!r}")
            elif not re.fullmatch(r"STATE-[A-Za-z0-9_-]+", state_id, re.IGNORECASE):
                failures.append(f"matrix row {idx}: invalid State ID {state_id!r} (must match STATE-<name>)")

            # Validate Source
            if source not in ALLOWED_SOURCES:
                failures.append(
                    f"matrix row {idx} ({sid}/{state_id}): invalid source {source!r}, expected one of {', '.join(sorted(ALLOWED_SOURCES))}"
                )

            # Validate Triad (sees, understands, can do)
            if not sees or sees.lower() in ("none", "n/a", "-"):
                failures.append(f"matrix row {idx} ({sid}/{state_id}): 'User sees' is empty")
            if not understands or understands.lower() in ("none", "n/a", "-"):
                failures.append(f"matrix row {idx} ({sid}/{state_id}): 'User understands' is empty")
            if not can_do or can_do.lower() in ("none", "n/a", "-"):
                failures.append(f"matrix row {idx} ({sid}/{state_id}): 'User can do' is empty")

            # Duplicate check
            pair = (sid, state_id)
            if pair in seen_pairs:
                failures.append(f"matrix row {idx}: duplicate entry for screen {sid} state {state_id}")
            seen_pairs.add(pair)

            matrix_rows.append((sid, state_id))

    # 1b. Check exact state set per screen against Process 04
    rows_not_in_p04 = 0
    for sid in sorted(known_screens):
        p04_set = {normalize_state_name(s) for s in p04_states.get(sid, [])}
        actual_set = {normalize_state_name(state_id) for (s, state_id) in matrix_rows if s == sid}

        missing = p04_set - actual_set
        extra = actual_set - p04_set

        for st in sorted(missing):
            failures.append(f"{sid}: state {st!r} from Process 04 is missing in Matrix")
        for st in sorted(extra):
            rows_not_in_p04 += 1
            failures.append(f"{sid}: state {st!r} in Matrix is not defined in Process 04 (unauthorized state)")

    for (sid, state_id) in matrix_rows:
        if sid not in known_screens:
            rows_not_in_p04 += 1

    # 2. Parse and validate Non-recoverable states register
    non_rec_sec = section(art, "Non-recoverable states")
    non_rec_dec_count = 0
    if non_rec_sec:
        raw_non_rec = table_rows(non_rec_sec)
        for idx, row in enumerate(raw_non_rec, start=1):
            if not row or row[0].lower() in ("none", "n/a", "no non-recoverable states", "-"):
                continue

            sid = row[0]
            state_id = row[1] if len(row) > 1 else ""
            dec_id = row[3] if len(row) > 3 else ""

            if sid and sid not in known_screens:
                failures.append(f"non-recoverable register: screen {sid!r} is not in the frozen flow inventory")
            if not state_id or not re.fullmatch(r"STATE-[A-Za-z0-9_-]+", state_id, re.IGNORECASE):
                failures.append(f"non-recoverable register: invalid State ID {state_id!r}")

            if not dec_id or not re.search(r"\bDEC-[A-Za-z0-9-]+\b", dec_id) or "…" in dec_id or "..." in dec_id:
                failures.append(f"non-recoverable state {sid}/{state_id}: missing or invalid Decision ID ({dec_id!r})")
            else:
                non_rec_dec_count += 1

    # 3. Lexical boundary audit
    failures.extend(_vum.audit_boundary(art))

    # 4. Coverage check
    cov_sec = section(art, "Coverage check")
    if not cov_sec:
        failures.append("missing the coverage check table")
    else:
        cov_rows = table_rows(cov_sec)
        screens_in_cov: set[str] = set()

        for row in cov_rows:
            if not row:
                continue
            csid = row[0]
            screens_in_cov.add(csid)

            if csid not in known_screens:
                failures.append(f"coverage check: screen {csid!r} is not in the frozen flow inventory")
                continue

            # Check states applicable in P04
            try:
                stated_p04 = int(row[1]) if len(row) > 1 else -1
            except ValueError:
                stated_p04 = -1
            expected_p04 = len(p04_states.get(csid, []))
            if stated_p04 != expected_p04:
                failures.append(f"coverage check: {csid} claims {stated_p04} states in P04, expected {expected_p04}")

            # Check rows present
            try:
                stated_rows = int(row[2]) if len(row) > 2 else -1
            except ValueError:
                stated_rows = -1
            actual_rows_for_csid = sum(1 for (sid, _) in matrix_rows if sid == csid)
            if stated_rows != actual_rows_for_csid:
                failures.append(f"coverage check: {csid} claims {stated_rows} rows present, expected {actual_rows_for_csid}")

        for s in sorted(known_screens - screens_in_cov):
            failures.append(f"coverage check: screen {s} is missing from coverage check table")

        # Totals check
        m_app = re.search(r"Applicable screen-state pairs:\s*`?(\d+)`?", cov_sec)
        m_rows = re.search(r"Rows present:\s*`?(\d+)`?", cov_sec)
        m_nonrec = re.search(r"Non-recoverable states with a decision:\s*`?(\d+)`?", cov_sec)
        m_notp04 = re.search(r"Rows for states not in Process 04:\s*`?(\d+)`?", cov_sec)

        if not m_app or not m_rows:
            failures.append("coverage check: missing or incomplete Totals line")
        else:
            totals_app = int(m_app.group(1))
            totals_rows = int(m_rows.group(1))
            totals_nonrec = int(m_nonrec.group(1)) if m_nonrec else 0
            totals_notp04 = int(m_notp04.group(1)) if m_notp04 else 0

            actual_matrix_count = len(matrix_rows)

            if totals_app != p04_matrix_count:
                failures.append(
                    f"coverage check totals: 'Applicable screen-state pairs' is {totals_app}, "
                    f"expected {p04_matrix_count} from Process 04"
                )
            if totals_rows != actual_matrix_count:
                failures.append(
                    f"coverage check totals: 'Rows present' is {totals_rows}, "
                    f"expected {actual_matrix_count} (actual rows in Matrix)"
                )
            if totals_nonrec != non_rec_dec_count:
                failures.append(
                    f"coverage check totals: 'Non-recoverable states with a decision' is {totals_nonrec}, "
                    f"expected {non_rec_dec_count}"
                )
            if totals_notp04 != 0:
                failures.append(
                    f"coverage check totals: 'Rows for states not in Process 04' is {totals_notp04}, "
                    f"expected 0 (blocks Gate 2)"
                )
            if totals_notp04 != rows_not_in_p04:
                failures.append(
                    f"coverage check totals: 'Rows for states not in Process 04' is {totals_notp04}, "
                    f"calculated {rows_not_in_p04}"
                )
            if rows_not_in_p04 != 0:
                failures.append(
                    f"Matrix contains {rows_not_in_p04} unauthorized state(s) not in Process 04 (any non-zero value blocks Gate 2)"
                )

    for f in failures:
        print(f"FAIL  {f}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    screens_with_rows = {sid for (sid, _) in matrix_rows}
    print(
        f"PASS  {len(matrix_rows)} matrix rows across {len(screens_with_rows)} screens, "
        f"P04 coverage verified ({p04_matrix_count} states), boundary clean"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
