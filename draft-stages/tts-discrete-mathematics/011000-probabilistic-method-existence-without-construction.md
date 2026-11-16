# 011000 — The Probabilistic Method: Existence without Construction

**Track:** Discrete Mathematics and Combinatorics. **Background:** counting, elementary probability, graphs and hypergraphs. **Central question:** how can a random experiment prove the existence of a mathematical object even when we never exhibit it?

<!-- BEGIN SPOKEN LECTURE -->

# The Probabilistic Method: Existence without Construction

Imagine a mathematical object defined by millions of choices: the colors of edges in a complete graph, or which vertices belong to a particular set. Searching every configuration is hopeless. But perhaps most choices are not disastrous. Or perhaps the expected number of failures is less than one. Then, without naming the successful object, we can prove that it exists.

This is the probabilistic method. It uses probability to prove a deterministic statement of existence. The random experiment is an instrument of the proof, not a claim that the desired object must itself be random.

## If the expected number of failures is less than one

Let X count bad events in a random construction. X is a nonnegative integer. If the expectation of X is less than one, then X cannot be positive for every outcome. If every outcome had at least one failure, its average would be at least one. Therefore some outcome has no failures at all.

That observation is simple, but it changes what we need to calculate. We do not need the exact probability that every bad event is absent. We only need an upper bound on the expected number of bad events. By linearity of expectation, we can add the individual probabilities even if the events are heavily dependent.

This is often much easier than an exact counting argument.

## Coloring a uniform hypergraph

A hypergraph generalizes a graph: an edge may contain more than two vertices. Suppose every hyperedge contains exactly r vertices, and there are m hyperedges. We want to color the vertices red and blue so that no hyperedge is monochromatic.

Color each vertex independently, each color with probability one half. Fix one hyperedge. All r vertices are red with probability two to the negative r, and all are blue with the same probability. Thus the probability that this edge is monochromatic is two to the power one minus r.

Let X count monochromatic hyperedges. By linearity of expectation, its expected value is m times that probability. So when m is strictly smaller than two to the power r minus one, the expectation is below one. Some coloring makes X zero. No hyperedge is monochromatic.

Notice how little we assumed about the pattern of intersections among hyperedges. They may share many vertices. The expectation argument still works because linearity requires no independence among the indicator variables. Independence was used only to compute the probability for each fixed edge.

We have proved a universal sufficient condition for two-colorability of a uniform hypergraph. It may not be sharp for a particular hypergraph, but it is a clean existence theorem with remarkably little structural information.

## A Ramsey lower bound

Now consider a complete graph with n labeled vertices, and color each edge red or blue independently. We seek a coloring with no monochromatic complete subgraph on k vertices. For any fixed k-element set S, the edges inside S are monochromatic exactly when all are red or all are blue.

There are k choose two edges inside S. The probability that they all have one color is two to the power one minus k choose two. And there are n choose k choices for S. Therefore the expected number of monochromatic k-vertex complete subgraphs equals n choose k times two to the power one minus k choose two.

If that product is less than one, a coloring without any monochromatic k-clique exists. In the language of Ramsey numbers, the diagonal Ramsey number R of k and k exceeds n.

This is a lower bound, not a construction of a particular extremal coloring. It was among the influential early examples developed by Paul Erdős. The method does not tell us which coloring works, only that the space of all colorings cannot be entirely bad.

## Random order and independent sets

The same point of view can prove a useful bound on independent sets. Choose a uniformly random ordering of the vertices of any finite simple graph. Select a vertex when it occurs earlier than all of its neighbors. No two adjacent vertices can both be selected: on an edge, one endpoint must occur later than the other.

For a vertex v with degree d, its chance of appearing first among itself and its d neighbors is one divided by d plus one. Sum these probabilities over all vertices. The expected size of the selected independent set is the sum of those reciprocals.

Therefore the graph has an independent set at least as large as that sum, rounded up as necessary. If its average degree is d bar, the convexity of one divided by x plus one gives the simpler lower bound n divided by d bar plus one.

