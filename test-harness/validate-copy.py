#!/usr/bin/env python3
"""Validate a Process 05 artifact 04 (Content and Copy Intent).

Checks the rules the template states and prose cannot enforce:
  1. Content requirements by screen:
     - Screen ID in frozen flow inventory.
     - Non-empty Content element.
     - Required or optional must be 'REQUIRED' or 'OPTIONAL'.
     - Every screen in the frozen inventory has at least one content requirement.
  2. Message intent register:
     - Message ID matches MSG-<id> (rejects MSG-… placeholders).
     - Screen ID in frozen flow inventory.
     - Valid non-empty State ID (rejects STATE-… placeholders).
     - Non-empty Job of the message, Tone constraint, and Must not imply.
     - No duplicate Message IDs.
  3. Boundary audit:
     - No component names (via validate-ux-model banned list).
     - No visual/color values, hex colors, token references, or raw dimensions.
  4. Coverage check:
     - Table agrees with frozen flow inventory.
     - Counts of required content elements, message intents defined, and states
       with a message match actual data in earlier sections.

Usage: python test-harness/validate-copy.py <artifact-04> <app-flow>
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

INVENTORY_ROW = re.compile(r"^\|\s*`?(SCREEN-[A-Za-z0-9-]+)`?\s*\|", re.M)

HEX_COLOR = re.compile(r"(?:^|[\s,;:(])(#[0-9a-fA-F]{3,8})\b")
TOKEN_PATTERN = re.compile(
    r"\b(?:sys|ref|comp|md\.sys|md\.ref|md\.comp)\.[a-zA-Z0-9_.-]+"
    r"|\b(?:color|elevation|motion|space|type)\.[a-zA-Z0-9_.-]+"
    r"|\bvar\(--[a-zA-Z0-9_-]+\)"
    r"|\btoken\([^\)]+\)",
    re.IGNORECASE,
)
DIMENSION_PATTERN = re.compile(r"\b\d+(?:\.\d+)?\s*(?:px|dp|sp|pt|rem|em)\b", re.IGNORECASE)
COLOR_NAMES = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "gray", "grey", "cyan", "magenta", "amber",
]


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


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
        if first in ("screen id", "screen", "screen_id", "message id", "message_id", "content", "id"):
            continue
        rows.append(c)
    return rows


def audit_components(art: str) -> list[str]:
    """Audit lexical boundary: component names, visual/color values, tokens, dimensions."""
    failures: list[str] = []
    body = _vum.mask_workflow_tabs(_vum.strip_fences(_vum.strip_rule_block(art)))

    # 1. UI component names
    for term in _vum.BANNED:
        pattern = re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
        for hit in pattern.finditer(body):
            line_no = body[: hit.start()].count("\n") + 1
            failures.append(
                f"boundary: line ~{line_no} matched component {term!r} — \"{_vum.sentence_at(body, hit.start())}\""
            )

    # 2. Hex colors
    for hit in HEX_COLOR.finditer(body):
        term = hit.group(1)
        line_no = body[: hit.start(1)].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched hex color {term!r} — \"{_vum.sentence_at(body, hit.start(1))}\""
        )

    # 3. Named colors
    for color in COLOR_NAMES:
        pattern = re.compile(rf"\b{re.escape(color)}\b", re.IGNORECASE)
        for hit in pattern.finditer(body):
            line_no = body[: hit.start()].count("\n") + 1
            failures.append(
                f"boundary: line ~{line_no} matched color {color!r} — \"{_vum.sentence_at(body, hit.start())}\""
            )

    # 4. Token references
    for hit in TOKEN_PATTERN.finditer(body):
        term = hit.group(0)
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched token reference {term!r} — \"{_vum.sentence_at(body, hit.start())}\""
        )

    # 5. Raw dimensions
    for hit in DIMENSION_PATTERN.finditer(body):
        term = hit.group(0)
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched dimension {term!r} — \"{_vum.sentence_at(body, hit.start())}\""
        )

    return failures


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
    if not known_screens:
        print("FAIL  no screens found in frozen app-flow")
        return 2

    failures: list[str] = []

    # 1. Content requirements by screen
    req_sec = section(art, "Content requirements by screen")
    content_rows_per_screen: dict[str, list[tuple[str, str]]] = {s: [] for s in known_screens}
    if not req_sec:
        failures.append("missing 'Content requirements by screen' section")
    else:
        raw_req_rows = table_rows(req_sec)
        for idx, row in enumerate(raw_req_rows, start=1):
            if len(row) < 3:
                failures.append(f"content requirements row {idx}: too few columns ({len(row)}), expected at least 3")
                continue

            sid = row[0]
            element = row[1]
            req_or_opt = row[2].upper()

            if not sid or not re.fullmatch(r"SCREEN-[A-Za-z0-9-]+", sid):
                failures.append(f"content requirements row {idx}: invalid Screen ID {sid!r}")
            elif sid not in known_screens:
                failures.append(f"content requirements row {idx}: screen {sid!r} is not in the frozen flow inventory")
            else:
                content_rows_per_screen[sid].append((element, req_or_opt))

            if not element or element.lower() in ("none", "n/a", "-") or "…" in element or "..." in element:
                failures.append(f"content requirements row {idx} ({sid}): 'Content element' is empty or placeholder")

            if req_or_opt not in ("REQUIRED", "OPTIONAL"):
                failures.append(
                    f"content requirements row {idx} ({sid}): 'Required or optional' is {row[2]!r}, expected REQUIRED or OPTIONAL"
                )

        # Ensure all screens have at least one content requirement defined
        for sid, items in content_rows_per_screen.items():
            if not items:
                failures.append(f"content requirements: screen {sid} has no content requirements defined")

    # 2. Message intent register
    msg_sec = section(art, "Message intent register")
    messages_per_screen: dict[str, list[dict[str, str]]] = {s: [] for s in known_screens}
    seen_msg_ids: set[str] = set()

    if not msg_sec:
        failures.append("missing 'Message intent register' section")
    else:
        raw_msg_rows = table_rows(msg_sec)
        for idx, row in enumerate(raw_msg_rows, start=1):
            if len(row) < 7:
                failures.append(f"message register row {idx}: too few columns ({len(row)}), expected 7")
                continue

            mid = row[0]
            sid = row[1]
            state_id = row[2]
            trigger = row[3]
            job = row[4]
            tone = row[5]
            must_not_imply = row[6]

            # Validate Message ID
            if not mid or mid in ("MSG-…", "MSG-...") or "…" in mid or "..." in mid:
                failures.append(f"message register row {idx}: placeholder or empty Message ID {mid!r}")
            elif not re.fullmatch(r"MSG-[A-Za-z0-9_-]+", mid, re.IGNORECASE):
                failures.append(f"message register row {idx}: invalid Message ID {mid!r} (must match MSG-<name>)")
            elif mid in seen_msg_ids:
                failures.append(f"message register row {idx}: duplicate Message ID {mid!r}")
            seen_msg_ids.add(mid)

            # Validate Screen ID
            if not sid or not re.fullmatch(r"SCREEN-[A-Za-z0-9-]+", sid):
                failures.append(f"message register row {idx}: invalid Screen ID {sid!r}")
            elif sid not in known_screens:
                failures.append(f"message register row {idx}: screen {sid!r} is not in the frozen flow inventory")
            else:
                messages_per_screen[sid].append({
                    "mid": mid, "state_id": state_id, "trigger": trigger,
                    "job": job, "tone": tone, "must_not_imply": must_not_imply,
                })

            # Validate State ID
            if not state_id or state_id in ("STATE-…", "STATE-...") or "…" in state_id or "..." in state_id:
                failures.append(f"message register row {idx} ({mid}): placeholder or empty State ID {state_id!r}")
            elif not re.fullmatch(r"STATE-[A-Za-z0-9_-]+", state_id, re.IGNORECASE):
                failures.append(f"message register row {idx} ({mid}): invalid State ID {state_id!r} (must match STATE-<name>)")

            # Validate required prose intents
            if not job or job.lower() in ("none", "n/a", "-") or "…" in job or "..." in job:
                failures.append(f"message register row {idx} ({mid}): 'Job of the message' is empty or placeholder")
            if not tone or tone.lower() in ("none", "n/a", "-") or "…" in tone or "..." in tone:
                failures.append(f"message register row {idx} ({mid}): 'Tone constraint' is empty or placeholder")
            if not must_not_imply or must_not_imply.lower() in ("none", "n/a", "-") or "…" in must_not_imply or "..." in must_not_imply:
                failures.append(f"message register row {idx} ({mid}): 'Must not imply' is empty or placeholder")

    # 3. Lexical boundary audit
    failures.extend(audit_components(art))

    # 4. Coverage check
    cov_sec = section(art, "Coverage check")
    if not cov_sec:
        failures.append("missing 'Coverage check' section")
    else:
        cov_rows = table_rows(cov_sec)
        screens_in_cov: set[str] = set()

        for idx, row in enumerate(cov_rows, start=1):
            if len(row) < 4:
                failures.append(f"coverage check row {idx}: too few columns ({len(row)}), expected at least 4")
                continue

            csid = row[0]
            screens_in_cov.add(csid)

            if csid not in known_screens:
                failures.append(f"coverage check: screen {csid!r} is not in the frozen flow inventory")
                continue

            # Check required content elements count
            try:
                stated_req = int(row[1])
            except ValueError:
                stated_req = -1
            actual_req = sum(1 for (el, opt) in content_rows_per_screen.get(csid, []) if opt == "REQUIRED")
            if stated_req != actual_req:
                failures.append(
                    f"coverage check: {csid} claims {stated_req} required content elements, expected {actual_req}"
                )

            # Check message intents defined count
            try:
                stated_intents = int(row[2])
            except ValueError:
                stated_intents = -1
            actual_intents = len(messages_per_screen.get(csid, []))
            if stated_intents != actual_intents:
                failures.append(
                    f"coverage check: {csid} claims {stated_intents} message intents defined, expected {actual_intents}"
                )

            # Check states with a message count
            try:
                stated_states = int(row[3])
            except ValueError:
                stated_states = -1
            actual_states = len({m["state_id"] for m in messages_per_screen.get(csid, [])})
            if stated_states != actual_states:
                failures.append(
                    f"coverage check: {csid} claims {stated_states} states with a message, expected {actual_states}"
                )

        for s in sorted(known_screens - screens_in_cov):
            failures.append(f"coverage check: screen {s} is missing from coverage check table")

    for f in failures:
        print(f"FAIL  {f}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    total_req_elements = sum(
        sum(1 for (_, opt) in items if opt == "REQUIRED")
        for items in content_rows_per_screen.values()
    )
    total_messages = sum(len(m) for m in messages_per_screen.values())
    print(
        f"PASS  {len(known_screens)} screens covered, {total_req_elements} required content elements, "
        f"{total_messages} message intents defined, boundary clean"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
