# The Tree, the Witness, and the Machine: A Common-Subtree Capstone

<!-- BEGIN SPOKEN LECTURE -->

Imagine being handed two trees and asked to find their greatest common part. It sounds like a question about shapes. You look at the branches, decide which ones correspond, and try to keep as much structure as possible. Then someone asks you to prove that your answer is the best possible. That is already a different problem. Someone else asks you to prove that the particular program shipped in a Python wheel always returns that answer. And someone else wants to know whether the program has the running time claimed by the paper from which it was adapted.

The tempting response is to treat these requests as different formulations of the same question. They are not. Each one introduces an object that was absent from the previous one: a specification of valid common structure, a mathematical optimality proof, an algorithm with representations and update rules, a program whose arithmetic and memory have concrete behavior, and finally an interface through which somebody can ask the program a question and receive recognizable nodes in return.

This course began with three research papers and a repository implementing and formalizing algorithms related to them. Lozano and Valiente studied common embedded subtrees of ordered trees in 2004. Droschinsky, Kriege, and Mutzel studied maximum-weight common subtree isomorphism in 2016, and maximum-weight common subtree embedding with distance penalties in 2018. We have learned how their algorithms work and explored the Lean proofs already present in the accompanying project. A useful conclusion is not to announce that every remaining theorem is proved. It is to assemble the ideas into a clear account of how we could finish more of the work, one trustworthy link at a time.

I want to do that in two passes. First, consider one small example through the lenses of all three papers. Then follow a candidate solution from its definition, through the dynamic program, into a fast implementation, and back to a Python user. Along the way we will stop at three unfinished proof obligations. They are substantial enough to be genuine mathematical work, but small enough to give a sensible place to begin.

## A small tree that changes its meaning

Take a tree with two vertices, Alice and Bob, joined by an edge. Give Alice a compatible counterpart worth five points, and Bob a counterpart worth four. Now take a second tree whose corresponding endpoints are separated by one intermediate vertex. The second tree is a three-vertex path. The intermediate vertex is not compatible with either Alice or Bob. Suppose skipping one intermediate vertex costs two points.

If our problem is strict common subtree isomorphism, an edge in the selected subtree must map to an edge of the other selected subtree. We cannot preserve Alice and Bob together as adjacent matched vertices, because their compatible partners are not adjacent. We may select Alice alone for five points, or Bob alone for four. Under these particular compatibility rules, the optimum is five. A proposed solution containing both endpoints is invalid regardless of how attractive its sum of vertex scores looks.

If our problem is topological common subtree embedding, one abstract edge is allowed to be realized by a path. Alice and Bob can both be selected. The connecting path in the second tree passes through the intermediate vertex. Their vertex rewards sum to nine. One skipped vertex costs two, so the embedding scores seven. Selecting both is now better than selecting Alice alone. The mathematics did not discover a cleverer way to solve the strict problem. It changed the set of feasible witnesses, and consequently changed the optimum.

Now vary the penalty. If the skip cost is one, the two-endpoint solution scores eight. If the cost is three, it scores six. If the cost is five, it scores four, and the single Alice vertex is better at five. At a penalty of four, the two alternatives tie. This little calculation shows why a distance penalty is not merely something tacked onto the final answer. It changes which structure is worth preserving. The 2018 paper formalizes the choice with a scoring rule that treats genuine one-edge connections differently from connections expanded into paths. An abstract edge receives its direct-edge reward only when its realization has length one in both input trees. Otherwise the score is governed by the skipped interior vertices. A direct edge on just one side is not enough to claim the direct-edge reward.

The ordered-tree problem from 2004 takes a third approach. If we equip these paths with roots and sibling order, it can ask whether a smaller ordered shape can be obtained by contracting edges of a larger ordered shape. Contracting an edge removes a structural separation; it is not the same as the 2018 weighted mapping with a skip penalty, nor the same as preserving a 2016 induced subgraph. The 2004 objective concerns the size of the common contracted ordered structure, and its recurrence depends on the order of siblings. Our five, four, and two point calculation does not carry across unchanged. It was designed to illuminate the two weighted Droschinsky models, not to sneak their scoring convention into Lozano and Valiente.

This is the first intellectual discipline the three papers teach together: the word subtree does not identify a unique mathematical relation. Before we can compare algorithms, or claim that one implementation solves another paper's problem, we have to say which substructures are admissible. We need a witness object, a validity predicate on that object, and an objective function. A beautiful recurrence for the wrong predicate is still the wrong recurrence.

## Three structures, three reasons dynamic programming works

