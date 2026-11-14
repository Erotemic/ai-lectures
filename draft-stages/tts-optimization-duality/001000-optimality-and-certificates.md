# 001000 — When Is a Solution Truly Best? Optimization and Certificates

**Track:** Optimization, Convexity, and Duality. **Background:** elementary algebra, graphs, and functions; introductory derivatives are explained where used. **Theme:** modeling choices, constraints, geometry, and independent certificates of optimality.

<!-- BEGIN SPOKEN LECTURE -->

# When Is a Solution Truly Best? Optimization and Certificates

A factory has a limited amount of material and machine time. It can produce two products, each with a different benefit. You can try a plausible allocation, perhaps make two of the first product and two of the second. You calculate a benefit of ten units. That sounds good. But how could you establish that no other feasible allocation does better?

This question is deeper than merely finding a promising answer. There might be thousands of allocations, or a continuous range of choices too large to enumerate. Even if an algorithm searches efficiently and returns a candidate, we still need to distinguish 'this is what the algorithm found' from 'this is globally optimal.' Mathematical optimization is the study of problems that ask for the best feasible choice, but its most satisfying results often provide a short, independent explanation of why a choice is best.

Today we will develop such an explanation. We will begin with a tiny production problem. Then we will find a way to certify its optimum without checking every possible allocation. This leads to linear programming duality, supporting geometry, and the larger idea that a difficult search problem can have an easily checked proof of optimality.

## A production problem you can calculate by hand

Imagine two products, A and B. Each unit of A contributes three units of value. Each unit of B contributes two. Let x be the quantity of A and y the quantity of B. We are allowed to produce fractional quantities, perhaps because we are measuring tons of output or divisible processing time. Both x and y must be nonnegative.

The shared machine can handle at most four units altogether, so x plus y is at most four. A specialized part limits production of A to at most two units. A separate supply limits B to at most three. These are the constraints. The objective is three times x plus two times y, which we want to maximize.

Start with a reasonable feasible choice. Two units of A and two of B use all four units of machine capacity, meet the specialized-part limit, and stay under the supply limit for B. Their value is six plus four, or ten. Could another combination exceed ten?

The temptation is to sample possibilities. Four units of B would be worth eight, but violate the B supply limit. One unit of A and three of B are feasible and worth nine. Two units of A and one unit of B are worth eight, leaving a unit of machine time unused. Sampling suggests the ten-unit solution is strong. It has not yet established optimality.

Here is a different argument. Take any feasible allocation, not just the one we tried. Its value is three x plus two y. Regroup that expression as two times the sum x plus y, plus an additional x. The total quantity x plus y is at most four. The amount x is at most two. Therefore the value is at most two times four plus two, which is ten.

Stop and notice what just happened. The proof applies simultaneously to every feasible choice. We used two resource limits, multiplied them by nonnegative numbers, and combined them into an upper bound on the objective. The proposed allocation achieves the bound. Consequently it is optimal. There is nowhere better to look.

This is an optimality certificate. It is short enough to check by hand, even if the search that discovered the allocation were extremely complicated. The upper bound would still be valid if we added thousands of feasible candidates that obeyed the same constraints.

## The geometry under the arithmetic

There is a picture behind the argument. Put x on a horizontal axis and y on a vertical axis. Nonnegativity confines us to the first quadrant. The inequality x plus y at most four lies below a downward-sloping line. The specialized-part limit lies to the left of the vertical line x equals two. The B supply limit lies below the horizontal line y equals three.

The feasible choices form a polygon. As long as we stay inside it, every constraint is satisfied. The objective has straight contour lines: all allocations with value nine lie on one line, and those with value ten lie on a parallel line. To maximize value, imagine sliding the objective line outward until it just touches the feasible polygon. For this problem it touches at x equals two and y equals two.

Why can an optimum of a linear function on a bounded polygon be found at a vertex? If a point lies in the middle of a line segment joining two feasible points, its value is the same weighted average of the endpoint values. It cannot exceed both endpoints. Repeatedly moving toward an endpoint never reduces the best attainable value. When there are finitely many polygon vertices, one of them attains a maximum. A linear objective can also be constant along an entire edge, so 'the optimum is a vertex' means that a vertex optimum exists, not that every optimum is an isolated corner.

This geometric account is intuitive, but we should distinguish it from the earlier certificate. The certificate did not require us to list every polygon vertex. It used inequalities to place a ceiling on all feasible objective values. A good optimizer needs both perspectives: a method for constructing candidates, and a principle for explaining why a candidate cannot be improved.

## Why constraints have prices

