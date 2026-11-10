# Process 03 — Upstream Register

Checked: 2026-11-10. Upstream files are preserved verbatim where noted. Custom Process 03 behavior belongs in the active Skill, prompts and templates.

## 1. ferminrp — Product Shaping (existing repository reference)
- Repository: https://github.com/ferminrp/agent-skills
- Source: https://github.com/ferminrp/agent-skills/blob/main/skills/product-shaping/SKILL.md
- Existing local copy: upstream/ferminrp/product-shaping/SKILL.md
- Upstream blob SHA: 66afdf3d1fb4c6e40925ca768ccbe02571c45920
- Supporting local references: prototype-guide.md (blob 9031781d8a954bdfda273f195c481d7e3d9bfdcd); shaping-doc-template.md (blob f4e7b1b57168d496dde09aa80fe4d927463be264).
- License: upstream README declares MIT. A standalone root LICENSE was not present at the prior source check; see LICENSES/FERMINRP-LICENSE-STATUS.md.
- Use: unknowns framework, shaping fidelity, key decisions, no-gos and deferred unknowns.
- Handling: already preserved verbatim elsewhere in this repository; linked rather than copied again. Process 03 does not automatically run prototype phases or create UI prototypes.

## 2. The Pragmatic PM — PM Product Brief
- Repository: https://github.com/marfoerst/the-pragmatic-pm
- Source: https://github.com/marfoerst/the-pragmatic-pm/blob/main/skills/pm-product-brief/SKILL.md
- Local copy: .agents/skills/product-definition/references/upstream/pm-product-brief/SKILL.md
- Upstream blob SHA: 46ffc5b69092cdccf6980d179344f140211b9ba2
- License: MIT. Repository LICENSE blob: 5f63e803e2f9bdb0d2ec0c46f1e845e3e40167d6. License text copied to product-definition-kit/LICENSES/PM-TOOLKIT-MIT-LICENSE.txt.
- Use: customer-outcome framing, working-backwards logic, value proposition and outcome ladder.
- Handling: copied verbatim. Reference-only; the host plugin's optional context files are not required dependencies of this kit. Treat examples as examples, never real customer evidence.

## Selection rationale
Product Shaping is the closest match for turning a fuzzy concept into a product shape without prematurely specifying implementation. PM Product Brief adds customer-outcome and value-proposition discipline.

Engineering-ready PRD skills were not copied because they would collapse Product Definition into later specification work. Executive one-pager skills were not copied because they serve leadership pitches rather than the canonical product definition artifact.

## Update policy
- Never edit upstream copies in place.
- For every updated upstream copy, record source URL, check date, blob SHA and license.
- Keep Process 03-specific gates, file contracts and restrictions in custom files.
- Do not claim a custom adapter is an upstream skill.


## Scope boundaries for upstream references

These copies are method references only. Process 03 may selectively borrow outcome ladders, weakest assumptions, no-gos, deferred unknowns and decision framing. It must not execute prototype phases, create HTML/UI prototypes, invent fictional customer quotes/personas, walk through customer journeys, draft activation paths, generate a PRD or route work to engineering skills absent from this kit.

### Immutable source identity

- ferminrp/agent-skills product-shaping source file blob: 66afdf3d1fb4c6e40925ca768ccbe02571c45920. Upstream HEAD reported by the independent review: 5dac874 (short SHA only; full commit permalink not verified here). License status remains unresolved; see LICENSES/FERMINRP-LICENSE-STATUS.md. Do not invent a notice.
- marfoerst/the-pragmatic-pm Product Brief blob: 46ffc5b69092cdccf6980d179344f140211b9ba2. MIT license blob: 5f63e803e2f9bdb0d2ec0c46f1e845e3e40167d6. Upstream HEAD reported by the independent review: 667676c (short SHA only; full commit permalink not verified here).

The blob hashes identify the vendored file contents. The short repository HEAD values above are review observations, not full commit identifiers. Replace them with full immutable commit permalinks only after verifying the upstream refs; do not infer missing SHA characters.
