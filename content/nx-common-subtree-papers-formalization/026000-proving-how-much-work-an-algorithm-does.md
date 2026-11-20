# Proving How Much Work an Algorithm Does: Complexity in Lean

<!-- BEGIN SPOKEN LECTURE -->

Imagine that you have proved a dynamic program correct. Every possible input tree has a mathematically defined optimum, and a theorem says that the table produced by your evaluator contains exactly that optimum. Your implementation terminates, its output is right, and every dependency in its recurrence is justified. Now you would like to claim that it runs in time proportional to the product of the sizes of the two trees.

What, exactly, would you need to prove next?

Counting the possible table entries is a place to begin. It is not the end of the argument. A table entry might require solving a weighted bipartite matching problem. Looking up an entry might mean traversing a linked list. Building the key might copy a whole subtree. An implementation might compute an optimal answer just once and then spend longer copying the witnesses than it spent finding their score. And if the program uses a hash map, an expected-time statement has a hypothesis that a mathematical bound on the number of states cannot discharge.

There is a reason to distinguish all of these things. Our three common-subtree papers rely on the same general discipline of charging operations to some finite collection of combinatorial objects. Their methods are different, but a formal complexity proof must make the charged operation and the collection precise. The Lean repository contains useful, already checked examples. We will follow those examples, work a small trace by hand, and then examine the part of the proof that is still missing for the production solver.

## Four claims that sound like one

Suppose two trees have n and m vertices. A developer says: there are at most n times m vertex pairs, so the program takes time proportional to n times m. This compresses four claims into one sentence.

The first claim is a state-space bound: the algorithm has no more than n times m distinct states of the chosen form. The second is an execution bound: no state is expanded more than some number of times, ideally once. The third is a cost bound: expanding one state, including any matching or cache operations, has a known cost. The fourth is an aggregation bound: if the expansion costs depend on the vertex degrees, their sum across all states has the advertised order.

A proof of the first claim is valuable even when the other three have not been proved. But if a state can be recomputed exponentially many times, the first claim is compatible with exponential execution. If each state is expanded once but costs n time to find in a list, then a quadratic number of states can mean cubic or worse total work. If each state invokes a matching algorithm whose cost depends on both local degrees, the sum of those local costs needs an additional argument. Neither the number of states nor the correctness of their values settles that accounting.

A fifth claim appears when we leave an abstract algorithm and discuss a particular executable program. Does the source code actually implement the counted operations? Does the chosen memory representation have the lookup and update costs in the model? Does its numeric representation preserve the intended comparisons? Does it allocate only the counted objects, and is it safe under its size assumptions? A mathematical algorithm can satisfy a very good operation bound without an arbitrary Rust implementation of it satisfying the same bound.

This is not a complaint about asymptotic notation. Big O is useful precisely because it abstracts away constants and lower-order terms. The missing step is to decide what the abstract units are and show that the implementation pays no more than the bound claims, under the chosen cost model.

## A tiny memoized computation, counted twice

Let us take a dependency graph with six keys, called A through F. A needs B and C. B needs D and E. C needs E and F. D, E, and F are terminal states. Imagine that each state returns a single exact integer, so that we can postpone questions about the size of values. Ask for A, starting with an empty cache.

Without memoization, the request for E occurs twice. In a larger diamond-shaped dependency graph, this duplication can multiply at many levels. With a sound cache, the first request for E computes its value and stores it. The later request reads that value without expanding E again. The computation has six distinct completed states, but seven state requests: one for A and six child requests. Requests and expansions are not the same quantity.

Now suppose that the caller requests A again after the first calculation, or asks for A three times in the same batch. Each repeated root still performs a lookup. No new state is completed, but the number of requests increases. That is why a precise execution theorem should not blindly identify calls with distinct states.

The repository has exactly this distinction in its generic memoization complexity development. In `Complexity/Memo/Bounds.lean`, the theorem `roots_request_identity` relates the number of lookup calls to the number of requested roots plus the sum of the child-request counts of the states actually completed. The identity is about the execution trace. It does not infer the number of calls just from the shape of a proposed recurrence.

