# Upstream register

Checked: **2026-11-10**. Re-checked: **2026-11-12** for Processes 05–08 (sections 3–6). Source branches were `main` at retrieval time. Blob SHAs below identify the exact upstream file versions copied into this repository.

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

## 4. pbakaus/impeccable — verified 2026-11-12, reference-only

- Repository: https://github.com/pbakaus/impeccable
- Licence: **Apache-2.0** (`LICENSE` at repository root, 10,766 bytes).
- Signal at check time: 108,590 stars, 6,454 forks, last push `2026-11-12T09:06:48Z`, not archived.
- Skill entry point: `skill/SKILL.src.md` (name `impeccable`), plus **41** playbooks under `skill/reference/`.
- Status: **evaluated for Processes 05–08; nothing copied.** No blob SHA is claimed.

This is the strongest upstream found for the design half of the sequence. The playbooks that matter here:

| Playbook | What it is | Target process |
|---|---|---|
| `shape.md` | Plan UX/UI before writing code | 05 |
| `critique.md` | UX design review with heuristic scoring | 05 review, 08 |
| `extract.md` | Pull reusable tokens and components into a design system | 06 |
| `document.md` | Generate `DESIGN.md` from existing project code | 06 |
| `craft-floor.md` | Quality floor, absolute bans, reflexes no detector catches | 06, 07 |
| `layout.md`, `typeset.md`, `colorize.md`, `animate.md` | Hierarchy, type, colour, motion | 07 |
| `adapt.md`, `adapt.native.md` | Device and screen-size adaptation | 07 |
| `polish.md`, `clarify.md`, `harden.md` | Final pass, UX copy, edge cases | 07 |
| `audit.md`, `audit.native.md`, `component-review.md` | Accessibility, performance, responsive, component review | 08 |
| `android.md` | Android platform guidance | 06, 07, 08 |

### Why reference-only, not an active Skill

Two independent reasons, either of which is sufficient.

1. **It is a design agent, not a design method.** `new-work` designs and writes production code in one pass. Adopting it as the Process 05 active Skill would collapse P05→P07 in a single command and make Gates 1 and 2 decorative. This is the same failure mode already recorded for Product Shaping below: a skill that runs several phases at once cannot sit inside a three-tab gate model.
2. **It carries a runtime.** The skill shells out to `impeccable context`, `impeccable pin`, a design-detector hook and a self-contained binary shipped beside the skill. This repository is deliberately markdown-only with no execution dependency; adding a vendored binary would change what "installing the repo" means.

### Intended use

Read the playbooks as method. Lift the heuristic scoring rubric from `critique.md` into Process 08 Tab 03, the ban list from `craft-floor.md` into the Process 07 lexical audit, and the platform rules from `android.md` into the Process 06 Control File as a recorded platform decision. Cite the playbook and the upstream commit in the artifact that uses it.

If a future process genuinely needs the executable, treat it as a separate, explicitly authorised dependency with its own provenance record — not as a silently vendored skill.

## 5. Conradgui/zero-to-one-product-discovery — rejected, no licence

- Repository: https://github.com/Conradgui/zero-to-one-product-discovery
- Licence: **none declared.** The GitHub API returns `"license": null`.
- Signal at check time: 6 stars, last push `2026-06-08T14:00:52Z`, Python.

**Status: not usable.** A repository with no licence is all rights reserved by default; copying its content into this repository would be a licence violation regardless of how small the excerpt is. The description is a reasonable statement of intent for Seed and Discovery, but intent is not permission.

If this source is wanted later, the route is to ask the author for an explicit licence, or to read it for ideas and write original text — which is what "never relabel a rewrite as an upstream Skill" already requires. Do not copy it and do not cite it as an upstream.

## 6. elcodabra/validate-idea-skills — usable, marginal

- Repository: https://github.com/elcodabra/validate-idea-skills
- Licence: **MIT**.
- Signal at check time: 2 stars, 71 KB, last push `2026-11-03T21:49:04Z`.

A seven-step idea-validation pack: competitor research, value proposition, landing page, smoke test, acquisition, pre-sale, GO/PIVOT/KILL. Legally usable. Practically thin — two stars and a small surface mean it has not been exercised by anyone but its author, and its scope is market validation rather than product shaping.

Status: recorded as available, not selected. Process 02 Product Discovery already owns assumption testing and experiment design; this pack would duplicate it with weaker provenance.

## Why Product Shaping is reference-only

The upstream Product Shaping skill runs multiple phases in one guided process, including research, prototyping, interview, shaping document and gut-check. That is useful as a source, but it would collapse the deliberately separate Tab 01 / Tab 02 / Tab 03 responsibilities and could push The Seed into prototype/spec work too early. We therefore preserve it as upstream material and do not rewrite it into a fake upstream skill. The active workflow uses the Anthropic brainstorming skill for Tab 01 and custom, narrowly scoped workflow adapters for research and review.

## Change policy

- Never silently edit an upstream file in place.
- When updating an upstream copy, record the new source URL, retrieval date, upstream blob SHA, and license state.
- Put project-specific behavior in `seed-*` adapters, prompts and templates.
- A custom adapter is not an upstream skill and must never be described as one.
