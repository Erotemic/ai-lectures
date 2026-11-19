# 001000 — Spectral subspaces and exact decompositions

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** spectral. **Audience:** self-adjoint matrices and their eigenspaces, orthogonal projections, isometric frames, basic complex analysis.

<!-- BEGIN SPOKEN LECTURE -->

Spectral subspaces and exact decompositions

The sine-theta theorem compares an approximate subspace with an exact one. This lecture is about the exact one: what it means for a subspace to be exactly preserved by a self-adjoint operator, how the operator splits into blocks around such a subspace, and how the spectral theorem produces these subspaces from regions of the spectrum. By the end we will have the precise form in which the Davis–Kahan paper states its exact data: two isometric frames, F zero for the wanted subspace and F one for its orthogonal complement, and a self-adjoint operator Lambda one describing the operator on the complement.

The results are these. First, for a self-adjoint operator, a closed subspace that the operator maps into itself automatically has a complement that the operator also maps into itself; invariant and reducing are the same. Second, with isometric frames for the subspace and its complement, the operator becomes block diagonal, with blocks Lambda zero and Lambda one, and its spectrum is the union of theirs. Third, the spectral theorem assigns an orthogonal projection to every Borel set of real numbers, and the range of each such projection is a reducing subspace on which the operator has spectrum inside the closure of the set. Fourth, when the selected part of the spectrum is isolated, the projection is a contour integral of the resolvent. Fifth, the Davis–Kahan theorems need only the reducing decomposition; their spectral hypotheses are imposed on the blocks.

I will write A for a self-adjoint operator. In the sine-theta theorem the operator whose exact subspace we want is the perturbed operator, which the paper writes A hat, equal to A plus H; everything here applies to whichever operator plays that role.

A three-by-three example

Take the real symmetric matrix with first row two, one, zero; second row one, two, zero; and third row zero, zero, five. Its eigenvalues are one, three, and five. The eigenvector for one is e one minus e two, normalized; for three it is e one plus e two, normalized; and for five it is e three.

Suppose the eigenvalues one and three are the ones we care about, and five is unwanted. The wanted subspace is the span of the two eigenvectors for one and three, which is the plane spanned by e one and e two. Notice that this subspace is described without naming its eigenvectors: it is simply the first two coordinates. The matrix maps that plane into itself, since the third row and column have no entries mixing with the first two.

Choose frames. Let F zero be the three by two matrix with columns e one and e two, and F one the column e three. Then F zero star A F zero is the two by two matrix with rows two, one and one, two. Call it Lambda zero. It is not diagonal, but it has eigenvalues one and three. And F one star A F one is the number five, Lambda one. The off-diagonal blocks, F one star A F zero and its adjoint, are zero. In the coordinates given by the two frames, A is block diagonal with blocks Lambda zero and Lambda one.

This is the shape of the exact data in the paper. The wanted subspace is a whole subspace, not a chosen list of eigenvectors, and the operator on it, Lambda zero, can be any self-adjoint operator with the wanted spectrum. That freedom matters when eigenvalues repeat or cluster, because then individual eigenvectors are not determined, while the subspace is.

Invariant and reducing subspaces

A closed subspace U is invariant under an operator if the operator maps U into U. It is reducing if, in addition, the operator maps the orthogonal complement of U into the complement. Reducing is what makes the block form diagonal: invariance kills one off-diagonal block, and invariance of the complement kills the other.

For a general matrix the two notions differ. The upper triangular matrix with rows one, one and zero, two maps the horizontal axis into itself, since it sends e one to e one. But it sends e two to e one plus two e two, which leaves the vertical axis. So the horizontal axis is invariant without being reducing.

For a self-adjoint operator they coincide. Suppose A maps U into U, and take a vector v perpendicular to U. For every u in U, the inner product of A v with u equals the inner product of v with A u, by self-adjointness, and that is zero because A u is in U. So A v is perpendicular to every u in U: A maps the complement into the complement. In terms of the projection P onto U, a closed subspace reduces a bounded operator exactly when P commutes with the operator.

Blocks and frames

Let U be a closed subspace reducing A. Choose an isometry F zero from a coordinate Hilbert space onto U, and an isometry F one from another coordinate space onto the complement of U. The two frames satisfy F zero star F one equals zero, because their ranges are perpendicular, and F zero F zero star plus F one F one star equals the identity, because their ranges together fill the space. Every vector x splits as F zero times F zero star x, plus F one times F one star x.

