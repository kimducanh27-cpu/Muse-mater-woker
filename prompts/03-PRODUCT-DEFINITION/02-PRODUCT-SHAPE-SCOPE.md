# PROCESS 03 — TAB 02: PRODUCT SHAPE & SCOPE

Use the active product-definition Skill in a fresh Antigravity conversation. Do not rely on prior chat history.

## Read first
- product/definition/00_PRODUCT_DEFINITION_CONTROL.md
- product/definition/01_PRODUCT_INTENT.md
- product/definition/02_POSITIONING.md
- The pinned Process 02 sources recorded in the Control File.

## Entry gate
1. Verify this is the same initiative.
2. Verify handoff status and recompute all pinned Process 02 source hashes.
3. For READY FOR TESTING, verify persisted ACCEPT RESIDUAL UNCERTAINTY command and timestamp.
4. Verify Gate 1 = APPROVED.
5. Recompute hashes of 01_PRODUCT_INTENT.md and 02_POSITIONING.md and compare with Gate 1 approved_artifacts.

If any prerequisite is missing, mismatched, REOPENED, REJECTED or NOT_VERIFIED, stop. A changed source reopens dependent gates; do not proceed on stale approval.

## Work
1. Define the core product concept and mechanism at high-level fidelity: what the customer brings, what the product enables and what outcome changes — not a sequence of screens.
2. Create only product principles that resolve real trade-offs.
3. Convert the opportunity into a small set of customer-facing capabilities. Describe user abilities/outcomes, not controls or components. Assign stable IDs: CAP-01, CAP-02, ...
4. Define first-release boundaries:
   - IN: required to deliver the primary promise.
   - NOT NOW: valuable but not necessary for first release.
   - OUT: explicitly excluded from this product/direction.
5. Apply a cut-line test to each IN item: if removed, does the primary value promise fail?
6. Record dependencies, operational/platform constraints, ethical/privacy considerations and major risks at product level.
7. Define leading and lagging success measures with definitions and sources. Mark unknown baselines/targets visibly.
8. Record decisions, rejected alternatives, accepted risks, deferred unknowns and rationale for material scope boundaries.

## Output
Create/update:
- product/definition/03_PRODUCT_SHAPE.md
- product/definition/04_CAPABILITY_SCOPE.md
- product/definition/05_SUCCESS_MEASURES.md
- product/definition/06_DECISION_LOG.md

Maintain traceability to Process 02 evidence IDs and the inherited segment/job/alternatives.

## Boundaries
No App Flow, navigation, step-by-step user journeys, screens, wireframes, UX/UI, visual design or interaction specification. No detailed PRD, acceptance criteria, engineering stories, technical architecture, API/database schema, tasks or code.

## Gate 2
Wait for exact command APPROVE PRODUCT SCOPE. A revision request is logged as REVISION_REQUESTED; REJECT PRODUCT SCOPE sets the gate to REJECTED.

On approval:
- Compute SHA-256 for all four output artifacts.
- Record Gate 2 = APPROVED, exact command, user decision, real local timestamp and approved_artifacts.
- Increment state_seq, save, read back and verify.

Do not claim success or start Tab 03 if hashing, timestamp, write or read-back fails. Never start Tab 03 automatically.

## Invalidation
Any change to artifacts 03–06 reopens Gates 2 and 3. A change to artifacts 01–02 or a pinned Process 02 source also invalidates dependent gates under the Skill's matrix.
