# 003000 - Linear Programming and Duality: Two Answers That Certify Each Other

**Track:** Optimization, Convexity, and Duality. **Background:** algebra, inequalities, feasible regions. **Theme:** linear programming, weak and strong duality, complementary slackness, and shadow prices.

<!-- BEGIN SPOKEN LECTURE -->

# Linear Programming and Duality: Two Answers That Certify Each Other

Imagine running a small workshop with two products. Every day, you choose how many units of each to make. The products earn different amounts of money, but they compete for limited resources: raw material, machine time, perhaps storage space. You could try a few promising production plans and select the most profitable. But how would you know that some other feasible plan, among all the countless possibilities, would not be better?

Linear programming answers this question with an unexpected partnership. One problem chooses a feasible production plan and tries to make its value as large as possible. A second problem assigns prices to the scarce resources and tries to make an upper bound on production value as small as possible. The two problems look different. Yet in the appropriate mathematical setting, their best values agree. A feasible plan and a matching price assignment become a proof that no better plan exists.

We will build this idea from scratch using a workshop small enough to calculate by hand. Along the way we will distinguish weak duality, which needs only arithmetic, from strong duality, which is a deeper theorem. We will examine how the unused resources of an optimal plan relate to prices, and how the algebra becomes a practical certificate rather than merely a solver output.

## A workshop with three constraints

Let x be the daily quantity of the first product and y the quantity of the second. Each unit of x earns three units of value; each unit of y earns two. We want to maximize three x plus two y. We have three restrictions. Together, the two products use at most four units of a shared resource. The first product can use at most two units of a specialized resource. The second product can use at most three units of another. Production quantities must be nonnegative.

In symbols, the first constraint says x plus y is at most four. The next says x is at most two. The third says y is at most three. If the products were indivisible, we would have a different, discrete problem. For now we allow nonnegative real quantities. That is a modeling choice with consequences: our feasible set is a convex polygon and the objective is linear.

A quick candidate is x equals two, y equals two. It satisfies the shared limit exactly, uses all of the first specialized resource, and leaves one unit of the second specialized resource unused. Its objective value is three times two plus two times two, or ten. That is a valid lower bound on the maximum: we have demonstrated a plan earning ten. But does any plan earn eleven?

Try x equals two and y equals three. It earns twelve, but violates the shared resource constraint because the total is five. Try x equals one and y equals three. It is feasible and earns nine. Sampling plans gives us evidence that ten is plausible; sampling cannot rule out every possibility. To certify optimality, we need an inequality that covers the entire feasible region at once.

## Turn resource constraints into a bound

Look at the objective. Three x plus two y can be rewritten as two times the sum x plus y, plus one more x. This expression is helpful because the shared resource constraint bounds x plus y by four, and the first specialized resource bounds x by two. Therefore three x plus two y is at most two times four plus two, or ten, for every feasible plan.

Our candidate earns ten and our inequality says no feasible plan can exceed ten. We have a complete mathematical certificate. We can show it to someone who knows nothing about how we searched for the candidate. They need only check two things: the plan is feasible, and the weighted constraint inequality is valid.

Notice what we did not use. The inequality y at most three played no role in the upper bound. Its multiplier was zero. This turns out to correspond to a resource that is not binding at the selected optimum. Increasing that resource alone would not help the workshop, at least locally and in this simple model, because another constraint limits what can be produced.

We can imagine the inequality as a price list. Give each unit of shared resource a price of two. Give each unit of the first specialized resource a price of one. Give each unit of the second specialized resource a price of zero. Under those prices, producing one unit of x consumes resources with total assigned price three; producing one unit of y consumes resources with total assigned price two. The prices cover the contribution of every product. The total resource budget is priced at ten.

A price list of this kind is a dual-feasible solution. Its existence proves an upper bound on every primal production plan. In the example, the bound is sharp because a feasible plan reaches it. The production plan is primal feasible, the resource prices are dual feasible, and the two objective values match.

## The algebra of the dual

Let us generalize without losing the thread. A linear program can maximize a linear objective over nonnegative decision variables, subject to linear inequalities. Imagine a matrix of resource requirements: every row represents a resource constraint, every column represents a product or activity. The vector of available resources provides the right-hand sides. The vector of product values gives the objective coefficients.

