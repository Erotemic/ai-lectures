# Forced patterns, spectral expansion, and graph separators

<!-- BEGIN SPOKEN LECTURE -->

# Forced patterns, spectral expansion, and graph separators

## Ramsey Theory: Why Large Structures Force Patterns

Consider a gathering of six people. For every pair, either they know each other or they do not. Must there be three people who all know one another, or three people who are pairwise strangers? The answer is yes, and this familiar puzzle is the gateway to Ramsey theory.

The subject studies a surprising tension. A coloring of a large combinatorial structure can look arbitrary, but sufficiently large structures force monochromatic or otherwise ordered substructures. This is not the same as saying a random structure will be simple. It says every structure above a certain size must contain a specified fragment of order.

### Translate people into graph coloring

Represent each person by a vertex. Color the edge between two vertices red if they know each other and blue if they do not. A red triangle is a group of three mutual acquaintances; a blue triangle is a group of three mutual strangers.

Take one vertex in a complete graph with six vertices. It has five incident edges. At least three of those five must have the same color, by the pigeonhole principle. Suppose three incident edges are red, leading to vertices a, b, and c. If any of the edges joining a, b, and c is red, then that edge and the original vertex form a red triangle. If none is red, all three edges among a, b, and c are blue, forming a blue triangle. The blue case for the original three edges is symmetric. Thus every two-coloring of the edges of a complete graph on six vertices has a monochromatic triangle.

Can we lower six to five? No. Arrange five vertices in a cycle, color the five cycle edges red, and color the remaining five edges blue. Both color classes form five-cycles, so neither contains a triangle. We have proved both a lower bound and an upper bound. The exact answer is six.

### Ramsey numbers

Write R of s and t for the smallest number of vertices in a complete graph such that every red-blue edge coloring contains a red complete graph on s vertices or a blue complete graph on t vertices. Our argument shows R of three and three is six.

The definition is asymmetric in wording but symmetric in value: interchanging red and blue shows R of s and t equals R of t and s. Finding exact values quickly becomes difficult. What makes the theory accessible is that general bounds can be proved without knowing the exact numbers.

A basic recurrence says R of s and t is at most R of s minus one and t, plus R of s and t minus one, when s and t are at least two. To understand why, take one vertex in a complete graph of the proposed size. Either it has enough red neighbors to force a red clique of size s minus one among them, or enough blue neighbors to force a blue clique of size t minus one. Adding the original vertex then completes the required clique in its color.

More precisely, the count of incident edges is one less than the number of vertices. If fewer than R of s minus one and t edges were red and fewer than R of s and t minus one were blue, those two counts would add to too few edges. One of the two colors must meet its threshold. This gives the recurrence.

### From the recurrence to a binomial upper bound

Boundary cases are easy: R of one and t, and R of s and one, both equal one. Induct through the recurrence using Pascal's identity, the relation that two adjacent binomial coefficients sum to the next one. We obtain the general bound R of s and t is at most the binomial coefficient with top index s plus t minus two and bottom index s minus one.

For s and t both three, that expression is six, giving the same upper bound as our direct proof. For larger arguments, the binomial upper bound is often far from sharp, but it proves a fundamental existence fact: for every fixed pair of target clique sizes, some finite threshold forces one of them.

This is the finite graph form of Ramsey's theorem. Stronger versions concern colorings of larger subsets and patterns beyond graphs. The central logic remains: find a finite bound that no coloring can evade.

### A probabilistic argument in the opposite direction

The probabilistic method lets us show that certain smaller complete graphs can avoid monochromatic cliques. Color each edge independently red or blue with equal probability. Fix a set of k vertices. The probability that all its edges are red is two to the negative number of edges; the probability all are blue is the same. So the probability this k-set forms a monochromatic clique is two times two to the negative binomial coefficient k choose two.

There are n choose k candidate vertex sets. By linearity of expectation, the expected number of monochromatic k-cliques is n choose k, multiplied by that probability. If this expected count is below one, some coloring must contain zero such cliques. Why? Because the count is a nonnegative integer. If every coloring had at least one, its expectation could not be below one.

This gives a lower bound on the diagonal Ramsey number R of k and k. It shows that a large amount of apparent chaos can coexist with the complete absence of one chosen pattern. In fact, as k grows, the random-coloring argument produces lower bounds exponential in k.

