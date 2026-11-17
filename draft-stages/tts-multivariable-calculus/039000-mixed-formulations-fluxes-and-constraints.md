# Mixed Variational Formulations: When One Unknown Is Not Enough

**Track:** Multivariable Calculus from First Principles. **Focus:** primal and mixed Poisson formulations, flux as an independent field, integration by parts, boundary conditions, conservation, and a solved two-cell approximation.

<!-- BEGIN SPOKEN LECTURE -->

# Mixed Variational Formulations: When One Unknown Is Not Enough

Consider a thin rod carrying heat from one end to the other. The temperature is a scalar function. The heat flux tells us how much thermal energy crosses a point per unit time and area. We can compute the flux by differentiating temperature, once we have a sufficiently smooth temperature field. But what if the flux itself is the quantity that matters? A temperature approximation can look accurate while the amount of heat leaving one cell does not quite match the amount entering its neighbor. A conservation law notices that discrepancy even when a plot does not.

There is a way to put temperature and flux on equal footing, solving for them together. It introduces an extra unknown, but it also reveals a different variational structure. That structure will lead us to saddle-point matrices and, eventually, to the question of whether two finite-element spaces fit together.

We will use a one-dimensional diffusion equation to make every sign and boundary term visible. The same principles extend to Darcy flow, electromagnetism, elasticity, and incompressible fluids, although their function spaces and constraints are not all identical.

## The equation we already know

Let the rod occupy the interval from zero to one. The conductivity k is strictly positive. For now let k equal one, prescribe zero temperature at both endpoints, and suppose the interior contains a uniform source of one unit. The equation says that negative the second derivative of temperature equals one.

In the primal, or single-field, formulation, multiply the equation by a test function v that vanishes at both endpoints, integrate, and move one derivative from the temperature onto v. The result is that the integral of temperature prime times v prime equals the integral of v. We seek the temperature among zero-boundary functions with square-integrable first derivative.

The solution is the parabola: one half times x times one minus x. It is zero at both ends and rises to one eighth at the midpoint. Its slope is one half minus x. With conductivity one, the physical flux flowing to the right is minus that slope. Thus the flux is x minus one half. At the left endpoint it is negative one half, indicating heat leaving to the left; at the right it is positive one half, indicating heat leaving to the right. The flux increases with derivative one because one unit of heat is being produced per unit length.

Everything is consistent. But the primal variational problem treats flux as a derivative computed after solving for temperature. Suppose instead we want the flux as a primary unknown and conservation as an equation we impose directly.

## Split a second-order equation into two first-order equations

Name the flux q. Fourier's constitutive law says q equals minus k times the temperature gradient. Conservation says the divergence of q equals the source f. In one dimension, divergence is just an ordinary derivative, so q prime equals f.

Here we have two equations for two unknowns: temperature u and flux q. One of the equations says how the material responds, and the other says what is conserved. They play different roles. If the conductivity varies, the constitutive law changes while the conservation law retains exactly the same form.

We can write both equations weakly. Take the constitutive equation, rearranged as inverse conductivity times q plus the gradient of u equals zero. Multiply by a trial flux r, integrate, and integrate the temperature-gradient term by parts. What remains in the interior is the integral of inverse conductivity times q times r, minus the integral of u times the derivative of r. The boundary contributes temperature times outward normal flux of r.

For zero prescribed endpoint temperature, that boundary term disappears. The first mixed equation therefore asks that the flux inner product weighted by inverse conductivity equal the integral of u times r prime. The second equation asks that the integral of q prime times any scalar test v equal the integral of f times v.

The first equation is a weak constitutive law. The second is a weak conservation law. Neither has disappeared; we have redistributed derivatives between the variables and tests.

Notice a consequence that can initially seem backwards. The mixed formulation does not require u to have a square-integrable derivative. It only needs u to be square integrable. The derivative has moved onto the flux test function. In higher dimensions, the appropriate flux space consists of square-integrable vector fields whose divergence is also square integrable. This is called H div. It is not generally the same as requiring every component of flux to belong to H one.

On a mesh, that distinction is powerful. An H div conforming flux has a single normal component across a shared cell face, in the appropriate trace sense. Its tangential components need not match. Temperature, by contrast, can be represented by discontinuous cellwise polynomials. In the original primal formulation we typically chose a continuous approximate temperature and recovered a possibly less reliable flux by differentiation. In the mixed formulation we deliberately allocate continuity to the quantity carrying conserved material or energy across faces.

## Boundary conditions change their job

Here is a detail that is easy to lose when changing formulations. In the primal weak Poisson problem, prescribing temperature is built into the choice of the trial space, while prescribing a normal flux appears as a boundary term. In the mixed formulation, with flux as the H div variable, the roles exchange. A prescribed normal flux restricts the admissible flux field. A prescribed temperature enters through the boundary pairing in the constitutive equation.

