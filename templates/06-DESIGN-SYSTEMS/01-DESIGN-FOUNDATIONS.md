# 01 — Design Foundations

> Artifact of Process 06. Owner: Tab 01. Bound by Gate 1.
> This is the first artifact in the sequence permitted to contain concrete values. Use that permission.

## Rules for this artifact

- Every value states the **role** it serves and **where a screen would use it**. A value with no role is decoration and is rejected.
- Colour is defined as roles, not as a palette. `#1B6B4A` is not a decision; "action.primary, used for the one affirmative action on a screen" is.
- On Android, elevation is tonal and state layers are platform behaviours. Decide them; do not inherit them silently.
- No component, no screen layout, no copy.

## Platform

| Field | Value |
|---|---|
| Target | `android` |
| Framework | `jetpack-compose` |
| Design language | `material-3` |
| Decision reference | `process-charters/06-DESIGN-SYSTEMS.md#8a` |
| Dynamic colour | ADOPTED / NOT ADOPTED — with rationale |
| Dark theme | IN SCOPE v1 / DEFERRED — with rationale |

## Colour roles

| Role ID | Role | Reference token | Use | Must not be used for |
|---|---|---|---|---|
| `color.action.primary` | The one affirmative action on a screen | | | Secondary actions, destructive actions |
| `color.action.destructive` | An action that removes or destroys | | | Anything reversible |
| `color.surface.base` | The default background | | | Elevated containers |
| `color.text.primary` | Body and heading text on base surface | | | Text on an inverse surface |
| `color.text.muted` | Supporting text that is not required to act on | | | Anything the user must read to proceed |
| `color.state.disabled` | A control that cannot be used | | | A control that is merely unavailable right now |
| `color.feedback.danger` | A failure the user must act on | | | Warnings, which are not failures |

Every role needs an entry in both columns. "Must not be used for" is what prevents a role from becoming a synonym for a colour.

## Type scale

| Step | Role | Size | Line height | Weight | Use |
|---|---|---|---|---|---|
| `type.display` | | | | | |
| `type.title` | | | | | |
| `type.body` | | | | | |
| `type.label` | | | | | |
| `type.caption` | | | | | |

**Ratio and rationale.** State the scale ratio and why. A scale assembled from taste has no defence when a reviewer asks why step 3 is 17 and not 16.

## Spacing scale

| Token | Value | Role | Use |
|---|---|---|---|
| `space.inline.sm` | | Between elements on one line | |
| `space.stack.md` | | Between stacked blocks | |
| `space.inset.screen` | | Screen edge inset | |

## Radius

| Token | Value | Role | Use |
|---|---|---|---|
| | | | |

## Elevation

Material 3 elevation is tonal, not a shadow stack. Record the levels and what each one means semantically.

| Level | Token | Meaning | Use |
|---|---|---|---|
| 0 | `elevation.flat` | Part of the surface | |
| 1 | `elevation.raised` | Temporarily above the surface | |
| 2 | `elevation.overlay` | Blocks interaction with what is beneath | |

## Motion

| Token | Duration | Easing | Use |
|---|---|---|---|
| `motion.enter` | | | |
| `motion.exit` | | | |
| `motion.emphasized` | | | |

Per-screen choreography is Process 07. This artifact defines only the vocabulary.

## Layout grid

| Field | Value |
|---|---|
| Base unit | |
| Columns — compact width | |
| Columns — expanded width | |
| Gutter | |
| Screen margin | |

## Foundation index — required at the end of the artifact

| Value | Role stated | Use stated | Cited by token |
|---|---|---|---|
| | yes / no | yes / no | yes / no |

**Totals.** Values defined: `<n>`. Values with a role and a use: `<n>`. Values with no role: must be `0`.
