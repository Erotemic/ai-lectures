# From Tree Proof to Original Tokens: Reading the Lean and Rust Verification Chain

<!-- BEGIN SPOKEN LECTURE -->

An algorithm that returns the number two has not yet told us which two edges were matched. And an algorithm that returns two pairs of indices has not yet shown that those indices belong to the original input, appear in the correct order, and actually describe the same contracted tree.

These differences are easy to ignore on paper, where a proof of an optimal score and a picture of a corresponding tree may appear side by side. In a working graph library, they are separate engineering obligations. The code must store representations, reconstruct choices, move between trees and balanced sequences, respect integer bounds, and hand the caller identities it can use. A proof of the mathematical recurrence settles only part of that work.

The Lean development accompanying the NetworkX common-subtree repository is an opportunity to watch the obligations being discharged in stages. It begins with an independent model of rooted ordered trees, proves that contracting edges is the same as deleting balanced-word pairs, proves that the recurrence finds a maximum, then refines a reference implementation through indexed witnesses to original Boolean token positions. We will read that route as a mathematician would read a chain of lemmas: at each link, identify the objects on either side, the invariant being transported, and what the theorem does *not* yet claim.

This is a reading guide to the repository snapshot supplied on November nineteenth, twenty twenty-six. It is not a claim that the optimized production backend or every Python adapter has been formally verified. Some actual Rust reference entry points have source-level proofs; other boundaries remain open.

## Start from the mathematical object, not the array

At the tree level, the formalization defines an inductive type called OrderedTree. Its sole constructor is node, carrying a list of child trees. A singleton is a node with the empty child list. A fork is a node with two singleton children. The ordering of this list is part of the object. Swapping its two children may not matter when they happen to be identical, but in general a left-right permutation is a different ordered tree.

The edge count is defined recursively. Every child contributes one edge connecting it to its parent, plus all edges inside that child. The vertex count is the edge count plus one because these trees always have a root. Depth counts root-to-leaf vertices, and a leaf is a vertex with an empty child list. These conventions are visible in the Lean definitions, instead of being left to the reader's intuition about whether an empty balanced word represents zero vertices or one.

The first relation is ContractStep. It is not defined in terms of strings, indices or dynamic programming. Its witness identifies an enclosing tree context, a list of siblings to the left, a chosen child, and a list of siblings to the right. The before-tree has that child between the two sibling lists; the after-tree has the chosen child's own children spliced between them. The context tells us where this change occurs below the original root.

A context is itself an inductively defined tree with one hole. It can be just the hole, meaning the contracted edge is incident to the root of the tree fragment under consideration. Or it can place the hole below an ancestor, with fixed siblings to either side. This is a convenient way to formalize the phrase 'at any depth.' We do not need to write a different contraction rule for every possible path from the root.

The theorem ContractStep dot edgeCount_decreases proves that a single contraction removes exactly one edge. You can understand its proof without knowing every tactic: the context contributes the same edges before and after, and replacing one child by that child's children removes precisely the incoming edge. The equation is not a heuristic measure of progress; it is a property of every witness to the step relation.

The reflexive and transitive closure of ContractStep is called Embeds. Here the arguments are written as small, large, in that order, although the underlying step runs from the large tree to the small one. A useful habit in reading such Lean definitions is to check the direction of the relation, not just its name. The same convention appears again for balanced words and indexed deletions.

Finally the independent specification IsMaximumCommon says two things. First, the candidate is obtainable by contractions from both inputs. Second, every other candidate obtainable from both has at most as many edges. The definition mentions no algorithm. That separation makes the later statement 'the program returns a maximum' meaningful.

## Replace the tree with a word, and prove nothing was lost

The next layer uses balanced words, known mathematically as Dyck words. An encoding traverses an ordered tree in left-to-right depth-first order, writing an opening symbol for each descent along an edge and a closing symbol for the return. Each edge contributes exactly one opening and one closing symbol. Encoding a singleton gives the empty word. Every balanced word decodes to an ordered tree by attaching an implicit root to its decoded forest.

