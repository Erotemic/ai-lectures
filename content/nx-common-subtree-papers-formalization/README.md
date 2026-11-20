# NX Common Subtree Papers & Formalization

**Goal:** Read and understand three common-subtree papers well enough to follow their mathematical arguments, read the actual Lean formalization, and identify productive next theorems and implementation-refinement work in `networkx_algo_common_subtree`.

The course starts with **independent problem definitions**, works through recurrences and complexity arguments, then follows those statements into Lean and Rust. The papers are not collapsed into a single definition of embedding. Listening time is determined by the mathematical substance, not a duration quota. Narration is self-contained at its declared level; precise notation, proofs and source paths appear in non-spoken companions.

## Available lectures

| ID | Lecture | Role |
| --- | --- | --- |
| 000000 | [Three Meanings of a Common Subtree](000000-three-meanings-of-a-common-subtree.md) | Orientation and the three paper contracts |
| 001000 | [Trees, Roots, Order, and the Shape of a Witness](001000-trees-roots-order-and-witnesses.md) | Shared graph prerequisites and feasible witnesses |
| 002000 | [Tree Dynamic Programming as a Proof](002000-tree-dynamic-programming-as-a-proof.md) | States, rooted recurrence, soundness, completeness and cost |
| 003000 | [Balanced Words and Ordered-Tree Contractions](003000-balanced-words-and-ordered-tree-contractions.md) | Foundation for Lozano–Valiente 2004 |
| 004000 | [Matching Child Branches and Reusing the Answer](004000-matchings-child-branches-and-reuse.md) | Foundation for both Droschinsky papers |
| 005000 | [The Small World of D, R, and S](005000-the-small-world-of-d-r-and-s.md) | Decomposition, six-state example, Theorem 1 and actual-leaf correction |
| 006000 | [Lemma 8: Three Exhaustive Choices](006000-lemma-eight-three-exhaustive-choices.md) | Soundness, completeness, witnesses and the independent optimum |
| 007000 | [From a Small State Space to a Running-Time Theorem](007000-from-small-state-space-to-runtime.md) | Theorem 3, expected hashing, actual operation counts and remaining costs |
| 008000 | [The Definition That Misses an Edge](008000-the-definition-that-misses-an-edge.md) | Printed containment audit, smallest counterexample, corrected operational bridge |
| 009000 | [From Tree Proof to Original Tokens](009000-from-tree-proof-to-original-tokens.md) | Lean theorem-reading path, independent contracts, indexed/token witnesses, verified Rust reference boundary |
| 010000 | [The Map Is the Object](010000-the-map-is-the-object.md) | Droschinsky 2016 nonempty weighted isomorphisms, scoring and Lean specification |
| 011000 | [Why the Children Become a Matching](011000-why-the-children-become-a-matching.md) | Equation (1), both proof directions, fixed-root Lemma 2 and the rooted Lean reference |
| 012000 | [From Optional Branches to a Perfect Assignment](012000-from-optional-branches-to-a-perfect-assignment.md) | Lemma 5, copied graph, dual certificate, initial matching and rectangular cost |
| 013000 | [One Deletion, One Augmentation](013000-one-deletion-one-augmentation.md) | Lemma 6, unmatched reuse, one-deficit repair and family cost |
| 014000 | [Counting the Whole Algorithm](014000-counting-the-whole-algorithm.md) | Algorithm 1, Theorems 7 and 4, grouped families and tree-degree summation |
| 015000 | [From a Proved Recurrence to Fast Rust](015000-from-proved-math-to-fast-rust.md) | Exact Lean/Rust assurance frontier, production representation gaps and viable proof interfaces |

The first five lectures establish foundations. Lectures `005000`–`007000` develop the Lozano–Valiente decomposition, recurrence and cost argument. `008000` audits the printed Definition 2 against actual contractions; `009000` gives a source-guided Lean and Rust reference-proof reading. Lectures `010000`–`015000` develop the 2016 paper: the independent weighted-isomorphism specification, the rooted matching recurrence and fixed-root lemma, the copied-graph matching reduction (Lemma 5), the one-right-vertex deletion family (Lemma 6), the whole-algorithm degree-sum proof (Theorems 7 and 4), and the formalization/source-refinement frontier. None of these lectures certifies the optimized graph backend or the end-to-end Python/NetworkX API. See [ROADMAP.md](ROADMAP.md) for the remaining paper-specific sequence and [FORMALIZATION_MAP.md](FORMALIZATION_MAP.md) for the exact snapshot of proved and open source results.

## Suggested listening routes

