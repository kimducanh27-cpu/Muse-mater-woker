#!/usr/bin/env python3
"""Validate a Process 05 artifact 01 (Screen UX Model) against the frozen flow.

Checks four things the Skill requires and prose cannot enforce:
  1. Screen set: every SCREEN ID in the frozen flow has exactly one entry, and
     no entry names a screen that does not exist.
  2. One primary action per screen, non-empty.
  3. The component-name audit, run as a procedure: word boundaries, body only,
     excluding the rule block and fenced blocks.
  4. Required template sections present.

Usage: python test-harness/validate-ux-model.py <artifact-01> <app-flow>
Exit:  0 = PASS, 1 = FAIL, 2 = cannot evaluate
"""

import pathlib
import re
import sys

BANNED = [
    "button", "card", "modal", "dialog", "toast", "chip", "tab", "drawer",
    "tooltip", "badge", "banner", "accordion",
    "app bar", "top bar", "bottom sheet", "navigation rail",
    "floating action button", "fab", "snackbar", "system back",
    "predictive back", "window size class", "inset",
]

REQUIRED_SECTIONS = ["Information hierarchy", "Structural block", "Open questions"]
SCREEN_HEADING = re.compile(r"^## (SCREEN-[A-Za-z0-9-]+) — ", re.M)
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
    in_flow = {m.group(1) for m in INVENTORY_ROW.finditer(flow)}
    in_art = [m.group(1) for m in SCREEN_HEADING.finditer(art)]
    seen = set(in_art)

    for sid in sorted(in_flow - seen):
        failures.append(f"screen {sid} exists in the frozen flow but has no entry")
    for sid in sorted(seen - in_flow):
        failures.append(f"entry {sid} does not exist in the frozen flow")
    for sid in sorted({s for s in in_art if in_art.count(s) > 1}):
        failures.append(f"screen {sid} has {in_art.count(sid)} entries, expected 1")

    # 2. one primary action per entry
    entries = list(SCREEN_HEADING.finditer(art))
    for i, m in enumerate(entries):
        end = entries[i + 1].start() if i + 1 < len(entries) else len(art)
        chunk = art[m.start():end]
        actions = re.findall(r"^\|\s*Primary action\s*\|\s*(.+?)\s*\|", chunk, re.M)
        if len(actions) != 1:
            failures.append(f"{m.group(1)}: {len(actions)} primary-action rows, expected 1")
        elif actions[0].strip().lower() in {"", "none", "not applicable", "n/a"}:
            failures.append(f"{m.group(1)}: primary action is empty")

    # 3. component audit
    body = mask_workflow_tabs(strip_fences(strip_rule_block(art)))
    for term in BANNED:
        pattern = re.compile(rf"\b{re.escape(term)}\b", re.IGNORECASE)
        for hit in pattern.finditer(body):
            line_no = body[: hit.start()].count("\n") + 1
            failures.append(
                f"component audit: line ~{line_no} matched {term!r} — \"{sentence_at(body, hit.start())}\""
            )

    # 4. sections
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^#+\s+{re.escape(section)}", art, re.M | re.IGNORECASE):
            failures.append(f"missing required section: {section}")

    for f in failures:
        print(f"FAIL  {f}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    print(
        f"PASS  {len(in_art)} entries, screen set matches the frozen flow, "
        f"one primary action each, component audit clean"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
