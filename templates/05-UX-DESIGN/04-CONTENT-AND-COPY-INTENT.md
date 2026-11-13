# 04 — Content and Copy Intent

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> What content each screen requires, and the intent of each message. **Never final wording.** Final strings are composed in Process 07 against real layout constraints.

## Rules for this artifact

- Intent, not copy. "Tell the user the payment failed and that no money moved" is intent. "Payment failed. You have not been charged." is Process 07's job.
- Every message states its **job**: what the user must understand or do after reading it.
- Every message states its **tone constraint** and its **prohibited implication**. A failure message must not imply data loss when none occurred; a destructive confirmation must not imply reversibility.
- Character budgets are set in Process 07, not here. Do not guess a length.
- No placeholder that could be mistaken for approved copy.

## Content requirements by screen

| Screen ID | Content element | Required or optional | Source of truth | Notes |
|---|---|---|---|---|
| `SCREEN-…` | | REQUIRED / OPTIONAL | | |

## Message intent register

| Message ID | Screen ID | State ID | Trigger | Job of the message | Tone constraint | Must not imply |
|---|---|---|---|---|---|---|
| `MSG-…` | `SCREEN-…` | `STATE-…` | | | | |

## Content that must never be shown

| Content | Why prohibited | Scope |
|---|---|---|
| | | All screens / specific screen |

Typical entries: internal identifiers, raw error codes, partial data that implies completeness, counts that may be stale.

## Coverage check — required at the end of the artifact

| Screen ID | Required content elements | Message intents defined | States with a message | States with no message, and why |
|---|---|---|---|---|
| `SCREEN-…` | `<n>` | `<n>` | `<n>` | |

Every failure-bearing state in artifact 03 must have at least one message intent, or an approved decision stating that the state is silent by design.
