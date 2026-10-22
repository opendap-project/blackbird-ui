#!/usr/bin/env python3
"""Generate every OpenDAP brand SVG: the mark, the wordmark and the vertical lockup, in each colour.

The wordmark is "OpenDAP" in IBM Plex Sans SemiBold (SIL OFL 1.1), shaped with HarfBuzz (kerning on)
and converted to outlines, so no font is needed to display it. The font is not stored here: pass the
OTF from https://github.com/IBM/plex (ibm-plex-sans, fonts/complete/otf).

Every output is flat (see mark.py): one filled <path>, absolute coordinates, cubic Béziers only, no
transforms, groups, strokes, text or styles, and a viewBox fitted to the ink with its origin at 0,0.

  logo.py --font IBMPlexSans-SemiBold.otf [--out DIR]

Requires fontTools and uharfbuzz.
"""
import argparse, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

import mark

S = mark.STROKE                                # every lockup measure is a multiple of the stroke
LOCKUPS = {
    # name: (cap height, gap between mark and wordmark). For horizontal spaces the wordmark stands alone.
    "vertical": (5 * S / 2, 3 * S / 2),        # 70 u caps, 42 u gap, wordmark centred under the mark
}
WORDMARK_CAP = 5 * S                           # the standalone wordmark's scale (it is scaled as a whole)
COLOURS = {"light": "#F5F6F4", "dark": "#111315", "accent": "#FF6A2A", "current": "currentColor"}
NUM = lambda v: f"{round(v, 3):g}"


def wordmark(font_path, cap_u, x0, baseline):
    """Path data and ink bounds of "OpenDAP" with its cap height at cap_u, starting at x0 (the
    left edge of the O's ink) on the given baseline."""
    face = hb.Face(hb.Blob.from_file_path(font_path)); font = hb.Font(face)
    buf = hb.Buffer(); buf.add_str("OpenDAP"); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    tt = TTFont(font_path); glyphs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    s = cap_u / tt["OS/2"].sCapHeight
    placed, x = [], 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        placed.append((order[info.codepoint], x + pos.x_offset, pos.y_offset)); x += pos.x_advance
    bp = BoundsPen(glyphs)
    for g, gx, gy in placed:
        glyphs[g].draw(TransformPen(bp, (s, 0, 0, -s, gx * s, -gy * s)))
    left = bp.bounds[0]
    pen, bp = SVGPathPen(glyphs, ntos=NUM), BoundsPen(glyphs)
    for g, gx, gy in placed:
        t = (s, 0, 0, -s, gx * s + x0 - left, baseline - gy * s)
        glyphs[g].draw(TransformPen(pen, t)); glyphs[g].draw(TransformPen(bp, t))
    return pen.getCommands(), bp.bounds


def layouts(font):
    """Each output as a function of an offset (ox, oy) -> (path data, ink bounds); the bounds at
    offset 0 tell the offset that puts the ink at 0,0."""
    cs = mark.contours()
    mx0, my0, mx1, my1 = mark.bounds(cs)
    m = lambda ox, oy: mark.path_data(cs, -ox, -oy)
    mb = lambda ox, oy: (mx0 + ox, my0 + oy, mx1 + ox, my1 + oy)
    cap_v, gap_v = LOCKUPS["vertical"]
    probe = wordmark(font, cap_v, 0, 0)[1]
    width_v = probe[2] - probe[0]
    words = {
        "wordmark": lambda ox, oy: wordmark(font, WORDMARK_CAP, ox, WORDMARK_CAP + oy),
        "vertical": lambda ox, oy: wordmark(font, cap_v, (mx0 + mx1) / 2 - width_v / 2 + ox, my1 + gap_v + cap_v + oy),
    }
    out = {"mark": lambda ox, oy: (m(ox, oy), mb(ox, oy)), "wordmark": words["wordmark"]}
    for name in ("vertical",):
        def f(ox, oy, w=words[name]):
            wd, wb = w(ox, oy); b = mb(ox, oy)
            return m(ox, oy) + wd, (min(b[0], wb[0]), min(b[1], wb[1]), max(b[2], wb[2]), max(b[3], wb[3]))
        out[name] = f
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--font", required=True, help="IBMPlexSans-SemiBold.otf")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for name, build in layouts(a.font).items():
        x0, y0, x1, y1 = build(0, 0)[1]
        d, _ = build(-x0, -y0)
        for colour, fill in COLOURS.items():
            if colour == "accent" and name != "mark":
                continue                       # the orange is for the mark alone
            with open(os.path.join(a.out, f"opendap-{name}-{colour}.svg"), "w") as f:
                f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {NUM(x1 - x0)} {NUM(y1 - y0)}" role="img">'
                        f'<title>OpenDAP</title><path fill="{fill}" d="{d}"/></svg>\n')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "opendap-mark-construction.svg"), "w") as f:
        f.write(mark.construction())


if __name__ == "__main__":
    main()
