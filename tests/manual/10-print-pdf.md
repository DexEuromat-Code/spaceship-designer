# Feature: Print to PDF

**ID prefix:** `PRN` · **Area:** **Print to PDF** button and *Skip empty levels* option (under the top view)

## Background

- **Given** `index.html` is opened from disk in a desktop browser
- **And** `test-data/test-ship-alpha.json` is loaded with **Load JSON** (blocks on levels 1–6, layers 1–15, see [test data](README.md#test-data))

## Given Skip empty levels is ticked

### When the tester clicks Print to PDF

- [ ] **PRN-01** — Then the browser print dialog opens and its preview contains only the top-view pages (no app interface)
- [ ] **PRN-02** — Then there are 6 pages, ordered Level 1, 2, 3, 4, 5, 6 (lowest to highest)
- [ ] **PRN-03** — Then each page header shows "Test Ship Alpha", "Top view — Level n / 33" and "Page x of 6"
- [ ] **PRN-04** — Then each grid shows column numbers (1–33) on top and layer numbers on the left, with the bow at the top and blocks only in layers 1–15, columns 13–21
- [ ] **PRN-05** — Then each legend lists exactly the blocks of that level plus "Block on another level": L1 #06 Heavy armor · L2 #15 BATTERY · L3 #01 H2 Tank, #05 O2 Tank · L4 #03 Conveyors · L5 #10 ION Thruster · L6 #07 Light Armor

### When the tester chooses Save as PDF and saves the file

- [ ] **PRN-06** — Then the PDF opens with 6 A4 pages; levels 1 and 6 show a solid 9 × 15 rectangle and levels 2–5 show the single-block and cluster patterns in their colors

## Given Skip empty levels is NOT ticked

### When the tester clicks Print to PDF

- [ ] **PRN-07** — Then the print preview has 33 pages, from Level 1 to Level 33; pages for levels 7–33 show only the light-gray silhouette

## Given a new project with no saved blocks

### When the tester clicks Print to PDF

- [ ] **PRN-08** — Then the message "Nothing to print — no saved blocks on any level." appears and no print dialog opens

## Given test-ship-beta.json is loaded and layer 1 is in edit mode with an extra block painted on level 10

### When the tester clicks Print to PDF

- [ ] **PRN-09** — Then a note says unsaved changes are not printed and the preview has 6 pages (no page for level 10)

## Given test-ship-beta.json is loaded and the ship length is changed to 125

### When the tester clicks Print to PDF

- [ ] **PRN-10** — Then each page shows the whole grid (layers 1–125) on a single A4 page without cutting it off, with the tapered Beta hull in layers 1–15
