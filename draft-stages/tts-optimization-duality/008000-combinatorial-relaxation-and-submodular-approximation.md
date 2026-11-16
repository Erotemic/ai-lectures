# Combinatorial relaxation and submodular approximation

<!-- BEGIN SPOKEN LECTURE -->

# Combinatorial relaxation and submodular approximation

## Discrete Optimization: Relaxations, Integrality Gaps, and Certificates

Many decisions cannot be fractional. We either build a facility or do not. A job is assigned to one worker, not seven tenths of a worker. A vertex of a graph is selected or it is not. These yes-or-no requirements make optimization much more difficult than simply minimizing a smooth function over a convex region.

A useful strategy is to temporarily remove the integrality restriction. Let each binary decision variable take any real value between zero and one. Solve the resulting linear or convex optimization problem. Its solution may not be a valid decision, but it gives a rigorous bound on the best valid decision. This is called a relaxation.

We must be careful about the direction of the bound. For minimization, allowing more candidate solutions can only decrease the optimal value. So the relaxed optimum is a lower bound on the best integer objective. For maximization, allowing more candidates can only increase the optimum, so the relaxed optimum is an upper bound. If we find a valid integer candidate whose objective matches the relaxation bound, we have proved that candidate optimal.

### A triangle with three constraints

Consider a triangle graph with vertices A, B, and C. We want to select as few vertices as possible so that every edge has at least one selected endpoint. This is the minimum vertex-cover problem.

Assign a binary variable to each vertex, one if selected and zero otherwise. For each edge, require the sum of the variables at its endpoints to be at least one. Minimize the sum of all three variables.

An integer solution cannot select only one vertex: that vertex misses the edge between the other two. Selecting any two vertices works, so the integer optimum is two.

Now relax the variables to lie between zero and one. Assign one half to each vertex. Every edge constraint is satisfied because one half plus one half equals one. The total objective is one and one half. In fact this is the best fractional value. Sum the three edge inequalities. Every vertex appears twice, so twice the total sum must be at least three. Therefore the sum is at least one and one half, attained by the half-half-half assignment.

The linear program has proved a lower bound of one and one half, but the actual discrete problem requires two. Their difference is an integrality gap. As a ratio, the integer optimum divided by the relaxed optimum is four thirds for this instance.

This example teaches two things at once. A relaxation can give a sharp bound on the continuous feasible set, complete with a short proof, and still fail to describe the integer feasible set exactly. The distinction is structural, not numerical rounding error.

### When the relaxation is exact

Some discrete problems have linear relaxations whose extreme points are automatically integral. Bipartite vertex cover is one example when written with its standard edge-cover constraints and nonnegative costs: the associated vertex-cover polyhedron has integral extreme points. This is related to the structure behind König's theorem and maximum flow.

Another language for this phenomenon is total unimodularity. If an integer constraint matrix is totally unimodular and the right-hand side is integral, then vertices of the associated polyhedron are integral under the usual full-rank and feasibility qualifications. This can eliminate the need for branching or rounding. Not every graph or combinatorial constraint matrix has that property. The triangle example demonstrates a fractional vertex, so its relaxation is not integral.

For a model builder, the question should not be merely whether an integer program has been written down. Ask whether its linear relaxation has special structure that makes it exact, or almost exact, or whether it can be strengthened by valid inequalities.

### Branch-and-bound turns bounds into a proof

Suppose the linear relaxation has a fractional optimum. Pick a variable that must be integer but currently has a fractional value. In a binary problem, split the search into two subproblems: one fixes the variable to zero and the other fixes it to one. Every valid integer solution belongs to one of these branches.

Solve a relaxation in each branch. Because these are minimization problems, each relaxed optimum gives a lower bound on integer solutions in that branch. Meanwhile, any valid integer solution gives an upper bound on the global optimum. If a branch's lower bound is no better than the current integer solution, we may discard that entire branch: no descendant can improve the incumbent.

Return to the triangle. At the fractional solution, all three variables equal one half. Branch on the variable for A. If A is zero, both B and C must be one to cover the edges incident to A. The objective is at least two. If A is one, the edge between B and C still requires B plus C to be at least one, so the objective is again at least two. A feasible selection of two vertices attains that value. Both branches are resolved; the integer optimum is certified.

