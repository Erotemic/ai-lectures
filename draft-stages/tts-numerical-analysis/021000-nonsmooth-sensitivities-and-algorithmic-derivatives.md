# 021000 — Nonsmooth Sensitivity: What a Derivative Can and Cannot Tell You

**Track:** Numerical Analysis. **Background:** automatic differentiation, constrained optimization, projections, implicit functions and generalized derivatives. **Central question:** what happens when a numerical algorithm changes branches or its optimum moves across a constraint boundary?

<!-- BEGIN SPOKEN LECTURE -->

# A program can return a number without having a derivative

Automatic differentiation lets us differentiate a program by composing derivatives of its elementary operations. On a smooth computational graph, it can produce an exact derivative up to floating-point arithmetic. But many useful numerical algorithms contain comparisons, projections, maximum operations, stopping rules, and active constraints. Their outputs may be continuous without being differentiable everywhere.

Imagine a simple optimization problem. We want to minimize the square of the difference between a decision x and a parameter theta, but x is constrained to be nonnegative. If theta is positive, the best x equals theta. If theta is negative, the best x is zero. The solution map is the maximum of theta and zero.

Every value of theta has a perfectly well-defined optimizer. But the optimizer map has a corner at zero. Its derivative is zero for negative theta and one for positive theta. At zero there is no ordinary derivative: the left and right slopes disagree.

Now suppose we write an optimizer in software and differentiate through it. A typical automatic differentiation system follows the branch chosen by the program. At theta equal to zero, it might report the derivative associated with one branch, or a conventional derivative assigned to the maximum operation. This number can be useful computationally, but it is not the unique classical derivative of the underlying mathematical map, because no such derivative exists there.

# Directional derivatives reveal the corner

The correct local question at a kink may be directional. Starting at theta equal to zero, perturb it in a direction h by a small positive step. If h is positive, the optimizer increases with rate h. If h is negative, the optimizer remains at zero, with rate zero. So the directional derivative at zero is the maximum of h and zero.

Notice that this response is not linear in h. A classical Fréchet derivative must be a linear map. The directional response can exist in every direction yet still fail to assemble into an ordinary Jacobian.

There are generalized derivative concepts that capture such behavior. For a locally Lipschitz scalar function, the Clarke generalized gradient is the convex hull of limiting ordinary gradients at nearby differentiability points. In the maximum example, the Clarke generalized derivative at zero is the entire interval from zero to one.

This generalized object is not a license to pick an arbitrary number and claim all smooth chain rules hold unchanged. Generalized chain rules usually involve inclusions or additional regularity assumptions, and a chosen computational derivative may describe only one branch.

# Soft-thresholding is another transparent example

Earlier in Optimization we encountered the proximal operator of the absolute-value penalty. It is the soft-thresholding function: values whose magnitude is below a threshold go to zero, while larger magnitudes move toward zero by the threshold amount.

Away from the two threshold points, the derivative with respect to its input is either zero or one. At the thresholds, the slope changes abruptly. This simple function appears in sparse regression, denoising, and proximal algorithms.

If we differentiate a solver that repeatedly applies soft thresholding, the derivative may depend on which coefficients are active. On a region where the active set is stable, we can often differentiate the corresponding smooth system. Near an active-set transition, the derivative may jump or cease to exist.

# Implicit differentiation has hypotheses

Consider a smoothly parameterized equation F of x and theta equals zero. If the Jacobian of F with respect to x is invertible at a solution, the implicit function theorem gives a differentiable local solution branch. The sensitivity of x is obtained by solving a linear system involving the two Jacobians.

That method is powerful because it avoids differentiating through every iteration of a numerical solver. But the invertibility and smoothness assumptions matter. An active constraint can make a naive Jacobian singular or cause the relevant equation system to change as theta varies.

For constrained optimization, we may differentiate the Karush–Kuhn–Tucker conditions, provided suitable constraint qualification, second-order regularity, and active-set stability conditions hold. Strict complementarity is one common sufficient ingredient in many formulations, not a universal requirement of differentiability.

If these conditions fail, we should investigate directional derivatives, generalized Jacobians, piecewise-smooth solution maps, or a reformulation that preserves the desired sensitivities.

# Finite differences are not automatically a rescue

A natural fallback is to perturb theta numerically and estimate the derivative with a difference quotient. Away from the kink this works as usual if the step is chosen appropriately and solver error is controlled. At the kink, however, one-sided differences give different answers. A symmetric difference produces the average slope in the maximum example, one half. That number is not the classical derivative, and changing the finite-difference convention changes the result.

