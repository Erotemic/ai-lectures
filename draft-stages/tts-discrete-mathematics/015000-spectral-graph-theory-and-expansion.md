# 015000 — Spectral Graph Theory: Eigenvalues, Cuts, and Expansion

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs and cuts, matrices and eigenvalues, Rayleigh quotients, elementary probability. **Central question:** how can a list of eigenvalues reveal whether a graph is held together by a bottleneck?

<!-- BEGIN SPOKEN LECTURE -->

# Spectral Graph Theory: Eigenvalues, Cuts, and Expansion

Two large communities may each contain many connections, yet a single bridge might join them. Remove that bridge, and the network falls apart. From a list of vertex degrees alone, the network may appear healthy. A few local measurements cannot reliably detect that global bottleneck.

Spectral graph theory translates the graph into a matrix and looks at its eigenvalues. A particular eigenvalue, the first nonzero eigenvalue of a graph Laplacian, can reveal how tightly the graph is connected. This is a meeting point between combinatorics, linear algebra, and optimization.

## The Laplacian as a discrete derivative

Let the graph be finite, undirected, and unweighted. Assign a real number to every vertex, perhaps temperature, voltage, or a score expressing which community it belongs to. At a vertex, the graph Laplacian takes its degree times its assigned number, then subtracts the numbers at all neighboring vertices.

In matrix form this is the degree matrix minus the adjacency matrix. It is symmetric. The constant function is in its kernel, because every vertex agrees with its neighbors when all numbers are equal.

There is a revealing identity. Multiply the vector of vertex values by the Laplacian and take its inner product with itself in the appropriate quadratic form. The result is the sum, over every edge, of the square of the difference between its endpoint values.

This is a discrete energy. It is always nonnegative. And it is zero precisely when the assigned values are constant on each connected component. Therefore the number of zero eigenvalues equals the number of connected components. An exact combinatorial fact has become an exact statement about a matrix spectrum.

## The Rayleigh quotient and the second eigenvalue

Suppose the graph is connected. The smallest Laplacian eigenvalue is zero, with the constant vector as its eigenvector. The second-smallest eigenvalue can be characterized by minimizing the edge-difference energy over vectors perpendicular to the constant vector, normalized to have squared length one.

Why is that a measure of connectivity? Imagine assigning values near plus one on one community and near minus one on the other. Within each community, neighboring vertices have nearly equal values, so internal edges contribute little energy. Only the scarce bridge edges contribute substantially. The Rayleigh quotient can therefore be small.

If, instead, every large partition has many crossing edges, it is difficult to assign two distinct plateaus without paying a substantial energy cost. The second eigenvalue tends to be larger.

The eigenvalue is not itself a cut size; it is a continuous relaxation of the search for a low-boundary partition. We allowed each vertex to take any real score rather than requiring a rigid yes-or-no assignment. That relaxation makes powerful linear-algebraic methods available.

## A small exact example

Take a cycle on four vertices. Each vertex has degree two, and the adjacency matrix connects every vertex to its two neighbors. Its ordinary Laplacian has eigenvalues zero, two, two, and four.

The zero eigenvalue comes from constant values. The two equal middle eigenvalues represent two independent ways to vary around the cycle at the same energy scale. The largest eigenvalue corresponds to alternating signs around the cycle, which makes every edge disagree as much as possible relative to the vector's size.

If we delete one edge and obtain a path of four vertices, the graph remains connected, but its second eigenvalue is smaller. The new graph has a more pronounced geometric separation across its middle. The spectral statement recognizes that loss of connectivity strength before the graph becomes disconnected.

## Degrees matter: the normalized Laplacian

The ordinary Laplacian weights a high-degree vertex differently from a low-degree vertex. For irregular graphs, we often prefer the normalized Laplacian, built by scaling with the inverse square roots of the degrees.

This has a spectrum between zero and two when there are no isolated vertices. It connects naturally to random walks. The walk transition matrix moves from a vertex to a uniformly selected neighbor; after an appropriate similarity transformation, its eigenvalues are one minus those of the normalized Laplacian.

For a connected graph, zero is a simple normalized-Laplacian eigenvalue. The first nonzero eigenvalue is called the spectral gap. A large gap roughly expresses resistance to being separated into two substantial sets by relatively few edges. It also informs how rapidly random walks forget their starting position—but for a non-lazy walk on a bipartite graph, an eigenvalue at negative one creates periodic oscillation. The spectral gap near one does not by itself remove that issue. Making the walk lazy, so it sometimes stays put, is a standard remedy.

## Cheeger's inequality connects cuts to spectra