A general branch-and-bound algorithm may explore many nodes, sometimes exponentially many. Its advantage is that every pruned subtree has a mathematical justification. A final optimality claim can be supported by a feasible incumbent and bounds covering the remaining alternatives.

### Cuts sharpen the relaxation

Instead of branching immediately, we can add inequalities that every integer solution satisfies but some fractional solutions violate. These are cutting planes. In the triangle problem, add the inequality that the sum of all three vertex variables must be at least two. It is valid for every integer vertex cover, but violated by the all-halves fractional solution. The relaxation becomes tighter without excluding any permissible integer answer.

The key obligation is to prove validity. A cut that removes an inconvenient fractional point but also removes a valid integer optimum is not a legitimate relaxation improvement.

In the triangle, validity follows from a short combinatorial argument: selecting at most one vertex leaves the edge between the other two uncovered. For larger models, inequalities may come from parity, flows, cycles, submodularity, or problem-specific combinatorics.

### Approximation from a fractional solution

Sometimes finding the exact integer optimum is computationally too expensive, but the relaxation can guide a solution with a provable approximation ratio.

For weighted vertex cover with nonnegative vertex costs, solve the linear relaxation. Select every vertex whose fractional value is at least one half. Every edge has endpoint values summing to at least one, so at least one endpoint crosses the threshold. Thus the rounded selection covers all edges.

What does it cost? Every selected vertex has cost at most twice its cost multiplied by its fractional value, because its fractional value is at least one half. Summing over selected vertices, the rounded cost is at most twice the fractional objective over all vertices. And the fractional optimum is at most the integer optimum. Therefore the rounded solution costs at most twice the best possible integer cover.

This is a two-approximation guarantee. It is not a claim that every instance incurs twice the optimum; it is a worst-case upper bound derived from two explicit inequalities. We have used the relaxed solution both as a guide for rounding and as a certificate against which to compare the result.

### What a certificate should contain

For a discrete minimization problem, a useful proof artifact consists of a valid discrete solution, its objective value, and a lower bound established by a relaxation, a dual feasible point, a combinatorial inequality, or a complete branch-and-bound argument. If the lower and upper bounds match, optimality is proved. If they differ, the gap quantifies what has not been established.

The same logic extends to semidefinite relaxations, where a binary vector may be lifted to a positive semidefinite matrix and a difficult rank constraint is dropped. The resulting bound can be stronger than a simple linear relaxation, but the direction of the bound must still be tracked, and converting the matrix back to a valid discrete solution requires a separate argument.

Discrete optimization connects combinatorics to convex analysis precisely because the continuous problem is not the whole problem. Relaxations, integrality results, valid cuts, and rounding methods let us use continuous mathematics without pretending fractional answers are acceptable final decisions.

## Relaxation, submodularity, nonmonotonicity, and matroid constraints

### Submodular Optimization: Why Greedy Choices Can Be Provably Good

Imagine choosing a small set of sensors to observe a large region. The first sensor may reveal an enormous amount. A second sensor placed nearby may add little because its coverage overlaps the first. A sensor placed far away may reveal new territory. This is a diminishing-returns problem: the value of an additional choice depends on what we have already selected.

The mathematical abstraction is a submodular set function. It assigns a value to each subset of a finite ground set. Submodularity says that adding an element to a smaller set cannot be less beneficial than adding it to a larger set, provided that element is not already present. It is the set-function analogue of diminishing marginal returns.

#### Coverage is the basic example

Suppose each possible sensor covers a subset of locations. The value of a chosen sensor set is the number, or total weight, of locations covered by at least one selected sensor. This function is normalized because an empty choice covers nothing. It is monotone because adding sensors cannot reduce coverage. And it is submodular because once some locations have been covered, later sensors can gain credit only for previously unseen locations.

This is not merely a verbal observation. If A is contained in B, then the locations newly covered by adding sensor x to B form a subset of those newly covered by adding x to A. Therefore the marginal contribution of x can only decrease as the selected set grows.

The same pattern appears in facility placement, document summarization, experimental design under suitable objectives, and information gathering. The value need not literally count locations, but the mathematical diminishing-returns inequality is the common structure.

#### A greedy algorithm with a numerical guarantee

Suppose we may select at most k sensors. Greedy begins with the empty set. At each step it adds the available sensor giving the largest increase in value. There is no backtracking. It is appealing because each step seems locally sensible, but a locally sensible rule can be arbitrarily bad in many optimization problems.