A second theorem constrains where completions can occur. Begin with a finite set of keys, an envelope, closed under the dependencies of the independently defined computation. If every requested root belongs to the envelope, every newly completed state belongs to it as well. An initially populated cache is allowed: the envelope can contain both cached and uncached keys, and some stored entries can lie outside it. The expansion bound counts the initially missing keys inside the envelope, not every state in the universe and not every root request.

For our six-state example, the envelope is A through F. Its maximum number of new completions is six. If D and E are already cached with correct values, the number of initially missing keys falls to four. Correct caching is doing real work in the theorem: we need an invariant that stored values equal the independently specified values, so that a cache hit cannot corrupt the recurrence or change which dependencies the computation follows.

There is also an induction hidden in this account. A child request must decrease a rank, such as the size of the remaining subproblem. Otherwise a memoized evaluator could cycle on an uncached key and never reach a completion. Correctness, termination, the finite envelope, and the work accounting are separate arguments that eventually reinforce each other.

## From counting requests to charging operations

We have bounded how often work can be requested. We have not priced a request. A cache lookup, a cache insertion, and the local recurrence body may each have different costs.

The Lean file `Complexity/Memo/Work.lean` introduces a `WorkModel`. It describes a storage size, a bound on read work at that size, a bound on write work, and conditions saying that these bounds do not decrease when the store grows. It also requires that one completed insertion increases the modeled storage size by at most one. This is an abstract contract for a cache representation, not a law of computer hardware.

Here is the shape of its main whole-run theorem. Let M be the initially missing keys in a finite, dependency-closed envelope. Let R be the number of root requests. For each missing key k, let a of k bound the number of child requests and let b of k bound the local body work. Let S be the initial cache size. If the cost of a read in a cache of size x is bounded by c read of x, and similarly c write of x, then the total charged work is bounded by three contributions.

The first contribution is the maximum read-plus-request overhead, multiplied by R plus the sum of the a values over missing keys. The second is the maximum write-plus-expansion overhead, multiplied by the number of missing keys. The third is the sum of the b values over those missing keys. The maximum read and write costs are evaluated at cache size S plus M, because the cache may grow while the evaluation proceeds.

Notice the granularity. The theorem does not just say that something is linear in the number of states. It allows one state to request no children, another to request ten, and a third to perform more local work than either. It also accounts for warm-cache hits that still incur lookup costs. In Lean, the result is named `roots_weighted_work_envelope`. Its statement supplies the local bounds and closure hypotheses and produces both a successful result and a numeric work inequality for the emitted event trace. A companion theorem packages the same argument as a weakest-precondition contract for the evaluator.

Return to A through F. Suppose every state requests at most two children, every completed state performs at most five primitive units of local work, and we ask for one root. There are six missing keys. The general request bound gives at most one plus twelve lookups, even though our actual execution has only seven. There are at most six completions, and at most thirty local units. These are deliberately simple upper bounds, not measurements from a machine. A tighter proof could use the actual child arities and get the exact seven calls for this example.

This gives us an important lesson about formal proofs of complexity: a conservative bound is often easy to compose, while a nonuniform bound can recover the structure needed for a sharper result. We should choose the one that proves the algorithm's intended guarantee, not the one with the prettiest formula.

## The same recurrence, two very different caches

Now change only how the table is represented. The repository supplies concrete work models for two caches.

The first cache is a list of key-value pairs. A lookup may inspect the entire list. If K entries have been accumulated, a lookup is charged up to K units in this model. The second cache is a directly indexed array, where a key identifies an array cell. A simple direct lookup is charged one unit, and a product-indexed lookup is charged three primitive units for the indexing machinery. The proofs of those charges live in `Complexity/Memo/RepresentationWork.lean`.

For the six-state example, even with only thirteen possible lookup requests, a list that grows to six entries can incur as many as seventy-eight read units under the coarse bound. A direct cache incurs a fixed modeled charge per request. The result can be a linear rather than quadratic abstract lookup budget as the number of memo entries grows. We have changed the cost without changing the recurrence or its mathematical output.

