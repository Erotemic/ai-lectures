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

The initial five lectures are foundations and orientation, not a claim that the complete papers or their formalization have already been taught. See [ROADMAP.md](ROADMAP.md) for the remaining paper-specific sequence and [FORMALIZATION_MAP.md](FORMALIZATION_MAP.md) for the exact snapshot of proved and open source results.

## Suggested listening routes

**All three papers:** `000000 → 001000 → 002000 → 003000 → 004000`, then follow the planned paper-specific lectures as they are written.

**Lozano–Valiente (ordered contractions):** `000000 → 001000 → 002000 → 003000`. An optional earlier refresher is `algorithms-computability-complexity:011000` (dynamic programming), with `logic-types:004000` (inductive types) available before the formalization lectures.

**Droschinsky 2016 (unordered isomorphism):** `000000 → 001000 → 002000 → 004000`. Existing `discrete-mathematics:005000` develops matchings and flow certificates at greater breadth; `algorithms-computability-complexity:015000` develops optimization certificates.

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

**Future sessions:** Follow [ROADMAP.md](ROADMAP.md) by the user's preferred paper or theorem frontier. Each new session can add complete manuscripts without forcing the entire course to be written in one batch.
