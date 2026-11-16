# Hodge and elliptic operators by example

<!-- BEGIN SPOKEN LECTURE -->

# Hodge and elliptic operators by example

## Hodge Decomposition and Harmonic Forms

Consider a differential one-form on a torus. It might describe how a quantity changes when we move a small distance along the surface. Some part of it may come from the gradient of a globally defined function. Another part can circulate around a handle and never be written as a global gradient. How can we distinguish these behaviors in a systematic way?

Topology provides a classification using cohomology. Differential geometry provides a metric and differential operators. Hodge theory brings them together: on a compact oriented Riemannian manifold without boundary, every de Rham cohomology class has exactly one harmonic representative.

The word harmonic should evoke familiar equations. A harmonic function in Euclidean space satisfies Laplace's equation. For differential forms, the Laplacian must take account of both the exterior derivative and its formal adjoint. The resulting operator measures two ways a form can fail to be balanced.

### From gradients to exact and coexact forms

The exterior derivative takes a differential form to one of the next degree and has the defining property that applying it twice gives zero. Forms that are exterior derivatives of other forms are called exact. Forms whose exterior derivative vanishes are called closed. Every exact form is closed, but not every closed form is exact globally.

A Riemannian metric gives an inner product on forms, allowing us to define an adjoint to the exterior derivative. On a closed manifold, integration by parts has no boundary term, so the adjoint is an honest global operator. Combine the derivative and its adjoint to build the Hodge Laplacian.

A form is harmonic when this Laplacian vanishes. Because the Laplacian is the sum of two nonnegative quadratic contributions, on a compact manifold without boundary a harmonic form is both closed and co-closed: the exterior derivative and its adjoint each vanish.

This is a stronger condition than merely being closed. It chooses the most balanced representative from a cohomology class, much as an orthogonal projection chooses a particular vector from an affine subspace.

### The decomposition theorem

Hodge decomposition says that any smooth form can be written uniquely as a sum of three mutually orthogonal pieces: a harmonic part, an exact part, and a coexact part. The exact piece carries changes that are gradients in a generalized sense. The coexact piece carries the complementary differential information. The harmonic part cannot be removed by adding an exact correction.

If we begin with a closed form, its coexact component must vanish. We are left with a harmonic form plus an exact form. Thus changing the original form by an exact term can bring it to a harmonic representative, and the representative is unique.

The proof is an elliptic PDE theorem, not a trick that follows from linear algebra alone. One must know that the Laplacian has a well-behaved inverse on the orthogonal complement of its finite-dimensional kernel. Compactness and ellipticity are what make that analytic step possible.

### Hearing the topology of a circle and torus

On a circle with the standard metric, constants are the harmonic zero-forms. A constant multiple of the angle one-form is a harmonic one-form. That one-form represents the class that measures a complete trip around the circle. It is closed, yet not exact: a globally single-valued function cannot increase by one full period when you walk back to your starting point.

For a flat two-dimensional torus, there are two independent harmonic one-forms, one for each fundamental direction. A harmonic two-form represents the oriented area class, and constants give one harmonic zero-form. The dimensions are one, two, and one. These are the torus's real Betti numbers.

Now deform the metric. Distances, angles, and the explicit harmonic representatives generally change. But the dimensions of their spaces do not: the cohomology groups are topological invariants. The metric chooses canonical representatives within topological classes; it does not create the classes themselves.

### Duality appears again

The Hodge star converts a form of degree k to one of complementary degree. On a closed oriented manifold, it sends harmonic forms to harmonic forms. As a result, the dimensions of harmonic spaces in complementary degrees agree. This is an analytic realization of Poincaré duality over the real numbers.

There are important limits to the statement. On a noncompact manifold, harmonic forms may not represent ordinary de Rham cohomology uniquely without growth or integrability conditions. On a manifold with boundary, boundary conditions become part of the theorem. Simply writing the same formula without those choices can be wrong.

Hodge theory illustrates a recurring mathematical achievement. A topological obstruction, initially defined by whether forms can be integrated globally, becomes a finite-dimensional space of solutions to a differential equation. Geometry supplies the metric, analysis supplies elliptic regularity, and topology tells us how many solutions to expect.

