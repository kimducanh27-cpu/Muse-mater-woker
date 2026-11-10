# Process 04 — App Flow Kit

Process 04 follows Product Definition. It translates the frozen product contract into user tasks, navigation, functional screen nodes, transitions, states and recovery paths.

**It defines functional user journeys and navigation. It does not define visual UI or implementation.**

## Three independent Antigravity tabs
1. **Tab 01 — User Tasks & Flow Architecture:** `prompts/04-APP-FLOW/01-TASK-MODEL.md`
2. **Tab 02 — Navigation & Screen Flow Specification:** `prompts/04-APP-FLOW/02-NAVIGATION-FLOW.md`
3. **Tab 03 — Independent Flow Review and authorized freeze:** `prompts/04-APP-FLOW/03-INDEPENDENT-REVIEW.md`

Active Skill: `.agents/skills/app-flow/SKILL.md`

All paths are repository-root-relative. Do not confuse this Process 04 review prompt with `prompts/03-TAB-INDEPENDENT-REVIEW.md` or another process's similarly named prompt.

## Input contract
Require:
- `product/definition/00_PRODUCT_DEFINITION_CONTROL.md`
- `product/definition/PRODUCT_DEFINITION.md`

Process 03 Gate 3 must be APPROVED, lifecycle_status FROZEN, initiative IDs must match, and actual Product Definition SHA-256 must equal Process 03 Control File `gate_3.frozen_artifact.sha256`. A missing, stale or unreadable source blocks entry.

## Outputs
Canonical state: `product/app-flow/00_APP_FLOW_CONTROL.md`

Working artifacts:
- 01_TASK_MODEL.md
- 02_FLOW_ARCHITECTURE.md
- 03_NAVIGATION_MODEL.md
- 04_SCREEN_INVENTORY.md
- 05_FLOW_SPECIFICATION.md
- 06_STATE_AND_EXCEPTION_MATRIX.md
- 07_FLOW_REVIEW.md (append-only rounds)
- 08_APP_FLOW_DRAFT.md (complete reviewed candidate, not a summary)
- 09_DECISION_LOG.md (append-only, user-approved decisions)

Frozen output: `product/app-flow/APP_FLOW.md`  
Frozen-output schema: `templates/04-APP-FLOW/09-APP-FLOW.md`  
Decision-log template: `templates/04-APP-FLOW/10-DECISION-LOG.md`

Template numbering is local to the template directory and is not the working-artifact number. In particular, template `10-DECISION-LOG.md` initializes working file `09_DECISION_LOG.md`; template `08-APP-FLOW-DRAFT.md` initializes working file `08_APP_FLOW_DRAFT.md`; template `09-APP-FLOW.md` is the frozen-output schema.

## Human gates
| Tab | Gate | Exact command |
|---|---|---|
| 01 | Task model approved | `APPROVE TASK MODEL` |
| 02 | App flow approved | `APPROVE APP FLOW` |
| 03 | Review completed; freeze only after all preconditions pass | `FREEZE APP FLOW` |

Additional exact commands:
- `APPROVE FLOW DECISION [DECISION-ID]`
- `REJECT FLOW DECISION [DECISION-ID]`
- `DEFER FLOW DECISION [DECISION-ID]`
- `ACCEPT RESIDUAL RISK [FINDING-ID]` (MAJOR/MINOR only, with rationale)
- `REJECT TASK MODEL` / `REJECT APP FLOW`
- `REQUEST APP FLOW CHANGE [description]`
- `ABANDON APP FLOW`

Tab 03 must not freeze automatically after a GO verdict. The user must issue the separate exact freeze command. Tab 03 is read-only on Decision Log 09; decision outcomes must return to their owning writer tab. Gate approvals/freeze require canonical event types and matching `approved_state_seq` values. No automatic handoff; each tab runs in a fresh conversation and reads persisted workspace artifacts.

## Decision Log integrity

The Decision Log identity header must match the initiative ID in both Process 03 and Process 04 Control Files. Gate 1/2/3 approvals are append-only typed events (`GATE_1_APPROVED`, `GATE_2_APPROVED`, `GATE_3_FROZEN`) with required hashes and committed sequence numbers. Any Decision Log byte change after Gate 2 approval reopens Gates 2–3 because Gate 2 binds the whole file. See the governing Skill and Control template for classification and bounded recovery rules.

## Freeze integrity
The reviewed draft 08 is the complete canonical content candidate. Freeze copies it byte-for-byte to APP_FLOW.md and changes only the exact status line from REVIEWED CANDIDATE — NOT FROZEN to FROZEN. It does not rebuild or re-summarize content.

Before freeze, require Gate 1 and Gate 2 hashes, at least one append-only review round, matching review/draft hashes, zero open findings and user-originated acceptance records for accepted MAJOR/MINOR risks. The final SHA-256 is stored in the Control File, not inside APP_FLOW.md (avoids a self-referential hash).

Before re-freezing, archive the prior verified canonical output as APP_FLOW.v<N>.md. If canonical write succeeds but Control File write/read-back fails, report INCOMPLETE — NOT FROZEN. An orphan APP_FLOW.md is not eligible downstream.

## Boundaries
Do not create wireframes, visual layouts, colors, typography, design systems, polished UI mockups, APIs, database schemas, implementation plans or code. Screen inventory is functional, not visual. Any new capability or scope expansion returns to Process 03 for a product change decision.

## Verification status
This checklist distinguishes repository/paper verification from live Antigravity runtime verification. Do not label Process 04 production-ready until live tests in the actual Windows workspace have evidence.
