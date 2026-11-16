# 011000 — Optimization Sensitivity: Perturbation Bounds and Shadow Prices

**Track:** Optimization, Convexity, and Duality. **Background:** convex programs, Lagrange multipliers, KKT conditions, duality and interior-point methods. **Central question:** what can a dual solution tell us about how the optimal value changes when constraints are perturbed?

<!-- BEGIN SPOKEN LECTURE -->

# Optimization Sensitivity: Perturbation Bounds and Shadow Prices

Suppose we have solved an optimization problem: minimize cost while satisfying a collection of resource limits. Now a customer offers to relax one limit slightly, or a regulator tightens it. How much should the optimal cost change? Do we need to solve the entire problem again to answer that question?

Convex duality offers an elegant first answer. The multipliers associated with constraints do more than certify optimality. Under the right conditions, they measure the sensitivity of the optimal value to changes in those constraints. But sensitivity is a local or bounded statement about a mathematically specified perturbation, not a license to treat every multiplier as a constant market price for arbitrary changes.

## Build a perturbed problem

Begin with a convex minimization problem. Let the objective be f zero of x. Let its inequality constraints be f i of x at most zero, and its equality constraints be h j of x equal to zero, with the equality functions affine.

Introduce parameters u and v. Replace each inequality bound zero with u i, and each equality bound zero with v j. The optimal value now becomes a function of these perturbations, called p star of u and v.

Positive u means relaxing an inequality: a constraint of the form f i of x at most u i admits a larger feasible set. Thus, if only one inequality is relaxed, the minimum cost cannot increase. A negative u tightens it and may raise cost or destroy feasibility. Equality perturbations are not naturally ordered in the same way.

This simple definition matters. The sign and interpretation of a multiplier depend on how the constraints were written. A resource lower bound, written as a negative inequality, gives the opposite apparent sign from a resource upper bound. Always return to the actual perturbation convention before interpreting a shadow price.

## Dual variables produce an affine bound

The Lagrangian adds each inequality violation, multiplied by a nonnegative multiplier lambda, and each equality residual multiplied by an unrestricted multiplier nu. When the right-hand sides shift to u and v, the Lagrangian picks up an additional constant: negative lambda dotted with u, minus nu dotted with v.

Assume the original problem has strong duality and an attained optimal dual solution, lambda star and nu star. Keep these multipliers fixed while we perturb the constraints. The resulting dual objective gives a lower bound on the perturbed primal optimum. That lower bound is the original optimal value minus lambda star dotted with u, minus nu star dotted with v.

This is a global affine lower bound on the perturbed optimal-value function, wherever that value is defined in the extended-real sense. It tells us how much improvement a relaxation can possibly buy relative to a known dual certificate. But by itself it is not an exact prediction of the new optimum.

## Sensitivity as a derivative

If the optimal-value function is differentiable at zero perturbation, the same multipliers identify its derivative. The partial derivative with respect to an inequality bound u i is negative lambda i star. The derivative with respect to an equality right-hand side v j is negative nu j star.

This is the mathematical meaning of a shadow price. A positive inequality multiplier describes the first-order decrease in cost as the corresponding upper bound is relaxed. If the constraint is inactive and standard complementary slackness applies, the multiplier is zero: a small relaxation of an already slack constraint does not provide immediate value through that multiplier.

If the value function is not differentiable, an optimal dual multiplier may still define a subgradient of the convex perturbation-value function, with a negative sign. Different optimal multipliers can encode different supporting slopes. In that case asking for a unique derivative may be the wrong question.

## A complete one-variable example

Minimize x squared subject to x being at least one. The optimal solution is x equal to one and the optimal value is one. Write the constraint as one minus x at most zero. The Lagrangian is x squared plus lambda times one minus x, where lambda must be nonnegative.

The stationarity condition requires twice x minus lambda to be zero. At the optimum x equals one, so lambda equals two. This multiplier predicts that relaxing the inequality upper bound by a small positive amount u reduces the optimal value at first order by two times u.

Check directly. The perturbed constraint is one minus x at most u, or x at least one minus u. For sufficiently small u, the new minimizer is one minus u, so the optimal value is one minus u, squared. Expand: one minus twice u plus u squared. The derivative at zero is negative two, exactly the negative of the multiplier.

We can also see why the multiplier is not an exact price for large changes. If u reaches one, the point x equal to zero becomes feasible, and the optimal cost becomes zero. Relaxing beyond that does not reduce it further. The linear prediction would keep decreasing without bound, which is impossible here. The affine inequality remains a valid lower bound; the first-order approximation has stopped being accurate.

## The optimal point can be much less stable than the value

Sensitivity of the optimal value is different from sensitivity of the optimizer itself. Consider minimizing a shallow quadratic: epsilon over two times x squared, minus b times x, where epsilon is a small positive number and b is a parameter. The minimizer is b divided by epsilon.

Change b by a small amount delta. The minimizer moves by delta divided by epsilon. If epsilon is tiny, even a modest input perturbation can move the optimizer dramatically. The objective is strictly convex and has a unique minimum, yet the location of that minimum is poorly conditioned with respect to the linear coefficient.

