# Local tests and structural containers

<!-- BEGIN SPOKEN LECTURE -->

# Local tests and structural containers

## Property Testing: Deciding Without Reading Everything

Suppose someone hands you a truth table with more entries than you could inspect in a lifetime. They claim the table represents a linear function. You can check a few random values, but how could a hundred checks say anything about billions of unseen entries?

There is an essential change of goal. Property testing does not usually promise to decide whether the data differs from the desired property in even one place. It promises to accept objects that have the property and reject objects that are far from it. There may be a middle region where either answer is permitted. Once we allow that gap, local tests can detect global structure with surprisingly few queries.

This difference between exact decision and approximate property testing is central. An adversary can hide a single incorrect entry anywhere in a huge table. No tester using a fixed number of queries can guarantee finding it. But if one quarter of the entries must be changed to make the table linear, random local consistency checks have a chance to expose that widespread defect.

## A three-query test for linearity

Consider functions from n-bit vectors to one bit, where addition is performed modulo two. A linear function must satisfy the rule that the value at x plus y equals the sum of the values at x and y, again modulo two.

The Blum–Luby–Rubinfeld test samples two independent uniform inputs x and y, queries the function at x, y, and their sum, and checks that equation. Every truly linear function passes every time. More remarkably, if the function is far from every linear function, a nontrivial fraction of random pairs expose a violation.

To hear a complete miniature example, take the parity function and flip every output bit. The result is an affine function, parity plus one, but it is not linear because its value at zero is one. Evaluate the test equation: the two flipped terms on the left cancel their extra ones, but the single flipped term on the right retains one. Every test rejects. This is why a linearity tester is testing homomorphisms, not arbitrary affine maps.

Now imagine that the function equals parity except on a small random set of inputs. Most checks still pass, and the rejection rate reflects the amount of corruption. We repeat the experiment and estimate its rejection probability. The BLR soundness theorem connects that probability to distance from the closest linear function.

## Why the theorem is deeper than random inspection

A failed equation proves only that one local triple is inconsistent. The difficult direction is showing that if almost every triple is consistent, there exists one global linear function close to the original table. The proof builds that global candidate from the overwhelmingly consistent local behavior, often using majority correction or Fourier analysis on the Boolean cube.

This is a local-to-global principle. We are not accumulating enough samples to recover an entire truth table. We are exploiting an algebraic constraint that couples different entries. The structure of linearity is what makes the tester powerful.

The query count depends on the tolerated distance and the target error probability, not on the number of entries in the truth table. The work needed to generate a random n-bit query still depends on n, so it would be misleading to say that every aspect of running time is independent of input size. The important sublinear guarantee concerns oracle probes.

## Distance depends on how data is presented

For a Boolean function, distance is the fraction of inputs on which two functions disagree. For a dense graph stored as an adjacency matrix, distance commonly means a fraction of the possible edges that would have to be added or removed. For a bounded-degree graph accessed through adjacency lists, distance is scaled by the maximum degree times the number of vertices. These are different models, with different queries and different notions of being far.

A graph could look easy to test in one model and hard in another. Consider testing whether a dense graph is triangle-free. If the graph is far from triangle-free, the triangle-removal lemma implies that there are many triangles, in a quantitative sense depending on the distance parameter. Sample random triples of vertices, check their three adjacency relations, and a tester can eventually find one with probability bounded away from zero.

The quantitative bound obtained from the triangle-removal lemma can be enormous. Constant query complexity as a function of graph size does not mean a small or practical constant as a function of the required accuracy. That subtlety matters when turning a theorem into an algorithm.

## A graph oracle changes the questions we can ask

In the bounded-degree model, we can query a vertex and an index to retrieve a neighboring vertex. We cannot instantly ask whether an arbitrary pair is connected unless the oracle supports such a question. A local algorithm may explore a neighborhood by breadth-first search and decide whether it finds a forbidden configuration.

