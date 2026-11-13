---
# SIMULATED — NOT ELIGIBLE DOWNSTREAM
schema_version: 2
process: "03-product-definition"
initiative_id: "draft-saving-initiative"
state_seq: 3
process_02_handoff:
  route: "PROCESS_02"
  status: "SIMULATED_VERIFIED"
  source_initiative_id: "draft-saving-initiative"
  source_control: "fixtures/chain-probe/00_DISCOVERY_CONTROL.md"
  source_decision: "fixtures/chain-probe/07_DISCOVERY_DECISION.md"
  source_outcome: null
  source_gate_3_status: "SIMULATED_APPROVED"
  discovery_decision: "PROCEED"
  discovery_status: "FROZEN_OUTCOME"
  evidence_status: "PRIMARY_EVIDENCE_PRESENT"
  source_artifacts:
    - "fixtures/chain-probe/07_DISCOVERY_DECISION.md"
  handoff_verified_at_local: "2026-11-13 15:00 Asia/Ho_Chi_Minh"
residual_uncertainty_acceptance:
  accepted: true
  command: "ACCEPT RESIDUAL UNCERTAINTY"
  accepted_at_local: "2026-11-13 15:05 Asia/Ho_Chi_Minh"
  evidence_status_at_acceptance: "PRIMARY_EVIDENCE_PRESENT"
  decision_note: "SIMULATED: Accepted single-device scope limitation"
accepted_residual_risks: []
existing_product_context:
  command: null
  source_path: null
  source_sha256: null
gate_1:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE PRODUCT INTENT"
  approved_command: "APPROVE PRODUCT INTENT"
  approved_at_local: "2026-11-13 15:10 Asia/Ho_Chi_Minh"
  approved_artifacts: []
  decision_note: "SIMULATED: Product intent approved"
gate_2:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE PRODUCT SCOPE"
  approved_command: "APPROVE PRODUCT SCOPE"
  approved_at_local: "2026-11-13 15:20 Asia/Ho_Chi_Minh"
  approved_artifacts: []
  decision_note: "SIMULATED: Capability scope including CAP-01 approved"
gate_3:
  status: "SIMULATED_APPROVED"
  required_command: "FREEZE PRODUCT DEFINITION"
  approved_command: "FREEZE PRODUCT DEFINITION"
  approved_at_local: "2026-11-13 15:30 Asia/Ho_Chi_Minh"
  approved_artifacts: []
  frozen_at_local: "2026-11-13 15:30 Asia/Ho_Chi_Minh"
  frozen_artifact:
    path: "fixtures/chain-probe/PRODUCT_DEFINITION.md"
    sha256: "2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075"
  reviewed_draft:
    path: "fixtures/chain-probe/08_PRODUCT_DEFINITION_DRAFT.md"
    sha256: null
  reviewed_sources: []
  frozen_version: 1
review:
  round: 1
  status: "READY_FOR_FREEZE"
  open_blockers: 0
  open_major: 0
  open_minor: 0
  latest_review_path: "fixtures/chain-probe/07_DEFINITION_REVIEW.md"
  latest_review_sha256: null
lifecycle_status: "FROZEN"
last_updated_local: "2026-11-13 15:30 Asia/Ho_Chi_Minh"
---

# Process 03 — Canonical Product Definition Control

Copy this template to product/definition/00_PRODUCT_DEFINITION_CONTROL.md when starting one initiative. This template is not the live state.

## Allowed values

- Gate states: PENDING, APPROVED, REJECTED, REOPENED.
- Lifecycle states: DRAFT, REVIEW_REQUIRED, FROZEN.
- Handoff route: PROCESS_02, EXISTING_PRODUCT_CONTEXT.
- Handoff status: VERIFIED, NOT_VERIFIED, REOPENED.
- Evidence status: PRIMARY_EVIDENCE_PRESENT, SECONDARY_ONLY, NOT_COLLECTED, NOT_VERIFIED.
- Discovery status snapshot: FROZEN_OUTCOME, READY_FOR_TESTING, EXISTING_PRODUCT_CONTEXT, NOT_VERIFIED.
- Review status: NOT_STARTED, BLOCKERS_FOUND, READY_FOR_FREEZE.

Gate 3 status remains APPROVED after freeze. Only lifecycle_status becomes FROZEN.

## Eligibility

PROCESS_02 route:
- Process 02 Gate 3 = APPROVED.
- Opportunity decision = PROCEED or NARROW.
- Either discovery_outcome.status = FROZEN and the Outcome header agrees, or the Decision Brief says READY FOR TESTING while discovery_outcome.status is NOT_CREATED/absent and the user explicitly accepts residual uncertainty.
- PIVOT, PAUSE, STOP, DRAFT Outcome, REVIEW_REQUIRED Outcome or any source mismatch blocks entry.

## Integrity and update rules

1. Hash exact artifacts covered by an approval with SHA-256. Never use a free-text revision in place of a hash.
2. Obtain timestamps from a real local clock.
3. For every control update, read current state, verify state_seq, update once, increment state_seq, save, read back and verify.
4. Do not claim approval or freeze success until the Control File has been read back and all stored hashes match.

## Event log

| Local timestamp | state_seq | Event | Exact command | Decision / reason | Artifact paths and SHA-256 |
|---|---:|---|---|---|---|
| 2026-11-13 14:55 | 0 | INITIALIZED | — | Initial state; all gates pending | Control file |
| 2026-11-13 15:00 | 1 | HANDOFF_VERIFIED | VERIFY PROCESS 02 HANDOFF | SIMULATED: String match on P02 control | fixtures/chain-probe/07_DISCOVERY_DECISION.md |
| 2026-11-13 15:20 | 2 | GATE_2_APPROVED | APPROVE PRODUCT SCOPE | SIMULATED: Scope approved | fixtures/chain-probe/04_CAPABILITY_SCOPE.md |
| 2026-11-13 15:30 | 3 | DEFINITION_FROZEN | FREEZE PRODUCT DEFINITION | SIMULATED: Frozen Product Definition | fixtures/chain-probe/PRODUCT_DEFINITION.md: 2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075 |
