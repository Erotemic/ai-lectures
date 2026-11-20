# The Last Mile: From a Proved Solver to a Python Answer

<!-- BEGIN SPOKEN LECTURE -->

Suppose a mathematician has proved that a particular algorithm always returns a maximum common subtree. The proof is checked by Lean. The recurrence is correct. The witness exists. There is no missing case in the combinatorics. A programmer then exposes the algorithm as a Python function accepting two NetworkX graphs. The programmer runs the function, sees a plausible answer, and says that the Python API is verified.

What, exactly, has been proved?

The mathematical theorem did not mention Python objects. It did not know about dictionary keys, floating-point rounding, callbacks, shared libraries, exceptions, graph edge iteration, or native memory. It did not know whether the returned witness would refer to the input's actual nodes rather than a fresh collection of anonymous integers. And it did not know whether the installed package would call the proved algorithm or a faster, separately maintained one.

This is not a reason to dismiss the theorem. It is a reason to understand its scope. A convincing public correctness claim requires a chain of relations: from user inputs to a mathematical instance, from that instance to the algorithm's representation, from the implementation's result to a mathematical witness, and from that witness back to the objects the user supplied. Each relation has a different proof obligation. Some parts of this chain are already proved in the common-subtree repository. Other parts are guarded by runtime validation and tests. Still others remain open research work.

The repository gives us a particularly good opportunity to compare two paths. The ordered-isomorphism API has a compiled, exact-rational Lean solver with a correctness theorem. The unordered 2016 and 2018 APIs offer optimized Rust solvers with floating-point scores and substantial independent tests, but not a complete source-level refinement theorem. These are both useful products. Their guarantees are not interchangeable.

## The object on one side of the boundary is not the object on the other

Start with the public weighted unordered function, `maximum_common_subtree_isomorphism`. The caller passes two NetworkX graphs. The vertices may be integers, strings, tuples, or other hashable Python objects. The graphs may carry attributes, and the caller may supply node and edge weighting functions. The return value is a `CommonSubtreeResult`: a numeric weight, pairs of original nodes, and paths made of original nodes. Its `mapping` property builds a dictionary from the pairs.

Inside the native algorithm, none of those objects are needed. A tree is represented by consecutively numbered vertices, integer label codes, and edges between those integers. A callback-based scoring rule becomes a table of optional floating-point values. An output mapping is first a collection of pairs of integer indices. That makes the algorithm practical to implement in Rust. It also creates a representation boundary.

For a correctness proof, the boundary needs two directions. Encoding must preserve the problem: compatible pairs, tree adjacency, root restrictions, and scores must mean the same thing in the indexed model as they did in the original graphs. Decoding must preserve the answer: a pair of indices returned by the solver must become the corresponding two original node objects, with paths and score attached to those nodes. A theorem confined to the indexed algorithm addresses neither direction automatically.

The Python code makes the intended correspondence explicit. It first takes the tuple of nodes in NetworkX iteration order and makes a dictionary from each node to its index. When the native answer returns, it looks each index up in those stored tuples. If a vertex was the tuple `("b", 2)`, it returns that tuple as a node, not the string representation of the tuple and not an invented numeric label. The object's position in the Python input is temporary; its identity as a graph node is the API's observable result.

This distinction is particularly important for trees with repeated node attributes. A node's label attribute is a constraint on matching, not the identity of the node. Several nodes can share the same label, and a correct witness must still distinguish them by their actual input vertices. The code uses separate dictionaries for node identities and for compact codes describing label equality. A formal proof should keep those two dictionaries separate too.

There is one more subtlety. The order of nodes and edges is an implementation detail that determines the temporary integers and can affect which of several tied optimal solutions is returned. The public documentation promises deterministic choices for fixed input iteration order and backend, but it does not promise that the Python reference and Rust backend select the same optimum when there are ties. A theorem asserting equality of one particular sequence of pairs would be stronger than the stated API contract, and in general the wrong specification. The desired theorem is usually that the returned mapping is valid and its score is optimal, not that its arbitrary tie break matches another solver's tie break.

## Following a witness all the way home

Consider two tiny trees. On the left, the nodes are named oak, bridge, and pine, connected in that order. On the right, they are east, span, and west, also connected in a path. Give oak and east the shared label A. Give pine and west the shared label B. The intermediate nodes carry different labels, so they cannot be matched to each other. Let each matched node contribute four points, and let the ordinary direct-edge reward be two points.

