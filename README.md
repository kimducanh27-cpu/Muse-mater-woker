# THE SEED — Human-Gated Product Building Workflow

**Cấu hình The Seed:** AI = **Sparring** · Research = **Deep** · Antigravity = **3 tabs**.

**New session? Read `docs/PRD.md`, then `docs/HANDOFF.md`, then `docs/PROGRESS.md`, then `docs/RULES.md` before writing anything.** `docs/TASKS.md` says what to do next; `docs/ARCHITECTURE.md` and `docs/DESIGN.md` explain why the kit is shaped this way. To refresh the pack later, use `docs/UPDATE-PROMPT.md`.

This repository defines six processes (01–06) of a numbered product-building sequence. Processes 07–08 are chartered in `process-charters/` and have no contract yet. The sequence is open-ended and no total count is asserted: a process is added only when it passes the admission test in `process-charters/README.md`. A number is a slot, not a promise.

The `docs/` pack is **derived and non-authoritative**. It exists so a new session does not have to re-read 2,031 lines of Skill to find out where things stand. On any disagreement, the Control File wins.

## Architecture
Principles: **upstream-first, orchestration-second**.
- Preserve suitable upstream Skills verbatim where license allows; record source, SHA and license.
- Put workspace-specific behavior in custom adapters, prompts and templates.
- Never relabel a rewrite as an upstream Skill.
- Label every rule VERBATIM, ADAPTED or LOCAL. Prefer an upstream over a local invention; when none exists, say so instead of letting a local choice read like a standard. See `PROVENANCE.md`.
- No automatic process handoff. Each stage has human gates and file-persisted state.

## Process sequence

| # | Process | Status | Entry artifact |
|---|---|---|---|
| 01 | The Seed | DEFINED | rough idea |
| 02 | Product Discovery | DEFINED | approved Seed |
| 03 | Product Definition | DEFINED | eligible Discovery decision |
| 04 | App Flow | DEFINED | frozen Product Definition |
| 05 | UX Design | DEFINED | frozen App Flow |
| 06 | Design Systems | DEFINED | frozen UX Spec |
| 07 | UI Design | CHARTER ONLY | frozen UX Spec + Design System |
| 08 | Validation | CHARTER ONLY | all four frozen artifacts |

Charters are scope documents, not contracts. A chartered process has no Skill, prompts, templates, Control File or gates and cannot be executed. See `process-charters/README.md` for the admission test that decides whether a stage earns its own process or stays a tab inside an existing one.

**Platform: Android native** — Jetpack Compose, Material 3, no web or iOS target in v1. Recorded as a decision in `process-charters/06-DESIGN-SYSTEMS.md` section 8a, because a platform assumption inherited from a folder name is not a decision. It binds Processes 06–08; Process 05 stays platform-neutral by design so that platform idioms cannot pre-empt the design system.

## Process 01 — The Seed
Turns a rough idea into a structured problem/idea seed approved by the user. Three tabs: Explore / Sparring, Deep Research, Independent Review. Frozen output: product/seed/SEED.md.

## Process 02 — Product Discovery
Active Skill: .agents/skills/product-discovery/SKILL.md

Explores opportunities, gathers customer evidence, maps assumptions and designs experiments. Three tabs: Opportunity Discovery, Customer Evidence, Solution & Experiments.

Canonical state: product/discovery/00_DISCOVERY_CONTROL.md. Gate 2 approval is not validation. Gate 3 approves the experiment plan, not execution. If no experiment has run, the decision remains READY FOR TESTING; do not create an Outcome based only on a test plan.

Kit: product-discovery-kit/README.md.

## Process 03 — Product Definition
Active Skill: .agents/skills/product-definition/SKILL.md

Defines target segment, customer outcome, positioning, product concept, principles, first-release capability scope, success measures and non-goals.

Three tabs: Product Intent & Positioning; Product Shape & Scope; Independent Definition Review.

Canonical state: product/definition/00_PRODUCT_DEFINITION_CONTROL.md.
Frozen output: product/definition/PRODUCT_DEFINITION.md.

Process 03 defines WHAT and WHY. It does not create App Flow, UX/UI, technical architecture, engineering-ready PRD or code.

Kit: product-definition-kit/README.md.

## Process 04 — App Flow
Active Skill: .agents/skills/app-flow/SKILL.md

Translates the frozen Product Definition into user tasks, flow architecture, navigation, functional screen inventory, transitions, states, exceptions and recovery paths.

Three tabs:
1. User Tasks & Flow Architecture
2. Navigation & Screen Flow Specification
3. Independent Flow Review and authorized freeze (only after the separate exact command `FREEZE APP FLOW`).

