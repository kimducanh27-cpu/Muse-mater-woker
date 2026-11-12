# 01 — Screen UX Model

> Artifact of Process 05. Owner: Tab 01. Bound by Gate 1.
> One entry per SCREEN ID from the frozen Process 04 inventory. Do not add, merge or rename screens.

## Rules for this artifact

- Every entry begins with the exact `SCREEN ID` from `04_SCREEN_INVENTORY.md`. No screen, no entry.
- Exactly one primary action per screen. If two actions compete, the hierarchy is unresolved and Gate 1 fails.
- The ordered hierarchy list is the contract. The structural block is illustrative only.
- No named UI component, colour, typeface, size, spacing value or image.
- Capability IDs must exist in the frozen Product Definition.
- **Do not cite `NODE-` or `TRANSITION-` IDs.** The frozen App Flow does not carry them: its schema has no node or transition inventory, and freeze copies the draft byte-for-byte. A required column that no upstream artifact can fill is not a requirement, it is a defect. Describe the entry in words instead.

---

## SCREEN-01 — Draft list

| Field | Value |
|---|---|
| Screen ID | `SCREEN-01` |
| Source screen | `SCREEN-01` — exists in the frozen Process 04 inventory |
| Entry transition | The user opens the application from an idle state and lands here as the first destination |
| User goal on this screen | See all existing drafts at a glance and choose which one to open or create a new one |
| Primary action | Open an existing draft |
| Secondary actions | Create a new draft |
| Entry expectation | The user expects to find any draft they previously saved waiting for them here |
| Exit guarantee | The user has selected a specific draft to work on, or has initiated creation of a new draft; no draft is lost or hidden |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | A first-time user may not understand that an empty list means no drafts have been saved yet, and may think previous work was lost |

### Information hierarchy

1. The list of saved drafts, ordered so the most recently touched draft is immediately visible
2. The title or label of each draft, sufficient to distinguish one from another
3. An affordance to begin a new draft when the list is empty or the user wants a fresh start
4. Supporting context (last-modified time or status) that confirms each draft is intact

### Structural block — illustrative, not authoritative

```text
+------------------------------------------+
| Draft list                               |
|   [draft title]        [last modified]   |
|   [draft title]        [last modified]   |
+------------------------------------------+
| New draft affordance                     |
+------------------------------------------+
```

### Open questions

- None.

---

## SCREEN-02 — Draft editor

| Field | Value |
|---|---|
| Screen ID | `SCREEN-02` |
| Source screen | `SCREEN-02` — exists in the frozen Process 04 inventory |
| Entry transition | The user arrives here after selecting an existing draft from the draft list, or after initiating a new draft from the draft list |
| User goal on this screen | Write or revise the draft and be confident it will be saved without manual effort |
| Primary action | Edit the draft content |
| Secondary actions | Save the draft explicitly |
| Entry expectation | The user expects the draft to load with its last-saved content intact and ready to edit |
| Exit guarantee | The draft content as of the last save is persisted; the user is never left uncertain whether their most recent edits are stored |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | A first-time user may not know when saving happens automatically versus when it requires explicit action, and may leave the screen fearing their edits were lost |

### Information hierarchy

1. The editable content area of the draft, occupying the primary focus so the user can begin writing immediately
2. A clear and persistent indication of the current save state (default, saving, saved, or save-failed) so the user never needs to guess
3. An affordance to trigger an explicit save when the user wants certainty
4. A way to navigate back to the draft list without losing saved content

### Structural block — illustrative, not authoritative

```text
+------------------------------------------+
| Navigation — back to list                |
+------------------------------------------+
| Draft content area (editable)            |
|                                          |
|                                          |
+------------------------------------------+
| Save status indicator   [Save action]    |
+------------------------------------------+
```

### Open questions

- None.

---

## Coverage table — required at the end of the artifact

| Screen ID | Entry present | Primary action | Capability IDs | States owned (from P04 matrix) |
|---|---|---|---|---|
| `SCREEN-01` | yes | Open an existing draft | `CAP-01` | `3` (empty, loading, populated) |
| `SCREEN-02` | yes | Edit the draft content | `CAP-01` | `4` (default, saving, saved, save-failed) |

**Totals.** Screens in source: `2`. Screens with an entry: `2`. Capability IDs in frozen scope: `2` (`CAP-01` IN, `CAP-02` NOT NOW). Capabilities served: `1` (`CAP-01`; `CAP-02` deferred per Product Definition status NOT NOW).
