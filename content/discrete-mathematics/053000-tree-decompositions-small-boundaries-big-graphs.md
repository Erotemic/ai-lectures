# Small Boundaries, Big Graphs: Tree Decompositions and Dynamic Programming

**Track:** Discrete Mathematics and Combinatorics  
**Lecture:** 053000  
**Preparation:** Graphs, trees, paths, basic recursion, and maximum independent sets.  
**Companion:** The three tree-decomposition axioms, a three-bag example, and an exact dynamic-programming recurrence.

<!-- BEGIN SPOKEN LECTURE -->

Some graphs are large because they contain many repetitions of a small pattern. Others are difficult because distant pieces interact in many different ways. Those are not the same phenomenon. A thousand rooms arranged in a corridor may be easier to reason about than twenty rooms where every room is connected to every other one. The size of a network and the complexity of its interconnections deserve different measurements.

Treewidth is one way to separate those ideas. It asks whether a graph can be organized as a tree of small overlapping groups of vertices. The groups are called *bags*. The original graph need not be a tree. It may have cycles and junctions. The claim is that its complicated interactions can be represented through a tree whose nodes remember a bounded amount of local context.

This is not just a drawing technique. If the bags are small, dynamic programming can often solve a problem by remembering what happens on the boundary between a region and the rest of the graph. The search may still be exponential in the bag size, but it can be linear or nearly linear in the number of bags. A problem that is hard on arbitrary graphs becomes manageable on graphs whose entanglement is limited.

We will derive that claim from the definition, work through a complete maximum-independent-set example, and explain exactly what a correct decomposition must preserve.

## The most misleading picture of a graph

Suppose a network consists of two triangles sharing a single vertex c. The left triangle has vertices a, b, c. The right has c, d, e. Within each triangle every pair is connected. So the edge set contains a-b, a-c, b-c, c-d, c-e, and d-e.

The graph has cycles, so it is not itself a tree. But its two triangles only communicate through c. Once we know whether c has been selected for some combinatorial structure, choices on the left and on the right can be made independently, provided that the structure respects the edges of each triangle.

We can describe this graph with three bags. The left bag contains a, b, and c. The middle bag contains only c. The right bag contains c, d, and e. Connect the left bag to the middle bag and the middle bag to the right bag. The bags themselves form a path, and a path is a tree.

Every original vertex appears in some bag. Every original graph edge has both endpoints in one bag. And the bags containing a particular original vertex form a connected part of the bag tree: c appears in all three consecutive bags, while a and b appear only on the left, and d and e only on the right.

These are precisely the three requirements of a tree decomposition. The width of a decomposition is the size of its largest bag minus one. Our largest bag contains three vertices, so the width is two. The treewidth of the graph is the smallest width achievable over all valid decompositions; this example shows that it is at most two. Since the graph contains a triangle, it is actually two, but we will not need that lower bound to run the algorithm.

Why subtract one? A tree with at least one edge has a decomposition of width one: take a bag for each edge containing its two endpoints and arrange those bags appropriately. Width one is the baseline for forests, so a small width can be interpreted as a controlled extension of tree-like structure. A clique on r vertices, in contrast, has treewidth r minus one. It needs a bag large enough to hold every member of the clique somewhere in the decomposition.

## Why the third axiom does real work

The first two rules sound like an ordinary covering of vertices and edges. Why insist that the bags containing a particular vertex form a connected subtree of the bag tree?

Consider a triangle on vertices a, b, and x. Imagine trying to cheat by using three bags of size two: a with x, a with b, and b with x, connected in that order. Every vertex appears somewhere, and every triangle edge appears in some bag. If those were the only rules, we would apparently have a width-one decomposition of a triangle.

But x appears in the first and last bag and disappears in the middle. The bag nodes containing x are disconnected. This violates the third requirement. The rule prevents us from making an important vertex vanish from the separator and then reappear, allowing incompatible local choices to slip past each other.

There is a precise separation principle behind this. Root the bag tree at some node. Remove one bag node and look at the child components that remain. If a vertex appears strictly inside one component but not in the removed bag, it cannot also appear in another component; that would force the bags containing that vertex to pass through the removed node, contradicting the running-intersection property. Nor can there be a graph edge between such private vertices from two different components: an edge would have to appear together in some bag, which cannot simultaneously belong to both separated components.

Thus the removed bag really is a boundary. The pieces beyond it have no direct interaction except through vertices remembered in the bag. That is exactly what a dynamic program needs. It may solve the children independently once it knows the relevant boundary choices.

Notice the distinction between two forms of reasoning. One can *state* a table indexed by bag choices, but that table is not automatically sufficient. The running-intersection property is the structural theorem showing why no hidden cross-component interaction escapes the table.

## Maximum independent set as a complete example

An independent set is a selection of graph vertices containing no adjacent pair. We want one of maximum size. On an arbitrary graph, this optimization problem can be hard. On our two-triangle example, the answer is easy to see, but we will deliberately use the general dynamic-programming method.

