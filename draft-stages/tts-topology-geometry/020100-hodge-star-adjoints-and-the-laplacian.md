# 020100 — Hodge Theory by Hand: Star, Adjoint, and Laplacian

**Track:** Topology and Geometry. **Background:** differential forms, orientations, an inner product, integration by parts. **Central question:** where does the Hodge Laplacian come from, and what exactly does it measure?

<!-- BEGIN SPOKEN LECTURE -->

# Hodge Theory by Hand: Star, Adjoint, and Laplacian

On a flat torus, there is a closed one-form that measures each trip around the horizontal direction, and another that measures each trip around the vertical direction. Neither comes from differentiating a globally defined real function. Hodge theory says that these topological measurements can be recognized as special solutions of a differential equation.

That is a striking connection between topology and analysis. But before using the theorem, we should know how the equation is assembled. We will construct the Hodge star on a flat surface, use integration by parts to discover the adjoint of the exterior derivative, and calculate what harmonic means for functions and one-forms.

## Complementary directions and the Hodge star

In the Euclidean plane, the x direction and the y direction are perpendicular. Give the plane the orientation in which x followed by y is positive. The Hodge star turns the one-form measuring x displacement into the one-form measuring y displacement. Turn y into the negative x form. Apply the star twice to a one-form, and you get its negative.

The star also converts the constant function one, treated as a zero-form, into the oriented area form. It converts that area form back into the constant one. In higher dimensions, it maps a k-form to a form whose degree is the dimension minus k.

Why choose these signs? They make the wedge product of a form with the star of another form represent their pointwise inner product times oriented volume. In other words, the star lets us turn the metric's algebra of angles into something we can integrate.

The construction uses both the metric and the orientation. Change the metric and the star changes, even though the exterior derivative itself does not. That distinction will matter when we compare a metric-dependent harmonic representative with the metric-independent cohomology class it represents.

## Integration by parts creates an adjoint

For ordinary functions on an interval, integration by parts moves a derivative from one factor to another, at the cost of a minus sign and a boundary term. A similar principle applies to differential forms.

On a closed manifold, meaning compact with no boundary, the boundary term is absent. We can define an operator called the codifferential, or the adjoint of the exterior derivative, by requiring that integrating the inner product of d alpha with beta equal integrating the inner product of alpha with the codifferential of beta.

The exterior derivative increases degree by one. Its adjoint decreases degree by one. If d is the generalized gradient, the codifferential is a generalized negative divergence. On a flat Euclidean surface, a one-form with components P and Q has codifferential equal to minus the ordinary divergence of the vector field with those components.

The sign is not decorative. It makes the operator built from d and its adjoint nonnegative in the integrated energy sense. This is the convention behind much of elliptic Hodge theory.

## The Hodge Laplacian

A one-form can first be differentiated up a degree and then brought back down, or first sent down and then differentiated back up. Add those two operations. The result is the Hodge Laplacian.

For a function, the first route is impossible because there are no forms of negative degree. The Laplacian is just the codifferential of the gradient one-form. With our nonnegative convention, it is the negative of the sum of the usual second partial derivatives.

For a one-form, both routes contribute. One component measures the failure of being closed, and the other measures the failure of being co-closed. A form is harmonic when this Laplacian is zero. On a closed manifold, integrating the inner product of a form with its Laplacian gives a sum of two squares: the squared norm of its exterior derivative and the squared norm of its codifferential.

Consequently, harmonic is equivalent to being both closed and co-closed, in this compact boundaryless setting. The conclusion is stronger than simply setting a differential expression equal to zero. It comes from integration by parts and positivity, and it relies on the absence of uncontrolled boundary terms.

## One-form examples on the torus

Return to the flat unit torus. The coordinate one-forms d x and d y are globally defined, closed, and co-closed. They are harmonic. Every constant combination of them is harmonic as well. These are precisely the harmonic one-forms in that metric.

Consider instead the one-form whose horizontal component is the sine of two pi times x and whose vertical component is zero. It is the derivative of a globally defined cosine-based function. Its integral around the horizontal loop is zero, and it represents the zero cohomology class. It is an exact one-form.

Now add three times d y. The resulting form still contains the oscillating exact piece, but its cohomology class is nonzero because the integral around the vertical loop is three. Hodge decomposition finds a unique harmonic representative for the class: the constant form three d y. The oscillation can be removed by adding an exact correction; the vertical winding cannot.

