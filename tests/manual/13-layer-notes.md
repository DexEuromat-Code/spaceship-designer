# Feature: Layer notes

**ID prefix:** `NTS` · **Area:** *Layer notes* field under the layer editor grid

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** a new project is started and `examples/basic-colors_palette.json` is loaded with **Load palette**

## Given layer 1 is opened and NOT in edit mode

### When the tester looks at the field under the grid

- [ ] **NTS-01** — Then a field labelled "Layer notes" with the placeholder "e.g. rotor / hinge swing range" and the counter `0/256` is shown

### When the tester clicks into the Layer notes field and tries to type

- [ ] **NTS-02** — Then no text can be entered and the message "Click "Edit" to edit the notes of this layer." appears

## Given layer 1 is in edit mode

### When the tester types "Rotor R1: swing -45° to +45°" in Layer notes

- [ ] **NTS-03** — Then the text appears, the counter shows `28/256` and the status changes to "Editing • unsaved"

### When the tester tries to type or paste more than 256 characters

- [ ] **NTS-04** — Then the field stops at 256 characters and the counter shows `256/256` in orange

### When the tester types a note (without painting blocks) and clicks Save

- [ ] **NTS-05** — Then the status is "Saved", the field becomes read-only and still shows the note

## Given layer 1 has the saved note "Rotor R1: swing -45° to +45°"

### When the tester goes to layer 2 and back to layer 1

- [ ] **NTS-06** — Then layer 2 shows an empty notes field and layer 1 shows the saved note again

### When the tester clicks Edit, changes the note to "Hinge H1: 0° to 90°" and clicks Save

- [ ] **NTS-07** — Then layer 1 shows the updated note "Hinge H1: 0° to 90°"

### When the tester clicks Edit, changes the note and clicks ▶ and accepts discarding the changes

- [ ] **NTS-08** — Then returning to layer 1 shows the original note (the change was not saved)

### When the tester clicks Save to JSON and opens the downloaded file

- [ ] **NTS-09** — Then the entry for layer 1 contains `"notes": "Rotor R1: swing -45° to +45°"`

### When the tester starts a new project and loads the saved file with Load JSON

- [ ] **NTS-10** — Then layer 1 shows the note "Rotor R1: swing -45° to +45°"

### When the tester clicks Delete and accepts the confirmation

- [ ] **NTS-11** — Then the confirmation mentions "content and notes" and after accepting the notes field of layer 1 is empty

## Given layer 1 has blocks and a saved note, and layer 2 is in edit mode with an empty note (Bow → Stern)

### When the tester clicks Copy previous

- [ ] **NTS-12** — Then the blocks of layer 1 are copied but the notes field of layer 2 stays empty