The upper and lower arguments pull in opposite directions. Recursive counting proves that sufficiently large structures must contain order. Random construction proves that quite large structures can still avoid it. Understanding the gap is a major part of the subject.

### Pattern forcing is not pattern finding

There is an algorithmic distinction. An existence theorem says a monochromatic clique must be present. It does not automatically give an efficient method for locating one in a given enormous coloring, nor does it make the exact threshold easy to compute. Conversely, the probabilistic proof may show that a suitable coloring exists without telling us how to construct it efficiently.

Ramsey theory also connects to the graph-coloring lecture we have already developed. In chromatic graph theory, we ask how many colors are needed to avoid adjacent vertices sharing a color. Here the edges themselves receive colors, and we ask which monochromatic complete subgraphs are unavoidable. Changing what is colored changes the theorem.

The conceptual result is deeper than the party puzzle. Arbitrarily complicated finite structures have regularities forced by size alone. Yet those regularities may be small compared with the ambient structure, and proving precise thresholds can be hard. Ramsey theory studies the boundary between what can be avoided and what every sufficiently large object must contain.

## Spectral Graph Theory: Eigenvalues, Cuts, and Expansion

Two large communities may each contain many connections, yet a single bridge might join them. Remove that bridge, and the network falls apart. From a list of vertex degrees alone, the network may appear healthy. A few local measurements cannot reliably detect that global bottleneck.

Spectral graph theory translates the graph into a matrix and looks at its eigenvalues. A particular eigenvalue, the first nonzero eigenvalue of a graph Laplacian, can reveal how tightly the graph is connected. This is a meeting point between combinatorics, linear algebra, and optimization.

### The Laplacian as a discrete derivative

Let the graph be finite, undirected, and unweighted. Assign a real number to every vertex, perhaps temperature, voltage, or a score expressing which community it belongs to. At a vertex, the graph Laplacian takes its degree times its assigned number, then subtracts the numbers at all neighboring vertices.

In matrix form this is the degree matrix minus the adjacency matrix. It is symmetric. The constant function is in its kernel, because every vertex agrees with its neighbors when all numbers are equal.

There is a revealing identity. Multiply the vector of vertex values by the Laplacian and take its inner product with itself in the appropriate quadratic form. The result is the sum, over every edge, of the square of the difference between its endpoint values.

This is a discrete energy. It is always nonnegative. And it is zero precisely when the assigned values are constant on each connected component. Therefore the number of zero eigenvalues equals the number of connected components. An exact combinatorial fact has become an exact statement about a matrix spectrum.

### The Rayleigh quotient and the second eigenvalue

Suppose the graph is connected. The smallest Laplacian eigenvalue is zero, with the constant vector as its eigenvector. The second-smallest eigenvalue can be characterized by minimizing the edge-difference energy over vectors perpendicular to the constant vector, normalized to have squared length one.

Why is that a measure of connectivity? Imagine assigning values near plus one on one community and near minus one on the other. Within each community, neighboring vertices have nearly equal values, so internal edges contribute little energy. Only the scarce bridge edges contribute substantially. The Rayleigh quotient can therefore be small.

If, instead, every large partition has many crossing edges, it is difficult to assign two distinct plateaus without paying a substantial energy cost. The second eigenvalue tends to be larger.

The eigenvalue is not itself a cut size; it is a continuous relaxation of the search for a low-boundary partition. We allowed each vertex to take any real score rather than requiring a rigid yes-or-no assignment. That relaxation makes powerful linear-algebraic methods available.

### A small exact example

Take a cycle on four vertices. Each vertex has degree two, and the adjacency matrix connects every vertex to its two neighbors. Its ordinary Laplacian has eigenvalues zero, two, two, and four.

The zero eigenvalue comes from constant values. The two equal middle eigenvalues represent two independent ways to vary around the cycle at the same energy scale. The largest eigenvalue corresponds to alternating signs around the cycle, which makes every edge disagree as much as possible relative to the vector's size.

If we delete one edge and obtain a path of four vertices, the graph remains connected, but its second eigenvalue is smaller. The new graph has a more pronounced geometric separation across its middle. The spectral statement recognizes that loss of connectivity strength before the graph becomes disconnected.

### Degrees matter: the normalized Laplacian

The ordinary Laplacian weights a high-degree vertex differently from a low-degree vertex. For irregular graphs, we often prefer the normalized Laplacian, built by scaling with the inverse square roots of the degrees.

