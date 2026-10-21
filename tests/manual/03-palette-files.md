# Feature: Palette save / load

**ID prefix:** `PFL` · **Area:** **Save palette** / **Load palette** buttons under the palette

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project named "Palette Test" is started (**New project** → OK, then rename)

## Given the palette contains 3 blocks in slots 01, 02 and 04

### When the tester clicks Save palette

- [ ] **PFL-01** — Then a file named `Palette_Test_palette.json` is downloaded
- [ ] **PFL-02** — Then the file lists the 3 blocks at positions 1, 2 and 4, with `null` for the empty slots in between

## Given the palette is empty

### When the tester clicks Save palette

- [ ] **PFL-03** — Then the message "The palette is empty — nothing to save." appears and no file is downloaded

## Given no layer contains painted blocks

### When the tester loads examples/basic-colors_palette.json with Load palette

- [ ] **PFL-04** — Then the palette is replaced without a confirmation and shows Red, Orange, Yellow, Green, Blue, Purple in slots `01`–`06`
- [ ] **PFL-05** — Then the message "Palette loaded: 6 blocks." appears

### When the tester loads a full project JSON file with Load palette

- [ ] **PFL-06** — Then only the palette of that project is loaded; layers, name and length of the current project stay unchanged

### When the tester selects a file that is not valid JSON (e.g. a renamed .txt)

- [ ] **PFL-07** — Then the message "Load error: not a valid JSON file." appears and the palette is unchanged

## Given layers use blocks in slots 01 and 02 and the file to load has different blocks there

### When the tester clicks Load palette and selects the file

- [ ] **PFL-08** — Then a confirmation lists the affected slots ("01, 02") and warns that painted cells keep their slot numbers

### When the tester cancels the confirmation

- [ ] **PFL-09** — Then the current palette and all painted colors stay unchanged

### When the tester accepts the confirmation

- [ ] **PFL-10** — Then the palette is replaced and the painted cells now show the colors of the new blocks in slots `01` and `02`
