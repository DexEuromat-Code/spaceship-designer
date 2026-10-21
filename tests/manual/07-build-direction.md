# Feature: Build direction & Copy previous

**ID prefix:** `DIR` · **Area:** *Build direction* selector, **Copy previous** button, *Show previous layer* option

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started and `examples/basic-colors_palette.json` is loaded with **Load palette**

## Given a new project with layer 1 in edit mode

### When the tester looks at the Build direction selector and the editor buttons

- [ ] **DIR-01** — Then **Bow → Stern** is highlighted and **Copy previous** is disabled (layer 1 has no bow-side neighbor)

## Given direction Bow → Stern, layers 4 and 6 saved with different blocks, layer 5 in edit mode

### When the tester looks at the Copy previous button

- [ ] **DIR-02** — Then the button reads "Copy previous (4)"

### When the tester clicks Copy previous

- [ ] **DIR-03** — Then layer 4's blocks are loaded into the editor, the status reads "Editing • unsaved" and the message "Layer 4 copied into layer 5 — click "Save" to keep it." appears

### When the tester ticks Show previous layer

- [ ] **DIR-04** — Then the shadow under the grid shows layer 4

## Given layers 4 and 6 are saved with different blocks and layer 5 is in edit mode

### When the tester clicks Stern → Bow

- [ ] **DIR-05** — Then **Stern → Bow** is highlighted, a message explains "previous = layer on the stern side (N+1)" and the button reads "Copy previous (6)"

### When the tester switches to Stern → Bow and clicks Copy previous

- [ ] **DIR-06** — Then layer 6's blocks are loaded into the editor

### When the tester switches to Stern → Bow and ticks Show previous layer

- [ ] **DIR-07** — Then the shadow under the grid shows layer 6

## Given direction Stern → Bow and the last layer (25) is in edit mode

### When the tester looks at the Copy previous button

- [ ] **DIR-08** — Then the button reads "Copy previous" and is disabled

## Given a project with direction Stern → Bow was saved with Save to JSON

### When the tester starts a new project and loads that file with Load JSON

- [ ] **DIR-09** — Then **Stern → Bow** is highlighted and the editor opens at the last layer

### When the tester loads a project file saved before the build direction existed

- [ ] **DIR-10** — Then **Bow → Stern** is highlighted and the editor opens at layer 1

## Given layer 5 is in edit mode with painted cells and layer 4 is saved (Bow → Stern)

### When the tester clicks Copy previous

- [ ] **DIR-11** — Then a confirmation asks "Replace the editor content with layer 4?"; Cancel keeps the painted cells
