# 010000 — Distance gaps and the Hilbert–Schmidt estimate

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sylvester. **Audience:** the Sylvester equation, Theorems 5.1 and 5.2, Hilbert–Schmidt operators, spectral theorem.

<!-- BEGIN SPOKEN LECTURE -->

Distance gaps and the Hilbert–Schmidt estimate

Windows and cuts give the Sylvester estimate with constant one in every unitarily invariant norm. Sometimes neither is available. The eigenvalues we want may be scattered among the ones we do not want, so that the wanted and unwanted spectra interlace, with only a minimum distance between them. This lecture explains what survives: the Hilbert–Schmidt estimate with constant one, an operator-norm estimate with a factor depending on rank, and Davis and Kahan's Theorem 6.2, the sine-theta theorem for distance gaps.

Here is what we will establish. First, the space of Hilbert–Schmidt operators is itself a Hilbert space, and on it the Sylvester map, taking X to C X minus X B, is a self-adjoint operator whose spectrum consists of differences of spectral values of C and B. If every such difference is at least delta in absolute value, the Sylvester map has an inverse of norm at most one over delta, which is the Hilbert–Schmidt estimate, Davis and Kahan's inequality 5.1. Second, the operator norm is at most the Hilbert–Schmidt norm, and the Hilbert–Schmidt norm of a rank r operator is at most root r times its operator norm, which gives inequality 5.2. Third, Theorem 6.2: under a distance gap between the trial spectrum and the unwanted spectrum, delta times the Hilbert–Schmidt norm of the sine of Theta zero is at most the Hilbert–Schmidt norm of the residual. Fourth, the operator-norm constant one is false under a distance gap, and the best universal constant turned out to be pi over two.

When interlacing is natural

Consider the diagonal matrix with entries one, two, and three, and suppose we want the eigenvectors for one and three together, the span of e one and e three, and not the eigenvector for two. This happens, for instance, when the wanted eigenvalues are selected by a symmetry rather than by their size. A trial operator approximating the wanted part has spectrum near one and three, and the unwanted spectrum is two.

No interval contains one and three while excluding two, so the interval and exterior hypothesis fails. No cut puts one and three on the same side of two, so the ordered hypothesis fails. The only separation available is distance: two is at distance one from both. If the trial values are exactly one and three, delta is one.

The Hilbert–Schmidt space

The Hilbert–Schmidt operators from one Hilbert space to another form a Hilbert space themselves, with inner product the trace of X star times Z. In finite dimensions this is the familiar Frobenius inner product: the sum over all entries of the conjugate of one matrix's entry times the other's.

On this Hilbert space consider two operators. Left multiplication by C takes X to C X, and right multiplication by B takes X to X B. If C and B are bounded and self-adjoint, both multiplications are self-adjoint operators on the Hilbert–Schmidt space, and they commute with each other, because multiplying on the left and multiplying on the right do not interfere. Their difference is the Sylvester map, X goes to C X minus X B.

Two commuting self-adjoint operators can be diagonalized together, in the sense of the spectral theorem, and their difference has spectrum contained in the set of differences of their spectral values. Left multiplication by C has the spectrum of C, and right multiplication by B has the spectrum of B. So the Sylvester map is a self-adjoint operator on the Hilbert–Schmidt space whose spectrum lies in the set of numbers c minus b, with c in the spectrum of C and b in the spectrum of B.

If the distance between the two spectra is at least delta, every such difference has absolute value at least delta, so zero lies outside the spectrum of the Sylvester map with room delta around it. A self-adjoint operator whose spectrum stays at least delta away from zero is invertible, with inverse of norm at most one over delta. Therefore, if C X minus X B equals Y, the Hilbert–Schmidt norm of X is at most the Hilbert–Schmidt norm of Y divided by delta.

This argument is the operator form of the diagonal calculation, in which each entry of X was an entry of Y divided by a difference of eigenvalues. What made it work is that the Hilbert–Schmidt norm is a Hilbert-space norm, so the size of a self-adjoint operator's inverse is controlled entirely by how far its spectrum stays from zero. The interlacing of the two spectra is irrelevant; only the distance matters. Davis and Kahan state this as their inequality 5.1, and the same argument extends to unbounded self-adjoint coefficients on arbitrary complex Hilbert spaces, showing that X is Hilbert–Schmidt whenever the right-hand side is.

Why the operator norm is different