This has a spectrum between zero and two when there are no isolated vertices. It connects naturally to random walks. The walk transition matrix moves from a vertex to a uniformly selected neighbor; after an appropriate similarity transformation, its eigenvalues are one minus those of the normalized Laplacian.

For a connected graph, zero is a simple normalized-Laplacian eigenvalue. The first nonzero eigenvalue is called the spectral gap. A large gap roughly expresses resistance to being separated into two substantial sets by relatively few edges. It also informs how rapidly random walks forget their starting position—but for a non-lazy walk on a bipartite graph, an eigenvalue at negative one creates periodic oscillation. The spectral gap near one does not by itself remove that issue. Making the walk lazy, so it sometimes stays put, is a standard remedy.

### Cheeger's inequality connects cuts to spectra

To quantify a bottleneck, define a set's volume as the sum of the degrees of its vertices. For a nonempty set occupying at most half the graph's total volume, take the number of crossing edges divided by that volume. The smallest such ratio is the graph's conductance, often written phi.

For the normalized Laplacian, Cheeger's inequality places the conductance between one half of the second eigenvalue and the square root of twice that eigenvalue. The two bounds are not equalities in general, but they give an important correspondence: a small conductance forces a small eigenvalue, and a small eigenvalue guarantees a cut whose conductance is bounded in terms of its square root.

The upper bound has an algorithmic interpretation. Compute an eigenvector for the second normalized-Laplacian eigenvalue, order vertices by a suitable degree-adjusted score, and try cuts along that ordering. A sweep-cut argument proves that one such cut achieves the guaranteed bound.

This is more than saying graphs can be visualized in Euclidean space. The proof uses a continuous minimization to identify a discrete partition with a quantitative approximation guarantee.

### When not to overinterpret a spectrum

An eigenvalue does not identify every structural feature of a graph. Different graphs can share the same spectrum. A strong spectral gap does not say that every pair of vertices is adjacent; it says something global about expansion under the chosen normalization. Numerical computations introduce their own limitations, especially when an eigenvalue is clustered or when the graph is so large that only approximate eigenpairs are available.

There is also an important distinction between a graph's topology and its diffusion process. The graph Laplacian defines one natural dynamics, but changing edge weights or walk rules changes the operator and often the relevant notion of connectivity.

The payoff is that a matrix can be a lens into a combinatorial object. By minimizing a quadratic energy, we detect partitions that would otherwise require searching through exponentially many subsets. That bridge between continuous relaxation and discrete structure will reappear in graph partitioning, data analysis, random walks, and the numerical eigenvalue algorithms studied elsewhere in the library.

## Graph Minors and Treewidth: Solving Hard Problems by Separators

A graph may have millions of vertices, yet be easy to reason about if its complicated pieces meet along small boundaries. Conversely, a graph with far fewer vertices may be difficult because the same dependencies overlap in too many directions. Treewidth is a mathematical measure of this distinction. It tells us when we can organize a graph like a tree of small interacting regions.

Before defining it, consider the maximum independent set problem. We want as many vertices as possible, with no edge joining two selected vertices. On a general graph this is a hard optimization problem. On a tree it becomes a small dynamic program: for each vertex, record the best solution if it is included and the best solution if it is excluded. Once the choices at the root of a subtree are fixed, its child subtrees become independent.

The magic is the small interface. Every child subtree communicates with the rest of the tree through a single vertex. Treewidth generalizes that idea from one-vertex boundaries to boundaries of a bounded number of vertices.

### A tree whose nodes contain pieces of another graph

A tree decomposition of a graph is itself a tree, but each node of this new tree carries a bag of vertices from the original graph. Every original vertex must appear in some bag. Both ends of every original edge must appear together in at least one bag. And the bags containing any fixed vertex must form a connected subtree.

That last requirement prevents a variable from disappearing and then returning without any record of its state. As information moves through the decomposition tree, a vertex remains present along every step between any two places where it is used.

The width is one less than the size of the largest bag. Treewidth is the smallest width over all possible tree decompositions. The subtraction of one makes a tree with at least one edge have treewidth one, since bags containing the endpoints of each edge are sufficient. An isolated graph with vertices but no edges has treewidth zero.

