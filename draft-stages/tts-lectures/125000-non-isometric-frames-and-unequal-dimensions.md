# 125000 — Non-isometric frames and unequal dimensions

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `015000`, `017000`, `035000`, `108000`, `124000`. **Next:** `126000`, weak spectral gaps and Hilbert–Schmidt estimates.

<!-- BEGIN SPOKEN LECTURE -->

# Non-isometric frames and unequal dimensions

A trial subspace is often represented by orthonormal columns, but computational trial frames may be scaled, nonorthogonal, or redundant. The Gram operator measures their failure to have orthonormal coordinates, and that error affects how residual estimates are normalized.

Davis and Kahan's Theorem six point one keeps the trial map itself rather than silently replacing it with an isometry. It permits a non-isometric frame and different dimensions of the trial and exact subspaces. Its additional factor, epsilon, comes directly from a lower bound on that frame.

## Distinguish a frame from its range

Let F be a coordinate Hilbert space and H the ambient Hilbert space. A trial frame E zero is a bounded linear map from F to H. Its range is the trial subspace, assuming it has closed range as guaranteed here by a positive lower bound.

If E zero is an isometry, the length of every coordinate vector is preserved. But for a general frame that is false. The same ambient trial subspace can be described by many different frames, such as an orthonormal frame multiplied by an invertible matrix.

We assume there is a positive epsilon such that the length of E zero x is at least epsilon times the length of x for every coordinate vector x. This says the frame does not collapse any coordinate direction. It also says the inverse on its range has norm at most one over epsilon.

Here epsilon bounds the lengths of trial-frame outputs from below. If lambda-min denotes the smallest eigenvalue of E zero adjoint E zero, the corresponding length bound is the square root of lambda-min. Confusing the length bound with the eigenvalue changes the constant.

## Obtain orthonormal coordinates by polar decomposition

Take the positive modulus of E zero, the square root of E zero adjoint E zero. The lower-frame hypothesis implies this modulus is bounded below by epsilon and therefore has a bounded inverse.

Write the polar decomposition of E zero as W times its modulus. Because E zero is injective with closed range, W is an isometry of F onto the trial subspace. This is a canonical way to normalize the frame without changing its range.

If the smallest singular value of E zero is epsilon, then the inverse of its modulus has operator norm at most one over epsilon. That one inequality will explain the entire normalization penalty.

Picture an exact horizontal plane in three-dimensional space, spanned by the first two coordinate axes. We measure how far a trial plane rises out of it.

Use two trial columns. The first points along the first coordinate axis and has length two. The second has length one quarter. It tilts away from the second coordinate axis toward the vertical axis through an angle theta. The columns are perpendicular, but their lengths differ by a factor of eight.

Their Gram matrix measures those column lengths squared: four and one sixteenth on the diagonal. Taking its positive square root recovers the lengths two and one quarter. This is the matrix we divide out when we turn the columns into an orthonormal frame. The small second column then becomes a unit vector with the same tilt theta.

The smallest frame length is one quarter, so epsilon is one quarter. The normalized frame W has two unit columns; its second column still makes angle theta with the selected plane. Normalization changes the coordinates and the residual's scale, while the trial subspace and its angle stay the same.

## Choose exact spectral coordinates

Let A be a possibly unbounded self-adjoint operator on H. Choose an exact reducing spectral decomposition with an exact selected component and its orthogonal complement. Let F one be an isometric coordinate map into that complementary component, and let Lambda one denote the restricted operator there.

Choose a self-adjoint trial coordinate operator A zero on F. Suppose E zero maps the trial coordinates into the domain of A and satisfies the residual equation: A applied to E zero equals E zero followed by A zero, plus a bounded residual map R.

The domain clause is necessary if A is unbounded. We cannot even write the residual for all coordinates unless E zero lands in the domain. The exact complement is also required to reduce A, so its restricted operator is well-defined on the appropriate domain.

## Compress the residual equation

Apply F one adjoint to the residual identity. Because F one identifies the exact complementary reducing space, F one adjoint A E zero becomes Lambda one applied to F one adjoint E zero.

Define X as F one adjoint E zero. The remaining term is X A zero. Thus we obtain the Sylvester equation: Lambda one X minus X A zero equals F one adjoint R.

The spectral hypothesis is a genuine ordered or interval-versus-exterior Sylvester gap of size delta between A zero and Lambda one. Under that hypothesis, the applicable ideal estimate gives delta times the ideal norm of X no greater than the ideal norm of R. Projection by F one adjoint does not increase the relevant singular values.

