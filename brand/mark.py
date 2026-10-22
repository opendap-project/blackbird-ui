#!/usr/bin/env python3
"""Generate the OpenDAP mark (Draft), constructed on a 1:1 grid with industrial angles.

Construction (grid units, u):
- Angles: 0°, 90° and 60°. The sides rise 7 u per 4 u across (60.26°), the grid-exact
  approximation of the 60° set-square angle (within 0.3°).
- Strokes: horizontal edges and the vertical centre line 21 u. The 60° sides are 24 u wide
  measured horizontally (20.8 u perpendicular): optically equal, and on the grid.
- Height 70 u = 21 u + 28 u counter + 21 u (stroke 30 % of the height). The top edge is
  offset 40 u (70 x 4/7). Overall 125 u x 70 u.
- Counters: triangles (a horizontal stroke, a 60° side and the centre line, which meets the
  side's inner contour at the counter's tip), with all three corners chamfered; every cut face
  is 3 u long: two six-sided counters.
- Acute outer corners cut vertically at the side's grid point one stroke above the corner:
  each cut is 21 u long, one stroke, echoing the centre line.
- Outer corners: every corner of the outline chamfered with the same cut-face length as the
  counters (3 u).
- Rounding: every corner, outer and inner, by a true circular arc of 1.5 u radius (half a
  cut face), so the curve is identical at every corner whatever its angle.

  mark.py OUT.svg [--unit PX] [--fg HEX] [--bg HEX|none] [--grid]
"""
import argparse, math

STROKE, COUNTER, CHAMFER, R = 21, 28, 3, 0
R_OUTER = 1.5                             # radius of every corner, outer and inner (half a cut face)       # stroke and counter height (multiples of 7 for the 7:4 grid)
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
    """Closed polygon with every corner rounded by a true circular arc of radius r (the same
    curve at every corner, whatever its angle). The tangent points sit r / tan(t/2) from the
    corner along each edge, t being the corner's interior angle."""
    f = lambda p: f"{p[0] * u:.3f},{p[1] * u:.3f}"
    if r <= 0:
        return "M" + " L".join(f(p) for p in pts) + " Z"
    n, corners = len(pts), []
    for i in range(n):
        prev, cur, nxt = pts[i - 1], pts[i], pts[(i + 1) % n]
        v1 = (prev[0] - cur[0], prev[1] - cur[1]); v2 = (nxt[0] - cur[0], nxt[1] - cur[1])
        d1, d2 = math.hypot(*v1), math.hypot(*v2)
        cosang = max(-1.0, min(1.0, (v1[0] * v2[0] + v1[1] * v2[1]) / (d1 * d2)))
        angle = math.acos(cosang)
        t = r / math.tan(angle / 2)
        t = min(t, d1 / 2, d2 / 2)
        radius = t * math.tan(angle / 2)
        a = (cur[0] + v1[0] * t / d1, cur[1] + v1[1] * t / d1)
        b = (cur[0] + v2[0] * t / d2, cur[1] + v2[1] * t / d2)
        cross = (cur[0] - prev[0]) * (nxt[1] - cur[1]) - (cur[1] - prev[1]) * (nxt[0] - cur[0])
        corners.append((a, b, radius, 1 if cross > 0 else 0))
    d = f"M{f(corners[0][1])}"
    for i in range(1, n + 1):
        a, b, radius, sweep = corners[i % n]
        d += f" L{f(a)} A{radius * u:.3f},{radius * u:.3f} 0 0 {sweep} {f(b)}"
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
    d = rounded_path(chamfer(OUTER, CHAMFER), R_OUTER, u) + " " + rounded_path(left, R_OUTER, u) + " " + rounded_path(right, R_OUTER, u)
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
