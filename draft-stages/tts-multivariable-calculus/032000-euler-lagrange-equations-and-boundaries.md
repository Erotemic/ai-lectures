# Euler–Lagrange Equations: The Differential Equation and the Boundary Terms

**Track:** Multivariable Calculus from First Principles. **Focus:** integration by parts, the fundamental lemma, natural boundary conditions, isoperimetric constraints, and the distinction between energy minima and stationary actions.

<!-- BEGIN SPOKEN LECTURE -->

# Euler–Lagrange Equations: The Differential Equation and the Boundary Terms

A stretched string can be pinned to a wall, attached to a spring, or left free. All three systems may obey the same differential equation in the middle of the string, yet their shapes can be different. The distinction lives at the boundary. This is one reason the calculus of variations is more than a recipe for differentiating an integral: the terms left behind by integration by parts tell us which physical or geometric problem we are actually solving.

We will derive the Euler–Lagrange equation carefully, keep track of its boundary terms, and solve a loaded string with an elastic end support. Then we will add an integral constraint and see an ordinary Lagrange multiplier reappear in a problem whose unknown is an entire function.

## A general energy density

Consider a curve u on an interval from a to b. Assign it an energy by integrating a function of three things: the location x, the height u of x, and the slope u prime of x. Call the integrand F. In a model of a mechanical string, F might contain a squared-slope penalty and a term representing a distributed force. In other applications, it could measure arc length, elastic deformation, or deviation from data.

Choose an admissible perturbation eta, and replace u by u plus t eta. Differentiate the energy with respect to t at zero. The chain rule gives two terms: the partial derivative of F with respect to its height argument, multiplied by eta, and the partial derivative with respect to its slope argument, multiplied by eta prime. Integrate their sum across the interval.

The second term contains eta prime, not eta. Integration by parts transfers that derivative away from the perturbation. The interior integral then has a coefficient multiplying eta: the derivative of F with respect to height, minus the derivative with respect to x of the partial derivative of F with respect to slope. The leftover boundary expression is the slope derivative of F, multiplied by eta, evaluated at the two endpoints, with opposite signs.

If both endpoint values of u are fixed, every allowed eta is zero there. The boundary expression vanishes. Stationarity then requires the interior coefficient to vanish for every compactly supported test function. Under suitable smoothness, the fundamental lemma gives the Euler–Lagrange equation: derivative of F with respect to height minus the total x derivative of its slope derivative equals zero.

The phrase total derivative matters. The slope derivative of F is itself evaluated along the curve. It can depend on x, u, and u prime. Differentiating it with respect to x includes those dependencies. Writing an ordinary partial derivative in the wrong place can omit terms.

This equation is necessary for a smooth interior stationary curve under the hypotheses of the derivation. It is not by itself a guarantee of a minimum. For a nonconvex integrand the same Euler–Lagrange equation can describe maxima or saddle points. In mechanics, an action that is stationary under variation need not be a minimum even when the associated motion is physically relevant.

## Fixed and free ends are different problems

Return to the energy of a string with unit stiffness under unit load: integrate one half of the squared slope minus the height. Fix its left endpoint at zero, but do not fix its right endpoint. The interior equation remains negative u double prime equals one, because we can test with perturbations supported away from the ends.

What happens at the right end? We may choose a perturbation that is zero at the left endpoint but nonzero at the right. The boundary contribution is u prime at the right endpoint multiplied by that freely chosen perturbation value. For stationarity under all such perturbations, the slope at the right endpoint must be zero. This is a natural boundary condition, not an extra condition added after the derivation.

The general solution of the interior equation is negative one half x squared plus C times x plus D. Fixing the left endpoint gives D zero. The natural right-end condition gives C one, so the right endpoint rises to one half. Contrast this with the string pinned at both ends: there C equals one half and the right endpoint stays at zero. Both curves obey exactly the same interior differential equation. The boundary conditions select different solutions.

The distinction between essential and natural boundary conditions is useful. An essential, or Dirichlet, condition is built into which trial functions are allowed: a prescribed value at an endpoint is not permitted to vary. A natural, or Neumann-type, condition arises from the boundary term when the corresponding endpoint is allowed to move. One must still specify the physical model carefully: not every mathematical free boundary corresponds to a zero physical force, especially if the energy includes explicit boundary work.

## A string attached to a spring

Let us improve the right-end model. The left endpoint is still pinned, and a uniform load still pulls on the string. But now the right endpoint is connected to a spring that resists displacement from zero. Add one half of kappa times the square of the right-end height to the energy. Kappa is positive spring stiffness. We have not changed the energy density in the interior; we have added a boundary energy.