For Lozano and Valiente, the input trees are ordered. Their balanced-word encoding preserves the nested structure of a rooted tree: an opening symbol records descent, a closing symbol records return. The decomposition families called D, R, and S organize a finite collection of remaining-word subproblems. The recurrence in Lemma 8 takes advantage of that decomposition. Its alternatives correspond to exhaustive ways the next portion of a common contracted structure can be retained or passed over. The critical proof has two directions. Every legal common contraction must fall into one of the recurrence cases; every recurrence case must assemble a legal common contraction. The table is correct because those two facts make the recurrence both an upper and a lower bound on the true optimum.

The encoding itself has a separate proof story. A balanced word represents a tree, but that fact alone does not prove an edge contraction corresponds to deletion of a matched parenthesis pair. The repository proves precisely that operational equivalence in `embeds_iff_dyckEmbeds`. It also finds a problem with the paper's printed recursive containment relation when interpreted literally as a least relation: a valid operational contraction is missing. The formalization does not resolve the discrepancy by quietly declaring the printed and operational relations equal. It proves their difference and uses the corrected operational relation where that is the intended mathematics.

That example should change how we think about formalization. A paper is not a sacred string of symbols to be transcribed. It is a proposed mathematical account. When a definition fails to express the examples and construction it was intended to capture, the first task is to expose the difference. The target of a correctness theorem must be an independent, coherent specification, not an implementation of a typo in the prose.

For the 2016 paper, unordered branches replace parentheses. A common subtree isomorphism selects connected induced subtrees and a structure-preserving bijection between their vertices. Each selected edge has to be an actual edge on both sides. Weights can reward or penalize mapped vertices and edges, and negative infinity can represent a forbidden pairing. At a pair of selected roots, different chosen child branches cannot reuse the same child on either side. That is precisely a partial bipartite matching constraint. Each candidate child-to-child pair carries the best score of the corresponding rooted descendant subproblem, together with the reward for keeping the connecting edge.

A partial matching is important. We need not match every child. With signed weights, an extra compatible branch can reduce the score; with forbidden weights, it may be impossible to choose. The optimum is not obtained by pairing children greedily in isolation, because each selected child occupies a resource needed by other candidates. The rooted recurrence is correct when a valid isomorphism decomposes into such a matching of independent child witnesses, and when any such matching permits its selected witnesses to be assembled without conflict.

The 2016 fixed-root lemma then explains a shortcut specific to strict subtree isomorphism. If we choose a root in one input tree, the selected connected physical subtree has a highest selected vertex. It is an actual vertex of the common mapping. This fact lets the unrooted optimum be represented by a suitably oriented rooted family. We can exploit the tree's geometry without losing any valid answer.

The 2018 paper permits an abstract edge to expand into a path. This changes the state invariant. A boundary vertex of a physical subtree may itself be mapped, or it may only be a skipped point on the way to a mapped vertex. The mapped and skipped states of Lemma 5 are not alternate programming styles. They correspond to different forms of admissible boundary witness. The mapped state still matches independent child branches. The skipped state descends through one continuing branch, charging the appropriate skipped-vertex penalty. A hidden junction serving three selected branches would violate path separation, so a skipped vertex on a realized abstract edge cannot be treated as an ordinary selected branching vertex.

The proof of the 2018 rooted recurrence again goes in both directions. From any valid witness, inspect whether its boundary is mapped or skipped and decompose it into smaller valid witnesses. Conversely, take a matching or skipped continuation from the recurrence, assemble the corresponding paths, and prove that no two abstract edges meet at an unselected branching point. Score additivity must then follow the exact direct-edge or penalty rule. This final condition is why it is worth keeping the independent score definition visible throughout the proof, rather than embedding the score inside code and calling the code the definition.

These three recurrences share a method but not a witness type. All three turn global optimization into local subproblems using a structural decomposition theorem. The decomposition tells us how to disassemble every feasible global solution. The assembly lemma tells us that the local answers can be combined without creating an infeasible global solution. The objective calculation tells us that the recurrence has neither invented nor lost any reward or penalty. From these ingredients, finite induction or a well-founded dependency argument can prove that the table computes the optimum.

## There are actually two correctness proofs

We often say that dynamic programming has been proved correct once its recurrence is derived. That is only half the job. The recurrence characterizes a mathematical value. A program has to evaluate those values in an order that respects their dependencies, or use a memoization mechanism that guarantees the same effect. It must handle empty candidate families, impossible matches, negative optima, and the base cases of the tree.

The existing 2018 formalization shows the distinction well. Its `skipped_recurrence_two_state` and mapped recurrence theorems relate independently defined optimum values to smaller optimum values. Its `RootedDynamicProgram.step_correct` is a conditional theorem: one step calculates the correct state if the dependent states already contain correct values. The finite-table arguments then justify sufficient evaluation rounds. Finally, `RootedDynamicProgram.solve_correct` identifies the solver's readout with the independent mathematical optimum. The conclusion is stronger than the recurrence alone because it closes the loop between local equations and the executable evaluator.

