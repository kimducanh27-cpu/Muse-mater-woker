# Tab 02 — Tokens, Components, Accessibility

You are running **Process 06 Design Systems, Tab 02** in a fresh conversation.

## Before anything else

1. Read `.agents/skills/design-system/SKILL.md` in full.
2. Re-verify both sources exactly as in Tab 01.
3. Verify Gate 1: `APPROVED`, with a well-formed `GATE_1_APPROVED` event, `gate_1.approved_state_seq` equal to that event's `state_seq`, and every hash in `gate_1.approved_artifacts` recomputed.
4. Verify the Decision Log identity, a non-null `decision_log.latest_sha256`, and that the actual hash matches. Classify every entry: no `GATE_1`-affecting update after the Gate 1 event.
5. Read `01_DESIGN_FOUNDATIONS.md` and `product/ux-design/UX_SPEC.md` in full.

If any check fails, reopen the affected gates, append `INVALIDATED` with expected and observed hashes, and stop.

## Your job

Three artifacts, in this order:

**`02_TOKEN_CONTRACT.md`** from template `02`. Three layers — primitive, semantic, component. A component token may reference only a semantic token. A semantic token must name a role; "blue" is a name, "action.primary" is a role. Record explicit prohibitions, because a token with no forbidden use becomes a suggestion.

**`03_COMPONENT_INVENTORY.md`** from template `03`. Every component cites at least one `SCREEN-` ID from the frozen UX spec. For each: purpose, anatomy, variants, sizes, every interaction state styled, slots, content limits, and a mandatory "when not to use this".

**`04_COMPONENT_ACCESSIBILITY.md`** from template `04`. Measure every contrast pair from the resolved primitive values. A ratio without a hex pair and a stated method is not a measurement. Record target size in dp, focus visibility, and announcement intent per component.

## The admission rule

A component exists only if a frozen screen requires it. Not because Material 3 has one, not because a future screen might need it, not because the library feels incomplete without it.

If a screen needs something the system cannot express, you have two honest options: add the component with that screen cited, or record a decision explaining why the screen is served by composition instead. Silently omitting the screen is the one option that fails Gate 2.

## What you must not do

- Do not place, arrange or size components on a screen. No layout, no regions, no composition.
- Do not write final copy. Content limits are limits, not strings.
- Do not write code, Compose or theme files.
- Do not edit artifacts 01 or 07's existing bytes.
- Do not add a screen, a state or a capability.

## Gate 2

Run the set comparisons and show the compared IDs, not a claim:

| Comparison | Required |
|---|---|
| Components with zero citing screens | `0` |
| Citing SCREEN IDs absent from the frozen inventory | `0` |
| Screens citing at least one component | = screens in source |
| Component tokens referencing a primitive | `0` |
| Semantic tokens without a role statement | `0` |
| Contrast pairs measured | = pairs required |
| Contrast pairs failing | `0` |
| Colour-only state signals | `0` |
| Screen layout, placement or composition present | `0` |
| Final copy, code or image present | `0` |

Then wait for exactly:

```
APPROVE COMPONENT LIBRARY
```

One Control update: set `gate_2.approved_state_seq`, `gate_2.decision_log_sha256`, the coverage snapshot, and append `GATE_2_APPROVED` with path/hash pairs for 02–04. Read back and verify.

Stop after Gate 2. Do not start Tab 03.
