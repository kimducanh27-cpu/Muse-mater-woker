#!/usr/bin/env python3
"""Validate a Process 05 artifact 01 (Screen UX Model) against the frozen flow.

Checks four things the Skill requires and prose cannot enforce:
  1. Screen set: every SCREEN ID in the frozen flow has exactly one entry, and
     no entry names a screen that does not exist.
  2. One primary action per screen, non-empty.
  3. The boundary audit: component names, visual values (hex colors, color names,
     token refs, raw dimensions), run as a procedure: word boundaries, body only,
     excluding the rule block and fenced blocks.
  4. Required sections per screen, structural block width <= 100, and coverage table.

Usage: python test-harness/validate-ux-model.py <artifact-01> <app-flow>
Exit:  0 = PASS, 1 = FAIL, 2 = cannot evaluate
"""

import pathlib
import re
import sys

BANNED_COMPONENTS = [
    "button", "card", "modal", "dialog", "toast", "chip", "tab", "drawer",
    "tooltip", "badge", "banner", "accordion",
    "app bar", "top bar", "bottom sheet", "navigation rail",
    "floating action button", "fab", "snackbar", "system back",
    "predictive back", "window size class", "inset",
]
BANNED = BANNED_COMPONENTS  # backward compatibility for imports

BANNED_COLORS = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "white", "black", "gray", "grey", "teal", "indigo", "violet",
    "amber", "emerald", "lime", "rose",
]

HEX_COLOR_PATTERN = re.compile(r"(?<![#&0-9a-zA-Z])#[0-9a-fA-F]{3,8}(?![0-9a-fA-F_-])")
COLOR_NAME_PATTERN = re.compile(rf"\b(?:{'|'.join(BANNED_COLORS)})\b", re.IGNORECASE)
TOKEN_REF_PATTERN = re.compile(r"\b(?:sys|ref|comp|color)\.[a-zA-Z0-9_.-]+", re.IGNORECASE)
DIMENSION_PATTERN = re.compile(r"\b\d+(?:\.\d+)?\s*(?:px|dp|sp|pt|rem|em)\b", re.IGNORECASE)

REQUIRED_PER_SCREEN = ["Information hierarchy", "Structural block", "Open questions"]
SCREEN_HEADING = re.compile(r"^##\s+(SCREEN-[A-Za-z0-9-]+)\s*—", re.M)
INVENTORY_ROW = re.compile(r"^\|\s*`?(SCREEN-[A-Za-z0-9-]+)`?\s*\|", re.M)


def strip_rule_block(text: str) -> str:
    """Drop the 'Rules for this artifact' section: it quotes the rule it bans."""
    out, skipping = [], False
    for line in text.splitlines(keepends=True):
        if line.startswith("## "):
            skipping = "Rules for this artifact" in line
            out.append(line)
            continue
        if not skipping:
            out.append(line)
    return "".join(out)


def strip_fences(text: str) -> str:
    """Drop fenced blocks: a structural diagram is not prose."""
    out, inside = [], False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            inside = not inside
            out.append("\n")
            continue
        if not inside:
            out.append(line)
    return "".join(out)


def mask_workflow_tabs(text: str) -> str:
    """Blank out `Tab 01` / `TAB_01`: the workflow's own vocabulary, not a UI tab.

    Same length, so offsets and line numbers survive. Without this every
    artifact fails on its own header line, which is how an audit loses
    credibility on first contact.
    """
    for pattern in (r"\bTab\s+\d+\b", r"\bTAB_\d+\b"):
        text = re.sub(pattern, lambda m: " " * len(m.group(0)), text)
    return text


def sentence_at(text: str, offset: int) -> str:
    start = max(text.rfind(". ", 0, offset), text.rfind("\n", 0, offset)) + 1
    end = text.find(". ", offset)
    end = len(text) if end < 0 else end + 1
    return " ".join(text[start:end].split())[:160]


def get_flow_screens(flow: str) -> set[str]:
    m = re.search(r"^##\s+(?:Functional\s+)?screen\s+inventory", flow, re.M | re.I)
    if not m:
        return set()
    start = m.end()
    m2 = re.search(r"^##\s+", flow[start:], re.M)
    sec_text = flow[start : start + m2.start()] if m2 else flow[start:]
    return {match.group(1) for match in INVENTORY_ROW.finditer(sec_text)}


