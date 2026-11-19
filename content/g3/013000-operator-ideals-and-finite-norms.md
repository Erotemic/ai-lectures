# 013000 — Operator ideals and finite norms

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** norms. **Audience:** unitarily invariant norms, Ky Fan norms, compact operators, sequence spaces.

<!-- BEGIN SPOKEN LECTURE -->

Operator ideals and finite norms

In finite dimensions every matrix has a finite trace norm, a finite Frobenius norm, and a finite operator norm, and every unitarily invariant norm is defined everywhere. In infinite dimensions this fails. The identity operator on an infinite-dimensional Hilbert space has operator norm one, but its trace norm, the sum of infinitely many ones, is infinite. A theorem stating that delta times the trace norm of the sine is at most the trace norm of the residual must therefore say what happens when one side is infinite. This lecture sets up the infinite-dimensional norms of the paper and the membership conditions that go with them.

Here is what we will establish. For bounded operators, singular values are replaced by approximation numbers: the j-th approximation number is the distance from the operator to the operators of rank less than j. A unitarily invariant norm becomes a gauge, which may take the value infinity, and the operators with finite gauge form an operator ideal: they are closed under addition and under multiplication by bounded operators on either side. The Schatten ideals, including the trace class and the Hilbert–Schmidt class, are the main examples. The paper's theorems hold for normalized symmetric ideal norms with Ky Fan dominance, and they require that the operators displayed in the conclusion actually belong to the ideal. Finally, Davis and Kahan's Lemma 5.1 says that cutting an operator down by projections that converge to the identity vector by vector makes each approximation number converge; this is how estimates pass from bounded cutoffs to unbounded operators.

Approximation numbers

For a compact operator, singular values work exactly as for matrices: the eigenvalues of Z star Z form a sequence decreasing to zero, and their square roots are the singular values. For a general bounded operator, Z star Z may have continuous spectrum, and there may be no eigenvalues to list. The replacement is the approximation number. The first approximation number of Z is its distance to the zero operator, the operator norm. The second is the smallest distance from Z to an operator of rank at most one. In general, the j-th approximation number is the smallest operator-norm distance from Z to an operator of rank less than j.

For a compact operator these are the singular values, by the Eckart–Young principle that the best approximation of rank less than j is obtained by truncating the singular value decomposition. For the identity on an infinite-dimensional space, every approximation number is one, since removing finitely many directions still leaves an operator of norm one. For a diagonal operator on sequences with entries one, one half, one third, and so on, the approximation numbers are exactly those entries, in order.

Davis and Kahan define the singular values of a bounded operator through the same min-max formula used for matrices, and note that for noncompact operators the language of spectral multiplicity may be more appropriate. What matters for the theorems is that Ky Fan sums of the first k approximation numbers make sense for every bounded operator, and are finite for each k.

Gauges and ideals

Now take a symmetric gauge function, such as the maximum, the sum, or the root sum of squares, and apply it to the sequence of approximation numbers. The result is an extended nonnegative number, possibly infinity. For the maximum, it is always the operator norm, which is finite. For the sum, it is the trace norm, which is finite only for trace-class operators. For the root sum of squares, it is the Hilbert–Schmidt norm, finite only for Hilbert–Schmidt operators.

The set of operators with finite gauge is an operator ideal. It is a linear space, by the triangle inequality for the gauge. And it is closed under multiplication on either side by bounded operators, because of the contraction law: the gauge of K Z L is at most the operator norm of K, times the gauge of Z, times the operator norm of L. So if Z has finite gauge, so does K Z L. This two-sided closure is what the word ideal means, by analogy with ideals in rings.

The Schatten p-class consists of the compact operators whose singular values have a finite sum of p-th powers. For p equal to one it is the trace class, and for p equal to two it is the Hilbert–Schmidt class. These classes are nested: a trace-class operator is Hilbert–Schmidt, and a Hilbert–Schmidt operator is compact.

Consider the diagonal operator D with entries one, one half, one third, and so on. Its trace norm would be the harmonic series, which diverges, so D is not trace class. Its Hilbert–Schmidt norm squared is the sum of one over n squared, which converges to pi squared over six, so D is Hilbert–Schmidt, with Hilbert–Schmidt norm pi over root six, about one point two eight. Its Schatten p-norm is finite exactly when p is greater than one.

Why membership must be assumed

Davis and Kahan announce a convention at the start of their paper: some of their results are vacuous when certain norms occurring in them fail to exist, and they will not mention this at each statement. The recent journal paper on this theory makes the convention explicit. The sine-theta theorem is stated for a normalized symmetric ideal norm N, and its conclusion, delta times N of sine Theta zero at most N of R, is asserted under the hypotheses that sine Theta zero and R both belong to the ideal of N.

