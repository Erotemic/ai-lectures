# Random discrete structures: existence, reliability, and concentration

<!-- BEGIN SPOKEN LECTURE -->

# Random discrete structures: existence, reliability, and concentration

## The Probabilistic Method: Existence without Construction

Imagine a mathematical object defined by millions of choices: the colors of edges in a complete graph, or which vertices belong to a particular set. Searching every configuration is hopeless. But perhaps most choices are not disastrous. Or perhaps the expected number of failures is less than one. Then, without naming the successful object, we can prove that it exists.

This is the probabilistic method. It uses probability to prove a deterministic statement of existence. The random experiment is an instrument of the proof, not a claim that the desired object must itself be random.

### If the expected number of failures is less than one

Let X count bad events in a random construction. X is a nonnegative integer. If the expectation of X is less than one, then X cannot be positive for every outcome. If every outcome had at least one failure, its average would be at least one. Therefore some outcome has no failures at all.

That observation is simple, but it changes what we need to calculate. We do not need the exact probability that every bad event is absent. We only need an upper bound on the expected number of bad events. By linearity of expectation, we can add the individual probabilities even if the events are heavily dependent.

This is often much easier than an exact counting argument.

### Coloring a uniform hypergraph

A hypergraph generalizes a graph: an edge may contain more than two vertices. Suppose every hyperedge contains exactly r vertices, and there are m hyperedges. We want to color the vertices red and blue so that no hyperedge is monochromatic.

Color each vertex independently, each color with probability one half. Fix one hyperedge. All r vertices are red with probability two to the negative r, and all are blue with the same probability. Thus the probability that this edge is monochromatic is two to the power one minus r.

Let X count monochromatic hyperedges. By linearity of expectation, its expected value is m times that probability. So when m is strictly smaller than two to the power r minus one, the expectation is below one. Some coloring makes X zero. No hyperedge is monochromatic.

Notice how little we assumed about the pattern of intersections among hyperedges. They may share many vertices. The expectation argument still works because linearity requires no independence among the indicator variables. Independence was used only to compute the probability for each fixed edge.

We have proved a universal sufficient condition for two-colorability of a uniform hypergraph. It may not be sharp for a particular hypergraph, but it is a clean existence theorem with remarkably little structural information.

### A Ramsey lower bound

Now consider a complete graph with n labeled vertices, and color each edge red or blue independently. We seek a coloring with no monochromatic complete subgraph on k vertices. For any fixed k-element set S, the edges inside S are monochromatic exactly when all are red or all are blue.

There are k choose two edges inside S. The probability that they all have one color is two to the power one minus k choose two. And there are n choose k choices for S. Therefore the expected number of monochromatic k-vertex complete subgraphs equals n choose k times two to the power one minus k choose two.

If that product is less than one, a coloring without any monochromatic k-clique exists. In the language of Ramsey numbers, the diagonal Ramsey number R of k and k exceeds n.

This is a lower bound, not a construction of a particular extremal coloring. It was among the influential early examples developed by Paul Erdős. The method does not tell us which coloring works, only that the space of all colorings cannot be entirely bad.

### Random order and independent sets

The same point of view can prove a useful bound on independent sets. Choose a uniformly random ordering of the vertices of any finite simple graph. Select a vertex when it occurs earlier than all of its neighbors. No two adjacent vertices can both be selected: on an edge, one endpoint must occur later than the other.

For a vertex v with degree d, its chance of appearing first among itself and its d neighbors is one divided by d plus one. Sum these probabilities over all vertices. The expected size of the selected independent set is the sum of those reciprocals.

Therefore the graph has an independent set at least as large as that sum, rounded up as necessary. If its average degree is d bar, the convexity of one divided by x plus one gives the simpler lower bound n divided by d bar plus one.

Here the random choice was not a random subset of vertices but a random ordering. Selecting the right probability space can make the desired structural property automatic. Only the size remains to be controlled by expectation.

### From existence to algorithms

A proof by random choice may look nonconstructive, but sometimes we can systematically remove the randomness. Suppose our proof shows that the expected number of bad events is below one. Expose the random choices one at a time. At each step, choose a value whose conditional expected number of future failures is no larger than the current expectation. Such a choice exists because the current conditional expectation is an average of the possible next conditional expectations.