Vary the curve. The interior calculation is unchanged. The integral's boundary term contributes u prime at the right end times eta there. The spring contributes kappa times the right-end height times eta there. Stationarity requires their combined coefficient to vanish. Thus u prime at one plus kappa times u at one equals zero.

This is a Robin boundary condition. It mixes value and derivative. The mathematical name is less important than its meaning: the elastic support allows displacement, but produces an opposing force proportional to that displacement.

Take kappa equal to two. The interior solution is again negative one half x squared plus C x. Its slope at one is C minus one, while its height at one is C minus one half. The boundary condition says C minus one plus twice C minus one half equals zero. That gives three C equals two, or C equal to two thirds. The right-end height is then one sixth, and the right-end slope is negative one third. The slope force and spring force cancel: negative one third plus twice one sixth equals zero.

We can see the whole family of models by varying kappa. Zero spring stiffness recovers a free end, with right-end slope zero. Large positive stiffness keeps the right-end displacement close to zero. In the limit, the result approaches the doubly pinned solution, though a limit of boundary conditions should not be confused with an exact prescribed value at finite stiffness.

For a right-end applied load g, we would subtract g times the right-end height from the energy. The resulting condition becomes u prime at one plus kappa times u at one equals g. The natural boundary term records the applied force as directly as the interior equation records the distributed load.

## A different constraint: prescribed total area

Boundary values are not the only possible constraints on a function. Suppose both endpoints are pinned at zero, and we want the area under the graph to equal a prescribed number m. We may be choosing the shape of a flexible profile while requiring a fixed total amount of material or displacement.

Minimize one half the integral of squared slope subject to the integral of u being m. The constraint is a single scalar equation on the space of curves. We can introduce an ordinary scalar Lagrange multiplier lambda, just as in constrained multivariable optimization. Add lambda times the integral of u minus m to the objective, then vary the curve.

The interior Euler–Lagrange equation says negative u double prime plus lambda equals zero. In other words, u double prime is constant. The endpoint values again make u a multiple of x times one minus x, and the area condition fixes that multiple. In fact u of x equals six m times x times one minus x, and the corresponding multiplier is negative twelve m.

Why is the solution an arch, rather than a constant-height strip? A nonzero constant would violate the pinned endpoints. To produce the prescribed area at the lowest squared-slope cost, the curve distributes its change smoothly over the interval. The Lagrange multiplier represents how much the optimal energy changes when we alter the required area, with a sign determined by how we wrote the constraint.

There is a qualification. In infinite-dimensional settings, multiplier conclusions require appropriate regularity or constraint qualification. Here the area functional is a nonzero continuous linear functional, so the familiar multiplier argument is justified. More complicated constraints on functions can fail the needed regularity, just as finite-dimensional constraints can.

## From a curve to a field

The same calculation works in several spatial dimensions. Let u be a scalar field on a region, and assign it an energy equal to one half the integral of squared gradient, minus the integral of a source f times u. The first variation in the direction eta is the integral of the gradient of u dotted with the gradient of eta, minus the source term.

If the field is smooth and we integrate by parts over the region, we obtain the interior equation negative Laplacian of u equals f. The boundary contribution is the outward normal derivative of u multiplied by eta. At a part of the boundary where the value of u is prescribed, eta must vanish. Where eta is free, the normal derivative has to match the specified boundary flux or force, including any contribution from explicit boundary energy.

This is the multi-dimensional analogue of the string's fixed end and spring end. It is also a bridge to partial differential equations. The first variation already gives a meaningful integral identity without requiring second derivatives of u to exist pointwise. That identity will be our starting point for weak solutions.

Pure Neumann conditions contain a caution. If all boundary values are free and the energy only penalizes gradients, adding a constant does not change the gradient energy. For a steady Poisson problem, total interior source and prescribed outward flux must satisfy a compatibility condition. Even when they do, the solution is determined only up to an additive constant unless we impose a normalization such as zero mean. This is not a technical nuisance: it is the same flat constant direction we encountered in the previous lecture.

## Boundaries are part of the mathematics

When you derive Euler–Lagrange equations, there are really three objects to carry through the computation: the energy, the admissible class, and the resulting first variation. The interior differential equation is only part of the answer. The endpoint or boundary terms reveal what was fixed, what was free, and what forces or penalties were present. Integral constraints introduce multipliers; nonlinear energies raise second-variation questions; the same interior equation can support different solutions under different boundary assumptions.

The next step is to take the integral equation seriously in its own right. Sometimes a solution has a corner or an interface at which a classical second derivative does not exist. The weak equation can still be precise, stable, and useful, provided we choose the right function space and retain the correct boundary information.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### General Euler–Lagrange derivation

