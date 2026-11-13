> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `7432476`, 2026-11-13.

# What this repository is

A **process kit**, not an application. It contains no product code, no UI and no user. It defines how an AI agent and a human move a software idea from a raw thought to a frozen interface specification, in six gated stages, without the agent inventing decisions the human has not made.

Read this file first. It is the one-page answer to "what am I looking at".

## The problem it solves

An agent asked to "design an Android app" will produce something. It will be plausible, internally consistent, and untraceable. It will invent users, invent features, and skip the decisions that are expensive to make and easy to skip.

This kit makes those decisions visible and ordered. Every stage owns one frozen artifact. Every stage has a gate the human must open with an exact command. Every artifact carries a hash so a later stage can tell whether it is looking at what was approved.

## Who it is for

One person directing an agent across several chat sessions. The human decides; the agent executes and records. The agent may refuse. It may not approve.

If two people are reviewing, the gate model still works, but the exact-command protocol assumes one approver.

## What exists

| Stage | Name | Status |
|---|---|---|
| 01 | Seed | contract exists |
| 02 | Product Discovery | contract exists |
| 03 | Product Definition | contract exists |
| 04 | App Flow | contract exists, schema v4 |
| 05 | UX Design | contract exists, schema v1 |
| 06 | Design Systems | contract exists, schema v1 |
| 07 | UI Design | charter only |
| 08 | Validation | charter only |

Nine Skills, 57 templates, five checking scripts, thirteen recorded findings.

## What does not exist

- **No product.** No initiative has run end to end. There is no `PRODUCT_DEFINITION.md` for any real idea, no frozen App Flow, no frozen UX Spec, no design system.
- **No live gate.** No approval command has ever been issued. No Control File event has ever been written by a real tab.
- **No runtime evidence.** 130 checklist scenarios across Processes 04–06 are `NOT RUN`. Eleven probes have executed pieces of the machinery; none converted a scenario into a `PASS`.

## What this is not for

- **Not a code generator.** It stops at a frozen interface specification. No component code, no theme file, no screen implementation.
- **Not a substitute for a designer.** It orders and records decisions. It does not make them, and a gate that nobody with taste opens produces a well-documented bad decision.
- **Not for a team.** One approver, exact commands typed by that person. Two people reviewing still works; a committee does not, because the protocol assumes one voice per gate.
- **Not a compliance framework.** A hash proves byte identity. It does not prove the artifact is correct, complete, or usable.
- **Not proven.** Nothing has run end to end. Treat every claim in this pack as a design intention until a live gate produces evidence.

## The honest one-liner

The kit is well specified and unproven. Six stages of contract exist; not one of them has been used to produce something a user could touch.

If you are a new session picking this up: read `docs/PROGRESS.md` for what is actually done, `docs/TASKS.md` for what to do next, and `docs/RULES.md` before writing anything.
