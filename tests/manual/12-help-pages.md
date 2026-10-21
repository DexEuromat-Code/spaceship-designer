# Feature: User guide pages

**ID prefix:** `HLP` · **Area:** **? Help** button, `help.html`, `help_pl.html`, `help_es.html`

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** the current project contains at least one saved layer

## Given the app is open

### When the tester clicks ? Help in the title bar

- [ ] **HLP-01** — Then the English user guide opens in the same tab with the "EN" button highlighted

## Given the user guide is open

### When the tester clicks ← Back to app (in the top bar, under the contents, and at the bottom of the page)

- [ ] **HLP-02** — Then each button returns to the app and the project is intact

### When the tester clicks PL and then ES in the language switcher

- [ ] **HLP-03** — Then the Polish and the Spanish guide open, with "PL" / "ES" highlighted respectively and the back button translated

### When the tester clicks an entry in the contents list

- [ ] **HLP-04** — Then the page scrolls to that section and its heading is not hidden under the top bar

### When the tester clicks ↑ Back to top at the end of a section

- [ ] **HLP-05** — Then the page scrolls back to the top

### When the tester narrows the window below 900 px

- [ ] **HLP-06** — Then the contents list moves above the sections in a single column and there is no horizontal scrollbar

## Given each language version (EN, PL, ES) is opened in turn

### When the tester compares the pages

- [ ] **HLP-07** — Then all three have the same 13 sections numbered 1–13, the same styling (dark theme from help.css) and describe Build direction, Copy from layer… and Layer notes
- [ ] **HLP-08** — Then section 3 "Design limitations" (PL "Ograniczenia projektowe", ES "Limitaciones del diseño") comes right before "Creating blocks" and lists the 4 points: no large/small grid distinction, full-size blocks only, pistons in 2 or 6 blocks, angles described in the notes of the rotor / hinge layer

## Given the app or a guide page is open

### When the tester looks at the title bar

- [ ] **HLP-09** — Then the app name reads "SPACESHIP DESIGNER" with the subtitle "For Space Engineers", and the browser tab title starts with "Spaceship Designer"
