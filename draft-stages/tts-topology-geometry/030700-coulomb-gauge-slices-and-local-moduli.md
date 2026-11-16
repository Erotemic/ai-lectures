# 030700 - Coulomb Gauge and Local Moduli: Removing Redundant Directions

**Track:** Topology and Geometry. **Background:** covariant derivatives, adjoints, implicit function theorem, Sobolev spaces, deformation complexes. **Central question:** how do we turn a gauge-invariant equation into a local elliptic problem without pretending the gauge symmetry disappears globally?

<!-- BEGIN SPOKEN LECTURE -->

# Coulomb Gauge and Local Moduli: Removing Redundant Directions

Imagine trying to find the geometry of all connections satisfying a differential equation. A connection can be described by a one-form in each chart. But that description is redundant: infinitely many one-forms related by gauge transformations describe the same geometric connection. If we blindly linearize the equation, some directions of change are merely changes of coordinates in the bundle.

To do analysis, we need a local rule that selects a manageable representative from each nearby gauge orbit. One such rule is a Coulomb gauge condition. Its name recalls the divergence-free condition of electromagnetism, but here it is a geometric statement involving the adjoint of a covariant derivative.

## The elementary abelian model

Start with a unitary line bundle over a region where it is trivial. Its connection one-form is imaginary valued. A gauge transformation is a circle-valued function, and it shifts the connection one-form by an exact imaginary one-form. If we write the gauge as the exponential of a real phase, the shift is the differential of that phase, times the imaginary unit.

Fix a reference connection and let a denote the difference from that reference. The simplest Coulomb condition says the divergence of a is zero, or in the language of forms, its codifferential is zero. We seek a gauge phase whose differential removes the divergence part of a.

This requires solving a Laplace equation for the phase. On a closed connected manifold, constants lie in the kernel of the scalar Laplacian, and the right-hand side has integral zero automatically. So a solution exists after choosing the phase's average to be zero. The remaining constant gauges are stabilizers: they act trivially on an abelian connection.

Already we can see why a gauge condition is a local slice, not a universal one-to-one coordinate system. The constant ambiguity survives, and large gauge transformations with nonzero winding can identify different representatives that satisfy the same divergence condition.

## Nonabelian Coulomb gauge

For a connection with a noncommutative structure group, the transformation law contains both a derivative term and a conjugation term. Fix a smooth connection A nought. A nearby connection is A nought plus a Lie-algebra-valued one-form a. The Coulomb slice uses the formal adjoint of the covariant derivative at A nought: the covariant divergence of a is set to zero.

To find a small gauge transformation bringing the connection into the slice, linearize the gauge-fixing equation in an infinitesimal Lie-algebra-valued function. The leading operator is the covariant Laplacian: derivative, then adjoint derivative. On a compact manifold it is elliptic. If we restrict away from its kernel, the implicit function theorem supplies a local solution under appropriate Sobolev regularity and smallness conditions.

The kernel consists of covariantly constant infinitesimal gauge transformations, which are precisely the infinitesimal stabilizers of the reference connection. For an irreducible SU-two connection, that Lie-algebra kernel vanishes: its remaining central stabilizer is discrete. At a reducible connection, a continuous stabilizer may remain, and the local quotient can be singular.

## A finite-dimensional picture of the same problem

Picture an ordinary sphere and a symmetry group rotating it around the vertical axis. Away from the poles, nearby group orbits are circles, and a short transverse segment can meet each nearby orbit once. At a pole, the whole rotation group stabilizes the point. A naive transverse coordinate picture changes because the orbit size collapses.

Gauge theory follows the same logic in an infinite-dimensional setting. The slice gives local transverse directions. Stabilizers control how those directions are identified. A slice theorem does not prove there is one globally preferred gauge throughout the entire space of connections.

## The Kuranishi reduction