Why not simply allow the value infinity and read the inequality in the extended sense? If R is not in the ideal, its norm is infinite and the inequality holds trivially. The case that needs care is the other one: could the residual have finite norm while the sine does not? The comparison principle used in the proof, Ky Fan dominance, is assumed in the paper's ideal norms only where both values exist. It compares norms of two operators whose Ky Fan sums are ordered, but it does not by itself conclude that the smaller operator belongs to the ideal. The precise statement therefore carries membership of both operators as hypotheses. Each familiar ideal, such as the trace class, the Hilbert–Schmidt class, and the Schatten classes, does transfer membership along Ky Fan domination, but that is an additional property of those particular ideals, not part of the general hypothesis.

In practice, membership of the residual is usually easy. If the trial subspace is finite-dimensional, the residual has finite rank and lies in every ideal. In the beam example the residual has rank two. If the residual comes from a perturbation, R equals H E zero, and if H belongs to an ideal, then so does H E zero, by the ideal property.

The norms in the paper's theorems

Put together, the paper's norms are normalized symmetric operator-ideal norms with Ky Fan dominance. Each word has a role.

Operator-ideal norm means a gauge defined on bounded operators between any pair of Hilbert spaces, subadditive, homogeneous, at least the operator norm, and satisfying the two-sided contraction law. The family must work across different spaces, because the residual maps trial coordinates into the ambient space while the sine of Theta zero maps trial coordinates to themselves.

Symmetric means unchanged by taking adjoints, and, together with the other laws, unchanged by multiplication by unitaries and isometries. That is what makes the norm of the rectangular block S equal to the norm of its modulus, the sine of Theta zero.

Normalized means a rank-one operator of norm one has gauge one.

Ky Fan dominance means: if every Ky Fan sum of one operator is at most the corresponding sum for another, and both gauges are finite, then the first gauge is at most the second. The proofs in the paper establish Ky Fan inequalities and use dominance to reach every norm.

The operator norm, the trace norm, the Hilbert–Schmidt norm, the Schatten norms, and the Ky Fan norms all qualify.

Cutoffs and convergence of approximation numbers

The last ingredient is the technical lemma that lets estimates proved for bounded truncations pass to unbounded operators.

Let Omega t be orthogonal projections that converge strongly to the identity as t grows, meaning that Omega t applied to any fixed vector converges to that vector. The spectral projections of an unbounded self-adjoint operator for the intervals from minus t to t are an example. Let K be a bounded operator. Davis and Kahan's Lemma 5.1 says: for each index j, the j-th approximation number of K times Omega t converges to the j-th approximation number of K.

One inequality is immediate: since Omega t is a contraction, each approximation number of K Omega t is at most that of K. The other direction says that truncation eventually captures everything that makes K large. For the first approximation number, the norm, this is clear: pick a unit vector x on which K x is nearly as long as the norm of K; then Omega t x approaches x, so K Omega t x approaches K x. For later approximation numbers, the same idea applies to finitely many well-chosen directions at once.

Why is this needed? In the unbounded sine and tangent theorems, the operator equations hold only on domains, and the estimates are first proved for cutoff versions of the unbounded operators, where everything is bounded. The cutoff inequalities are inequalities between Ky Fan sums of truncated operators. Lemma 5.1 lets each Ky Fan sum pass to the limit, and Ky Fan dominance then gives the inequality for every norm.

Convergence in one ideal and not another

One more example clarifies why statements must be made norm by norm. Take again the diagonal operator D with entries one over n, and truncate it after m entries. The truncations converge to D in operator norm, since the remainder has norm one over m plus one. They converge in Hilbert–Schmidt norm, since the remainder has squared Hilbert–Schmidt norm equal to the tail of the sum of one over n squared. But they do not converge in trace norm. D is not even trace class, and the trace norms of the truncations, the partial harmonic sums, grow without bound. The same sequence of finite-rank operators is a good approximation in two ideals and useless in a third.

Where these ideas come from

Robert Schatten developed normed operator ideals in his 1950 monograph A Theory of Cross-Spaces, and the systematic theory of symmetrically normed ideals was later developed by Gohberg and Krein. Davis and Kahan state their theorems in this framework, so a single theorem covers the operator norm, the Hilbert–Schmidt norm, and every other symmetric norm at once.

