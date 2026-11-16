# Algorithms, Computability, and Complexity

An independent, audio-first lecture track for mathematical computer science. The aim is to understand algorithms as objects that can be **specified, proved, implemented, and analyzed**, then to study the limits of what can be computed and what can be computed economically.

## Published sequence

| ID | Lecture | Central problem |
|---|---|---|
| 001000 | What Is an Algorithm, Really? | Specify a general problem, derive Euclid's algorithm, distinguish correctness from termination and computability |
| 002000 | Why Some Problems Are Harder Than Others | Understand cost models, recurrence analysis, information-theoretic lower bounds, and bit-size pitfalls |
| 003000 | From Mathematical Proof to Executable Algorithm | Derive a lower-bound search from a specification and transfer its obligations into executable code |
| 004000 | Why No Program Can Decide Every Halting Question | Modern diagonal proof of halting undecidability, finite-bounded contrast, and Turing's original historical formulation |
| 005000 | Recognizing an Answer Is Not the Same as Deciding It | Recognizers versus deciders, complement theorem, fair dovetailing, and computable enumeration |
| 006000 | Reductions: How One Impossible Decision Problem Reveals Another | Mapping reductions, direction and totality, acceptance/halting equivalences, and full proof of Rice's theorem |

These are standalone narrated lectures. They make their assumptions explicit and avoid relying on previous episodes for necessary definitions. Lecture length follows the mathematics being taught; there are no target durations or word-count requirements.

## Source and evidence conventions

- `track.json` is the course manifest. Lecture IDs are stable within this track.
- Each manuscript contains one spoken-text region. Exact definitions, proofs, code, bibliographic notes, and exercises live below the ending marker.
- `metadata/sources.json` records bibliographic sources, including primary papers and credited instructors/authors.
- `metadata/<id>.json` links source records to **exact spoken anchors**. An original worked calculation is labeled as such rather than presented as an external author's result.
- `examples/lower_bound_reference.py` and `examples/finite_reductions_lab.py` are independent, executable **checking and teaching code**, not machine-checked proofs. The second script never treats a timeout as proof of divergence. No claim of formal Lean verification is made.
- `BACKLOG.md` records optional future topics and source-research needs; it is not a promise to reach a particular lecture count.

## Focused verification

After import into the repository root:

```bash
python tools/lecture_inventory.py
python draft-stages/tts-algorithms-computability-complexity/examples/lower_bound_reference.py --check
python draft-stages/tts-algorithms-computability-complexity/citations/validate.py
python draft-stages/tts-algorithms-computability-complexity/examples/finite_reductions_lab.py --check
```

For independent citation checks, each anchored phrase should occur exactly once inside the *spoken* region, and each `source_id` should resolve in `metadata/sources.json`. No runtime pack builds, TTS, or repository-wide test suite is required for this authoring batch.

## Relationship with existing tracks

`tts-logic-types` covers logical and type-theoretic foundations; `tts-category-theory` and `tts-numerical-analysis` explore adjacent mathematics. This track focuses on the algorithmic specification, upper and lower cost bounds, decidability, reductions, and proof-to-implementation relationships. It may use similar technical vocabulary without assuming the listener has completed those other courses.