Neither boundary condition has become more or less physical. The function spaces have changed, so the way each condition is imposed has changed. If a boundary is divided into a temperature portion and a flux portion, we must keep the corresponding tests and traces straight. We cannot simply erase every boundary term on a mixed-boundary problem.

For the all-zero temperature data of our example, the mixed equations are particularly simple. We can verify them with the exact parabola and exact affine flux. The conservation equation is immediate because the derivative of x minus one half equals one. For the constitutive equation, integrating u prime times r by parts yields exactly the same relation as the first mixed equation. No guesswork about signs is needed.

## A two-cell calculation

Now divide the rod into two equal cells. The dividing point is one half. Choose an approximate flux that is continuous and affine on each cell; it has values at the left endpoint, the midpoint, and the right endpoint. For temperature choose one constant number on each cell. The temperature is allowed to jump at the midpoint. At first this seems like an inferior approximation: surely a continuous parabola is better represented by a continuous piecewise linear function than by two constants. But our goal here is different. We want a flux respecting conservation, and we want to understand how the variables cooperate.

For this particular source, the exact flux happens to belong to the chosen flux space: x minus one half is globally affine. Its three nodal values are negative one half, zero, and positive one half. Its derivative on both cells is exactly one. Consequently the discrete conservation equation holds on each cell, not merely in some averaged equation over the entire domain.

What temperatures should accompany that flux? The average of our parabola over the left half is one twelfth. By symmetry, the average over the right half is also one twelfth. Let the two discrete temperatures have those values.

Why do these averages make the first mixed equation true? A piecewise affine flux test has a constant derivative on each cell. The integral of the exact temperature times that constant is unchanged if we replace the exact temperature with its average on the cell. Since the exact temperature and flux satisfy the continuous mixed equation, the chosen discrete fields satisfy every discrete test equation as well.

This gives a small but revealing exact calculation. The approximate temperature is piecewise constant and is not the exact parabola. But the flux is recovered exactly, and the cellwise conservation law is exact. Under the mixed formulation and these data, the pair is a legitimate discrete solution. The lesson is not that mixed methods always recover exact fluxes. It is that the choice of approximation spaces determines which physical and mathematical properties are represented directly.

## Why an extra unknown can improve an approximation

Every finite element method restricts an infinite-dimensional problem to finitely many degrees of freedom. The usual argument for choosing a space is approximation quality: can the basis functions resemble the exact solution as the mesh is refined? Mixed methods require a second question. Do the spaces cooperate with the differential equations tying the fields together?

In our rod, the derivative of a continuous piecewise affine flux is a cellwise constant. That matches the temperature test space and the piecewise constant source. Conservation can therefore be imposed cell by cell. In a higher-dimensional Raviart–Thomas construction, an analogous relation connects an H div conforming flux space to cellwise polynomial scalar fields. Normal flux degrees of freedom are shared across interfaces, which supports local conservation.

But a pair that looks natural by polynomial degree can fail in a more basic way. Perhaps it permits a scalar mode that the discrete divergence cannot detect. Then the equations cannot determine that scalar variable, even though both spaces approximate smooth functions separately. The obstacle is not approximation alone; it is stability of the coupling.

The mixed equations can be written as a block matrix. There is a block measuring flux against flux, another block coupling flux divergence to temperature, and a zero block where a temperature-only positive quadratic energy would otherwise appear. This is a saddle-point structure, not an ordinary positive-definite system on all unknowns. Directly applying an algorithm designed only for positive-definite matrices may fail.

One might ask why we don't simply eliminate the flux and return to the primal formulation. Sometimes we should. But elimination changes what is approximated and how conservation is enforced; it may also create a denser or differently conditioned matrix. Mixed methods earn their complexity when physical fluxes, constraints, local conservation, or robustness with variable material coefficients matter.

We have reached a precise question. When does a coupling between a flux space and a scalar space detect every scalar mode, with a bound that does not collapse as the mesh is refined? The mathematical answer involves an infimum and a supremum. Behind that formidable name is a simple idea: every proposed constraint must be testable by some admissible field with a controlled amount of effort.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: mixed Poisson with a fixed sign convention

For the Dirichlet problem in a bounded Lipschitz domain \(\Omega\), with \(0<k_0\le k(x)\le k_1\), set

\[
-\nabla\!\cdot(k\nabla u)=f,\qquad u|_{\partial\Omega}=g,\qquad q=-k\nabla u.
\]

Then \(k^{-1}q+\nabla u=0\) and \(\nabla\cdot q=f\). Define \(\Sigma=H(\operatorname{div};\Omega)\), \(W=L^2(\Omega)\); the Dirichlet mixed equations are

