# 09 — UX Spec (frozen output schema)

> This is the schema of the frozen artifact `product/ux-design/UX_SPEC.md`. It is not a working file.
> The frozen artifact is produced by copying the reviewed draft byte-for-byte and replacing exactly one line.

> Status: FROZEN

## Freeze invariants

| Invariant | Rule |
|---|---|
| Content source | Byte-for-byte copy of `07_UX_SPEC_DRAFT.md` |
| Permitted change | Only the status line, from `> Status: REVIEWED CANDIDATE — NOT FROZEN` to `> Status: FROZEN` |
| Forbidden | Rebuilding, summarising, reordering, re-formatting, adding a hash or a timestamp |
| Hash location | Control File `gate_3.frozen_artifact.sha256` only. Never inside this file |
| Version | `gate_3.frozen_version`, incremented by one per freeze |
| Prior version | Archived byte-for-byte as `UX_SPEC.v<N>.md` before replacement |

A file that differs from the reviewed draft by anything other than the status line is `NOT_VERIFIED`, even if its hash is recorded in the Control File. A file present at this path without a matching `GATE_3_FROZEN` event and sequence anchor is an orphan and is not eligible downstream.

## Required sections

### 1. Document identity

| Field | Value |
|---|---|
| Process | 05 UX Design |
| Initiative ID | |
| Source Process 04 frozen artifact | `product/app-flow/APP_FLOW.md` |
| Source Process 04 SHA-256 | |
| Source Product Definition SHA-256 | |
| Frozen version | |
| Review round | |

### 2. Screen UX model

Complete content of artifact 01, in screen ID order.

### 3. Interaction patterns

Complete content of artifact 02.

### 4. State experience

Complete content of artifact 03, in screen ID order then state ID order.

### 5. Content and copy intent

Complete content of artifact 04.

### 6. Accessibility requirements

Complete content of artifact 05.

### 7. Approved decisions

Every decision `APPROVED` at freeze time, with DEC ID, statement, rationale and bound artifacts. Proposals, rejected and deferred decisions are listed under section 8 and are not policy.

### 8. Open questions

Every question still open at freeze, with what it blocks and why it does not alter the frozen contract.

### 9. Accepted residual risks

Every accepted MAJOR or MINOR finding with finding ID, severity, exact command and rationale.

### 10. Coverage statement

| Counter | Source count | Covered |
|---|---|---|
| Screens | | |
| Applicable screen-state pairs | | |
| Capabilities | | |

### 11. Boundary declaration

This specification defines experience only. It contains no colour, typography, spacing, elevation, iconography, component definition, design token, final copy, code or prototype.

## Downstream contract

A Process 06 consumer must, before reading any section, independently:

1. Read `product/ux-design/00_UX_CONTROL.md` and confirm `lifecycle_status: FROZEN`.
2. Confirm all three gates `APPROVED` and that each `approved_state_seq` equals its own approval event's `state_seq`.
3. Recompute the actual SHA-256 of this file and compare it with `gate_3.frozen_artifact.sha256`.
4. Confirm the latest review snapshot in the Control File still matches `07_UX_SPEC_DRAFT.md`.
5. Confirm both source statuses remain `VERIFIED` against the current Process 04 artifacts.

Any mismatch blocks Process 06. A FROZEN status line, a filename or a prior agent's claim is never proof of freeze.
