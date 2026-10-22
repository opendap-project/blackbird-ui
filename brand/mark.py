#!/usr/bin/env python3
"""Generate the OpenDAP mark (Draft), constructed on a 1:1 grid with industrial angles.

Construction (grid units, u):
- Angles: 0°, 90° and 45° only. 45° is the industrial (set-square) angle native to a
  square grid: the sides rise one unit per unit across.
- Strokes: horizontal edges and the vertical centre line 4 u. The 45° sides are 6 u wide
  measured horizontally, 4.24 u measured perpendicular: about 6 % heavier, the usual
  optical compensation for diagonals, and it keeps the inner contour on the grid.
- Height 24 u = 4 u + 16 u counter + 4 u. The top edge is offset 24 u (45°). Horizontal
  edges 40 u long; overall 64 u x 24 u. Centre line from x = 30 u to 34 u (the middle of 64 u).
- Counters: each narrows to 4 u (one stroke) at its tip and widens to 20 u at its base.
- Acute corners (bottom-left, top-right) cut vertically at the first grid point of the side,
  4 u long (one stroke), echoing the centre line.
- Every corner, outer and inner, rounded by 0.5 u: subtle, almost invisible.

  mark.py OUT.svg [--unit PX] [--fg HEX] [--bg HEX|none] [--grid]
"""
import argparse, math

H, W, SLANT, R = 24, 40, 24, 0.5
TOTAL_W = W + SLANT
OUTER = [(4, 20), (4, 24), (40, 24), (60, 4), (60, 0), (24, 0)]   # clockwise, acute corners cut
INNER = [(10, 20), (38, 20), (54, 4), (26, 4)]                     # counters' outer boundary
BAR = (30, 34)                                                     # centre line x range


def rounded_path(pts, r, u):
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


def counters():
    # The inner contour split by the centre line into the two counters (the O's and D's holes).
    left = [(10, 20), (BAR[0], 20), (BAR[0], 4), (26, 4)]
    right = [(BAR[1], 20), (38, 20), (54, 4), (BAR[1], 4)]
    return left, right


def svg(u, fg, bg, grid):
    pad = 4 if grid else 2
    vw, vh = (TOTAL_W + 2 * pad) * u, (H + 2 * pad) * u
    left, right = counters()
    d = rounded_path(OUTER, R, u) + " " + rounded_path(left, R, u) + " " + rounded_path(right, R, u)
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
        # 45° reference square at the bottom-left
        out.append(f'<g fill="none" stroke="#69BFFF" stroke-width="{u * 0.12}">'
                   f'<polyline points="0,{H * u} {4 * u},{H * u} {4 * u},{(H - 4) * u} 0,{H * u}"/></g>')
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
