---
schema_version: 1
process: "06-design-systems"
initiative_id: "REPLACE_WITH_VERIFIED_INITIATIVE_ID"
state_seq: 0
created_at_local: null
last_updated_local: "NOT_VERIFIED"
platform:
  target: "android"
  framework: "jetpack-compose"
  design_language: "material-3"
  decision_ref: "process-charters/06-DESIGN-SYSTEMS.md#8a"
  recorded_at_local: null
source_process_05:
  control_path: "product/ux-design/00_UX_CONTROL.md"
  initiative_id: null
  gate_3_status: "NOT_VERIFIED"
  lifecycle_status: "NOT_VERIFIED"
  frozen_artifact_path: "product/ux-design/UX_SPEC.md"
  frozen_artifact_sha256: null
  verified_file_sha256: null
  status: "NOT_VERIFIED"
  verified_at_local: null
source_process_04:
  control_path: "product/app-flow/00_APP_FLOW_CONTROL.md"
  frozen_artifact_path: "product/app-flow/APP_FLOW.md"
  frozen_artifact_sha256: null
  verified_file_sha256: null
  status: "NOT_VERIFIED"
gate_1:
  status: "PENDING"
  required_command: "APPROVE DESIGN FOUNDATIONS"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE COMPONENT LIBRARY"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_3:
  status: "PENDING"
  required_command: "FREEZE DESIGN SYSTEM"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  frozen_at_local: null
  reviewed_draft:
    path: "product/design-system/06_DS_DRAFT.md"
    sha256: null
  frozen_artifact:
    path: "product/design-system/DESIGN_SYSTEM.md"
    sha256: null
  frozen_version: 0
  archived_versions: []
coverage:
  screens_in_source: null
  screens_citing_a_component: null
  tokens_defined: null
  components_defined: null
  components_cited: null
  contrast_pairs_measured: null
  contrast_pairs_total: null
  last_computed_at_local: null
review:
  round: 0
  status: "NOT_STARTED"
  open_blockers: 0
  open_critical: 0
  open_major: 0
  open_minor: 0
  latest_review_path: "product/design-system/05_DS_REVIEW.md"
  latest_review_sha256: null
  reviewed_draft_path: "product/design-system/06_DS_DRAFT.md"
  reviewed_draft_sha256: null
  reviewed_artifacts: []
decision_log:
  path: "product/design-system/07_DECISION_LOG.md"
  latest_sha256: null
accepted_residual_risks: []
event_log: []
lifecycle_status: "DRAFT"
timezone: "Asia/Ho_Chi_Minh"
---

# Process 06 — Canonical Design System Control (Schema v1)

This is a template, not a live Control File. Copy it to `product/design-system/00_DS_CONTROL.md` only after both sources are verified. Never overwrite another initiative's Control File.

## Allowed values

- Gate: `PENDING`, `APPROVED`, `REJECTED`, `REOPENED`.
- Lifecycle: `DRAFT`, `REVIEW_REQUIRED`, `FROZEN`, `ABANDONED`.
- Source status: `VERIFIED`, `NOT_VERIFIED`, `REOPENED`.
- Review: `NOT_STARTED`, `BLOCKERS_FOUND`, `READY_FOR_FREEZE`.
- Finding severity: `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`.
- Finding status: `OPEN`, `RESOLVED`, `ACCEPTED_BY_USER`.

Gate 3 status remains `APPROVED` after a successful freeze; only `lifecycle_status` becomes `FROZEN`.

## Platform is a field, not an assumption

`platform` is written once at initialization and is immutable for the life of the workspace. Changing it is not a local decision: it reopens Gates 1–3 and requires a new design system, because target size, type scale, elevation semantics and motion budget all derive from it.

The recorded value is `android` / `jetpack-compose` / `material-3`, decided in `process-charters/06-DESIGN-SYSTEMS.md` section 8a. A workspace with a different value is not wrong — it is a different product, and it needs its own initiative ID.

A Material 3 default is not a design decision. The platform supplies a vocabulary; this process still has to decide which parts of it the product uses, and justify each one against a citing screen.

## Source eligibility

**Process 05 (the UX spec).** Require `initiative_id` present; `gate_3.status = APPROVED`; `lifecycle_status = FROZEN`; `gate_3.frozen_artifact.path` equals `product/ux-design/UX_SPEC.md`; actual SHA-256 of that file equals `gate_3.frozen_artifact.sha256`; no open Change Request in the Process 05 workspace.

**Process 04 (the flow).** Verified transitively: the actual SHA-256 of `product/app-flow/APP_FLOW.md` must equal the hash Process 05 recorded in its own `source_process_04.frozen_artifact_sha256`. Process 06 does not re-open Process 04 and does not read a Process 03 file at all.

