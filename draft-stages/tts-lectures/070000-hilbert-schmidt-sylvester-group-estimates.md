# 070000 — Hilbert–Schmidt Sylvester group estimates

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `057000` Schatten and Frobenius norms; `062000–069000` Sylvester equations and spectral gap estimates. **Next:** `071000` Sylvester identities for compressed blocks.

<!-- BEGIN SPOKEN LECTURE -->

# The matrix equation becomes an equation on a Hilbert space

Take a column map C with entries two and four. Let A on the output plane have eigenvalues negative two and positive two, while B on the input line is zero. To solve A X minus X B equals C, divide the two coordinates by their spectral differences. The answer X is the column negative one, two.

The length of C is twice the square root of five. The length of X is the square root of five. Their ratio reflects the spectral gap of two. In this column example there is only one input direction, so the ordinary operator norm and the Hilbert-Schmidt norm happen to agree.

With more columns, the Hilbert-Schmidt norm has a special advantage. It treats the entries of a matrix as orthogonal coordinates of a new vector. Once we make that change of viewpoint, the Sylvester equation becomes an ordinary self-adjoint operator equation on a Hilbert space of maps.

## Treat rectangular maps as vectors

Consider a two-by-three complex matrix. It is a map from three-dimensional input space to two-dimensional output space. But it can also be seen as a vector with six complex coordinates.

Its Hilbert-Schmidt norm is the square root of the sum of the squared magnitudes of those six entries. We can define an inner product of two matrices by summing the conjugate of each entry of the first times the corresponding entry of the second.

Why is this useful? Imagine separating a matrix into blocks by orthogonal output and input projections. Blocks belonging to different pairs of projections are perpendicular in this matrix Hilbert space. The total squared norm is exactly the sum of their squared norms.

For the two-by-two matrix with entries one, two, three, four, that total squared norm is one plus four plus nine plus sixteen, or thirty. Rearranging it into individual entry blocks does not change the sum. Operator norm, which asks for the single most stretched input direction, has no such additivity rule.

## The Sylvester map is self-adjoint here

Let A be bounded and self-adjoint on the output Hilbert space and B bounded and self-adjoint on the input Hilbert space. Define a new operator on Hilbert-Schmidt maps: send Z to A Z minus Z B. Call it the Sylvester map S.

We can move A from one argument of the Hilbert-Schmidt inner product to the other, because A equals its adjoint. We can do the same for B. The minus sign stays attached to the right multiplication. Therefore S is self-adjoint on this Hilbert space of maps.

This is a change in the level at which we apply spectral theory. A and B act on ordinary vectors in different spaces. S acts on entire cross-space operators, and its spectral values describe differences between the spectral values of A and B.

## One rank-one map at a time

In finite dimensions choose an orthonormal eigenbasis for A and another for B. Pick one output eigenvector u, with eigenvalue a, and one input eigenvector v, with eigenvalue b.

Build a rank-one map that measures how much an input points along v, and produces that multiple of u. Apply the Sylvester map to this rank-one operator. Left multiplication by A gives a copies of the map. Right multiplication by B gives b copies. Their difference is a minus b copies.

So the rank-one map is an eigenvector of S, with eigenvalue a minus b. All pairs of eigenvectors give an orthonormal basis for the Hilbert space of matrices.

In the running column example, there are two such rank-one maps and their Sylvester eigenvalues are negative two and positive two. A spectral gap around zero for S is exactly the assertion that neither cross difference is too small.

## Prove the square-norm gap estimate

Suppose every cross-spectral difference has absolute value at least delta, where delta is positive. Expand any matrix Z in the rank-one eigenbasis. The Sylvester map multiplies each coefficient by its own difference a minus b.

Square the Hilbert-Schmidt norm after applying S. Each coefficient contributes its original squared magnitude times the square of that difference. Every multiplier is at least delta squared. Add over all coefficients, and take a square root.

