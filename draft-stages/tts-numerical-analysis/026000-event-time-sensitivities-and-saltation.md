# 026000 - Event-Time Sensitivities and Saltation Matrices

**Track:** Numerical Analysis. **Background:** ordinary differential equation solvers, implicit differentiation, and hybrid dynamics. **Central question:** how do derivatives change when a trajectory crosses an event and the governing dynamics jump?

<!-- BEGIN SPOKEN LECTURE -->

# A smooth trajectory can have a nonsmooth program

Many simulations evolve smoothly until a condition becomes true. A ball hits the ground and reverses velocity. A controller switches modes when a threshold is crossed. A chemical process changes equations after a reaction stage. These are hybrid dynamical systems: continuous differential equations joined by discrete events.

A common numerical mistake is to differentiate the continuous evolution while treating the detected event time as a fixed constant. That can give a derivative that looks precise yet describes the wrong problem. Change an initial condition slightly, and the event happens at a slightly different time. The trajectory spends more or less time under each vector field. Its sensitivity contains a correction for that timing shift.

This lesson matters for optimal control, parameter estimation, inverse problems, and differentiable simulation. An event detector is not merely an implementation detail. Its root defines part of the mathematical map whose derivative we want.

# Events are roots of a moving equation

Consider a state x evolving under an ordinary differential equation that depends on a parameter theta. An event occurs when a scalar guard function of the state, parameter, and time reaches zero. Let tau denote the first relevant crossing time.

A small parameter change perturbs the trajectory. The event location moves because the guard is evaluated along the changed trajectory. Differentiate the guard equation with respect to theta. The total derivative contains the direct parameter derivative of the guard, the derivative of the state at a fixed time, and the vector field multiplied by the derivative of the event time.

Solving this linear equation gives the event-time derivative. Its denominator is the rate at which the guard changes along the unperturbed trajectory. If that rate is nonzero, the crossing is transverse, and the implicit function theorem gives a locally smooth event-time function.

If the rate is zero, the trajectory grazes the event surface. Then the denominator vanishes and first-order event sensitivity may fail. The solution may touch without crossing, or the number and order of events may change under arbitrarily small perturbations. No amount of numerical precision can justify applying the transverse formula at an actual grazing point.

# A falling ball makes the derivative visible

Drop a ball from height twenty under a constant downward acceleration of ten, starting from rest. In idealized units, the height falls quadratically in time. It reaches the ground after two time units.

Differentiate the impact time with respect to release height. The derivative is one over acceleration times the impact time. Here it is one twentieth of a time unit per unit height. A small increase in height delays the impact, even before we consider what happens to the velocity after the bounce.

At impact, the downward velocity has magnitude twenty. A restitution rule reverses velocity and multiplies its magnitude by a coefficient e between zero and one. The outgoing speed is therefore twenty times e.

Now vary the release height. The outgoing speed changes both because the preimpact velocity changes and because impact happens later. If a differentiation tool treats the impact as taking place at exactly the old time, it misses the timing contribution. The result is not the derivative of the physical bounce map.

# Reset maps are not the whole story

Let the pre-event and post-event vector fields be different, and let a reset map transform the state at the event. Its ordinary Jacobian describes how a change in the event state affects the reset output at that event time.

But a perturbation observed at a common clock time requires more. One perturbed trajectory may already have bounced while the other is still falling. To compare them, we must account for the small time shift before and after the reset.

The saltation matrix is the corrected linear map. It combines the reset Jacobian with an additional rank-one term. That term contains the difference between the outgoing vector field and the reset of the incoming vector field, divided by the transverse crossing rate.

This rank-one correction disappears in special cases, for example when the vector fields match appropriately across a continuous identity transition. It does not disappear merely because a reset is simple. Even an instantaneous velocity reversal can have a substantial saltation correction.

# The bounce can be worked out exactly

