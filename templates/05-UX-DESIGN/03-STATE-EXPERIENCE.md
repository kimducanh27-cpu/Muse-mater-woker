# 03 — State Experience

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> One row per screen × state that applies to that screen, projected from the frozen Process 04 state matrix.

## Rules for this artifact

- The state space belongs to Process 04. This artifact may not add a state. A genuinely missing state is a Change Request to Process 04.
- Every row states what the user **sees**, **understands** and **can do** — three different things. "Shows an error" fails all three.
- Every failure-bearing state needs a recovery affordance, or an approved decision that says there is none and why.
- No component names, no colour, no wording. Message intent belongs to artifact 04.

## Projection rule

A state applies to a screen when the frozen Process 04 matrix marks it applicable, or when the screen's transition set can produce it. Record the source of the projection:

| Projection source | Meaning |
|---|---|
| `P04-MATRIX` | The Process 04 matrix names this screen for this state |
| `P04-TRANSITION` | A transition into this screen can produce this state |
| `P04-EXPLICIT-EXCLUSION` | Process 04 excluded this state; the rationale must be quoted |

## Matrix

| Screen ID | State ID | Source | User sees | User understands | User can do | Recovery affordance | Pattern |
|---|---|---|---|---|---|---|---|
| `SCREEN-…` | `STATE-…` | `P04-MATRIX` | | | | | `PAT-…` |

## Non-recoverable states — explicit register

States where recovery is genuinely impossible or out of scope. Each needs an approved decision; silence is a defect.

| Screen ID | State ID | Why recovery is impossible | Decision ID |
|---|---|---|---|
| `SCREEN-…` | `STATE-…` | | `DEC-…` |

## Coverage check — required at the end of the artifact

| Screen ID | States applicable in P04 | Rows present | Missing |
|---|---|---|---|
| `SCREEN-…` | `<n>` | `<n>` | `<list or none>` |

**Totals.** Applicable screen-state pairs: `<n>`. Rows present: `<n>`. Non-recoverable states with a decision: `<n>`. Rows for states not in Process 04: `0` (any non-zero value blocks Gate 2).