There is also an interaction between perturbation size and numerical accuracy. If the solver's optimality error is comparable to the effect of the parameter perturbation, the difference quotient may amplify solver noise by dividing it by a very small step. A numerical sensitivity estimate is credible only when both mathematical nonsmoothness and numerical error are addressed.

# Stopping rules create additional branches

Even an iterative algorithm built from smooth arithmetic can be nonsmooth as a function of its inputs if it stops when a residual drops below a tolerance. A tiny parameter change might increase the iteration count by one, producing a small but abrupt change in the returned approximation. Differentiating the fixed number of iterations used on one run is not automatically the derivative of the full 'iterate until converged' algorithm.

If the goal is the derivative of the mathematical solution, implicit differentiation of the defining equations may be preferable when justified. If the goal is the derivative of a fixed computational procedure, differentiating through that procedure may be exactly right. The two questions should not be confused.

# A practical hierarchy of sensitivity claims

For a numerical result depending on a parameter, first ask whether the mathematical solution map is differentiable. If it is, check which theorem or calculation supplies the derivative. Next determine whether the implemented algorithm approximates the solution and derivative accurately enough. Finally, identify nondifferentiable events: projections, changes of active set, root multiplicities, mesh changes, or stopping decisions.

This hierarchy separates several different objects: the derivative of an exact solution, a generalized derivative at a kink, a derivative of a finite sequence of algorithmic steps, and a finite-difference estimate contaminated by solver error. Each can be useful. Problems arise when we report one as though it were another.

The central lesson is that differentiable programming is not the same as making mathematics smooth. Automatic differentiation is a powerful tool, but its output inherits the analytical conditions and branch structure of the computation being differentiated.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Consider
\[
x^*(\theta)=\arg\min_{x\ge0}\frac12(x-\theta)^2
=\max(0,\theta).
\]
For `theta<0`, `dx*/dtheta=0`; for `theta>0`, `dx*/dtheta=1`. At `theta=0`, the classical two-sided derivative does not exist. The directional derivative in direction h is
\[
D x^*(0;h)=\max(0,h),
\]
which is not a linear function of h. The Clarke generalized derivative at zero is `[0,1]`, while the B-subdifferential comprises the limiting branch slopes `{0,1}`.

The soft-threshold map for `lambda>0` is
\[
\operatorname{prox}_{\lambda|\cdot|}(z)
=\operatorname{sign}(z)\max(|z|-\lambda,0).
\]
Its derivative is zero when `|z|<lambda`, one when `|z|>lambda`, and does not exist at `z=+-lambda` as a classical two-sided derivative.

For a smooth equation `F(x,theta)=0` with invertible `F_x`, the implicit function theorem gives
\[
\frac{dx^*}{d\theta}=-(F_x)^{-1}F_\theta.
\]
This does not justify the same formula at a singular Jacobian or at an active-set switch without additional analysis. Finite differences at the ReLU kink satisfy
\[
\lim_{h\downarrow0}\frac{x^*(h)-x^*(0)}h=1,\quad
\lim_{h\downarrow0}\frac{x^*(0)-x^*(-h)}h=0,
\]
and the centered quotient gives `1/2` for every positive h, demonstrating convention dependence.

### Exercises with answers

1. At theta zero, what is the directional derivative of `max(theta,0)` in direction `-2`? **Answer:** zero.
2. What is the Clarke generalized derivative of the same map at zero? **Answer:** the interval `[0,1]`.
3. When can the smooth implicit sensitivity formula be applied directly? **Answer:** when the defining map is differentiable and the relevant Jacobian with respect to the unknown is invertible.
4. What is wrong with interpreting an AD-chosen branch slope at a kink as the unique mathematical derivative? **Answer:** the ordinary derivative does not exist there, and a branch convention is only one selected generalized response.

### Reading and source notes

- [The Elements of Differentiable Programming, Differentiation](https://diffprog.github.io/diff.html), generalized Jacobians and algorithmic derivatives.
- [Khan and Barton, A Vector Forward Mode of Automatic Differentiation for Generalized Derivative Evaluation](https://doi.org/10.1080/10556788.2015.1025400), nonsmooth generalized derivatives.
- [Clarke, Optimization and Nonsmooth Analysis](https://doi.org/10.1137/1.9781611971309), generalized gradients and nonsmooth calculus.
