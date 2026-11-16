# 013000 — Submodular Optimization: Why Greedy Choices Can Be Provably Good

**Track:** Optimization, Convexity, and Duality. **Background:** set functions, matroids, LP relaxations, approximation algorithms. **Central question:** how much can we guarantee by repeatedly taking the best remaining marginal improvement?

<!-- BEGIN SPOKEN LECTURE -->

# Submodular Optimization: Why Greedy Choices Can Be Provably Good

Imagine choosing a small set of sensors to observe a large region. The first sensor may reveal an enormous amount. A second sensor placed nearby may add little because its coverage overlaps the first. A sensor placed far away may reveal new territory. This is a diminishing-returns problem: the value of an additional choice depends on what we have already selected.

The mathematical abstraction is a submodular set function. It assigns a value to each subset of a finite ground set. Submodularity says that adding an element to a smaller set cannot be less beneficial than adding it to a larger set, provided that element is not already present. It is the set-function analogue of diminishing marginal returns.

## Coverage is the basic example

Suppose each possible sensor covers a subset of locations. The value of a chosen sensor set is the number, or total weight, of locations covered by at least one selected sensor. This function is normalized because an empty choice covers nothing. It is monotone because adding sensors cannot reduce coverage. And it is submodular because once some locations have been covered, later sensors can gain credit only for previously unseen locations.

This is not merely a verbal observation. If A is contained in B, then the locations newly covered by adding sensor x to B form a subset of those newly covered by adding x to A. Therefore the marginal contribution of x can only decrease as the selected set grows.

The same pattern appears in facility placement, document summarization, experimental design under suitable objectives, and information gathering. The value need not literally count locations, but the mathematical diminishing-returns inequality is the common structure.

## A greedy algorithm with a numerical guarantee

Suppose we may select at most k sensors. Greedy begins with the empty set. At each step it adds the available sensor giving the largest increase in value. There is no backtracking. It is appealing because each step seems locally sensible, but a locally sensible rule can be arbitrarily bad in many optimization problems.

For nonnegative, normalized, monotone submodular functions under a cardinality budget, however, a remarkable theorem gives a guarantee. Greedy achieves at least one minus the exponential of negative one, approximately sixty-three percent, of the optimum. More precisely, after k steps its ratio is at least one minus the kth power of one minus one over k.

The proof does not require guessing the optimal set. Let the current greedy value be some amount below optimum. Consider all the elements in an optimal size-k solution that have not yet been chosen. By monotonicity and submodularity, their combined possible improvement is at least the remaining gap to optimum, but no greater than the sum of their individual marginal gains at the current set. There are at most k of them.

Therefore at least one of those candidates has a marginal gain at least one kth of the current gap. Greedy chooses the best remaining element, so its gain is at least that large. After one step, the gap shrinks by a factor no worse than one minus one over k. After k steps, the gap is at most that factor raised to the kth power times the initial optimum. Rearranging gives the guarantee.

This proof is one of the cleanest examples of a global approximation theorem derived from a local rule. The guarantee comes from the shape of the objective, not from a fortunate accident on a particular data set.

## The conditions must not disappear

It is easy to misstate this theorem. Submodularity alone is not sufficient for that greedy guarantee. We also used monotonicity, normalization, and a cardinality constraint. Without monotonicity, an added item can decrease value. For example, the number of edges crossing a cut of a graph is a submodular set function, but adding a vertex can remove as well as create crossing edges.

Constraints matter as well. If the feasible subsets are the independent sets of a matroid, a basic greedy rule has a different general guarantee for monotone submodular maximization: one half, not automatically one minus one over e. More advanced algorithms, such as continuous-greedy methods with suitable rounding, can recover stronger guarantees under matroid constraints. The distinction is not a technical footnote: it tells us exactly which proof we are allowed to apply.

Nor does a constant-factor guarantee mean the obtained solution is globally optimal. A greedy answer can miss a combination whose early components look less impressive individually but collectively give the best result. The theorem quantifies how much loss can occur under the stated assumptions.

## Submodularity also helps minimization

A set function is submodular if for any two sets, the sum of their separate values is at least the sum of the values of their union and intersection. This is equivalent to diminishing returns on a finite ground set.

There is a deep connection to convex analysis. Every set function has an associated Lovasz extension to real vectors on the unit cube, built by sorting the vector's coordinates and interpolating between values on nested sets. The Lovasz extension is convex exactly when the original set function is submodular.

That equivalence gives a bridge from discrete optimization to continuous convex optimization. Unconstrained submodular function minimization can be performed in polynomial time using a value oracle model and suitable algorithms. General submodular maximization is a different matter: it can be computationally difficult, and approximation guarantees depend strongly on monotonicity and constraints.

