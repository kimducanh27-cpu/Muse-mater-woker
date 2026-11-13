---
# SIMULATED — NOT ELIGIBLE DOWNSTREAM
schema_version: 4
process: "04-app-flow"
initiative_id: "draft-saving-initiative"
state_seq: 3
created_at_local: "2026-11-13 15:35 Asia/Ho_Chi_Minh"
last_updated_local: "2026-11-13 16:00 Asia/Ho_Chi_Minh"
source_process_03:
  control_path: "fixtures/chain-probe/00_PRODUCT_DEFINITION_CONTROL.md"
  initiative_id: "draft-saving-initiative"
  gate_3_status: "SIMULATED_APPROVED"
  lifecycle_status: "FROZEN"
  frozen_artifact_path: "fixtures/chain-probe/PRODUCT_DEFINITION.md"
  frozen_artifact_sha256: "2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075"
  verified_file_sha256: "2e6b6c6d5e398fb3fb630606842f56d06b337e0721535fdb5338ef17b88fc075"
  status: "SIMULATED_VERIFIED"
  verified_at_local: "2026-11-13 15:35 Asia/Ho_Chi_Minh"
gate_1:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE TASK MODEL"
  approved_command: "APPROVE TASK MODEL"
  approved_at_local: "2026-11-13 15:40 Asia/Ho_Chi_Minh"
  approved_state_seq: 1
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: "SIMULATED: Task model approved"
gate_2:
  status: "SIMULATED_APPROVED"
  required_command: "APPROVE APP FLOW"
  approved_command: "APPROVE APP FLOW"
  approved_at_local: "2026-11-13 15:50 Asia/Ho_Chi_Minh"
  approved_state_seq: 2
  decision_log_sha256: null
  approved_artifacts: []
  decision_note: "SIMULATED: Screen inventory approved"
gate_3:
  status: "SIMULATED_APPROVED"
  required_command: "FREEZE APP FLOW"
  approved_command: "FREEZE APP FLOW"
  approved_at_local: "2026-11-13 16:00 Asia/Ho_Chi_Minh"
  approved_state_seq: 3
  frozen_at_local: "2026-11-13 16:00 Asia/Ho_Chi_Minh"
  approved_artifacts: []
  reviewed_draft:
    path: "fixtures/chain-probe/08_APP_FLOW_DRAFT.md"
    sha256: null
  frozen_artifact:
    path: "fixtures/chain-probe/04_SCREEN_INVENTORY.md"
    sha256: "5379b4799753ee50f7af4953c6fcfe54493fc8d6e8ee42830c0f7c6d72fe40f6"
  frozen_version: 1
  archived_versions: []
review:
  round: 1
  status: "READY_FOR_FREEZE"
  open_blockers: 0
  open_critical: 0
  open_major: 0
  open_minor: 0
  latest_review_path: "fixtures/chain-probe/07_FLOW_REVIEW.md"
  latest_review_sha256: null
  reviewed_draft_path: "fixtures/chain-probe/08_APP_FLOW_DRAFT.md"
  reviewed_draft_sha256: null
  reviewed_artifacts: []
decision_log:
  path: "fixtures/chain-probe/09_DECISION_LOG.md"
  latest_sha256: null
change_request_register:
  path: "fixtures/chain-probe/10_CHANGE_REQUEST_REGISTER.md"
  schema_version: 1
  last_verified_sha256: null
  last_register_seq: 0
  last_event_id: null
accepted_residual_risks: []
event_log: []
lifecycle_status: "FROZEN"
timezone: "Asia/Ho_Chi_Minh"
---

# Process 04 — Canonical App Flow Control (Schema v4)

This is a simulated control file for Process 04.