A clique on k plus one vertices has treewidth k. All members of a clique must coexist in some bag of every tree decomposition; the connected-subtree property forces this. Cycles have treewidth two, while trees need width one. A square grid gets wider as its side length grows, even though every vertex has degree at most four. Low degree therefore does not imply low treewidth.

### Dynamic programming on the bags

Suppose a tree decomposition of width k is already given. Root it, and move information from leaves to root. For independent set, a state can specify which vertices in the current bag are selected. There are at most two to the power k plus one such subsets. Discard states selecting adjacent bag vertices, and store the best value attainable in the part of the graph already processed.

At an introduce step, a new vertex enters a bag. It can be selected only if no selected neighbor already present conflicts. At a forget step, a vertex leaves the interface. We maximize over whether it was selected, because future bags will no longer need to know its state. At a join step, two processed regions share the same interface; combine their values and correct for anything counted twice in the bag.

The running time is exponential in the width but, with an appropriate decomposition, only linear up to polynomial factors in the number of vertices. For a fixed small width, this can turn an otherwise intractable search into an efficient algorithm. The algorithmic promise is conditional: finding a good tree decomposition is itself a computational problem, and a graph of large treewidth gives no comparable speedup from this approach.

The same pattern can solve problems involving vertex covers, colorings, connectivity, and many logical properties, though the necessary state space may be much larger. One should not assume that every graph problem becomes easy merely because a tree decomposition is supplied. The specific dynamic program and its state invariants still need to be established.

### Minors: the structure that survives simplification

There is another graph operation that clarifies why treewidth matters. A graph minor is obtained by deleting vertices, deleting edges, and contracting edges. Contraction joins the endpoints of an edge into one vertex, merging incident edges and removing loops if we work with simple graphs.

These operations express a structural question: can a complicated graph be simplified until a particular pattern appears? For example, planar graphs cannot contain a minor isomorphic to either of the two classical obstructions, the complete graph on five vertices or the complete bipartite graph with parts of size three. Wagner's theorem says these two forbidden minors characterize planarity.

Treewidth cannot increase when we take a minor. Deleting an edge cannot create a new interaction. Deleting a vertex can only reduce what bags need to contain. Contracting an edge can be handled by replacing its two endpoints with their identified vertex in every relevant bag. The decomposition rules continue to hold without increasing bag size.

Yet there is a critical distinction. Excluding one fixed minor does not necessarily bound treewidth by a constant. Planar graphs exclude the complete graph on five vertices as a minor, but square planar grids have arbitrarily large treewidth. Deep graph-minor theory describes the structural consequences of excluding a fixed minor; it is not the assertion that all such graphs admit tiny tree decompositions.

### Why separators and minors belong together

A small bag behaves as a separator: once its vertices are fixed, parts of the graph below different branches can often be processed independently. This is why the decomposition is algorithmically valuable. A large grid, by contrast, has many intertwined routes; separating a substantial region requires a boundary that grows with the grid. That geometric intuition is reflected in its growing treewidth.

The Robertson–Seymour graph-minor program established that finite graphs are well-quasi-ordered under the minor relation, among many deeper structural results. One consequence is that every minor-closed family of finite graphs is characterized by a finite collection of excluded minors. This is a structural existence theorem, not necessarily a practical way to discover the forbidden list or an efficient solver for an arbitrary problem.

The connection between minors and algorithms is therefore twofold. Minor structure can tell us what kinds of complex subgraphs a family avoids. Treewidth tells us whether that restriction is strong enough, or can be combined with additional structure, to support manageable dynamic programming.

### What to remember

Graph size and graph complexity are not interchangeable. Treewidth measures the size of the interface required to build a graph from tree-like pieces. Minor operations preserve structural obstructions, and treewidth is monotone under these simplifications. With a good decomposition and a carefully designed state space, exponential dependence can be confined to the width rather than the whole graph.

That viewpoint is useful not only in graph algorithms, but anywhere local computations are coupled through small separators: probabilistic graphical models, constraint satisfaction, circuit analysis, and formal reasoning about finite structures.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Ramsey Theory: Why Large Structures Force Patterns

**Track:** Discrete Mathematics and Combinatorics. **Background:** graph coloring, elementary counting, the probabilistic method. **Central question:** how large must a finite configuration become before a prescribed ordered or colored pattern is unavoidable?

#### Mathematical companion (not spoken)

