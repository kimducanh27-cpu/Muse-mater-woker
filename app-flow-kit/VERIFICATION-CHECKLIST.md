# Process 04 — Verification Checklist

This checklist distinguishes repository/paper checks from live runtime verification. A checked paper scenario is not proof that Antigravity executed it correctly.

## Repository and workspace setup
- [ ] Repository is at workspace root; `.agents/skills/app-flow/SKILL.md` is discoverable.
- [ ] All three prompts exist at their fully qualified paths under `prompts/04-APP-FLOW/`.
- [ ] Every prompt names the exact templates it must use.
- [ ] Control and artifact templates exist under `templates/04-APP-FLOW/`.
- [ ] Process 03 source files are readable in the same workspace.
- [ ] Process 04 initiative ID equals Process 03 initiative ID.
- [ ] No prompt-name collision causes the wrong review prompt to be selected.

## Entry-gate simulations
| Scenario | Expected behavior |
|---|---|
| Process 03 Gate 3 not APPROVED | Stop; NOT_VERIFIED / ineligible |
| Process 03 lifecycle not FROZEN | Stop |
| Product Definition hash differs from Process 03 `gate_3.frozen_artifact.sha256` | Stop; do not initialize approval |
| Product Definition or Process 03 Control File missing/unreadable | Stop |
| Initiative IDs conflict | Stop; do not overwrite either initiative |
| Process 03 frozen and hash matches | Eligible to initialize Process 04 |
| Process 04 source_status still NOT_VERIFIED | Gate 1 must refuse |
| Decision Log missing/unreadable or `decision_log.latest_sha256` is null | Gate 1 and Tab 02 refuse; NOT_VERIFIED |
| Actual Decision Log SHA-256 differs from `decision_log.latest_sha256` | Reopen Gates 1–3, invalidate review, record expected/observed hashes and stop |
| `DECISION_LOG_UPDATED` with `affected_gate: GATE_1` occurs after the latest Gate 1 approval | Reopen Gates 1–3 and return to Tab 01 |
| Decision Log approval/update events cannot be ordered by `state_seq` | NOT_VERIFIED; do not assume Gate 1 is current |

## Template and capability coverage simulations
| Scenario | Expected behavior |
|---|---|
| Agent writes prose-only task model without template tables | Gate 1 refuses |
| Required template heading/column is missing or blank | Gate refuses; report exact missing section |
| One approved capability has no task | Gate 1 refuses unless user-approved deferral exists |
| A task has no approved capability | Gate 1 refuses and flags scope mismatch |
| Deferred capability has no approved Decision ID | Gate 1 refuses |
| Decision is only PROPOSED | It is not treated as approved product/flow policy |

## Gate and invalidation simulations
| Scenario | Expected behavior |
|---|---|
| Gate 1 absent | Tab 02 and Tab 03 blocked |
| Decision Log hash is correct and no later GATE_1 update exists | Tab 02 may pass the Decision Log entry check |
| Decision Log changes with affected_gate GATE_1 after Gate 1 approval | Gates 1–3 reopened; Tab 02 stops |
| Decision Log changes with affected_gate GATE_2 after Gate 1 approval | Gates 2–3 reopened; Gate 1 may remain valid |
| Gate 1 artifact hash changed | Gate 1 and downstream gates REOPENED |
| Gate 2 absent | Tab 03 and freeze blocked |
| Tab 02 artifact hash changed after Gate 2 | Gate 2/3 and review invalidated |
| Process 03 Product Definition changes | Source REOPENED; Gates 1–3 reopened |
| User says "looks good" without exact approval command | No gate approval |
| Hash/read-back fails | INCOMPLETE / NOT_VERIFIED; no success claim |
| state_seq stale | Stop, reload and reconcile; no concurrent write |
| Change request without exact user decision | Log request; do not infer approval |