It is not enough to show that encoding a tree gives a balanced word. The proof also needs to know whether distinct trees can collapse to the same word, and whether every balanced word represents a tree. The formalization proves both round-trip identities. Decode after encode gives the original tree. Encode after decode gives the original balanced word. These results justify transporting the problem across representations.

Try the smallest nontrivial example. A root with one child, which has two leaf children, encodes to 001011. The outer pair records the first edge and the interior 0101 records the two descendant edges. Decoding 001011 recovers that same rooted, ordered three-edge tree. If the two descendants had different subtrees, their order would likewise be recovered.

Now compare the contraction operations. The tree relation allows contracting an edge anywhere inside a tree context. The word relation allows deleting one matched pair anywhere inside a balanced-word context. A word context has a hole surrounded by balanced siblings or nested inside another pair. The two kinds of context express the same structural freedom in different syntaxes.

The forward theorem, embeds_encodeDyck, converts a sequence of actual tree contractions into a sequence of actual word-pair deletions. The reverse theorem, dyckEmbeds_decodeDyck, converts each word deletion into a real tree contraction. Combining these with the encoding round trips gives embeds_iff_dyckEmbeds.

Read that if-and-only-if as two separate promises. If an algorithm returns a word obtained by valid pair deletions, the decoded tree is feasible. And if a tree is a valid contraction, its word lies in the operational deletion relation. The first direction is soundness; the second is completeness. Completeness is important because an optimization algorithm that silently overlooks some legal contractions can return a feasible but nonmaximum answer.

The printed Definition 2 of the 2004 paper is kept in a different Lean type, PrintedContains. Its recursive clauses omit some nested single-pair deletions. The bridge we just described uses the corrected operational DyckEmbeds relation. That explicit choice keeps the correctness theorem tied to the problem the paper intends to solve.

## Now earn the word 'maximum'

At this point the proof can specify the longest common balanced word independently of an algorithm. Such a word must be operationally obtainable from each input, and no larger feasible common word may exist. Theorem 2's formal counterpart, isMaximumCommon_iff_isLongestCommonBalanced, says that maximum common contraction of trees and maximum common operational balanced word are equivalent under encoding. The theorem longestCommonBalanced_decodes_maximum packages the direction needed to decode a best word into a best tree.

The paper's Lemma 8 introduces a way to compute that word. Split each nonempty input into its first enclosing pair, the interior of that pair, and the following tail. There are three possibilities for an optimal common result: retain the first pair on both sides, contract the first pair on the left, or contract the first pair on the right. In the first case, the interiors and tails become independent common-contraction problems. In the other cases, the affected input loses its first pair and the recurrence continues.

The Lean definition paperCommon actually returns a balanced word. That is stronger than calculating a score with no witness. Its termination measure is the sum of the two input semilengths, which decreases in every recursive branch. The proof paperCommon_sound shows the returned word is feasible in both inputs. The proof paperCommon_upper shows every independently feasible common candidate is no larger than it. Together they yield paperCommon_correct.

Notice how the two proof directions match the mathematics. One tells us we have not fabricated a word that cannot be contracted from the originals. The other tells us we have not left out a larger possibility. Both are required for an optimum.

The theorem paperCommon_tree_correct then connects the word witness back to IsMaximumCommon for trees. Separately, paperLcs is a numeric recursive calculation. The theorem paperLcs_optimum proves its number agrees with the independent optimal score. There is no need to identify a numerical implementation with a constructive word implementation by definition. Their agreement is proven.

A useful way to read these theorem statements is to find the moment when the independent specification appears. Look for IsMaximumCommon or the independently defined feasible-word relation. If you see only an equation between two recursive functions, you may be looking at a local computation lemma. If you see a proof relating the function's result to a universally quantified maximum over all feasible candidates, you have reached a semantic correctness theorem.

