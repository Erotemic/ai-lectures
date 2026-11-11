# 126000 — Weak spectral gaps and Hilbert–Schmidt estimates

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `063000`, `069000`, `070000`, `099000`, `125000`. **Next:** `127000`, the generalized tangent bound.

<!-- BEGIN SPOKEN LECTURE -->

# Weak spectral gaps and Hilbert–Schmidt estimates

A spectral gap can mean two rather different things. The spectra may be separated in one ordered direction, or every point of one spectrum may merely be a positive distance from every point of the other. This distinction also separates the hypotheses of Davis and Kahan’s Theorems six point one and six point two.

Theorem six point two allows the weaker, pairwise-distance condition. The price is that its original general estimate is in the square, or Hilbert–Schmidt, norm. We will prove the underlying multiplier inequality, place it in the trial-frame geometry, and give a counterexample to a tempting stronger claim.

## Recall the two gaps

An ordered gap means, for example, that every point of one spectrum lies at least delta below every point of the other. An interval-versus-exterior gap lets one spectrum occupy a middle interval while the other lies outside an expanded interval, with distance at least delta.

A pairwise gap only asserts that each spectral value of one operator is at least delta away from each spectral value of the other. The two spectra can interlace. Their order can change as we move among eigenvalues.

Every ordered gap is a pairwise gap. The converse fails. Consider one diagonal operator with eigenvalues negative one and one, and a second with eigenvalues zero and two. Every cross difference has absolute value at least one, but there is no single ordering that places one entire spectrum above the other.

This weaker hypothesis does not supply a uniformly decaying exponential product. It does, however, supply a pointwise lower bound for each denominator in the diagonal Sylvester equation.

## Prove the square-norm inequality in matrices

Let A zero and Lambda one be finite-dimensional self-adjoint operators, possibly acting on coordinate spaces of different dimensions. Suppose their spectra have pairwise distance at least delta, with delta positive.

Consider the Sylvester equation Lambda one X minus X A zero equals C. Choose orthonormal eigenbases of both operators. In those bases, the entry of the left side in row i and column j is the eigenvalue of Lambda one in row i minus the eigenvalue of A zero in column j, multiplied by the entry of X.

Therefore the absolute value of that entry is at least delta times the absolute value of the corresponding entry of X. Square, sum over all rows and columns, and take square roots.

We get delta times the Frobenius norm of X at most the Frobenius norm of C. This is a constant-one bound for completely interlaced spectra. It does not require their eigenvalues to be ordered.

The proof works because the Frobenius norm is exactly the square root of the sum of squared matrix entries in every pair of orthonormal bases. The operator norm lacks that decomposition, so the entrywise argument cannot simply be recycled.

Work with a two-by-two unknown matrix X. Let the operator multiplying it on the left have eigenvalues one and negative one. Let the operator on the right have eigenvalues zero and two.

The Sylvester equation acts on each matrix entry by multiplying it by a difference of those eigenvalues. Reading across the first row, the differences are one and negative one. Across the second row, they are negative one and negative three. None is smaller than one in magnitude.

If the forcing matrix is C, solving the equation divides each entry of C by its corresponding difference. The sum of squares of the entries can therefore only decrease. That sum of squares is the square of the Frobenius norm. It gives the constant-one Hilbert–Schmidt estimate immediately.

The operator norm measures the largest stretching direction of the whole matrix. It is sensitive to how entries cooperate. Dividing every entry by a number of magnitude at least one does not give the same constant-one assertion in that norm. The spectral geometry must justify a stronger estimate separately.

## Carry the argument into Hilbert space

The Hilbert–Schmidt operators from one Hilbert space to another form a Hilbert space of their own. For self-adjoint A zero and Lambda one, the spectral theorem represents their left and right actions by multiplication in suitable spectral variables.

In that representation the Sylvester map acts, schematically, as multiplication by the real scalar lambda minus mu, where lambda comes from Lambda one and mu comes from A zero. Pairwise separation says the magnitude of this multiplier is at least delta almost everywhere in the relevant product spectral measure.

Integrating the squared magnitude of the transformed operator gives the same estimate: delta times the Hilbert–Schmidt norm of X is at most the Hilbert–Schmidt norm of the Sylvester right-hand side.

For unbounded operators we must first justify the expression on the common domain or via spectral cutoffs. The inequality then survives by convergence in the Hilbert–Schmidt norm where the inputs have finite square energy. It is not permission to compose two arbitrary unbounded operators everywhere.

