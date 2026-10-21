# Feature: Tools & options

**ID prefix:** `TOL` · **Area:** *Tool* section, symmetry and previous-layer options, layer editor grid

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started and `examples/basic-colors_palette.json` is loaded with **Load palette**
- **And** slot `01` (Red) is selected

## Given layer 1 is in edit mode (Edit clicked)

### When the tester drags across the grid with the left mouse button

- [ ] **TOL-01** — Then every cell the cursor passes over is painted red

### When the tester drags across painted cells with the right mouse button

- [ ] **TOL-02** — Then those cells are erased (Brush stays the active tool)

### When the tester presses E and drags with the left mouse button

- [ ] **TOL-03** — Then **Eraser (E)** is highlighted and the cells are erased

### When the tester presses B while the Eraser is active

- [ ] **TOL-04** — Then **Brush (B)** is highlighted again and left-dragging paints

### When the Eraser is active and the tester clicks a saved palette slot

- [ ] **TOL-05** — Then the tool switches back to **Brush (B)** automatically

## Given layer 1 is in edit mode and Left–right symmetry is ticked

### When the tester looks at the grid

- [ ] **TOL-06** — Then an orange dashed vertical line runs through the middle of the center column (17)

### When the tester paints the cell at X 5

- [ ] **TOL-07** — Then the mirrored cell at X 29 in the same row is painted too, and while hovering both cells are outlined

### When the tester paints a cell in column 17

- [ ] **TOL-08** — Then only that single cell is painted (no duplicate)

### When the tester unticks Left–right symmetry

- [ ] **TOL-09** — Then the dashed line disappears and painting no longer mirrors

## Given layer 1 is saved with blocks and layer 2 is in edit mode (build direction Bow → Stern)

### When the tester ticks Show previous layer

- [ ] **TOL-10** — Then the blocks of layer 1 appear as a faint, semi-transparent shadow in the empty cells of layer 2 and are not saved with layer 2

## Given the current layer is NOT in edit mode

### When the tester clicks on the grid

- [ ] **TOL-11** — Then the message "Click "Edit" to edit this layer." appears and nothing is painted
