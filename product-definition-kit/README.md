# Process 03 — Product Definition Kit

Process 03 follows Product Discovery and precedes App Flow. It turns an eligible discovery decision into a clear definition: target segment, customer outcome, value proposition, product concept, principles, capability-level scope, success measures and non-goals.

**It defines WHAT product is intended and WHY. It does not define HOW users navigate or how engineers implement it.**

## Position in the seven-process workflow
1. The Seed — idea/problem seed.
2. Product Discovery — opportunities, customer evidence, assumptions and experiments.
3. Product Definition — product intent, positioning, product shape and scope.
4. App Flow — navigation and user/task flows.
5–7. Later process contracts are not yet specified here. Do not infer them from numbering.

## Architecture: one active Skill, three independent tabs

Active Skill:
- .agents/skills/product-definition/SKILL.md

Tabs:
1. Tab 01 — Product Intent & Positioning: ../prompts/03-PRODUCT-DEFINITION/01-PRODUCT-INTENT.md
2. Tab 02 — Product Shape & Scope: ../prompts/03-PRODUCT-DEFINITION/02-PRODUCT-SHAPE-SCOPE.md
3. Tab 03 — Independent Definition Review: ../prompts/03-PRODUCT-DEFINITION/03-INDEPENDENT-REVIEW.md

Each tab is a fresh Antigravity conversation in the same workspace. Transfer work through files, not chat history. No automatic handoff.

## Inputs and entry criteria

Preferred Process 02 inputs:
- product/discovery/00_DISCOVERY_CONTROL.md
- product/discovery/07_DISCOVERY_DECISION.md
- product/discovery/08_DISCOVERY_OUTCOME.md, if frozen
- Discovery Brief, Opportunity Map, Evidence Register, Assumption Map and source material cited by the decision/outcome.

Eligibility requires Process 02 Gate 3 APPROVED and either:
- a frozen Discovery Outcome; or
- an approved Decision Brief in READY FOR TESTING state, plus the user's explicit acceptance of residual uncertainty.

If source control state cannot be verified, stop. Existing products may use documented existing-product context only when the user explicitly selects that route.

## Canonical state and human gates

Every initiative has product/definition/00_PRODUCT_DEFINITION_CONTROL.md, copied from templates/03-PRODUCT-DEFINITION/00-PRODUCT-DEFINITION-CONTROL.md.

| Tab | Output | Gate |
|---|---|---|
| 01 Product Intent & Positioning | 01_PRODUCT_INTENT.md, 02_POSITIONING.md | APPROVE PRODUCT INTENT |
| 02 Product Shape & Scope | 03_PRODUCT_SHAPE.md, 04_CAPABILITY_SCOPE.md, 05_SUCCESS_MEASURES.md, 06_DECISION_LOG.md | APPROVE PRODUCT SCOPE |
| 03 Independent Review | 07_DEFINITION_REVIEW.md, 08_PRODUCT_DEFINITION_DRAFT.md | FREEZE PRODUCT DEFINITION |

A gate passes only after the exact user command and local timestamp are saved in the canonical control file. No approval is inferred from silence or chat history.

## Product Definition output

The frozen output is product/definition/PRODUCT_DEFINITION.md. It includes target segment, customer outcome, positioning, product concept, product principles, first-release capability boundaries, success measures, decisions, alternatives, dependencies, risks, deferred unknowns and explicit handoff to Process 04 — App Flow.

## Boundaries

Do not create user journeys, screen-by-screen flows, navigation maps, screen inventories, wireframes, visual design, UX/UI, design systems, interaction specs, engineering-ready PRDs, user stories, acceptance criteria, API/database architecture, implementation plans, tasks or code.

Do not invent customer quotes, personas, evidence, competitor claims, baselines or metrics. Freezing Product Definition means direction/scope is approved; it does not mean the market or solution is validated.

## Upstream methods

- ferminrp/agent-skills Product Shaping is available as an existing verbatim reference at upstream/ferminrp/product-shaping/. It informs the unknowns log, shaping fidelity, no-gos and deferred unknowns. See existing license-status note.
- marfoerst/the-pragmatic-pm pm-product-brief is copied verbatim under MIT. It informs customer-outcome framing and the outcome ladder. It is reference-only; its optional host context files are not required dependencies.
- See UPSTREAMS.md and LICENSES/PM-TOOLKIT-MIT-LICENSE.txt.

## How to start

Open Tab 01 in the same workspace, read the active Skill, initialize the control file, verify Process 02 handoff and paste the matching prompt. Do not jump to Tab 02 or 03 until the relevant human gate is recorded.

Keep private participant data outside a public repository. Store only anonymized, authorized evidence references.


## Integrity and handoff hardening

The canonical control template is schema version 2. It binds each approval to SHA-256 hashes of the exact artifacts approved. Gate 3 remains APPROVED; lifecycle_status becomes FROZEN only after the canonical Product Definition hash is stored and read back.

For the PROCESS_02 route, Process 03 accepts only PROCEED or NARROW decisions and re-verifies source hashes at Tab 02, Tab 03 and freeze. PIVOT, PAUSE, STOP, a source mismatch or an unverified hash blocks progression. READY FOR TESTING requires the exact command ACCEPT RESIDUAL UNCERTAINTY.

Tab 03 is read-only on artifacts 01–06. Review history is append-only. Remediation returns to Tab 01 or Tab 02, requires the affected approval again and is followed by a new review round. MAJOR/MINOR findings require explicit user acceptance; freeze does not imply acceptance.

PowerShell SHA-256 and Asia/Ho_Chi_Minh timestamp procedures are specified in the active Skill. If the terminal or hash verification is unavailable, approval/freeze remains NOT_VERIFIED. state_seq detects stale reads but is not a file lock; only one tab may write the Control File at a time.

See VERIFICATION-CHECKLIST.md for paper failure simulations and live Antigravity checks. Paper simulations are not runtime tests.
