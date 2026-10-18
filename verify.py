#!/usr/bin/env python3
"""Count the triangles in a line arrangement, exactly.

Each line is given by three integers (a, b, c) meaning a*x + b*y + c = 0.
Three lines form a triangle of the arrangement when no other line passes
through the inside of the triangle they bound. Everything is done with
integers, so there is no rounding.

    python3 verify.py certificates/n74_1763.json

Only the Python standard library is needed.
"""
import json
import sys
from itertools import combinations


def sign(v):
    return (v > 0) - (v < 0)


def meet(l1, l2):
    """Intersection point in homogeneous coordinates (X, Y, W), W > 0."""
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    X, Y, W = b1 * c2 - b2 * c1, c1 * a2 - c2 * a1, a1 * b2 - a2 * b1
    if W == 0:
        return None                      # parallel
    if W < 0:
        X, Y, W = -X, -Y, -W
    return X, Y, W


def det3(p, q, r):
    return (p[0] * (q[1] * r[2] - q[2] * r[1]) - p[1] * (q[0] * r[2] - q[2] * r[0])
            + p[2] * (q[0] * r[1] - q[1] * r[0]))


def count_triangles(lines):
    n = len(lines)
    if len({tuple(l) for l in lines}) != n:
        raise ValueError("duplicate lines")
    pts = {}
    for i, j in combinations(range(n), 2):
        pts[i, j] = meet(lines[i], lines[j])
    # side[l][(i, j)] = which side of line l the point i∩j is on (-1, 0, +1)
    side = [{} for _ in range(n)]
    for l, (a, b, c) in enumerate(lines):
        for key, p in pts.items():
            if p is not None:
                side[l][key] = sign(a * p[0] + b * p[1] + c * p[2])
    total = 0
    for i, j, k in combinations(range(n), 3):
        corners = [(i, j), (i, k), (j, k)]
        if any(pts[q] is None for q in corners) or det3(lines[i], lines[j], lines[k]) == 0:
            continue                     # parallel pair, or all three lines through one point
        ok = True
        for l in range(n):
            if l in (i, j, k):
                continue
            s = {side[l][q] for q in corners}
            if 1 in s and -1 in s:       # line l cuts through the triangle
                ok = False
                break
        total += ok
    return total


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    data = json.load(open(sys.argv[1]))
    lines = [tuple(int(v) for v in l) for l in data["lines"]]
    t = count_triangles(lines)
    print(f"{len(lines)} lines, {t} triangles")
    claimed = data.get("triangles")
    if claimed is not None and claimed != t:
        sys.exit(f"MISMATCH: file says {claimed}")


if __name__ == "__main__":
    main()
