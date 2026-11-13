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

### `CMP-01` — Draft List Item Card

| Field | Value |
|---|---|
| Component ID | `CMP-01` |
| Purpose | Displays draft identifier, status, and content preview summary within the draft collection, enabling selection to open. |
| Citing screens | `SCREEN-01` |
| Material 3 equivalent | Card (`ElevatedCard` / `OutlinedCard`) |
| Variants | elevated, outlined |
| Sizes | standard |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | leading (status icon/indicator), title, preview (snippet text), trailing (action affordance) |
| Content limits | Title: max 120 chars (single-line or truncated); Preview: max 240 chars (multi-line clamp with ellipsis beyond limit) |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Container surface | Required | `comp.draft-list-item.container.color`, `comp.draft-list-item.container.elevation`, `comp.draft-list-item.container.radius` |
| Title text | Required | `comp.draft-list-item.text.title.color`, `comp.draft-list-item.text.title.font` |
| Status indicator | Required | `comp.draft-list-item.status.color` |
| Preview text | Optional | `comp.draft-list-item.text.preview.color`, `comp.draft-list-item.text.preview.font` |
| Trailing affordance | Optional | `comp.draft-list-item.affordance.color` |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `sys.color.surface.container` | `sys.color.text.primary` | `sys.color.outline.subtle` | `sys.color.action.secondary` |
| hover | `sys.color.surface.container-high` | `sys.color.text.primary` | `sys.color.outline.subtle` | `sys.color.action.secondary` |
| focus | `sys.color.surface.container` | `sys.color.text.primary` | `sys.color.outline.focus` | `sys.color.action.primary` |
| pressed | `sys.color.surface.container-highest` | `sys.color.text.primary` | `sys.color.outline.subtle` | `sys.color.action.primary` |
| disabled | `sys.color.surface.disabled` | `sys.color.text.disabled` | `sys.color.outline.disabled` | `sys.color.action.disabled` |
| loading | `sys.color.surface.container` | `sys.color.text.placeholder` | `sys.color.outline.subtle` | `sys.color.action.disabled` |
| error | `sys.color.surface.container` | `sys.color.text.primary` | `sys.color.outline.error` | `sys.color.action.error` |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use as an action button or generic card container. For document composition or multi-line text input, use `CMP-04` (Text Area / Editor).

---

### `CMP-02` — Action Button

| Field | Value |
|---|---|
| Component ID | `CMP-02` |
| Purpose | Triggers an immediate affirmative user action or recovery flow (e.g., create new draft, retry save). |
| Citing screens | `SCREEN-01`, `SCREEN-02` |
| Material 3 equivalent | `Button` (`FilledButton` / `TonalButton` / `OutlinedButton`) |
| Variants | primary-filled, secondary-tonal, outlined |
| Sizes | compact, standard |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | leading-icon (optional), label (required) |
| Content limits | Label: max 30 characters; text wraps to single line and truncates with ellipsis if container constrained |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Container background | Required | `comp.button.container.color`, `comp.button.container.radius` |
| Icon | Optional | `comp.button.icon.color` |
| Text label | Required | `comp.button.label.color`, `comp.button.label.font` |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `sys.color.action.primary` | `sys.color.text.inverse` | `sys.color.outline.none` | `sys.color.action.primary` |
| hover | `sys.color.action.primary-hover` | `sys.color.text.inverse` | `sys.color.outline.none` | `sys.color.action.primary-hover` |
| focus | `sys.color.action.primary` | `sys.color.text.inverse` | `sys.color.outline.focus` | `sys.color.action.primary` |
| pressed | `sys.color.action.primary-pressed` | `sys.color.text.inverse` | `sys.color.outline.none` | `sys.color.action.primary-pressed` |
| disabled | `sys.color.action.disabled` | `sys.color.text.disabled` | `sys.color.outline.none` | `sys.color.action.disabled` |
| loading | `sys.color.action.primary` | `sys.color.text.inverse` | `sys.color.outline.none` | `sys.color.action.primary` |
| error | `sys.color.action.error` | `sys.color.text.inverse` | `sys.color.outline.error` | `sys.color.action.error` |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use for static status indicators or navigation backlinks without primary action intent. For pure back navigation, use `CMP-06` (Navigation Icon Button).

---

### `CMP-03` — Status Indicator Badge

