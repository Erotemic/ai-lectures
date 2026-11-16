# 028000 — Discrepancy: Balancing Many Sets at Once

**Track:** Discrete Mathematics. **Background:** set systems, concentration inequalities, randomized algorithms, and combinatorial bounds. **Central question:** can we color elements with plus and minus signs while keeping every relevant subset nearly balanced?

<!-- BEGIN SPOKEN LECTURE -->

# A perfect balance for one set can spoil another

Suppose a warehouse contains many items, and we must assign every item to one of two teams. We would like each team to receive approximately half of every category: heavy items, fragile items, expensive items, and items required for a particular job. An assignment that balances one category may produce a large imbalance in another.

Mathematically, we have a ground set of items and a family of distinguished subsets. We assign each element a sign, plus one or minus one. For each distinguished subset, add the signs of its elements. That signed sum is its imbalance. Discrepancy theory asks us to make the largest absolute imbalance as small as possible.

If there is only one subset containing an even number of elements, we can balance it perfectly by choosing equal numbers of plus and minus signs. But if the family includes many overlapping subsets, their requirements compete. The challenge is simultaneous balance.

# From a set family to a matrix

Write an incidence matrix whose rows correspond to the distinguished subsets and whose columns correspond to elements. Each entry is one when the element belongs to that subset, and zero otherwise. A coloring becomes a vector of plus and minus ones. The row sums of the matrix times that vector are exactly the discrepancies of the sets.

This matrix viewpoint is useful because it connects discrepancy to numerical linear algebra. The goal is to choose a sign vector whose image under the incidence matrix has small maximum absolute coordinate. Unlike least squares, we do not get to choose arbitrary real coefficients: each coordinate must be exactly plus or minus one.

For a path of four items with distinguished subsets consisting of consecutive pairs, alternating signs plus, minus, plus, minus produce discrepancy zero in every pair. But add a different collection of subsets, and a perfect assignment may cease to exist. We need upper bounds that work without discovering an exact zero-discrepancy solution.

# Random signs already give a bound

The first strategy is the same probabilistic idea we used in the earlier combinatorics lectures: assign each element an independent fair sign. For any particular subset containing r items, the expected signed sum is zero. A concentration bound says that large deviations from zero are exponentially unlikely in the square of the threshold divided by r.

If there are m distinguished subsets and each has at most r elements, we can take a union bound over all m possible failures. The probability that any subset has imbalance larger than a certain threshold is at most two m times an exponential term. Choose the threshold slightly larger than the square root of two r times the logarithm of two m. Then the upper bound drops below one.

A probability smaller than one for failure proves that some coloring succeeds. It also gives a useful randomized algorithm when the success probability is sufficiently high, or when a method of conditional expectation can derandomize the bound.

Notice what this result depends on. It grows with the size of the largest set and logarithmically with the number of constrained sets. It does not promise square-root-of-n discrepancy for every possible family of subsets: a family with exponentially many sets can defeat that expectation.

# The family of all subsets shows the limit

Take every subset of an n-element ground set as a constraint. Given any coloring, look at the set of all positively colored elements and the set of all negatively colored elements. One of those two sets has at least half the elements. Its signed sum has magnitude at least n over two.

Because both sets belong to the family, the discrepancy of the complete set system is at least n over two for every coloring. In fact it is exactly the larger of the number of plus and minus signs, so the optimum is the ceiling of n over two.

This example matters because it prevents us from overstating the power of random coloring. A guarantee must depend on structural information about the family. A low number of sets, small membership degrees, geometric structure, or limited combinatorial complexity can all help.

# Partial coloring: do not decide everything at once

A major advance in discrepancy theory is to avoid fixing every sign immediately. A partial coloring assigns plus or minus one to some elements and leaves others temporarily uncolored. We try to color a substantial fraction while keeping each constrained sum under control. Then we repeat on the remaining elements.

Why can this help? A fully colored sign vector lives at a vertex of a high-dimensional cube. A partial coloring can be found by moving through the cube while satisfying or approximately satisfying many linear constraints. Each round decreases the number of undecided coordinates. If the imbalance added at successive rounds is controlled, the total imbalance remains small.

