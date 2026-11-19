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
| 007000 | What a Finite Machine Can Remember | DFA definition, two complete transition-table invariants, product closure, decidable equivalence, and an infinite-prefix nonregularity proof |
| 008000 | Many Descriptions, One Regular Language | NFA subset construction, regular-expression equivalence, correct pumping-lemma quantifiers, and both directions of Myhill–Nerode |
| 009000 | When a Stack Changes the Language | Context-free grammar derivations, PDA recognition, CYK parsing proof, ambiguity, and an explicit non-context-freeness argument |
| 010000 | Divide and Conquer: Choosing a Pivot That Earns Its Cost | Deterministic order statistics, three-way partition invariants, median-of-medians selection, and worst-case linear recurrence proof |
| 011000 | Dynamic Programming: A Proof Hidden in the Table | Weighted interval scheduling: state definitions, include/exclude proof, O(n log n) table and witness recovery |
| 012000 | Greedy Algorithms: When the Next Choice Can Be Trusted | Earliest-finish exchange and staying-ahead proofs; weighted counterexamples, matroid augmentation and its limits |

These are standalone narrated lectures. They make their assumptions explicit and avoid relying on previous episodes for necessary definitions. Lecture length follows the mathematics being taught; there are no target durations or word-count requirements.

## Source and evidence conventions

- `track.json` is the course manifest. Lecture IDs are stable within this track.
- Each manuscript contains one spoken-text region. Exact definitions, proofs, code, bibliographic notes, and exercises live below the ending marker.
- `metadata/sources.json` records bibliographic sources, including primary papers and credited instructors/authors.
- `metadata/<id>.json` links source records to **exact spoken anchors**. An original worked calculation is labeled as such rather than presented as an external author's result.
- `examples/` contains independent, executable **checking and teaching code**, not machine-checked proofs. `finite_reductions_lab.py` never treats a timeout as proof of divergence; the selection and scheduling checks compare against independent finite specifications. No claim of formal Lean verification is made.
- `BACKLOG.md` records optional future topics and source-research needs; it is not a promise to reach a particular lecture count.

## Focused verification

After import into the repository root:

```bash
python tools/lecture_inventory.py
python content/algorithms-computability-complexity/examples/lower_bound_reference.py --check
python content/algorithms-computability-complexity/citations/validate.py
python content/algorithms-computability-complexity/examples/finite_reductions_lab.py --check
python content/algorithms-computability-complexity/examples/automata_and_grammars_lab.py --check
python content/algorithms-computability-complexity/examples/algorithm_design_lab.py --check
```

For independent citation checks, each anchored phrase should occur exactly once inside the *spoken* region, and each `source_id` should resolve in `metadata/sources.json`. No runtime pack builds, TTS, or repository-wide test suite is required for this authoring batch.

## Relationship with existing tracks

`tts-logic-types` covers logical and type-theoretic foundations; `tts-category-theory` and `tts-numerical-analysis` explore adjacent mathematics. This track focuses on the algorithmic specification, upper and lower cost bounds, decidability, reductions, and proof-to-implementation relationships. It may use similar technical vocabulary without assuming the listener has completed those other courses.

## Automata and grammar examples (007000–009000)

`examples/automata_and_grammars_lab.py` implements two complete DFAs, an NFA
with subset determinization, reachable product construction, BFS disagreement
witnesses, a stack recognizer, balanced parentheses, a CNF CYK chart, and
parse-tree counts for one ambiguous grammar. Its `--check` mode exhaustively
compares *bounded* input sets against independent specifications. The lectures
contain the universal mathematical arguments; exhaustive testing to a fixed
input length is **not** a formal proof of regularity, nonregularity, or
context-freeness. Existing Isabelle/HOL CYK formalization is cited separately
with correct authorship; no Lean formal proof is claimed here.


## Algorithm-design lab (010000–012000)

`examples/algorithm_design_lab.py` implements three-way median-of-medians
selection, a deliberately weak first-pivot selection routine, weighted interval
scheduling by dynamic programming (including a witness), and unweighted
interval scheduling by earliest finish. Run `python content/algorithms-computability-complexity/examples/algorithm_design_lab.py --check`. Its independent oracles are sorted order
statistics and enumerated compatible job subsets. Bounded input checks do not
constitute universal correctness, linear-time, or greedy-optimality proofs;
those appear as mathematical arguments in the manuscripts. No runtime library,
additional Python package, or binary asset is needed.

## Graph algorithms, hardness, and amortized resources (013000-017000)

Five new narrated foundations: BFS/DFS certificates (013000); weighted shortest paths with Dijkstra, Bellman-Ford, and acyclic order (014000); residual flow, cuts, and matching (015000); polynomial verification, NP, and an explicit three-SAT to independent-set reduction (016000); dynamic array and binary counter amortized analysis (017000). Each includes worked proofs, counterexamples, reading notes, and exercises with answers. The source-owned `navigation.json` offers `graph-algorithms` and `complexity-and-resource-bounds` deep dives; `overview` includes all 17 lectures; the original `:main` archive remains available.
