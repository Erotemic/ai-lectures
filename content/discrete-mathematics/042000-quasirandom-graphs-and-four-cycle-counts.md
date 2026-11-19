# 042000 — Quasirandom Graphs and Four-Cycle Counts

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, eigenvalues, expectation, and counting. **Central question:** how can a few global counts certify that a large deterministic graph behaves like a random graph?

<!-- BEGIN SPOKEN LECTURE -->

# What does a random-looking graph mean?

Suppose someone gives us a graph with a million vertices and refuses to tell us how its edges were chosen. We count roughly half of all possible edges. Does that make it behave like a random graph in which each edge was included independently with probability one half?

Not remotely. Divide the vertices into two equal groups and connect every pair within a group, leaving no edges between groups. That graph also has edge density approaching one half. But it has a perfect division into two communities, and a random graph with edge probability one half does not usually have such an enormous empty cut.

A single statistic did not tell us enough. Yet a surprisingly small collection of statistics can. In the dense-graph setting, edge density together with the number of four-cycles, counted in the right asymptotic way, characterizes quasirandomness.

This is a theorem of Chung, Graham, and Wilson. Its significance is that many apparently different definitions of randomness turn out to be equivalent along a sequence of large graphs. Random-like behavior can be recognized without knowing that random choices were ever made.

# Count four-cycles carefully

Take a graph on n vertices and call its adjacency matrix A. The matrix entry for vertices i and j is one if they are adjacent and zero otherwise. The entry of A squared at i,j counts common neighbors. Summing the squares of those common-neighbor counts gives the trace of A to the fourth power.

That trace counts closed walks of length four. Some walks repeat vertices, so it is not literally the number of simple four-cycles. But the repeated-vertex walks contribute lower-order terms in the dense large-n limit. For asymptotic quasirandomness, it is convenient to count labeled four-cycle homomorphisms, and the trace formula is exact for that count.

In an independent-edge graph of density p, the leading term is p to the fourth times n to the fourth. A quasirandom graph should have the same leading count.

Return to the union of two complete graphs of equal size. A four-cycle homomorphism has to stay entirely within one half, up to the lower-order issue of repeated vertices. Thus its leading count is two times the fourth power of n over two. That is n to the fourth divided by eight.

But p is one half, so a random graph would give n to the fourth divided by sixteen. The two-clique graph has twice the expected four-cycle density. Counting squares of common-neighbor numbers exposes the hidden block structure.

# The matrix inequality behind the theorem

Why should the four-cycle count have a universal lower bound for a given edge density? The trace of A to the fourth power is the sum of fourth powers of its eigenvalues. One can also derive a bound by repeated Cauchy–Schwarz inequalities on degrees and common-neighbor counts.

In the large-graph limit, four-cycle density is at least the fourth power of edge density. Roughly speaking, equality forces several variance terms to be small. Degrees must be nearly constant, and codegrees must look nearly constant as well. Once that happens, the edge distribution across any two large vertex subsets approaches the density predicted by the random model.

This provides an explanation for the theorem. Large irregularities cannot hide: they create excessive common-neighbor concentration, which increases the four-cycle count. Four-cycles act as a sensitive detector of global structure.

# Equivalent views of quasirandomness

One definition demands that every sufficiently large vertex subset contain roughly the expected number of edges. A stronger-looking version makes the same demand across two different large subsets. Another definition counts every fixed small graph and asks for the expected leading number of copies. A spectral definition asks that there be one dominant adjacency eigenvalue close to p times n and that the remaining eigenvalues be small compared with n.

For dense graphs with a fixed edge density bounded away from zero and one, these conditions are equivalent in the appropriate asymptotic sense. The surprising fact is not that a genuinely random graph satisfies them with high probability. It is that a deterministic graph satisfying any one of them automatically satisfies the others.

The qualifiers matter. Sparse graphs need different scaling, and four-cycle counts alone are not a universal test in every sparse regime. A finite graph with exactly the correct two statistics is also not automatically identical to a random draw. The theory concerns asymptotic approximation and quantitative error bounds.

# Why quasirandomness is useful

A pseudorandom graph can be highly structured in how it was built and still support counting and embedding arguments that resemble probabilistic ones. Spectral expanders, incidence graphs, and explicitly constructed families can sometimes replace randomness in algorithms and combinatorial existence proofs.

Quasirandomness offers a discipline for checking such claims. Instead of saying a picture looks random, specify a measurable property. Then prove that it implies the properties the application actually needs.

The two-clique counterexample teaches the first lesson: edge density alone is weak. The four-cycle theorem teaches the second: carefully chosen higher-order counts can be powerful. Random-looking behavior is not a mood or an aesthetic judgment. It is a collection of mathematical tests whose equivalence can be proved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a graph `G` with adjacency matrix `A`, `\mathrm{hom}(C_4,G)=\mathrm{tr}(A^4)=\sum_{u,v}(A^2)_{uv}^2`. This counts ordered graph homomorphisms, allowing repeated vertices. If `G_n` is a sequence with `n\to\infty`, edge density tending to `p\in(0,1)`, the Chung–Graham–Wilson criterion reads
\[
\mathrm{hom}(C_4,G_n)= (p^4+o(1))n^4.
\]
Together with edge density, this is equivalent to the usual dense quasirandom conditions, including counts of every fixed graph `H` and uniform edge distribution on linear-size subsets.

For `G_n=K_{n/2}\sqcup K_{n/2}` with even `n`, `2e(G_n)/n^2\to1/2`, while `\mathrm{hom}(C_4,G_n)/n^4\to 2(1/2)^4=1/8` rather than `(1/2)^4=1/16`. For `G(n,p)`, `\mathbb E\mathrm{hom}(C_4,G)=p^4n^4+O(n^3)` at fixed `p` because tuples with collisions occupy `O(n^3)` possibilities.

The matrix perspective uses `\mathrm{tr}(A^4)=\sum_i\lambda_i^4`; after normalizing by `n`, the quasirandom condition constrains the total fourth powers of nonprincipal eigenvalues. For `p` fixed, an asymptotic spectral criterion is `\lambda_1=pn+o(n)` and `\max_{i>1}|\lambda_i|=o(n)`. Do not apply this dense version without adjustment when `p=p(n)\to0`.

### Exercises with answers

1. What does `(A^2)_{u,v}` count? **Answer:** common neighbors of u and v.
2. What is the limiting four-cycle density in the two-equal-cliques graph? **Answer:** `1/8`, versus `1/16` for density `p=1/2` quasirandom graphs.
3. Can an explicit deterministic graph be quasirandom? **Answer:** Yes; the definition concerns its asymptotic counts, not its construction history.
4. Why do repeated-vertex walks not affect the leading dense four-cycle term? **Answer:** there are only `O(n^3)` vertex tuples with a collision, versus `\Theta(n^4)` general tuples.

### Reading and source notes

- [Chung, Graham, and Wilson, Quasi-random Graphs (bibliography)](https://www.rongraham.org/fan-chung/papers), original Combinatorica 1989 theorem.
- [Quasirandom Graphs and the Pantograph Equation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8388949/), explicit statement of edge- and four-cycle-equivalence criteria.