A hash map is a third representation, and it needs a different theorem. Expected constant-time lookup depends on assumptions about hashing and collision behavior; worst-case lookup may still examine many entries. If two distinct balanced words have the same hash, equality must resolve the collision correctly, and that equality can itself have structural cost. A proof that a hash table contains the right entries proves functional behavior, not automatically expected constant-time behavior. To claim an expected bound, we need a probability model or a stated hashing assumption and a justified bound on the work of the actual lookup and equality operations. The ordered-tree project uses hash memoization in one of its verified functional paths, but the presence of a hash map does not turn its functional theorem into an unconditional runtime theorem.

The contrast becomes more concrete in the repository's edit-distance demonstration. For strings of lengths n and m, its finite grid has n plus one times m plus one cells. The interior contains n times m cells, while boundary states carry no child-request or local-score charge. The source proves this interior cardinality. It then instantiates the same generic memoization theorem with both a list cache and a dense cache. The dense version includes the expense of allocating and initializing the array, and it charges its index operations. The list version charges searches through the growing memo table. Both bounds come with correctness of the declared evaluator. They are not simply two informal estimates written beside the code.

The ordered-tree branch has its own specialization. `Complexity/Paper2004/MemoWork.lean` proves `cold_list_work` for the Lozano–Valiente memo evaluator. The theorem charges its list-cache setup even if the root-request list is empty, and it gives a whole-run bound in declared units for lookups, insertions, and local score operations. The state envelope is not merely every substring of the two inputs. It comes from the decomposition machinery, whose size is independently bounded in the ordered-tree proofs. Combining those theorems is the beginning of a paper-specific complexity proof.

But the comment at the top of that Lean file draws a boundary. The declared units do not yet price construction of structural words, keys or recurrence bodies, materialization of witnesses, or actual source execution. A whole-run numerical inequality is a substantial theorem even when its currency is narrower than elapsed runtime.

And be careful about the direct array. Constant-cost lookup in this model does not say that obtaining the key is constant time. If constructing the key traverses an input tree or copies a balanced word, that operation must be paid elsewhere. Nor does an array of K cells prove that live memory is exactly K cells. Capacity, initialization, temporary objects, and the behavior of the compiler's representation remain separate questions.

## Paying for a family of matchings

The Droschinsky papers give us a harder problem than counting cache reads. At a pair of tree vertices, the dynamic program may need an optimal weighted partial matching between the two sets of child branches. Each right-neighbor deletion changes that matching problem. Solving every deletion independently wastes the information carried by the original optimum.

The 2016 paper exploits that relationship with copied assignments and a repair process. The 2018 paper also needs families of right-deletion matchings. In both settings, the savings are established at the family level. A bound that applies to obtaining the base matching and all related deletions is not a per-deletion bound that should be multiplied by the number of deleted neighbors a second time.

Here is one way to reason about reuse. An optimal matching matches a certain set of right vertices. If a right vertex that is not matched is removed, the original matching is still feasible. More than that, it remains optimal: any supposedly better matching after deletion would also have been feasible before deletion, contradicting the original optimum. There is no new matching search to perform in that case.

If the deleted right vertex was matched, the old matching has lost one edge. The algorithm can repair the deficit by following an augmenting or exchange path, updating the matching and its certificate rather than resolving the entire instance from scratch. To prove a bound on the full family, count the base solve, the eligible deletions that actually require repair, and the work of each repair. The potential method provides one language for doing this: define a nonnegative potential that measures stored progress, and show that actual cost plus the potential change is bounded by a charge. Summing over operations cancels internal potential changes. An explicit family-sum inequality is another language, sometimes more direct for a static collection of related instances.

The important part is not whether we call an argument amortized. We must identify the common resource being reused and prove that the total charge applies to the whole family. The 2018 paper uses separate analyses for more balanced matching instances and for highly rectangular instances, then combines them. That is how a collection of locally expensive operations can admit the global bound established in Theorem 15.

