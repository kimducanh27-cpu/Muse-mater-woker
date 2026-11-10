---
schema_version: 2
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
  approved_artifacts: []
  decision_note: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE APP FLOW"
  approved_command: null
  approved_at_local: null
  approved_artifacts: []
  decision_note: null
gate_3:
  status: "PENDING"
  required_command: "FREEZE APP FLOW"
  approved_command: null
  approved_at_local: null
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

Copy this template to \`product/app-flow/00_APP_FLOW_CONTROL.md\` for one initiative. This template is not the live state. Replace the initiative placeholder only after verifying the Process 03 initiative.

## Allowed values

- Gate states: \`PENDING\`, \`APPROVED\`, \`REJECTED\`, \`REOPENED\`.
- Lifecycle states: \`DRAFT\`, \`REVIEW_REQUIRED\`, \`FROZEN\`, \`ABANDONED\`.
- Process 03 source status: \`VERIFIED\`, \`NOT_VERIFIED\`, \`REOPENED\`.
- Review status: \`NOT_STARTED\`, \`BLOCKERS_FOUND\`, \`READY_FOR_FREEZE\`.
- Finding severity: \`BLOCKER\`, \`CRITICAL\`, \`MAJOR\`, \`MINOR\`.
- Finding status: \`OPEN\`, \`RESOLVED\`, \`ACCEPTED_BY_USER\`.

Gate 3 remains APPROVED after a successful freeze; lifecycle_status becomes FROZEN. Do not set a gate to FROZEN.

## Entry eligibility and source binding

Set Process 04 \`initiative_id\` and \`source_process_03.initiative_id\` equal to the Process 03 Control File's \`initiative_id\`.

Before setting source status VERIFIED:
- Process 03 \`gate_3.status = APPROVED\`.
- Process 03 \`lifecycle_status = FROZEN\`.
- Process 03 \`gate_3.frozen_artifact.path = product/definition/PRODUCT_DEFINITION.md\`.
- Actual Product Definition SHA-256 equals Process 03 \`gate_3.frozen_artifact.sha256\`.
- Both Control Files are readable and no conflicting initiative is present.

The authoritative comparison target is Process 03 \`gate_3.frozen_artifact.sha256\`, not a cached Process 04 hash. Store expected source hash and independently computed current file hash separately; both must match.

## Gate rules

- Gate 1 binds exact SHA-256 values for \`01_TASK_MODEL.md\` and \`02_FLOW_ARCHITECTURE.md\`. It requires source status VERIFIED, complete template structure, full capability coverage or user-approved deferral, and no unresolved policy decision being treated as settled.
- Gate 2 binds exact SHA-256 values for \`03_NAVIGATION_MODEL.md\`, \`04_SCREEN_INVENTORY.md\`, \`05_FLOW_SPECIFICATION.md\`, \`06_STATE_AND_EXCEPTION_MATRIX.md\`, and current \`09_DECISION_LOG.md\`. It requires Gate 1 and every Gate 1 artifact hash to remain valid.
- Gate 3 requires Gate 1 and Gate 2 APPROVED with matching hashes; at least one append-only review round; latest review and draft hashes matching the Control File; zero open BLOCKER, CRITICAL, MAJOR and MINOR findings; user-originated acceptance records for accepted risks; decision log reviewed; and the exact reviewed draft frozen by status-line substitution only.
- No missing review is equivalent to a clean review. \`review.round\` must be at least 1 and the latest review artifact must exist and hash-match.
- A hash proves identity/integrity of bytes, not correctness of content. Completeness, template conformance and graph/traceability checks need explicit evidence.

## Append-only event and review records

Append objects to \`event_log\`; never delete or rewrite prior events. Record approvals, rejections, revision requests, invalidations, decision approvals, risk acceptances, review rounds, freezes, archives and abandonment. Each event should include local timestamp, state_seq, event type, exact user command (or NOT_APPLICABLE), reason, changed paths and relevant hashes.

The review history \`07_FLOW_REVIEW.md\` is append-only. Every round records source/artifact/draft hashes, verdict, status, finding counts and set/graph evidence.

## Invalidation matrix

| Changed file/source | Reopen |
|---|---|
| Process 03 Control File or frozen Product Definition | source REOPENED; Gates 1–3; lifecycle REVIEW_REQUIRED |
| \`01_TASK_MODEL.md\` or \`02_FLOW_ARCHITECTURE.md\` | Gates 1–3 |
| \`03_NAVIGATION_MODEL.md\`, \`04_SCREEN_INVENTORY.md\`, \`05_FLOW_SPECIFICATION.md\`, \`06_STATE_AND_EXCEPTION_MATRIX.md\` | Gates 2–3 |
| \`07_FLOW_REVIEW.md\` or \`08_APP_FLOW_DRAFT.md\` | Gate 3; new review round required |
| \`09_DECISION_LOG.md\` | Earliest gate named by appended decision's \`affected_gate\`, plus all downstream gates |
| \`APP_FLOW.md\` after freeze | Gate 3; lifecycle REVIEW_REQUIRED; downstream use prohibited |

Reopening Gate 1 reopens Gates 2 and 3. Reopening Gate 2 reopens Gate 3. Any material change after freeze sets lifecycle_status to REVIEW_REQUIRED. Record every invalidation as an append-only event; never silently overwrite an approval.

## Re-freeze and archive

Before re-freezing, verify current \`APP_FLOW.md\` against the Control File's frozen hash. Preserve the previous canonical artifact as \`APP_FLOW.v<N>.md\`, where N is the previous \`frozen_version\`. Never overwrite an archive. Record its path/hash and increment the version only after the new canonical artifact and Control File both pass read-back.

## Failure handling

If canonical output writes but Control File write/read-back fails, report \`INCOMPLETE — NOT FROZEN\`. An orphan \`APP_FLOW.md\` is not eligible downstream. The only eligible output is one whose bytes hash-match \`gate_3.frozen_artifact.sha256\` while Gate 3 is APPROVED and lifecycle is FROZEN.

If an artifact or Control File cannot be read, hashed or written, stop with NOT_VERIFIED. Never guess, synthesize a hash or claim a gate/freeze succeeded.

## Decision log

\`09_DECISION_LOG.md\` is append-only. Each material flow-policy decision has a stable DEC ID, affected artifacts, affected gate, alternatives, rationale and user approval. A proposal is not an approved decision. The exact command \`APPROVE FLOW DECISION [DECISION-ID]\` is required before a proposal is treated as an approved rule.

## Residual-risk acceptance

Only MAJOR/MINOR findings may be accepted. Each requires exact user command \`ACCEPT RESIDUAL RISK [FINDING-ID]\` plus rationale and a record containing finding_id, severity, accepted_by, exact_command, rationale and accepted_at_local. BLOCKER/CRITICAL findings cannot be accepted. Freeze does not imply acceptance.

## Single-writer and timestamps

For every Control File change: read state_seq, verify prerequisites, write one update, increment state_seq, append an event, read back and verify. state_seq is not a lock; only one tab writes at a time. Use real Asia/Ho_Chi_Minh timestamps and lowercase SHA-256. If verification fails, stop.
