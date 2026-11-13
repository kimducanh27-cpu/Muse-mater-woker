#!/usr/bin/env python3
"""Apply one gate approval to a Control File, mechanically.

The gate protocol has three parts: the human types an exact command, the agent
records one event, the workspace still verifies. This script does the second
and third, and refuses the first unless the command matches exactly.

It exists because "the agent writes the event" produced two failures in one
session: a wrong field name (F-06) and a digest that verified under nothing
(F-08). A gate is too important to be hand-written YAML.

Usage:
  python test-harness/apply-gate.py <control> --gate 1 \
      --command "APPROVE SCREEN UX MODEL" --artifact <artifact-01>

Exit: 0 = gate applied and verified, 1 = refused or failed, 2 = cannot evaluate.
"""

import hashlib
import pathlib
import re
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent

# Gate number -> (required command field, artifact validator, artifact glob)
GATES = {
    1: ("required_command", "validate-ux-model.py", None),
}


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("FAIL  no YAML frontmatter")
    return m.group(1), m.group(2)


def now_local() -> str:
    """+07:00 fixed. Vietnam has no daylight saving, so no tz database is needed.

    zoneinfo would be more general but requires the tzdata package on Windows,
    which is not installed here. A fixed offset is exact for this zone and
    cannot fail at runtime.
    """
    import datetime

    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S %z")


def main() -> int:
    args = sys.argv[1:]
    if not args or "--gate" not in args or "--command" not in args:
        print(__doc__)
        return 2

    control = pathlib.Path(args[0])
    gate_no = int(args[args.index("--gate") + 1])
    command = args[args.index("--command") + 1]
    artifact = pathlib.Path(args[args.index("--artifact") + 1]) if "--artifact" in args else None

    if not control.exists():
        print(f"FAIL  control not found: {control}")
        return 2
    if gate_no not in GATES:
        print(f"FAIL  gate {gate_no} has no validator mapping in this script.")
        print("      Refusing rather than applying a gate nothing checks.")
        return 2

    fm_text, body = split_frontmatter(control.read_text(encoding="utf-8"))
    doc = yaml.safe_load(fm_text)

    gate = doc.get(f"gate_{gate_no}") or {}
    required = gate.get("required_command")
    if command != required:
        print("FAIL  command does not match the gate's required_command")
        print(f"      given   : {command!r}")
        print(f"      required: {required!r}")
        return 1

    if gate.get("status") not in ("PENDING", "REOPENED"):
        print(f"FAIL  gate_{gate_no}.status is {gate.get('status')!r}; only PENDING or REOPENED may be approved")
        return 1

    if artifact is None or not artifact.exists():
        print("FAIL  --artifact is required for gate 1 and must exist")
        return 1

    # The artifact must pass its own validator before a gate may bind it.
    import subprocess

    validator = REPO / "test-harness" / GATES[gate_no][1]
    flow = control.parent.parent.parent / "product/app-flow/APP_FLOW.md"
    result = subprocess.run(
        [sys.executable, str(validator), str(artifact), str(flow)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("FAIL  the artifact does not pass its validator; gate not applied")
        print(result.stdout.strip() or result.stderr.strip())
        return 1

    decision_log = control.parent / "08_DECISION_LOG.md"
    if not decision_log.exists():
        print(f"FAIL  decision log not found at {decision_log}; gate cannot bind a hash")
        return 1

    new_seq = int(doc.get("state_seq") or 0) + 1
    event = {
        "event_type": f"GATE_{gate_no}_APPROVED",
        "state_seq": new_seq,
        "timestamp_local": now_local(),
        "exact_user_command": command,
        "reason": "Gate approved by the repository owner.",
        "changed_paths": [str(control.relative_to(control.parents[2]))],
        "relevant_hashes": {
            "artifact": sha(artifact),
            "decision_log": sha(decision_log),
        },
        "gate": f"GATE_{gate_no}",
        "approved_artifacts": [
            {"path": str(artifact.relative_to(control.parents[2])), "sha256": sha(artifact)}
        ],
        "decision_log_sha256": sha(decision_log),
        "coverage_snapshot": doc.get("coverage") or {},
    }

    doc["state_seq"] = new_seq
    doc.setdefault("event_log", []).append(event)
    doc[f"gate_{gate_no}"].update({
        "status": "APPROVED",
        "approved_command": command,
        "approved_at_local": event["timestamp_local"],
        "approved_state_seq": new_seq,
        "decision_log_sha256": event["decision_log_sha256"],
        "approved_artifacts": event["approved_artifacts"],
    })

    dumped = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100)
    control.write_text(f"---\n{dumped}---\n{body}", encoding="utf-8", newline="\n")

    # Read back and verify against the field contract.
    check = subprocess.run(
        [sys.executable, str(REPO / "test-harness" / "validate-control.py"), str(control)],
        capture_output=True, text=True,
    )
    print(f"applied GATE_{gate_no} at state_seq {new_seq}")
    print(check.stdout.strip())
    if check.returncode != 0:
        print("FAIL  the Control File no longer verifies after the write")
        return 1
    print("PASS  gate applied, event bound, workspace still verifies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
