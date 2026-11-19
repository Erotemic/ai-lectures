# Parameterized algorithms and expander structure

<!-- BEGIN SPOKEN LECTURE -->

# Parameterized algorithms and expander structure

## Parameterized Algorithms: Finding Structure Inside Hard Problems

A graph problem may be difficult in the worst case and still be easy on the instances we actually need to solve. Consider a social network with millions of vertices, but suppose we seek a very small set of vertices touching every edge in a selected conflict subgraph. Exponential search over every subset of all vertices is hopeless. Exponential search over a small requested solution size might be entirely reasonable.

Parameterized algorithms separate these two quantities. We use n for input size and k for a parameter describing the aspect of the instance we hope is small. The goal of fixed-parameter tractability is a running time of the form a function of k times a polynomial in n, with the polynomial exponent independent of k.

The place where the parameter appears changes the complexity guarantee. A running time of n to the k-th power is polynomial if k is fixed in advance, but the exponent grows as the parameter grows. It belongs to a broader category often called XP. A running time like two to the k times n squared is fixed-parameter tractable, or FPT. Both may be useful, but the latter has a much stronger scalability guarantee when n becomes large.

### Branching on a vertex-cover decision

The vertex-cover problem supplies a clean example. We have a graph and want at most k vertices so that each edge has at least one endpoint chosen. Pick any remaining edge between u and v. Every valid vertex cover must contain u or v; otherwise that edge remains uncovered.

So we can branch. In one branch we select u, remove the edges it covers, and decrease the remaining budget by one. In the other we select v and do the same. If the budget becomes negative, that branch fails. If no edges remain, the branch succeeds.

Every branch decreases the parameter. The search tree has at most two to the k leaves, apart from polynomial bookkeeping in the graph. Thus vertex cover admits an FPT algorithm. We did not discover a polynomial-time algorithm for arbitrary k. We used the desired answer size to confine the exponential part of the search.

Notice how different this is from treewidth. A small tree decomposition makes it possible to solve many problems by dynamic programming across narrow separators. Vertex-cover parameterization instead exploits a small set of selected vertices. A graph can have small vertex-cover number without us first supplying a tree decomposition, and different parameters can expose different useful structures.

### Kernelization: shrink the instance first

A second technique is to reduce the graph to an equivalent smaller instance whose size is bounded by a function of k. Such a reduction is called kernelization. We can see it concretely for vertex cover.

Suppose a vertex has degree greater than k. If we refuse to choose that vertex, we must choose every one of its more than k neighbors to cover its incident edges. That exceeds our budget. Therefore the high-degree vertex is forced into every size-at-most-k solution. Include it, delete its incident edges, and reduce k by one.

Repeat until every remaining vertex has degree at most the remaining budget. Now consider the remaining edges. If there are more than k squared edges, then even k vertices, each covering at most k edges, cannot cover them all. We can reject the instance. Otherwise there are at most k squared edges, and after deleting isolated vertices there are at most twice k squared vertices.

That is a polynomial kernel: in polynomial time we obtain either a definite no answer or an equivalent instance of size bounded by a polynomial in k. The reduction is not merely a heuristic. Every rule is justified by a proof that the existence of a solution is preserved.

### Parameter choice can change everything

Now consider the problem of finding a clique of size k: a set of k vertices with every pair connected. Its obvious search checks combinations of k vertices and takes roughly n to the k time. Unlike vertex cover, clique parameterized by solution size is W-one-complete, a standard form of evidence against an FPT algorithm under customary complexity assumptions.

It would be incorrect to conclude that finding cliques is never tractable. In a graph of bounded degeneracy, small treewidth, or special geometric structure, different parameters can lead to useful algorithms. The lesson is that the choice of parameter is part of the mathematical insight, not bookkeeping added after the algorithm is designed.

Another technique, color coding, finds simple paths with a prescribed number of vertices by randomly assigning colors and searching for paths that use distinct colors. The color assignment turns a global non-repetition condition into dynamic programming over subsets of colors. Randomization and derandomization provide other routes to FPT algorithms when elementary two-way branching does not expose the structure.

### What the guarantee does and does not promise

An FPT theorem proves a bound of the form f of k times n to a fixed power. It says nothing by itself about whether f of k is tolerable. A double exponential in k can be prohibitive at values where a single exponential is practical. It also does not promise that finding the parameter, such as an optimal tree decomposition, is free.

The careful way to use parameterized reasoning is to identify the actual bottleneck, choose a quantity that is small in the intended data, derive a reduction or recursion that exploits it, and prove that the parameter does not hide in the exponent of n. Kernelization, bounded search trees, color coding, and separator-based dynamic programming are different manifestations of that same principle.

