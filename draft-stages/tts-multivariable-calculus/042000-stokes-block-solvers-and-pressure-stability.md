# Stokes Flow and Mixed Solvers: Pressure, Blocks, and Reliable Refinement

**Track:** Multivariable Calculus from First Principles. **Focus:** Stokes weak formulation, pressure gauge, Taylor–Hood stability, Schur complement preconditioning, pressure robustness, and mixed finite-element error estimates.

<!-- BEGIN SPOKEN LECTURE -->

# Stokes Flow and Mixed Solvers: Pressure, Blocks, and Reliable Refinement

Take a tank filled with a thick incompressible fluid. Imagine stirring it so slowly that inertia is negligible. Its motion is controlled by viscosity, external forcing, and pressure. Viscosity resists deformation. Pressure supplies exactly the force needed to prevent local compression or expansion.

You could try to compute only the velocity and then reconstruct the pressure afterward. But pressure is not merely an output decoration. In the incompressible equations it acts as a Lagrange multiplier for the condition that velocity has zero divergence. Finding velocity and pressure together leads to a mixed variational problem and an indefinite block matrix.

This lecture will put the earlier ideas—weak forms, saddle-point stability, compatible finite elements, and Schur complements—into a single physical example. We will also separate three questions that are often conflated. Is the continuous problem well posed? Is the discretization stable? And can we solve the resulting matrix efficiently? A method must address all three.

## Pressure enforces zero divergence

Write the stationary Stokes equations for a fluid with positive constant viscosity nu. Negative nu times the Laplacian of velocity, plus the gradient of pressure, equals the applied body force. The divergence of velocity equals zero. For clarity, assume velocity vanishes on the entire boundary of a connected, bounded, sufficiently regular domain, and let the force be square integrable.

Multiply the momentum equation by a test velocity that also vanishes at the boundary, integrate, and move one derivative from the Laplacian onto the test velocity. The viscous part becomes nu times the integral of the gradient of velocity paired with the gradient of the test. The pressure-gradient term, after integration by parts, becomes minus the integral of pressure times the divergence of the test velocity.

We also test incompressibility: the integral of pressure test q times the divergence of the unknown velocity must be zero. Since zero equals its negative, we may use the same negative-divergence coupling in both rows. With that sign choice, the combined matrix is symmetric. Changing the sign of an entire constraint equation is legitimate; changing only one sign without tracking the convention is not.

For the velocity we use vector-valued H one functions with zero boundary values. For the pressure we use square-integrable scalar functions. But there is a catch. If the velocity vanishes on the boundary, the integral of its divergence over the domain is zero. Therefore a constant pressure contributes nothing to the weak momentum equation. The physical velocity does not care whether we add a constant to pressure everywhere.

To obtain a unique pressure, we fix the gauge. A convenient choice is to require pressure to have integral zero over the domain. That is why the pressure space is the mean-zero L two space. If we forget the gauge, the block matrix has a null vector with zero velocity and constant pressure. That is not evidence that the physical flow is indeterminate. It is an arbitrary reference level for pressure.

## The saddle block and its two jobs

After choosing finite-element bases, the Stokes equations have the block form: velocity stiffness matrix A in the upper left; a divergence coupling transpose in the upper right; the divergence coupling in the lower left; and zero in the lower right. With our sign convention the system is symmetric and indefinite.

The velocity stiffness A measures viscous deformation. With zero boundary velocity, it is positive definite on the discrete velocity space. The coupling block B represents the negative divergence operator tested against the pressure basis. The equation B times velocity equals zero enforces the discrete incompressibility condition.

This is the same algebraic arrangement we saw in a constrained two-variable quadratic problem. The field has a positive energy, and the multiplier has no independent quadratic energy. So the pressure can only be determined if the coupling is sufficiently rich to detect each allowed pressure mode.

The continuous condition is a positive inf–sup constant for divergence against mean-zero pressure. A discrete velocity-pressure pair must satisfy a corresponding inf–sup bound independent of mesh size. The energy also needs to control velocities in the discrete kernel of B. For homogeneous Dirichlet Stokes, the viscous form is coercive on the whole velocity space, so kernel coercivity is automatic; the substantial additional challenge is the divergence-pressure coupling.

We have already seen how an apparently natural equal-degree pair failed in a one-dimensional derivative model. That calculation does not prove that every equal-order Stokes discretization fails. Some use stable enrichments, different meshes, or consistent stabilization. It does explain why simply assigning the same ordinary continuous linear basis to velocity and pressure is not a generally reliable default.

