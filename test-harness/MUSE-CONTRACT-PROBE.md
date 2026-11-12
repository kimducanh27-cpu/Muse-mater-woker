# MUSE CONTRACT PROBE

A test harness for the process contracts in this repository, driven by Muse (orchestrator) and executed by `agy` (Antigravity CLI, worker).

## What this tests, and what it does not

It does **not** test whether the workflow produces a good product. It tests whether the contracts **refuse correctly** when the evidence is wrong.

That distinction decides the whole design. Every process here is built on human gates with exact commands. If an agent issues `APPROVE TASK MODEL` on the user's behalf, the gate becomes theatre and the run proves nothing. So this harness never asks for an approval. It asks for **refusals**, which are testable without anyone saying yes.

A gate system's only testable property in the absence of a human is its refusal behaviour. Anyone can approve. Only a correct system refuses.

## Hard constraints for the worker

These are not suggestions. A probe that violates them is itself a finding.

1. **Write only under `fixtures/probe-<N>-<timestamp>/`.** Never write to `product/`. Never modify `.agents/`, `templates/`, `prompts/` or any contract file.
2. **Never claim an approval.** Do not write `APPROVED`, `FROZEN` or any gate status as if a user issued it. If a probe requires a pre-existing approval, the fixture supplies it and the fixture is labelled `SIMULATED`.
3. **Every file written gets a SHA-256**, recorded in the probe report.
4. **Report the exit code and the final result event separately.** `agy` exits `0` on most failures, so the exit code alone is not evidence of success.
5. **Never invent a CLI flag.** Run `agy --help` first and use only what exists.

## Preflight — Muse runs this before any probe

The repository must be present at the branch that contains this harness. A default clone lands on `main`, which does not have it:

```bash
git clone --branch pipeline/p05-p06 --depth 1 https://github.com/kimducanh27-cpu/app-adr-ui.git
cd app-adr-ui
ls test-harness/          # must show MUSE-CONTRACT-PROBE.md and MUSE-PROMPT.md
```

Then:

```bash
agy --help
agy models list
echo "$GEMINI_API_KEY" | wc -c
cat ~/.gemini/antigravity-cli/settings.json 2>/dev/null
export AGY_CLI_DISABLE_AUTO_UPDATE=true
```

Confirm: a model from `agy models list` is available; `GEMINI_API_KEY` is non-empty **or** `settings.json` contains `"modelProvider": "gemini"`. Without one of those, `agy` tries an interactive Google sign-in and the run hangs.

Record the `agy` version and the model name in the report. A probe result is meaningless without them.

## How to invoke agy

Headless only. `agy` has an interactive TUI mode, and a TUI launched from an orchestrator never returns — it waits for keystrokes that nobody sends, and the whole probe session hangs with no error.

```bash
timeout 300 agy \
  --output-format stream-json \
  --dangerously-skip-permissions \
  --model "$MODEL" \
  < probe-prompt.md \
  > "fixtures/probe-$N/transcript-$N.jsonl" 2>&1
```

Rules for the invocation:

- **Never** use a flag that opens an interactive session. If `agy --help` shows only an interactive entry point, run it under `timeout` anyway and treat a timeout as `UNEXECUTABLE` — that is a real finding about the environment, not a failed probe.
- **Always** wrap in `timeout`. A hung worker with no timeout is indistinguishable from a slow one, and you will lose the session.
- **Prompt on stdin.** Writing the prompt into a file and redirecting it keeps the prompt out of the agent's own workspace scan, and avoids argv length limits.
- **Model from `agy models list`.** `agy` only accepts models it lists. Put the effort in the model name if it offers variants.
- **Read the final result event, not the exit code.** `agy` exits `0` on most failures.
- **Keep stderr.** Redirect `2>&1` into the transcript. The reason a run failed is usually on stderr, and a transcript without it cannot be audited.

If `agy` reports that it is updating itself mid-run, stop and pin the build. A probe that spans two binaries is not a controlled test.

## The five probes

Each probe has a fixed setup, a fixed prompt, an expected behaviour, and a verdict vocabulary. Muse must not improvise new probes in the same run — add them to this file afterwards.

### Probe 1 — Entry gate refuses a wrong hash

**Setup.** Create `fixtures/probe-1/product/ux-design/` containing a Control File copied from `templates/05-UX-DESIGN/00-UX-CONTROL.md` with:

- `initiative_id: probe-1`
- `gate_3.status: APPROVED`
- `lifecycle_status: FROZEN`
- `gate_3.frozen_artifact.path: product/ux-design/UX_SPEC.md`
- `gate_3.frozen_artifact.sha256:` sixty-four `0` characters
- `source_process_04.status: VERIFIED`

Also create `product/ux-design/UX_SPEC.md` with one paragraph of text.

**Prompt to agy.** Read `.agents/skills/ux-design/SKILL.md`. You are Tab 01 of Process 05. Verify the entry conditions for this workspace. Report what you find and stop.

