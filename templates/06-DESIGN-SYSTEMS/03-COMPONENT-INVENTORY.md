# 03 — Component Inventory

> Artifact of Process 06. Owner: Tab 02. Bound by Gate 2.
> Every component cites the frozen screens that require it. A component with no citing screen is not admitted.

## Rules for this artifact

- **Citing screens are mandatory.** At least one `SCREEN-` ID from the frozen Process 05 inventory. A component nobody needs is a component nobody will maintain.
- A citing screen that does not exist in the frozen inventory makes the entry `NOT_VERIFIED`.
- A component that exists only because Material 3 has one is speculative. Justify it against a screen or remove it.
- No placement, no layout, no composition. This artifact says what a component *is*, never where it *goes*.
- No final copy. Content limits are limits, not strings.

## Component entry

### `CMP-<NN>` — <component name>

| Field | Value |
|---|---|
| Component ID | `CMP-<NN>` |
| Purpose | One sentence: what job it does |
| Citing screens | `SCREEN-…`, `SCREEN-…` |
| Material 3 equivalent | Named, or `NONE` with rationale |
| Variants | |
| Sizes | |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | |
| Content limits | Maximum characters or items, and what happens beyond it |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| | | |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | | | | |
| focus | | | | |
| disabled | | | | |
| error | | | | |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?

---

## Inventory summary — required at the end of the artifact

| Component ID | Name | Variants | Citing screens | Cited by count |
|---|---|---|---|---|
| `CMP-<NN>` | | `<n>` | | `<n>` |

## Set checks — required at the end of the artifact

| Check | Result |
|---|---|
| Components with zero citing screens | must be `0` |
| Citing SCREEN IDs absent from the frozen Process 05 inventory | must be `0` |
| SCREEN IDs in the frozen inventory with no citing component | `<n>` — each needs a decision |
| Components with no "when not to use" statement | must be `0` |
| Components with an unstyled interaction state | must be `0` |
| Components defined | `<n>` |
| Components cited | `<n>` |
| Screens in source | `<n>` |
| Screens citing at least one component | `<n>` |

The two totals that must match at Gate 2: components defined = components cited; screens in source = screens citing at least one component.
