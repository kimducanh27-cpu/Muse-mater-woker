> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `7432476`, 2026-11-13.

# Handoff

This file carries what a docs pack cannot: the state of a *session*, not the state of a repository. It is replaced, not updated. Everything durable is in the six content files beside it.

Written 2026-11-13. The `handoff` skill asks for `%TEMP%`; this lives in `docs/` on the user's instruction so it travels with the repo.

## What the previous session did

Two days of work, in one arc:

1. Corrected Process 04's remediation plan — the Register required each event block to carry a hash of that same block. ADR-P04-11 resolved it with a sentinel (`<HASH_OMITTED>`).
2. Wrote Process 05 (UX Design) and Process 06 (Design Systems) contracts from scratch.
3. Found that the process charters and the decision register contradicted each other about whether implementation was authorised. Reconciled without rewriting the hashed plan.
4. Built `PROVENANCE.md` and discovered 16 of 23 rules are local invention.
5. Built a probe harness and ran **11 probes** against `agy` 1.5.6. Found **13 defects**. Closed 7 by re-running the probe, 5 by specification only.

The full account is in `test-harness/runs/` and `test-harness/FINDINGS.md`. Do not re-derive it.

## Where things stand

| | |
|---|---|
| Branch | `pipeline/p05-p06`, HEAD `7432476`, 40 commits ahead of `main` |
| Pull requests | #1 (P04, draft, base `main`), #2 (P05/P06, draft, stacked on #1) |
| Working tree | clean |
| Gates opened | **zero** |
| Scenarios passing | **zero** — 130 are `NOT RUN` |

## In flight

Three threads a fresh session would otherwise re-discover the hard way.

**1. The archive protocol has never worked.** A fold/archive system exists outside this repository — `SỔ GẤP.md` ledgers, 18-field blocks, pushed to `kimducanh27-cpu/context-chatgpt-data`. The last attempt was refused twice over: no `SANITIZED_RAW_SOURCE` excerpt was pasted, and the data repo returns **404** to both the public API and the GitHub connector, so the push would fail even with an excerpt. Before any future fold: confirm that repo exists and is reachable.

**2. Meta Muse can run `agy`, but nothing was tested there.** The user's VM was confirmed to run shell commands and `agy` 1.5.6 is installed. Every probe in this session ran locally on Windows instead. `test-harness/MUSE-PROMPT.md` is ready and untested.

**3. Process 04's Skill does not fit in one agent turn.** Reading the 500-line Skill plus a 15 KB Register and acting on it reached step 46 of 71 with no result, killed at 300 s. Any future P04 probe must be decomposed or run multi-turn.

## Environment gotchas

Two that cost real time and will cost it again.

**Heredoc mangles backslashes.** Running `python - <<'PY' ... PY` through this shell silently rewrites `\n` inside string literals — observed as `/n` and `//n`. It produced two identical `AssertionError: anchor not found` failures on files whose bytes were correct, and the cause was invisible in the output. **Do not put `\n` in a heredoc.** Either use triple-quoted strings with real line breaks, or write the script with a file-writing tool and execute the file.

**`/tmp` does not mean the same thing to bash and to Windows Python.** `cp` into `/tmp` succeeds, then `pathlib.Path("/tmp/...")` resolves to `\tmp\...` and raises `FileNotFoundError`, while a script argument with the same path is converted correctly. Use a workspace-relative scratch directory.

## First action

`docs/TASKS.md` task 1: open one gate for real. Every Control File still reads `gate_1: PENDING` with an empty `event_log`. The three validators check consistent workspaces; not one has ever checked a transition.

Nothing else in this repository is worth doing before that.

## Suggested skills

| Skill | When |
|---|---|
| `grilling` | Before any structural decision. It caught the six-file naming problem before it was built. |
| `verification-before-completion` | Before claiming anything works. Every finding in this session came from claiming success too early. |
| `systematic-debugging` | If a probe stalls with no result event. Three runs were lost to that before the cause was found. |
| `handoff` | At the end of the next session, to replace this file. |

## What not to do

- Do not write a product PRD. No product exists.
- Do not claim a `NOT RUN` scenario passed.
- Do not add a seventh content file. Six is the number; `UPDATE-PROMPT.md` and this file are operational, not content.
- Do not trust this file over a Control File.
