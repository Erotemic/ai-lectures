# 141000 — How much can a distance-only gap say

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `031000`, `062000–071000`, `107000–110000`, `126000`. **Next:** `142000`.

<!-- BEGIN SPOKEN LECTURE -->

# How much can a distance-only gap say?

Put two sets of numbers on a line. The first set contains minus two and two; the second contains minus one and one. Every number in the first set stays at least one unit away from every number in the second, so the sets are disjoint with a positive distance. Yet neither set lies entirely above the other. No single ordered gap separates them.

For a scalar Sylvester equation any nonzero difference gives a denominator. For a matrix equation, interlacing spectra still keep the entrywise denominators away from zero, but the operator norm of the assembled solution requires a different argument. Davis and Kahan's first question about improving residual-angle estimates brings this distinction to the foreground.

This is the question Davis and Kahan raise in Question ten point one. It asks how sharply we can control the angle of a trial subspace using a residual if we know only that every trial spectral value is at least delta away from every complementary exact spectral value.

The Sylvester equation illustrates two distinct difficulties. A single scalar denominator is easy to control. A whole matrix of denominators can behave differently depending on the operator norm we choose. The scalar calculation gives the sharp constant one in an ordered setting. A counterexample shows why pairwise separation alone does not extend that estimate to every operator norm; a more general bound uses a larger constant.

## The compressed equation returns

Let E map the trial coordinate space isometrically into our Hilbert space. Let F one map the exact complementary spectral space into that Hilbert space. The trial compression is A zero, and the exact complementary compression is Lambda one.

Form the residual by applying the original operator to E and subtracting E times A zero. Project that residual onto the exact complementary space. Because that space reduces the exact operator, the projected residual equals Lambda one times F one star E, minus F one star E times A zero.

Call X the map F one star E and C the projected residual. We obtain the Sylvester equation Lambda one X minus X A zero equals C.

The singular values of X are the directed principal sines from the trial space toward the exact complementary subspace. Thus a bound for X gives an angle estimate. And since F one star is a contraction, the norm of C cannot exceed the residual norm in any compatible invariant norm.

So everything reduces to an inverse estimate for this Sylvester equation.

## Pairwise separation solves the scalar equations

Start with finite-dimensional self-adjoint blocks. Choose orthonormal eigenbases of Lambda one and A zero. Write their eigenvalues as lambda i and alpha j.

In those coordinates, the Sylvester equation says that lambda i minus alpha j, multiplied by the entry X i j, equals C i j. If the two spectra have pairwise distance at least delta, then every denominator has absolute value at least delta.

Thus each entry of X has absolute value at most the corresponding entry of C divided by delta. That immediately proves a Frobenius estimate: square all entries, add, and take the square root. Delta times the Frobenius norm of X is no greater than the Frobenius norm of C.

This is the clean constant-one result. It remains valid even if the two spectra are wildly interlaced. The Frobenius norm is built from the sum of squared matrix entries in orthonormal bases, and the Sylvester operator acts diagonally on those matrix units.

For Hilbert–Schmidt operators in Hilbert space, the same argument is expressed by a spectral product measure or the Hilbert–Schmidt group representation. The essential point is unchanged: each spectral-pair frequency has multiplier whose absolute value is at least delta.

## Why operator norm is harder

Now attempt the same proof for operator norm. The inequality on each matrix entry is still true, but operator norm is not the maximum absolute entry. It depends on how entries cooperate when the matrix acts on a vector.

Entrywise multiplication by a bounded coefficient matrix is called a Schur multiplier. Its operator norm can exceed the largest absolute coefficient. That is exactly what happens when the inverse Sylvester operator divides entries by different signed spectral differences.

We can demonstrate the failure in two dimensions without approximation.

Take A to be the diagonal matrix with entries one and minus one. Take B to be the diagonal matrix with entries zero and two. Their spectra are one and minus one, and zero and two. Every pairwise spectral distance is at least one.

Choose X to be the symmetric matrix with rows three, minus three, and minus three, one. Compute A X minus X B. The result C has rows three, three, and three, minus three.

The operator norm of C is three times square root of two. The operator norm of X is two plus square root of ten. Since two plus square root of ten is larger, the proposed inequality norm of X no greater than norm of C, with delta equal to one, fails.