Define \(R(s,t)\) to be the least \(n\) such that every red-blue edge-coloring of \(K_n\) contains a red \(K_s\) or a blue \(K_t\). It is symmetric and finite. For \(s,t\ge2\),
\[R(s,t)\le R(s-1,t)+R(s,t-1),\qquad
R(s,t)\le\binom{s+t-2}{s-1}.\]
The recurrence follows by partitioning the neighbors of an arbitrary vertex by edge color; the binomial bound follows by induction and Pascal's rule. \(R(3,3)=6\): the one-vertex/three-neighbors argument proves the upper bound; coloring \(K_5\)'s cycle edges red and its complement blue proves the lower bound.

**Probabilistic lower bound:** independently color each edge of \(K_n\) with each color probability \(1/2\). For an individual \(k\)-set, a monochromatic clique occurs with probability \(2^{1-\binom{k}{2}}\). Therefore
\[\mathbb E\,[\#\text{monochromatic }K_k]=\binom nk 2^{1-\binom{k}{2}}.\]
If the right side is \(<1\), there exists a coloring with no monochromatic \(K_k\), proving \(R(k,k)>n\). This is a nonconstructive first-moment statement; no algorithmic complexity claim follows without further argument.

##### Exercises with answers

1. Describe a coloring of \(K_5\) with no monochromatic triangle. **Answer:** red cycle edges and blue non-cycle edges; each color gives a five-cycle.
2. What is the general binomial upper bound for \(R(4,3)\)? **Answer:** \(\binom{5}{3}=10\) (the exact value is nine).
3. What does expected monochromatic-clique count below one imply? **Answer:** at least one coloring has zero such cliques, because the count is nonnegative and integer-valued.
4. Is Ramsey's statement that every sufficiently large two-colored complete graph contains a large monochromatic *vertex-color* class? **No:** the theorem here concerns edge colorings; the object being colored is essential.

##### Reading and source notes

- [Applied Combinatorics, Section 11.2: Small Ramsey Numbers](https://appliedcombinatorics.org/book/s_ramsey_small.html), elementary exact values and comparison of bounds.
- Joel Spencer, [*Probabilistic Methods in Combinatorics*](https://cs.nyu.edu/~spencer/papers/icmtalk.pdf), overview of Erdős's probabilistic method and Ramsey lower bounds.
- Reinhard Diestel, [*Graph Theory*, author-hosted resources](https://diestel-graph-theory.com/basic.html?level=1), basic clique and coloring concepts.

### Spectral Graph Theory: Eigenvalues, Cuts, and Expansion

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs and cuts, matrices and eigenvalues, Rayleigh quotients, elementary probability. **Central question:** how can a list of eigenvalues reveal whether a graph is held together by a bottleneck?

#### Mathematical companion (not spoken)

For a finite undirected graph \(G=(V,E)\), \(L=D-A\) is the combinatorial Laplacian. For \(f\in\mathbb R^V\),
\[f^T Lf=\sum_{\{u,v\}\in E}(f_u-f_v)^2\ge0.\]
The multiplicity of eigenvalue zero is the number of connected components. For connected \(G\), \(\lambda_2(L)=\min_{f\perp\mathbf1,\ f\ne0}f^TLf/f^Tf\).

If all degrees are positive, the normalized Laplacian is \(\mathcal L=I-D^{-1/2}AD^{-1/2}\), with eigenvalues in \([0,2]\). For \(\operatorname{vol}(S)=\sum_{v\in S}d_v\) and \(\partial S\) the set of crossing edges, define
\[\Phi(G)=\min_{0<\operatorname{vol}(S)\le\operatorname{vol}(V)/2}\frac{|\partial S|}{\operatorname{vol}(S)}.\]
For connected graphs, the normalized Cheeger bounds are
\[\frac{\lambda_2(\mathcal L)}2\le\Phi(G)\le\sqrt{2\lambda_2(\mathcal L)}.\]
A normalized eigenvector with coordinates \(x_v\) is sweep-cut using scores \(x_v/\sqrt{d_v}\) (equivalently generalized eigenvectors for \(Lf=\lambda Df\)).

**Cycle example:** \(C_4\) has \(\operatorname{spec}(L)=\{0,2,2,4\}\) and \(\operatorname{spec}(\mathcal L)=\{0,1,1,2\}\). For the nonlazy random walk \(P=D^{-1}A\), \(\operatorname{spec}(P)=\{1,0,0,-1\}\); the negative-one eigenvalue causes period-two behavior.

##### Exercises with answers

1. Why does \(Lf=0\) imply \(f\) constant on components? **Answer:** the quadratic energy vanishes, so each edge joins equal values.
2. Find the Laplacian eigenvalues of a single edge. **Answer:** for \(L=\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)\), they are zero and two.
3. Does a second eigenvalue near zero imply the graph is disconnected? **No:** only exact zero gives another component; near zero indicates a weak cut.
4. Why is a lazy walk useful on a bipartite graph? **Answer:** holding with positive probability prevents exact period-two oscillation; for \((I+P)/2\), eigenvalues of \(P\) are mapped to nonnegative values.

##### Reading and source notes

- Fan R. K. Chung, [*Spectral Graph Theory* and related papers](https://www.math.ucsd.edu/~fan/wp/), Laplacian, Cheeger inequalities, and random walks.
- [UC San Diego, Introduction to Spectral Graph Theory](https://www.math.ucsd.edu/~fan/teach/262/notes/03/LectureNote6.pdf), normalized Laplacian and random walk operator.
- Daniel Spielman, [Spectral Graph Theory lecture notes](https://cs.yale.edu/homes/spielman/561/), Rayleigh quotient and graph partitioning.

### Graph Minors and Treewidth: Solving Hard Problems by Separators

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, trees, matching, dynamic programming. **Central question:** when does a large graph have a small enough interface for exponential work to become manageable?

#### Mathematical companion (not spoken)

A **tree decomposition** \((T,\{B_t\}_{t\in V(T)})\) of \(G=(V,E)\) satisfies: (1) \(\bigcup_t B_t=V\); (2) for every \(uv\in E\), some bag contains u and v; (3) for every vertex v, \(\{t:v\in B_t\}\) induces a nonempty connected subtree. Its width is \(\max_t |B_t|-1\); \(\operatorname{tw}(G)\) minimizes this.

**Examples:** nontrivial trees have width one, \(\operatorname{tw}(K_n)=n-1\), \(\operatorname{tw}(C_n)=2\) for \(n\ge3\). A square \(r\times r\) grid has treewidth r (with the standard Cartesian grid definition, for \(r\ge2\)). The width is minor-monotone: \(H\preceq_m G\Rightarrow\operatorname{tw}(H)\le\operatorname{tw}(G)\). Planar grids show excluding \(K_5\) does not imply bounded treewidth.

For maximum weighted independent set, one can use a nice rooted decomposition. At each bag B maintain \(DP_t(S)\) for independent subsets \(S\subseteq B\), representing the best solution below node t with interface S. Introduce, forget, and join updates account for newly introduced, forgotten, and doubly counted bag contributions. For a supplied width-k decomposition, standard implementations use \(2^{O(k)}\operatorname{poly}(k)n\) time for this task.

A **minor** is produced by vertex deletion, edge deletion, and edge contraction. Wagner's theorem: finite G is planar iff it has neither \(K_5\) nor \(K_{3,3}\) as a minor. The Robertson–Seymour theorem: finite graphs are well-quasi-ordered by the minor relation; hence any minor-closed family has a finite obstruction set.

##### Exercises with answers

1. What is the treewidth of a path with at least two vertices? **Answer:** one; use one bag per edge.
2. Why does a clique of size r require a bag of size at least r? **Answer:** the connected subtrees of bags containing individual clique vertices are pairwise intersecting and, by the Helly property for subtrees of a tree, have common intersection.
3. Can a bounded-degree graph have unbounded treewidth? **Answer:** yes, square grids have maximum degree four and unbounded treewidth.
4. Does exclusion of a fixed graph minor always give bounded treewidth? **Answer:** no; all planar graphs exclude K5, yet planar grids have arbitrarily high width.

##### Reading and source notes

- Uriel Feige, [*Dynamic Programming, Treewidth and Graph Minors*](https://www.wisdom.weizmann.ac.il/~feige/Algs2022/TreewidthLecture.pdf), decomposition proofs and dynamic programs.
- Hans L. Bodlaender, [*Dynamic Programming on Graphs with Bounded Treewidth*](https://dspace.mit.edu/entities/publication/bf906865-ecb9-4914-bf24-ef1e633c7c8d), foundational algorithmic analysis.
- [*Algorithmic Graph Structure Theory*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2013.7), graph-minor structural context.
