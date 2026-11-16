# Mathematical Reasoning and Proof from First Principles — foundational track

**Created:** 2026-11-16, Mathematics Continuation 32. **Status:** 18 complete manuscripts, each with a standalone spoken region, an exact non-spoken mathematical companion, exercises with answers, and source metadata. Lecture length follows what is needed to teach the material, without a fixed duration policy.

## Why a distinct track?

The existing `tts-logic-types` course starts with propositions as types and assumes experience with basic proofs. `tts-discrete-mathematics` and the advanced geometry/algebra tracks rely on induction, constructions, rigorous quantifiers, sets, and functions. This introductory course teaches those prerequisites explicitly. It also gives the newer core Linear Algebra and Multivariable Calculus tracks a shared proof vocabulary.

## Complete sequence

| ID | Lecture | Background |
|---|---|---|
| 001000 | [What Counts as a Mathematical Proof?](001000-statements-evidence-and-proof.md) | Everyday arithmetic; no prior proof training |
| 002000 | [And, Or, Not, and If: Reading Mathematical Logic](002000-connectives-implication-truth.md) | Statements and counterexamples |
| 003000 | [For Every and There Exists: Quantifiers and Their Scope](003000-quantifiers-domains-and-negation.md) | Basic logical connectives |
| 004000 | [Definitions and If-and-Only-If: Keeping Both Directions](004000-definitions-equivalence-and-scope.md) | Implications and quantifiers |
| 005000 | [Direct Proof: Turning a Hypothesis into a Conclusion](005000-direct-proof-and-witnesses.md) | Definitions of integers and divisibility |
| 006000 | [Contraposition and Cases: Changing the Route, Not the Claim](006000-contraposition-and-proof-by-cases.md) | Implication and direct proof |
| 007000 | [Contradiction: Proving Something Cannot Happen](007000-contradiction-and-irrationality.md) | Even and odd integers; direct proof |
| 008000 | [Counterexamples: How One Example Defeats a General Claim](008000-counterexamples-and-failed-proofs.md) | Universal statements and implication |
| 009000 | [Sets and Subsets: Proving Two Collections Are Equal](009000-set-membership-and-identities.md) | Logic and quantified definitions |
| 010000 | [Functions: Images, Preimages, Injections, and Inverses](010000-functions-and-inverse-images.md) | Sets, quantifiers, and basic algebra |
| 011000 | [Equivalence Relations: Building New Objects by Identifying Old Ones](011000-equivalence-relations-and-quotients.md) | Sets and functions |
| 012000 | [Induction: Why Proving One Step Can Prove Infinitely Many](012000-mathematical-induction.md) | Natural numbers, algebra, implications |
| 013000 | [Strong Induction, Recursion, and Well-Ordering](013000-well-ordering-recursion-invariants.md) | Mathematical induction and divisibility |
| 014000 | [Countable and Uncountable: Comparing Infinite Sets](014000-countability-and-diagonal-arguments.md) | Functions and injections |
| 015000 | [Existence, Uniqueness, and Constructive Descriptions](015000-existence-uniqueness-and-well-definedness.md) | Quantifiers, functions, and direct proofs |
| 016000 | [Epsilon Proofs for Sequences: Making Eventually Precise](016000-epsilon-n-sequence-proofs.md) | Real numbers, inequalities, quantifiers |
| 017000 | [Epsilon-Delta Proofs: Controlling a Function Near a Point](017000-epsilon-delta-continuity.md) | Sequences and basic algebra |
| 018000 | [Compactness and Subsequence Proofs: From Infinity to Finite Control](018000-compactness-subsequences-and-structure.md) | Sequence limits, completeness, and elementary sets |

## Connections to existing mathematics lectures

| IDs | Tools established | Needed later |
|---|---|---|
| 001000-004000 | Theorem statements, implication, quantifier scope, definitions | All mathematics tracks; Logic/Types 001000-003000 |
| 005000-008000 | Direct, contrapositive, cases, contradiction, counterexample | Abstract Algebra; Discrete Mathematics; Analysis |
| 009000-011000 | Set reasoning, functions and preimages, equivalence classes | Topology/Geometry; Category Theory; Linear Algebra 015000 |
| 012000-014000 | Induction, recursion, well-ordering, infinite cardinality | Algorithms/Complexity; Discrete Mathematics; Logic/Types 004000 |
| 015000 | Existence, uniqueness, and well-definedness | Differential Equations; Linear Algebra; quotient constructions |
| 016000-018000 | Precise convergence, continuity, compactness proofs | Analysis 001000-010000; Multivariable Calculus 002000-004000 |

## How to use this track

The main listening sequence has no exercises or sources embedded as raw notation; the exact formal statements, diagrams in words, and exercise answers are in non-spoken companions. In advanced lectures, refer to the relevant IDs as prerequisites without requiring every learner to finish the entire track. For formal proof assistants, proceed afterward to `tts-logic-types` (its first lectures start from the proposition-as-type correspondence).

## Evidence and attribution

The lecture texts and examples are freshly authored explanations of established mathematics. Their reference metadata records independent sources: Richard Hammack, MIT OpenCourseWare, *forall x: Calgary*, *Mathematics in Lean*, and Wikipedia topic links. No textbook passages were copied. The spoken section is isolated by `BEGIN SPOKEN LECTURE` / `END SPOKEN LECTURE` markers; all bibliographic records are in `metadata/sources.json` and the corresponding per-lecture metadata.