The infinite-dimensional proof follows the same matrix-entry idea, except that the entries are replaced by a continuous distribution of spectral coordinates. First keep only spectral values in bounded intervals. Within those intervals, multiplication by the inverse spectral difference is well defined and uniformly bounded by one over the gap.

Now enlarge the intervals. Hilbert–Schmidt operators form a Hilbert space, so their spectral cutoffs converge in its squared-sum norm. That convergence passes the estimate to the limit. We need this step because, for unbounded operators, writing a product of operators does not guarantee that every input belongs to the required domains.

## Insert the trial-space residual

Return to the setup of Theorem six point one. We have a frame E zero, its positive lower bound epsilon, an exact complementary coordinate map F one, and the Sylvester unknown X equal to F one adjoint E zero.

The residual equation gives Lambda one X minus X A zero equals F one adjoint R. We now assume only that the spectra of Lambda one and A zero have pairwise distance at least delta.

If R is Hilbert–Schmidt, so is its compression F one adjoint R. The square-norm Sylvester inequality then controls X. Normalize E zero by its polar decomposition by writing the overlap as a polar factor times a positive operator, paying the factor epsilon.

The result is delta epsilon times the Hilbert–Schmidt norm of the directed sine representative at most the Hilbert–Schmidt norm of R.

Theorem six point two trades stronger spectral separation for a more specialized norm: pairwise spectral distance suffices for a Hilbert–Schmidt estimate under its stated hypotheses.

## A numerical obstruction in operator norm

Let the first coefficient matrix be diagonal with entries one and negative one. Let the second be diagonal with entries zero and two. Their pairwise spectral gap is one.

Take X to have rows three, negative three, and negative three, one. Compute C as the first coefficient matrix times X minus X times the second. The result has rows three, three, and three, negative three.

The matrix C has two orthogonal columns, each with length three times the square root of two. Its operator norm is therefore three square root two, around four point two four.

Now compare squared energies before comparing the largest singular values. The four entries of X have squares nine, nine, nine, and one, totaling twenty-eight. Every entry of C has magnitude three, so its square energy is thirty-six. The Frobenius inequality says twenty-eight is at most thirty-six, which is true. Only the distribution of this energy among singular directions makes the operator-norm inequality fail.

The symmetric matrix X has eigenvalues two plus the square root of ten and two minus the square root of ten. Its operator norm is two plus the square root of ten, around five point one six.

Thus the gap, which is one, times the operator norm of X is larger than the operator norm of C. The constant-one operator-norm assertion is false under pairwise separation alone.

In the Frobenius norm, the inequality goes in the other direction. The Frobenius norm of X squared is twenty-eight, while that of C squared is thirty-six. Theorem six point two is entirely consistent with the example.

## What happens if the square norm is infinite?

On an infinite-dimensional Hilbert space, some bounded operators are not Hilbert–Schmidt. The identity operator is an immediate example. Its squared singular-value sum diverges.

For a finite estimate, require that the residual have finite Hilbert–Schmidt energy. Then its compressed right-hand side also has finite energy, and the multiplier estimate provides finite energy of X. The frame-normalization inequality transfers that finiteness to the directed sine.

If the residual has infinite square energy, an extended-valued inequality can still be stated, but it provides no numerical angle bound. This is why ideal membership is a hypothesis in the finite-energy theorem, while the extended theorem allows an infinite right-hand side.

A finite-norm statement and an extended-valued statement are logically different. State which one is intended, including whether ideal membership is a hypothesis or a conclusion.

## Do not replace the square norm by a favorite gauge

We can obtain other bounds under extra assumptions. For example, if the relevant right-hand side has rank at most r, its Frobenius norm is at most the square root of r times its operator norm. Combining this with the square-norm Sylvester bound gives an operator-norm estimate with that rank factor.

A Fourier multiplier construction gives a dimension-free operator-norm bound with the constant pi over two under general separated self-adjoint spectra. But neither argument proves the constant-one operator-norm statement.

Similarly, the nuclear norm, a general Schatten norm, or an arbitrary symmetric ideal gauge requires its own suitable multiplier estimate. We must not read the square-norm theorem as an all-gauge theorem.

## Close

The proof is a single idea used carefully: pairwise spectral distance controls every scalar spectral multiplier in squared energy. The lower-frame bound then converts the crossed residual estimate to a directed sine estimate.

Theorem six point two is precisely the place where a weaker gap works because the Hilbert–Schmidt norm has a coordinatewise quadratic structure.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)


