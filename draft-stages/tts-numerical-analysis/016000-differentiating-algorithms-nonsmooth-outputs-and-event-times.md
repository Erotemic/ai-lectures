# Differentiating algorithms, nonsmooth outputs, and event times

<!-- BEGIN SPOKEN LECTURE -->

# Differentiating algorithms, nonsmooth outputs, and event times

## Automatic Differentiation and Adjoint Sensitivity

A numerical model may involve millions of arithmetic operations. Perhaps it solves a fluid equation, fits a physical parameter, or predicts the output of a complicated network. Now suppose we want to know how its final answer changes when one input parameter changes. We could rerun the model after nudging the input. But repeated perturbations may be expensive, inaccurate, or numerically unstable. Automatic differentiation offers another approach: differentiate the computation itself.

The key point is that a complicated numerical program is composed of elementary operations. If we know the derivative rule for each operation, the chain rule can propagate derivative information through the entire computation. We do not need to invent a new symbolic formula for the whole program, nor approximate the derivative by subtracting two nearly equal outputs.

### Forward differentiation follows the calculation

Imagine a computation as a sequence of intermediate variables. Each variable is produced from earlier ones by addition, multiplication, division, or a smooth elementary function. Forward-mode automatic differentiation carries an ordinary value and a directional derivative together through those operations.

For multiplication, the derivative follows the product rule. For sine, it follows the cosine rule. A convenient mathematical model is a dual number: an ordinary scalar plus a small formal component whose square is zero. Multiplying dual numbers automatically enforces the first-order product rule, because all terms involving the square of that formal component disappear exactly.

This is not the same as evaluating a function with a tiny numerical perturbation. The formal component is bookkeeping for the derivative, not a floating-point step size to be chosen. Forward mode computes a Jacobian-vector product: it tells us how the outputs vary in one specified input direction.

If there are only a few input parameters and many outputs, forward mode can be very effective. We propagate one direction at a time, or a collection of directions in parallel, without constructing a symbolic derivative expression.

### Reverse differentiation follows the dependence backward

Suppose instead there are a million inputs but only one scalar objective. Running forward mode once per input would be wasteful. Reverse mode takes advantage of the fact that all inputs contribute to the same final scalar.

First evaluate the program normally, recording or reconstructing the intermediate values needed for derivatives. Then propagate sensitivity backward from the final scalar. At an addition node, the incoming derivative contributes to both inputs. At a multiplication node, the derivative passed to either input is multiplied by the other input's forward value. The derivative contributions from different downstream paths are accumulated.

This is reverse-mode automatic differentiation, also called backpropagation in many machine-learning settings. Its computational cost for a scalar output is often a small multiple of the original evaluation, rather than a multiple proportional to the number of input variables. The tradeoff is storage or recomputation: the backward pass needs information from the forward calculation.

Take a small example. Let the objective equal x squared times y plus sine of x times y. To compute it, form x squared, multiply by y, form x times y, take its sine, and add the two branches. Reverse accumulation returns the partial derivative with respect to x as twice x times y plus y times the cosine of x times y. The derivative with respect to y is x squared plus x times that same cosine. Every term follows from a local chain-rule operation on the computation graph.

The example may look easy enough to differentiate by hand, but the point is that the same algorithm scales to graphs containing thousands or millions of such operations.

### Differentiating a solved equation

Many scientific computations are not explicit formulas. They solve an equation, such as a linear system, and use the solution in an objective. It is possible to differentiate every iteration of the chosen solver. But often a more stable and efficient route is to differentiate the equation defining the exact solution.

Suppose a parameter theta determines a nonsingular matrix A and a right-hand side b, and the state u solves A times u equals b. Differentiating the equation gives the derivative of A times u, plus A times the derivative of u, equal to the derivative of b. Rearranging, the state derivative is the solution of another linear system with the same matrix A.

If theta has many components, solving one such sensitivity system per component may again be expensive. Instead, suppose the output we care about is a scalar objective depending on u and possibly theta directly. Introduce an adjoint vector by solving the transposed linear system with the derivative of the objective with respect to u on the right-hand side.

Once we have this adjoint, the derivative of the scalar objective with respect to theta can be computed by pairing the adjoint with the derivative of b minus the derivative of A applied to u, then adding any direct dependence of the objective on theta. One adjoint solve can support sensitivities with respect to many parameters.