A classical stable family is the Taylor–Hood choice: continuous piecewise quadratic velocity and continuous piecewise linear pressure, with the pressure mean fixed and the mesh satisfying the relevant shape and stability hypotheses. Extra velocity degrees of freedom give the divergence tests more room to detect pressure modes. It is not the extra polynomial degree by itself that proves stability; the result rests on an inf–sup theorem for the specified spaces and meshes.

## A flow produced entirely by pressure

There is a useful way to test whether we understand the roles of the variables. Consider a unit square and choose the forcing to be a constant vector pointing right. It is the gradient of the scalar function x. The stationary Stokes solution with zero boundary velocity can have velocity identically zero and pressure equal to x minus one half. The pressure gradient is precisely the force, while the fluid does not move.

Check both equations. Zero velocity has zero Laplacian and zero divergence. The pressure gradient points right with magnitude one. It balances the forcing exactly. The pressure has mean zero on the square because the average x-coordinate is one half.

This is not a curiosity. It exposes a distinction between inf–sup stability and pressure robustness. In the exact incompressible equations, adding a gradient field to the force can change pressure without changing velocity. A discrete velocity space that is only weakly divergence-free may react to some gradient forces with a nonzero velocity error, even if the velocity-pressure pair satisfies an inf–sup condition. Specialized pressure-robust schemes are designed to preserve that separation more faithfully.

For our simple linear pressure example, a suitable discrete pressure space that contains x minus one half can represent the balance exactly, so zero velocity is attainable. With a more complicated potential not represented in the pressure space, the issue becomes visible. The lesson is not that standard Taylor–Hood elements are invalid; it is that stability, approximation, local conservation, and pressure robustness are distinct properties.

## The Schur complement becomes a pressure equation

Now suppose the discrete velocity block A is invertible. The momentum row can be rearranged to express velocity in terms of the body force and pressure. Substituting into the constraint produces the pressure Schur complement S, equal to B times A inverse times B transpose.

S tells us how a candidate pressure force propagates through a viscous velocity solve and returns as measured divergence. On the mean-zero pressure space, if the discrete inf–sup condition holds, S is positive definite. Its smallest eigenvalue, with appropriate scaling and norms, is controlled by the square of the discrete inf–sup constant.

This has an immediate computational interpretation. We can solve the pressure Schur system, recover velocity from the momentum equation, and obtain the mixed solution. But computing A inverse as a dense matrix would squander the sparsity of the finite-element system. We instead apply an approximate inverse to vectors, typically through a preconditioned solve of the velocity block.

The exact Schur complement can itself be expensive. A common block preconditioner replaces A by an effective approximation to the viscous operator and S by a pressure-space mass operator with suitable viscosity scaling, provided theory or experiments establish spectral equivalence for the chosen formulation. In standard constant-viscosity Stokes with stable spaces and fixed boundary conditions, the Schur complement is comparable, in the right coefficient norms, to a pressure mass matrix scaled by inverse viscosity.

That comparison is not an identity. A wildly varying viscosity, changed boundary conditions, different pressure norms, or a nonstandard discretization can demand a more careful preconditioner. Equations that are mathematically well posed can still be computationally difficult at large scale if the preconditioner does not reflect their structure.

## Which iterative method can solve the block matrix?

There is another direct consequence of symmetry and indefiniteness. Conjugate gradients, in its standard form, assumes a symmetric positive-definite operator. It is suitable for the viscosity block A or for a properly defined positive-definite Schur complement S, but not for the entire symmetric-indefinite saddle matrix.

MINRES is designed for symmetric systems, including indefinite ones. With a symmetric positive-definite block preconditioner applied in a compatible way, it is a natural choice for the symmetric Stokes block system. GMRES is another option, particularly when nonsymmetric block preconditioners, convection, or other nonsymmetric terms enter the operator. Sparse direct solvers are also useful, especially for smaller problems or verification, but they must handle indefinite pivots.

It is essential to distinguish the preconditioner from the original equation. A block-diagonal approximation built from the velocity stiffness and pressure mass does not change the Stokes equations. It changes how rapidly an iterative method converges to their solution. By contrast, adding a penalty directly to the pressure-pressure block changes the discrete equations. That may be a legitimate stabilized method when carefully designed and analyzed, but it is not merely a new linear solver.

## Stability leads to an error estimate

Why do analysts work so hard to prove an inf–sup condition? Because it ties the discrete solution to the best available approximation in the chosen spaces. Under the ordinary boundedness, coercivity, compatibility, and mesh-uniform inf–sup assumptions, mixed Galerkin theory gives a quasioptimal estimate. The combined velocity and pressure error is bounded by a constant times the best velocity and pressure approximation errors in their appropriate norms.