Ask the 2018 embedding solver to charge one half point for each skipped internal vertex. The best witness matches oak to east and pine to west. There are two matched nodes, worth eight. The common-tree edge is realized by a two-edge path on the left and another two-edge path on the right. Each path has one skipped internal vertex, so the penalty is one point in total. The result has score seven.

Notice a scoring trap. The two paths each consist of two edges. Even though the original trees have edges, the single common-tree edge is not represented by a direct edge on both sides. The 2018 rule does not add the ordinary edge reward here. It adds the skipped-vertex penalty instead. A generic graph-matching intuition could easily produce an incorrect score of nine by adding the direct-edge reward to the path case. The API's independent rescoring function checks precisely this distinction.

Now call the 2016 strict-isomorphism function with the same node labels and weights. The two leaf nodes cannot both participate: they are not adjacent in either original tree. The best result is a single matched node, worth four. If we call the 2018 embedding function again with infinite skipping penalty, a path with an internal skipped vertex is forbidden, and the best score is four again.

This small experiment is valuable because it distinguishes the mathematical problems at the public boundary, not merely in the paper. The isomorphism API returns a connected induced correspondence. The embedding API can return a common skeleton whose abstract edges are realized by paths. The `edge_paths` field retains the original intermediate vertices, even though those vertices do not appear as matched node pairs. A decoder that threw those intermediate vertices away could report the right number but still fail to return a usable witness.

The repository contains two different kinds of protection for this situation. The Rust binding reconstructs a skeleton from selected nodes by trimming irrelevant leaves, then follows paths between selected branch endpoints. It rejects a reconstruction with a missing branching vertex or incompatible common skeletons. The Python result constructor translates those paths into original node objects. Separately, `score_common_subtree_embedding` can inspect a supplied result, reject invalid paths, and recompute its score using the 2018 rule.

That last check is useful, but it is not itself an optimality proof. If I gave the scorer a valid single-node witness of weight four, it would verify that witness as valid even when the two-node embedding of weight seven exists. A checker of feasibility and score is weaker than a solver-correctness theorem. A complete certificate could combine a feasibility-and-score verifier with a separate theorem or certified bound establishing that no better solution exists. The current independent rescorer does not supply that upper bound.

## Inputs are part of the theorem

The weighted unordered interface is deliberately restrictive about its graphs. It accepts simple undirected NetworkX trees. A nonempty graph must be connected and acyclic. A directed graph, multigraph, cycle, or disconnected nonempty graph is rejected. Empty graphs are accepted, because the optional empty solution has an explicit interpretation in the API.

A formal API contract should not quietly assume that the caller passes trees. It should say what happens when the caller does not. There are at least two plausible contracts. One is a partial function defined only on valid trees. The other, closer to an actual Python interface, is a total operation whose result is either a valid solution or a documented failure. The latter requires precise input validation and error behavior, not just a proof about successful computations.

The API also separates labels and weights. A named node-label attribute constrains node compatibility. An edge-label attribute constrains direct edge compatibility. If the weights are callbacks, the Python adapter evaluates compatible node and edge pairs before entering the Rust solver, storing optional scores in matrices. Returning `None` from a callback forbids that pair. Returning zero permits a pair of zero contribution. That distinction is important with negative weights and with the question of whether a nonempty witness exists.

Imagine two one-node trees with a compatible node pair worth negative two. Under the paper's nonempty formulation, that one pair is the best possible nonempty solution, and its score is negative two. But the public function defaults to `allow_empty=True`. It may choose the empty witness of score zero. With `allow_empty=False`, it returns the negative optimum. If the callback instead returns `None`, and no other match is possible, `allow_empty=False` returns Python `None`, meaning no nonempty feasible solution exists. A `CommonSubtreeResult` with zero weight and no pairs is not the same as a Python `None` result.

These states must be represented separately in the theorem. The mathematics of the 2016 paper optimizes over nonempty common subtrees. The Python convenience wrapper optionally adjoins one more feasible object, the empty witness of score zero. Proving that the nonempty solver is correct does not by itself prove that the wrapper handles all negative, zero, and infeasible cases correctly. Fortunately, the wrapper's logic can be specified with a short case split rather than a new tree theorem.

Root constraints add another distinction. In the unordered API, `roots=(u,v)` fixes ambient orientations of the input trees. With `root_to_root=True`, the supplied roots themselves must be matched. Without that second flag, the highest common matched pair may lie below the supplied roots. This is not the same interface as the ordered-isomorphism `rooted` Boolean we will meet later. Giving two distinct APIs similar mathematical names does not establish that they impose identical restrictions.

