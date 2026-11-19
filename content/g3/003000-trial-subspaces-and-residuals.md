# 003000 — Trial subspaces and residuals

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** spectral. **Audience:** self-adjoint operators and spectral subspaces, isometric frames, eigenvalues of symmetric matrices.

<!-- BEGIN SPOKEN LECTURE -->

Trial subspaces and residuals

In practice we almost never know an exact eigenspace. We have a candidate: a subspace produced by a numerical method, by an approximation of a differential equation, or by the eigenspace of a nearby operator. The question Davis and Kahan answer is how far such a candidate can be from the exact spectral subspace, given information we can actually compute. The computable information is a residual. This lecture defines it, interprets it, and shows what it already tells us before any angle theorem is proved.

Here is what we will establish. First, a trial subspace is described by an isometric frame E zero and a trial operator A zero, and the residual R equals A hat E zero minus E zero A zero; the residual is zero exactly when the trial subspace is invariant and A zero represents the operator on it. Second, among all choices of trial operator, the Rayleigh–Ritz choice, E zero star A hat E zero, gives the smallest residual, and its residual is perpendicular to the trial subspace. Third, when the operator is a perturbation A hat equal to A plus H, and the trial frame is an exact eigenspace frame of A, the residual is H E zero, so its norm is at most the norm of H. Fourth, residuals control eigenvalues: there are eigenvalues of A hat within the size of the residual of the trial eigenvalues. Weyl's inequality says the same thing for a perturbation. Fifth, eigenvalue control does not give eigenvector control: a two by two example has identical eigenvalues and perpendicular eigenvectors, which is why a spectral gap must enter.

One vector

Start with one unit vector v and an operator A hat. How close is v to being an eigenvector? If it were one, A hat v would be a multiple of v. So choose a number rho and measure the failure: the vector r equal to A hat v minus rho v.

Which rho? The natural choice is the one that makes r as short as possible. As rho varies, rho v runs along the line through v, and r is the difference between A hat v and a point of that line. The difference is shortest when rho v is the orthogonal projection of A hat v onto the line, which means rho equals the inner product of v with A hat v. This is the Rayleigh quotient of v. With that choice, the residual r is perpendicular to v.

The paper's first figure makes this concrete. Let A hat be the diagonal matrix with entries one point nine and zero point seven, and let v be the unit vector at forty degrees above the horizontal axis, with coordinates cosine forty degrees and sine forty degrees. The Rayleigh quotient rho is one point nine times cosine squared forty plus zero point seven times sine squared forty, which is about one point four zero. The residual has coordinates about zero point three eight and minus zero point four five, its length is about zero point five nine, and it is perpendicular to v.

Now compare with the exact subspaces. The eigenvector for one point nine is the horizontal axis, and the eigenvector for zero point seven is the vertical axis. Suppose the horizontal axis is the subspace we want. The part of v outside it has length sine forty degrees, about zero point six four. That is the error we would like to bound.

Look at the vertical component of the residual. It equals zero point seven minus rho, times sine forty degrees. That is a simple identity: projecting the residual onto the unwanted axis gives the unwanted eigenvalue minus rho, times the unwanted component of v. So the length of the unwanted part of the residual is the distance from rho to the unwanted eigenvalue, about zero point seven zero, times the sine of the angle. Since a part of a vector is no longer than the whole vector, the distance from rho to the unwanted eigenvalue times the sine of the angle is at most the length of the residual. In numbers, zero point four five is at most zero point five nine. Dividing, the sine of the angle is at most zero point five nine over zero point seven zero, about zero point eight four. The true value is zero point six four.

That small calculation is the whole sine-theta theorem in one dimension: a computable residual, divided by the separation between the trial value and the unwanted spectrum, bounds the sine of the angle to the wanted eigenspace. The rest of the theory makes it work for whole subspaces, for every unitarily invariant norm, and in infinite dimensions.

Trial frames and trial operators

For a trial subspace of any dimension, replace the vector v by an isometry E zero from a coordinate Hilbert space into the ambient space. E zero takes a list of coordinates to a vector of the trial subspace, without changing lengths, and E zero star E zero is the identity on coordinates. Replace the number rho by a self-adjoint operator A zero on the coordinate space, the trial operator. It plays the role of the operator restricted to the trial subspace, written in trial coordinates.

The residual is R equal to A hat E zero minus E zero A zero. It takes trial coordinates to the ambient space, and compares two ways of acting: apply A hat to the trial vector, or apply A zero to the coordinates and then embed. If A hat is unbounded, this is required on the domain of A zero, with E zero carrying that domain into the domain of A hat, and R is the bounded operator agreeing with the difference there.