This is the central strategy behind powerful partial-coloring theorems. Their proofs require more than the elementary union bound: dimension counting, entropy arguments, or randomized walks can locate colorings with many coordinates fixed and all constraints reasonably balanced.

A famous result says that when the number of sets is comparable to the number of elements, the discrepancy can be bounded on the order of the square root of the number of elements, with a universal constant. This is stronger than a direct union bound in that regime. But there are important hypotheses on the family size, and the proof is not simply 'color randomly and hope.'

# Membership degree and geometry

Another structural parameter is how many sets contain a single element. If each element appears in at most t distinguished subsets, one can obtain a discrepancy bound linear in t. This is the setting of the Beck–Fiala theorem. A dense family can have many sets, yet remain easy to balance when each element affects only a few constraints.

Geometric set systems offer a different form of structure. Intervals, rectangles, halfspaces, and other ranges have controlled pattern complexity, often described using VC dimension. But VC dimension and discrepancy are not the same invariant. Low VC dimension may support refined bounds under additional conditions; it does not imply a single universal discrepancy formula.

The broader idea is that constrained choices can become easier when we exploit how constraints overlap. Randomization gives a baseline. Partial coloring and geometric or algebraic structure improve the bound. For optimization, resource allocation, and computational geometry, the problem is not merely to split objects into two groups; it is to split them while respecting many measurements simultaneously.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For set system `F subseteq P([n])` and a coloring `chi:[n]->{-1,+1}`, define
\[
\operatorname{disc}(\chi,\mathcal F)
=\max_{S\in\mathcal F}\left|\sum_{i\in S}\chi_i\right|,\qquad
\operatorname{disc}(\mathcal F)=\min_\chi\operatorname{disc}(\chi,\mathcal F).
\]
If A is the `m x n` incidence matrix, this is `min_{chi in {-1,+1}^n} ||A chi||_infinity`.

With independent Rademacher `chi_i`, Hoeffding's inequality gives for any set of size at most r:
\[
\Pr\left(\left|\sum_{i\in S}\chi_i\right|\ge t\right)
\le 2\exp\left(-\frac{t^2}{2|S|}\right)
\le 2\exp\left(-\frac{t^2}{2r}\right).
\]
Thus by a union bound `P(max_S |sum|>=t)<=2m exp(-t^2/(2r))`. Taking **strictly** `t>sqrt(2r log(2m))` proves the existence of a coloring with `max_S |sum|<t` (with the boundary interpreted appropriately for integer sums).

For the full power set `F=P([n])`, any coloring has `max_S |sum|=max(n_+,n_-)`. Therefore `disc(F)=ceil(n/2)`; this prevents a uniform `O(sqrt n)` bound over all families.

Classical stronger results include the Beck–Fiala bound `disc(F)<=2t-1` when every ground element lies in at most t sets (for positive integer t), and Spencer-type `O(sqrt n)` bounds for families with m on the order of n. These theorems require their respective hypotheses; the elementary random-sign proof above does not establish them.

### Exercises with answers

1. A set system has 16 sets of size at most 9. Give a sufficient threshold from the union bound. **Answer:** any `t>sqrt(18 log 32)` is sufficient for existence.
2. Why does the complete power set require discrepancy at least `ceil(n/2)`? **Answer:** one of the positive and negative sign classes has at least that many elements and is a member of the family.
3. What does a partial coloring leave undecided? **Answer:** some coordinates retain value zero until later rounds.
4. Is low VC dimension identical to a bounded discrepancy guarantee? **Answer:** no; the two parameters measure different properties and additional assumptions enter specific bounds.

### Reading and source notes

- [Chazelle, The Discrepancy Method](https://www.cs.princeton.edu/~chazelle/pubs/book.pdf), elementary, geometric and partial-coloring methods.
- [Lovett and Meka, Constructive Discrepancy Minimization by Walking on the Edges](https://arxiv.org/abs/1203.5747), randomized constructive partial-coloring methods.
- [Matoušek, Geometric Discrepancy](https://doi.org/10.1007/978-3-642-03942-3), geometric set systems and discrepancy bounds.