After all choices have been fixed, the remaining conditional expectation equals the actual integer number of failures. It is still less than one, so it must be zero. This is the method of conditional expectations.

There is a qualification. A proof that this deterministic procedure exists does not automatically give an efficient algorithm. We must also be able to compute or bound the relevant conditional expectations efficiently. When that is possible, a probabilistic existence proof may become a practical deterministic construction.

### Beyond the first moment

The first-moment argument works when the total expected number of failures is already less than one. If each failure is rare but there are too many of them to make that sum small, we may need other tools. A second-moment calculation can show that a random variable is positive somewhere by controlling its variance. The Lovász local lemma can show that all bad events can be avoided when they are sufficiently rare and have limited dependencies.

Those more advanced tools extend the same principle: do not enumerate every object if a probability calculation can certify that an acceptable object must exist.

The probabilistic method is a kind of mathematical compression. A gigantic finite search is replaced by one inequality about an average. The final claim is not that a lucky drawing happened. It is that failure at every point would contradict the calculation. Randomness in the proof reveals certainty about the existence of structure.

## Random Graph Thresholds, Second Moments, and Concentration

Imagine beginning with one hundred isolated vertices. For every possible pair, flip an independent biased coin: with probability p, place an edge; otherwise leave the pair disconnected. Repeat the experiment many times while slowly increasing p. At some densities, most outcomes are collections of tiny components. At others, one large component dominates. Eventually isolated vertices disappear and the graph becomes connected with high probability.

This is the Erdős–Rényi random graph model, often called G of n comma p. It invites a precise question. What does it mean for a property to have a threshold, and how can elementary inequalities reveal where that threshold lies?

### From random edges to random variables

There are n choose two potential edges. Each is present independently with probability p. Their indicators are independent Bernoulli random variables. Summing them gives the total edge count, with expectation p times n choose two.

The degree of a fixed vertex is a different sum: it counts the n minus one possible edges incident to that vertex. Its expected value is p times n minus one. Because those edge choices are independent, its degree follows a binomial distribution.

But degrees at different vertices are not independent: any pair shares the possible edge joining them. A claim about one vertex cannot be multiplied into a claim about all vertices without accounting for their dependencies. Linearity of expectation works even when variables are dependent. Multiplying probabilities, in contrast, requires independence or a carefully justified conditional argument.

### The first-moment threshold for isolated vertices

Consider X, the number of isolated vertices. A given vertex is isolated if all n minus one of its possible incident edges are missing. Its probability of isolation is one minus p, raised to the power n minus one. Therefore the expected number of isolated vertices is n times that probability.

Suppose p is approximately the logarithm of n divided by n. Then the expected number of isolated vertices is of constant order. If p is substantially larger—more precisely, if n p minus log n tends to positive infinity while p stays in the relevant sparse range—the expected count tends to zero. Markov's inequality now gives a complete conclusion: the probability of even one isolated vertex tends to zero.

This is a first-moment existence argument in reverse. An event that would force a nonnegative count to be at least one must become improbable when the expected count goes to zero.

What if p is smaller? Then the expectation of X grows. Can we conclude isolated vertices probably exist? Not from expectation alone. A random variable may have a large mean because it is enormous on extremely rare outcomes. We need to understand its variance or another measure of concentration.

### The second moment supplies the missing direction

Write X as the sum of isolation indicators, one for each vertex. For two distinct vertices to both be isolated, all their incident edges must be absent. There are two n minus three distinct edges in that union, because the edge between the pair was counted twice. Their joint isolation probability is one minus p to that power.

This lets us compute the second moment of X. Below the logarithmic threshold by a term tending to infinity, the variance is small compared with the square of the growing mean. Chebyshev's inequality then shows X is positive with probability tending to one.

The threshold is therefore not a loose intuition about when the average degree becomes large. It is a precise two-sided statement obtained by pairing first and second moment arguments.

At the finer scale p equals log n plus a fixed constant c, all divided by n, the expected number of isolated vertices approaches the exponential of negative c. In fact, the count of isolated vertices converges in distribution to a Poisson random variable with that mean. The limiting probability of having no isolated vertex is therefore the exponential of minus the exponential of negative c. Proving the Poisson statement requires more than the first two moments; one route uses factorial moments.

