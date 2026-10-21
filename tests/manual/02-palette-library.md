# Feature: Block palette & library

**ID prefix:** `PAL` · **Area:** *Block palette* panel (left column)

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started (**New project** → OK)

## Given the palette is empty

### When the tester looks at the palette

- [ ] **PAL-01** — Then 10 slots numbered `01`–`10` are shown, each marked "empty"
- [ ] **PAL-02** — Then the page controls are hidden and the counter reads "0 blocks in library"

### When the tester selects slot 05 and saves a new block

- [ ] **PAL-03** — Then the block is stored in slot `05` (the selected empty slot), not in slot `01`

## Given all 10 slots on page 1 contain blocks

### When the tester saves an 11th block

- [ ] **PAL-04** — Then the message "Visible slots are full — "…" saved to the library (page 2)." appears
- [ ] **PAL-05** — Then the palette shows page 2 with the new block in slot `11` and slots `12`–`20` empty
- [ ] **PAL-06** — Then the page controls appear under the palette showing "Page 2 / 2" and the counter reads "11 blocks in library"

### When the tester uses ⏮ ◀ ▶ ⏭

- [ ] **PAL-07** — Then the displayed page changes accordingly, and ⏮ ◀ are disabled on the first page while ▶ ⏭ are disabled on the last page

## Given page 1 of the palette is displayed and no text field has focus

### When the tester presses keys 1 to 9 and then 0

- [ ] **PAL-08** — Then keys 1–9 select slots `01`–`09` and key 0 selects slot `10`

### When the tester hovers the mouse over a saved slot

- [ ] **PAL-09** — Then a tooltip shows `#NN name (HEX) — key K`, e.g. "#03 Glass (#88CCFF) — key 3"

### When the tester types digits in the Block name field

- [ ] **PAL-10** — Then the digits go into the field and the selected palette slot does not change

## Given page 2 of the palette is displayed

### When the tester presses key 3

- [ ] **PAL-11** — Then slot `13` (the third slot of page 2) is selected