For nonnegative, normalized, monotone submodular functions under a cardinality budget, however, a remarkable theorem gives a guarantee. Greedy achieves at least one minus the exponential of negative one, approximately sixty-three percent, of the optimum. More precisely, after k steps its ratio is at least one minus the kth power of one minus one over k.

The proof does not require guessing the optimal set. Let the current greedy value be some amount below optimum. Consider all the elements in an optimal size-k solution that have not yet been chosen. By monotonicity and submodularity, their combined possible improvement is at least the remaining gap to optimum, but no greater than the sum of their individual marginal gains at the current set. There are at most k of them.

Therefore at least one of those candidates has a marginal gain at least one kth of the current gap. Greedy chooses the best remaining element, so its gain is at least that large. After one step, the gap shrinks by a factor no worse than one minus one over k. After k steps, the gap is at most that factor raised to the kth power times the initial optimum. Rearranging gives the guarantee.

This proof is one of the cleanest examples of a global approximation theorem derived from a local rule. The guarantee comes from the shape of the objective, not from a fortunate accident on a particular data set.

#### The conditions must not disappear

It is easy to misstate this theorem. Submodularity alone is not sufficient for that greedy guarantee. We also used monotonicity, normalization, and a cardinality constraint. Without monotonicity, an added item can decrease value. For example, the number of edges crossing a cut of a graph is a submodular set function, but adding a vertex can remove as well as create crossing edges.

Constraints matter as well. If the feasible subsets are the independent sets of a matroid, a basic greedy rule has a different general guarantee for monotone submodular maximization: one half, not automatically one minus one over e. More advanced algorithms, such as continuous-greedy methods with suitable rounding, can recover stronger guarantees under matroid constraints. The distinction is not a technical footnote: it tells us exactly which proof we are allowed to apply.

Nor does a constant-factor guarantee mean the obtained solution is globally optimal. A greedy answer can miss a combination whose early components look less impressive individually but collectively give the best result. The theorem quantifies how much loss can occur under the stated assumptions.

#### Submodularity also helps minimization

A set function is submodular if for any two sets, the sum of their separate values is at least the sum of the values of their union and intersection. This is equivalent to diminishing returns on a finite ground set.

There is a deep connection to convex analysis. Every set function has an associated Lovasz extension to real vectors on the unit cube, built by sorting the vector's coordinates and interpolating between values on nested sets. The Lovasz extension is convex exactly when the original set function is submodular.

That equivalence gives a bridge from discrete optimization to continuous convex optimization. Unconstrained submodular function minimization can be performed in polynomial time using a value oracle model and suitable algorithms. General submodular maximization is a different matter: it can be computationally difficult, and approximation guarantees depend strongly on monotonicity and constraints.

It is tempting to reason that because the Lovasz extension is convex, maximizing a submodular function should be easy too. But convexity helps minimization. Maximizing a convex function over a convex domain is generally not a tractable convex-optimization problem. Direction matters.

#### An example with overlapping sets

Take four locations in a row. Sensor A sees the first two, sensor B sees the middle two, and sensor C sees the last two. We may select two sensors. Choosing A and C covers all four locations. A greedy implementation can find this optimum if it chooses A or C first. But if ties are resolved by picking B first, the second sensor adds only one new location, and greedy covers three.

The example is small enough to inspect directly. Every first sensor seems equally valuable by itself, yet their overlap patterns differ. Greedy's theoretical guarantee accommodates this tie dependence. It never promises that a careless tie-break yields the optimum; it promises a rigorous lower bound across all greedy choices satisfying its rule.

#### When the approximation result is the right tool

The practical value of a theorem is not only its percentage. It tells us which problem assumptions are worth checking before committing to an algorithm. Do marginal gains really decrease? Is the objective guaranteed monotone? Are we choosing at most k items, or are there matroid or knapsack constraints? Can we evaluate the marginal gain accurately, or only estimate it with noise?

When these questions are answered, a greedy algorithm can provide a transparent tradeoff between speed and provable quality. When they are not, the same simple algorithm is only a heuristic. Submodular optimization is powerful precisely because it turns that distinction into mathematics: a local rule receives a global guarantee only after the structure that justifies it has been established.

### Nonmonotone Submodular Optimization: When More Can Be Worse

