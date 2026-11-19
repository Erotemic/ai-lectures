# Krylov eigenproblems, implicit time steps, and preconditioning

<!-- BEGIN SPOKEN LECTURE -->

# Krylov eigenproblems, implicit time steps, and preconditioning

## Sparse Eigenvalue Problems: Krylov Spaces, Lanczos, and Arnoldi

Many scientific matrices are enormous. A grid with millions of points, a large graph, or a discretized partial differential equation may produce a matrix with millions of rows. But each row can contain only a few nonzero entries, because each point interacts directly with a small neighborhood.

Computing a complete dense eigenvalue decomposition would destroy that advantage. It could require far too much memory and arithmetic. Often we need only a handful of eigenvalues: perhaps the largest eigenvalue, a small cluster near zero, or the modes responsible for instability. Krylov subspace algorithms approach this task using matrix-vector products rather than the full dense matrix.

### Start with the power method

Take a matrix A and a starting vector v. Multiply by A, normalize, and repeat. Under appropriate assumptions, the direction of the iterates approaches an eigenvector corresponding to an eigenvalue of largest magnitude.

For example, let A be diagonal with entries nine, four, and one, and start with a vector whose three components are all one. After one multiplication the components become nine, four, and one. After another they become eighty-one, sixteen, and one. The direction increasingly favors the first coordinate. The ratio between the dominant and next-largest magnitudes controls how quickly this happens.

The method has limitations. If the starting vector has no component in the dominant eigendirection, it cannot discover it in exact arithmetic. If eigenvalues of equal maximal magnitude compete, the normalized sequence may not converge to one direction. And the power method preferentially finds large-magnitude eigenvalues, not whichever eigenvalue happens to be scientifically interesting.

### Keep the subspace instead of one vector

Rather than discard previous information after each multiplication, collect the vectors v, A times v, A squared times v, and so on. Their span after k terms is the k-th Krylov subspace.

Every vector in this subspace is a polynomial in A applied to the starting vector, with polynomial degree less than k. This observation connects the eigenvalue problem to polynomial approximation. By choosing different polynomials implicitly, the algorithm can emphasize useful parts of the spectrum and suppress others.

But the raw powers are a poor numerical basis. The columns quickly become nearly parallel when one spectral component dominates. The resulting basis can be extremely ill-conditioned. We therefore orthogonalize as we construct the subspace.

### Arnoldi orthogonalization

Arnoldi's method constructs an orthonormal basis q one through q k for the Krylov subspace. At each step it multiplies the newest basis vector by A, subtracts components in all the current basis directions, and normalizes the remaining component if it is nonzero.

The inner products used in those subtractions form a small upper-Hessenberg matrix H. It represents the action of A after projecting back into the current subspace. Instead of solving a huge eigenvalue problem, we solve a small one involving H.

The approximate eigenvalues of H are called Ritz values. If y is an eigenvector of H with Ritz value theta, multiply the Arnoldi basis matrix Q by y. The result is a candidate eigenvector of A. The hope is that A acting on that candidate approximately multiplies it by theta.

This is a projection method, not a mysterious transformation of the original matrix. It chooses a restricted subspace, demands that the residual be orthogonal to that subspace, and solves the resulting small problem.

### Why symmetry makes Lanczos cheaper

If A is real symmetric, or complex Hermitian, the orthogonality structure becomes simpler. The Hessenberg matrix collapses to a symmetric tridiagonal matrix. In exact arithmetic, each new Lanczos basis vector can be generated using only the current and previous basis vectors, together with a new multiplication by A.

That short recurrence saves work and makes Lanczos especially attractive for large sparse Hermitian eigenproblems. But its ideal behavior assumes exact orthogonality. In floating-point arithmetic, the computed vectors can lose orthogonality, producing repeated or ghost Ritz values. Reorthogonalization, selective orthogonalization, and restarted variants are practical responses.

Arnoldi is more general and handles nonsymmetric matrices, including cases with complex eigenvalues, but maintaining an orthonormal basis generally costs more storage and inner products as the subspace grows. This is an important algorithmic tradeoff, not simply a preference between two implementations.

