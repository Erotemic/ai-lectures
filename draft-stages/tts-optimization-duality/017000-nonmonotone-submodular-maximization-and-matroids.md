# 017000 — Nonmonotone Submodular Optimization: When More Can Be Worse

**Track:** Optimization and Duality. **Background:** matroids, submodularity, greedy approximation, randomized rounding. **Central question:** how should we optimize diminishing-returns objectives when adding another element can reduce the total value?

<!-- BEGIN SPOKEN LECTURE -->

# Diminishing returns does not mean every addition helps

A submodular function assigns a value to each subset of a finite ground set. Its defining property is diminishing marginal returns: an element added to a larger set gives no greater incremental benefit than the same element added to a smaller one.

Many useful examples are monotone: adding an item never reduces the value. Coverage is a familiar case. If selecting a sensor covers new territory, the additional coverage generally shrinks as more sensors are installed, but it does not become negative.

Not every submodular function is monotone. A cut function in a graph is a central counterexample. Given a set of vertices, its value is the total weight of edges with exactly one endpoint in the set. Adding a vertex may create new crossing edges, but it may also remove edges that used to cross. The total cut value can decrease.

Now suppose we can select only sets that are independent in a matroid. The matroid might represent a cardinality limit, one option from each category, or linear independence of chosen vectors. We want a large objective value, but we must obey an exchange-based feasibility system and cannot assume every addition helps.

## The smallest counterexample to filling the budget

Take a graph with two vertices connected by one edge of weight one. The cut value of either singleton is one. The cut value of the empty set is zero, and the cut value of the full two-vertex set is also zero.

If our matroid allows up to two vertices, a naive instruction to keep adding until the budget is full produces value zero. The optimal choice is either singleton, with value one. More was worse.

This example rules out a tempting extension of monotone greedy analysis. In the monotone case, once we have chosen a set, adding another feasible element never hurts. For a nonmonotone objective, deciding whether to add an element is itself part of the optimization problem. The algorithm must account for the possibility of negative marginal gain.

## What submodularity still gives us

Diminishing returns survives even when monotonicity fails. For sets A contained in B and an element e outside B, the marginal gain of e on A is at least its marginal gain on B. This can be expressed as a four-set inequality involving the union and intersection of any two sets.

Submodularity also provides subadditivity when the function is normalized and nonnegative. In particular, the value of a chosen set cannot exceed the sum of the values of its singleton members. If an optimal feasible set has at most r elements, at least one of those singletons has value at least the optimum divided by r.

That gives a simple approximation guarantee: choose the best feasible singleton, or the empty set if necessary. It is a weak guarantee when r is large, but it is a valid bound with a transparent proof. More sophisticated algorithms aim for ratios bounded away from zero as r grows.

## Why matroids change the algorithm

For unconstrained nonnegative submodular maximization, a randomized double-greedy algorithm achieves an expected one-half approximation. It starts with a lower set containing nothing and an upper set containing everything. For each element, it compares the marginal effects of adding it to the lower set and removing it from the upper set, and randomizes between those choices. At the end the lower and upper sets agree.

The guarantee is a theorem about the unconstrained problem. We cannot simply add a matroid restriction and claim the same algorithm still works. The upper set may not be independent, and an addition to the lower set may violate the matroid constraint. The family of feasible sets introduces geometric structure that the unconstrained process does not respect.

For a single matroid, continuous relaxations and randomized algorithms can achieve constant-factor approximations under the standard assumptions that the function is nonnegative and submodular and that value and independence queries are available. The precise ratio depends on the algorithm and model. It should never be copied from the monotone case without checking the hypotheses.

## The multilinear extension

To connect discrete sets to continuous optimization, assign each element a fractional coordinate between zero and one. Interpret that coordinate as the probability of independently including the element. The multilinear extension F of the set function is the expected value of a randomly sampled set under those independent choices.

For a submodular function, mixed second derivatives of F are nonpositive. This is a continuous version of diminishing returns. But F need not be concave, and when the original function is nonmonotone, increasing a coordinate may decrease F.

