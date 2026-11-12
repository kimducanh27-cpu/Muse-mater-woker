# Upstream register

Checked: **2026-11-10**. Source branches were `main` at retrieval time. Blob SHAs below identify the exact upstream file versions copied into this repository.

## 1. Anthropic — Product Brainstorming

- Repository: https://github.com/anthropics/knowledge-work-plugins
- Source file: https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/product-brainstorming/SKILL.md
- Local path: `.agents/skills/product-brainstorming/SKILL.md`
- Upstream blob SHA: `d37e2c2433179bb6b65c169b1a5261bc8ce1c955`
- License: Apache-2.0 (the product-management package license is copied to `LICENSES/ANTHROPIC-PRODUCT-MANAGEMENT-LICENSE.txt`).
- Handling: copied verbatim; this file is intentionally not rewritten. The Seed-specific restrictions live in the separate `seed-explore` adapter and tab prompt.

## 2. ferminrp — Product Shaping

- Repository: https://github.com/ferminrp/agent-skills
- Source skill: https://github.com/ferminrp/agent-skills/blob/main/skills/product-shaping/SKILL.md
- Local path: `upstream/ferminrp/product-shaping/SKILL.md`
- Upstream blob SHA: `66afdf3d1fb4c6e40925ca768ccbe02571c45920`
- References copied verbatim:
  - `references/prototype-guide.md` — blob `9031781d8a954bdfda273f195c481d7e3d9bfdcd`
  - `references/shaping-doc-template.md` — blob `f4e7b1b57168d496dde09aa80fe4d927463be264`
- License status: the upstream repository README declares MIT. A root `LICENSE` file was not present in the repository root listing checked on 2026-11-10. This is recorded rather than fabricating a copyright notice or license file. Verify the upstream repository's current license before further redistribution.
- Handling: source and references are retained verbatim for inspection, but are **not** placed in `.agents/skills/` and are not part of the three-tab active workflow.

## 3. anthropics/knowledge-work-plugins — evaluated, not yet copied

- Repository: https://github.com/anthropics/knowledge-work-plugins
- Licence: Apache-2.0 (repository root `LICENSE`).
- Status: **evaluated 2026-11-12 for Processes 05–08; nothing copied into this repository yet.** No blob SHA can be recorded until a file is actually copied, and none is claimed here.

Candidate skills, by target process:

| Target | Upstream path |
|---|---|
| 05 UX Design | `design/skills/user-research`, `design/skills/ux-copy`, `design/skills/accessibility-review`, `design/skills/design-critique` |
| 06 Design Systems | `design/skills/design-system`, `design/skills/accessibility-review`, `design/skills/design-critique` |
| 07 UI Design | `design/skills/design-handoff`, `design/skills/design-critique`, `design/skills/accessibility-review` |
| 08 Validation | `engineering/skills/testing-strategy`, `design/skills/accessibility-review`, `design/skills/design-critique` |

These are domain skills, not process contracts. They supply method for a tab; they do not supply gates, Control Files, hashes or handoff rules. Copying one of them does not create a process, and a process that uses one is still a custom adapter.

At copy time, record for each file: source URL, retrieval date, upstream blob SHA, licence, and the local path. Until then this section is a candidate list only.

## Why Product Shaping is reference-only

The upstream Product Shaping skill runs multiple phases in one guided process, including research, prototyping, interview, shaping document and gut-check. That is useful as a source, but it would collapse the deliberately separate Tab 01 / Tab 02 / Tab 03 responsibilities and could push The Seed into prototype/spec work too early. We therefore preserve it as upstream material and do not rewrite it into a fake upstream skill. The active workflow uses the Anthropic brainstorming skill for Tab 01 and custom, narrowly scoped workflow adapters for research and review.

## Change policy

- Never silently edit an upstream file in place.
- When updating an upstream copy, record the new source URL, retrieval date, upstream blob SHA, and license state.
- Put project-specific behavior in `seed-*` adapters, prompts and templates.
- A custom adapter is not an upstream skill and must never be described as one.
