# Product Discovery — Upstream Register

Checked: **2026-11-10**. Source repository: https://github.com/phuryn/pm-skills  
Package: https://github.com/phuryn/pm-skills/tree/main/pm-product-discovery  
License: **MIT**, copied to `product-discovery-kit/LICENSES/PM-SKILLS-MIT-LICENSE.txt`.

The source package README describes 13 skills and 5 commands. This kit intentionally selects methods used for discovery and retains the copied files verbatim under `.agents/skills/product-discovery/references/upstream/`. These are reference materials, not separate active Antigravity skills and not The Seed-specific instructions.

## Included upstream source files

| Upstream file | Local reference path | Upstream blob SHA | Use |
|---|---|---|---|
| `brainstorm-ideas-new/SKILL.md` | `references/upstream/brainstorm-ideas-new/SKILL.md` | `449ef41b53a1218261fb192053c56b233a28e1db` | Initial discovery ideation |
| `brainstorm-ideas-existing/SKILL.md` | `references/upstream/brainstorm-ideas-existing/SKILL.md` | `2228dd7097debad34abd05874d8c709fdac68d54` | Continuous discovery ideation |
| `identify-assumptions-new/SKILL.md` | `references/upstream/identify-assumptions-new/SKILL.md` | `3ddc8bc514b2a05cf5f0914635f144940797f5ac` | New-product risks |
| `identify-assumptions-existing/SKILL.md` | `references/upstream/identify-assumptions-existing/SKILL.md` | `66da6c92e1a0722791882f325734d1de3d98e5b2` | Existing-product risks |
| `prioritize-assumptions/SKILL.md` | `references/upstream/prioritize-assumptions/SKILL.md` | `bf7ed8a8ba9522cba14a7d5d0080fcfb69282e6b` | Impact/risk prioritization |
| `opportunity-solution-tree/SKILL.md` | `references/upstream/opportunity-solution-tree/SKILL.md` | `d62668118be00de5626e08488673ec22e7f83491` | Opportunity → solution → experiment map |
| `interview-script/SKILL.md` | `references/upstream/interview-script/SKILL.md` | `7ec574e0d107507cb6c1926d2620e2ac822c00b6` | Customer interview guide |
| `summarize-interview/SKILL.md` | `references/upstream/summarize-interview/SKILL.md` | `b4fee4359979f565a785f9ee704ab6d9ee48d54a` | Interview synthesis |
| `brainstorm-experiments-new/SKILL.md` | `references/upstream/brainstorm-experiments-new/SKILL.md` | `8c946a51839c85b7ffb666c268ca4b06513166ed` | New-product experiments |
| `brainstorm-experiments-existing/SKILL.md` | `references/upstream/brainstorm-experiments-existing/SKILL.md` | `cf151f5c2a8761dfc4bdf5a8c5b326775689437a` | Existing-product experiments |
| `analyze-feature-requests/SKILL.md` | `references/upstream/analyze-feature-requests/SOURCE.md` | `755b5cae934fb0fb8c334fdef10bbb358ed1492d` | Existing-product request triage |
| `commands/discover.md` | `references/upstream/discover-command/SOURCE.md` | `c7867a64ffb7d989be069e9f8a01baf4abcff72f` | Reference workflow |
| `commands/interview.md` | `references/upstream/interview-command/SOURCE.md` | `a8e228e3c43de5c26dc9930868efe8c1736cba74` | Reference interview workflow |
| Package README | `product-discovery-kit/upstream/README.md` | `cb36a5f39bfbb93f26c0bc75069c0c42869ca712` | Upstream package index |

## Excluded from active kit

- `metrics-dashboard`: primarily an analytics/dashboard setup task. Existing analytics may still be examined as evidence during discovery.
- `prioritize-features`: backlog/feature ranking can bias the process toward feature factory behavior. This kit prioritizes user opportunities and risky assumptions instead.
- Other package skills/commands unrelated to opportunity, evidence, assumptions, interviews and experiments.

## Adaptation boundary

Upstream files remain verbatim. The custom `product-discovery` skill and prompts add this repository's operating model: three separate tabs, input/output contracts, artifact locations, human approval gates, evidence labels and an explicit prohibition on moving into PRD/App Flow/UX/UI/implementation.

The upstream `discover` command is not invoked as the top-level runner because its end-to-end sequence differs from this staged, human-gated kit. Its methods are reference material.

## Update policy

When updating a source copy, record the check date, source URL, upstream blob SHA and license. Never edit a copied upstream file silently. Put project-specific behavior in the custom skill and prompts.
