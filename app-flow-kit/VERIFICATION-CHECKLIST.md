# Process 04 — Verification Checklist

This checklist distinguishes paper review from live runtime verification. A checked paper scenario is not proof that Antigravity executed it correctly.

## Repository and workspace setup
- [ ] Repository is at workspace root; .agents/skills/app-flow/SKILL.md is discoverable.
- [ ] All three prompts exist at their fully qualified paths under prompts/04-APP-FLOW/.
- [ ] Control template and artifact templates exist under templates/04-APP-FLOW/.
- [ ] Process 03 source files are readable in the same workspace.

## Entry-gate simulations
| Scenario | Expected behavior |
|---|---|
| Process 03 Gate 3 not APPROVED | Stop; NOT_VERIFIED / ineligible |
| Process 03 lifecycle not FROZEN | Stop |
| Product Definition hash mismatch | Stop; do not initialize approval |
| Product Definition missing | Stop |
| Initiative IDs conflict | Stop; do not overwrite either initiative |
| Process 03 frozen and hash matches | Eligible to initialize Process 04 |

## Gate and invalidation simulations
| Scenario | Expected behavior |
|---|---|
| Gate 1 absent | Tab 02 and Tab 03 blocked |
| Gate 1 artifact hash changed | Gate 1 invalidated; downstream blocked |
| Gate 2 absent | Tab 03 and freeze blocked |
| Tab 02 artifact hash changed after Gate 2 | Gate 2 and review invalidated |
| Reviewer finds BLOCKER/CRITICAL | Freeze blocked |
| MAJOR/MINOR remains | User must fix or explicitly accept with rationale |
| User says “looks good” without exact command | No gate approval |
| Hash/read-back fails | NOT_VERIFIED; no success claim |
| state_seq stale | Stop, reload and reconcile; no concurrent write |

## Structural integrity tests
- [ ] Every task maps to one or more approved capability IDs.
- [ ] Every flow has an entry and a defined completion/exit condition.
- [ ] Every node is reachable or explicitly marked as an external entry/terminal node.
- [ ] No unexplained orphan screen or dead-end.
- [ ] Every transition has a condition or is explicitly unconditional.
- [ ] Back/cancel/retry/resume behavior is specified where relevant.
- [ ] State matrix agrees with flow specification and screen inventory.
- [ ] No capability expansion or visual/technical design leakage.
- [ ] Every unresolved decision is visible and assigned.

## Live Antigravity test record
Run in the actual Windows workspace. Do not mark these passed based only on repository inspection.

| Test | Result (PASS/FAIL/NOT RUN) | Evidence path | Notes |
|---|---|---|---|
| Skill discovery | NOT RUN | | |
| Tab 01 input verification and file writes | NOT RUN | | |
| Exact Gate 1 command and read-back | NOT RUN | | |
| Fresh Tab 02 context reconstruction | NOT RUN | | |
| Gate 1 hash invalidation | NOT RUN | | |
| Exact Gate 2 command and read-back | NOT RUN | | |
| Fresh Tab 03 read-only review | NOT RUN | | |
| Remediation and re-review | NOT RUN | | |
| Freeze hash and read-back | NOT RUN | | |

## Release decision
Do not label Process 04 production-ready until all live tests have evidence. Record limitations and unresolved defects in the independent review.