But X still contains the nonorthonormal scaling of E zero. It is not yet the intrinsic sine map of the trial subspace.

## Remove the scaling, and find epsilon

Replace E zero by its polar factorization W times the modulus. Then X equals F one adjoint W followed by that modulus.

The map F one adjoint W goes from trial coordinates to complementary exact coordinates. Its singular values are the directed sines. Let us call it S. The raw cross operator X has the same domain and codomain, but its singular values also contain the scaling inherited from E zero.

We have X equals S times the modulus. Multiply on the right by the inverse modulus. Then S equals X times that inverse. Since the inverse has norm at most one over epsilon, every supported unitarily invariant ideal norm obeys epsilon times the norm of S at most the norm of X.

Combine this with the Sylvester bound. The conclusion is delta times epsilon times the directed sine norm no greater than the residual norm.

The two factors have different sources. Delta comes from spectral separation. Epsilon comes from frame conditioning. Neither can be omitted without changing the data being estimated.

Return to the tilted second column. Choose the ambient diagonal operator with eigenvalues zero, zero, and positive d. It ignores horizontal motion and multiplies the vertical coordinate by d. Choose the trial operator to be zero.

The long first column has no vertical component, so its residual vanishes. The shorter column has vertical component one quarter times sine theta. Applying the ambient operator makes its residual length d times sine theta divided by four. That is the only nonzero singular value of the residual.

The unnormalized cross projection has size sine theta divided by four. Once we normalize the frame, the geometric sine is simply sine theta. We have gained a factor of four in the normalized sine because we divided out the quarter-length column. The lower frame bound, one quarter, restores the correct scale: gap d times one quarter times sine theta equals the residual length. Here the estimate is exact.

The calculation also shows why it is the smallest frame length that enters: the residual is concentrated in the column whose normalization requires the largest amplification.

## Check the constant in one dimension

Take the ambient plane with A diagonal, with eigenvalues zero and d, where d is positive. Choose the exact selected subspace as the horizontal axis and its complement as the vertical axis.

Let the trial coordinate space be one-dimensional. Map the unit coordinate to epsilon times the unit vector at angle theta above the horizontal axis. Take the trial coordinate operator A zero to be zero. The residual is simply A applied to the trial vector, which has length epsilon d sine theta.

Here the cross operator X has length epsilon sine theta and the normalized directed sine has value sine theta. The gap delta between the trial zero and the complementary eigenvalue d is exactly d.

Thus delta epsilon sine theta equals the residual norm. The estimate is sharp for every positive epsilon and every theta between zero and a right angle.

If we had omitted epsilon, shrinking the frame would make the residual arbitrarily small while the subspace angle stayed fixed. The inequality would become false. The factor is therefore mathematically necessary.

## Unequal dimensions require a direction

Now consider a line U inside a plane V in three-dimensional space. The directed sine from U toward V is zero because every vector of U lies in V. But the reverse directed sine from V toward U is one, since V contains a direction perpendicular to U.

An ambient projection difference registers that missing direction and has norm one. A theorem based only on the trial map E zero and the complementary part of the exact decomposition generally controls the first directed sine, not the entire ambient projection difference.

Theorem six point one therefore allows the trial and exact selected coordinates to have different dimensions without pretending that both directed angles are equal. The conclusion is stated for a representative having the appropriate directed sine singular values.

This is also why a convenient rectangular operator representative is allowed in the formal statement. Different source and target coordinate spaces can carry the same nonzero singular-value list, possibly supplemented by zeros. The ideal norm depends on that list rather than on how the representative is embedded.

## What the theorem does and does not promise

A positive lower-frame bound does not itself establish spectral separation. A small residual does not determine which exact cluster to compare against. The theorem needs the self-adjoint coordinate operators, exact spectral decomposition, domain-aware residual, positive frame bound, and a legitimate Sylvester gap.

In a symmetric ideal one must also assume the residual belongs to the ideal and prove that the sine representative belongs to it. That membership is part of the conclusion, not a default property of arbitrary bounded operators.

The original Section six theorem uses interval-versus-exterior spectral separation, with either ordering allowed. An equivalent or stronger abstract gap condition may also support the analytic estimate, but the interval-versus-exterior assumption is the one used in the original theorem.

## Summary

The result can be reconstructed from three moves. Compress the residual to obtain a Sylvester equation. Bound the crossed operator X by the residual using the spectral gap. Normalize the frame by polar decomposition, paying exactly the inverse lower-frame bound.