The result says: the Hilbert-Schmidt norm of S Z is at least delta times the Hilbert-Schmidt norm of Z. If S X equals C, this becomes delta times the Hilbert-Schmidt norm of X at most the Hilbert-Schmidt norm of C.

Notice why the constant is one. We used a spectral lower bound on each orthogonal coordinate and then added squares. We never inserted a comparison between different matrix norms.

For our column, delta is two, and the estimate is an equality. In a full matrix with interlaced spectra, it remains valid even when the same constant-one statement in operator norm fails. The proof has not changed; the definition of the norm is doing essential work.

## A unitary group on the space of maps

There is a dynamical way to view the same self-adjoint Sylvester map. Evolve a map Z by multiplying it on the left with the exponential of i times t A, and on the right with the exponential of negative i times t B.

Because both factors are unitary, this evolution preserves the Hilbert-Schmidt inner product. Applying time s and then time t is the same as evolving for s plus t. We have a unitary group acting on a space whose vectors happen to be operators.

For bounded A and B, differentiating at zero gives i times A Z minus Z B, or i times S Z. So S is the self-adjoint generator after removing i. Its spectral gap is the cross-spectral gap between A and B.

This viewpoint replaces entrywise manipulation with spectral theory for a single operator. It also explains the appearance of the same left-right evolution in Fourier representations of Sylvester inverses.

## Extend from matrices to infinite dimensions

An infinite-dimensional bounded operator need not be Hilbert-Schmidt. The identity map on a countably infinite-dimensional Hilbert space sends every basis vector to a vector of length one, so the sum of squared output lengths diverges.

Hilbert-Schmidt operators form a complete Hilbert space in their own norm. Left or right multiplication by a bounded operator preserves this class, and unitary multiplications preserve its inner product.

For bounded self-adjoint A and B, we can define the same self-adjoint Sylvester map on that Hilbert-Schmidt space. We cannot expect ordinary eigenvectors of A and B to span everything when their spectra have continuous parts. Instead, use their spectral projections onto narrow bands.

A block of an operator connecting one output band to one input band is almost multiplied by the difference of the two band centers. The approximation error is controlled by the band widths. Blocks for different pairs of spectral bands are orthogonal in Hilbert-Schmidt norm.

As the bands narrow, the approximate scalar differences give the same lower bound. One may express this more directly with the spectral measure of S: the entire spectrum of S stays at least delta away from zero when the two original spectra are separated by delta.

The gap then makes S invertible on the Hilbert-Schmidt space, with inverse norm at most one over delta.

## When the known solution was only bounded

There is a further issue worth distinguishing from the inequality. Suppose C is Hilbert-Schmidt but someone has handed us a merely bounded solution X of the Sylvester equation. Are we allowed to apply a Hilbert-Schmidt estimate to X before knowing that X is Hilbert-Schmidt?

No. First construct a Hilbert-Schmidt solution Y using the inverse of S on the Hilbert-Schmidt space. This Y also solves the equation as a bounded cross-operator. For bounded operators A and B with disjoint spectra, the bounded Sylvester solution is unique. Hence X equals Y, and X is Hilbert-Schmidt after all. Only then apply the square-norm estimate.

This order prevents a common circular argument: assuming ideal membership in order to prove ideal membership.

For unbounded self-adjoint A or B, the unitary groups remain strongly continuous, but their generator lives on a specified domain. One must prove domain compatibility of the Sylvester expression and use the appropriate closed generator; a formula using A Z and Z B cannot automatically be applied to every Hilbert-Schmidt Z.

## What the estimate gives a subspace problem

If a projected subspace error X satisfies a Sylvester equation, its residual C is the known quantity. The spectral gap for the two compressed coefficients controls the Hilbert-Schmidt size of X without a dimension factor.

The geometric interpretation of X then converts that estimate into an angle bound. But the intermediate step is still a theorem about the space of Hilbert-Schmidt maps. It is the square-sum structure, rather than a generic appeal to spectral distance, that provides the constant-one estimate under arbitrary pairwise separation.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

