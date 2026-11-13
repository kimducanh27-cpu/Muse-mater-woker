# CHAIN PROBE — one thread through six processes

A second probe suite, run after `MUSE-CONTRACT-PROBE.md`. That one tests whether each gate refuses. This one tests whether the chain **closes**.

## Why one thread, not the whole pipeline

A full run is eighteen tabs and roughly sixty artifacts. An agent asked to do that degrades somewhere in the middle and the report becomes unusable — you cannot tell a broken contract from a tired model.

So this probe pulls **one capability** through all six processes. Six small artifacts, each the minimum that carries the thread forward. If one capability cannot be traced end to end, the chain is broken, and the place it breaks is the finding.

The risk in this repository is not inside any single process. It is at the seams. A thread test is aimed at the seams.

## The hypothesis to confirm or refute

Stated before the run, so the run can actually falsify it:

> The chain is verifiable from Process 03 onward and only asserted before it. Process 01 has no canonical state file, and Process 02's Control File contains no hash binding, so the handoff into Process 03 compares strings rather than bytes.

If the probe confirms this, it is the single most important finding in the suite: three of six processes cannot produce evidence that survives a file edit.

## Hard constraints

Same as the first suite, plus:

- Write only under `fixtures/chain-<timestamp>/`.
- Every artifact carries a header line `> SIMULATED — NOT ELIGIBLE DOWNSTREAM`.
- Every approval you issue is written as `SIMULATED` and never as a real gate status. If a template requires `APPROVED`, write `SIMULATED_APPROVED` and record that substitution in the report.
- Never modify a contract, template or prompt.

## The thread

Pick one capability with a short, unambiguous path. Suggested shape:

```
CAP-01 — the user can save a draft and return to it later
```

It must be small enough to survive six processes without invention, and concrete enough that a screen and a component can be derived from it.

## Steps

For each process, produce one artifact from the real template in `templates/`, under the fixture root. Keep each minimal but valid — every required heading present, every required column filled.

| Step | Process | Artifact to produce | Thread element |
|---|---|---|---|
| 1 | 01 Seed | `01_SEED_CANDIDATE.md` | The problem and the capability as a hypothesis |
| 2 | 02 Discovery | `00_DISCOVERY_CONTROL.md` + `07_DISCOVERY_DECISION.md` | The decision that the capability is worth pursuing |
| 3 | 03 Definition | `00_PRODUCT_DEFINITION_CONTROL.md` + `PRODUCT_DEFINITION.md` | `CAP-01` enters the approved capability scope |
| 4 | 04 App Flow | `00_APP_FLOW_CONTROL.md` + `04_SCREEN_INVENTORY.md` | A screen that serves `CAP-01` |
| 5 | 05 UX Design | `01_SCREEN_UX_MODEL.md` | The screen's goal, primary action, states |
| 6 | 06 Design Systems | `03_COMPONENT_INVENTORY.md` | A component citing that screen |

At each step, record the SHA-256 of the artifact you wrote, and the SHA-256 the next process would need in order to verify it.

## The closure audit

After step 6, fill this table. Every row is a set comparison, not a claim.

| Link | From | To | Closed? | Evidence |
|---|---|---|---|---|
| L1 | Seed hypothesis | Discovery decision | | |
| L2 | Discovery decision | `CAP-01` in approved scope | | |
| L3 | `CAP-01` | at least one screen | | |
| L4 | Screen | UX model entry | | |
| L5 | Screen | at least one component | | |
| L6 | Component | measured contrast pair | | |
| L7 | Every hash | recorded in a Control File | | |

L7 is the one this probe exists for. For each link, answer: **could a later process detect that this artifact changed?** If the answer is "only by trusting a string", mark it `ASSERTED` rather than `CLOSED`.

## Verdicts

| Verdict | Meaning |
|---|---|
| `CLOSED` | The link is traceable and byte-verifiable |
| `ASSERTED` | The link is traceable but only by trusting a written claim |
| `BROKEN` | The thread does not reach the next process |
| `UNEXECUTABLE` | The template cannot carry the thread without invention |

A chain of six `CLOSED` would refute the hypothesis. A chain with `ASSERTED` at L1–L2 and `CLOSED` from L3 is the hypothesis confirmed.

## Report

Append to the same report file as the first suite, under a `## Chain probe` heading:

- the thread you chose, in one sentence
- the six artifacts with their hashes
- the closure table
- the verdict per link
- whether the hypothesis was confirmed or refuted
- the single weakest link, and what it would take to close it

## What this still does not prove

- It does not prove the pipeline is usable by a human. Every approval is `SIMULATED`.
- It does not prove the artifacts are good. One capability, minimal content.
- It does not convert a `NOT RUN` into a `PASS`.

It proves one thing: whether a capability can travel from an idea to a component without the chain losing it, and whether each handoff can be verified rather than believed.
