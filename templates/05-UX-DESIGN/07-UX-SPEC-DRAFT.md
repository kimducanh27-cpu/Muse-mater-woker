# 07 — UX Spec Draft

> Owner: Tab 03. This is the complete reviewed candidate, not a summary.
> It must begin with the exact status line below. Freeze changes only that line.

> Status: REVIEWED CANDIDATE — NOT FROZEN

## How to assemble this draft

- Copy the full content of artifacts 01–05 and the approved decisions from 08. Do not summarise, compress or reorder.
- Do not resolve, invent or introduce a product or UX decision while assembling. If assembly reveals a contradiction, record it as a finding in 06 and stop.
- Do not add a hash, a freeze timestamp or a Control File sequence number to this file. Those live in the Control File.
- Preserve every stable ID exactly: `SCREEN-`, `NODE-`, `TRANSITION-`, `STATE-`, `PAT-`, `MSG-`, `CAP-`, `DEC-`, `DLE-`, `F-`.

## Required sections

### 1. Document identity

| Field | Value |
|---|---|
| Process | 05 UX Design |
| Initiative ID | |
| Source Process 04 frozen artifact | `product/app-flow/APP_FLOW.md` |
| Source Process 04 SHA-256 | |
| Source Product Definition SHA-256 | |
| Draft assembled at local | |
| Review round | |

### 2. Screen UX model

Full content of `01_SCREEN_UX_MODEL.md`, in screen ID order.

### 3. Interaction patterns

Full content of `02_INTERACTION_PATTERNS.md`.

### 4. State experience

Full content of `03_STATE_EXPERIENCE.md`, in screen ID order then state ID order.

### 5. Content and copy intent

Full content of `04_CONTENT_AND_COPY_INTENT.md`.

### 6. Accessibility requirements

Full content of `05_ACCESSIBILITY_REQUIREMENTS.md`.

### 7. Approved decisions

Every decision currently `APPROVED`, with its DEC ID, statement, rationale and the artifacts it binds. Proposals, rejected and deferred decisions are listed separately under section 8 and are not policy.

### 8. Open questions and unresolved items

Every question that remains open, with what it blocks. An open question that changes a screen goal, a primary action or a state is a Gate blocker; an open question that changes nothing in the contract is recorded and does not block.

### 9. Accepted residual risks

Every MAJOR or MINOR finding accepted by the user, with finding ID, severity, exact command and rationale.

### 10. Coverage statement

| Counter | Source count | Covered |
|---|---|---|
| Screens | | |
| Applicable screen-state pairs | | |
| Capabilities | | |

These numbers must equal the `coverage` block in the Control File at freeze time. A draft whose coverage is lower than the source count cannot be frozen.

### 11. Boundary declaration

This specification defines experience only. It contains no colour, typography, spacing, elevation, iconography, component definition, design token, final copy, code or prototype. Visual language is Process 06; composition is Process 07; conformance evidence is Process 08.

## Assembly checks — complete before appending a review round

| Check | Result |
|---|---|
| Status line is exactly `> Status: REVIEWED CANDIDATE — NOT FROZEN` | |
| Every artifact 01–05 section present and complete | |
| No named UI component anywhere in the document | |
| No colour, typeface, size, spacing, radius or shadow value | |
| Every `SCREEN-` ID in the draft exists in the Process 04 inventory | |
| Every `STATE-` ID in the draft exists in the Process 04 matrix | |
| Every `PAT-` and `MSG-` ID cited is defined in this document | |
| Coverage numbers equal the source counts | |
