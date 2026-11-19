# Corners and Singularities: When a Valid Solution Defeats a High-Order Error Bound

**Track:** Multivariable Calculus from First Principles. **Focus:** reentrant sectors, exact harmonic singularities, energy versus H-two regularity, cutoff solutions with smooth forcing, finite-element rate limits, and adaptive refinement.

<!-- BEGIN SPOKEN LECTURE -->

# Corners and Singularities: When a Valid Solution Defeats a High-Order Error Bound

Imagine that we solve the same Poisson equation on two metal plates. They have the same conductivity, the same kind of boundary condition, and smooth internal heating. One plate is a rectangle. The other has a square notch cut out of it, leaving an inward-pointing corner. We use the same linear finite-element method and reduce the mesh size in the same way. On the rectangle we may observe the expected first-order decrease of the energy error. On the notched plate, the error can decrease much more slowly.

It is tempting to blame the numerical solver. But the real difference may be geometric. The corner changes the regularity of the exact mathematical solution. In other words, the differential equation and the data can be innocent while the shape of the region prevents the solution from possessing the derivatives required by a familiar error theorem.

We can see this without running a simulation. There is an exact harmonic function near a corner whose degree of smoothness can be calculated by one-dimensional integrals. That calculation will also explain why improving the polynomial degree of the finite elements, without addressing the corner, may not produce the improvement one expects.

## A wedge with a prescribed opening angle

Take a planar sector, like a slice of a disk. Describe points by distance r from the tip and angle theta measured from one side. Let theta range from zero to an opening angle omega, and let r range from zero to one. The wedge has straight sides along theta equal to zero and theta equal to omega, plus an outer circular arc.

We seek functions that are harmonic inside the sector and vanish on its straight sides. In polar coordinates, the Laplacian has a radial second-derivative term, a radial first-derivative term divided by r, and an angular second-derivative term divided by r squared. Try a separated form: r raised to a power alpha, times sine of alpha theta.

Two facts make this a good guess. The sine vanishes at theta equal to zero, so one side automatically has zero temperature. If alpha times omega equals pi, the sine also vanishes on the other straight side. And when we substitute the product into the polar Laplacian, the radial contributions sum to alpha squared times r to the power alpha minus two, while the angular contribution cancels them exactly. Away from the tip, the Laplacian is zero.

Therefore alpha equals pi divided by omega gives a harmonic function that satisfies homogeneous Dirichlet conditions on both straight sides. It is a legitimate local model of a corner singularity. The geometry determines its exponent.

For a right angle, omega equals pi over two, so alpha equals two. The model function reduces to a smooth quadratic polynomial. For a flat angle, omega equals pi, so alpha equals one and the model is simply a linear coordinate function. But for an inward or reentrant angle of three pi over two, alpha equals two thirds. The function then behaves like r to the two-thirds power as we approach the corner.

It tends to zero at the tip, so the temperature itself does not blow up. Its gradient grows, however, like r to the power negative one third. Its second derivatives grow still faster, like r to the power negative four thirds. Which of these singularities is permitted by the weak energy theory?

## Energy can remain finite while second derivatives fail

A two-dimensional area integral in polar coordinates contains a factor of r. The squared gradient of the corner function behaves like r to the power twice alpha minus two. After including the area factor, the integral near the tip behaves like the integral of r to the power twice alpha minus one.

That integral is finite whenever alpha is positive. In our three-pi-over-two sector, alpha is two thirds, so the corner function has finite gradient energy. It belongs to H one locally all the way to the tip. It is a valid energy-scale weak solution, not an illegal infinite-energy field.

Now look at the second derivatives. Their squares behave, for this non-integer exponent, like r to the power twice alpha minus four. Including the area factor gives the integral of r to the power twice alpha minus three. With alpha equal to two thirds, the exponent is negative five thirds. That integral diverges at zero. The function is not H two near the corner.

No contradiction is involved. The weak Poisson equation requires only the gradient to be square integrable. Elliptic interior regularity can still hold everywhere a positive distance away from the tip. What fails is a global H two estimate reaching the reentrant boundary corner. The singularity is concentrated at the geometry's non-smooth point.

The precise opening angle matters. For a general wedge, alpha equals pi divided by omega. Widening the interior angle beyond pi makes alpha less than one, and the leading nontrivial corner mode loses H two regularity. This is why concave corners matter for estimates even when the coefficient and forcing are smooth.

## But what about boundary values on the curved edge?

Our harmonic model vanishes on the wedge's straight sides, but not generally on its outer circular arc. If we want a genuine zero-Dirichlet Poisson problem on the entire truncated wedge, we can modify it without removing the singularity.

Choose a smooth radial cutoff. Make it equal one for points very close to the tip, and make it vanish before reaching the outer arc. Multiply the harmonic corner function by this cutoff. The resulting function vanishes on both straight sides and on the outer boundary. Near the tip it is unchanged, so it still has finite H one energy and still fails to be H two.