Use height and vertical velocity as the state. Between impacts, height changes at the current velocity and velocity decreases at the gravitational acceleration. The guard is height equals zero. The reset leaves height unchanged and maps the incoming velocity to minus e times that velocity.

The ordinary reset Jacobian is diagonal: one for height and minus e for velocity. The saltation matrix has a different first diagonal entry, minus e, and an additional term coupling height perturbations into velocity perturbations. That coupling is proportional to the gravitational acceleration divided by the incoming velocity.

Near a grazing event, the incoming velocity approaches zero. The coupling can become large, reflecting genuine ill conditioning. This is not necessarily a bug in automatic differentiation. The physical event map itself becomes highly sensitive as the path barely touches the guard.

A programmer who differentiates only the reset rule would return the diagonal reset Jacobian and miss this effect. The exact two-dimensional model therefore gives a useful acceptance test for differentiable hybrid solvers.

# Detecting and differentiating events numerically

Practical ODE solvers often detect sign changes of a guard between accepted steps and then interpolate to locate the event. If the dense output interpolation has controlled error, event-time error can be bounded from the guard residual divided by a lower bound on the transverse crossing rate.

But sign-change detection alone misses a tangential contact with no sign reversal. It can also confuse multiple nearby crossings when step sizes are too large. Robust event location requires assumptions about the guard, local dynamics, and the number of crossings in the step.

For sensitivities, it is often preferable to differentiate the mathematically defined root of the guard equation rather than the particular sequence of iterative event-finder operations. The latter can change discontinuously when the number of root-finder iterations or rejected steps changes. A custom implicit derivative can be both simpler and closer to the intended continuous model.

That derivative must still be checked against the actual numerical approximation. If the dense output is inaccurate or the event root was not isolated, the formal sensitivity of the exact trajectory may not match the accuracy of the computed one.

# Adjoint methods need jumps too

When many parameters influence one scalar objective, adjoint sensitivity methods are efficient because they propagate a gradient backward through time. In a hybrid system, the forward perturbation jumps according to the saltation matrix. The corresponding adjoint jump involves its transpose, with additional terms when the objective includes event costs or the event definition depends explicitly on parameters.

Ignoring the jump can produce gradients that are systematically wrong even if the forward state trajectory looks correct. This is especially important in optimization: a descent algorithm may follow a plausible but false gradient for many iterations before the error becomes apparent.

One should also distinguish a differentiable trajectory with a fixed event sequence from a function whose event sequence changes. The saltation framework describes a local branch under transversality and consistent event ordering. At simultaneous events, grazing contacts, and mode-creation boundaries, a single classical derivative may not exist.

# A useful verification checklist

For every differentiated hybrid simulation, record the guard, the pre-event vector field, the reset, the post-event vector field, and any explicit time or parameter dependence. Check transversality. Locate the event with a controlled root tolerance. Apply the event-time derivative and saltation update. Compare with finite differences only in a perturbation regime that preserves the same event sequence.

The key conceptual point is simple. An event changes not only the state but also the duration spent under each dynamics. The saltation matrix captures both effects. When a model includes impacts or switching, sensitivity through time is part of the model, not an optional detail that can be delegated blindly to a generic differentiation engine.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. What is the transversality denominator for a time-independent height guard? **Answer:** vertical velocity at contact.
2. If initial height increases slightly, what happens to a transverse free-fall impact time? **Answer:** it increases, with derivative `1/(g_0 tau)` from rest.
3. Does differentiating only the reset Jacobian give the saltation matrix? **Answer:** generally not; event-time change adds a correction.
4. Why can a central finite difference fail near grazing? **Answer:** perturbed trajectories may have different event sequences or no crossing.

### Reading and source notes

- [Saltation Matrix and Hybrid Sensitivity Background](https://www.andrew.cmu.edu/user/amj1/papers/Payne2024.pdf), explicit saltation formula and transverse-event assumptions.
- [Kong et al., Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems](https://arxiv.org/abs/2306.06862), applications of saltation-based linearization in hybrid systems.
