---
schema_version: 1
process: "05-ux-design"
initiative_id: "probe-2"
state_seq: 1
created_at_local: null
last_updated_local: "2026-11-12 17:41:10 +07:00"
source_process_04:
  control_path: "product/app-flow/00_APP_FLOW_CONTROL.md"
  initiative_id: "probe-2"
  control_schema_version: 4
  gate_3_status: "APPROVED"
  lifecycle_status: "FROZEN"
  frozen_artifact_path: "product/app-flow/APP_FLOW.md"
  frozen_artifact_sha256: "1a35de5f36d12dc533d9d63ecc5f8555a375175333509a78f784005f941311c9"
  verified_file_sha256: "1a35de5f36d12dc533d9d63ecc5f8555a375175333509a78f784005f941311c9"
  blocking_change_requests: 0
  status: "VERIFIED"
  verified_at_local: null
source_process_03:
  control_path: "product/definition/00_PRODUCT_DEFINITION_CONTROL.md"
  frozen_artifact_path: "product/definition/PRODUCT_DEFINITION.md"
  frozen_artifact_sha256: "697c6f7b05b11a4efbaea954945fee7a1d5479d1fa4abb91fb192e6cfea0e684"
  verified_file_sha256: "697c6f7b05b11a4efbaea954945fee7a1d5479d1fa4abb91fb192e6cfea0e684"
  status: "VERIFIED"
gate_1:
  status: "PENDING"
  required_command: "APPROVE SCREEN UX MODEL"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE UX SPEC"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_3:
  status: "PENDING"
  required_command: "FREEZE UX SPEC"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  frozen_at_local: null
  reviewed_draft:
    path: "product/ux-design/07_UX_SPEC_DRAFT.md"
    sha256: null
  frozen_artifact:
    path: "product/ux-design/UX_SPEC.md"
    sha256: null
  frozen_version: 0
  archived_versions: []
coverage:
  screens_in_source: null
  screens_covered: null
  states_in_source: null
  states_covered: null
  capabilities_in_source: null
  capabilities_covered: null
  last_computed_at_local: null
review:
  round: 0
  status: "NOT_STARTED"
  open_blockers: 0
  open_critical: 0
  open_major: 0
  open_minor: 0
  latest_review_path: "product/ux-design/06_UX_REVIEW.md"
  latest_review_sha256: null
  reviewed_draft_path: "product/ux-design/07_UX_SPEC_DRAFT.md"
  reviewed_draft_sha256: null
  reviewed_artifacts: []
decision_log:
  path: "product/ux-design/08_DECISION_LOG.md"
  latest_sha256: "ecbe8fc2f292f9852cf20ad9655f9b78145853671ed2a45740dfa4bf8121459e"
accepted_residual_risks: []
event_log:
  - event_type: "DECISION_LOG_UPDATED"
    state_seq: 1
    timestamp_local: "2026-11-12 17:41:10 +07:00"
    exact_user_command: "NOT_APPLICABLE"
    reason: "Initialize Decision Log identity header and baseline hash"
    changed_paths:
      - "product/ux-design/08_DECISION_LOG.md"
    relevant_hashes:
      - "ecbe8fc2f292f9852cf20ad9655f9b78145853671ed2a45740dfa4bf8121459e"
    decision_id: null
    decision_log_event_id: "INITIALIZATION"
    decision_event_kind: "INITIALIZATION"
    status_before: null
    status_after: null
    affected_gate: "GATE_1"
    path: "product/ux-design/08_DECISION_LOG.md"
    resulting_sha256: "ecbe8fc2f292f9852cf20ad9655f9b78145853671ed2a45740dfa4bf8121459e"
lifecycle_status: "DRAFT"
timezone: "Asia/Ho_Chi_Minh"
---

# Process 05 — Canonical UX Control (Schema v1)

This is a template, not a live Control File. Copy it to `product/ux-design/00_UX_CONTROL.md` only after the Process 04 source has been verified and the initiative ID has been read from that source. Never overwrite another initiative's Control File.

## Allowed values

- Gate: `PENDING`, `APPROVED`, `REJECTED`, `REOPENED`.
- Lifecycle: `DRAFT`, `REVIEW_REQUIRED`, `FROZEN`, `ABANDONED`.
- P04 source: `VERIFIED`, `NOT_VERIFIED`, `REOPENED`.
- P03 source: `VERIFIED`, `NOT_VERIFIED`, `REOPENED`.
- Review: `NOT_STARTED`, `BLOCKERS_FOUND`, `READY_FOR_FREEZE`.
- Finding severity: `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`.
- Finding status: `OPEN`, `RESOLVED`, `ACCEPTED_BY_USER`.

Gate 3 status remains `APPROVED` after a successful freeze; only `lifecycle_status` becomes `FROZEN`.

## Source eligibility — both sources, not one

Process 05 needs two frozen artifacts, and they are verified differently.

**Process 04 (the flow).** Read `product/app-flow/00_APP_FLOW_CONTROL.md`. Require: `initiative_id` present; `gate_3.status = APPROVED`; `lifecycle_status = FROZEN`; `gate_3.frozen_artifact.path` equals `product/app-flow/APP_FLOW.md`; actual SHA-256 of that file equals `gate_3.frozen_artifact.sha256`; and the reconstructed blocking Change Request set is empty. A Control File that cannot be read, a schema older than the one this workspace was initialized against, a non-empty blocking set, or any hash mismatch sets `source_process_04.status = NOT_VERIFIED` and blocks entry.