Return to the bound of ten. We multiplied the shared machine constraint by two and the A-specific constraint by one. The B-specific constraint did not enter our proof. Think of these multipliers as prices placed on scarce resources. One unit of shared machine capacity is priced at two units of value, while one unit of the A-specific resource is priced at one. The B resource currently receives price zero.

These are not market prices quoted by a factory. They are mathematical numbers chosen to make a global upper bound. Every unit of A earns value three and consumes one unit of shared capacity plus one A-specific unit, whose assigned prices total three. Every unit of B earns value two and consumes one unit of shared capacity, whose price is two. So the assigned prices cover the value of either product.

The total priced resource supply is two times four plus one times two, again ten. No feasible production plan can earn more value than the resources are assigned. The candidate earning ten exactly matches this bound. That is the heart of linear programming duality.

Let's see why the direction of the inequality is essential. If I am trying to maximize value, a valid certificate gives an upper bound. An upper bound of twelve does not prove ten is optimal; some feasible allocation might earn eleven. A bound of ten, together with a feasible allocation earning ten, closes the gap. The best lower bound from a feasible candidate and the best upper bound from a certificate meet.

A general linear program has variables, an objective, and linear equality or inequality constraints. Its dual is another optimization problem whose variables are often associated with the original constraints. Feasible solutions of the dual produce bounds on feasible solutions of the original, or primal, problem. The property that makes those bounds valid is weak duality. Under suitable conditions, strong duality says the best primal value and the best dual bound agree.

The words 'under suitable conditions' deserve attention. In finite-dimensional linear programming, when a finite optimum is attained under the usual feasible bounded assumptions, a dual optimum with the same value exists. In more general nonlinear and infinite-dimensional optimization, additional qualifications can be important. We should not teach strong duality as an unconditional magic formula.

## George Dantzig and the problem of planning

In the years after the Second World War, organizations faced planning questions involving resources, shipments, schedules, and conflicting requirements. George Dantzig worked on mechanizing aspects of planning for the United States military. In a later oral history, he explained that many planning rules had been handled manually and that translating them into a system of linear inequalities made mathematical treatment possible.

Dantzig described formulating a linear programming model in June 1947 and proposing the simplex method that August. His account also emphasizes that early attempts and intuitions did not make the eventual method obvious. He initially considered movement along the edges of a feasible polyhedron unattractive, then found a way to exploit the geometric structure productively. The mathematics arose from an institutional need, but it outgrew that setting.

We should not confuse the name simplex with a claim that the procedure always takes a small number of steps. There are linear programs on which particular simplex pivot rules have exponential worst-case behavior. Yet the method has been extraordinarily successful in practice, and later interior-point algorithms supplied different powerful methods and complexity guarantees. Here is a fruitful distinction: a mathematical characterization of optimality and an algorithm for locating an optimum are related but separate achievements.

The human context is worth remembering. An optimizer does not choose society's goals. Someone decides what is being counted as value, what resources are protected, and which constraints express genuine obligations. Efficiently solving the wrong model can produce an answer that is mathematically impeccable and operationally harmful. Optimization makes tradeoffs explicit; it does not absolve us of choosing them responsibly.

## From straight lines to curved surfaces

Not every objective is linear. Suppose we want to minimize a cost that measures how far a chosen setting x lies from three. Let the cost be the square of x minus three, plus one. Its smallest unrestricted value is one, attained at x equals three. But suppose the device is required to operate at x at least four. The unconstrained optimum is infeasible.

We can solve this by inspection. For x at least four, the distance from three grows as x grows. So the minimum occurs at the boundary x equals four, where the cost is one squared plus one, or two. If we plotted the cost, we would see a bowl-shaped curve and the feasible region beginning to the right of four.

That bowl has a crucial property: it is convex. If you draw a straight chord between two points on its graph, the graph lies no higher than the chord. In one variable, twice differentiable convex functions have nonnegative second derivatives; our squared distance has second derivative two. In higher dimensions, convexity requires the same kind of inequality for every line segment joining two feasible points.

For a convex objective minimized over a convex feasible set, any local minimum is global. Why? Suppose x is locally optimal but another feasible point y has strictly smaller cost. Move a tiny distance from x toward y. Convexity tells us the cost on that short segment is no larger than the corresponding weighted average of the endpoint costs, and therefore strictly smaller than the cost at x. That contradicts local optimality. The shape of the problem excludes hidden deeper valleys.

This property is one reason convex optimization occupies such a central place in numerical mathematics. It does not say every convex problem is easy computationally or that every relevant real-world problem is convex. It gives us powerful global reasoning that is absent for arbitrary nonlinear objectives.

## An inequality that supports a curve

