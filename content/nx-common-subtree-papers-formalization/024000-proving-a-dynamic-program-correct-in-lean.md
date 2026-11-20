# Proving a Dynamic Program Correct in Lean: From Witnesses to a Finished Table

<!-- BEGIN SPOKEN LECTURE -->

Suppose you have found the right recurrence for a tree problem. You can explain every branch of it, and perhaps even prove that the answer at one pair of vertices follows from the answers at the smaller pairs. You implement the recurrence, run it on a few small trees, and it returns the expected answer. Have you proved the program correct?

Not yet. You have proved something about a mathematical equation, perhaps something about one table update, and observed something about a program. The claim we ultimately want is stronger: for every admissible input, the table actually produced by the program contains the independently defined optimal answers. The missing argument is not a minor technicality. It is the argument that connects an equation involving ideal answers to a finite process that begins with an empty table.

The Droschinsky 2018 formalization gives us a precise example. Its rooted problem has two states at each pair of vertices. It proves the recurrences against independently defined common-tree witnesses. It then defines a reference evaluator, proves one step correct when the values it depends on are correct, and proves that a finite number of rounds makes every required value correct. We can read the entire chain. Along the way, we will see why negative infinity is a genuine state value, why dependencies descend in either one tree or both, and why a synchronous table can be easier to verify than a faster in-place implementation.

## The answer does not live in the table

Start by separating two objects. On one side is an independently specified optimization problem. Choose an actual common tree, embed it into both input trees, respect the rooted boundary conditions, charge the weights and distance penalties, and take the maximum score over the feasible choices. This defines an optimal value without any reference to a dynamic-programming table. On the other side is a program that works with finite lists of vertices, pairs of vertex identifiers, and previously computed numbers.

In the Lean development, the independent boundary optima are named `mappedValue` and `skippedValue`. Their definitions ultimately refer to `StateValid`, `stateScore`, and finite families of mathematical witnesses. The reference program does not define these values. It is supposed to calculate them.

The two states distinguish what happens to the current pair of boundary vertices. A mapped state maps the current vertices to each other. A skipped state keeps an actual common-tree witness below the current boundary but does not map both boundary vertices as the current top pair. The second state is essential because a common-tree edge can travel along a path rather than a single input edge. One physical step downward may incur a penalty before we arrive at the next mapped vertex.

We represent each numerical value using a type with an additional bottom element. Bottom means that no feasible witness of the required kind exists. It is not zero. Zero is a perfectly legitimate finite score; a legal common-tree witness may have score zero, minus five, or any other allowed signed value. If we confused bottom with zero, an impossible continuation could compete with a legal continuation, and we could accidentally construct an answer containing an edge or path that is not permitted.

The independent `sourceState` in the Lean file is a pair: first the mapped optimum, then the skipped optimum. The table is supposed to store that pair for every vertex pair. Notice the strength of this target. We are not proving that one especially interesting output number is plausible. We are asking every stored state to equal a mathematical maximum taken over actual trees and embeddings.

## The two recurrences, spoken slowly

Fix roots for the two input trees, and examine vertices u and v. The mapped recurrence starts with the weight for mapping u to v. Its remaining contribution is an optimal partial matching between their immediate children. A matching can leave a child unused, and it cannot pair the same child twice.

What weight does a potential child pair c and d receive? There are two possibilities. If the next common-tree edge is realized as one actual edge in each input, we receive the direct-edge reward and continue in the mapped state at c and d. Alternatively, the common-tree edge may have a longer realization, in which case the continuation is represented by the skipped state at c and d; the path penalties have already been accounted for in that state's score. We choose the better of those alternatives before the matching optimizer selects a compatible collection of child pairs.

The skipped recurrence looks different. It descends one immediate edge in the left input, holding the right boundary vertex fixed, or descends one immediate edge in the right input, holding the left vertex fixed. Either descent incurs one skipped-vertex penalty. After that step, the continuation may be mapped or skipped. The best score over all such descents becomes the skipped value for the current boundary pair.

We do not need to descend in both inputs simultaneously in this recurrence. The complete structural proof shows that an eligible skipped witness can be reduced by one step on at least one side. Repeated steps can represent a longer path. The rule charges the penalty at each step, rather than guessing a path length and subtracting it all at once. This one-step formulation is particularly useful for a dependency proof.

