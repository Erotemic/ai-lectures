# Why the Children Become a Matching: The 2016 Recurrence and Fixed-Root Lemma

<!-- BEGIN SPOKEN LECTURE -->

Picture two rooted trees. Their roots, u and v, have already been chosen as corresponding vertices. In the first tree, u has two child branches. In the second, v has three. We have to decide which branches to keep, how to pair them, and whether the extra branch on the right should be ignored. We also have to account for the reward or penalty of the two roots and of every edge and vertex further down.

It is tempting to think of this as trying different combinations of descendants. That would quickly lead to a large search space. The 2016 paper by Droschinsky, Kriege and Mutzel observes a much stronger structural fact. Because the common subtree is a connected, induced isomorphism, and because u is mapped to v, each retained child branch of u must correspond to exactly one retained child branch of v. Two branches cannot be merged into one. Nor may a branch jump through the root and reappear in some other branch without preserving the required edges.

Consequently the entire choice at the root is a maximum-weight bipartite matching between the two child sets. Each candidate matching edge stands for an already solved smaller rooted common-subtree problem plus the reward for the edge joining that child to the root. The recursive table stores the best possible continuation value. Matching makes compatible choices among those continuations.

That is Equation 1 of the paper. The important work is showing why it is an equality, rather than simply writing down a plausible recurrence. We will calculate an example, prove the two inequalities, see how a fixed-root theorem recovers unrooted solutions, and identify the corresponding Lean declarations and their actual proof boundaries.

## Define a rooted state independently

Let G and H be finite unordered trees. First choose an ambient root in each. This orients every edge from parent toward child and tells us which vertices are descendants of another vertex. Now let u be a vertex of G and v a vertex of H. Consider only connected common-tree isomorphisms within the descendant subtree of u and the descendant subtree of v that include the mapping u to v.

Call the maximum score among those legal witnesses F of u and v. The root pair is mandatory. This F is defined by the optimization problem, not by an algorithm. It is the number we intend our recurrence to compute.

One way to picture the state is that the trees have been cut just above u and v. Nothing outside those cuts is eligible for this subproblem. But the actual induced subgraphs are still taken from the original trees, and the original vertex and edge weights are unchanged.

There are three immediate cases worth fixing in mind. If u has no children, a connected root-preserving witness cannot map a child branch below u, so the only feasible root-containing mapping is the singleton u to v. The same is true if v has no children. In either case F of u and v is precisely the vertex-pair reward of u and v. That remains true when the reward is negative.

If both roots have children, there may be many candidate pairings. Every candidate child pair c and d has a continuation optimum F of c and d, computed inside their descendant subtrees. It also brings in the edge correspondence u-c to v-d. So the score contributed by selecting that child pair is the mapped-edge reward plus F of c and d. The parent-root reward must not be counted in this child contribution; it will be added exactly once after the matching.

If the edge correspondence or the continuation has negative-infinity score, the candidate effectively has negative-infinity contribution. It is never necessary to select such a child pair when the empty matching is allowed. But the mandatory mapped parent could itself score negative infinity, in which case the rooted optimum may also be negative infinity. Keeping these two levels separate prevents accidental clamping of the whole rooted state.

## The matching graph is the entire decision at the root

Construct a bipartite graph with one left vertex for each child of u and one right vertex for each child of v. Between child c and child d, put the weight we just described: the reward for mapping the two incident root edges, plus the best rooted score of the two descendant subtrees. The paper presents the instance as a complete bipartite graph with weights. Negative infinity can express a pair that should never be selected.

A matching is a set of edges in this bipartite graph with no shared left or right endpoints. It is not required to be perfect. Some children may remain unmatched, and all of them may remain unmatched. The weight of a matching is the sum of its selected edge weights. Since the empty matching has score zero, the best matching score is at least zero even if every nonempty pairing is negative.

Let the maximum such weight be called M of u and v. Then Equation 1 says that F of u and v equals the root vertex-pair reward plus M of u and v. This has a pleasing shape. One term accounts for the common root; the other accounts for the independent branches that can be attached beneath it.

But nothing in the word 'matching' itself proves that a common subtree decomposes that way. We need to understand why an arbitrary valid witness yields a matching, and why an arbitrary matching of valid branch witnesses yields a valid common tree.