Now calculate its forcing by taking negative the Laplacian. Close to the tip the cutoff is constant and the harmonic function has zero Laplacian. Far from the tip the cutoff is zero. The only contribution comes from a ring where the cutoff changes, away from the singular point. There, both the cutoff and the original harmonic function are smooth. Thus the forcing is smooth and bounded, and can be chosen to vanish near the tip.

We have produced a completely legitimate boundary-value problem with zero Dirichlet data, a smooth forcing term, and a unique H naught one weak solution that is not globally H two. The breakdown is caused by the reentrant corner, not by bad data or by a failure of weak existence.

This example is stronger than pointing to a rough numerical picture. It rules out an overgeneral theorem: one cannot claim that every weak solution of the Dirichlet Poisson problem with an L two source on every bounded Lipschitz domain belongs to H two. A reentrant polygon or sector gives a counterexample.

## What the singularity does to a finite-element mesh

For continuous piecewise-linear finite elements on a shape-regular quasi-uniform mesh, the standard energy-error estimate based on H two regularity is proportional to h times the H two seminorm of the exact solution. But here that seminorm is infinite. The theorem tells us nothing, and the numerical error need not decay like h.

To see the scale of the difficulty, focus on one small triangle adjacent to the corner, with diameter h. Across that element, our singular function has size proportional to h to the power alpha. Its gradient has size proportional to h to the power alpha minus one. The triangle has area proportional to h squared. Squaring the gradient and integrating therefore produces a scale of h to the power twice alpha. Taking a square root gives an energy scale of h to the power alpha.

An affine finite-element function has a constant gradient on a triangle. It cannot reproduce the varying singular gradient exactly. When we rescale the triangle to a fixed reference shape, the best constant-gradient approximation still leaves a positive error. That gives a lower bound of the same h-to-the-alpha scale on a regular corner element. With alpha equal to two thirds, we should not expect an energy error better than order h to the two-thirds from an ordinary quasi-uniform piecewise-linear discretization of this model.

There is a complementary upper-bound viewpoint. The corner function belongs locally to H one plus s for every s strictly smaller than two thirds, but it does not reach the regularity demanded by the H two interpolation estimate. Fractional-order approximation theorems therefore support energy bounds of order h to the s for each such s. For this explicit singular model and appropriate quasi-uniform meshes, more specialized arguments often identify the observed sharp scale h to the two-thirds. The exact statement depends on the mesh and the problem; the safe conceptual point is that the corner exponent, not just the polynomial degree, limits a uniform-mesh rate.

The usual L two error estimate needs another step. It often uses a dual or adjoint elliptic problem and a regularity estimate for that dual solution. On a domain with the same reentrant corner, the dual problem can have the same regularity obstruction. So it is not justified simply to claim the smooth-domain second-order L two rate after the energy estimate has already failed.

## Why local refinement can help

The singular gradient is large near the tip and much calmer away from it. A uniform mesh spends the same geometric resolution in regions that do not need it. An adaptive method can put smaller elements near the corner and larger elements elsewhere, distributing the degrees of freedom according to the spatial structure of the error.

For a fixed polynomial degree, carefully graded meshes can recover more favorable approximation behavior, sometimes including rates associated with smooth solutions when error is measured against the number of degrees of freedom under suitable conditions. But this is not an automatic promise for every refinement strategy. Element shape, grading, marking criteria, and the norm being measured all matter.

There are at least three distinct numerical strategies. We can grade the mesh based on known corner exponents. We can use an a posteriori error estimator to locate large residual or flux mismatch contributions and refine adaptively. Or we can enrich the approximation space with a carefully chosen singular function. Each strategy addresses the missing approximation power near the corner in a different way.

An equilibrated-flux estimator is especially relevant because it can certify energy error without pretending that the exact solution is H two. It relies on a conservation identity and a reconstructed flux, not on an unavailable second derivative. This connects the present geometric lesson to the earlier mixed-flux and numerical-analysis lectures.

## Geometry becomes part of the theorem

We are now in a position to sort several statements that are easy to confuse. On a bounded Lipschitz domain, weak existence for the zero-Dirichlet Poisson problem follows from coercivity. Interior H two regularity holds under appropriate coefficient assumptions away from the boundary. Global H two regularity may require a smoother boundary or special geometry, such as a convex polygon for the scalar Dirichlet Laplacian. A reentrant corner can destroy the global conclusion while leaving existence untouched.

Even saying that the source is smooth does not cure every singularity. The cutoff example gave us smooth forcing and still no global H two solution. Conversely, a function may be very smooth at most locations and still fail an integral regularity norm because of what happens in an arbitrarily small region near one corner.

The right workflow follows the logic of these distinctions. Prove that the weak problem is well posed. Determine which regularity its operator, coefficients, domain, and boundary data actually give. Choose interpolation estimates appropriate to that regularity. Only then announce a convergence rate. If the rate is too slow, modify the approximation strategy where the mathematical solution demands it.

A finite-element solver has not failed because it cannot produce a first-order energy error on a concave domain. The wrong claim would be that first order was guaranteed without the missing H two hypothesis. By understanding a single exact function on a sector, we can diagnose that mistake before ever compiling a numerical model.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Sector solution and regularity test

