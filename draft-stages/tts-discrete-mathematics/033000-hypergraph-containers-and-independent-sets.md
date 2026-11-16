# 033000 — Hypergraph Containers: Counting Rare Combinatorial Structures

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, hypergraphs, independent sets, supersaturation, and extremal counting. **Central question:** how can an enormous family of forbidden-pattern-free objects be covered by a much smaller family of approximate models?

<!-- BEGIN SPOKEN LECTURE -->

# There are far too many graphs to enumerate

A graph on n labelled vertices has roughly n squared divided by two potential edges. Every potential edge is either present or absent. Consequently the number of graphs is two raised to roughly n squared divided by two. Even for moderate n, listing all graphs is out of the question.

Suppose we care only about triangle-free graphs: graphs containing no three vertices with all three connecting edges. This is an extremal problem, because we want to know how dense a triangle-free graph can be. It is also an enumeration problem, because we want to know how many triangle-free graphs exist.

The maximum-edge question has a beautiful answer. Mantel's theorem says that a triangle-free graph on n vertices has at most the floor of n squared divided by four edges. A balanced complete bipartite graph attains that bound. But the theorem alone does not automatically count triangle-free graphs. To count all subgraphs of one extremal bipartite graph gives a lower bound; other triangle-free graphs use different bipartitions and may not be bipartite at all.

Hypergraph containers provide a systematic bridge between structure and enumeration. They say, roughly, that every set avoiding a forbidden pattern is contained in one of relatively few larger sets, and each larger set has only a small number of forbidden patterns. We do not force every container itself to be pattern-free. That relaxation is what makes the covering family small.

# Encode forbidden patterns as hyperedges

Build a three-uniform hypergraph. Its vertices are the potential edges of the original complete graph. A hyperedge consists of the three original graph edges making one triangle. Now select a collection of hypergraph vertices. That selection is exactly a graph on the original labelled vertices.

The selected graph is triangle-free precisely when the selected hypergraph vertices contain no entire hyperedge. In the language of hypergraphs, triangle-free graphs are independent sets of the triangle hypergraph.

Why is this useful? Because a theorem about independent sets of a uniform hypergraph can now control a completely different family of combinatorial structures. The same translation works for sets with no three-term arithmetic progression: vertices are integers and hyperedges are the three terms of each progression. A forbidden configuration becomes a hyperedge; an avoiding object becomes an independent set.

# A small fingerprint can select a large container

The core idea is an encoding argument. Imagine inspecting an independent set and recording a small fingerprint of distinguished vertices. The fingerprint is much smaller than the whole independent set. From the fingerprint, and from the original hypergraph, a deterministic procedure constructs a container containing the independent set.

The container need not equal the independent set. It may include many other vertices, including some forbidden configurations. Its job is to be not too large or not too dense in forbidden patterns. Because there are relatively few possible fingerprints, there are relatively few possible containers.

This is why container proofs pay close attention to how many edges overlap at one vertex, two vertices, or more. If many hyperedges share the same tiny collection of vertices, a naive fingerprint does not reveal enough information. Codegree hypotheses prevent that concentration from overwhelming the argument.

For an r-uniform hypergraph, the average vertex degree and the degrees of fixed small vertex sets govern the useful parameter regime. Under suitable codegree conditions, the container theorem constructs a controlled list of sets capturing every independent set. The precise hypotheses and quantitative bounds matter. There is no universal promise that every hypergraph has a tiny list of tiny containers.

# Counting triangle-free graphs

Return to the triangle hypergraph. Each original edge belongs to about n triangles. A pair of distinct original edges belongs together to at most one triangle. That separation between degree and pair-codegree is exactly the kind of profile that helps a container argument.

For large n, one obtains a collection of containers whose number is two raised to a term that is small relative to n squared. Every triangle-free graph has its edges inside one of these containers. Each container has only a small fraction of the possible triangles, relative to n cubed.

Now use supersaturation. If a graph has noticeably more than n squared divided by four edges, it necessarily contains noticeably many triangles. Therefore any container with sufficiently few triangles can have at most n squared divided by four plus a lower-order correction in its edge count.

