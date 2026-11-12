# Tab 02 — Patterns, States, Content, Accessibility

You are running **Process 05 UX Design, Tab 02** in a fresh conversation.

## Before anything else

1. Read `.agents/skills/ux-design/SKILL.md` in full.
2. Re-verify both sources exactly as in Tab 01, including the Process 03 hash bound through Process 04.
3. Verify Gate 1: `APPROVED`, with a well-formed `GATE_1_APPROVED` event, `gate_1.approved_state_seq` equal to that event's `state_seq`, and every artifact hash in `gate_1.approved_artifacts` recomputed and matching.
4. Verify the Decision Log identity header, that `decision_log.latest_sha256` is non-null, and that the actual file hash matches it. Independently classify every entry: no `GATE_1`-affecting update may have occurred after the Gate 1 event.
5. Read `product/ux-design/01_SCREEN_UX_MODEL.md` in full.

If any check fails, reopen the affected gates, append `INVALIDATED` with expected and observed hashes, and stop.

## Your job

Produce four artifacts, in this order:

**`02_INTERACTION_PATTERNS.md`** from template `02`. Define patterns before citing them. Each pattern needs an ID, when to use, when not to use, and the failure it prevents. A pattern with no refusal condition is a habit.

**`03_STATE_EXPERIENCE.md`** from template `03`. Project the frozen Process 04 state matrix onto every screen. One row per applicable screen × state. Each row states what the user sees, understands and can do, plus the recovery affordance. Every failure-bearing state needs recovery or an approved decision that there is none.

**`04_CONTENT_AND_COPY_INTENT.md`** from template `04`. Content required per screen and the intent of every message. Intent only — never final wording. Every failure-bearing state needs a message intent or an approved decision that it is silent by design.

**`05_ACCESSIBILITY_REQUIREMENTS.md`** from template `05`. Record the target conformance level as a decision, then per-screen keyboard, focus order intent, announcement intent and minimum target size. Requirements, not tokens.

## What you must not do

- Do not add a state that the Process 04 matrix does not define. That is a Change Request to Process 04.
- Do not add a screen or a capability.
- Do not name a UI component anywhere in artifacts 02–05.
- Do not write a colour, font, size, spacing, radius or shadow value.
- Do not write final copy or guess a character budget.
- Do not edit artifacts 01 or 08's existing bytes. New decisions are appended, never rewritten.

## Gate 2

Run the set comparisons and show them explicitly, not as a claim:

| Comparison | Required result |
|---|---|
| SCREEN IDs in 01 vs frozen Process 04 inventory | identical sets |
| (screen, state) rows in 03 vs the applicable matrix projection | identical sets |
| Pattern IDs cited vs pattern IDs defined | closed, or reserved with a decision |
| Capabilities in frozen Process 03 scope vs capabilities served | complete, or approved deferral |
| Named components in 01–05 | zero |
| Colour, typography, spacing values in 01–05 | zero |

Then wait for exactly:

```
APPROVE UX SPEC
```

One Control File update: set `gate_2.approved_state_seq`, `gate_2.decision_log_sha256`, the coverage snapshot, and append `GATE_2_APPROVED` with path/hash pairs for 02–05. Read back and verify.

Stop after Gate 2. Do not start Tab 03.
