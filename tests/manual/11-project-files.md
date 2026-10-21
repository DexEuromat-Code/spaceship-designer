# Feature: Project save / load

**ID prefix:** `PRJ` · **Area:** title bar — project name, **Save to JSON**, **Load JSON**, **New project**; automatic saving

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a project named "Test Ship v1.2" is prepared: length 50, direction Stern → Bow, a palette with 3 blocks and 3 saved layers

## Given the prepared project is open

### When the tester clicks Save to JSON

- [ ] **PRJ-01** — Then a file named `Test_Ship_v1_2.json` is downloaded (dots and spaces replaced with `_`)
- [ ] **PRJ-02** — Then the file contains the name, `"length": 50`, `"direction": "stern"`, the palette and the 3 layers

### When the tester clicks New project and accepts the confirmation

- [ ] **PRJ-03** — Then the project is cleared: name "New ship", length 25, direction Bow → Stern, empty palette and layers

### When the tester clicks New project and cancels the confirmation

- [ ] **PRJ-04** — Then the project stays unchanged

## Given a new project is open and the file Test_Ship_v1_2.json exists

### When the tester loads the file with Load JSON

- [ ] **PRJ-05** — Then the name, length, direction, palette and all 3 layers are restored exactly as saved
- [ ] **PRJ-06** — Then the message "Project "Test Ship v1.2" loaded." appears

### When the tester loads a JSON file with "length": 30

- [ ] **PRJ-07** — Then the message "Load error: Invalid ship length." appears and the current project is unchanged

## Given the prepared project is open and all layers are saved

### When the tester closes the browser tab and opens index.html again

- [ ] **PRJ-08** — Then the project is restored automatically with the same name, palette, layers and settings

## Given a project file saved by an earlier version of the app (palette of 10 slots, no "direction")

### When the tester loads it with Load JSON

- [ ] **PRJ-09** — Then the project loads without errors with direction Bow → Stern
