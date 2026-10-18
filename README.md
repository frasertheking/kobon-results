# Kobon triangles

Results from an ongoing computer search on the Kobon triangle problem: how many
non-overlapping triangles can you make with n straight lines?

Known values and bounds are collected in [OEIS A006066](https://oeis.org/A006066).
The best public collection of arrangements is the gallery by Parpalak and Utkin
([ud1/kobon-solutions](https://github.com/ud1/kobon-solutions)).

## Results

| n  | triangles | upper bound | file |
|----|-----------|-------------|------|
| 74 | 1763      | 1767        | [certificates/n74_1763.json](certificates/n74_1763.json) |

**74 lines, 1763 triangles.** We start from a perfect 73-line arrangement (1727
triangles) and add one line far out, beyond every crossing point, at an angle where it
closes off 36 of the outer wedges into new triangles. None of the original triangles
are lost.

The idea itself is not new. Bartholdi, Blanc and Loisel describe it, and Zarzuelo
proves that it always gains m triangles for 2m+1 lines in this situation. What's new
here is the explicit 74-line file. The classical construction gives 1752 for n = 74.
The 73-line base is a cleaned-up version of a perfect arrangement from the
[rsi-kobon-triangles](https://github.com/Rohith18p/rsi-kobon-triangles) repo.

There's an interactive picture in [viewer/n74_1763.html](viewer/n74_1763.html).
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

Lines through existing crossing points aren't covered by the proof. We're still
checking those by computer.

## Checking a file

Every file lists its lines as integer triples (a, b, c), meaning a·x + b·y + c = 0.
The counter only needs Python:

    python3 verify.py certificates/n74_1763.json

It uses exact integer arithmetic, so there is no floating point anywhere.

## Status

Still searching, mainly for n = 39, 40, 44, 47 and 48, where OEIS has no value yet.
This repo only gets updated when something is verified.

Fraser King, 2026
