# 068000 — The Banach-space Sylvester lower-bound theorem

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `004000–005000` bounded operators and their algebra; `057000–058000` compatible operator norms; `064000–067000` Sylvester invertibility and spectral separation. **Next:** norm dependence of Sylvester bounds.

<!-- BEGIN SPOKEN LECTURE -->

# A gap estimate from a geometric series

Start with a scalar equation: four times an unknown, minus the unknown itself, equals six. The answer is two. But there is a revealing way to obtain it without dividing by three immediately.

Move the smaller term to the right and divide by four. The unknown equals one and a half plus one quarter of itself. Substitute that formula back into itself. The result is one and a half, plus a quarter of one and a half, plus another quarter of that, and so on. Every correction is one quarter of its predecessor.

The sum converges because the correction shrinks. More importantly, its total size is controlled by the margin between the large coefficient and the small one. Davis and Kahan's Theorem five point one turns this elementary picture into a bound on a map between two Banach spaces.

## Which operator acts on which space?

A Banach space is a complete normed vector space: every Cauchy sequence has a limit in the space. We need two of them because a Sylvester unknown may be rectangular.

Call the input space H and the output space Y. The unknown map T carries vectors from H into Y. A acts on Y, B acts on H, and the known residual C also maps H into Y. The equation is A T minus T B equals C.

We are going to measure T with a norm N. It may be the ordinary operator norm, or a compatible operator ideal norm when the spaces have that additional structure. Only three properties are used: the triangle inequality, scaling by scalars, and control under multiplication on the left and right.

Specifically, if L acts on Y and R acts on H, then N of L T R is at most the operator norm of L, times N of T, times the operator norm of R. Think of this as a rule against magnifying T more than the two outside multipliers can magnify it.

For the ordinary operator norm this follows by applying the composite to a unit vector. For a Schatten norm on Hilbert spaces it follows from the ideal property. For arbitrary Banach spaces it must be an explicit assumption; there is no basis-independent Frobenius norm available for every Banach space.

## Identify the contraction

Assume B has operator norm at most gamma, where gamma is nonnegative. Assume A has a bounded inverse, whose norm is at most one over gamma plus delta, for some positive delta.

Why these two bounds? Apply the inverse of A to the equation. The result is T equals A inverse C plus A inverse T B. This is the operator version of our scalar geometric-series equation.

The first term is the known starting point. The second term is the correction, which takes any map T, applies B before it and A inverse after it. By compatibility, its size is at most gamma over gamma plus delta times the size of T.

That ratio is strictly less than one. We have identified a contraction on the space of cross-operators. The number delta is the leftover margin that makes contraction possible.

## Derive the constant-one estimate

Apply the norm N to the fixed-point identity. The triangle inequality bounds N of T by N of A inverse C plus N of A inverse T B.

Use the two-sided multiplication rule. The first term is at most N of C divided by gamma plus delta. The second is at most gamma over gamma plus delta times N of T.

Now gather the unknown terms. Multiply by gamma plus delta, and move gamma times N of T to the left. Precisely delta times N of T remains. The result is delta times N of T at most N of C.

No matrix size appears. We did not compare Frobenius and operator norms or count eigenvalues. The constant is one because the same contraction margin, delta, appears when the unknown term is moved across the inequality.

This estimate applies to any solution T that satisfies the equation. To obtain a solution from scratch, use the geometric series of repeated correction maps. In the ordinary bounded-operator norm, the space of cross-operators is complete, so that series converges. In an operator ideal, convergence in its own norm requires the ideal to be complete and stable under the multiplications used here.

## Revisit a two-sided spectral example

Now use a concrete example with spectral values on both sides of zero. Let the input space be one-dimensional and B equal to zero. Let A on the output plane be diagonal with entries negative two and positive two. Let C send one to the column two, four.

The inverse of A is diagonal with entries negative one half and positive one half. Its norm is one half. Choose gamma equal to zero and delta equal to two. Our contraction has ratio zero, because B is zero, and the geometric series stops after its first term.

Applying A inverse gives T with entries negative one and positive two. Its length is the square root of five. The length of C is twice the square root of five. Thus delta times the norm of T equals the norm of C, an exact instance of the constant-one estimate.

Here the spectral values of A straddle B. We did not need an ordered gap. We needed a controlled inverse of A relative to the small norm of B.

## Shifting the center of the picture

The equation does not change if the same scalar c is subtracted from A and B. The extra terms are negative c times T on both sides of the Sylvester difference, so they cancel.

This lets us move the center of a spectral picture to zero. Suppose B is self-adjoint with spectrum inside an interval of radius gamma around c. Then B minus c identity has norm at most gamma.

Suppose A is self-adjoint and every spectral value lies at least gamma plus delta away from c. Then A minus c identity has a bounded inverse with norm at most one over gamma plus delta. Apply the same contraction proof to these shifted operators.

Geometrically, the B spectrum is contained in a central interval while the A spectrum stays outside a larger interval. A may lie to the left, to the right, or on both sides. This is the interval-versus-exterior situation. The ordinary ordered semigroup proof cannot handle both sides simultaneously, but the bounded-inverse proof can.

## Spectral separation is not enough on a Banach space

The hypotheses refer to an inverse norm, not merely a distance to the spectrum. That difference is decisive when operators are nonnormal.

For example, take an upper-triangular two-by-two matrix with diagonal entries one and a very large upper-right entry. Its only spectral value is one, at distance one from zero. Yet its inverse has a correspondingly large off-diagonal entry, and its norm can be much greater than one.