### An exact small example

Take the two-by-two diagonal matrix with eigenvalues two and five. Start with the unit vector whose components are equal. Restrict to the one-dimensional subspace spanned by that vector. The Rayleigh quotient, its estimated eigenvalue, is the average of two and five: three and one-half.

Apply the original matrix to the vector and subtract three and one-half times the vector. The residual has magnitude one and one-half. That is not a small error, because our single trial direction mixes both eigenspaces equally.

Expand the Krylov subspace to include the matrix applied to the starting vector. These two vectors are linearly independent, so their span is the entire two-dimensional space. With exact arithmetic, the second Ritz calculation recovers the eigenvalues two and five exactly.

This toy example captures the mechanism. As the Krylov subspace expands, it gains directions that resolve the action of A. The small projected problem becomes more informative about the actual spectrum.

### Residuals are the first credibility check

An approximate eigenpair consists of a scalar theta and a nonzero vector v. Its residual is A times v minus theta times v. A small residual says the pair almost satisfies the eigenvalue equation.

For a symmetric or Hermitian A, there is a particularly clear theorem: if v has unit norm, at least one true eigenvalue of A lies within the residual norm of theta. The proof follows by expanding v in an orthonormal eigenbasis. If every eigenvalue were farther from theta than that residual norm, the squared residual would have to be larger than it actually is.

This is a rigorous absolute eigenvalue enclosure when the residual norm is itself computed or enclosed reliably. But it does not necessarily identify *which* eigenvalue is nearby, and it does not certify that the corresponding eigenvector is accurate. Eigenvector error bounds need additional information, such as a spectral gap. For nonsymmetric matrices, nonnormality can make a small residual much less informative about the spectrum.

For Arnoldi, the residual can be estimated cheaply from the last recurrence coefficient and the final component of the Ritz vector in the projected basis. In finite precision, it remains sensible to evaluate a candidate's residual directly against the original matrix, especially when orthogonality has degraded.

### Finding eigenvalues near a chosen location

Standard Krylov iterations often favor extremal parts of the spectrum. To find an interior eigenvalue near a target sigma, a common technique is shift-and-invert. Instead of multiplying by A, apply the inverse of A minus sigma times the identity. Eigenvalues near sigma are transformed into eigenvalues of large magnitude, making them easier for power-like methods to capture.

The price is that every iteration now requires solving a linear system. If the matrix is sparse and a factorization can be reused, this may be worthwhile. But a difficult or poorly conditioned shifted solve can dominate the computation. The method is not a free shortcut, and the chosen shift must avoid a singular system or be handled with appropriate methods.

### When the computation is finished

A reliable sparse eigensolver should report what it actually established: the Ritz value, an approximate eigenvector, residual information, and assumptions under which residuals imply spectral error. It should also distinguish matrix approximation error from discretization error. If A came from a PDE, a certified eigenvalue of A is not automatically a certified eigenvalue of the continuous differential operator.

Krylov algorithms are powerful because they use the matrix in the form we can afford: as an operation on vectors. Arnoldi builds a general projected problem; Lanczos exploits Hermitian symmetry for a shorter recurrence; Rayleigh–Ritz turns the projection into candidate eigenpairs. Residual analysis turns those candidates into defensible numerical claims.

## Implicit Time Stepping, Newton–Krylov Solvers, and Preconditioning

Suppose a system contains one very fast decaying process and one slow process that we actually want to observe. The fast process may become negligible almost immediately, yet an explicit numerical method can be forced to take tiny steps for the entire simulation. The issue is not accuracy in the slow variables. It is stability of the discretization in the presence of fast decay.

Implicit time stepping addresses that problem. It replaces a direct update with an equation that must be solved for the next state. This can permit much larger stable time steps, but it creates a new numerical task: solve a nonlinear system at every step, and often a large linear system inside that solve.

### A scalar experiment diagnoses stiffness