Every container with m edges has at most two to the m subgraphs. Multiply that number by the number of containers. The exponent contributed by the number of containers is negligible compared with n squared. We obtain at most two raised to n squared divided by four plus a lower-order term triangle-free graphs.

The lower bound comes from a single balanced bipartition: every subgraph of the complete bipartite graph is triangle-free. There are two raised to the floor of n squared divided by four such subgraphs. Upper and lower bounds therefore agree in their leading exponent. We have counted a family vastly too large to enumerate, using extremal structure plus a compressed covering.

# Why a container is not a classification

It would be incorrect to say that every triangle-free graph is bipartite. An odd cycle of length five is triangle-free but not bipartite. The container argument handles this possibility because a container is only approximately extremal and may represent many different subgraphs.

It would also be incorrect to say that all containers are triangle-free. They are allowed to have a controlled number of triangles, which is a weaker and more flexible property. Supersaturation then converts that quantitative control into an upper bound on their number of edges.

There are two separate hard ingredients: the hypergraph container theorem, which compresses independent sets into a small collection of containers; and a supersaturation theorem, which says those containers cannot all be too dense. Leaving either part out destroys the counting argument.

# A method that travels between problems

Hypergraph containers have become useful for counting independent sets, colorings, forbidden subgraphs, arithmetic-progression-free sets, and structures in sparse random environments. In each application, the shape of the hyperedges and their overlap profile determine what can be proved.

The larger lesson is a change in viewpoint. Instead of listing every allowed object, describe a small family of coarse possibilities containing all allowed objects. An enormous counting problem can become manageable when the descriptions are short enough and the containers restrictive enough.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `H_n` be the three-uniform hypergraph with vertex set `E(K_n)` and one hyperedge `{ij,jk,ki}` for each triple of distinct vertices i,j,k. Independent sets of `H_n` correspond exactly to labelled triangle-free graphs on n vertices.

`|V(H_n)|=binom(n,2)`, `|E(H_n)|=binom(n,3)`, average hypergraph degree is `n-2`, and pair codegree is at most one. Suitable hypergraph-container theorems imply a family `C_n` of containers with `log_2 |C_n|=o(n^2)`, such that every independent set lies in some C and each induced graph on C contains `o(n^3)` triangles. **Supersaturation:** for each fixed epsilon>0, an n-vertex graph with at least `(1/4+epsilon)n^2` edges has at least `c(epsilon)n^3` triangles for sufficiently large n. Hence every container has at most `n^2/4+o(n^2)` graph edges. Therefore
\[
 2^{\lfloor n^2/4\rfloor}\le T_n\le |\mathcal C_n|\,2^{n^2/4+o(n^2)}=2^{n^2/4+o(n^2)},
\]
where `T_n` counts labelled triangle-free graphs. The lower bound is the family of subgraphs of one balanced complete bipartite graph. The container theorem, rather than this calculation alone, establishes the existence of the small covering family.

### Exercises with answers

1. How many vertices does the triangle hypergraph on K_6 have? **Answer:** `binom(6,2)=15`.
2. Is a five-cycle triangle-free? Is it bipartite? **Answer:** yes to triangle-free, no to bipartite.
3. Why is it permissible for a container to contain triangles? **Answer:** it only has to contain the target independent set and have sufficiently few forbidden configurations; supersaturation controls its size.
4. What is the leading base-two logarithm of the count of triangle-free graphs? **Answer:** `n^2/4+o(n^2)`.

### Reading and source notes

- [Balogh, Morris, and Samotij, Independent sets in hypergraphs](https://doi.org/10.1090/S0894-0347-2014-00816-X), one of the foundational container theorems.
- [Saxton and Thomason, Online containers for hypergraphs](https://www.sciencedirect.com/science/article/pii/S0095895616300442), fingerprints and explicit construction ideas.
- [Saxton and Thomason, Hypergraph containers](https://arxiv.org/abs/1204.6595), co-degree hypotheses and counting applications.
