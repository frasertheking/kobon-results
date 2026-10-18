# How many triangles can one extra line add?

## Setup

A is a simple arrangement of n lines: no two parallel, no three through one point. Its
bounded edges are the pieces of the lines between consecutive crossings. Each line has
n − 2 of them, so n(n − 2) in total.

A triangle uses 3 bounded edges, and a bounded edge can belong to at most one triangle.
(The two lines through its endpoints meet on only one side of it.) So A has at most
n(n − 2)/3 triangles. Call A *perfect* if it reaches ⌊n(n − 2)/3⌋. In a perfect
arrangement, every bounded edge is in exactly one triangle, except for
δ = n(n − 2) mod 3 "uncovered" edges. That's 2 uncovered edges when n ≡ 1 (mod 3) and
none otherwise.

## Lemma

Let A be perfect with n = 2m + 1, and let H be a new line that is not parallel to any
line of A and doesn't go through any crossing of A. Then H adds at most m triangles,
or m + 1 if H crosses one of the uncovered edges.

The argument only uses the order in which H meets the lines, so it works for
pseudolines too.

## Proof

H crosses the n lines at points p_1, …, p_n (in order along H) and passes through
faces F_0, F_1, …, F_n of A. Faces F_(i−1) and F_i share the edge (or ray) e_i of
line i that H crosses at p_i.

*Where new triangles come from.* Every face of A ∪ H is either an old face that H
misses, or one of the two pieces H cuts a face into.

* F_0 and F_n contain the ends of H, so both their pieces are unbounded.
* For 1 ≤ i ≤ n − 1, a piece of F_i is a triangle only when e_i and e_(i+1) are
  neighbouring sides of F_i, so that H cuts off the corner where they meet. That can
  happen on at most one side, so each F_i gives at most one new triangle.
* If F_i was itself a triangle, it's destroyed but leaves a triangle behind (any two
  sides of a triangle are neighbours). Net change 0.

So the gain equals the number of faces F_1, …, F_(n−1) that are not triangles but get
a corner cut off. Mark those faces with c_i = 1, and the rest with c_i = 0.

*No two neighbours.* Look at F_(i−1) and F_i, which share e_i.

* If e_i is a bounded edge covered by a triangle, that triangle is F_(i−1) or F_i, so
  one of them has c = 0.
* If e_i is a ray of line i, it has one endpoint v. A corner cut in F_(i−1) at e_i
  must be at v, so v lies on line i − 1. A corner cut in F_i at e_i puts v on line
  i + 1 too. Three lines through v is impossible in a simple arrangement, so the two
  cuts can't both happen.
* If e_i is an uncovered edge, there's no restriction.

*Counting.* c_1, …, c_(n−1) is a 0/1 sequence of length 2m with no two 1s next to
each other, except across uncovered edges. With no uncovered crossings, there are at
most m ones. One or two uncovered crossings split the sequence into blocks whose
lengths add up to 2m. That allows at most two odd blocks, so at most m + 1 ones. ∎

## Remarks

* The bound is reached by a line placed beyond all the crossings of A, which turns m
  of the outer wedges (unbounded faces with a single corner) into triangles. That's
  the classical way to get from 2m + 1 lines to 2m + 2.
* Nothing above used perfectness except to say which edges are covered. For any simple
  arrangement, the gain is at most (n − 1 + number of odd blocks)/2, where the blocks
  are split by the uncovered edges H crosses. This gives quick lower limits on how
  many uncovered edges a line must cross to reach a target. That's what made the n = 44
  and n = 74 checks fast.
* Lines through existing crossings are not covered. In exhaustive checks over about 150
  perfect arrangements with n between 7 and 37, no straight line ever added more than
  m. A few curved pseudolines through crossings reached m + 1, for n = 7 and one
  n = 31 arrangement, but they can't be drawn straight.

## Prior work

The far-out line and the "gains exactly m" result for perfect arrangements are in
Bartholdi–Blanc–Loisel (arXiv:0706.0723), Blanc (arXiv:0801.2845) and Zarzuelo
([kobon-proof](https://github.com/alejandrozu/kobon-proof), extension manuscript,
Lemma 2 and Corollary 4). Zarzuelo's upper bound covers lines outside the arrangement.
We haven't found a bound for lines passing through the middle, which is what the lemma
adds. If you know of one, please open an issue.