| Field | Value |
|---|---|
| Component ID | `CMP-03` |
| Purpose | Communicates discrete system, draft persistence, or save synchronization states (e.g., saving, saved, save-failed, collection status). |
| Citing screens | `SCREEN-01`, `SCREEN-02` |
| Material 3 equivalent | `Badge` / `AssistChip` (read-only indicator) |
| Variants | neutral, success, warning, error |
| Sizes | compact, standard |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | status-dot (required), status-label (required) |
| Content limits | Label: max 25 characters; single line only, strictly no wrap |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Badge container | Required | `comp.badge.container.color`, `comp.badge.container.radius` |
| Status dot indicator | Required | `comp.badge.indicator.color` |
| Status label | Required | `comp.badge.label.color`, `comp.badge.label.font` |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `sys.color.surface.container-low` | `sys.color.text.secondary` | `sys.color.outline.subtle` | `sys.color.indicator.neutral` |
| hover | `sys.color.surface.container` | `sys.color.text.secondary` | `sys.color.outline.subtle` | `sys.color.indicator.neutral` |
| focus | `sys.color.surface.container-low` | `sys.color.text.secondary` | `sys.color.outline.focus` | `sys.color.indicator.neutral` |
| pressed | `sys.color.surface.container-high` | `sys.color.text.secondary` | `sys.color.outline.subtle` | `sys.color.indicator.neutral` |
| disabled | `sys.color.surface.disabled` | `sys.color.text.disabled` | `sys.color.outline.disabled` | `sys.color.indicator.disabled` |
| loading | `sys.color.surface.container-low` | `sys.color.text.secondary` | `sys.color.outline.subtle` | `sys.color.indicator.animated` |
| error | `sys.color.surface.error-container` | `sys.color.text.error` | `sys.color.outline.error` | `sys.color.indicator.error` |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use as an interactive action trigger. For actionable notifications that provide a retry button, pair with or use `CMP-05` (Notification Banner) or `CMP-02` (Action Button).

---

### `CMP-04` — Document Editor Text Area

| Field | Value |
|---|---|
| Component ID | `CMP-04` |
| Purpose | Enables composing and modifying draft document text content with focus and input state handling. |
| Citing screens | `SCREEN-02` |
| Material 3 equivalent | `TextField` (`BasicTextField` / `OutlinedTextField`) |
| Variants | frameless, outlined |
| Sizes | flexible (fills editing viewport) |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | input-content (required), placeholder (optional) |
| Content limits | Scalable document buffer; max single draft input 100,000 characters; scrolls vertically when exceeding bounds |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Input canvas container | Required | `comp.editor.container.color`, `comp.editor.container.padding` |
| Placeholder text | Optional | `comp.editor.placeholder.color`, `comp.editor.placeholder.font` |
| Draft text body | Required | `comp.editor.text.color`, `comp.editor.text.font` |
| Focus indicator | Required | `comp.editor.cursor.color`, `comp.editor.outline.focus` |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `sys.color.surface.base` | `sys.color.text.primary` | `sys.color.outline.none` | `sys.color.cursor.primary` |
| hover | `sys.color.surface.base` | `sys.color.text.primary` | `sys.color.outline.subtle` | `sys.color.cursor.primary` |
| focus | `sys.color.surface.base` | `sys.color.text.primary` | `sys.color.outline.focus` | `sys.color.cursor.active` |
| pressed | `sys.color.surface.base` | `sys.color.text.primary` | `sys.color.outline.focus` | `sys.color.cursor.active` |
| disabled | `sys.color.surface.disabled` | `sys.color.text.disabled` | `sys.color.outline.none` | `sys.color.cursor.none` |
| loading | `sys.color.surface.base` | `sys.color.text.secondary` | `sys.color.outline.none` | `sys.color.cursor.disabled` |
| error | `sys.color.surface.base` | `sys.color.text.primary` | `sys.color.outline.error` | `sys.color.cursor.error` |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use for single-line constrained inputs or read-only preview snippets. Use `CMP-01` (Draft List Item Card) for preview display.

---

### `CMP-05` — Notification Banner

