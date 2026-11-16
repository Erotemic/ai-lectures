# 018000 — Inexact Proximal Algorithms: Convergence When Inner Solves Are Imperfect

**Track:** Optimization and Duality. **Background:** convex composite optimization, proximal maps, first-order conditions and convergence estimates. **Central question:** how much error can we tolerate when each optimization step is itself solved approximately?

<!-- BEGIN SPOKEN LECTURE -->

# An optimization algorithm may contain another optimization problem

Proximal algorithms are useful because they separate two kinds of structure. We may have a smooth objective whose gradient is easy to calculate, and a nonsmooth penalty whose proximal operator is easy to evaluate. A proximal-gradient step first moves in the negative gradient direction, then solves a small regularized optimization problem to incorporate the nonsmooth penalty.

For an absolute-value penalty, the proximal operator is soft thresholding, which has a closed formula. But for more complicated penalties or constraints, the proximal subproblem may require its own iterative solver. Then each outer iteration depends on an approximate inner solution. The mathematical algorithm asks for an exact proximal point, but the computer returns one with residual error.

Does the outer algorithm still converge? There is no single answer independent of how the error is measured. We need to distinguish an error in the returned point, an error in the subproblem objective, and a residual in its first-order optimality condition. These are not interchangeable without assumptions.

# The exact step as a reference point

Consider an objective made of a smooth convex part and a proper closed convex penalty. Assume the smooth part has a Lipschitz-continuous gradient. For a sufficiently small step size, the exact proximal-gradient update decreases the objective and moves toward a minimizer, under the usual existence assumptions.

The proximal operator minimizes the penalty plus a quadratic distance from the gradient step. That quadratic term makes the proximal subproblem strongly convex, so the proximal point is unique. The update balances the local linear approximation of the smooth function against the exact nonsmooth penalty.

There is also a natural stationarity measure called the proximal-gradient mapping. It is the current point minus its exact proximal-gradient update, divided by the step size. This mapping vanishes precisely when the first-order optimality condition for the convex composite objective is satisfied.

Thus an exact update provides both a descent step and a way to assess convergence. If we approximate the update, we must also quantify how far the reported stationarity measure might be from the true one.

# A simple example with a known answer

Take a one-dimensional smooth objective equal to half the square of x minus three, and add the absolute value of x with coefficient one. The exact minimizer is x equals two. For a unit step size, the gradient move always lands at three, regardless of the previous iterate. The proximal map soft-thresholds three by one and returns two.

Now imagine an inner solver returns two point zero zero one instead. The objective value is only slightly above optimal. The first-order stationarity residual is also small: the smooth derivative at that point is approximately minus zero point nine nine nine, while the derivative of the absolute value penalty is one. Their sum is zero point zero zero one.

This is a simple instance where we can compute the error exactly. In a large problem, we may not know the true minimizer, so we should try to calculate a verifiable inner residual or a bound on the distance from the true proximal point.

# Absolute summability and accumulated error

A common convergence principle is that errors which are absolutely summable can be absorbed into the analysis of a nonexpansive or averaged iteration. If the sum of the sizes of the errors over all iterations is finite, their total accumulated disturbance is controlled.

For exact proximal point iterations and closely related firmly nonexpansive maps, summable perturbations permit useful convergence theorems under appropriate assumptions, including existence of fixed points. In finite-dimensional convex composite settings, one can obtain related results for inexact proximal-gradient methods, but additional conditions may be needed depending on whether the error is measured as a point perturbation, a subproblem residual, or an objective tolerance.

The phrase 'the error goes to zero' is weaker than summability. An error of size one divided by the square root of the iteration count tends to zero but its sum diverges. Some algorithms still converge under weaker conditions, but that requires a different theorem. We should not simply assert that any vanishing inner tolerance is sufficient.

# Why feasibility matters

Suppose the nonsmooth penalty is the indicator of a constraint set. It is zero for feasible points and infinite for infeasible points. The exact proximal operator becomes a projection onto that set.

An approximate point may be close to the projection in Euclidean distance yet lie just outside the constraint set. Reporting it as though it were a valid optimization iterate can make the objective undefined or infinite. So a pointwise approximation guarantee alone may not preserve feasibility.

An implementer should either require a feasible approximate proximal point or use a theorem explicitly designed for infeasible or approximate projections. In constrained problems, the distance to feasibility and the stationarity residual serve different purposes. Both may be needed.

# Stopping criteria and certificates

Suppose a numerical solver reports that its update is very small. That is not by itself a proof of near-optimality. A small step can arise from a genuinely near-stationary point, but also from a poorly solved proximal subproblem, a tiny step size, or a numerical failure.

