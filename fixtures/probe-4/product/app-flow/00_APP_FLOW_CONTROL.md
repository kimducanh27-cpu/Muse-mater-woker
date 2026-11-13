---
schema_version: 4
process: "04-app-flow"
initiative_id: "probe-2"
state_seq: 0
created_at_local: null
last_updated_local: "NOT_VERIFIED"
source_process_03:
  control_path: "product/definition/00_PRODUCT_DEFINITION_CONTROL.md"
  initiative_id: null
  gate_3_status: "APPROVED"
  lifecycle_status: "FROZEN"
  frozen_artifact_path: "product/definition/PRODUCT_DEFINITION.md"
  frozen_artifact_sha256: "697c6f7b05b11a4efbaea954945fee7a1d5479d1fa4abb91fb192e6cfea0e684"
  verified_file_sha256: "697c6f7b05b11a4efbaea954945fee7a1d5479d1fa4abb91fb192e6cfea0e684"
  status: "VERIFIED"
  verified_at_local: null
gate_1:
  status: "APPROVED"
  required_command: "APPROVE TASK MODEL"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_2:
  status: "APPROVED"
  required_command: "APPROVE APP FLOW"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_3:
  status: "APPROVED"
  required_command: "FREEZE APP FLOW"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  frozen_at_local: null
  approved_artifacts: []
  reviewed_draft:
    path: "product/app-flow/08_APP_FLOW_DRAFT.md"
    sha256: null
  frozen_artifact:
    path: "product/app-flow/APP_FLOW.md"
    sha256: "1a35de5f36d12dc533d9d63ecc5f8555a375175333509a78f784005f941311c9"
  frozen_version: 1
  archived_versions: []
review:
  round: 0
  status: "NOT_STARTED"
  open_blockers: 0
  open_critical: 0
  open_major: 0
  open_minor: 0
  latest_review_path: "product/app-flow/07_FLOW_REVIEW.md"
  latest_review_sha256: null
  reviewed_draft_path: "product/app-flow/08_APP_FLOW_DRAFT.md"
  reviewed_draft_sha256: null
  reviewed_artifacts: []
decision_log:
  path: "product/app-flow/09_DECISION_LOG.md"
  latest_sha256: null
change_request_register:
  path: "product/app-flow/10_CHANGE_REQUEST_REGISTER.md"
  schema_version: 1
  last_verified_sha256: "a1c5402f840edbe54ff6a89fb08dc4cc15d7b2e91b1ee7234ab207e907c7ad59"
  last_register_seq: 0
  last_event_id: INITIALIZATION
accepted_residual_risks: []
event_log: []
lifecycle_status: "FROZEN"
timezone: "Asia/Ho_Chi_Minh"
---

# Process 04 — Canonical App Flow Control (Schema v4)

This is a template, not a live Control File. Copy it to `product/app-flow/00_APP_FLOW_CONTROL.md` only after verifying the Process 03 initiative identity. Replace the initiative placeholder only with the exact verified ID. The Register is not initialized until its dedicated initialization receipt is committed and read back.

## Allowed values

- Gate: `PENDING`, `APPROVED`, `REJECTED`, `REOPENED`.
- Lifecycle: `DRAFT`, `REVIEW_REQUIRED`, `FROZEN`, `ABANDONED`.
- P03 source: `VERIFIED`, `NOT_VERIFIED`, `REOPENED`.
- Review: `NOT_STARTED`, `BLOCKERS_FOUND`, `READY_FOR_FREEZE`.
- Finding severity: `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`.
- Finding status: `OPEN`, `RESOLVED`, `ACCEPTED_BY_USER`.
- CR business states are reconstructed only from the Register; never add a second CR status array here.

## Source eligibility

Before P04 source status becomes `VERIFIED`, verify the actual P03 v2 Control File and frozen Product Definition. Require P03 Gate 3 `APPROVED`, lifecycle `FROZEN`, correct frozen artifact path, actual SHA-256 equal to P03 v2 `gate_3.frozen_artifact.sha256`, and exact initiative identity match. Do not invent `gate_3.approved_state_seq` in P03. P04 MUST NOT modify P03.

## Register checkpoint and initialization

`change_request_register` is an integrity pointer, not a business-status store. It MUST contain `path`, `schema_version`, `last_verified_sha256`, `last_register_seq` and `last_event_id`.

At v4 workspace initialization, create the header-only Register and append one Control `CHANGE_REQUEST_REGISTER_INITIALIZED` event at the next committed Control sequence. Bind initiative ID, path, Register schema v1, `register_seq: 0`, `last_event_id: INITIALIZATION` and the non-null exact-byte `last_verified_sha256`. Read both files back. A v4 workspace with zero CRs still has `last_register_seq: 0` and a non-null hash. Null hash or missing initialization receipt means `NOT_VERIFIED`.

