# 030400 - The Weitzenbock Formula: Curvature in the Square of Dirac

**Track:** Topology and Geometry. **Background:** spinor Dirac operators, covariant Laplacians, curvature, integration by parts. **Central question:** why does squaring a first-order geometric operator reveal a useful second-order positivity estimate?

<!-- BEGIN SPOKEN LECTURE -->

# The Weitzenbock Formula: Curvature in the Square of Dirac

Consider the Dirac equation: a spinor is killed by a first-order differential operator. The equation mixes all coordinate directions through matrix multiplication. How can we tell whether it has nonzero solutions, or control their size without solving it explicitly?

One of the most powerful moves in geometric analysis is to square the operator. The square of a Dirac operator resembles the connection Laplacian, but with a correction involving curvature. This is called a Weitzenbock formula. In the spin case, the familiar version is also known as the Lichnerowicz formula.

## First think about the ordinary Laplacian

For a function on a compact manifold without boundary, integrate the function against its nonnegative Laplacian. Integration by parts says that the result is the integral of the squared length of its gradient. If the Laplacian kills the function, its gradient has zero length everywhere. On a connected manifold, the function is constant.

That argument does not require coordinates. It uses a positive quadratic expression obtained by integrating by parts. We want a corresponding argument for spinors, but spinors carry a connection, and second covariant derivatives do not generally commute.

## What changes when derivatives fail to commute

Apply the Dirac operator twice. Terms involving the same directional second derivative collect into the rough, or connection, Laplacian. Terms in which two different directional derivatives appear in opposite orders produce their commutator. The commutator of covariant derivatives is curvature.

Clifford multiplication combines the curvature components in a specific way. For the untwisted spin Dirac operator, the correction simplifies to one quarter of the scalar curvature times the identity. For a spin-C Dirac operator, there is an additional term involving Clifford multiplication by the curvature of the determinant line.

The exact signs depend on whether one declares Clifford multiplication skew-adjoint or self-adjoint and how one normalizes the determinant connection. We will use the Riemannian convention in which a unit vector squares to minus one. With that choice, the square of the spin Dirac operator is the nonnegative connection Laplacian plus one quarter of scalar curvature.

## A vanishing argument that takes one line of analysis

Suppose the manifold is closed, spin, and has everywhere positive scalar curvature. Let a spinor solve the untwisted Dirac equation. Its Dirac norm is zero. Integrating the Lichnerowicz formula gives the sum of two nonnegative quantities: the squared norm of its covariant derivative and one quarter of scalar curvature times the squared norm of the spinor.

If scalar curvature is strictly positive everywhere, both terms can sum to zero only if the spinor itself vanishes. Thus the untwisted spin Dirac operator has no harmonic spinors.

This is a global statement proved without writing down any special function solutions. The geometry, through scalar curvature, forces an analytic kernel to be zero. It is one of the classic examples of geometry controlling a differential equation.

## The example of the round sphere

A round sphere has positive scalar curvature, so an untwisted spin Dirac operator on it has no zero modes. Compare this with de Rham theory: a round two-sphere certainly has harmonic zero-forms and harmonic top-degree forms. Its de Rham operator therefore has a nontrivial kernel, despite being another Dirac-type operator.

Again, there is no conflict. The Lichnerowicz formula depends on which Clifford module and connection are used. The curvature correction for forms is not simply scalar curvature over four. It includes the curvature action on the form bundle, and the harmonic constants survive.

## Why spin-C curvature changes the argument

A spin-C spinor is coupled to a determinant-line connection. That line's curvature contributes an additional algebraic operator to the squared Dirac equation. The extra term need not be nonnegative. Even on a manifold with positive scalar curvature, a sufficiently strong or suitably signed line curvature can change the picture.

In Seiberg-Witten theory the curvature is not an externally fixed coefficient. It is linked to the spinor by another equation. Combining that equation with the Weitzenbock formula produces estimates for the spinor, often beginning with a maximum-principle argument. Those estimates help establish compactness for monopole solutions on a closed four-manifold.

But the formula alone does not prove compactness. We still need suitable gauges for connections, control of derivatives, and elliptic regularity. The identity supplies a key estimate within that larger chain.

## The broader family of formulas

A Weitzenbock identity is not limited to spinors. On one-forms, the Hodge Laplacian can be written as a connection Laplacian plus a Ricci curvature term. If Ricci curvature is positive, a harmonic one-form must vanish. Through Hodge theory, this gives a topological conclusion: the first real Betti number is zero.

Both stories have the same architecture. An elliptic operator's square or associated Laplacian equals a manifestly nonnegative derivative term plus a curvature term. Integrate against a solution, use positivity, and obtain vanishing or a priori bounds.

When we later meet the Dirac and gauge equations in four-dimensional topology, we should search for this pattern rather than memorizing a particular formula. It explains where estimates come from, which geometric hypotheses they require, and why changing the connection or metric can change the analytic conclusions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For the untwisted spin Dirac operator on a closed Riemannian spin manifold, with \(c(v)^2=-|v|^2\),
\[D^2=\nabla^*\nabla+\frac14\operatorname{Scal}.\]
Hence for \(D\psi=0\),
\[0=\|D\psi\|_{L^2}^2=\|\nabla\psi\|_{L^2}^2+\int_X\frac{\operatorname{Scal}}4|\psi|^2\,d\mathrm{vol}.\]
If scalar curvature is everywhere strictly positive, \(\psi=0\). For a spin-C determinant connection \(A\), the standard formula is
\[D_A^2=\nabla_A^*\nabla_A+\frac14\operatorname{Scal}+\frac12c(F_A),\]
where \(F_A\) is the imaginary-valued curvature two-form, and \(c(F_A)\) is the induced Clifford action; adjust the coefficient if using a convention where \(A\) denotes the half-weight spinor line connection instead of the determinant connection.

For harmonic one-forms, the Bochner identity gives \(\Delta_H\alpha=\nabla^*\nabla\alpha+\operatorname{Ric}(\alpha)\); strictly positive Ricci curvature on a closed manifold implies \(H^1(X;\mathbb R)=0\).

### Exercises with answers

1. **Curvature term.** Which scalar geometric quantity appears in the untwisted spin formula? **Answer:** one quarter of scalar curvature.
2. **Vanishing.** Why does positive scalar curvature rule out harmonic untwisted spinors? **Answer:** the integrated equality is a sum of nonnegative terms, one strictly positive wherever the spinor is nonzero.
3. **Twist.** What new term appears for the spin-C operator? **Answer:** Clifford action by half the determinant-line curvature in the specified convention.
4. **Forms.** Does the untwisted spin vanishing argument eliminate constant harmonic functions? **Answer:** no; functions live in a different Dirac-type module with a different curvature identity.

### Sources and further reading

- Liviu Nicolaescu, [Notes on Seiberg-Witten Theory](https://www3.nd.edu/~lnicolae/new1.pdf), geometric Dirac bundles and Weitzenbock identities.
- Daniel Freed and Karen Uhlenbeck, [Instantons and Four-Manifolds](https://doi.org/10.1007/978-1-4613-9703-8) (book; publisher access may apply).
- Overviews: [Lichnerowicz formula](https://en.wikipedia.org/wiki/Lichnerowicz_formula), [Bochner technique](https://en.wikipedia.org/wiki/Bochner_technique).
