---
schema_version: 3
process: "04-app-flow"
initiative_id: "REPLACE_WITH_UNIQUE_SLUG"
state_seq: 0
created_at_local: null
last_updated_local: "NOT_VERIFIED"
source_process_03:
  control_path: "product/definition/00_PRODUCT_DEFINITION_CONTROL.md"
  initiative_id: null
  gate_3_status: "NOT_VERIFIED"
  lifecycle_status: "NOT_VERIFIED"
  frozen_artifact_path: "product/definition/PRODUCT_DEFINITION.md"
  frozen_artifact_sha256: null
  verified_file_sha256: null
  status: "NOT_VERIFIED"
  verified_at_local: null
gate_1:
  status: "PENDING"
  required_command: "APPROVE TASK MODEL"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE APP FLOW"
  approved_command: null
  approved_at_local: null
  approved_state_seq: null
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: null
gate_3:
  status: "PENDING"
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
    sha256: null
  frozen_version: 0
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
accepted_residual_risks: []
change_requests: []
event_log: []
lifecycle_status: "DRAFT"
timezone: "Asia/Ho_Chi_Minh"
---

# Process 04 — Canonical App Flow Control

Copy this template to `product/app-flow/00_APP_FLOW_CONTROL.md` for one initiative. This template is not the live state. Replace the initiative placeholder only after verifying the Process 03 initiative.

## Allowed values

- Gate states: `PENDING`, `APPROVED`, `REJECTED`, `REOPENED`.
- Lifecycle states: `DRAFT`, `REVIEW_REQUIRED`, `FROZEN`, `ABANDONED`.
- Process 03 source status: `VERIFIED`, `NOT_VERIFIED`, `REOPENED`.
- Review status: `NOT_STARTED`, `BLOCKERS_FOUND`, `READY_FOR_FREEZE`.
- Finding severity: `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`.
- Finding status: `OPEN`, `RESOLVED`, `ACCEPTED_BY_USER`.

Gate 3 remains APPROVED after a successful freeze; lifecycle_status becomes FROZEN. Do not set a gate to FROZEN.

## Entry eligibility and source binding

Set Process 04 `initiative_id` and `source_process_03.initiative_id` equal to the Process 03 Control File's `initiative_id`.

Before setting source status VERIFIED:
- Process 03 `gate_3.status = APPROVED`.
- Process 03 `lifecycle_status = FROZEN`.
- Process 03 `gate_3.frozen_artifact.path = product/definition/PRODUCT_DEFINITION.md`.
- Actual Product Definition SHA-256 equals Process 03 `gate_3.frozen_artifact.sha256`.
- Both Control Files are readable and no conflicting initiative is present.

The authoritative comparison target is Process 03 `gate_3.frozen_artifact.sha256`, not a cached Process 04 hash. Store expected source hash and independently computed current file hash separately; both must match.

## Gate rules

- Gate 1 binds exact SHA-256 values for `01_TASK_MODEL.md` and `02_FLOW_ARCHITECTURE.md`. At approval, `gate_1.decision_log_sha256` snapshots the actual Decision Log SHA-256; this is an audit snapshot, not a requirement that the log remain byte-identical after an independently verified GATE_2/GATE_3 update. Gate 1 requires source status VERIFIED, complete template structure, full capability coverage or user-approved deferral, no unresolved GATE_1 policy decision being treated as settled, and a readable Decision Log whose actual SHA-256 matches non-null `decision_log.latest_sha256`.
- Gate 2 binds exact SHA-256 values for `03_NAVIGATION_MODEL.md`, `04_SCREEN_INVENTORY.md`, `05_FLOW_SPECIFICATION.md`, `06_STATE_AND_EXCEPTION_MATRIX.md`, and current `09_DECISION_LOG.md`. `gate_2.decision_log_sha256` must equal the current log hash at approval. It requires Gate 1 and every Gate 1 artifact hash to remain valid.
- Gate 3 requires Gate 1 and Gate 2 APPROVED with matching hashes; at least one append-only review round; latest review and draft hashes matching the Control File; zero open BLOCKER, CRITICAL, MAJOR and MINOR findings; user-originated acceptance records for accepted risks; decision log reviewed; and the exact reviewed draft frozen by status-line substitution only.
- No missing review is equivalent to a clean review. `review.round` must be at least 1 and the latest review artifact must exist and hash-match.
- A hash proves identity/integrity of bytes, not correctness of content. Completeness, template conformance and graph/traceability checks need explicit evidence.

## Append-only event and review records

Append objects to `event_log`; never delete or rewrite prior events. Record approvals, rejections, revision requests, invalidations, decision-log updates, decision outcomes, risk acceptances, review rounds, freezes, archives and abandonment. Each event MUST include `event_type`, `state_seq`, `timestamp_local`, `exact_user_command` (or `NOT_APPLICABLE`), `reason`, `changed_paths` and `relevant_hashes`. `state_seq` equals the new committed Control File sequence, never the stale pre-update value. Use only these canonical event types and type-specific fields:

