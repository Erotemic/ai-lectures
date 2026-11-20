# 002000 — Tree Dynamic Programming as a Proof

**Track:** NX Common Subtree Papers & Formalization. **Section:** Shared mathematics. **Background:** Finite trees, induction, optimization. **Focus:** Defining state meaning, deriving recurrence branches, constructing witnesses, and separating correctness from cost.

<!-- BEGIN SPOKEN LECTURE -->

# Tree Dynamic Programming as a Proof

An efficient dynamic program often looks as if someone discovered a clever table and then wrote down a formula to fill it. In a rigorous account the order runs the other way. First we say what a table entry means. Then we examine all possible valid solutions to that smaller problem. We divide them into cases, prove that the cases are exhaustive, and show how their best scores reduce to smaller entries. Finally we implement the recurrence and count the work.

This is especially fruitful for trees, because cutting a parent-child edge separates the graph cleanly. But there is also a trap. The solution within one branch may interact with another branch through a shared matching constraint or a path that passes through the parent. We cannot combine branch optima merely because the tree has no cycles. We need to identify what the branches share and preserve exactly that boundary information in the state.

Let's build that reasoning, starting with a strict common subtree.

## Name the state before giving the formula

Take two rooted, unordered trees. Their roots are u and v. Consider the problem of finding the best common connected subtree whose selected roots are exactly u and v and are paired to each other. Call the optimum score F of u and v.

The root-to-root restriction is essential. A common subtree somewhere below u or somewhere below v has a different boundary condition. It should not silently qualify for F. We can later optimize over root choices to solve a less restricted problem, but for now we are establishing a local recurrence.

Each pair of matched vertices has a weight, and each pair of matched edges has a weight. The score of a candidate is the sum of those contributions. If we want an unweighted largest common subtree, set every vertex match weight to one and every edge match weight to zero. The chosen common subtree is required to be nonempty, so matching u with v is the starting point.

Imagine u has two children, a and b, while v has three, x, y and z. If we retain an edge from u to a, it must correspond to an edge from v to exactly one of x, y and z. And if we retain both u-to-a and u-to-b, their right-hand endpoints must be distinct. The child-to-child pairing is injective in both directions.

Suppose we already know F for every possible pair of the children: F of a and x, F of a and y, and so forth. Those values represent complete optimal solutions confined to the corresponding descendant subtrees, with their local roots matched. Pair a with x and we earn the optimal score F of a and x, plus the weight for pairing the edges u-to-a and v-to-x. The rest of the subtree below a can be left to that smaller optimum. Pair b with z and we get another independent branch contribution.

What must be optimized at u and v is the set of child pairs. We cannot choose a-to-x and b-to-x simultaneously. We must select a collection with no repeated child on either side. That is exactly the definition of a bipartite matching.

## The root-matching recurrence

Write w of u and v for the weight of matching the root vertices, and q of a and x for the weight of matching their connecting edges. Construct a bipartite graph whose left vertices are the children of u and whose right vertices are the children of v. Its edge from a to x has weight q of a and x plus F of a and x. The best additional reward is the maximum sum over any matching of those child-pair edges. Empty matching is allowed; if every available branch makes the score worse, we keep only the two matched roots.

Thus F of u and v equals their root-match weight plus the weight of a maximum-weight child matching. In symbolic terms, the optimum over an entire pair of trees has been reduced to an optimum over a small bipartite graph, whose edge weights are smaller tree optima.

Take an unweighted example. Suppose a is the root of a two-vertex chain, b is a leaf, x is a leaf, and y is the root of a two-vertex chain. Ignore z for the moment. Then the best rooted match a-to-x has one vertex. The best a-to-y has two. The best b-to-x has one and b-to-y has one. If we pair a with y and b with x, we retain three vertices below the roots and one paired root, for a total of four. If we instead pair a with x and b with y, we retain only two below the roots and one paired root, for three. The matching optimization finds the former pairing.

The example exposes why a greedy choice can fail. Choosing the highest local score for a child is not enough when that choice blocks another child. Every child pair competes for endpoints. Even if the tree itself has no cycles, the child-alignment decision is a genuine combinatorial optimization problem.

## Proving the recurrence in both directions

A recurrence is not justified by the fact that we can write it down. We need an upper bound and an attainable lower bound.

For the upper bound, take any feasible common subtree matching u to v. Remove the matched roots from that candidate. Because the candidate is a connected tree and the parents are paired, the remaining retained components hang below distinct children of u and distinct children of v. Their pairing is a matching M between the child sets. Every component attached by a particular pair, say a and x, is a valid rooted common subtree of those two child subtrees. Its score is no greater than F of a and x. The matched connecting edge contributes exactly q of a and x. Summing over M, the candidate's total score is bounded by w of u and v plus the weight of M, which is bounded by the maximum matching weight.

