# Curriculum map — Algorithms, Computability, and Complexity

This is an editorial map, **not** a count or duration policy. Lecture boundaries may change when mathematical exposition demands it. No lecture should be shortened to meet a fixed runtime, and no topic should be retained merely to achieve a quota.

## Foundations (drafted)

- **001000** — What Is an Algorithm, Really? Formal problems, specifications, Euclidean algorithm, invariants, termination, and Church–Turing thesis.
- **002000** — Why Some Problems Are Harder Than Others. Input encodings, asymptotic notation, merge sort, comparison lower bound, bit versus word models.
- **003000** — From Mathematical Proof to Executable Algorithm. Lower-bound search; invariant, decreasing measure, proof-to-implementation gaps, and verification practice.

## Computability and mathematical limits (partly drafted)

- **004000 — drafted:** Why No Program Can Decide Every Halting Question; detailed diagonal argument, its exact assumptions, and restricted program classes.
- **005000 — drafted:** Recognizing an Answer Is Not the Same as Deciding It; r.e. languages, complements, dovetailing, enumeration.
- **006000 — drafted:** Reductions: How One Impossible Decision Problem Reveals Another; mapping reductions, two-way transfer, and Rice's theorem.
- Finite-state computation: languages, regular expressions, automata, and real implementation limits.
- Stacks and grammars: pushdown automata, context-free parsing, and recognition boundaries.
- Mathematical models of computation: universal machines, lambda calculus, recursive functions, and the proper scope of the Church–Turing thesis.

## Design paradigms and problem-solving techniques

- Divide-and-conquer beyond merge sort: selection, recurrence proof methods, data movement costs.
- Dynamic programming as a state-space argument: optimal substructure, overlapping subproblems, correct state invariants.
- Greedy algorithms: exchange arguments, counterexamples, matroids, and selection criteria.
- Graph traversal: BFS, DFS, reachability, connected components, and complexity under adjacency representations.
- Shortest paths: Dijkstra, Bellman–Ford, negative edges, potentials, and invariant-driven correctness.
- Flows, cuts, and matchings: residual networks, augmentation, maximality, minimum cut, and reductions.
- Data structures and amortized analysis: dynamic arrays, potential method, union-find and inverse-Ackermann phenomena.
- Randomized algorithms: algorithmic randomness versus input distributions, one- versus two-sided error, and repeatability.

## Complexity theory and limits of efficiency

- Polynomial time and the importance of encoding: decision problems and formal cost models.
- NP and polynomially checkable certificates: exact definition before hardness rhetoric.
- Polynomial-time many-one reductions, NP-hardness, and NP-completeness: explicit proof ladders and Cook–Levin's contribution.
- Space complexity: configuration arguments, nondeterminism, and time–space tradeoffs.
- Beyond P and NP: exponential time, hierarchy ideas, parameterized complexity, and conditional bounds.
- Approximation: lower bounds, approximation ratios, and when guarantees do and do not transfer.
- Online and streaming algorithms: one-pass information limits, competitive analysis, and sketches.
- Fine-grained complexity: conditional reductions under named hypotheses; distinguish hypotheses from established theorems.

## From mathematics to verifiable implementations

- Recursive specification and structural induction: abstract semantics and executable correspondences.
- Refinement of graph/tree algorithms: representation invariants, finite memory, integer widths, and asymptotic resources.
- Formal complexity proofs: cost semantics, recurrence bounds, and compatibility with Lean and related proof assistants.
- Trust boundaries of verified computation: kernels, code extraction, foreign functions, compilers, and machine models.

## Attribution and source-check priorities

- Foundational results should credit original authors (e.g., Turing, Church, Floyd, Hoare, Cook, Levin, Dijkstra) separately from modern textbook exposition. Don't attribute standard original derivations to a secondary lecture note.
- Lower bounds always identify the computational model. Reductions specify direction and resource overhead. Hardness statements identify assumptions and whether a conjecture remains open.
- For future complexity-formalization lectures, compare current Lean/Mathlib and research infrastructure at time of drafting rather than assume today's ecosystem remains fixed.
- For each new lecture, include exact claim anchors and explicit provenance classes for source-backed claims, original reasoning, or unresolved interpretations. Cite full texts precisely when accessible and flag abstract-only access.

## Suggested next focused batch

The next independent block should distinguish **finite-state models, automata, and context-free languages** from Turing-complete computation; then return to **design paradigms** (divide-and-conquer, dynamic programming, greedy algorithms, graph search). A later focused block should tackle polynomial-time reductions and NP-completeness with explicit cost bounds. Preserve complete proofs without any lecture-duration policy.
