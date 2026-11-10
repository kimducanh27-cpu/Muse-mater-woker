# PROCESS 03 — TAB 03: INDEPENDENT PRODUCT DEFINITION REVIEW

Use the active product-definition Skill in a fresh Antigravity conversation. Do not rely on prior tab chat history.

## Read first
- product/definition/00_PRODUCT_DEFINITION_CONTROL.md
- product/definition/01_PRODUCT_INTENT.md
- product/definition/02_POSITIONING.md
- product/definition/03_PRODUCT_SHAPE.md
- product/definition/04_CAPABILITY_SCOPE.md
- product/definition/05_SUCCESS_MEASURES.md
- product/definition/06_DECISION_LOG.md
- Relevant Process 02 decision/outcome/evidence artifacts.

## Entry gate
Verify Gate 1 and Gate 2 are both APPROVED in the canonical control file. If either is absent, PENDING, REJECTED or REOPENED, stop and identify the blocker.

## Reviewer stance
Act as an independent reviewer. Do not defend prior tabs' decisions. Detect weak reasoning, unsupported claims, contradictions, scope creep and unresolved choices.

## Review protocol
1. Trace every major product promise and capability to the Process 02 opportunity and evidence IDs.
2. Distinguish observation, user report, interpretation, hypothesis and strategic choice.
3. Challenge target-user specificity and avoid treating a generic persona as evidence.
4. Check that the value proposition describes a customer outcome, not a feature list.
5. Check differentiation against real alternatives and verified sources.
6. Check whether capability scope can deliver the promise without becoming App Flow or engineering specification.
7. Test IN / NOT NOW / OUT boundaries for ambiguity and scope creep.
8. Check metrics for definitions, sources, baselines, targets, time windows and owners. Missing data stays visible.
9. Check principles for concrete trade-off guidance.
10. Inspect risks, dependencies, ethics/privacy and deferred unknowns.
11. Identify what would make the product direction wrong or not worth building.

## Output
Create:
- product/definition/07_DEFINITION_REVIEW.md
- product/definition/08_PRODUCT_DEFINITION_DRAFT.md only if there are no BLOCKER findings.

Rank every finding BLOCKER / MAJOR / MINOR. Include exact file/section, why it matters, evidence and required correction. If BLOCKER exists, do not prepare a freeze candidate. After remediation, re-review changed sections and invalidate affected gates.

## Freeze
After corrections and a clean review, show the user the recommendation and residual risks. Wait for exact command: FREEZE PRODUCT DEFINITION.

When received:
1. Recheck Gates 1 and 2 are APPROVED and no BLOCKER remains.
2. Copy the reviewed draft to product/definition/PRODUCT_DEFINITION.md.
3. Set Gate 3 and lifecycle state to FROZEN in product/definition/00_PRODUCT_DEFINITION_CONTROL.md.
4. Record exact command, user decision, local timestamp and reviewed artifact revision.
5. Report success only after both files are saved.

Do not create App Flow, UI/UX, architecture or implementation. Do not auto-start Process 04.