For the lower bound, start with a maximum-weight matching M. For each edge a-to-x of M, select a rooted subtree witness attaining F of a and x. All these witnesses lie in disjoint child branches on each side. Join their roots to u and v and add the pair u-to-v. We have built a valid connected common subtree. No original child is reused because M is a matching, and the pieces cannot cross because their original branches are disjoint. Its score is exactly w of u and v plus the weight of M.

One direction says no feasible witness can do better than the recurrence. The other constructs a witness with precisely the recurrence's score. Together they establish equality. This method is more informative than an invocation of the “principle of optimality,” because it identifies exactly why the branch decomposition works.

The recurrence also tells us how to reconstruct an answer. Store not only the maximum score of the child matching, but the chosen pairs. For each chosen child pair, recurse into its stored witness, then graft the pieces below the matched root. If our implementation returns only a numeric table, we have proved the optimum value, but we have not yet proved that its reconstruction procedure returns feasible original identities. Those are separate obligations.

## The dependency graph and why recursion terminates

A dynamic program must not depend circularly on itself. In our rooted recurrence, F of u and v refers only to F of children of u and v. Each step strictly decreases both descendant-subtree sizes. The leaves are base cases because they have no child matching work. This gives us a well-founded order: solve smaller subtree pairs before the larger pair that uses them.

We can formalize that proof by induction on the sum of the two subtree sizes, or by nested structural induction on their tree shapes. A bottom-up implementation uses postorder traversal on both inputs. Any table entry is evaluated after the entries corresponding to its children have been completed.

Now consider the unrooted problem. The same undirected edge may serve as a parent edge in one orientation and a child edge in another. If we start evaluating every rooted orientation through recursive calls without planning the dependency order, it is easy to create redundant computation or a dependency cycle in the code. A written claim that “all the required values are available” needs a proof about the actual schedule. That becomes particularly significant in the 2018 algorithm, where skipping a vertex introduces dependencies along a branch in addition to the ordinary child-matching dependencies.

## The state remembers the boundary condition

Why does the 2018 paper need more than F of u and v? Suppose a common edge is realized by a two-edge route on one side. The intermediate vertex is not a mapped endpoint of a common vertex; it lies inside the path. A recursion that insists the current roots are always matched would have no way to move through that intermediate vertex without either adding an unwanted common vertex or abandoning the path.

The paper introduces two states for each pair of current roots. One represents the case where the current vertices are mapped to each other. The other represents a case where at least one current vertex is skipped along a future topological path. Moving downward in the skipped case accumulates the appropriate distance penalty. In the mapped case, independently mapped child branches are again combined by maximum-weight matching.

This is a general lesson in state design: when a recursive subproblem attaches to its parent in more than one kind of way, a single optimum score may conflate incompatible partial solutions. We introduce a state for each relevant boundary behavior. If we invent too many states, the algorithm becomes expensive and the proof cumbersome. If we invent too few, it may be incorrect. The two states in the 2018 paper are not arbitrary implementation flags; they express a mathematical distinction about how the common edge is being realized.

In the 2004 ordered-tree problem, the boundary information looks different. Rather than choosing an arbitrary matching between child sets, the algorithm works with a balanced sequence whose first matched pair splits the input into an inside part and a following part. Its recurrence considers keeping the first paired structure in both inputs, or contracting that first pair in one input, or contracting it in the other. Because these are ordered structures, the recursive pieces have a prescribed sequence order. This is closer to string dynamic programming than to unordered matching, though the semantics are still about trees.

## The source of a complexity bound

It is tempting to count the number of table entries, multiply by a constant, and declare victory. The recurrence we just derived does not have constant work per entry. At every pair u and v, we must solve a maximum-weight bipartite matching problem between their child sets. How expensive is that problem? How many different versions of it appear across possible rootings? Can related versions reuse calculations when a single child is deleted?

The 2016 paper devotes much of its algorithmic analysis to those questions. A correct reference dynamic program based on ordinary matching may be polynomial-time, but it does not automatically meet the faster source-paper bound. The paper's optimized algorithm obtains its advantage through relationships between matching instances. In the Lean repository, the rooted recurrence and reference objective can be proved independently of whether the optimized matching family has been fully connected to production Rust.

The 2004 paper has a different cost issue. Its three-way recurrence performs a small constant number of lookups for each pair of balanced-word states, but the subproblem words must be represented, identified, and stored. The published expected-time result assumes the relevant dictionary operations have expected constant cost. A formal table-call count is not a proof that constructing, copying, comparing and hashing variable-length words has that cost. An actual linked-list memo could scan many entries, changing the runtime even though it computes exactly the same optimum.

So there are three resource questions, not one: how many mathematically different states exist; what work the ideal transition performs; and what the actual representation and implementation must do to execute that transition. A proof of the first two can be valuable without pretending it already closes the third.

## How this looks in Lean

A Lean development can define a predicate for feasible witnesses, define their scores, and state that an answer is optimal if it is feasible and dominates every other feasible witness. That is the independent specification. It can then introduce a recursive function or table which calculates a score by the child-matching recurrence. The central theorem establishes equality between the computed score and the independent finite optimum.