To quantify a bottleneck, define a set's volume as the sum of the degrees of its vertices. For a nonempty set occupying at most half the graph's total volume, take the number of crossing edges divided by that volume. The smallest such ratio is the graph's conductance, often written phi.

For the normalized Laplacian, Cheeger's inequality places the conductance between one half of the second eigenvalue and the square root of twice that eigenvalue. The two bounds are not equalities in general, but they give an important correspondence: a small conductance forces a small eigenvalue, and a small eigenvalue guarantees a cut whose conductance is bounded in terms of its square root.

The upper bound has an algorithmic interpretation. Compute an eigenvector for the second normalized-Laplacian eigenvalue, order vertices by a suitable degree-adjusted score, and try cuts along that ordering. A sweep-cut argument proves that one such cut achieves the guaranteed bound.

This is more than saying graphs can be visualized in Euclidean space. The proof uses a continuous minimization to identify a discrete partition with a quantitative approximation guarantee.

## When not to overinterpret a spectrum

An eigenvalue does not identify every structural feature of a graph. Different graphs can share the same spectrum. A strong spectral gap does not say that every pair of vertices is adjacent; it says something global about expansion under the chosen normalization. Numerical computations introduce their own limitations, especially when an eigenvalue is clustered or when the graph is so large that only approximate eigenpairs are available.

There is also an important distinction between a graph's topology and its diffusion process. The graph Laplacian defines one natural dynamics, but changing edge weights or walk rules changes the operator and often the relevant notion of connectivity.

The payoff is that a matrix can be a lens into a combinatorial object. By minimizing a quadratic energy, we detect partitions that would otherwise require searching through exponentially many subsets. That bridge between continuous relaxation and discrete structure will reappear in graph partitioning, data analysis, random walks, and the numerical eigenvalue algorithms studied elsewhere in the library.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a finite undirected graph \(G=(V,E)\), \(L=D-A\) is the combinatorial Laplacian. For \(f\in\mathbb R^V\),
\[f^T Lf=\sum_{\{u,v\}\in E}(f_u-f_v)^2\ge0.\]
The multiplicity of eigenvalue zero is the number of connected components. For connected \(G\), \(\lambda_2(L)=\min_{f\perp\mathbf1,\ f\ne0}f^TLf/f^Tf\).

If all degrees are positive, the normalized Laplacian is \(\mathcal L=I-D^{-1/2}AD^{-1/2}\), with eigenvalues in \([0,2]\). For \(\operatorname{vol}(S)=\sum_{v\in S}d_v\) and \(\partial S\) the set of crossing edges, define
\[\Phi(G)=\min_{0<\operatorname{vol}(S)\le\operatorname{vol}(V)/2}\frac{|\partial S|}{\operatorname{vol}(S)}.\]
For connected graphs, the normalized Cheeger bounds are
\[\frac{\lambda_2(\mathcal L)}2\le\Phi(G)\le\sqrt{2\lambda_2(\mathcal L)}.\]
A normalized eigenvector with coordinates \(x_v\) is sweep-cut using scores \(x_v/\sqrt{d_v}\) (equivalently generalized eigenvectors for \(Lf=\lambda Df\)).

**Cycle example:** \(C_4\) has \(\operatorname{spec}(L)=\{0,2,2,4\}\) and \(\operatorname{spec}(\mathcal L)=\{0,1,1,2\}\). For the nonlazy random walk \(P=D^{-1}A\), \(\operatorname{spec}(P)=\{1,0,0,-1\}\); the negative-one eigenvalue causes period-two behavior.

### Exercises with answers

1. Why does \(Lf=0\) imply \(f\) constant on components? **Answer:** the quadratic energy vanishes, so each edge joins equal values.
2. Find the Laplacian eigenvalues of a single edge. **Answer:** for \(L=\bigl(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr)\), they are zero and two.
3. Does a second eigenvalue near zero imply the graph is disconnected? **No:** only exact zero gives another component; near zero indicates a weak cut.
4. Why is a lazy walk useful on a bipartite graph? **Answer:** holding with positive probability prevents exact period-two oscillation; for \((I+P)/2\), eigenvalues of \(P\) are mapped to nonnegative values.

### Reading and source notes

- Fan R. K. Chung, [*Spectral Graph Theory* and related papers](https://www.math.ucsd.edu/~fan/wp/), Laplacian, Cheeger inequalities, and random walks.
- [UC San Diego, Introduction to Spectral Graph Theory](https://www.math.ucsd.edu/~fan/teach/262/notes/03/LectureNote6.pdf), normalized Laplacian and random walk operator.
- Daniel Spielman, [Spectral Graph Theory lecture notes](https://cs.yale.edu/homes/spielman/561/), Rayleigh quotient and graph partitioning.
