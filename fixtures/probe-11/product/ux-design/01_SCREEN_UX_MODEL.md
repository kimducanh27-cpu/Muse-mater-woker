# 01 — Screen UX Model

> Artifact of Process 05. Owner: Tab 01. Bound by Gate 1.
> One entry per SCREEN ID from the frozen Process 04 inventory. Do not add, merge or rename screens.

## Rules for this artifact

- Every entry begins with the exact `SCREEN ID` from the frozen Process 04 inventory. No screen, no entry.
- Exactly one primary action per screen. If two actions compete, the hierarchy is unresolved and Gate 1 fails.
- The ordered hierarchy list is the contract. The structural block is illustrative only.
- No named UI component, colour, typeface, size, spacing value or image.
- Capability IDs must exist in the frozen Product Definition.
- Do not cite `NODE-` or `TRANSITION-` IDs. The frozen App Flow does not carry them. Describe entry in words instead.

---

## SCREEN-01 — Draft list

| Field | Value |
|---|---|
| Screen ID | `SCREEN-01` |
| Source screen | `SCREEN-01` — exists in the frozen Process 04 inventory |
| Entry transition | The user opens the application. The draft list is the first screen presented. The user may also arrive here after finishing work in the editor and choosing to leave it. |
| User goal on this screen | See all saved drafts and choose which one to open, or start a new one. |
| Primary action | Open a draft |
| Secondary actions | Start a new draft |
| Entry expectation | The user expects to see a list of previously saved drafts, ordered by recency. If none exist, the user expects a clear indication that the list is empty and a path to create the first draft. |
| Exit guarantee | A specific draft has been selected and the user proceeds to the editor, or a new draft has been initiated and the editor opens for it. |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | A first-time user may not know whether a draft they started was saved. They may scan the list looking for a name they remember but find nothing because the draft was never committed. The list must distinguish between drafts that exist and the absence of any draft. |

### Information hierarchy

1. The set of saved drafts, each identified by a distinguishable label and a recency signal
2. Whether the list is populated, loading, or empty
3. The means to begin a new draft
4. Any status signal indicating the last save action succeeded or is in progress

### Structural block — illustrative, not authoritative

```text
+------------------------------------------+
| Draft list                               |
|  [draft label]           [recency]       |
|  [draft label]           [recency]       |
|  [draft label]           [recency]       |
+------------------------------------------+
| [new draft]                              |
+------------------------------------------+
```

### Open questions

None.

---

## SCREEN-02 — Draft editor

| Field | Value |
|---|---|
| Screen ID | `SCREEN-02` |
| Source screen | `SCREEN-02` — exists in the frozen Process 04 inventory |
| Entry transition | The user arrives from the draft list by selecting an existing draft or initiating a new one. The editor opens with the selected draft's content pre-loaded, or blank for a new draft. |
| User goal on this screen | Write or revise the content of one draft without having to think about saving it. |
| Primary action | Save the draft |
| Secondary actions | Return to the draft list |
| Entry expectation | The user expects the draft content they last left to be present and unaltered. For a new draft, the user expects a blank, ready-to-write surface. The user expects to know whether the draft is currently saved. |
| Exit guarantee | On every exit, the draft's content at the moment of leaving is saved and will be retrievable from the draft list. The save status is communicated before the user leaves the screen. |
| Capability IDs served | `CAP-01` |
| Cognitive load risk | A first-time user may be uncertain whether their edits were saved before they leave. The editor must make the saved state unambiguous at all times so the user never has to decide whether to save manually before navigating away. |

### Information hierarchy

1. The editable content area containing the draft text
2. The current save status (saving, saved, or save-failed) so the user always knows whether their work is safe
3. The means to return to the draft list
4. Any error or recovery indication when saving fails

### Structural block — illustrative, not authoritative

```text
+------------------------------------------+
| [save status]            [back to list]  |
+------------------------------------------+
| Draft content area                       |
|                                          |
|                                          |
+------------------------------------------+
```

### Open questions

None.

---

## Coverage table — required at the end of the artifact

| Screen ID | Entry present | Primary action | Capability IDs | States owned (from P04 matrix) |
|---|---|---|---|---|
| `SCREEN-01` | yes | Open a draft | `CAP-01` | 3 (empty, loading, populated) |
| `SCREEN-02` | yes | Save the draft | `CAP-01` | 4 (default, saving, saved, save-failed) |

**Totals.** Screens in source: `2`. Screens with an entry: `2`. Capability IDs in frozen scope: `2` (`CAP-01` IN, `CAP-02` NOT NOW). Capabilities served: `1` (`CAP-01`; `CAP-02` is NOT NOW — deferred by Product Definition, no entry required).