Let \(\Omega_\omega=\{(r,\theta):0<r<1,\ 0<\theta<\omega\}\), \(\alpha=\pi/\omega\), and

\[
u_s(r,\theta)=r^\alpha\sin(\alpha\theta).
\]

In polar coordinates \(\Delta=\partial_{rr}+r^{-1}\partial_r+r^{-2}\partial_{\theta\theta}\). Then

\[
\Delta u_s
=\bigl[\alpha(\alpha-1)+\alpha-\alpha^2\bigr]r^{\alpha-2}\sin(\alpha\theta)=0
\]

for \(r>0\), with zero traces on the straight edges. For \(\omega=3\pi/2\), \(\alpha=2/3\). Near the tip,

\[
\int_{\Omega_\omega\cap\{r<\varepsilon\}}|\nabla u_s|^2
\asymp \int_0^\varepsilon r^{2\alpha-1}\,dr<\infty,
\qquad
\int|D^2u_s|^2\asymp\int_0^\varepsilon r^{2\alpha-3}\,dr=\infty.
\]

Here \(\asymp\) suppresses finite positive factors from angular integration. The Hessian expression applies to the noninteger exponent \(\alpha=2/3\) in this example; do not apply it mechanically to cases where the harmonic function becomes an affine polynomial.

### Smooth forcing with homogeneous boundary data

Choose \(\chi\in C^\infty([0,1])\), equal to 1 for \(r\le1/4\), and to 0 for \(r\ge1/2\). Set \(u=\chi(r)r^\alpha\sin(\alpha\theta)\). Then \(u\in H_0^1(\Omega_\omega)\setminus H^2(\Omega_\omega)\) for \(\alpha=2/3\), while

\[
f=-\Delta u=-\bigl[\chi''(r)r^\alpha+(2\alpha+1)\chi'(r)r^{\alpha-1}\bigr]\sin(\alpha\theta)
\]

is smooth, supported in an annulus away from the singular tip, and bounded. The function \(u\) is the unique weak solution of the homogeneous Dirichlet problem with this forcing.

### Finite-element scaling and qualifications

On a shape-regular corner triangle \(T_h=hT_1\), changing variables \(x=hy\) for the homogeneous corner mode yields

\[
\inf_{p\in\mathbb P_1(T_h)}\|\nabla(u_s-p)\|_{L^2(T_h)}
=h^\alpha\inf_{q\in\mathbb P_1(T_1)}\|\nabla(u_s-q)\|_{L^2(T_1)}.
\]

The last infimum is strictly positive for the non-affine mode. Thus the energy error of any conforming P-one approximation on this element is at least \(c h^\alpha\). Standard fractional interpolation gives upper estimates \(O(h^s)\) for \(s<\alpha\) under appropriate domain and mesh assumptions; exact endpoint rates require additional analysis.

### Exercises and answers

1. **Opening angle.** Find the leading Dirichlet harmonic exponent for \(\omega=4\pi/3\). **Answer:** \(\alpha=3/4\), so the leading nontrivial corner mode has finite H one energy but fails H two.
2. **Smooth wedge.** For \(\omega=\pi/2\), identify the harmonic function. **Answer:** \(r^2\sin(2\theta)=2xy\), a smooth polynomial.
3. **Why the cutoff matters.** Where is \(-\Delta(\chi u_s)\) nonzero? **Answer:** Only where \(\chi'\) or \(\chi''\) is nonzero, a fixed annulus away from the corner.
4. **Numerical theorem audit.** Which assumption is missing if one claims \(\|\nabla(u-u_h)\|_2\le Ch\|u\|_{H^2}\) for the cutoff corner solution? **Answer:** \(u\notin H^2\), so that bound has an infinite right side and supplies no rate.
5. **Rate inference.** Does a best-approximation lower bound on one corner triangle prove that every adaptive method is limited to \(h^{2/3}\)? **Answer:** No. The bound is for a quasi-uniform corner element of diameter h. Graded or adaptive meshes change the local element sizes and the complexity measure.

### Sources and further reading

- Long Chen, University of California Irvine, [*Adaptive Finite Element Methods*](https://www.math.uci.edu/~chenlong/ifemdoc/afemdoc.html), the L-shaped domain example \(r^{2/3}\sin(2\theta/3)\), and mesh refinement.
- Gautam Iyer, Carnegie Mellon University, [*Elliptic equations*](https://www.math.cmu.edu/~gautam/c/2026-632/notes/elliptic-equations.html), interior regularity and boundary distinctions.
- Hyung Jun Choi, [*A numerical solution for the inhomogeneous Dirichlet boundary value problem on a non-convex polygon*](https://doi.org/10.1016/j.amc.2018.08.011) (2019), corner singularities and regular/singular decomposition.
- [Wikipedia: Finite element method](https://en.wikipedia.org/wiki/Finite_element_method); [Wikipedia: Elliptic partial differential equation](https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation), broader context.
- Companion within this library: `numerical-analysis:018000` derives equilibrated-flux energy estimators without assuming global H-two smoothness.