Define Lambda zero to be F zero star A F zero and Lambda one to be F one star A F one. These are self-adjoint operators on the coordinate spaces, and the reducing property says the cross blocks vanish. Equivalently, A F one equals F one Lambda one: applying A after embedding a complementary coordinate vector gives the same result as applying Lambda one first and then embedding. A F zero equals F zero Lambda zero in the same way.

This intertwining identity has the same shape as the residual of a trial subspace. For a trial frame E zero and trial operator A zero, the residual is A E zero minus E zero A zero. An exact decomposition is the case of zero residual on both sides.

The spectrum of A is the union of the spectra of Lambda zero and Lambda one. For a block-diagonal operator, A minus z times the identity is invertible exactly when both diagonal blocks minus z are invertible. In the three by three example, the spectrum one, three, five is the union of one and three with five.

The paper's predicate for exact data asks for less than the full block decomposition. It requires F zero and F one to be isometries with perpendicular ranges filling the space, and it requires the single intertwining identity A F one equals F one Lambda one, together with a domain condition when A is unbounded. The wanted block Lambda zero never appears in the hypotheses of the sine-theta theorem, so the predicate does not mention it; it does appear in the paper's block form and in the doubled-sine theorem. For a self-adjoint operator, invariance of the complement already implies that the wanted subspace is reducing, by the argument we just gave.

Selecting a subspace by its spectrum

Where do reducing subspaces come from? The spectral theorem.

For a self-adjoint matrix, list the distinct eigenvalues and their eigenspace projections. For any set S of real numbers, the spectral projection for S is the sum of the eigenprojections for the eigenvalues lying in S. Its range is the span of all eigenvectors whose eigenvalues lie in S. In the example, the set of numbers less than or equal to four selects the eigenvalues one and three, and its spectral projection is the projection onto the plane of e one and e two.

The spectral theorem extends this to every self-adjoint operator on a Hilbert space, bounded or not. It provides a projection-valued measure: an assignment of an orthogonal projection, written E of S, to every Borel set S of real numbers. The projection for the whole line is the identity. The projection for an intersection of two sets is the product of their projections, so projections for disjoint sets are perpendicular. And the projection for a countable disjoint union is the sum of the individual projections, converging in the strong sense, vector by vector. The operator is recovered as the integral of lambda against this measure, which in finite dimensions is the familiar sum of eigenvalues times eigenprojections.

Each spectral projection commutes with A, so its range is a reducing subspace. On that range, the restricted operator has spectrum inside the closure of S, and on the complementary range, inside the closure of the complement of S. These are the spectral subspaces of the paper.

The point of the general theorem is that spectral subspaces exist even when there are no eigenvectors. Consider the operator on square-integrable functions on the interval from zero to one that multiplies a function by t. It is self-adjoint and bounded, its spectrum is the whole interval, and it has no eigenvectors: an eigenfunction for the value lambda would have to vanish except at the single point t equal to lambda. Its spectral projection for a set S is multiplication by the indicator function of S. So the spectral subspace for the interval from zero to one half consists of the functions vanishing after one half. On that subspace the operator is multiplication by t on the first half of the interval, with spectrum from zero to one half; on the complement it is multiplication by t on the second half, with spectrum from one half to one.

Notice that in this example the two spectra touch at one half. The decomposition is exact, but nothing separates the wanted spectrum from the unwanted one. All of the Davis–Kahan estimates divide by a positive separation, and here they give no information. A spectral subspace exists for every Borel set, but only a separated one comes with an estimate of how far it can move.

Isolated spectrum and the resolvent

When the selected part of the spectrum is separated from the rest, there is an analytic formula for its projection, and it explains why such projections behave well under perturbation.

The resolvent of A at a complex number z, outside the spectrum, is the inverse of z times the identity minus A. For a self-adjoint matrix, the resolvent acts on each eigenvector as one over z minus the eigenvalue. Now draw a closed contour in the complex plane that encircles the wanted eigenvalues and no others, and integrate the resolvent around it, dividing by two pi i. For each eigenvalue, the scalar integral of one over z minus that eigenvalue, divided by two pi i, is one if the contour encircles the eigenvalue and zero if it does not, by Cauchy's integral formula. So the integral of the resolvent acts as one on the wanted eigenvectors and zero on the others: it is the spectral projection.

