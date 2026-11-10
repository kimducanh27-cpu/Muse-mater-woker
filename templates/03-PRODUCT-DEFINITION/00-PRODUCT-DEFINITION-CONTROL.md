---
schema_version: 2
process: "03-product-definition"
initiative_id: "REPLACE_WITH_UNIQUE_SLUG"
state_seq: 0
process_02_handoff:
  route: "PROCESS_02"
  status: "NOT_VERIFIED"
  source_initiative_id: null
  source_control: "product/discovery/00_DISCOVERY_CONTROL.md"
  source_decision: "product/discovery/07_DISCOVERY_DECISION.md"
  source_outcome: null
  source_gate_3_status: "NOT_VERIFIED"
  discovery_decision: "NOT_VERIFIED"
  discovery_status: "NOT_VERIFIED"
  evidence_status: "NOT_VERIFIED"
  source_artifacts: []
  handoff_verified_at_local: null
residual_uncertainty_acceptance:
  accepted: false
  command: null
  accepted_at_local: null
  evidence_status_at_acceptance: null
  decision_note: null
existing_product_context:
  command: null
  source_path: null
  source_sha256: null
gate_1:
  status: "PENDING"
  required_command: "APPROVE PRODUCT INTENT"
  approved_command: null
  approved_at_local: null
  approved_artifacts: []
  decision_note: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE PRODUCT SCOPE"
  approved_command: null
  approved_at_local: null
  approved_artifacts: []
  decision_note: null
gate_3:
  status: "PENDING"
  required_command: "FREEZE PRODUCT DEFINITION"
  approved_command: null
  approved_at_local: null
  approved_artifacts: []
  frozen_at_local: null
  frozen_artifact:
    path: null
    sha256: null
  reviewed_draft:
    path: "product/definition/08_PRODUCT_DEFINITION_DRAFT.md"
    sha256: null
  reviewed_sources: []
  frozen_version: 0
review:
  round: 0
  status: "NOT_STARTED"
  open_blockers: 0
  open_major: 0
  open_minor: 0
  latest_review_path: "product/definition/07_DEFINITION_REVIEW.md"
  latest_review_sha256: null
lifecycle_status: "DRAFT"
last_updated_local: "NOT_VERIFIED"
---

# Process 03 — Canonical Product Definition Control

Copy this template to product/definition/00_PRODUCT_DEFINITION_CONTROL.md when starting one initiative. This template is not the live state.

## Allowed values

- Gate states: PENDING, APPROVED, REJECTED, REOPENED.
- Lifecycle states: DRAFT, REVIEW_REQUIRED, FROZEN.
- Handoff route: PROCESS_02, EXISTING_PRODUCT_CONTEXT.
- Handoff status: VERIFIED, NOT_VERIFIED, REOPENED.
- Evidence status: PRIMARY_EVIDENCE_PRESENT, SECONDARY_ONLY, NOT_COLLECTED, NOT_VERIFIED.
- Review status: NOT_STARTED, BLOCKERS_FOUND, READY_FOR_FREEZE.

Gate 3 status remains APPROVED after freeze. Only lifecycle_status becomes FROZEN.

## Eligibility

PROCESS_02 route:
- Process 02 Gate 3 = APPROVED.
- Opportunity decision = PROCEED or NARROW.
- Either discovery_outcome.status = FROZEN and the Outcome header agrees, or the Decision Brief says READY FOR TESTING while discovery_outcome.status is NOT_CREATED/absent and the user explicitly accepts residual uncertainty.
- PIVOT, PAUSE, STOP, DRAFT Outcome, REVIEW_REQUIRED Outcome or any source mismatch blocks entry.

EXISTING_PRODUCT_CONTEXT route:
- The user must issue USE EXISTING PRODUCT CONTEXT.
- Record a readable source-context path and SHA-256.
- Do not represent this route as a completed Process 02 handoff.

## Integrity and update rules

1. Hash exact artifacts covered by an approval with SHA-256. Never use a free-text revision in place of a hash.
2. Obtain timestamps from a real local clock. On Windows use PowerShell with the SE Asia Standard Time zone. If unavailable, record NOT_VERIFIED and do not approve/freeze.
3. For every control update, read current state, verify state_seq, update once, increment state_seq, save, read back and verify. state_seq detects stale reads; it is not a file lock. Only one tab writes this file at a time.
4. Do not claim approval or freeze success until the Control File has been read back and all stored hashes match.
5. If a write or read-back fails, report INCOMPLETE and stop. Do not infer or repair state by guessing.
6. Do not overwrite another initiative's control file. Use one initiative per workspace or a separate initiative path.
7. Preserve an append-only event log. Log approvals, rejections, revision requests, invalidations, risk acceptances, review rounds and freezes.
8. A non-approval revision request is REVISION_REQUESTED. Only exact rejection commands set REJECTED.
9. Recompute Process 02 hashes at Tab 02, Tab 03 and before freeze. A mismatch makes the handoff NOT_VERIFIED and reopens dependent gates.
10. Recompute approved Process 03 artifact hashes at every downstream tab entry and before freeze.

## Invalidation matrix

| Changed artifact | Gates reopened |
|---|---|
| Material Process 02 input | Gates 1–3; handoff NOT_VERIFIED |
| 01_PRODUCT_INTENT.md or 02_POSITIONING.md | Gates 1–3 |
| 03_PRODUCT_SHAPE.md, 04_CAPABILITY_SCOPE.md, 05_SUCCESS_MEASURES.md, 06_DECISION_LOG.md | Gates 2–3 |
| 07_DEFINITION_REVIEW.md or 08_PRODUCT_DEFINITION_DRAFT.md | Gate 3 |
| PRODUCT_DEFINITION.md | Gate 3; lifecycle REVIEW_REQUIRED |

Reopening Gate 1 also reopens Gates 2 and 3. Reopening Gate 2 also reopens Gate 3. Any material source change after freeze sets lifecycle_status to REVIEW_REQUIRED.

## Event log

Append new rows; do not delete or rewrite prior events.

| Local timestamp | state_seq | Event | Exact command | Decision / reason | Artifact paths and SHA-256 |
|---|---:|---|---|---|---|
| NOT_VERIFIED | 0 | INITIALIZED | — | All gates pending | Control template |
