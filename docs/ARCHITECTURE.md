> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `42f615a`, 2026-11-13.

# How the kit is built

## The pipeline

```
01 Seed ──► 02 Discovery ──► 03 Definition ──► 04 App Flow ──► 05 UX ──► 06 Design Systems ──► 07 UI ──► 08 Validation
             (charter)        (charter)          (v4)           (v1)        (v1)              charter    charter
```

Each stage consumes the previous stage's **frozen** output and produces one frozen artifact. A stage that cannot verify its input stops with `NOT_VERIFIED`. It does not proceed on a guess.

## Three tabs per stage

Every defined process runs as three separate chat sessions:

| Tab | Owns | May write |
|---|---|---|
| 01 | The first half of the artifact | Its artifacts, Control events it owns, Decision Log entries for its gate |
| 02 | The second half | Its artifacts, Control events it owns |
| 03 | Independent review and the mechanical freeze | Review history, the draft, Control events for review and freeze |

Tab 03 runs in a clean context on purpose. A reviewer that shares the author's context is not independent, and the review would test nothing.

The tabs never hand off through chat. They hand off through files on disk. A tab that reads its own conversation history instead of the Control File is the failure mode the whole design exists to prevent.

## Where truth lives

| Question | Answer |
|---|---|
| What is the current state? | `product/<process>/00_*_CONTROL.md` |
| What was decided, and by whom? | The Decision Log, append-only |
| What is the frozen output? | The named artifact, hash recorded in the Control File |
| What rules apply? | `.agents/skills/<process>/SKILL.md` |
| What did we learn by running it? | `test-harness/runs/*.md` and `test-harness/FINDINGS.md` |

A Control File is YAML frontmatter plus prose. The YAML is state; the prose is explanation. Only the YAML is parsed.

## The state model

- `state_seq` is a monotonic counter. Every committed change increments it by one and appends one event to `event_log`.
- An event's key set is fixed by `templates/CONTROL-FIELDS-v1.yaml`. That file is normative; the prose tables in the templates are not.
- Gates bind hashes. `gate_1.approved_state_seq` must equal the `state_seq` of the event that approved it. A status of `APPROVED` with a null anchor is not an approval.
- Freeze copies the reviewed draft byte-for-byte and changes one line. The frozen hash lives in the Control File, never inside the frozen file.

## Repository layout

```
.agents/skills/          9 Skills — the normative contracts
templates/              56 templates, one set per process
prompts/                tab prompts, one directory per process
process-charters/       scope arguments for 05–08, and the admission test
product/<process>/      live workspace per process (empty — nothing has run)
upstream/               verbatim copies of external method, with provenance
test-harness/           probes, fixtures, validators, run reports
docs/                   this orientation pack
```

## Why validators exist

Four scripts, each born from a demonstrated failure:

| Script | Checks | Born from |
|---|---|---|
| `validate-control.py` | Control File frontmatter, event key sets, decision log hash, lifecycle consistency | An agent wrote `status_before` instead of `decision_status_before_update` and reported success |
| `validate-register.py` | Register event block hashes under the sentinel rule, chain contiguity | An agent wrote a digest that verified under nothing |
| `validate-ux-model.py` | Screen set equality, one primary action each, component audit | A word-list audit that failed correct prose |
| `apply-gate.py` | Applies one gate approval: exact-command check, artifact validation, event append, re-verify | Hand-written gate events produced F-06 and F-08 |

The pattern is consistent: prose was not enforced, a mechanical check was, and behaviour followed the check.

## What is deliberately absent

- No orchestrator. No agent calls another agent. The human moves between tabs.
- No code generation. The kit stops at a frozen interface specification.
- No runtime dependency for the process itself. The validators are development tools, not part of the workflow.