The crucial words are that the constant does not blow up as the mesh is refined. Once that is established, standard interpolation estimates can turn smoothness of the exact solution and polynomial degree into convergence rates. Without a uniform inf–sup bound, a formal approximation estimate for each field separately cannot guarantee a reliable mixed answer.

Mesh size is only part of the story. The pressure gauge must be fixed or treated as a quotient space. Boundary conditions must be compatible with incompressibility. The regularity needed for a desired convergence order must actually hold. When corners, interfaces, or rough data degrade regularity, the numerical rate can be slower than a smooth-model calculation predicts. And the iterative solver must reduce algebraic error enough that it does not swamp the discretization error.

These are separate checks with different remedies. A poor interpolant calls for a better mesh or polynomial space. An inf–sup failure calls for a compatible discrete pair or a justified stabilization. A slow Krylov iteration calls for better preconditioning. A constant-pressure nullspace calls for pressure normalization, not for an arbitrary physical pressure penalty.

## Where mixed formulations lead

The larger story is that a partial differential equation does not merely dictate one list of unknowns. We choose variables according to what we want to control. A primal Poisson method puts temperature in H one and computes flux afterward. A mixed diffusion method puts flux in H div and the scalar in L two. Stokes flow uses an H one velocity and an L two pressure multiplier. In each case the differential operator between the spaces determines stability.

There are deeper geometric versions of this insight. Gradient, curl, and divergence fit into sequences of spaces connected by identities such as divergence of curl equals zero. Compatible numerical methods preserve enough of that structure to control spurious solutions. That is part of the motivation for finite-element exterior calculus.

But the practical conclusion is already useful. When faced with a coupled PDE, ask four questions. What is conserved or constrained? Which field should represent it directly? Can the discrete test fields detect every multiplier mode uniformly as the mesh changes? And does the linear solver respect the resulting block structure? Answer those, and the inf–sup condition stops looking like an isolated theorem. It becomes a design principle connecting physics, function spaces, discretization, and numerical computation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: Stokes weak form and block solvers

For a bounded, connected Lipschitz domain \(\Omega\subset\mathbb R^d\), \(d=2,3\), homogeneous Dirichlet velocity, positive constant viscosity \(\nu\), and appropriate data, set

\[
-\nu\Delta u+\nabla p=f,\quad\nabla\cdot u=0,\quad u|_{\partial\Omega}=0,
\quad\int_\Omega p=0.
\]

Use \(V=H^1_0(\Omega)^d\), \(Q=L^2_0(\Omega)\), and

\[
a(u,v)=\nu\int_\Omega\nabla u:\nabla v,\qquad
b(v,q)=-\int_\Omega q\,\nabla\cdot v.
\]

The weak equations are

\[
a(u,v)+b(v,p)=(f,v)\quad(\forall v\in V),\qquad
b(u,q)=0\quad(\forall q\in Q).
\]

The sign of the second row is chosen to make the assembled matrix symmetric; it remains the equation \(\nabla\cdot u=0\). With basis functions \(\{\phi_i\}\) and \(\{\psi_j\}\),

\[
\begin{bmatrix}A&B^T\\B&0\end{bmatrix}
\begin{bmatrix}U\\P\end{bmatrix}=
\begin{bmatrix}F\\G\end{bmatrix},\qquad
A_{ij}=a(\phi_j,\phi_i),\quad B_{ji}=b(\phi_i,\psi_j).
\]

Here \(G=0\) for incompressibility. After fixing the pressure gauge and assuming a stable discrete pair, \(A\) is SPD and \(B\) has full row rank. Elimination gives

\[
S=BA^{-1}B^T,\quad SP=BA^{-1}F-G,\quad U=A^{-1}(F-B^TP).
\]

For a pressure coefficient vector \(P\), \(P^TSP=\|B^TP\|_{A^{-1}}^2\). In a stable inf–sup pair, in the pressure-mass norm, \(S\) is spectrally comparable to \(\nu^{-1}\) times the pressure mass matrix, with equivalence constants depending on domain and uniform stability/continuity constants. This is the basis of a common block preconditioner, not an assertion that the two matrices are equal.

### A tiny pressure Schur matrix

For a toy velocity matrix \(A=\operatorname{diag}(2,1,1)\) and coupling

