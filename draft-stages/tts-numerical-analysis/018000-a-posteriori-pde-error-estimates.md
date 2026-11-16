# 018000 — A Posteriori Error Estimates for Finite Element Solutions

**Track:** Numerical Analysis. **Background:** weak Poisson problems, finite elements, Hilbert-space norms, integration by parts. **Central question:** how can we bound the error of a computed PDE solution when the exact solution is unknown?

<!-- BEGIN SPOKEN LECTURE -->

# A Posteriori PDE Error Estimates

A numerical solver produces an approximation to a partial differential equation. We can plot it, refine the mesh, and compare different numerical methods. But when the exact solution is unknown, how do we decide whether the computed field is accurate? Merely obtaining a small linear-system residual does not settle the question. The error may be hidden in the discretization, not in the algebraic solve.

A posteriori error estimation addresses this problem. Instead of predicting error in advance from an assumed mesh size, it uses the computed approximation and the differential equation to estimate or bound the error after the computation. The distinction is useful in simulations with sharp layers, irregular geometry, and local singularities, where some regions need much more resolution than others.

To see the logic, consider the Poisson equation with zero values prescribed on the boundary. The differential equation says that the negative Laplacian of the solution equals a given source function. Its weak form asks us to match gradients against every admissible test function. A finite element approximation enforces that equality only for test functions in a finite-dimensional space.

## The residual is a functional

Let u be the exact solution and u sub h the computed finite element solution. The error is their difference, which we do not know. But we do know how badly the computed solution satisfies the weak equation for an arbitrary test function. Subtract the computed gradient term from the source term and call the resulting linear functional the residual.

The error and residual are related exactly by the weak equation. The residual applied to a test function equals the inner product of the error gradient with the test gradient. Therefore, in the energy norm induced by the Poisson problem, the size of the error equals the dual norm of the residual over the full test space.

That identity is theoretically satisfying but not yet computationally convenient. Taking a supremum over all test functions is almost as hard as solving the original PDE. The practical breakthrough is to bound that dual norm by quantities computed on individual mesh elements and their shared faces.

## Two sources of residual

On each element of a finite element mesh, we can compute how strongly the approximation fails the differential equation. For a piecewise linear approximation, its Laplacian vanishes inside each element, so the element residual depends directly on the source. That may sound surprising: the numerical solution can be excellent while the element residual is not individually zero.

The missing information lives at element interfaces. The gradient of a piecewise linear function is constant within each element but jumps across neighboring elements. If we integrate the weak residual by parts on each element, interface terms appear. They involve the jump in the normal derivative of the computed solution.

Thus a useful residual estimator has two components. The element part measures equation mismatch inside cells, weighted by cell diameter. The face part measures jumps in normal flux, weighted by face size. Squaring and summing these indicators gives a global measure of where the discretization is failing.

The mesh weights matter because a residual with units of a source term cannot be compared directly with an error in a gradient norm. Multiplying by the appropriate powers of cell size gives the scaling required by interpolation and trace inequalities.

## Reliability and efficiency are different claims

An estimator is reliable if the true error is bounded above by a constant times the estimator, possibly plus explicitly identified data-approximation effects. Reliability means that a small estimator certifies a small error, up to the stated constant and hypotheses.

An estimator is efficient if it does not substantially overestimate the error, again with appropriate constants and local data oscillation terms. An estimator can be reliable but very pessimistic. Or it can correlate nicely with observed errors without providing a rigorous upper bound.

The constants depend on the problem and mesh regularity. For standard residual indicators, one generally assumes a shape-regular mesh and the proper variational setting. If the source has been approximated numerically, oscillation of that data enters the analysis. We should not silently remove such assumptions when reporting an error certificate.

## A one-element calculation

Consider the one-dimensional Poisson equation on the interval from zero to one, with a constant source equal to one and zero boundary values. The exact solution is half of x times one minus x, a simple parabola.

Now discretize using a single linear element covering the entire interval, with both endpoint values fixed to zero. The finite element space has no interior degree of freedom, so the computed solution is identically zero.