## Hodge Theory by Hand: Star, Adjoint, and Laplacian

On a flat torus, there is a closed one-form that measures each trip around the horizontal direction, and another that measures each trip around the vertical direction. Neither comes from differentiating a globally defined real function. Hodge theory says that these topological measurements can be recognized as special solutions of a differential equation.

That is a striking connection between topology and analysis. But before using the theorem, we should know how the equation is assembled. We will construct the Hodge star on a flat surface, use integration by parts to discover the adjoint of the exterior derivative, and calculate what harmonic means for functions and one-forms.

### Complementary directions and the Hodge star

In the Euclidean plane, the x direction and the y direction are perpendicular. Give the plane the orientation in which x followed by y is positive. The Hodge star turns the one-form measuring x displacement into the one-form measuring y displacement. Turn y into the negative x form. Apply the star twice to a one-form, and you get its negative.

The star also converts the constant function one, treated as a zero-form, into the oriented area form. It converts that area form back into the constant one. In higher dimensions, it maps a k-form to a form whose degree is the dimension minus k.

Why choose these signs? They make the wedge product of a form with the star of another form represent their pointwise inner product times oriented volume. In other words, the star lets us turn the metric's algebra of angles into something we can integrate.

The construction uses both the metric and the orientation. Change the metric and the star changes, even though the exterior derivative itself does not. That distinction will matter when we compare a metric-dependent harmonic representative with the metric-independent cohomology class it represents.

### Integration by parts creates an adjoint

For ordinary functions on an interval, integration by parts moves a derivative from one factor to another, at the cost of a minus sign and a boundary term. A similar principle applies to differential forms.

On a closed manifold, meaning compact with no boundary, the boundary term is absent. We can define an operator called the codifferential, or the adjoint of the exterior derivative, by requiring that integrating the inner product of d alpha with beta equal integrating the inner product of alpha with the codifferential of beta.

The exterior derivative increases degree by one. Its adjoint decreases degree by one. If d is the generalized gradient, the codifferential is a generalized negative divergence. On a flat Euclidean surface, a one-form with components P and Q has codifferential equal to minus the ordinary divergence of the vector field with those components.

The sign is not decorative. It makes the operator built from d and its adjoint nonnegative in the integrated energy sense. This is the convention behind much of elliptic Hodge theory.

### The Hodge Laplacian

A one-form can first be differentiated up a degree and then brought back down, or first sent down and then differentiated back up. Add those two operations. The result is the Hodge Laplacian.

For a function, the first route is impossible because there are no forms of negative degree. The Laplacian is just the codifferential of the gradient one-form. With our nonnegative convention, it is the negative of the sum of the usual second partial derivatives.

For a one-form, both routes contribute. One component measures the failure of being closed, and the other measures the failure of being co-closed. A form is harmonic when this Laplacian is zero. On a closed manifold, integrating the inner product of a form with its Laplacian gives a sum of two squares: the squared norm of its exterior derivative and the squared norm of its codifferential.

Consequently, harmonic is equivalent to being both closed and co-closed, in this compact boundaryless setting. The conclusion is stronger than simply setting a differential expression equal to zero. It comes from integration by parts and positivity, and it relies on the absence of uncontrolled boundary terms.

### One-form examples on the torus

Return to the flat unit torus. The coordinate one-forms d x and d y are globally defined, closed, and co-closed. They are harmonic. Every constant combination of them is harmonic as well. These are precisely the harmonic one-forms in that metric.

Consider instead the one-form whose horizontal component is the sine of two pi times x and whose vertical component is zero. It is the derivative of a globally defined cosine-based function. Its integral around the horizontal loop is zero, and it represents the zero cohomology class. It is an exact one-form.

Now add three times d y. The resulting form still contains the oscillating exact piece, but its cohomology class is nonzero because the integral around the vertical loop is three. Hodge decomposition finds a unique harmonic representative for the class: the constant form three d y. The oscillation can be removed by adding an exact correction; the vertical winding cannot.

