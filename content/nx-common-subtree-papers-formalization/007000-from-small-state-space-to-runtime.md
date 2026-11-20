# From a Small State Space to a Running-Time Theorem

<!-- BEGIN SPOKEN LECTURE -->

We have a correct three-branch recurrence for the maximum common embedded ordered subtree, and we know that its arguments belong to a controlled collection of balanced-word states. Is that enough to say that the algorithm runs in polynomial time? The answer depends on what the program does to represent, look up, and combine those states.

There is a mathematical theorem about the number of distinct states. There is a theorem about the number of recursive calls made by a memoized evaluator. There is a theorem about how much work each call requires under a specified representation. And there is the actual program a computer runs. Each step can be rigorous, but they are different claims. Lozano and Valiente's Theorem 3 joins the first three under a particular expected-time dictionary model. The Lean repository establishes several parts of the chain and leaves other representation and resource costs open.

This lecture derives the paper's headline complexity, then examines exactly which parts correspond to proved operations in the uploaded formalization. The point is to learn how a theoretical running-time proof is constructed, not to judge an implementation by whether its benchmark happens to look fast.

## How many distinct questions can the dynamic program ask?

Suppose the first input tree has n-one edges and the second has n-two edges. For each, let depth mean the maximum number of vertices on a root-to-leaf path, and let leaves mean the actual number of leaves. Define m-one to be the smaller of the first tree's depth and leaf count; define m-two analogously.

Theorem 1 says that the decomposition family of the first tree has no more than n-one times one plus m-one, plus one states. The second family has the analogous bound. A dynamic-program state consists of a pair, one left word and one right word, so the number of distinct possible questions is at most the product of those two bounds.

For large nontrivial trees, this is on the order of n-one times m-one times n-two times m-two. In the paper's notation, the headline is proportional to the product of the two input sizes and the two minima of depth and leaf count. The exact plus-ones handle small trees; we should not let asymptotic notation erase a single-vertex tree, whose balanced word is empty and whose valid optimum has zero edges.

Notice the asymmetry built into the state product. One tree could be a long path with one leaf, and the other could be bushy. The minimum is computed separately for each tree. It is not the minimum of the two trees' depths or the minimum of their numbers of leaves taken globally.

To see what the minimum buys us, consider a path of n edges. Its depth measured in vertices is n plus one, but it has one leaf. The bound on its decomposition states is therefore linear in n. Now consider a star of n edges. It has n leaves but depth two, so its bound is also linear. Trees with intermediate branching and nesting can have larger state families, and the formula permits that. We have a shape-sensitive estimate rather than a generic claim that every tree has the same quadratic state count.

## Four child requests and one stored result

Recall Lemma 8. The maximum common edge count for two nonempty words is the maximum of three candidates. The retain-first-pair candidate needs the answer for the two heads and the answer for the two tails. The contract-left candidate needs one answer, and the contract-right candidate needs one. Four child requests are made at most when a previously uncomputed pair is expanded.

A memo evaluator first looks for the current pair in its table. If it finds the value, it returns immediately. If not, it computes the child values and stores its own value. Each distinct pair can cause at most one miss if the table is threaded consistently and entries never need to be recomputed. There are at most B distinct pairs, where B is the product of the two decomposition cardinalities.

So there are at most B misses. A computation that expands each missed pair into no more than four child requests makes at most four B plus one calls, including the initial call. This is a counting argument about a recursion tree whose genuinely expanding nodes are bounded by B. It gives an explicit linear relationship between dynamic-program calls and the number of distinct states.

The supplied Lean source has this theorem. In `MemoizedDynamicProgram.lean`, `memoLcs_operation_bound` proves the miss and call counts for an actual, recursively defined memo evaluator. `memoLcs_tree_operation_bound` substitutes the independently proved tree-state cardinality estimates. That is stronger evidence than a recurrence written on paper and described as memoized: the proof is attached to a particular functional evaluator whose cache is threaded through the calls.