def audit_boundary(art: str) -> list[str]:
    """Audit lexical and visual boundary: component names, hex colors, color names,
    token refs, raw dimensions."""
    failures: list[str] = []
    body = mask_workflow_tabs(strip_fences(strip_rule_block(art)))

    # 1. UI components
    for term in BANNED_COMPONENTS:
        pattern = re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
        for hit in pattern.finditer(body):
            line_no = body[: hit.start()].count("\n") + 1
            failures.append(
                f"boundary: line ~{line_no} matched component {term!r} — \"{sentence_at(body, hit.start())}\""
            )

    # 2. Hex colors
    for hit in HEX_COLOR_PATTERN.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched hex color {hit.group(0)!r} — \"{sentence_at(body, hit.start())}\""
        )

    # 3. Color names
    for hit in COLOR_NAME_PATTERN.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched color {hit.group(0)!r} — \"{sentence_at(body, hit.start())}\""
        )

    # 4. Token refs
    for hit in TOKEN_REF_PATTERN.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched token ref {hit.group(0)!r} — \"{sentence_at(body, hit.start())}\""
        )

    # 5. Raw dimensions
    for hit in DIMENSION_PATTERN.finditer(body):
        line_no = body[: hit.start()].count("\n") + 1
        failures.append(
            f"boundary: line ~{line_no} matched dimension {hit.group(0)!r} — \"{sentence_at(body, hit.start())}\""
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

    failures: list[str] = []

    # 1. screen set
    in_flow = get_flow_screens(flow)
    if not in_flow:
        failures.append("frozen flow contains no screen inventory section or no screens")

    in_art = [m.group(1) for m in SCREEN_HEADING.finditer(art)]
    seen = set(in_art)

    for sid in sorted(in_flow - seen):
        failures.append(f"screen {sid} exists in the frozen flow but has no entry")
    for sid in sorted(seen - in_flow):
        failures.append(f"entry {sid} does not exist in the frozen flow")
    for sid in sorted({s for s in in_art if in_art.count(s) > 1}):
        failures.append(f"screen {sid} has {in_art.count(sid)} entries, expected 1")

    # 2. per-screen validation
    entries = list(SCREEN_HEADING.finditer(art))
    for i, m in enumerate(entries):
        sid = m.group(1)
        next_h2 = re.search(r"^##\s+", art[m.end():], re.M)
        end = m.end() + next_h2.start() if next_h2 else len(art)
        chunk = art[m.start():end]

        # Primary action
        actions = re.findall(r"^\|\s*Primary action\s*\|\s*(.+?)\s*\|", chunk, re.M)
        if len(actions) != 1:
            failures.append(f"{sid}: {len(actions)} primary-action rows, expected 1")
        elif actions[0].strip().lower() in {"", "none", "not applicable", "n/a"}:
            failures.append(f"{sid}: primary action is empty")

        # Required subsections per screen
        for sec in REQUIRED_PER_SCREEN:
            if not re.search(rf"^###\s+{re.escape(sec)}", chunk, re.M | re.I):
                failures.append(f"{sid}: missing required section '### {sec}'")

        # Structural block max line length <= 100
        struct_match = re.search(r"###\s+Structural block[^\n]*\n+```[a-zA-Z0-9_-]*\n(.*?)\n```", chunk, re.DOTALL | re.I)
        if struct_match:
            for l_idx, line in enumerate(struct_match.group(1).splitlines(), start=1):
                if len(line) > 100:
                    failures.append(f"{sid}: structural block line {l_idx} length {len(line)} exceeds 100 characters")

    # 3. boundary audit
    failures.extend(audit_boundary(art))

    # 4. coverage table
    cov_match = re.search(r"^##\s+Coverage table[^\n]*\n(.*?)(?=\n##|\Z)", art, re.M | re.S)
    if not cov_match:
        failures.append("missing required section '## Coverage table'")
    else:
        cov_rows = re.findall(r"^\|\s*`?(SCREEN-[A-Za-z0-9-]+)`?\s*\|", cov_match.group(1), re.M)
        cov_screens = set(cov_rows)
        for sid in sorted(in_flow - cov_screens):
            failures.append(f"coverage table: missing screen {sid}")
        for sid in sorted(cov_screens - in_flow):
            failures.append(f"coverage table: screen {sid} not in frozen flow")

    for f in failures:
        print(f"FAIL  {f}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    print(
        f"PASS  {len(in_art)} entries, screen set matches the frozen flow, "
        f"one primary action each, boundary audit clean"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