This is the same reverse accumulation principle at the level of an implicit numerical model. Rather than propagating all parameter variations forward, we propagate the influence of the scalar objective backward through the governing equation.

### A concrete optimization setting

Suppose a heat-transfer model depends on a conductivity parameter, and the objective measures the mismatch between predicted temperatures and sensor readings. The forward solve computes the temperature field. The adjoint solve computes how the mismatch responds to perturbations of the field. The conductivity gradient is then obtained by combining the forward and adjoint fields with the derivative of the discretized operator.

There are two distinct derivatives here. One is the derivative of the finite-dimensional discretized problem actually solved by the computer. The other is the derivative of the underlying continuum model. If we differentiate the discrete system, the result may be accurate for that discretization while still differing from the continuum sensitivity. Refining the mesh, checking consistency, and analyzing numerical errors remain necessary.

### The pitfalls are mathematical, not only computational

Automatic differentiation computes derivatives of the executed differentiable operations. It does not make a nondifferentiable program differentiable. A branch that changes abruptly, a maximum with a tie, a pivot choice, an iteration stopping criterion, or a change in the active set of an optimization problem may create discontinuities or derivative conventions that require careful interpretation.

Similarly, an implicit differentiation formula assumes the matrix or Jacobian being inverted is nonsingular. Near a singular point, sensitivities may become enormous. This is genuine conditioning, not an error caused by automatic differentiation. A correct algorithm can accurately report an extremely sensitive problem.

Memory is another practical issue. Reverse mode may need intermediate values from a very long calculation. Checkpointing trades extra recomputation for less storage. For time-dependent models, an adjoint calculation may run backward through the history while reconstructing forward states as needed. That requires deliberate numerical design, especially for chaotic or highly unstable dynamics.

### Why derivatives are now part of the model

Finite differences ask what happens after we change an input and rerun the model. Automatic differentiation follows the chain rule through the model's operations. Adjoint methods exploit the structure of an implicit equation to compute many parameter sensitivities from a small number of linearized solves.

Together, these techniques make gradients accessible for large simulations, inverse problems, and optimal control. But they do not remove the need to distinguish an implemented function from a continuous mathematical model, or numerical stability from differentiability. The best use of automatic differentiation is to combine exact chain-rule structure with the same conditioning and error analysis we apply to every serious numerical algorithm.

## Nonsmooth Sensitivity: What a Derivative Can and Cannot Tell You

Automatic differentiation lets us differentiate a program by composing derivatives of its elementary operations. On a smooth computational graph, it can produce an exact derivative up to floating-point arithmetic. But many useful numerical algorithms contain comparisons, projections, maximum operations, stopping rules, and active constraints. Their outputs may be continuous without being differentiable everywhere.

Imagine a simple optimization problem. We want to minimize the square of the difference between a decision x and a parameter theta, but x is constrained to be nonnegative. If theta is positive, the best x equals theta. If theta is negative, the best x is zero. The solution map is the maximum of theta and zero.

Every value of theta has a perfectly well-defined optimizer. But the optimizer map has a corner at zero. Its derivative is zero for negative theta and one for positive theta. At zero there is no ordinary derivative: the left and right slopes disagree.

Now suppose we write an optimizer in software and differentiate through it. A typical automatic differentiation system follows the branch chosen by the program. At theta equal to zero, it might report the derivative associated with one branch, or a conventional derivative assigned to the maximum operation. This number can be useful computationally, but it is not the unique classical derivative of the underlying mathematical map, because no such derivative exists there.

## Directional derivatives reveal the corner

The correct local question at a kink may be directional. Starting at theta equal to zero, perturb it in a direction h by a small positive step. If h is positive, the optimizer increases with rate h. If h is negative, the optimizer remains at zero, with rate zero. So the directional derivative at zero is the maximum of h and zero.

Notice that this response is not linear in h. A classical Fréchet derivative must be a linear map. The directional response can exist in every direction yet still fail to assemble into an ordinary Jacobian.

There are generalized derivative concepts that capture such behavior. For a locally Lipschitz scalar function, the Clarke generalized gradient is the convex hull of limiting ordinary gradients at nearby differentiability points. In the maximum example, the Clarke generalized derivative at zero is the entire interval from zero to one.