A submodular function assigns a value to each subset of a finite ground set. Its defining property is diminishing marginal returns: an element added to a larger set gives no greater incremental benefit than the same element added to a smaller one.

Many useful examples are monotone: adding an item never reduces the value. Coverage is a familiar case. If selecting a sensor covers new territory, the additional coverage generally shrinks as more sensors are installed, but it does not become negative.

Not every submodular function is monotone. A cut function in a graph is a central counterexample. Given a set of vertices, its value is the total weight of edges with exactly one endpoint in the set. Adding a vertex may create new crossing edges, but it may also remove edges that used to cross. The total cut value can decrease.

Now suppose we can select only sets that are independent in a matroid. The matroid might represent a cardinality limit, one option from each category, or linear independence of chosen vectors. We want a large objective value, but we must obey an exchange-based feasibility system and cannot assume every addition helps.

#### The smallest counterexample to filling the budget

Take a graph with two vertices connected by one edge of weight one. The cut value of either singleton is one. The cut value of the empty set is zero, and the cut value of the full two-vertex set is also zero.

If our matroid allows up to two vertices, a naive instruction to keep adding until the budget is full produces value zero. The optimal choice is either singleton, with value one. More was worse.

This example rules out a tempting extension of monotone greedy analysis. In the monotone case, once we have chosen a set, adding another feasible element never hurts. For a nonmonotone objective, deciding whether to add an element is itself part of the optimization problem. The algorithm must account for the possibility of negative marginal gain.

#### What submodularity still gives us

Diminishing returns survives even when monotonicity fails. For sets A contained in B and an element e outside B, the marginal gain of e on A is at least its marginal gain on B. This can be expressed as a four-set inequality involving the union and intersection of any two sets.

Submodularity also provides subadditivity when the function is normalized and nonnegative. In particular, the value of a chosen set cannot exceed the sum of the values of its singleton members. If an optimal feasible set has at most r elements, at least one of those singletons has value at least the optimum divided by r.

That gives a simple approximation guarantee: choose the best feasible singleton, or the empty set if necessary. It is a weak guarantee when r is large, but it is a valid bound with a transparent proof. More sophisticated algorithms aim for ratios bounded away from zero as r grows.

#### Why matroids change the algorithm

For unconstrained nonnegative submodular maximization, a randomized double-greedy algorithm achieves an expected one-half approximation. It starts with a lower set containing nothing and an upper set containing everything. For each element, it compares the marginal effects of adding it to the lower set and removing it from the upper set, and randomizes between those choices. At the end the lower and upper sets agree.

The guarantee is a theorem about the unconstrained problem. We cannot simply add a matroid restriction and claim the same algorithm still works. The upper set may not be independent, and an addition to the lower set may violate the matroid constraint. The family of feasible sets introduces geometric structure that the unconstrained process does not respect.

For a single matroid, continuous relaxations and randomized algorithms can achieve constant-factor approximations under the standard assumptions that the function is nonnegative and submodular and that value and independence queries are available. The precise ratio depends on the algorithm and model. It should never be copied from the monotone case without checking the hypotheses.

#### The multilinear extension

To connect discrete sets to continuous optimization, assign each element a fractional coordinate between zero and one. Interpret that coordinate as the probability of independently including the element. The multilinear extension F of the set function is the expected value of a randomly sampled set under those independent choices.

For a submodular function, mixed second derivatives of F are nonpositive. This is a continuous version of diminishing returns. But F need not be concave, and when the original function is nonmonotone, increasing a coordinate may decrease F.

The matroid polytope is the convex hull of characteristic vectors of independent sets. Optimizing F over this polytope is a structured continuous problem. A rounding procedure must then turn a fractional point into an independent set while preserving enough expected objective value. Some methods use swaps or contention resolution. Others use randomized greedy steps tailored directly to the matroid.

A crucial distinction remains: the value of F at a fractional point is an expectation under independent inclusion, and independent inclusion does not necessarily satisfy the matroid constraints. A feasible rounding theorem is what connects the relaxation to the discrete answer.

#### How to assess a claimed guarantee

For a proposed algorithm, ask whether the objective is monotone or nonmonotone, normalized or merely nonnegative, and whether negative values are allowed. Ask what matroid or collection of matroids constrains the solution. Ask whether the guarantee is deterministic or in expectation, and how many value and independence-oracle calls the method uses.

