# PROCESS 03 — TAB 03: INDEPENDENT PRODUCT DEFINITION REVIEW

Use the active product-definition Skill in a fresh Antigravity conversation. Do not rely on prior tab chat history.

## Read first
- product/definition/00_PRODUCT_DEFINITION_CONTROL.md
- product/definition/01_PRODUCT_INTENT.md through 06_DECISION_LOG.md
- product/discovery/00_DISCOVERY_CONTROL.md and pinned Process 02 artifacts for the PROCESS_02 route
- product/definition/07_DEFINITION_REVIEW.md if it exists
- product/definition/08_PRODUCT_DEFINITION_DRAFT.md if it exists

## Entry gate
- Verify route, source initiative and handoff eligibility.
- Recompute pinned Process 02 source hashes.
- Verify any READY FOR TESTING uncertainty acceptance.
- Verify Gate 1 and Gate 2 = APPROVED.
- Recompute hashes of artifacts 01–06 and compare with approved_artifacts.

If any condition fails, stop, log the mismatch, reopen affected gates and do not review or freeze stale content.

## Reviewer permissions
- Read-only on Process 02 sources and Process 03 artifacts 01–06.
- May append a review round to 07_DEFINITION_REVIEW.md.
- May create/update the draft candidate 08_PRODUCT_DEFINITION_DRAFT.md.
- Must not edit artifacts 01–06 or Process 02 sources.
- Route remediation to a fresh Tab 01 or Tab 02 conversation.

## Review protocol
1. Trace every material promise and capability to Discovery evidence or label it as HYPOTHESIS / strategic choice.
2. Verify target segment, job and alternatives are inherited from Process 02 or have an explicit deviation and rationale.
3. Check product promise, differentiation and alternatives.
4. Test capability scope and IN / NOT NOW / OUT boundaries.
5. Check product principles for useful trade-offs.
6. Check measures, baseline and target status.
7. Find contradictions, dependencies, risks, ethical/privacy concerns and scope creep.
8. Identify what would make the product direction wrong or not worth building.
9. Record BLOCKER / MAJOR / MINOR findings with stable IDs, exact source sections, evidence, consequence and required correction.

## Review history
Append a new round to product/definition/07_DEFINITION_REVIEW.md. Never delete or overwrite earlier rounds. Record source hashes for artifacts 01–06, round number, finding status and draft hash when one exists.

If BLOCKER findings exist, do not create a freeze candidate. Send findings to the responsible tab:
- Intent/Positioning -> Tab 01.
- Shape/Scope/Measures/Decision Log -> Tab 02.

The responsible tab must make the correction and obtain the affected gate approval again. Then run a new full review round.

## Draft consistency check
Only with zero unresolved BLOCKER findings, create/update product/definition/08_PRODUCT_DEFINITION_DRAFT.md.

Verify it preserves the reviewed content from 01–06, all material decisions, evidence labels, accepted risks and deferred unknowns. It must introduce no new unsupported promise/capability and must not turn HYPOTHESIS into FACT. It must not contain App Flow, UI/UX or engineering specification.

Record hashes of 01–06 and 08 in the review round and Control File. Record review status and open finding counts.

## Residual risk acceptance
The reviewer may recommend acceptance but cannot accept risk on the user's behalf. Each unresolved MAJOR/MINOR finding requires the exact user command ACCEPT RESIDUAL RISK [FINDING-ID]. Record who accepted it, exact command, rationale and timestamp in the Control File and review history. FREEZE PRODUCT DEFINITION does not imply risk acceptance.

## Freeze
Wait for exact command FREEZE PRODUCT DEFINITION.

Before freezing:
1. Re-verify handoff, Gates 1 and 2, pinned source hashes and residual-uncertainty acceptance where applicable.
2. Recompute and compare hashes for artifacts 01–08 with the latest review round.
3. Confirm no unresolved BLOCKER remains and all residual MAJOR/MINOR findings are resolved or explicitly accepted.
4. Confirm the draft consistency check passed.
5. If an earlier PRODUCT_DEFINITION.md exists, archive it as PRODUCT_DEFINITION.v<N>.md without overwriting prior versions.
6. Copy the reviewed draft to PRODUCT_DEFINITION.md. The only permitted transformation is replacing the metadata line "Status: REVIEWED CANDIDATE — NOT FROZEN" with "Status: FROZEN".
7. Compute final canonical SHA-256 and store it in Gate 3 along with reviewed source hashes, draft hash, timestamp and version.
8. Set Gate 3 status = APPROVED and lifecycle_status = FROZEN. Never set Gate 3 status to FROZEN.
9. Increment state_seq, save the Control File, read it back and recompute the canonical hash.
10. Report success only after both files and hashes verify.

If a write/read-back fails, report INCOMPLETE — NOT FROZEN. Do not let Process 04 consume an orphan canonical file.

Do not create App Flow, UI/UX, architecture or implementation. Do not auto-start Process 04.
