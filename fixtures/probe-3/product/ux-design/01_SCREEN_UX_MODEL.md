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

## SCREEN-01 — Draft list

| Field | Value |
|---|---|
| Screen ID | `SCREEN-01` |
| Source node / transition | NOT APPLICABLE (probe fixture APP_FLOW.md specifies screen inventory and state matrix without node or transition identifiers) |
| User goal on this screen | Locate and open an existing saved draft or begin a new draft |
| Primary action | Open selected draft to resume writing |
| Secondary actions | Create new draft |
| Entry expectation | The user expects to see all previously saved writing drafts available to resume |
| Exit guarantee | The selected draft or a new draft workspace is opened with no draft loss |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | A first-time user with no prior drafts may be unclear on whether drafts persist automatically or require manual initiation |

### Information hierarchy

1. Presence and status of existing saved drafts
2. Identifier and preview text of each draft
3. Affordance to create a new draft
4. Supporting system status or feedback message

### Structural block — illustrative, not authoritative

```text
+--------------------------------------------------------------------------------------------------+
| Draft collection overview                                                                        |
|   Collection status                     Create draft affordance                                  |
+--------------------------------------------------------------------------------------------------+
| Saved drafts area                                                                                |
|   Draft item title                      Draft state indicator                                    |
|   Draft preview summary                                                                          |
+--------------------------------------------------------------------------------------------------+
```

### Open questions

- NOT APPLICABLE: No open questions blocking SCREEN-01 model.

---

## SCREEN-02 — Draft editor

| Field | Value |
|---|---|
| Screen ID | `SCREEN-02` |
| Source node / transition | NOT APPLICABLE (probe fixture APP_FLOW.md specifies screen inventory and state matrix without node or transition identifiers) |
| User goal on this screen | Compose and edit draft content with certainty that progress is saved |
| Primary action | The user taps the primary button in the app bar to commit the edit |
| Secondary actions | Return to draft list, retry save if save failed |
| Entry expectation | The user expects to view and modify their document content with immediate confirmation of draft save state |
| Exit guarantee | The draft is retained in storage so the user never has to remember whether changes were saved |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | The user may worry that leaving the editor discards unsaved text if the current save status is ambiguous |

### Information hierarchy

1. Current draft save confirmation status
2. Document content editing area
3. Navigation affordance to return to draft list
4. Error recovery affordance if save fails

### Structural block — illustrative, not authoritative

```text
+--------------------------------------------------------------------------------------------------+
| Editor header area                                                                               |
|   Return navigation                     Save status confirmation                                 |
+--------------------------------------------------------------------------------------------------+
| Document composition area                                                                        |
|   Draft text content                                                                             |
|   Save error recovery notification (when save fails)                                             |
+--------------------------------------------------------------------------------------------------+
```

### Open questions

- NOT APPLICABLE: No open questions blocking SCREEN-02 model.

---

## Coverage table — required at the end of the artifact

| Screen ID | Entry present | Primary action | Capability IDs | States owned (from P04 matrix) |
|---|---|---|---|---|
| `SCREEN-01` | yes | Open selected draft to resume writing | `CAP-01` | 3 |
| `SCREEN-02` | yes | Edit draft content | `CAP-01` | 4 |

**Totals.** Screens in source: 2. Screens with an entry: 2. Capability IDs in frozen scope: 1. Capabilities served: 1.