The connectivity threshold of the whole graph occurs at the same scale. Showing that disappearance of isolated vertices accounts for connectivity at this scale requires ruling out other small disconnected components; the isolated-vertex calculation alone is not a proof of connectivity.

### Concentration when many independent choices contribute

For sums of independent bounded random variables, expectation is often not enough to describe the typical outcome. Chernoff bounds quantify how difficult it is for a Bernoulli sum to depart substantially from its mean.

A standard multiplicative form says that the probability of exceeding one plus delta times the mean decays exponentially in the mean, with an exponent depending on delta. The lower-tail bound behaves similarly. When the mean grows, relative deviations become less probable.

For a fixed vertex, we may apply such bounds directly to its degree. But for a conclusion about every vertex, we also need a union bound over all n vertices. If the probability that one vertex has a large deviation is roughly n to a negative power, multiplying by n may still be too large unless the exponent beats one.

This explains why an average-degree estimate does not automatically give nearly regular behavior at the graph-wide level. We must pay for the number of simultaneous claims.

### A second threshold: triangles

An isolated vertex depends on missing edges around one point. A triangle depends on three present edges among a triple of vertices. Let T count the triangles. Every triple has probability p cubed of forming a triangle, so the expected value is n choose three times p cubed.

When p is far below one over n, this expected value goes to zero. Markov tells us a triangle is then absent with high probability. When p is much larger than one over n, the expected value grows, and a second-moment argument can show that triangles appear with high probability. At the critical scale p equals c divided by n for fixed positive c, the expected triangle count tends to c cubed divided by six.

Two graph properties therefore have very different characteristic densities. Triangle appearance occurs around one over n. The disappearance of isolated vertices occurs around log n over n. A graph can have many triangles while still containing many isolated vertices.

### What a threshold means—and does not mean

A threshold is an asymptotic statement about a sequence of graphs as n grows. It does not say that every graph of a given size suddenly changes at one exact value of p. It also does not say all properties change at the same rate. Some thresholds have narrow windows; others are spread over larger ranges.

The broad lesson is a method. Represent a structural feature by a count. Calculate its expectation. Use the first moment to rule out existence on one side. Use second moments, concentration, or more refined distributional methods to establish existence on the other side. Finally, distinguish the property you actually proved from a nearby one that still needs its own argument.

Random graph theory turns seemingly chaotic networks into objects whose large-scale behavior can be predicted. The prediction succeeds because probability, combinatorics, and asymptotic reasoning work together—not because randomness erases structure, but because it creates structure that can be quantified.

Thresholds describe when random structure appears. Reliability asks a related question about a fixed network whose edges may fail: how likely is the surviving graph to stay connected?

## Network Reliability and Random Connectivity

A network can have hundreds of edges and still become useless when one critical connection fails. Another network with fewer edges can survive many failures because it has alternative routes. Counting edges is not the same as counting reliable paths. To measure reliability, we have to ask which combinations of surviving edges leave the network connected.

Start with three vertices arranged in a path. There are two required links. If each survives independently with probability p, both must survive, so the probability of connectivity is p squared. Now connect the endpoints, turning the path into a triangle. Any two of its three links suffice. The reliability becomes three times p squared minus two times p cubed. At a survival probability of one half, the path is connected only one quarter of the time; the triangle is connected one half of the time.

That difference is redundancy expressed as a polynomial. The triangle has three separate ways for exactly two edges to survive, and it also succeeds when all three survive. We are not adding probabilities of paths directly, because path events overlap. Correct counting handles the overlaps.

### The reliability polynomial

Fix an undirected graph with a given set of possible links. Suppose every link survives independently with the same probability p. For each subset of surviving edges, ask whether it connects all the vertices. Add the probability of that subset over all connected subsets. The result is the graph's all-terminal reliability polynomial.

The formula is finite and exact. It also becomes expensive for a large graph, because the number of edge subsets grows exponentially. Structural information can help. A bridge must survive in every connected realization, so its survival probability factors out. A cut is a collection of edges whose complete failure disconnects the graph. Small cuts often dominate failure probability when links are individually reliable.