For example, with the diagonal matrix having entries one and three, take the circle of radius one centered at one. The resolvent is diagonal with entries one over z minus one and one over z minus three. The first integrates to one, and the second to zero, since its only singularity, three, lies outside the circle. The integral is the projection onto the first coordinate.

The same formula, the Riesz projection, works for any isolated bounded part of the spectrum of a self-adjoint operator, including an unbounded one, because the resolvent is a bounded, everywhere-defined operator at each point of the contour. If A is perturbed slightly, the resolvent changes slightly along the contour, provided the contour stays away from the new spectrum, and so the projection changes slightly. This is the classical reason, central to Kato's perturbation theory, that isolated spectral subspaces move continuously. Davis and Kahan answer a quantitative version of the same question with different tools: instead of integrating the resolvent, they solve a Sylvester equation, and the separation of spectra enters as a bound on its solution. The contour formula needs complex numbers; the paper's results hold for real Hilbert spaces as well, through complexification.

The Borel calculus covers more than isolated bounded clusters. A half-infinite interval, such as all numbers less than or equal to some b, has a spectral projection even when the operator is unbounded and its spectrum extends to infinity on both sides. Such projections appear in the paper's ordered separation hypotheses, where one block lies below b and the other lies above b plus delta, and the operators involved may be unbounded.

What the theorems assume

It is worth being exact about how the Davis–Kahan theorems use all this. Their exact data is a reducing decomposition: isometric frames F zero and F one with perpendicular ranges filling the space, and blocks Lambda zero and Lambda one, the operator acting on the wanted subspace and its complement. In their Section 1, Davis and Kahan state explicitly that no assumption is made that the projections are spectral projectors or that the spectra of the two blocks are disjoint.

The spectral content enters only through hypotheses on the blocks. The sine-theta theorem, for instance, asks that the spectrum of the trial operator A zero lie in an interval, and the spectrum of Lambda one lie outside the interval enlarged by delta on each side, or the same with the roles exchanged. If the wanted subspace is the spectral subspace of A hat for a set S and the trial operator approximates the operator on that subspace, these hypotheses say that the trial spectrum is separated from the spectrum of A hat outside S.

In the three by three example, take the trial operator to have spectrum inside the interval from one to three. Lambda one is five, so it lies outside the interval enlarged by any delta up to two. If the trial spectrum is exactly one and three, the sine-theta separation is two.

To summarize. For a self-adjoint operator, invariant closed subspaces are reducing, so a wanted subspace and its complement split the operator into two self-adjoint blocks, Lambda zero and Lambda one, with A F one equal to F one Lambda one, and the spectrum of the operator is the union of the blocks' spectra. The spectral theorem supplies such a subspace for every Borel set, as the range of a spectral projection, even when there are no eigenvectors; for an isolated part of the spectrum, that projection is the contour integral of the resolvent, which is why it moves continuously under perturbation. The Davis–Kahan theorems take the reducing decomposition as given and put their spectral hypotheses on the blocks, mainly on Lambda one.

What a reducing decomposition does not provide is separation. The multiplication operator split at one half is an exact decomposition with no gap between the two blocks, and for it the sine-theta theorem says nothing. The size of the gap, and its geometric shape, is what the theorems need next.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Example

\[
A=\begin{pmatrix}2&1&0\\1&2&0\\0&0&5\end{pmatrix},\quad
\sigma(A)=\{1,3,5\},\quad v_1=\tfrac1{\sqrt2}(1,-1,0),\ v_3=\tfrac1{\sqrt2}(1,1,0),\ v_5=e_3 .
\]
\(F_0=[e_1\ e_2]\), \(F_1=e_3\), \(\Lambda_0=F_0^*AF_0=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), \(\Lambda_1=5\), \(F_1^*AF_0=0\); \(E((-\infty,4])=F_0F_0^*\).

Non-self-adjoint contrast: \(\begin{pmatrix}1&1\\0&2\end{pmatrix}\) leaves \(\operatorname{span}e_1\) invariant but not its complement.

### Statements

