# 02 — Token Contract

> Artifact of Process 06. Owner: Tab 02. Bound by Gate 2.
> Three layers. Each layer may reference only the layer above it.

## Rules for this artifact

The three layers are **Material 3's**, not a local naming scheme: reference (`ref`), system (`sys`), component (`comp`). Use Material's prefixes so this contract and the Compose theme files share one vocabulary.

- **Reference (`ref`)** — a raw value with no meaning. Never referenced by a component.
- **System (`sys`)** — a role. This is what theming and contrast measurement attach to.
- **Component (`comp`)** — a component-scoped alias. May reference system tokens only.
- A component token that references a reference token is a Gate 2 defect: it opts out of theming and out of the contrast guarantee.
- A system token with no role statement is a naming defect. "blue" is not a role.
- No value may exist here that is absent from artifact 01.

## Layer 1 — Reference (`ref`)

| Token | Value | Notes |
|---|---|---|
| `ref.palette.<hue>.<step>` | | Not referenced by components |
| `ref.size.<n>` | | |

## Layer 2 — System (`sys`)

| Token | References | Role | Used by components |
|---|---|---|---|
| `sys.color.action.primary` | `ref.palette.…` | | |
| `sys.color.surface.base` | | | |
| `sys.space.inline.sm` | `ref.size.…` | | |
| `sys.type.body` | | | |
| `sys.elevation.raised` | | | |
| `sys.motion.enter` | | | |

## Layer 3 — Component (`comp`)

| Token | References system token | Component | Notes |
|---|---|---|---|
| `comp.button.primary.container` | `sys.color.action.primary` | `CMP-…` | |

## Forbidden usage register

Explicit prohibitions. This is what stops a token from becoming a suggestion.

| Token or role | Forbidden use | Why |
|---|---|---|
| `sys.color.action.primary` | More than one affirmative action on a screen | Two primaries means no primary |
| `sys.color.action.destructive` | Any reversible action | Destructive styling trains the user to hesitate |
| `sys.color.text.muted` | Text the user must read to complete the task | Muted implies optional |

## Naming rules

| Rule | Statement |
|---|---|
| Case | |
| Separator | |
| Layer prefix | |
| Forbidden words | Colour names, size numbers or component names inside a system token |

## Layering check — required at the end of the artifact

| Check | Result |
|---|---|
| Reference tokens referenced by a component token | must be `0` |
| System tokens without a role statement | must be `0` |
| Component tokens referencing a non-existent system token | must be `0` |
| Values present here but absent from artifact 01 | must be `0` |
| Reference tokens defined | `<n>` |
| System tokens defined | `<n>` |
| Component tokens defined | `<n>` |