Complexity is not only a property of a problem name. It is a property of the problem together with the promises and parameters we are prepared to use. The right parameter can turn an intractable-looking instance into one for which we have a rigorous and implementable strategy.

## Expander Constructions and Pseudorandom Graphs

Imagine a network where every vertex has just three or four neighbors. That sounds fragile. Remove a small set of vertices and one might expect the network to fall into separate regions. But some sparse graphs have a surprising property: every moderately small set of vertices has many neighbors outside itself. These are expander graphs.

Expanders let us use a small number of edges while retaining strong global connectivity. They are useful in error-correcting codes, randomized algorithms, pseudorandom generators, communication networks, and complexity theory. Their power comes from a tension between local sparsity and global mixing.

There are several definitions of expansion. One counts edges leaving subsets. Another follows a random walk. A third examines eigenvalues of the adjacency matrix. Under suitable regularity assumptions, these definitions are tightly connected, although their constants are not identical.

### The spectral perspective

Take a finite undirected d-regular graph. Divide its adjacency matrix by d. The result is the transition matrix for a random walk that chooses a neighbor uniformly. The constant vector is an eigenvector with eigenvalue one. Every other eigenvector represents a pattern that departs from the uniform distribution.

If all nonconstant eigenvalues have absolute value significantly below one, the random walk rapidly loses memory of its starting point. After a moderate number of steps, the distribution approaches uniform. The nontrivial spectral radius is a measure of how much disagreement survives each step.

A cycle makes a useful counterexample. A random walk on a long cycle only moves locally. Its second eigenvalue approaches one as the cycle grows, and mixing becomes slow. A complete graph mixes quickly but uses a huge number of edges. The challenge is to preserve mixing without spending so many edges.

The expander mixing lemma makes the spectral meaning concrete. Consider two sets of vertices. In a well-mixing regular graph, the number of edges between them is close to what we would expect if edge endpoints were distributed uniformly, up to an error controlled by the nontrivial eigenvalue bound. A small spectral radius makes edge counts look pseudorandom on sufficiently large sets.

Notice the word sufficiently. Spectral expansion is not the assertion that every small set of edges is random or independent. The graph is deterministic, and short cycles or other patterns may still exist. Pseudorandom here means that selected statistical tests, such as edge counts and mixing, are controlled.

### Why random graphs are not the whole story

Random regular graphs often expand well. This suggests a probabilistic existence proof: if most objects chosen from a distribution have the desired property, then some such objects exist. But existence does not automatically give an efficient deterministic construction. For applications in which a graph must be generated from a short description, we want a family whose neighbors can be computed explicitly.

Graph products provide a route to this goal. Squaring a random-walk matrix improves its nontrivial eigenvalues, but dramatically increases degree. Repeating that operation alone makes the graph dense. We need another operation that restores low degree without destroying expansion.

### The zig-zag product

The zig-zag product, introduced by Reingold, Vadhan, and Wigderson, combines one large graph with a much smaller graph. Picture a vertex of the product as a large-graph vertex together with a label describing one of its ports. First take a small step among the port labels, then traverse one edge of the large graph, and finally take another small step in the port-label graph.

This is the zig, the large step, and the zag. The two small steps mix the port information so that the large step does not preserve too much structure. If the large graph has degree m and the small graph has m vertices and degree d, the product has roughly the number of vertices of the large graph times m, but degree d squared. Crucially, its expansion can be controlled using the expansion of the factors.

The operation looks like a compromise: it increases the number of vertices but keeps degree dependent only on the small graph. Combined with graph powers and a carefully chosen fixed small expander, it yields explicit families with bounded degree and a spectral gap independent of the graph size.

We should not pretend that an arbitrary choice of factors automatically works. The spectral inequalities, degree conventions, and seed parameters matter. The construction theorem is what guarantees the desired bound.

### Expander walks as pseudorandom sampling

Suppose a subset of the vertices is marked bad. A walk started from the stationary distribution visits that subset with the expected frequency. If successive samples were independent, concentration would be straightforward. Expander walks reuse previous randomness, so the samples are correlated. Yet the spectral gap lets us control many of those correlations.

This is why expanders can economize random bits. One uniform starting vertex requires logarithmically many random bits, and each subsequent step in a fixed-degree graph needs only a constant number. A sequence of independent uniform vertices would require a fresh logarithmic number for each sample.

A deterministic sparse network can therefore help simulate selected features of random sampling. The deeper lesson is that randomness and pseudorandomness are different resources. A random construction can prove that expanders exist, while an explicit construction gives us a machine for producing them predictably.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Parameterized Algorithms: Finding Structure Inside Hard Problems

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, vertex covers, complexity classes, elementary algorithm analysis. **Central question:** can an exponentially difficult problem be made practical when a meaningful structural parameter is small?