There is a second, useful question. Instead of keeping a graph fixed and randomly deleting links, start with a set of n vertices and include each possible edge independently with probability p. This is the Erdős–Rényi random graph model. Now we ask how p should scale with n for the entire graph to be connected with high probability.

### Why one isolated vertex controls the threshold

Choose a particular vertex. It has n minus one possible neighbors. To be isolated, all those potential edges must be absent. The isolation probability is one minus p, raised to the n minus one power.

Multiply by n and we get the expected number of isolated vertices. If p is roughly a constant divided by n, the graph may already contain a giant connected component, but it still has many isolated vertices. The giant component is not the whole graph.

A different scale emerges when p is approximately log n divided by n. At that scale, the probability of one given vertex being isolated is roughly one over n. With n possible vertices, the expected number of isolated vertices is roughly one. The logarithm appears because the problem is not to connect a typical vertex, but to prevent even one vertex from being left behind.

Suppose p equals log n plus a fixed constant c, all divided by n. Then the number of isolated vertices approaches a Poisson distribution with mean the exponential of minus c. Consequently, the probability of having no isolated vertices approaches the exponential of minus the exponential of minus c.

The remarkable theorem is that, in this critical window, the probability the entire graph is connected approaches the same expression. Showing that there are no isolated vertices is not by itself sufficient: one must also rule out disconnected components of size two or more. The theorem says their remaining probability becomes negligible in this window.

### A transition, not a fixed safe percentage

If p is a fixed fraction smaller than log n divided by n, the graph is disconnected with probability tending to one as n grows. If p is a fixed fraction larger, it is connected with probability tending to one. This is a threshold phenomenon: the relevant scale shifts as the system grows.

It would be a mistake to say every real network has this threshold. The independent-edge model permits every possible connection and makes all those connections equally likely. Physical and communication networks have geography, correlated failures, designed redundancy, and constraints that are not present in this model.

Even within the model, reliability at a finite n is a probability, not a guarantee. A network with p above the asymptotic threshold can still disconnect. The sharp threshold tells us how the probability behaves for large n, not which specific sample must work.

### What this viewpoint teaches us

The exact reliability polynomial answers the question for a fixed graph. Random graph theory answers what happens for a growing family of graphs. Cut sets explain particular vulnerabilities. Isolated vertices explain the connectivity threshold. These are complementary viewpoints, and each exposes a different reason that redundancy matters.

The deepest lesson is that connecting almost everybody and connecting everybody are mathematically different tasks. The last isolated vertex can require a logarithmic increase in the number of links per node. A robust network must be designed and analyzed for the guarantee it actually needs.

## Martingales, Bounded Differences, and Concentration

We often analyze a random graph by computing how many edges or triangles it is expected to contain. Expectation is valuable, but it describes an average over many random outcomes. To know whether a typical graph behaves that way, we need a stronger statement: a bound on the probability of being far from the average.

Concentration inequalities provide those bounds. Some rely on independence and a sum of small contributions. Others apply even when the quantity of interest is a complicated function of many independent choices. The key question then is not whether the final quantity is a sum, but how much it can change when one input choice changes.

Imagine constructing a random graph by revealing one possible edge at a time. There may be many thousands of edges to decide. The final number of triangles depends on all of them in an entangled way. Yet changing one edge affects only the triangles that use that edge. That local sensitivity gives a route to global probability bounds.

### Revealing information one piece at a time

A martingale is a sequence of random variables whose next conditional expectation, given everything currently known, equals the present value. One way to construct a martingale is to begin with the expected value of a final random quantity, reveal one random input, update the conditional expectation, and continue until the final quantity is known.

This is called the Doob exposure martingale. It records how our best prediction evolves as information arrives. Its increments may be positive or negative, but by construction their conditional means are zero.

Suppose that changing the i-th independent input, while fixing all others, can alter the final output by at most a number c sub i. Then revealing that input cannot change the conditional expectation by more than that amount. This turns a deterministic sensitivity statement into a bound on martingale increments.