If R is zero, then A hat maps every trial vector to another trial vector, so the trial subspace is invariant, and, for a self-adjoint operator, reducing. A zero is then exactly the operator on that subspace in trial coordinates. A nonzero residual measures the failure of invariance. It is an operator, not a number, and in an eigenbasis of A zero its columns are the individual residuals of the trial eigenpairs: for each eigenvector of A zero with eigenvalue alpha, applying R gives A hat applied to the corresponding trial vector minus alpha times that vector.

The Rayleigh–Ritz choice

The trial operator is ours to choose. The paper's theorems allow any self-adjoint A zero satisfying their spectral hypotheses. But there is a best choice for making the residual small.

Split the residual into its part inside the trial subspace and its part outside. The part inside, in coordinates, is E zero star R, which equals E zero star A hat E zero minus A zero. The part outside is the identity minus E zero E zero star, applied to R, and since that projection kills E zero A zero, it equals the identity minus E zero E zero star, times A hat E zero. The outside part does not depend on A zero at all. By the Pythagorean theorem, for every coordinate vector x, the squared length of R x is the squared length of the inside part plus the squared length of the outside part. Only the inside part can be changed, and it vanishes exactly when A zero equals E zero star A hat E zero.

That choice is the Rayleigh–Ritz operator, the compression of A hat to the trial subspace. Its eigenvalues are the Ritz values, and its eigenvectors, embedded by E zero, are the Ritz vectors. For a one-dimensional trial subspace it is the Rayleigh quotient. With this choice, E zero star R is zero: the residual is perpendicular to the trial subspace, a condition called Galerkin orthogonality. Every other choice of A zero produces a residual at least as large, vector by vector, and therefore in every unitarily invariant norm.

Davis and Kahan express the same fact in block form. Relative to the trial subspace and its complement, the perturbation H has diagonal block H zero on the trial subspace and off-diagonal block B. With the trial operator inherited from A, R star R equals H zero squared plus B star B. The Rayleigh–Ritz choice removes H zero and leaves only B star B. The condition H zero equal to zero is one of the hypotheses of the tangent theorem, and the stronger condition that both diagonal blocks of H vanish appears in the doubled-tangent theorem; these are different hypotheses and the paper keeps them apart.

But the residual must always be paired with its own trial operator. Return to the forty-degree vector. If instead of the Rayleigh quotient we take the trial value to be one point nine, the wanted eigenvalue itself, the residual becomes A hat v minus one point nine v. Its horizontal part vanishes, and its vertical part is zero point seven minus one point nine, times sine forty degrees, of length about zero point seven seven. This residual is longer. But the separation of the trial value one point nine from the unwanted eigenvalue zero point seven is also larger, one point two, and one point two times sine forty degrees is exactly zero point seven seven. The bound holds with equality. Each choice of trial operator gives a valid pair of residual and separation, and the two must be used together. Combining the shorter Rayleigh–Ritz residual with the larger separation of the other choice would give a false bound.

Residuals from a perturbation

The second formulation in the Davis–Kahan paper starts from a perturbation. Let A be a self-adjoint operator whose spectral subspaces we know, and let A hat equal A plus H, with H bounded and self-adjoint. Take E zero to be a frame for an exact spectral subspace of A, and A zero to be the block of A on that subspace. Then A E zero equals E zero A zero, and the residual for A hat is A hat E zero minus E zero A zero, which is H E zero.

So the residual is the perturbation applied to the old eigenspace, and its norm is at most the norm of H, in the operator norm and in every unitarily invariant norm in which H is finite. A bound on angles in terms of the residual immediately becomes a bound on the angle between the spectral subspace of A and the corresponding spectral subspace of A plus H, in terms of the size of H. This is how the theorem is used in statistics and numerical analysis: we know A, or an estimate of it, and we only know that the perturbation is small.

The beam example in the paper is of this kind. The unperturbed beam operator has a two-dimensional null space spanned by the rigid motions, and E zero is a frame for it, with A zero equal to zero. The perturbation is multiplication by epsilon t. So the residual is epsilon t times each rigid motion. If instead we use the Rayleigh–Ritz operator, E zero star H E zero, we find the diagonal matrix with entries epsilon times one half minus one over two root three, and epsilon times one half plus one over two root three, about zero point two one epsilon and zero point seven nine epsilon. These are the Ritz values, and the corresponding residual is smaller.

What residuals say about eigenvalues

The residual already controls eigenvalues, without any gap hypothesis.

