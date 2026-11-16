# 021000 — Submodular Maximization Under Intersecting Matroid Constraints

**Track:** Optimization and Duality. **Background:** submodular functions, greedy approximation, matroids, and exchange properties. **Central question:** how do approximation guarantees change when one feasible-set rule is replaced by several simultaneous independence rules?

<!-- BEGIN SPOKEN LECTURE -->

# A single exchange rule is powerful

Suppose we select a subset of possible projects. Their total value increases as projects are added, but each new project may contribute less after others are already present. This diminishing-returns property is called submodularity.

If there were no constraints, a monotone submodular function would be maximized by taking everything. Real selection problems have rules. Perhaps at most one project can be chosen from each team, or selected jobs must fit a schedule, or chosen edges may not form a cycle.

A matroid captures a broad family of constraints in which feasible sets are hereditary and satisfy an exchange property. The exchange property gives greedy algorithms real mathematical strength. Under a single matroid, repeatedly adding the feasible element with the largest current marginal gain gives a one-half approximation for a normalized nonnegative monotone submodular objective.

But many applications impose more than one matroid condition. A project may use one worker and one machine, with each resource allowed only once. Each resource family gives a partition matroid. Feasible selections lie in the intersection of the two matroids. What becomes of the exchange argument when several rules must hold at once?

# A bipartite matching is already an intersection

Consider a bipartite graph with workers on one side and jobs on the other. Choosing a set of edges represents assigning workers to jobs. No worker can receive two assignments, and no job can be assigned twice.

The no-duplicate-worker rule defines one partition matroid on edges. The no-duplicate-job rule defines another. Their intersection is the family of matchings. Thus even the familiar weighted bipartite matching problem is optimization over the intersection of two matroids.

Here is a small example that exposes greedy's weakness. There are two workers and two jobs. One edge joins worker one to job one and has weight one plus a tiny positive epsilon. Another joins worker one to job two and has weight one. A third joins worker two to job one and has weight one. No other edge is available.

Greedy picks the highest-weight edge, the one worth one plus epsilon. That choice blocks both remaining edges because each conflicts with one of its endpoints. Its total value is one plus epsilon. The optimal matching selects the other two edges and has value two.

As epsilon approaches zero, the ratio of greedy value to optimal value approaches one half. This example uses an additive objective, which is a special case of a monotone submodular function. The difficulty is therefore already present before the nonlinear diminishing-returns effect appears.

# Why several matroids permit larger exchanges

Inside one matroid, adding a new element to an independent set requires exchanging at most one suitable existing element in the relevant exchange argument. In an intersection of k matroids, a proposed element may violate a different constraint in each matroid. Restoring feasibility can require removing up to k existing elements.

This leads to the language of k-extendible systems. A feasible system is k-extendible if, when an element can be added to a smaller feasible set, adding it to a larger feasible set containing that smaller one can be repaired by deleting at most k elements from the larger set.

The intersection of k matroids has this property. Apply the matroid exchange rule separately in each constraint. Each rule may identify one blocking element. Taking the union of those deletions removes at most k elements and restores all constraints at once.

The extra deletions are the reason a simple greedy analysis loses a factor with k. Every valuable greedy addition may force us, in an imagined comparison with an optimal solution, to charge against several optimal elements rather than one.

# The diminishing-returns charging argument

Let the objective be normalized, nonnegative, monotone, and submodular. Greedy builds its set by repeatedly choosing the feasible element with maximum marginal gain.

Imagine maintaining a feasible comparison set that initially contains an optimum. At each greedy choice, add that greedy element to the comparison set and remove at most k elements to restore feasibility, using the extendibility property. We keep the greedy prefix inside the modified comparison set.

Because greedy chose the best feasible marginal at that step, the marginal value of each removed optimal element, measured at the appropriate prefix, cannot exceed the marginal of the greedy element. Submodularity ensures that later additions do not become more valuable just because the prefix grows.

After charging every removed element, the optimum's value is at most the greedy value plus k times the total greedy gain. The resulting guarantee is that greedy obtains at least one over k plus one of the optimal value.

For one matroid this gives one half. For two matroids it gives one third. The matching example with a ratio near one half does not show that one third is tight; it simply shows that naive greedy can already be suboptimal in a very small case. Stronger algorithms can improve these ratios under particular constraints or using more elaborate search strategies.