The matroid polytope is the convex hull of characteristic vectors of independent sets. Optimizing F over this polytope is a structured continuous problem. A rounding procedure must then turn a fractional point into an independent set while preserving enough expected objective value. Some methods use swaps or contention resolution. Others use randomized greedy steps tailored directly to the matroid.

A crucial distinction remains: the value of F at a fractional point is an expectation under independent inclusion, and independent inclusion does not necessarily satisfy the matroid constraints. A feasible rounding theorem is what connects the relaxation to the discrete answer.

## How to assess a claimed guarantee

For a proposed algorithm, ask whether the objective is monotone or nonmonotone, normalized or merely nonnegative, and whether negative values are allowed. Ask what matroid or collection of matroids constrains the solution. Ask whether the guarantee is deterministic or in expectation, and how many value and independence-oracle calls the method uses.

Finally, distinguish an approximation certificate from an optimality certificate. Producing a nonmonotone submodular solution of high value is useful. Proving that it is within a factor of the unknown optimum requires a correct theorem with the right assumptions. Proving exact optimality is a different and generally harder task.

The two-vertex cut example captures the problem's central tension. Diminishing returns allows powerful structural arguments, but without monotonicity we cannot assume that selecting more will help. Good algorithms must choose what to include and what deliberately to leave out, while respecting the exchange constraints of the matroid.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Submodularity can be stated as `f(A)+f(B) >= f(A union B)+f(A cap B)`, equivalently `Delta_e f(A)>=Delta_e f(B)` whenever `A subset B` and `e notin B`. A cut function of an undirected nonnegatively weighted graph is nonnegative and submodular, but not monotone. On the graph of one unit-weight edge `ab`, `f({a})=f({b})=1`, `f(empty)=f({a,b})=0`.

If `f(empty)=0` and f is submodular, repeated diminishing returns gives `f(S)<=sum_{e in S} f({e})`. For any matroid whose rank is at most r, the best feasible singleton has value at least `OPT/r`, assuming `OPT>0`, `r>=1` and the elements of an optimal independent set are nonloops. This is a valid but weak bound; it does not imply a constant factor independent of r.

For a set function f, the multilinear extension is
\[
F(x)=\sum_{S\subseteq E} f(S)\prod_{e\in S}x_e\prod_{e\notin S}(1-x_e)=\mathbb E[f(R_x)].
\]
For submodular f, `partial_{ij}^2 F <=0` for distinct i,j; no general concavity of F follows. The independent-set polytope of a matroid M is `P(M)=conv{1_I:I independent}`. An independent Bernoulli draw from x in P(M) need not itself be independent, so rounding is an additional mathematical obligation.

For unconstrained **nonnegative** submodular maximization, randomized double greedy has an expected `1/2` approximation (Buchbinder–Feldman–Naor–Schwartz). Do not apply that ratio unchanged to a general matroid constraint. Constant-factor matroid algorithms require different techniques; see the cited work of Lee–Mirrokni–Nagarajan–Sviridenko and later improvements.

### Exercises with answers

1. Why is the one-edge cut function nonmonotone? **Answer:** adding the second vertex to a singleton reduces the value from one to zero.
2. What bound follows from selecting the best singleton of a rank-r matroid for normalized submodular f? **Answer:** at least `OPT/r`, under the stated assumptions.
3. Is a multilinear extension necessarily concave? **Answer:** no; submodularity controls mixed partial derivatives, not full Hessian negative semidefiniteness.
4. Why does independent Bernoulli rounding fail to automatically respect a matroid? **Answer:** the randomly selected set can violate independence even if its marginal vector lies in the matroid polytope.

### Reading and source notes

- [Buchbinder, Feldman, Naor, and Schwartz, A Tight Linear Time (1/2)-Approximation for Unconstrained Submodular Maximization](https://doi.org/10.1137/130929205), the unconstrained double-greedy guarantee.
- [Lee, Mirrokni, Nagarajan, and Sviridenko, Maximizing Nonmonotone Submodular Functions under Matroid or Knapsack Constraints](https://doi.org/10.1137/090750020), constant-factor algorithms under combinatorial constraints.
- [Chen, Nath, Peng, and Kuhnle, Discretely Beyond 1/e](https://arxiv.org/abs/2405.05202), later combinatorial improvements for constrained nonmonotone maximization.