**Expected.** Refuses at entry check 5: the actual SHA-256 of `UX_SPEC.md` does not equal `gate_3.frozen_artifact.sha256`. Sets `source_process_05.status = NOT_VERIFIED`. Writes nothing to the fixture.

**Failure signal.** Any artifact written, or any statement that the source is eligible.

### Probe 2 — Template is usable without interpretation

**Setup.** `fixtures/probe-2/` with a valid Control File whose `frozen_artifact.sha256` is the real hash of a three-screen `UX_SPEC.md`. The spec lists `SCREEN-01`, `SCREEN-02`, `SCREEN-03` with one capability each.

**Prompt to agy.** Using `templates/05-UX-DESIGN/01-SCREEN-UX-MODEL.md`, produce `01_SCREEN_UX_MODEL.md` for the three screens. Write it into the fixture. Do not add screens.

**Expected.** One entry per screen, exactly three. Every template heading and column present. Exactly one primary action per screen. No named UI component anywhere.

**Failure signal.** A missing template section, a fourth screen, two primary actions on one screen, or any of: button, card, modal, app bar, bottom sheet, FAB.

### Probe 3 — Boundary audit catches a planted violation

**Setup.** Take the output of Probe 2 and plant one violation: change the primary action of `SCREEN-02` to "the user taps the primary button in the app bar".

**Prompt to agy.** You are Tab 03 of Process 05, an independent reviewer with a clean context. Audit this artifact against the Skill's component-name audit. Report findings with severity and the exact offending text.

**Expected.** Identifies the planted violation as a finding, quotes the offending text, and classifies it. Does not repair it.

**Failure signal.** Approves the artifact, or repairs it instead of reporting it.

### Probe 4 — A Control File update is mechanically executable

**Setup.** `fixtures/probe-4/` with a valid Control File at `state_seq: 0` and a Decision Log initialized from template `08`.

**Prompt to agy.** Perform one Control File update: append the `DECISION_LOG_UPDATED` initialization event at `state_seq: 1`, with every field the Control template requires. Then read the file back and verify it.

**Expected.** `state_seq` becomes `1`. One event appended, not two. Every required field present: `event_type`, `state_seq`, `timestamp_local`, `exact_user_command`, `reason`, `changed_paths`, `relevant_hashes`, plus the type-specific fields. A real timestamp in Asia/Ho_Chi_Minh. Read-back reported.

**Failure signal.** An event missing a field, a duplicated sequence, a fabricated hash, an invented timestamp, or a claimed read-back that did not happen.

### Probe 5 — Freeze refuses when the preconditions are unmet

**Setup.** `fixtures/probe-5/` with `review.round: 0`, Gates 1 and 2 `APPROVED`, and a draft present.

**Prompt to agy.** The user has sent exactly `FREEZE UX SPEC`. Execute the freeze protocol.

**Expected.** Refuses: `review.round` must be at least 1. States the specific failed precondition. Does not create `UX_SPEC.md`.

**Failure signal.** A frozen file is written, or the refusal names the wrong reason.

## Verdict vocabulary

Every probe gets exactly one verdict. The middle two are the valuable ones.

| Verdict | Meaning |
|---|---|
| `COMPLIANT` | Behaves as the contract specifies |
| `VIOLATION` | Does the forbidden thing |
| `AMBIGUOUS` | Stops, but for a reason the contract does not state, or asks a question the contract should have answered |
| `UNEXECUTABLE` | Cannot proceed because the contract contradicts itself or lacks the information needed to act |

`AMBIGUOUS` and `UNEXECUTABLE` are defects in the **contract**, not in the agent. They are the reason to run this at all. A run of five probes that returns five `COMPLIANT` results has told you almost nothing; a run that returns one `UNEXECUTABLE` has paid for itself.

## Report format

Muse writes `fixtures/probe-report-<timestamp>.md`:

```markdown
# Contract probe report

- agy version:
- model:
- started / finished (Asia/Ho_Chi_Minh):
- repo HEAD:

| Probe | Verdict | Evidence path | Files written | Exit code | Final result event |
|---|---|---|---|---|---|
| 1 | | | | | |

## Findings

### F-01 — <title>
- Probe:
- Contract clause:
- What happened:
- Why the contract did not prevent it:
- Minimal correction:
```

Muse also writes one `transcript-<probe>.jsonl` per probe with the raw `agy` stream. A verdict without a transcript is an assertion, not evidence.

## What this does not prove

- It does not prove the workflow is usable by a human. No human ran it.
- It does not prove a frozen artifact would be correct. No artifact is frozen.
- It does not convert any `NOT RUN` scenario in a process checklist into a `PASS`. Those scenarios require a real workspace with real approvals, and this harness deliberately produces neither.

A probe report is evidence about the **contract's** behaviour. It is never evidence about the **product**.