For each resource constraint, choose a nonnegative price. If the weighted sum of resource requirements for every product is at least that product's value, then the total priced resource budget is an upper bound on all feasible production value. Why? Multiply each resource inequality by its nonnegative price and add them. Nonnegative multipliers preserve the direction of inequalities. Reorganize the sum by product. The price condition on each product gives the required bound.

The primal question is: how much value can our resources produce? The dual question is: how cheaply can we assign nonnegative resource prices so that the resources required for each product cost at least what that product is worth? The primal wants a large number, the dual a small one. Their feasibility requirements guarantee that every primal value is at most every dual value.

This last sentence is weak duality. It is called weak because it does not guarantee that the best primal and dual values are equal. It simply provides the bound. The proof is short, universal, and extremely useful. We can verify it by expanding one line of matrix algebra or by following the workshop's weighted inequalities.

Weak duality even tells us something when a problem is hard to solve. A feasible primal plan earning ninety and a dual-feasible certificate worth one hundred show that the true optimum lies between ninety and one hundred. We have a gap of ten. We may improve either side independently, and each improvement narrows the uncertainty about the optimum.

## When the bounds meet

Strong duality is the deeper claim: for ordinary finite-dimensional linear programs under the appropriate feasibility and finiteness conditions, the best primal and dual values are equal and the optima are attained. This is not just a lucky feature of our workshop example. It is a structural theorem about linear inequalities.

There are qualifications. If a linear program is infeasible, there is no admissible plan on one side. If it is unbounded in the optimizing direction, there may be no finite best value. One must state the hypotheses before claiming equal attained optima. In particular, the casual phrase "the primal and dual always have the same optimum" is false unless we specify the cases in which optima exist.

The geometry helps explain why equality is possible. The feasible set is a polyhedron, formed by the intersection of halfspaces. The objective's level sets are parallel hyperplanes. As we push the objective plane upward, the last one touching the feasible set is a supporting plane at the optimum. The coefficients of that plane can be represented, under the duality theorem, through nonnegative combinations of active constraint normals.

The multipliers of the active constraints become dual prices. This geometric picture connects the arithmetic certificate to separation theorems. The primal solution locates a supporting objective plane; the dual expresses the support using the resource constraints. We should still prove strong duality through a rigorous theorem, but the geometry shows why it is plausible.

For our workshop, no general theorem is required to establish the specific answer. The feasible plan worth ten and the resource-price bound worth ten already prove optimality. Strong duality tells us that such exact matching certificates exist much more broadly when a linear program has a finite optimum.

## Complementary slackness: unused capacity and zero prices

Inspect the workshop solution again. Shared resource use is four, so the shared constraint is tight. The specialized resource for x is also used fully. The specialized resource for y has one unit unused. Our dual prices were two, one, and zero. The unused resource received price zero.

That pattern is a special case of complementary slackness. At optimal primal and dual solutions, the product of each resource constraint's slack and its dual price is zero. A resource with positive price must be used up at the optimum. A resource with unused capacity must have zero price. The converse direction needs care: a tight constraint can still have zero price, so being fully used does not automatically imply positive value.

There is a companion condition on products. If a product is produced in positive quantity, its value must match its resource cost at the optimal dual prices. If a product's resource cost strictly exceeds its value, optimal production of that product must be zero. Our two products are produced, and their priced requirements match three and two exactly.

These conditions can be derived from the proof of weak duality. The difference between the dual and primal objective values is a sum of nonnegative terms. The terms come from unused resource budgets multiplied by their prices, and from product quantities multiplied by excess priced resource cost. If the total gap is zero, every nonnegative term must be zero. This gives complementary slackness.

The argument is valuable for debugging. Suppose a solver reports a primal plan, dual multipliers, and a zero objective gap, but one constraint is violated. The certificate fails. Or suppose every constraint is satisfied but a claimed positive price is attached to a resource with positive slack. The purported optimum violates complementary slackness and needs investigation.

## How the historical problem looked to its inventors

These ideas were developed by people dealing with concrete resource-allocation problems. In the late 1930s, Leonid Kantorovich worked on allocating equipment and materials for Soviet plywood production. The challenge was to coordinate machines producing different outputs under resource constraints. Kantorovich's 1939 work used resolving multipliers related to what we now recognize as dual prices. It was mathematics with an immediate industrial setting, developed in a distinct political and institutional environment.

