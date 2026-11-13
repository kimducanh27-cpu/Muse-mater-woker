# 02 — Interaction Pattern Library

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> Patterns are defined here once, then cited by ID. A screen may not describe bespoke interaction behaviour inline without a pattern entry.

## Rules for this artifact

- Every pattern has a stable `PAT-<NN>` ID and is defined before first use.
- "When not to use" is mandatory. A pattern without a refusal condition is a habit, not a decision.
- A pattern states the failure it prevents. If it prevents nothing, delete it.
- Patterns describe behaviour, not appearance. No component names, no animation curves, no colour.

## Pattern register

| Pattern ID | Name | When to use | When not to use | Failure it prevents | Used by screens |
|---|---|---|---|---|---|
| `PAT-01` | | | | | `SCREEN-…` |

## Pattern detail — `PAT-<NN>`

**Behaviour.** What happens, in what order, from the user's point of view.

**Preconditions.** What must already be true.

**Recovery.** What the user can do when it fails.

**Refusal condition.** The situation where this pattern is the wrong choice, and what to do instead.

**Cited by.** `SCREEN-<ID>` for each citing screen.

---

## Reserved patterns

Patterns defined but not yet cited. Each requires a reason and a decision ID if it stays reserved at Gate 2.

| Pattern ID | Reason reserved | Decision ID |
|---|---|---|
| `PAT-<NN>` | | `DEC-<NN>` |

## Citation check — required at the end of the artifact

| Pattern ID | Cited by count | Status |
|---|---|---|
| `PAT-<NN>` | `<n>` | CITED / RESERVED |

Every cited pattern ID must exist above. Every pattern above must be cited at least once or listed as reserved with a decision.