For finite Hilbert spaces, equip rectangular maps with
\[
\langle Z,W\rangle_{HS}=\operatorname{tr}(Z^*W),\qquad
\mathscr S(Z)=AZ-ZB.
\]
For self-adjoint \(A,B\), the induced \(\mathscr S\) is self-adjoint; on rank-one eigenblocks \(u_i v_j^*\) it has eigenvalue \(a_i-b_j\). Hence, under \(\operatorname{dist}(\sigma(A),\sigma(B))\ge\delta>0\),
\[
\|\mathscr S Z\|_{HS}^2=\sum_{i,j}|a_i-b_j|^2|z_{ij}|^2
\ge\delta^2\|Z\|_{HS}^2.
\]
For infinite-dimensional Hilbert spaces, the spectral-block and unitary-group construction replaces the finite eigenbasis. The source theorem also proves Hilbert–Schmidt membership of a bounded solution when the defect has finite energy.

**The same exact column in the matrix-Hilbert-space picture.** For
\[
 A=\operatorname{diag}(-2,2),\quad B=[0],\quad
 C=(2,4)^\mathsf T,\quad X=(-1,2)^\mathsf T,
\]
we have \(\mathscr S(X)=AX-XB=C\) and
\[
\|C\|_{HS}^2=20,\qquad \|X\|_{HS}^2=5,\qquad
\delta^2\|X\|_{HS}^2=4\cdot5=20=\|C\|_{HS}^2.
\]
For bounded self-adjoint \(A,B\), the induced bounded self-adjoint
\(\mathscr S\) acts on the Hilbert space \(S_2(H_{in},H_{out})\).
Spectral separation yields
\(\operatorname{dist}(0,\sigma(\mathscr S))\ge\delta\), hence
\(\|\mathscr S^{-1}\|_{S_2\to S_2}\le1/\delta\).
A bounded solution for a Hilbert-Schmidt right-hand side belongs to \(S_2\)
by bounded-solution uniqueness and comparison with this \(S_2\) solution.
The generator for unbounded \(A,B\) requires its own domain statement.

**Lean bridge (verified source excerpts).**

`DavisKahan/Sources/DavisKahan1970/Sylvester/HilbertSchmidtEstimate.lean` — `hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap` (exact source declaration header):

```lean
theorem hilbertSchmidt_sylvester_le_of_pairwiseSpectrumGap
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
    (hC : approximationNumberEnergy C ≠ ⊤) :
    approximationNumberEnergy X ≠ ⊤ ∧
      δ * ContinuousLinearMap.hilbertSchmidtNorm X ≤ ContinuousLinearMap.hilbertSchmidtNorm C :=
```

The hypotheses require complex Hilbert spaces, self-adjoint partial operators, a positive pairwise spectral gap, an exact Sylvester equation, and finite defect approximation-number energy. The conclusion includes both solution ideal membership and the sharp square-norm estimate.

`ForTauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Block.lean` — `tsum_enorm_sq_blockFun` (exact source declaration header):

```lean
theorem tsum_enorm_sq_blockFun {ι' : Type*} (b : HilbertBasis ι 𝕜 F)
    (P : ι' → (E →L[𝕜] E)) (Q : ι' → (F →L[𝕜] F))
    (hP : ∀ v : E, ∑' i, ‖P i v‖ₑ ^ 2 = ‖v‖ₑ ^ 2)
    (hQ : ∀ v : F, ∑' j, ‖(Q j).adjoint v‖ₑ ^ 2 = ‖v‖ₑ ^ 2)
    (f : lp (fun _ : ι => E) 2) :
    ∑' p : ι' × ι', ‖blockFun b (P p.1) (Q p.2) f‖ₑ ^ 2 = ‖f‖ₑ ^ 2 := by
```

This is the orthogonal block-energy reassembly on the ell-two column model, subject to norm-splitting hypotheses for the two projection families.
