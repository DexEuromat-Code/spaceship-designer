# Feature: Block creation

**ID prefix:** `BLK` · **Area:** *Create block* panel (left column)

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started (**New project** → OK)

## Given the block form is empty

### When the tester looks at the form

- [ ] **BLK-01** — Then the counter under *Block name* shows `0/25`
- [ ] **BLK-02** — Then the preview next to the color square shows the current color, `—` as the name and the HEX code

### When the tester types "Hull" in Block name and picks a red color

- [ ] **BLK-03** — Then the preview updates immediately with the name "Hull", a red swatch and the matching HEX code

### When the tester tries to type a name longer than 25 characters

- [ ] **BLK-04** — Then the field stops accepting characters at 25 and the counter shows `25/25` in orange

### When the tester clicks Save with an empty name

- [ ] **BLK-05** — Then the message "Enter a block name." appears and no block is added to the palette

## Given the name "Heavy Armor" and a gray color are entered

### When the tester clicks Save

- [ ] **BLK-06** — Then the block appears in slot `01` with the name "Heavy Armor" and the gray swatch
- [ ] **BLK-07** — Then the form is cleared and slot `01` is selected (orange frame)
- [ ] **BLK-08** — Then the message "Block "Heavy Armor" added (slot 01, page 1)." appears

## Given a saved block is selected and already painted on a saved layer

### When the tester clicks Edit

- [ ] **BLK-09** — Then the block's name and color are loaded into the form, the slot shows `✎` and the button reads **Cancel edit**

### When the tester clicks Edit, changes the color to blue and clicks Save

- [ ] **BLK-10** — Then the block in the same slot turns blue and every painted cell using it turns blue in the editor and the top view

### When the tester clicks Edit and then Cancel edit

- [ ] **BLK-11** — Then the form is cleared, the `✎` mark disappears and the block is unchanged

## Given an empty palette slot is selected

### When the tester clicks Edit

- [ ] **BLK-12** — Then the message "Select a saved block in the palette to edit it." appears and the form stays empty