The computed element residual is the constant source one. Its weighted norm gives a residual indicator of one, using the usual unit element-length scaling. The exact energy error can also be computed: differentiate the parabola and integrate the square of the derivative. Its norm is the reciprocal of the square root of twelve, about twenty-nine hundredths.

The indicator is not equal to the error. It is larger, and a reliability constant connects them. This simple example explains why we should distinguish an estimator from an exact error and why constants are part of the mathematical statement.

## Adaptive refinement follows the estimator

Once we have a local error indicator for every element, we can refine the elements contributing most to the global estimate. Solve the discrete equation again on the refined mesh, recompute the indicators, and repeat. This is the basic solve, estimate, mark, refine cycle of adaptive finite elements.

The method allocates degrees of freedom where the solution needs them, rather than uniformly enlarging the whole problem. Near a corner singularity, that can lead to much better accuracy for the same computational budget. But achieving proven convergence or optimality for an adaptive algorithm requires additional analysis of marking rules, refinement, and estimator properties.

The key idea is to translate a global unknown error into local computable violations of the equation. For a linear coercive problem, the residual is not merely a warning light: it is mathematically tied to the energy error. A posteriori analysis turns a numerical solution into something we can interrogate, adapt, and—under stated conditions—certify.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(\Omega\subset\mathbf R^d\) be a bounded Lipschitz domain. For \(-\Delta u=f\) in Ω with homogeneous Dirichlet data, define \(V=H_0^1(\Omega)\), \(a(u,v)=\int_\Omega\nabla u\cdot\nabla v\,dx\), and \(F(v)=\int_\Omega fv\,dx\). Let \(u_h\in V_h\subset V\) be a conforming finite element solution, so \(a(u_h,v_h)=F(v_h)\) for all \(v_h\in V_h\).

Define the residual \(R(v)=F(v)-a(u_h,v)\). For \(e=u-u_h\), \(R(v)=a(e,v)\) and
\[\|\nabla e\|_{L^2(\Omega)}=\|R\|_{V'}:=\sup_{v\in V\setminus0}\frac{|R(v)|}{\|\nabla v\|_{L^2}}.\]
For a shape-regular simplicial mesh \(\mathcal T_h\), set \(R_K=f+\Delta u_h\) in each element K, and \(J_E=[\nabla u_h\cdot n_E]\) on each *interior* face. A standard residual estimator is
\[\eta^2=\sum_{K\in\mathcal T_h}h_K^2\|R_K\|_{L^2(K)}^2+\sum_{E\in\mathcal E_h^{\rm int}}h_E\|J_E\|_{L^2(E)}^2.\]
With conventional regularity and mesh assumptions, reliability gives \(\|\nabla e\|\le C_{\rm rel}\eta\); efficiency gives a reverse inequality up to data oscillation. Specific constants and additional oscillation terms depend on how f is represented and which estimator is used. A small *algebraic* residual for the discrete solve is not the same as a small *PDE* residual for u_h.

**One-element example:** \(\Omega=(0,1), f=1, u(0)=u(1)=0\). Then \(u(x)=x(1-x)/2\) and a single P1 element with both endpoints fixed gives \(u_h=0\). The residual indicator is \(\eta=1\), while \(\|u'-u_h'\|_2^2=\int_0^1(1/2-x)^2dx=1/12\). The indicator is not an exact equality.

### Exercises with answers

1. Why does Galerkin orthogonality imply \(R(v_h)=0\) for any discrete test function? **Answer:** both the exact and finite element weak equations agree on \(V_h\).
2. What is the element Laplacian of an affine P1 approximation within a mesh element? **Answer:** zero.
3. Where do gradient jumps enter the estimator? **Answer:** integration by parts separately on adjacent elements produces interior face terms.
4. Can a small linear solver residual rule out discretization error? **Answer:** no; the discrete equations can be solved accurately on an inadequate mesh.

### Reading and source notes

- [Rüdiger Verfürth, A Posteriori Error Estimation Techniques for Finite Element Methods](https://doi.org/10.1093/acprof:oso/9780199679423.001.0001), reliability, efficiency, and residual indicators (publisher reference).
- [Lawrence C. Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), weak solutions and coercive variational problems.
