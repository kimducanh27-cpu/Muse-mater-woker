# PROVENANCE — where every rule comes from

## The rule

Every normative sentence in a process contract must carry one of three labels:

| Label | Meaning | Evidence required |
|---|---|---|
| **VERBATIM** | Copied byte-for-byte from a licensed upstream | Blob SHA, size, licence, retrieval date |
| **ADAPTED** | A documented source, changed for this workflow | Source named, and the change stated |
| **LOCAL** | No upstream defines this. This repository decided it | Rationale, risk, and what evidence would retire it |

Invention is not forbidden. **Unlabelled invention is.** If a reader cannot tell which rules have external backing and which are this repository's own guess, then nobody knows which rules to trust — and every rule gets the same unearned confidence.

## Why LOCAL is allowed at all

No upstream repository defines a three-tab, human-gated process with Control Files, hash-anchored gates and exact-command approvals. That machinery is this repository's contribution. A rule forbidding LOCAL content would forbid the repository.

What is forbidden is letting a LOCAL rule look like a standard.

## Audit — Process 05 UX Design

| Rule | Label | Source |
|---|---|---|
| Three tabs, three gates, exact commands | LOCAL | Repo configuration, inherited from 01–04 |
| Control File, `state_seq`, single-writer, event log | LOCAL | Repo precedent, Process 04 |
| Decision Log with immutable proposals and DLE pairing | LOCAL | Repo precedent, Process 04 |
| Append-only review history and bounded recovery | LOCAL | Repo precedent, Process 04 |
| Severity taxonomy BLOCKER/CRITICAL/MAJOR/MINOR | LOCAL | Repo precedent, Process 04 |
| Fail-closed `NOT_VERIFIED` on unreadable evidence | LOCAL | Repo precedent |
| Transitive Process 03 verification through Process 04's hash | LOCAL | Repo decision, avoids inventing a P03 field. See L-8 |
| Advisory status and asserted linkage for Processes 01–03 | LOCAL | Exploratory stages; byte-verified chain starts at Process 04. See L-8 |
| Accessibility criteria | ADAPTED | WCAG 2.2; `upstream/.../accessibility-review/SKILL.md` (verbatim file, 2.1) |
| Copy-intent method | VERBATIM | `upstream/.../ux-copy/SKILL.md` |
| Review structure | VERBATIM | `upstream/.../design-critique/SKILL.md` |
| ASCII structural block rule (≤100 chars, non-authoritative) | LOCAL | See L-1 |
| Three lexical audits (no component, no visual value, no final copy) | LOCAL | Concept from `impeccable` `craft-floor.md`; word list local. See L-2 |
| Coverage counters | LOCAL | See L-3 |
| Accessibility split across 05 / 06 / 08 | LOCAL | See L-4 |

## Audit — Process 06 Design Systems

