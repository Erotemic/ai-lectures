# From Graph Search to Spectral Cuts: What the Laplacian Measures

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 035000  
**Preparation:** Graph connectivity, Markov chains, matrix eigenvalues, and the graph heat equation.  
**Companion:** Laplacian quadratic form, spectral gap, path example, and a cut relaxation.

<!-- BEGIN SPOKEN LECTURE -->

Consider a network with two well-connected neighborhoods joined by one bridge. A breadth-first search can determine whether every house is reachable from every other. It can also identify the bridge. But suppose you release a random walker into the network. It moves freely within one neighborhood, yet takes a long time to explore the other because it rarely crosses the connecting edge. The network is connected, but it does not mix quickly. How can a matrix detect the difference between connectivity and a bottleneck?

Begin with an undirected graph. Each vertex has a degree, the number of incident edges. Its adjacency matrix has a one for every edge and zero elsewhere. Subtract adjacency from the diagonal degree matrix to obtain the graph Laplacian. The Laplacian is symmetric for an ordinary undirected graph, and the sum of each row is zero. That last fact means the all-ones vector is an eigenvector with eigenvalue zero.

There is a remarkable identity. Choose one real number for each vertex, collected in a vector x. Multiply x transpose by the Laplacian and then by x. The answer is the sum, over every undirected edge, of the square of the difference between the two endpoint values. This quadratic form is always nonnegative. It is zero exactly when x has the same value at both ends of every edge. Thus on a connected graph, it vanishes only for constant vectors. On a disconnected graph, it may take a different constant value on each connected component.

We get an algebraic proof of a graph fact: the number of independent zero-eigenvalue directions of the Laplacian equals the number of connected components. Ordinary graph search finds components by following edges. Spectral linear algebra finds them as vectors unchanged by the Laplacian. These are two algorithms studying the same combinatorial structure through different representations.

Now order the eigenvalues of a connected graph from smallest to largest. The smallest is zero. The next one, commonly called the algebraic connectivity or second Laplacian eigenvalue, is positive. It asks how much the endpoint values must vary across edges when the vertex values have mean zero and squared length one. If the graph can be divided into two large regions with few edges between them, a vector nearly constant on each region but different between regions pays little quadratic energy. The second eigenvalue tends to be small. A tightly connected network makes it harder to maintain such a low-energy disagreement.

This connection can be made precise without introducing an advanced theorem. Take a subset S of vertices and assign value one to vertices in S, zero to vertices outside S. Every edge entirely inside either region contributes zero to the Laplacian quadratic form. Every edge crossing the boundary contributes one. So the quadratic form equals the number of edges crossing the cut. We can subtract the vector's mean without changing any differences across edges, thereby making it orthogonal to the all-ones vector. The centered vector's squared length is the size of S times the size of its complement divided by the total number of vertices.

By the variational characterization of the second eigenvalue, the second eigenvalue is no larger than the quotient of cut size by that centered squared length. A balanced cut with very few crossing edges therefore forces a small second eigenvalue. The reverse direction, which translates a small eigenvalue into a quantitatively good cut, requires more work and is related to Cheeger inequalities. We should not claim that merely reading off the smallest nonzero eigenvalue produces the exact minimum cut.

Here is the computational idea of spectral partitioning. Instead of demanding that every vertex belong to one side or the other, allow real-valued labels. Minimize the graph's squared edge differences subject to constraints that prevent the constant solution and fix the size of the labels. The optimizer is an eigenvector corresponding to the second eigenvalue, often called a Fiedler vector. To turn real labels into two groups, choose a threshold, perhaps after examining several candidates. This is a relaxation: the continuous optimization is mathematically clean, while the final discrete partition may depend on how we round.

We also need to distinguish graph Laplacians. The unnormalized Laplacian, degree minus adjacency, weights raw edge differences. A normalized Laplacian compensates for vertex degrees, and it connects naturally to a random walk that chooses neighbors uniformly. With degree matrix D and adjacency A, the random-walk transition matrix is D inverse times A, for graphs without isolated vertices. Its stationary probabilities are proportional to vertex degree. The corresponding random-walk Laplacian is the identity minus that transition matrix. A symmetrically normalized version uses inverse square roots of degrees on both sides of A, making a symmetric matrix with the same eigenvalues as the random-walk version.

This normalization matters because a high-degree vertex is visited more often by the neighbor-uniform walk in equilibrium. An ordinary cut counts edges crossing a boundary. A conductance-style cut measures outgoing edge weight relative to the volume or total degree of a region. Both quantify bottlenecks, but they normalize by different notions of region size. An algorithm that silently swaps graph Laplacians may change its optimization target and the interpretation of its eigenvectors.

