# Process 07 — UI Design (charter)

> Status: **CHARTER — NO CONTRACT.** Scope only. No Skill, prompts, templates, Control File or gates exist.

## 1. Why this process exists

After Process 06 there is a language but no sentences. Process 07 composes every screen out of the frozen system, in every state, at every supported width, with final copy — to the point where a builder never has to ask a design question.

The measure of success is negative: **zero questions returned to the designer during build.** Every question a builder has to ask is a hole in this process.

## 2. Position in the sequence

```
05 UX Design ──▶ 06 Design Systems ──▶ 07 UI Design ──frozen UI_SPEC.md + hash──▶ 08 Validation
```

## 3. Input contract

- `product/ux-design/UX_SPEC.md` — frozen, hash verified
- `product/design-system/DESIGN_SYSTEM.md` — frozen, hash verified
- `product/app-flow/APP_FLOW.md` — read-only, for the screen and state inventory

Entry is blocked if either upstream has an open Change Request, or if the design system cannot express a screen required by the UX spec.

## 4. Output contract

Proposed working artifacts (`product/ui-design/`):

| File | Purpose |
|---|---|
| `01_SCREEN_COMPOSITION.md` | Per SCREEN ID: layout structure, grid placement, ordered component instances with inventory IDs, visual hierarchy |
| `02_RESPONSIVE_SPEC.md` | Breakpoints, reflow and collapse rules, min/max widths, what truncates and what wraps |
| `03_STATE_COMPOSITION.md` | Every state composed, not described — including empty, loading, partial, error, permission-denied and destructive-confirmation |
| `04_COPY_DECK.md` | Final strings per screen and state, with character budget and truncation behaviour |
| `05_HANDOFF_SPEC.md` | Spacing and sizing values, asset inventory with hashes, motion choreography, edge cases |
| `06_UI_REVIEW.md` | Append-only independent review rounds |
| `07_UI_SPEC_DRAFT.md` | Complete reviewed candidate |
| `08_DECISION_LOG.md` | Append-only user-approved UI decisions |

Frozen output: `product/ui-design/UI_SPEC.md`.

Control schema: `v1`.

## 5. Gates and exact commands

| Tab | Gate | Exact command |
|---|---|---|
| 01 Composition and responsive behaviour | Composition approved | `APPROVE SCREEN COMPOSITION` |
| 02 States, copy and handoff | UI spec approved | `APPROVE UI SPEC` |
| 03 Independent UI review | Freeze authorized | `FREEZE UI SPEC` |

## 6. Boundaries — what Process 07 must not do

- **No new components.** A needed component is a Change Request to 06, which reopens the component library gate.
- **No new screens.** A needed screen is a Change Request to 04.
- **No new states.** A needed state is a Change Request to 05.
- **No token changes.** If a spacing value does not exist in the scale, that is a 06 decision, not a local exception.
- **No product or UX policy decisions.** If composition reveals a UX contradiction, it returns to 05.
- **No code, no working prototype, no CSS, no framework component.** Images may be attached as evidence; they are not the contract.
- **No second theme** unless Process 06 froze more than one.

## 7. Integrity rule specific to this process

Process 07 is where drift becomes visible, so its Gate 2 must run **set comparisons, not assertions**:

- Set of SCREEN IDs composed = set of SCREEN IDs in the frozen Process 04 inventory.
- Set of component IDs instantiated ⊆ set of component IDs in the frozen Process 06 inventory.
- Set of states composed per screen = set of states for that screen in the frozen Process 05 spec.
- Every string in the copy deck maps to a screen and state; no orphan string, no missing string.
- Every spacing value used exists in the token contract; report every literal value not backed by a token.

An unexplained extra ID in any of these sets blocks the gate.

## 8. Upstream sources

| Upstream | Path | Use |
|---|---|---|
| `pbakaus/impeccable` | `skill/reference/layout.md` | Spacing, rhythm, visual hierarchy |
| `pbakaus/impeccable` | `skill/reference/typeset.md` | Typography hierarchy within frozen tokens |
| `pbakaus/impeccable` | `skill/reference/adapt.md`, `adapt.native.md` | Responsive and device adaptation |
| `pbakaus/impeccable` | `skill/reference/android.md` | Android layout and insets rules |
| `pbakaus/impeccable` | `skill/reference/craft-floor.md` | Ban list for the lexical audit |
| `anthropics/knowledge-work-plugins` | `design/skills/design-handoff` | Handoff artifact structure and completeness |
| `anthropics/knowledge-work-plugins` | `design/skills/design-critique` | Review method for Tab 03 |
| `anthropics/knowledge-work-plugins` | `design/skills/accessibility-review` | Focus order and target-size verification during composition |

`impeccable` is Apache-2.0 and reference-only; see `UPSTREAMS.md` section 4. Its `colorize` and `animate` playbooks are deliberately **not** listed here: colour is frozen in Process 06, and per-screen motion choreography is already owned by artifact 05. A playbook that would let Process 07 reopen a Process 06 decision is not a source, it is a boundary leak.

## 9. Open questions — must be resolved before the contract is written

1. **Does a UI spec need images?** A text-and-table UI contract is diffable and hashable but hard to judge. Options: (a) text only; (b) images stored under `product/ui-design/assets/`, referenced by path and SHA-256, with the text table remaining the authoritative contract and images explicitly evidence-only; (c) a generated HTML prototype, which is code and therefore out of bounds. Current recommendation: (b) — it preserves the hash-anchored contract while letting a human actually see the screen.
2. **Copy and localisation.** If the product ships in more than one language, character budgets must be defined per language or the layout will break on the longest one. Recommendation: copy deck records the budget in characters plus the truncation rule, and names the longest supported language.
3. **State coverage cost.** Composing every state of every screen is the single largest cost in this process. Recommendation: compose shared patterns once in `03` and record per-screen deviations, but require an explicit per-screen checklist so "shared pattern" never becomes an excuse for a missing state.
4. **Who owns empty-state illustration** — 06 (as an asset) or 07 (as a composition)? Recommendation: 07 owns the composition, 06 owns the asset if it is reusable.

## 10. Entry and exit in one line

**Entry:** two frozen upstream artifacts and a system that can express every screen. **Exit:** every screen buildable without a question, every state visible, every string final, every ID traceable.