To summarize. In infinite dimensions, approximation numbers replace singular values, and a symmetric gauge of the approximation numbers may be infinite. The operators where it is finite form a two-sided ideal, thanks to the contraction law; the trace class and the Hilbert–Schmidt class are the main examples, and the diagonal operator with entries one over n is Hilbert–Schmidt without being trace class. The paper's theorems use normalized symmetric ideal norms with Ky Fan dominance where both values are defined, and the precise statement assumes membership of both the sine and the residual. Lemma 5.1, convergence of approximation numbers under strongly convergent cutoffs, carries estimates from bounded truncations to unbounded operators.

The cost of this generality is bookkeeping, not mathematics. Every displayed norm must be finite for the inequality to say something, and an approximation that converges in one ideal can diverge in another.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Definitions

- Approximation numbers: \(a_j(Z)=\inf\{\|Z-F\|:\operatorname{rank}F<j\}\); \(a_j=s_j\) for compact \(Z\) (Eckart–Young); \(a_j(I)=1\) in infinite dimensions.
- Davis–Kahan (1.10): \(\kappa_k=\inf_{\dim\mathcal S=k-1}\sup_{\|x\|=1,\,x\perp\mathcal S}\|Kx\|\).
- Gauge: \(N(Z)=\Phi(a_1(Z),a_2(Z),\dots)\in[0,\infty]\); ideal \(\mathfrak I_N=\{Z:N(Z)<\infty\}\); \(N(KZL)\le\|K\|N(Z)\|L\|\).
- Schatten: \(\|Z\|_{S_p}=(\sum_js_j(Z)^p)^{1/p}\); \(S_1\subset S_2\subset\text{compact}\).
- \(D=\operatorname{diag}(1/n)\): \(D\notin S_1\); \(\|D\|_{S_2}=\pi/\sqrt6\approx1.283\); \(D\in S_p\iff p>1\). Truncations \(D_m\): \(\|D-D_m\|=1/(m+1)\), \(\|D-D_m\|_{S_2}^2=\sum_{n>m}n^{-2}\to0\), \(\|D_m\|_{S_1}=H_m\to\infty\).
- **Lemma 5.1:** \(\Omega_t\to I\) strongly, \(K\) bounded \(\Rightarrow a_j(K\Omega_t)\to a_j(K)\) for each \(j\).

### Lean correspondence

Tau Ceti, `TauCeti/Analysis/OperatorIdeal/Family.lean`:

```lean
structure OperatorIdealFamily (𝕜 : Type u) [RCLike 𝕜] where
  gauge : ∀ {E : Type v} {F : Type w} [...], (E →L[𝕜] F) → ℝ≥0∞
  gauge_add_le : ... gauge (A + B) ≤ gauge A + gauge B
  gauge_smul : ... gauge (c • A) = ‖c‖ₑ * gauge A
  enorm_le_gauge : ... ‖A‖ₑ ≤ gauge A
  gauge_comp_le : ... gauge (L ∘L A ∘L R) ≤ ‖L‖ₑ * gauge A * ‖R‖ₑ

structure SymmetricOperatorIdealFamily (𝕜 : Type u) [RCLike 𝕜]
    extends OperatorIdealFamily.{u, v, v} 𝕜 where
  gauge_adjoint : ... gauge (ContinuousLinearMap.adjoint A) = gauge A
```

Davis–Kahan library, `DavisKahan/OperatorIdeal/NormalizedUnitaryInvariantNorm.lean`:

```lean
structure NormalizedSymmetricOperatorIdealFamily (𝕜 : Type u) [RCLike 𝕜] where
  toSymmetricOperatorIdealFamily : TauCeti.SymmetricOperatorIdealFamily.{u, v} 𝕜
  gauge_rankOne_eq_one : ∀ {E F : Type v} [...]
      {V : E →L[𝕜] F}, ‖V‖ = 1 → V.rank ≤ (1 : Cardinal) →
      (toSymmetricOperatorIdealFamily.gauge V).toReal = 1
  gauge_le_of_forall_kyFanApproximationGauge_le_defined : ...
```

(`[...]` abbreviates the Hilbert-space instance arguments shown in full in the sources.)

**Mapping notes.**

- `gauge` takes values in `ℝ≥0∞`; `N.Mem T` is finiteness of the gauge and `N.gaugeReal T` its real value. The headline sine-theta theorem assumes `N.Mem (sourceDirectedSinThetaOperator E0 F0)` and `N.Mem R`.
- The docstring of `NormalizedSymmetricOperatorIdealFamily` states that Ky Fan dominance is stored “only at its where-defined scope” and “does not transfer ideal membership,” which is why both memberships are hypotheses.
- Lemma 5.1: `TauCeti.DavisKahan1970.lemma5_1`, `lemma5_1_complex`, `lemma5_1_real` (`dev/davis-kahan-1970-formalization-result-inventory.json`, `DK-5.1-lem`).