We can prove the constrained minimum without relying on a picture. At x equals four, the cost is two. For any x at least four, write the cost as two plus two times x minus four, plus the square of x minus four. Both remaining terms are nonnegative. So the cost is at least two, with equality at four.

That is another certificate: an explicit decomposition into an attained lower bound plus nonnegative terms. The squared-distance structure made it possible to write. The same idea appears when we use a tangent line as a supporting line of a convex function. At the boundary point four, the tangent slope is two. The tangent line gives a global lower bound for the convex function, and the feasible region begins where that tangent line is already rising.

Let's write the derivative concept in words. The derivative of the cost at x measures how the cost changes under a tiny movement in x. Here the derivative is twice x minus three. At x equals four, it equals two. Moving to the right initially raises the cost at rate two per unit. Movement to the left would lower the cost, but the constraint forbids it. Thus the positive slope and the active boundary constraint fit together.

This is an elementary example of an optimality condition. In an unconstrained differentiable problem, an interior optimum must have zero derivative. At a constrained optimum, the derivative need not vanish; it can be balanced by a constraint that prevents movement in an improving direction. That balance leads to Lagrange multipliers.

## Lagrange multipliers as a balance of forces

Represent the constraint x at least four as four minus x at most zero. Multiply it by a nonnegative number called lambda, and add it to the cost. This forms a Lagrangian. For any feasible x, four minus x is nonpositive, so the Lagrangian is no greater than the original cost. If we then minimize the Lagrangian over all x, even infeasible ones, we get a lower bound on the best feasible cost.

Try lambda equal to two. The Lagrangian is the square of x minus three, plus one, plus two times four minus x. Complete the square. It becomes the square of x minus four, plus two. Its minimum over all real x is exactly two. So every feasible x must have original cost at least two. Our candidate x equals four achieves it. Once again, a feasible candidate and a matching bound certify optimality.

The multiplier two has a geometric meaning: it balances the slope of the original objective with the slope of the active constraint. In the formal conditions, the derivative of the Lagrangian vanishes at the optimizer. The multiplier is nonnegative, the constraint is satisfied, and the multiplier times the constraint slack is zero. The last condition is called complementary slackness.

Why would a multiplier times slack have to vanish? If a resource is not binding, meaning there is slack left over, then a strictly positive price would ordinarily waste some of our bound. If the price is positive at an exact optimum, the corresponding resource is binding. This principle was visible in our production example: the unused B-specific supply received a price of zero, while the two tight resource limits carried positive prices.

For well-behaved convex problems, these ideas connect through the Karush–Kuhn–Tucker conditions. They form a system of feasibility, stationarity, multiplier sign, and complementary slackness equations. Under appropriate constraint qualifications they provide necessary conditions; with convexity they can give sufficient conditions for global optimality. Without the relevant hypotheses, memorizing these conditions can lead to false conclusions.

## A trap: the best-looking answer is not a proof

Consider a nonconvex function with two valleys. A gradient-based algorithm may walk downhill until it reaches the nearest valley. It can satisfy a zero-gradient condition and still miss a deeper valley elsewhere. Even a solution that looks stable to small perturbations can fail to be globally best.

Or consider integer decisions. Perhaps a factory must manufacture whole machines, and half a machine is not allowed. Our earlier linear relaxation permitted fractions. A linear-programming optimum can provide a bound for the integer problem, but a fractional solution is not necessarily feasible for the original decision. Integer programming needs additional reasoning, such as branching, cutting planes, or problem-specific combinatorial structure. The upper-bound logic survives, yet feasibility is more demanding.

A verified optimization algorithm must therefore say what it guarantees. Does it find a feasible point? Does it converge to a stationary point? Does it approximate the global minimum within a tolerance? Does it return a certificate that can be independently checked? Those are distinct mathematical contracts.

For numerical methods there is another issue: floating-point error. A program might report a candidate and a bound that differ by a tiny amount. If the reported inequalities were rounded, we should not simply declare a mathematical optimum from their printed decimals. A rigorous certificate may require exact rational arithmetic, interval bounds, or a carefully established error analysis. Mathematical optimization and numerical verification meet at this boundary.

## The broader idea of duality

Duality can look mysterious when introduced as a second optimization program appearing from a table of formulas. The examples give us a more useful picture. Start with a problem of constructing the best feasible plan. Then build a second problem of assigning values to constraints so that no plan can exceed a certain bound. The two problems look different, but they describe opposite sides of the same question.