**All three papers:** `000000 → 001000 → 002000 → 003000 → 004000`, then choose a paper path. The 2004 paper path is available through `009000`; the 2016 branch is written through `015000`, including the whole-algorithm runtime argument and a formalization/source-refinement reading guide.

**Lozano–Valiente (ordered contractions):** `000000 → 001000 → 002000 → 003000 → 005000 → 006000 → 007000 → 008000 → 009000`. An optional earlier refresher is `algorithms-computability-complexity:011000` (dynamic programming), with `logic-types:004000` (inductive types) available before the formalization lectures.

**Droschinsky 2016 (unordered isomorphism):** `000000 → 001000 → 002000 → 004000 → 010000 → 011000 → 012000 → 013000 → 014000 → 015000`. These lectures follow independent specification, recurrence, Lemmas 5–6, Theorems 7 and 4, and the exact current Lean/Rust proof frontier. Existing `discrete-mathematics:005000` develops matchings and flow certificates at greater breadth; `algorithms-computability-complexity:015000` develops optimization certificates.

**Droschinsky 2018 (topological embedding):** `000000 → 001000 → 002000 → 004000`. The 2016 path is helpful for the shared matching machinery but its strict-isomorphism problem is **not** a prerequisite definition that can substitute for the 2018 embedding contract.

These are suggestions, not hidden audio or duplication of existing tracks. Manuscripts in other tracks remain there; cross-links identify them by `track:lecture_id`.

## Existing math and Lean foundations to reuse

| Existing lecture | Why use it |
| --- | --- |
| `mathematical-proof:009000` | Finite sets, functions, quotients and induction |
| `algorithms-computability-complexity:011000` | Dynamic programming as a correctness argument |
| `algorithms-computability-complexity:017000` | Amortized costs, resource accounting and data-structure growth |
| `discrete-mathematics:005000` | Graph matchings, flow certificates and related combinatorics |
| `logic-types:004000` | Inductive data types and structural recursion |
| `logic-types:005000` and `logic-types:006000` | Equality and rewriting in Lean |
| `logic-types:008000` | Proof assistant kernel, elaboration and what is actually checked |

The future source-refinement lectures may warrant a new general-purpose course on verification of imperative code and complexity/cost semantics. This track will introduce the pieces it needs rather than requiring a full type-theory curriculum.

## Primary paper editions

1. Antoni Lozano and Gabriel Valiente, [*On the Maximum Common Embedded Subtree Problem for Ordered Trees*](https://www.cs.upc.edu/~antoni/subtree.pdf) (2004), original manuscript. Ordered edge contraction, balanced sequences, decomposition family and Lemma 8.
2. Andre Droschinsky, Nils M. Kriege and Petra Mutzel, [*Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*](https://arxiv.org/pdf/1602.07210v4) (2016), pinned arXiv v4. Weighted strict subtree isomorphism, root reduction and related matching instances.
3. Andre Droschinsky, Nils M. Kriege and Petra Mutzel, [*Largest Weight Common Subtree Embeddings with Distance Penalties*](https://arxiv.org/pdf/1805.00821v1) (2018), pinned arXiv v1. Topological path embedding, edge reward and skipped-vertex penalty, mapped/skipped states.

The repository's `docs/planning/paper_statement_crosswalk.md` supplies theorem-level pins and manuscript hashes. Its `proofs/PROOF_STATUS.md` describes the source-level assurance frontier. The exact snapshot is from the two repositories supplied on **November 19, 2026**. Status may change when code or Lean proofs change; refresh the crosswalk before drafting subsequent proof lectures.

## Authoring boundaries

- A transcript is indexed only when its complete spoken manuscript and metadata exist. Future numbered titles remain in `ROADMAP.md` until written.
- Avoid assertions like “fully verified” unless the particular statement, executable path and cost model are identified. Mathematical correctness, actual Rust behavior, Python conversion and complexity are different endpoints.
- The 2004 printed Definition 2 must remain distinguishable from operational matched-pair deletion; the two are not equivalent in the least-relation interpretation.
- The ordered exact-rational isomorphism backend is a project extension with its own contract, not a theorem claimed by the 2004 paper.
- The 2018 direct-edge reward is awarded only if **both** representing paths have length one. Otherwise skipped-vertex distance penalties apply.

**Next paper branch:** `016000`, begin Droschinsky 2018 with its independent skeleton/path-embedding definition, then the exact edge-reward and skipped-path penalty rules. Shared Lean/Rust proof-method lectures are planned after the paper branches. **Future sessions:** Follow [ROADMAP.md](ROADMAP.md) by the desired paper or proof frontier; refresh the latest source crosswalk for status-sensitive lectures.
