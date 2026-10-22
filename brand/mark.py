#!/usr/bin/env python3
"""Generate the OpenDAP mark (Draft), constructed on a 1:1 grid with industrial angles.

Construction (grid units, u):
- Angles: 0°, 90° and 60°. The sides rise 7 u per 4 u across (60.26°), the grid-exact
  approximation of the 60° set-square angle (within 0.3°).
- Strokes: horizontal edges and the vertical centre line 28 u. The 60° sides are 32 u wide
  measured horizontally (27.8 u perpendicular): optically equal, and on the grid.
- Height 91 u = 28 u + 35 u counter + 28 u (stroke 30.8 % of the height). The top edge is
  offset 52 u (91 x 4/7). Overall 164 u x 91 u.
- Counters: triangles (a horizontal stroke, a 60° side and the centre line, which meets the
  side's inner contour at the counter's tip), with all three corners chamfered; every cut face
  is 4 u long: two six-sided counters.
- Acute outer corners cut vertically at the side's grid point one stroke above the corner:
  each cut is 28 u long, one stroke, echoing the centre line.
- Outer corners: every corner of the outline chamfered with the same cut-face length as the
  counters (4 u).
- Rounding: only the outer chamfers, 2 u (half a cut face); the counters stay sharp.

  mark.py OUT.svg [--unit PX] [--fg HEX] [--bg HEX|none] [--grid]
"""
import argparse, math

STROKE, COUNTER, CHAMFER, R = 28, 35, 4, 0
R_OUTER = 2                             # rounding of the outer chamfers' corners (half a cut face)       # stroke and counter height (multiples of 7 for the 7:4 grid)
H = 2 * STROKE + COUNTER                # 21 u
SLANT = H * 4 // 7                      # top-edge offset of a 7:4 (60°) side: 12 u
DIAG = 8 * STROKE // 7                  # 60° side width measured horizontally (0.993 x STROKE perpendicular)
LEFT_IN = lambda y: (H - y) * 4 // 7 + DIAG          # inner contour of the left side
# Triangular counters: the left side's inner contour meets the centre line at the counter's top.
BAR = (LEFT_IN(STROKE), LEFT_IN(STROKE) + STROKE)    # centre line x range
TOTAL_W = 2 * BAR[0] + STROKE                        # centre line in the middle of the width
W = TOTAL_W - SLANT                                  # length of the horizontal edges
RIGHT_IN = lambda y: W + (H - y) * 4 // 7 - DIAG
CUT = 4 * STROKE // 7                   # the side's grid point one stroke above its acute corner
OUTER = [(CUT, H - STROKE), (CUT, H), (W, H), (TOTAL_W - CUT, STROKE), (TOTAL_W - CUT, 0), (SLANT, 0)]  # acute corners cut
INNER = [(LEFT_IN(H - STROKE), H - STROKE), (RIGHT_IN(H - STROKE), H - STROKE),
         (RIGHT_IN(STROKE), STROKE), (LEFT_IN(STROKE), STROKE)]


def rounded_path(pts, r, u):
    if r <= 0:
        f = lambda p: f"{p[0] * u:.3f},{p[1] * u:.3f}"
        return "M" + " L".join(f(p) for p in pts) + " Z"
    n, segs = len(pts), []
    for i in range(n):
        prev, cur, nxt = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b):
            d = math.dist(a, b); k = min(r, d / 2) / d
            return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
        segs.append((toward(cur, prev), cur, toward(cur, nxt)))
    f = lambda p: f"{p[0] * u:.2f},{p[1] * u:.2f}"
    d = f"M{f(segs[0][2])}"
    for i in range(1, n + 1):
        a, c, b = segs[i % n]
        d += f" L{f(a)} Q{f(c)} {f(b)}"
    return d + " Z"


def chamfer(poly, length):
    """Cut every corner of a polygon so that every cut face has the same length.
    A corner of angle t cut symmetrically with a face of length L moves L / (2 sin(t/2))
    along each of its edges."""
    out, n = [], len(poly)
    for i in range(n):
        prev, cur, nxt = poly[i - 1], poly[i], poly[(i + 1) % n]
        v1 = (prev[0] - cur[0], prev[1] - cur[1]); v2 = (nxt[0] - cur[0], nxt[1] - cur[1])
        d1, d2 = math.hypot(*v1), math.hypot(*v2)
        angle = math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (d1 * d2))
        leg = length / (2 * math.sin(angle / 2))
        out.append((cur[0] + v1[0] * leg / d1, cur[1] + v1[1] * leg / d1))
        out.append((cur[0] + v2[0] * leg / d2, cur[1] + v2[1] * leg / d2))
    return out


def counters():
    # Each counter is a triangle (a horizontal stroke, a 60° side and the centre line) with all
    # three corners chamfered with cut faces of equal length (CHAMFER u): a six-sided counter.
    yb, yt = H - STROKE, STROKE
    left = [(LEFT_IN(yb), yb), (BAR[0], yb), (BAR[0], yt)]
    right = [(BAR[1], yb), (BAR[1], yt), (RIGHT_IN(yt), yt)]
    return chamfer(left, CHAMFER), chamfer(right, CHAMFER)


def svg(u, fg, bg, grid):
    pad = 4 if grid else 2
    vw, vh = (TOTAL_W + 2 * pad) * u, (H + 2 * pad) * u
    left, right = counters()
    d = rounded_path(chamfer(OUTER, CHAMFER), R_OUTER, u) + " " + rounded_path(left, R, u) + " " + rounded_path(right, R, u)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad * u} {-pad * u} {vw} {vh}">',
           '<title>OpenDAP</title>']
    if bg != "none":
        out.append(f'<rect x="{-pad * u}" y="{-pad * u}" width="{vw}" height="{vh}" fill="{bg}"/>')
    if grid:
        g = []
        for x in range(-pad, TOTAL_W + pad + 1):
            g.append(f'<line x1="{x * u}" y1="{-pad * u}" x2="{x * u}" y2="{(H + pad) * u}"/>')
        for y in range(-pad, H + pad + 1):
            g.append(f'<line x1="{-pad * u}" y1="{y * u}" x2="{(TOTAL_W + pad) * u}" y2="{y * u}"/>')
        out.append(f'<g stroke="#3A4148" stroke-width="{u * 0.04}">' + "".join(g) + '</g>')
    out.append(f'<path d="{d}" fill="{fg}" fill-rule="evenodd"{" opacity=\"0.85\"" if grid else ""}/>')
    if grid:
        par = " ".join(f"{x * u},{y * u}" for x, y in [(0, H), (W, H), (TOTAL_W, 0), (SLANT, 0)])
        inn = " ".join(f"{x * u},{y * u}" for x, y in INNER)
        out.append(f'<g fill="none" stroke="#FF6A2A" stroke-width="{u * 0.12}" stroke-dasharray="{u * 0.5},{u * 0.3}">'
                   f'<polygon points="{par}"/><polygon points="{inn}"/></g>')
        # 7:4 (60°) reference triangle at the bottom-left
        out.append(f'<g fill="none" stroke="#69BFFF" stroke-width="{u * 0.12}">'
                   f'<polyline points="0,{H * u} {CUT * u},{H * u} {CUT * u},{(H - STROKE) * u} 0,{H * u}"/></g>')
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