Suppose \(J(u)=\int_a^b F(x,u,u')\,dx\) and the relevant functions are smooth enough. Set \(u_t=u+t\eta\). Then

\[
\begin{aligned}
\delta J(u)[\eta]
&=\int_a^b\big(F_u\eta+F_p\eta'\big)\,dx\\
&=\int_a^b\left(F_u-\frac{d}{dx}F_p\right)\eta\,dx
 +\left[F_p\eta\right]_a^b,
\end{aligned}
\]

where \(F_p=\partial F/\partial p\), evaluated at \((x,u(x),u'(x))\). If \(\eta\) vanishes at both ends, the fundamental lemma gives \(F_u-dF_p/dx=0\). If \(\eta(b)\) is free, the natural boundary condition is \(F_p(b)=0\) unless the functional contains separate boundary terms.

For \(J(u)=\int_0^1(\frac12|u'|^2-u)\,dx+\frac\kappa2(u(1)-d)^2-g u(1)\), with \(u(0)=0\),

\[
-u''=1,\quad u(0)=0,\quad
u'(1)+\kappa\big(u(1)-d\big)=g.
\]

With \(\kappa=2,d=g=0\): \(u(x)=-\tfrac12x^2+\tfrac23x\), \(u(1)=1/6\), \(u'(1)=-1/3\). Notice the right boundary condition follows from varying the *boundary energy*; it is not chosen independently afterward.

### Isoperimetric constraint

Minimize \(\frac12\int_0^1|u'|^2\,dx\) over \(H_0^1(0,1)\) subject to \(\int_0^1u\,dx=m\). Define

\[
\mathcal L(u,\lambda)=\frac12\int_0^1|u'|^2\,dx+\lambda\left(\int_0^1u\,dx-m\right).
\]

The weak stationarity identity is \(\int u'\eta'+\lambda\eta=0\), yielding \(-u''+\lambda=0\). Thus

\[
u(x)=6m x(1-x),\qquad \lambda=-12m,\qquad
\min J=\frac12 (6m)^2\int_0^1(1-2x)^2\,dx=6m^2.
\]

The optimized value satisfies \(d(6m^2)/dm=12m=-\lambda\), consistent with differentiating \(\mathcal L=J+\lambda(\int u-m)\) with respect to \(m\).

### Higher-dimensional weak and boundary equations

For a sufficiently regular bounded domain \(\Omega\), with \(\partial\Omega=\Gamma_D\cup\Gamma_N\), consider

\[
E(u)=\tfrac12\int_\Omega|\nabla u|^2\,dx-\int_\Omega f u\,dx-\int_{\Gamma_N}g u\,ds.
\]

Admissible variations vanish on \(\Gamma_D\). Formally,

\[
\delta E(u)[v]=\int_\Omega\nabla u\cdot\nabla v-fv\,dx-\int_{\Gamma_N}gv\,ds,
\]

so the classical equations are \(-\Delta u=f\) in \(\Omega\), \(u=u_D\) on \(\Gamma_D\), and \(\partial_nu=g\) on \(\Gamma_N\). Pure Neumann problems require \(\int_\Omega f\,dx+\int_{\partial\Omega}g\,ds=0\) and have additive-constant freedom.

### Exercises with answers

1. **Free end:** Derive the solution of \(-u''=1\), \(u(0)=0\), \(u'(1)=0\). **Answer:** \(u=x-x^2/2\).
2. **Spring:** Solve the same problem with \(u'(1)+k u(1)=0\). **Answer:** \(u=-x^2/2+C x\) with \(C=(1+k/2)/(1+k)\) for \(k\ge0\).
3. **Area constraint:** Verify \(\int_0^1 6m x(1-x)\,dx=m\). **Answer:** \(6m(1/6)=m\).
4. **Boundary flux:** For homogeneous Neumann data, why is \(f=1\) incompatible on a bounded domain? **Answer:** Integrating \(-\Delta u=1\) gives \(-\int_{\partial\Omega}\partial_nu=|\Omega|\), contradicting zero flux.

### Sources and further reading

- L. C. Evans, [*Mathematical Methods for Optimization* / calculus-of-variations notes](https://math.berkeley.edu/~evans/math%20195%20notes.pdf), on Euler–Lagrange equations, variations, and free-end transversality.
- Luca Heltai, [*Model Problems and the Ritz–Galerkin Method*](https://luca-heltai.github.io/nmpde/lectures/lecture-01/), for the weak and variational Poisson model.
- [Wikipedia: Euler–Lagrange equation](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation) and [Neumann boundary condition](https://en.wikipedia.org/wiki/Neumann_boundary_condition), for terminology.

*Teaching connections:* `multivariable-calculus:027000` and `030000` develop finite-dimensional multipliers and sensitivity; `topology-geometry:009000` develops integration and boundary orientation; `differential-equations:019000` studies stationary action in geometric PDE dynamics.