Canonical state: `product/app-flow/00_APP_FLOW_CONTROL.md` (schema v4). CR business state is owned only by `product/app-flow/10_CHANGE_REQUEST_REGISTER.md`; Control stores receipts/checkpoints, not per-CR statuses.
Working artifacts: 01–10, including append-only review history, decision log and Change Request Register (`10_CHANGE_REQUEST_REGISTER.md`).
Frozen output: product/app-flow/APP_FLOW.md.

The frozen output is copied from the complete reviewed draft; freeze changes only its status line. The canonical SHA-256 is stored in the Control File. Re-freeze archives the previous output as APP_FLOW.v<N>.md.

Process 04 defines functional user journeys and navigation. It does not create wireframes, visual layouts, design systems, UI/UX, APIs, database architecture or code.

Kit: app-flow-kit/README.md.

## Process 05 — UX Design
Active Skill: .agents/skills/ux-design/SKILL.md

Converts each functional screen from the frozen App Flow into an experience contract: user goal, exactly one primary action, information hierarchy, interaction pattern, the experience of every state the flow defines, content intent and accessibility requirements.

Three tabs:
1. Screen UX Model
2. Patterns, States, Content, Accessibility
3. Independent UX Review and authorized freeze (only after the separate exact command `FREEZE UX SPEC`).

Canonical state: `product/ux-design/00_UX_CONTROL.md` (schema v1).
Working artifacts: 01–08, including append-only review history and decision log.
Frozen output: `product/ux-design/UX_SPEC.md`.

Process 05 defines experience only. It does not create colour, typography, spacing, elevation, iconography, components, design tokens, wireframes, images, prototypes, final copy, APIs or code. The first process allowed to produce concrete visual values is Process 06.

Three lexical audits are enforced at Gate 2 and again at review: no named UI component, no visual value, no final copy. They exist because this is the process most likely to absorb decisions that belong to its neighbours.

Kit: ux-design-kit/README.md.

## Process 06 — Design Systems
Active Skill: .agents/skills/design-system/SKILL.md

Defines the reusable visual language and the component contract: colour roles, type scale, spacing, radius, elevation, motion, a three-layer token system, and a component inventory in which every component cites the frozen screens that require it.

Three tabs:
1. Foundations and Tokens
2. Tokens, Components, Accessibility
3. Independent Review and authorized freeze (only after the separate exact command `FREEZE DESIGN SYSTEM`).

Canonical state: `product/design-system/00_DS_CONTROL.md` (schema v1).
Working artifacts: 01–07, including append-only review history and decision log.
Frozen output: `product/design-system/DESIGN_SYSTEM.md`.

This is the first process permitted to produce concrete visual values. Platform is recorded in the Control File (`android` / `jetpack-compose` / `material-3`) and is immutable per workspace.

Three rules carry the process: a component exists only if a frozen screen cites it; tokens are layered reference → system → component and a component token may not reach past the system layer; contrast is measured from resolved values, never declared.

Process 06 defines a system. It does not place anything on a screen. Composition is Process 07.

Kit: design-system-kit/README.md.

## Handoffs
- Process 01 → Process 02: approved Seed.
- Process 02 → Process 03: eligible Discovery decision under Process 03's explicit handoff rules.
- Process 03 → Process 04: frozen Product Definition with Gate 3 APPROVED and matching SHA-256.
- Process 04 → Process 05: frozen App Flow with Gate 1, Gate 2 and Gate 3 approved, lifecycle FROZEN and matching canonical hash; full Register chain verified; reconstructed blocking CR set empty; all implementation CRs in the freeze batch CLOSED_IMPLEMENTED against the same freeze tuple. A downstream process must verify Control receipts, Register chain and frozen artifact hashes; filename/status text alone is not proof of eligibility.
- Process 05 → Process 06: frozen UX Spec with Gate 1, Gate 2 and Gate 3 approved, lifecycle FROZEN and matching canonical hash. A downstream process must verify the Process 05 Control File and recompute the UX Spec hash; a status line is not proof of freeze.
- Process 06 → Process 07 (chartered): frozen Design System with all three gates approved, lifecycle FROZEN, matching canonical hash, and `platform.target` equal to the platform Process 07 composes for.

## Antigravity setup
1. Place this repository at the project workspace root.
2. Keep .agents/skills/ at that root.
3. Check the active Skill in Antigravity's Customizations panel.
4. For each tab, read the active Skill, initialize/verify its canonical Control File and prerequisites, then open a fresh conversation and paste only that tab's matching prompt.
5. Transfer context through workspace artifacts, not chat history.

Each process kit contains its prerequisites, output contracts, gates and verification notes. Repository checks are not a substitute for live Antigravity tests.
