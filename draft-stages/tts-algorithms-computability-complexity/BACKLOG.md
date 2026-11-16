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
- **007000 — drafted:** Finite-state computation, DFA invariants, product closure, decidability, and bounded-memory limits.
- **008000 — drafted:** NFA/regex equivalence, pumping and minimal states. **009000 — drafted:** Stacks, context-free grammars, CYK, ambiguity, and the CFL pumping barrier.
- Mathematical models of computation: universal machines, lambda calculus, recursive functions, and the proper scope of the Church–Turing thesis.

## Design paradigms and problem-solving techniques

- **010000 — drafted:** Divide-and-conquer selection, deterministic pivot guarantees, rank invariants, and explicit recurrence proof.
- **011000 — drafted:** Dynamic programming via weighted interval scheduling, optimal-substructure proofs, witness recovery, and resource assumptions.
- **012000 — drafted:** Greedy interval scheduling with two proofs, weighted counterexamples, and matroid comparison.
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

Lectures 010000–012000 now establish three algorithm-design proof patterns.
Next, graph traversal and shortest paths (BFS, DFS, Dijkstra, Bellman–Ford)
would apply invariants to structured data and test how representation changes
cost. The following focused block should develop a full complexity-classification
and polynomial-reduction ladder through NP-completeness, with explicit input
encodings and careful attribution to Cook and Levin. Return to universal
computational models and machine-checked complexity analysis later. No lecture
length or count target applies.