This generalized object is not a license to pick an arbitrary number and claim all smooth chain rules hold unchanged. Generalized chain rules usually involve inclusions or additional regularity assumptions, and a chosen computational derivative may describe only one branch.

## Soft-thresholding is another transparent example

Earlier in Optimization we encountered the proximal operator of the absolute-value penalty. It is the soft-thresholding function: values whose magnitude is below a threshold go to zero, while larger magnitudes move toward zero by the threshold amount.

Away from the two threshold points, the derivative with respect to its input is either zero or one. At the thresholds, the slope changes abruptly. This simple function appears in sparse regression, denoising, and proximal algorithms.

If we differentiate a solver that repeatedly applies soft thresholding, the derivative may depend on which coefficients are active. On a region where the active set is stable, we can often differentiate the corresponding smooth system. Near an active-set transition, the derivative may jump or cease to exist.

## Implicit differentiation has hypotheses

Consider a smoothly parameterized equation F of x and theta equals zero. If the Jacobian of F with respect to x is invertible at a solution, the implicit function theorem gives a differentiable local solution branch. The sensitivity of x is obtained by solving a linear system involving the two Jacobians.

That method is powerful because it avoids differentiating through every iteration of a numerical solver. But the invertibility and smoothness assumptions matter. An active constraint can make a naive Jacobian singular or cause the relevant equation system to change as theta varies.

For constrained optimization, we may differentiate the Karush–Kuhn–Tucker conditions, provided suitable constraint qualification, second-order regularity, and active-set stability conditions hold. Strict complementarity is one common sufficient ingredient in many formulations, not a universal requirement of differentiability.

If these conditions fail, we should investigate directional derivatives, generalized Jacobians, piecewise-smooth solution maps, or a reformulation that preserves the desired sensitivities.

## Finite differences are not automatically a rescue

A natural fallback is to perturb theta numerically and estimate the derivative with a difference quotient. Away from the kink this works as usual if the step is chosen appropriately and solver error is controlled. At the kink, however, one-sided differences give different answers. A symmetric difference produces the average slope in the maximum example, one half. That number is not the classical derivative, and changing the finite-difference convention changes the result.

There is also an interaction between perturbation size and numerical accuracy. If the solver's optimality error is comparable to the effect of the parameter perturbation, the difference quotient may amplify solver noise by dividing it by a very small step. A numerical sensitivity estimate is credible only when both mathematical nonsmoothness and numerical error are addressed.

## Stopping rules create additional branches

Even an iterative algorithm built from smooth arithmetic can be nonsmooth as a function of its inputs if it stops when a residual drops below a tolerance. A tiny parameter change might increase the iteration count by one, producing a small but abrupt change in the returned approximation. Differentiating the fixed number of iterations used on one run is not automatically the derivative of the full 'iterate until converged' algorithm.

If the goal is the derivative of the mathematical solution, implicit differentiation of the defining equations may be preferable when justified. If the goal is the derivative of a fixed computational procedure, differentiating through that procedure may be exactly right. The two questions should not be confused.

## A practical hierarchy of sensitivity claims

For a numerical result depending on a parameter, first ask whether the mathematical solution map is differentiable. If it is, check which theorem or calculation supplies the derivative. Next determine whether the implemented algorithm approximates the solution and derivative accurately enough. Finally, identify nondifferentiable events: projections, changes of active set, root multiplicities, mesh changes, or stopping decisions.

This hierarchy separates several different objects: the derivative of an exact solution, a generalized derivative at a kink, a derivative of a finite sequence of algorithmic steps, and a finite-difference estimate contaminated by solver error. Each can be useful. Problems arise when we report one as though it were another.

The central lesson is that differentiable programming is not the same as making mathematics smooth. Automatic differentiation is a powerful tool, but its output inherits the analytical conditions and branch structure of the computation being differentiated.

## Event-Time Sensitivities and Saltation Matrices

Many simulations evolve smoothly until a condition becomes true. A ball hits the ground and reverses velocity. A controller switches modes when a threshold is crossed. A chemical process changes equations after a reaction stage. These are hybrid dynamical systems: continuous differential equations joined by discrete events.