For some graph properties, testers can use a number of neighbor queries depending mainly on the degree bound and the distance parameter. Others provably require dependence on the number of vertices. We should not transfer a query-complexity claim from dense adjacency matrices to bounded-degree access without checking its assumptions.

Property testing also differs from local computation. A tester returns a yes-or-no answer about approximate membership. A local computation algorithm answers a query about one part of a hypothetical global solution, while ensuring consistency between answers to different queries. For example, one might want to know the color of a queried vertex in a proper coloring without constructing and storing the whole coloring. This consistency requirement can be much more demanding than merely detecting an error.

## The tradeoff between promises and conclusions

There are two more distinctions worth making. A tolerant tester must distinguish objects very close to the property from objects substantially farther away, rather than accepting only exact members. A distribution-free tester must be accurate when input points are drawn from an unknown distribution, not necessarily the uniform distribution built into the BLR model. Both strengthen the problem and can increase its complexity.

We should also separate one-sided error from two-sided error. The BLR test never rejects a genuinely linear function, so it has one-sided error. A more general tester might have some probability of rejecting a correct object, but it must meet a specified acceptance guarantee.

The real achievement of property testing is not magic access to unseen data. It is the discovery that some global structures have local consistency witnesses, and that widespread violations force many such witnesses. Three queries can be enough to expose a distant failure of linearity because addition binds the entire truth table together. When that kind of coupling is absent, no comparable guarantee should be expected.

## Hypergraph Containers: Counting Rare Combinatorial Structures

A graph on n labelled vertices has roughly n squared divided by two potential edges. Every potential edge is either present or absent. Consequently the number of graphs is two raised to roughly n squared divided by two. Even for moderate n, listing all graphs is out of the question.

Suppose we care only about triangle-free graphs: graphs containing no three vertices with all three connecting edges. This is an extremal problem, because we want to know how dense a triangle-free graph can be. It is also an enumeration problem, because we want to know how many triangle-free graphs exist.

The maximum-edge question has a beautiful answer. Mantel's theorem says that a triangle-free graph on n vertices has at most the floor of n squared divided by four edges. A balanced complete bipartite graph attains that bound. But the theorem alone does not automatically count triangle-free graphs. To count all subgraphs of one extremal bipartite graph gives a lower bound; other triangle-free graphs use different bipartitions and may not be bipartite at all.

Hypergraph containers provide a systematic bridge between structure and enumeration. They say, roughly, that every set avoiding a forbidden pattern is contained in one of relatively few larger sets, and each larger set has only a small number of forbidden patterns. We do not force every container itself to be pattern-free. That relaxation is what makes the covering family small.

## Encode forbidden patterns as hyperedges

Build a three-uniform hypergraph. Its vertices are the potential edges of the original complete graph. A hyperedge consists of the three original graph edges making one triangle. Now select a collection of hypergraph vertices. That selection is exactly a graph on the original labelled vertices.

The selected graph is triangle-free precisely when the selected hypergraph vertices contain no entire hyperedge. In the language of hypergraphs, triangle-free graphs are independent sets of the triangle hypergraph.

Why is this useful? Because a theorem about independent sets of a uniform hypergraph can now control a completely different family of combinatorial structures. The same translation works for sets with no three-term arithmetic progression: vertices are integers and hyperedges are the three terms of each progression. A forbidden configuration becomes a hyperedge; an avoiding object becomes an independent set.

## A small fingerprint can select a large container

The core idea is an encoding argument. Imagine inspecting an independent set and recording a small fingerprint of distinguished vertices. The fingerprint is much smaller than the whole independent set. From the fingerprint, and from the original hypergraph, a deterministic procedure constructs a container containing the independent set.

The container need not equal the independent set. It may include many other vertices, including some forbidden configurations. Its job is to be not too large or not too dense in forbidden patterns. Because there are relatively few possible fingerprints, there are relatively few possible containers.

This is why container proofs pay close attention to how many edges overlap at one vertex, two vertices, or more. If many hyperedges share the same tiny collection of vertices, a naive fingerprint does not reveal enough information. Codegree hypotheses prevent that concentration from overwhelming the argument.