There is also a third kind of term, called coexact. On a flat surface, a one-form with a suitably oscillating vertical component can be obtained by applying the codifferential to a two-form. Hodge decomposition separates an arbitrary form into exact, coexact, and harmonic parts, orthogonal with respect to the metric's integrated inner product.

## What changes at a boundary?

Take a disk instead of a torus. Integration by parts now has a boundary term. To obtain a self-adjoint elliptic problem, we must state boundary conditions. Even for ordinary functions there is a difference between prescribing the function on the boundary and prescribing its normal derivative. They lead to different spaces of admissible solutions.

For differential forms, there are analogues called relative and absolute boundary conditions. The appropriate Hodge theorem must use the boundary conditions that match the chosen cohomology theory. Ignoring the boundary while repeating the formula from a closed manifold can produce false claims about uniqueness and harmonic representatives.

On a noncompact manifold, another complication appears: integration of a square may be infinite, and the closure and domain of differential operators matter. There are several possible harmonic theories depending on growth or integrability requirements. They must not be silently identified with ordinary de Rham cohomology.

## Why the calculation matters

We have followed the construction from finite-dimensional geometry to an analytic equation. The metric and orientation give the star. The star and integration give an inner product on forms. Integration by parts gives the adjoint of d. Combining d and its adjoint gives the Hodge Laplacian. The energy identity identifies harmonic forms as the simultaneously closed and co-closed ones.

The full Hodge theorem adds a difficult analytic step: on a compact closed manifold, elliptic theory gives a finite-dimensional harmonic space and a decomposition into exact, coexact, and harmonic pieces. That step deserves its own foundations, because it is also what makes the elliptic index theorem possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On an oriented Riemannian n-manifold, \(\alpha\wedge *\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}_g\) for same-degree forms. On the oriented Euclidean plane, \(*1=dx\wedge dy\), \(*dx=dy\), \(*dy=-dx\), \(*(dx\wedge dy)=1\). In dimension n, \(**\alpha=(-1)^{k(n-k)}\alpha\) for k-forms.

For a k-form, with the standard L² sign convention, the codifferential is \(\delta=(-1)^{n(k+1)+1}*d*\), and \(\Delta=d\delta+\delta d\). On Euclidean functions, \(\Delta f=-\sum_i\partial_i^2f\). On the oriented plane, for \(\alpha=Pdx+Qdy\), \(\delta\alpha=-(\partial_xP+\partial_yQ)\). For compact boundaryless \(M\), \(\langle\Delta\alpha,\alpha\rangle_{L^2}=\|d\alpha\|^2_{L^2}+\|\delta\alpha\|^2_{L^2}\); hence \(\ker\Delta=\ker d\cap\ker\delta\).

On \(T^2=\mathbf R^2/\mathbf Z^2\), \(\alpha=\sin(2\pi x)dx+3dy\) decomposes as \(d[-\cos(2\pi x)/(2\pi)]+3dy\). Its harmonic representative is \(3dy\). A coexact example is \(\beta=\cos(2\pi x)dy=\delta[-\sin(2\pi x)/(2\pi)dx\wedge dy]\). The compact Hodge theorem gives \(\Omega^k=\operatorname{im}d\oplus\operatorname{im}\delta\oplus\mathcal H^k\) and \(\mathcal H^k\cong H^k_{\mathrm{dR}}(M)\); this requires elliptic analysis beyond the algebraic energy identity.

### Exercises with answers

1. **Star.** On an oriented Euclidean plane compute \(**dx\). **Answer:** \(-dx\).
2. **Adjoint.** For \(\alpha=x\,dx+y\,dy\) on a local Euclidean chart, what is \(\delta\alpha\)? **Answer:** \(-2\).
3. **Torus.** What is the harmonic representative of \(\sin(2\pi x)dx+3dy\)? **Answer:** \(3dy\).
4. **Boundary.** Why does the compact boundaryless energy identity need qualification on a disk? **Answer:** Integration by parts adds boundary terms unless boundary conditions control them.

### Sources and further reading

- J. D. Moore, [Lectures on Riemannian Geometry](https://web.math.ucsb.edu/~moore/riemanniangeometry.pdf), Hodge theory.
- Christian Schnell, [Complex Manifolds lecture notes](https://www.math.stonybrook.edu/~cschnell/pdf/notes/complex-manifolds.pdf), elliptic Hodge theory.
- Overviews: [Hodge star operator](https://en.wikipedia.org/wiki/Hodge_star_operator), [Hodge theory](https://en.wikipedia.org/wiki/Hodge_theory).