Start with the equation y prime equals negative alpha times y, where alpha is large and positive. The exact solution decays exponentially. There is no physical instability.

Explicit Euler takes the current state and adds the time step times the current derivative. Its amplification factor is one minus alpha times the step size. If the step size is larger than twice the reciprocal of alpha, the absolute value of the amplification factor exceeds one, so the numerical sequence grows and oscillates instead of decaying.

For alpha equal to one thousand and step size one tenth, the factor is negative ninety-nine. A perfectly stable physical process becomes wildly unstable numerically.

Now evaluate the derivative at the unknown next state instead. Implicit Euler says the next y equals the current y minus alpha times the step size times the next y. Solve this one linear equation, and the amplification factor becomes one divided by one plus alpha times the step size. With the same values, that is one over one hundred and one. It decays, as it should.

The difference is not subtle. Implicit Euler has an entire left half-plane stability region for the scalar test equation with complex negative-real-part lambda. It is A-stable. And as the magnitude of a large negative step times lambda grows, its amplification tends to zero; it is also L-stable. Both properties help explain its behavior for stiff decaying modes.

### Stability does not mean accuracy

A stable step can still be inaccurate. Implicit Euler is first-order: its local truncation error is typically of second order in the step size, and over a fixed interval its global error is typically first order, assuming the standard smoothness and stability hypotheses.

In the scalar example, a very large step can crush the fast mode without resolving its early transient. That may be exactly what a long-time simulation needs, or it may erase a short event that matters physically. Numerical stability says errors are not amplified in the forbidden way; it does not say the approximation answers every scientific question.

Other implicit methods make different compromises. The trapezoidal rule is second-order and A-stable, but its amplification factor approaches negative one for very stiff negative modes. Thus it need not strongly damp the fastest components. Some backward differentiation formulas, and implicit Runge–Kutta methods such as Radau methods, are designed to offer better stiff stability properties with higher accuracy.

### Every implicit step is a nonlinear equation

For a general differential equation, the implicit Euler update asks for an unknown vector z satisfying z equals the previous state plus the step size times the vector field evaluated at the future time and at z.

Move all terms to one side to define a nonlinear residual. Newton's method repeatedly linearizes that residual around the current guess. The Jacobian of the residual is the identity matrix minus the step size times the Jacobian of the vector field.

At each Newton iteration, we solve a linear system for a correction, update the guess, and recompute the residual. A good initial guess may come from the previous state or an explicit predictor. But Newton's method is local. A poor guess, an ill-conditioned Jacobian, or an overly ambitious step can cause convergence problems.

The robust implementation must also decide when to stop the nonlinear iterations. A small change in the iterate is not always a reliable indicator of a small residual, and a small residual need not imply a small forward error in an ill-conditioned problem. These are the same distinctions between residual, conditioning, and accuracy that appeared earlier in numerical analysis.

### Why Krylov methods enter

For a large discretized PDE, forming and factoring the full Newton Jacobian can be prohibitively expensive. Newton–Krylov methods keep Newton's outer iteration but solve its linear systems iteratively, often using GMRES for nonsymmetric matrices.

A Krylov method needs the action of the Jacobian on a vector. It may not need the full matrix. That action can be supplied by automatic differentiation, a hand-derived linearized operator, or a carefully controlled finite-difference approximation to the residual.

This opens the door to matrix-free implicit simulation. The vector field and residual may be available as functions, while the linear solver asks only for products of the form Jacobian times vector.

But there is a catch. Krylov iterations may converge very slowly if the linear system is badly conditioned or has a difficult spectrum. The implicit step has cured one stability limitation while exposing a hard linear-algebra problem.

### Preconditioning changes the problem seen by the solver

A preconditioner is an approximation to the inverse, or an easily inverted approximation to the Jacobian, chosen so that the transformed linear system is easier to solve iteratively. Good preconditioning makes the relevant eigenvalues or other convergence-controlling features more favorable, at lower cost than an exact solve.

