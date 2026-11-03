# Far-line doubling for odd bundles

This note describes the construction behind the 39/477, 40/496, 47/701 and 48/723
arrangements in `certificates/`.

## Classical doubling and why it stops at sizes 1 mod 4

The doubling of Bartholdi et al. (and Forge and Ramirez Alfonsin) takes an arrangement A with a
line Y0 and adds m new lines running in a thin strip around Y0. Inside the strip the m + 1
lines (Y0 and the new ones) cross each other in an odd-even transposition pattern, one round of
crossings between each pair of consecutive lines of A that cross Y0. Using only the order of the
lines inside the strip, the strip can hold at most m^2 new triangles, and that maximum is reached.

The catch is what happens to the triangles A already had on Y0. Such a triangle survives only on
a segment of Y0 where the outermost strip line on its side does not take part in a crossing.

- With m even, the top and bottom strip lines are free on complementary segments. The usual
  pattern, one triangle of A on every segment of Y0 with sides alternating, survives completely,
  and the gain is exactly m^2.
- With m odd, both outer strip lines are free on the same alternate segments. The usual pattern
  loses (m - 1)/2 triangles.

Doubling an odd perfect arrangement therefore only works with an even bundle, which gives sizes
2m - 1 with m odd, i.e. 1 mod 4. 39 and 47 are 3 mod 4.

## The fix: a far line with alternating wedges

Take a perfect odd arrangement C of m lines and choose Y0 far outside C. The triangles that Y0
forms with C are wedges of C: unbounded faces whose two rays leave from one vertex. Two wedges
can never be adjacent along Y0, so Y0 gets exactly (m - 1)/2 of them, on alternating segments.
That is exactly the pattern an odd bundle preserves.

So add m lines (an odd bundle) around Y0:

    K(2m + 1) >= K(C) + (m - 1)/2 + m^2

A bundle of m + 1 lines gives

    K(2m + 2) >= K(C) + (m - 1)/2 + m(m + 1).

Small checks, with exact counts of constructed arrangements:

| C | 2m+1 lines (formula) | 2m+2 lines (formula) |
|---|---|---|
| m = 5 (5 triangles) | 11 lines: 32 (32, the known optimum) | 12 lines: 37 (37) |
| m = 7 (11) | 15 lines: 63 (63) | 16 lines: 70 (70) |
| m = 9 (21) | 19 lines: 106 (106) | |

## Making it straight

The bundle lines are tangents to a conic with parameters beta_w. Two of them cross at
x = x_c + lambda * tan(beta_w + beta_w'). Requiring every pair to cross between the right two
lines of C is a linear program in the betas. It is solved over the choice of Y0 (direction,
distance, which window of wedges) and the chart (x_c, lambda). The result is rounded to integers
with a strip width of about 1e-8, and the triangles are counted exactly. For most bases the LP is
infeasible. The bases that worked are gallery perfect arrangements by Parpalak and Utkin
([ud1/kobon-solutions](https://github.com/ud1/kobon-solutions)):

| result | base C | count |
|---|---|---|
| 39 / 477 | P19-12daaceiiq6nr (107) | 107 + 9 + 361 |
| 40 / 496 | P19-12hco47xx8083 (107) | 107 + 9 + 380 |
| 47 / 701 | P23-23kpm7pjzyn1v (161) | 161 + 11 + 529 |
| 48 / 723 | P23-23kpm7pjzyn1v (161) | one short of 161 + 11 + 552 = 724 |

Each certificate was counted by `verify.py`, by the triangle list check in `check_triangles.py`,
and by two further independent counters. All four arrangements are simple.