## A numerical example where greedy pairing fails

Use two tiny rooted trees. G has root a and leaves b and c. H has root x and leaves y and z. The required root correspondence a to x has score negative two. The four leaf-pair rewards are: b to y is four; b to z is one; c to y is three; and c to z is two.

Because each leaf has no descendants, these four numbers are already the rooted continuation scores for the leaf pairs. The corresponding root-edge pairs have additional rewards. Mapping a-b to x-y adds ten. Mapping a-b to x-z adds two. Mapping a-c to x-y adds ten. Mapping a-c to x-z adds negative six.

Add the continuation and the incident-edge reward for each possibility. Pairing b with y gives fourteen. Pairing b with z gives three. Pairing c with y gives thirteen. Pairing c with z gives negative four. These are the weights of a two-by-two bipartite matching instance.

The largest individual edge is b to y, worth fourteen. A greedy method would select it. The only disjoint edge left is c to z, worth negative four, which the greedy method sensibly omits. It would report matching value fourteen. But another matching selects b to z, worth three, and c to y, worth thirteen. The edges have disjoint endpoints, so both may be selected, for total sixteen. Greedy misses the optimum even though the instance has only two children on each side.

The full rooted common-tree value is not sixteen. The root correspondence a to x scores negative two, so F of a and x is fourteen. The selected matching reconstructs the witness mapping a to x, b to z, and c to y. Its vertex contributions are negative two, one and three. Its mapped-edge contributions are two and ten. The grand total is fourteen, as required.

We can check every possible matching. The empty matching scores zero. A one-edge matching scores at most fourteen. There are exactly two two-edge matchings. One selects b to y and c to z and scores fourteen minus four, or ten. The other selects b to z and c to y and scores three plus thirteen, or sixteen. Thus the matching optimum is sixteen, and the corresponding rooted witness has score fourteen. The equality in Equation 1 is visible in this complete small calculation.

Notice what would go wrong if we confused the matching score with the rooted score: we would drop the negative root contribution. If we added the two leaf scores a second time, we would count descendants twice. The recurrence is arranged so that every mapped vertex and edge contributes exactly once.

## First direction: every witness decomposes

Take any valid rooted common-subtree witness P containing u mapped to v. Because P preserves adjacency, a selected neighbor of u must map to a selected neighbor of v. Because we are inside descendant subtrees, those selected neighbors are children, not parents. And because P is a partial bijection, distinct selected children of u map to distinct selected children of v. The selected child pairs therefore form a matching.

Consider one selected child pair c to d. Restrict P to the selected vertices below c on the left, and their corresponding vertices below d on the right. We must show this restriction is a legal rooted witness. This does not follow from injectivity alone. Connectivity of P and the uniqueness of paths in a tree ensure that every selected vertex below c is connected to u through c, and its image lies below d. No selected path from that branch can move into a different branch without passing through u, which the restricted branch omits. The restrictions remain connected and preserve adjacency in both directions.

The chosen branch has some score. By the definition of F of c and d, that score is no greater than the optimal descendant score F of c and d. The full score of P can be partitioned into the reward for u to v, the rewards for the selected incident edges, and the internal scores of the selected descendant branches. There are no extra cross-branch edges to account for: different branches of a tree meet only at their parent.

Replacing each actual branch score by its independent optimum cannot decrease the sum. The selected child pairs form a legal matching, whose weight in the auxiliary bipartite graph is precisely the sum of these edge rewards and optimal continuation values. That matching score cannot exceed the best matching score M of u and v. Therefore the score of P cannot exceed the root reward plus M.

P was arbitrary. In particular, an optimal rooted P obeys this inequality. We have proved that F of u and v is at most the right side of Equation 1. This is the *decomposition* or upper-bound direction. It establishes that the recurrence is not overlooking a hidden kind of connected witness with a better score.

## Second direction: a matching assembles a witness

For the reverse inequality, start with a maximum-weight matching of the child graph. For each selected child pair c to d, choose an optimal rooted witness within those descendant subtrees. We know such a witness exists because the set of feasible mappings is finite and the singleton c to d is always a candidate.

Now take the union of all these child-branch witnesses, and add the pair u to v. Also include the root incident edges implicitly, because the induced subgraphs on the selected vertex sets contain them.