A common numerical mistake is to differentiate the continuous evolution while treating the detected event time as a fixed constant. That can give a derivative that looks precise yet describes the wrong problem. Change an initial condition slightly, and the event happens at a slightly different time. The trajectory spends more or less time under each vector field. Its sensitivity contains a correction for that timing shift.

This lesson matters for optimal control, parameter estimation, inverse problems, and differentiable simulation. An event detector is not merely an implementation detail. Its root defines part of the mathematical map whose derivative we want.

## Events are roots of a moving equation

Consider a state x evolving under an ordinary differential equation that depends on a parameter theta. An event occurs when a scalar guard function of the state, parameter, and time reaches zero. Let tau denote the first relevant crossing time.

A small parameter change perturbs the trajectory. The event location moves because the guard is evaluated along the changed trajectory. Differentiate the guard equation with respect to theta. The total derivative contains the direct parameter derivative of the guard, the derivative of the state at a fixed time, and the vector field multiplied by the derivative of the event time.

Solving this linear equation gives the event-time derivative. Its denominator is the rate at which the guard changes along the unperturbed trajectory. If that rate is nonzero, the crossing is transverse, and the implicit function theorem gives a locally smooth event-time function.

If the rate is zero, the trajectory grazes the event surface. Then the denominator vanishes and first-order event sensitivity may fail. The solution may touch without crossing, or the number and order of events may change under arbitrarily small perturbations. No amount of numerical precision can justify applying the transverse formula at an actual grazing point.

## A falling ball makes the derivative visible

Drop a ball from height twenty under a constant downward acceleration of ten, starting from rest. In idealized units, the height falls quadratically in time. It reaches the ground after two time units.

Differentiate the impact time with respect to release height. The derivative is one over acceleration times the impact time. Here it is one twentieth of a time unit per unit height. A small increase in height delays the impact, even before we consider what happens to the velocity after the bounce.

At impact, the downward velocity has magnitude twenty. A restitution rule reverses velocity and multiplies its magnitude by a coefficient e between zero and one. The outgoing speed is therefore twenty times e.

Now vary the release height. The outgoing speed changes both because the preimpact velocity changes and because impact happens later. If a differentiation tool treats the impact as taking place at exactly the old time, it misses the timing contribution. The result is not the derivative of the physical bounce map.

## Reset maps are not the whole story

Let the pre-event and post-event vector fields be different, and let a reset map transform the state at the event. Its ordinary Jacobian describes how a change in the event state affects the reset output at that event time.

But a perturbation observed at a common clock time requires more. One perturbed trajectory may already have bounced while the other is still falling. To compare them, we must account for the small time shift before and after the reset.

The saltation matrix is the corrected linear map. It combines the reset Jacobian with an additional rank-one term. That term contains the difference between the outgoing vector field and the reset of the incoming vector field, divided by the transverse crossing rate.

This rank-one correction disappears in special cases, for example when the vector fields match appropriately across a continuous identity transition. It does not disappear merely because a reset is simple. Even an instantaneous velocity reversal can have a substantial saltation correction.

## The bounce can be worked out exactly

Use height and vertical velocity as the state. Between impacts, height changes at the current velocity and velocity decreases at the gravitational acceleration. The guard is height equals zero. The reset leaves height unchanged and maps the incoming velocity to minus e times that velocity.

The ordinary reset Jacobian is diagonal: one for height and minus e for velocity. The saltation matrix has a different first diagonal entry, minus e, and an additional term coupling height perturbations into velocity perturbations. That coupling is proportional to the gravitational acceleration divided by the incoming velocity.

Near a grazing event, the incoming velocity approaches zero. The coupling can become large, reflecting genuine ill conditioning. This is not necessarily a bug in automatic differentiation. The physical event map itself becomes highly sensitive as the path barely touches the guard.

A programmer who differentiates only the reset rule would return the diagonal reset Jacobian and miss this effect. The exact two-dimensional model therefore gives a useful acceptance test for differentiable hybrid solvers.

## Detecting and differentiating events numerically

Practical ODE solvers often detect sign changes of a guard between accepted steps and then interpolate to locate the event. If the dense output interpolation has controlled error, event-time error can be bounded from the guard residual divided by a lower bound on the transverse crossing rate.

But sign-change detection alone misses a tangential contact with no sign reversal. It can also confuse multiple nearby crossings when step sizes are too large. Robust event location requires assumptions about the guard, local dynamics, and the number of crossings in the step.

