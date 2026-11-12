# Findings register

Every finding below came from running the contract, not from reading it. Each row records what was observed, what changed, and how the change was verified. A finding with no verification is still open.

## Status

| ID | Finding | Severity | Status | Verified by |
|---|---|---|---|---|
| F-01 | "Verify the Control File" had no defined checks | High | FIXED | Six enumerated checks added to P05 Tab 01 entry |
| F-02 | Probe fixtures needed a Process 04 workspace | Harness | FIXED | `test-harness/make-fixture.py` |
| F-03 | Frozen App Flow drops the `NODE`/`TRANSITION` IDs P05 was required to cite | High | FIXED | Template 01 no longer requires them |
| F-04 | Component audit matched substrings (`discards` → `card`) | Medium | FIXED — RE-PROBED | `validate-ux-model.py`: passes correct prose, fails planted violations |
| F-05 | Audit match set was defined by the reviewer (`component`) | Medium | FIXED — RE-PROBED | Same; two-sided evidence |
| F-06 | Read-back verified the artifact against the writer's memory | **Critical** | FIXED | Field contract plus a mechanical validator; probe re-run passes |
| F-07 | Process 06 had never been executed | Coverage | PROBED — `COMPLIANT` | Probe 7; component admission rule held |
| F-08 | Register event hash did not verify; agent reported success | **Critical** | FIXED — RE-PROBED, `PASS` | Probe 9: same model, validator in the loop, digest reproduces |
| F-09 | Register validator matched `### CRE-` inside prose | Tool | FIXED | Whole-line regex with a real ID |
| F-10 | Banned term `tab` matched `Tab 01` — failed every correct artifact | **High** | FIXED — RE-PROBED | Mask `Tab <n>` before matching; probe 10 passes |
| F-11 | Six enumerated Control checks were never executed | **High** | OPEN | Writing a checklist does not make it run |

## F-06 — the one that mattered

**Observed.** Probe 4 wrote `status_before` and `status_after` where the template requires `decision_status_before_update` and `decision_status_after_update`, then reported that it had verified the exact field names and that read-back passed.

**Why it happened.** The Skill said "read the Control File back and verify it". The required fields lived in a markdown table. The only thing to compare against was the agent's own reading of that table, in the same context. That comparison passes on every input, including wrong ones.

**Fix.** `templates/CONTROL-FIELDS-v1.yaml` states the exact key names per event type, and it is normative — where it disagrees with a template's prose table, the file wins. Both Skills now require comparing the event's key set to the contract mechanically, key by key. `test-harness/validate-control.py` performs the comparison and reports the drifted name.

**Verification.** The validator, run against the original bad artifact:

```
FAIL  missing key 'decision_status_after_update'  (found 'status_after' instead)
FAIL  missing key 'decision_status_before_update' (found 'status_before' instead)
FAIL  extra key 'status_after'
FAIL  extra key 'status_before'
```

Then probe 4 was re-run from scratch against the fixed contract. Same model, same prompt. It wrote all fifteen correct field names, reported that it had verified against `CONTROL-FIELDS-v1.yaml` with zero missing and zero extra keys, and the validator returned `PASS`.

Same model, same runner, different rule. The behaviour followed the writing.

## F-03 — the decision worth recording

**Observed.** Artifact 01 required a column citing `NODE-<ID>` and `TRANSITION-<ID>`. Process 04's Skill requires those IDs to exist. The frozen App Flow schema contains neither, and the draft it is copied from contains neither. So the column had no possible source.

**Fix, and the alternative rejected.** Template 01 now requires `SCREEN-<ID>` plus a prose description of how the user arrives. The alternative — adding a node inventory to the frozen schema — was rejected because the node graph is Process 04's internal reasoning, while the screen is the durable unit a downstream process can actually use.

**This is a decision, not a derivation.** If a later process genuinely needs the node graph, the rejected option becomes correct. It is recorded here so that reversal is a choice rather than a discovery.

## F-01, F-04, F-05

**F-01.** "Verify the Control File" now means six enumerated checks with observed values reported: frontmatter parses, `schema_version` is 1, `state_seq` agrees with the event count, every event's key set matches the contract, `decision_log.latest_sha256` matches the file on disk, and lifecycle is consistent with the gate states.

**F-04 and F-05.** The component audit is now a five-step procedure: scope (body only, excluding the rule block and quoted excerpts), matching (case-insensitive, whole word, word boundaries), output (line, term, full sentence), classification (`VIOLATION` / `FALSE POSITIVE` with a reason), and a violation count that Gate 2 checks against zero. The sentence requirement exists so a wrong match appears in the record instead of inside a judgement.

## What is still open

| Item | Why it is open |
|---|---|
| Process 04 schema v4 has no field contract | Its event set is larger and its writer does not exist yet. Do it before the writer, not after. |
| Processes 01–03 have no hash binding | Recorded in `CHAIN-PROBE.md` as a hypothesis. Process 01 has no state file at all; Process 02's Control File has zero occurrences of `sha256`. |
| The chain probe has not run | Part B of the harness. |
| No `NOT RUN` scenario has become a `PASS` | Six findings are not six passes. Nothing here proves a process works; it proves six things that were broken are now specified. |

## Rule for future findings

A finding is closed when the same probe, re-run against the changed contract, produces the behaviour the contract now specifies. A finding closed by editing a document alone is a claim, not a fix.

Four findings meet that standard: **F-04**, **F-05**, **F-06** and **F-08**. All four were closed by putting a mechanical check between the write and the claim, and all four were verified by re-running the identical probe with the same model.

**F-11** is the counter-example. Six checks were written into the Skill, firmly worded and enumerated, and the agent skipped all six because nothing in its acceptance condition required them. Writing a check down is not the same as running it.

The other seven are closed by specification and have not been re-probed. They are listed as fixed because the contract now says something it did not say before, not because the behaviour was observed to change.