The Azuma–Hoeffding inequality says that a martingale with bounded increments is unlikely to accumulate a large unexpected deviation. The exponential decay is controlled by the sum of the squared increment bounds. The larger the number of small influences, the more tightly the final result can concentrate when measured against the appropriate scale.

### A concrete count of random edges

Let a graph have n vertices, with each possible edge independently present with probability p. There are n choose two possible edges. The expected number of present edges is that number times p.

The final edge count is the sum of independent zero-or-one variables. Changing the outcome of one edge changes the count by at most one. A bounded-differences inequality therefore gives an exponentially small upper bound on the probability that the count differs from expectation by a prescribed amount.

For a graph with one hundred vertices, there are four thousand nine hundred fifty potential edges. A fluctuation of order the square root of this number is normal; a fluctuation proportional to the number of potential edges has an exponentially small probability. The bound does not say the edge count is always close to its expectation. It quantifies how rare a large deviation is.

For a sum of independent Bernoulli variables, sharper Chernoff inequalities are often preferable because they use more information about the distribution and the mean. Bounded differences are especially useful when the output is not a simple sum.

### Counting triangles reveals the tradeoff

Consider the number of triangles in that same random graph. Flipping one edge can create or destroy at most n minus two triangles: one for each possible third vertex. So bounded differences still applies, with a larger sensitivity per revealed edge.

The resulting concentration inequality is valid, but sometimes weak. It treats every potential edge as though it could always affect the maximum possible number of triangles, even when the graph is sparse and most candidate triangles do not exist. More refined approaches can use variances, dependency structures, or specialized martingale bounds to obtain sharper results.

This is an important methodological lesson. A correct inequality may be too coarse for the mathematical question. Validity and strength are different properties. We should inspect what information the bound discards before treating it as a final answer.

### From concentration to constructive probability

Concentration inequalities also support the probabilistic method. If a random construction has a positive probability of satisfying all desired properties, then at least one deterministic object with those properties exists. Previously we used expectation to prove existence. Now we can show that not only one lucky configuration, but a large fraction of outcomes, work.

For example, suppose an algorithm makes many independent random choices, and changing one choice can alter a performance score by only a small amount. If its expected score is good, bounded differences may establish that most runs achieve a score close to that expectation. The random method becomes reliable rather than merely promising on average.

But independence of the exposed inputs matters for the standard bounded-differences theorem. A martingale can handle certain dependencies, provided its increments are bounded in the appropriate filtration. One cannot simply apply the independent-input inequality to strongly correlated choices and hope the same estimate survives.

The central idea is a bridge between two kinds of reasoning. First we prove a deterministic Lipschitz statement: no single input can move the answer very far. Then we combine that with the randomness of independent inputs, or a suitable martingale, to show that many small changes are unlikely to align in one direction. This is why concentration can govern random graphs, randomized algorithms, and combinatorial constructions with very complicated outputs.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### The Probabilistic Method: Existence without Construction

**Track:** Discrete Mathematics and Combinatorics. **Background:** counting, elementary probability, graphs and hypergraphs. **Central question:** how can a random experiment prove the existence of a mathematical object even when we never exhibit it?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. For \(r=4\), what does the sufficient hypergraph-coloring bound say? **Answer:** any 4-uniform hypergraph with fewer than eight edges is two-colorable.
2. Why can monochromatic-edge indicators be dependent without invalidating the proof? **Answer:** linearity of expectation holds without independence.
3. What is the bound for a \(d\)-regular graph with \(n\) vertices? **Answer:** \(\alpha(G)\ge n/(d+1)\).
4. Does the Ramsey expectation proof identify a specific coloring? **No:** it proves one exists; conditional expectations may give a construction when efficiently computable.

##### Reading and source notes