This structure appears across mathematics. In shortest-path problems, a path gives an upper bound on the shortest distance, while suitable distance potentials establish lower bounds. In maximum-flow problems, a flow gives a lower bound on the maximum value, while a cut bounds it from above. In spectral analysis, variational principles characterize eigenvalues through minimization and maximization over spaces or subspaces. In convex geometry, supporting hyperplanes bound a shape through linear functionals. The details differ, but the idea of an independently checkable bound is persistent.

There is also a way to translate an optimality certificate into an explanation of scarcity. A positive dual multiplier can indicate that increasing a particular resource could improve the optimum, under the local assumptions of the model. But do not interpret every multiplier as a universal real-world market value. Sensitivities depend on the formulation, active constraints, uniqueness, and the range over which the model remains valid.

## What it means to know an answer is best

Our first allocation earned ten units. The candidate alone was a proposal. The inequality bounding every feasible allocation by ten was the proof. For a curved cost, the candidate x equals four was a proposal. The completed square gave a universal lower bound of two, and the candidate achieved it. Both problems taught the same pattern from different sides.

To solve an optimization problem is to find a feasible object with a favorable value. To establish optimality is to connect that object to a bound no feasible object can beat. Geometry explains why such bounds exist in structured problems. Duality gives a systematic way to construct them. Convexity explains when local reasoning is globally reliable.

Perhaps the most useful habit is to ask two questions whenever a computed answer is called optimal. First, what proves that the answer satisfies the actual constraints? Second, what proves that a better feasible answer is impossible, or at least how far away could the best answer still be? These are questions that join algorithms, mathematics, and formal verification. They turn a numerical result into an argument.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### A complete linear program and its dual

Primal:

\[
\max_{x,y\geq0}3x+2y\quad\text{subject to } x+y\leq4,\ x\leq2,\ y\leq3.
\]

Dual:

\[
\min_{a,b,c\geq0}4a+2b+3c\quad\text{subject to }a+b\geq3,\ a+c\geq2.
\]

The primal candidate \((x,y)=(2,2)\) has value \(10\), and dual candidate \((a,b,c)=(2,1,0)\) has value \(10\). Weak duality follows for any feasible choices:

\[
3x+2y\leq(a+b)x+(a+c)y=a(x+y)+bx+cy\leq4a+2b+3c.
\]

Thus both candidates are optimal. The direct certificate is \(3x+2y=2(x+y)+x\leq10\).

### A convex Lagrangian certificate

\[
\min_{x\geq4} f(x)=(x-3)^2+1,
\qquad g(x)=4-x\leq0.
\]

Lagrangian \(L(x,\lambda)=f(x)+\lambda g(x)\), \(\lambda\geq0\). The dual function is

\[
q(\lambda)=\inf_{x\in\mathbb R}L(x,\lambda)=1+\lambda-\frac{\lambda^2}{4}.
\]

At \(\lambda=2\), \(q(2)=2=f(4)\). Stationarity \(f'(4)+\lambda g'(4)=2-2=0\); complementary slackness \(\lambda g(4)=0\). This supplies an explicit saddle-point certificate.

### General principle and caveats

For minimization with \(g_i(x)\leq0\), \(\lambda_i\geq0\),
\[
q(\lambda)=\inf_x\left[f(x)+\sum_i\lambda_i g_i(x)\right]\leq\inf_{x\text{ feasible}}f(x).
\]

Weak duality requires no convexity. Equality of optimal primal/dual values needs additional hypotheses. KKT is sufficient for convex differentiable objectives/constraints with suitable sign convention when primal feasibility, dual feasibility, stationarity and complementary slackness all hold. Necessary KKT conditions generally need a constraint qualification.

### Exercises and answers

1. **Exercise:** Give a feasible production plan with value nine. **Answer:** \((x,y)=(1,3)\).
2. **Exercise:** Why does a dual bound of eleven not certify the value-ten candidate? **Answer:** It leaves a one-unit optimality gap.
3. **Exercise:** What changes if x and y must be integers? **Answer:** Linear relaxation still bounds the integer optimum, but a fractional relaxation optimum need not be feasible.
4. **Exercise:** Give an exact certificate for the constrained quadratic minimum. **Answer:** \(f(x)=(x-4)^2+2(x-4)+2\geq2\) for \(x\geq4\), with equality at four.

### References

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, https://web.stanford.edu/~boyd/cvxbook/
- George B. Dantzig, oral-history interview, INFORMS, https://www.informs.org/Explore/History-of-O.R.-Excellence/Oral-Histories/George-Dantzig
- George B. Dantzig, “Origins of the Simplex Method,” Computer History Museum archive.
- Dimitris Bertsimas and John N. Tsitsiklis, *Introduction to Linear Optimization*, Athena Scientific (1997).