## Memoization changes the program, not the objective

The direct recurrence is a clear specification of an algorithm, but repeatedly evaluating the same states is inefficient. The source development therefore includes a memoized numeric evaluator. In the Lean model, a memo key is a pair of balanced words. A memo table is a list of key-value pairs, and a run records the result and counts associated with the evaluation.

The table is intended to cache the same optimum for each key that the independent mathematics assigns. The invariant MemoSound says its stored entries are correct. The correctness proof shows a table satisfying that invariant remains sound after a run and yields the same answer. Additional lemmas show that fresh keys belong to the decomposition-product domain, that keys are not inserted twice, and that counts of actual calls are bounded by the number of misses.

This is where a formal proof of a running program starts to look different from a mathematical proof of a recurrence. It has to track state threaded through calls, account for cache hits and misses, and show that an updated memo remains valid. The paper's mathematical state bound is a crucial ingredient, but the proof also needs operational facts about the evaluator.

There is a subtle limitation. The checked memo representation is an association list. Searching it can require scanning earlier entries. The proof of the reference evaluator's key-comparison bound therefore has an extra factor corresponding to the table size. And the counted comparisons do not themselves measure the byte cost of comparing large structural words. Thus proving that the number of memo states is polynomial is not yet the same as proving the paper's optimized expected-time bound for an actual source implementation.

We also have a witness problem. A memoized score of two may tell us the optimum edge count but not which original two edges achieved it. To serve a graph library, the algorithm must reconstruct a choice and relate it to the original input, where identities have not been forgotten.

## Shape is not identity

Consider our three-edge example, 001011. Give each matched edge pair an identity in opening order: pair zero is the outer R-to-A edge; pair one is the first descendant edge; pair two is the second descendant edge. These identities are not token offsets. They enumerate edges or matched pairs, once each.

Suppose the output keeps the outer edge and the first descendant edge. Its shape is 0011. If we forget the original labels, that shape could also be produced from another occurrence of a two-edge path elsewhere in a larger tree. A proof about the final shape cannot, by itself, tell us which original edges were retained.

The formalization introduces an indexed word: a binary-tree-shaped representation whose nodes carry natural-number pair identities. Erasing those identities returns the unindexed balanced word. A canonical numbering assigns zero-based pair IDs in opening, or preorder, order. The equation canonical_indices says the original indices are exactly the range from zero to one less than the input edge count.

Now define a new operational relation directly on indexed words. Its Step removes an indexed pair and retains its indexed interior and tail, in their existing order. Its reflexive/transitive closure is Retains. This is not defined by calling an optimizer and checking what it returned. It is an independent feasibility relation for witnesses with identities.

The key invariant is straightforward but powerful: deletion never invents an index, never duplicates an index and never reorders the surviving indices. The theorem Retains.indices_sublist says that the list of indices in the retained word is a sublist of the list of indices in the original. A sublist is stronger than an arbitrary subset. It preserves order, which is essential when the tree is ordered.

From this, the theory derives distinctness and bounds. If the original canonical list is zero, one, two, through the edge count minus one, any retained list has unique indices lying within that range. Erasing the indexed witness gives a valid operational Dyck contraction, and decoding gives a valid tree contraction.

But we still need optimality. The independent specification IndexedMaximum requires two indexed witnesses, one retained from the canonical left original and one from the canonical right original. Their erased words must have the same shape. That decoded shape must be an independent maximum common embedded tree. Finally, the recorded score must equal its true edge count. This definition combines feasibility, agreement, optimality and score accounting, while leaving the solver completely unnamed.

That is a good theorem interface for a reconstruction function. The function can change its internal data structures as long as it continues to satisfy IndexedMaximum.

## From edge identities to token positions

There is another index space. The flat token word 001011 has six token positions, numbered zero through five. Its three matched pairs occupy positions zero and five, one and two, and three and four, respectively. Pair identity zero therefore corresponds to two token offsets, not to token offset zero alone.