## Floating point changes the question being asked

The public unordered adapter converts weights to Python floats and requires ordinary weights to be finite. It accepts a nonnegative skipping penalty, including positive infinity, whose special interpretation is that skipped vertices are forbidden. The native graph binding receives `f64` values and optional matrices, validates dimensions and finiteness, and then invokes the Rust solver.

This means a theorem over exact real or rational weights does not automatically say what the Rust code returns. Floating-point addition rounds. Cancellation can erase low-order information. A sum of individually finite scores can overflow. Two mathematically distinct optima can become indistinguishable under rounding, while a strict comparison can choose a different branch when values are nearly equal.

For example, if one choice scores one tenth and another scores an exactly represented nearby binary value, the native program compares stored binary approximations, not abstract rational numbers one tenth apart. Even when every input was expressed as a Python integer, conversion to `f64` can lose distinctions among sufficiently large integers. None of this refutes the paper's optimality theorem. It means we need to decide what numerical statement the compiled backend is expected to satisfy.

There are several honest possibilities. A program might promise the optimum in an exact rational model, in which case it needs exact arithmetic throughout or a rigorous refinement from a different representation. It might promise optimality relative to a clearly specified floating-point objective. It might guarantee an error bound under score-gap and magnitude hypotheses. Or it might explicitly document that the fast path is tested empirically, without a universal source-level numerical proof. The supplied unordered Rust path is currently in this last category. Its code rejects nonfinite ordinary inputs and catches several overflow failures, while tests compare it against independent small-input references. These are valuable safeguards, not a theorem that every floating-point execution equals the exact mathematical optimum.

There is also a difference between a source algorithm's totality and a Python extension's failure policy. The graph binding wraps the solver call in a Rust panic catcher. It converts certain overflow and finiteness failures to `ValueError` and other caught panics to `RuntimeError`. It releases the Python interpreter lock while the Rust tree solver runs because Python callbacks have already been evaluated. These details are visible behavior, and useful engineering choices. A panic caught and translated to an exception is not evidence that the algorithm cannot panic. A properly handled exception is not the same as a successful mathematical result.

## The different route taken by the proved ordered solver

Now change papers and arithmetic models. The Lozano-Valiente ordered-isomorphism API can explicitly select `impl="verified-lean"`. This is not an alias for the optimized unordered Rust solver, and it is not the 2018 topological-embedding backend. It solves the ordered common-subtree-isomorphism problem using exact nonnegative rational node affinities.

Here the Python adapter converts the ordered tree into balanced tokens and then into an indexed nested representation. It evaluates each relevant pair affinity, requiring integers, fractions, or other exact rational values that can be converted to fractions. It rejects negative affinities. Zero means a forbidden match in this ordered affinity model, unlike a zero-valued but permitted edge in the unordered weighted model. Floating-point affinities are rejected unless the caller explicitly converts them, making the precision decision visible.

The request is serialized as JSON. Each rational weight is sent as a numerator and denominator, not a rounded decimal. A compiled Lean executable reads that request and evaluates the proved memoized rational solver. The response contains matched original preorder indices and an exact rational score. The Python adapter validates index bounds and uniqueness, checks that the score equals the sum of the selected original affinities, rejects forbidden selected pairs, and reconstructs the selected opening and closing tokens from their original positions.

The key Lean theorem is `RationalSolver.solveResult_correct`. It connects the actual hash-memoized computation to the independent ordered-isomorphism specification, including feasibility, optimality, score, and preorder. A companion theorem, `solve_unique_endpoints`, covers original endpoint uniqueness under its hypotheses. That is substantially stronger than comparing a Rust result with an oracle on a set of tests: the algorithm used by the compiled Lean path is the one appearing in the theorem.

Still, the proof does not swallow the entire Python process. Python's NetworkX-to-token conversion, JSON encoding and decoding, process lifecycle, and interpretation of returned node objects are tested integration boundaries. The Lean compiler and runtime, rational and hash-map implementations, and operating system process machinery also sit within the execution trust story. If the compiled executable is absent, explicitly requesting `verified-lean` raises `ImportError`; the adapter does not silently call an unproved substitute. That matters because a claim about which algorithm was used is false if selecting the proved backend can silently fall back to a different one.

The repository also exposes an independently source-proved unweighted Rust token route, selected by a restricted ordered backend name. It does not accept arbitrary node-affinity callbacks, and it does not establish the same rational weighted theorem. Different verification methods cover different slices of the public interface. We should resist the temptation to combine them into one imagined blanket certificate.

