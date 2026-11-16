# 016000 — Random Graph Thresholds, Second Moments, and Concentration

**Track:** Discrete Mathematics and Combinatorics. **Background:** graph properties, indicator variables, expectation, variance, and basic probability. **Central question:** at what edge density does a random graph suddenly acquire a global property?

<!-- BEGIN SPOKEN LECTURE -->

# Random Graph Thresholds, Second Moments, and Concentration

Imagine beginning with one hundred isolated vertices. For every possible pair, flip an independent biased coin: with probability p, place an edge; otherwise leave the pair disconnected. Repeat the experiment many times while slowly increasing p. At some densities, most outcomes are collections of tiny components. At others, one large component dominates. Eventually isolated vertices disappear and the graph becomes connected with high probability.

This is the Erdős–Rényi random graph model, often called G of n comma p. It invites a precise question. What does it mean for a property to have a threshold, and how can elementary inequalities reveal where that threshold lies?

## From random edges to random variables

There are n choose two potential edges. Each is present independently with probability p. Their indicators are independent Bernoulli random variables. Summing them gives the total edge count, with expectation p times n choose two.

The degree of a fixed vertex is a different sum: it counts the n minus one possible edges incident to that vertex. Its expected value is p times n minus one. Because those edge choices are independent, its degree follows a binomial distribution.

But degrees at different vertices are not independent: any pair shares the possible edge joining them. That distinction matters when we move from a statement about one vertex to a statement about all vertices. Linearity of expectation works even when variables are dependent. Multiplying probabilities, in contrast, requires independence or a carefully justified conditional argument.

## The first-moment threshold for isolated vertices

Consider X, the number of isolated vertices. A given vertex is isolated if all n minus one of its possible incident edges are missing. Its probability of isolation is one minus p, raised to the power n minus one. Therefore the expected number of isolated vertices is n times that probability.

Suppose p is approximately the logarithm of n divided by n. Then the expected number of isolated vertices is of constant order. If p is substantially larger—more precisely, if n p minus log n tends to positive infinity while p stays in the relevant sparse range—the expected count tends to zero. Markov's inequality now gives a complete conclusion: the probability of even one isolated vertex tends to zero.

This is a first-moment existence argument in reverse. An event that would force a nonnegative count to be at least one must become improbable when the expected count goes to zero.

What if p is smaller? Then the expectation of X grows. Can we conclude isolated vertices probably exist? Not from expectation alone. A random variable may have a large mean because it is enormous on extremely rare outcomes. We need to understand its variance or another measure of concentration.

## The second moment supplies the missing direction

Write X as the sum of isolation indicators, one for each vertex. For two distinct vertices to both be isolated, all their incident edges must be absent. There are two n minus three distinct edges in that union, because the edge between the pair was counted twice. Their joint isolation probability is one minus p to that power.

This lets us compute the second moment of X. Below the logarithmic threshold by a term tending to infinity, the variance is small compared with the square of the growing mean. Chebyshev's inequality then shows X is positive with probability tending to one.

The threshold is therefore not a loose intuition about when the average degree becomes large. It is a precise two-sided statement obtained by pairing first and second moment arguments.

At the finer scale p equals log n plus a fixed constant c, all divided by n, the expected number of isolated vertices approaches the exponential of negative c. In fact, the count of isolated vertices converges in distribution to a Poisson random variable with that mean. The limiting probability of having no isolated vertex is therefore the exponential of minus the exponential of negative c. Proving the Poisson statement requires more than the first two moments; one route uses factorial moments.

The connectivity threshold of the whole graph occurs at the same scale. Showing that disappearance of isolated vertices accounts for connectivity at this scale requires ruling out other small disconnected components; the isolated-vertex calculation alone is not a proof of connectivity.

## Concentration when many independent choices contribute

For sums of independent bounded random variables, expectation is often not enough to describe the typical outcome. Chernoff bounds quantify how difficult it is for a Bernoulli sum to depart substantially from its mean.

A standard multiplicative form says that the probability of exceeding one plus delta times the mean decays exponentially in the mean, with an exponent depending on delta. The lower-tail bound behaves similarly. When the mean grows, relative deviations become less probable.

For a fixed vertex, we may apply such bounds directly to its degree. But for a conclusion about every vertex, we also need a union bound over all n vertices. If the probability that one vertex has a large deviation is roughly n to a negative power, multiplying by n may still be too large unless the exponent beats one.

