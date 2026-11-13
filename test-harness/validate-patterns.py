#!/usr/bin/env python3
"""Validate a Process 05 artifact 02 (Interaction Pattern Library).

Checks the rules the template states and prose cannot enforce:
  1. Every pattern in the register has a detail section, and every detail
     section belongs to a registered pattern.
  2. Every detail carries the five mandatory subsections.
  3. Every pattern is cited by at least one screen, or is reserved with a
     decision ID. A pattern that does neither is a habit.
  4. Citing screens exist in the frozen Process 04 inventory.
  5. The citation check table agrees with the register.
  6. The boundary holds: no component names, no visual values.

Usage: python test-harness/validate-patterns.py <artifact-02> <app-flow>
Exit:  0 = PASS, 1 = FAIL, 2 = cannot evaluate
"""

import importlib.util
import pathlib
import re
import sys

# Reuse the audit helpers rather than copying them. A duplicated word list
# drifts, and a drifted audit is how F-04 happened.
_spec = importlib.util.spec_from_file_location(
    "vum", pathlib.Path(__file__).resolve().parent / "validate-ux-model.py"
)
_vum = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vum)

PAT = re.compile(r"`?(PAT-\d{2,})`?")
REGISTER_ROW = re.compile(r"^\|\s*`?(PAT-\d{2,})`?\s*\|(.+)$", re.M)
DETAIL = re.compile(r"^##\s+Pattern detail\s+—\s+`?(PAT-\d{2,})`?\s*$", re.M)
INVENTORY_ROW = re.compile(r"^\|\s*`?(SCREEN-[A-Za-z0-9-]+)`?\s*\|", re.M)
SUBSECTIONS = ["Behaviour", "Preconditions", "Recovery", "Refusal condition", "Cited by"]


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def section(art: str, heading: str) -> str:
    """Return the body of one `## heading` section, and nothing after it.

    Scanning the whole document instead is how this validator first reported
    every pattern twice: the citation check table is also a table of PAT IDs.
    A checker that reads past the end of its section measures the wrong thing.
    """
    marker = f"## {heading}"
    i = art.find(marker)
    if i < 0:
        return ""
    j = art.find("\n## ", i + len(marker))
    return art[i:] if j < 0 else art[i:j]


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

    failures: list[str] = []

    # 1-2. register and details
    register: dict[str, list[str]] = {}
    for m in REGISTER_ROW.finditer(section(art, "Pattern register")):
        pid, rest = m.group(1), m.group(2)
        if pid in register:
            failures.append(f"{pid} appears twice in the pattern register")
        register[pid] = cells("|" + rest)

    details = {m.group(1): m.start() for m in DETAIL.finditer(art)}
    for pid in sorted(set(register) - set(details)):
        failures.append(f"{pid} is registered but has no detail section")
    for pid in sorted(set(details) - set(register)):
        failures.append(f"{pid} has a detail section but is not in the register")

    detail_spans = sorted(details.items(), key=lambda kv: kv[1])
    for i, (pid, start) in enumerate(detail_spans):
        end = detail_spans[i + 1][1] if i + 1 < len(detail_spans) else len(art)
        chunk = art[start:end]
        for sub in SUBSECTIONS:
            if not re.search(rf"\*\*{re.escape(sub)}\.\*\*", chunk):
                failures.append(f"{pid}: missing subsection {sub!r}")

    # 3-4. citation or reservation
    reserved: dict[str, str] = {}
    if section(art, "Reserved patterns"):
        for m in REGISTER_ROW.finditer(section(art, "Reserved patterns")):
            row = cells("|" + m.group(2))
            decision = row[1] if len(row) > 1 else ""
            reserved[m.group(1)] = decision

    for pid, row in register.items():
        used_by = row[4] if len(row) > 4 else ""
        screens = set(re.findall(r"SCREEN-[A-Za-z0-9-]+", used_by))
        unknown = screens - known_screens
        for s in sorted(unknown):
            failures.append(f"{pid}: cites {s}, which is not in the frozen flow")
        if not screens:
            if pid not in reserved:
                failures.append(f"{pid} is cited by no screen and is not reserved — that is a habit, not a decision")
            elif not reserved[pid] or not re.search(r"DEC-\d+", reserved[pid]):
                failures.append(f"{pid} is reserved without a decision ID")

    # 5. citation check table
    check_block = art.split("## Citation check", 1)
    if len(check_block) != 2:
        failures.append("missing the citation check table")
    else:
        seen = set()
        for m in REGISTER_ROW.finditer(check_block[1]):
            pid = m.group(1)
            row = cells("|" + m.group(2))
            seen.add(pid)
            if pid not in register:
                failures.append(f"citation check lists {pid}, which is not in the register")
                continue
            status = (row[1] if len(row) > 1 else "").upper()
            if status not in ("CITED", "RESERVED"):
                failures.append(f"{pid}: citation status is {status!r}, expected CITED or RESERVED")
            elif status == "RESERVED" and pid not in reserved:
                failures.append(f"{pid} is marked RESERVED in the check but is not in the reserved table")
            elif status == "CITED" and pid in reserved:
                failures.append(f"{pid} is marked CITED in the check but is listed as reserved")
        for pid in sorted(set(register) - seen):
            failures.append(f"{pid} is missing from the citation check table")

    # 6. boundary
    body = _vum.mask_workflow_tabs(_vum.strip_fences(_vum.strip_rule_block(art)))
    for term in _vum.BANNED:
        for hit in re.finditer(rf"\b{re.escape(term)}\b", body, re.IGNORECASE):
            line_no = body[: hit.start()].count("\n") + 1
            failures.append(f"boundary: line ~{line_no} matched {term!r} — \"{_vum.sentence_at(body, hit.start())}\"")

    for f in failures:
        print(f"FAIL  {f}")
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    print(f"PASS  {len(register)} patterns, all defined, cited or reserved, boundary clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