For an r-uniform hypergraph, the average vertex degree and the degrees of fixed small vertex sets govern the useful parameter regime. Under suitable codegree conditions, the container theorem constructs a controlled list of sets capturing every independent set. The precise hypotheses and quantitative bounds matter. There is no universal promise that every hypergraph has a tiny list of tiny containers.

## Counting triangle-free graphs

Return to the triangle hypergraph. Each original edge belongs to about n triangles. A pair of distinct original edges belongs together to at most one triangle. That separation between degree and pair-codegree is exactly the kind of profile that helps a container argument.

For large n, one obtains a collection of containers whose number is two raised to a term that is small relative to n squared. Every triangle-free graph has its edges inside one of these containers. Each container has only a small fraction of the possible triangles, relative to n cubed.

Now use supersaturation. If a graph has noticeably more than n squared divided by four edges, it necessarily contains noticeably many triangles. Therefore any container with sufficiently few triangles can have at most n squared divided by four plus a lower-order correction in its edge count.

Every container with m edges has at most two to the m subgraphs. Multiply that number by the number of containers. The exponent contributed by the number of containers is negligible compared with n squared. We obtain at most two raised to n squared divided by four plus a lower-order term triangle-free graphs.

The lower bound comes from a single balanced bipartition: every subgraph of the complete bipartite graph is triangle-free. There are two raised to the floor of n squared divided by four such subgraphs. Upper and lower bounds therefore agree in their leading exponent. We have counted a family vastly too large to enumerate, using extremal structure plus a compressed covering.

## Why a container is not a classification

It would be incorrect to say that every triangle-free graph is bipartite. An odd cycle of length five is triangle-free but not bipartite. The container argument handles this possibility because a container is only approximately extremal and may represent many different subgraphs.

It would also be incorrect to say that all containers are triangle-free. They are allowed to have a controlled number of triangles, which is a weaker and more flexible property. Supersaturation then converts that quantitative control into an upper bound on their number of edges.

There are two separate hard ingredients: the hypergraph container theorem, which compresses independent sets into a small collection of containers; and a supersaturation theorem, which says those containers cannot all be too dense. Leaving either part out destroys the counting argument.

## A method that travels between problems

Hypergraph containers have become useful for counting independent sets, colorings, forbidden subgraphs, arithmetic-progression-free sets, and structures in sparse random environments. In each application, the shape of the hyperedges and their overlap profile determine what can be proved.

The larger lesson is a change in viewpoint. Instead of listing every allowed object, describe a small family of coarse possibilities containing all allowed objects. An enormous counting problem can become manageable when the descriptions are short enough and the containers restrictive enough.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Property Testing: Deciding Without Reading Everything

**Track:** Discrete Mathematics. **Background:** probability, graphs, finite fields, randomized algorithms. **Central question:** when can a few queries distinguish a property from objects far away from having it?

#### Mathematical companion (not spoken)

For `f:F_2^n -> F_2`, define relative Hamming distance to linearity by
\[
\operatorname{dist}(f,\mathrm{Lin})=\min_{\ell\text{ linear}}\Pr_{x\sim U}[f(x)\ne\ell(x)].
\]
The BLR tester draws independent uniform x,y and accepts iff `f(x)+f(y)=f(x+y)` in F2. It has perfect completeness. Its soundness theorem shows rejection probability bounded below by a positive function of `dist(f,Lin)` (indeed a linear lower bound in standard formulations); sampling `O(1/epsilon)` independent pairs suffices for constant rejection probability if f is epsilon-far, up to the particular soundness constant. All oracle query statements use the uniform-table access model.

For `f(x)=<a,x>+1`, `f(x)+f(y)=<a,x+y>` while `f(x+y)=<a,x+y>+1`: rejection probability is one. A graph in the dense model is epsilon-far from triangle-free if at least `epsilon n^2` adjacency changes (up to normalization conventions) are needed; the triangle removal lemma ensures `delta(epsilon)n^3` triangles and therefore a tester based on O(`1/delta(epsilon)`) sampled vertex triples. This theorem's quantitative dependence on epsilon can be huge, and a bounded-degree adjacency-list oracle is a different model.

