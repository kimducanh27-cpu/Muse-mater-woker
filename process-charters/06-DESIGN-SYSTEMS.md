# Process 06 — Design Systems (charter)

> Status: **REALIZED — SUPERSEDED BY CONTRACT.** The contract exists at `.agents/skills/design-system/SKILL.md` with `design-system-kit/` and `templates/06-DESIGN-SYSTEMS/`. This charter is retained for provenance: it records the scope argument, the platform decision, and the open questions the contract had to answer.

## 1. Why this process exists

Process 06 is the first process in the sequence allowed to produce **concrete visual values** — hex, point sizes, spacing units, durations. Everything before it is deliberately value-free.

Its job is to make a decision once that would otherwise be made independently on every screen: what a primary action looks like, how many steps the type scale has, what "danger" means as a colour role, what a disabled control does, how much space separates two sections. Without this, Process 07 composes screens out of locally invented styles, and the product drifts by the fourth screen.

The test of a design system is not that it is complete. It is that **no screen needs a one-off**.

## 2. Position in the sequence

```
05 UX Design ──frozen UX_SPEC.md + hash──▶ 06 Design Systems ──frozen DESIGN_SYSTEM.md + hash──▶ 07 UI Design
```

## 3. Input contract

- `product/ux-design/UX_SPEC.md` — frozen, hash verified against the Process 05 Control File
- `product/app-flow/APP_FLOW.md` — read-only, for screen and state inventory
- `product/definition/PRODUCT_DEFINITION.md` — read-only, for constraints and non-goals

Entry is blocked if any Process 05 Change Request remains open, or if the UX spec references a state that the design system has no way to express.

## 4. Output contract

Proposed working artifacts (`product/design-system/`):

| File | Purpose |
|---|---|
| `01_DESIGN_FOUNDATIONS.md` | Colour roles, type scale, spacing scale, radius, elevation, motion durations and easing, layout grid |
| `02_TOKEN_CONTRACT.md` | Three-layer token table (primitive → semantic → component), naming rules, allowed and forbidden usage per token |
| `03_COMPONENT_INVENTORY.md` | Every component: purpose, anatomy, variants, sizes, interaction states, slots, content limits |
| `04_COMPONENT_ACCESSIBILITY.md` | Measured contrast pairs, focus visibility, minimum target size, announcement intent per component |
| `05_DESIGN_SYSTEM_REVIEW.md` | Append-only independent review rounds |
| `06_DESIGN_SYSTEM_DRAFT.md` | Complete reviewed candidate |
| `07_DECISION_LOG.md` | Append-only user-approved system decisions |

Frozen output: `product/design-system/DESIGN_SYSTEM.md`.

Control schema: `v1`.

## 5. Gates and exact commands

| Tab | Gate | Exact command |
|---|---|---|
| 01 Foundations and tokens | Foundations approved | `APPROVE DESIGN FOUNDATIONS` |
| 02 Component library | Library approved | `APPROVE COMPONENT LIBRARY` |
| 03 Independent system review | Freeze authorized | `FREEZE DESIGN SYSTEM` |

Gate 2 binds foundations **and** the component library together. A component that contradicts an approved token is not a valid component.

## 6. Boundaries — what Process 06 must not do

- **No screen composition.** It defines what a card *is*, never where a card *goes*. Placement is Process 07.
- **No screen-specific layout, grid placement or responsive behaviour.**
- **No speculative components.** A component may exist only if at least one screen in the frozen UX spec requires it, and the inventory must cite the SCREEN IDs. A component with no citing screen is rejected at Gate 2. This rule is what keeps the system honest and traceable.
- **No final copy, no per-screen microcopy.**
- **No code, no component implementation, no Storybook, no CSS.**
- **No new screens, states or capabilities.** Any of those returns to 04, 05 or 03 respectively.
- **No illustration, photography or brand campaign work** in v1.

## 7. Upstream sources

