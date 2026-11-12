# Process charters — 05 to 08

A charter is **not** a contract. It fixes the scope of a future process so that the scope can be argued about before a thousand lines of gate machinery depend on it.

A chartered process has no Skill, no prompts, no templates, no Control File and no gates. It cannot be executed. Downstream work must not treat a charter as evidence that a process exists.

## Current sequence

| # | Process | Status | Contract path |
|---|---|---|---|
| 01 | The Seed | DEFINED | `.agents/skills/seed-explore/`, `seed-research/`, `seed-independent-review/` |
| 02 | Product Discovery | DEFINED | `.agents/skills/product-discovery/SKILL.md` |
| 03 | Product Definition | DEFINED | `.agents/skills/product-definition/SKILL.md` |
| 04 | App Flow | DEFINED | `.agents/skills/app-flow/SKILL.md` |
| 05 | UX Design | DEFINED | `.agents/skills/ux-design/SKILL.md` |
| 06 | Design Systems | DEFINED | `.agents/skills/design-system/SKILL.md` |
| 07 | UI Design | CHARTER ONLY | `process-charters/07-UI-DESIGN.md` |
| 08 | Validation | CHARTER ONLY | `process-charters/08-VALIDATION.md` |

The sequence is open-ended. No total count is asserted, in this file or in the root README. A number in this table means a slot, not a promise.

## Why the count is not fixed

The original plan named seven stages: Seed, Product Discovery, App Flow, UX Design, Design Systems, UI Design, Validation. Product Definition was added during development because Discovery decisions were being silently converted into product scope inside App Flow. That is the expected behaviour of a real pipeline, and it is the reason no total is written down.

A stage earns its own process by **separation of decisions**, not by separation of deliverables.

## Admission test

A new process may be created only when all six hold. Any failure means the work belongs inside an existing process, usually as a tab.

1. **Distinct decision class.** The process settles a category of decision that no earlier process is allowed to settle, and no later process may reopen locally.
2. **Own frozen artifact.** It produces one artifact that downstream processes consume by path and SHA-256, not by conversation.
3. **Clean boundary.** It can state, in one paragraph, what it must never produce. If that paragraph is vague, the boundary is not real.
4. **Blocking gate.** A downstream process can be blocked by its absence. A process nothing depends on is documentation, not a process.
5. **Verifiable evidence.** Its claims can be checked by set comparison, hash comparison or executed test — not by re-reading prose and agreeing with it.
6. **Upstream or adapter.** It either preserves a licensed upstream Skill verbatim, or its custom behaviour is isolated in an adapter that is never described as upstream.

## Cross-cutting rules for every new process

These are inherited from Processes 01–04 and are not re-negotiable per process.

- **Three tabs, three gates, three exact commands.** Each tab runs in a fresh conversation and reconstructs state from files. No automatic handoff.
- **Human gate, exact string.** Natural language, "looks good", "continue" and silence never substitute for an approval command.
- **Canonical Control File, single writer.** Every state change is one committed `state_seq` increment plus one appended event. Read-back before reporting success.
- **Append-only history.** Decision logs, review rounds and registers are never edited in place. Recovery is bounded, named and precondition-checked.
- **Hash-anchored handoff.** The downstream process verifies the upstream Control File and recomputes the frozen artifact hash. A status line is not proof of freeze.
- **Independent review tab.** Review is executed by a reviewer with a clean context and read-only rights on upstream artifacts. The reviewer may append findings and its own review history; it may not repair the artifacts it judges. Remediation returns to the owning tab.
- **Fail closed.** Missing, unreadable, mismatched or unorderable evidence yields `NOT_VERIFIED`, never a best guess.
- **Schema per process.** Each new process starts at Control schema `v1`. There is no inherited migration path from another process's schema.

## Amendment

Changing a charter requires the same discipline as changing a contract: the change is stated, the affected downstream process is named, and the reason is recorded. Silently widening a charter is how scope bleed starts.
