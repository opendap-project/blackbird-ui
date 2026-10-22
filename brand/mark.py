#!/usr/bin/env python3
"""Generate the OpenDAP mark (Draft): a horizontal rhombus outline with the top and bottom
corners cut flat and the left and right tips rounded, a thick inside stroke (it grows inward,
no fill), and a vertical centre line of the same thickness. The outline reads as the O and,
with the line, the D of OpenDAP.

  mark.py [--width W] [--height H] [--cut K] [--round K] [--stroke T] [--fg HEX] [--bg HEX|none] OUT.svg
"""
import argparse


def mark(width, height, cut, rnd, stroke, fg, bg, pad):
    left, top, right, bottom = (0, height / 2), (width / 2, 0), (width, height / 2), (width / 2, height)
    lerp = lambda a, b, k: (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
    p1, a = lerp(left, top, rnd), lerp(left, top, 1 - cut)
    b, p2 = lerp(top, right, cut), lerp(top, right, 1 - rnd)
    p3, c = lerp(right, bottom, rnd), lerp(right, bottom, 1 - cut)
    d, p4 = lerp(bottom, left, cut), lerp(bottom, left, 1 - rnd)
    f = lambda p: f"{p[0]:.2f},{p[1]:.2f}"
    path = (f"M{f(p1)} L{f(a)} L{f(b)} L{f(p2)} Q{f(right)} {f(p3)} "
            f"L{f(c)} L{f(d)} L{f(p4)} Q{f(left)} {f(p1)} Z")
    w, h = width + 2 * pad, height + 2 * pad
    background = "" if bg == "none" else f'<rect x="{-pad}" y="{-pad}" width="{w}" height="{h}" fill="{bg}"/>\n'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {w} {h}">\n'
            f'<title>OpenDAP</title>\n{background}'
            f'<defs><clipPath id="mark-shape"><path d="{path}"/></clipPath></defs>\n'
            f'<g clip-path="url(#mark-shape)" fill="none" stroke="{fg}" stroke-linejoin="round">\n'
            f'<path d="{path}" stroke-width="{2 * stroke}"/>\n'
            f'<line x1="{width / 2}" y1="0" x2="{width / 2}" y2="{height}" stroke-width="{stroke}"/>\n'
            '</g>\n</svg>\n')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--width", type=float, default=240)
    ap.add_argument("--height", type=float, default=150)
    ap.add_argument("--cut", type=float, default=0.16, help="top/bottom cut, fraction of the edge")
    ap.add_argument("--round", type=float, default=0.16, help="left/right rounding, fraction of the edge")
    ap.add_argument("--stroke", type=float, default=22, help="inside stroke and centre line thickness")
    ap.add_argument("--fg", default="#F5F6F4")
    ap.add_argument("--bg", default="none")
    ap.add_argument("--pad", type=float, default=20)
    a = ap.parse_args()
    open(a.out, "w").write(mark(a.width, a.height, a.cut, a.round, a.stroke, a.fg, a.bg, a.pad))
