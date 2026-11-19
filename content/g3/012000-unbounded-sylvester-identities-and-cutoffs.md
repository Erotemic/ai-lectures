# 012000 — Unbounded Sylvester identities and spectral cutoffs

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sylvester. **Audience:** unbounded self-adjoint operators and domains, exact decompositions, Theorems 5.1 and 5.2, approximation numbers and Lemma 5.1.

<!-- BEGIN SPOKEN LECTURE -->

Unbounded Sylvester identities and spectral cutoffs

The sine-theta proof has three steps: derive a Sylvester equation, bound its solution using the gap, and identify the solution's size with the size of the sine. For bounded operators the first step is one line of algebra. For unbounded operators, every expression in that line must be checked to make sense, and the bounding step is usually proved first for bounded approximations and then passed to the limit. This lecture does both carefully, because this is where most of the extra work in the paper's unbounded results lives.

Here is what we will establish. First, if the operator under study, A hat, is self-adjoint and the exact decomposition and trial residual are given with their domain conditions, then X, equal to F one star E zero, maps the domain of the trial operator A zero into the domain of Lambda one, and the Sylvester equation Lambda one X minus X A zero equals F one star R holds there. The proof uses self-adjointness through a duality test. Second, spectral cutoffs give bounded approximations to an unbounded self-adjoint operator, but the naive truncation, which is zero outside the retained band, can destroy a spectral gap. Filling the discarded part with a constant on the correct side of the gap preserves it. Third, cutoffs converge to the identity vector by vector but not in norm, so passing an estimate to the limit needs a statement about approximation numbers, Lemma 5.1, and Ky Fan dominance completes the passage to every norm.

The domain question

Recall the data. A hat is self-adjoint, possibly unbounded. E zero is an isometric trial frame, and A zero a self-adjoint trial operator, with E zero mapping the domain of A zero into the domain of A hat, and R a bounded operator equal to A hat E zero minus E zero A zero on the domain of A zero. F zero and F one are isometric frames for the exact wanted subspace and its complement, and Lambda one is self-adjoint, with F one mapping the domain of Lambda one into the domain of A hat and A hat F one equal to F one Lambda one there.

For bounded operators, the Sylvester equation came from applying F one star to the residual and using F one star A hat equals Lambda one F one star. For unbounded operators that adjoint identity is not available as written: F one star A hat is only defined on the domain of A hat, and Lambda one F one star only where F one star lands in the domain of Lambda one. The question is: if x is in the domain of A zero, is X x, which is F one star E zero x, in the domain of Lambda one? The hypotheses do not say so directly.

A duality test

Self-adjointness answers it. For a self-adjoint operator, a vector y belongs to the domain exactly when the map that sends z, in the domain, to the inner product of Lambda one z with y is bounded in z; that is the definition of the domain of the adjoint, and self-adjointness says it equals the domain of the operator.

So test y equal to F one star E zero x against every z in the domain of Lambda one. The inner product of Lambda one z with F one star E zero x equals the inner product of F one Lambda one z with E zero x, by the definition of the adjoint of the bounded map F one. By the intertwining hypothesis, F one Lambda one z equals A hat F one z, and F one z lies in the domain of A hat. And E zero x also lies in the domain of A hat, by the trial hypothesis. Since A hat is self-adjoint, the inner product of A hat F one z with E zero x equals the inner product of F one z with A hat E zero x. That last expression is bounded in z, by the length of z times the length of A hat E zero x, because F one is an isometry.

Therefore y is in the domain of the adjoint of Lambda one, which is the domain of Lambda one. Reading off the identity, Lambda one y equals F one star A hat E zero x. Now use the residual equation: A hat E zero x equals E zero A zero x plus R x. Applying F one star, Lambda one X x equals X A zero x plus F one star R x. That is the Sylvester equation, valid for every x in the domain of A zero, with the bounded right-hand side F one star R.

The argument used three things: the intertwining identity on the unwanted side, the domain inclusion for the trial frame, and self-adjointness of both A hat and Lambda one. This is why the paper's exact-decomposition hypothesis needs only the single intertwining identity for Lambda one. The domain compatibility of X is derived, not assumed.

Bounded approximations

With the equation in hand, the next step is the estimate. For a window with an unbounded unwanted block, Theorem 5.1 applies directly, since only a bounded inverse is needed. For a cut with both operators unbounded, Theorem 5.2 applies; one proof writes the solution as an integral of exponentials, which are bounded even for unbounded operators. Another route for the two-unbounded ordered case, and the pattern used in the paper's appendix on unbounded sine and tangent theorems, is to approximate the unbounded operators by bounded ones, prove the estimate for the approximations, and pass to the limit.

Spectral cutoffs are the natural approximations. For a self-adjoint operator C, let P of tau be its spectral projection for the interval from minus tau to tau. The operator C times P of tau is bounded, it agrees with C on the range of P of tau, and as tau grows, C P of tau applied to any x in the domain converges to C x.