- Joel Spencer, [*Probabilistic Methods in Combinatorics*](https://cs.nyu.edu/~spencer/papers/icmtalk.pdf), including the Erdős Ramsey first-moment argument.
- Noga Alon and Joel H. Spencer, *The Probabilistic Method*, fourth edition (Wiley, 2016).
- Joel Spencer, [*Ten Lectures on the Probabilistic Method*](https://pages.cs.wisc.edu/~cs787-1/Spencer.pdf).

### Random Graph Thresholds, Second Moments, and Concentration

**Track:** Discrete Mathematics and Combinatorics. **Background:** graph properties, indicator variables, expectation, variance, and basic probability. **Central question:** at what edge density does a random graph suddenly acquire a global property?

#### Mathematical companion (not spoken)

In \(G(n,p)\), each edge independently exists with probability \(p\). Edge count \(E\sim\operatorname{Bin}(\binom n2,p)\) and fixed-vertex degree \(d(v)\sim\operatorname{Bin}(n-1,p)\).

Let \(X\) count isolated vertices. With \(I_v=1_{\{v\text{ isolated}\}}\):
\[\mathbb EX=n(1-p)^{n-1},\qquad\mathbb E[X(X-1)]=n(n-1)(1-p)^{2n-3}.\]
When \(p=(\log n+c)/n\) with fixed real \(c\), \(\mathbb EX\to e^{-c}\), and \(X\) converges to \(\operatorname{Poisson}(e^{-c})\); hence \(\Pr(X=0)\to\exp(-e^{-c})\). At the same window, \(\Pr(G(n,p)\text{ connected})\to\exp(-e^{-c})\), a strictly stronger theorem requiring exclusion of other disconnected components.

For independent Bernoulli variables with sum \(Y\) and mean \(\mu\), a standard Chernoff bound is
\[\Pr(Y\ge(1+\delta)\mu)\le\exp\left(-\frac{\delta^2\mu}{2+\delta}\right),\qquad\Pr(Y\le(1-\delta)\mu)\le\exp(-\delta^2\mu/2)\quad(0<\delta<1).\]
For triangle count \(T\), \(\mathbb ET=\binom n3p^3\). Thus the appearance threshold is at scale \(p\asymp1/n\), distinct from connectivity scale \(\log n/n\).

##### Exercises with answers

1. What is the expected number of edges at \(p=c/n\)? **Answer:** \(\binom n2 c/n=c(n-1)/2\).
2. At \(p=(\log n+\omega(n))/n\), \(\omega(n)\to\infty\), why are isolated vertices absent with high probability? **Answer:** \(\mathbb EX\to0\), so \(\Pr(X\ge1)\le\mathbb EX\to0\), with \(p\in[0,1]\).
3. Why is \(\Pr(I_u=I_v=1)=(1-p)^{2n-3}\), not \((1-p)^{2n-2}\)? **Answer:** the edge \(uv\) is shared by both incident-edge lists.
4. Does a positive expected triangle count prove a triangle exists with high probability? **No:** use a second-moment or stronger distributional argument.

##### Reading and source notes

- Noga Alon and Joel H. Spencer, [*The Probabilistic Method*](https://www.wiley.com/en-us/The+Probabilistic+Method%2C+4th+Edition-p-9781119061953), moments and concentration tools.
- [Georgia Tech, Random Graphs lecture notes](https://santoshv.github.io/2023CS4540/Lec8_1011.pdf), isolated-vertex threshold and second-moment proof.
- [MIT Mathematics, Combinatorics course materials](https://ocw.mit.edu/courses/18-314-combinatorial-analysis-fall-2014/), random structures and counting foundations.

### Network Reliability and Random Connectivity

**Track:** Discrete Mathematics and Combinatorics. **Background:** graphs, independent random variables, inclusion–exclusion, concentration and thresholds. **Central question:** how many independent links does a network need before all its vertices are connected?

#### Mathematical companion (not spoken)

For a fixed connected-or-not graph G=(V,E), m=|E|, with iid edge-survival probability p, its all-terminal reliability is
\[R_G(p)=\sum_{A\subseteq E\, :\, (V,A)\text{ connected}}p^{|A|}(1-p)^{m-|A|}.\]
For the path P_3, \(R_{P_3}(p)=p^2\). For the triangle C_3, \(R_{C_3}(p)=3p^2(1-p)+p^3=3p^2-2p^3\). At p=1/2 these are 1/4 and 1/2.

Let G(n,p) be the random graph with independent edges. If I_n is the number of isolated vertices, then
\[\mathbb E I_n=n(1-p)^{n-1}.\]
For \(p=(\log n+c)/n\) and fixed real c, \(\mathbb EI_n\to e^{-c}\). More strongly, \(I_n\Rightarrow\mathrm{Poisson}(e^{-c})\) and the **connectivity window theorem** gives
\[\Pr\big(G(n,p)\text{ connected}\big)\longrightarrow e^{-e^{-c}}.\]
In particular, for constant \(a<1\), p=a log(n)/n gives probability tending to zero; for constant a>1 it tends to one. The proof of the limiting formula also controls components of size two through n/2; convergence of the isolated-vertex count alone does not prove connectivity.

An elementary failure bound for a fixed graph uses cuts: for any specified cut C, all its edges failing has probability \((1-p)^{|C|}\), giving a **lower** bound on the probability of disconnection. A union bound over cuts gives an upper bound, but generally overcounts overlapping events.

##### Exercises with answers

1. Evaluate triangle reliability at p=3/4. **Answer:** \(3(9/16)-2(27/64)=54/32-27/32=27/32\).
2. Why does every bridge factor p out of all-terminal reliability? **Answer:** every connected surviving-edge set must contain the bridge.
3. If p=log(n)/n, to what constant does the connectivity probability converge? **Answer:** \(e^{-1}\), since c=0.
4. Does the existence of one giant component imply connectivity? **Answer:** no; isolated vertices and other small components can remain.

##### Reading and source notes

- [Richard Durrett, Erdős–Rényi Random Graphs, Chapter 1](https://services.math.duke.edu/~rtd/DoG/Chapter1.pdf), especially the connectivity window proof.
- [Ryan O'Donnell, Probability and Computing lecture notes](https://www.cs.cmu.edu/~odonnell/papers/probability-and-computing-lecture-notes.pdf), random graph threshold examples.

### Martingales, Bounded Differences, and Concentration

**Track:** Discrete Mathematics and Combinatorics. **Background:** conditional expectation, random graphs, independent random variables, basic probability bounds. **Central question:** why do complicated random constructions often remain close to their expected behavior?

#### Mathematical companion (not spoken)

Let \(M_0,\ldots,M_N\) be a martingale with respect to a filtration \(\mathcal F_i\), with \(|M_i-M_{i-1}|\le c_i\) almost surely. Azuma–Hoeffding gives
\[\mathbf P(M_N-M_0\ge t)\le \exp\!\left(-\frac{t^2}{2\sum_{i=1}^N c_i^2}\right).\]
For independent inputs \(X_1,\ldots,X_N\) and a function f satisfying \(|f(x)-f(x')|\le c_i\) whenever inputs differ only at coordinate i, McDiarmid's bounded-differences inequality is
\[\mathbf P(f(X)-\mathbf E f(X)\ge t)\le\exp\!\left(-\frac{2t^2}{\sum_i c_i^2}\right).\]
These are distinct inequalities with different constants and hypotheses. The Doob martingale \(M_i=\mathbf E[f(X)\mid X_1,\ldots,X_i]\) connects them.

For \(G(n,p)\), the edge count \(E\) has \(N=\binom n2\) independent Bernoulli indicators, \(\mathbf E E=Np\), and McDiarmid gives \(\mathbf P(|E-Np|\ge t)\le 2e^{-2t^2/N}\). For the triangle count T, changing one potential edge alters T by at most n−2, so the valid bounded-differences bound has denominator \(N(n-2)^2\). It need not be sharp, particularly when p is small.

##### Exercises with answers

1. What is \(\mathbf E E\) for \(G(10,1/2)\)? **Answer:** \(\binom{10}2/2=22.5\).
2. Give a coordinate sensitivity for the number of triangles in \(G(10,p)\). **Answer:** at most 8 triangles can involve any chosen edge.
3. What is the difference between an expected value and a concentration bound? **Answer:** expectation is an average; concentration bounds probabilities of deviations from that average.
4. Can McDiarmid be applied unchanged to arbitrarily dependent input coordinates? **Answer:** no; the standard result assumes independent coordinates.

##### Reading and source notes

- [MIT OpenCourseWare 6.042J Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), conditional expectation and concentration foundations.
- [Carnegie Mellon 15-859FF course materials](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859-f19/www/), randomized methods in algorithmic combinatorics.
