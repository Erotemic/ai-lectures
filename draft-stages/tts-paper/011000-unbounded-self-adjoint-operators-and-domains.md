# 011000 — Unbounded self-adjoint operators and their domains

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** spectral. **Audience:** Hilbert spaces, spectral subspaces and projection-valued measures, basic real analysis.

<!-- BEGIN SPOKEN LECTURE -->

Unbounded self-adjoint operators and their domains

The Davis–Kahan paper does not restrict itself to bounded operators. Its own numerical example is a vibrating beam, whose operator is a fourth derivative, and the theorems are stated so that they apply to such operators. This lecture explains what changes when the operator is unbounded, and what stays the same.

Here is what we will establish. First, the Hellinger–Toeplitz theorem: a symmetric operator defined on every vector of a Hilbert space is automatically bounded. So an unbounded self-adjoint operator cannot act on every vector; it comes with a domain, a dense subspace on which it is defined. Second, the spectral theorem still holds: the operator has a projection-valued measure, its spectral projections are bounded and defined everywhere, and its domain consists of the vectors whose spectral measure has finite second moment. Third, lower and upper bounds on an unbounded operator are stated as quadratic-form inequalities on its domain, and for a self-adjoint operator they are the same as spectral bounds on a half-infinite interval. Fourth, every operator identity in the paper, such as the residual equation and the intertwining equation for the exact subspace, has to say on which vectors it holds, and the useful theorems require the residual to be bounded even when the operator is not.

A vibrating beam

Take the real Hilbert space of square-integrable functions on the interval from zero to one. The free beam operator takes a function u to its fourth derivative, with the boundary conditions that the second and third derivatives vanish at both ends. Physically, u is the transverse displacement of a beam whose ends are free, and the eigenvalues are the squares of its natural frequencies, suitably scaled.

The operator is self-adjoint and has eigenvalues zero, zero, and then an increasing sequence of positive values, the first of which is a little above five hundred. The two zero eigenvalues belong to the rigid motions of the beam: a uniform translation, given by a constant function, and a rigid rotation, given by a linear function. The positive eigenvalues grow like the fourth power of their index, without bound.

This operator cannot act on every square-integrable function. A function with a jump has no fourth derivative at all. And even among smooth functions, the ratio of the length of the fourth derivative to the length of the function is unbounded: the function sine of n pi t has fourth derivative of size n pi to the fourth times the function, which grows without limit as n grows. The operator is unbounded, and its natural domain is the set of functions with four square-integrable derivatives satisfying the boundary conditions.

Davis and Kahan perturb this operator by H, multiplication by epsilon times t, with epsilon between zero and one hundred. Multiplication by t is bounded, with norm one, so the perturbation is bounded even though the beam operator is not. Their trial subspace is the span of the two rigid motions, with the trial operator zero. We will come back to this example when we discuss residuals.

Why unbounded operators need domains

The Hellinger–Toeplitz theorem, from 1910, says that a symmetric operator defined on all of a Hilbert space is bounded. Symmetric means that the inner product of A x with y equals the inner product of x with A y, for all x and y where A is defined.

Here is why. Suppose x n converges to x, and A x n converges to some vector y. For every vector z, the inner product of y with z is the limit of the inner products of A x n with z, which by symmetry equals the limit of the inner products of x n with A z, which is the inner product of x with A z, which by symmetry again is the inner product of A x with z. Since this holds for every z, y equals A x. In words: the graph of A, the set of pairs x, A x, is closed. The closed graph theorem then says that an everywhere-defined linear operator with closed graph on a complete space is bounded.

So an unbounded symmetric operator cannot be defined everywhere. It must come with a domain, a subspace of vectors on which it acts, and for the theory to work the domain must be dense. This is not a technicality to be removed later. It is a structural fact about the operators the paper allows.

A sequence-space example

The simplest unbounded self-adjoint operator lives on square-summable sequences. Let N multiply the n-th entry by n, for n equal to one, two, three, and so on. Its domain is the set of sequences a for which the sum of n squared times the squared absolute value of a n is finite.

The domain is dense, because every sequence with finitely many nonzero entries belongs to it, and those are dense. But it is not everything. The sequence with entries one, one half, one third, and so on, is square-summable, yet N would turn it into the sequence of all ones, which is not. So that sequence is not in the domain. And N is unbounded, since it sends the n-th coordinate vector to n times itself.