## A compiled wheel is an interface, not a proof of semantics

The optimized Rust extension uses PyO3 to export functions to Python. Its public low-level graph function accepts arrays of integer label codes, edge triples, optional weight matrices, numeric parameters, and optional root indices. Its result is either absent or a weight together with indexed node pairs and indexed paths. The higher-level Python wrapper then restores the original NetworkX objects.

The build configuration also supports Python's stable ABI for a suitable minimum interpreter version. An ABI3 wheel can be exercised across several CPython versions without recompiling a separate extension for every minor release. The supplied project's release records include installed-wheel and ABI compatibility tests. Those tests answer important distribution questions: can the extension be imported, are the expected entrypoints present, do representations cross the foreign-function boundary correctly for tested cases, and does a released artifact behave like the source checkout?

They do not answer every mathematical question. ABI compatibility does not imply that a mapping is optimal. A successful import does not prove the returned node pair belongs to the correct input tree. A numerical parity test does not establish a uniform floating-point error bound. And proving a function inside one Rust crate does not show that the Python wheel invokes that function when a user selects a particular backend.

A complete verification story would therefore name the artifact and path of execution, not just the repository. Which installed module was imported? Which native function did the wrapper call? Which options were selected by `auto`? Which source commit and compiler settings produced that binary? A research theorem remains true independent of the wheel, but the wheel's claim to implement it depends on this chain of identification.

For the current Python APIs, backend selection is observable. In the unordered package, `impl="auto"` chooses the Rust extension when its expected graph entrypoint is available and otherwise the exhaustive Python reference. An explicit `impl="rust"` does not quietly substitute the reference if the Rust graph function is missing. The ordered isomorphism API has its own backend-selection policy; `verified-lean` is an explicit option, not a universal implication of `auto`. A user who wants a theorem-backed run must know which option carries that theorem and what its remaining trusted boundaries are.

## What an end-to-end theorem would look like

We can now express the mathematical shape of the missing theorem. Start with two original NetworkX trees and fixed callback values. Assume the graphs satisfy the documented input constraints, labels are hashable, callbacks return permitted finite scores or `None`, and any required arithmetic hypotheses hold. Encode the graphs into indexed trees and scoring matrices. Run the designated backend. Decode the indexed result to original node pairs and paths.

For every successful return, prove that the decoded witness is a valid common subtree in the selected problem, that its score is the score specified by the public API, and that no other valid witness has a better score under the stated numerical semantics. If the API allows an empty solution, include its zero baseline. If it forbids empty solutions, distinguish a negative optimum from absence of a feasible nonempty mapping. If a root restriction is supplied, show the decoded witness satisfies that exact restriction. For every rejected input class in the documented contract, establish the specified error behavior, or state explicitly which Python and runtime failures lie outside the theorem's scope.

There is no need to prove all this in one gigantic file. One can first prove the indexing correspondence for graph nodes and edges. A second theorem can prove that precomputed callbacks produce the intended compatibility matrices. A third can establish indexed-path reconstruction and independent rescoring. Another can connect a particular proved algorithm to the indexed specification. The outer theorem merely composes them. For the optimized `f64` backend, the numerical refinement is a separate, probably difficult bridge; its absence should remain visible instead of being hidden inside a broad assertion called `correct`.

A narrow milestone would already be useful: prove that decoding a valid indexed 2018 witness returns valid original-node paths with the same skipped-vertex count and with no hidden branching point. Such a theorem does not need Hungarian duality or a global optimality proof. It closes a real gap between algorithm output and the value a NetworkX user receives. Another tractable milestone is a precise wrapper theorem for the `allow_empty` case split, assuming correctness of the nonempty solver. Those results compose later with the source refinement rather than depending on its completion.

## The meaning of a verification label

The lesson is not that software can never be verified completely. It is that verified claims are quantified statements with domains, hypotheses, and named boundaries. Saying that the ordered exact-rational Lean solver is proved is meaningful. Saying that the unordered floating Rust backend is extensively tested but its complete source proof remains open is meaningful. Saying that the Python wrapper restores original node objects and independently checks returned paths describes concrete code and tests. None of those statements needs to be weakened, and none should be inflated into another.

The public caller does not receive a Lean theorem. The caller receives Python objects. To call that answer verified, we should be able to follow every relevant representation change and identify the theorem or tested trust assumption at each step. The common-subtree project is already equipped with substantial mathematics, exact source-level results for selected components, a proved rational solver, and independent public API tests. The remaining task is to fit these into a compositional account of what each installed entrypoint guarantees.

