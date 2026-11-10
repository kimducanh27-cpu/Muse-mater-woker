# Product Discovery — Canonical Control State

This file is the single source of truth for approvals and lifecycle state for one Process 02 initiative. Copy it to product/discovery/00_DISCOVERY_CONTROL.md when starting that initiative. Do not edit this template as the live state file.

---
process: "02-product-discovery"
initiative_id: "REPLACE_WITH_UNIQUE_SLUG"
evidence_status: "NOT_COLLECTED"
gate_1:
  status: "PENDING"
  required_command: "APPROVE OPPORTUNITY FOCUS"
  approved_command: null
  approved_at_local: null
  decision_note: null
gate_2:
  status: "PENDING"
  required_command: "APPROVE EVIDENCE REVIEW"
  approved_command: null
  approved_at_local: null
  decision_note: null
gate_3:
  status: "PENDING"
  required_command: "APPROVE EXPERIMENT PLAN"
  approved_command: null
  approved_at_local: null
  decision_note: null
experiment_execution_authorizations: []
discovery_outcome:
  status: "NOT_CREATED"
  freeze_command: "FREEZE DISCOVERY"
  frozen_at_local: null
  decision_note: null
last_updated_local: "YYYY-MM-DD HH:mm Asia/Ho_Chi_Minh"
---

## State rules

Allowed gate states: PENDING, APPROVED, REJECTED, REOPENED.

Allowed evidence states:
- PRIMARY_EVIDENCE_PRESENT — inspected first-hand customer behavior/interviews or first-party product analytics exist.
- SECONDARY_ONLY — only secondary/desk research exists.
- NOT_COLLECTED — no usable evidence has been supplied or collected.

Allowed Outcome states: NOT_CREATED, DRAFT, FROZEN, REVIEW_REQUIRED.

Approval commands:
- Gate 1: APPROVE OPPORTUNITY FOCUS
- Gate 2: APPROVE EVIDENCE REVIEW
- Gate 3: APPROVE EXPERIMENT PLAN
- Experiment execution: AUTHORIZE EXPERIMENT [ID] (one explicit authorization per experiment)
- Outcome freeze: FREEZE DISCOVERY

Gate 3 approval is approval of the experiment plan only. It is not permission to execute an experiment.

## Mandatory update rules

1. Update this file immediately after the user issues an exact approval/authorization command. Record the command, decision and local timestamp. Do not claim success if the file could not be saved.
2. Never infer approval from silence, praise, ambiguous wording or AI recommendation.
3. If the discovery brief or opportunity map changes, set Gates 1–3 to REOPENED.
4. If the evidence register, interview synthesis or assumption map changes, set Gates 2–3 to REOPENED.
5. If the experiment plan changes, set Gate 3 to REOPENED.
6. If a material upstream artifact changes after Outcome freeze, set Outcome to REVIEW_REQUIRED and explain why. Preserve the old decision in the log.
7. Do not reset or delete the approval history. Add a new row explaining every approval, rejection, reopening, execution authorization or freeze.
8. If the file belongs to another initiative, do not overwrite it. Use a separate initiative directory/control file.

## Approval and change log

| Local timestamp (Asia/Ho_Chi_Minh) | Event | Exact command | Decision / reason | Artifact(s) affected |
|---|---|---|---|---|
| YYYY-MM-DD HH:mm | INITIALIZED | — | Initial state; all gates pending | Control file |
