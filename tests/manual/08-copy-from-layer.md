# Feature: Copy from layer dialog

**ID prefix:** `CPY` · **Area:** **Copy from layer…** button, dialog and layer numbers in the top view

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started and `examples/basic-colors_palette.json` is loaded with **Load palette**
- **And** layers 3 and 10 are saved with different blocks (layer 10 has exactly 3 blocks); build direction is **Bow → Stern**

## Given layer 20 is opened but NOT in edit mode

### When the tester looks at the editor buttons

- [ ] **CPY-01** — Then **Copy from layer…** is disabled

## Given layer 20 is in edit mode

### When the tester clicks Copy from layer…

- [ ] **CPY-02** — Then a dialog "Copy from layer" opens naming layer **20** as the target, with an empty *Source layer* field and **Copy** disabled
- [ ] **CPY-03** — Then a column of layer numbers appears left of the top view: 3 and 10 bright, empty layers dim, 20 orange, and the hint reads "Click a row to pick it as the source layer."

### When the tester types 10 in the dialog

- [ ] **CPY-04** — Then the status reads "Layer 10 — saved, 3 blocks." in green, row 10 is highlighted green in the top view and **Copy** is enabled

### When the tester types 5, then 20, then 99 in the dialog

- [ ] **CPY-05** — Then the status reads "Layer 5 is empty.", "This is the layer you are editing." and "Enter a number from 1 to 25." respectively, and **Copy** stays disabled

### When the tester clicks row 3 in the top view while the dialog is open

- [ ] **CPY-06** — Then the field changes to 3 and the editor stays on layer 20

### When the tester selects layer 10 and clicks Copy (or presses Enter)

- [ ] **CPY-07** — Then layer 10's blocks appear in the editor, the dialog closes, the number column disappears and the status reads "Editing • unsaved"

### When the tester presses Esc or clicks Cancel

- [ ] **CPY-08** — Then the dialog closes, the number column disappears and the editor content is unchanged

## Given layer 20 is in edit mode and the dialog is open

### When the tester clicks ◀ in the layer navigation (and accepts the unsaved-changes warning if shown)

- [ ] **CPY-09** — Then the dialog closes automatically and the editor shows layer 19 in read-only mode

## Given layer 11 is in edit mode (previous layer 10 is saved)

### When the tester clicks Copy from layer…

- [ ] **CPY-10** — Then the *Source layer* field is pre-filled with 10 and the status shows it as saved
