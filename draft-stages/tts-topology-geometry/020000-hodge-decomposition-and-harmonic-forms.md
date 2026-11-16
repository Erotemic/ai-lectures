# 020000 — Hodge Decomposition and Harmonic Forms

**Track:** Topology and Geometry. **Background:** differential forms, exterior derivatives, Riemannian metrics, de Rham cohomology. **Central question:** why can a topological cohomology class be represented by a solution of a differential equation?

<!-- BEGIN SPOKEN LECTURE -->

# Hodge Decomposition and Harmonic Forms

Consider a differential one-form on a torus. It might describe how a quantity changes when we move a small distance along the surface. Some part of it may come from the gradient of a globally defined function. Another part can circulate around a handle and never be written as a global gradient. How can we distinguish these behaviors in a systematic way?

Topology provides a classification using cohomology. Differential geometry provides a metric and differential operators. Hodge theory brings them together: on a compact oriented Riemannian manifold without boundary, every de Rham cohomology class has exactly one harmonic representative.

The word harmonic should evoke familiar equations. A harmonic function in Euclidean space satisfies Laplace's equation. For differential forms, the Laplacian must take account of both the exterior derivative and its formal adjoint. The resulting operator measures two ways a form can fail to be balanced.

## From gradients to exact and coexact forms

The exterior derivative takes a differential form to one of the next degree and has the defining property that applying it twice gives zero. Forms that are exterior derivatives of other forms are called exact. Forms whose exterior derivative vanishes are called closed. Every exact form is closed, but not every closed form is exact globally.

A Riemannian metric gives an inner product on forms, allowing us to define an adjoint to the exterior derivative. On a closed manifold, integration by parts has no boundary term, so the adjoint is an honest global operator. Combine the derivative and its adjoint to build the Hodge Laplacian.

A form is harmonic when this Laplacian vanishes. Because the Laplacian is the sum of two nonnegative quadratic contributions, on a compact manifold without boundary a harmonic form is both closed and co-closed: the exterior derivative and its adjoint each vanish.

This is a stronger condition than merely being closed. It chooses the most balanced representative from a cohomology class, much as an orthogonal projection chooses a particular vector from an affine subspace.

## The decomposition theorem

Hodge decomposition says that any smooth form can be written uniquely as a sum of three mutually orthogonal pieces: a harmonic part, an exact part, and a coexact part. The exact piece carries changes that are gradients in a generalized sense. The coexact piece carries the complementary differential information. The harmonic part cannot be removed by adding an exact correction.

If we begin with a closed form, its coexact component must vanish. We are left with a harmonic form plus an exact form. Thus changing the original form by an exact term can bring it to a harmonic representative, and the representative is unique.

The proof is an elliptic PDE theorem, not a trick that follows from linear algebra alone. One must know that the Laplacian has a well-behaved inverse on the orthogonal complement of its finite-dimensional kernel. Compactness and ellipticity are what make that analytic step possible.

## Hearing the topology of a circle and torus

On a circle with the standard metric, constants are the harmonic zero-forms. A constant multiple of the angle one-form is a harmonic one-form. That one-form represents the class that measures a complete trip around the circle. It is closed, yet not exact: a globally single-valued function cannot increase by one full period when you walk back to your starting point.

For a flat two-dimensional torus, there are two independent harmonic one-forms, one for each fundamental direction. A harmonic two-form represents the oriented area class, and constants give one harmonic zero-form. The dimensions are one, two, and one. These are the torus's real Betti numbers.

Now deform the metric. Distances, angles, and the explicit harmonic representatives generally change. But the dimensions of their spaces do not: the cohomology groups are topological invariants. The metric chooses canonical representatives within topological classes; it does not create the classes themselves.

## Duality appears again

The Hodge star converts a form of degree k to one of complementary degree. On a closed oriented manifold, it sends harmonic forms to harmonic forms. As a result, the dimensions of harmonic spaces in complementary degrees agree. This is an analytic realization of Poincaré duality over the real numbers.

There are important limits to the statement. On a noncompact manifold, harmonic forms may not represent ordinary de Rham cohomology uniquely without growth or integrability conditions. On a manifold with boundary, boundary conditions become part of the theorem. Simply writing the same formula without those choices can be wrong.

Hodge theory illustrates a recurring mathematical achievement. A topological obstruction, initially defined by whether forms can be integrated globally, becomes a finite-dimensional space of solutions to a differential equation. Geometry supplies the metric, analysis supplies elliptic regularity, and topology tells us how many solutions to expect.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let M be a compact, oriented, smooth Riemannian n-manifold **without boundary**. With inner product \(\langle\alpha,\beta\rangle=\int_M\alpha\wedge*\beta\), write \(d^\dagger\) for the formal L² adjoint of d. The Hodge Laplacian is
\[\Delta=dd^\dagger+d^\dagger d,\qquad\mathcal H^k(M)=\ker(\Delta:\Omega^k\to\Omega^k).\]
Integration by parts gives \(\langle\Delta\alpha,\alpha\rangle=\|d\alpha\|^2+\|d^\dagger\alpha\|^2\). Hence \(\Delta\alpha=0\iff d\alpha=d^\dagger\alpha=0\).

**Hodge decomposition:**
\[\Omega^k(M)=\mathcal H^k(M)\oplus d\Omega^{k-1}(M)\oplus d^\dagger\Omega^{k+1}(M),\]
with L² orthogonality. Elliptic regularity and Fredholm theory yield the decomposition, finite-dimensionality, and the canonical isomorphism \(\mathcal H^k(M)\cong H^k_{\mathrm{dR}}(M;\mathbf R)\). For a closed form, the coexact summand vanishes, giving a unique harmonic representative in each de Rham class.

**Examples.** Standard circle S¹: harmonic 0-forms are constants and harmonic 1-forms are multiples of dθ (globally defined even though θ is not a single-valued global function). Flat torus T²: bases 1, dx,dy, and dx wedge dy for degrees 0,1,2; hence Betti numbers (1,2,1). Hodge star sends \(\mathcal H^k\) to \(\mathcal H^{n-k}\), realizing real Poincaré duality in the oriented case.

### Exercises with answers

1. Why is every harmonic form closed on a closed compact manifold? **Answer:** the integrated nonnegative energy identity forces dα=0 and d†α=0.
2. How many independent harmonic one-forms exist on a flat two-torus? **Answer:** two, represented by dx and dy.
3. If the metric changes, must the dimension of harmonic k-forms change? **Answer:** no; it equals the kth real Betti number.
4. Why does a boundary require extra choices? **Answer:** integration by parts produces boundary terms; absolute, relative, or other boundary conditions affect the Hodge problem.

### Reading and source notes

- [J. D. Moore, Lectures on Riemannian Geometry](https://web.math.ucsb.edu/~moore/riemanniangeometry.pdf), Hodge theorem and Poincaré duality.
- [Christian Schnell, Complex Manifolds notes](https://www.math.stonybrook.edu/~cschnell/pdf/notes/complex-manifolds.pdf), elliptic Laplacians and harmonic representatives.