This is not a failure of convexity. Strict convexity guarantees uniqueness in this simple example. Strong curvature, or an appropriate second-order growth condition, is what provides quantitative stability. A small duality gap alone also does not guarantee an accurate optimizer when the objective is nearly flat.

## Constraints can change their active set

Real optimization problems often have multiple competing constraints. A small change may cause a previously inactive constraint to become active, or make an active one slack. Near such a transition, the value function can have a kink. Multipliers may fail to be unique, and derivatives may need to be replaced with directional derivatives or subgradients.

Constraint qualifications matter as well. Strong duality, dual attainment, and regularity are conditions to check, not assumptions to smuggle in because a numerical solver returned a vector called a multiplier. Degenerate constraints can give misleadingly large or nonunique multipliers even when the underlying optimal value is well behaved.

For numerical work, complementarity residuals, primal feasibility, dual feasibility, and conditioning must all be considered before attaching an economic interpretation to computed shadow prices. Units and scaling matter: doubling the units in which a constraint is measured changes the numerical multiplier inversely.

## Turning optimization output into useful knowledge

The dual certificate supplies a global inequality for the value of nearby or distant perturbed problems. Differentiability turns a multiplier into an exact first-order sensitivity. Strong curvature and regularity can make the optimizer stable as well. Without these additional hypotheses, a solver's reported multiplier is a potentially useful diagnostic, not an unconditional forecast.

This is how duality extends beyond proving that one solution is optimal. It can tell us what a small relaxation is worth, which constraints are binding, and where a computation is sensitive to uncertain input. The essential discipline is to distinguish a rigorous supporting bound, a local derivative, and an extrapolated prediction. They answer different questions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a convex optimization problem with convex \(f_0,f_i\) and affine \(h_j\), define the perturbed value
\[p^\star(u,v)=\inf_x\{f_0(x):f_i(x)\le u_i,\ h_j(x)=v_j\}.\]
The Lagrangian is
\[L(x,\lambda,\nu;u,v)=f_0(x)+\sum_i\lambda_i(f_i(x)-u_i)+\sum_j\nu_j(h_j(x)-v_j),\quad\lambda\ge0.\]
If \(p^\star(0,0)\) is finite and the unperturbed dual optimum is attained at \((\lambda^\star,\nu^\star)\) with zero duality gap, weak duality with the same multipliers for perturbed data yields
\[p^\star(u,v)\ge p^\star(0,0)-\lambda^{\star T}u-\nu^{\star T}v.\]
Thus \((-\lambda^\star,-\nu^\star)\) is a subgradient of the convex value function at zero (where the latter is proper); if differentiable there, \(\nabla p^\star(0,0)=(-\lambda^\star,-\nu^\star)\).

**One-dimensional example:** minimize \(x^2\) subject to \(1-x\le u\). For \(u<1\), \(x^\star(u)=1-u\) and \(p^\star(u)=(1-u)^2\); for \(u\ge1\), the optimum is \(x=0\) and \(p^\star(u)=0\). At \(u=0\), \(\lambda^\star=2\), \(\frac{d}{du}p^\star(0)=-2\), and the global supporting line is \(p^\star(u)\ge1-2u\). The exact change has a quadratic correction for small \(u\), and extrapolation past the active-set change is inaccurate.

**Conditioning example:** for \(\varepsilon>0\), \(f(x;b)=\tfrac\varepsilon2x^2-bx\) has \(x^\star(b)=b/\varepsilon\). Parameter sensitivity \(\partial x^\star/\partial b=1/\varepsilon\) diverges as curvature \(\varepsilon\downarrow0\). Uniqueness alone does not imply numerical robustness.

### Exercises with answers

1. With the convention \(f_i(x)\le u_i\), what sign does a nonnegative inequality multiplier give for the derivative of optimal value with respect to \(u_i\)? **Answer:** \(-\lambda_i^\star\), if the value function is differentiable and regularity assumptions hold.
2. Compute the new optimum for the one-variable example at \(u=1/2\). **Answer:** \(x^\star=1/2\), \(p^\star=1/4\); the linear lower bound is \(0\), so it is valid but not exact.
3. Does strict convexity alone guarantee that an optimizer changes little under parameter perturbations? **No:** the shallow quadratic has sensitivity \(1/\varepsilon\).
4. What does a nonunique optimal multiplier imply about interpreting one reported shadow price? **Answer:** differentiability and a unique sensitivity have not been established; consider subgradients and constraint degeneracy.

### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*, Section 5.6 on perturbation and sensitivity](https://web.stanford.edu/~boyd/cvxbook/), dual lower bounds and local multiplier sensitivity.
- Stanford EE364A, [Convex Optimization course resources](https://web.stanford.edu/class/ee364a/), KKT and perturbation theory.
- [JuMP documentation: Tolerances and numerical issues](https://jump.dev/JuMP.jl/stable/tutorials/getting_started/tolerances/), numerical qualifications when reading solver certificates.