These rules are not invented by the executable evaluator. They are established as theorems. The mapped identity is `mapped_recurrence`. The skipped identity is `skipped_recurrence_two_state`. Their proofs depend on decomposing all legal witnesses and constructing legal witnesses from the chosen branches. That mathematical work has to be in place before an implementation proof can appeal to these equations.

## A four-state example

Let's give the program a tiny input. The left tree has a root P with one child C. The right tree has a root Q with one child D. Every tree has two vertices and one edge. Let the penalty for one skipped vertex be two points.

Assign four node-pair weights. Mapping P to Q earns three. Mapping C to D earns five. Mapping P to D earns one. Mapping C to Q earns zero. If the left edge from P to C is matched directly to the right edge from Q to D, award four more points. There is only one edge on either side, so that is the only direct-edge reward we need.

First consider the two leaves C and D. They can be mapped for five points, but neither has a child to skip to. Their state is therefore: mapped five, skipped impossible. This is the base case, obtained from the same recurrence as every other case. The partial child matching is empty and has weight zero. The skipped state tries to descend, finds no legal choice, and stays at bottom.

Next look at P and D. D has no child, so there can be no child matching extending the mapped pair. The mapped score is simply one. But the skipped state can move from P to C, paying two points, and then map C to D for five. Five minus two is three. Thus the state for P and D is mapped one, skipped three. By symmetry of the example's chosen weights, C and Q has mapped zero and skipped three.

Finally examine P and Q. In the mapped state, map those roots for three points. We may also match their children, C and D. That branch has direct-edge reward four plus mapped continuation five, so it contributes nine. The complete mapped value is three plus nine, or twelve. There is no advantage to omitting that positive branch.

For the skipped state at P and Q, move down on one side. Descending left gives the best of the mapped and skipped values at C and Q, which is three. Descending right gives the best at P and D, also three. Subtract the one-step penalty two. The skipped value is one. Our four independent target states are now clear: C,D is five and bottom; P,D is one and three; C,Q is zero and three; and P,Q is twelve and one.

That calculation already tells us something about the dependency graph. The state at P,Q uses the mapped child pair C,D, and its skipped half also uses C,Q and P,D. The state at P,D uses C,D. The state at C,Q likewise uses C,D. No state in this example needs to know its own answer in order to calculate itself. If we can place these dependencies in a strict order, evaluation can terminate and be proved correct.

## One update needs a hypothesis

Open `Droschinsky2018/RootedDynamicProgram.lean`. Its `step` function takes explicit child lists, the scoring function, the one-step penalty, a function providing the previous table's values, and the vertex pair u,v. It constructs the matching matrix, asks an exhaustive partial-matching routine for a matching, and returns the mapped and skipped numbers described above.

The theorem `step_correct` is the bridge from that code to the independent optimum. Its crucial hypothesis is not that every entry in the entire preceding table is correct. It requires correctness at exactly those pairs on which the current update can depend. In the source, the relation has the name `RootedEvaluationOrder.Depends`.

A dependency is one of three shapes. Descend in the left tree only, descend in the right tree only, or descend in both. Those are exactly the possibilities read by the two-state update. If the previous table has correct independent values at all pairs of those shapes, then `step` at u,v equals `sourceState` at u,v. That is the local correctness theorem.

The proof has several separate jobs. First it shows that the program's child-weight matrix equals the mathematical matrix used in the mapped recurrence. It does so entry by entry. For a legal pair of children, it invokes the previous-table hypothesis to replace the stored continuation with the independent one. For an illegal pair, both matrices declare that pair forbidden. The formal result is equality of functions, not just agreement on a chosen test matrix.

Next it proves that the matching selected by the executable exhaustive optimizer is optimal for this exact matrix. Here the program receives a finite list, constructed as the product of the two child lists. The proof needs to show that every compatible child pair appears in that list. It does not need to enumerate impossible pairs, because the matching's admissibility predicate excludes them. The shared theorem `exhaustive_correct_of_allowed_complete` is built for precisely this purpose.

Then the proof handles the skipped state. Its code takes a maximum over the left-child list and another over the right-child list. The mathematical recurrence uses finite sets. The proof establishes that the lists describe exactly the true children, converts list maxima to finite-set suprema, and replaces previous-table entries with independent values using the corresponding dependency hypotheses.

