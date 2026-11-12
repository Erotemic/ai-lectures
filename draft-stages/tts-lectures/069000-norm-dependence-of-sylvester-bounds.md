# 069000 — Norm dependence of Sylvester bounds

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `052000–058000` singular values and operator ideals; `063000–068000` Sylvester equations and their integral/inverse estimates. **Next:** Hilbert–Schmidt Sylvester group estimates.

<!-- BEGIN SPOKEN LECTURE -->

# A spectral gap does not choose your norm

Suppose two operators have no spectral values closer than two units. You might reasonably expect that solving a Sylvester equation divides the size of its residual by at least two. In a one-column example that intuition is exactly right.

Let A be diagonal on the plane, with values negative two and positive two, and B be zero on the input line. With C equal to the column two, four, the solution X has entries negative one and positive two. The output length is precisely half the residual length.

But now change the input space from a line to a plane. The unknown becomes a full matrix. Even if every individual coefficient is divided by a spectral difference of magnitude at least one, its operator norm can behave differently from the sum of the squares of its entries. This is why any claim about a Sylvester gap must name both the gap configuration and the norm.

## Three ways to measure the same matrix

The operator norm asks: among unit input vectors, which one is stretched the most? It is the largest singular value.

The Hilbert-Schmidt, or Frobenius, norm takes the square root of the total sum of squared entry magnitudes in orthonormal coordinates. Equivalently it takes the square root of the sum of squares of the singular values. It measures total energy over independent directions.

The nuclear norm adds the singular values without squaring. These norms agree on the absolute value of a one-by-one matrix. For matrices with multiple independent directions, they need not agree at all.

That is the first lesson of our column example. Its operator norm and Hilbert-Schmidt norm happen to coincide because a column has rank one. It cannot reveal the difficulty that arises with a full matrix.

## What every cross-spectral denominator guarantees

Let A and B be finite-dimensional self-adjoint matrices, and suppose every difference between their respective eigenvalues has absolute value at least delta, with delta positive.

Choose orthonormal eigenbases. In those coordinates, the equation A X minus X B equals C says that each coefficient of X equals the matching coefficient of C divided by its left eigenvalue minus its right eigenvalue.

For each coefficient, its squared magnitude in X is at most one over delta squared times the squared magnitude in C. Add these inequalities across all pairs of eigenvectors. Taking the square root gives delta times the Hilbert-Schmidt norm of X at most the Hilbert-Schmidt norm of C.

The spectral values may interlace. Some differences may be positive and others negative. Absolute squares remove that sign issue. The estimate is sharp, because a single pair of eigenvectors with separation exactly delta attains equality.

Pause at the key step: summing squared coefficients is exactly how the Hilbert-Schmidt norm works. There is no analogous step that sums independent coefficientwise estimates into a sharp operator-norm inequality.

## A two-by-two matrix that defeats constant one

Let A have diagonal entries positive one and negative one. Let B have diagonal entries zero and two. The two spectra are disjoint, and every cross difference has magnitude at least one. The gap delta is one.

Choose X to be the symmetric matrix whose first row is three, negative three, and whose second row is negative three, one. Form the residual C by multiplying X on the left by A and subtracting X multiplied on the right by B.

The result C has rows three, three, and three, negative three. Its columns are perpendicular and have the same length. As a consequence, C stretches every unit direction by three times the square root of two, approximately four point two four.

Now examine X. Its largest absolute eigenvalue is two plus the square root of ten, about five point one six. A unit vector aligned with that eigenvector is stretched by X more than any unit input direction is stretched by C.

So the operator norm of X exceeds the operator norm of C, even though every entry of X was obtained by dividing by a denominator of absolute value at least one.

Nothing contradicts the coefficientwise argument. The Frobenius norm of X is the square root of twenty-eight; the Frobenius norm of C is six. The square-norm inequality still holds. The counterexample isolates the false step: translating independent coefficient bounds into a constant-one claim about maximum directional amplification.

## Recovering a rank-dependent operator estimate

There is a safe route from the square norm to the operator norm, but it has a price. The operator norm of X is at most its Hilbert-Schmidt norm. And if C has rank r, the Hilbert-Schmidt norm of C is at most the square root of r times its operator norm.

Chaining these facts gives delta times the operator norm of X at most the square root of r times the operator norm of C. The rank factor belongs to the norm comparison, not to the underlying spectral division.

In the two-by-two counterexample, r is two. A factor of the square root of two is more than enough to accommodate the observed increase. But for large rank, that estimate grows with dimension and may be wasteful.

## Two ways to obtain dimension-free control

Return to the spectral picture. If all left eigenvalues lie at least delta above all right eigenvalues, there is a single orientation in which the exponential transport decays. Integrating that decay gives the operator-norm inequality with constant one. The same argument works for compatible ideal norms because left and right multiplication obey their ideal estimates.

There is also the interval-versus-exterior picture. After a common scalar shift, suppose B has norm at most gamma and A has a bounded inverse of norm at most one over gamma plus delta. The fixed-point identity then gives constant one. In a self-adjoint Hilbert setting, the spectral theorem can supply those inverse bounds from a central interval and an exterior set.

Our original column with left values negative two and positive two and right value zero belongs to the interval-versus-exterior setting, even though it is not ordered. Its constant-one behavior has an explanation stronger than pairwise separation alone.