The Lean repository currently formalizes some of the associated counting. In `Complexity/MatchingFamilies.lean`, the value `storedPairs` counts the retained pairs of a base matching and the materialized repairs for matched-right deletions. Unmatched deletions share the base rather than making copies. The theorem `storedPairs_le_product` bounds those pair cells by twice the product of the two bipartite side sizes. It is a theorem about feasible mathematical matchings, not a theorem that the production Rust vectors occupy that many bytes.

## The degree-sum trick and what it actually buys

Why is this local matching-family bound relevant to the full tree problem? Suppose a family associated with vertices u and v uses at most two times their degrees multiplied together in pair cells. Sum that over every vertex u of the first tree and every vertex v of the second.

The double sum separates. It becomes two times the sum of the degrees in the first tree, times the sum of the degrees in the second. For a finite tree with n vertices, the degree sum is two times n minus one. The corresponding sum for the other tree is two times m minus one. Multiplying gives at most eight times the quantity n minus one, times the quantity m minus one, pair cells across all those families.

That is the bound proved by `tree_family_pairs_le`, under its finite-tree and matching-feasibility hypotheses. The proof uses the handshaking identity and the tree edge-count theorem. It does not assume the degree-sum result as a mysterious scheduler fact. The finite-set combinatorics does the algebra, and Lean checks the conversion to the stated bound.

For example, if one tree has four vertices and the other has five, the theorem gives the coarse upper bound of eight times three times four, or ninety-six pair cells for the modeled collection. The actual collection may occupy fewer. What we gain is the ability to replace a sum over many vertex-pair-specific degree products with one expression in the total input sizes.

The scope is just as important as the arithmetic. The counted objects are retained matching pairs, including tags identifying which deletion repair owns a pair. There may also be headers, index metadata, vectors with unused capacity, dynamic-programming tables, recursion stacks, temporary assignment matrices, and reconstructed output paths. Some may be shared, some may be copied, and some may coexist at peak memory. A bound on mathematical pair cells does not settle all of those allocations. The source comment explicitly says that a vector and arena refinement is still needed for a production space theorem.

We should also distinguish total allocation over the whole execution from peak live space. A program that allocates and frees one thousand cells a million times may use only about one thousand cells at once while allocating a billion cells cumulatively. A time proof might charge each allocation. A space proof has to describe which objects are simultaneously live and what their representations consume. Those are different invariants.

## What must be proved about the source

We can now state the distance between our mathematical inequalities and a genuine source-level resource theorem.

First define the observation. Do we count memo lookups, comparisons, array accesses, integer operations, allocations, or steps of a source-language interpreter? A theorem about logical comparisons can be strong enough for an algorithmic paper while saying little about worst-case physical cycles. Conversely, a precise operational semantics might count individual instructions, but then we must show that the extracted model corresponds to the specific program being executed.

Second connect the source's data structures to the mathematical objects. A source vector of pair indices must represent a valid mathematical matching. A cached state must correspond to a unique key in the finite envelope. A reused deletion result must be the matching described by the family theorem. Without these correspondence invariants, applying a combinatorial counting lemma to a Rust loop would be an unsupported leap.

Third price the actual operations. The `WorkModel` proves bounds conditional on the read and write contracts it is given. It does not automatically prove that the code generated by Rust has that cost. A heap-allocated list lookup has a different abstraction boundary from direct indexing into a contiguous array, and both may have input-dependent key construction. If the theorem counts elementary operations on mathematical integers, arbitrary-precision arithmetic has a bit cost that needs its own argument. If the source uses fixed-width integers, the proof instead needs range and overflow conditions. Floating-point weights bring rounding, exceptional values, and comparison semantics into the functional correspondence before timing even enters the picture.

Fourth, establish the execution schedule. The 2018 rooted reference evaluator is correct because the dependency rank decreases and enough rounds produce the required values. That proof alone does not show that the optimized implementation evaluates each state once, in an order allowing each sibling matching to reuse its predecessor. The schedule and its accompanying resource charges are algorithmic objects worth formalizing in their own right.

