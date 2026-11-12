# 04 — Component Accessibility

> Artifact of Process 06. Owner: Tab 02. Bound by Gate 2.
> Contrast is **computed from token values**, never declared. A pair that was not measured is not evidence.

## Conformance target

| Field | Value |
|---|---|
| Standard | WCAG 2.2 |
| Level | `AA` (record the actual decision) |
| Decision ID | `DEC-…` |
| Platform conformance | Material 3 accessibility guidance + TalkBack |
| Minimum target size | Record the value in dp; Material 3 guidance is the starting point, not the answer |

## Contrast pairs — measured

Every text/background and icon/background combination the inventory can produce. Compute the ratio from the resolved reference values behind the system tokens.

| Pair ID | Foreground token | Background token | Resolved hex | Ratio | Required | Result |
|---|---|---|---|---|---|---|
| `CP-<NN>` | `color.text.primary` | `color.surface.base` | `#… on #…` | `n.nn:1` | 4.5:1 | PASS / FAIL |

| Summary | Value |
|---|---|
| Pairs required | `<n>` |
| Pairs measured | `<n>` |
| Pairs failing | must be `0` at Gate 2 |
| Measurement method | Record the formula or tool. A ratio with no method is a guess. |

A failing pair is a Gate 2 defect, not a note for later. The fix belongs in artifact 01 (the role) or 02 (the token), not in a per-component exception.

## Per-component accessibility

| Component ID | Target size (dp) | Focus visible | Focus order role | Announcement intent | Notes |
|---|---|---|---|---|---|
| `CMP-<NN>` | | yes / no | | What must be conveyed non-visually, and when | |

**Announcement intent** states what the user must be told when the state changes — for example "the user must be told the save failed and that their input is intact". It does not name an ARIA attribute or a Compose semantics property; those are Process 07.

## Non-colour signalling

| Component ID | State | How it is conveyed without colour | Verified by |
|---|---|---|---|
| `CMP-<NN>` | error | | Process 07 composition + Process 08 audit |

Every state that is currently conveyed by colour alone must appear in this table. "Red means error" is a colour-only signal and fails.

## Motion and timing

| Concern | Requirement | Rationale |
|---|---|---|
| Reduced motion | | |
| Time limits | | |
| Auto-advancing content | | |

## Coverage check — required at the end of the artifact

| Check | Result |
|---|---|
| Contrast pairs required | `<n>` |
| Contrast pairs measured | `<n>` |
| Contrast pairs failing | must be `0` |
| Components with a target size | `<n>` of `<n>` |
| Components with an announcement intent | `<n>` of `<n>` |
| Colour-only state signals remaining | must be `0` |
