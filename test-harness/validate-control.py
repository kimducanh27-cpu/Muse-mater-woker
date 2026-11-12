#!/usr/bin/env python3
"""Validate a Process 05 or 06 Control File against templates/CONTROL-FIELDS-v1.yaml.

Exists because a read-back that compares an artifact to the writer's memory of
writing it always passes. This compares it to something external.

Usage: python test-harness/validate-control.py <control-file>
Exit:  0 = PASS, 1 = FAIL, 2 = cannot evaluate
"""

import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml")
    sys.exit(2)

CONTRACT = pathlib.Path(__file__).resolve().parent.parent / "templates" / "CONTROL-FIELDS-v1.yaml"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL  file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        print("FAIL  no YAML frontmatter")
        return 1

    try:
        doc = yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        print(f"FAIL  frontmatter does not parse: {exc}")
        return 1

    contract = yaml.safe_load(CONTRACT.read_text(encoding="utf-8"))
    common = set(contract["common"])
    events = contract["events"]
    prose = set(contract.get("prose_events") or [])
    drift = contract.get("known_drift") or {}

    failures: list[str] = []
    notes: list[str] = []

    # 1-3. header state
    if doc.get("schema_version") != contract["schema_version"]:
        failures.append(f"schema_version is {doc.get('schema_version')!r}, expected {contract['schema_version']}")

    seq = doc.get("state_seq")
    log = doc.get("event_log") or []
    if not isinstance(seq, int) or seq < 0:
        failures.append(f"state_seq is {seq!r}, expected a non-negative integer")
    elif len(log) > seq:
        failures.append(f"event_log has {len(log)} events but state_seq is {seq}")

    # 4. per-event key sets
    for i, ev in enumerate(log):
        if not isinstance(ev, dict):
            failures.append(f"event[{i}] is not a mapping")
            continue
        et = ev.get("event_type")
        if et in prose:
            required = common
        elif et in events:
            required = common | set(events[et])
        else:
            failures.append(f"event[{i}] has unknown event_type {et!r}")
            continue

        got = set(ev.keys())
        for key in sorted(required - got):
            hint = ""
            for canonical, wrong in drift.items():
                if canonical == key:
                    hit = [w for w in wrong if w in got]
                    if hit:
                        hint = f"  (found {hit[0]!r} instead)"
            failures.append(f"event[{i}] {et}: missing key {key!r}{hint}")
        for key in sorted(got - required):
            failures.append(f"event[{i}] {et}: extra key {key!r}")

        if ev.get("state_seq") != seq - len(log) + i + 1 and len(log) == seq:
            notes.append(f"event[{i}] state_seq is {ev.get('state_seq')!r}; sequence is not contiguous from 1")

    # 5. decision log hash
    dl = doc.get("decision_log") or {}
    declared = dl.get("latest_sha256")
    dl_path = dl.get("path")
    if not declared:
        failures.append("decision_log.latest_sha256 is null")
    elif dl_path:
        base = path.parent
        for candidate in (base.parent.parent / dl_path, base.parent.parent.parent / dl_path):
            if candidate.exists():
                import hashlib

                actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
                if actual != declared:
                    failures.append(f"decision_log.latest_sha256 does not match {candidate} (declared {declared[:12]}…, actual {actual[:12]}…)")
                break
        else:
            notes.append(f"decision log not found on disk at {dl_path}; hash not verified")

    # 6. lifecycle consistency
    life = doc.get("lifecycle_status")
    g3 = (doc.get("gate_3") or {}).get("status")
    if life == "FROZEN" and g3 != "APPROVED":
        failures.append(f"lifecycle_status FROZEN requires gate_3 APPROVED, found {g3!r}")
    if life == "DRAFT" and g3 == "APPROVED":
        failures.append("lifecycle_status DRAFT with gate_3 APPROVED is inconsistent")

    for n in notes:
        print(f"NOTE  {n}")
    for f in failures:
        print(f"FAIL  {f}")

    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1

    print("PASS  Control File matches the field contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