A better diagnostic evaluates the proximal-gradient mapping, or an upper bound on its norm if the proximal operator was approximated. For convex objectives, an actual first-order stationarity residual has a clear interpretation. With stronger assumptions such as strong convexity, we may convert a residual bound into a distance or objective-gap estimate. Without those assumptions, a residual norm is not necessarily a numerical upper bound on the global objective gap.

It is also useful to distinguish a theorem of asymptotic convergence from a finite stopping certificate. Convergence says what happens if we continue the algorithm indefinitely under the stated error conditions. A stopping certificate justifies a claim about the finite approximate solution we currently hold. These are different questions.

# Choosing the inner accuracy schedule

In practice, there is a tradeoff. Solving every proximal subproblem to extreme accuracy wastes work early, when the outer iterate is still far from the optimum. Solving them too crudely late may prevent further progress.

An adaptive approach asks for coarse inner solves at first and tighter solves as the outer stationarity measure falls. But any rigorous complexity or convergence guarantee must connect the schedule to a precise error model. We can use certificates from the inner solver, such as primal-dual gaps or optimality residuals, to make this connection explicit.

The main lesson is a disciplined separation of levels. The outer objective has a mathematical minimizer. The exact proximal algorithm has an ideal update. The inner numerical routine returns an approximation to that update. Each arrow between these objects needs an error estimate. Once those estimates are explicit, inexact proximal methods become analyzable rather than a matter of trusting a solver's iteration count.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let `F=f+g`, with f convex differentiable and `L`-Lipschitz gradient, and g proper, lower semicontinuous and convex. The proximal-gradient update for `0<alpha<=1/L` is
\[
z=T_\alpha(x):=\operatorname{prox}_{\alpha g}(x-\alpha\nabla f(x)),
\quad G_\alpha(x)=\frac{x-T_\alpha(x)}\alpha.
\]
Optimality of z gives `0 in partial g(z)+nabla f(x)+(z-x)/alpha`. Since g is convex and f is L-smooth, one obtains
\[
F(z)\le F(x)-\left(\frac1\alpha-\frac L2\right)\|z-x\|^2,
\]
when the function values are finite. `G_alpha(x)=0` if and only if `0 in nabla f(x)+partial g(x)`; for convex F, this is the global optimality condition.

If an approximate point `z_tilde` satisfies `||z_tilde-z||<=epsilon`, then the approximate mapping `G_tilde=(x-z_tilde)/alpha` obeys the certified comparison
\[
\|G_\alpha(x)-\widetilde G_\alpha(x)\|\le\epsilon/\alpha.
\]
A small `||G_tilde||` is only meaningful if epsilon is controlled. If g is an indicator, arbitrary point errors do not imply feasibility. A residual in the proximal optimality inclusion is a different error model from `||z_tilde-z||` and needs its own conversion theorem.

**Exact example.** `f(x)=(x-3)^2/2`, `g(x)=|x|`, `alpha=1`. For any x, `x-alpha f'(x)=3`, hence `T_1(x)=soft(3,1)=2`, the minimizer. At `x=2.001`, `f'(x)+g'(x)=x-3+1=0.001`.

With inexact nonexpansive fixed-point iterations, absolute summability `sum_k ||e_k||<infinity` is a common sufficient hypothesis in convergence theorems. Whether the same conclusion holds for a particular inexact proximal-gradient implementation depends on the exact iteration, domain, and error model. An `epsilon_k->0` condition by itself is not generally a substitute for a correct theorem.

### Exercises with answers

1. If an approximate proximal point has error at most `10^-4` and `alpha=0.1`, how far can its gradient mapping be from the exact one? **Answer:** at most `10^-3` in norm.
2. Does an infeasible point close to a projection automatically have finite indicator-penalty objective? **Answer:** no.
3. What does `G_alpha(x)=0` mean for a convex composite problem? **Answer:** the convex first-order optimality condition holds, so x minimizes F.
4. Is `epsilon_k->0` identical to `sum epsilon_k<infinity`? **Answer:** no; for example `epsilon_k=1/sqrt(k)` tends to zero but is not summable.

### Reading and source notes

- [Parikh and Boyd, Proximal Algorithms](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf), proximal operators, splitting and convergence.
- [Schmidt, Le Roux, and Bach, Convergence Rates of Inexact Proximal-Gradient Methods for Convex Optimization](https://arxiv.org/abs/1109.2415), explicit inexactness models and rates.
- [Beck and Teboulle, A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems](https://doi.org/10.1137/080716542), composite proximal-gradient methods and rates.
