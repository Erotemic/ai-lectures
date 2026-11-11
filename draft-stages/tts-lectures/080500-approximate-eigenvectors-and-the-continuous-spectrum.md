# 080500 — Approximate eigenvectors and the continuous spectrum

**Draft status:** audio-first mathematical lecture. **Prerequisites:** bounded self-adjoint operators, Hilbert spaces, the spectrum, and L2 multiplication operators. **Related:** `080000` spectral restrictions, `081000` resolvent integrals, `086000` spectral location.

<!-- BEGIN SPOKEN LECTURE -->

# When every approximate eigenvector exists but no eigenvector does

In a two-by-two diagonal matrix, a number belongs to the spectrum precisely when it appears as an eigenvalue. We can find a nonzero vector on which the matrix acts by multiplication by that number. Infinite-dimensional self-adjoint operators behave differently: a spectral value may admit vectors that are arbitrarily close to being eigenvectors without admitting any actual eigenvector.

Here is an operator we can calculate with. Take the Hilbert space of square-integrable complex functions on the interval from zero to one. Two functions count as the same vector when they agree almost everywhere. Let A multiply a function by the coordinate: at position t, the output is t times the input. This operator is bounded, self-adjoint, and has norm one.

Could one-half be an eigenvalue? That would require a nonzero square-integrable function f for which t times f of t equals one-half times f of t almost everywhere. Wherever t differs from one-half, the equation forces f of t to be zero. The only remaining point is t equal to one-half, which has measure zero. Any function supported on just that point represents the zero vector in this Hilbert space. So one-half is not an eigenvalue.

## Concentrate near the desired frequency

Now choose a small interval centered at one-half, of total width two epsilon. Define f epsilon to be a constant on that short interval and zero outside it. Choose the constant so that the integral of its squared magnitude is one. The resulting function is a unit vector.

When A acts on f epsilon, it multiplies each value by a number t that lies within epsilon of one-half. The difference between A f epsilon and one-half times f epsilon is therefore small: its norm is at most epsilon. As epsilon approaches zero, this defect tends to zero.

We have produced a sequence of unit vectors with arbitrarily small eigen-equation residual for one-half. Such vectors are called approximate eigenvectors, and one-half belongs to the approximate point spectrum. The vectors become narrower and taller; they do not converge in norm to a nonzero eigenvector.

The same construction works at every point strictly inside the interval from zero to one, and one-sided shrinking intervals work at the endpoints. Thus each point of the interval has approximate eigenvectors although this particular multiplication operator has no eigenvectors at all.

## Why an approximate eigenvector prevents a bounded inverse

Suppose A minus lambda times the identity had a bounded inverse S. For every vector x in the space, applying S after A minus lambda would recover x. Therefore the norm of x would be at most the operator norm of S times the norm of A minus lambda applied to x.

Put an approximate unit eigenvector into that inequality. The left side is one, while the residual on the right tends to zero. This is impossible if S has finite norm. Hence lambda belongs to the spectrum whenever it has unit approximate eigenvectors.

For our multiplication operator, every number between zero and one is therefore spectral. What about a real number two? Multiplication by t minus two is bounded away from zero on the whole interval. We can invert it by multiplying by one divided by t minus two. The inverse is bounded because the denominator never gets close to zero. The same reasoning works for every complex number outside the closed interval.

Consequently the spectrum is exactly the interval from zero to one. This conclusion combines approximate eigenvectors inside with a bounded inverse outside.

## A second example: a diagonal sequence with an accumulating spectrum

Take the space of square-summable sequences, and let A multiply coordinate n by one divided by n. Every basis vector is a genuine eigenvector, with eigenvalue one divided by n. Those eigenvalues approach zero.

Zero itself is not an eigenvalue: the equation A x equals zero forces every coordinate of x to vanish. But the basis vectors are approximate zero eigenvectors, since the norm of A e n is one divided by n, which approaches zero. So zero is a spectral value without a corresponding nonzero eigenvector.

This example has a pure diagonal basis, while the multiplication example has no eigenvectors. Both show that the spectrum includes more than the set of eigenvalues. The reason is the same: an inverse may fail to be bounded even when the operator has no nonzero kernel.

## Point spectrum and continuous spectrum

The point spectrum consists of eigenvalues. For a bounded self-adjoint operator, a spectral point that is not an eigenvalue belongs to the continuous spectrum: the shifted operator has zero kernel and dense range, yet has no bounded inverse defined on the full Hilbert space.