A useful way to visualize this is as two routes to the same answer. Along the mathematical route, start with a valid common-tree witness, score it, and maximize over all valid witnesses. Along the computational route, encode subproblems, fill a table, and read the selected entry. Correctness means both routes agree. The recurrence theorem relates the upper mathematical route to its smaller pieces. The induction and table theorem establish that the computational route follows those relations. Witness reconstruction adds a third route: not just a number, but a selected set of original vertices and paths whose score achieves that number.

There is a subtle logical separation between a correct score and a correct witness. A table can calculate the right optimum even if its choice pointers are corrupted. A set of returned node pairs can form a valid witness even if it is not optimal. An independent rescorer can detect invalid paths or incorrect scores, but cannot, by rescoring that one witness, prove that no better witness exists. This distinction becomes especially important when a proven mathematical recurrence is implemented by a fast Rust routine that stores compact choice records instead of whole proof objects.

The next separation is between functional correctness and speed. The reference implementation may repeatedly scan every matching or try every possible root and be mathematically unimpeachable. The paper's contribution may be a reorganization that avoids this repeated work. Proving the reference program correct does not prove the reorganized implementation correct, and proving both correct does not establish that the reorganized one uses the claimed amount of time and memory.

## The algorithm gets faster by remembering what changed

The two Droschinsky papers reuse a striking combinatorial fact. Suppose we have solved a weighted bipartite matching problem for the child branches of two vertices. Nearby tree states often ask us to solve essentially the same matching problem again, except that one right-side neighbor is forbidden because it leads back toward the parent in a different orientation. If we start over for every forbidden neighbor, we pay repeatedly for nearly identical searches.

Here is a small example, independent of any particular tree. There are two left choices, A and B, and three right choices, X, Y, and Z. A earns nine by matching X, seven by matching Y, and zero by matching Z. B earns eight with X, zero with Y, and seven with Z. The best partial matching in the full matrix assigns A to X and B to Z for a total of sixteen. If we delete Y, the same matching is still valid and still optimal. Nothing has to be repaired. If we delete X, the saved matching loses A's selected partner; a new optimum can assign A to Y and B to Z for fourteen. If we delete Z, the alternative A to Y and B to X scores fifteen.

The example exposes two different arguments. First, why may we reuse the original matching after deleting an unmatched right vertex? Every feasible matching in the reduced graph was already feasible in the full graph, and the saved optimum remains feasible with the same score. No reduced matching can beat an optimum of the larger feasible family. Second, why can we repair a matched deletion locally? Because only one previously occupied slot has been removed. A primal-dual matching algorithm can retain enough of its old certificate and adjust the assignment through a single augmenting-path repair instead of reconstructing every dual variable and matching choice from scratch.

The paper's analysis charges the repair work across the entire family of deletions, not separately as if every member were a new matching problem. A matching uses at most the smaller partition's number of vertices. Therefore at most that many right-side deletions can invalidate a saved matching. All other deletions reuse the base result. The rectangular algorithm and its dual potentials make the expensive cases manageable. When aggregated over vertex pairs in two trees, the tree degree-sum identity converts those local family costs into the paper's global bounds.

This is also where implementation details become mathematically consequential. The optimized Rust matcher stores an assignment state with row and column potentials, selected columns, predecessor data, and an orientation choice. Depending on which partition is smaller, a requested right-vertex deletion can appear to the assignment solver as deletion of a column or as deletion of a row in a transposed problem. A row deletion is not literally the same repair as a column deletion. In that branch, the code introduces a zero-cost dummy row and works with previously occupied columns. The repository already proves an exact ordered-arithmetic theorem showing when such a restricted repair is globally optimal. It does not follow that every floating-point operation in the production caller satisfies that theorem's hypotheses.

For the 2018 embedding algorithm there is a second form of reuse. We fixed a first-tree root to organize the dynamic program. But the highest physical point of a realized common edge might be skipped, rather than mapped. That breaks the simple fixed-root lemma from 2016. The 2018 paper repairs the loss of candidates by splitting the unrooted optimum into two structural families. One family has a highest mapped vertex. In the other, the highest physical point is an interior vertex of one abstract edge, and the embedding divides into two branches passing through distinct children. The efficient algorithm reuses rooted values to evaluate those cases without rerooting everything. Matching reuse and structural reuse work together.

A paper complexity proof counts these mathematical operations and how often they are required. The Lean repository has nontrivial complexity infrastructure, including memoization request and completion bounds, abstract cache work models, tree degree sums, and bounds on the number of retained matching pairs. But a program also performs vector initialization, index conversion, hashing, allocations, choice storage, and final witness reconstruction. Proving that a mathematical family contains at most a quadratic number of pairs is not yet a theorem about the peak allocated bytes of a particular Rust process. Similarly, an abstract expected hash operation or unit-cost arithmetic step is not the elapsed time of a compiled executable.

