# Feature: Layer editor

**ID prefix:** `LAY` · **Area:** central 33 × 33 grid, layer navigation and **Save / Edit / Delete** buttons

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started and `examples/basic-colors_palette.json` is loaded with **Load palette**

## Given the editor shows layer 1 of a new project

### When the tester looks at the editor

- [ ] **LAY-01** — Then it shows "Layer 1 / 25", status "Empty", ⏮ ◀ are disabled, **Save** / **Copy previous** / **Copy from layer…** / **Delete** are disabled and **Edit** is enabled

### When the tester uses ▶, ⏭ and then types 12 in the Layer field and presses Enter

- [ ] **LAY-02** — Then the editor moves to layers 2, 25 and 12 in turn and the orange frame in the top view follows the current layer

### When the tester hovers over the top-left cell of the grid

- [ ] **LAY-03** — Then the text under the grid shows "X: 1 · Level: 33"

## Given layer 1 is opened

### When the tester clicks Edit

- [ ] **LAY-04** — Then the status is "Editing", the cursor over the grid is a crosshair, **Edit** is disabled and **Save** is enabled

### When the tester clicks Edit, paints a few cells and clicks Save

- [ ] **LAY-05** — Then the message "Layer 1 saved." appears, the status is "Saved" (green) and the grid is read-only again

### When the tester clicks Edit, paints a cell and clicks ▶

- [ ] **LAY-06** — Then a confirmation about unsaved changes in layer 1 appears; Cancel keeps the editor on layer 1 with the changes, OK moves to layer 2 and discards them

## Given layer 1 is saved with blocks

### When the tester clicks Delete and accepts the confirmation

- [ ] **LAY-07** — Then the message "Layer 1 deleted." appears, the grid is empty and the status is "Empty"

### When the tester clicks Delete and cancels the confirmation

- [ ] **LAY-08** — Then the layer keeps all its blocks and the status stays "Saved"

### When the tester clicks Edit, erases every block and clicks Save

- [ ] **LAY-09** — Then the status is "Empty" (an empty layer is not stored)

## Given layer 1 is in edit mode with unsaved changes ("Editing • unsaved")

### When the tester tries to reload or close the browser tab

- [ ] **LAY-10** — Then the browser shows a "leave site?" warning
