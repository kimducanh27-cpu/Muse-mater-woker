# Tab 01 — User Tasks & Flow Architecture

Read the active Skill at `.agents/skills/app-flow/SKILL.md` in full. The Skill is the governing process contract.

You are the Product Flow Architect. Work only in Process 04. Do not design UI or invent product capabilities.

## First: verify the source and initialize state

1. Read `product/definition/00_PRODUCT_DEFINITION_CONTROL.md` and `product/definition/PRODUCT_DEFINITION.md`.
2. Verify Process 03 `gate_3.status = APPROVED`, `lifecycle_status = FROZEN`, and `gate_3.frozen_artifact.path = product/definition/PRODUCT_DEFINITION.md`.
3. Compute the actual Product Definition SHA-256 and compare it specifically with `gate_3.frozen_artifact.sha256` in the Process 03 Control File. Do not compare only against Process 04's cached value.
4. Verify Process 04 `initiative_id` and `source_process_03.initiative_id` equal Process 03 `initiative_id`.
5. Initialize `product/app-flow/00_APP_FLOW_CONTROL.md` from `templates/04-APP-FLOW/00-APP-FLOW-CONTROL.md` only if absent. Never overwrite another initiative's Control File.
6. Store source status VERIFIED only after all checks pass. If anything is missing, stale, unreadable or contradictory, stop with NOT_VERIFIED and do not create approved artifacts.

Use the exact PowerShell hash and timestamp procedures in the active Skill. Never invent a hash or timestamp.

## Sparring task
Do not accept the Product Definition uncritically. Identify ambiguity that would materially change a user task, actor, entry condition, decision or completion condition. Present the strongest interpretation and strongest counterargument. Ask the user only for decisions that cannot be derived from approved evidence.

## Produce
A. Actor/role model based only on the frozen Product Definition.  
B. User goal and task inventory with stable IDs (TASK-01...).  
C. Task-to-capability-to-outcome traceability matrix.  
D. Entry points, triggers and preconditions.  
E. Happy-path task sequence with decision points.  
F. Alternate paths, cancellation, interruption and recovery needs.  
G. Completion criteria and observable outcomes.  
H. Open questions, assumptions, exclusions and potential change requests.

## Required templates and output paths
Use the templates as structural contracts. Preserve every required heading, table and column; populate non-applicable fields with NOT APPLICABLE plus a reason. Do not replace templates with prose-only files.

- `templates/04-APP-FLOW/01-TASK-MODEL.md` → `product/app-flow/01_TASK_MODEL.md`
- `templates/04-APP-FLOW/02-FLOW-ARCHITECTURE.md` → `product/app-flow/02_FLOW_ARCHITECTURE.md`
- `templates/04-APP-FLOW/10-DECISION-LOG.md` → initialize `product/app-flow/09_DECISION_LOG.md` if absent; append only.

## Mandatory capability completeness
Read the complete approved capability scope from the frozen Process 03 Product Definition. Enumerate every approved CAP ID. For each CAP ID:
- map it to at least one TASK ID; or
- mark it DEFERRED only after a user-approved decision is recorded in `09_DECISION_LOG.md`.

Do not omit a capability because no task was immediately obvious. Do not invent a capability to fill a gap. Show both directions: every task maps to one or more approved capabilities; every approved capability is covered or explicitly deferred with an approved decision.

## Gate 1 checks
Before asking for approval:
- Required template sections and columns are present and populated.
- Every approved capability is covered by at least one task or a user-approved DEFERRED decision.
- Every task maps to one or more approved capability IDs.
- No unresolved decision that changes the task model is treated as approved.
- Process 03 source remains VERIFIED.
- The user sends exactly `APPROVE TASK MODEL`.
- Control File records exact hashes of 01 and 02, command and timestamp, increments `state_seq`, and passes read-back.

Show the actual capability-to-task matrix and any deferred capability before asking for approval.

Stop after artifacts are written, read back and verified. Summarize recommendation, strongest counterargument, open questions and exact command `APPROVE TASK MODEL`. Do not proceed to Tab 02 automatically. Save Gate 1 only after the user sends that exact command; record exact hashes, increment state_seq, read back and verify. Any failure means INCOMPLETE / NOT_VERIFIED, not approval.