Why is this union well formed? Distinct child subtrees of u do not overlap, and the same holds for distinct child subtrees of v. The matching condition ensures no two branches try to use the same child on either side. Their independent mappings cannot collide across branches. The root pair does not occur inside any strict descendant branch. So the union is still a partial bijection.

Why is it connected? Every chosen branch contains its root c to d, and c is adjacent to u while d is adjacent to v. Adding the mapped root joins each selected branch to a common center on both sides. If the matching is empty, the selected graph is the singleton root, which is connected.

Why is adjacency preserved? It already is inside each branch. The selected root edges correspond by construction. There are no edges joining two different child branches in a tree. Thus no additional adjacency relation appears on either side to spoil the isomorphism. The induced nature of the selected graphs is respected, rather than merely asserted.

Finally, the score of the assembled witness is exactly the reward for the root pair plus the weight of the chosen matching. Every descendant score is counted in its own branch, every root incident edge is counted with the associated matching edge, and the root node reward is counted once. No term is omitted or duplicated.

This gives a feasible witness with the recurrence's score, so the independent rooted optimum F is at least the root reward plus M. Combining this with the upper bound proves Equation 1.

It is worth noticing that the two directions have different jobs. Decomposition controls *all possible* legal witnesses. Assembly constructs *a witness from the proposed optimizer*. If we proved only assembly, we would know the answer is feasible, but we would not know it is best. If we proved only decomposition, we would have a numerical upper bound without knowing it is attainable.

## A theorem about roots, not merely an optimization trick

The recurrence applies when a root pair is required. The original 2016 problem has no roots. One brute-force solution would try every possible root in G and every possible root in H, solve all those rooted problems, and take the largest score. The paper shows we can do better even before introducing its sophisticated matching updates.

Pick any single vertex r of G and declare it to be an ambient root. Keep it fixed. The paper's Lemma 2 says that the unrestricted maximum can be recovered by considering every descendant-root choice u in this orientation of G and every choice v of root in H. We are permitted to root H at v for that subproblem. We do not need to try all ambient orientations of G.

Why should that work? Take any legal nonempty common subtree P in the unrooted problem. Look at its selected vertices in G. They form a connected set. Relative to the arbitrarily fixed ambient root r, that connected set has one distinguished vertex u nearest to r. The uniqueness is a property of trees: if two selected vertices were tied for nearest position in different branches, the path between them would pass through a still closer common ancestor; connectivity would force that ancestor to be selected, a contradiction.

Every selected left vertex therefore lies below u. Let v be the image of u under P. Root H at v. The selected right vertices form a connected subtree containing v, so every one of them lies in the descendants of v in this new orientation. The original P now qualifies as a rooted witness for the descendant subtrees at u and v. We have not changed a vertex pairing, an edge pairing, or a weight. We have only exhibited an orientation in which the already valid witness belongs to one of the restricted families.

Conversely, every rooted witness considered by the fixed-root method is also a legal unrooted witness. So the restricted family is neither missing a better unrestricted solution nor introducing a new kind of solution. The maxima are equal. This is Lemma 2's mathematical content.

Two easy misreadings are worth avoiding. Fixing r does not mean the optimal correspondence must contain r. The closest selected vertex u might be strictly below it. And fixing one left ambient orientation does not mean both roots are fixed once and for all. The method still ranges over left descendant roots u and right root choices v. What Lemma 2 removes is a whole dimension of unnecessary left rerooting.

The distinction affects both performance and proof organization. A correct fixed-root theorem reduces the family of mathematical subproblems. It does not, by itself, establish the final optimized runtime. The paper still needs a schedule that reuses table entries and an efficient method for handling similar weighted matching instances. Those are the next mathematical subjects.

## What has actually been proved in Lean?

The repository's `Droschinsky2016/Rooted.lean` defines `RootedValid` as the independent valid mapping, plus membership of the required root pair and containment in the designated descendant regions. `rootedValue` takes the maximum score over that finite family. The declaration `Valid.fixed_root_representative` proves the unique highest selected pair under a fixed left root. The theorem `fixedRootValue_eq_unrootedValue` proves exactly the fixed-root variational equality we derived.