If we retain pair identities zero and one, the output token positions are zero, one, two and five, in that order. Reading those positions from the original six tokens yields 0011. The list has four entries because the result contains two matched pairs, each with two actual symbols.

This is precisely the issue handled by the token layer. In the formalization's Boolean encoding, false is an opening token and true is a closing token. A function called positionPairs computes the original opening and closing coordinates of every pair. The indexed witness then expands its retained pair identities through those coordinates, outputting the opening token, recursively outputting the interior, outputting the closing token, and continuing through the tail.

The resulting list of token coordinates must be increasing in original token order. It must be free of duplicates and within input bounds. Most importantly, reading the original array at those coordinates must produce exactly the balanced word described by the indexed witness. A mere in-bounds check would not prove that the opening and closing tokens still match, nor that the two inputs spell the same final shape.

The independent contract MaximumTokenEmbedding states all of those conditions together. It says both input token lists encode balanced words; the returned index lists are sublists of the respective original token ranges; reading those positions from the originals spells one common balanced word; the decoded common word is globally optimum for the original tree-contraction problem; and the reported score equals its number of pairs.

There is also a simple useful consequence. If the score is k, each output index list has exactly two k entries. If a function returned a score of three but only five token positions, it could not satisfy this contract. The formalization proves the length relation rather than trusting an emitter to get it right.

## An actual Rust reference endpoint enters the picture

Up to this point we have discussed independent mathematical definitions and algorithms modeled in Lean. The repository also contains Rust source and a translation/verification pipeline, using Aeneas-style translated source models. Those results should be named precisely, because 'the Rust is verified' would conceal crucial boundaries.

The Rust ordered-core crate contains an indexed reference function, maximum_common_embedding_indexed. It calls a shape solver, numbers both original inputs, reconstructs a retained indexed witness in each one, and returns the witnesses and the edge score. The theorem maximum_common_embedding_indexed_of_trees proves that for independently specified ordered trees with fewer than two to the thirty-second power edges each, the actual public indexed Rust entry point succeeds and returns a result satisfying IndexedMaximum. The proof composes the established shape optimum, the canonical-numbering correspondence and the actual reconstruction proofs. Separate consequences state that the returned original pair indices are unique, genuine and in bounds.

The token adapter goes further. The Rust function maximum_common_token_embedding accepts two slices of Boolean tokens. It parses them, runs an indexed guided reconstruction solver, and emits original token offsets for both sides. A theorem called maximum_common_token_embedding_total_spec covers every represented pair of inputs: either they are admitted balanced inputs under the pair-count bound and the function returns a maximum with the stated readback contract, or it reports the appropriate rejected input side. The left input has error precedence when both inputs are invalid. The source-level proof also rules out internal solver or index errors on admitted inputs.

Why does this count as a meaningful source refinement rather than a second abstract reimplementation? The source proofs refer to translated Rust functions, including the parser, the indexed solver and the emitter, and show that their executions satisfy an independently stated mathematical predicate. The proof cannot assume an optimum witness is magically supplied at the input boundary. The program must compute or reconstruct it, and the theorem must account for that success.

This is a substantial level of assurance for the reference Boolean-token path. It has a clear scope: rooted ordered trees represented by flat balanced Boolean tokens, unweighted edge counts, bounded pair identities, the stated parser/error behavior, and original token-coordinate witnesses. It is not a proof that an optimized default NetworkX backend implements the same algorithm in the paper's claimed running time.

## Four gaps you should not collapse into one

The first gap is between *reference* and *optimized*. The indexed/token reference path has proven correctness results, but reconstructing a witness can use backtracking. The finite state-count result for the score recurrence does not by itself establish a polynomial running-time bound for that reconstruction. The paper's Theorem 3 is a separate resource claim, and the source-level dictionary, structural-word, allocation and comparison costs still need appropriate models and bounds.

