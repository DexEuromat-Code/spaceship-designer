# Feature: Top view

**ID prefix:** `TOP` · **Area:** *Top view* panel (right column)

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a project is prepared with saved layers 1–10 that contain blocks on the top row (level 33) and on lower levels

## Given the project has just been loaded

### When the tester looks at the top view

- [ ] **TOP-01** — Then it shows "Level 33 / 33" and the ⤒ ▲ buttons are disabled
- [ ] **TOP-02** — Then "▲ Bow" is above the grid, "▼ Stern" below it, and there is one row per layer (bow = row 1 at the top)

### When the tester uses ▼, ⤓, ▲ and ⤒

- [ ] **TOP-03** — Then the level number changes accordingly (⤓ = 1, ⤒ = 33) and the dashed orange frame in the layer editor moves to the matching row

### When the tester views a level that contains blocks

- [ ] **TOP-04** — Then blocks on that level are shown in their colors, and columns that have blocks only on other levels are shown in dark blue (silhouette)

### When the tester clicks row 8

- [ ] **TOP-05** — Then the layer editor opens layer 8 and the orange frame in the top view is on row 8

### When the tester hovers over a cell

- [ ] **TOP-06** — Then a tooltip shows "Layer n, X: m" for that cell

## Given a layer is in edit mode

### When the tester paints cells on the level shown in the top view

- [ ] **TOP-07** — Then the top view updates immediately, before the layer is saved