But an invocation of a function is not automatically a unit of machine time. If the evaluator searches a long list for a key, the cost of one call depends on the table's size. If it copies a long balanced word while constructing a new key, the cost of the requested operation depends on the word's length. Counting calls is a beginning, not a finished implementation-level time theorem.

## The paper's representation strategy

The paper recognizes the need to turn balanced words into table positions. It proposes enumerating the decomposition families and assigning unique codes to their members, maintaining a dictionary that identifies words already encountered. Once the states of both input trees have codes, an ordered pair of codes can serve as an index into a two-dimensional array containing the optimum value for that pair.

With those codes in hand, an array lookup and update are constant-time operations in the paper's abstract model. When a state is expanded, its head, tail, and first-contracted state are known as other members of the decomposition family. The recurrence can use their codes. A state is computed once, and a constant number of table accesses is used per state.

Why does the paper say expected time? It relies on dictionary operations such as looking up an already assigned code and inserting a new code, with expected constant cost using standard hashing. The proof treats those operations as primitive expected constant-time steps. This is an algorithmic assumption about how the canonical representation is constructed and accessed, not a purely combinatorial property of ordered trees.

The authors also discuss using unique identifiers for balanced sequences, including an approach based on equivalence classes of restricted subtree isomorphism. That is a distinct task from taking the balanced word `001011` and naively hashing every character each time it appears. The time needed to obtain and use identifiers is part of the implementation story. With suitable interning and dictionary assumptions, their proposed state enumeration can be charged to the number of states.

We should keep the word expected attached to the bound. Expected constant-time hashing says something about average behavior under a hash or dictionary model. It does not say that every individual lookup or every maliciously chosen collision pattern is constant-time in the worst case. Nor does it mean that ordinary full-string hashing is automatically free.

## Assemble Theorem 3

Let B-one and B-two denote the sizes of the two decomposition families. The expected work of assigning identifiers is proportional to B-one plus B-two in the paper's model, once its representation assumptions are satisfied. The table of possible state pairs has at most B-one times B-two entries. Since each entry is expanded once and each expansion performs a constant number of coded-state operations, the dynamic program requires work proportional to B-one times B-two.

Because both state families contain at least one member, the sum of their sizes is bounded by a constant multiple of their product. So the product term dominates the enumeration term. Substitute the depth-and-leaf bound for each family. The result is the paper's claimed expected running time: proportional to the product of the input sizes, multiplied by the minimum of depth and leaf count for the first tree, multiplied by the corresponding minimum for the second.

This derivation explains each factor. The input sizes count how many structural positions could contribute states. The depth-or-leaf minima come from bounding the auxiliary S family. The multiplication between trees comes from taking pairs of states. The constant-time work per pair is the representation and dictionary assumption. None of those factors was obtained by silently assuming that contracting every possible edge subset is easy.

The paper's theorem is also about an ordered-tree problem. Applying this formula to the 2016 unordered weighted isomorphism paper or the 2018 weighted topological embedding paper would be an error. Those papers have different feasible witnesses and different central subroutines, especially weighted matching. The common-subtree label does not permit transferring an asymptotic bound across problem definitions.

## A concrete state budget

Return to the balanced word 00011101, the four-edge tree we used in the decomposition lecture. Its D family has six distinct words. Comparing that tree to itself gives at most six times six, or thirty-six, distinct memo keys for this decomposition scheme. Theorem 1 independently gives an upper bound of thirteen states on each side, hence one hundred sixty-nine possible keys. The latter is conservative but guaranteed by the structural parameters. The exact enumeration tightens it for this particular input.

The abstract call bound becomes at most four times thirty-six plus one, or one hundred forty-five calls, when we use the actual state-family cardinality. That is a bound, not a prediction of the number of calls on this input. If we use the weaker Theorem 1 bound without enumerating states, the corresponding call bound is four times one hundred sixty-nine plus one, or six hundred seventy-seven.

A run with a memo table of thirty-six keys could still do more than thirty-six elementary comparisons. Indeed, if it stores key-value pairs in an unsorted linked list and searches from the front every time, a single lookup may scan much of the list. Our arithmetic has so far counted key requests, not their internal search costs.

