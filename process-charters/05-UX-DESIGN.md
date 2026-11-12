# Process 05 — UX Design (charter)

> Status: **REALIZED — SUPERSEDED BY CONTRACT.** The contract exists at `.agents/skills/ux-design/SKILL.md` with `ux-design-kit/` and `templates/05-UX-DESIGN/`. This charter is retained for provenance: it records the scope argument and the four open questions the contract had to answer.

## Resolutions recorded at contract time

| Open question | Resolution |
|---|---|
| 1. Text-only UX artefact | Option (b). One fenced `text` structural block per screen, ≤100 characters, spatial grouping only, never authoritative — the ordered hierarchy list wins. |
| 2. Accessibility ownership split | Three layers made explicit: Process 05 states requirements, Process 06 supplies tokens and components, Process 08 measures conformance. |
| 3. Late usability evidence | Reopens Process 05. Experience defects belong to the process that owns experience; they are not pushed downstream as Change Requests. |
| 4. Information architecture scope | Within-screen only. Cross-screen structure belongs to Process 04 and returns there as a Change Request. |

## 1. Why this process exists

Process 04 answers *what the user must accomplish and through which functional screens*. It deliberately says nothing about what a person actually perceives while doing it. That gap is not cosmetic: a functionally complete flow can still be unusable because the primary action is buried, the empty state is unexplained, an error tells the user nothing actionable, or a destructive action looks identical to a safe one.

Process 05 converts each functional screen into an **experience contract**: on this screen, in this state, what must the user understand, what must be obvious, what must be recoverable, and what must never be ambiguous.

It is the last process that can still change the product cheaply. Everything after it is increasingly expensive to reverse.

## 2. Position in the sequence

```
04 App Flow ──frozen APP_FLOW.md + hash──▶ 05 UX Design ──frozen UX_SPEC.md + hash──▶ 06 Design Systems
```

Process 05 consumes the frozen App Flow and the frozen Product Definition. It does not consume Process 02 or 03 working artifacts; if it needs Discovery evidence, that evidence must already be reflected in the frozen Product Definition.

## 3. Input contract

Required, all verified before any work:

- `product/app-flow/APP_FLOW.md` — frozen, Gate 3 APPROVED, lifecycle `FROZEN`
- `product/app-flow/00_APP_FLOW_CONTROL.md` — `gate_3.frozen_artifact.sha256` matches the actual file hash
- `product/definition/PRODUCT_DEFINITION.md` — target segment, customer outcomes, constraints, non-goals

If Process 04 has any open Change Request in the freeze batch, entry is blocked. A flow with an unresolved CR is not a stable base for experience decisions.

## 4. Output contract

Proposed working artifacts (`product/ux-design/`):

| File | Purpose |
|---|---|
| `01_SCREEN_UX_MODEL.md` | Per SCREEN ID: user goal, primary/secondary/tertiary action, information hierarchy, cognitive load notes, entry expectation, exit guarantee |
| `02_INTERACTION_PATTERN_LIBRARY.md` | Named UX patterns with when-to-use and when-not-to-use; each screen cites pattern IDs instead of inventing behaviour |
| `03_STATE_EXPERIENCE_SPEC.md` | For every state P4 defined: what the user sees, understands, and can do; the recovery affordance; the failure message intent |
| `04_CONTENT_AND_COPY_INTENT.md` | What content each screen requires, required vs optional, and the *intent* of each message — not final wording |
| `05_ACCESSIBILITY_REQUIREMENTS.md` | Target conformance level, per-screen keyboard/focus/announcement requirements |
| `06_UX_REVIEW.md` | Append-only independent review rounds |
| `07_UX_SPEC_DRAFT.md` | Complete reviewed candidate, not a summary |
| `08_DECISION_LOG.md` | Append-only user-approved UX decisions |

Frozen output: `product/ux-design/UX_SPEC.md`.

Control schema: `v1` (new process, no inherited migration path).

## 5. Gates and exact commands

| Tab | Gate | Exact command |
|---|---|---|
| 01 Screen UX model | Structure approved | `APPROVE SCREEN UX MODEL` |
| 02 Interaction, states, content, accessibility | UX spec approved | `APPROVE UX SPEC` |
| 03 Independent UX review | Freeze authorized | `FREEZE UX SPEC` |

Gate 2 binds the exact hashes of artifacts 01–05 and the whole Decision Log. Any later Decision Log byte change reopens Gates 2–3. Freeze copies the reviewed draft byte-for-byte and changes only the status line.

## 6. Boundaries — what Process 05 must not do

- **No visual style.** No colour, typography, spacing, radius, elevation, iconography, imagery, brand expression.
- **No components.** No button, card, modal, toast or any named UI component. Naming a component here pre-empts Process 06.
- **No design system, tokens or style guide.**
- **No new screens.** Every screen must exist in the Process 04 screen inventory. A needed screen is a Change Request back to 04.
- **No new states.** Process 04 owns the functional state space. Process 05 may specify how a state is *experienced*; it may not invent a state. A genuinely missing state is a Change Request to 04.
- **No new capability.** Any capability absent from the frozen Product Definition returns to Process 03.
- **No final copy.** Intent only. Final wording belongs to Process 07, where length and layout constraints exist.
- **No code, no prototype, no wireframe image.**

## 7. Upstream sources

| Upstream | Path | Use |
|---|---|---|
| `anthropics/knowledge-work-plugins` | `design/skills/user-research` | Evidence discipline for usability claims |
| `anthropics/knowledge-work-plugins` | `design/skills/ux-copy` | Copy-intent method for artifact 04 |
| `anthropics/knowledge-work-plugins` | `design/skills/accessibility-review` | Accessibility requirement taxonomy for artifact 05 |
| `anthropics/knowledge-work-plugins` | `design/skills/design-critique` | Review method for Tab 03 |

All four are Apache-2.0. Copy verbatim into `.agents/skills/` or `upstream/`, record source URL, retrieval date, blob SHA and licence in `UPSTREAMS.md`. Custom gate behaviour goes in a `ux-design` adapter and is never described as upstream.

## 8. Open questions — must be resolved before the contract is written

1. **Text-only UX artefact.** Every other process produces prose and tables. A UX contract without any spatial artefact may be too weak to constrain Process 06 and 07. Options: (a) accept text-only, hierarchy expressed as ordered lists; (b) allow a constrained ASCII/grid layout block inside artifact 01; (c) allow an external image referenced by hash. Current recommendation: (b), because it is diffable and hashable.
2. **Accessibility ownership split.** Process 05 states per-screen requirements, Process 06 supplies tokens and components that satisfy them, Process 08 measures conformance. This three-way split must be written explicitly or the requirement will fall between processes.
3. **Where does UX research evidence enter?** If a usability finding arrives after Process 05 freezes, does it reopen 05, or become a Change Request handled in 07? Current recommendation: reopen 05 — experience defects belong to the process that owns experience.
4. **Does Process 05 own information architecture across screens,** or only within a screen? Cross-screen IA was largely settled by Process 04 navigation. Current recommendation: within-screen only; cross-screen structure is a Change Request to 04.

## 9. Entry and exit in one line

**Entry:** a frozen flow with no open Change Requests. **Exit:** every screen has an experience contract covering every state, reviewed independently, with a frozen hash that Process 06 verifies.
