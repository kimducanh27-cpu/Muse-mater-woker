# THE SEED — Human-Gated Product Building Workflow

**Cấu hình The Seed:** AI = **Sparring** · Research = **Deep** · Antigravity = **3 tabs**.

This repository defines four processes (01–04) of a numbered product-building sequence. Processes 05–08 are chartered in `process-charters/` and have no contract yet. The sequence is open-ended and no total count is asserted: a process is added only when it passes the admission test in `process-charters/README.md`. A number is a slot, not a promise.

## Architecture
Principles: **upstream-first, orchestration-second**.
- Preserve suitable upstream Skills verbatim where license allows; record source, SHA and license.
- Put workspace-specific behavior in custom adapters, prompts and templates.
- Never relabel a rewrite as an upstream Skill.
- No automatic process handoff. Each stage has human gates and file-persisted state.

## Process sequence

| # | Process | Status | Entry artifact |
|---|---|---|---|
| 01 | The Seed | DEFINED | rough idea |
| 02 | Product Discovery | DEFINED | approved Seed |
| 03 | Product Definition | DEFINED | eligible Discovery decision |
| 04 | App Flow | DEFINED | frozen Product Definition |
| 05 | UX Design | CHARTER ONLY | frozen App Flow |
| 06 | Design Systems | CHARTER ONLY | frozen UX Spec |
| 07 | UI Design | CHARTER ONLY | frozen UX Spec + Design System |
| 08 | Validation | CHARTER ONLY | all four frozen artifacts |

Charters are scope documents, not contracts. A chartered process has no Skill, prompts, templates, Control File or gates and cannot be executed. See `process-charters/README.md` for the admission test that decides whether a stage earns its own process or stays a tab inside an existing one.

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

Canonical state: product/app-flow/00_APP_FLOW_CONTROL.md.
Working artifacts: 01–09, including append-only review history and decision log.
Frozen output: product/app-flow/APP_FLOW.md.

The frozen output is copied from the complete reviewed draft; freeze changes only its status line. The canonical SHA-256 is stored in the Control File. Re-freeze archives the previous output as APP_FLOW.v<N>.md.

Process 04 defines functional user journeys and navigation. It does not create wireframes, visual layouts, design systems, UI/UX, APIs, database architecture or code.

Kit: app-flow-kit/README.md.

## Handoffs
- Process 01 → Process 02: approved Seed.
- Process 02 → Process 03: eligible Discovery decision under Process 03's explicit handoff rules.
- Process 03 → Process 04: frozen Product Definition with Gate 3 APPROVED and matching SHA-256.
- Process 04 → Process 05 (chartered): frozen App Flow with Gate 1, Gate 2 and Gate 3 approved, lifecycle FROZEN and matching canonical hash, and no open Change Request in the freeze batch. A downstream process must verify the Process 04 Control File, the Register chain and the frozen artifact hash; filename/status text alone is not proof of freeze.

## Antigravity setup
1. Place this repository at the project workspace root.
2. Keep .agents/skills/ at that root.
3. Check the active Skill in Antigravity's Customizations panel.
4. For each tab, read the active Skill, initialize/verify its canonical Control File and prerequisites, then open a fresh conversation and paste only that tab's matching prompt.
5. Transfer context through workspace artifacts, not chat history.

Each process kit contains its prerequisites, output contracts, gates and verification notes. Repository checks are not a substitute for live Antigravity tests.