Why is its range dense? For a bounded self-adjoint T, the orthogonal complement of the range of T is the kernel of its adjoint. For T equal to A minus a real lambda, the adjoint is the same operator. If lambda is not an eigenvalue, that kernel is zero, so the range is dense. Why can the range fail to be all of the space? A bounded bijective operator between Banach spaces would have a bounded inverse. Our approximate eigenvectors rule that out.

A general nonnormal operator can also have residual spectrum, where the range of the shift is not dense. The self-adjoint argument excludes that possibility for real spectral parameters, and a self-adjoint operator has only real spectrum.

## Spectral windows make the approximation geometrically visible

For the multiplication operator, selecting a short interval around lambda is the same as applying the corresponding spectral projection: it cuts a function down to that interval. By shrinking the window we make the operator act more and more like scalar multiplication by lambda on the selected vectors.

For an arbitrary bounded self-adjoint operator, the spectral theorem provides the same idea. If lambda is in the spectrum, every sufficiently small neighborhood of lambda has nonzero spectral projection. Take a unit vector in that spectral subspace. The spectral theorem bounds the residual by the width of the neighborhood. Hence every spectral value of a bounded self-adjoint operator has approximate unit eigenvectors.

This statement needs self-adjointness. For general bounded operators, spectral points need not all be approximate eigenvalues. It also concerns the operator spectrum itself; a selected finite-dimensional approximation may have a different collection of eigenvalues.

## The resolvent and distance to spectrum

When the shift lambda lies outside the spectrum of a self-adjoint operator, its inverse exists and is bounded. The norm of that inverse is exactly the reciprocal of the distance from lambda to the spectrum. In the multiplication example, the inverse multiplies by one divided by t minus lambda, and its norm is the essential supremum of that reciprocal.

Approaching the spectral interval from outside therefore makes the inverse norm grow. Approaching a point of the interval from within produces approximate eigenvectors with vanishing residual. These are two sides of the same spectral geometry: invertibility is stable away from the spectrum, and unit residuals can become arbitrarily small at spectral points.

One final distinction is worth retaining. A vector with a tiny residual is evidence that a spectral value lies nearby for a self-adjoint operator. It is not automatically evidence that the operator has a genuine eigenvector at that value. In infinite dimensions, the continuous spectrum is where that difference becomes unavoidable.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (display only)

Let \(H=L^2([0,1])\) and \(Af(t)=t f(t)\). Then \(A=A^*\), \(\|A\|=1\), \(\sigma(A)=[0,1]\), and \(\sigma_p(A)=\varnothing\). For \(\lambda\in(0,1)\) and \(0<\varepsilon<\min\{\lambda,1-\lambda\}\), put
\[
f_\varepsilon(t)=\frac{\mathbf 1_{[\lambda-\varepsilon,\lambda+\varepsilon]}(t)}{\sqrt{2\varepsilon}}.
\]
Then \(\|f_\varepsilon\|_2=1\), and
\[
\|(A-\lambda I)f_\varepsilon\|_2^2
=\frac1{2\varepsilon}\int_{-\varepsilon}^{\varepsilon}s^2\,ds
=\frac{\varepsilon^2}{3}.
\]
The bound \(\|(A-\lambda I)f_\varepsilon\|\leq\varepsilon\) also follows without computing the integral. One-sided normalized indicators treat \(\lambda\in\{0,1\}\).

For \(z\notin[0,1]\), \(((A-zI)^{-1}f)(t)=f(t)/(t-z)\), and
\[
\|(A-zI)^{-1}\|=\frac1{\operatorname{dist}(z,[0,1])}.
\]
For \(De_n=n^{-1}e_n\) on \(\ell^2\), \(D\) has eigenvalues \(1/n\) but \(0\notin\sigma_p(D)\); nevertheless \(\|De_n\|=1/n\to0\), so \(0\in\sigma(D)\).

If \(T=T^*\in\mathcal B(H)\), then \(\lambda\in\sigma(T)\) implies \(\forall\varepsilon>0\), \(E_T((\lambda-\varepsilon,\lambda+\varepsilon))\ne0\). A unit vector \(x\) in its range obeys \(\|(T-\lambda I)x\|\le\varepsilon\). For real \(\lambda\), \(\overline{\operatorname{Ran}(T-\lambda I)}=(\ker(T-\lambda I))^\perp\); if \(\lambda\notin\sigma_p(T)\), the range is dense but not all of \(H\).

No Lean declaration is asserted for these standard spectral-theorem consequences.
