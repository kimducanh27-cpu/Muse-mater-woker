---
# SIMULATED — NOT ELIGIBLE DOWNSTREAM
process: "02-product-discovery"
initiative_id: "draft-saving-initiative"
evidence_status: "PRIMARY_EVIDENCE_PRESENT"
gate_1:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE OPPORTUNITY FOCUS"
  approved_command: "APPROVE OPPORTUNITY FOCUS"
  approved_at_local: "2026-11-13 14:00 Asia/Ho_Chi_Minh"
  decision_note: "SIMULATED: Focus on draft saving confirmed"
gate_2:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE EVIDENCE REVIEW"
  approved_command: "APPROVE EVIDENCE REVIEW"
  approved_at_local: "2026-11-13 14:15 Asia/Ho_Chi_Minh"
  decision_note: "SIMULATED: Primary interview evidence validated"
gate_3:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE EXPERIMENT PLAN"
  approved_command: "APPROVE EXPERIMENT PLAN"
  approved_at_local: "2026-11-13 14:30 Asia/Ho_Chi_Minh"
  decision_note: "SIMULATED: Experiment plan and proceed decision accepted"
experiment_execution_authorizations:
  - "AUTHORIZE EXPERIMENT EXP-01"
discovery_outcome:
  status: "FROZEN"
  freeze_command: "FREEZE DISCOVERY"
  frozen_at_local: "2026-11-13 14:45 Asia/Ho_Chi_Minh"
  decision_note: "SIMULATED: Discovery outcome frozen"
last_updated_local: "2026-11-13 14:45 Asia/Ho_Chi_Minh"
---

> SIMULATED — NOT ELIGIBLE DOWNSTREAM

# Product Discovery — Canonical Control State

This file is the single source of truth for approvals and lifecycle state for one Process 02 initiative. Copy it to product/discovery/00_DISCOVERY_CONTROL.md when starting that initiative. Do not edit this template as the live state file.

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
| 2026-11-13 13:50 | INITIALIZED | — | Initial state; all gates pending | Control file |
| 2026-11-13 14:00 | GATE_1_APPROVED | APPROVE OPPORTUNITY FOCUS | SIMULATED: Opportunity focus accepted | 01_OPPORTUNITY_MAP.md |
| 2026-11-13 14:15 | GATE_2_APPROVED | APPROVE EVIDENCE REVIEW | SIMULATED: Evidence verified | 03_EVIDENCE_REGISTER.md |
| 2026-11-13 14:30 | GATE_3_APPROVED | APPROVE EXPERIMENT PLAN | SIMULATED: Experiment plan approved | 06_EXPERIMENT_PLAN.md |
| 2026-11-13 14:45 | OUTCOME_FROZEN | FREEZE DISCOVERY | SIMULATED: Frozen discovery | 07_DISCOVERY_DECISION.md |
