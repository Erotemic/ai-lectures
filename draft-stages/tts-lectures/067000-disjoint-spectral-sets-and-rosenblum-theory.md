# 067000 — Disjoint spectral sets and Rosenblum theory

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `008000` resolvents; `030000` spectral projections; `063000–066000` Sylvester inversion and integral representations. **Next:** the Banach-space Theorem 5.1 lower bound.

<!-- BEGIN SPOKEN LECTURE -->

# Dividing by spectral differences without eigenvectors

Imagine two spectral values on the left: negative two and positive two. On the right there is just zero. The Sylvester equation asks for a map X such that A X minus X B equals C. Take A to be the diagonal matrix with values negative two and positive two, B equal to zero, and C the column two, four. Entrywise division gives X equal to negative one, two.

That is an easy calculation because A is diagonal. But suppose A has a Jordan block and does not possess enough eigenvectors to diagonalize. Or suppose A acts on an infinite-dimensional Banach space. Can we still divide by the separation between the two spectra?

The answer is yes for bounded complex operators with disjoint spectra. The method is associated with Rosenblum. Its engine is a contour integral of resolvents. The contour allows us to isolate one spectrum from the other without constructing eigenvectors.

## A resolvent is division by a shifted operator

For a scalar a, the number one divided by z minus a is defined whenever z differs from a. Here z may be complex. Replace a by a bounded operator A: the resolvent at z is the inverse of z times identity minus A, wherever that inverse exists.

The collection of z for which the inverse fails is the spectrum. For a nonnormal matrix, a spectral value may belong to a Jordan block; for an infinite-dimensional operator it may fail to be an eigenvalue at all. The resolvent still describes its spectral boundary.

In the complex plane, integrating the scalar function one over z minus a around a counterclockwise loop yields one after dividing by two pi i if a lies inside, and zero if it lies outside. The operator version is a Riesz spectral projection. When the loop surrounds the entire spectrum of A, the resulting projection is the identity.

This is exactly the kind of selector we need: a contour that counts A's spectrum but excludes B's.

## Put the spaces and the factors in order

Let A act on a complex Banach space Y, and B act on a possibly different complex Banach space H. The unknown X and the given C both map H into Y.

At a complex number z outside both spectra, build a map by applying B's resolvent first to a vector in H, then C, then A's resolvent on Y. The order is important: the operator product is the A resolvent, then C, then the B resolvent.

Call that product K of z. Integrate K around a counterclockwise contour that encloses A's spectrum and excludes B's. Divide the integral by two pi i. Our claim is that this operator is the solution X.

The proof comes from one cancellation identity. We can derive it without spectral decompositions.

## Watch the cancellation

For the A resolvent, multiplying by A is the same as multiplying by z and then subtracting the identity. For the B resolvent, multiplying by B on the right is likewise multiplying by z and subtracting the identity.

Apply the Sylvester operator to K. In the first term, A acts on the left resolvent. In the second term, B acts on the right resolvent.

The first substitution creates z times K, minus C followed by the B resolvent. The second creates z times K, minus the A resolvent followed by C. Subtract the second from the first. The two copies of z times K cancel.

What remains is the A resolvent followed by C, minus C followed by the B resolvent.

Now integrate. The normalized integral of the A resolvent is identity because A is enclosed. The normalized integral of the B resolvent is zero because B is excluded. So the integral of that difference is C. The proposed X therefore satisfies A X minus X B equals C.

Notice the work done by each ingredient. Resolvent algebra creates the cancellation. The contour distinguishes the two spectral sets. Neither step asks for orthogonal eigenvectors, real eigenvalues, or an ordering of the spectra.

## The two-loop example

Return to A with diagonal entries negative two and positive two, and B equal to zero. There is no single disk containing both left eigenvalues while excluding zero: a disk is convex, so a disk containing both endpoints also contains their midpoint.

Instead choose two small counterclockwise circles, one around negative two and the other around positive two. Neither contains zero. Add their contour integrals.

For the horizontal component of C, the integrand has a pole at negative two and a harmless factor from the B resolvent. The residue supplies two divided by negative two, which is negative one. The second circle supplies four divided by positive two, which is two. The same two-entry answer appears, now obtained by contour integration.

This is the concrete reason to allow several contour components. A spectral separator need not be a single circle, even for three scalar spectral values.

## What changes for a Jordan block

Consider the upper-triangular matrix with negative two on the diagonal and one immediately above the diagonal. Its only eigenvalue is negative two, yet it has too few eigenvectors for ordinary diagonalization. Keep B equal to zero.

Solving A X equals C with C equal to the column two, four gives X equal to negative two, negative two. The first output includes a contribution from the second entry of C because of the off-diagonal one. A simple rule that divides each entry of C by negative two would miss that coupling.

The contour formula does not miss it. The resolvent of this Jordan block contains both a first-order pole and a second-order pole at negative two. Integrating their residues reproduces the coupling term in the inverse. The details belong in the companion equations, but the lesson is concrete: resolvents know about Jordan structure even when eigenvectors do not provide a basis.

## Why the solution is unique

So far we have shown that the contour recipe produces a solution for every C. We also need to rule out a second solution.