For a diffusion problem discretized on a fine grid, the Jacobian often reflects elliptic operators and their wide range of spatial scales. Sparse factorizations, incomplete factorizations, or multigrid ideas may provide effective preconditioners. Their performance depends on the operator, mesh, coefficients, boundary conditions, and implementation.

There is no universal preconditioner. And preconditioning must be assessed for total work, not only for reducing the number of iterations. An expensive setup that saves a handful of inexpensive Krylov steps may make the computation slower overall.

### Match the error tolerances

A full implicit time integrator has at least three numerical error sources: time discretization, nonlinear solve error, and inexact linear solve error. They interact.

If a step's desired temporal accuracy is modest, solving its Newton systems to machine precision may waste work. Conversely, if inner iterations are stopped far too early, the resulting algebraic errors may dominate the discretization error or even spoil the solver's stability. Adaptive step-size controllers should account for the achieved nonlinear convergence, not merely the formal order of the method.

This is why reliable software distinguishes failure to solve an implicit step from a successful step whose estimated time-discretization error is too large. The remedies differ: improve the nonlinear guess, change the step, adjust tolerances, or strengthen the preconditioner.

### What implicit methods buy us

Implicit methods do not abolish the cost of stiffness. They trade a severe explicit stability restriction for nonlinear and linear algebra that can often be handled efficiently. The right choice depends on the timescales one must resolve, the size and structure of the Jacobian, and the accuracy actually required.

The core workflow is a sequence of explicit questions. Which physical modes decay? Which stability region does the time integrator have? How accurately must each future-state equation be solved? Can Jacobian-vector products be computed efficiently? Is the preconditioner worth its construction cost? A robust stiff solver answers all five, rather than treating a stable step size as the whole problem.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Sparse Eigenvalue Problems: Krylov Spaces, Lanczos, and Arnoldi

**Track:** Numerical Analysis and Reliable Computation. **Background:** matrix-vector products, eigenvalues, orthogonal projections, iterative linear solvers. **Central question:** how can we approximate important eigenvalues of a matrix too large to diagonalize, and what makes an approximation trustworthy?

#### Mathematical companion (not spoken)

For \(A\in\mathbb C^{n\times n}\), \(v\ne0\), the \(k\)-th Krylov subspace is
\[\mathcal K_k(A,v)=\operatorname{span}\{v,Av,\ldots,A^{k-1}v\}.\]
Arnoldi constructs an orthonormal \(Q_k\) and Hessenberg \(H_k=Q_k^*AQ_k\) with the recurrence
\[AQ_k=Q_kH_k+h_{k+1,k}q_{k+1}e_k^*.\]
For an eigenpair \(H_ky=\theta y\), \(\|y\|=1\), the Ritz vector \(z=Q_ky\) has residual
\[r=Az-\theta z=h_{k+1,k}(e_k^*y)q_{k+1},\qquad \|r\|=|h_{k+1,k}e_k^*y|\]
in exact arithmetic. For Hermitian \(A\), Lanczos produces a real symmetric tridiagonal \(H_k\); finite precision may require reorthogonalization.

**Hermitian residual theorem:** \(\operatorname{dist}(\theta,\sigma(A))\le\|Az-\theta z\|/\|z\|\). Proof: if \(A=U\operatorname{diag}(\lambda_i)U^*\), then \(\|r\|^2=\sum_i|\lambda_i-\theta|^2|\langle u_i,z\rangle|^2\ge \operatorname{dist}(\theta,\sigma(A))^2\|z\|^2\).

**Two-dimensional example:** \(A=\operatorname{diag}(2,5)\), \(q_1=(1,1)/\sqrt2\), \(\theta=q_1^*Aq_1=7/2\), \(\|Aq_1-\theta q_1\|=3/2\). At \(k=2\), the Krylov subspace is all \(\mathbb R^2\), so both Ritz values are exact. For shift-and-invert, \(B=(A-\sigma I)^{-1}\) (when invertible) has eigenvalues \((\lambda_i-\sigma)^{-1}\); each action of \(B\) requires a solve.