\[
\begin{aligned}
(k^{-1}q,r)-(u,\nabla\cdot r)&=-\langle g,r\cdot n\rangle_{\partial\Omega}&&\forall r\in\Sigma,\\
(\nabla\cdot q,v)&=(f,v)&&\forall v\in W.
\end{aligned}
\]

On a mixed boundary, only flux tests with the appropriate homogeneous essential normal-trace condition are used, and the Dirichlet pairing is restricted to its boundary portion. A prescribed normal flux is incorporated in an affine \(H(\mathrm{div})\) space. The boundary pairing is between compatible trace/dual-trace spaces, not necessarily an ordinary pointwise integral.

The first equation follows from

\[
(k^{-1}q,r)=-(\nabla u,r)=(u,\nabla\cdot r)-\langle g,r\cdot n\rangle.
\]

In one dimension, \(\Sigma=H^1(0,1)\), and \(q'=f\).

### The two-cell exactness calculation

Choose \(k=f=1\), \(g=0\), \(h=1/2\), and

\[
u(x)=\frac{x(1-x)}2,\quad q(x)=x-\frac12,\quad
\Sigma_h=\{r\in C^0[0,1]:r|_K\in P_1(K)\},\quad
W_h=\{v:v|_K\in P_0(K)\}.
\]

For \(K_1=[0,1/2]\) and \(K_2=[1/2,1]\),

\[
\bar u_1=\frac1{h}\int_{K_1}u(x)\,dx=\frac1{12},\qquad
\bar u_2=\frac1{h}\int_{K_2}u(x)\,dx=\frac1{12}.
\]

The candidate \(q_h=q\), \(u_h|_{K_i}=\bar u_i\) satisfies

\[
(q_h,r_h)-(u_h,r_h')=(q,r_h)-(u,r_h')=0
\]

because \(r_h'\) is constant on each cell and cell averaging preserves each \(\int_{K_i}u r_h'\). Moreover \((q_h',v_h)=(1,v_h)\) for every \(v_h\in W_h\). This exactness is specific to these data and spaces.

For any cell \(K\), testing conservation with its indicator gives the balance

\[
\int_{\partial K}q_h\cdot n=\int_Kf\,dx
\]

provided the load integral is assembled exactly; if numerical quadrature is used, the balance is relative to the quadrature-computed cell load.

### Exercises with answers

1. **Changing signs:** Define \(\sigma=k\nabla u=-q\). Show the resulting mixed equations have \((k^{-1}\sigma,r)+(u,\nabla\cdot r)=\langle g,r\cdot n\rangle\) and \(\nabla\cdot\sigma=-f\). **Answer:** Multiply both occurrences of \(q\) by \(-1\); both coupling signs change consistently.
2. **Flux balances:** Calculate \(q(1/2)-q(0)\) and \(q(1)-q(1/2)\). **Answer:** Both are \(1/2\), equal to the source integral over each half-cell.
3. **Why \(L^2\)?** Which derivatives of the scalar unknown occur in the mixed test equations? **Answer:** None; its derivatives are transferred to \(r\), so \(L^2\) is sufficient for the scalar variable.
4. **Boundary terms:** If \(g(0)=1\), \(g(1)=0\), what is the one-dimensional right-hand side of the first mixed equation? **Answer:** \(-[g r]_{0}^{1}=r(0)\), using outward normals implicitly in the bracket.
5. **Limits of exactness:** If \(f=x\), does the same \(P_1\) flux space contain the exact flux? **Answer:** In general no; \(q'=x\) makes \(q\) quadratic.

### Sources and further reading

- Daniele Boffi, Franco Brezzi and Michel Fortin, [*Mixed Finite Element Methods and Applications* (2013)](https://link.springer.com/book/10.1007/978-3-642-36519-5), particularly the mixed-elliptic formulation and \(H(\mathrm{div})\) chapters.
- FEniCS/DOLFINx, [*Mixed formulation of the Poisson equation*](https://docs.fenicsproject.org/dolfinx/main/python/demos/demo_mixed-poisson.html), for a computational realization with flux and discontinuous potential spaces; its sign convention defines flux with the opposite sign from ours.
- Douglas N. Arnold, Richard S. Falk and Ragnar Winther, [*Finite element exterior calculus: From Hodge theory to numerical stability*](https://doi.org/10.1090/S0273-0979-10-01278-4) (2010), for the broader idea of compatible spaces.
- [Wikipedia: Mixed finite element method](https://en.wikipedia.org/wiki/Mixed_finite_element_method), for terminology and related formulations.

*Teaching connections:* `multivariable-calculus:033000` derives the primal weak equation, `034000` constructs an ordinary Galerkin method, and `multivariable-calculus:029000` introduces finite-dimensional saddle-point blocks.