For one vector, the argument is short. Expand the unit vector v in an orthonormal eigenbasis of A hat, with coefficients c i and eigenvalues lambda i. The squared length of A hat v minus rho v is the sum of lambda i minus rho, squared, times the squared absolute value of c i. Each term is at least the smallest squared distance from rho to an eigenvalue, times the squared coefficient, and the squared coefficients add up to one. So some eigenvalue of A hat lies within the length of the residual of rho. In the forty-degree example, the residual has length about zero point five nine, and indeed the nearer eigenvalue, one point nine, is within zero point five of rho. The same argument works for any self-adjoint operator, using the spectral measure in place of the eigenbasis.

For a whole trial subspace, Davis and Kahan record the corresponding fact: if alpha one through alpha m are the eigenvalues of A zero, then m eigenvalues of A hat can be matched to them so that each pair differs by at most the operator norm of R, and the sum of their squared differences is at most the squared Hilbert–Schmidt norm of R.

For a perturbation, the classical statement is Weyl's inequality. If A and A plus H are Hermitian matrices of the same size, with their eigenvalues listed in increasing order, then the k-th eigenvalue of A and the k-th eigenvalue of A plus H differ by at most the operator norm of H. The proof goes through the Courant–Fischer min-max principle, which describes the k-th eigenvalue as the largest value, over all subspaces of dimension k, of the smallest Rayleigh quotient on that subspace. Adding H changes every Rayleigh quotient by at most the norm of H, so every min-max value moves by at most that much. Eigenvalues are stable: they move no more than the perturbation.

Eigenvalues are not eigenvectors

Here is the example in the paper that shows why a separate theory is needed for eigenvectors. For a small positive number epsilon, let A be the two by two diagonal matrix with entries zero and epsilon, and let A hat be the diagonal matrix with entries epsilon and zero.

The two matrices have exactly the same eigenvalues, zero and epsilon, so Weyl's inequality is satisfied with room to spare. Their difference has operator norm epsilon. Yet the eigenvector of A for the lower eigenvalue zero is the horizontal axis, and the eigenvector of A hat for zero is the vertical axis. They are perpendicular. An arbitrarily small perturbation, in an absolute sense, has turned the lowest eigenvector through ninety degrees.

What went wrong? The perturbation is small, but not small compared with the gap. The two eigenvalues of A are separated by exactly epsilon, the same as the norm of the perturbation. An eigenvector question has to compare the size of the perturbation, or of the residual, with a spectral separation. And when eigenvalues are repeated or tightly clustered, individual eigenvectors are not even well defined, while the whole spectral subspace for the cluster is. That is why Davis and Kahan bound angles between subspaces, and why every one of their theorems divides a residual or a perturbation by a gap delta.

Where these ideas come from

Rayleigh estimated vibration frequencies in his Theory of Sound, published in 1877, by evaluating energy ratios on trial shapes, and Walter Ritz turned this into a systematic method of finite-dimensional trial spaces in work published in 1909. Hermann Weyl's 1912 paper on the asymptotic distribution of eigenvalues contains the eigenvalue comparison inequalities that bear his name. Chandler Davis studied the rotation of eigenvectors under perturbation in papers of 1963 and 1965, and the 1969 announcement and 1970 paper with William Kahan treat both formulations at once: the trial subspace with its residual, and the exact subspace of a perturbed operator.

To summarize. A trial subspace is given by an isometric frame E zero and a trial operator A zero, and the residual R is A hat E zero minus E zero A zero, defined on the domain of A zero and bounded. R is zero exactly when the trial subspace is invariant. The Rayleigh–Ritz operator E zero star A hat E zero minimizes the residual and makes it perpendicular to the trial subspace, but every trial operator gives a valid residual, which must be paired with its own spectral separation. When A hat is A plus H and the trial frame is an exact frame for A, the residual is H E zero, with norm at most that of H. Residuals and perturbations control eigenvalues directly, through the Rayleigh quotient argument and Weyl's inequality. They do not control eigenvectors without a gap: the swapped diagonal matrices have the same eigenvalues and perpendicular eigenvectors.

In the forty-degree example, the unwanted part of the residual was exactly the separation times the sine of the angle. In higher dimensions the same relation becomes an operator equation, a Sylvester equation, and turning it into an inequality is where the shape of the spectral gap begins to matter.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### One vector (journal paper, Figure 1)