But the plain cutoff can break the gap. Take the sequence-space example: C multiplies the n-th entry by n plus two, and B multiplies the n-th entry by minus n. Every spectral value of C is at least three, and every spectral value of B is at most minus one, so they are ordered with gap four. Now keep the first N coordinates of each and replace the rest by zero. Both truncated operators acquire the eigenvalue zero on the discarded tail. Zero is below three and above minus one, so the truncated C is no longer at least three and the truncated B is no longer at most minus one. The truncated operators have overlapping spectra, and the gap is gone.

The fix is to fill the discarded part with a constant on the correct side. Define the filled truncation of C to be C on the retained band and the constant three on the discarded tail, and the filled truncation of B to be B on its retained band and the constant minus one on its discarded tail. Each filled operator is bounded for each fixed N. The filled C is still at least three, since its values are either original eigenvalues, all at least three, or the fill value three. The filled B is still at most minus one. So the gap of four survives every truncation, and on the retained coordinates the filled operators agree with the originals.

In general, the filled truncation is the cutoff operator plus a real scalar times the projection onto the discarded part. It proves that a lower form bound on the original operator becomes a global lower bound on the filled truncation when the fill value is that same bound, and the upper-bound analogue.

Truncating the equation

Now truncate the Sylvester equation itself. Suppose C X minus X B equals Y on the domain of B, with C at least gamma plus delta and B at most gamma. Let P of tau be the cutoff for C and Q of tau the cutoff for B. Multiply the equation on the left by P of tau and on the right by Q of tau. Spectral projections commute with their operators on the domain, so P of tau C becomes C restricted to the band, and B Q of tau becomes B restricted to its band. The compressed solution, P of tau X Q of tau, satisfies a Sylvester equation with the filled truncations as coefficients and P of tau Y Q of tau on the right. Since the compressed solution maps into the retained band of C and is fed only from the retained band of B, the fill values never act on it; they serve only to keep the coefficients' spectra on the correct sides.

Now everything is bounded and ordered with gap delta. The bounded form of Theorem 5.2 gives, for every Ky Fan norm, delta times the Ky Fan k-norm of the compressed solution at most the Ky Fan k-norm of P of tau Y Q of tau, which is at most the Ky Fan k-norm of Y, by the contraction law.

Passing to the limit

As tau grows, P of tau and Q of tau converge to the identity strongly: for each fixed vector, the projected vector converges to the original. They do not converge in norm. On square-summable sequences, the projection onto the first N coordinates differs from the identity by an operator of norm one for every N, as the next coordinate vector shows. So the compressed solutions converge to X vector by vector, but not necessarily in norm, and we cannot simply say their norms converge.

This is where Lemma 5.1 enters. If projections converge strongly to the identity, then the approximation numbers of an operator compressed by them converge to the approximation numbers of the operator. Applied on each side, each Ky Fan k-norm of the compressed solution converges to the Ky Fan k-norm of X. The inequality delta times the Ky Fan k-norm of the compressed solution, at most the Ky Fan k-norm of Y, therefore passes to the limit: delta times the Ky Fan k-norm of X is at most the Ky Fan k-norm of Y, for every k. Ky Fan dominance then gives delta times N of X at most N of Y, for every unitarily invariant norm N in which both are finite.

There is a second kind of convergence hidden here. For a vector x in the domain of an unbounded operator, the cutoffs converge not only in the ordinary norm but in the graph norm: the projected vector approaches x, and the operator applied to the projected vector approaches the operator applied to x. In the diagonal example, x has a square-summable tail, and so does the sequence obtained by multiplying the entries by their indices; both tails go to zero. Graph-norm convergence is what lets the truncated equations recover the original equation on the domain.

What the residual must do

All of this assumes the right-hand side is bounded. Davis and Kahan state the requirement explicitly for half-infinite spectral intervals: they assume that A hat E zero and E zero A zero share a dense domain on which the residual is bounded, extend the residual continuously, and only then apply Theorem 5.2. If the residual were unbounded, the right-hand side of every estimate would be infinite, and the truncation argument would give nothing.

In the paper's appendix on unbounded sine and tangent theorems, the same pattern is used with an extra ingredient for the tangent: spectral cutoffs of the trial operator together with finite-rank projections chosen to nearly capture the largest angles. A lemma about such near-maximizing projections, Lemma 6.3, controls the error they leave behind.

To summarize. For a self-adjoint A hat with an exact decomposition and a trial residual, the Sylvester equation Lambda one X minus X A zero equals F one star R holds on the domain of A zero; the domain inclusion for X follows from a duality test using self-adjointness of A hat and Lambda one. Unbounded coefficients are approximated by spectral cutoffs, and filling the discarded part with a constant on the correct side preserves an ordered gap that a zero fill would destroy. The truncated equation satisfies the bounded estimate, and because cutoffs converge only strongly, Lemma 5.1 on approximation numbers carries each Ky Fan inequality to the limit, after which Ky Fan dominance gives every norm.