The formula is delta epsilon times the directed sine norm at most the residual norm.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)


For \(E_0:F\to H\), the Lean predicate `LowerFrameBound E₀ ε` records \(\|E_0x\|\ge\varepsilon\|x\|\). Polar decomposition gives \(E_0=W|E_0|\), with \(W^*W=I_F\) and \(\||E_0|^{-1}\|\le1/\varepsilon\). The raw crossed map \(X=F_1^*E_0\) satisfies a domain-aware Sylvester equation; the normalized directed sine is represented by \(S=F_1^*W=X|E_0|^{-1}\). Thus
\[\delta\,\varepsilon\,N(S)\le N(R).\]
`SinThetaRepresentativeAcross` permits equivalent rectangular realizations, while `IsTrialResidualEquation` and `IsExactSpectralDecomposition` encode the actual domain and exact-reduction obligations. The paper-facing spectral condition is interval/exterior separation, rather than an arbitrary `PairwiseSpectrumGap`.


**A conditioned two-column frame attaining the estimate.** On \(H=\mathbb R^3\), let \(U=\operatorname{span}(e_1,e_2)\), \(A=\operatorname{diag}(0,0,d)\) with \(d>0\), \(F=\mathbb R^2\), and
\[
 W=\begin{pmatrix}1&0\\0&\cos\theta\\0&\sin\theta\end{pmatrix},\qquad
 D=\operatorname{diag}(2,\tfrac14),\qquad E_0=WD,\qquad A_0=0.
\]
Then \(E_0^*E_0=D^2=\operatorname{diag}(4,1/16)\), so \(\varepsilon=1/4\) is the optimal lower frame bound. With \(F_1=e_3\) and \(\Lambda_1=d\),
\[
 X=F_1^*E_0=(0,\tfrac14\sin\theta),\quad
 S=F_1^*W=(0,\sin\theta),\quad
 R=AE_0=(0,0,\tfrac d4\sin\theta)\,e_2^*.
\]
Here \(R\) denotes the \(3\times2\) map whose second column is \((d\sin\theta/4)e_3\); equivalently \(R=(d\sin\theta/4)e_3 e_2^*\). For \(0<\theta<\pi/2\), each map has rank one, and
\[
 \delta\varepsilon\|S\|_{S_q}=d\tfrac14\sin\theta=\|R\|_{S_q}
\]
for every finite Schatten \(q\) and in operator norm. This checks the factor \(1/\varepsilon\) and separates raw leakage from the intrinsic angle.

### Exact Lean declaration excerpts


`DavisKahan/Sources/DavisKahan1970/Theorem61.lean` — `theorem6_1_complex` (exact declaration header; proof body omitted):

```lean
theorem theorem6_1_complex
    {E₀' F₀' : Type v}
    [NormedAddCommGroup E₀'] [InnerProductSpace ℂ E₀'] [CompleteSpace E₀']
    [NormedAddCommGroup F₀'] [InnerProductSpace ℂ F₀'] [CompleteSpace F₀']
    (N : SymmetricNormingFunction)
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) (hgap : FormBoundedSylvesterGap A₀ Λ₁ δ)
    (S : SinThetaRepresentativeAcross (E₀ :=
```


`DavisKahan/Sources/DavisKahan1970/Section6SourceScope.lean` — `theorem6_1_printedGap_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem theorem6_1_printedGap_sourceExact_complex
    [NormedAddCommGroup E₀'] [InnerProductSpace ℂ E₀'] [CompleteSpace E₀']
    [NormedAddCommGroup F₀'] [InnerProductSpace ℂ F₀'] [CompleteSpace F₀']
    [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [TopologicalSpace.SeparableSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
    [NormedAddCommGroup G] [InnerProductSpace ℂ G] [CompleteSpace G]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) {β α : ℝ} (hβα : β ≤ α)
    (hgap : DavisKahan.Sylvester.RealSpectrumIntervalExteriorGap A₀ Λ₁ β α δ)
    (S : SinThetaRepresentativeAcross (E₀ :=
```



**Mapping.** `E₀` is the bounded, potentially non-isometric trial map; `F₀` and `F₁` give exact spectral coordinates. `A`, `A₀`, and `Λ₁` are the closed self-adjoint ambient, trial, and complementary operators. `htrial` and `hexact` carry domain and reduction data; `hframe` and `hε` expose the normalization factor. `S` specifies a singular-value-equivalent sine representative; `hR` asserts ideal membership.

