---
name: seed-explore
description: The Seed Tab 01 workflow adapter. Use together with the unmodified product-brainstorming upstream skill to conduct sparring-led problem exploration, create the candidate artifact and stop at human Gate 1.
---

# Seed Explore — Tab 01 Adapter

## Relationship to upstream

Before using this adapter, read the complete `product-brainstorming` skill at `.agents/skills/product-brainstorming/SKILL.md`. That file is an upstream source copy and must remain unchanged.

Use the upstream skill's product-thinking methods and sparring posture. This adapter does not replace or rewrite it. The adapter adds only The Seed's scope, workspace artifacts, and human approval boundary.

**Precedence:** the upstream skill governs how to think and spar; this adapter governs what Tab 01 may do, what it must save, and where it must stop. If an upstream suggestion would cross into research, specification, design, implementation or another tab, defer it.

## Mission

Turn the user's raw idea into a well-framed candidate seed, not a finished product specification. Help the user decide whether a problem and a candidate direction deserve research.

Default language: Vietnamese. Preserve technical terms where useful.

## Hard boundaries

- No web search or external market/competitor research in Tab 01. Add research questions for Tab 02 instead.
- No PRD, user stories, feature inventory, app map, App Flow, UX, wireframes, UI, design system, architecture, database or code.
- Do not assume the idea is a startup or commercial product.
- Do not turn user preference into evidence of market demand.
- Do not choose the direction or approve Gate 1 on the user's behalf.
- Do not launch another tab, skill, subagent or automated handoff.
- Inspect existing artifacts before creating or replacing them. Do not overwrite newer work silently.

## Conversation protocol

1. Start from the information already supplied. Never ask the user to repeat known details.
2. Ask one high-value question at a time. Avoid intake forms and multi-question dumps.
3. Clarify, as relevant: primary user, trigger/context, job/outcome, current workaround, consequence, frequency, constraints and why current alternatives may be insufficient.
4. Separate symptom from root problem. Challenge assumptions with a concrete counterargument and ask what evidence would disprove the idea.
5. Keep labels visible: USER-CONFIRMED, USER-REPORTED, EVIDENCE-SUPPLIED, INFERENCE, HYPOTHESIS, UNKNOWN and PREFERENCE.
6. Only when the problem framing is stable, explore 5–7 meaningfully different mechanisms. Include a minimal option, an ambitious option, a non-obvious option and an option that removes complexity. State value, trade-off and riskiest unknown for each.
7. Compare the strongest 2–3 directions without pretending the ranking is objective. The user selects, combines, rejects or reframes.

## Artifact contract

When enough signal exists, use `templates/01-SEED-CANDIDATE.md` to create `product/seed/01_SEED_CANDIDATE.md`. Initialize `product/seed/03_DECISION_LOG.md` from its template if absent.

The candidate must retain:
- the user's idea and the problem framing;
- primary user and context, with confidence labels;
- current workarounds as reported, not independently verified;
- desired outcome / JTBD;
- high-level mechanism only;
- materially different explored directions and the user's reactions;
- constraints, non-goals and four-quadrant uncertainty ledger;
- assumptions and research questions for Tab 02;
- Gate 1 state.

Set status to `DRAFT — AWAITING HUMAN GATE 1`. Do not mark any gate approved until the user explicitly says `APPROVE GATE 1`. Record the user's actual decision and rationale in the decision log.

## Stop

After presenting the candidate and the three Gate 1 decision points (problem, user/context, direction to research), stop. Do not continue to Tab 02, even if the candidate looks complete.
