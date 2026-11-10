# THE SEED — Human-Gated Product Building Workflow

**Cấu hình The Seed:** AI = **Sparring** · Research = **Deep** · Antigravity = **3 tabs**.

This repository defines four processes in a seven-process workflow. Later contracts must be added explicitly; do not infer them from numbering.

## Architecture
Principles: **upstream-first, orchestration-second**.
- Preserve suitable upstream Skills verbatim where license allows; record source, SHA and license.
- Put workspace-specific behavior in custom adapters, prompts and templates.
- Never relabel a rewrite as an upstream Skill.
- No automatic process handoff. Each stage has human gates and file-persisted state.

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
3. Independent Flow Review

Canonical state: product/app-flow/00_APP_FLOW_CONTROL.md.
Frozen output: product/app-flow/APP_FLOW.md.

Process 04 defines functional user journeys and navigation. It does not create wireframes, visual layouts, design systems, UI/UX, APIs, database architecture or code.

Kit: app-flow-kit/README.md.

## Handoffs
- Process 01 → Process 02: approved Seed.
- Process 02 → Process 03: eligible Discovery decision under Process 03's explicit handoff rules.
- Process 03 → Process 04: frozen Product Definition with Gate 3 APPROVED and matching SHA-256.
- Process 04 → Process 05: frozen App Flow with approved gates and matching hashes. Process 05 must not silently change product scope or functional flow.

## Antigravity setup
1. Place this repository at the project workspace root.
2. Keep .agents/skills/ at that root.
3. Check the active Skill in Antigravity's Customizations panel.
4. For each tab, read the active Skill, initialize/verify its canonical Control File and prerequisites, then open a fresh conversation and paste only that tab's matching prompt.
5. Transfer context through workspace artifacts, not chat history.

Each process kit contains its prerequisites, output contracts, gates and verification notes. Repository checks are not a substitute for live Antigravity tests.
