# Upstream source record — anthropics/knowledge-work-plugins (design)

Files in this directory are **byte-identical copies** of upstream. They are not edited, reformatted or renamed. Do not edit them: a local change would silently fork the method and make the provenance record false.

Retrieved: **2026-11-12** from `main`.

## Files

| Local path | Upstream path | Blob SHA-1 | Size (bytes) | SHA-256 |
|---|---|---|---|---|
| `design/skills/accessibility-review/SKILL.md` | `design/skills/accessibility-review/SKILL.md` | `3ef332cd837da5b4f7089503eb93e14c04090ccf` | 4,278 | `ef42982af0d51238dda2ab16d08626712891bdd41864876c32d1e7b13fb3124f` |
| `design/skills/design-critique/SKILL.md` | `design/skills/design-critique/SKILL.md` | `b6eaac1535f0a7482e35d91e039239ceb6031157` | 3,923 | `3a4f260eb9f60b431782bf6d90f22afb480c0c67860267a032df58a3e1bd19cd` |
| `design/skills/design-system/SKILL.md` | `design/skills/design-system/SKILL.md` | `0346fc13900d4cd8dbf79461a4ad6d7500fb3858` | 5,600 | `fb31bd0144c43955106f01927126ae9fd2d4148be44c8d5887b3391f40c31445` |
| `design/skills/ux-copy/SKILL.md` | `design/skills/ux-copy/SKILL.md` | `14ad66b916dbef712d0f35f208e1fdd137d28973` | 3,436 | `d46a00a62ec637e9ca9d5f7823ea3e0a4ec26dffc53bb5035f59b48ebfcdcde7` |
| `design/CONNECTORS.md` | `design/CONNECTORS.md` | `1443063b984d825aba151ae672c415c70c7b2829` | 1,139 | — |

Repository: https://github.com/anthropics/knowledge-work-plugins
Licence: **Apache-2.0**. The upstream package licence is preserved at `LICENSES/ANTHROPIC-PRODUCT-MANAGEMENT-LICENSE.txt`.

`CONNECTORS.md` is vendored only so that the relative link `../../CONNECTORS.md` inside each SKILL.md resolves. Without it every one of the four files carries a dangling reference.

## How these files may be used

They are **method references, not active skills.** They live outside `.agents/skills/` deliberately: if they were installed as active skills, an agent could load `accessibility-review` or `design-system` instead of the Process 05 or 06 gate contract, and the tab's write permissions, hash binding and gate rules would silently not apply.

A tab reads one of these when its own Skill tells it to, quotes the method it used, and records the path in the artifact. It never treats the upstream file as authority over the process contract. Where they disagree, the contract wins and the disagreement is recorded below.

## Recorded deviations

Verbatim copying imports upstream's assumptions along with its method. Two of them conflict with decisions this repository has already made. They are recorded here rather than patched in the copied files, because patching would make the copies no longer verbatim and the provenance record no longer true.

### D-1. Accessibility standard: upstream 2.1, contract 2.2

All four upstream files that discuss conformance say **WCAG 2.1 AA** (`accessibility-review/SKILL.md` lines 3, 11, 21, 66). Processes 05 and 06 record **WCAG 2.2 AA** in their accessibility artifacts.

**Resolution.** The contract governs. WCAG 2.2 supersedes 2.1 and adds criteria that 2.1 audits miss, including focus-not-obscured and dragging alternatives. When a tab uses `accessibility-review` as its method, it audits against 2.2 and records that it did so; it does not downgrade to match the upstream text.

This is exactly the failure mode that makes "copy verbatim and move on" unsafe: the copy carries a stale standard, and nothing in the copy signals that it is stale.

### D-2. Connector placeholders that have no meaning here

Each upstream file opens by pointing at `CONNECTORS.md` and assumes connected tools such as Figma. This workflow has no such connectors; its inputs are frozen markdown artifacts.

**Resolution.** The pointer resolves and the file is present, but a tab must treat any connector-dependent step as NOT APPLICABLE and record that it skipped it. Inventing a connector result to satisfy the method would be fabrication.

## What was deliberately not copied

`pbakaus/impeccable` is **not** vendored. Its playbooks are not self-contained: they invoke `impeccable context`, load `PRODUCT.md` and `DESIGN.md` through a binary, and depend on a design-detector hook. Copying the markdown alone would bake a broken dependency into the repository — instructions that call a tool that is not there. See `UPSTREAMS.md` section 4.
