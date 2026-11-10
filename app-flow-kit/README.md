# Process 04 — App Flow Kit

Process 04 follows Product Definition and precedes UX/UI design. It translates the frozen product contract into user tasks, navigation, functional screen nodes, transitions, states and recovery paths.

**It defines how users move through the product functionally. It does not define visual UI or implementation.**

## Three independent Antigravity tabs
1. User Tasks & Flow Architecture — prompts/04-APP-FLOW/01-TASK-MODEL.md
2. Navigation & Screen Flow Specification — prompts/04-APP-FLOW/02-NAVIGATION-FLOW.md
3. Independent Flow Review — prompts/04-APP-FLOW/03-INDEPENDENT-REVIEW.md

Active Skill: .agents/skills/app-flow/SKILL.md

## Input contract
Require product/definition/00_PRODUCT_DEFINITION_CONTROL.md and product/definition/PRODUCT_DEFINITION.md. Gate 3 must be APPROVED, lifecycle_status FROZEN and the Product Definition SHA-256 must match. If not verifiable, stop.

## Outputs
Canonical state: product/app-flow/00_APP_FLOW_CONTROL.md
Working artifacts: 01_TASK_MODEL.md through 08_APP_FLOW_DRAFT.md
Frozen output: product/app-flow/APP_FLOW.md (based on templates/04-APP-FLOW/09-APP-FLOW.md)

## Human gates
| Tab | Gate | Exact command |
|---|---|---|
| 01 | Task model approved | APPROVE TASK MODEL |
| 02 | App flow approved | APPROVE APP FLOW |
| 03 | Freeze | FREEZE APP FLOW |

No automatic handoff. Each tab runs in a fresh conversation and reads persisted workspace artifacts.

## Boundaries
Do not create wireframes, visual layouts, colors, typography, design systems, polished UI mockups, APIs, database schemas, implementation plans or code. Screen inventory is functional, not visual. Any new capability or scope expansion returns to Process 03 for a product change decision.

## Freeze requirements
Source and gate hashes must match; review must have no unresolved BLOCKER/CRITICAL findings; MAJOR/MINOR findings must be fixed or explicitly accepted by the user; graph and traceability checks must pass; frozen output must be hashed and read back.

Live Antigravity runtime behavior is not verified by this repository-only setup. Run the verification checklist in the actual workspace before production use.
