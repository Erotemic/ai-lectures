# 022000 — Martingales, Bounded Differences, and Concentration

**Track:** Discrete Mathematics and Combinatorics. **Background:** conditional expectation, random graphs, independent random variables, basic probability bounds. **Central question:** why do complicated random constructions often remain close to their expected behavior?

<!-- BEGIN SPOKEN LECTURE -->

# Concentration Through Martingales and Bounded Differences

We often analyze a random graph by computing how many edges or triangles it is expected to contain. Expectation is valuable, but it describes an average over many random outcomes. To know whether a typical graph behaves that way, we need a stronger statement: a bound on the probability of being far from the average.

Concentration inequalities provide those bounds. Some rely on independence and a sum of small contributions. Others apply even when the quantity of interest is a complicated function of many independent choices. The key question then is not whether the final quantity is a sum, but how much it can change when one input choice changes.

Imagine constructing a random graph by revealing one possible edge at a time. There may be many thousands of edges to decide. The final number of triangles depends on all of them in an entangled way. Yet changing one edge affects only the triangles that use that edge. That local sensitivity gives a route to global probability bounds.

## Revealing information one piece at a time

A martingale is a sequence of random variables whose next conditional expectation, given everything currently known, equals the present value. One way to construct a martingale is to begin with the expected value of a final random quantity, reveal one random input, update the conditional expectation, and continue until the final quantity is known.

This is called the Doob exposure martingale. It records how our best prediction evolves as information arrives. Its increments may be positive or negative, but by construction their conditional means are zero.

Suppose that changing the i-th independent input, while fixing all others, can alter the final output by at most a number c sub i. Then revealing that input cannot change the conditional expectation by more than that amount. This turns a deterministic sensitivity statement into a bound on martingale increments.

The Azuma–Hoeffding inequality says that a martingale with bounded increments is unlikely to accumulate a large unexpected deviation. The exponential decay is controlled by the sum of the squared increment bounds. The larger the number of small influences, the more tightly the final result can concentrate when measured against the appropriate scale.

## A concrete count of random edges

Let a graph have n vertices, with each possible edge independently present with probability p. There are n choose two possible edges. The expected number of present edges is that number times p.

The final edge count is the sum of independent zero-or-one variables. Changing the outcome of one edge changes the count by at most one. A bounded-differences inequality therefore gives an exponentially small upper bound on the probability that the count differs from expectation by a prescribed amount.

For a graph with one hundred vertices, there are four thousand nine hundred fifty potential edges. A fluctuation of order the square root of this number is normal; a fluctuation proportional to the number of potential edges has an exponentially small probability. The bound does not say the edge count is always close to its expectation. It quantifies how rare a large deviation is.

For a sum of independent Bernoulli variables, sharper Chernoff inequalities are often preferable because they use more information about the distribution and the mean. Bounded differences are especially useful when the output is not a simple sum.

## Counting triangles reveals the tradeoff

Consider the number of triangles in that same random graph. Flipping one edge can create or destroy at most n minus two triangles: one for each possible third vertex. So bounded differences still applies, with a larger sensitivity per revealed edge.

The resulting concentration inequality is valid, but sometimes weak. It treats every potential edge as though it could always affect the maximum possible number of triangles, even when the graph is sparse and most candidate triangles do not exist. More refined approaches can use variances, dependency structures, or specialized martingale bounds to obtain sharper results.

This is an important methodological lesson. A correct inequality may be too coarse for the mathematical question. Validity and strength are different properties. We should inspect what information the bound discards before treating it as a final answer.

## From concentration to constructive probability

Concentration inequalities also support the probabilistic method. If a random construction has a positive probability of satisfying all desired properties, then at least one deterministic object with those properties exists. Previously we used expectation to prove existence. Now we can show that not only one lucky configuration, but a large fraction of outcomes, work.

For example, suppose an algorithm makes many independent random choices, and changing one choice can alter a performance score by only a small amount. If its expected score is good, bounded differences may establish that most runs achieve a score close to that expectation. The random method becomes reliable rather than merely promising on average.

But independence of the exposed inputs matters for the standard bounded-differences theorem. A martingale can handle certain dependencies, provided its increments are bounded in the appropriate filtration. One cannot simply apply the independent-input inequality to strongly correlated choices and hope the same estimate survives.

The central idea is a bridge between two kinds of reasoning. First we prove a deterministic Lipschitz statement: no single input can move the answer very far. Then we combine that with the randomness of independent inputs, or a suitable martingale, to show that many small changes are unlikely to align in one direction. This is why concentration can govern random graphs, randomized algorithms, and combinatorial constructions with very complicated outputs.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(M_0,\ldots,M_N\) be a martingale with respect to a filtration \(\mathcal F_i\), with \(|M_i-M_{i-1}|\le c_i\) almost surely. Azuma–Hoeffding gives
\[\mathbf P(M_N-M_0\ge t)\le \exp\!\left(-\frac{t^2}{2\sum_{i=1}^N c_i^2}\right).\]
For independent inputs \(X_1,\ldots,X_N\) and a function f satisfying \(|f(x)-f(x')|\le c_i\) whenever inputs differ only at coordinate i, McDiarmid's bounded-differences inequality is
\[\mathbf P(f(X)-\mathbf E f(X)\ge t)\le\exp\!\left(-\frac{2t^2}{\sum_i c_i^2}\right).\]
These are distinct inequalities with different constants and hypotheses. The Doob martingale \(M_i=\mathbf E[f(X)\mid X_1,\ldots,X_i]\) connects them.

For \(G(n,p)\), the edge count \(E\) has \(N=\binom n2\) independent Bernoulli indicators, \(\mathbf E E=Np\), and McDiarmid gives \(\mathbf P(|E-Np|\ge t)\le 2e^{-2t^2/N}\). For the triangle count T, changing one potential edge alters T by at most n−2, so the valid bounded-differences bound has denominator \(N(n-2)^2\). It need not be sharp, particularly when p is small.

### Exercises with answers

1. What is \(\mathbf E E\) for \(G(10,1/2)\)? **Answer:** \(\binom{10}2/2=22.5\).
2. Give a coordinate sensitivity for the number of triangles in \(G(10,p)\). **Answer:** at most 8 triangles can involve any chosen edge.
3. What is the difference between an expected value and a concentration bound? **Answer:** expectation is an average; concentration bounds probabilities of deviations from that average.
4. Can McDiarmid be applied unchanged to arbitrarily dependent input coordinates? **Answer:** no; the standard result assumes independent coordinates.

### Reading and source notes

- [MIT OpenCourseWare 6.042J Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), conditional expectation and concentration foundations.
- [Carnegie Mellon 15-859FF course materials](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859-f19/www/), randomized methods in algorithmic combinatorics.