At the end it uses equality of pairs, often called product extensionality. One component is the mapped recurrence; the other is the skipped recurrence. That completes `step_correct`. Notice what we still do not have: the hypothesis about the previous table has not been established for any particular execution. We have proved a rule for transferring correctness from dependencies to a parent, not that the dependencies are already correct.

## The rounds start with nothing

The generic module `Shared/FiniteTable.lean` supplies the next bridge. It defines an association-list table and a function called `rounds`. With zero rounds, the table is empty. With one more round, the program constructs a fresh table by evaluating every listed key against the table produced in the preceding round. Reads of missing keys return a supplied fallback value. For our two-state problem, that fallback is bottom in both components.

The word *synchronous* is useful here. A round reads only the preceding round's table, even as it constructs a new table for every pair. The computation does not depend on the iteration order of the key list inside a round. That choice may repeat work, but it gives the proof a simple shape: the update at rank r only needs values from earlier ranks, and enough rounds will make those values available.

In our example, round one makes the leaf pair C,D correct. The pair P,D still has its initial mapped one but has not yet received the skipped continuation worth three. The pair C,Q is in the same situation. And the pair P,Q cannot yet see the five-point mapped child. Round one is not a fixed point and does not need to be.

In round two, C,D is still correct. P,D and C,Q now obtain skipped value three because they can see C,D from the previous round. P,Q also obtains its mapped value twelve because its direct branch depends on C,D. Its skipped value is not yet correct: it sees the incomplete skipped values at P,D and C,Q from round one. It can achieve only minus one in that component, rather than the final value one. In round three, the two intermediate states are already correct, and P,Q obtains skipped value one. All four states now agree with the independent optima.

Here we have a useful warning against a common intuition. A round may contain some correct components and some incorrect components. The theorem does not say that the table is globally correct after any arbitrarily chosen number of iterations. It gives a sufficient number of rounds for a specific query, based on a rank.

## Rank is the missing induction measure

How can Lean know how many rounds are sufficient? In `Shared/RootedEvaluationOrder.lean`, the development defines the depth of a vertex from the fixed root as the length of the unique root-to-vertex path. It takes the maximum depth over all vertices, and subtracts the depth of the current vertex from that maximum. This creates a rank that decreases as we move downward through the rooted tree.

For a pair u,v, the combined rank is the sum of the two individual ranks. Descend in the left tree and the left contribution strictly decreases. Descend in the right and the right contribution strictly decreases. Descend in both and both decrease. Thus every dependency of a table entry has a strictly smaller nonnegative rank.

Our two small trees have maximum depth one. Their leaf vertices have remaining-depth rank zero; their roots have rank one. The combined ranks are zero for C,D, one for C,Q and P,D, and two for P,Q. Those are exactly the levels visible in the three evaluation rounds.

The source proves a rank-decrease theorem for all three dependency shapes, and then a well-foundedness theorem for the dependency relation. It also proves a size bound: the combined rank is strictly less than the number of left vertices plus the number of right vertices. The reason is that a simple path cannot traverse more edges than the tree has vertices minus one. Summing those two facts gives a universal, computable upper bound on the rounds needed.

The generic theorem `FiniteTable.rounds_correct` packages the induction. Assume that the key list is complete, that dependencies strictly decrease a rank, and that a single update gives the right target whenever all dependencies have the right target. Then after more rounds than a queried key's rank, reading that key from the resulting table returns the target value. The proof is induction on the number of rounds. In the successor step, it invokes the one-step update theorem. Every needed child has smaller rank, so the induction hypothesis supplies its correct value in the previous round.

There is a delicate but valuable design point here. The proof does not assume that the table update reads only earlier-ranked entries in a syntactic sense. It assumes its *result* is correct when the specified dependencies are correct. A computation could read an additional irrelevant entry without invalidating the theorem, so long as the additional read does not affect the answer. The dependency relation captures semantic dependencies relevant to the local correctness argument.

## From a conditional step to a public function

The tree-specific theorem `evaluate_correct` applies the generic induction to the mapped/skipped evaluator. It supplies the independent `sourceState` as the target, the three-way tree dependency relation, the rank theorem, and the already proved `step_correct` as the update rule. It requires a complete list of vertex pairs and enough rounds for the queried pair.

