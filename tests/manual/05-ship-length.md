# Feature: Ship length

**ID prefix:** `LEN` · **Area:** *Ship length (layers)* selector (left column)

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started (**New project** → OK)
- **And** at least one block exists in the palette

## Given a new project

### When the tester looks at the ship length selector

- [ ] **LEN-01** — Then **25** is highlighted, the layer navigation shows "/ 25" and the top view has 25 rows

### When the tester clicks 125

- [ ] **LEN-02** — Then no confirmation appears, the navigation shows "/ 125" and the top view has 125 rows with a scrollbar

## Given the length is 50 and layer 40 contains saved blocks

### When the tester clicks 25

- [ ] **LEN-03** — Then a confirmation says shortening to 25 layers will delete the content and notes of 1 layer

### When the tester clicks 25 and cancels the confirmation

- [ ] **LEN-04** — Then the length stays 50 and layer 40 still contains its blocks

### When the tester opens layer 40, clicks 25 and accepts the confirmation

- [ ] **LEN-05** — Then the length becomes 25, layer 40 is deleted and the editor moves to layer 25

## Given the length is 50 and only layers 1–25 contain blocks

### When the tester clicks 25

- [ ] **LEN-06** — Then the length changes to 25 without a confirmation and all layers 1–25 are kept
