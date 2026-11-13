> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `42f615a`, 2026-11-13.

# Progress

## Done

| Thing | Evidence |
|---|---|
| Six process contracts (01–06) | Nine Skills, 56 templates, prompts and kits for each |
| Process 04 schema v4 with a Change Request Register | Register v1 template, abort-pair contract, migration rules, 22 stress scenarios |
| Process 04 sentinel hash rule (ADR-P04-11) | Resolved the self-referential preimage; verified comprehensible by probe 8 |
| Process 05 UX Design contract | 53 scenarios, three lexical audits, review history, freeze protocol |
| Process 06 Design Systems contract | 55 scenarios, component admission rule, Material 3 token tiers |
| Platform decision | Android native, recorded as an immutable Control field |
| Provenance governance | 23 rules labelled VERBATIM / ADAPTED / LOCAL; 7 LOCAL decisions registered |
| Upstream method vendored | Four files copied byte-for-byte from an Apache-2.0 source, blob SHAs recorded |
| Three validators | Control File, Register chain, UX artifact 01 — each tested against a known-bad input |
| Eleven probes | Nine run reports; 13 findings, 7 closed by re-running the probe |

## Broken, then fixed

Thirteen findings. Seven were closed the only way that counts: the same probe, re-run against the changed contract, produced the behaviour the contract now specifies.

| ID | What broke | How it was closed |
|---|---|---|
| F-04 | Component audit matched `card` inside `discards` | Word-boundary procedure; validator passes correct prose, fails planted violations |
| F-05 | Audit match set defined by the reviewer, not the rule | Six-step procedure with required sentence output |
| F-06 | Read-back compared the artifact to the writer's memory | Field contract plus validator; probe re-run passes |
| F-08 | Register digest verified under nothing; agent reported success | Validator in the loop; probe re-run passes on the first attempt |
| F-10 | Banned term `tab` matched `Tab 01`, failing every correct artifact | Mask workflow vocabulary before matching |
| F-11 | Six enumerated checks never executed | Validator made a required step; probe re-run passes |
| F-13 | Narrating checks and running a checker gave two ways to comply | Prose requirement deleted; the validator output is the record |

Five more were closed by specification only and say so in `test-harness/FINDINGS.md`: F-01, F-02, F-03, F-09, F-12. The thirteenth, F-07, is not a fix at all — it records that Process 06 had never been executed, and that it now has been once.

## Open

| Item | Why it matters |
|---|---|
| **No gate has ever been exercised** | Every Control File has `gate_1: PENDING` and an empty `event_log`. The validators check consistent workspaces, never transitions. |
| **No product exists** | No initiative has run end to end. No frozen artifact exists for any real idea. |
| **Processes 01–03 have no hash binding** | Process 01 has no state file; Process 02's Control File contains zero occurrences of `sha256`. A chain built on them is asserted, not verified. |
| **Process 04 schema v4 has no field contract** | Its event set is larger than v1 and unguarded. |
| **P05 artifacts 02–05 have no validators** | Prose-only, which is the condition that produced three findings. |
| **130 scenarios are `NOT RUN`** | 22 in Process 04, 53 in Process 05, 55 in Process 06. |
| **Two draft PRs, no merge** | Merge authorization not granted. |

## The one thing worth carrying forward

Every finding closed by re-probe was closed the same way: **a mechanical check placed between the write and the claim.**

F-06 and F-08 were agents reporting success on artifacts that did not verify. Both stopped failing the moment a validator stood between the artifact and the report. F-11 was six checks written down and skipped; it started working when the checker became a required step.

The corollary is in `docs/RULES.md`: when a check replaces a prose requirement, delete the prose. F-13 is what happens when both are kept.

## Next

`docs/TASKS.md`, in order. The first task is to open one gate for real, because nothing in this repository has ever crossed one.