For sensitivities, it is often preferable to differentiate the mathematically defined root of the guard equation rather than the particular sequence of iterative event-finder operations. The latter can change discontinuously when the number of root-finder iterations or rejected steps changes. A custom implicit derivative can be both simpler and closer to the intended continuous model.

That derivative must still be checked against the actual numerical approximation. If the dense output is inaccurate or the event root was not isolated, the formal sensitivity of the exact trajectory may not match the accuracy of the computed one.

## Adjoint methods need jumps too

When many parameters influence one scalar objective, adjoint sensitivity methods are efficient because they propagate a gradient backward through time. In a hybrid system, the forward perturbation jumps according to the saltation matrix. The corresponding adjoint jump involves its transpose, with additional terms when the objective includes event costs or the event definition depends explicitly on parameters.

Ignoring the jump can produce gradients that are systematically wrong even if the forward state trajectory looks correct. This is especially important in optimization: a descent algorithm may follow a plausible but false gradient for many iterations before the error becomes apparent.

One should also distinguish a differentiable trajectory with a fixed event sequence from a function whose event sequence changes. The saltation framework describes a local branch under transversality and consistent event ordering. At simultaneous events, grazing contacts, and mode-creation boundaries, a single classical derivative may not exist.

## A useful verification checklist

For every differentiated hybrid simulation, record the guard, the pre-event vector field, the reset, the post-event vector field, and any explicit time or parameter dependence. Check transversality. Locate the event with a controlled root tolerance. Apply the event-time derivative and saltation update. Compare with finite differences only in a perturbation regime that preserves the same event sequence.

The key conceptual point is simple. An event changes not only the state but also the duration spent under each dynamics. The saltation matrix captures both effects. When a model includes impacts or switching, sensitivity through time is part of the model, not an optional detail that can be delegated blindly to a generic differentiation engine.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Automatic Differentiation and Adjoint Sensitivity

**Track:** Numerical Analysis and Reliable Computation. **Background:** derivatives, chain rule, linear systems, numerical solvers, optimization. **Central question:** how can we differentiate a computation with thousands of intermediate steps without forming its full Jacobian?

#### Mathematical companion (not spoken)

For \(F:\mathbb R^n\to\mathbb R^m\), forward AD computes a **Jacobian-vector product** \(J_F(x)v\); reverse AD computes a **vector-Jacobian product** \(w^\top J_F(x)\). Dual numbers \(a+b\varepsilon\), \(\varepsilon^2=0\), implement first-order forward propagation.

**Worked graph:** \(f(x,y)=x^2y+\sin(xy)\). Then
\[\partial_x f=2xy+y\cos(xy),\qquad\partial_y f=x^2+x\cos(xy).\]
For x=2, y=3: \(\nabla f=(12+3\cos6,\ 4+2\cos6)\).

**Implicit adjoint:** assume a differentiable, nonsingular \(A(\theta)\), differentiable \(b(\theta)\), and state \(u(\theta)\) satisfying \(A(\theta)u=b(\theta)\). For a differentiable scalar objective \(J(u,\theta)\), set \(A(\theta)^\top\lambda=\nabla_u J\). For a scalar parameter \(\theta\),
\[\frac{dJ}{d\theta}=\frac{\partial J}{\partial\theta}+\lambda^\top\left(\frac{db}{d\theta}-\frac{dA}{d\theta}u\right).\]
For multiple parameters, replace derivatives by corresponding directional derivatives or collect the resulting gradient components. This is differentiation of the exact algebraic solution, not automatically of a finite-iteration stopping rule.

##### Exercises with answers

1. What does forward AD compute for a direction v? **Answer:** \(J_F(x)v\), without forming the full Jacobian.
2. Why is reverse mode attractive for one scalar objective with many parameters? **Answer:** one backward accumulation computes the full gradient at a cost typically proportional to a small multiple of the primal evaluation.
3. If \(A\) does not depend on theta but b does, what remains of the adjoint formula? **Answer:** \(dJ/d\theta=\partial_\theta J+\lambda^\top b_\theta\).
4. What goes wrong near a singular A? **Answer:** implicit sensitivities can become ill-conditioned or fail to exist, irrespective of how derivatives are implemented.