A fully specified performance claim needs an explicit cost model and a bridge from source steps to that model. It may prove a work bound on the operations executed by the source; it may establish a bound on allocations or live storage; it may separately justify an amortized cost for a data structure. These are worthwhile mathematical theorems. They should not be promoted into an unconditional claim about wall-clock seconds or physical memory without a model that supports that interpretation.

## What has already been achieved

It is easy, looking at a long list of remaining proofs, to overlook what the project already establishes. In the source snapshot accompanying this course, the 2004 branch proves the operational ordered-tree and balanced-word contraction equivalence, develops the decomposition recurrence and its optimum, and formally distinguishes the paper's printed recursive relation from the intended contraction relation. The ordered exact-rational isomorphism extension has a compiled Lean execution path with a theorem, `RationalSolver.solveResult_correct`, relating its memoized result to an independent specification under its stated domain. That is not the same as saying the entire 2004 Python-facing surface or its runtime is verified, but it is an actual algorithm-level proof.

The 2016 branch defines valid weighted strict subtree isomorphisms independently, proves existence of an optimum and the rooted matching recurrence, and proves correctness of an executable reference evaluator. The Lean repository contains mathematical matching, copied-assignment, dual and deletion-repair results, as well as source-level correctness theorems for designated exact-integer Rust matching functions. Those theorems have specific input domains and error conditions. They do not silently certify the optimized floating-point tree solver that calls a different matching representation.

The 2018 branch has an independent path-embedding specification, explicit direct-edge and skip-penalty scoring, sound mapped/skipped recurrences, and a correct reference solver with an all-roots unrooted optimum. It has not yet established the optimized fixed-first-root structural reduction, the full production scheduling invariants, or the published source-level work and space theorem. Its reference evaluator is therefore a correctness anchor, not a completed proof of the faster implementation.

This is a good moment to remember why we insist on an independent specification. If the specification just repeats the Rust code in different syntax, proving their agreement may show no more than that the transcription was faithful. The independent witness definitions make it possible to detect a wrong path convention, a hidden branching point, an omitted negative optimum, or an off-by-one skip penalty even when two implementations share the same bug. They also give us something stable against which several algorithms, including exhaustive references and optimized versions, can be compared.

We can now ask how to turn the open boundaries into a realistic mathematical program. I will choose three proof obligations, each with a distinct shape: one is a theorem about trees, one is a theorem about a program's data representation, and one is a theorem about the meaning of an answer returned to a user.

## First workshop: the root that was never selected

The first target is the 2018 optimized unrooted reduction, corresponding to the structural ideas behind Lemmas 9 through 11. Fix a root in the first physical tree. The reference solver knows how to maximize over all possible roots. We want to show that the same global optimum is captured by just two families of candidates: the best rooted embedding whose highest physical vertex is selected, and the best split embedding whose highest physical vertex is skipped on a realized abstract edge.

The theorem we want is simple to say: for every legal input pair and every choice of first-tree root, the independently defined unrooted optimum equals the maximum of those two candidate-family optima. A statement that a particular Rust function returns this maximum is a later theorem. We should first make the two families mathematically precise and prove the identity for the independent witness relation.

Start with the upper-bound direction. Take any candidate from the rooted family. Its rooted witness can be forgotten to produce a valid unrooted witness. Now take any candidate from the split family. It consists of two rooted boundary witnesses, with distinct first-tree child origins, and corresponding opposite-side components in the second tree. Join them by one abstract edge passing through the central skipped first-tree vertex. The proof must establish that the two physical realizations meet only where allowed, that the joined common graph is still a tree, and that the central vertex is not secretly used as a branching point. Then calculate the score. The two subproblem scores are added, and the skipped central vertex is charged exactly once. The connecting abstract edge cannot claim a direct-edge reward because one of its realized paths already has at least two edges. Each assembled candidate is valid, so neither candidate family can exceed the true optimum.

For the other inequality, start with an arbitrary optimal unrooted witness. Consider the union of its realized paths in the first input tree, and take the highest physical vertex with respect to the fixed root. There is a unique highest vertex because the realized set is connected. If it is mapped, orient the abstract common tree there and place the witness in the rooted family. If it is not mapped, it must lie in the interior of a realized abstract edge. The two sides of that edge descend into two different child branches. Path separation forbids a third selected branch from passing through the same skipped point. Cut the abstract edge, choose an appropriate separating physical edge in the second tree, and identify the two smaller rooted witnesses. This puts the original optimum into the split family, with precisely the same score after the central penalty is restored.

