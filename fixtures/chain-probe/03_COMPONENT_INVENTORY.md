> SIMULATED — NOT ELIGIBLE DOWNSTREAM
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

### `CMP-01` — Draft Save Control

| Field | Value |
|---|---|
| Component ID | `CMP-01` |
| Purpose | Provides an explicit touch target and visual feedback to commit form state to persistent storage |
| Citing screens | `SCREEN-01` |
| Material 3 equivalent | Filled Button with progress indicator |
| Variants | Primary Elevated |
| Sizes | Medium (height 48dp) |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | Leading icon slot, text label slot, trailing status slot |
| Content limits | Label text maximum 24 characters; truncates with ellipsis if exceeded |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Container | required | `color.surface.base` (`#FDFBFF`) |
| Label text | required | `color.text.primary` (`#1A1C1E`) — measured contrast pair `CP-01` (15.8:1 on `color.surface.base`) |
| Icon | optional | `color.primary.base` (`#0061A4`) |
| Border | optional | `color.outline.subtle` (`#73777F`) |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `color.primary.container` | `color.text.primary` | none | elevated shadow 1 |
| focus | `color.primary.container` | `color.text.primary` | `color.primary.focus_ring` | outline 2dp |
| disabled | `color.surface.disabled` | `color.text.disabled` | none | flat |
| error | `color.error.container` | `color.error.text` | `color.error.border` | alert state |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use `CMP-01` for destructive or final irreversible actions such as deleting user accounts or submitting final applications; use dedicated confirmation dialogs or standard submission controls instead.

---

## Contrast pairs reference — measured

| Pair ID | Foreground token | Background token | Resolved hex | Ratio | Required | Result |
|---|---|---|---|---|---|---|
| `CP-01` | `color.text.primary` | `color.surface.base` | `#1A1C1E on #FDFBFF` | 15.8:1 | 4.5:1 | PASS |

---

## Inventory summary — required at the end of the artifact

| Component ID | Name | Variants | Citing screens | Cited by count |
|---|---|---|---|---|
| `CMP-01` | Draft Save Control | 1 | `SCREEN-01` | 1 |

## Set checks — required at the end of the artifact

| Check | Result |
|---|---|
| Components with zero citing screens | 0 |
| Citing SCREEN IDs absent from the frozen Process 05 inventory | 0 |
| SCREEN IDs in the frozen inventory with no citing component | 0 |
| Components with no "when not to use" statement | 0 |
| Components with an unstyled interaction state | 0 |
| Components defined | 1 |
| Components cited | 1 |
| Screens in source | 1 |
| Screens citing at least one component | 1 |

The two totals that must match at Gate 2: components defined = components cited (1 = 1); screens in source = screens citing at least one component (1 = 1).
