# 015000 — Implicit Time Stepping, Newton–Krylov Solvers, and Preconditioning

**Track:** Numerical Analysis and Reliable Computation. **Background:** numerical ODEs, stiffness, Jacobians, Newton's method, iterative linear solvers. **Central question:** how can a time-stepping method remain stable without making every tiny decay timescale dictate the step size?

<!-- BEGIN SPOKEN LECTURE -->

# Implicit Time Stepping, Newton–Krylov Solvers, and Preconditioning

Suppose a system contains one very fast decaying process and one slow process that we actually want to observe. The fast process may become negligible almost immediately, yet an explicit numerical method can be forced to take tiny steps for the entire simulation. The issue is not accuracy in the slow variables. It is stability of the discretization in the presence of fast decay.

Implicit time stepping addresses that problem. It replaces a direct update with an equation that must be solved for the next state. This can permit much larger stable time steps, but it creates a new numerical task: solve a nonlinear system at every step, and often a large linear system inside that solve.

## A scalar experiment diagnoses stiffness

Start with the equation y prime equals negative alpha times y, where alpha is large and positive. The exact solution decays exponentially. There is no physical instability.

Explicit Euler takes the current state and adds the time step times the current derivative. Its amplification factor is one minus alpha times the step size. If the step size is larger than twice the reciprocal of alpha, the absolute value of the amplification factor exceeds one, so the numerical sequence grows and oscillates instead of decaying.

For alpha equal to one thousand and step size one tenth, the factor is negative ninety-nine. A perfectly stable physical process becomes wildly unstable numerically.

Now evaluate the derivative at the unknown next state instead. Implicit Euler says the next y equals the current y minus alpha times the step size times the next y. Solve this one linear equation, and the amplification factor becomes one divided by one plus alpha times the step size. With the same values, that is one over one hundred and one. It decays, as it should.

The difference is not subtle. Implicit Euler has an entire left half-plane stability region for the scalar test equation with complex negative-real-part lambda. It is A-stable. And as the magnitude of a large negative step times lambda grows, its amplification tends to zero; it is also L-stable. Both properties help explain its behavior for stiff decaying modes.

## Stability does not mean accuracy

A stable step can still be inaccurate. Implicit Euler is first-order: its local truncation error is typically of second order in the step size, and over a fixed interval its global error is typically first order, assuming the standard smoothness and stability hypotheses.

In the scalar example, a very large step can crush the fast mode without resolving its early transient. That may be exactly what a long-time simulation needs, or it may erase a short event that matters physically. Numerical stability says errors are not amplified in the forbidden way; it does not say the approximation answers every scientific question.

Other implicit methods make different compromises. The trapezoidal rule is second-order and A-stable, but its amplification factor approaches negative one for very stiff negative modes. Thus it need not strongly damp the fastest components. Some backward differentiation formulas, and implicit Runge–Kutta methods such as Radau methods, are designed to offer better stiff stability properties with higher accuracy.

## Every implicit step is a nonlinear equation

For a general differential equation, the implicit Euler update asks for an unknown vector z satisfying z equals the previous state plus the step size times the vector field evaluated at the future time and at z.

Move all terms to one side to define a nonlinear residual. Newton's method repeatedly linearizes that residual around the current guess. The Jacobian of the residual is the identity matrix minus the step size times the Jacobian of the vector field.

At each Newton iteration, we solve a linear system for a correction, update the guess, and recompute the residual. A good initial guess may come from the previous state or an explicit predictor. But Newton's method is local. A poor guess, an ill-conditioned Jacobian, or an overly ambitious step can cause convergence problems.

The robust implementation must also decide when to stop the nonlinear iterations. A small change in the iterate is not always a reliable indicator of a small residual, and a small residual need not imply a small forward error in an ill-conditioned problem. These are the same distinctions between residual, conditioning, and accuracy that appeared earlier in numerical analysis.

## Why Krylov methods enter

For a large discretized PDE, forming and factoring the full Newton Jacobian can be prohibitively expensive. Newton–Krylov methods keep Newton's outer iteration but solve its linear systems iteratively, often using GMRES for nonsymmetric matrices.

A Krylov method needs the action of the Jacobian on a vector. It may not need the full matrix. That action can be supplied by automatic differentiation, a hand-derived linearized operator, or a carefully controlled finite-difference approximation to the residual.

This opens the door to matrix-free implicit simulation. The vector field and residual may be available as functions, while the linear solver asks only for products of the form Jacobian times vector.