There is real work concealed inside each sentence. The unique highest vertex needs a theorem about connected subtrees of rooted trees. The skipped case needs path-separation lemmas. Cutting and rejoining needs an explicit relation between common-tree vertices, selected pairs, and physical path interiors. The proof cannot declare that the pieces are independent merely because they were drawn in separate boxes. It must establish disjointness and preserve every score contribution. Ties and empty intermediate candidate sets need defined maximum conventions.

Once that structural identity is proved, the cardinality-two optimization becomes approachable. If two component candidates must use distinct first-tree child origins, a best-one and best-two summary can answer the exclusion query, provided those two representatives have distinct origins. The proof has to handle several equal best scores and an instance with fewer than two eligible origins. It is tempting to write a theorem called 'top two works'; a useful Lean theorem should say exactly which candidate family was maximized, which origin was excluded, and how a returned representative realizes the optimum.

This is the most self-contained of our three projects. It is about finite trees and witness geometry. It does not need PyO3, floating-point rounding, or Hungarian implementation arrays. It would close a major mathematical link between the independent 2018 specification and the faster unrooted algorithm.

## Second workshop: the assignment that survives the deletion

The second target is the optimized right-deletion matching family in Rust. We want more than a numerical comparison with a reference solver. We want a theorem that says each returned matching is a valid optimum for the corresponding original-index problem after one named right vertex is removed, including the case where the output reuses the original matching without constructing a separate result.

Begin above the source code. Define an independent weighted partial-matching optimum for a finite matrix of permitted pairs. Define its right-deletion family by deleting one named right index from the permitted set. The existing Lean theorem `deletionFamily_correct` proves a reference mathematical family correct, and `IsMaximum.deleteRight` handles the unmatched-deletion case. These are reusable pieces of our target proof, not promises about the production implementation.

Next describe the representation invariant for the actual optimized assignment state. Its arrays encode a partial assignment with no repeated occupied columns. Its row and column potentials satisfy a feasibility inequality against the represented cost matrix. Selected assignment edges are tight, meaning their cost agrees with the corresponding sum of dual values. The state remembers which physical row and column each compact index denotes, especially if the rectangular problem was transposed. The sentinel and predecessor entries obey bounds and represent a valid alternating search frontier. An iteration may update potentials and change assignments, but it must preserve these properties.

For an unmatched deletion, correctness is nearly free once the original state is certified: reuse retains a valid optimum. For a matched deletion, one assignment position is freed. We want a repair theorem saying that one authorized augmentation restores a valid tight matching and a feasible dual certificate for the reduced problem. Weak duality then supplies optimality. The direct orientation removes a column and repairs its freed row. The transposed orientation replaces a removed row with a dummy, restricts repair to previously occupied columns, and requires the theorem justifying why that restricted solution is also globally optimal in the full rectangular instance. The repository's `transposed_repair_global_minimum` is a mathematical result aimed at that last difficulty. It still needs a source-refinement bridge showing the production array operations establish its hypotheses.

Consider again our two-by-three example. The full optimum scores sixteen using X and Z. Deleting Y should return the same original-index matching. Deleting X should return A with Y and B with Z for fourteen. Deleting Z should return A with Y and B with X for fifteen. A source theorem must say which original labels appear in those results, not just that some compact indices add to the right weight. The transposed representation cannot be permitted to exchange the roles of left and right endpoints in the decoded witness. This apparently mundane bookkeeping belongs inside the statement being proved.

The hardest choice is numerical. Lean's exact ordered-arithmetic matching theorems are not, by themselves, theorems about arbitrary IEEE floating-point calculations. A source proof might begin with a restricted exact-integer path, carry an invariant over nonoverflowing machine integers, or define a faithful floating-point semantics that is weaker than exact real-number optimality. The sensible approach depends on which backend we intend to certify. We should not accept a hidden assumption that floating-point addition preserves every comparison in an arbitrary signed weighted matching problem.

Correctness alone would still not prove the paper's speedup. The companion work theorem must count the saved base assignment, the limited number of affected deletions, augmenting-path steps, potential updates, array initialization and copying. The logical bound that at most the smaller partition's many right vertices are matched is already proved. The rest needs a source-oriented cost contract and an accounting of what the concrete loops do. The space result needs a separate bound on live arrays and stored choices. A family of outputs that holds on to full copied assignment matrices may have a different memory bound from one that records only changes and shares the base state.

This proof project is more difficult than the structural root split because it crosses abstraction layers. That is also its value. The same matching-family component is useful to both Droschinsky algorithms, so a precise source refinement could discharge a repeated obligation instead of proving two nearly identical low-level engines independently.

## Third workshop: the result with Alice's name on it