Finally, distinguish an approximation certificate from an optimality certificate. Producing a nonmonotone submodular solution of high value is useful. Proving that it is within a factor of the unknown optimum requires a correct theorem with the right assumptions. Proving exact optimality is a different and generally harder task.

The two-vertex cut example captures the problem's central tension. Diminishing returns allows powerful structural arguments, but without monotonicity we cannot assume that selecting more will help. Good algorithms must choose what to include and what deliberately to leave out, while respecting the exchange constraints of the matroid.

### Submodular Maximization Under Intersecting Matroid Constraints

Suppose we select a subset of possible projects. Their total value increases as projects are added, but each new project may contribute less after others are already present. This diminishing-returns property is called submodularity.

If there were no constraints, a monotone submodular function would be maximized by taking everything. Real selection problems have rules. Perhaps at most one project can be chosen from each team, or selected jobs must fit a schedule, or chosen edges may not form a cycle.

A matroid captures a broad family of constraints in which feasible sets are hereditary and satisfy an exchange property. The exchange property gives greedy algorithms real mathematical strength. Under a single matroid, repeatedly adding the feasible element with the largest current marginal gain gives a one-half approximation for a normalized nonnegative monotone submodular objective.

But many applications impose more than one matroid condition. A project may use one worker and one machine, with each resource allowed only once. Each resource family gives a partition matroid. Feasible selections lie in the intersection of the two matroids. What becomes of the exchange argument when several rules must hold at once?

### A bipartite matching is already an intersection

Consider a bipartite graph with workers on one side and jobs on the other. Choosing a set of edges represents assigning workers to jobs. No worker can receive two assignments, and no job can be assigned twice.

The no-duplicate-worker rule defines one partition matroid on edges. The no-duplicate-job rule defines another. Their intersection is the family of matchings. Thus even the familiar weighted bipartite matching problem is optimization over the intersection of two matroids.

Here is a small example that exposes greedy's weakness. There are two workers and two jobs. One edge joins worker one to job one and has weight one plus a tiny positive epsilon. Another joins worker one to job two and has weight one. A third joins worker two to job one and has weight one. No other edge is available.

Greedy picks the highest-weight edge, the one worth one plus epsilon. That choice blocks both remaining edges because each conflicts with one of its endpoints. Its total value is one plus epsilon. The optimal matching selects the other two edges and has value two.

As epsilon approaches zero, the ratio of greedy value to optimal value approaches one half. This example uses an additive objective, which is a special case of a monotone submodular function. The difficulty is therefore already present before the nonlinear diminishing-returns effect appears.

### Why several matroids permit larger exchanges

Inside one matroid, adding a new element to an independent set requires exchanging at most one suitable existing element in the relevant exchange argument. In an intersection of k matroids, a proposed element may violate a different constraint in each matroid. Restoring feasibility can require removing up to k existing elements.

This leads to the language of k-extendible systems. A feasible system is k-extendible if, when an element can be added to a smaller feasible set, adding it to a larger feasible set containing that smaller one can be repaired by deleting at most k elements from the larger set.

The intersection of k matroids has this property. Apply the matroid exchange rule separately in each constraint. Each rule may identify one blocking element. Taking the union of those deletions removes at most k elements and restores all constraints at once.

The extra deletions are the reason a simple greedy analysis loses a factor with k. Every valuable greedy addition may force us, in an imagined comparison with an optimal solution, to charge against several optimal elements rather than one.

### The diminishing-returns charging argument

Let the objective be normalized, nonnegative, monotone, and submodular. Greedy builds its set by repeatedly choosing the feasible element with maximum marginal gain.

Imagine maintaining a feasible comparison set that initially contains an optimum. At each greedy choice, add that greedy element to the comparison set and remove at most k elements to restore feasibility, using the extendibility property. We keep the greedy prefix inside the modified comparison set.

Because greedy chose the best feasible marginal at that step, the marginal value of each removed optimal element, measured at the appropriate prefix, cannot exceed the marginal of the greedy element. Submodularity ensures that later additions do not become more valuable just because the prefix grows.

After charging every removed element, the optimum's value is at most the greedy value plus k times the total greedy gain. The resulting guarantee is that greedy obtains at least one over k plus one of the optimal value.