| Event type | Required type-specific fields |
|---|---|
| `DECISION_LOG_UPDATED` | `decision_id`, `decision_status_after_update`, `affected_gate`, `path`, `resulting_sha256` |
| `GATE_1_APPROVED` | `gate: GATE_1`, exact command `APPROVE TASK MODEL`, `approved_artifacts` (01 and 02 path/hash pairs), `decision_log_sha256` |
| `GATE_2_APPROVED` | `gate: GATE_2`, exact command `APPROVE APP FLOW`, `approved_artifacts` (03–06 path/hash pairs), `decision_log_sha256` |
| `GATE_3_FROZEN` | `gate: GATE_3`, exact command `FREEZE APP FLOW`, `draft_sha256`, `frozen_artifact_path`, `frozen_artifact_sha256`, `frozen_version` |
| `INVALIDATED` | `reopened_gates`, `affected_gate` when known, `expected_hashes`, `observed_hashes` and reason |
| `DECISION_LOG_RECOVERED` | `decision_id`, `recovered_from_event_seq`, `resulting_sha256`, `affected_gate`, `reopened_gates` |
| `SCHEMA_MIGRATED` | `from_schema_version: 2`, `to_schema_version: 3`, archived Control File/Decision Log paths and hashes, exact user command |
| `REVIEW_ROUND_RECORDED` | review round, review path/hash, draft path/hash and verdict/status |
| `RESIDUAL_RISK_ACCEPTED` | finding ID, severity, exact user command, rationale and acceptance timestamp |

Use `decision_status_after_update: NOT_APPLICABLE` only for initial log creation. Gate 1, Gate 2 and Gate 3 `approved_state_seq` must equal the sequence of their latest corresponding approval/freeze event. For Gate 1 and Gate 2, the stored `gate_1.decision_log_sha256` / `gate_2.decision_log_sha256` must also equal the `decision_log_sha256` snapshot in that exact corresponding approval event; Gate 2's snapshot must additionally equal the current whole-file Decision Log hash while Gate 2 remains approved. A status field or `approved_command` alone is never proof of approval. Do not use free-form event names for these transitions.

The review history `07_FLOW_REVIEW.md` is append-only. Every round records source/artifact/draft hashes, verdict, status, finding counts and set/graph evidence.

## Invalidation matrix

| Changed file/source | Reopen |
|---|---|
| Process 03 Control File or frozen Product Definition | source REOPENED; Gates 1–3; lifecycle REVIEW_REQUIRED |
| `01_TASK_MODEL.md` or `02_FLOW_ARCHITECTURE.md` | Gates 1–3 |
| `03_NAVIGATION_MODEL.md`, `04_SCREEN_INVENTORY.md`, `05_FLOW_SPECIFICATION.md`, `06_STATE_AND_EXCEPTION_MATRIX.md` | Gates 2–3 |
| `07_FLOW_REVIEW.md` or `08_APP_FLOW_DRAFT.md` | Gate 3; new review round required |
| `09_DECISION_LOG.md` before Gate 2 approval | Earliest independently verified affected gate and downstream gates: GATE_1 → 1–3; GATE_2 → 2–3; GATE_3 → 3 |
| Any `09_DECISION_LOG.md` byte change after Gate 2 approval | Gates 2–3 always reopen because Gate 2 binds the whole file; also reopen Gate 1 when independent scope classification is GATE_1 |
| `APP_FLOW.md` after freeze | Gate 3; lifecycle REVIEW_REQUIRED; downstream use prohibited |

Reopening Gate 1 reopens Gates 2 and 3. Reopening Gate 2 reopens Gate 3. Any material change after freeze sets lifecycle_status to REVIEW_REQUIRED. Record every invalidation as an append-only event; never silently overwrite an approval.

## Re-freeze and archive

Before re-freezing, verify current `APP_FLOW.md` against the Control File's frozen hash. Preserve the previous canonical artifact as `APP_FLOW.v<N>.md`, where N is the previous `frozen_version`. Never overwrite an archive. Record its path/hash and increment the version only after the new canonical artifact and Control File both pass read-back.

## Failure handling

If canonical output writes but Control File write/read-back fails, report `INCOMPLETE — NOT FROZEN`. An orphan `APP_FLOW.md` is not eligible downstream. The only eligible output is one whose bytes hash-match `gate_3.frozen_artifact.sha256` while Gate 3 is APPROVED and lifecycle is FROZEN.

If an artifact or Control File cannot be read, hashed or written, stop with NOT_VERIFIED. Never guess, synthesize a hash or claim a gate/freeze succeeded.