The third target starts at the Python boundary. Suppose a user passes two NetworkX trees containing nodes that are strings, tuples, or custom hashable objects. The Python wrapper assigns temporary integer indices, collects compatibility and weight tables, calls a backend, and decodes the result. We need a theorem connecting the returned original objects and paths to the independent graph-level witness specification.

This can begin with a narrower statement than optimality. Assume the backend returns a valid indexed witness. Prove that decoding its vertex pairs yields pairs of actual input nodes, that no original node is used twice on either side, and that every returned path is the unique path in the corresponding original input tree between its selected endpoints. Prove that path interiors are exactly the skipped vertices and that there are no hidden branching conflicts. Finally, prove that rescoring the decoded witness from the original, already-evaluated callback tables gives the same mathematical score as the indexed witness. This theorem is valuable even if the optimized backend remains unproved, because it separates correct interpretation of an answer from the unresolved claim that the answer is best possible.

A second small theorem can handle the empty-solution convention. The paper specifications typically concern a nonempty common tree. The public API may allow the empty answer with score zero. If a solver returns a genuine best nonempty witness, the wrapper must select the empty answer exactly when the documented option and score comparison require it. An absent feasible nonempty witness is not the same as a feasible witness whose best score is negative. A correct wrapper proof needs both branches, rather than using zero as a convenient stand-in for failure.

A third theorem can handle backend selection, input rejection, and numeric conversions. The ordered exact-rational Lean backend is a distinct path with its own checked solver theorem and JSON transport. The unordered fast Rust functions use floating-point score tables and a PyO3 interface. The fact that a wheel imports across Python versions says something about distribution compatibility, not about its optimizer's mathematical result. A claim about the public function must name which backend ran, which arithmetic contract applied, and what was done when the backend was unavailable or an input was invalid.

Only then do we compose the larger statement. Assume encoding maps each legal original graph instance to an equivalent indexed mathematical problem. Assume a specified backend returns an optimal indexed witness under a stated arithmetic semantics. Assume decoding preserves validity, paths, score, and the documented empty policy. These premises imply that the returned Python witness is optimal for the original instance under that semantics. The composition proof can be short because each change of representation has already been explained and proved. It does not erase the trusted compiler, interpreter or runtime boundary, and it does not make a theorem about one backend apply to another.

This last project is conceptually close to the reason one writes software in the first place. The user does not ask for a `Fin` index or a pointer into a Rust vector. The user asks which vertices of their two trees correspond. A complete theorem should end with that answer, rather than stopping at an internal optimum that cannot yet be connected to the returned node objects.

## How a large proof becomes a sequence of small ones

Our three workshops are connected, but they are not forced to wait for one another. The 2018 structural reduction can be proved against the independent witness definitions without touching Rust. The deletion-family theorem can be developed against an independent matrix optimum without knowing anything about NetworkX. The decoding theorem can assume an indexed witness is valid without claiming that the producer is optimal. Each result closes a compositional gap. Later we can combine them with the reference dynamic-programming correctness theorem, a correct optimized schedule, a verified source implementation, and an explicit numerical and resource contract.

There is a useful order to the reasoning. Prove the object is valid before proving it is optimal. Prove the recurrence before proving the table evaluator. Prove the table evaluator before claiming the optimized schedule realizes the same entries. Prove assignment repair before claiming every family of deletions is optimally computed. Prove output indices correspond to the original objects before calling the Python result a verified witness. And prove a concrete cost model before turning a mathematical count of states into a statement about an executable's runtime.

These are not bureaucratic proof milestones. Each one prevents a characteristic mistake. Without an independent validity predicate, a shared bug can masquerade as agreement. Without the reverse direction of a recurrence, an algorithm may omit its best witness. Without a dependency-order proof, a correct recurrence may be evaluated with stale values. Without an arithmetic scope, an exact optimum theorem may be applied to rounded computations. Without an index-reconstruction theorem, a correct internal solution may name the wrong vertices. Without a resource model, a quadratic number of states can hide much larger copying and allocation costs.

The project already offers a practical starting set of theorem names to inspect. For ordered contractions, `embeds_iff_dyckEmbeds` makes a mathematical representation equivalence explicit. For the 2016 recurrence, `rooted_matching_recurrence` connects strict tree witnesses to partial child matching. For 2018, `skipped_recurrence_two_state` and `RootedDynamicProgram.solve_correct` separate mathematical recursion from executable evaluation. For matching-family reuse, `deletionFamily_correct` and `transposed_repair_global_minimum` tell us which exact mathematical facts have already been checked. For complexity, `roots_weighted_work_envelope` and `tree_family_pairs_le` distinguish abstract operations and storage from actual source work. For the ordered rational execution path, `RationalSolver.solveResult_correct` shows what a source-oriented optimality endpoint can look like when arithmetic and the computation are both specified carefully.