But there is a catch. Krylov iterations may converge very slowly if the linear system is badly conditioned or has a difficult spectrum. The implicit step has cured one stability limitation while exposing a hard linear-algebra problem.

## Preconditioning changes the problem seen by the solver

A preconditioner is an approximation to the inverse, or an easily inverted approximation to the Jacobian, chosen so that the transformed linear system is easier to solve iteratively. Good preconditioning makes the relevant eigenvalues or other convergence-controlling features more favorable, at lower cost than an exact solve.

For a diffusion problem discretized on a fine grid, the Jacobian often reflects elliptic operators and their wide range of spatial scales. Sparse factorizations, incomplete factorizations, or multigrid ideas may provide effective preconditioners. Their performance depends on the operator, mesh, coefficients, boundary conditions, and implementation.

There is no universal preconditioner. And preconditioning must be assessed for total work, not only for reducing the number of iterations. An expensive setup that saves a handful of inexpensive Krylov steps may make the computation slower overall.

## Match the error tolerances

A full implicit time integrator has at least three numerical error sources: time discretization, nonlinear solve error, and inexact linear solve error. They interact.

If a step's desired temporal accuracy is modest, solving its Newton systems to machine precision may waste work. Conversely, if inner iterations are stopped far too early, the resulting algebraic errors may dominate the discretization error or even spoil the solver's stability. Adaptive step-size controllers should account for the achieved nonlinear convergence, not merely the formal order of the method.

This is why reliable software distinguishes failure to solve an implicit step from a successful step whose estimated time-discretization error is too large. The remedies differ: improve the nonlinear guess, change the step, adjust tolerances, or strengthen the preconditioner.

## What implicit methods buy us

Implicit methods do not abolish the cost of stiffness. They trade a severe explicit stability restriction for nonlinear and linear algebra that can often be handled efficiently. The right choice depends on the timescales one must resolve, the size and structure of the Jacobian, and the accuracy actually required.

The core workflow is a sequence of explicit questions. Which physical modes decay? Which stability region does the time integrator have? How accurately must each future-state equation be solved? Can Jacobian-vector products be computed efficiently? Is the preconditioner worth its construction cost? A robust stiff solver answers all five, rather than treating a stable step size as the whole problem.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(y'=\lambda y\), with \(\Re\lambda\le0\) and \(z=h\lambda\): explicit Euler has stability function \(R_E(z)=1+z\); implicit Euler has \(R_I(z)=1/(1-z)\). For \(\Re z\le0\), \(|1-z|\ge1\), hence \(|R_I(z)|\le1\) (A-stability). As \(z\to-\infty\) on the real axis, \(R_I(z)\to0\) (L-stability). The trapezoidal rule has \(R_T(z)=(1+z/2)/(1-z/2)\), which is A-stable but \(R_T(-r)\to-1\) for \(r\to+\infty\), so it is not L-stable.

**Worked scalar comparison:** \(y'=-1000y\), \(h=0.1\), \(R_E=-99\), \(R_I=1/101\).

For a nonlinear ODE \(y'=f(t,y)\), the implicit Euler residual and Newton Jacobian are
\[F(z)=z-y_n-hf(t_{n+1},z),\qquad J_F(z)=I-hJ_f(t_{n+1},z).\]
Newton updates solve \(J_F(z_k)\delta_k=-F(z_k)\), \(z_{k+1}=z_k+\delta_k\). Inexact Newton–Krylov uses an iterative solver such as GMRES for each correction, with Jacobian-vector products \(J_F(z)v\). A preconditioner \(P\approx J_F\) should make application of \(P^{-1}\) cheap and accelerate convergence.

### Exercises with answers

1. Why does explicit Euler explode on \(y'=-1000y\) with \(h=0.1\)? **Answer:** amplification magnitude is 99, greater than one.
2. Is implicit Euler exact for this scalar equation? **No:** its factor \(1/(1+1000h)\) approximates but differs from \(e^{-1000h}\).
3. Does A-stability guarantee all high-frequency modes are strongly damped? **No:** the A-stable trapezoidal rule is not L-stable.
4. What matrix is solved in Newton's method for implicit Euler? **Answer:** \(I-hJ_f\), evaluated at the current nonlinear iterate and future time.

### Reading and source notes

- [SciPy documentation, `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html), stiff BDF/Radau methods and Jacobian interfaces.
- [MIT 18.330 Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/), stability regions and time integration.
- Ernst Hairer and Gerhard Wanner, [*Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems*](https://link.springer.com/book/10.1007/978-3-642-05221-7), stability and stiff algorithms.