- \(A=A^*\), \(AU\subseteq U\Rightarrow AU^\perp\subseteq U^\perp\). For bounded \(A\): \(U\) reduces \(A\iff PA=AP\).
- Frames: \(F_0^*F_1=0\), \(F_0F_0^*+F_1F_1^*=I\); \(\Lambda_j=F_j^*AF_j\); \(AF_j=F_j\Lambda_j\); \(\sigma(A)=\sigma(\Lambda_0)\cup\sigma(\Lambda_1)\).
- PVM: \(E(\mathbb R)=I\), \(E(S\cap T)=E(S)E(T)\), countable additivity in the strong operator topology, \(A=\int\lambda\,dE(\lambda)\); \(E(S)\) commutes with \(A\); \(\sigma(A|_{\operatorname{ran}E(S)})\subseteq\overline S\).
- Multiplication example: \((M_tf)(t)=tf(t)\) on \(L^2[0,1]\), \(E(S)=M_{\chi_S}\), no eigenvalues; split at \(1/2\): \(\sigma(\Lambda_0)=[0,\tfrac12]\), \(\sigma(\Lambda_1)=[\tfrac12,1]\).
- Riesz projection: \(P_\Gamma=\frac1{2\pi i}\oint_\Gamma(zI-A)^{-1}\,dz\). Example: \(A=\operatorname{diag}(1,3)\), \(\Gamma=\{|z-1|=1\}\), \(P_\Gamma=\operatorname{diag}(1,0)\).
- Davis–Kahan (1.3): \(A+H\sim_F\operatorname{diag}(\Lambda_0,\Lambda_1)\), with no assumption that \(Q\) is spectral or that \(\sigma(\Lambda_0)\cap\sigma(\Lambda_1)=\varnothing\).
- Sine-theta separation (interval/exterior form): \(\sigma(A_0)\subseteq[\beta,\alpha]\), \(\sigma(\Lambda_1)\cap(\beta-\delta,\alpha+\delta)=\varnothing\), or roles exchanged. Example: \(\sigma(A_0)=\{1,3\}\), \(\Lambda_1=5\): \(\delta=2\).

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/SineTheta/Presentation.lean`, `namespace TauCeti.DavisKahan1970`, with `A : E →ₗ.[𝕜] E` a linear partial map (possibly unbounded):

```lean
structure IsExactSpectralDecomposition
    (A : E →ₗ.[𝕜] E)
    (Λ₁ : G →ₗ.[𝕜] G)
    (F₀ : H →L[𝕜] E)
    (F₁ : G →L[𝕜] E) : Prop where
  desiredIsometry : IsometricEmbedding F₀
  complementIsometry : IsometricEmbedding F₁
  orthogonal : F₀.adjoint ∘L F₁ = 0
  complete :
    F₀ ∘L F₀.adjoint + F₁ ∘L F₁.adjoint =
      ContinuousLinearMap.id 𝕜 E
  mapsDomain : ∀ y : Λ₁.domain, F₁ (y : G) ∈ A.domain
  intertwines : ∀ y : Λ₁.domain,
    A ⟨F₁ (y : G), mapsDomain y⟩ =
      F₁ (Λ₁ y)
```

`DavisKahan/InfiniteDimensional/SinTheta/General.lean` (bounded symmetric case):

```lean
noncomputable def spectralProjection (A : E →L[𝕜] E) (hA : A.IsSymmetric)
    (s : Set ℝ) (hs : MeasurableSet s) :
    E →L[𝕜] E :=
  (spectralSubspace A hA s hs).starProjection

theorem isInvariant_spectralSubspace (A : E →L[𝕜] E)
    (hA : A.IsSymmetric) (s : Set ℝ) (hs : MeasurableSet s) :
    Submodule.IsReducing (spectralSubspace A hA s hs) A
```

**Mapping notes.**

- `IsExactSpectralDecomposition` contains only the complementary intertwining `A F₁ = F₁ Λ₁` (plus the domain inclusion), as the lecture says; `Λ₀` does not occur.
- The proof of `isInvariant_spectralSubspace` uses `LinearMap.IsSymmetric.isReducing_iff_mem_invtSubmodule`, the formal version of “invariant implies reducing for self-adjoint operators.”
- The Borel spectral projections for unbounded self-adjoint operators are built from a projection-valued measure adapted from Bornemann's Spectra development; the journal paper, §2.5 and §4.3, describes this.