The next theorem is `solve_correct`. This is where the public reference table constructor discharges those premises. The caller supplies two lists that contain every vertex in their respective trees, along with child-list functions whose membership exactly describes the mathematical child relation for the chosen roots. The function `solve` forms the product of the vertex lists and runs as many rounds as the sum of their lengths. The proof shows that this product contains every pair, that list lengths bound finite vertex counts, and therefore that the chosen fuel exceeds every required rank. It then invokes `evaluate_correct`.

At last we have an unconditional statement about that particular reference computation, under input-representation hypotheses: when the child lists and vertex lists represent the actual finite trees, reading any state from `solve` gives the independently specified mapped and skipped optimum for that pair. The program is allowed to use exhaustive matching and repeated rounds. It does not have to be fast for this theorem to be meaningful.

Two higher-level theorems read out the values. `rootedOptimum_correct` takes the maximum of mapped entries over all vertex pairs in fixed ambient orientations and proves equality with the independent rooted optimum. `unrootedOptimum_correct` reroots both inputs and evaluates the designated mapped entry for each root pair. It proves the unrestricted optimum of the independent topological-embedding specification. This is a correct but expensive baseline, not the optimized fixed-root construction from the 2018 paper.

## How an optimized proof would differ

The reference evaluator spends considerable effort on simplicity. It recomputes every table key over multiple rounds. It asks an exhaustive matching routine to search subsets of child pairs. That supplies a clean source of correctness but not the time bound the paper proves for its optimized algorithm.

A faster evaluator might schedule each state only after its actual dependencies have been computed, reuse a matching after one child deletion, and maintain compact arrays of score and choice information. To verify that program, we need another invariant. One option is to say that every state marked complete equals its independently specified value, and every reference made by the next update points to an already complete dependency. The proof then studies the scheduler: which states become complete, whether a state can be read too early, whether the matching-family reuse preserves the local optimal value, and whether all necessary states are eventually reached.

The generic rank argument is reusable intellectual machinery, but it does not automatically validate a different schedule. In particular, the optimized unrooted 2018 algorithm has a structural case distinction that the all-roots baseline avoids. Proving a correct rooted table would still leave the highest-vertex decomposition, the right-view representation, and the matching-reuse schedule to be connected to the global optimum.

There is also a separate question about witnesses. The reference score table proves numbers, not a returned map of original input vertices and paths. A source program may record choices and reconstruct an answer, but its correctness needs a theorem saying those choices form a feasible common-tree witness and that its score equals the optimum just computed. That is not a consequence of storing correct scores alone.

We can now read a dynamic-program correctness claim without confusing its layers. The independent witness definition gives the target. The recurrence proof establishes the mathematical identity. `step_correct` establishes a conditional implementation step. The rank theorem establishes a descending dependency relation. `rounds_correct` turns those facts into induction on a finite computation. `solve_correct` removes the remaining scheduling and enumeration premises for the reference solver. The optimum-readout theorems connect table entries to the full rooted or unrooted problem.

That chain is the proof, not a single magical tactic. More importantly, it gives us a template for new formalization work. If a proposed optimization does not fit the reference evaluator, we can locate the exact bridge that must be replaced or extended, instead of starting the mathematical correctness argument again from scratch.

<!-- END SPOKEN LECTURE -->

## Companion: the exact theorem chain

All module names refer to the **2026-11-19 uploaded** `networkx_algo_common_subtree` snapshot. The abbreviated snippets below omit implicit typeclass parameters and enclosing namespaces.

### The mathematical target

In `proofs/SubtreeProofs/Droschinsky2018/RootedDynamicProgram.lean`:

```lean
noncomputable def sourceState (left : FiniteTree V) (right : FiniteTree W)
    (weights : Scoring V W K) (penalty : WithTop K) (leftBase : V) (rightBase : W)
    (u : V) (v : W) : State K :=
  (mappedValue left right weights penalty leftBase rightBase u v,
    skippedValue left right weights penalty leftBase rightBase u v)
```

This definition cites **independent finite witness** maxima supplied by `BoundaryStates.lean` and `SkippedRecurrence.lean`, not the table evaluation.

### The executable update

```lean
def childWeights (...) (u : V) (v : W) (c : V) (d : W) : Option (WithBot K) :=
  if c ∈ leftChildren u ∧ d ∈ rightChildren v then
    some (max (weights.edge s(u,c) s(v,d) + (previous c d).1)
      (previous c d).2)
  else none

-- Two components of step, schematically:
( weights.node u v + WeightedMatching.weight matrix matching,
  oneSkip + max (bestLeftDescent previous) (bestRightDescent previous) )
```