The operator norm is not a Hilbert-space norm, and the same argument does not apply. Davis and Kahan's two by two example shows the failure. With C diagonal with entries one and minus one, and B diagonal with entries zero and two, the spectra minus one and one, and zero and two, are at distance one and interlace. The solution X with rows three, minus three and minus three, one has operator norm two plus root ten, about five point one six, while the right-hand side, with rows three, three and three, minus three, has operator norm three root two, about four point two four. The operator-norm estimate with constant one fails. The Hilbert–Schmidt estimate holds: the squared Hilbert–Schmidt norm of X is twenty-eight, of Y thirty-six, and the square root of twenty-eight is less than six.

What can be said in the operator norm? Two elementary inequalities give an answer. The operator norm of X is at most its Hilbert–Schmidt norm, since the largest singular value is at most the root sum of squares. And if Y has rank r, its Hilbert–Schmidt norm is at most root r times its operator norm, since it has at most r nonzero singular values, each at most the largest. Chaining them, delta times the operator norm of X is at most root r times the operator norm of Y. This is Davis and Kahan's inequality 5.2. In the two by two example, r is two, and root two times four point two four is six, which indeed exceeds five point one six.

Davis and Kahan remark that 5.2 is not best possible unless the rank is one, and ask whether the factor root r can be replaced by a universal constant. Later work answered yes: for self-adjoint coefficients whose spectra are distance delta apart, the operator norm of X is at most pi over two times the operator norm of Y divided by delta, and pi over two cannot be improved. So under a distance gap, the operator-norm constant is genuinely larger than one, and the root-rank factor in 5.2 is a feature of that particular argument rather than of the problem.

Theorem 6.2

Now return to angles. The sine-theta argument gives the Sylvester equation Lambda one X minus X A zero equals F one star R, where X is F one star E zero and the modulus of X is the sine of Theta zero. Apply the Hilbert–Schmidt estimate: if the spectra of A zero and Lambda one are at distance at least delta, then delta times the Hilbert–Schmidt norm of X is at most the Hilbert–Schmidt norm of F one star R, which is at most the Hilbert–Schmidt norm of R. Therefore delta times the Hilbert–Schmidt norm of the sine of Theta zero is at most the Hilbert–Schmidt norm of R.

That is the core of Davis and Kahan's Theorem 6.2. The theorem is stated more generally, for trial frames that are not isometric but have a lower frame bound epsilon, in which case the left side acquires a factor epsilon; and the sine is then Hilbert–Schmidt whenever the residual is. If the residual has finite rank, the same chain of inequalities gives an operator-norm bound with the factor root rank.

In the example with eigenvalues one, two, three and wanted values one and three, a trial subspace whose trial operator has eigenvalues within one half of one and three would have its trial spectrum at distance at least one half from the unwanted value two. Then the Hilbert–Schmidt norm of the sine of Theta zero is at most twice the Hilbert–Schmidt norm of the residual, and its operator norm is at most twice the operator norm of the residual times root two, since a two-dimensional trial subspace has a residual of rank at most two.

Choosing the right estimate

The three Sylvester estimates fit together as a small decision procedure for reading or applying the paper.

If the trial spectrum lies in an interval and the unwanted spectrum outside it, or the reverse, use Theorem 5.1: constant one in every unitarily invariant norm.

If the two spectra are separated by a cut, with possibly both operators unbounded, use Theorem 5.2: again constant one in every unitarily invariant norm.

If the spectra merely keep a distance delta, use inequality 5.1 and Theorem 6.2: constant one in the Hilbert–Schmidt norm only. For the operator norm, accept either the factor root rank or the universal constant pi over two.

The error to avoid is using a distance gap with an estimate proved only for windows or cuts. The two by two example is a concrete reminder: same delta, interlaced spectra, and the operator-norm estimate with constant one is false.

To summarize. On the Hilbert space of Hilbert–Schmidt operators, the Sylvester map is self-adjoint with spectrum in the set of differences of spectral values, so a distance gap delta bounds its inverse by one over delta, giving the Hilbert–Schmidt estimate with constant one, Davis and Kahan's inequality 5.1. Comparing operator and Hilbert–Schmidt norms gives the operator-norm bound with factor root rank, inequality 5.2, which is not sharp; the sharp universal constant is pi over two. Theorem 6.2 transfers the Hilbert–Schmidt estimate to angles: under a distance gap between the trial spectrum and the unwanted spectrum, delta times the Hilbert–Schmidt norm of the sine of Theta zero is at most the Hilbert–Schmidt norm of the residual.

