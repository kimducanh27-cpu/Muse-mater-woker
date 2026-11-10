# THE SEED — Human-Gated Product Building Workflow

**Cấu hình The Seed đã chốt:** AI = **Sparring** · Research = **Deep** · Antigravity = **3 tabs**.

This repository currently contains three defined processes in a seven-process workflow. Later process contracts must be added explicitly; do not infer them from process numbering.

## Architecture
Principles: **upstream-first, orchestration-second**.
- Preserve suitable upstream Skills verbatim where license allows; record source, SHA and license.
- Put workspace-specific behavior in custom adapters, prompts and templates.
- Never relabel a rewrite as an upstream Skill.
- No automatic process handoff. Each stage has human gates and file-persisted state.

## Process 01 — The Seed
The Seed turns a rough idea into a structured problem/idea seed approved by the user. Three tabs: Explore / Sparring, Deep Research, Independent Review. The frozen product/seed/SEED.md is the preferred input to Process 02.

## Process 02 — Product Discovery
Active Skill: .agents/skills/product-discovery/SKILL.md

Product Discovery explores opportunities, gathers customer evidence, maps assumptions and designs experiments. Three independent tabs: Opportunity Discovery, Customer Evidence, Solution & Experiments.

Canonical state: product/discovery/00_DISCOVERY_CONTROL.md. Gate 2 approval is not validation. Gate 3 approves the experiment plan, not execution. If no experiment has run, 07_DISCOVERY_DECISION.md remains READY FOR TESTING; do not create an Outcome based only on a test plan.

Kit: product-discovery-kit/README.md.

## Process 03 — Product Definition
Active Skill: .agents/skills/product-definition/SKILL.md

Product Definition turns the eligible Process 02 decision into a product direction: target segment, customer outcome, positioning, product concept, principles, first-release capability scope, success measures and explicit non-goals.

Three independent tabs:
1. Product Intent & Positioning
2. Product Shape & Scope
3. Independent Definition Review

Canonical state: product/definition/00_PRODUCT_DEFINITION_CONTROL.md.
Frozen output: product/definition/PRODUCT_DEFINITION.md.

Process 03 defines WHAT the product is and WHY. It does not create App Flow, screens, UX/UI, technical architecture, an engineering-ready PRD or code.

Kit: product-definition-kit/README.md.

## Handoff
PRODUCT_DEFINITION.md is the intended input to Process 04 — App Flow. Process 04 must derive user/navigation flows from the approved product capabilities without silently changing the product promise or scope. The Process 04 contract has not yet been created in this repository.

## Antigravity setup
1. Place this repository at the project workspace root.
2. Keep .agents/skills/ at that root.
3. Check the active Skill in Antigravity's Customizations panel.
4. Open a fresh conversation for each tab and paste only that tab's prompt.
5. Transfer context through workspace artifacts, not chat history.

Each process README contains its prerequisites, output contracts, gates and upstream register.


## Process 03 integrity note

Process 03 uses a schema-version-2 canonical Control File. Before using a frozen Product Definition, verify Gate 3 = APPROVED, lifecycle_status = FROZEN and the stored SHA-256 matches product/definition/PRODUCT_DEFINITION.md. Process 03 accepts only PROCEED or NARROW from Process 02; READY FOR TESTING requires explicit persisted uncertainty acceptance. Tab 03 is read-only on source artifacts and review rounds are append-only. See product-definition-kit/VERIFICATION-CHECKLIST.md. Live Antigravity behavior remains unverified until tested in the actual workspace.
