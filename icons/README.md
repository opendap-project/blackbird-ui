# OpenDAP Icons

The icon library of the Engineered Matter design system (DS-021). Every icon is drawn once in [`icons.py`](icons.py), which writes the SVGs, the catalogue and the [preview](../renders/web/icons.html).

## Grammar

- **Grids.**
  - 24 px for everything on the 166 ppi panel: header actions, list lines, controls.
  - 16 px for the status bar.
  - On the 24 grid the live area is 2–22.
- **Strokes.**
  - 2 px, square caps, miter joins with a miter limit of 2, so right angles stay sharp and acute ones bevel.
  - Horizontal and vertical strokes are centred on whole pixels, so they cover whole pixels and stay crisp.
- **Outline by default, filled for learned, stateful controls:** transport, Liked, and the status-bar glyphs, which are filled where the shape allows, as phones do.
- **Character.** The grammar of IBM Carbon (drawn for IBM Plex, the design system's typeface), redrawn natively on a 24 px grid. Carbon's 32 px masters would land on 1.5 px strokes at 24. No Carbon artwork is copied. If a Carbon glyph is ever imported, it keeps its Apache-2.0 licence in its own file under REUSE.

## Names

Names are **semantic**: what the icon means (`signal-path`, `output-balanced`, `waiting`), not what it shows. Code, templates and capabilities refer to icons only by name (`icon: "like"`), never by file. That is what makes replacement possible.

The catalogue [`icons.json`](icons.json) lists each icon's name, grid, category, style and default accessible label. The label is a fallback: the control's own accessible name always says what it does.

## Customising

- **Themes** (SYS-030) may redraw any catalogued icon. A theme ships `icons/<grid>/<name>.svg` for the names it changes; every other name falls back to these. Replacements are checked with `python3 icons.py --check <theme>/icons`:
  - known names only;
  - the right canvas;
  - `currentColor` only, so the theme's tokens colour them.
- **Derivatives** (OS-028) replace the set the same way, in their image.
- **Capabilities** use catalogue names only (template tier A, system ADR 0002). A glyph the catalogue lacks is contributed here first (system ADR 0004), so every surface and theme gets it.
- **New icons** are added to `icons.py`, regenerated, and checked in the preview at 16, 20, 24, 32 and 48 px before they are merged.

## Licence

MPL-2.0, like the rest of the design system's assets (REUSE).