The second gap is between *tokens* and *external graph objects*. The verified Boolean token offsets refer to the original token arrays. They are not yet a formal correctness theorem for a Python NetworkX graph's arbitrary hashable vertex objects, and they are not the same thing as edge or pair identities. A bridge into the public Python API must establish that serialization from original graph nodes and decoding of returned choices preserve the intended graph witness and the documented error behavior. The repository reports tests and backend integration in this area, but distinguishes them from a source-level proof of the complete Python/PyO3 boundary.

The third gap is between *edge contraction* and *strict subtree isomorphism*. The repository also develops ordered-isomorphism solvers. They use a different relation: skipping a child does not promote that child's grandchildren. Edge contraction can promote descendants. Some indexed and token machinery is shared, and parts of the isomorphism reference path have their own proofs. But substituting a strict-isomorphism theorem for an embedding theorem would change the optimization problem. The two contracts must stay separate.

The fourth gap is between *exact mathematical values* and *machine arithmetic*. For the unweighted 2004 problem, the score is a natural number of edges and the reference implementation has explicit unsigned integer bounds. For weighted extensions, the project also considers exact integer or rational scores and floating-point production behavior. A proof for exact arithmetic does not automatically certify IEEE floating-point computation, tie behavior or every extension's affinity score.

There are many Lean modules because those boundaries are real. A file proving the correctness of a reconstruction helper has a narrower job than a theorem saying every accepted pair of Python graphs returns an independently maximum common weighted graph. The small, compositional theorems are how one could eventually support the larger claim.

## How to read one source theorem without drowning in tactics

Open IndexedOrderedEntrypoint dot lean and find maximum_common_embedding_indexed_of_trees. Do not begin by interpreting every tactic in its dependencies. Begin with the theorem's inputs: two independently specified ordered trees, and an edge-count bound for each. The conclusion says there exists a result that the actual indexed Rust call returns successfully, and that the result satisfies IndexedMaximum for the original trees.

Then open CanonicalIndexedWord dot lean and read the definition of IndexedMaximum. Expand its clauses in ordinary language. Each witness is retained from the canonically indexed original; both erasures have the same shape; the decoded shape is a maximum common tree under the independent tree-contraction relation; and the returned score is exact. That one definition tells you what the endpoint theorem guarantees without requiring you to inspect all of its internal proof tactics.

Next find the numbered-model-canonical bridge. It prevents a dangerous proof gap: having some numbered tree that looks plausible is not enough. The indices must refer to the *specific original input*. Then follow the reconstruction-success lemmas, whose role is to show that the computed shape can be realized as a retained indexed witness on each original side.

Only after you understand that proof shape should you descend into the implementation proof of a reconstruction helper, or into the details of the translated Rust result type. If you want to understand the flat token endpoint, repeat the same exercise with MaximumTokenEmbedding and maximum_common_token_embedding_total_spec. Start from the independent contract, then find the parser, guided indexed solver and token-emitter subproofs that make the contract true.

The Lean syntax becomes easier when every theorem has a clear job. An existential witness says something concrete must be produced. A conjunction says several guarantees must all hold. A reflexive-transitive closure means zero or more certified steps. A sublist says original order survives. A universally quantified competing candidate is the signature of global optimality. A size hypothesis identifies the actual machine-domain boundary. These are mathematical ideas expressed in a proof assistant, not arbitrary formal incantations.

## What would taking this formalization further look like?

One productive next task would be to identify the optimized ordered solver's exact mathematical entry point and prove that its returned shape, witness choices and original indices satisfy the same independent contract as the reference solver. We would need a refinement from the fast memo and choice representations to the indexed witness relation, not just a comparison of scores on small examples. If the optimized algorithm already has strong helper proofs, the remaining goal may be composition; if a choice can lose original identity, that invariant must be established first.

