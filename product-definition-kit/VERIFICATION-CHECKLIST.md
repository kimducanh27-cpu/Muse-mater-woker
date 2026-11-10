# Process 03 — Hardening Verification Checklist

This checklist contains paper simulations and environment tests. A paper simulation is not a live Antigravity test.

## Static checks

- [ ] Control template YAML parses and schema_version is 2.
- [ ] Gate enums are PENDING / APPROVED / REJECTED / REOPENED only.
- [ ] Gate 3 is APPROVED after freeze; lifecycle_status is FROZEN.
- [ ] Gate 1 stores hashes for artifacts 01 and 02.
- [ ] Gate 2 stores hashes for artifacts 03–06.
- [ ] Gate 3 stores final canonical hash, reviewed draft hash and reviewed source hashes.
- [ ] Handoff stores route, source initiative, decision, evidence status and source hashes.
- [ ] READY FOR TESTING acceptance stores exact command, timestamp and evidence status.
- [ ] Process 02 decisions PIVOT / PAUSE / STOP block entry.
- [ ] Handoff and artifact hashes are re-verified at Tab 02, Tab 03 and freeze.
- [ ] Invalidation matrix is consistent in Skill, Control File and prompts.
- [ ] Tab 03 is read-only on artifacts 01–06.
- [ ] Review rounds append; previous rounds and findings are preserved.
- [ ] Draft 08 consistency check is recorded before freeze.
- [ ] Unresolved BLOCKER blocks freeze.
- [ ] Open MAJOR/MINOR requires explicit user acceptance.
- [ ] No Process 04 instruction permits silent edits to Product Definition.
- [ ] All internal paths referenced by Process 03 resolve.

## Paper failure simulations

| ID | Input | Expected result |
|---|---|---|
| S01 | Frozen Outcome, Gate 3 APPROVED, decision PROCEED | Eligible after source hashes verify |
| S02 | Decision NARROW | Eligible; preserve narrowed direction |
| S03 | Decision PIVOT | Stop; return to Process 02 |
| S04 | Decision PAUSE or STOP | Stop |
| S05 | READY FOR TESTING without acceptance command | Stop before Gate 1 |
| S06 | READY FOR TESTING with persisted acceptance | Eligible if all other checks pass |
| S07 | Process 02 Gate 3 PENDING | Stop |
| S08 | Process 02 Control File unreadable | NOT_VERIFIED; stop |
| S09 | Outcome header conflicts with Control File | NOT_VERIFIED; stop |
| S10 | Process 02 source hash changes | Reopen dependent gates; stop |
| S11 | Gate 1 missing or not APPROVED | Tab 02/03 stop |
| S12 | Gate 2 missing or not APPROVED | Tab 03 stop |
| S13 | Approved artifact changes out of band | Hash mismatch; reopen affected gate |
| S14 | Reviewer finds BLOCKER | No draft candidate or freeze |
| S15 | Reviewer finds MAJOR/MINOR | Explicit user acceptance required |
| S16 | User accepts one risk with exact command | Persist finding ID, command, rationale and time |
| S17 | Draft 08 changes after review | Gate 3 reopens; new review required |
| S18 | Canonical artifact write fails | INCOMPLETE — NOT FROZEN |
| S19 | Canonical write succeeds; Control File write fails | Orphan artifact; INCOMPLETE — NOT FROZEN |
| S20 | Frozen Product Definition edited | Hash mismatch; Gate 3 reopened; REVIEW_REQUIRED |
| S21 | Re-freeze requested | Archive previous version, then create new version |
| S22 | Control File belongs to another initiative | Stop; do not overwrite |
| S23 | Terminal/hash unavailable | NOT_VERIFIED; no approval/freeze |
| S24 | Two tabs try to write Control File | Stop second writer; reload and reconcile stale state |

For every simulation, record input state, expected result, actual paper result, PASS/FAIL/NOT VERIFIED, responsible file and consequence.

## Live Antigravity checks — must be run in the actual workspace

- [ ] Active Skill appears in Antigravity Customizations.
- [ ] Explicit Skill invocation works.
- [ ] Nested upstream SKILL.md indexing behavior is inspected in Customizations.
- [ ] PowerShell timestamp and Get-FileHash are available to the agent.
- [ ] Fresh conversations reconstruct state from workspace files only.
- [ ] Control File YAML remains valid after repeated updates.
- [ ] Read-back detects a deliberately simulated write failure.
- [ ] Tab 03 does not edit artifacts 01–06.
- [ ] Large Process 02 inputs are handled without silently omitting sources.

Mark every unrun item NOT VERIFIED. Never describe paper simulation as runtime validation.