Across the world, George Dantzig was involved in large-scale military planning during and after the Second World War. In a later interview, he recalled the enormous amount of work required to prepare plans by hand, before general-purpose computing made large optimization models routine. His colleagues sought a way to mechanize planning. By 1947 he had developed the linear-programming formulation and the simplex method for solving it.

The two lines of work were substantially independent. Dantzig's recollections give a human view of the problem: planners faced competing requirements, repeated adjustments, and a proliferation of rules that did not make it easy to identify the best overall decision. A mathematical objective and a feasible system of inequalities supplied a common language. The simplex method then offered a systematic way to search the vertices of the feasible polyhedron.

The history has an important complication. Neither the mathematical objective nor the constraints could decide what a society ought to value. A supply plan maximizing one chosen quantity might neglect costs, risks, or people not represented in the model. The mathematics can optimize an explicit objective; selecting that objective is a human and institutional decision. The power of linear programming is greatest when we remember which questions the model answers and which it leaves open.

## Why vertices are useful and sometimes misleading

In two dimensions, we can draw the feasible polygon and evaluate the objective at its corners. For a linear objective over a nonempty bounded polytope, at least one maximum occurs at a vertex. That explains why solving tiny linear programs by inspection of corners often works. For our workshop, the relevant candidate lies where x equals two and x plus y equals four.

But the slogan "the optimum is at a corner" is not a complete algorithm. In high dimensions there may be an enormous number of vertices. A nonempty polyhedron can also be unbounded, and the objective may have no finite maximum. An optimal face may contain many points, only some of which are vertices. We need the relevant existence and polyhedral hypotheses before drawing strong conclusions.

The simplex algorithm moves among basic feasible solutions, usually associated with vertices, improving the objective under a pivoting rule. Its practical success is substantial, but basic pivot rules can exhibit worst-case exponential behavior. The dual certificate is more general than the trajectory of any one algorithm. An interior-point solver and a simplex solver can arrive at certificates of the same mathematical optimum despite following quite different computational paths.

That separation between method and certificate is powerful. We may rely on sophisticated heuristics, sparse matrix methods, presolvers, and numerical approximations to discover promising candidates. Once a candidate primal-dual pair is available, we can evaluate the defining inequalities and objective gap independently. With rational coefficients, exact rational arithmetic can sometimes certify the result. With floating-point data, interval bounds and residual analysis can quantify what the computed certificate actually establishes.

## A small sensitivity experiment

The workshop's shared resource has dual price two. Suppose we increase its capacity from four to four and a half units, while keeping the other restrictions unchanged. We could raise y from two to two and a half while keeping x equal to two. Production value increases from ten to eleven. The dual price two correctly predicts the gain: half an extra unit of resource is worth one more unit of objective value in this range.

If we keep increasing the shared resource indefinitely, the price cannot remain valid forever. Eventually y reaches its own cap of three, and with x still capped at two the total production cannot exceed five units. Once the shared resource exceeds five, increasing it further adds no value. Shadow prices represent local or piecewise-linear marginal values, subject to changes in the active constraints.

This is why dual variables can aid decision-making rather than merely prove a theorem. They identify scarce constraints and approximate the value of relaxing them. But the interpretation depends on the model, the relevant range, and degeneracy or nonuniqueness of dual solutions. An optimal multiplier is a mathematically valid sensitivity certificate under appropriate conditions, not an unconditional market price or a statement about moral worth.

## The primal-dual gap as an auditable quantity

For the workshop, the dual objective is four times the shared-resource price, plus two times the first specialized price, plus three times the second specialized price. The primal objective is three x plus two y. Subtract the primal value from the dual bound. With a little algebra, the gap splits into two families of nonnegative contributions.

The first family charges each unused unit of resource at its dual price. The second charges each produced unit for any excess of its priced resource requirements over its product value. When primal and dual feasibility hold, every contribution is nonnegative. So a zero total gap forces every contribution to vanish. That is complementary slackness, derived from an accounting identity rather than memorized as a mysterious theorem.

At x equals two, y equals two, with dual prices two, one, and zero, the shared-resource slack is zero and the first specialized slack is zero. The second specialized slack is one but has zero price. The priced requirements of both products exactly equal their unit values. Every term in the gap is zero. We can audit the equality by reading the production plan and the price list side by side.

