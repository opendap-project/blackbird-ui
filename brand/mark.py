#!/usr/bin/env python3
"""Generate the OpenDAP mark (Draft): a lying rhomboid (parallelogram) outline with horizontal
top and bottom edges and sides rising diagonally to the right; the acute corners are cut, every
corner is rounded; a thick inside stroke (it grows inward, no fill) and a vertical centre line of
the same thickness. The outline reads as the O and, with the line, the D of OpenDAP.

  mark.py [--width W] [--height H] [--slant S] [--cut C] [--radius R] [--stroke T] [--fg HEX] [--bg HEX|none] OUT.svg
"""
import argparse, math


def rounded_path(pts, radius):
    """Closed polygon with every corner rounded: each corner is replaced by a quadratic curve
    starting and ending `radius` along its two edges (limited to half the edge length)."""
    n, out = len(pts), []
    for i in range(n):
        prev, cur, nxt = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b):
            d = math.dist(a, b); k = min(radius, d / 2) / d
            return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
        out.append((toward(cur, prev), cur, toward(cur, nxt)))
    f = lambda p: f"{p[0]:.2f},{p[1]:.2f}"
    d = f"M{f(out[0][2])}"
    for i in range(1, n + 1):
        a, c, b = out[i % n]
        d += f" L{f(a)} Q{f(c)} {f(b)}"
    return d + " Z"


def mark(width, height, slant, cut, radius, stroke, fg, bg, pad):
    # Parallelogram: bottom-left, bottom-right, top-right, top-left; sides rise to the right.
    bl, br, tr, tl = (0, height), (width, height), (width + slant, 0), (slant, 0)
    lerp = lambda a, b, d: (a[0] + (b[0] - a[0]) * d / math.dist(a, b), a[1] + (b[1] - a[1]) * d / math.dist(a, b))
    # Cut the two acute corners (bottom-left and top-right) by `cut` along each edge.
    pts = [lerp(bl, tl, cut), lerp(bl, br, cut), br, lerp(tr, br, cut), lerp(tr, tl, cut), tl]
    path = rounded_path(pts, radius)
    cx = (width + slant) / 2
    total_w = width + slant
    w, h = total_w + 2 * pad, height + 2 * pad
    background = "" if bg == "none" else f'<rect x="{-pad}" y="{-pad}" width="{w}" height="{h}" fill="{bg}"/>\n'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {w} {h}">\n'
            f'<title>OpenDAP</title>\n{background}'
            f'<defs><clipPath id="mark-shape"><path d="{path}"/></clipPath></defs>\n'
            f'<g clip-path="url(#mark-shape)" fill="none" stroke="{fg}" stroke-linejoin="round">\n'
            f'<path d="{path}" stroke-width="{2 * stroke}"/>\n'
            f'<line x1="{cx}" y1="0" x2="{cx}" y2="{height}" stroke-width="{stroke}"/>\n'
            '</g>\n</svg>\n')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--width", type=float, default=200, help="length of the horizontal edges")
    ap.add_argument("--height", type=float, default=130)
    ap.add_argument("--slant", type=float, default=70, help="horizontal offset of the top edge (rising sides)")
    ap.add_argument("--cut", type=float, default=34, help="cut of the two acute corners, along each edge")
    ap.add_argument("--radius", type=float, default=14, help="rounding of every corner")
    ap.add_argument("--stroke", type=float, default=22, help="inside stroke and centre line thickness")
    ap.add_argument("--fg", default="#F5F6F4")
    ap.add_argument("--bg", default="none")
    ap.add_argument("--pad", type=float, default=20)
    a = ap.parse_args()
    open(a.out, "w").write(mark(a.width, a.height, a.slant, a.cut, a.radius, a.stroke, a.fg, a.bg, a.pad))
