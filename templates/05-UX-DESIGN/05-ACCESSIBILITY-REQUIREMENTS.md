# 05 — Accessibility Requirements

> Artifact of Process 05. Owner: Tab 02. Bound by Gate 2.
> Requirements only. Process 06 supplies the tokens and components that satisfy them; Process 08 measures conformance. This artifact must not choose a colour, size or token.

## Target conformance

| Field | Value |
|---|---|
| Standard | WCAG 2.2 |
| Level | `AA` (record the actual decision; do not assume) |
| Decision ID | `DEC-…` |
| Scope | All screens in the frozen Process 04 inventory |
| Out of scope | Stated explicitly, with rationale |

The target level is a decision, not a default. It is recorded here and in the Decision Log because it changes the audit checklist and the number of findings in Process 08.

## Per-screen requirements

| Screen ID | Keyboard reachable | Focus order intent | Announcement intent | Minimum target size | Motion constraint | Notes |
|---|---|---|---|---|---|---|
| `SCREEN-…` | REQUIRED / N/A | Ordered list of what receives focus, in sequence | What must be announced on state change, and when | Requirement, not a value | | |

**Focus order intent** is a sequence of *things*, not elements: "primary action, then the list, then the escape hatch". Process 06 and 07 translate it into real focus targets.

**Announcement intent** states what must be conveyed non-visually when a state changes — for example "the user must be told that the save failed and that their draft is intact". It does not name an ARIA attribute.

## Requirements that apply to every screen

| Requirement | Statement | Verified by |
|---|---|---|
| Text alternatives | Every non-text element that carries meaning has a stated alternative intent | Process 07 composition |
| Colour independence | No state may be conveyed by colour alone | Process 06 tokens + Process 08 audit |
| Focus visibility | Every focusable element must be visibly distinguishable | Process 06 + Process 08 |
| Timing | No interaction may require a response faster than the user can read the message | Process 05 review |
| Error identification | Every error names what failed and what to do | Artifact 04 message intent |

## Known constraints inherited from upstream

| Constraint | Source | Consequence |
|---|---|---|
| | Product Definition constraint | |

## Coverage check — required at the end of the artifact

| Check | Result |
|---|---|
| Screens in source | `<n>` |
| Screens with a requirements row | `<n>` |
| Target level recorded with a decision ID | yes / no |
| Any token, colour or size value present in this artifact | must be `0` |