Start with any map Y and form its residual A Y minus Y B. Feed that residual into the contour recipe. Another resolvent cancellation reduces the integrand to the A resolvent followed by Y, minus Y followed by the B resolvent. Integrating gives identity times Y minus Y times zero, which is Y.

Thus the contour recipe recovers any map from its Sylvester residual. If two maps had the same residual, their difference would have residual zero and therefore be zero. Existence and uniqueness hold together.

For bounded complex operators with disjoint compact spectra, one can choose a finite union of suitable contours in the common resolvent set. This yields a bounded inverse of the Sylvester map on the Banach space of bounded cross-operators.

## The size of the inverse is another question

Look again at the example with negative two and positive two. It has a gap of two from zero, and the solution is half as large as C in norm. That numerical statement used the special diagonal matrix.

For a nonnormal operator, resolvent norms can become large far from what a simple spectral-distance picture would suggest. The contour formula gives a bound involving contour lengths and resolvent norms along the curves, not a universal constant-one estimate based only on distance between the two spectral sets.

This separates two questions that are easy to conflate. Disjoint spectra give a unique bounded solution for bounded complex operators. A quantitative error estimate requires additional information about operator geometry and the norm used to measure X and C.

A Riesz projection need not be orthogonal for a nonnormal operator. The contour argument works because its projection algebra is valid, not because it preserves Euclidean lengths. That distinction explains both the breadth of the existence theorem and why norm estimates need separate proofs.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

For \(R_A(z)=(zI-A)^{-1}\) and \(R_B(z)=(zI-B)^{-1}\),
\[
A\bigl(R_A(z)CR_B(z)\bigr)-\bigl(R_A(z)CR_B(z)\bigr)B
=R_A(z)C-CR_B(z).
\]
If a positively oriented contour \(\Gamma\) lies in the common resolvent set, encloses \(\sigma(A)\) and excludes \(\sigma(B)\), then
\[
X=\frac1{2\pi i}\oint_\Gamma R_A(z)CR_B(z)\,dz,
\qquad AX-XB=C.
\]
The complementary identity \(R_A(z)(AX-XB)R_B(z)=R_A(z)X-XR_B(z)\) proves uniqueness. The cited Lean existence/uniqueness theorem uses one positively oriented separating **circle**; general disjoint compact spectra may require a union of contour components, not covered by that exact theorem statement.

**Two-component contour.** For
\[
A=\begin{bmatrix}-2&0\\0&2\end{bmatrix},\quad B=[0],\quad
C=\begin{bmatrix}2\\4\end{bmatrix},
\]
choose \(\Gamma=\Gamma_{-2}+\Gamma_{2}\), the sum of two positively
oriented circles with radius smaller than 2. They surround \(\sigma(A)\)
but have winding number zero about \(\sigma(B)=\{0\}\). Then
\[
X=\frac{1}{2\pi i}\int_{\Gamma}(zI-A)^{-1}C(zI-B)^{-1}\,dz
=\begin{bmatrix}2/(-2)\\4/2\end{bmatrix}
=\begin{bmatrix}-1\\2\end{bmatrix}.
\]
A single disk enclosing both \(-2\) and \(2\) must contain \(0\), so two
contour components (or a noncircular separator with suitable winding) are
needed.

**Nonnormal Jordan check.** With
\[
A_J=\begin{bmatrix}-2&1\\0&-2\end{bmatrix},\quad B=[0],\quad
C=\begin{bmatrix}2\\4\end{bmatrix},\quad
A_J^{-1}=\begin{bmatrix}-\tfrac12&-\tfrac14\\0&-\tfrac12\end{bmatrix},
\]
we obtain \(X=A_J^{-1}C=(-2,-2)^\mathsf T\). The resolvent is
\[
(zI-A_J)^{-1}=\begin{bmatrix}(z+2)^{-1}&(z+2)^{-2}\\0&(z+2)^{-1}\end{bmatrix}.
\]
The second-order pole contributes the off-diagonal inverse term. This is
why dividing individual entries by the eigenvalue is invalid for a Jordan block.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/Sylvester/RosenblumExistence.lean` — `rosenblumSolution`:

```lean
noncomputable def rosenblumSolution (A : E →L[ℂ] E) (B : F →L[ℂ] F)
    (C : F →L[ℂ] E) (center radius : ℝ) : F →L[ℂ] E :=
  (2 * Real.pi * Complex.I)⁻¹ •
    ∮ z in C((center : ℂ), radius), rosenblumIntegrand A B C z
```

The concrete contour solver uses circle integrals and bounded complex Banach-space operators.

`DavisKahan/Sylvester/RosenblumExistence.lean` — `existsUnique_comp_sub_comp_eq`:

```lean
theorem existsUnique_comp_sub_comp_eq (hr : 0 < radius)
    (hA : spectrum ℂ A ⊆ ball ((center : ℂ)) radius)
    (hB : ∀ z : ℂ, z ∈ closedBall ((center : ℂ)) radius → z ∉ spectrum ℂ B) :
    ∃! S : F →L[ℂ] E, A ∘L S - S ∘L B = C := by
```

The theorem proves both existence and uniqueness when **one circle** encloses the spectrum of `A` and its closed disk excludes the spectrum of `B`. It does not directly state the arbitrary-contour version.