Now impose a nonlinear equation, such as anti-self-duality of the curvature. On the Coulomb slice, its linearization is the gauge-fixed elliptic operator we met in the deformation-complex lecture. Ellipticity splits the local function space into a finite-dimensional kernel and a closed complement. The implicit function theorem can solve the equation in the complement as a function of the kernel coordinates, subject to a finite-dimensional obstruction equation.

The surviving finite-dimensional map is called a Kuranishi map. Its source is closely related to first deformation cohomology, and its target to the obstruction space in second cohomology. Zeros of that map, modulo the residual stabilizer, model the moduli space locally.

If the obstruction space vanishes and the stabilizer is discrete, the quotient is locally a smooth manifold with dimension given by the deformation-space dimension. If not, we may obtain a singular zero set or a quotient singularity. Those are mathematical features of the moduli space, not failures of notation.

## Why function spaces matter here

The nonlinear curvature map includes the product of two connection perturbations. To run the implicit function theorem, that product must be continuous between the chosen Banach spaces, and the gauge group must act smoothly at the required regularity. On a four-manifold, one often works with Sobolev exponents strictly above critical thresholds for a clean Banach Lie group setup, then uses regularity to compare with smooth solutions.

The weak first-Sobolev estimates from earlier lectures are central to compactness questions, but a local slice theorem at exactly critical regularity can require subtler arguments. These are different uses of Sobolev theory and should not be combined into an unsupported statement that any bounded weak connection has a unique smooth gauge.

We have now built the local analytic scaffold of gauge moduli. The gauge condition removes redundant infinitesimal directions, ellipticity leaves finite-dimensional data, and the nonlinear equation produces an obstruction map. When advanced lectures refer to a 'moduli space cut out transversely,' this is the structure behind the phrase.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a unitary connection \(A\) and \(g:X\to U(1)\), \(A^g=A+g^{-1}dg\). In a local logarithm \(g=e^{i\phi}\), \(A^g=A+i\,d\phi\). If \(a=A-A_0\), Coulomb gauge relative to \(A_0\) requires \(d^*a=0\); solve \(\Delta\phi\) with a sign determined by \(d^*d\phi\) to reach the slice, modulo constants and large gauges.

For compact structure group \(G\), a local slice through \(A_0\) is \(d_{A_0}^*(A-A_0)=0\). Linearizing the gauge condition at the identity yields (up to sign) \(d_{A_0}^*d_{A_0}\xi\), an elliptic operator whose kernel is \(\ker d_{A_0}=H_{A_0}^0\). In a suitable Sobolev setup, invert the linearization perpendicular to its kernel and apply the Banach implicit function theorem to obtain a local slice. The nonlinear ASD equation in this slice has a local Kuranishi model
\[\{x\in H_A^1:\kappa(x)=0\}/\operatorname{Stab}(A),\qquad \kappa:H_A^1\to H_A^2,\quad \kappa(0)=0,\quad d\kappa_0=0.\]
Smoothness needs suitable transversality and control of the residual stabilizer. Do not infer a global gauge slice or a global unique representative from the local argument.

### Exercises with answers

1. **Abelian gauge.** What equation determines an infinitesimal phase that imposes \(d^*a=0\)? **Answer:** a scalar Laplace equation with right side minus the divergence of the original perturbation, after fixing the sign convention.
2. **Stabilizer.** Why are constants an ambiguity for the abelian Laplacian? **Answer:** their derivatives vanish, so they do not change the connection.
3. **Reducibility.** What can fail at a reducible solution? **Answer:** the stabilizer may have positive dimension, affecting the local quotient.
4. **Obstructions.** What remains after solving the equation in the infinite-dimensional complement? **Answer:** a finite-dimensional Kuranishi obstruction map on deformation cohomology.

### Sources and further reading

- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8), manifolds of connections and Sobolev gauge transformations.
- Karen Uhlenbeck, [Connections with L-p bounds on curvature](https://doi.org/10.1007/BF01947069), 1982.
- Overviews: [Gauge fixing](https://en.wikipedia.org/wiki/Gauge_fixing), [Yang-Mills theory](https://en.wikipedia.org/wiki/Yang%E2%80%93Mills_theory).