That is the last mile of formalization. It begins where the elegant recurrence ends: with the precise meaning of a Python result, its original vertices, its paths, its score, and the circumstances under which the user is entitled to trust it.

<!-- END SPOKEN LECTURE -->

## Source and theorem companion (not narrated)

The code and proof-status observations below refer to the **user-supplied `networkx_algo_common_subtree` source snapshot dated 2026-11-19**. This lecture does not modify or extend any Lean/Rust proof. Proposed theorem interfaces are marked explicitly and are not existing declarations.

### Checked public examples: original-node paths and empty results

The following was run against the `impl="python"` reference backend in the uploaded repository snapshot. It avoids relying on a native extension being installed in the authoring environment.

```python
import networkx as nx
from networkx_algo_common_subtree import (
    maximum_common_subtree_isomorphism,
    largest_weight_common_subtree_embedding_with_distance_penalty,
    score_common_subtree_embedding,
)

left = nx.Graph()
left.add_nodes_from([
    ("oak", {"kind": "A"}),
    ("bridge", {"kind": "only-left"}),
    ("pine", {"kind": "B"}),
])
left.add_edges_from([("oak", "bridge"), ("bridge", "pine")])

right = nx.Graph()
right.add_nodes_from([
    ("east", {"kind": "A"}),
    ("span", {"kind": "only-right"}),
    ("west", {"kind": "B"}),
])
right.add_edges_from([("east", "span"), ("span", "west")])

common_kwargs = dict(node_label="kind", node_weight=4, edge_weight=2, impl="python")
embedded = largest_weight_common_subtree_embedding_with_distance_penalty(
    left, right, skip_vertex_penalty=0.5, **common_kwargs
)
assert embedded.weight == 7.0
assert embedded.node_pairs == (("oak", "east"), ("pine", "west"))
assert embedded.edge_paths == (
    (("oak", "bridge", "pine"), ("east", "span", "west")),
)
assert score_common_subtree_embedding(
    left, right, embedded, node_label="kind", node_weight=4,
    edge_weight=2, skip_vertex_penalty=0.5,
) == 7.0

strict = maximum_common_subtree_isomorphism(left, right, **common_kwargs)
assert strict.weight == 4.0
blocked = largest_weight_common_subtree_embedding_with_distance_penalty(
    left, right, skip_vertex_penalty=float("inf"), **common_kwargs
)
assert blocked.weight == 4.0

one_left = nx.Graph(); one_left.add_node("a")
one_right = nx.Graph(); one_right.add_node("b")
assert maximum_common_subtree_isomorphism(
    one_left, one_right, impl="python", node_weight=-2
).weight == 0.0
assert maximum_common_subtree_isomorphism(
    one_left, one_right, impl="python", node_weight=-2,
    allow_empty=False
).weight == -2.0
assert maximum_common_subtree_isomorphism(
    one_left, one_right, impl="python",
    node_weight=lambda u, v: None, allow_empty=False
) is None
```

For the displayed embedding, the common-tree edge is represented by paths with two edges each; the contribution is `-0.5 * (1+1) = -1`, not the nominal direct-edge reward of `2`.

### Public API shape and source landmarks

