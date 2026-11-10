# Navigation Model

## Global navigation structure
Describe hierarchy and relationships in text or Mermaid. This is structural, not visual. Identify all start/entry nodes.

## Node inventory
| Node ID | Node type: SCREEN / EXTERNAL_ENTRY / SYSTEM / TERMINAL | Screen ID (if applicable) | Purpose | Entry condition | Exit node(s) |
|---|---|---|---|---|---|

Every NODE ID must be unique. Every SCREEN ID must exist in 04_SCREEN_INVENTORY.md. External/system/terminal nodes must be explicitly typed and justified.

## Transition rules
| Transition ID | From Node ID | To Node ID | Trigger | Guard/condition | Result | Capability IDs |
|---|---|---|---|---|---|---|

Every source and destination must resolve to a declared node, except explicitly defined external endpoints.

## Entry, reachability and terminal analysis
- Entry node IDs:
- Reachable node IDs (from each entry):
- Unreachable node IDs:
- Terminal node IDs:
- Nodes with no outgoing transition:
- Orphan transitions:
- Loops and why they terminate:

## Back, cancel and external entry
Document behavior and unresolved decisions. Do not assume platform behavior where it affects product policy.

## Set comparison evidence
- Node IDs vs screen inventory references:
- Missing node/screen references:
- Duplicate IDs:
- Result: PASS / FAIL / NOT_VERIFIED