For a Decision Log append followed by a failed or ambiguous Control File baseline/event update, stop all writers and do not repeat the append. Apply only the Skill's bounded recovery procedure. Recovery is permitted only when the actual Decision Log hash exactly matches a valid, already-persisted `DECISION_LOG_UPDATED` event for the same decision and scope; otherwise restore a trusted copy matching the prior `latest_sha256` or remain NOT_VERIFIED. If the Control File event history is partial or unreadable, restore a trusted Control File copy or stop for human-led reconciliation. Never infer a missing event or adopt an unexplained hash.

## Decision log

`09_DECISION_LOG.md` is append-only and one-initiative-only. Its immutable identity header must contain `Process: 04` and an `Initiative ID` exactly matching this Control File and Process 03; missing/mismatched identity is NOT_VERIFIED and must not be adopted by hashing. Each material flow-policy decision has a stable DEC ID, affected artifacts, affected gate, alternatives and rationale. Derive `affected_gate` from scope: 01/02 or capability-to-task mapping → GATE_1; only 03–06 → GATE_2; only review/draft 07/08 → GATE_3; mixed scope takes the earliest gate. Process 03 capability/scope changes return to Process 03. Independently validate the label against decision text and affected artifacts. The user records exactly one outcome using `APPROVE FLOW DECISION [DECISION-ID]`, `REJECT FLOW DECISION [DECISION-ID]`, or `DEFER FLOW DECISION [DECISION-ID]`, with a rationale. Append a status event; never rewrite the proposal. Only APPROVED decisions may define current flow policy. REJECTED and DEFERRED decisions remain visible and must not be treated as approved rules.

### Decision Log hash baseline

`decision_log.latest_sha256` stores the last verified SHA-256 of the current `09_DECISION_LOG.md` bytes. Populate it after initial file creation and refresh it after every append/status event. Each refresh must follow a successful file write and read-back, then update the Control File as a single-writer transaction: calculate the next sequence (`previous state_seq + 1`), set the Control File to that value, and append a `DECISION_LOG_UPDATED` event with `decision_id` (or NOT_APPLICABLE), `decision_status_after_update` (or NOT_APPLICABLE), `affected_gate`, path, `resulting_sha256`, timestamp and that same new committed `state_seq`. Read the Control File back and verify both the event and hash. Tab 01/02 alone may write the log; Tab 03 is read-only. Never store the stale pre-update sequence in the event. Gate 1 and Tab 02 require a non-null baseline and exact match with the actual file hash.

Never overwrite the expected hash merely because a later read detects a mismatch. A missing/unreadable log, wrong initiative identity, null baseline, misclassified decision or unexplained hash mismatch makes the decision state NOT_VERIFIED. Conservatively reopen Gates 1–3, invalidate the review, set lifecycle REVIEW_REQUIRED, append `INVALIDATED` with expected/observed hashes and exact reopened gates, and stop.

Recovery requires explicit user command `RECOVER DECISION LOG [DECISION-ID]`. It is allowed only when the actual bytes hash exactly equals the `resulting_sha256` of one already-persisted, well-formed `DECISION_LOG_UPDATED` event for that DEC ID/status/path/scope and its sequence is valid. Then the owning tab may set the baseline to that already-recorded hash, append `DECISION_LOG_RECOVERED` referencing the original event sequence, reopen affected gates, increment sequence and read back. If no exact event matches, do not adopt observed bytes: restore a trusted copy matching the old expected hash or stop. If the Control File event history is partial/unreadable, restore a trusted Control File copy or stop; never synthesize events.

For Tab 02 entry, require a latest `GATE_1_APPROVED` event with exact command `APPROVE TASK MODEL`; `gate_1.approved_state_seq` must equal that event sequence. No GATE_1-affecting `DECISION_LOG_UPDATED` event may occur after it. Independently classify every decision against its artifacts and semantics; if the label is wrong or ambiguous, fail closed. Once Gate 2 has been approved, any subsequent Decision Log byte change reopens Gates 2–3 because Gate 2 binds the whole file; a GATE_1 change additionally reopens Gate 1. Missing events, identity or unorderable sequences are NOT_VERIFIED.

## Residual-risk acceptance

Only MAJOR/MINOR findings may be accepted. Each requires exact user command `ACCEPT RESIDUAL RISK [FINDING-ID]` plus rationale and a record containing finding_id, severity, accepted_by, exact_command, rationale and accepted_at_local. BLOCKER/CRITICAL findings cannot be accepted. Freeze does not imply acceptance.

## Single-writer and timestamps

For every Control File change: read state_seq, verify prerequisites, write one update, increment state_seq, append an event, read back and verify. state_seq is not a lock; only one tab writes at a time. Use real Asia/Ho_Chi_Minh timestamps and lowercase SHA-256. If verification fails, stop.