It is tempting to reason that because the Lovasz extension is convex, maximizing a submodular function should be easy too. But convexity helps minimization. Maximizing a convex function over a convex domain is generally not a tractable convex-optimization problem. Direction matters.

## An example with overlapping sets

Take four locations in a row. Sensor A sees the first two, sensor B sees the middle two, and sensor C sees the last two. We may select two sensors. Choosing A and C covers all four locations. A greedy implementation can find this optimum if it chooses A or C first. But if ties are resolved by picking B first, the second sensor adds only one new location, and greedy covers three.

The example is small enough to inspect directly. Every first sensor seems equally valuable by itself, yet their overlap patterns differ. Greedy's theoretical guarantee accommodates this tie dependence. It never promises that a careless tie-break yields the optimum; it promises a rigorous lower bound across all greedy choices satisfying its rule.

## When the approximation result is the right tool

The practical value of a theorem is not only its percentage. It tells us which problem assumptions are worth checking before committing to an algorithm. Do marginal gains really decrease? Is the objective guaranteed monotone? Are we choosing at most k items, or are there matroid or knapsack constraints? Can we evaluate the marginal gain accurately, or only estimate it with noise?

When these questions are answered, a greedy algorithm can provide a transparent tradeoff between speed and provable quality. When they are not, the same simple algorithm is only a heuristic. Submodular optimization is powerful precisely because it turns that distinction into mathematics: a local rule receives a global guarantee only after the structure that justifies it has been established.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A set function \(f:2^V\to\mathbb R\) is **submodular** if
\[f(A)+f(B)\ge f(A\cup B)+f(A\cap B).\]
Equivalently, for \(A\subseteq B\subseteq V\), \(x\notin B\), its marginal gains satisfy \(f(A\cup\{x\})-f(A)\ge f(B\cup\{x\})-f(B)\). It is **monotone** if \(A\subseteq B\Rightarrow f(A)\le f(B)\), and **normalized** if \(f(\varnothing)=0\).

**Cardinality-k greedy theorem (Nemhauser–Wolsey–Fisher):** if f is nonnegative, monotone, normalized, and submodular, greedy chooses a new element with maximum marginal gain at each of k steps (or until all V is selected). If O is optimal with \(|O|\le k\), and \(S_i\) is the greedy set after i steps, then
\[f(O)-f(S_{i+1})\le\left(1-\frac1k\right)(f(O)-f(S_i)),\]
so
\[f(S_k)\ge \left[1-\left(1-\frac1k\right)^k\right]f(O)\ge(1-1/e)f(O).\]
For graph cuts, \(f(S)=|\delta(S)|\) is submodular but not monotone. The general matroid-constraint guarantee for plain greedy monotone submodular maximization is \(1/2\), not automatically \(1-1/e\).

**Lovasz extension:** for a set function f with \(f(\emptyset)=0\), sort coordinates \(x_{\pi(1)}\ge\cdots\ge x_{\pi(n)}\), and set \(S_i=\{\pi(1),\ldots,\pi(i)\}\). The Lovasz extension can be expressed as
\[\widehat f(x)=\sum_{i=1}^n x_{\pi(i)}\bigl(f(S_i)-f(S_{i-1})\bigr).\]
It is convex iff f is submodular. This connects submodular **minimization** to convex analysis, not arbitrary maximization.

### Exercises with answers

1. Why is weighted set coverage submodular for nonnegative weights? **Answer:** the newly covered elements after a larger selected set are a subset of those newly covered after a smaller set.
2. What factor does greedy guarantee under a cardinality budget? **Answer:** \(1-(1-1/k)^k\ge1-1/e\), under normalization, monotonicity and submodularity.
3. Why does the cut-size example invalidate an unrestricted monotone-greedy claim? **Answer:** cut size can decrease when a vertex is added, so the monotonicity hypothesis fails.
4. For the three sensors covering adjacent pairs of four points, what is the optimum with budget two? **Answer:** choose the two end sensors, covering all four points.

### Reading and source notes

- G. L. Nemhauser, L. A. Wolsey, and M. L. Fisher, [*An Analysis of Approximations for Maximizing Submodular Set Functions I*](https://research.dial.uclouvain.be/entities/publication/a725e7a1-a49a-403e-8774-d62d8b8e000a), original approximation analysis (1978).
- G. L. Nemhauser and L. A. Wolsey, [*Best Algorithms for Approximating the Maximum of a Submodular Set Function*](https://pubsonline.informs.org/doi/10.1287/moor.3.3.177), oracle complexity and greedy bounds (1978).
- Francis Bach, [*Learning with Submodular Functions: A Convex Optimization Perspective*](https://arxiv.org/abs/1111.6453), Lovasz extensions and convex analysis.
