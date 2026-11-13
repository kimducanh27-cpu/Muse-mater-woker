> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `78667ac`, 2026-11-13.

# Progress

## Done

| Thing | Evidence |
|---|---|
| Six process contracts (01–06) | Nine Skills, 57 templates, prompts and kits for each |
| Process 04 schema v4 with a Change Request Register | Register v1 template, abort-pair contract, migration rules, 22 stress scenarios |
| Process 04 sentinel hash rule (ADR-P04-11) | Resolved the self-referential preimage; verified comprehensible by probe 8 |
| Process 04 schema v4 field contract | `CONTROL-FIELDS-v4.yaml` covering 15 event types; `validate-control.py` version-aware |
| Process 05 UX Design contract | 53 scenarios, three lexical audits, review history, freeze protocol |
| Process 06 Design Systems contract | 55 scenarios, component admission rule, Material 3 token tiers |
| Platform decision | Android native, recorded as an immutable Control field |
| Provenance governance | 24 rules labelled VERBATIM / ADAPTED / LOCAL; 8 LOCAL decisions registered (L-1–L-8) |
| Upstream method vendored | Four files copied byte-for-byte from an Apache-2.0 source, blob SHAs recorded |
| Eight checking scripts | Control File, Register chain, UX artifacts 01–05, gate applier — each tested against a known-bad input |
| One gate exercised for real | `fixtures/probe-11` Gate 1 approved with command `APPROVE SCREEN UX MODEL`, `state_seq` 0 to 1, verified |
| Chain probe executed | Report `10-chain-probe.md`: confirmed hypothesis (L1–L2 asserted, L3–L6 closed) |
| Twelve probes | Ten run reports; 13 findings, 7 closed by re-running the probe |
| Pipeline P05-P06 merged to main | Explicit human command 'MERGE PIPELINE P05-P06 TO MAIN'; 3 rounds of adversarial review complete |

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
| **No product exists** | No initiative has run end to end. No frozen artifact exists for any real idea. |
| **No live initiative in product/** | Live workspace remains unrun. One simulated gate was exercised on `fixtures/probe-11`. |
| **130 scenarios are `NOT RUN`** | 22 in Process 04, 53 in Process 05, 55 in Process 06. |

## The one thing worth carrying forward

Every finding closed by re-probe was closed the same way: **a mechanical check placed between the write and the claim.**

F-06 and F-08 were agents reporting success on artifacts that did not verify. Both stopped failing the moment a validator stood between the artifact and the report. F-11 was six checks written down and skipped; it started working when the checker became a required step.

The corollary is in `docs/RULES.md`: when a check replaces a prose requirement, delete the prose. F-13 is what happens when both are kept.

## Next

All tasks 1–6 are complete. The pipeline contracts and mechanical checkers for Processes 01–06 are merged and verified on `main`.