| Upstream | Path | Use |
|---|---|---|
| `pbakaus/impeccable` | `skill/reference/extract.md` | Token and component extraction method |
| `pbakaus/impeccable` | `skill/reference/document.md` | `DESIGN.md` structure and completeness |
| `pbakaus/impeccable` | `skill/reference/craft-floor.md` | Quality floor and absolute bans |
| `pbakaus/impeccable` | `skill/reference/android.md` | Android platform rules for foundations |
| `anthropics/knowledge-work-plugins` | `design/skills/design-system` | Foundations and token method |
| `anthropics/knowledge-work-plugins` | `design/skills/accessibility-review` | Contrast and focus measurement discipline |
| `anthropics/knowledge-work-plugins` | `design/skills/design-critique` | Review method for Tab 03 |

`impeccable` is Apache-2.0 and reference-only; see `UPSTREAMS.md` section 4. Gate behaviour lives in a `design-system` adapter.

**What the contract actually did (2026-11-12).** `design-system`, `accessibility-review` and `design-critique` were copied byte-for-byte into `upstream/anthropics/knowledge-work-plugins/design/skills/` with blob SHAs in `SOURCE.md`. The `impeccable` rows remain citations only, because its playbooks invoke a runtime binary and copying the markdown alone would bake a broken dependency into the repository.

## 8. Open questions — must be resolved before the contract is written

1. **Theme support in v1.** A single theme is cheaper; retrofitting a second theme after 40 components exist is expensive. Recommendation: build the semantic token layer so a second theme is *possible*, but ship exactly one theme in v1 and say so explicitly in the Control File. With Android chosen, the second theme is almost certainly dark mode, and Material 3 makes the semantic layer mandatory rather than optional.
2. **Target platform.** **RESOLVED 2026-11-12 — Android native. See section 8a.**
3. **Contrast measurement source.** Contrast must be computed from actual token values, not asserted. That requires tokens to carry concrete hex, which makes this the first artifact in the repo with real colour values — the charter must state that explicitly so no reviewer treats it as a boundary violation.
4. **Icon system.** Icons are components with a grid and a stroke rule. Recommendation: include a named icon inventory in v1, but allow the set to be extended by Change Request rather than by per-screen invention in 07. On Android the Material icon set is a starting point, not a free pass: every icon still needs a citing screen.
5. **Motion.** Durations and easing are tokens. Per-screen animation choreography is Process 07. The split must be written down or both processes will claim it.

## 8a. Platform decision — Android native

**Decision.** The product ships as a native Android application. The design system targets Jetpack Compose and Material 3. No web target, no iOS target, no cross-platform framework in v1.

**Rationale.** The repository name, the project's origin as an Android app, and every design reference consulted assume Android. Leaving it unrecorded was the defect, not the choice.

**Consequences that must appear in the Process 06 contract:**

| Consequence | Where it binds |
|---|---|
| Minimum touch target, type scale and elevation follow Material 3, not a web scale | Foundations and component inventory |
| Dynamic colour and dark theme are Material 3 platform behaviours, not optional extras | Token layer must be semantic, not literal |
| System back, predictive back and window insets are platform contracts, not per-screen choices | Component and pattern inventory |
| Elevation is tonal in Material 3, not a drop shadow | Elevation tokens |
| Platform conformance is auditable against `impeccable` `android.md` | Gate 2 and Process 08 audit |

**What this does not authorise.** A Material 3 component is not automatically in scope. The rule in section 6 still governs: a component exists only if a frozen Process 05 screen requires it, and it must cite the SCREEN IDs. Platform default is not demand.

**Boundary note for neighbours.** Process 05 stays platform-neutral in its vocabulary — it may state a requirement such as "the user must be able to abandon this task without losing input", but it may not name the system back gesture or a Material component. Process 07 may use platform affordances because by then the system has frozen them. This ordering is deliberate: platform idioms absorbed at Process 05 would pre-empt Process 06 with decisions nobody audited.

## 9. Entry and exit in one line

**Entry:** a frozen UX spec where every screen's needs are known. **Exit:** a frozen system that can express every screen and state without a one-off, with measured accessibility evidence.