##### Exercises with answers

1. Why can a constant-query tester not always detect a single wrong table entry? **Answer:** an adversary can place that entry outside the queried positions; property testing has a far-from-property rejection promise, not exact error detection.
2. Does an affine function with constant term one satisfy the BLR equality? **Answer:** no; it violates every pair check.
3. Must triangle-testing guarantees transfer unchanged from dense to sparse graph models? **Answer:** no; the query oracles and distance normalization differ.
4. Does a property tester reconstruct the whole nearest linear function? **Answer:** no; testing and correction/reconstruction are distinct tasks.

##### Reading and source notes

- [Oded Goldreich, Introduction to Property Testing](https://www.wisdom.weizmann.ac.il/~oded/pt-intro.html), models, algorithms and limitations.
- [Goldreich, property-testing lecture notes](https://www.wisdom.weizmann.ac.il/~oded/pt-ln.html), BLR and graph testing examples.
- [Blum, Luby and Rubinfeld, Self-Testing/Correcting with Applications to Numerical Problems](https://doi.org/10.1145/100216.100225), original local linearity testing work.

### Hypergraph Containers: Counting Rare Combinatorial Structures

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, hypergraphs, independent sets, supersaturation, and extremal counting. **Central question:** how can an enormous family of forbidden-pattern-free objects be covered by a much smaller family of approximate models?

#### Mathematical companion (not spoken)

Let `H_n` be the three-uniform hypergraph with vertex set `E(K_n)` and one hyperedge `{ij,jk,ki}` for each triple of distinct vertices i,j,k. Independent sets of `H_n` correspond exactly to labelled triangle-free graphs on n vertices.

`|V(H_n)|=binom(n,2)`, `|E(H_n)|=binom(n,3)`, average hypergraph degree is `n-2`, and pair codegree is at most one. Suitable hypergraph-container theorems imply a family `C_n` of containers with `log_2 |C_n|=o(n^2)`, such that every independent set lies in some C and each induced graph on C contains `o(n^3)` triangles. **Supersaturation:** for each fixed epsilon>0, an n-vertex graph with at least `(1/4+epsilon)n^2` edges has at least `c(epsilon)n^3` triangles for sufficiently large n. Hence every container has at most `n^2/4+o(n^2)` graph edges. Therefore
\[
 2^{\lfloor n^2/4\rfloor}\le T_n\le |\mathcal C_n|\,2^{n^2/4+o(n^2)}=2^{n^2/4+o(n^2)},
\]
where `T_n` counts labelled triangle-free graphs. The lower bound is the family of subgraphs of one balanced complete bipartite graph. The container theorem, rather than this calculation alone, establishes the existence of the small covering family.

##### Exercises with answers

1. How many vertices does the triangle hypergraph on K_6 have? **Answer:** `binom(6,2)=15`.
2. Is a five-cycle triangle-free? Is it bipartite? **Answer:** yes to triangle-free, no to bipartite.
3. Why is it permissible for a container to contain triangles? **Answer:** it only has to contain the target independent set and have sufficiently few forbidden configurations; supersaturation controls its size.
4. What is the leading base-two logarithm of the count of triangle-free graphs? **Answer:** `n^2/4+o(n^2)`.

##### Reading and source notes

- [Balogh, Morris, and Samotij, Independent sets in hypergraphs](https://doi.org/10.1090/S0894-0347-2014-00816-X), one of the foundational container theorems.
- [Saxton and Thomason, Online containers for hypergraphs](https://www.sciencedirect.com/science/article/pii/S0095895616300442), fingerprints and explicit construction ideas.
- [Saxton and Thomason, Hypergraph containers](https://arxiv.org/abs/1204.6595), co-degree hypotheses and counting applications.
