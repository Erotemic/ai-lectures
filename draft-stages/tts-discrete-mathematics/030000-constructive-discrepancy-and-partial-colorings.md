# 030000 — Constructive Discrepancy: From Random Signs to Partial Coloring

**Track:** Discrete Mathematics. **Background:** probability inequalities, finite set systems, and linear algebra. **Central question:** how can we actually find a red-blue coloring whose imbalance is provably small across many overlapping sets?

<!-- BEGIN SPOKEN LECTURE -->

# Red and blue under conflicting demands

Suppose we have a collection of objects, and several different groups of objects that we care about. We must color every object red or blue. For each group, we count red as plus one and blue as minus one, and measure the absolute value of the sum. That number is the imbalance, or discrepancy, of the group.

If every group could be handled independently, we would just split each as evenly as possible. But the groups overlap. A color choice that balances one group may unbalance another. Discrepancy theory studies how much simultaneous imbalance is unavoidable, and how good a coloring we can construct.

There is a difference between proving that a coloring exists and finding one efficiently. The two tasks can use different mathematical ideas. Random signs give a simple existence argument; conditional expectation can turn that argument into a deterministic algorithm. More powerful bounds need more delicate algorithms, such as semidefinite rounding or constrained random walks.

# Start with four objects

Number four objects from one through four. Consider the sets consisting of the first two objects, the middle two, and the last two. Color them plus, minus, plus, minus. Each of the three sets has sum zero.

This shows perfect balancing is possible for this particular family. But if we also include every singleton set, no coloring can have discrepancy zero, because every singleton contains exactly one sign. Its absolute sum is one. The attainable discrepancy is controlled by the incidence structure, not just by our skill in choosing colors.

Represent a set system by a matrix with one row per set and one column per object. Put a one wherever an object belongs to a set and a zero elsewhere. A coloring is a vector of signs. Its discrepancies are the absolute values of the entries of the matrix times that sign vector.

The matrix viewpoint exposes the connection to rounding and optimization: we are trying to choose a vertex of the hypercube, with entries plus or minus one, while keeping many linear forms small.

# Random signs and a union bound

Give every object an independent random sign. For any fixed set, the expected sum is zero. If the set contains s elements, its sum is a collection of s independent centered signs. Hoeffding's inequality says the chance that its absolute sum exceeds t is at most two times the exponential of minus t squared divided by twice s.

If every set has size at most n and there are m sets, the probability that any set exceeds t is bounded by two m times the exponential of minus t squared divided by twice n. Choose t proportional to the square root of n times the logarithm of m. This makes the probability of failure smaller than one.

We have now proved that some coloring exists with discrepancy at most that threshold. But the proof as stated is existential. We could keep sampling colorings until one works, but that introduces randomness into our procedure and may not be the most efficient strategy.

# Making the random proof constructive

A standard derandomization technique is conditional expectation. Instead of assigning every sign at once, we choose signs one at a time. At each step, choose a sign so that the conditional expected value of a suitable potential does not increase.

A useful potential is the sum, over all rows, of two exponentials: one exponential of the positive weighted row sum, and the other of its negative. These exponentials penalize large absolute values. Initially, under random signs, their expectation can be bounded using a hyperbolic-cosine estimate. Once we choose a sign, we recompute the two possible conditional expectations and take the smaller one.

One of the two choices must have conditional expectation no larger than the current expectation, because the current value is their average. Repeating this yields a fully specified sign vector whose exponential potential is no larger than the initial bound. A large discrepancy would force one exponential term above that bound, so it cannot occur.

This method produces the same logarithmic style of discrepancy bound as the elementary random-sign argument. It is not yet the stronger bound that says, roughly, that n sets on n objects can all be balanced with discrepancy on the order of the square root of n.

# Why partial coloring is stronger

The remarkable idea behind the stronger bound is to avoid forcing every variable to a sign immediately. Start with entries allowed to vary continuously between minus one and plus one. Keep the important linear constraints under control while moving until a substantial fraction of the variables reach the boundary. Those variables are now permanently colored.

We call this a partial coloring. The uncolored variables remain available for another round. If the number of uncolored variables decreases geometrically, we can attempt to sum the discrepancy introduced in each round. Strong theorems show that, under the appropriate relation between the number of sets and objects, the total is much smaller than the naive random-sign union-bound estimate.