The price of unboundedness is paid in hypotheses: domain inclusions, a bounded residual, and self-adjointness used as a statement about domains. Without any one of them the equation, or the estimate, has no meaning.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Domain compatibility

Hypotheses: \(\widehat A=\widehat A^*\), \(\Lambda_1=\Lambda_1^*\); \(E_0(\operatorname{dom}A_0)\subseteq\operatorname{dom}\widehat A\), \(R=\widehat AE_0-E_0A_0\) on \(\operatorname{dom}A_0\); \(F_1(\operatorname{dom}\Lambda_1)\subseteq\operatorname{dom}\widehat A\), \(\widehat AF_1=F_1\Lambda_1\) there. For \(x\in\operatorname{dom}A_0\), \(y=F_1^*E_0x\), and \(z\in\operatorname{dom}\Lambda_1\):
\[
\langle\Lambda_1z,y\rangle=\langle F_1\Lambda_1z,E_0x\rangle=\langle\widehat AF_1z,E_0x\rangle=\langle F_1z,\widehat AE_0x\rangle,
\]
so \(|\langle\Lambda_1z,y\rangle|\le\|z\|\,\|\widehat AE_0x\|\), \(y\in\operatorname{dom}\Lambda_1^*=\operatorname{dom}\Lambda_1\), \(\Lambda_1y=F_1^*\widehat AE_0x\), and
\[
\Lambda_1Xx-XA_0x=F_1^*Rx\qquad(x\in\operatorname{dom}A_0).
\]

### Filled truncations

\(C_\tau^{\rm fill}=CP(\tau)+a\,(I-P(\tau))\), \(P(\tau)=E_C([-\tau,\tau])\). If \(C\ge aI\) (forms), then \(C_\tau^{\rm fill}\ge aI\). Example: \(Ce_n=(n+2)e_n\), \(Be_n=-ne_n\), gap \(4\); zero fill gives eigenvalue \(0\) to both; filling with \(3\) and \(-1\) keeps the gap \(4\).

Compressed equation: \(C_\tau^{\rm fill}(P_\tau XQ_\tau)-(P_\tau XQ_\tau)B_\tau^{\rm fill}=P_\tau YQ_\tau\). Bounded Theorem 5.2: \(\delta\|P_\tau XQ_\tau\|_{(k)}\le\|Y\|_{(k)}\). Strong convergence \(P_\tau,Q_\tau\to I\) and Lemma 5.1 give \(\|P_\tau XQ_\tau\|_{(k)}\to\|X\|_{(k)}\); Fan dominance gives all norms.

\(\|I-P_N\|=1\) for coordinate projections \(P_N\); graph-norm convergence on \(\operatorname{dom}N\).

### Lean correspondence

`DavisKahan/Sylvester/FilledTruncation.lean`, `namespace TauCeti.DavisKahan.Sylvester`:

```lean
noncomputable def filledTruncation
    {H : Type v}
    [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]
    (A : H →ₗ.[𝕜] H)
    (hA : IsSelfAdjoint A)
    (Pcut : SpectralCutoffInterface A hA)
    (Tcut : BoundedTruncationInterface A hA Pcut)
    (a τ : ℝ) : H →L[𝕜] H :=
  Tcut.truncation τ +
    ((a : ℝ) : 𝕜) •
      (ContinuousLinearMap.id 𝕜 H - Pcut.cutoff τ)

theorem filledTruncation_lowerBound
    ... {a τ : ℝ} (hτ : 0 ≤ τ)
    (ha : TauCeti.LinearPMap.SemiboundedBelow A a) :
    ∀ x, a * ‖x‖ ^ 2 ≤
      RCLike.re ⟪filledTruncation A hA Pcut Tcut a τ x, x⟫_𝕜
```

with companions `filledTruncation_upperBound`, `filledTruncation_eq_on_cutoff`, `filledTruncation_tendsto_on_domain`. `DavisKahan/Sylvester/Unbounded/OrderedFromCutoffs.lean` assembles the projection, filled-truncation, domain-equation and strong Ky Fan limit steps for the ordered two-unbounded Sylvester theorem. Lemma 5.1: `TauCeti.DavisKahan1970.lemma5_1`.

**Mapping notes.**

- The journal paper (§3, “Why the Sylvester estimate gives the angle bound”) says that deriving the domain compatibility of \(X\) is part of the argument; the duality test above is that derivation.
- The cutoff interfaces (`SpectralCutoffInterface`, `BoundedTruncationInterface`) are instantiated from the Borel spectral calculus adapted from Spectra.
