# P04 — Repository Owner Decision Register

- **Target specification:** P04 Remediation Plan v0.3.1
- **Decision date:** 2026-11-12
- **Decision status:** ALL OWNER DECISIONS APPROVED
- **Implementation authorization:** Granted by the Owner's explicit instruction `triển full luôn đi`, limited to this approved P04 scope on a dedicated branch.
- **Merge authorization:** NOT GRANTED.
- **Runtime verification:** NOT RUN.

## 1. Approved ADRs

| ID | Decision | Approved scope | Status |
|---|---|---|---|
| ADR-P04-01 | Decision Log enum and pairing | `DECISION_STATUS_CHANGED`; preserve append-only history; unverified legacy events remain `LEGACY_UNVERIFIED` / `NOT_VERIFIED`. | APPROVED |
| ADR-P04-02 | Sole CR source of truth | Register is the sole CR business-state source; Control stores receipts, checkpoints and commit evidence only. | APPROVED |
| ADR-P04-03 | Paired append-and-receipt protocol | Paired Register/Control append-and-receipt; canonical byte/hash-chain and bounded recovery from v0.3.1. | APPROVED |
| ADR-P04-04 | Submission boundary and CR-ID ownership | External processes submit immutable payloads; Tab 01 verifies source/hash/idempotency, assigns CR-ID and owns intake; no external Register writes. | APPROVED |
| ADR-P04-05 | Three-tab ownership | Tab 01 coordinates CR lifecycle/Register; Tab 02 performs assigned work only; Tab 03 reviews/Freeze and never writes CR business state. | APPROVED |
| ADR-P04-06 | CR State Machine | Adopt 13 business states and closed T01–T18; no REFROZEN; NOT_VERIFIED is integrity-only. | APPROVED |
| ADR-P04-07 | Gate validity and downstream eligibility | Keep Gate validity, Freeze eligibility and downstream eligibility distinct; a new CR blocks downstream without byte-change-based Gate invalidation. | APPROVED |
| ADR-P04-08 | P03 return and re-entry | Preserve CR-ID; verify each CR against its own P03 return snapshot; P03 schema v2 remains unchanged. | APPROVED |
| ADR-P04-09 | Control Schema v4 and migration | Adopt v4; preserve v3 approvals only when sequence and every bound hash/evidence verify; migration is one logical transaction/one complete Control replacement. | APPROVED |
| ADR-P04-10 | Downstream frozen binding | Bind initiative/schema/frozen version/hash/P03 source/Gate sequences/Register hash+sequence/empty blockers; no circular Control sequence in APP_FLOW. | APPROVED |
| ADR-P04-11 | Non-self-referential event-block hash (P04-IMP-01) | Resolve the P0 blocker by sentinel normalization: `event_block_sha256` is computed over the event block with that field's value replaced by the literal `<HASH_OMITTED>`; writers hash then write the digest, readers substitute then recompute. This is the only permitted normalization in Register v1. It supersedes the "exact bytes including the hash field" preimage rule of P04 Remediation Plan v0.3.1 Section 4.4 for this field only; the plan file is not rewritten and its recorded SHA-256 remains valid. | APPROVED |

## 2. Approved clarifications

| ID | Decision | Approved scope | Status |
|---|---|---|---|
| CL-01 | Abort pair and hash-chain | One receipt commits staged event plus abort marker; H(k) is internal, not a checkpoint; staged event is ABORTED_NOT_EFFECTIVE; recovery never duplicates the marker. | APPROVED |
| CL-02 | Register initialization | Register starts at seq 0 with non-null H_init, CHANGE_REQUEST_REGISTER_INITIALIZED and Control receipt; zero-CR workspaces remain verifiable. | APPROVED |
| CL-03 | Migration transaction | SCHEMA_MIGRATED and CHANGE_REQUEST_REGISTER_INITIALIZED are one logical transaction in one complete Control replacement, with explicit staging/verification/recovery. | APPROVED |
| CL-04 | Accepted CR cancellation/clarification | No ACCEPTED_FOR_IMPLEMENTATION→TRIAGE or →NEEDS_CLARIFICATION; use T14 if no bytes changed, T15/T16 after byte changes; rescope via a new linked CR; no T19. | APPROVED |
| CL-05 | Partial batch closure | Batch command expands to individual idempotent CR-close events/receipts under one Freeze batch; downstream remains blocked until all batch CRs are closed and verified. | APPROVED |

## 3. Approval summary

- ADRs approved: **11/11** (10 at intake, ADR-P04-11 added on 2026-11-12 to resolve P04-IMP-01).
- Clarifications approved: **5/5**.
- Total Owner decisions approved: **16/16**.
- Implementation authorization: **GRANTED for a dedicated branch** by explicit Owner instruction on 2026-11-12.
- Merge authorization: **NOT GRANTED**.
- Runtime verification: **NOT RUN**.

## 3a. P04-IMP-01 resolution record

- **Blocker:** the approved specification required `event_block_sha256` to be a SHA-256 of an event block that contains the field itself, making the preimage self-referential and the value underivable.
- **Decision:** ADR-P04-11, sentinel normalization (option 1 of the two models presented in `P04-IMPLEMENTATION-RECORD-v0.3.1.md`).
- **Normative artifacts amended:** `.agents/skills/app-flow/SKILL.md` (Register v1 canonical bytes and hash definitions) and `templates/04-APP-FLOW/11-CHANGE-REQUEST-REGISTER.md` (event block field and hash rule).
- **Deliberately not amended:** `app-flow-kit/specs/P04-REMEDIATION-PLAN-v0.3.1.md`. It is an approved artifact with a recorded SHA-256; rewriting it would invalidate that provenance. Its Section 4.4 preimage rule is superseded for this field by reference, not by edit.
- **Verification status:** static only. No Register writer exists yet, so the sentinel rule has not been executed against a real workspace. Runtime remains NOT RUN.

## 4. Provenance

- Owner decisions were made in the conversation on 2026-11-12.
- P04 Remediation Plan v0.3.1 source SHA-256: `cb982ff1ed2592ea44e8e5173c887b32143b13023c91553ee013ab4839cc32c6`.
- Pre-existing Owner Decision Register intake SHA-256: `e7c343742d2b7fdae9f015b4604a11c7598ee9451c38ea0a2c73910389166d69`.
- Verified repository `kimducanh27-cpu/app-adr-ui`, `main` HEAD: `99ac2c629a5e3ecc53e45f2b923163b0593d5b6a`.
- Implementation branch: `p04/implementation-v0.3.1`.
- Phase 1 isolated Decision Log correction commit: `16861152249e2c2983d8f067f677e32e22068db2`.
- No P03 file/schema change is authorized.

## 5. Limits

This register records Owner decisions. It does not claim runtime flows passed or authorize merge to `main`. Static verification and independent review apply to the actual branch diff; Windows Antigravity tests remain NOT RUN until evidenced.