##### Reading and source notes

- [MIT 18.S096, Forward and Reverse-Mode Automatic Differentiation](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/mit18_s096iap23_lec08.pdf), Jacobian products and storage tradeoffs.
- Andreas Griewank and Andrea Walther, [*Evaluating Derivatives*](https://epubs.siam.org/doi/book/10.1137/1.9780898717761), algorithmic differentiation foundations.
- [SciPy, sparse linear algebra documentation](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html), numerical solve context for adjoint systems.

### Nonsmooth Sensitivity: What a Derivative Can and Cannot Tell You

**Track:** Numerical Analysis. **Background:** automatic differentiation, constrained optimization, projections, implicit functions and generalized derivatives. **Central question:** what happens when a numerical algorithm changes branches or its optimum moves across a constraint boundary?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. At theta zero, what is the directional derivative of `max(theta,0)` in direction `-2`? **Answer:** zero.
2. What is the Clarke generalized derivative of the same map at zero? **Answer:** the interval `[0,1]`.
3. When can the smooth implicit sensitivity formula be applied directly? **Answer:** when the defining map is differentiable and the relevant Jacobian with respect to the unknown is invertible.
4. What is wrong with interpreting an AD-chosen branch slope at a kink as the unique mathematical derivative? **Answer:** the ordinary derivative does not exist there, and a branch convention is only one selected generalized response.

##### Reading and source notes

- [The Elements of Differentiable Programming, Differentiation](https://diffprog.github.io/diff.html), generalized Jacobians and algorithmic derivatives.
- [Khan and Barton, A Vector Forward Mode of Automatic Differentiation for Generalized Derivative Evaluation](https://doi.org/10.1080/10556788.2015.1025400), nonsmooth generalized derivatives.
- [Clarke, Optimization and Nonsmooth Analysis](https://doi.org/10.1137/1.9781611971309), generalized gradients and nonsmooth calculus.

### Event-Time Sensitivities and Saltation Matrices

**Track:** Numerical Analysis. **Background:** ordinary differential equation solvers, implicit differentiation, and hybrid dynamics. **Central question:** how do derivatives change when a trajectory crosses an event and the governing dynamics jump?

#### Mathematical companion (not spoken)

For `x'=f^-(x,theta,t)` until `g(x,theta,t)=0`, let `tau(theta)` be a transverse event. With `x_theta^-` denoting the fixed-time pre-event sensitivity,
\[
\frac{d\tau}{d\theta}=-\frac{g_x x_\theta^-+g_\theta}{g_x f^-+g_t},
\qquad g_x f^-+g_t\ne0.
\]
For reset `R(x,t)` and post-event field `f^+`, the state saltation matrix at equal clock time is
\[
S=R_x+\frac{(f^+-R_x f^- -R_t)g_x}{g_x f^-+g_t}.
\]
For a bouncing ball `x=(h,v)`, `f=(v,-g_0)`, guard `g=h`, reset `R=(h,-e v)`, the matrix is
\[
S=\begin{pmatrix}-e&0\\-(1+e)g_0/v^-&-e\end{pmatrix}
\]
at a transverse impact `v^-!=0`. With `h_0=20`, `v_0=0`, `g_0=10`, one has `tau=sqrt(2h_0/g_0)=2`, `d tau/d h_0=1/(g_0 tau)=1/20`, and outgoing speed `20e`. Grazing invalidates the division by `v^-`.

##### Exercises with answers

1. What is the transversality denominator for a time-independent height guard? **Answer:** vertical velocity at contact.
2. If initial height increases slightly, what happens to a transverse free-fall impact time? **Answer:** it increases, with derivative `1/(g_0 tau)` from rest.
3. Does differentiating only the reset Jacobian give the saltation matrix? **Answer:** generally not; event-time change adds a correction.
4. Why can a central finite difference fail near grazing? **Answer:** perturbed trajectories may have different event sequences or no crossing.

##### Reading and source notes

- [Saltation Matrix and Hybrid Sensitivity Background](https://www.andrew.cmu.edu/user/amj1/papers/Payne2024.pdf), explicit saltation formula and transverse-event assumptions.
- [Kong et al., Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems](https://arxiv.org/abs/2306.06862), applications of saltation-based linearization in hybrid systems.