Both statuses must be `VERIFIED` before any artifact is written.

## Coverage counters

`coverage` is a computed checkpoint, not a judgement. The two numbers that matter:

- `components_cited` must equal `components_defined` at Gate 2. A component nobody cites is speculative and is rejected.
- `screens_citing_a_component` must equal `screens_in_source` at Gate 2. A screen that cites no component either needs one or proves the system cannot express it.

`contrast_pairs_measured` must equal `contrast_pairs_total` at Gate 2. A contrast pair that was declared but not computed is not evidence.

A coverage number that decreases without an `INVALIDATED` event is evidence of tampering, not progress.

## Control event log

Every `event_log` object MUST contain `event_type`, `state_seq`, `timestamp_local`, `exact_user_command` (or `NOT_APPLICABLE`), `reason`, `changed_paths` and `relevant_hashes`. `state_seq` is strictly increasing and equals the new committed sequence.

**Field names are normative in `templates/CONTROL-FIELDS-v1.yaml`, not in the table below.** The table describes intent; that file lists the exact key names. A read-back compares the event's key set to the contract, not to what the writer remembers writing.

| Event type | Required type-specific fields |
|---|---|
| `DECISION_LOG_UPDATED` | decision_id; decision_log_event_id; decision_event_kind (`INITIALIZATION`, `PROPOSAL_CREATED`, `DECISION_STATUS_CHANGED`); status before/after; affected_gate; path; resulting_sha256 |
| `GATE_1_APPROVED` | gate=GATE_1; exact command; approved_artifacts (01 path/hash); decision_log_sha256; coverage snapshot |
| `GATE_2_APPROVED` | gate=GATE_2; exact command; approved_artifacts (02–04 path/hash); decision_log_sha256; coverage snapshot |
| `GATE_3_FROZEN` | gate=GATE_3; exact command; draft_sha256; frozen_artifact_path; frozen_artifact_sha256; frozen_version |
| `INVALIDATED` | reopened_gates; affected_gate when known; expected_hashes; observed_hashes; reason |
| `DECISION_LOG_RECOVERED` | decision_id; decision_log_event_id; recovered_from_event_seq; resulting_sha256; affected_gate; reopened_gates |
| `REVIEW_HISTORY_INITIALIZED` | review_path; review_sha256 |
| `REVIEW_ROUND_RECORDED` | review_round; review_path; previous_review_sha256; review_sha256; draft_path; draft_sha256; verdict; review_status |
| `REVIEW_ROUND_RECOVERED` | review_round; review_path; previous_review_sha256; review_sha256; draft_path; draft_sha256; verdict; review_status; recovered_from_state_seq |
| `RESIDUAL_RISK_ACCEPTED` | finding_id; severity; exact command; rationale; accepted_at_local |
| `GATE_REJECTED`, `REVISION_REQUESTED`, `DESIGN_SYSTEM_ABANDONED` | exact targets, reason and hashes needed to reconstruct the event |

There is no migration event in schema v1. A Control File claiming a predecessor schema, or carrying `SCHEMA_MIGRATED`, is `NOT_VERIFIED`.

## Gate rules

- **Gate 1** binds artifact 01 (foundations) plus the Decision Log. It asserts that every foundation value has a named role, and that no value exists without a role that a screen could need.
- **Gate 2** binds 02–04 and the Decision Log. It asserts that every component cites at least one frozen SCREEN ID, every screen cites at least one component, and every contrast pair is measured.
- **Gate 3** binds the reviewed draft and the frozen output. At least one review round, zero open findings, matching hashes.

Any Decision Log byte change after Gate 2 reopens Gates 2–3. A change independently classified as Gate 1 also reopens Gate 1.

## Freeze

The reviewed draft is the complete canonical candidate. Freeze copies it byte-for-byte and changes only the status line from `REVIEWED CANDIDATE — NOT FROZEN` to `FROZEN`. The frozen SHA-256 lives here, never inside `DESIGN_SYSTEM.md`.

Before re-freeze, archive the prior canonical output as `DESIGN_SYSTEM.v<N>.md`, verify it byte-for-byte, then replace.

## Downstream eligibility

A Process 07 consumer requires: workspace integrity `VERIFIED`; schema v1 with a valid event sequence; both sources `VERIFIED`; all three Gates `APPROVED` with current hashes and sequence anchors; lifecycle `FROZEN`; actual `DESIGN_SYSTEM.md` hash equal to `gate_3.frozen_artifact.sha256`; the latest review snapshot matching the current draft; and `platform.target` equal to the platform Process 07 is composing for.

A FROZEN status line is never proof of freeze.