**Process 03 (the product definition).** Process 05 does not re-open Process 03. It verifies the Product Definition through the chain Process 04 already bound: the actual SHA-256 of `product/definition/PRODUCT_DEFINITION.md` must equal the hash Process 04 recorded in `source_process_03.frozen_artifact_sha256`. If Process 04 has no recorded P03 hash, the chain is broken and the source is `NOT_VERIFIED`. This is transitive verification, not a second opinion, and it deliberately avoids inventing fields in a Process 03 Control File that this process must not modify.

Both source statuses must be `VERIFIED` before any artifact is written.

## Coverage counters

`coverage` is a computed checkpoint, not a judgement. It records how many SCREEN IDs, states and capabilities exist in the frozen sources and how many have been addressed. It is recomputed at every Gate and stored so that a later reader can detect a silent shrink — a coverage number that goes down without an `INVALIDATED` event is evidence of tampering, not progress.

`states_in_source` and `capabilities_in_source` are read from the frozen Process 04 and Process 03 artifacts. `screens_in_source` is the count of SCREEN IDs in the Process 04 screen inventory.

## Control event log

Every `event_log` object MUST contain `event_type`, `state_seq`, `timestamp_local`, `exact_user_command` (or `NOT_APPLICABLE`), `reason`, `changed_paths` and `relevant_hashes`. `state_seq` is strictly increasing and equals the new committed Control File sequence.

| Event type | Required type-specific fields |
|---|---|
| `DECISION_LOG_UPDATED` | decision_id; decision_log_event_id; decision_event_kind (`INITIALIZATION`, `PROPOSAL_CREATED`, `DECISION_STATUS_CHANGED`); status before/after; affected_gate; path; resulting_sha256 |
| `GATE_1_APPROVED` | gate=GATE_1; exact command; approved_artifacts (01 path/hash); decision_log_sha256; coverage snapshot |
| `GATE_2_APPROVED` | gate=GATE_2; exact command; approved_artifacts (02–05 path/hash); decision_log_sha256; coverage snapshot |
| `GATE_3_FROZEN` | gate=GATE_3; exact command; draft_sha256; frozen_artifact_path; frozen_artifact_sha256; frozen_version |
| `INVALIDATED` | reopened_gates; affected_gate when known; expected_hashes; observed_hashes; reason |
| `DECISION_LOG_RECOVERED` | decision_id; decision_log_event_id; recovered_from_event_seq; resulting_sha256; affected_gate; reopened_gates |
| `REVIEW_HISTORY_INITIALIZED` | review_path; review_sha256 |
| `REVIEW_ROUND_RECORDED` | review_round; review_path; previous_review_sha256; review_sha256; draft_path; draft_sha256; verdict; review_status |
| `REVIEW_ROUND_RECOVERED` | review_round; review_path; previous_review_sha256; review_sha256; draft_path; draft_sha256; verdict; review_status; recovered_from_state_seq |
| `RESIDUAL_RISK_ACCEPTED` | finding_id; severity; exact command; rationale; accepted_at_local |
| `GATE_REJECTED`, `REVISION_REQUESTED`, `UX_SPEC_ABANDONED` | exact targets, reason and hashes needed to reconstruct the event |

There is no `SCHEMA_MIGRATED` event in schema v1. A Process 05 workspace has no predecessor schema; a Control File claiming otherwise is `NOT_VERIFIED`.

## Gate rules

- **Gate 1** binds artifact 01 only, plus the whole Decision Log hash at approval time. It asserts that every SCREEN ID in the frozen Process 04 inventory has an entry, and that no entry names a screen that does not exist.
- **Gate 2** binds artifacts 02–05 together with the Decision Log. It asserts that every state in the frozen Process 04 state matrix is addressed for every screen that owns it, and that every capability has at least one screen whose UX model cites it.
- **Gate 3** binds the reviewed draft and the frozen output. It requires at least one appended review round, zero open findings, and matching hashes.

Gate 1 and Gate 2 stored `decision_log_sha256` values must equal the snapshot in their own approval event. Any Decision Log byte change after Gate 2 reopens Gates 2–3 regardless of the change's apparent scope; a change independently classified as Gate 1 also reopens Gate 1.

## Freeze

The reviewed draft is the complete canonical content candidate. Freeze copies it byte-for-byte and changes only the status line from `REVIEWED CANDIDATE — NOT FROZEN` to `FROZEN`. It does not rebuild, summarise or reorder content. The frozen SHA-256 lives in this Control File, never inside `UX_SPEC.md`, to avoid a self-referential hash.

Before re-freeze, verify the existing canonical file hash against this Control File, archive it as `UX_SPEC.v<N>.md` byte-for-byte, hash the archive, and only then replace the canonical file. Never overwrite an existing archive.

## Downstream eligibility

A Process 06 consumer requires: workspace integrity `VERIFIED`; schema v1 with a valid event sequence; both source statuses `VERIFIED`; all three Gates `APPROVED` with current hashes and sequence anchors; lifecycle `FROZEN`; actual `UX_SPEC.md` hash equal to `gate_3.frozen_artifact.sha256`; and the latest review snapshot matching the current draft. Filename, status line or a prior agent's claim is never proof of freeze.
