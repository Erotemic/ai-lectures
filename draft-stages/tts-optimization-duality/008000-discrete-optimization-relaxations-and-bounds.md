# 008000 — Discrete Optimization: Relaxations, Integrality Gaps, and Certificates

**Track:** Optimization, Convexity, and Duality. **Background:** linear programming, dual bounds, graph constraints, and semidefinite relaxations. **Question:** how can continuous optimization help prove facts about decisions that must be integers or yes-or-no choices?

<!-- BEGIN SPOKEN LECTURE -->

# Discrete Optimization: Relaxations, Integrality Gaps, and Certificates

Many decisions cannot be fractional. We either build a facility or do not. A job is assigned to one worker, not seven tenths of a worker. A vertex of a graph is selected or it is not. These yes-or-no requirements make optimization much more difficult than simply minimizing a smooth function over a convex region.

A useful strategy is to temporarily remove the integrality restriction. Let each binary decision variable take any real value between zero and one. Solve the resulting linear or convex optimization problem. Its solution may not be a valid decision, but it gives a rigorous bound on the best valid decision. This is called a relaxation.

We must be careful about the direction of the bound. For minimization, allowing more candidate solutions can only decrease the optimal value. So the relaxed optimum is a lower bound on the best integer objective. For maximization, allowing more candidates can only increase the optimum, so the relaxed optimum is an upper bound. If we find a valid integer candidate whose objective matches the relaxation bound, we have proved that candidate optimal.

## A triangle with three constraints

Consider a triangle graph with vertices A, B, and C. We want to select as few vertices as possible so that every edge has at least one selected endpoint. This is the minimum vertex-cover problem.

Assign a binary variable to each vertex, one if selected and zero otherwise. For each edge, require the sum of the variables at its endpoints to be at least one. Minimize the sum of all three variables.

An integer solution cannot select only one vertex: that vertex misses the edge between the other two. Selecting any two vertices works, so the integer optimum is two.

Now relax the variables to lie between zero and one. Assign one half to each vertex. Every edge constraint is satisfied because one half plus one half equals one. The total objective is one and one half. In fact this is the best fractional value. Sum the three edge inequalities. Every vertex appears twice, so twice the total sum must be at least three. Therefore the sum is at least one and one half, attained by the half-half-half assignment.

The linear program has proved a lower bound of one and one half, but the actual discrete problem requires two. Their difference is an integrality gap. As a ratio, the integer optimum divided by the relaxed optimum is four thirds for this instance.

This example teaches two things at once. A relaxation can give a sharp bound on the continuous feasible set, complete with a short proof, and still fail to describe the integer feasible set exactly. The distinction is structural, not numerical rounding error.

## When the relaxation is exact

Some discrete problems have linear relaxations whose extreme points are automatically integral. Bipartite vertex cover is one example when written with its standard edge-cover constraints and nonnegative costs: the associated vertex-cover polyhedron has integral extreme points. This is related to the structure behind König's theorem and maximum flow.

Another language for this phenomenon is total unimodularity. If an integer constraint matrix is totally unimodular and the right-hand side is integral, then vertices of the associated polyhedron are integral under the usual full-rank and feasibility qualifications. This can eliminate the need for branching or rounding. Not every graph or combinatorial constraint matrix has that property. The triangle example demonstrates a fractional vertex, so its relaxation is not integral.

For a model builder, the question should not be merely whether an integer program has been written down. Ask whether its linear relaxation has special structure that makes it exact, or almost exact, or whether it can be strengthened by valid inequalities.

## Branch-and-bound turns bounds into a proof

Suppose the linear relaxation has a fractional optimum. Pick a variable that must be integer but currently has a fractional value. In a binary problem, split the search into two subproblems: one fixes the variable to zero and the other fixes it to one. Every valid integer solution belongs to one of these branches.

Solve a relaxation in each branch. Because these are minimization problems, each relaxed optimum gives a lower bound on integer solutions in that branch. Meanwhile, any valid integer solution gives an upper bound on the global optimum. If a branch's lower bound is no better than the current integer solution, we may discard that entire branch: no descendant can improve the incumbent.

