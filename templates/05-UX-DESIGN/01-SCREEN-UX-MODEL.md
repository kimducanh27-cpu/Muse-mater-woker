# 01 — Screen UX Model

> Artifact of Process 05. Owner: Tab 01. Bound by Gate 1.
> One entry per SCREEN ID from the frozen Process 04 inventory. Do not add, merge or rename screens.

## Rules for this artifact

- Every entry begins with the exact `SCREEN ID` from `04_SCREEN_INVENTORY.md`. No screen, no entry.
- Exactly one primary action per screen. If two actions compete, the hierarchy is unresolved and Gate 1 fails.
- The ordered hierarchy list is the contract. The structural block is illustrative only.
- No named UI component, colour, typeface, size, spacing value or image.
- Capability IDs must exist in the frozen Product Definition.

---

## SCREEN-<ID> — <screen name>

| Field | Value |
|---|---|
| Screen ID | `SCREEN-<ID>` |
| Source node / transition | `NODE-<ID>`, `TRANSITION-<ID>` |
| User goal on this screen | One sentence, outcome-shaped |
| Primary action | Exactly one |
| Secondary actions | Ordered list, may be empty |
| Entry expectation | What the user believes before arriving |
| Exit guarantee | What is true when the user leaves, in every exit |
| Capability IDs served | `CAP-<ID>`, … |
| Cognitive load risk | What a first-time user is most likely to misunderstand |

### Information hierarchy

1. First thing the user must perceive
2. Second
3. Third
4. Supporting detail, if any

### Structural block — illustrative, not authoritative

```text
+------------------------------------------+
| <region label>                           |
|   <element>              <element>       |
+------------------------------------------+
| <region label>                           |
|   <element>                              |
+------------------------------------------+
```

### Open questions

- `OQ-<NN>`: question, and what it blocks.

---

## Coverage table — required at the end of the artifact

| Screen ID | Entry present | Primary action | Capability IDs | States owned (from P04 matrix) |
|---|---|---|---|---|
| `SCREEN-<ID>` | yes | `<action>` | `CAP-<ID>` | `<n>` |

**Totals.** Screens in source: `<n>`. Screens with an entry: `<n>`. Capability IDs in frozen scope: `<n>`. Capabilities served: `<n>`.