Symmetry of N on its domain is immediate, since it is a real diagonal operator. Self-adjointness is a stronger requirement: the adjoint of N, defined on all vectors y for which the map taking x to the inner product of N x with y is bounded, must have exactly the same domain as N. For this diagonal operator with its maximal domain, that holds. If instead we had defined N only on finitely supported sequences, it would still be symmetric, but its adjoint would have the larger maximal domain, and the operator would not be self-adjoint. The spectral theorem requires self-adjointness, and the paper's operators are self-adjoint.

The spectral theorem for unbounded operators

The spectral theorem holds for unbounded self-adjoint operators in the same form as for bounded ones. There is a projection-valued measure E, assigning an orthogonal projection to each Borel set of real numbers, and the operator is the integral of lambda against E.

Three features deserve attention. First, every spectral projection is bounded and defined everywhere, even though the operator is not. For N, the projection for a set S keeps the coordinates whose index lies in S and zeros out the rest.

Second, the domain is described by the spectral measure: a vector x lies in the domain exactly when the integral of lambda squared against the measure that E assigns to x is finite. For N, the measure assigned to a sequence a puts weight equal to the squared absolute value of a n at the point n, so the domain condition is the sum of n squared times the squared absolute value of a n being finite, as before.

Third, spectral cutoffs give bounded approximations. The projection for a bounded interval, say from minus m to m, maps every vector into the domain, and the operator composed with that projection is bounded. For N, cutting off at m gives the diagonal operator with entries one through m followed by zeros. For any x in the domain, these truncated operators applied to x converge to N x as m grows. This is how statements about unbounded operators are often proved: establish them for the bounded cutoffs, then pass to the limit. The paper's appendix on unbounded sine and tangent estimates uses exactly this pattern.

The spectrum of an unbounded self-adjoint operator is a closed subset of the real line, possibly unbounded in one direction or both. N has spectrum one, two, three, and so on. The beam operator has spectrum zero together with its increasing sequence of positive eigenvalues.

Bounds stated through quadratic forms

For a bounded self-adjoint operator, the statement that A is at least a times the identity means that the inner product of A x with x is at least a times the squared length of x, for every x. For an unbounded operator, the same statement is made for every x in the domain. The paper writes the ordered separation hypotheses in this form. For example, A zero at least b plus delta, and Lambda one at most b, means that the quadratic form of A zero is at least b plus delta times the squared length on the domain of A zero, and the quadratic form of Lambda one is at most b times the squared length on the domain of Lambda one.

For a self-adjoint operator, a form bound below by a is equivalent to the spectrum lying in the half-line from a to infinity. One direction is the spectral theorem: if the spectrum lies in that half-line, the quadratic form is an integral of lambda against a positive measure supported where lambda is at least a. The other direction uses the fact that, if a point c below a belonged to the spectrum, spectral projections for small intervals around c would supply vectors with quadratic form close to c times their squared length.

The paper's ordered hypotheses allow both operators to be unbounded at once, which the interval form cannot do. Here is the example it gives. On square-summable sequences indexed from one, let A zero multiply the n-th entry by n plus delta, and let Lambda one multiply the n-th entry by minus n. Then A zero is bounded below by one plus delta, which is at least delta, and Lambda one is bounded above by minus one, which is at most zero. So the ordered hypothesis holds with b equal to zero. But neither spectrum lies in a finite interval: one runs off to plus infinity and the other to minus infinity. A theorem that only allowed an interval and its exterior would not apply to this pair, while the ordered version does.

Where identities hold

Every operator identity that involves an unbounded operator must specify the vectors on which it holds. This affects two equations that appear in every perturbation theorem of the paper.

The first is the intertwining equation for the exact subspace. With F one the isometric frame for the complement of the wanted subspace, and Lambda one the operator on that complement, the equation A hat F one equals F one Lambda one means: for every y in the domain of Lambda one, the vector F one y lies in the domain of A hat, and A hat applied to F one y equals F one applied to Lambda one y. The domain inclusion is part of the hypothesis.

The second is the residual equation. With E zero the isometric trial frame and A zero the trial operator, the residual R is A hat E zero minus E zero A zero. For this to make sense, E zero must carry the domain of A zero into the domain of A hat. The paper assumes that A hat E zero and E zero A zero share a dense domain. Since E zero is defined everywhere, that common domain is the domain of A zero, and the condition says E zero maps it into the domain of A hat. The difference is then defined on the domain of A zero, and the theorems assume that it is bounded there, so that it extends to a bounded operator on the whole trial coordinate space. That extension is the residual R in the estimates.