| Field | Value |
|---|---|
| Component ID | `CMP-05` |
| Purpose | Displays error recovery or feedback notifications (e.g., save failure alerts with retry context, system status notices). |
| Citing screens | `SCREEN-01`, `SCREEN-02` |
| Material 3 equivalent | `Snackbar` / `Banner` |
| Variants | error, informational |
| Sizes | standard |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | icon (optional), message (required), action-slot (optional) |
| Content limits | Message: max 160 characters; action: max 1 action slot |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Banner surface | Required | `comp.banner.container.color`, `comp.banner.container.radius` |
| Notification icon | Optional | `comp.banner.icon.color` |
| Message body | Required | `comp.banner.message.color`, `comp.banner.message.font` |
| Action container slot | Optional | `comp.banner.action.slot` |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `sys.color.surface.error-container` | `sys.color.text.error` | `sys.color.outline.error` | `sys.color.action.error` |
| hover | `sys.color.surface.error-container` | `sys.color.text.error` | `sys.color.outline.error` | `sys.color.action.error-hover` |
| focus | `sys.color.surface.error-container` | `sys.color.text.error` | `sys.color.outline.focus` | `sys.color.action.error` |
| pressed | `sys.color.surface.error-container` | `sys.color.text.error` | `sys.color.outline.error` | `sys.color.action.error-pressed` |
| disabled | `sys.color.surface.disabled` | `sys.color.text.disabled` | `sys.color.outline.disabled` | `sys.color.action.disabled` |
| loading | `sys.color.surface.error-container` | `sys.color.text.secondary` | `sys.color.outline.error` | `sys.color.action.disabled` |
| error | `sys.color.surface.error-container` | `sys.color.text.error` | `sys.color.outline.error-bold` | `sys.color.action.error` |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use for passive, persistent state tags. For simple non-alert status indicators, use `CMP-03` (Status Indicator Badge).

---

### `CMP-06` — Navigation Icon Button

| Field | Value |
|---|---|
| Component ID | `CMP-06` |
| Purpose | Provides directional navigation affordance to return to the draft list from the editor. |
| Citing screens | `SCREEN-02` |
| Material 3 equivalent | `IconButton` |
| Variants | standard |
| Sizes | compact (48x48dp touch target) |
| Interaction states | default / hover / focus / pressed / disabled / loading / error |
| Slots | icon (required) |
| Content limits | Single glyph/icon; strictly no textual label inside container |

**Anatomy.** The parts, in order, with which are required and which are optional.

| Part | Required | Token references |
|---|---|---|
| Touch target container | Required | `comp.icon-button.container.color`, `comp.icon-button.container.radius` |
| Navigation icon glyph | Required | `comp.icon-button.icon.color` |

**State matrix.** One row per state. A state that exists but is unstyled is a defect.

| State | Container | Content | Border | Affordance |
|---|---|---|---|---|
| default | `sys.color.surface.transparent` | `sys.color.action.nav` | `sys.color.outline.none` | `sys.color.action.nav` |
| hover | `sys.color.surface.container-high` | `sys.color.action.nav` | `sys.color.outline.none` | `sys.color.action.nav` |
| focus | `sys.color.surface.transparent` | `sys.color.action.nav` | `sys.color.outline.focus` | `sys.color.action.nav` |
| pressed | `sys.color.surface.container-highest` | `sys.color.action.nav` | `sys.color.outline.none` | `sys.color.action.nav` |
| disabled | `sys.color.surface.transparent` | `sys.color.action.disabled` | `sys.color.outline.none` | `sys.color.action.disabled` |
| loading | `sys.color.surface.transparent` | `sys.color.action.disabled` | `sys.color.outline.none` | `sys.color.action.disabled` |
| error | `sys.color.surface.transparent` | `sys.color.action.error` | `sys.color.outline.error` | `sys.color.action.error` |

**When not to use this component.** Mandatory. What is the wrong situation for it, and what is used instead?
Do not use for actions requiring explicit label text (such as "Create draft" or "Retry save"). Use `CMP-02` (Action Button) instead.

---

## Inventory summary — required at the end of the artifact

| Component ID | Name | Variants | Citing screens | Cited by count |
|---|---|---|---|---|
| `CMP-01` | Draft List Item Card | 2 | `SCREEN-01` | 1 |
| `CMP-02` | Action Button | 3 | `SCREEN-01`, `SCREEN-02` | 2 |
| `CMP-03` | Status Indicator Badge | 4 | `SCREEN-01`, `SCREEN-02` | 2 |
| `CMP-04` | Document Editor Text Area | 2 | `SCREEN-02` | 1 |
| `CMP-05` | Notification Banner | 2 | `SCREEN-01`, `SCREEN-02` | 2 |
| `CMP-06` | Navigation Icon Button | 1 | `SCREEN-02` | 1 |

## Set checks — required at the end of the artifact

| Check | Result |
|---|---|
| Components with zero citing screens | `0` |
| Citing SCREEN IDs absent from the frozen Process 05 inventory | `0` |
| SCREEN IDs in the frozen inventory with no citing component | `0` |
| Components with no "when not to use" statement | `0` |
| Components with an unstyled interaction state | `0` |
| Components defined | `6` |
| Components cited | `6` |
| Screens in source | `2` |
| Screens citing at least one component | `2` |

The two totals that must match at Gate 2: components defined = components cited; screens in source = screens citing at least one component.