Return to the triangle. At the fractional solution, all three variables equal one half. Branch on the variable for A. If A is zero, both B and C must be one to cover the edges incident to A. The objective is at least two. If A is one, the edge between B and C still requires B plus C to be at least one, so the objective is again at least two. A feasible selection of two vertices attains that value. Both branches are resolved; the integer optimum is certified.

A general branch-and-bound algorithm may explore many nodes, sometimes exponentially many. Its advantage is that every pruned subtree has a mathematical justification. A final optimality claim can be supported by a feasible incumbent and bounds covering the remaining alternatives.

## Cuts sharpen the relaxation

Instead of branching immediately, we can add inequalities that every integer solution satisfies but some fractional solutions violate. These are cutting planes. In the triangle problem, add the inequality that the sum of all three vertex variables must be at least two. It is valid for every integer vertex cover, but violated by the all-halves fractional solution. The relaxation becomes tighter without excluding any permissible integer answer.

The key obligation is to prove validity. A cut that removes an inconvenient fractional point but also removes a valid integer optimum is not a legitimate relaxation improvement.

In the triangle, validity follows from a short combinatorial argument: selecting at most one vertex leaves the edge between the other two uncovered. For larger models, inequalities may come from parity, flows, cycles, submodularity, or problem-specific combinatorics.

## Approximation from a fractional solution

Sometimes finding the exact integer optimum is computationally too expensive, but the relaxation can guide a solution with a provable approximation ratio.

For weighted vertex cover with nonnegative vertex costs, solve the linear relaxation. Select every vertex whose fractional value is at least one half. Every edge has endpoint values summing to at least one, so at least one endpoint crosses the threshold. Thus the rounded selection covers all edges.

What does it cost? Every selected vertex has cost at most twice its cost multiplied by its fractional value, because its fractional value is at least one half. Summing over selected vertices, the rounded cost is at most twice the fractional objective over all vertices. And the fractional optimum is at most the integer optimum. Therefore the rounded solution costs at most twice the best possible integer cover.

This is a two-approximation guarantee. It is not a claim that every instance incurs twice the optimum; it is a worst-case upper bound derived from two explicit inequalities. We have used the relaxed solution both as a guide for rounding and as a certificate against which to compare the result.

## What a certificate should contain

For a discrete minimization problem, a useful proof artifact consists of a valid discrete solution, its objective value, and a lower bound established by a relaxation, a dual feasible point, a combinatorial inequality, or a complete branch-and-bound argument. If the lower and upper bounds match, optimality is proved. If they differ, the gap quantifies what has not been established.

The same logic extends to semidefinite relaxations, where a binary vector may be lifted to a positive semidefinite matrix and a difficult rank constraint is dropped. The resulting bound can be stronger than a simple linear relaxation, but the direction of the bound must still be tracked, and converting the matrix back to a valid discrete solution requires a separate argument.

Discrete optimization connects combinatorics to convex analysis precisely because the continuous problem is not the whole problem. Relaxations, integrality results, valid cuts, and rounding methods let us use continuous mathematics without pretending fractional answers are acceptable final decisions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Is an LP relaxation's objective an upper bound or lower bound in integer minimization? **Answer:** a lower bound.
2. What extra inequality makes the triangle's original fractional optimum infeasible without rejecting any integer cover? **Answer:** \(x_1+x_2+x_3\ge2\).
3. Why does thresholding at one half cover every edge? **Answer:** an edge with both endpoints below one half would violate its LP edge constraint.
4. If a valid integer minimization solution costs 12 and a relaxation proves 12, what remains to prove optimality? **Answer:** nothing, provided both feasibility and the bound are correct.

### Reading

Stephen Boyd and Lieven Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), relaxations and dual bounds; Stanford EE364b, [branch-and-bound and SDP relaxation lecture materials](https://web.stanford.edu/class/ee364b/lectures.html); MIT 6.854, [flow and integrality notes](https://courses.csail.mit.edu/6.854/18/Notes/n7-flow_computation.html).
