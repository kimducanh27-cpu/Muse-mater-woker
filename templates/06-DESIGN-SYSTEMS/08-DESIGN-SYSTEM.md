# 08 — Design System (frozen output schema)

> Schema of the frozen artifact `product/design-system/DESIGN_SYSTEM.md`. Not a working file.
> Produced by copying the reviewed draft byte-for-byte and replacing exactly one line.

> Status: FROZEN

## Freeze invariants

| Invariant | Rule |
|---|---|
| Content source | Byte-for-byte copy of `06_DS_DRAFT.md` |
| Permitted change | Only the status line, from `> Status: REVIEWED CANDIDATE — NOT FROZEN` to `> Status: FROZEN` |
| Forbidden | Rebuilding, summarising, reordering, re-formatting, adding a hash or a timestamp |
| Hash location | Control File `gate_3.frozen_artifact.sha256` only |
| Version | `gate_3.frozen_version`, incremented by one per freeze |
| Prior version | Archived byte-for-byte as `DESIGN_SYSTEM.v<N>.md` before replacement |

A file that differs from the reviewed draft by anything other than the status line is `NOT_VERIFIED`, even if its hash is recorded. A file present at this path without a matching `GATE_3_FROZEN` event and sequence anchor is an orphan and is not eligible downstream.

## Required sections

### 1. Document identity

| Field | Value |
|---|---|
| Process | 06 Design Systems |
| Initiative ID | |
| Platform | `android` / `jetpack-compose` / `material-3` |
| Source Process 05 frozen artifact | `product/ux-design/UX_SPEC.md` |
| Source Process 05 SHA-256 | |
| Source Process 04 SHA-256 | |
| Frozen version | |
| Review round | |

### 2. Design foundations

Complete content of artifact 01.

### 3. Token contract

Complete content of artifact 02, all three layers.

### 4. Component inventory

Complete content of artifact 03, in component ID order, each entry with its citing screens.

### 5. Component accessibility

Complete content of artifact 04, including measured contrast.

### 6. Approved decisions

Every decision `APPROVED` at freeze time.

### 7. Open questions

Every question still open at freeze, with what it blocks and why it does not alter the frozen system.

### 8. Accepted residual risks

Every accepted MAJOR or MINOR finding with finding ID, severity, exact command and rationale.

### 9. Coverage statement

| Counter | Source count | Covered |
|---|---|---|
| Screens | | |
| Screens citing at least one component | | |
| Components defined | | |
| Components cited | | |
| Contrast pairs required | | |
| Contrast pairs measured | | |

### 10. Boundary declaration

This specification defines a visual system. It contains no screen layout, placement, composition, final copy, code or image.

## Downstream contract

A Process 07 consumer must, before reading any section, independently:

1. Read `product/design-system/00_DS_CONTROL.md` and confirm `lifecycle_status: FROZEN`.
2. Confirm all three gates `APPROVED` and each `approved_state_seq` equals its own approval event's `state_seq`.
3. Recompute the actual SHA-256 of this file and compare it with `gate_3.frozen_artifact.sha256`.
4. Confirm the latest review snapshot still matches `06_DS_DRAFT.md`.
5. Confirm both source statuses remain `VERIFIED` against the current Process 05 artifacts.
6. Confirm `platform.target` equals the platform Process 07 is composing for.

Any mismatch blocks Process 07. A FROZEN status line is never proof of freeze.
