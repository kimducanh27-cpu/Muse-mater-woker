# 02 — Token Contract

> Artifact of Process 06. Owner: Tab 02. Bound by Gate 2.
> Three layers. Each layer may reference only the layer above it.

## Rules for this artifact

- **Primitive** — a raw value with no meaning. Never referenced by a component.
- **Semantic** — a role. This is what theming and contrast measurement attach to.
- **Component** — a component-scoped alias. May reference semantic tokens only.
- A component token that references a primitive is a Gate 2 defect: it opts out of theming and out of the contrast guarantee.
- A semantic token with no role statement is a naming defect. "blue" is not a role.
- No value may exist here that is absent from artifact 01.

## Layer 1 — Primitive

| Token | Value | Notes |
|---|---|---|
| `palette.<hue>.<step>` | | Not referenced by components |
| `size.<n>` | | |

## Layer 2 — Semantic

| Token | References | Role | Used by components |
|---|---|---|---|
| `color.action.primary` | `palette.…` | | |
| `color.surface.base` | | | |
| `space.inline.sm` | `size.…` | | |
| `type.body` | | | |
| `elevation.raised` | | | |
| `motion.enter` | | | |

## Layer 3 — Component

| Token | References semantic token | Component | Notes |
|---|---|---|---|
| `button.primary.container` | `color.action.primary` | `CMP-…` | |

## Forbidden usage register

Explicit prohibitions. This is what stops a token from becoming a suggestion.

| Token or role | Forbidden use | Why |
|---|---|---|
| `color.action.primary` | More than one affirmative action on a screen | Two primaries means no primary |
| `color.action.destructive` | Any reversible action | Destructive styling trains the user to hesitate |
| `color.text.muted` | Text the user must read to complete the task | Muted implies optional |

## Naming rules

| Rule | Statement |
|---|---|
| Case | |
| Separator | |
| Layer prefix | |
| Forbidden words | Colour names, size numbers or component names inside a semantic token |

## Layering check — required at the end of the artifact

| Check | Result |
|---|---|
| Primitive tokens referenced by a component token | must be `0` |
| Semantic tokens without a role statement | must be `0` |
| Component tokens referencing a non-existent semantic token | must be `0` |
| Values present here but absent from artifact 01 | must be `0` |
| Primitives defined | `<n>` |
| Semantic tokens defined | `<n>` |
| Component tokens defined | `<n>` |
