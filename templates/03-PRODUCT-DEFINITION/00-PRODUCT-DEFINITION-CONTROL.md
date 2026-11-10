# Process 03 — Canonical Product Definition Control

Copy this template to product/definition/00_PRODUCT_DEFINITION_CONTROL.md when starting a new initiative. This template itself is not the live state.

---
process: "03-product-definition"
initiative_id: "REPLACE_WITH_UNIQUE_SLUG"
process_02_handoff:
  source_control: "product/discovery/00_DISCOVERY_CONTROL.md"
  source_decision: "product/discovery/07_DISCOVERY_DECISION.md"
  source_outcome: null
  source_gate_3_status: "NOT_VERIFIED"
  discovery_status: "NOT_VERIFIED"
  evidence_status: "NOT_VERIFIED"
  accepted_residual_uncertainty: false
gate_1:
  status: "PENDING"
  required_command: "APPROVE PRODUCT INTENT"
  approved_command: null
  approved_at_local: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE PRODUCT SCOPE"
  approved_command: null
  approved_at_local: null
gate_3:
  status: "PENDING"
  required_command: "FREEZE PRODUCT DEFINITION"
  approved_command: null
  frozen_at_local: null
lifecycle_status: "DRAFT"
last_updated_local: "YYYY-MM-DD HH:mm Asia/Ho_Chi_Minh"
---

## State rules
Gate states: PENDING, APPROVED, REJECTED, REOPENED.
Lifecycle states: DRAFT, REVIEW_REQUIRED, FROZEN.

Eligible Process 02 input:
- Process 02 Gate 3 = APPROVED; and
- either its Discovery Outcome is FROZEN, or its Decision Brief is READY FOR TESTING and the user explicitly accepts residual uncertainty.

If source control cannot be verified, set the source field to NOT_VERIFIED and stop.

## Mandatory update rules
1. Save exact user commands, decisions and local timestamps before reporting a gate passed.
2. Never infer approval from silence, praise, AI recommendation or chat history.
3. Changes to Product Intent or Positioning reopen Gates 1 and 2 and require a fresh review.
4. Changes to Product Shape, Capability Scope, Success Measures or Decision Log reopen Gate 2 and require a fresh review.
5. Material Process 02 input changes reopen Gates 1 and 2; set draft lifecycle REVIEW_REQUIRED.
6. Changes to PRODUCT_DEFINITION.md after freeze set lifecycle REVIEW_REQUIRED until re-reviewed and re-frozen.
7. Preserve old decisions and artifact revisions in the log.
8. Never overwrite a control file from another initiative.

## Approval and change log
| Local timestamp (Asia/Ho_Chi_Minh) | Event | Exact command | Decision / reason | Artifact revision |
|---|---|---|---|---|
| YYYY-MM-DD HH:mm | INITIALIZED | — | All gates pending; Process 02 handoff recorded | Control file |