Take again the path of three vertices: left, middle, right. Its unnormalized Laplacian has eigenvalues zero, one, and three. The constant vector is the zero mode. The vector positive on the left, zero in the middle, and negative on the right is an eigenvector for eigenvalue one. The mode reflecting a large middle-versus-ends contrast has eigenvalue three. In the continuous-time graph heat equation, the first nonconstant imbalance decays like the exponential of negative kappa times time; the sharper middle-versus-ends imbalance decays three times as fast in the exponent.

For the discrete-time neighbor-uniform walk, another issue arises: the three-vertex path is bipartite. Without a self-loop, the walker alternates between the middle and an endpoint. Its distribution may fail to converge even though a stationary distribution exists. Making the walk lazy, so it stays put with probability one half and otherwise takes an ordinary step, removes that period-two oscillation. A nonzero spectral gap for an appropriate reversible, aperiodic chain then controls the rate at which certain discrepancies from stationarity decrease. We must state which transition operator and norm are involved before quoting a mixing-time bound.

There is a useful analogy with the heat equation on an interval. A spatially constant temperature is an equilibrium mode. Other temperature patterns decompose into eigenfunctions of a differential operator and decay at rates set by eigenvalues. On a finite graph, the same reasoning decomposes vertex values into eigenvectors of the Laplacian. The graph replaces spatial derivatives with differences across edges. Continuous space and discrete networks can share the language of energy and spectral decay because both are governed by self-adjoint, positive operators in suitable settings.

Does this mean spectral clustering is automatically the best way to group data? No. The graph itself must be chosen from the data, often using a nearest-neighbor rule or a similarity kernel. Different choices of neighbors, weights, and normalization can produce different clusters. The second eigenvector describes a relaxed partition objective, not ground truth. A disconnected graph has multiple zero eigenvalues, and near-disconnected components can make individual eigenvectors sensitive to perturbation. Spectral geometry supplies structure and diagnostics, but application-specific assumptions determine what that structure means.

We have arrived at a connection between three ways of reasoning. Graph algorithms talk about paths, cuts, and reachable vertices. Probability talks about how random walkers distribute themselves and forget their starting points. Linear algebra talks about quadratic forms, eigenvalues, and the decay of modes. The Laplacian is the bridge. It assigns an energy to disagreement across edges and converts local movement into global statements about connectivity, diffusion, and bottlenecks.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For an undirected simple graph, \(L=D-A\) and
\[
x^\top Lx=\sum_{\{i,j\}\in E}(x_i-x_j)^2\ge0.
\]
The kernel of \(L\) consists of vectors constant on each connected component. For connected \(G\), \(\lambda_2(L)>0\) and
\[
\lambda_2(L)=\min_{x\perp\mathbf1,\,x\ne0}\frac{x^\top Lx}{x^\top x}.
\]
For \(S\subset V\) with \(0<|S|<n\), take \(x=\mathbf1_S-(|S|/n)\mathbf1\). Then
\[
x^\top Lx=|\partial S|,\quad x^\top x=\frac{|S|(n-|S|)}n,
\quad \lambda_2(L)\le\frac{n|\partial S|}{|S|(n-|S|)}.
\]
This is one direction of a spectral bottleneck relationship, not a proof that the thresholded eigenvector attains a globally optimal cut.

On a graph with positive degrees, the simple random-walk matrix \(P=D^{-1}A\) has stationary \(\pi_i=d_i/\sum_jd_j\); detailed balance holds because \(\pi_iP_{ij}=1/\sum_jd_j\) for each edge. The symmetric normalized Laplacian \(L_{\mathrm{sym}}=I-D^{-1/2}AD^{-1/2}\) is similar to \(I-P\), so they share eigenvalues. For an undirected connected graph, lazy walk \(P_{\mathrm{lazy}}=(I+P)/2\) is aperiodic.

### Exercises and answers

1. **Components.** Why does a graph with three connected components have at least three independent zero modes of L? **Answer:** The indicator of each component is constant across its edges, hence in the kernel; these indicators are independent.
2. **Energy.** What is the energy of a zero-one vertex labeling? **Answer:** The number of edges whose endpoints receive different labels.
3. **Stationarity.** For the simple random walk on a path of three vertices, what are the stationary probabilities? **Answer:** One quarter, one half, one quarter.
4. **Relaxation.** Is the Fiedler vector itself a two-way graph partition? **Answer:** Not necessarily; it supplies real values that must be thresholded or otherwise rounded.

### Reading and attribution

- Levin and Peres, *Markov Chains and Mixing Times*, second edition, finite reversible chains and spectral methods: https://pages.uoregon.edu/dlevin/MARKOV/.
- Kleinberg and Tardos, *Algorithm Design*, Chapter 3, graph connectivity and cuts, https://www.cs.princeton.edu/~wayne/kleinberg-tardos/.
- The Rayleigh-quotient cut calculation and three-vertex example are original mathematical exposition of standard facts.