| Layer | Maintained source | Contract or observation |
| --- | --- | --- |
| 2016/2018 NetworkX entrypoints | `networkx_algo_common_subtree/unordered.py` | `_tree_data`, `_Problem`, `_solve`, `maximum_common_subtree_isomorphism`, `largest_weight_common_subtree_embedding_with_distance_penalty`; node/edge compatibility and callback matrices |
| Result construction | `unordered.py` | `_Problem.result` maps native integer indices to stored original-node tuples; `CommonSubtreeResult(weight, node_pairs, edge_paths)` and `mapping` property |
| Independent result validation | `unordered.py` | `_score_path_witness`, `_check_rooted_mapping`, `_rescore`, `score_common_subtree_isomorphism`, `score_common_subtree_embedding`; feasibility/score checks, **not** a global optimality certificate |
| Native graph boundary | `rust/src/graph_bindings.rs` | `solve_graph`, PyO3 graph functions, `validate_matrix`, `checked_call`, `witness_paths`; primitive indexed inputs and path reconstruction |
| Public extension registration | `rust/src/lib.rs` | `#[pymodule] fn _rust` calls `graph_bindings::register`; contains separate ordered/token entrypoints |
| Optimized weighted graph algorithms | `rust/crates/common_subtree_algorithms/src/{tree,matching}.rs` | Production indexed Rust DP and matching; no claimed end-to-end source theorem |
| Ordered exact-rational API | `networkx_algo_common_subtree/{tree_isomorphism,balanced_isomorphism,balanced_isomorphism_lean}.py` | `impl="verified-lean"`, exact `Fraction` affine scores, JSON worker, score/index validation; no silent fallback |
| Proved ordered implementation | `proofs/SubtreeProofs/Paper2004/RationalOrderedSolver.lean` | `RationalSolver.solveResult_correct` and `solve_unique_endpoints`; proof for actual Lean rational memoized computation |
| Separate exact Rust theorem | `proofs/SubtreeProofs/Rust/MatchingEntrypoint.lean` | `max_weight_partial_matching_total_spec` is for a bounded signed-integer reference matching API, not an end-to-end unordered NetworkX result |
| Release and ABI evidence | `rust/Cargo.toml`, `CMakeLists.txt`, `docs/planning/RESUME.md` and `proofs/PROOF_STATUS.md` | `abi3-py310` feature and recorded installed-wheel/ABI tests; packaging compatibility is not functional optimality |

### Exact vs floating contracts

For unordered `impl="rust"`, Python converts ordinary weights to finite floats; `None` forbids a node/edge pair, while zero is a permissible score. `skip_vertex_penalty=+inf` specifically forbids skipped vertices. `allow_empty=True` adjoins the zero-valued empty witness. `impl="auto"` chooses the Rust graph backend when available, otherwise the Python exhaustive reference.

For ordered `impl="verified-lean"`, each affinity is an exact nonnegative rational; zero **forbids** a node pair. Fractions are serialized as `[numerator, denominator]` decimal strings, and the result score is a `Fraction`. The executable calls the proved Lean rational solver. The Python process/transport/graph conversion and compiled Lean runtime are outside the checked Lean theorem. An unavailable executable raises `ImportError` rather than falling back to a different backend.

### A proposed compositional API contract (not yet proved)

Let `encode(G,H,options) = (L,R,W,policy,orig)` translate original-node NetworkX inputs into indexed trees, optional weight tables, a root policy and index-to-node maps. Let `decode(orig, indexed_witness)` reconstruct `CommonSubtreeResult` including original paths. For a declared arithmetic semantics `S`, a useful theorem would have the shape

\[
\begin{aligned}
&\operatorname{WellFormed}_{S}(G,H,options) \land
  \operatorname{encodeRel}(G,H,L,R,W,orig)\\
&\qquad\Longrightarrow
\operatorname{runAPI}(G,H,options)=\operatorname{Success}(res)\\
&\qquad\phantom{\Longrightarrow}\land
  \operatorname{ValidCommonWitness}_{S}(G,H,res,policy)\\
&\qquad\phantom{\Longrightarrow}\land
  res.weight=\operatorname{Score}_{S}(res)\\
&\qquad\phantom{\Longrightarrow}\land
  res.weight=\operatorname{Optimum}_{S}(G,H,policy).
\end{aligned}
\]

This must be adapted to `allow_empty`, feasible-nonempty absence and the exact Python exception contract. It is **not** an assertion that existing Lean theorems already cover `runAPI` or a real compiled wheel. Numerical semantics `S` must distinguish exact rationals from the observed floating-point implementation.

Potential smaller proofs to develop independently:

1. `encode_indices_correct`: every input vertex/edge is represented exactly once and every compatible pair/table entry corresponds to its original objects and fixed weight value.
2. `decode_paths_valid`: every valid indexed 2018 skeleton/path witness decodes to paths in original NetworkX nodes, retaining skipped interior vertices, preserving branch separation and score components.
3. `empty_policy_correct`: assuming correctness of the nonempty solver, selecting the empty score-zero witness is sound for `allow_empty=True`, including negative and zero optima.
4. `graph_bindings_refines_indexed`: PyO3 argument validation/selection, native result and caught-error behavior are related to the chosen source algorithm under explicit numeric/ABI assumptions.
5. `installed_entrypoint_correspondence`: selected backend names and build artifacts invoke the intended proved or tested implementation, with no mislabeled fallback.

The next possible workshop can work from these proposed interfaces, the optimized matching-family invariant from `027000`, and the 2018 unrooted structural split to prioritize three concrete proof developments without claiming they have already been checked.