There is also a third kind of term, called coexact. On a flat surface, a one-form with a suitably oscillating vertical component can be obtained by applying the codifferential to a two-form. Hodge decomposition separates an arbitrary form into exact, coexact, and harmonic parts, orthogonal with respect to the metric's integrated inner product.

### What changes at a boundary?

Take a disk instead of a torus. Integration by parts now has a boundary term. To obtain a self-adjoint elliptic problem, we must state boundary conditions. Even for ordinary functions there is a difference between prescribing the function on the boundary and prescribing its normal derivative. They lead to different spaces of admissible solutions.

For differential forms, there are analogues called relative and absolute boundary conditions. The appropriate Hodge theorem must use the boundary conditions that match the chosen cohomology theory. Ignoring the boundary while repeating the formula from a closed manifold can produce false claims about uniqueness and harmonic representatives.

On a noncompact manifold, another complication appears: integration of a square may be infinite, and the closure and domain of differential operators matter. There are several possible harmonic theories depending on growth or integrability requirements. They must not be silently identified with ordinary de Rham cohomology.

### Why the calculation matters

We have followed the construction from finite-dimensional geometry to an analytic equation. The metric and orientation give the star. The star and integration give an inner product on forms. Integration by parts gives the adjoint of d. Combining d and its adjoint gives the Hodge Laplacian. The energy identity identifies harmonic forms as the simultaneously closed and co-closed ones.

The full Hodge theorem adds a difficult analytic step: on a compact closed manifold, elliptic theory gives a finite-dimensional harmonic space and a decomposition into exact, coexact, and harmonic pieces. That step deserves its own foundations, because it is also what makes the elliptic index theorem possible.

## Elliptic Operators: From Their Symbols to Finite-Dimensional Obstructions

Consider the equation that asks for a function on a closed surface whose Laplacian equals a given source function. On a flat torus we can analyze the equation using Fourier modes. High-frequency modes are controlled strongly by the Laplacian, and the main difficulty occurs at the constant mode: the derivative of a constant is zero, so the Laplacian cannot distinguish one constant from another.

This example contains the central idea of elliptic theory. Although a differential operator acts on infinite-dimensional spaces of functions, its failure of invertibility can be confined to finite-dimensional kernel and cokernel spaces. The correct language for that phenomenon is Fredholm theory.

### The easiest necessary condition

Suppose the Laplacian of u equals f on a compact connected manifold without boundary. Integrate both sides over the manifold. Integration by parts tells us that the integral of the Laplacian is zero. Therefore the integral of f must be zero. A constant positive source cannot be the Laplacian of a globally defined smooth function on such a manifold.

The condition is also sufficient for this operator, once elliptic existence theory is available. If f has mean zero, there is a smooth solution, and any two solutions differ by a constant. The kernel consists of constants. The obstruction to solving the equation is the single scalar condition that f have integral zero.

That is a model of a Fredholm alternative: either the equation is solvable, or its right-hand side fails one or more compatibility conditions determined by solutions of the adjoint homogeneous equation.

### Look at high-frequency behavior

To understand why this can happen, examine how a differential operator acts on a rapidly oscillating wave. Differentiation multiplies an oscillation by its frequency. A second derivative multiplies it by frequency squared. For the negative Euclidean Laplacian, a wave with frequency vector xi is multiplied by the squared length of xi.

The highest-order part of an operator can be recorded as a function of position and frequency, called its principal symbol. For the Laplacian, that symbol is positive for every nonzero frequency. There is no direction in frequency space in which the leading derivative control disappears.

An operator is elliptic when its principal symbol is invertible for every nonzero cotangent vector. For scalar Laplace-type operators, this says that the leading symbol never vanishes away from zero frequency. For operators between vector bundles, it requires an invertible linear map between the fibers at every nonzero covector.

Ellipticity is a high-frequency condition. It does not assert that the operator itself is invertible. The Laplacian is elliptic but has constants in its kernel. The symbol tells us that its failure of invertibility cannot be caused by arbitrarily many unconstrained high-frequency modes on a compact manifold.

### What compactness contributes