# Not all combinatorial constraints are matroids

A capacity limit on the total weight of chosen projects is a knapsack constraint. It is not automatically a matroid because feasible sets may violate exchange. A graph-matching constraint in a general nonbipartite graph also does not become an intersection of two vertex-side partition matroids, because there is no fixed two-sided vertex partition.

Moreover, maximizing a nonmonotone submodular function is a different problem. Adding a project might reduce the total value. Greedy that always adds the best currently feasible positive marginal may need different analysis or might stop early. Guarantees must not be copied from the monotone setting without checking their hypotheses.

Even within matroids, approximation bounds depend on the algorithmic model. A simple one-pass greedy procedure, a local-search method, and a continuous relaxation followed by rounding have different guarantees and costs. An approximation factor is never a property of the problem class alone; it is a theorem about a specific algorithm under stated assumptions.

# Why multiple constraints matter in practice

In recommendation systems, a set of items may have diminishing informational value while facing separate limits on categories, authors, and placements. In sensor selection, each new measurement helps less when similar sensors are already chosen, while power, location, and communication constraints apply simultaneously. In experiment design, statistical coverage is submodular but staff and instrument assignments can interact.

The correct modelling step is to identify which restrictions really form matroids, how many independently constrain the set, and whether the objective is monotone. Then one can select an algorithm with a credible approximation theorem.

The conceptual transition is simple and important. One matroid offers a one-for-one exchange. Intersecting k matroids may require k-for-one exchange. The greedy approximation factor follows that combinatorial accounting. More sophisticated optimization methods improve on greedy by making larger coordinated changes, but they still have to confront the same exchange structure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `f:2^E -> R_{>=0}` be normalized `f(empty)=0`, monotone and submodular: for `A subseteq B`, `e notin B`, `Delta(e|A)=f(A+e)-f(A)>=Delta(e|B)`. Feasible sets are `F=I_1 intersect ... intersect I_k` for matroid independent-set families I_j. This is a k-extendible system: given `A subseteq B` feasible and `A+e` feasible, separately use each matroid exchange to remove at most one element from `B\A`; their union has size at most k, and `(B\Z)+e` is feasible.

The maximum-marginal greedy algorithm for a normalized nonnegative monotone submodular f on a k-extendible system satisfies
\[
f(S_{\rm greedy})\ge\frac{1}{k+1}\,f(S^*).
\]
An exchange-charging proof maintains a feasible comparison set containing the greedy prefix; at each step, at most k removed comparison elements have marginals bounded by the chosen greedy marginal. Submodularity telescopes the bound `f(S*)<=f(S_greedy)+k sum_i Delta(g_i|S_{i-1})=(k+1)f(S_greedy)`.

**Worked bipartite matching example:** edges `e_11=(u_1,v_1)` weight `1+epsilon`, `e_12=(u_1,v_2)` weight 1, `e_21=(u_2,v_1)` weight 1. With epsilon in (0,1), greedy selects e_11, value `1+epsilon`, while optimum selects `{e_12,e_21}`, value 2. The ratio tends to 1/2. This is a counterexample to greedy optimality, **not** a tight example for the general `1/(k+1)` bound when k=2.

### Exercises with answers

1. How many matroids describe a bipartite matching through left and right degree constraints? **Answer:** two partition matroids.
2. What simple greedy guarantee holds for a monotone submodular objective over the intersection of three matroids? **Answer:** at least `1/(3+1)=1/4` of optimum.
3. Why is a knapsack constraint not automatically a matroid? **Answer:** its weighted feasibility generally fails the matroid exchange axiom.
4. Does the same one-over-k-plus-one statement automatically hold for nonmonotone f? **Answer:** no; monotonicity was used in the charging proof.

### Reading and source notes

- [Feldman and Ward, Submodular Maximization over a Matroid k-Intersection](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.89/LIPIcs.ICALP.2026.89.html), greedy baseline and newer approximation algorithms.
- [Constrained submodular maximization via greedy local search](https://www.sciencedirect.com/science/article/pii/S0167637718300038), multi-constraint local-exchange algorithms.
- [Feldman and Ward, arXiv preprint](https://arxiv.org/abs/2602.08473), formal problem statement and algorithmic improvements.