## Control event log

Every `event_log` object MUST contain `event_type`, `state_seq`, `timestamp_local`, `exact_user_command` (or `NOT_APPLICABLE`), `reason`, `changed_paths` and `relevant_hashes`. `state_seq` is strictly increasing and equals the new committed Control File sequence. Use only these event kinds and required fields:

| Event type | Required type-specific fields |
|---|---|
| `DECISION_LOG_UPDATED` | decision_id; decision_log_event_id; decision_event_kind (`INITIALIZATION`, `PROPOSAL_CREATED`, `DECISION_STATUS_CHANGED`); status before/after; affected_gate; path; resulting_sha256 |
| `GATE_1_APPROVED` | gate=GATE_1; exact command; approved_artifacts (01/02 path/hash); decision_log_sha256 |
| `GATE_2_APPROVED` | gate=GATE_2; exact command; approved_artifacts (03–06 path/hash); decision_log_sha256 |
| `GATE_3_FROZEN` | gate=GATE_3; exact command; draft_sha256; frozen_artifact_path; frozen_artifact_sha256; frozen_version |
| `INVALIDATED` | reopened_gates; affected_gate when known; expected_hashes; observed_hashes; reason |
| `DECISION_LOG_RECOVERED` | decision_id; decision_log_event_id; recovered_from_event_seq; resulting_sha256; affected_gate; reopened_gates |
| `REVIEW_HISTORY_INITIALIZED` | review_path; review_sha256 |
| `REVIEW_ROUND_RECORDED` | review_round; review_path; previous_review_sha256; review_sha256; draft_path; draft_sha256; verdict; review_status |
| `REVIEW_ROUND_RECOVERED` | review_round; review_path; previous_review_sha256; review_sha256; draft_path; draft_sha256; verdict; review_status; recovered_from_state_seq |
| `SCHEMA_MIGRATED` | from_schema_version=3; to_schema_version=4; exact migration command; attestation; archive_directory; archive_manifest_path/hash; preserved/reopened Gate summary |
| `CHANGE_REQUEST_REGISTER_INITIALIZED` | initiative_id; path; register_schema_version=1; register_seq=0; last_event_id=INITIALIZATION; last_verified_sha256 |
| `CHANGE_REQUEST_REGISTER_UPDATED` | initiative_id; change_request_id; register_event_id; register_seq; previous_register_sha256; event_block_sha256; resulting_register_sha256 |
| `CHANGE_REQUEST_EVENT_ABORTED` | initiative_id; first/last register sequence; staged CRE-ID/CR-ID; abort-marker CRE-ID; H(k-1); staged event-block hash; H(k); abort-marker event-block hash; H(k+1); status_effect=NONE |
| `RESIDUAL_RISK_ACCEPTED` | finding_id; severity; exact command; rationale; accepted_at_local |
| `GATE_REJECTED`, `REVISION_REQUESTED`, `APP_FLOW_ABANDONED` | exact targets, reason and hashes needed to reconstruct the event |

Each `state_seq` is unique and strictly increasing. A normal Register update receipt pairs exactly one Register business event. An abort receipt pairs exactly two consecutive Register events. No receipt/event may be double-accounted. Control MUST NOT store per-CR business statuses or authoritative blocking counts/lists.

## Gate validity and downstream eligibility

Gate validity, Freeze eligibility and downstream eligibility are separate predicates. A new CR blocks downstream at `RECORDED`; it does not itself invalidate previously approved Gates until relevant bound source/artifact bytes change. Reconstruct blockers from the Register on every read. Register `NOT_VERIFIED` blocks all ordinary writes, Gate approvals, Freeze and downstream use.

Downstream requires: workspace integrity `VERIFIED`; schema v4 and valid Control event sequence; P03 v2 identity/hash verified; all three Gates approved with current hashes and sequence anchors; lifecycle `FROZEN`; actual APP_FLOW hash matching the Gate 3 Freeze receipt; full Register chain verified; reconstructed blocking set empty; every implementation CR in the Freeze batch `CLOSED_IMPLEMENTED` against the same frozen version, Gate 3 sequence and APP_FLOW hash; latest Review snapshot matching the Register hash/sequence/last event/CR set.

## Single-writer and timestamps

Tab 01 is the sole Register writer. Tab 02 and Tab 03 are read-only for Register business state. Only one logical writer may modify the Control File at a time. `state_seq` is a stale-read detector, not an OS lock, CAS, filesystem mutex or distributed lock. Use actual Asia/Ho_Chi_Minh timestamps and lowercase SHA-256. If any read-back, hash or sequence check fails, stop at `NOT_VERIFIED`.