Elliptic estimates say, roughly, that the stronger norm of a solution is controlled by a weaker norm of the input plus a lower-order term. On a compact manifold, bounded sets in a sufficiently strong Sobolev space are compact in a weaker Sobolev space. That compact embedding is a crucial second ingredient.

Together, elliptic regularity and compactness lead to finite-dimensional kernel and cokernel and closed range for an elliptic differential operator acting between appropriate Sobolev spaces. This is the Fredholm property. It is not generally guaranteed on a noncompact manifold or without adequate boundary conditions. A differential expression written in coordinates does not automatically specify a closed operator with a suitable domain.

Elliptic regularity adds another statement: a weak solution becomes smoother when the coefficients and forcing have appropriate regularity. On a compact manifold, a smooth forcing term produces smooth solutions to an elliptic equation, modulo the usual compatibility conditions.

### A first example with a nontrivial cokernel

Consider differentiation around a circle. The derivative of a periodic function has integral zero over a full period. Conversely, if a periodic target function has integral zero, integrating it produces a periodic antiderivative after choosing a constant of integration.

The kernel of differentiation consists of constants. Its image consists of mean-zero functions, so the cokernel can be represented by the missing constant direction. Both are one-dimensional. Their dimension difference is zero. Thus the derivative on the circle is a simple elliptic Fredholm operator with nonzero kernel and cokernel but index zero.

The principal symbol here is multiplication by a nonzero imaginary frequency, so it is invertible whenever the frequency is nonzero. The example makes clear that ellipticity concerns the leading behavior, while kernel and cokernel concern the full global operator.

### The index as a stable integer

For a Fredholm operator, define its index as the dimension of its kernel minus the dimension of its cokernel. An operator may lose a kernel vector under a perturbation while gaining an obstruction elsewhere. Yet the index remains stable under appropriate continuous Fredholm deformations, and in particular under compact perturbations.

For elliptic differential operators on a compact manifold, lower-order perturbations do not change the principal symbol and do not change the Fredholm index. This is why the index can be governed by the topology of the symbol rather than by every lower-order coefficient in a differential equation.

The Atiyah–Singer index theorem is the deep general result connecting the analytic index to topological data. We are not proving it here. We are making its two sides intelligible: the analytic side counts kernel and cokernel, while the symbol defines a topological object on the nonzero cotangent directions.

### How this supports Hodge theory

The Hodge Laplacian is elliptic. Its kernel is the space of harmonic differential forms, which is therefore finite-dimensional on a compact closed manifold. An elliptic decomposition also allows us to solve the Laplace equation orthogonally to that kernel. From there one obtains the exact, coexact, and harmonic decomposition of forms.

Thus the statement that each de Rham cohomology class has a unique harmonic representative depends on analytic facts: ellipticity, compactness, closed range, and regularity. These facts are not consequences of merely writing down the identity that the exterior derivative applied twice is zero.

Later gauge theory uses similar ideas. Linearizing a nonlinear equation produces a differential operator or elliptic complex. Its kernel models infinitesimal solutions, its image may include gauge directions, and its cokernel models obstructions. The Fredholm index predicts a virtual dimension even before a nonlinear moduli space is constructed.

That is the foundational insight: infinite-dimensional equations can have finite-dimensional obstruction theory. The principal symbol controls the high frequencies; compactness controls the global remainder; and the index records a stable algebraic difference. With those ideas in place, an index theorem is no longer an unexplained formula linking unrelated subjects.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Hodge Decomposition and Harmonic Forms

**Track:** Topology and Geometry. **Background:** differential forms, exterior derivatives, Riemannian metrics, de Rham cohomology. **Central question:** why can a topological cohomology class be represented by a solution of a differential equation?

#### Mathematical companion (not spoken)

Let M be a compact, oriented, smooth Riemannian n-manifold **without boundary**. With inner product \(\langle\alpha,\beta\rangle=\int_M\alpha\wedge*\beta\), write \(d^\dagger\) for the formal L² adjoint of d. The Hodge Laplacian is
\[\Delta=dd^\dagger+d^\dagger d,\qquad\mathcal H^k(M)=\ker(\Delta:\Omega^k\to\Omega^k).\]
Integration by parts gives \(\langle\Delta\alpha,\alpha\rangle=\|d\alpha\|^2+\|d^\dagger\alpha\|^2\). Hence \(\Delta\alpha=0\iff d\alpha=d^\dagger\alpha=0\).