\(\widehat A=\operatorname{diag}(1.9,0.7)\), \(v=(\cos40^\circ,\sin40^\circ)\):
\(\rho=\langle v,\widehat Av\rangle\approx1.4042\), \(r=\widehat Av-\rho v\approx(0.3798,-0.4526)\), \(\|r\|\approx0.5909\), \(r\perp v\).
\(\delta=\rho-0.7\approx0.7042\), \(\|P_{\rm exact}^\perp r\|=\delta\sin\theta\approx0.4526\le\|r\|\), so \(\sin\theta\le\|r\|/\delta\approx0.839\) (true \(0.643\)).
With trial value \(1.9\): \(r'=(0,-0.7713)\), \(\delta'=1.2\), \(\delta'\sin\theta=\|r'\|\) (equality).
\(\operatorname{dist}(\rho,\sigma(\widehat A))\approx0.496\le\|r\|\).

### Trial frames and the Rayleigh–Ritz choice

\(E_0^*E_0=I\), \(R=\widehat AE_0-E_0A_0\) (on \(\operatorname{dom}A_0\), bounded extension).
\[
E_0^*R=E_0^*\widehat AE_0-A_0,\qquad (I-E_0E_0^*)R=(I-E_0E_0^*)\widehat AE_0,
\]
\[
\|Rx\|^2=\|(E_0^*\widehat AE_0-A_0)x\|^2+\|(I-E_0E_0^*)\widehat AE_0x\|^2 .
\]
Rayleigh–Ritz: \(A_0=E_0^*\widehat AE_0\Rightarrow E_0^*R=0\). Davis–Kahan (1.8): with \(H\sim\begin{pmatrix}H_0&B^*\\B&H_1\end{pmatrix}\) and \(A_0\) inherited from \(A\), \(R^*R=H_0^2+B^*B\).

### Perturbation form

\(AE_0=E_0A_0\Rightarrow R=HE_0\), \(N(R)\le N(H)\) for unitarily invariant \(N\) (since \(\|E_0\|=1\)).
Beam: \(E_0^*HE_0=\varepsilon\operatorname{diag}\bigl(\tfrac12-\tfrac1{2\sqrt3},\ \tfrac12+\tfrac1{2\sqrt3}\bigr)\approx\varepsilon\operatorname{diag}(0.211,0.789)\).

### Eigenvalue control

- One vector: \(\|(\widehat A-\rho)v\|^2=\sum_i(\lambda_i-\rho)^2|c_i|^2\ge\operatorname{dist}(\rho,\sigma(\widehat A))^2\).
- Davis–Kahan (after (1.8)): eigenvalues \(\alpha_j\) of \(A_0\) can be matched with eigenvalues \(\lambda_j\) of \(\widehat A\) so that \(|\alpha_j-\lambda_j|\le\|R\|_{\rm op}\) and \(\sum_j(\alpha_j-\lambda_j)^2\le\|R\|_{\rm HS}^2\).
- Weyl: \(\max_k|\lambda_k(A)-\lambda_k(A+H)|\le\|H\|_{\rm op}\), via Courant–Fischer \(\lambda_k=\max_{\dim S=k}\min_{x\in S,\|x\|=1}\langle Ax,x\rangle\).
- Swap example: \(A_\varepsilon=\operatorname{diag}(0,\varepsilon)\), \(\widehat A_\varepsilon=\operatorname{diag}(\varepsilon,0)\): same eigenvalues, \(\|A_\varepsilon-\widehat A_\varepsilon\|=\varepsilon\), lowest eigenvectors perpendicular; gap \(=\varepsilon=\) perturbation norm.

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/SineTheta/Presentation.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
structure IsTrialResidual
    (A : E →ₗ.[𝕜] E)
    (A₀ : F →ₗ.[𝕜] F)
    (E₀ : F →L[𝕜] E)
    (R : F →L[𝕜] E) : Prop where
  isometry : IsometricEmbedding E₀
  mapsDomain : ∀ x : A₀.domain, E₀ (x : F) ∈ A.domain
  residualEquation : ∀ x : A₀.domain,
    A ⟨E₀ (x : F), mapsDomain x⟩ -
      E₀ (A₀ x) = R (x : F)
```

**Mapping notes.**

- Lean's `A` is the operator under study, \(\widehat A\) in the lecture.
- `IsTrialResidual` places no condition on `A₀` beyond what the theorem using it adds (self-adjointness, a gap); the Rayleigh–Ritz choice is a special case, matching the paper's statement that the theorem allows other self-adjoint trial operators.
- Weyl's inequality and Courant–Fischer were formalized in this development and later adapted into Tau Ceti (journal paper, §2.9); their provenance is documented in the formalization repository's `papers/dk_formalization_journal/COURANT_FISCHER_LINEAGE_AUDIT.md`.
