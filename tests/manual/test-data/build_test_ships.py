"""Generates the test ships used by the manual tests (mainly Print to PDF).

Usage:  python tests/manual/test-data/build_test_ships.py
Geometry (both ships): 15 layers long (layers 1-15 of a 25-layer project — 25 is the app's
minimum length), 6 levels high (levels 1-6), up to 9 blocks wide, centered on column 17.
  Level 1 and level 6: completely filled with one block type.
  Levels 2-5: alternating patterns of single blocks and clusters of 3 or 4 blocks.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PALETTE_FILE = HERE.parents[2] / "Standard_palette.json"
N = 33
CENTER = 16  # 0-based index of column 17

# Standard palette slot indices (0-based; slot 01 = index 0)
H2_TANK, CONVEYORS, O2_TANK, HEAVY, LIGHT, ION, DOOR, PISTONS, BATTERY = 0, 2, 4, 5, 6, 9, 11, 12, 14


def empty_layer():
    return [[-1] * N for _ in range(N)]


def row_of(level):            # level 1 = bottom row (index 32), level 33 = top row (index 0)
    return N - level


def columns(width):           # centered column indices for a given width
    half = width // 2
    return list(range(CENTER - half, CENTER + half + 1))


def build_alpha():
    """Constant 9-wide box. L1 Heavy armor, L6 Light Armor, L2-L5 alternating patterns."""
    layers = {}
    for n in range(1, 16):
        g, cols = empty_layer(), columns(9)
        for i, x in enumerate(cols):
            g[row_of(1)][x] = HEAVY                                        # level 1: full
            g[row_of(6)][x] = LIGHT                                        # level 6: full
            if (i + n) % 2 == 0:                                           # level 2: single blocks, checkerboard
                g[row_of(2)][x] = BATTERY
            if i % 4 != 3:                                                 # level 3: clusters of 3 across, 1 gap
                g[row_of(3)][x] = H2_TANK if (i // 4 + n) % 2 else O2_TANK
            if ((n - 1) // 2 + i // 2) % 2 == 0 and i < 8:                 # level 4: 2x2 clusters of 4
                g[row_of(4)][x] = CONVEYORS
            if (i + n) % 2 == 1:                                           # level 5: single blocks, inverse checkerboard
                g[row_of(5)][x] = ION
        layers[n] = g
    return layers


def build_beta():
    """Tapered hull: 5 wide at the bow, 7 in the middle, 9 at the stern.
    L1 Light Armor, L6 Heavy armor, L2-L5 alternating clusters of 4, singles and clusters of 3."""
    layers = {}
    for n in range(1, 16):
        g = empty_layer()
        width = 5 if n <= 3 else 7 if n <= 7 else 9
        cols = columns(width)
        for i, x in enumerate(cols):
            g[row_of(1)][x] = LIGHT                                        # level 1: full
            g[row_of(6)][x] = HEAVY                                        # level 6: full
            if (n - 1) % 5 < 4 and x % 2 == 0:                             # level 2: lines of 4 along the length
                g[row_of(2)][x] = O2_TANK
            if (i + n) % 3 == 0:                                           # level 3: single blocks, diagonal
                g[row_of(3)][x] = DOOR
            if (n - 1) % 4 < 2 and i % 3 != 2:                             # level 4: L-shaped clusters of 3
                if not ((n - 1) % 4 == 1 and i % 3 == 1):
                    g[row_of(4)][x] = PISTONS
            if (n - 1) % 2 == 0:                                           # level 5: clusters of 4 across + singles
                if i < 4:
                    g[row_of(5)][x] = BATTERY
                elif width == 9 and i >= 5:
                    g[row_of(5)][x] = H2_TANK
                elif width == 7 and i == 6:
                    g[row_of(5)][x] = H2_TANK
        layers[n] = g
    return layers


def project(name, direction, palette, layers):
    return {
        "app": "se-ship-designer", "version": 2, "name": name, "gridSize": N,
        "length": 25, "direction": direction,
        "orientation": "layer 1 = bow; row 0 = top; cell = palette index or -1",
        "palette": palette,
        "layers": [{"layer": n, "rows": layers[n]} for n in sorted(layers)],
    }


def dump(obj, path):
    text = json.dumps(obj, indent=2, ensure_ascii=False)
    # keep each 33-cell row on one line, like the app's own export
    import re
    text = re.sub(r"\[\s*(-?\d+(?:,\s*-?\d+)*)\s*\]", lambda m: "[" + re.sub(r"\s+", "", m.group(1)) + "]", text)
    path.write_text(text + "\n", encoding="utf-8")


def summary(layers, palette):
    for level in range(1, 7):
        used = sorted({v for g in layers.values() for v in g[row_of(level)] if v >= 0})
        count = sum(v >= 0 for g in layers.values() for v in g[row_of(level)])
        names = ", ".join(f"#{u + 1:02d} {palette[u]['name']}" for u in used)
        print(f"  level {level}: {count:3d} blocks — {names}")


def main():
    palette = json.loads(PALETTE_FILE.read_text(encoding="utf-8"))["palette"]
    ships = [
        ("Test Ship Alpha", "bow", build_alpha(), "test-ship-alpha.json"),
        ("Test Ship Beta", "stern", build_beta(), "test-ship-beta.json"),
    ]
    for name, direction, layers, fname in ships:
        dump(project(name, direction, palette, layers), HERE / fname)
        print(f"{fname}:")
        summary(layers, palette)


if __name__ == "__main__":
    main()
