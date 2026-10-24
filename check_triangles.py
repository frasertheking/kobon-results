#!/usr/bin/env python3
"""Check a list of triangles against a line arrangement, exactly.

This is a second, independent check: it does not count anything itself. It
takes the triangles listed in a *_triangles.json file and checks each one:

  1. its three lines are distinct, no two are parallel, and they do not all
     pass through one point, so they bound a real triangle;
  2. no other line of the arrangement passes through the inside of it.

A triangle that passes both checks is a face of the arrangement. Two different
faces never overlap, so if every listed triangle passes and no triple is listed
twice, the arrangement has at least that many non-overlapping triangles.
Everything is done with integers, so there is no rounding.

    python3 check_triangles.py certificates/n40_495.json certificates/n40_495_triangles.json

Only the Python standard library is needed.
"""
import json
import sys


def sign(v):
    return (v > 0) - (v < 0)


def meet(l1, l2):
    """Intersection point in homogeneous coordinates (X, Y, W), W > 0, or None if parallel."""
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    X, Y, W = b1 * c2 - b2 * c1, c1 * a2 - c2 * a1, a1 * b2 - a2 * b1
    if W == 0:
        return None
    if W < 0:
        X, Y, W = -X, -Y, -W
    return X, Y, W


def check(lines, tri):
    i, j, k = tri
    if len({i, j, k}) != 3:
        return "repeated line"
    corners = [meet(lines[i], lines[j]), meet(lines[i], lines[k]), meet(lines[j], lines[k])]
    if None in corners:
        return "two of its lines are parallel"
    p, q = corners[0], corners[1]                    # same point? compare cross-multiplied coordinates
    if p[0] * q[2] == q[0] * p[2] and p[1] * q[2] == q[1] * p[2]:
        return "its three lines meet in one point"
    for l, (a, b, c) in enumerate(lines):
        if l in tri:
            continue
        s = {sign(a * X + b * Y + c * W) for X, Y, W in corners}
        if 1 in s and -1 in s:
            return f"line {l} passes through it"
    return None


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    lines = [tuple(int(v) for v in l) for l in json.load(open(sys.argv[1]))["lines"]]
    data = json.load(open(sys.argv[2]))
    tris = [tuple(t) for t in data["triangles"]]
    if len({tuple(sorted(t)) for t in tris}) != len(tris):
        sys.exit("FAIL: a triangle is listed twice")
    bad = 0
    for t in tris:
        why = check(lines, t)
        if why:
            print(f"FAIL {t}: {why}")
            bad += 1
    print(f"{len(lines)} lines, {len(tris)} listed triangles, {len(tris) - bad} pass")
    if bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