For one matroid this gives one half. For two matroids it gives one third. The matching example with a ratio near one half does not show that one third is tight; it simply shows that naive greedy can already be suboptimal in a very small case. Stronger algorithms can improve these ratios under particular constraints or using more elaborate search strategies.

### Not all combinatorial constraints are matroids

A capacity limit on the total weight of chosen projects is a knapsack constraint. It is not automatically a matroid because feasible sets may violate exchange. A graph-matching constraint in a general nonbipartite graph also does not become an intersection of two vertex-side partition matroids, because there is no fixed two-sided vertex partition.

Moreover, maximizing a nonmonotone submodular function is a different problem. Adding a project might reduce the total value. Greedy that always adds the best currently feasible positive marginal may need different analysis or might stop early. Guarantees must not be copied from the monotone setting without checking their hypotheses.

Even within matroids, approximation bounds depend on the algorithmic model. A simple one-pass greedy procedure, a local-search method, and a continuous relaxation followed by rounding have different guarantees and costs. An approximation factor is never a property of the problem class alone; it is a theorem about a specific algorithm under stated assumptions.

### Why multiple constraints matter in practice

In recommendation systems, a set of items may have diminishing informational value while facing separate limits on categories, authors, and placements. In sensor selection, each new measurement helps less when similar sensors are already chosen, while power, location, and communication constraints apply simultaneously. In experiment design, statistical coverage is submodular but staff and instrument assignments can interact.

The correct modelling step is to identify which restrictions really form matroids, how many independently constrain the set, and whether the objective is monotone. Then one can select an algorithm with a credible approximation theorem.

The conceptual transition is simple and important. One matroid offers a one-for-one exchange. Intersecting k matroids may require k-for-one exchange. The greedy approximation factor follows that combinatorial accounting. More sophisticated optimization methods improve on greedy by making larger coordinated changes, but they still have to confront the same exchange structure.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Discrete Optimization: Relaxations, Integrality Gaps, and Certificates

**Track:** Optimization, Convexity, and Duality. **Background:** linear programming, dual bounds, graph constraints, and semidefinite relaxations. **Question:** how can continuous optimization help prove facts about decisions that must be integers or yes-or-no choices?

#### Mathematical companion (not spoken)

**Triangle vertex cover.** Minimize \(x_1+x_2+x_3\) subject to
\[
x_1+x_2\ge1,\quad x_2+x_3\ge1,\quad x_1+x_3\ge1,\quad x_i\in\{0,1\}.
\]
Integer optimum \(\mathrm{OPT}_{IP}=2\). Relaxing to \(0\le x_i\le1\) gives \(x_i=1/2\), with \(\mathrm{OPT}_{LP}=3/2\). The summed inequalities imply \(2\sum_i x_i\ge3\), so the relaxed optimum is certified. The ratio \(\mathrm{OPT}_{IP}/\mathrm{OPT}_{LP}=4/3\).

**Bound directions.** For minimization: \(\mathrm{OPT}_{relax}\le\mathrm{OPT}_{integer}\le f(x_{feasible})\). For maximization, reverse the roles: \(f(x_{feasible})\le\mathrm{OPT}_{integer}\le\mathrm{OPT}_{relax}\).

**Valid cut.** \(x_1+x_2+x_3\ge2\) for the triangle vertex-cover integer hull. It cuts off the fractional optimum but no valid integer cover.

**Branch-and-bound.** Branch on \(x_1\): if \(x_1=0\), then \(x_2=x_3=1\); if \(x_1=1\), then \(x_2+x_3\ge1\). Both branches have lower bound two. A cover of size two gives a matching upper bound.

**Weighted two-approximation.** For \(w_i\ge0\), rounding a feasible vertex-cover LP solution by \(\widehat x_i=\mathbf1[x_i\ge1/2]\) yields a valid cover and
\[
\sum_i w_i\widehat x_i\le2\sum_iw_ix_i\le2\,\mathrm{OPT}_{IP}
\]
when \(x\) is an LP optimum. Exactness for bipartite graphs is a separate integrality theorem related to the bipartite incidence matrix and König's theorem.

##### Exercises with answers

1. Is an LP relaxation's objective an upper bound or lower bound in integer minimization? **Answer:** a lower bound.
2. What extra inequality makes the triangle's original fractional optimum infeasible without rejecting any integer cover? **Answer:** \(x_1+x_2+x_3\ge2\).
3. Why does thresholding at one half cover every edge? **Answer:** an edge with both endpoints below one half would violate its LP edge constraint.
4. If a valid integer minimization solution costs 12 and a relaxation proves 12, what remains to prove optimality? **Answer:** nothing, provided both feasibility and the bound are correct.