A separate task would be a formal resource theorem. Choose the actual optimized solver and an explicit cost model. Connect the number of distinct decomposition-product states to the work needed to construct and identify keys, compare or hash words, access the memo table, and reconstruct the answer. If the target is an expected-time theorem, specify the dictionary assumptions supporting expectation. If a deterministic bound is preferred, state the cost of that chosen data structure. The number of mathematical states alone does not settle either question.

A third task would be to carry original pair or token witnesses through the remaining Python/NetworkX conversion boundary. The specification should quantify over the graph or ordered-tree objects users actually submit and should state the exact relationship between returned node or edge identities and the input. This is also where an independently tested adapter becomes a formally proved one.

The repository's status ledger identifies these as open or partially open in the supplied snapshot. It also records substantial achievements for the reference path. There is no advantage in calling them all complete, and no advantage in pretending the already proved parts have no value. The right unit of progress is an implication with explicitly named assumptions and outputs.

We can now see the whole 2004 route. Define actual contractions on ordered trees. Encode them as matched-pair deletions, with a two-way theorem. Prove the recurrence correct for the independent optimum. Carry its shape into indexed witnesses that retain original pair identities. Carry those identities into original token coordinates with exact readback. Prove that actual Rust reference entry points perform the promised computation on their admitted domain. And finally, keep the optimized runtime, production API and remaining representation bridges as explicit next questions.

Understanding that route is what makes formalization useful for research. It tells us not merely whether a theorem has a check mark, but which bridge to build next, what statement that bridge must establish, and what evidence would count as completing it.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: the proof-reading chain

The terminology, declarations, and proof statuses below refer to the supplied `networkx_algo_common_subtree` snapshot of 2026-11-19. File paths are relative to that source repository.

### 1. Independent tree and word specifications

```lean
-- Sketches of exact signature shapes, simplified only in notation:
inductive OrderedTree where
  | node : List OrderedTree → OrderedTree

-- One step has an explicit enclosing context and selected edge.
def ContractStep (before after : OrderedTree) : Prop := ...

-- The argument order is (small, large); step order is (large, small).
def Embeds (small large : OrderedTree) : Prop :=
  Relation.ReflTransGen ContractStep large small

def IsMaximumCommon (candidate left right : OrderedTree) : Prop :=
  CommonEmbedding candidate left right ∧
    ∀ other, CommonEmbedding other left right →
      edgeCount other ≤ edgeCount candidate
```

`proofs/SubtreeProofs/Paper2004/OrderedTree.lean` is independent of the solver. `ContractionSoundness.lean` defines `DyckContractStep` and `DyckEmbeds`; `ContractionCompleteness.lean` proves:

\[
\operatorname{Embeds}(S,T)
\quad\longleftrightarrow\quad
\operatorname{DyckEmbeds}(\operatorname{encodeDyck}(S),\operatorname{encodeDyck}(T)).
\]

`EncodingEquivalence.lean` proves both `decodeDyck_encodeDyck` and `encodeDyck_decodeDyck`.

### 2. Independent optimum and recurrence

`OptimalEncoding.lean`: `isMaximumCommon_iff_isLongestCommonBalanced`, `longestCommonBalanced_decodes_maximum`.

`DynamicProgram.lean`: `paperCommon` returns a witness, with termination measure `left.semilength + right.semilength`. The proof splits into `paperCommon_sound` (feasibility) and `paperCommon_upper` (optimality upper bound); then `paperCommon_correct`, `paperCommon_tree_correct`, and `paperLcs_optimum` for an independent numerical computation.

`MemoizedDynamicProgram.lean`: `MemoSound`, `memoLcs_correct`, `memoLcs_nodup`, `memoLcs_new_keys`, `memoLcs_counts`, `memoLcs_operation_bound`, `memoLcs_comparison_state_bound`. This reference memo uses a list, so key comparisons incur an extra state-size factor. No full Theorem 3 source-cost theorem follows from these lemmas alone.