**Exact local premise** in `step_correct`:

```lean
hprevious : ∀ p,
  RootedEvaluationOrder.Depends left right leftBase rightBase p (u,v) →
  previous p.1 p.2 = sourceState left right weights penalty leftBase rightBase p.1 p.2
```

The theorem also requires `hleft` and `hright`, asserting that membership in the supplied child lists is logically equivalent to the actual `FiniteTree.Child` relation. Its proof concludes with `Prod.ext` and appeals to `mapped_recurrence` and `skipped_recurrence_two_state`.

### Dependency and rank

In `Shared/RootedEvaluationOrder.lean`, for a fixed pair of ambient roots:

```lean
noncomputable def rank (pair : V × W) : Nat :=
  left.depthRank leftBase pair.1 + right.depthRank rightBase pair.2

def Depends (child parent : V × W) : Prop :=
  (left.Child leftBase parent.1 child.1 ∧ child.2 = parent.2) ∨
  (child.1 = parent.1 ∧ right.Child rightBase parent.2 child.2) ∨
  (left.Child leftBase parent.1 child.1 ∧ right.Child rightBase parent.2 child.2)
```

`rank_decreases` proves a strict inequality for each alternative. `rank_lt_size` proves every pair rank is smaller than `Fintype.card V + Fintype.card W`.

### The generic evaluation proof

In `Shared/FiniteTable.lean`:

```lean
def rounds (keys : List A) (fallback : B) (update : (A → B) → A → B) : Nat → Table A B
  | 0 => []
  | fuel + 1 =>
    let previous := rounds keys fallback update fuel
    keys.map (fun key => (key, update (read fallback previous) key))

-- Essential hypotheses of rounds_correct:
complete : ∀ key, key ∈ keys
decreases : ∀ child parent, depends child parent → rank child < rank parent
hupdate : ∀ previous key,
  (∀ child, depends child key → previous child = target child) →
  update previous key = target key
```

The theorem concludes `read fallback (rounds ... fuel) key = target key` when `rank key < fuel`. In the source, `evaluate_correct` instantiates this generic theorem; `solve_correct` uses complete vertex lists and `leftVertices.length + rightVertices.length` rounds to satisfy its hypotheses.

### Worked state table

Each table cell displays `(mapped, skipped)`. `⊥` means *no feasible skipped witness*, never numerical zero.

| Pair | Independent target | Rank | First round at which both components are correct |
| --- | --- | ---: | ---: |
| C,D | `(5, ⊥)` | 0 | 1 |
| P,D | `(1, 3)` | 1 | 2 |
| C,Q | `(0, 3)` | 1 | 2 |
| P,Q | `(12, 1)` | 2 | 3 |

Node rewards: `w(P,Q)=3`, `w(C,D)=5`, `w(P,D)=1`, `w(C,Q)=0`. One direct edge-pair reward is `4`. Penalty for one skipped vertex is `2`. Actual `solve` chooses four rounds because each vertex list has length two.

**Dependency graphs:** `P,Q` depends on `C,Q`, `P,D`, and `C,D`; `P,D` and `C,Q` both depend on `C,D`. The proof works for arbitrarily sized finite trees, not just this graph.

### Practice with the declarations

1. In `step_correct`, find the hypothesis that converts lists into true child relations. Describe a wrong child list that would make the conclusion false without that hypothesis.
2. Read `FiniteTable.rounds_correct` and identify its induction variable. Why must rank decrease **strictly**, rather than weakly?
3. For the four-state example, compute the skipped component at P,Q after rounds one, two, and three. Explain why the middle result is not the independent optimum.
4. Explain why `unrootedOptimum_correct` does not prove the paper's optimized unrooted time bound, although it proves the exact unrestricted optimal score.

**Source map:** `Droschinsky2018/BoundaryStates.lean`, `SkippedRecurrence.lean`, `MappedDecomposition.lean`, `MatchingAssembly.lean`, `RootedDynamicProgram.lean`; `Shared/FiniteTable.lean`, `RootedEvaluationOrder.lean`; `docs/planning/paper_statement_crosswalk.md`. Companion to `018000` and `022000`; broader prerequisites: `logic-types:004000`–`008000`.
