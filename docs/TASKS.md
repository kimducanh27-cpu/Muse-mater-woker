> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `7432476`, 2026-11-13.

# Tasks

Ordered by what produces evidence, not by what is easy. Do them one at a time. A task is done when its stated evidence exists, not when the file is written.

## 1. Exercise one gate for real

**Why first.** No gate has ever been opened. Every Control File in this repository has `gate_1.status: PENDING` and an empty `event_log`. The validators check a workspace that is already consistent; none has ever checked a *transition*.

**Do.** Take `fixtures/probe-11`, produce artifact 01 with both validators passing, then have the human type `APPROVE SCREEN UX MODEL`.

`test-harness/apply-gate.py` performs the Control update mechanically: it refuses a command that does not match `required_command`, refuses a gate that is not `PENDING` or `REOPENED`, runs the artifact validator first, and re-validates after writing. Tested on a throwaway copy — refusal path and success path both behave. The live fixture is still `PENDING`.

**Evidence.** The Control File parses, `validate-control.py` passes with one event, and the event's key set matches `CONTROL-FIELDS-v1.yaml`. Then re-run `validate-control.py` — it must still pass.

**Fails if.** The agent writes the event without the human's command, or writes `APPROVED` without the sequence anchor.

## 2. Run the chain probe (Part B)

**Why.** `test-harness/CHAIN-PROBE.md` states a hypothesis: the chain is verifiable from Process 03 onward and only asserted before it. That has been confirmed statically — Process 01 has no state file, Process 02's Control File contains zero occurrences of `sha256` — but never demonstrated by running.

**Do.** Pull one capability from Process 01 to Process 06 with six minimal artifacts, every approval marked `SIMULATED`, then fill the closure table.

**Evidence.** The closure table, with `CLOSED` / `ASSERTED` / `BROKEN` per link.

**Fails if.** Any link is marked `CLOSED` that only compares strings.

## 3. Write the Process 04 field contract — **done 2026-11-13**

**Why.** `templates/CONTROL-FIELDS-v1.yaml` covers Processes 05 and 06. Process 04 schema v4 has a larger event set — register initialization, receipts, aborts — and no field contract. Do this before anyone builds a Register writer, not after.

**Do.** Enumerate every v4 event type and its required keys. Reuse the shape of the v1 file, including a `known_drift` section.

**Evidence.** A fixture with one of each event type passes a v4 validator.

## 4. Add validators for P05 artifacts 02–05 — **02 done 2026-11-13, 03–05 open**

**Why.** Only artifact 01 is mechanically checked. Interaction patterns, state design, copy intent and accessibility requirements are prose-only, which is the condition that produced findings F-04, F-05 and F-11.

**Do.** One validator each, or one that covers all four. Start with the accessibility artifact: contrast pairs either have a resolved hex pair and a ratio or they do not.

**Evidence.** Each validator passes a correct artifact and fails a deliberately broken one.

## 5. Decide the P01–P03 hash binding — **done 2026-11-13**

**Why.** Three of six processes cannot produce evidence that survives a file edit. Process 01 has no canonical state file at all. This is a decision, not a bug fix: either those stages get Control Files with hash binding, or they are declared advisory and the kit stops claiming a six-stage verified chain.

**Do.** Decide, then either build it or write down that the chain is asserted before Process 03.

**Evidence.** A statement in `PROVENANCE.md` that a reader can act on.

## 6. Merge to main

**Blocked.** Merge authorization has not been granted. Two draft pull requests are open. Do not merge until at least one live gate has been exercised and its evidence recorded.

## Not yet

Processes 07 and 08 are charter-only. They stay that way until a real initiative reaches Process 06. Writing their contracts now would repeat the mistake Process 04 made: a large mechanism built before the three-tab model had run once.