Why insist that the residual be bounded? Because the theorems bound a norm of an angle by a norm of the residual, and if the residual is unbounded the right-hand side is infinite and the inequality says nothing. Davis and Kahan make this point explicitly for half-infinite spectral intervals: without a bounded residual, no useful conclusion follows.

Consider what can go wrong without the domain condition. Take N on sequences, and a trial vector whose entries are one, one half, one third, and so on, normalized. This vector is not in the domain of N, so N cannot be applied to it, and there is no residual at all. A trial subspace for an unbounded operator must consist of vectors on which the operator can act, at least on a dense subspace of trial coordinates.

When the operator under study is a perturbation A hat equal to A plus H, with H bounded and defined everywhere, the domain of A hat equals the domain of A. Davis and Kahan state their unbounded results for this situation: the domain of H contains the domain of A, and the pertinent perturbation or residual extends boundedly. If the trial frame is an exact reducing frame for the unperturbed operator A, with A zero its block, then A E zero equals E zero A zero on the domain of A zero, and the residual reduces to H E zero, which is bounded because H is.

Back to the beam

In the beam example, the trial frame E zero takes two coordinates to the corresponding combination of two rigid motions. These are two orthonormal linear functions, each equal to one plus or minus the square root of three times two t minus one, all divided by root two. These functions are smooth and satisfy the free-end boundary conditions, since their second and third derivatives are zero. They lie in the domain of the beam operator, which annihilates them. With the trial operator A zero equal to zero, the residual is the perturbed operator applied to E zero, which is H E zero: multiplication by epsilon t applied to each rigid motion. That is a bounded operator from the two-dimensional coordinate space into the function space, with an explicit two by two Gram matrix, epsilon squared over thirty times the matrix with entries eleven minus root seventy-five, minus one, minus one, eleven plus root seventy-five. Its eigenvalues are epsilon squared over thirty times eleven plus or minus root seventy-six.

On the other side, H is positive, so the perturbed operator is at least the unperturbed one, and the third eigenvalue of the perturbed beam is above five hundred. The wanted subspace of the perturbed operator is the span of its two lowest eigenfunctions; the complement has spectrum above five hundred. So the unbounded part of the spectrum sits far from the trial operator's spectrum, which is just zero, and the residual is small and bounded. This is the configuration in which the sine-theta theorem gives a strong estimate, and the paper carries it out in Section 9.

To summarize. A symmetric operator defined everywhere is bounded, so unbounded self-adjoint operators come with dense proper domains. The spectral theorem still provides a projection-valued measure whose projections are bounded; the domain is where the spectral second moment is finite; and spectral cutoffs give bounded approximations converging on the domain. Order bounds on unbounded operators are quadratic-form inequalities on the domain, equivalent for self-adjoint operators to spectral containment in a half-line, and the ordered separation hypothesis lets both blocks be unbounded. Every residual and intertwining equation includes a domain inclusion, and the useful estimates require the residual to extend to a bounded operator.

The limitation is real. If the trial vectors leave the domain, or if the residual is unbounded, the estimates are vacuous. The theorems control angles through the size of a residual, and the residual has to be a bounded operator for that size to mean anything.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Statements

- **Hellinger–Toeplitz.** \(A:\mathcal E\to\mathcal E\) linear, everywhere defined, \(\langle Ax,y\rangle=\langle x,Ay\rangle\) \(\Rightarrow\) graph closed \(\Rightarrow\) \(A\) bounded (closed graph theorem).
- **Diagonal example.** \((Na)_n=na_n\) on \(\ell^2(\mathbb N_{\ge1})\), \(\operatorname{dom}N=\{a:\sum n^2|a_n|^2<\infty\}\); \(a_n=1/n\notin\operatorname{dom}N\). Restricted to finitely supported sequences, \(N\) is symmetric but not self-adjoint (essentially self-adjoint).
- **Spectral theorem.** \(A=\int\lambda\,dE(\lambda)\), \(\operatorname{dom}A=\{x:\int\lambda^2\,d\langle E(\lambda)x,x\rangle<\infty\}\); \(E(S)\) bounded; for bounded \(S\), \(E(S)\mathcal E\subseteq\operatorname{dom}A\) and \(AE(S)\) is bounded; \(AE([-m,m])x\to Ax\) for \(x\in\operatorname{dom}A\).
- **Form bounds.** \(A\ge aI\iff\langle Ax,x\rangle\ge a\|x\|^2\ \forall x\in\operatorname{dom}A\iff\sigma(A)\subseteq[a,\infty)\) (self-adjoint \(A\)).
- **Paper's both-unbounded example.** \(A_0e_n=(n+\delta)e_n\), \(\Lambda_1e_n=-ne_n\): \(A_0\ge\delta I\), \(\Lambda_1\le0\), ordered separation with \(b=0\).
- **Residual.** \(E_0(\operatorname{dom}A_0)\subseteq\operatorname{dom}\widehat A\), \(R=\widehat AE_0-E_0A_0\) on \(\operatorname{dom}A_0\), extended boundedly. If \(\widehat A=A+H\) with \(H\) bounded and \(AE_0=E_0A_0\) on \(\operatorname{dom}A_0\), then \(R=HE_0\).
- **Intertwining.** \(F_1(\operatorname{dom}\Lambda_1)\subseteq\operatorname{dom}\widehat A\), \(\widehat AF_1=F_1\Lambda_1\) there.