### 3. Original pair identities

`IndexedWord.lean`: `Word := BinaryTree Nat`, `erase`, `indices`, `Step`, `Retains`, `Retains.indices_sublist`, `Retains.erase_embeds`.

`CanonicalIndexedWord.lean`:

```lean
def IndexedMaximum
    (left right : OrderedTree)
    (leftWitness rightWitness : Word) (score : Nat) : Prop :=
  Retains leftWitness (canonical left) ∧
  Retains rightWitness (canonical right) ∧
  erase leftWitness = erase rightWitness ∧
  IsMaximumCommon (decodeDyck (erase leftWitness)) left right ∧
  score = (decodeDyck (erase leftWitness)).edgeCount
```

This is a requirement on exact original pair identities, not merely on the output score or shape.

### 4. Original flat-token positions

`TokenEncoding.lean`: Boolean alphabet `false = opening`, `true = closing`; `encoded`, `positionPairs`. `TokenMaximum.lean`: `MaximumTokenEmbedding`, `indexedMaximum_tokens`, `MaximumTokenEmbedding.lengths`, `MaximumTokenEmbedding.indices_valid`. `TokenReading.lean` and `CanonicalTokenPositions.lean` prove that readback uses original token coordinates in order.

**Worked coordinate example:**

```text
Original word:             0 0 1 0 1 1
Original token offsets:    0 1 2 3 4 5
Canonical pair identities: 0 1   2
Pair coordinates:          pair 0 -> (0,5)
                           pair 1 -> (1,2)
                           pair 2 -> (3,4)
Keep pair IDs:             [0,1]
Original token offsets:    [0,1,2,5]
Readback from original:    0011
Score:                     2 edges = 4 retained tokens
```

In particular, **pair IDs** and **token offsets** are two different coordinate systems.

### 5. Actual verified Rust reference calls and boundaries

`rust/crates/verified_ordered_core/src/indexed.rs`:

- Source function `maximum_common_embedding_indexed` combines the shape optimum, canonical numbering and two reconstructions.
- `proofs/SubtreeProofs/Rust/IndexedOrderedEntrypoint.lean` proves `maximum_common_embedding_indexed_of_trees` and `maximum_common_embedding_indexed_indices` for inputs with fewer than \(2^{32}\) edges on each side.

`rust/crates/verified_ordered_core/src/token_matching.rs`:

- Source function `maximum_common_token_embedding` parses, solves with guided indexed reconstruction and emits token coordinates.
- `proofs/SubtreeProofs/Rust/TokenMatchingEntrypoint.lean` proves `maximum_common_token_embedding_spec` and `maximum_common_token_embedding_total_spec` against `MaximumTokenEmbedding`, including rejected-input behavior and left-input precedence.

**Scope of the latter theorem:** represented Boolean token slices; balanced and size-bounded inputs succeed; rejected inputs signal the appropriate side; returned original-coordinate lists read back a globally optimal common balanced contraction. The project separately tracks optimized production DP/witness refinement, source-level complexity, Python/PyO3 graph conversion and weighted extensions as open proof boundaries.

### Reading exercise

Without reading tactics, locate in the displayed `IndexedMaximum` definition: (a) feasibility on both input sides, (b) common shape, (c) global optimum, (d) exact score. Then find the size premise of `maximum_common_embedding_indexed_of_trees`. Finally compare that source endpoint with `maximum_common_token_embedding_total_spec`, which quantifies over all represented token slices and handles error cases explicitly.

**Primary references:** [Lozano & Valiente (2004)](https://www.cs.upc.edu/~antoni/subtree.pdf), `docs/planning/paper_statement_crosswalk.md`, `proofs/PROOF_STATUS.md`, `docs/planning/lozano_valiente_2004_containment_definition_audit.md` in the supplied repository.

**Optional refresher:** `logic-types:004000` through `008000` (inductive structures, rewriting, and what proof checking establishes).
