# 062000 — A Differential Equation Without Second Derivatives: Weak Poisson Problems

**Track:** Analysis from First Principles. **Background:** H-one Sobolev spaces, integration by parts, bounded linear functionals. **Central question:** How can we prove existence and uniqueness of a boundary-value solution that may not be twice differentiable?

<!-- BEGIN SPOKEN LECTURE -->

# A Differential Equation Without Second Derivatives: Weak Poisson Problems

Suppose a thin elastic sheet is fastened along its edge and pushed by a distributed load. Its equilibrium shape is often described by Poisson's equation: minus the Laplacian of the displacement equals the applied force. In ordinary calculus language, the Laplacian means adding the second derivatives in all spatial directions. But if the load is rough, why should the shape have classical second derivatives everywhere?

A weak formulation avoids demanding more differentiability than the physics supplies. It begins with an energy principle. A stretched sheet stores energy proportional to the square of its gradient: steep slopes cost energy. The applied load does work against the displacement. Equilibrium is the configuration that balances these effects, subject to the sheet remaining fixed at its boundary.

To derive the weak equation, multiply the classical Poisson equation by an arbitrary smooth test displacement that vanishes at the boundary, and integrate over the region. Integration by parts moves one derivative from the unknown displacement to the test function. The result says: the integral of the dot product of their gradients equals the integral of the force times the test function.

Notice what has changed. The unknown no longer needs two classical derivatives. It needs a weak first derivative with finite squared integral. That puts it in the Sobolev energy space H zero one, which incorporates the zero boundary condition. The test function is taken from the same space by density, so we can test against many more functions than the initial smooth probes.

In one dimension we can make the result explicit. On the interval from zero to one, hold the displacement at zero at both ends and apply a uniform unit load. The classical solution is one half times x times one minus x. Its graph is a parabola rising to one eighth at the midpoint. Differentiate once: the slope is one half minus x. The slope is square integrable, so the solution belongs to the energy space.

Test the weak equation with the solution itself. The left side is the integral of the squared slope. The right side is the integral of the load times the displacement. This is the energy identity. It says the work applied by the load equals the energy measured by the gradient in this normalization. The identity also gives control of the size of the solution in terms of the forcing.

Now let the forcing be an arbitrary square-integrable function rather than a constant. We may not have a formula for the solution. But a powerful theorem, Lax–Milgram, can prove there is a unique weak solution without solving the differential equation point by point.

Here is the idea. Define a bilinear form that takes two candidate functions and integrates the dot product of their gradients. This form is continuous: Cauchy–Schwarz bounds its absolute value by the product of the energy norms. It is coercive: when we insert the same function twice, we obtain the squared gradient norm, which controls the full H zero one norm through Poincaré's inequality. The forcing defines a bounded linear functional by integration against a test function. Lax–Milgram says there is exactly one function in the energy space whose pairing through the bilinear form matches that forcing functional for every test function.

The abstract theorem is not magic. On a Hilbert space, a continuous coercive bilinear form behaves like a stable invertible positive operator. It excludes directions along which the energy could vanish without the function itself vanishing. Once the boundary condition removes the constant-function ambiguity, the energy gives enough control to make the solution both unique and stable.

Consider what would happen if we removed the boundary condition and used a pure Neumann problem, fixing only the normal derivative at the boundary. Then adding any constant to a solution would produce another solution. The gradient energy cannot see constants. Uniqueness fails unless we impose an additional normalization such as zero mean, and the forcing must satisfy a compatibility condition. This resembles the Fredholm alternative: a kernel creates an obstruction to uniqueness and an orthogonality condition for solvability.

Finite-element methods are built directly from the weak formulation. Instead of trying to approximate second derivatives at every point, choose a finite-dimensional set of candidate displacement functions. Require the weak equation only for test functions in that finite-dimensional space. The resulting algebraic system uses integrals of gradients and load terms. When the energy form is coercive, the discrete problem is a stable approximation of the continuous one.

A weak solution is not necessarily a classical one. On a smooth domain with a smooth forcing, further regularity theorems can show the solution has more derivatives. On a domain with corners, with discontinuous coefficients, or with rough loading, that improvement may be limited. Existence in the energy space and regularity beyond it are two separate mathematical questions.

This is the principal lesson of weak PDE theory. We can formulate an equation in a way that reflects the actual energy estimates available. We can then prove existence, uniqueness, and stability before asking whether a twice-differentiable graph exists. The weak formulation is not a compromise made for computers. It is often the natural mathematical expression of the underlying balance law.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(\Omega\subset\mathbb R^d\) be bounded Lipschitz, \(f\in L^2(\Omega)\). Find \(u\in H^1_0(\Omega)\) with
\[a(u,v)=F(v)\quad\forall v\in H^1_0(\Omega),\qquad a(u,v)=\int_\Omega\nabla u\cdot\nabla v,\quad F(v)=\int_\Omega fv.\]
Cauchy–Schwarz and Poincaré show \(|a(u,v)|\le\|u\|_V\|v\|_V\), \(a(v,v)=\|v\|_V^2\), and \(|F(v)|\le C_P\|f\|_2\|v\|_V\), with \(\|v\|_V=\|\nabla v\|_2\). The Lax–Milgram theorem yields a unique solution and \(\|\nabla u\|_2\le C_P\|f\|_2\).

For \(\Omega=(0,1)\), \(f=1\), \(u=x(1-x)/2\) satisfies \(-u''=1\), \(u(0)=u(1)=0\). Its energy identity is
\[\int_0^1|u'|^2dx=\int_0^1u\,dx=\frac1{12}.\]

If the Neumann condition is instead prescribed with zero flux, \(-\Delta u=f\) is solvable only if \(\int_\Omega f=0\) and u is unique only modulo constants on a connected domain.

### Exercises with answers

1. **Parabola height.** What is the maximum of \(u(x)=x(1-x)/2\) on \([0,1]\)? **Answer:** \(1/8\) at \(x=1/2\).
2. **Energy.** Why does \(a(u,u)=0\) imply \(u=0\) for \(u\in H^1_0\)? **Answer:** The gradient vanishes a.e.; Poincaré then forces zero L2 norm.
3. **Neumann source.** Can \(-u''=1\) with \(u'(0)=u'(1)=0\) have a solution? **Answer:** No: integrating gives \(-u'(1)+u'(0)=1\), a contradiction.

### Reading and source notes

- [John K. Hunter, Notes on Partial Differential Equations](https://www.math.ucdavis.edu/~hunter/m218a_09/pde_notes.pdf)
- [MIT OpenCourseWare, 18.102 Introduction to Functional Analysis, lecture notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/)
