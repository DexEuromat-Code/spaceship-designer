# Spaceship Designer — for Space Engineers

A lightweight 2D planner for **Space Engineers** ships. Design your ship slice by slice
(layers) from bow to stern on a 33 × 33 grid, check the shape in a top view, and print
every level as a PDF build sheet to follow in-game.

No installation, no account, no internet connection — it is a single HTML page that runs
in your browser.

## Features

- **Layer editor** — 33 × 33 cross-section of the ship, viewed from bow to stern, with
  **Edit / Save / Delete** per layer and protection against unsaved changes.
- **Top view** — any height level of the whole ship seen from above, from the top level (33)
  down to the lowest (1); click a row to open that layer.
- **Custom blocks** — name (up to 25 characters) and color with live preview.
- **Block palette & library** — 10 visible slots, unlimited pages (up to 990 blocks), keyboard
  shortcuts **1–0**; save / load palettes as JSON to reuse them between ships.
- **Ship length** — 25, 50, 75, 100 or 125 layers.
- **Drawing tools** — brush, eraser (also right mouse button), left–right **symmetry**,
  shadow of the previous layer.
- **Build direction** — work from the bow or from the stern; **Copy previous** follows the direction.
- **Copy from layer…** — copy any saved layer; layer numbers appear in the top view to help you pick.
- **Layer notes** — up to 256 characters per layer, e.g. the swing range of a rotor or hinge.
- **Print to PDF** — one A4 page per level, lowest to highest, with coordinates and a block legend.
- **Save / load projects** as JSON, plus automatic saving in the browser.
- **User guide** in English, Polish and Spanish (button **? Help** in the app).

## Getting started

1. Download `spaceship-designer-vX.Y.Z.zip` from the
   [Releases](../../releases) page and extract it anywhere.
2. Open **`index.html`** in a desktop browser (Chrome, Edge or Firefox — latest version).
3. Click **? Help** in the title bar for the full user guide.

Quick workflow:

1. Name the project, pick the ship length and the build direction.
2. Create blocks in **Create block** — or click **Load palette** and choose `Standard_palette.json`
   (16 common Space Engineers block types) or `examples/basic-colors_palette.json`.
3. In the layer editor click **Edit**, select a block and paint; click **Save**.
4. Move to the next layer (**▶** or **◀**), use **Copy previous** to repeat a hull section.
5. Check the result in the top view, then **Save to JSON** and **Print to PDF**.

## Design limitations

Please keep in mind that:

1. Designs make no distinction between large grid and small grid.
2. Blocks are always full-size — there are no half blocks or sloped (angled) blocks.
3. Moving blocks such as pistons are best designed in one of the two extreme positions:
   2 blocks (retracted) or 6 blocks (extended).
4. Blocks cannot be placed at an arbitrary angle — only in the vertical or horizontal plane.
   Where needed, describe the angle in the **Layer notes** of the layer containing the rotor or hinge.

## Files in the release

| File | Purpose |
|---|---|
| `index.html` | The application |
| `help.html`, `help_pl.html`, `help_es.html` | User guide — English, Polish, Spanish |
| `help.css` | Styles of the user guide |
| `Standard_palette.json` | Palette with 16 common Space Engineers block types |
| `examples/basic-colors_palette.json` | Palette with 6 basic colors |
| `README.md` | This file |
| `LICENSE` | MIT License |

Keep all files in the same folder structure — the guide pages need `help.css`, and the
**? Help** / **Back to app** links point to files next to each other.

## Your data

- Projects are saved **only on your computer**: as JSON files you download, and automatically
  in the browser's local storage. Nothing is sent anywhere.
- Clearing the browser's site data removes the automatic copy — keep important ships as JSON files.
- The automatic copy is tied to the browser and to the location of `index.html`; moving the
  folder or switching browsers starts with an empty project (load your JSON file again).

## File formats

**Project** (`Save to JSON`):

```jsonc
{
  "app": "se-ship-designer",
  "version": 2,
  "name": "My ship",
  "length": 25,
  "direction": "bow",
  "palette": [ { "name": "Heavy Armor", "color": "#808080" }, null /* … */ ],
  "layers": [
    { "layer": 1, "notes": "Rotor: ±45°", "rows": [ [-1, -1, 0, 0 /* … 33 cells */] /* … 33 rows */ ] }
  ]
}
```

- `length` — 25, 50, 75, 100 or 125; `direction` — `"bow"` or `"stern"`.
- Each cell holds a palette slot index (`0` = slot 01) or `-1` for an empty cell.
  Layer 1 is the bow; row 0 is the top level (33).
- `notes` is optional.

**Palette** (`Save palette`): `{ "app": "se-ship-designer-palette", "version": 1, "palette": [ … ] }`.
**Load palette** also accepts a project file and takes its palette.

## Browser support

Built for current desktop versions of Chrome, Edge and Firefox. Any modern browser with
`<canvas>` and `<dialog>` support should work. The app is designed for mouse and keyboard;
touch devices are not a target.

## Development

The whole app is plain HTML, CSS and JavaScript in `index.html` — no build step and no
dependencies. Edit the file and reload the page.

The repository also contains `tests/manual/` (not included in the release package):

- BDD-style manual test scenarios (`01-…md` – `13-…md`) with a results spreadsheet,
- test ships for the PDF tests (`tests/manual/test-data/`),
- Python scripts that regenerate the spreadsheet and the test ships (require `openpyxl`).

## License

Released under the [MIT License](LICENSE) — you may use, copy, modify and distribute it,
also commercially, as long as the copyright notice and the license text are kept.

## Disclaimer

Spaceship Designer is an unofficial fan-made tool. It is not affiliated with or endorsed by
Keen Software House. *Space Engineers* is a trademark of Keen Software House.
