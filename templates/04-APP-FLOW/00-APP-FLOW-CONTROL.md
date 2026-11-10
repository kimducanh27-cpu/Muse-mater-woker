# Process 04 — App Flow Control File

> One initiative per workspace. This file is the canonical state record. Do not overwrite an existing initiative.

## Identity
- schema_version: 1
- initiative_id:
- process: 04_APP_FLOW
- lifecycle_status: DRAFT
- state_seq: 0
- created_at_local:
- updated_at_local:
- timezone: Asia/Ho_Chi_Minh

## Process 03 source
- source_control_path: product/definition/00_PRODUCT_DEFINITION_CONTROL.md
- source_initiative_id:
- source_lifecycle_status:
- source_gate_3_status:
- product_definition_path: product/definition/PRODUCT_DEFINITION.md
- product_definition_sha256:
- source_verified_at_local:
- source_status: NOT_VERIFIED

## Gates
- gate_1_task_model: NOT_STARTED
- gate_1_command:
- gate_1_approved_at_local:
- gate_1_artifacts: []
- gate_2_app_flow: NOT_STARTED
- gate_2_command:
- gate_2_approved_at_local:
- gate_2_artifacts: []
- gate_3_freeze: NOT_STARTED
- gate_3_command:
- gate_3_approved_at_local:
- gate_3_artifacts: []

## Artifact hashes
- 01_TASK_MODEL.md:
- 02_FLOW_ARCHITECTURE.md:
- 03_NAVIGATION_MODEL.md:
- 04_SCREEN_INVENTORY.md:
- 05_FLOW_SPECIFICATION.md:
- 06_STATE_AND_EXCEPTION_MATRIX.md:
- 07_FLOW_REVIEW.md:
- 08_APP_FLOW_DRAFT.md:
- APP_FLOW.md:

## Review and accepted residual risks
- review_round: 0
- unresolved_blockers: []
- accepted_residual_risks: []
- change_requests: []
- invalidation_events: []

## State rules
- Gate 1 approval binds exact hashes of artifacts 01–02.
- Gate 2 approval binds exact hashes of artifacts 03–06 and requires Gate 1 still valid.
- Any changed artifact invalidates its gate and all downstream approvals/review.
- Gate 3 requires Gate 1 and Gate 2 APPROVED, no unresolved BLOCKER/CRITICAL, all MAJOR/MINOR fixed or explicitly accepted by user, source hash unchanged, and APP_FLOW.md hash read back.
- state_seq is a stale-read detector, not a lock. Only one tab writes this file at a time.
- Never invent timestamps or hashes. If read/hash/write/read-back fails, mark NOT_VERIFIED and stop.