This explains why an average-degree estimate does not automatically give nearly regular behavior at the graph-wide level. We must pay for the number of simultaneous claims.

## A second threshold: triangles

An isolated vertex depends on missing edges around one point. A triangle depends on three present edges among a triple of vertices. Let T count the triangles. Every triple has probability p cubed of forming a triangle, so the expected value is n choose three times p cubed.

When p is far below one over n, this expected value goes to zero. Markov tells us a triangle is then absent with high probability. When p is much larger than one over n, the expected value grows, and a second-moment argument can show that triangles appear with high probability. At the critical scale p equals c divided by n for fixed positive c, the expected triangle count tends to c cubed divided by six.

Two graph properties therefore have very different characteristic densities. Triangle appearance occurs around one over n. The disappearance of isolated vertices occurs around log n over n. A graph can have many triangles while still containing many isolated vertices.

## What a threshold means—and does not mean

A threshold is an asymptotic statement about a sequence of graphs as n grows. It does not say that every graph of a given size suddenly changes at one exact value of p. It also does not say all properties change at the same rate. Some thresholds have narrow windows; others are spread over larger ranges.

The broad lesson is a method. Represent a structural feature by a count. Calculate its expectation. Use the first moment to rule out existence on one side. Use second moments, concentration, or more refined distributional methods to establish existence on the other side. Finally, distinguish the property you actually proved from a nearby one that still needs its own argument.

Random graph theory turns seemingly chaotic networks into objects whose large-scale behavior can be predicted. The prediction succeeds because probability, combinatorics, and asymptotic reasoning work together—not because randomness erases structure, but because it creates structure that can be quantified.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

In \(G(n,p)\), each edge independently exists with probability \(p\). Edge count \(E\sim\operatorname{Bin}(\binom n2,p)\) and fixed-vertex degree \(d(v)\sim\operatorname{Bin}(n-1,p)\).

Let \(X\) count isolated vertices. With \(I_v=1_{\{v\text{ isolated}\}}\):
\[\mathbb EX=n(1-p)^{n-1},\qquad\mathbb E[X(X-1)]=n(n-1)(1-p)^{2n-3}.\]
When \(p=(\log n+c)/n\) with fixed real \(c\), \(\mathbb EX\to e^{-c}\), and \(X\) converges to \(\operatorname{Poisson}(e^{-c})\); hence \(\Pr(X=0)\to\exp(-e^{-c})\). At the same window, \(\Pr(G(n,p)\text{ connected})\to\exp(-e^{-c})\), a strictly stronger theorem requiring exclusion of other disconnected components.

For independent Bernoulli variables with sum \(Y\) and mean \(\mu\), a standard Chernoff bound is
\[\Pr(Y\ge(1+\delta)\mu)\le\exp\left(-\frac{\delta^2\mu}{2+\delta}\right),\qquad\Pr(Y\le(1-\delta)\mu)\le\exp(-\delta^2\mu/2)\quad(0<\delta<1).\]
For triangle count \(T\), \(\mathbb ET=\binom n3p^3\). Thus the appearance threshold is at scale \(p\asymp1/n\), distinct from connectivity scale \(\log n/n\).

### Exercises with answers

1. What is the expected number of edges at \(p=c/n\)? **Answer:** \(\binom n2 c/n=c(n-1)/2\).
2. At \(p=(\log n+\omega(n))/n\), \(\omega(n)\to\infty\), why are isolated vertices absent with high probability? **Answer:** \(\mathbb EX\to0\), so \(\Pr(X\ge1)\le\mathbb EX\to0\), with \(p\in[0,1]\).
3. Why is \(\Pr(I_u=I_v=1)=(1-p)^{2n-3}\), not \((1-p)^{2n-2}\)? **Answer:** the edge \(uv\) is shared by both incident-edge lists.
4. Does a positive expected triangle count prove a triangle exists with high probability? **No:** use a second-moment or stronger distributional argument.

### Reading and source notes

- Noga Alon and Joel H. Spencer, [*The Probabilistic Method*](https://www.wiley.com/en-us/The+Probabilistic+Method%2C+4th+Edition-p-9781119061953), moments and concentration tools.
- [Georgia Tech, Random Graphs lecture notes](https://santoshv.github.io/2023CS4540/Lec8_1011.pdf), isolated-vertex threshold and second-moment proof.
- [MIT Mathematics, Combinatorics course materials](https://ocw.mit.edu/courses/18-314-combinatorial-analysis-fall-2014/), random structures and counting foundations.