Thus knowing that the spectrum of A stays away from zero does not ensure the inverse norm bound used by this theorem. For self-adjoint operators on Hilbert spaces, spectral calculus supplies the reciprocal-distance formula. For arbitrary Banach operators, the theorem insists on the actual inverse estimate.

There is also a useful refinement. The inequality itself only needs a bounded left inverse L of A, meaning L A is identity. In the fixed-point derivation, nothing uses A L equal to identity. The original printed hypothesis includes a two-sided inverse, and the reusable result can be stated under the weaker explicit left-inverse condition.

A lower bound on vector lengths does not automatically supply such an everywhere-defined bounded left inverse on a general Banach space: the range may lack a bounded complement. State the inverse data rather than assume it.

## What has been established

The estimate attributed to Theorem five point one concerns a solution that is already given. Under its bounded-inverse and compatible-norm hypotheses, the residual C controls the unknown T with constant one and margin delta. A separate contraction argument can construct the solution when the relevant operator space is complete.

The same two-sided spectral example can therefore support several different conclusions. Spectral separation alone ensures invertibility in the bounded complex Rosenblum setting. A quantitative inverse-norm condition supplies this constant-one estimate. The distinction is worth retaining whenever a spectral gap appears in the denominator of a subspace perturbation theorem.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

Davis–Kahan (1970), Theorem 5.1, in its printed inverse formulation: for \(T,C\in\mathcal B(X,Y)\), \(AT-TB=C\), and a compatible cross-operator norm \(N\), assume
\[
\gamma\ge0,\quad\delta>0,\quad\|B\|\le\gamma,\quad
A^{-1}\in\mathcal B(Y),\quad\|A^{-1}\|\le(\gamma+\delta)^{-1}.
\]
Then
\[
\delta N(T)\le N(C).
\]
The fixed point \(T=A^{-1}C+A^{-1}TB\) and the ideal inequality give
\[
N(T)\le(\gamma+\delta)^{-1}N(C)
+\gamma(\gamma+\delta)^{-1}N(T).
\]
The reusable strengthened theorem needs only a *bounded left inverse*; the printed statement includes a two-sided inverse. A lower bound \(\|Ay\|\ge c\|y\|\) on an arbitrary Banach space need not provide a bounded everywhere-defined left inverse without further hypotheses.

**Contraction and example.** Set \(\mathcal K(T)=A^{-1}TB\). The hypotheses give
\[
N(\mathcal K T)\le\frac{\gamma}{\gamma+\delta}N(T),\qquad
T=(I-\mathcal K)^{-1}(A^{-1}C)
=\sum_{n=0}^\infty\mathcal K^n(A^{-1}C),
\]
where the series assertion requires completeness of the chosen normed space
and a two-sided inverse to recover the Sylvester equation from the fixed point.
In the printed theorem, \(A^{-1}\) is two-sided; the **estimate alone** also
holds with an explicitly supplied bounded left inverse.

For \(A=\operatorname{diag}(-2,2)\), \(B=[0]\), and
\(C=(2,4)^\mathsf T\), choose \(\gamma=0,\delta=2\). Then
\[
T=A^{-1}C=(-1,2)^\mathsf T,\qquad
\delta\|T\|=2\sqrt5=\|C\|.
\]
A nonnormal counterpoint is \(A_M=\begin{bmatrix}1&M\\0&1\end{bmatrix}\),
\(A_M^{-1}=\begin{bmatrix}1&-M\\0&1\end{bmatrix}\): its spectrum is
\(\{1\}\), while \(\|A_M^{-1}\|\ge\sqrt{1+M^2}\) by applying it to the
second coordinate vector.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/Sources/DavisKahan1970/Section5BanachSylvester.lean` — `theorem5_1_banach_sylvester_exact`:

```lean
theorem theorem5_1_banach_sylvester_exact
    (N : CompatibleCrossOperatorNorm (𝕜 := 𝕜) (X := X) (Y := Y))
    (A Ainv : Y →L[𝕜] Y) (B : X →L[𝕜] X)
    (T C : X →L[𝕜] Y) {gamma delta : ℝ}
    (hgamma : 0 ≤ gamma) (hdelta : 0 < delta)
    (hB : ‖B‖ ≤ gamma)
    (hAinv_left : Ainv ∘L A = ContinuousLinearMap.id 𝕜 Y)
    (_hAinv_right : A ∘L Ainv = ContinuousLinearMap.id 𝕜 Y)
    (hAinv_norm : ‖Ainv‖ ≤ (gamma + delta)⁻¹)
    (hEq : A ∘L T - T ∘L B = C) :
    delta * N T ≤ N C := by
```

This is the printed two-sided inverse hypothesis: `Ainv` cancels `A` on both sides, `‖Ainv‖ ≤ (gamma + delta)⁻¹`, `‖B‖ ≤ gamma`, and `N` is a compatible cross-operator norm.

`DavisKahan/Sources/DavisKahan1970/Section5BanachSylvester.lean` — `theorem5_1_banach_sylvester`:

```lean
theorem theorem5_1_banach_sylvester
    (N : CompatibleCrossOperatorNorm (𝕜 := 𝕜) (X := X) (Y := Y))
    (A : Y →L[𝕜] Y) (B : X →L[𝕜] X)
    (T C : X →L[𝕜] Y) {gamma delta : ℝ}
    (hgamma : 0 ≤ gamma) (hdelta : 0 < delta)
    (hB : ‖B‖ ≤ gamma)
    (hleft : BoundedLeftInverseData A (gamma + delta)⁻¹)
    (hEq : A ∘L T - T ∘L B = C) :
    delta * N T ≤ N C := by
```

The reusable result only needs the explicitly supplied **bounded left inverse** data; that is a stronger theorem than the printed version. Neither theorem requires an inner-product structure.