The words 'already proved' in that list refer to the supplied repository snapshot. They do not guarantee that a declaration still has the same hypotheses after later edits, nor do they expand the theorem beyond its printed type. For any new proof, the authoritative object is the current elaborated Lean statement and the current source program, not a summary from an earlier planning note.

The course began with the deceptively simple question of finding a common subtree. Its lasting lesson is that a mathematical answer has several kinds of identity. It is a shape with legal relations to two input trees. It is a witness satisfying an independent predicate. It is an optimum under a particular score. It is a value produced by an algorithm whose invariant and evaluation order are justified. It is a collection of actual source-level choices, using actual numbers, time and memory. And, when it reaches a user, it is a mapping back to the original objects the user supplied.

The reward for keeping these identities distinct is that we can connect them rigorously. The three papers give us the structural insight. The Lean development gives us a growing body of checked mathematics and source results. The Rust and Python code give the ideas practical form. The remaining work is not an amorphous demand to 'verify everything.' It is a set of theorems whose hypotheses and conclusions can be stated, challenged, and proved one at a time. When enough of those theorems compose, the program's claim becomes as precise as its mathematics.

That is a satisfying place to conclude this course, and a practical place to begin the next proof.

<!-- END SPOKEN LECTURE -->

## Companion: three concrete proof-development targets (not narrated)

**Source snapshot.** The observations here refer to the user-supplied `networkx_algo_common_subtree` archive dated **2026-11-19**, not to an automatically refreshed checkout. The theorem-interface names and sketches below are *proposals*. They are **not** declarations that were added, compiled, or proved as part of this lecture pack.

### The common mathematical picture

For a specified model `P`, define:

- `Valid_P(T,U,w)`: `w` is an admissible nonempty common-tree witness, including ordered contraction, strict induced isomorphism, or topological path realization as appropriate.
- `Score_P(T,U,w)`: the independent score on witnesses of that model.
- `Opt_P(T,U) = max { Score_P(T,U,w) | Valid_P(T,U,w) }` (or the model's bottom/optional-value convention).
- `Refines(encode, algorithm, decode, P)`: successful returned indexed witnesses decode to independent witnesses of `P`, with the intended optimum and score under the declared arithmetic semantics.

These are **schematic** mathematical interfaces; they are not meant to compile as Lean verbatim. In particular the three papers do not share one witness type, root policy or score codomain, and a nonempty optimum may require a bottom element when no witness exists.

### Target A — 2018 optimized unrooted split

**Mathematical statement to prove:** For any valid 2018 finite-tree instance and any chosen first-tree root `r`,

\[
\operatorname{Opt}_{\mathrm{unrooted}}(T,U)
=\max\bigl(M_1(T,U,r),\,M_2(T,U,r)\bigr),
\]

where `M1` ranges over rooted solutions with highest first-tree physical vertex selected, and `M2` over two admissible rooted components glued across one **skipped** highest physical vertex, with different first-tree child origins, the proper second-tree separating edge, and exactly one extra central skip penalty.

**Proof decomposition:**

1. Define the realized image of a common-tree witness as a connected physical set; prove that a fixed ambient root gives it one highest vertex.
2. If highest is mapped, construct an `M1` candidate without changing score. If highest is skipped, prove it is interior to exactly one abstract edge (by path-separation) and lies between exactly two selected sides; split into `M2` components and prove score conservation.
3. From either candidate family, assemble a valid independent unrooted witness, including path-interior disjointness and exact direct-edge/penalty accounting.
4. Prove an exclusion-max lemma: if combining two candidates requires distinct child origins, the two best representatives with distinct origins suffice for each excluded origin; handle ties, bottom values and small sets.

**Existing source anchors:** `Droschinsky2018/Specification.lean`, `PointedWitness.lean`, `OverallOptima.lean` (`unrootedValue_eq_max_rerooted_mapped`), `RootedDynamicProgram.lean` (`unrootedOptimum_correct`), and `rust/crates/common_subtree_algorithms/src/tree.rs` (`compute_embeddings`). The all-roots theorem is **not** the proposed fixed-root M1/M2 theorem. The statement crosswalk records the structural and optimized source links as open.

### Target B — optimized rectangular deletion-family source refinement

**Mathematical statement to prove:** For any supported indexed weight matrix and every original right index `j`, the production `WeightedMatchingFamily` base or deletion output, decoded in original indices, is an optimal feasible partial matching in the matrix with column `j` forbidden. The statement must quantify over orientation, input shapes, exact numeric domain/error behavior, and the treatment of a reused `None` family entry.

**Intermediate invariants:**

- Encoded `AssignmentState` is a partial injective row-to-column choice, with valid bounds, one origin mapping for every compact row/column and permitted selected edges.
- Row and column potentials are dual feasible; selected edges are tight, with the correct sign and cost-vs-weight transformation.
- Deleting an unmatched right vertex preserves the base optimum (`IsMaximum.deleteRight`).
- Deleting a matched column leaves a one-deficit state whose augmentation is feasible, tight and optimal.
- In the transposed case, dummy-row replacement, old occupied-column restriction, and original-column projection meet the hypotheses of `transposed_repair_global_minimum`.
- Each family result has exact original-index witness reconstruction and correct weight; absent family slot means **reuse**, not infeasibility.

**Existing anchors:** `Shared/MatchingDeletion.lean` (`deletionFamily_correct`, `deletion_repair_card_bound`), `Shared/CopiedMatchingDeletion.lean`, `Shared/CopiedMatchingRepair.lean`, `Shared/TransposedMatchingDeletion.lean` (`transposed_repair_global_minimum`), `Rust/MatchingDeletionEntrypoint.lean` (`max_weight_matching_deletions_total_spec` for the exact-integer reference), `Rust/SparseDeletionEntrypoint.lean` (`repair_deleted_sparse_vertex_spec` for a conditional exact caller), and `rust/crates/common_subtree_algorithms/src/matching.rs` for the optimized `f64` family. The first two Rust claims do **not** certify the final `f64` source function.

**Cost obligation, separate from correctness:** Derive one base matching plus at most `min(left,right)` actual repairs, charge every augmentation and state/copy operation under a declared source cost model, and aggregate over the tree-degree families. `Complexity/MatchingFamilies.lean` bounds tagged retained matching pairs; peak Rust allocation and time/space execution remain separate theorems.

### Target C — NetworkX original-node and path decoding

**Conditional statement to prove:** For any legal 2018 original-graph input and any *valid* indexed embedding witness returned by the designated backend, decoding its node pairs and realized paths yields a valid independent original-graph embedding, including injectivity, unique physical paths, path interior separation, original node identities and exact score correspondence under the declared numeric semantics. This statement can be proved **without** assuming the backend is optimal.

**Proof decomposition:**

1. Prove the index maps are injective and encode graph edges/paths faithfully; preserve callback compatibility and scores (including `None` as forbidden, not zero).
2. Prove indexed common-skeleton paths decode to the unique paths between original input nodes, preserving skipped interiors and no-hidden-branching constraints.
3. Prove the independent score agrees with decoded tables for selected vertices and direct-edge or skip-penalty contributions.
4. Prove the `allow_empty` policy: a negative feasible nonempty optimum differs from no feasible witness, and the score-zero empty result is selected precisely under the public option.
5. Compose with *a separately proved backend optimum* and explicit arithmetic/backend-selection assumptions to obtain a public API optimum theorem. Document which transport, runtime and packaging behavior is tested rather than formally modeled.

**Existing anchors:** `networkx_algo_common_subtree/unordered.py`, `rust/src/graph_bindings.rs`, `Droschinsky2018/Specification.lean`, `Droschinsky2018/Witness.lean`, `Droschinsky2018/RootedDynamicProgram.lean`, `Paper2004/RationalOrderedSolver.lean` (`solveResult_correct` for the **separate** ordered exact-rational backend). The source snapshot's Python/PyO3 conversion is tested, not yet covered by the proposed original-graph theorem.

### A proof-dependency sequence

```text
Independent graph/tree specification
       |
       +--> structural decomposition and recurrence
       |         |
       |         +--> correct reference table and witness
       |         |
       |         +--> optimized unrooted M1/M2 theorem (Target A)
       |                   |
       |                   +--> optimized table schedule correctness
       |
       +--> independent matching specification
                 |
                 +--> reference + mathematical deletion theorems
                 |
                 +--> optimized Rust family refinement (Target B)
                                   |
                                   +--> source work and memory cost

Indexed witness + original graph representation
       |
       +--> encode/decode validity and score (Target C)
                 |
                 +--> backend optimum + numeric contract
                           |
                           +--> documented public API guarantee
```

The arrows describe needed logical composition, not a claim that every node is already proved. In particular, neither `f64`-to-real optimality nor physical peak-memory bounds follow from exact arithmetic or mathematical state-count results.

**Primary sources:** Lozano and Valiente (2004), *On the Maximum Common Embedded Subtree Problem for Ordered Trees*; Droschinsky, Kriege, and Mutzel (2016), *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*; Droschinsky, Kriege, and Mutzel (2018), *Largest Weight Common Subtree Embeddings with Distance Penalties*. Pinned editions and links are in `metadata/sources.json`. **Verification ledger:** `docs/planning/paper_statement_crosswalk.md` and `proofs/PROOF_STATUS.md` from the uploaded 2026-11-19 repository.
