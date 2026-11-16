# 017000 — Graph Minors and Treewidth: Solving Hard Problems by Separators

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, trees, matching, dynamic programming. **Central question:** when does a large graph have a small enough interface for exponential work to become manageable?

<!-- BEGIN SPOKEN LECTURE -->

# Graph Minors and Treewidth: Solving Hard Problems by Separators

A graph may have millions of vertices, yet be easy to reason about if its complicated pieces meet along small boundaries. Conversely, a graph with far fewer vertices may be difficult because the same dependencies overlap in too many directions. Treewidth is a mathematical measure of this distinction. It tells us when we can organize a graph like a tree of small interacting regions.

Before defining it, consider the maximum independent set problem. We want as many vertices as possible, with no edge joining two selected vertices. On a general graph this is a hard optimization problem. On a tree it becomes a small dynamic program: for each vertex, record the best solution if it is included and the best solution if it is excluded. Once the choices at the root of a subtree are fixed, its child subtrees become independent.

The magic is the small interface. Every child subtree communicates with the rest of the tree through a single vertex. Treewidth generalizes that idea from one-vertex boundaries to boundaries of a bounded number of vertices.

## A tree whose nodes contain pieces of another graph

A tree decomposition of a graph is itself a tree, but each node of this new tree carries a bag of vertices from the original graph. Every original vertex must appear in some bag. Both ends of every original edge must appear together in at least one bag. And the bags containing any fixed vertex must form a connected subtree.

That last requirement prevents a variable from disappearing and then returning without any record of its state. As information moves through the decomposition tree, a vertex remains present along every step between any two places where it is used.

The width is one less than the size of the largest bag. Treewidth is the smallest width over all possible tree decompositions. The subtraction of one makes a tree with at least one edge have treewidth one, since bags containing the endpoints of each edge are sufficient. An isolated graph with vertices but no edges has treewidth zero.

A clique on k plus one vertices has treewidth k. All members of a clique must coexist in some bag of every tree decomposition; the connected-subtree property forces this. Cycles have treewidth two, while trees need width one. A square grid gets wider as its side length grows, even though every vertex has degree at most four. Low degree therefore does not imply low treewidth.

## Dynamic programming on the bags

Suppose a tree decomposition of width k is already given. Root it, and move information from leaves to root. For independent set, a state can specify which vertices in the current bag are selected. There are at most two to the power k plus one such subsets. Discard states selecting adjacent bag vertices, and store the best value attainable in the part of the graph already processed.

At an introduce step, a new vertex enters a bag. It can be selected only if no selected neighbor already present conflicts. At a forget step, a vertex leaves the interface. We maximize over whether it was selected, because future bags will no longer need to know its state. At a join step, two processed regions share the same interface; combine their values and correct for anything counted twice in the bag.

The running time is exponential in the width but, with an appropriate decomposition, only linear up to polynomial factors in the number of vertices. For a fixed small width, this can turn an otherwise intractable search into an efficient algorithm. The algorithmic promise is conditional: finding a good tree decomposition is itself a computational problem, and a graph of large treewidth gives no comparable speedup from this approach.

The same pattern can solve problems involving vertex covers, colorings, connectivity, and many logical properties, though the necessary state space may be much larger. One should not assume that every graph problem becomes easy merely because a tree decomposition is supplied. The specific dynamic program and its state invariants still need to be established.

## Minors: the structure that survives simplification

There is another graph operation that clarifies why treewidth matters. A graph minor is obtained by deleting vertices, deleting edges, and contracting edges. Contraction joins the endpoints of an edge into one vertex, merging incident edges and removing loops if we work with simple graphs.

These operations express a structural question: can a complicated graph be simplified until a particular pattern appears? For example, planar graphs cannot contain a minor isomorphic to either of the two classical obstructions, the complete graph on five vertices or the complete bipartite graph with parts of size three. Wagner's theorem says these two forbidden minors characterize planarity.

Treewidth cannot increase when we take a minor. Deleting an edge cannot create a new interaction. Deleting a vertex can only reduce what bags need to contain. Contracting an edge can be handled by replacing its two endpoints with their identified vertex in every relevant bag. The decomposition rules continue to hold without increasing bag size.

Yet there is a critical distinction. Excluding one fixed minor does not necessarily bound treewidth by a constant. Planar graphs exclude the complete graph on five vertices as a minor, but square planar grids have arbitrarily large treewidth. Deep graph-minor theory describes the structural consequences of excluding a fixed minor; it is not the assertion that all such graphs admit tiny tree decompositions.