## Review-history and freeze simulations
| Scenario | Expected behavior |
|---|---|
| No review file or review_round = 0 | Freeze refuses |
| Review round 1 exists, then round 2 is appended | Round 1 remains byte-for-byte intact |
| Review file hash differs from Control File | Freeze refuses |
| Draft 08 changes after review | Freeze refuses; new review round required |
| Latest review status BLOCKERS_FOUND | Freeze refuses |
| Unresolved BLOCKER or CRITICAL | Freeze refuses; cannot accept |
| Open MAJOR/MINOR | Freeze refuses until fixed or individually accepted |
| User says "accept all" without exact finding command and rationale | No residual-risk acceptance |
| User accepts one MAJOR/MINOR with exact command and rationale | One structured acceptance record and appended review addendum |
| Freeze before independent review | Freeze refuses |
| GO verdict without explicit freeze command | No freeze |
| Draft 08 contains a summary, not full canonical sections | Freeze refuses |
| APP_FLOW.md differs from draft beyond exact status line | Freeze refuses |
| APP_FLOW.md has no matching Control File Gate 3 record | Orphan; downstream use prohibited |
| Canonical write succeeds but Control File write/read-back fails | INCOMPLETE — NOT FROZEN |
| Re-freeze requested | Verify and archive prior version as APP_FLOW.v<N>.md before replacement |
| Existing archive contains different bytes | Stop; never overwrite archive |
| Frozen APP_FLOW.md is modified | Gate 3 REOPENED; lifecycle REVIEW_REQUIRED; downstream use blocked |
| ABANDON APP FLOW command | Lifecycle ABANDONED; terminal for that initiative |

## Structural integrity tests
- [ ] Every approved capability maps to task(s) or a user-approved deferral.
- [ ] Every task maps to approved capability ID(s).
- [ ] Every task appears in task-to-flow mapping.
- [ ] All flow/node/screen/transition IDs are unique.
- [ ] Screen IDs in 04 equal screen references in navigation nodes, except justified exclusions.
- [ ] Every transition source/destination references a valid node or declared external/terminal endpoint.
- [ ] Every flow has an entry and observable completion/terminal condition.
- [ ] Explicit reachability traversal is recorded; no unexplained unreachable node, orphan screen or dead end.
- [ ] State matrix agrees with flow specification and screen inventory.
- [ ] Every excluded state has a rationale.
- [ ] No capability expansion or visual/technical design leakage.
- [ ] All material decisions are approved or unresolved questions.

## Live Antigravity test record
Run in the actual Windows workspace. Do not mark these passed based only on repository inspection.

| Test | Result (PASS/FAIL/NOT RUN) | Evidence path | Notes |
|---|---|---|---|
| Skill discovery and explicit invocation | NOT RUN | | |
| Tab 01 rejects Process 03 Gate 3 PENDING | NOT RUN | | |
| Tab 01 writes 01–02 using templates | NOT RUN | | |
| Capability reverse-coverage failure is caught | NOT RUN | | |
| Exact Gate 1 command and read-back | NOT RUN | | |
| Fresh Tab 02 reconstructs Gate 1 from files | NOT RUN | | |
| Tab 02 writes 03–06 with template conformance | NOT RUN | | |
| Orphan screen / invalid transition is detected | NOT RUN | | |
| Exact Gate 2 command and read-back | NOT RUN | | |
| Fresh Tab 03 reconstructs all state | NOT RUN | | |
| Review round 2 preserves round 1 | NOT RUN | | |
| Freeze without a review refuses | NOT RUN | | |
| Freeze with open MAJOR finding refuses | NOT RUN | | |
| Explicit risk acceptance persists and is appended | NOT RUN | | |
| Draft 08 → APP_FLOW.md differs only by status line | NOT RUN | | |
| Canonical/control partial-write failure reports INCOMPLETE | NOT RUN | | |
| Re-freeze archives prior version | NOT RUN | | |
| Modified frozen artifact reopens Gate 3 | NOT RUN | | |

## Release decision
Do not label Process 04 production-ready until all mandatory live tests have evidence. Record limitations and unresolved defects in independent review. Repository inspection is not live Antigravity verification.