#### Mathematical companion (not spoken)

A parameterized decision problem \(L\subseteq\Sigma^*\times\mathbf N\) is FPT if it is decidable in \(f(k)|x|^{O(1)}\) time for some computable f. XP permits \(|x|^{f(k)}\). Fixed-parameter tractability requires the polynomial exponent to be independent of k.

**Bounded search tree for vertex cover:** for an uncovered edge uv, branch on including u or v and decrement k. A recurrence \(T(k)\le2T(k-1)+\mathrm{poly}(n,m)\) gives \(O(2^k\mathrm{poly}(n,m))\).

**Buss-type kernel:** while some v has degree greater than current k, force v and reduce k. Afterward all degrees are at most k. If more than \(k^2\) edges remain, reject: k vertices could cover at most \(k^2\) edges. Otherwise delete isolated vertices, leaving at most \(2k^2\) vertices. This is a valid polynomial kernel, not necessarily the best known kernel.

A clique of size k is W[1]-complete under the standard parameterization. The statement “no FPT algorithm exists” is **not** a proved separation of complexity classes; it is conditional on prevailing assumptions. Bounded treewidth and solution size are different parameters and can have different practical meanings.

##### Exercises with answers

1. Why must one endpoint of an uncovered edge belong to any vertex cover? **Answer:** otherwise that edge is left uncovered.
2. For k equal to 3, what edge count forces rejection after all remaining degrees are at most k? **Answer:** more than 9 edges.
3. Does an \(O(n^k)\) algorithm establish FPT with parameter k? **Answer:** no; the exponent depends on k.
4. Does FPT imply a small constant factor? **Answer:** no; the parameter dependence f(k) can be very large.

##### Reading and source notes

- [Carnegie Mellon 15-859FF: Parameterized and Fast-Exponential Algorithms](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859-f19/www/), course notes on FPT, XP, vertex-cover kernelization, and color coding.
- [MIT OpenCourseWare 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/), context on reductions, dynamic programming, and complexity.

### Expander Constructions and Pseudorandom Graphs

**Track:** Discrete Mathematics and Combinatorics. **Background:** eigenvalues of graphs, random walks, spectral gaps, graph products. **Central question:** can a sparse, explicitly describable graph behave like a richly connected random network?

#### Mathematical companion (not spoken)

For a d-regular undirected graph with n vertices, let `A` be adjacency and `P=A/d`. The top eigenvalue is one. For rapid mixing using absolute eigenvalues, assume `rho=max_{i>=2}|lambda_i(P)|<1`, excluding the bipartite `-1` obstruction. For a mean-zero function f, `||P^t f||_2 <= rho^t ||f||_2`. For arbitrary initial distribution, convert this to a mixing estimate using the stationary measure and Cauchy-Schwarz.

With `lambda=max_{i>=2}|lambda_i(A)|`, the expander mixing lemma gives, for oriented edge counts,
\[
\left|e(S,T)-\frac{d|S||T|}{n}\right|\le \lambda\sqrt{|S||T|},
\]
where `e(S,T)=1_S^T A 1_T`. The inequality follows by splitting each indicator into its constant component and orthogonal remainder, and bounding `A` on the orthogonal subspace. It is a *test-specific* pseudorandomness statement, not full statistical independence.

For a large graph G of degree m and a small graph H with m vertices and degree d (with compatible rotation maps), the zig-zag product has `|V(G)|m` vertices and degree `d^2`. Its nontrivial spectral bound is controlled by those of G and H; repeated products and powers can build constant-degree expander families. A cycle `C_n` has spectral gap on the order of `n^{-2}`, so cycles are not a bounded-degree expander family.

##### Exercises with answers

1. Why does a complete graph fail to demonstrate sparse expansion? **Answer:** its degree grows with the number of vertices.
2. What does `rho<1` imply for a mean-zero eigencomponent under t walk steps? **Answer:** it is contracted by at least the factor `rho^t` in absolute value.
3. Why does squaring a graph alone not maintain constant degree? **Answer:** length-two transitions yield degree about `d^2` when multiplicities are retained.
4. Does the expander mixing lemma guarantee independent edge indicators? **Answer:** no; it bounds aggregate edge counts, not independence.

##### Reading and source notes

- [Reingold, Vadhan and Wigderson, Entropy Waves and the Zig-Zag Product](https://annals.math.princeton.edu/2002/155-1/p04), original explicit construction.
- [Hoory, Linial and Wigderson, Expander Graphs and Their Applications](https://www.ias.edu/sites/default/files/math/csdm/05-06/shoory_expander_graphs_and_their_applications.pdf), spectral and combinatorial methods.
- [Linial and Wigderson, Expander Graphs course](https://www.boazbarak.org/expandercourse/), lecture notes and applications.