The Hilbert–Schmidt estimate is only as useful as the Hilbert–Schmidt norm of the residual. For an infinite-rank residual that is not Hilbert–Schmidt, Theorem 6.2 says nothing, while a window or a cut would still give an operator-norm bound.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Hilbert–Schmidt argument

\(\langle X,Z\rangle_{\rm HS}=\operatorname{tr}(X^*Z)\). \(L_C:X\mapsto CX\), \(R_B:X\mapsto XB\) are commuting self-adjoint operators on \(S_2\) with \(\sigma(L_C)=\sigma(C)\), \(\sigma(R_B)=\sigma(B)\), so
\[
\sigma(L_C-R_B)\subseteq\overline{\sigma(C)-\sigma(B)},\qquad \operatorname{dist}(\sigma(C),\sigma(B))\ge\delta\Rightarrow\|(L_C-R_B)^{-1}\|_{S_2\to S_2}\le\delta^{-1}.
\]
(5.1): \(\delta\|X\|_{\rm HS}\le\|CX-XB\|_{\rm HS}\). (5.2): \(\delta\|X\|_{\rm op}\le\delta\|X\|_{\rm HS}\le\|Y\|_{\rm HS}\le\sqrt{\operatorname{rank}Y}\,\|Y\|_{\rm op}\).

### Example (Section 5)

\(C=\operatorname{diag}(1,-1)\), \(B=\operatorname{diag}(0,2)\), \(X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix}\), \(Y=\begin{pmatrix}3&3\\3&-3\end{pmatrix}\): \(\|X\|_{\rm op}=2+\sqrt{10}\approx5.162\), \(\|Y\|_{\rm op}=3\sqrt2\approx4.243\), \(\|X\|_{\rm HS}=\sqrt{28}\approx5.292\le6=\|Y\|_{\rm HS}\), \(\sqrt2\|Y\|_{\rm op}=6\).

Universal constant: \(\delta\|X\|_{\rm op}\le\tfrac\pi2\|CX-XB\|_{\rm op}\) for self-adjoint \(C,B\) with \(\operatorname{dist}(\sigma(C),\sigma(B))\ge\delta\), and \(\pi/2\) is best possible (Bhatia, *Matrix Analysis*, Section VII.2).

### Theorem 6.2

\(E_0^*E_0\ge\varepsilon^2I\), \(\operatorname{dist}(\sigma(A_0),\sigma(\Lambda_1))\ge\delta\): \(\delta\varepsilon\|\sin\Theta_0\|_{\rm HS}\le\|R\|_{\rm HS}\); if \(R\) has finite rank, \(\delta\varepsilon\|\sin\Theta_0\|_{\rm op}\le\sqrt{\operatorname{rank}R}\,\|R\|_{\rm op}\).

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/Theorem61.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
theorem theorem6_2_complex
    {E₀' F₀' : Type v} [...]
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) (hdist : PairwiseSpectrumGap A₀ Λ₁ δ)
    (S : SinThetaRepresentativeAcross (E₀ := E₀') (F₀ := F₀')
      (sectionSixSinThetaBlock E₀ F₁ hframe hε))
    (hR : approximationNumberEnergy R ≠ ⊤) :
    approximationNumberEnergy S.operator ≠ ⊤ ∧
      δ * ε * ContinuousLinearMap.hilbertSchmidtNorm S.operator ≤
        ContinuousLinearMap.hilbertSchmidtNorm R
```

`DavisKahan/Sources/DavisKahan1970/Section5.lean`: `Inequality5_1` (alias of `DavisKahan.ExactSinTheta.hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap`) and `Inequality5_2` (alias of `DavisKahan.ExactSinTheta.opNorm_sylvester_le_of_pairwiseSpectrumGap`); the source's 2×2 witness is compiled as `sharp52_constant_one_too_small`.

**Mapping notes.**

- `approximationNumberEnergy R ≠ ⊤` is Hilbert–Schmidt membership of the residual; the conclusion includes membership of the sine representative.
- The docstring states that the counted Theorem 6.2 is the Hilbert–Schmidt statement; the finite-rank operator-norm consequence is recorded separately.
- `IsTrialResidualEquation` is `IsTrialResidual` without the isometry, since Theorem 6.2 allows a lower frame bound `ε`.