Start with the middle bag, containing only c. Ask a binary question: is c selected or not? That is the entire information the left and right triangles need to exchange. Once c's status is fixed, no edge crosses between the private vertices a,b on the left and d,e on the right.

Case one: select c. Then neither a nor b can be selected, since both are adjacent to c. Neither d nor e can be selected either. We obtain an independent set of size one, containing only c.

Case two: do not select c. The left triangle still contains the edge a-b, so at most one of a and b may be chosen. The right triangle still contains d-e, so at most one of d and e may be chosen. We can choose one from each side, for a total of two. For example, a together with d is independent. So the optimum is two.

Now reinterpret that reasoning as a table. The left child's state is determined by the chosen subset of its intersection with the parent bag. That intersection is just c. When c is included, the best contribution from the left child's private vertices is zero. When c is excluded, the best private contribution is one. The right child has the same table: zero if c is included, one if it is excluded.

At the middle bag, add the number of vertices selected in the bag itself and the contributions of the two children. Choosing c gives one plus zero plus zero, or one. Excluding c gives zero plus one plus one, or two. The result agrees with direct inspection. More importantly, the computation would still be valid if the two sides contained hundreds of vertices, provided each side had already been solved with the correct boundary information.

This explains the purpose of a dynamic-programming state. It does not record the entire partial solution. It records only what the rest of the graph needs to know. Here the interface is a single Boolean choice. On a bag of three vertices, the interface might be any of its eight subsets, although subsets that contain an internal graph edge are invalid and can be discarded.

## From a story to a recurrence

Let us generalize. Root a valid tree decomposition. For a bag B, let the region below that bag consist of every original graph vertex that appears in B or in one of its descendant bags. For each subset S of B, define F of B and S as the size of a largest independent set in that region whose intersection with B is *exactly* S. If S contains both ends of an edge, the state is infeasible, and we may record negative infinity rather than a number.

For a leaf bag, there is no additional region beyond the bag. Therefore F of B and S is just the size of S, provided S itself is independent. No difficult recurrence is needed at the leaves.

At an internal bag, consider each child bag C. The child's chosen subset R must agree with the parent's subset S on their overlap. If a vertex lies in both B and C, the two tables cannot disagree about whether it is selected. So the compatibility condition is that R intersect B equals S intersect C.

Suppose F of C and R already counts all selected vertices in that child's region, including the child bag. At the parent, start with the number selected in S. Then, for each child, take the best compatible child value and subtract the number of selected vertices in the overlap between B and C. We subtract because those overlap vertices were counted once in the parent and again in the child. What remains are the private contributions from the child region.

The children can be combined by addition because the tree-decomposition axioms guarantee that vertices strictly private to different child regions neither coincide nor share graph edges. The maximum can be taken separately for each child once S is fixed. That is the decomposition step. Conversely, compatible independent solutions in the child regions can be assembled with S into a globally independent solution for the whole region. That is the assembly step.

Those two directions are the heart of a correctness proof. Decomposition says the recurrence is at least as good as every valid solution, because every solution supplies compatible child states. Assembly says the recurrence cannot create a fictitious solution, because every set of compatible child states glues to a real independent set. Without both directions, a plausible-looking recurrence may overcount or miss the optimum.

At the root of the decomposition, we have represented the entire graph. Maximize F over all valid choices of S at the root. To reconstruct the actual selected vertices, store the maximizing child choices as well as their scores. Working back through those choices recovers an optimal independent set, not merely its cardinality.

## Why a small bag is valuable

If every bag has at most k plus one vertices, there are at most two to the k plus one possible subsets at each bag. This is the first reason small treewidth helps. The expensive local state is exponential in k rather than in the total number of graph vertices.

A naive implementation may compare many pairs of parent and child subsets, so its running time depends on how it performs compatibility lookups. With an appropriate normalized or *nice* tree decomposition and carefully organized transitions, maximum independent set can be computed in time roughly proportional to the number of decomposition nodes times a function exponential in k. The exact function and preprocessing cost depend on the chosen representation; it would be incorrect to claim that the definition alone proves a particular runtime.

There is another hidden qualification. We have assumed a tree decomposition is supplied. Finding one of minimum width is itself a computational problem and cannot be treated as free. For fixed small k, there are powerful algorithms for finding or approximating appropriate decompositions, but their costs belong in an end-to-end analysis.

What about enormous graphs with small separators? If we can arrange those separators into a valid tree decomposition, the method permits a large number of graph vertices without a proportionate explosion of state combinations. By contrast, a graph that contains a very large clique cannot have small treewidth. Its closely coupled vertices must be remembered together somewhere. The difficulty of local agreement then really is large.

## An invariant that can be formalized

This example is an excellent bridge between paper mathematics and formal proofs. First, we can state the decomposition as data: a tree of finite bags, a graph vertex set, and the three coverage and connectedness properties. Second, we can define the region below a bag and prove the separation lemma. Third, we can specify the independent-set table directly by quantifying over actual independent subsets of that region. Only then do we prove the recurrence equals the specification.