The source repository is not starting from zero on execution semantics. Its ordered-tree proof campaign has models of addressed memory, source operations, ownership and retirement, and checked theorems for substantial parts of the actual evaluator and public maximum call. The status file records agreement between certain source-model costs and interpreter traces, while explicitly leaving the complete production resource closure open. An addressed execution model is not, by itself, a measured CPU-time theorem or a proof of the behavior of an arbitrary allocator and compiler.

For the optimized 2016 and 2018 graph backends, further obligations include showing that the production routines construct the intended matching instances, maintain the correct cache and deletion-family invariant, reconstruct witnesses with original graph identities, and satisfy the numerical and error contracts of their public entry points. The paper runtime bounds are available as mathematics; a full translation of those bounds into the optimized Rust execution has not been completed in this supplied snapshot.

## Designing a useful theorem, rather than a slogan

What might we ask Lean to prove? Start with a concrete input contract for two trees and a concrete implementation, not merely an abstract big-O expression. Let the execution produce a result, a trace, and a peak-live-storage quantity. Prove that the result is an independently valid optimum. Then prove that the trace's charged work is bounded by a formula whose parameters are the vertex counts and maximum degrees of those input trees. Prove a separate bound on live storage. Only after choosing a uniform cost model and supplying input-size assumptions should we extract the familiar asymptotic notation.

For a tree matcher, a good intermediate theorem can be more useful than a premature global result. Prove that a family of right-neighbor-deletion calls returns exactly the independently defined optima and consumes at most a stated cost, *including the base solve and every repair*. Next prove that each source table state invokes the correct family and that its dependency schedule never requests an unready value. Then aggregate the local bounds using degree sums and maximum-degree inequalities. Finally relate abstract table entries, matching pairs, choice vectors and temporary storage to their actual source representations.

The corresponding error theorem belongs in the same story. A program that exits early on overflow is fast, but it has not calculated an optimum. A time bound for successful admissible inputs must state those preconditions. If rejected inputs are part of the public API, their branches can receive separate correctness and cost bounds, just as the signed-integer matching source theorem distinguishes successful results from shape and size errors.

A sensible final theorem might involve a constant times n times m times the smaller maximum degree, matching the 2018 paper's algorithmic goal, with a separate constant times n times m live-space bound. The constants would be relative to the declared operation and memory models, not universal promises about wall-clock time or bytes allocated by every compiler. It would be an achievement to prove even that carefully scoped claim for the actual optimized source.

We have arrived at a useful division of labor. Mathematical combinatorics tells us how many distinct things can happen. Execution invariants tell us how often they actually happen. Cost models say what each thing is charged. Representation proofs connect these things to executable code. Combining the four yields a resource theorem whose conclusion has a precise meaning. None can substitute for the others, and the Lean development already gives us several working examples of how to assemble them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: the exact work envelope

The generic theorem `SubtreeProofs.Complexity.Memo.roots_weighted_work_envelope` supplies a successful evaluator state, a trace invariant, and the bound

\[
\begin{aligned}
 W \le {}& (o_r+c_r(S+|M|))\left(R+\sum_{k\in M}a(k)\right)\\
 & +(o_w+c_w(S+|M|))|M|+\sum_{k\in M}b(k),
\end{aligned}
\]

where `M` is the subset of an **envelope** initially absent from the cache, `R` is the root-request list length, `a(k)` bounds the requests made by the independent body, `b(k)` bounds its local work, `S` is initial modeled storage size, and `o_r`, `o_w` are declared per-request/per-completion overheads. The actual Lean statement also requires closure under canonical requests, sound and valid initial cache contents, and enough fuel relative to ranks. It produces a bound on `Event.totalWork`, **not** a physical runtime or Rust instruction count. `roots_weighted_work_wp` repackages this as `Std.WP.wp` for the executable memo evaluator.

### Concrete instantiations to read

