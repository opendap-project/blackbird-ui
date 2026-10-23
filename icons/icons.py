#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 The OpenDAP Project
# SPDX-License-Identifier: MPL-2.0
"""OpenDAP Icons: the source of every icon of the Engineered Matter design system.

Each icon is drawn here once, on its grid, and this script writes:
  svg/24/<name>.svg  outline icons on a 24 px grid (2 px stroke, square caps, miter joins)
  svg/16/<name>.svg  status-bar glyphs on a 16 px grid (filled shapes, 2 px strokes)
  icons.json         the catalogue: name, grid, category, default accessible label, variants

Rules (design system §15.3, icons README):
  * live area 2..22 on the 24 grid (2 px padding); horizontal and vertical strokes are centred on
    whole-pixel coordinates, so a 2 px stroke covers whole pixels;
  * outline by default; "-filled" variants for learned, stateful controls;
  * names are semantic (what it means, not what it shows), so a theme can replace the drawing.

Run: python3 icons.py                 write svg/, icons.json and the preview (no dependencies)
     python3 icons.py --check DIR     validate a theme's replacement icons in DIR/<grid>/<name>.svg
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
HEADER = "<!-- SPDX-FileCopyrightText: 2026 The OpenDAP Project -->\n<!-- SPDX-License-Identifier: MPL-2.0 -->\n"

# (name, category, label, body). Outline bodies use the stroke style; filled bodies set fill.
S = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" stroke-linejoin="miter" stroke-miterlimit="2"'
F = 'fill="currentColor"'

ICONS_24 = [
    # transport (filled: learned, stateful)
    ("play", "transport", "Play", f'<path {F} d="M7 4 20 12 7 20Z"/>'),
    ("pause", "transport", "Pause", f'<path {F} d="M6 4h4v16H6zM14 4h4v16h-4z"/>'),
    ("previous", "transport", "Previous", f'<path {F} d="M4 4h2v16H4zM20 4v16L8 12z"/>'),
    ("next", "transport", "Next", f'<path {F} d="M18 4h2v16h-2zM4 4v16l12-8z"/>'),
    ("stop", "transport", "Stop", f'<path {F} d="M5 5h14v14H5z"/>'),
    ("shuffle", "transport", "Shuffle", f'<path {S} d="M3 7h4l10 10h3M3 17h4l3-3M14 10l3-3h3M18 4l3 3-3 3M18 14l3 3-3 3"/>'),
    ("repeat", "transport", "Repeat", f'<path {S} d="M4 11V6h15M17 3l3 3-3 3M20 13v5H5M7 21l-3-3 3-3"/>'),
    ("repeat-one", "transport", "Repeat one", f'<path {S} d="M4 11V6h15M17 3l3 3-3 3M20 13v5H5M7 21l-3-3 3-3M11 10l1-1v6"/>'),
    ("back-15", "transport", "Back 15 seconds", f'<path {S} d="M4 12a8 8 0 1 0 2-5M4 4v5h5"/>'),
    ("forward-30", "transport", "Forward 30 seconds", f'<path {S} d="M20 12a8 8 0 1 1-2-5M20 4v5h-5"/>'),
    ("eject", "transport", "Eject", f'<path {F} d="M12 4l8 9H4zM4 16h16v3H4z"/>'),
    # library
    ("album", "library", "Album", f'<g {S}><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2"/></g>'),
    ("artist", "library", "Artist", f'<g {S}><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></g>'),
    ("song", "library", "Song", f'<g {S}><path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/></g>'),
    ("playlist", "library", "Playlist", f'<g {S}><path d="M3 6h12M3 11h12M3 16h7M19 5v11"/><circle cx="17" cy="17" r="2"/></g>'),
    ("queue", "library", "Queue", f'<path {S} d="M3 6h18M3 12h11M3 18h11"/><path {F} d="M17 14l5 3-5 3z"/>'),
    ("folder", "library", "Folder", f'<path {S} d="M3 7v12h18V9h-9l-2-2z"/>'),
    ("podcast", "library", "Podcast", f'<g {S}><circle cx="12" cy="10" r="2"/><path d="M8 14a5 5 0 1 1 8 0M5 17a9 9 0 1 1 14 0M12 14v7"/></g>'),
    ("audiobook", "library", "Audiobook", f'<path {S} d="M4 5h6a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H4zM20 5h-6a2 2 0 0 0-2 2v13a2 2 0 0 1 2-2h6z"/>'),
    ("recording", "library", "Recording", f'<g {S}><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></g>'),
    ("lyrics", "library", "Lyrics", f'<path {S} d="M4 6h16M4 11h12M4 16h8"/><path {F} d="M16 15h4v3l-2 3h-2l1-3h-1z"/>'),
    ("like", "library", "Like", f'<path {S} d="M12 20s-8-5-8-11a4 4 0 0 1 8-1 4 4 0 0 1 8 1c0 6-8 11-8 11z"/>'),
    ("like-filled", "library", "Liked", f'<path {F} d="M12 21s-9-5.4-9-12a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 6.6-9 12-9 12z"/>'),
    # sound
    ("volume", "sound", "Volume", f'<path {S} d="M3 9h4l5-4v14l-5-4H3zM15 9a4 4 0 0 1 0 6M17 6a8 8 0 0 1 0 12"/>'),
    ("volume-muted", "sound", "Muted", f'<path {S} d="M3 9h4l5-4v14l-5-4H3zM16 9l5 6M21 9l-5 6"/>'),
    ("headphones", "sound", "Headphones", f'<g {S}><path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="4" height="7"/><rect x="17" y="14" width="4" height="7"/></g>'),
    ("output-jack", "sound", "Headphone output", f'<g {S}><rect x="9" y="3" width="6" height="11"/><path d="M9 8h6M12 14v8"/></g>'),
    ("output-balanced", "sound", "Balanced output", f'<g {S}><rect x="9" y="3" width="6" height="11"/><path d="M9 7h6M9 10h6M12 14v8"/></g>'),
    ("speaker", "sound", "Speaker", f'<g {S}><rect x="6" y="3" width="12" height="18"/><circle cx="12" cy="14" r="3"/></g><path {F} d="M11 6h2v2h-2z"/>'),
    ("signal-path", "sound", "Signal path", f'<g {S}><circle cx="12" cy="4" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="20" r="2"/><path d="M12 6v4M12 14v4"/></g>'),
    ("dac", "sound", "DAC", f'<g {S}><rect x="6" y="6" width="12" height="12"/><path d="M9 3v3M12 3v3M15 3v3M9 18v3M12 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/></g>'),
    ("tone", "sound", "Tone", f'<path {S} d="M6 4v16M12 4v16M18 4v16"/><path {F} d="M4 13h4v3H4zM10 7h4v3h-4zM16 15h4v3h-4z"/>'),
    ("compare", "sound", "Compare", f'<path {S} d="M3 5h18v14H3zM12 5v14"/><path {F} d="M4 6h8v12H4z"/>'),
    ("hearing", "sound", "Hearing", f'<path {S} d="M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-6 0M10 10a2 2 0 0 1 4 0"/>'),
    ("profile", "sound", "Profile", f'<g {S}><path d="M3 12h18"/><circle cx="9" cy="12" r="3"/></g>'),
    # devices and connectivity
    ("devices", "device", "Play on", f'<g {S}><rect x="3" y="5" width="12" height="9"/><path d="M2 18h14"/><rect x="18" y="8" width="4" height="12"/></g>'),
    ("this-device", "device", "This T1", f'<g {S}><rect x="7" y="2" width="10" height="20"/><path d="M10 19h4"/></g>'),
    ("bluetooth", "device", "Bluetooth", f'<path {S} d="M6 7l11 9-5 5V3l5 5-11 9"/>'),
    ("wifi", "device", "Wi-Fi", f'<path {S} d="M2 9a14 14 0 0 1 20 0M5 13a9 9 0 0 1 14 0M8 16a5 5 0 0 1 8 0"/><path {F} d="M11 19h2v2h-2z"/>'),
    ("usb", "device", "USB", f'<path {S} d="M12 6v13M12 14l-4-3V9M12 16l4-3v-2"/><path {F} d="M12 2l3 4H9zM7 6h2v3H7z"/><circle {F} cx="16" cy="9" r="2"/><circle {F} cx="12" cy="20" r="2"/>'),
    ("pair", "device", "Pair", f'<path {S} d="M10 14l4-4M8 11l-3 3a3 3 0 0 0 4 4l3-3M16 13l3-3a3 3 0 0 0-4-4l-3 3"/>'),
    ("sync", "device", "Sync", f'<path {S} d="M20 12a8 8 0 0 0-14-5M4 4v5h5M4 12a8 8 0 0 0 14 5M20 20v-5h-5"/>'),
    ("hat", "device", "HAT", f'<g {S}><rect x="4" y="5" width="16" height="11"/><path d="M8 16v4M12 16v4M16 16v4"/></g>'),
    ("battery", "device", "Battery", f'<path {S} d="M3 7h15v10H3zM21 10v4"/><path {F} d="M5 9h7v6H5z"/>'),
    ("storage", "device", "Storage", f'<path {S} d="M8 3h9l3 3v15H4V7z"/><path {S} d="M9 3v3M12 3v3M15 3v3"/>'),
    ("power", "device", "Power", f'<path {S} d="M12 3v8M7 6a8 8 0 1 0 10 0"/>'),
    ("restart", "device", "Restart", f'<path {S} d="M4 12a8 8 0 1 0 2-5M4 3v5h5"/>'),
    ("lock", "device", "Lock", f'<path {S} d="M5 11h14v10H5zM8 11V8a4 4 0 0 1 8 0v3"/>'),
    ("brightness", "device", "Brightness", f'<g {S}><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1 1M18 18l1 1M19 5l-1 1M5 19l1-1"/></g>'),
    ("sleep", "device", "Sleep timer", f'<path {S} d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z"/>'),
    ("update", "device", "Software update", f'<path {S} d="M12 3v12M7 10l5 5 5-5M4 17v4h16v-4"/>'),
    # actions and states
    ("back", "action", "Back", f'<path {S} d="M15 5l-7 7 7 7"/>'),
    ("forward", "action", "Forward", f'<path {S} d="M9 5l7 7-7 7"/>'),
    ("down", "action", "Down", f'<path {S} d="M5 9l7 7 7-7"/>'),
    ("up", "action", "Up", f'<path {S} d="M5 15l7-7 7 7"/>'),
    ("search", "action", "Search", f'<g {S}><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></g>'),
    ("add", "action", "Add", f'<path {S} d="M12 4v16M4 12h16"/>'),
    ("close", "action", "Close", f'<path {S} d="M5 5l14 14M19 5L5 19"/>'),
    ("done", "action", "Done", f'<path {S} d="M4 13l5 5L20 7"/>'),
    ("more", "action", "More", f'<path {F} d="M3 10h4v4H3zM10 10h4v4h-4zM17 10h4v4h-4z"/>'),
    ("reorder", "action", "Reorder", f'<path {S} d="M5 9h14M5 15h14"/>'),
    ("delete", "action", "Delete", f'<path {S} d="M4 6h16M9 6V3h6v3M6 6l1 15h10l1-15"/>'),
    ("undo", "action", "Undo", f'<path {S} d="M9 14L4 9l5-5M4 9h10a6 6 0 0 1 0 12h-4"/>'),
    ("waiting", "state", "Waiting", f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M12 7v5l4 2"/></g>'),
    ("error", "state", "Error", f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/></g>'),
    ("warning", "state", "Warning", f'<path {S} d="M12 4l9 16H3zM12 10v4"/><path {F} d="M11 16h2v2h-2z"/>'),
    ("info", "state", "Information", f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M12 11v6"/></g><path {F} d="M11 7h2v2h-2z"/>'),
]

# 16 px status-bar glyphs: filled where the shape allows (Android's status icons), 2 px strokes otherwise.
S16 = S
ICONS_16 = [
    ("status-microsd", "status", "microSD card", f'<path {F} d="M5 1h7l3 3v11H2V4zM6 3v3h1V3zM8 3v3h1V3zM10 3v3h1V3z" fill-rule="evenodd"/>'),
    ("status-volume", "status", "Volume", f'<path {F} d="M1 6h3l4-3v10L4 10H1z"/><path {S16} d="M11 6a3 3 0 0 1 0 4"/>'),
    ("status-bluetooth", "status", "Bluetooth", f'<path {S16} d="M4 5l7 6-3 3V2l3 3-7 6"/>'),
    ("status-wifi", "status", "Wi-Fi", f'<path {F} d="M8 14L1 6a10 10 0 0 1 14 0z"/>'),
    ("status-battery", "status", "Battery", f'<path {F} d="M1 4h12v8H1zM14 6h1v4h-1z" fill-opacity=".35"/><path {F} d="M2 5h8v6H2z"/>'),
]


def svg(size, body):
    return f'{HEADER}<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">{body}</svg>\n'


def main():
    catalogue = []
    for size, icons in ((24, ICONS_24), (16, ICONS_16)):
        out = HERE / "svg" / str(size)
        out.mkdir(parents=True, exist_ok=True)
        for name, category, label, body in icons:
            (out / f"{name}.svg").write_text(svg(size, body))
            catalogue.append({"name": name, "grid": size, "category": category, "label": {"en": label},
                              "style": "filled" if body.count('fill="currentColor"') and 'stroke=' not in body else "outline"})
    names = [c["name"] for c in catalogue]
    assert len(names) == len(set(names)), "duplicate icon names"
    (HERE / "icons.json").write_text(json.dumps({"schema": "opendap.icons/v1", "icons": catalogue}, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(catalogue)} icons written")




def preview():
    """renders/web/icons.html: every icon at its real sizes, on the dark surface, with a pixel grid."""
    cells = []
    for size, icons in ((24, ICONS_24), (16, ICONS_16)):
        for name, category, label, body in icons:
            sizes = (16, 20, 24, 32, 48) if size == 24 else (16, 32, 48)
            imgs = "".join(
                f'<span class="s" style="width:{px}px;height:{px}px"><svg viewBox="0 0 {size} {size}" width="{px}" height="{px}">{body}</svg></span>'
                for px in sizes)
            grid = f'<span class="g"><svg viewBox="0 0 {size} {size}" width="{size*6}" height="{size*6}" shape-rendering="crispEdges">{body}</svg></span>'
            cells.append(f'<figure><div class="row">{grid}<div class="sz">{imgs}</div></div><figcaption><b>{name}</b> {label} · {category} · {size} px grid</figcaption></figure>')
    html = f"""<!DOCTYPE html>
