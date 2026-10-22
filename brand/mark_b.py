#!/usr/bin/env python3
"""Generate the OpenDAP mark, option B: two identical triangular pieces, the O pointing left and the
D pointing right, offset diagonally. Built on the same 1:1 grid, stroke and chamfer family as the
main mark (mark.py); see README.md for the construction table.

  mark_b.py OUT.svg [--unit PX] [--fg HEX] [--bg HEX|none] [--grid]
"""
import argparse, importlib.util, os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("mark", os.path.join(_here, "mark.py"))
mark = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(mark)

STROKE, CHAMFER = mark.STROKE, mark.CHAMFER    # 28 u, 8 u: the main mark's stroke and counter face
CHAMFER_OUTER, R = mark.CHAMFER_OUTER, mark.R_OUTER   # 16 u, 2 u
SIDE = 8 * STROKE // 7                         # sloped stroke, measured vertically: 32 u
GAP = STROKE // 2                              # between the pieces, and each piece's offset: 14 u

# The D piece (stem on x = 0, apex to the right). The sides run 4 u down per 7 u across: the main
# mark's 7:4 side turned 90°.
STEM, DEPTH = 192, 168                         # STEM / 2 * 7 / 4 = DEPTH
TRI = [(0, 0), (DEPTH, STEM // 2), (0, STEM)]
COUNTER = [(STROKE, SIDE + STROKE * 4 // 7), (DEPTH - 2 * STROKE, STEM // 2), (STROKE, STEM - SIDE - STROKE * 4 // 7)]
APEX_IN = 14                                   # a 16 u face on the apex sits 14 u in from the tip


def piece():
    """Outline and counter of the D piece: one symmetric chamfer per corner, 16 u outside and 8 u
    in the counter, each face perpendicular to its corner's bisector."""
    return mark.chamfer(TRI, CHAMFER_OUTER), mark.chamfer(COUNTER, CHAMFER)


W, H = 2 * (DEPTH - APEX_IN) + GAP, STEM + 2 * GAP     # 322 u x 220 u


def placed():
    outer, counter = piece()
    d = lambda pts: [(x + DEPTH + GAP - APEX_IN, y) for x, y in pts]          # D: right, raised
    o = lambda pts: [(DEPTH - APEX_IN - x, STEM - y + 2 * GAP) for x, y in pts]  # O: the D turned 180°, lowered
    return [(o(outer), o(counter)), (d(outer), d(counter))], (o, d)


def svg(u, fg, bg, grid):
    pad = 21 if grid else 4
    vw, vh = (W + 2 * pad) * u, (H + 2 * pad) * u
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad * u} {-pad * u} {vw} {vh}">',
           '<title>OpenDAP</title>']
    if bg != "none":
        out.append(f'<rect x="{-pad * u}" y="{-pad * u}" width="{vw}" height="{vh}" fill="{bg}"/>')
    if grid:
        for step, colour, width in ((1, "#22272C", 0.04), (7, "#3A4148", 0.12)):
            g = [f'<line x1="{x * u}" y1="{-pad * u}" x2="{x * u}" y2="{(H + pad) * u}"/>' for x in range(0, W + 1, step)]
            g += [f'<line x1="{-pad * u}" y1="{y * u}" x2="{(W + pad) * u}" y2="{y * u}"/>' for y in range(0, H + 1, step)]
            out.append(f'<g stroke="{colour}" stroke-width="{u * width}">' + "".join(g) + '</g>')
    shapes, frames = placed()
    d = " ".join(mark.rounded_path(o, R, u) + " " + mark.rounded_path(c, R, u) for o, c in shapes)
    out.append(f'<path d="{d}" fill="{fg}" fill-rule="evenodd"{" opacity=\"0.85\"" if grid else ""}/>')
    if grid:
        # The unchamfered triangles, dashed; a 4:7 reference triangle at the D's top corner.
        pts = lambda f: " ".join(f"{x * u},{y * u}" for x, y in f)
        polys = "".join(f'<polygon points="{pts(f(p))}"/>' for f in frames for p in (TRI, COUNTER))
        out.append(f'<g fill="none" stroke="#FF6A2A" stroke-width="{u * 0.12}" stroke-dasharray="{u * 0.5},{u * 0.3}">{polys}</g>')
        x0 = DEPTH + GAP - APEX_IN
        out.append(f'<g fill="none" stroke="#69BFFF" stroke-width="{u * 0.12}">'
                   f'<polygon points="{pts([(x0, 0), (x0 + 28, 16), (x0, 16)])}"/></g>')
    out.append('</svg>')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--unit", type=float, default=10, help="pixels per grid unit")
    ap.add_argument("--fg", default="#F5F6F4")
    ap.add_argument("--bg", default="none")
    ap.add_argument("--grid", action="store_true", help="draw the construction grid")
    a = ap.parse_args()
    open(a.out, "w").write(svg(a.unit, a.fg, a.bg, a.grid))