## The actual association-list reference

That difference is explicit in the Lean source. Its `memoLcs` reference computation uses a list of key-value entries. The implementation carries counts for calls, cache misses, and comparisons. The theorem `memoLcs_table_bound` says the final table length is no greater than B-one times B-two. The operation bound then limits calls in terms of the same product.

A separate theorem, `memoLcs_comparison_state_bound`, proves that comparisons in the association-list implementation are bounded by the product of two quantities: approximately four B plus one calls, and B possible entries in the list. That is quadratic in B as an upper bound. It does not satisfy the paper's hoped-for constant-time lookup model simply by being memoized.

This is not a failure of the recurrence or the mathematical state theorem. It is a deliberate separation between a reference evaluator that is easy to specify and an efficient dictionary-backed evaluator. The reference can be proved correct and have a fully stated comparison bound even if it is not the final asymptotically optimal implementation.

The broader repository also contains Rust implementations and additional source and resource proofs. Some concrete, actual-source paths are proved to preserve the optimal ordered result, and the proof campaign has extensive work on memoized evaluation. But the crosswalk for Theorem 3 still lists structural word handling, expected hashing, and full implementation cost refinement as open. We should be precise about this: the source snapshot contains substantial proved functional and operation-count results; it does not claim an end-to-end expected-time theorem for the optimized application implementation.

## What must be charged to make a machine-level claim?

Suppose we give each balanced word a canonical integer identifier. Can we create the identifier for a new state in constant time? Not necessarily. It may take work to find its structural children, construct a concatenation, compare it for equality, or compute a hash. If two equal words appear in different memory locations, pointer comparison alone may not establish they represent the same state. We must either use a canonical representation or account for the extra structural test.

Suppose the DP table is an array indexed by pairs of integers. Is it dense enough to allocate B-one times B-two entries? If yes, we should count the space required, initialization, and the bounds of the indices. If instead we use a sparse dictionary, we need a cost model for its lookups and insertions. If the function returns a witness rather than just a numeric maximum, we also need to account for recording choices and reconstructing the original edge identities. A compact shape-only cache can lose the information needed to say which original nodes were matched.

Suppose the implementation uses fixed-width integers for indices and edge counts. Then the mathematical inequality that an edge count is nonnegative does not guarantee the machine addition cannot overflow. A source-level proof has to say whether the operation is checked, whether an overflow case is possible, and which preconditions eliminate it. These requirements are distinct from the paper's abstract complexity proof but central to proving real code correct.

For actual memory consumption, even a bound on the number of cache records is insufficient if each record owns dynamically allocated words. The size of a record depends on what the record contains. Peak allocation can include intermediate concatenations, hash buckets, retained lookup keys, and reconstruction data. Proving a polynomial bound on the number of states does not by itself prove that a particular program uses memory proportional to that state count.

## A formalization reading exercise

The progression through the uploaded Lean repository is unusually instructive because the tiers of assurance are explicit.

Start with `decomposition_card_bound` in `Paper2004/TreeStateBounds.lean`. Its input is an independently defined ordered tree. Its conclusion is a finite-set bound in the tree's edge count, depth, and actual leaf count. There is no cache in the statement and no machine-time conclusion. This is the combinatorial foundation.

Then find `paperLcs_optimum` in `Paper2004/DynamicProgram.lean`. Its claim is that the numeric recurrence agrees with the maximum over independent common contraction witnesses. It gives correctness of the value, not a call count.

Next read `memoLcs_optimum` and `memoLcs_operation_bound` in `Paper2004/MemoizedDynamicProgram.lean`. One establishes that the memoized evaluator computes the same optimum, and the other bounds its actual calls and misses. Finally read `memoLcs_comparison_state_bound`, which accounts for the concrete list lookup implementation rather than crediting it with imaginary constant-time searches.

At each step, ask which representation is fixed by the theorem statement. Is the object a tree, a balanced word, a numerical result, a list-based cache, or a translated source program? When the representation changes, identify the theorem that connects the two. A performance claim without such a bridge may still be a useful design hypothesis, but it is not a proved property of the code.

