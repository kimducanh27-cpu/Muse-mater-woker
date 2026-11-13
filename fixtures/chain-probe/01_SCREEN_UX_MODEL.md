> SIMULATED — NOT ELIGIBLE DOWNSTREAM
# 01 — Screen UX Model

> Artifact of Process 05. Owner: Tab 01. Bound by Gate 1.
> One entry per SCREEN ID from the frozen Process 04 inventory. Do not add, merge or rename screens.

## Rules for this artifact

- Every entry begins with the exact `SCREEN ID` from `04_SCREEN_INVENTORY.md`. No screen, no entry.
- Exactly one primary action per screen. If two actions compete, the hierarchy is unresolved and Gate 1 fails.
- The ordered hierarchy list is the contract. The structural block is illustrative only.
- No named UI component, colour, typeface, size, spacing value or image.
- Capability IDs must exist in the frozen Product Definition.
- Do not cite `NODE-` or `TRANSITION-` IDs. Describe the entry in words instead.

---

## SCREEN-01 — Draft Editor

| Field | Value |
|---|---|
| Screen ID | `SCREEN-01` |
| Source screen | `SCREEN-01` — must exist in the frozen Process 04 inventory |
| Entry transition | User opens an existing saved draft or begins a fresh entry sequence |
| User goal on this screen | Capture structured response values and preserve draft progress |
| Primary action | Save draft |
| Secondary actions | Discard draft, Proceed to submission |
| Entry expectation | The editing environment reflects either blank inputs or previously saved draft values |
| Exit guarantee | All entered field values are committed to local persistent storage before leaving |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | User uncertainty whether unsaved changes are retained without explicit save confirmation |

### Information hierarchy

1. Form title and current draft persistence status indicator
2. Active input fields requiring user entry
3. Primary action control to commit current progress to storage
4. Auxiliary actions to discard or proceed

### Structural block — illustrative, not authoritative

```text
+------------------------------------------+
| Header Region                            |
|   Title                  Save Status     |
+------------------------------------------+
| Form Body Region                         |
|   Field Inputs                           |
+------------------------------------------+
| Action Region                            |
|   Save Draft Action                      |
+------------------------------------------+
```

### Open questions

- `OQ-01`: None blocking Gate 1.

---

## Coverage table — required at the end of the artifact

| Screen ID | Entry present | Primary action | Capability IDs | States owned (from P04 matrix) |
|---|---|---|---|---|
| `SCREEN-01` | yes | Save draft | `CAP-01` | 1 |

**Totals.** Screens in source: 1. Screens with an entry: 1. Capability IDs in frozen scope: 1. Capabilities served: 1.
