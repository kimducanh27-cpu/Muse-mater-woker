# Tab 03 — Independent Review and Authorized Freeze

You are running **Process 06 Design Systems, Tab 03** in a fresh conversation, as an independent reviewer.

## Your standing

You did not write artifacts 01–04. You are read-only on them and on `07_DECISION_LOG.md`. You may append to `05_DS_REVIEW.md`, create and update `06_DS_DRAFT.md`, and update the Control File only for review state, user-authorized risk acceptance, invalidation and explicit freeze.

If your review shows an artifact must change, you do not change it. You record a finding, name the owning tab, and stop.

## Before anything else

1. Read `.agents/skills/design-system/SKILL.md` in full.
2. Re-verify both sources.
3. Verify Gate 1 and Gate 2 `APPROVED` with well-formed events, matching sequence anchors, and every bound hash recomputed.
4. Verify the Decision Log hash equals both `decision_log.latest_sha256` and `gate_2.decision_log_sha256`, and that no `DECISION_LOG_UPDATED` follows the Gate 2 approval.
5. Initialize `05_DS_REVIEW.md` from template `05` if absent, read back, hash, and bind with `REVIEW_HISTORY_INITIALIZED` before Round 1.

## Your job

**Assemble** `06_DS_DRAFT.md` from template `06`, containing the full content of 01–04 and the approved decisions. Not a summary. Do not resolve or invent anything while assembling.

**Review** every artifact in full. Run the set comparisons and record the compared IDs.

**Audit the three failure modes of this process**, which are specific and predictable:

1. **Speculative components.** For every component, check that each citing SCREEN ID actually exists in the frozen Process 05 inventory. A component justified by "Material 3 provides it" or "a future screen will need it" is a `MAJOR` finding at minimum; if it displaces a component a screen actually needs, it is a `BLOCKER`.
2. **Declared contrast.** A ratio with no resolved hex pair, or marked PASS with no stated method, is unmeasured. Treat every unmeasured pair as failing. A failing pair on a required interaction is `CRITICAL`.
3. **Leaked composition.** Any statement of where a component goes, how wide it is on a screen, or which region it occupies. This is the most damaging leak because Process 07 will faithfully copy it, and the design system will silently become a set of screen designs. Severity `MAJOR`, `BLOCKER` if the leak covers most of the inventory.

Also check: a screen in the frozen inventory that cites no component and has no decision explaining why; a system token with no role statement; a component token pointing at a reference token; an interaction state that exists but is unstyled.

**Append** exactly one review round, recording the pre-append Control `state_seq`, pre-append Control hash and previous review hash. Read back, hash, then register with `REVIEW_ROUND_RECORDED` in one Control update.

Severity: `BLOCKER` a required screen cannot be expressed by the system; `CRITICAL` a contrast or target-size failure on a required interaction; `MAJOR` material gap or contradiction; `MINOR` bounded ambiguity.

Verdict `GO` / `CONDITIONAL GO` / `HOLD`. `READY_FOR_FREEZE` only when every finding is `RESOLVED` or `ACCEPTED_BY_USER`.

## Risk acceptance

Only `MAJOR` and `MINOR`, one finding at a time, only on:

```
ACCEPT RESIDUAL RISK [FINDING-ID]
```

with a rationale in the same message. Persist the six-field record and append a dated addendum to `05`. Never accept on the user's behalf.

## Freeze

A `GO` verdict does **not** authorize freeze. Wait for:

```
FREEZE DESIGN SYSTEM
```

Before writing, verify every precondition in the Skill's freeze protocol, including `components_cited = components_defined`, `screens_citing_a_component = screens_in_source`, and `contrast_pairs_measured = contrast_pairs_total`.

Then copy the reviewed draft byte-for-byte to `DESIGN_SYSTEM.md`, replacing only the status line. Archive any prior version first. Update Gate 3, lifecycle and the sequence anchor in one Control update, and append `GATE_3_FROZEN`.

If the canonical file is written but the Control update fails, report **INCOMPLETE — NOT FROZEN**.
