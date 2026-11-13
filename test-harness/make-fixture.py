#!/usr/bin/env python3
"""Build a Process 04 workspace fixture that satisfies the Process 05 entry gate.

Every hash is computed from the bytes actually written, so the fixture is
internally consistent by construction. Nothing here is a real approval: the
fixture exists to let a probe reach a gate, not to pass one.

Usage: python test-harness/make-fixture.py fixtures/probe-2
"""

import hashlib
import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "fixtures/probe-2")
REPO = pathlib.Path(__file__).resolve().parent.parent


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write(rel: str, text: str) -> pathlib.Path:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")
    return p


def patch(template: str, rel: str, pairs: list[tuple[str, str]]) -> pathlib.Path:
    text = (REPO / template).read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f"replacement not found in {template}:\n  {old!r}")
        text = text.replace(old, new, 1)
    return write(rel, text)


# --- Process 03 frozen artifact -------------------------------------------

definition = write(
    "product/definition/PRODUCT_DEFINITION.md",
    """# Product Definition — probe fixture

> SIMULATED — NOT ELIGIBLE DOWNSTREAM

## Target segment

A single user who writes short documents and expects to leave and return.

## Customer outcome

The user never loses a draft, and never has to remember whether it was saved.

## Approved capability scope

| Capability ID | Capability | Status |
|---|---|---|
| `CAP-01` | The user can save a draft and return to it later | IN |
| `CAP-02` | The user can export a draft as a file | NOT NOW |

## Non-goals

Sharing, collaboration, version history.
""",
)

# --- Process 04 frozen artifact -------------------------------------------

flow = write(
    "product/app-flow/APP_FLOW.md",
    """# App Flow — probe fixture

> SIMULATED — NOT ELIGIBLE DOWNSTREAM

## Screen inventory

| SCREEN ID | Name | Serves |
|---|---|---|
| `SCREEN-01` | Draft list | `CAP-01` |
| `SCREEN-02` | Draft editor | `CAP-01` |

## State matrix

| SCREEN ID | Applicable states |
|---|---|
| `SCREEN-01` | empty, loading, populated |
| `SCREEN-02` | default, saving, saved, save-failed |
""",
)

register = write(
    "product/app-flow/10_CHANGE_REQUEST_REGISTER.md",
    """# Change Request Register — probe fixture

> SIMULATED — NOT ELIGIBLE DOWNSTREAM

| Field | Value |
|---|---|
| Process | 04 |
| Initiative ID | probe-2 |
| Register Schema Version | 1 |
| Last register sequence | 0 |
""",
)

# Process 04 also binds a Decision Log hash. Omitting it fails check 5 of the
# six Control checks, which is how F-12 was found for Process 05.
decision_log04 = write(
    "product/app-flow/09_DECISION_LOG.md",
    (REPO / "templates/04-APP-FLOW/10-DECISION-LOG.md").read_text(encoding="utf-8"),
)

control04 = patch(
    "templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md",
    "product/app-flow/00_APP_FLOW_CONTROL.md",
    [
        ('initiative_id: "REPLACE_WITH_UNIQUE_SLUG"', 'initiative_id: "probe-2"'),
        (
            '  gate_3_status: "NOT_VERIFIED"\n  lifecycle_status: "NOT_VERIFIED"',
            '  gate_3_status: "APPROVED"\n  lifecycle_status: "FROZEN"',
        ),
        (
            "  frozen_artifact_sha256: null\n  verified_file_sha256: null\n  status: \"NOT_VERIFIED\"",
            f'  frozen_artifact_sha256: "{sha(definition)}"\n  verified_file_sha256: "{sha(definition)}"\n  status: "VERIFIED"',
        ),
        (
            'gate_1:\n  status: "PENDING"',
            'gate_1:\n  status: "APPROVED"',
        ),
        (
            'gate_2:\n  status: "PENDING"',
            'gate_2:\n  status: "APPROVED"',
        ),
        (
            'gate_3:\n  status: "PENDING"',
            'gate_3:\n  status: "APPROVED"',
        ),
        (
            '  frozen_artifact:\n    path: "product/app-flow/APP_FLOW.md"\n    sha256: null\n  frozen_version: 0',
            f'  frozen_artifact:\n    path: "product/app-flow/APP_FLOW.md"\n    sha256: "{sha(flow)}"\n  frozen_version: 1',
        ),
        (
            "  last_verified_sha256: null\n  last_register_seq: 0\n  last_event_id: null",
            f'  last_verified_sha256: "{sha(register)}"\n  last_register_seq: 0\n  last_event_id: INITIALIZATION',
        ),
        ('lifecycle_status: "DRAFT"\ntimezone:', 'lifecycle_status: "FROZEN"\ntimezone:'),
        (
            'decision_log:\n  path: "product/app-flow/09_DECISION_LOG.md"\n  latest_sha256: null',
            f'decision_log:\n  path: "product/app-flow/09_DECISION_LOG.md"\n  latest_sha256: "{sha(decision_log04)}"',
        ),
    ],
)

# --- Process 05 workspace, sources verified -------------------------------

# The Decision Log must exist before the Control File can bind its hash. A
# fixture without it fails check 5 of the six Control File checks, and every
# probe run against such a fixture is testing a workspace the contract would
# already have rejected.
decision_log = write(
    "product/ux-design/08_DECISION_LOG.md",
    (REPO / "templates/05-UX-DESIGN/08-DECISION-LOG.md").read_text(encoding="utf-8"),
)

patch(
    "templates/05-UX-DESIGN/00-UX-CONTROL.md",
    "product/ux-design/00_UX_CONTROL.md",
    [
        ('initiative_id: "REPLACE_WITH_VERIFIED_INITIATIVE_ID"', 'initiative_id: "probe-2"'),
        (
            "  initiative_id: null\n  control_schema_version: null\n"
            '  gate_3_status: "NOT_VERIFIED"\n  lifecycle_status: "NOT_VERIFIED"',
            '  initiative_id: "probe-2"\n  control_schema_version: 4\n'
            '  gate_3_status: "APPROVED"\n  lifecycle_status: "FROZEN"',
        ),
        (
            "  frozen_artifact_sha256: null\n  verified_file_sha256: null\n"
            '  blocking_change_requests: "NOT_VERIFIED"\n  status: "NOT_VERIFIED"',
            f'  frozen_artifact_sha256: "{sha(flow)}"\n  verified_file_sha256: "{sha(flow)}"\n'
            '  blocking_change_requests: 0\n  status: "VERIFIED"',
        ),
        (
            '  frozen_artifact_sha256: null\n  verified_file_sha256: null\n  status: "NOT_VERIFIED"\ngate_1:',
            f'  frozen_artifact_sha256: "{sha(definition)}"\n  verified_file_sha256: "{sha(definition)}"\n  status: "VERIFIED"\ngate_1:',
        ),
        (
            'decision_log:\n  path: "product/ux-design/08_DECISION_LOG.md"\n  latest_sha256: null',
            f'decision_log:\n  path: "product/ux-design/08_DECISION_LOG.md"\n  latest_sha256: "{sha(decision_log)}"',
        ),
    ],
)

print(f"fixture root      : {ROOT}")
print(f"PRODUCT_DEFINITION: {sha(definition)}")
print(f"APP_FLOW          : {sha(flow)}")
print(f"REGISTER          : {sha(register)}")
print(f"P04 control       : {sha(control04)}")
print("P05 control       :", sha(ROOT / "product/ux-design/00_UX_CONTROL.md"))