### Free beam (Davis–Kahan Section 9)

\(L^2(0,1)\) (real), \(Au=u^{(4)}\) with \(u''(0)=u'''(0)=u''(1)=u'''(1)=0\); \(H=\) multiplication by \(\varepsilon t\), \(0<\varepsilon<100\). Eigenvalues \(\alpha_1=\alpha_2=0<\alpha_3<\dots\), \(\cos(\alpha_k^{1/4})\cosh(\alpha_k^{1/4})=1\) for \(k>2\), \(\alpha_3>500\).
\[
w_k(t)=\frac{1+(-1)^k\sqrt3(2t-1)}{\sqrt2},\quad E_0=(w_1\ w_2),\quad A_0=0,\quad R=HE_0,
\]
\[
R^*R=\frac{\varepsilon^2}{30}\begin{pmatrix}11-\sqrt{75}&-1\\-1&11+\sqrt{75}\end{pmatrix},\qquad
\sigma(R^*R)=\frac{\varepsilon^2}{30}\bigl(11\pm\sqrt{76}\bigr).
\]
Since \(H\ge0\), \(\lambda_3(A+H)\ge\alpha_3>500\).

### Lean correspondence

Possibly unbounded operators are linear partial maps `E →ₗ.[𝕜] E` (Mathlib `LinearPMap`), whose `domain` is a submodule.

`ForTauCeti/Analysis/InnerProductSpace/LinearPMap/Sylvester.lean`, `namespace TauCeti.LinearPMap`:

```lean
def SemiboundedBelow (A : E →ₗ.[𝕜] E) (c : ℝ) : Prop :=
  ∀ x : A.domain,
    c * ‖(x : E)‖ ^ 2 ≤ RCLike.re ⟪A x, (x : E)⟫_𝕜

def SemiboundedAbove (A : E →ₗ.[𝕜] E) (c : ℝ) : Prop :=
  ∀ x : A.domain,
    RCLike.re ⟪A x, (x : E)⟫_𝕜 ≤ c * ‖(x : E)‖ ^ 2
```

`DavisKahan/Sylvester/Gap.lean`, `namespace TauCeti.DavisKahan.Sylvester`:

```lean
inductive FormBoundedSylvesterGap
    (A : E →ₗ.[𝕜] E) (B : F →ₗ.[𝕜] F) (δ : ℝ) : Prop where
  | intervalExterior
      {β α : ℝ}
      (hβα : β ≤ α)
      (hgap : RealSpectrumIntervalExteriorGap A B β α δ)
  | leftAboveRightBelow
      (c : ℝ)
      (hA : TauCeti.LinearPMap.SemiboundedBelow A (c + δ))
      (hB : TauCeti.LinearPMap.SemiboundedAbove B c)
  | leftBelowRightAbove
      (c : ℝ)
      (hA : TauCeti.LinearPMap.SemiboundedAbove A c)
      (hB : TauCeti.LinearPMap.SemiboundedBelow B (c + δ))
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Presentation.lean`:

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

- `R : F →L[𝕜] E` is a bounded operator on all trial coordinates, and `residualEquation` asserts agreement on `A₀.domain`: this is “the residual extends boundedly.”
- The module docstring of `Gap.lean` records that the form-bound spelling (`SemiboundedBelow`) and the spectral spelling (`spectrum ⊆ Ici c`) describe the same configurations for self-adjoint blocks, but only the direction spectral \(\Rightarrow\) form is formalized there. A theorem whose hypothesis is the form-bounded predicate is therefore the stronger statement, which is how the paper's sine-theta theorem is stated.