The proof and algorithm must control many correlated constraints at once. This is where the geometry of high-dimensional convex sets and random walks becomes useful. An algorithm can move within the face of a cube while respecting nearly tight constraints. At each stage enough coordinates reach their extreme values, and the process eventually produces a full coloring.

# Constructive does not mean effortless

Spencer's six-standard-deviations theorem gives a discrepancy bound of order square root n for n sets on n elements. The original theorem did not itself provide the later efficient algorithms that achieve comparable bounds. Algorithmic developments by Bansal, and then by Lovett and Meka, supplied constructive methods based on semidefinite programming or a carefully restricted random walk.

It is important not to claim that the simple conditional-expectation potential automatically proves Spencer's sharper result. It proves a weaker, logarithmic bound. The stronger bound uses genuinely different ideas to exploit the simultaneous structure of the constraints.

# Choosing the tool for the guarantee

We can now distinguish three levels of result. Independent random signs show that good balance is possible. Conditional expectation gives an explicit deterministic construction for the elementary bound. Partial-coloring algorithms reach stronger guarantees for important families, but with additional analysis and algorithmic machinery.

The matrix description makes all three levels comparable. The objects are columns, the demands are rows, and the signs are discrete decisions. Discrepancy measures how well the rounding preserves many linear constraints at once. This is why the subject appears in sampling, computational geometry, approximation algorithms, and numerical rounding.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let A be the m-by-n incidence matrix of a set system. For sign vector `x in {-1,+1}^n`, discrepancy is `disc(A,x)=||Ax||_infty` and `disc(A)=min_x disc(A,x)`.

If X_j are independent Rademacher signs and row i has s_i nonzero incidence entries, Hoeffding yields
\[
\Pr\left(\left|\sum_j A_{ij}X_j\right|\ge t\right)
\le 2\exp(-t^2/(2s_i))\le2\exp(-t^2/(2n)).
\]
Hence `P(||AX||_infty >= t) <= 2m exp(-t^2/(2n))`. Taking `t=sqrt(2n log(4m))` makes this at most 1/2.

**Constructive exponential potential.** Define `Phi(x)=sum_i (exp(lambda (Ax)_i)+exp(-lambda (Ax)_i))`. Before signs are fixed,
\[
\mathbb E\Phi(X)=2\sum_i\prod_{j:A_{ij}=1}\cosh\lambda
\le 2m\exp(n\lambda^2/2).
\]
Set `lambda=sqrt(2log(4m)/n)` and `t=n lambda`. The initial expectation is at most `8m^2`, whereas a row discrepancy >= t implies `Phi >= exp(lambda t)=16m^2`. Fix signs sequentially so the conditional expectation never increases. This yields a deterministic coloring with `||Ax||_infty < t` (up to harmless boundary convention), assuming exact arithmetic in the idealized procedure.

The elementary bound is `O(sqrt(n log m))`; it is **not** Spencer's `O(sqrt n)` bound for m=n. Spencer's bound is existential, and constructive sharp-order methods are due to later work, including Bansal and Lovett–Meka.

### Exercises with answers

1. For the set family `{1,2}`, `{2,3}`, `{3,4}`, show that `(1,-1,1,-1)` has discrepancy zero. **Answer:** each two-element sum is zero.
2. If singleton sets are included, can total discrepancy be zero? **Answer:** no; every singleton has absolute sum one.
3. Why does conditional expectation always offer a non-increasing choice for the next sign? **Answer:** the old conditional expectation is the mean of the two possible next conditional expectations.
4. Does Hoeffding plus a union bound alone prove Spencer's `O(sqrt n)` theorem for m=n? **Answer:** no; it yields an additional `sqrt(log n)` factor.

### Reading and source notes

- [Lovett and Meka, Constructive Discrepancy Minimization by Walking on the Edges](https://doi.org/10.1137/130929400), a constructive partial-coloring method.
- [UC San Diego seminar summary of Spencer, Bansal and Lovett–Meka](https://www.math.ucsd.edu/seminar/constructive-discrepancy-minimization-walking-edges), attribution and comparison of existential and algorithmic results.
- [MIT OCW Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/), concentration and conditional expectation background.