## What a completed proof would add

A complete source-level analogue of Theorem 3 would identify the exact fast solver, its input representation, its memo and identifier operations, and a cost measure under which the running time can be bounded. If the desired bound is expected rather than deterministic, it would also identify the randomness or hash-table assumptions under which that expectation is evaluated. The proof would compose the already established state bound, the recurrence correctness, and the actual per-operation costs of the chosen implementation.

That does not require abandoning the proofs already present. It requires finishing the bridge between them. The great value of the 2004 argument is that its mathematical core is now understood at three levels: what an optimal common contraction is, why the three-branch recurrence finds it, and why only a bounded set of distinct subproblems is needed. Those are substantial results, and they leave us with a sharply defined question for the engineering formalization: does the actual fast program implement those operations at the costs the paper assumed?

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: exact complexity scopes

Let `n_i = |E(T_i)|`, `d_i` be **vertex** depth, `ℓ_i` the actual number of leaves, and

\[
B_i = |D(E(T_i))| \le n_i\bigl(1+\min(d_i,\ell_i)\bigr)+1,\qquad B=B_1B_2.
\]

With the three-branch/four-child recurrence and a correctly threaded memo:

\[
\text{distinct misses}\le B,\qquad \text{calls}\le 4B+1.
\]

The paper's expected dictionary/identifier and indexed-array model supports

\[
O(B_1+B_2+B_1B_2)=O(B_1B_2)
  =O\!\left(N_1N_2\min(d_1,\ell_1)\min(d_2,\ell_2)\right),
\]

where `N_i` is the number of vertices, with nontrivial-input conventions and constants absorbed in the final asymptotic expression. Expected constant-time dictionary access is an *implementation assumption*, not a consequence of finite-state counting.

### Comparison with actual reference memo costs

For the **association-list** memo evaluator in the Lean snapshot:

\[
\begin{aligned}
\operatorname{tableLength} &\le B,\\
\operatorname{misses}&\le B,\\
\operatorname{calls}&\le 4B+1,\\
\operatorname{comparisons}&\le (4B+1)B.
\end{aligned}
\]

The comparison bound counts key comparisons for list scans; it is not a byte-accurate cost for comparing entire structural words. Theorem 3's expected time needs canonical coding, word construction/equality, dictionary and array costs to be realized in the chosen implementation.

### Worked example

For `T` encoded by `00011101`, `D(T)` has 6 words while the general structural bound is 13. For `(T,T)`:

- **actual possible key domain:** at most `6×6=36` pairs; thus at most `4×36+1=145` calls,
- **coarse parameter bound:** at most `13×13=169` pairs and at most `677` calls.

Neither number asserts the actual observed call count.

### Reading specific source theorems

- `proofs/SubtreeProofs/Paper2004/TreeStateBounds.lean`: `decomposition_card_bound` — a bound on *mathematical* decomposition states.
- `proofs/SubtreeProofs/Paper2004/DynamicProgram.lean`: `paperLcs_optimum` — numeric recurrence returns independently defined optimum.
- `proofs/SubtreeProofs/Paper2004/MemoizedDynamicProgram.lean`: `memoLcs_optimum`, `memoLcs_table_bound`, `memoLcs_operation_bound`, `memoLcs_tree_operation_bound`, `memoLcs_comparison_state_bound` — correctness and actual counted operations of the reference evaluator.
- `docs/planning/paper_statement_crosswalk.md`: the Theorem 3 row and explicitly open structural-cost, expected hashing and source-refinement frontier.
- `proofs/PROOF_STATUS.md`: more recent proof campaign status from the supplied snapshot. Do not interpret a mathematical call bound as a fully closed optimized-source cost theorem.

**Primary source:** [Lozano and Valiente (2004), Section 4, Theorem 3](https://www.cs.upc.edu/~antoni/subtree.pdf).

**Optional broader link:** `algorithms-computability-complexity:017000` (amortized analysis and cost accounting).