Yet the Frobenius comparison holds: X has squared Frobenius norm twenty-eight, while C has squared Frobenius norm thirty-six. No contradiction occurs because these norms use different aggregation rules.

The numbers are useful for judging the size of the failure. The ratio between the operator norms is approximately one point two one seven. It already exceeds one with only two spectral values on each side. By contrast, the ratio between the Frobenius norms is the square root of twenty-eight divided by thirty-six, which is less than one. The gap is one in both comparisons; changing the norm is the entire reason the conclusions differ.

Why can dividing each entry by a number of magnitude at least the gap fail in operator norm? Imagine applying the resulting matrix to one input vector. Several entries contribute to the same output coordinate, and their signs determine whether those contributions reinforce or cancel.

The inverse Sylvester map divides each entry by its own signed spectral difference. That operation can change the cancellation pattern. The largest output length can increase, even though no individual entry has grown.

The Frobenius norm avoids this difficulty because it adds the squares of *individual entries*. Each entry shrinks, so their total squared sum shrinks. This is the part of the argument for which a distance-only gap is sufficient.

This example proves that the constant-one operator-norm estimate cannot follow from pairwise spectral distance alone.

## Ordered separation changes the proof

Suppose instead every eigenvalue of Lambda one lies at least delta above every eigenvalue of A zero. Then we can use a single exponential integral.

The solution X is the integral, from zero to infinity, of the semigroup generated by negative Lambda one on the left and positive A zero on the right, acting on C. In other words, every component decays with its spectral difference.

The entire operator integrand is bounded by the norm of C times exponential decay at rate delta. Integrate that scalar bound and obtain one over delta. This proof works for operator norm and compatible ideal norms because we estimate the whole product of operators, not its entries separately.

The precise improvement comes from the order assumption. It provides a common direction of decay across every spectral pair. Mere distance separation does not.

## What survives without order

For self-adjoint spectra that are disjoint with a positive distance, the inverse Sylvester operator can instead be represented using oscillatory unitary groups and a Fourier kernel. The scalar kernel reproduces the reciprocal of a frequency away from the forbidden gap around zero.

The reciprocal Fourier kernel has an integrable absolute value that yields an operator-norm estimate with the constant pi divided by twice the gap under the stated separated self-adjoint spectral hypotheses.

The proof is more delicate than entrywise division. One must construct a Fourier representation of the reciprocal multiplier on the allowed frequency set and bound the integral of conjugations by unitary groups. For unbounded self-adjoint blocks, one also needs the domain-aware Sylvester identity before invoking the formula.

Optimality of the factor pi over two depends on the specified class of spectral configurations. It gives a general guarantee where the naive constant one fails. If more is known about the arrangement of spectra, stronger bounds can be recovered.

Low-rank forcing gives an elementary fallback bound. Suppose the forcing matrix C has rank r. Its Frobenius norm is at most square root of r times its operator norm: there are at most r nonzero singular values, and none exceeds the largest.

The distance-gap Sylvester estimate controls X in Frobenius norm by the Frobenius norm of C divided by delta. And the operator norm of X is at most its Frobenius norm.

Putting those three steps in order gives an operator-norm estimate with constant square root of r over delta. It is a rank-dependent guarantee. When r is small it can beat the general distance-gap bound, while for large r it may be worse.

For rank one, the elementary square-root-of-rank estimate does recover constant one, because a rank-one forcing term has equal operator and Frobenius norms. At rank two it gives square root of two, which is weaker than our actual two-by-two ratio but better than the general pi-over-two bound. These are three different kinds of claims: a particular counterexample gives a lower limit on a universal constant; the rank estimate gives an upper bound under an extra rank hypothesis; and the Fourier representation gives an upper bound without that rank hypothesis.

## Read Question ten point one precisely

The historical question asks how sharp a residual-to-angle theorem can be under distance-only spectral separation. Theorem six point two gives constant-one Hilbert-Schmidt control under its spectral separation assumptions. The broader operator-norm story requires different techniques and constants. Our two-by-two example rules out a universal constant-one result in operator norm.

We must also specify which angle we control. X equals the exact complementary projection composed with the trial inclusion. It records directed sines. If the trial and exact subspaces have unequal dimensions or unmatched defects, an ambient projection-gap conclusion requires more information than one directed Sylvester equation.