## Why separators and minors belong together

A small bag behaves as a separator: once its vertices are fixed, parts of the graph below different branches can often be processed independently. This is why the decomposition is algorithmically valuable. A large grid, by contrast, has many intertwined routes; separating a substantial region requires a boundary that grows with the grid. That geometric intuition is reflected in its growing treewidth.

The Robertson–Seymour graph-minor program established that finite graphs are well-quasi-ordered under the minor relation, among many deeper structural results. One consequence is that every minor-closed family of finite graphs is characterized by a finite collection of excluded minors. This is a structural existence theorem, not necessarily a practical way to discover the forbidden list or an efficient solver for an arbitrary problem.

The connection between minors and algorithms is therefore twofold. Minor structure can tell us what kinds of complex subgraphs a family avoids. Treewidth tells us whether that restriction is strong enough, or can be combined with additional structure, to support manageable dynamic programming.

## What to remember

Graph size and graph complexity are not interchangeable. Treewidth measures the size of the interface required to build a graph from tree-like pieces. Minor operations preserve structural obstructions, and treewidth is monotone under these simplifications. With a good decomposition and a carefully designed state space, exponential dependence can be confined to the width rather than the whole graph.

That viewpoint is useful not only in graph algorithms, but anywhere local computations are coupled through small separators: probabilistic graphical models, constraint satisfaction, circuit analysis, and formal reasoning about finite structures.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A **tree decomposition** \((T,\{B_t\}_{t\in V(T)})\) of \(G=(V,E)\) satisfies: (1) \(\bigcup_t B_t=V\); (2) for every \(uv\in E\), some bag contains u and v; (3) for every vertex v, \(\{t:v\in B_t\}\) induces a nonempty connected subtree. Its width is \(\max_t |B_t|-1\); \(\operatorname{tw}(G)\) minimizes this.

**Examples:** nontrivial trees have width one, \(\operatorname{tw}(K_n)=n-1\), \(\operatorname{tw}(C_n)=2\) for \(n\ge3\). A square \(r\times r\) grid has treewidth r (with the standard Cartesian grid definition, for \(r\ge2\)). The width is minor-monotone: \(H\preceq_m G\Rightarrow\operatorname{tw}(H)\le\operatorname{tw}(G)\). Planar grids show excluding \(K_5\) does not imply bounded treewidth.

For maximum weighted independent set, one can use a nice rooted decomposition. At each bag B maintain \(DP_t(S)\) for independent subsets \(S\subseteq B\), representing the best solution below node t with interface S. Introduce, forget, and join updates account for newly introduced, forgotten, and doubly counted bag contributions. For a supplied width-k decomposition, standard implementations use \(2^{O(k)}\operatorname{poly}(k)n\) time for this task.

A **minor** is produced by vertex deletion, edge deletion, and edge contraction. Wagner's theorem: finite G is planar iff it has neither \(K_5\) nor \(K_{3,3}\) as a minor. The Robertson–Seymour theorem: finite graphs are well-quasi-ordered by the minor relation; hence any minor-closed family has a finite obstruction set.

### Exercises with answers

1. What is the treewidth of a path with at least two vertices? **Answer:** one; use one bag per edge.
2. Why does a clique of size r require a bag of size at least r? **Answer:** the connected subtrees of bags containing individual clique vertices are pairwise intersecting and, by the Helly property for subtrees of a tree, have common intersection.
3. Can a bounded-degree graph have unbounded treewidth? **Answer:** yes, square grids have maximum degree four and unbounded treewidth.
4. Does exclusion of a fixed graph minor always give bounded treewidth? **Answer:** no; all planar graphs exclude K5, yet planar grids have arbitrarily high width.

### Reading and source notes

- Uriel Feige, [*Dynamic Programming, Treewidth and Graph Minors*](https://www.wisdom.weizmann.ac.il/~feige/Algs2022/TreewidthLecture.pdf), decomposition proofs and dynamic programs.
- Hans L. Bodlaender, [*Dynamic Programming on Graphs with Bounded Treewidth*](https://dspace.mit.edu/entities/publication/bf906865-ecb9-4914-bf24-ef1e633c7c8d), foundational algorithmic analysis.
- [*Algorithmic Graph Structure Theory*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2013.7), graph-minor structural context.