<!-- SPDX-FileCopyrightText: 2026 The OpenDAP Project -->
<!-- SPDX-License-Identifier: MPL-2.0 -->
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>OpenDAP Icons</title>
<style>
:root{{--bg:#111315;--surface:#191C1F;--text:#F5F6F4;--muted:#939BA3;--grid:#2A2F34;}}
*{{box-sizing:border-box;margin:0}}
body{{background:#0B0C0E;color:var(--text);font:14px/20px system-ui,sans-serif;padding:32px 24px}}
h1{{font-size:24px;line-height:32px;font-weight:600}} p{{color:var(--muted);max-width:820px;margin-top:6px}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-top:24px}}
figure{{background:var(--surface);border-radius:12px;padding:12px}}
.row{{display:flex;gap:14px;align-items:center}}
.g{{display:block;background-color:var(--bg);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:6px 6px;outline:1px dashed #3A4148;color:var(--text)}}
.g svg{{display:block}}
.sz{{display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap}}
.s{{display:inline-grid;place-items:center;color:var(--text)}} .s svg{{display:block}}
figcaption{{margin-top:8px;font-size:12px;line-height:16px;color:var(--muted)}} figcaption b{{color:var(--text);font-weight:600}}
</style></head><body>
<h1>OpenDAP Icons</h1>
<p>Every icon of the Engineered Matter design system, drawn once in <code>icons/icons.py</code>: on its grid magnified six times over a pixel grid (the dashed box is the 24 px or 16 px canvas; the live area is 2–22), then at 16, 20, 24, 32 and 48 px. Outline icons use a 2 px stroke with square caps and miter joins; transport and stateful icons are filled. Generated file: do not edit by hand.</p>
<main>{''.join(cells)}</main></body></html>
"""
    out = HERE.parent / "renders" / "web" / "icons.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def check(theme_dir):
    """Validate replacement icons: known names, the right grid and canvas, and no hard-coded colours."""
    import re
    import sys
    known = {(24, n) for n, *_ in ICONS_24} | {(16, n) for n, *_ in ICONS_16}
    problems = 0
    for path in sorted(pathlib.Path(theme_dir).glob("*/*.svg")):
        grid, name = int(path.parent.name), path.stem
        text = path.read_text()
        errors = []
        if (grid, name) not in known:
            errors.append("unknown name or grid (replacements may only redraw catalogue icons)")
        if f'viewBox="0 0 {grid} {grid}"' not in text:
            errors.append(f"viewBox must be 0 0 {grid} {grid}")
        if re.search(r'(fill|stroke)="#', text):
            errors.append("use currentColor, never a fixed colour (the theme's tokens colour icons)")
        for e in errors:
            print(f"{path}: {e}", file=sys.stderr)
        problems += len(errors)
    print("ok" if not problems else f"{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        sys.exit(check(sys.argv[2]))
    main()
    preview()