##### Reading

Stephen Boyd and Lieven Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), relaxations and dual bounds; Stanford EE364b, [branch-and-bound and SDP relaxation lecture materials](https://web.stanford.edu/class/ee364b/lectures.html); MIT 6.854, [flow and integrality notes](https://courses.csail.mit.edu/6.854/18/Notes/n7-flow_computation.html).

### Relaxation, submodularity, nonmonotonicity, and matroid constraints

### Relaxation, submodularity, nonmonotonicity, and matroid constraints

#### Companions, sources, and study material (not spoken)

##### Submodular Optimization: Why Greedy Choices Can Be Provably Good

**Track:** Optimization, Convexity, and Duality. **Background:** set functions, matroids, LP relaxations, approximation algorithms. **Central question:** how much can we guarantee by repeatedly taking the best remaining marginal improvement?

###### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Why is weighted set coverage submodular for nonnegative weights? **Answer:** the newly covered elements after a larger selected set are a subset of those newly covered after a smaller set.
2. What factor does greedy guarantee under a cardinality budget? **Answer:** \(1-(1-1/k)^k\ge1-1/e\), under normalization, monotonicity and submodularity.
3. Why does the cut-size example invalidate an unrestricted monotone-greedy claim? **Answer:** cut size can decrease when a vertex is added, so the monotonicity hypothesis fails.
4. For the three sensors covering adjacent pairs of four points, what is the optimum with budget two? **Answer:** choose the two end sensors, covering all four points.

##### Reading and source notes

- G. L. Nemhauser, L. A. Wolsey, and M. L. Fisher, [*An Analysis of Approximations for Maximizing Submodular Set Functions I*](https://research.dial.uclouvain.be/entities/publication/a725e7a1-a49a-403e-8774-d62d8b8e000a), original approximation analysis (1978).
- G. L. Nemhauser and L. A. Wolsey, [*Best Algorithms for Approximating the Maximum of a Submodular Set Function*](https://pubsonline.informs.org/doi/10.1287/moor.3.3.177), oracle complexity and greedy bounds (1978).
- Francis Bach, [*Learning with Submodular Functions: A Convex Optimization Perspective*](https://arxiv.org/abs/1111.6453), Lovasz extensions and convex analysis.

##### Nonmonotone Submodular Optimization: When More Can Be Worse

**Track:** Optimization and Duality. **Background:** matroids, submodularity, greedy approximation, randomized rounding. **Central question:** how should we optimize diminishing-returns objectives when adding another element can reduce the total value?

###### Mathematical companion (not spoken)

Submodularity can be stated as `f(A)+f(B) >= f(A union B)+f(A cap B)`, equivalently `Delta_e f(A)>=Delta_e f(B)` whenever `A subset B` and `e notin B`. A cut function of an undirected nonnegatively weighted graph is nonnegative and submodular, but not monotone. On the graph of one unit-weight edge `ab`, `f({a})=f({b})=1`, `f(empty)=f({a,b})=0`.

If `f(empty)=0` and f is submodular, repeated diminishing returns gives `f(S)<=sum_{e in S} f({e})`. For any matroid whose rank is at most r, the best feasible singleton has value at least `OPT/r`, assuming `OPT>0`, `r>=1` and the elements of an optimal independent set are nonloops. This is a valid but weak bound; it does not imply a constant factor independent of r.

For a set function f, the multilinear extension is
\[
F(x)=\sum_{S\subseteq E} f(S)\prod_{e\in S}x_e\prod_{e\notin S}(1-x_e)=\mathbb E[f(R_x)].
\]
For submodular f, `partial_{ij}^2 F <=0` for distinct i,j; no general concavity of F follows. The independent-set polytope of a matroid M is `P(M)=conv{1_I:I independent}`. An independent Bernoulli draw from x in P(M) need not itself be independent, so rounding is an additional mathematical obligation.

For unconstrained **nonnegative** submodular maximization, randomized double greedy has an expected `1/2` approximation (Buchbinder–Feldman–Naor–Schwartz). Do not apply that ratio unchanged to a general matroid constraint. Constant-factor matroid algorithms require different techniques; see the cited work of Lee–Mirrokni–Nagarajan–Sviridenko and later improvements.

##### Exercises with answers

1. Why is the one-edge cut function nonmonotone? **Answer:** adding the second vertex to a singleton reduces the value from one to zero.
2. What bound follows from selecting the best singleton of a rank-r matroid for normalized submodular f? **Answer:** at least `OPT/r`, under the stated assumptions.
3. Is a multilinear extension necessarily concave? **Answer:** no; submodularity controls mixed partial derivatives, not full Hessian negative semidefiniteness.
4. Why does independent Bernoulli rounding fail to automatically respect a matroid? **Answer:** the randomly selected set can violate independence even if its marginal vector lies in the matroid polytope.

##### Reading and source notes

- [Buchbinder, Feldman, Naor, and Schwartz, A Tight Linear Time (1/2)-Approximation for Unconstrained Submodular Maximization](https://doi.org/10.1137/130929205), the unconstrained double-greedy guarantee.
- [Lee, Mirrokni, Nagarajan, and Sviridenko, Maximizing Nonmonotone Submodular Functions under Matroid or Knapsack Constraints](https://doi.org/10.1137/090750020), constant-factor algorithms under combinatorial constraints.
- [Chen, Nath, Peng, and Kuhnle, Discretely Beyond 1/e](https://arxiv.org/abs/2405.05202), later combinatorial improvements for constrained nonmonotone maximization.

##### Submodular Maximization Under Intersecting Matroid Constraints

**Track:** Optimization and Duality. **Background:** submodular functions, greedy approximation, matroids, and exchange properties. **Central question:** how do approximation guarantees change when one feasible-set rule is replaced by several simultaneous independence rules?

###### Mathematical companion (not spoken)

Let `f:2^E -> R_{>=0}` be normalized `f(empty)=0`, monotone and submodular: for `A subseteq B`, `e notin B`, `Delta(e|A)=f(A+e)-f(A)>=Delta(e|B)`. Feasible sets are `F=I_1 intersect ... intersect I_k` for matroid independent-set families I_j. This is a k-extendible system: given `A subseteq B` feasible and `A+e` feasible, separately use each matroid exchange to remove at most one element from `B\A`; their union has size at most k, and `(B\Z)+e` is feasible.

The maximum-marginal greedy algorithm for a normalized nonnegative monotone submodular f on a k-extendible system satisfies
\[
f(S_{\rm greedy})\ge\frac{1}{k+1}\,f(S^*).
\]
An exchange-charging proof maintains a feasible comparison set containing the greedy prefix; at each step, at most k removed comparison elements have marginals bounded by the chosen greedy marginal. Submodularity telescopes the bound `f(S*)<=f(S_greedy)+k sum_i Delta(g_i|S_{i-1})=(k+1)f(S_greedy)`.

**Worked bipartite matching example:** edges `e_11=(u_1,v_1)` weight `1+epsilon`, `e_12=(u_1,v_2)` weight 1, `e_21=(u_2,v_1)` weight 1. With epsilon in (0,1), greedy selects e_11, value `1+epsilon`, while optimum selects `{e_12,e_21}`, value 2. The ratio tends to 1/2. This is a counterexample to greedy optimality, **not** a tight example for the general `1/(k+1)` bound when k=2.

##### Exercises with answers

1. How many matroids describe a bipartite matching through left and right degree constraints? **Answer:** two partition matroids.
2. What simple greedy guarantee holds for a monotone submodular objective over the intersection of three matroids? **Answer:** at least `1/(3+1)=1/4` of optimum.
3. Why is a knapsack constraint not automatically a matroid? **Answer:** its weighted feasibility generally fails the matroid exchange axiom.
4. Does the same one-over-k-plus-one statement automatically hold for nonmonotone f? **Answer:** no; monotonicity was used in the charging proof.

##### Reading and source notes

- [Feldman and Ward, Submodular Maximization over a Matroid k-Intersection](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.89/LIPIcs.ICALP.2026.89.html), greedy baseline and newer approximation algorithms.
- [Constrained submodular maximization via greedy local search](https://www.sciencedirect.com/science/article/pii/S0167637718300038), multi-constraint local-exchange algorithms.
- [Feldman and Ward, arXiv preprint](https://arxiv.org/abs/2602.08473), formal problem statement and algorithmic improvements.