##### Exercises with answers

1. What operation must an efficient sparse Arnoldi iteration support? **Answer:** repeated matrix-vector products with \(A\), plus orthogonalization.
2. Why is the unorthogonalized power basis often numerically bad? **Answer:** repeated powers can become nearly linearly dependent as dominant modes overwhelm others.
3. For Hermitian \(A\) and a unit Ritz vector with residual norm \(10^{-6}\), what is certified in exact residual arithmetic? **Answer:** at least one eigenvalue lies within \(10^{-6}\) of the Ritz value, not necessarily a specified indexed eigenvalue.
4. What new work does shift-and-invert introduce? **Answer:** repeated linear solves involving \(A-\sigma I\); a sparse matrix-vector product alone no longer suffices.

##### Reading and source notes

- David Bindel, [Cornell CS 6210: Lanczos and Arnoldi](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-17.html), Krylov subspaces and recurrences.
- David Bindel, [Cornell CS 6210: Large-scale eigensolvers](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-12-01.html), Rayleigh–Ritz and residuals.
- ETH Zurich, [Lecture Notes on Solving Large Scale Eigenvalue Problems](https://people.inf.ethz.ch/arbenz/ewp/Lnotes/lsevp.pdf), Arnoldi and Lanczos algorithms.

### Implicit Time Stepping, Newton–Krylov Solvers, and Preconditioning

**Track:** Numerical Analysis and Reliable Computation. **Background:** numerical ODEs, stiffness, Jacobians, Newton's method, iterative linear solvers. **Central question:** how can a time-stepping method remain stable without making every tiny decay timescale dictate the step size?

#### Mathematical companion (not spoken)

For \(y'=\lambda y\), with \(\Re\lambda\le0\) and \(z=h\lambda\): explicit Euler has stability function \(R_E(z)=1+z\); implicit Euler has \(R_I(z)=1/(1-z)\). For \(\Re z\le0\), \(|1-z|\ge1\), hence \(|R_I(z)|\le1\) (A-stability). As \(z\to-\infty\) on the real axis, \(R_I(z)\to0\) (L-stability). The trapezoidal rule has \(R_T(z)=(1+z/2)/(1-z/2)\), which is A-stable but \(R_T(-r)\to-1\) for \(r\to+\infty\), so it is not L-stable.

**Worked scalar comparison:** \(y'=-1000y\), \(h=0.1\), \(R_E=-99\), \(R_I=1/101\).

For a nonlinear ODE \(y'=f(t,y)\), the implicit Euler residual and Newton Jacobian are
\[F(z)=z-y_n-hf(t_{n+1},z),\qquad J_F(z)=I-hJ_f(t_{n+1},z).\]
Newton updates solve \(J_F(z_k)\delta_k=-F(z_k)\), \(z_{k+1}=z_k+\delta_k\). Inexact Newton–Krylov uses an iterative solver such as GMRES for each correction, with Jacobian-vector products \(J_F(z)v\). A preconditioner \(P\approx J_F\) should make application of \(P^{-1}\) cheap and accelerate convergence.

##### Exercises with answers

1. Why does explicit Euler explode on \(y'=-1000y\) with \(h=0.1\)? **Answer:** amplification magnitude is 99, greater than one.
2. Is implicit Euler exact for this scalar equation? **No:** its factor \(1/(1+1000h)\) approximates but differs from \(e^{-1000h}\).
3. Does A-stability guarantee all high-frequency modes are strongly damped? **No:** the A-stable trapezoidal rule is not L-stable.
4. What matrix is solved in Newton's method for implicit Euler? **Answer:** \(I-hJ_f\), evaluated at the current nonlinear iterate and future time.

##### Reading and source notes

- [SciPy documentation, `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html), stiff BDF/Radau methods and Jacobian interfaces.
- [MIT 18.330 Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/), stability regions and time integration.
- Ernst Hairer and Gerhard Wanner, [*Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems*](https://link.springer.com/book/10.1007/978-3-642-05221-7), stability and stiff algorithms.