Thus four questions accompany any proposed distance-only estimate. Which spectral sets are compared? Does their separation have a common order? Which norm measures the residual and angle? And is the target a directed angle or an ambient angle?

The same caution becomes stronger for three reducing subspaces: multiple off-diagonal overlaps interact, so separate pairwise spectral gaps need not determine the best joint estimate. Any claimed improvement must identify its three-block hypotheses and the norm in which the interacting overlaps are measured.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

The norms in the displayed witness are
\[
 \|X\|_{\mathrm{op}}=2+\sqrt{10},\qquad
 \|C\|_{\mathrm{op}}=3\sqrt2,\qquad
 \|X\|_{S_2}^2=28,\qquad
 \|C\|_{S_2}^2=36.
\]
Thus \(\|X\|_{\rm op}/\|C\|_{\rm op}\approx1.21676>1\), while \(\|X\|_{S_2}/\|C\|_{S_2}=\sqrt{7/9}<1\). If \(\operatorname{rank}C\le r\), then \(\delta\|X\|_{\rm op}\le\delta\|X\|_{S_2}\le\|C\|_{S_2}\le\sqrt r\,\|C\|_{\rm op}\).

For finite-dimensional self-adjoint blocks \(A,B\) with \(\operatorname{dist}(\sigma(A),\sigma(B))\ge\delta>0\), and \(AX-XB=C\), the spectral matrix-unit decomposition proves
\[\delta\|X\|_{S_2}\le\|C\|_{S_2}.\]
The same constant one is not generally valid in operator norm. A direct witness is
\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
B=\begin{pmatrix}0&0\\0&2\end{pmatrix},\quad
X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix},\quad
C=AX-XB=\begin{pmatrix}3&3\\3&-3\end{pmatrix},
\]
with \(\delta=1\), \(\|X\|=2+\sqrt{10}>3\sqrt2=\|C\|\). Ordered gaps give the stronger norm-generic constant-one estimate through semigroup decay; pairwise separation admits a Fourier-based larger constant under the precise self-adjoint hypotheses. The historical Question 10.1 is an investigation of the sharpest conclusion from the weaker data, not a claim that its full optimal answer is supplied by the transcription.

## Exact Lean declaration excerpts


**`hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap_direct`.** Disjoint *pairwise* self-adjoint spectra with gap delta and Hilbert–Schmidt residual membership yield Hilbert–Schmidt solution membership and the constant-one estimate.

`DavisKahan/Sources/DavisKahan1970/Sylvester/HilbertSchmidtPairwise.lean` — `hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap_direct` (exact declaration header; proof body omitted):

```lean
theorem hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap_direct
    {A : E →ₗ.[ℂ] E}
    {B : F →ₗ.[ℂ] F}
    {X C : F →L[ℂ] E}
    (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {δ : ℝ} (hδ : 0 < δ)
    (hgap : PairwiseSpectrumGap A B δ)
    (hEq : _root_.LinearPMap.SylvesterEquation A B X C)
    (hC : approximationNumberEnergy C ≠ ⊤) :
    approximationNumberEnergy X ≠ ⊤ ∧
      δ * ContinuousLinearMap.hilbertSchmidtNorm X ≤ ContinuousLinearMap.hilbertSchmidtNorm C :=
```


**`opNorm_sylvester_le_of_pairwiseSpectrumGap`.** The source proves an operator-norm estimate with factor square root of rank under the additional finite-rank residual hypothesis.

`DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean` — `opNorm_sylvester_le_of_pairwiseSpectrumGap` (exact declaration header; proof body omitted):

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
    δ * ‖X‖ ≤ ‖C‖ * Real.sqrt r :=
```


**`sharp52_constant_one_too_small`.** The actual real two-by-two witness refutes the constant-one operator-norm conclusion under pairwise distance only; it does not refute the Hilbert–Schmidt estimate.

`DavisKahan/Sources/DavisKahan1970/Sylvester/OperatorNormEstimate.lean` — `sharp52_constant_one_too_small` (exact declaration header; proof body omitted):

```lean
theorem sharp52_constant_one_too_small :
    ‖sharpC52.toContinuousLinearMap‖ < 1 * ‖sharpX52.toContinuousLinearMap‖ :=
```