\[
B=\begin{bmatrix}1&1&0\\0&1&1\end{bmatrix},\qquad
S=BA^{-1}B^T=\begin{bmatrix}3/2&1\\1&2\end{bmatrix}.
\]

Its determinant is \(2\), and its eigenvalues are \((7\pm\sqrt{17})/4\), both positive. This is a finite-dimensional illustration of pressure modes coupling to velocity, not an assembled Stokes mesh.

### A pressure-only manufactured solution

On \(\Omega=(0,1)^2\), set \(u=0\), \(p=x-1/2\), \(f=(1,0)^T\). Then \(-\nu\Delta u+\nabla p=f\), \(\nabla\cdot u=0\), and \(\int_\Omega p=0\). In the continuous problem any gradient forcing \(\nabla\varphi\) can be balanced by a pressure change \(\varphi\) (after subtracting its mean), without changing the velocity, subject to the stated boundary setting.

### What an error theorem does and does not say

Under conforming approximation, bounded bilinear forms, suitable kernel coercivity and a mesh-uniform discrete inf–sup bound, a typical stable mixed estimate takes the form

\[
\|u-u_h\|_V+\|p-p_h\|_Q
\le C\left(\inf_{v_h\in V_h}\|u-v_h\|_V+
\inf_{q_h\in Q_h}\|p-q_h\|_Q\right)
\]

with \(C\) independent of \(h\). The precise constant and norm scalings depend on viscosity and the formulation. This is a discretization error statement; an iterative solver contributes additional algebraic error. It does not imply pointwise mass conservation, pressure robustness, or a fixed convergence rate without the corresponding extra hypotheses.

### Exercises with answers

1. **Gauge:** Show that replacing \(p\) by \(p+c\) leaves the weak Stokes momentum equation unchanged for tests in \(H_0^1(\Omega)^d\). **Answer:** \((c,\nabla\cdot v)=c\int_{\partial\Omega}v\cdot n=0\).
2. **Schur complement:** Multiply out the toy matrices to obtain \(S\). **Answer:** \(S_{11}=1/2+1=3/2\), \(S_{22}=1+1=2\), \(S_{12}=S_{21}=1\).
3. **MINRES versus CG:** Which matrix is indefinite? **Answer:** The complete saddle matrix; the velocity block A and, after gauge fixing and discrete stability, the Schur matrix S are SPD.
4. **Gradient forcing:** Verify that \(u=0\) and \(p=x-1/2\) solve Stokes with \(f=(1,0)\). **Answer:** \(\Delta 0=0\), \(\nabla p=(1,0)\), and \(\nabla\cdot 0=0\).
5. **Different failure modes:** Is reducing the linear residual sufficient to repair a zero discrete inf–sup constant? **Answer:** No; a converged algebraic solve cannot recover a pressure mode invisible to the discrete constraint operator.

### Sources and further reading

- Daniele Boffi, Franco Brezzi and Michel Fortin, [*Mixed Finite Element Methods and Applications* (2013)](https://link.springer.com/book/10.1007/978-3-642-36519-5), sections on Stokes problems, stable pairs, and preconditioning.
- FEniCS/DOLFINx, [*Stokes equations using Taylor–Hood elements*](https://docs.fenicsproject.org/dolfinx/main/python/demos/demo_stokes.html), which demonstrates block preconditioning, MINRES, direct solvers, and pressure nullspace handling with an explicit sign convention.
- FEniCS/DOLFINx, [*Mixed formulation of the Poisson equation*](https://docs.fenicsproject.org/dolfinx/main/python/demos/demo_mixed-poisson.html), for a contrasting \(H(\mathrm{div})\) formulation.
- Douglas N. Arnold, Richard S. Falk and Ragnar Winther, [*Finite element exterior calculus: From Hodge theory to numerical stability*](https://doi.org/10.1090/S0273-0979-10-01278-4) (2010), for compatible differential complexes.
- [Wikipedia: Ladyzhenskaya–Babuška–Brezzi condition](https://en.wikipedia.org/wiki/Ladyzhenskaya%E2%80%93Babu%C5%A1ka%E2%80%93Brezzi_condition), [Mixed finite element method](https://en.wikipedia.org/wiki/Mixed_finite_element_method), and [Uzawa iteration](https://en.wikipedia.org/wiki/Uzawa_iteration).

*Teaching connections:* `039000` introduces mixed diffusion and normal-flux conservation; `040000` derives the inf–sup and Schur ideas; `041000` exhibits a discrete pressure ghost mode and its stable repair; `linear-algebra:025000` discusses iterative SPD solvers for appropriate blocks.