For \(\lambda\in\sigma(\Lambda_1)\), \(\mu\in\sigma(A_0)\), assume \(|\lambda-\mu|\ge\delta\). Then the Hilbert–Schmidt Sylvester multiplier obeys
\[\delta^2\|X\|_{S_2}^2\le\|\Lambda_1X-XA_0\|_{S_2}^2.\]
After frame normalization,
\[\delta\varepsilon\|\sin\Theta_0\|_{S_2}\le\|R\|_{S_2}.\]
The source's finite-energy theorem assumes `approximationNumberEnergy R ≠ ⊤` and concludes finite energy of the sine representative. Its extended `ENNReal` theorem makes the inequality vacuous when the residual's square norm is infinite; it does not assert a finite operator-norm bound with the same constant.


**The same interlaced spectra in two matrix norms.** Put
\[
 \Lambda_1=\operatorname{diag}(1,-1),\quad A_0=\operatorname{diag}(0,2),\quad
 X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix}.
\]
The cross differences are \(\begin{psmallmatrix}1&-1\\-1&-3\end{psmallmatrix}\), so the pairwise spectral separation is \(\delta=1\), and
\[
 C=\Lambda_1X-XA_0=\begin{pmatrix}3&3\\3&-3\end{pmatrix}.
\]
Consequently \(\|X\|_{S_2}^2=28<36=\|C\|_{S_2}^2\), whereas
\[
 \|X\|_{\mathrm{op}}=2+\sqrt{10}>3\sqrt2=\|C\|_{\mathrm{op}}.
\]
The entrywise scalar multiplier gives the constant-one \(S_2\) inequality; the same claim for operator norm is false under the identical gap hypothesis. In spectral-measure language, the finite identity
\(\sum_{ij}|\lambda_i-\mu_j|^2|X_{ij}|^2\ge\delta^2\sum_{ij}|X_{ij}|^2\)
becomes an \(L^2\) estimate on the two spectral variables.

### Exact Lean declaration excerpts


`DavisKahan/Sources/DavisKahan1970/Theorem61.lean` — `theorem6_2_complex` (exact declaration header; proof body omitted):

```lean
theorem theorem6_2_complex
    {E₀' F₀' : Type v}
    [NormedAddCommGroup E₀'] [InnerProductSpace ℂ E₀'] [CompleteSpace E₀']
    [NormedAddCommGroup F₀'] [InnerProductSpace ℂ F₀'] [CompleteSpace F₀']
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) (hdist : PairwiseSpectrumGap A₀ Λ₁ δ)
    (S : SinThetaRepresentativeAcross (E₀ :=
```


`DavisKahan/Sources/DavisKahan1970/Section6SourceScope.lean` — `theorem6_2_vacuity_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem theorem6_2_vacuity_sourceExact_complex
    [NormedAddCommGroup E₀'] [InnerProductSpace ℂ E₀'] [CompleteSpace E₀']
    [NormedAddCommGroup F₀'] [InnerProductSpace ℂ F₀'] [CompleteSpace F₀']
    [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
    [TopologicalSpace.SeparableSpace E]
    [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
    [NormedAddCommGroup G] [InnerProductSpace ℂ G] [CompleteSpace G]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    (A : E →ₗ.[ℂ] E) (A₀ : F →ₗ.[ℂ] F) (Λ₁ : G →ₗ.[ℂ] G)
    (E₀ : F →L[ℂ] E) (F₀ : H →L[ℂ] E) (F₁ : G →L[ℂ] E) (R : F →L[ℂ] E)
    (hA : IsSelfAdjoint A) (hA₀ : IsSelfAdjoint A₀) (hΛ₁ : IsSelfAdjoint Λ₁)
    (htrial : IsTrialResidualEquation A A₀ E₀ R)
    (hexact : IsExactSpectralDecomposition A Λ₁ F₀ F₁)
    {ε : ℝ} (hε : 0 < ε) (hframe : LowerFrameBound E₀ ε)
    {δ : ℝ} (hδ : 0 < δ) (hdist : PairwiseSpectrumGap A₀ Λ₁ δ)
    (S : SinThetaRepresentativeAcross (E₀ :=
```



**Mapping.** `hdist : PairwiseSpectrumGap A₀ Λ₁ δ` is weaker than `FormBoundedSylvesterGap`. `approximationNumberEnergy R ≠ ⊤` expresses the nonvacuous square-norm condition, while the extended-gauge source theorem uses `ENNReal` and is well-defined even when the right-hand side is infinite.