| Rule | Label | Source |
|---|---|---|
| Gate, Control, Decision Log, review machinery | LOCAL | Repo precedent, Process 05 |
| Three-tier token model (`ref` / `sys` / `comp`) | ADAPTED | Material Design 3, "Design tokens" — [m3.material.io](https://m3.material.io/foundations/design-tokens/overview). Tier labels adopted; token names are product decisions |
| Tonal elevation, state layers, dynamic colour | ADAPTED | Material 3 |
| Component inventory completeness, documentation and consistency audit | VERBATIM | `upstream/.../design-system/SKILL.md` — a maintenance method (audit / document / extend) |
| How to choose colour roles, scale ratios and elevation levels | LOCAL | No upstream defines the choice. The copied skill lists token *categories*; it does not say how to pick values. See L-7 |
| Contrast measured, not asserted | ADAPTED | WCAG 2.2; `accessibility-review` (verbatim file, 2.1) |
| Component admission rule (must cite SCREEN IDs) | LOCAL | See L-5 |
| Platform recorded as an immutable Control field | LOCAL | See L-6 |
| Contrast failure fixed in foundations, never per component | LOCAL | Repo decision |

## LOCAL decisions register (8 registered)

Eight LOCAL decisions are registered (L-1 through L-8). Each entry states what it is, why it exists, what could go wrong, and what would retire it. A LOCAL rule that never gets retired after real use is a rule nobody examined.

### L-1 — Structural block rule

**What.** Artifact 01 may contain one fenced `text` block per screen, ≤100 characters, spatial grouping only, never authoritative.

**Why.** A UX contract with no spatial artefact is too weak to constrain Processes 06 and 07; an image is not diffable and not hashable.

**Risk.** The block and the ordered hierarchy list can disagree, and an agent may trust the picture over the list. Mitigated by making the list authoritative and a disagreement a Gate 1 defect — but that mitigation is itself untested.

**Retired when.** A live run shows either that blocks are never read, or that they are read instead of the list.

### L-2 — Three lexical audits

**What.** No named UI component, no colour/typography/spacing value, no final copy in artifacts 01–05.

**Why.** These are the three decisions that leak backwards most often. Naming a component in a UX spec turns Process 06 into a rubber stamp.

**Risk.** A word list is brittle. "App bar" is caught; "the header area" is not. The audit gives false confidence about a boundary it only partially enforces.

**Retired when.** A live run shows a leak the list missed, which is the expected outcome on first use.

### L-3 — Coverage counters

**What.** Computed counts of screens, states, components, contrast pairs, stored in the Control File and required to match at each gate.

**Why.** A count that decreases without an invalidation event is evidence of tampering. It makes silent shrinkage detectable.

**Risk.** Counters measure quantity, not quality. Every screen can have an entry and every entry can be empty. The counter will pass while the artifact is worthless.

**Retired when.** A live run shows a gate passing on a hollow artifact.

### L-4 — Accessibility split across three processes

**What.** 05 states requirements, 06 supplies tokens and components, 08 measures conformance.

**Why.** Each process has different evidence available. 05 cannot measure contrast; 08 cannot choose a role.

**Risk.** A three-way split is where requirements go to die. Each process can assume another owns it, and no single gate fails when the requirement is dropped.

**Retired when.** A live run produces a screen with an accessibility requirement that no artifact claims.

### L-5 — Component admission rule

**What.** A component exists only if a frozen screen cites it, and `components_defined` must equal `components_cited` at Gate 2.

**Why.** Without it a design system becomes a catalogue of everything the author imagined, and Process 07 composes from availability rather than demand.

**Risk.** It can produce an under-built system: a component genuinely needed by two screens may be awkward to express, and the rule gives no guidance on when to split or merge. It optimises for provable demand, not for a good library.

**First evidence, 2026-11-12.** Probe 7 ran Process 06 Tab 02 against a frozen two-screen spec. The agent admitted six components, each citing a real screen, and rejected four Material 3 defaults **by name** — `NavigationDrawer`, `FloatingActionButton`, `Tabs`, `Slider` — for lack of a citing screen. It was not told which to reject.

That is the rule constraining behaviour rather than describing an intention. One data point is not proof, and the under-built risk above remains untested. But this is the first LOCAL rule in this repository to survive contact with an agent, and it is recorded as exactly that and no more.

**Retired when.** A live run shows Process 07 blocked by a missing component the rule prevented.

### L-6 — Platform as an immutable Control field

**What.** `platform` is written once at initialization; changing it reopens every gate.

**Why.** Platform silently sets target size, type scale, elevation semantics and motion budget. Leaving it implicit meant it was never decided.

**Risk.** Immutability is heavy. A product that later adds a tablet or web target must start a new initiative, which may be disproportionate.

**Retired when.** A second platform is actually attempted.

### L-7 — Foundations are chosen, not derived

**What.** Colour roles, type-scale ratio, spacing base and elevation levels are chosen by the author and justified by use. No formula or upstream method produces them.

**Why.** The copied `design-system` skill lists token *categories* — colours, typography, spacing, borders, shadows, motion — but never says how to pick a value within a category. Material 3 supplies defaults, and this process explicitly forbids adopting one merely because it exists.

**Risk.** This is the most subjective step in the whole sequence, and it sits behind the same gate machinery as the most mechanical ones, so it inherits the same appearance of rigour. A reviewer can verify that every value has a role and a use. Nobody can verify that the ratio is right, or that `sys.color.action.primary` is the correct green. The gate proves the foundation is *documented*, not that it is *good*.

**Retired when.** A live run produces a screen the foundation cannot express, or a reviewer cannot tell a justified value from an arbitrary one.

### L-8 — Advisory status and asserted linkage for Processes 01–03

**What.** P01–P03 are advisory exploration stages. Inter-process handoffs are string-asserted; the byte-verified hash chain starts at Process 04.

**Why.** Reconciles the realities of upstream P01–P03 design without introducing unvetted control mechanisms retroactively.

**Risk.** P01–P03 artifacts could be silently modified without detection by downstream until Process 04 freeze.

**Retired when.** P01–P03 receive schema v4 Control Files with SHA-256 bindings if cryptographic verification of exploration is required.

## What this audit does not claim

- It does not claim the LOCAL rules are wrong. It claims nobody outside this repository has validated them.
- It does not claim completeness. It covers Processes 05 and 06 only; Processes 01–04 predate the audit and contain LOCAL content of their own, including the entire gate model.
- It does not convert any `NOT RUN` into a `PASS`. Every LOCAL rule above is untested in a live run.

## Rule for new processes

Before a contract is committed, every normative sentence must be classifiable in one hop. A reviewer asking "where does this come from" must get either a file with a blob SHA, a named standard, or a register entry in this document.

A new LOCAL rule that is not added to the register is an unlabelled invention, and unlabelled invention is what this document exists to prevent.
