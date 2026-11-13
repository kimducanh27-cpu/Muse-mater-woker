> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `78667ac`, 2026-11-13.

# How to update the docs pack

Six content files live in `docs/`. This is the seventh: the procedure for bringing them back into line. It is not content and it is not part of the pack a reader is meant to read first.

The six files are derived. They go stale the moment a commit lands.

## What this procedure is not

It is not a licence to rewrite. The structure of the six files is settled: what each one covers, and who reads it. An update changes **facts**, never shape. If a fact no longer fits the shape, that is a decision for the human, not a refactor for the agent.

## The prompt

Paste this into a fresh session with the repository checked out.

---

You are updating a derived documentation pack. It is not authoritative — the Control Files are — and it is written for a fresh agent session, not for a human reader.

Read `docs/UPDATE-PROMPT.md` in full before you start. It is this file.

**Step 1 — recompute the anchors. Do not remember them.**

```bash
git rev-parse --short HEAD
date -u +%Y-%m-%d
ls .agents/skills/*/SKILL.md | wc -l
find templates -name '*.md' -o -name '*.yaml' | wc -l
ls test-harness/validate-*.py | wc -l
grep -cE '^\| F-' test-harness/FINDINGS.md
grep -cE 'RE-PROBED' test-harness/FINDINGS.md
ls test-harness/runs/*.md | wc -l
```

Also read `test-harness/FINDINGS.md` in full: every status there is a fact the pack repeats, and a wrong status is the most damaging kind of staleness because it reads as reassurance.

**Step 2 — update the header line in all six files.**

```
> Generated from this repository at commit `<short HEAD>`, <YYYY-MM-DD>.
```

Do not touch the line above it. `Derived. Not authoritative.` is not decoration; it is the reason the pack is allowed to exist.

**Step 3 — update the facts, in this order.**

| File | What to recheck |
|---|---|
| `PRD.md` | The stage status table; the counts sentence; the "what does not exist" list |
| `ARCHITECTURE.md` | The pipeline diagram; the validator table; the repository layout |
| `DESIGN.md` | The platform block; the design-system rules; the tested-rule paragraph |
| `RULES.md` | The never/always lists; the validator commands; the gate command table |
| `TASKS.md` | Which tasks are done, which are blocked, and the order |
| `PROGRESS.md` | Done; broken-then-fixed with statuses; open items |

**Step 4 — never do these.**

- Do not claim a `NOT RUN` scenario is a `PASS`.
- Do not describe a product. No product exists. If one now does, say so with the artifact path that proves it, and stop — that is a structural change.
- Do not add a file to the pack. **Six content files is the number.** `UPDATE-PROMPT.md` and `HANDOFF.md` are operational, not content: one maintains the pack, the other carries session state. Neither is read first, and neither may grow into a seventh topic file.
- Do not soften a finding. If something is fixed by specification only, say that; it is different from fixed by re-running the probe.
- Do not edit a Control File, a Skill, a template, or anything under `test-harness/`. You are updating a description of them, not them.

**Step 5 — report before finishing.**

Print, in this order:

1. The old commit and the new commit.
2. Every number you changed, with its old and new value.
3. Every finding whose status you changed, with the reason.
4. Anything you could not verify, and why.
5. Any place where the pack and a Control File disagree — do not resolve it. Report it.

If nothing changed, say so and stop. A no-op update reported honestly is better than a rewrite that invents activity.

---

## Why the procedure is shaped this way

Every rule above came from a failure recorded in `test-harness/FINDINGS.md`.

Step 1 exists because an agent asked to "update the counts" will write plausible numbers. F-06 was an agent verifying an artifact against its own memory and reporting success. Recomputing is the only defence.

Step 2 exists because a pack without a commit anchor cannot be told from a current one. A reader has no way to know whether the numbers were true last week.

Step 4 exists because the failure mode of a documentation update is not an error — it is a confident, well-written sentence that is no longer true. F-03 was a required column with no possible source; it survived several readings before a probe found it.

Step 5 exists because the report is the only artefact a human can check without re-reading six files.

## The honest limitation

There is no validator for this pack. Three scripts check Control Files, Register chains and UX artifacts; none checks whether `PROGRESS.md` still tells the truth.

So this procedure is prose, and this repository has spent a day demonstrating that prose is not enforced. Treat the pack as a convenience that may be stale, never as a source. When it and a Control File disagree, the Control File wins and the pack is wrong.