To prove it, we expect lemmas for decomposing any feasible witness into child parts, assigning them to a matching, and assembling a matching together with optimal child witnesses into a feasible whole. After those mathematical results, a source-refinement theorem may connect the abstract score computation to a Rust implementation's memo storage, choice reconstruction and API return value.

These distinctions help us read the proof status ledger intelligently. If a line says the rooted recurrence is proved but efficient matching remains open, that is a coherent and substantial intermediate state. It tells us precisely which theorem links have been established and which optimization still needs justification. If a line says a reference solver is proved, we should ask whether it is the actual production solver, and whether its input and output conventions match the public Python API.

The dynamic-programming habit is simple but demanding. Define the feasible object. Define the table state. Split all feasible objects into exhaustive cases. Show that each branch's bound is attainable. Prove that dependencies get smaller. Build an output witness. And only then account for the computational work. Once we can do that for a single pair of rooted trees, much of the dense notation in all three papers becomes a record of decisions we already understand.

<!-- END SPOKEN LECTURE -->

## Exact mathematical companion

### 2016 rooted score recurrence, abstracted

Let `Gᵣ[u]` and `Hₛ[v]` be the descendant subtrees rooted at `u` and `v` in fixed orientations. Let `F(u,v)` be the optimum nonempty rooted common-subtree-isomorphism score with `u ↦ v`. For children `a ∈ C(u)` and `b ∈ C(v)`, define

\[
c(a,b) = \omega_E((u,a),(v,b)) + F(a,b).
\]

Let `MWM(C(u), C(v); c)` denote the maximum total weight of a **partial** bipartite matching, with empty matching available. Then

\[
F(u,v) = \omega_V(u,v) + \operatorname{MWM}(C(u), C(v); c).
\]

This is the rooted case of Eq. (1) in Droschinsky–Kriege–Mutzel (2016). If some pairs are forbidden or have negative-infinity weight, their feasibility must be modeled explicitly; do not silently replace those cases by finite zeros.

### A worked unweighted child matching

Root `u` has children `a` (a 2-vertex chain) and `b` (leaf); root `v` has children `x` (leaf) and `y` (a 2-vertex chain). With unit vertex-pair weight and zero edge-pair weight:

| Child pair | `F` score |
|---|---:|
| a–x | 1 |
| a–y | 2 |
| b–x | 1 |
| b–y | 1 |

Matching `(a,y), (b,x)` has weight 3, giving `F(u,v)=1+3=4`. Matching `(a,x), (b,y)` has weight 2, giving 3. No child may appear in two matching edges.

### The recurrence proof as two inequalities

Given arbitrary feasible witness `W`, its rooted branches define a partial matching `M_W`. The score of each branch is at most the corresponding `F(a,b)`. Hence `score(W) ≤ ω_V(u,v) + weight(M_W) ≤ RHS`. Conversely, fix an optimal child matching `M` and one optimal feasible witness for each selected child pair. Disjointness of rooted branches makes their assembly feasible, with score equal to `RHS`. Therefore `F(u,v)=RHS`.

### Compare with the 2004 three-branch recurrence

Writing `s = ( head(s) ) tail(s)`, where parentheses represent the first matched pair and `·` concatenation, the paper's Lemma 8 gives, for nonempty balanced words:

\[
L(s,t)=\max\begin{cases}
1+L(head(s),head(t))+L(tail(s),tail(t)),\\
L(head(s)\cdot tail(s),t),\\
L(s,head(t)\cdot tail(t)).
\end{cases}
\]

Base cases `L(s, ε)=L(ε,t)=0`. `L` counts retained matched pairs/edges. This is a different optimization problem from the unordered child-matching recurrence.

### Repository sources

- `proofs/SubtreeProofs/Droschinsky2016/RootedRecurrence.lean`
- `proofs/SubtreeProofs/Droschinsky2016/BranchDecomposition.lean`
- `proofs/SubtreeProofs/Droschinsky2016/BranchAssembly.lean`
- `proofs/SubtreeProofs/Droschinsky2016/RootedDynamicProgram.lean`
- `proofs/SubtreeProofs/Droschinsky2018/BoundaryStates.lean`
- `proofs/SubtreeProofs/Droschinsky2018/SkippedRecurrence.lean`
- `proofs/SubtreeProofs/Paper2004/DynamicProgram.lean`

**Preparation from existing tracks:** `algorithms-computability-complexity:011000` is a full stand-alone introduction to dynamic programming and its proof obligations; `mathematical-proof:009000` covers induction.

**Primary papers:** [2016, Sections 3–4](https://arxiv.org/pdf/1602.07210v4); [2018, Section 4 and Lemma 5](https://arxiv.org/pdf/1805.00821v1); [2004, Section 4 and Lemma 8](https://www.cs.upc.edu/~antoni/subtree.pdf).
