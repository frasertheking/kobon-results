# Kobon triangles

Results from an ongoing computer search on the Kobon triangle problem: how many
non-overlapping triangles can you make with n straight lines?

Known values and bounds are collected in [OEIS A006066](https://oeis.org/A006066).
The best public collection of arrangements is the gallery by Parpalak and Utkin
([ud1/kobon-solutions](https://github.com/ud1/kobon-solutions)).

## Results

| n  | triangles | upper bound | file |
|----|-----------|-------------|------|
| 40 | 495       | 502         | [certificates/n40_495.json](certificates/n40_495.json) |
| 74 | 1763      | 1767        | [certificates/n74_1763.json](certificates/n74_1763.json) |
| 98 | 3119      | 3125        | [certificates/n98_3119.json](certificates/n98_3119.json) |

**40 lines, 495 triangles.** The previous best we know of is 494, and OEIS has no
value for n = 40 yet. The arrangement has two triple points, both on the same line,
and no parallel lines.

How it was found: take a 494-triangle arrangement from our search, delete one line,
and work out exactly which way of putting a line back (as a pseudoline, allowed to
pass through existing crossing points) gives the most triangles. For this base the
answer is 495, using a line through two crossing points. The rest of the
arrangement was then nudged slightly until the straight line through those two
points crosses everything in the same order. This is the same kind of move as in
Parpalak and Utkin's 50-line arrangement with 792 triangles.

**74 lines, 1763 triangles.** We start from a perfect 73-line arrangement (1727
triangles) and add one line far out, beyond every crossing point, at an angle where it
closes off 36 of the outer wedges into new triangles. None of the original triangles
are lost.

The idea itself is not new. Bartholdi, Blanc and Loisel describe it, and Zarzuelo
proves that it always gains m triangles for 2m+1 lines in this situation. What's new
here is the explicit 74-line file. The classical construction gives 1752 for n = 74.
The 73-line base is a cleaned-up version of a perfect arrangement from the
[rsi-kobon-triangles](https://github.com/Rohith18p/rsi-kobon-triangles) repo.

**98 lines, 3119 triangles.** Same construction: a perfect 97-line arrangement (3071
triangles, a doubling from the rsi-kobon-triangles repo) plus a far line that adds 48.
The classical construction gives 3104 for n = 98, and we don't know of an explicit
98-line arrangement with more.

There are interactive pictures in [viewer/n40_495.html](viewer/n40_495.html) and
[viewer/n74_1763.html](viewer/n74_1763.html).
Download it and open it in a browser. Most of the triangles are tiny, so zoom in.

## Adding one line to a perfect arrangement

We also proved a small lemma (see [notes/single_line.md](notes/single_line.md)).
Take a perfect arrangement of n = 2m+1 lines and add one more line that doesn't pass
through any existing crossing point. The number of triangles goes up by at most m.
The only exception is a gain of m+1, which needs the new line to cross one of the
segments that isn't part of any triangle. There are 2 of these when n ≡ 1 (mod 3) and
none otherwise.

So for these arrangements, the far-out line is already the best single line you can
add. Using this as a search constraint, we checked:

* None of the 88 perfect 43-line arrangements in the Parpalak–Utkin gallery reaches
  609 triangles with one more line in general position. 608 is the current best for
  n = 44.
* No line in general position added to our perfect 73-line base reaches 1764.

Lines through existing crossing points aren't covered by the proof, but they are now
checked by computer: for each of the 88 bases we compute the best possible added
line exactly, including pseudolines and lines through crossing points. None of them
gets past 608.

## Checking a file

Every file lists its lines as integer triples (a, b, c), meaning a·x + b·y + c = 0.
The counter only needs Python:

    python3 verify.py certificates/n74_1763.json

It uses exact integer arithmetic, so there is no floating point anywhere.

## Status

Still searching, mainly for n = 39, 40, 44, 47 and 48, where OEIS has no value yet.
This repo only gets updated when something is verified.

Fraser King, 2026