The decomposition is developed in `BranchDecomposition.lean`. Among its results are the partition of selected vertices by child branches, preservation of a valid child-branch witness, partition of actual unordered mapped edges, and an identity called `score_decomposition`. That last identity makes the arithmetic of the recurrence exact; it proves the score really splits into root, incident edges and branch scores.

The converse is in `BranchAssembly.lean`. Its `assemble_valid` result builds a connected induced isomorphism out of a compatible matching and valid branch witnesses. Its `score_assemble` result states the corresponding score identity. These are the two halves we argued in words.

The theorem `rooted_matching_recurrence` in `RootedRecurrence.lean` combines them to prove Equation 1 for whole rooted trees. The code uses a finite exhaustive matching optimizer whose optimality has been proved independently. That is enough for a mathematical recurrence theorem, but it is not an efficient Hungarian algorithm and does not imply the claimed running time.

The theorem with the same short name in `OrientedRecurrence.lean` applies the reasoning to every descendant pair under fixed ambient roots. This distinction is important to a real dynamic program: when we recurse from u to c and from v to d, the meaning of descendant must stay consistent with the tables we are filling. A theorem for one whole-root case is not automatically a theorem for all fixed-orientation descendant states.

Finally, `RootedDynamicProgram.lean` contains an executable reference evaluator. It computes materialized tables in rank-ordered rounds, using finite child lists and exhaustive matching. The theorem `solve_correct` states that each table entry equals the independently specified rooted value under coverage and child-list representation hypotheses. The theorem `unrootedOptimum_correct` uses Lemma 2 to establish an exact unrooted reference optimum.

The scope of these results is already substantial. There is a specification independent of the algorithm, a proof that each valid mapping decomposes, a proof that matched branches assemble, an equation for the independent optimum, a fixed-root reduction, and a reference evaluation correctness theorem. But none of these automatically proves that the optimized floating-point Rust graph solver implements the same table, reconstructs every identity correctly, or achieves the running-time theorem. The repository's source crosswalk keeps those separate.

We have now reached a particularly useful point in the 2016 paper. The mathematical core of the rooted algorithm is not mysterious: select a root pair, score each possible pair of child continuations, choose a maximum-weight partial matching, and add the root reward. The proof follows the geometry of trees. The fixed-root lemma then shows how to search for an unrestricted optimum without rerooting both trees indiscriminately.

The optimization challenge that remains is not to invent a different recurrence. It is to compute many closely related child matchings without repeatedly paying the full price, and to account for that work across the trees. The next stage of this course can study the assignment reduction and the family of one-vertex-deleted matching instances with this exact rooted specification already in place.

<!-- END SPOKEN LECTURE -->

## Non-spoken companion: exact recurrence, examples and proof structure

### Rooted problem and Equation (1)

Fix ambient roots `r in V_G`, `s in V_H`. Let `G_u^r` and `H_v^s` be the descendant subtrees of `u` and `v`. Define `F_{r,s}(u,v)` as the independent maximum weight of a **nonempty**, connected, induced common-tree isomorphism of the two descendant subtrees which contains `(u,v)`.

For child sets `C_r(u)`, `C_s(v)`, define the candidate branch-pair weight

\[
q_{u,v}(c,d)=\omega_E(\{u,c\},\{v,d\})+F_{r,s}(c,d).
\]

A **partial** matching `M` in the bipartite graph on `C_r(u) \sqcup C_s(v)` has no repeated child on either side and may be empty. Writing `MWM(q)` for its maximum score,

\[
\boxed{F_{r,s}(u,v)=\omega_V(u,v)+\operatorname{MWM}(q_{u,v}).}
\]

This is paper Equation (1), extended to all descendant states in a fixed ambient orientation. When either child set is empty, `MWM=0`, and `F_{r,s}(u,v)=omega_V(u,v)`, even for a negative reward. Branch entries with `-infinity` are never required because the matching may omit them.

### Explicit 2-by-2 child matching example

Root pair `(a,x)` has node reward `-2`, left children `(b,c)`, right children `(y,z)`.

| Child pair | Descendant `F` | Incident-edge reward | Matching weight `q` |
| --- | ---: | ---: | ---: |
| `(b,y)` | 4 | 10 | 14 |
| `(b,z)` | 1 | 2 | 3 |
| `(c,y)` | 3 | 10 | 13 |
| `(c,z)` | 2 | -6 | -4 |

