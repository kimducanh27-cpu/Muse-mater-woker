> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `78667ac`, 2026-11-13.

# Handoff

This file carries what a docs pack cannot: the state of a *session*, not the state of a repository. It is replaced, not updated. Everything durable is in the six content files beside it.

Written 2026-11-13. The `handoff` skill asks for `%TEMP%`; this lives in `docs/` on the user's instruction so it travels with the repo.

## What the previous session did

Two days of work, in one arc:

1. Corrected Process 04's remediation plan — the Register required each event block to carry a hash of that same block. ADR-P04-11 resolved it with a sentinel (`<HASH_OMITTED>`).
2. Wrote Process 05 (UX Design) and Process 06 (Design Systems) contracts from scratch.
3. Reconciled process charters and decision register.
4. Built `PROVENANCE.md` (24 rules labelled, 8 LOCAL decisions registered).
5. Built a probe harness and ran **12 probes** (10 run reports, 13 defects tracked).
6. Built mechanical checkers for all P05 artifacts (`validate-patterns.py`, `validate-state.py`, `validate-copy.py`, `validate-a11y.py`).
7. Exercised Gate 1 for real on `fixtures/probe-11` with human command `APPROVE SCREEN UX MODEL`.
8. Ran Chain Probe (Part B) pulling `CAP-01` through P01–P06; confirmed hypothesis (L1–L2 asserted, L3–L6 byte-closed).
9. Decided P01–P03 hash binding via decision L-8.

## Where things stand

| | |
|---|---|
| Branch | `pipeline/p05-p06`, HEAD `78667ac`, 44 commits ahead of `main` |
| Pull requests | #1 (P04, draft, base `main`), #2 (P05/P06, draft, stacked on #1) |
| Working tree | clean |
| Gates opened | **1** (on `fixtures/probe-11`) |
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

`docs/TASKS.md` task 6: Merge to main. All prerequisite tasks (1–5) are fully satisfied with verifiable evidence.
Merge authorization from the repository owner is required before proceeding.

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