Here the random choice was not a random subset of vertices but a random ordering. Selecting the right probability space can make the desired structural property automatic. Only the size remains to be controlled by expectation.

## From existence to algorithms

A proof by random choice may look nonconstructive, but sometimes we can systematically remove the randomness. Suppose our proof shows that the expected number of bad events is below one. Expose the random choices one at a time. At each step, choose a value whose conditional expected number of future failures is no larger than the current expectation. Such a choice exists because the current conditional expectation is an average of the possible next conditional expectations.

After all choices have been fixed, the remaining conditional expectation equals the actual integer number of failures. It is still less than one, so it must be zero. This is the method of conditional expectations.

There is a qualification. A proof that this deterministic procedure exists does not automatically give an efficient algorithm. We must also be able to compute or bound the relevant conditional expectations efficiently. When that is possible, a probabilistic existence proof may become a practical deterministic construction.

## Beyond the first moment

The first-moment argument works when the total expected number of failures is already less than one. If each failure is rare but there are too many of them to make that sum small, we may need other tools. A second-moment calculation can show that a random variable is positive somewhere by controlling its variance. The Lovász local lemma can show that all bad events can be avoided when they are sufficiently rare and have limited dependencies.

Those more advanced tools extend the same principle: do not enumerate every object if a probability calculation can certify that an acceptable object must exist.

The probabilistic method is a kind of mathematical compression. A gigantic finite search is replaced by one inequality about an average. The final claim is not that a lucky drawing happened. It is that failure at every point would contradict the calculation. Randomness in the proof reveals certainty about the existence of structure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

If \(X\) is a nonnegative integer-valued random variable with \(\mathbb E[X]<1\), then \(\Pr(X=0)>0\). For indicators \(I_j\) of bad events, \(X=\sum_j I_j\), so \(\mathbb E[X]=\sum_j\Pr(I_j=1)\), **without** independence among the bad events.

**Hypergraph property B sufficient condition.** In an \(r\)-uniform hypergraph with \(m\) edges, independent fair vertex colors give
\[
\mathbb E[X]=m\,2^{1-r};\quad m<2^{r-1}\Longrightarrow\text{there is a two-coloring with no monochromatic edge}.
\]

**Ramsey lower bound.** For independent red-blue edge colors on \(K_n\),
\[
\mathbb E[X_k]=\binom nk\,2^{1-\binom k2}.
\]
If this quantity is strictly less than one, \(R(k,k)>n\).

**Independent-set bound (Caro–Wei).** In a finite simple graph, a random vertex ordering and the local-minima selection rule give
\[
\alpha(G)\ge \sum_{v\in V(G)}\frac1{d(v)+1}\ge\frac{n}{\bar d+1}.
\]
The second inequality is Jensen's, since \(x\mapsto1/(x+1)\) is convex on \([0,\infty)\).

**Derandomization.** If \(\mathbb E[X]<1\), choose successive outcomes without increasing the conditional expectation. The resulting fully determined integer \(X\) is \(<1\), hence zero. Computational efficiency additionally requires an efficient conditional-expectation oracle.

### Exercises with answers

1. For \(r=4\), what does the sufficient hypergraph-coloring bound say? **Answer:** any 4-uniform hypergraph with fewer than eight edges is two-colorable.
2. Why can monochromatic-edge indicators be dependent without invalidating the proof? **Answer:** linearity of expectation holds without independence.
3. What is the bound for a \(d\)-regular graph with \(n\) vertices? **Answer:** \(\alpha(G)\ge n/(d+1)\).
4. Does the Ramsey expectation proof identify a specific coloring? **No:** it proves one exists; conditional expectations may give a construction when efficiently computable.

### Reading and source notes

- Joel Spencer, [*Probabilistic Methods in Combinatorics*](https://cs.nyu.edu/~spencer/papers/icmtalk.pdf), including the Erdős Ramsey first-moment argument.
- Noga Alon and Joel H. Spencer, *The Probabilistic Method*, fourth edition (Wiley, 2016).
- Joel Spencer, [*Ten Lectures on the Probabilistic Method*](https://pages.cs.wisc.edu/~cs787-1/Spencer.pdf).