**Hodge decomposition:**
\[\Omega^k(M)=\mathcal H^k(M)\oplus d\Omega^{k-1}(M)\oplus d^\dagger\Omega^{k+1}(M),\]
with L² orthogonality. Elliptic regularity and Fredholm theory yield the decomposition, finite-dimensionality, and the canonical isomorphism \(\mathcal H^k(M)\cong H^k_{\mathrm{dR}}(M;\mathbf R)\). For a closed form, the coexact summand vanishes, giving a unique harmonic representative in each de Rham class.

**Examples.** Standard circle S¹: harmonic 0-forms are constants and harmonic 1-forms are multiples of dθ (globally defined even though θ is not a single-valued global function). Flat torus T²: bases 1, dx,dy, and dx wedge dy for degrees 0,1,2; hence Betti numbers (1,2,1). Hodge star sends \(\mathcal H^k\) to \(\mathcal H^{n-k}\), realizing real Poincaré duality in the oriented case.

##### Exercises with answers

1. Why is every harmonic form closed on a closed compact manifold? **Answer:** the integrated nonnegative energy identity forces dα=0 and d†α=0.
2. How many independent harmonic one-forms exist on a flat two-torus? **Answer:** two, represented by dx and dy.
3. If the metric changes, must the dimension of harmonic k-forms change? **Answer:** no; it equals the kth real Betti number.
4. Why does a boundary require extra choices? **Answer:** integration by parts produces boundary terms; absolute, relative, or other boundary conditions affect the Hodge problem.

##### Reading and source notes

