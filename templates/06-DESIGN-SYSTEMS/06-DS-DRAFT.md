# 06 — Design System Draft

> Owner: Tab 03. Complete reviewed candidate, not a summary.
> Must begin with the exact status line below. Freeze changes only that line.

> Status: REVIEWED CANDIDATE — NOT FROZEN

## How to assemble this draft

- Copy the full content of artifacts 01–04 and the approved decisions from 07. Do not summarise, compress or reorder.
- Do not resolve, invent or introduce a design decision while assembling. A contradiction found during assembly is a finding, not an edit.
- Do not add a hash, freeze timestamp or Control sequence number.
- Preserve every stable ID exactly: `CMP-`, `CP-`, `SCREEN-`, `DEC-`, `DLE-`, `F-`.

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
| Draft assembled at local | |
| Review round | |

### 2. Design foundations

Full content of `01_DESIGN_FOUNDATIONS.md`.

### 3. Token contract

Full content of `02_TOKEN_CONTRACT.md`, all three layers.

### 4. Component inventory

Full content of `03_COMPONENT_INVENTORY.md`, in component ID order, each entry with its citing screens.

### 5. Component accessibility

Full content of `04_COMPONENT_ACCESSIBILITY.md`, including the measured contrast table.

### 6. Approved decisions

Every decision currently `APPROVED`, with DEC ID, statement, rationale and bound artifacts.

### 7. Open questions and unresolved items

Every question still open, with what it blocks. An open question that changes a foundation role or a component's admission is a Gate blocker.

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

These numbers must equal the `coverage` block in the Control File at freeze time.

### 10. Boundary declaration

This specification defines a visual system. It contains no screen layout, no placement, no composition, no final copy, no code and no image. Composition is Process 07; conformance evidence is Process 08.

## Assembly checks — complete before appending a review round

| Check | Result |
|---|---|
| Status line is exactly `> Status: REVIEWED CANDIDATE — NOT FROZEN` | |
| Every artifact 01–04 section present and complete | |
| Every component entry carries at least one citing SCREEN ID | |
| Every cited SCREEN ID exists in the frozen Process 05 inventory | |
| Every contrast pair has a resolved hex pair and a ratio | |
| No screen layout, region or placement described anywhere | |
| No final copy, code or image | |
| Coverage numbers equal the source counts | |