For an approximate solver, the gap can be small rather than exactly zero. If we have independently verified feasibility, a dual value of ten point zero one and a primal value of ten tells us the true maximum lies in that one-hundredth interval. That is an interpretable guarantee. If the displayed values are merely rounded numbers and the underlying constraints are slightly violated, however, the apparent small gap is not yet a mathematical certificate. Residual checks must account for arithmetic error.

## Certificates when no feasible solution exists

Duality has a surprising sibling: an infeasibility certificate. Imagine requirements that x must be at least two and at most one. There is obviously no feasible x. We can prove it by adding the inequalities with suitable signs to obtain zero at most negative one. The contradiction certifies infeasibility without searching for a candidate.

In a general system of inequalities, Farkas-type alternatives formalize this phenomenon. Under an appropriate standard-form convention, either there exists a nonnegative vector satisfying the constraints, or there exists a vector of nonnegative multipliers that combines the constraints into an impossible inequality. The exact sign pattern depends on which form of the linear program we choose; changing inequality directions requires changing the certificate conditions too.

The idea is valuable in software verification and mathematical modeling. A numerical solver might announce that a planning problem is infeasible. A multiplier certificate provides a reason: a specific nonnegative combination of the stated requirements contradicts itself. That may expose an accidentally reversed inequality, a missing slack variable, or genuinely conflicting business requirements. Again, the machine's answer becomes easier to trust when it is accompanied by an independently checkable argument.

## What the two problems teach us

The primal and dual supply two different forms of evidence. A primal-feasible point proves that a certain value is attainable. A dual-feasible point proves that values beyond a certain bound are impossible. Weak duality guarantees that the lower and upper bounds cannot cross. Strong duality explains why, for suitable linear programs, the two frontiers can meet. Complementary slackness records what equality forces about resource use and reduced costs.

Return to the workshop. A person may find a production plan earning ten by insight or luck. Another may find a price list bounding earnings by ten. Neither person needs to trust the other's search procedure. By checking the plan and prices, both can agree that ten is optimal. This is one of optimization's deepest patterns: instead of trusting an answer because a solver produced it, we can ask for a second mathematical object that explains why the answer cannot be improved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### The workshop

Primal (P): maximize `3x+2y` subject to `x+y<=4`, `x<=2`, `y<=3`, `x,y>=0`.

Dual (D): minimize `4u+2v+3w` subject to `u+v>=3`, `u+w>=2`, `u,v,w>=0`.

Primal certificate: `(x,y)=(2,2)` gives value 10. Dual certificate: `(u,v,w)=(2,1,0)` gives value 10. For all primal feasible `(x,y)`, `3x+2y <=2(x+y)+x <= 2*4+2 = 10`.

### General primal-dual form

For `max c^T x` such that `A x <= b, x>=0`, the dual is `min b^T u` such that `A^T u>=c, u>=0`. Weak duality: `c^T x <= (A^T u)^T x = u^T A x <= u^T b`.

Complementary slackness at optimum: `u_i (b_i-(Ax)_i)=0` and `x_j ((A^T u)_j-c_j)=0`. If both solutions are feasible, these equalities imply equality of objective values and hence optimality.

### Exercises and answers

1. **Check feasibility:** Is `(x,y)=(1,3)` feasible? Value? **Answer:** Yes; shared resource 4, x cap 2, y cap 3; value 9.
2. **Dual check:** Is `(u,v,w)=(1,2,1)` feasible? Bound? **Answer:** Yes: `u+v=3`, `u+w=2`; dual objective `4+4+3=11`.
3. **Sensitivity:** Raising the shared cap from 4 to 4.5 increases optimum by how much? **Answer:** 1; plan `(2,2.5)` earns 11.
4. **Logical distinction:** Does weak duality by itself prove the primal and dual optima coincide? **Answer:** No; it only orders feasible objective values.

### References

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004), linear programming and duality: https://web.stanford.edu/~boyd/cvxbook/
- MIT 6.854 lecture notes, "LP Duality": https://courses.csail.mit.edu/6.854/18/Notes/n12-duality.html
- George Dantzig oral history, INFORMS: https://www.informs.org/Explore/History-of-O.R.-Excellence/Oral-Histories/George-Dantzig
- Leonid Kantorovich biography, MacTutor: https://mathshistory.st-andrews.ac.uk/Biographies/Kantorovich/