| File and declaration | Proved object | Boundary |
| --- | --- | --- |
| `Complexity/Memo/Bounds.lean`: `roots_request_identity` | `calls = roots.length + sum(actual completed body arities)` | Assumes successful traced execution and trace invariant |
| `Complexity/Memo/Bounds.lean`: `roots_envelope` | Successful execution, new completions bounded by initially missing envelope keys, call arity bound | Requires a finite, dependency-closed envelope and sound initial cache |
| `Complexity/Memo/RepresentationWork.lean`: `ListCache.workModel` | List lookup work bounded by modeled list length | Primitive list work only |
| `Complexity/Memo/RepresentationWork.lean`: `DirectCache.productWorkModel` | Product-indexed dense read and write work bounded by three declared units | Does not charge arbitrary key production or source machine operations |
| `Complexity/EditDistance/Work.lean`: `dense_weighted_work_spec` | Whole-run declared work including dense-array setup; only `n*m` interior bodies carry recurrence work | Abstract cache/body model; not machine resource theorem |
| `Complexity/Paper2004/MemoWork.lean`: `cold_list_work` | Cold-cache ordered-tree evaluation in declared work units; includes one setup unit | Structural word/key construction, witnesses and actual source work excluded |
| `Complexity/MatchingFamilies.lean`: `tree_family_pairs_le` | Tagged retained matching pair cells bounded by `8*(n-1)*(m-1)` | Feasible mathematical families; vector metadata, allocation and source space not proved |
| `Rust/SourceResourceCanonical.lean`, `Rust/SourceHeapResources.lean` | Components of addressed-source resource/ownership interpretation | Full production resource closure not claimed in `PROOF_STATUS.md` |

### The ordered-tree cold list inequality

With `cells = (envelope left right).card`, `roots` the list of requests, and `requestOverhead`, `expansionOverhead` nonnegative declared units, `cold_list_work` establishes an execution bound of the form

\[
1+(\text{requestOverhead}+\text{cells})(|\text{roots}|+4\cdot\text{cells})
 +(\text{expansionOverhead}+5)\cdot\text{cells}.
\]

The `1` charges list-cache creation; the formula is in explicitly declared event-work units. It does not silently price construction/copying of the Dyck-word keys or Rust execution. `Paper2004/TreeStateBounds.lean` proves the independent ordered-tree decomposition bound; those state counts can be combined with appropriate body and representation obligations.

### Whole-family pair-space calculation

For a family at vertex pair `(u,v)`, `storedPairs_le_product` proves

\[
\operatorname{storedPairs}(u,v)\le 2\deg(u)\deg(v).
\]

Then

\[
\sum_{u,v}\operatorname{storedPairs}(u,v)
\le 2\left(\sum_u\deg(u)\right)\left(\sum_v\deg(v)\right)
=8(n-1)(m-1).
\]

This is a count of *tagged pair cells* for feasible base/repaired matching families. It is not a peak-byte theorem or an assertion about the number of allocated `Vec` slots in Rust.

### Further reading and exercise

1. In the six-key example, compute the exact seven requests and six completions; explain why a second root request for `A` changes only the request count.
2. Compare `ListCache.workModel` with `DirectCache.productWorkModel`. Which operation cost changes, and which potential key-building cost is absent from both models?
3. In `Complexity/MatchingFamilies.lean`, trace `storedPairs_le_product → family_sum_le → tree_degree_sum → tree_family_pairs_le`. Where do feasibility and the handshaking identity enter?
4. In `proofs/PROOF_STATUS.md`, identify one addressed-source resource theorem that is established and one explicit frontier it leaves open. Why is a source-model cost theorem not automatically a wall-clock timing theorem?
5. Sketch a conditional lemma for the 2018 optimized matching family that includes a complete base solve, all right-neighbor deletions and the final repaired choices. Which result in the independent 2018 specification would its value theorem have to refine?

**Primary papers:** Lozano & Valiente (2004), Theorems 1 and 3; Droschinsky, Kriege & Mutzel (2016), Theorems 4 and 7; Droschinsky, Kriege & Mutzel (2018), Theorem 15. Source files are from the user-supplied November 19, 2026 `networkx_algo_common_subtree` archive. Useful external prerequisite: `algorithms-computability-complexity:017000` (amortization and data structures); immediate track prerequisites: `014000`, `020000`, `022000`–`025000`.