## A universal Fourier estimate for pairwise gaps

For bounded self-adjoint A and B under arbitrary pairwise separation, use their unitary groups instead. Weight the left-right evolution by an integrable scalar function whose Fourier transform divides by the spectral differences.

Unitary multiplication preserves operator norms. The norm of the weighted integral is therefore controlled by the absolute integral of the scalar kernel. A suitable kernel has mass pi divided by twice delta. This yields delta times the operator norm of X at most pi over two times the operator norm of C, without any rank factor.

The same integral argument applies to suitable compatible unitarily invariant ideal norms. It provides a general bound. It does not change the fact that in the Hilbert-Schmidt norm, orthogonal spectral blocks already give the better constant one.

## What to carry into a subspace theorem

An angle estimate often comes from dividing a projected residual by a spectral separation. Before choosing the division theorem, identify the two compressed operators, locate their spectra, and decide which norm is measuring the unknown cross block.

If the proof squares and sums spectral coefficients, the natural output is a Hilbert-Schmidt estimate. If it needs the largest directional error, the operator norm is relevant, and pairwise separation alone cannot justify constant one. Ordered decay, central-interval inverse bounds, or a Fourier multiplier each come with their own hypotheses.

A spectral gap controls division; the chosen norm determines how the divided coefficients can be combined. Both decisions are needed for a correct bound.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

Let \(A,B\) be bounded self-adjoint operators and let \(AX-XB=C\). Comparison by hypothesis and norm:

| Gap geometry | Norm | Supported estimate |
|---|---|---|
| Pairwise \(|a-b|\ge\delta\) | Hilbert–Schmidt | \(\delta\|X\|_{S_2}\le\|C\|_{S_2}\) |
| Pairwise, \(\operatorname{rank}(C)\le r\) | Operator | \(\delta\|X\|\le\sqrt r\|C\|\) |
| Pairwise | Operator | \(\delta\|X\|\le\tfrac\pi2\|C\|\) via the Fourier kernel |
| Ordered | Operator, compatible ideals | \(\delta N(X)\le N(C)\) via semigroup decay |
| Bounded inverse \(\|A^{-1}\|\le(\gamma+\delta)^{-1}\), \(\|B\|\le\gamma\) | Compatible Banach cross-operator norm | \(\delta N(X)\le N(C)\) |

The real symmetric source witness has
\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
B=\begin{pmatrix}0&0\\0&2\end{pmatrix},\quad
X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix},\quad
C=\begin{pmatrix}3&3\\3&-3\end{pmatrix}.
\]
For \(\delta=1\), \(\|X\|=2+\sqrt{10}>3\sqrt2=\|C\|\), refuting a constant-one pairwise-gap operator-norm claim.

**Shared scalar example and the matrix obstruction.** With
\(A=\operatorname{diag}(-2,2)\), \(B=[0]\), and \(C=(2,4)^\mathsf T\),
\(X=(-1,2)^\mathsf T\) and \(\delta\|X\|_2=\|C\|_2=2\sqrt5\).
For the interlaced two-by-two witness already displayed above,
\[
\|X\|_{S_2}^2=3^2+(-3)^2+(-3)^2+1^2=28,
\qquad \|C\|_{S_2}^2=36.
\]
Thus \(\|X\|_{S_2}\le\|C\|_{S_2}\) with \(\delta=1\), while
\(\|X\|_{op}=2+\sqrt{10}>3\sqrt2=\|C\|_{op}\). The example separates
the two *norm* claims without altering the spectral configuration.

**Lean bridge (verbatim source excerpts).**

`DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean` — `opNorm_sylvester_le_of_pairwiseSpectrumGap`:

```lean
theorem opNorm_sylvester_le_of_pairwiseSpectrumGap
    {E F : Type v}
    [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
    {A : E →ₗ.[ℂ] E}
    {B : F →ₗ.[ℂ] F}
    {X C : F →L[ℂ] E}
    (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : PairwiseSpectrumGap A B δ)
    (hEq : _root_.LinearPMap.SylvesterEquation A B X C)
    {r : ℕ} (hRank : C.rank ≤ (r : Cardinal)) :
    δ * ‖X‖ ≤ ‖C‖ * Real.sqrt r := by
```

The theorem derives the rank-dependent operator-norm bound from the Hilbert–Schmidt estimate. It applies to self-adjoint partial operators and a finite-rank right-hand side.

`DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean` — `sharp52_constant_one_too_small`:

```lean
theorem sharp52_constant_one_too_small :
    ‖sharpC52.toContinuousLinearMap‖ < 1 * ‖sharpX52.toContinuousLinearMap‖ := by
```

This is the exact counterexample showing that constant one fails for the operator norm under merely pairwise separation.

`DavisKahan/InfiniteDimensional/Sylvester/FourierSemigroup.lean` — `mul_l1_norm_separatedSylvesterMultiplier`:

```lean
theorem mul_l1_norm_separatedSylvesterMultiplier (d : ℝ) (hd : 0 < d) :
    d * (∫ t : ℝ, ‖separatedSylvesterMultiplier d hd t‖) = Real.pi / 2 := by
```

The source proves the exact `π/2` mass of the reciprocal Fourier multiplier, which underwrites the corresponding universal operator-norm upper bound.