An executable implementation might store bit masks for the subsets S, memoize child values, and reconstruct a set of original graph vertices. Each of these is a separate refinement step. We must show that a bit mask selects the intended vertices, that cached states correspond to the mathematical table, and that the recovered witness has no forbidden edge. A complexity theorem would add accounting for the number of bags, table entries, compatibility queries, and memory retained.

The architecture resembles many other graph dynamic programs. For vertex cover, we remember which boundary vertices are included in the cover. For coloring, we remember boundary colors and reject conflicts. For path problems, we may need to remember more complicated connectivity information among boundary vertices, not merely a subset. That extra state can grow much faster than two to the k.

The essential point is to choose a sufficient boundary description. If it forgets a dependency, the algorithm may combine incompatible regions. If it remembers too much, the algorithm may remain correct but waste exponential time. Tree decompositions let us ask that question explicitly: what information must cross a separator for the rest of the graph to make its decision?

A tree decomposition does not turn every graph into a tree. It identifies places where many choices can be summarized by a small shared boundary. The running-intersection rule guarantees those summaries remain consistent. The dynamic program exploits the resulting conditional independence. And the proof of its correctness is the same pair of arguments we used in the tiny two-triangle example: every true solution decomposes into compatible pieces, and every collection of compatible pieces assembles into a true solution.

That is the mathematical reason treewidth helps. The general graph may be huge, but its pieces only need to have small conversations with one another.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A **tree decomposition** of a finite graph \(G=(V,E)\) is a tree \(T\) and bags \(B_t\subseteq V\) for nodes \(t\in T\) satisfying:

1. \(\bigcup_{t\in T}B_t=V\).
2. Every edge \(uv\in E\) has both endpoints in some bag \(B_t\).
3. For each vertex \(v\in V\), \(\{t\in T:v\in B_t\}\) is connected in \(T\).

The **width** of this decomposition is \(\max_t|B_t|-1\); \(\operatorname{tw}(G)\) is the minimum width over all decompositions.

**Two-triangle example:** \(G\) has edges \(ab,ac,bc,cd,ce,de\). Decomposition tree: \(\{a,b,c\}\)--\(\{c\}\)--\(\{c,d,e\}\). Maximum bag size is 3, hence width 2. Conditioned on selected intersection \(S\subseteq\{c\}\), each leaf contributes private score 0 when \(c\in S\) and 1 when \(c\notin S\). Root scores are \(F(\{c\})=1\), \(F(\emptyset)=2\), so \(\alpha(G)=2\).

**General table:** Root \(T\). Let \(V_t=\bigcup_{u\text{ descends from }t} B_u\). For independent \(S\subseteq B_t\), set

\[
F_t(S)=\max\{|I|: I\subseteq V_t\text{ is independent},\ I\cap B_t=S\},
\]

with value \(-\infty\) for an infeasible state. If children of \(t\) are \(c\), then

\[
F_t(S)=|S|+\sum_{c}\Bigg[\max_{R\subseteq B_c,\ R\cap B_t=S\cap B_c}F_c(R)-|S\cap B_c|\Bigg].
\]

At a leaf, \(F_t(S)=|S|\) for independent \(S\). This recurrence relies on the separation lemma implied by running intersection and edge coverage. The global optimum is \(\max_{S\subseteq B_r} F_r(S)\).

**Exercises with solutions**

1. Give a width-one decomposition of a path on vertices 1,2,3,4. *Answer:* bags \(\{1,2\}\)--\(\{2,3\}\)--\(\{3,4\}\).
2. Why do bags \(\{a,x\}\)--\(\{a,b\}\)--\(\{b,x\}\) fail to decompose a triangle on a,b,x? *Answer:* the bags containing x are disconnected; edge coverage alone is insufficient.
3. In the two-triangle example, what if c is forced into the independent set? *Answer:* the unique feasible selected set is \(\{c\}\), of size 1.
4. Why is the treewidth of a clique on r vertices \(r-1\)? *Answer:* every pair of vertex bag-subtrees intersects, and connected subtrees of a tree have the Helly property, so one bag contains all r clique vertices; a single bag of size r attains this width.
5. Why must child and parent states agree on the intersection? *Answer:* both describe the same original graph vertices; disagreement would not correspond to any global selected set.

**Sources and attribution**

- SageMath graph theory reference, “Tree decompositions”: https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph_decompositions/tree_decomposition.html
- Uriel Feige, *Dynamic Programming, Treewidth and Graph Minors*, Weizmann Institute lecture notes: https://www.wisdom.weizmann.ac.il/~feige/Algs2022/TreewidthLecture.pdf
- Chun-Hung Liu, *Dynamic programming via a given tree-decomposition*, lecture notes, February 2026: https://people.tamu.edu/~chliu/teaching/spring26math689/2026_02_12.pdf
- The two-triangle instance and exact table computations are original teaching examples.