Possible two-edge matchings have scores `14+(-4)=10` and `3+13=16`. The best one-edge matching has score `14`, while the empty matching scores `0`. Therefore `MWM=16` and `F(a,x)=-2+16=14`. Witness `(a,x),(b,z),(c,y)` scores node rewards `-2+1+3=2`, edge rewards `2+10=12`, total `14`.

A greedy procedure selecting `(b,y)` first can be trapped at `14`, missing the disjoint pairing worth `16`.

### Proof of Equation (1)

- **Upper bound (decompose):** Each rooted valid witness induces a matching of its selected child pairs. Branch restrictions are independently rooted valid and have scores bounded by `F(c,d)`. `score_decomposition` partitions the actual mapped nodes and unordered edges, yielding `score(P) <= omega_V(u,v) + MWM(q)`.
- **Lower bound (assemble):** Choose a maximum matching, and for each selected `(c,d)` choose an independently optimal rooted witness. Their disjoint descendant regions and matching injection permit a connected induced-isomorphism union with mapped root `(u,v)`. `score_assemble` gives equality with `omega_V(u,v) + MWM(q)`.

### Lemma 2: fixed left orientation suffices

Choose an arbitrary vertex `r` as a fixed ambient root of G. For each `u in V_G`, root H at a candidate `v in V_H` and evaluate the rooted optimum mapping `u` to `v`. Then

\[
\boxed{\mathrm{MCS}(G,H)=\max_{u\in V_G}\max_{v\in V_H}
  \mathrm{MCS}_{\mathrm{root}}(G^r_u,H^v).}
\]

A connected selected vertex set in G has a unique selected top vertex `u` nearest `r`. Map `u` to `v` and root H at `v`; the same witness belongs to that rooted family. Conversely, any such rooted witness belongs to the unrestricted feasible family. **The fixed vertex `r` need not itself be mapped.**

### Crosswalk to checked source declarations (uploaded 2026-11-19 snapshot)

| Paper/math | Lean theorem or definition | File |
| --- | --- | --- |
| Independent restricted optimum | `RootedValid`, `rootedValue` | `Droschinsky2016/Rooted.lean` |
| Unique top mapped pair | `Valid.fixed_root_representative` | `Droschinsky2016/Rooted.lean` |
| Fixed-root equality, Lemma 2 | `fixedRootValue_eq_unrootedValue` | `Droschinsky2016/Rooted.lean` |
| Exact branch and edge partition | `branch_partition`, `edge_partition`, `score_decomposition` | `Droschinsky2016/BranchDecomposition.lean` |
| Converse witness/score construction | `BranchFamily.assemble_valid`, `score_assemble` | `Droschinsky2016/BranchAssembly.lean` |
| Whole rooted optimum, Eq. (1) | `rooted_matching_recurrence` | `Droschinsky2016/RootedRecurrence.lean` |
| Fixed-orientation descendant recurrence | `Oriented.rooted_matching_recurrence` | `Droschinsky2016/OrientedRecurrence.lean` |
| Executable reference DP | `RootedDP.solve_correct` | `Droschinsky2016/RootedDynamicProgram.lean` |
| Reference unrooted correctness | `RootedDP.unrootedOptimum_correct` | `Droschinsky2016/RootedDynamicProgram.lean` |

**Primary source:** Droschinsky, Kriege and Mutzel, *Faster Algorithms for the Maximum Common Subtree Isomorphism Problem*, arXiv `1602.07210v4`, Section 3: Equation (1), Proposition 1, Lemma 2, Proposition 3. [Pinned PDF](https://arxiv.org/pdf/1602.07210v4).

**Source status:** The mathematical Eq. (1), fixed-root equality, oriented recurrence and exhaustive reference evaluation are proved in Lean. Efficient matching, production Rust graph refinement, f64 correspondence, and the paper's optimized full runtime remain open in `docs/planning/paper_statement_crosswalk.md` and `proofs/PROOF_STATUS.md`. Proposition 1's `O(n^3)` statement and Proposition 3's `O(n^4)` result are **paper claims**; neither is established as an actual-source cost theorem by the checked recurrence.