- [J. D. Moore, Lectures on Riemannian Geometry](https://web.math.ucsb.edu/~moore/riemanniangeometry.pdf), Hodge theorem and Poincaré duality.
- [Christian Schnell, Complex Manifolds notes](https://www.math.stonybrook.edu/~cschnell/pdf/notes/complex-manifolds.pdf), elliptic Laplacians and harmonic representatives.

### Hodge Theory by Hand: Star, Adjoint, and Laplacian

**Track:** Topology and Geometry. **Background:** differential forms, orientations, an inner product, integration by parts. **Central question:** where does the Hodge Laplacian come from, and what exactly does it measure?

#### Mathematical companion (not spoken)

On an oriented Riemannian n-manifold, \(\alpha\wedge *\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}_g\) for same-degree forms. On the oriented Euclidean plane, \(*1=dx\wedge dy\), \(*dx=dy\), \(*dy=-dx\), \(*(dx\wedge dy)=1\). In dimension n, \(**\alpha=(-1)^{k(n-k)}\alpha\) for k-forms.

For a k-form, with the standard L² sign convention, the codifferential is \(\delta=(-1)^{n(k+1)+1}*d*\), and \(\Delta=d\delta+\delta d\). On Euclidean functions, \(\Delta f=-\sum_i\partial_i^2f\). On the oriented plane, for \(\alpha=Pdx+Qdy\), \(\delta\alpha=-(\partial_xP+\partial_yQ)\). For compact boundaryless \(M\), \(\langle\Delta\alpha,\alpha\rangle_{L^2}=\|d\alpha\|^2_{L^2}+\|\delta\alpha\|^2_{L^2}\); hence \(\ker\Delta=\ker d\cap\ker\delta\).

On \(T^2=\mathbf R^2/\mathbf Z^2\), \(\alpha=\sin(2\pi x)dx+3dy\) decomposes as \(d[-\cos(2\pi x)/(2\pi)]+3dy\). Its harmonic representative is \(3dy\). A coexact example is \(\beta=\cos(2\pi x)dy=\delta[-\sin(2\pi x)/(2\pi)dx\wedge dy]\). The compact Hodge theorem gives \(\Omega^k=\operatorname{im}d\oplus\operatorname{im}\delta\oplus\mathcal H^k\) and \(\mathcal H^k\cong H^k_{\mathrm{dR}}(M)\); this requires elliptic analysis beyond the algebraic energy identity.

##### Exercises with answers

1. **Star.** On an oriented Euclidean plane compute \(**dx\). **Answer:** \(-dx\).
2. **Adjoint.** For \(\alpha=x\,dx+y\,dy\) on a local Euclidean chart, what is \(\delta\alpha\)? **Answer:** \(-2\).
3. **Torus.** What is the harmonic representative of \(\sin(2\pi x)dx+3dy\)? **Answer:** \(3dy\).
4. **Boundary.** Why does the compact boundaryless energy identity need qualification on a disk? **Answer:** Integration by parts adds boundary terms unless boundary conditions control them.

##### Sources and further reading

- J. D. Moore, [Lectures on Riemannian Geometry](https://web.math.ucsb.edu/~moore/riemanniangeometry.pdf), Hodge theory.
- Christian Schnell, [Complex Manifolds lecture notes](https://www.math.stonybrook.edu/~cschnell/pdf/notes/complex-manifolds.pdf), elliptic Hodge theory.
- Overviews: [Hodge star operator](https://en.wikipedia.org/wiki/Hodge_star_operator), [Hodge theory](https://en.wikipedia.org/wiki/Hodge_theory).

### Elliptic Operators: From Their Symbols to Finite-Dimensional Obstructions

**Track:** Topology and Geometry. **Background:** partial derivatives, Hilbert spaces, Fourier modes, compactness, linear operators. **Central question:** why do some differential equations have only finitely many independent obstructions to being solved?

#### Mathematical companion (not spoken)

For a differential operator \(P\) of order m between bundles \(E\to M\), \(F\to M\), its principal symbol \(\sigma_m(P)(x,\xi):E_x\to F_x\) records highest-order derivatives. Ellipticity requires \(\sigma_m(P)(x,\xi)\) invertible for \(\xi\ne0\). For the positive Laplace–Beltrami operator \(\Delta=-\operatorname{div}\nabla\), \(\sigma_2(\Delta)(x,\xi)=|\xi|_g^2\).

On a smooth compact manifold without boundary, an elliptic differential operator has a Fredholm realization \(P:H^{s+m}(E)\to H^s(F)\) for appropriate Sobolev spaces. The Fredholm index is \(\operatorname{ind}P=\dim\ker P-\dim\operatorname{coker}P\), invariant under compact perturbations and continuous paths of Fredholm operators. For connected closed \(M\), \(\Delta u=f\) is solvable iff \(\int_M f\,dV=0\), with solutions unique modulo constants.

On \(S^1=\mathbf R/(2\pi\mathbf Z)\), \(P=\partial_\theta:H^{s+1}\to H^s\) has \(\ker P=\mathbf R\cdot1\), range the mean-zero functions, and \(\operatorname{coker}P\cong\mathbf R\). Thus \(\operatorname{ind}P=0\). Its first-order symbol (with Fourier convention) is \(i\xi\), invertible for \(\xi\ne0\). Boundaries and noncompact domains require additional hypotheses, domains, or boundary conditions for Fredholmness.

##### Exercises with answers

1. **Laplacian compatibility.** Could \(\Delta u=1\) hold on a connected closed manifold? **Answer:** No. Integrating gives \(0=\operatorname{vol}(M)>0\).
2. **Derivative on a circle.** Can \(u'(\theta)=\cos\theta\) have a periodic solution? **Answer:** Yes, \(u=\sin\theta+C\).
3. **Obstruction.** Can \(u'(\theta)=2\) have a periodic solution? **Answer:** No, because the target has nonzero mean.
4. **Index.** If an operator has kernel dimension three and cokernel dimension one, what is its index? **Answer:** Two.

##### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds, Fredholm operator lectures](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- University of Notre Dame, [Elliptic operators on compact manifolds](https://academicweb.nd.edu/~lnicolae/Pseudo.pdf).
- Overviews: [Elliptic operator](https://en.wikipedia.org/wiki/Elliptic_operator), [Fredholm operator](https://en.wikipedia.org/wiki/Fredholm_operator).
