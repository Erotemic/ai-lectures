# 006000 — Unitarily invariant norms and Ky Fan dominance

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** norms. **Audience:** singular values and the singular value decomposition, the min-max principle, principal angles.

<!-- BEGIN SPOKEN LECTURE -->

Unitarily invariant norms and Ky Fan dominance

The sine-theta theorem says that delta times the size of the sine of the angle operator is at most the size of the residual. Which size? The paper's answer is: every unitarily invariant norm at once. The operator norm, which records the largest sine; the Frobenius norm, which records the root sum of squares; the trace norm, which adds the sines; and infinitely many others. This lecture explains what these norms are, why one inequality can hold for all of them simultaneously, and why, in the transport part of the paper, different norms can disagree about which of two maps is better.

Here is what we will establish. A norm on operators is unitarily invariant if multiplying by unitaries on either side does not change it; such a norm depends only on the singular values, and von Neumann showed that these norms correspond exactly to symmetric gauge functions, norms on sequences that ignore order and signs. Normalized means a rank-one operator built from two unit vectors has norm one. Every such norm satisfies the contraction law: multiplying by operators of norm at most one cannot increase it. The Ky Fan k-norm is the sum of the k largest singular values. Ky Fan's dominance theorem says that one operator is no larger than another in every unitarily invariant norm exactly when it is no larger in every Ky Fan norm, that is, when its singular values are weakly majorized. Finally, Q-norms are those whose square is a unitarily invariant norm of Z star Z; the Frobenius norm is one, the trace norm is not, and that difference is the center of the paper's correction to Proposition 4.4.

Many ways to measure one list

Recall the four-dimensional example with principal angles of thirty and sixty degrees. The sine of the angle operator has singular values one half and root three over two. How large is it? The operator norm says root three over two, about zero point eight seven. The Frobenius norm says the square root of one quarter plus three quarters, which is one. The trace norm says one half plus root three over two, about one point three seven. Each is a reasonable answer to a different question: the worst direction, an energy over all directions, or a total over all directions.

All three share a property. If we change orthonormal bases in the input space or in the output space, none of them changes, because singular values do not change. That is the property that matters for subspace errors, since an error measure should not depend on how we chose bases.

Unitarily invariant norms

A norm N on operators between Hilbert spaces is unitarily invariant if N of U times Z times V equals N of Z for all unitaries U and V of the appropriate spaces. By the singular value decomposition, Z equals a unitary times a diagonal matrix of singular values times another unitary, so a unitarily invariant norm of Z depends only on the list of singular values.

Which functions of the singular value list arise this way? John von Neumann answered this in 1937 for matrices. Define a symmetric gauge function to be a norm on real sequences that does not change when the entries are permuted or when their signs are changed. Every unitarily invariant matrix norm is a symmetric gauge function applied to the singular values, and conversely every symmetric gauge function applied to singular values gives a unitarily invariant norm. The converse is the hard direction, because one must prove the triangle inequality for operators from a triangle inequality for sequences, even though the singular values of a sum are not the sums of singular values.

The examples are the familiar sequence norms. The maximum gives the operator norm. The square root of the sum of squares gives the Frobenius, or Hilbert–Schmidt, norm. The sum gives the trace norm, also called the nuclear norm. The p-th root of the sum of p-th powers gives the Schatten p-norm, for p at least one. And the sum of the k largest entries gives the Ky Fan k-norm.

Normalization and the contraction law

Davis and Kahan add two conventions. First, normalization: a rank-one operator that sends x to u times the inner product of v with x has norm equal to the length of u times the length of v. In sequence terms, the gauge of the list one, zero, zero, and so on, is one. Under normalization every unitarily invariant norm lies between the operator norm and the trace norm: it is at least the largest singular value and at most the sum of all of them.

Second, the contraction law: for bounded operators K and L, the norm of K Z L is at most the operator norm of K, times the norm of Z, times the operator norm of L. This follows from a fact about singular values. By the min-max principle, the j-th singular value of Z is the smallest possible maximum of the length of Z x over unit vectors x perpendicular to a subspace of dimension j minus one. Multiplying by K on the left can multiply each such length by at most the norm of K, so each singular value of K Z is at most the norm of K times the corresponding singular value of Z. Since a symmetric gauge function is monotone in each entry, the norm grows by at most that factor. The argument for L on the right is similar, applied to the adjoint.

The contraction law is used constantly in the paper. In the sine-theta proof, the complementary part of the residual is F one star R, where F one star is a contraction; so its norm is at most the norm of R. That one line is the last inequality in the chain from angle to residual.

Ky Fan norms and dominance

Ky Fan norms deserve special attention. The Ky Fan k-norm of Z is the sum of its k largest singular values. Ky Fan showed in 1951 that this is also the largest value of the real part of the sum, over k pairs, of the inner product of y i with Z x i, where x one through x k are orthonormal and y one through y k are orthonormal. That formula makes the triangle inequality obvious, since a supremum of linear expressions is subadditive, and it is a working tool: to bound a Ky Fan norm from below, exhibit orthonormal vectors; to bound it from above, bound every such sum.

A warning about notation, for reading the 1970 paper. Davis and Kahan write the Ky Fan norms with a subscript, so their subscript one is the Ky Fan one-norm, the largest singular value, which is the operator norm. They write the Hilbert–Schmidt norm with the subscript s q. Most modern texts, including the recent journal paper on this theory, follow the other convention, in which a subscript one denotes the trace norm. The same symbol therefore means the operator norm in one text and the trace norm in the other.

Ky Fan's dominance theorem is the reason a single theorem can hold for every unitarily invariant norm. It says: for operators K and L, the norm of K is at most the norm of L in every unitarily invariant norm if and only if, for every k, the Ky Fan k-norm of K is at most the Ky Fan k-norm of L. The condition on Ky Fan norms is called weak majorization of the singular values: each partial sum of the largest singular values of K is at most the corresponding partial sum for L.

Weak majorization is not entrywise comparison. Take K with singular values two and two, and L with singular values three and one. The second singular value of K is larger than the second singular value of L, so entrywise comparison fails. But the partial sums are two versus three, and four versus four, so K is weakly majorized by L. Dominance says every unitarily invariant norm of K is at most the same norm of L. Check: the operator norms are two and three, the Frobenius norms are root eight and root ten, and the trace norms are four and four.

Why is the theorem true? The direction from all norms to Ky Fan norms is immediate, since Ky Fan norms are among the unitarily invariant norms. For the other direction, suppose the partial sums of K's singular values are dominated by those of L. First increase the smallest singular values of K, if necessary, until the total equals the total for L; a symmetric gauge function is monotone in each entry, so this can only increase the norm of K. Now the two lists have the same total, and the partial sums of the first are still dominated. A theorem of Hardy, Littlewood, and Pólya then says the first list is an average of rearrangements of the second. In our example, two, two is the average of three, one and one, three. A symmetric gauge function gives every rearrangement of L's list the same value, and by convexity the value of an average is at most the average of the values. So the norm of K is at most the norm of L.

Davis and Kahan use dominance in exactly this way. They prove inequalities for every Ky Fan norm, often through the orthonormal-vectors formula, and then conclude the inequality for every unitarily invariant norm at once.

When norms disagree

Dominance also explains when norms disagree. If neither list weakly majorizes the other, some unitarily invariant norm prefers one and some other norm prefers the other.

The paper's counterexample to Proposition 4.4 is built on such a pair. Two orthogonal maps of four-dimensional real space carry the same plane onto the same tilted plane, with both principal angles equal to theta. The displacement of the direct rotation, the identity minus the rotation, has four singular values, each equal to two sine of theta over two. The displacement of a competing map has singular values two sine theta, two sine theta, zero, zero. At forty-five degrees, the first list is four copies of about zero point seven seven, and the second is two copies of about one point four one and two zeros.

Compare. The largest entry favors the direct rotation: zero point seven seven against one point four one. The total favors the competitor: about three point zero six against two point eight three. So the operator norm says the direct rotation moves less, and the trace norm says the competitor moves less. The Frobenius norm agrees with the operator norm here: the squared lists sum to about two point three four for the direct rotation and four for the competitor. Neither list weakly majorizes the other, so no single answer holds for all unitarily invariant norms. Proposition 4.4 claimed that the direct rotation wins in every unitarily invariant norm, and this pair shows that it does not.

Q-norms

Some unitarily invariant norms are better behaved with respect to squaring. Call N a Q-norm if there is a unitarily invariant norm M such that N of Z, squared, equals M of Z star Z, for every Z. The Frobenius norm is a Q-norm: its square is the sum of squared singular values, which is the trace norm of Z star Z. The operator norm is a Q-norm, with M the operator norm. The Schatten p-norm is a Q-norm when p is at least two, with M the Schatten p over two norm, which is a norm because p over two is at least one. The trace norm is not a Q-norm: its square would require the Schatten one-half functional of Z star Z, which is not a norm.

The point of Q-norms is that an inequality for Z star Z in every unitarily invariant norm, which is a statement about squared singular values, transfers to an inequality for Z in every Q-norm, by taking square roots. Davis and Kahan prove that the direct rotation minimizes the squared displacement, the identity minus W, star, times the identity minus W, in every unitarily invariant norm. That gives minimality of the unsquared displacement in every Q-norm, including the Frobenius norm and the operator norm, but not in the trace norm, which is where the counterexample lives.

The norms in the paper's theorems

In infinite dimensions, the paper's norms are norms on operator ideals, defined through the same singular-value data and finite only on part of the space of bounded operators. The paper's hypotheses on such a norm are: it is symmetric, meaning unitarily invariant; it is normalized; it satisfies the contraction law; and it has Ky Fan dominance whenever both values are finite. Each of the familiar examples has these properties, and the next lecture explains the infinite-dimensional setting in which membership in the ideal must be assumed.

To summarize. A unitarily invariant norm depends only on singular values, and von Neumann's theorem identifies these norms with symmetric gauge functions. Normalized norms lie between the operator norm and the trace norm and satisfy the contraction law, which is what lets the sine-theta proof discard the contraction F one star. Ky Fan norms add the k largest singular values; an operator is smaller in every unitarily invariant norm exactly when it is smaller in every Ky Fan norm, by majorization and averaging over rearrangements. Lists that do not weakly majorize each other are ranked differently by different norms, as the direct rotation and its competitor are in the Proposition 4.4 counterexample. Q-norms are those whose square is a norm of Z star Z, and they inherit squared-displacement inequalities.

A theorem "for every unitarily invariant norm" is therefore a theorem about weak majorization of singular values. Where a comparison of singular-value lists fails, as it does for the full displacement of transports, no choice of argument can recover a statement for every norm.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Definitions and facts

- **Unitarily invariant:** \(N(UZV)=N(Z)\); \(N(Z)=\Phi(s_1(Z),s_2(Z),\dots)\) for a symmetric gauge function \(\Phi\) (von Neumann 1937).
- **Normalized:** \(N(uv^*)=\|u\|\|v\|\); then \(\|Z\|_{\rm op}\le N(Z)\le\|Z\|_1\).
- **Contraction law:** \(s_j(KZL)\le\|K\|\,s_j(Z)\,\|L\|\) (min-max), hence \(N(KZL)\le\|K\|N(Z)\|L\|\).
- **Davis–Kahan (1.10)–(1.13):** \(\kappa_k=\inf_{\dim\mathcal S=k-1}\sup_{\|x\|=1,x\perp\mathcal S}\|Kx\|\); \(\|K\|_{(\nu)}=\kappa_1+\dots+\kappa_\nu=\sup_\Omega\|K\Omega\|_{(\nu)}=\sup\operatorname{Re}\sum_{k=1}^\nu y_k^*Kx_k\) over orthonormal \(\nu\)-tuples.
- **Fan dominance:** \(N(K)\le N(L)\ \forall N\iff\|K\|_{(k)}\le\|L\|_{(k)}\ \forall k\) (\(s(K)\prec_w s(L)\)). Proof: raise \(s(K)\) to \(z\ge s(K)\) with \(z\prec s(L)\); \(z\) is a convex combination of permutations of \(s(L)\) (Hardy–Littlewood–Pólya / Birkhoff); \(\Phi\) is symmetric, convex, monotone.
- **Example:** \((2,2)\prec_w(3,1)\): \(2\le3\), \(4\le4\); norms \(2\le3\), \(\sqrt8\le\sqrt{10}\), \(4\le4\).
- **Notation:** Davis–Kahan write \(\|K\|_\nu\) for the Ky Fan \(\nu\)-norm, so their \(\|\cdot\|_1\) is the operator norm and \(\|\cdot\|_{\rm sq}\) the Hilbert–Schmidt norm; the journal paper writes \(\|\cdot\|_1\) for the trace norm and \(\|\cdot\|_{(j)}\) for Ky Fan norms.
- **Q-norm:** \(N(Z)^2=M(Z^*Z)\). Frobenius (\(M=\|\cdot\|_1\)), operator (\(M=\|\cdot\|_{\rm op}\)), Schatten \(p\ge2\) (\(M=\|\cdot\|_{p/2}\)); trace norm is not.

### Prop 4.4 lists at \(\theta=45^\circ\)

| | singular values of \(I-W\) | max | sum | sum of squares |
|---|---|---|---|---|
| direct rotation | \(4\times2\sin22.5^\circ\approx0.765\) | 0.765 | 3.061 | 2.343 |
| competitor | \(2\sin45^\circ\approx1.414\) (×2), 0, 0 | 1.414 | 2.828 | 4 |

### Lean correspondence

Tau Ceti, `TauCeti/Analysis/InnerProductSpace/KyFan.lean`:

```lean
noncomputable def kyFanSum (A : E →ₗ[𝕜] F) (k : ℕ) : ℝ :=
  ∑ i ∈ Finset.range k, A.singularValues i
```

`TauCeti/Analysis/OperatorIdeal/SymmetricGauge/Basic.lean`:

```lean
structure SymmetricGauge where
  toFun : (ℕ →₀ ℝ≥0) → ℝ≥0
  map_add_le' : ∀ a b, toFun (a + b) ≤ toFun a + toFun b
  map_smul' : ∀ (c : ℝ≥0) a, toFun (c • a) = c * toFun a
  map_equivMapDomain' : ∀ (σ : Equiv.Perm ℕ) a, toFun (a.equivMapDomain σ) = toFun a
  monotone' : Monotone toFun
  map_single_zero_one' : toFun (Finsupp.single 0 1) = 1
```

`TauCeti/Analysis/OperatorIdeal/Family/KyFan/Dominance.lean`, `namespace TauCeti.OperatorIdealFamily`:

```lean
class IsKyFanDominant (Φ : OperatorIdealFamily.{u, v, w} 𝕜) : Prop where
  gauge_le_of_forall_kyFanGauge_le : ∀ {E G : Type v} {F H : Type w}
    [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]
    [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]
    [NormedAddCommGroup G] [InnerProductSpace 𝕜 G] [CompleteSpace G]
    [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]
    {A : E →L[𝕜] F} {B : G →L[𝕜] H},
    (∀ k, A.kyFanGauge k ≤ B.kyFanGauge k) → Φ.gauge A ≤ Φ.gauge B
```

**Mapping notes.**

- `SymmetricGauge` records exactly the lecture's properties (subadditive, homogeneous, permutation invariant, monotone, normalized); sign invariance is built in because the gauge acts on nonnegative sequences.
- Ky Fan dominance is a separate class. The module docstring states that the ideal-family laws do not force it, and gives instances for the operator-norm, Ky Fan, trace-class, Schatten, Hilbert–Schmidt families and every symmetric-gauge family. The paper's sine-theta theorem carries `[N.toOperatorIdealFamily.IsKyFanDominant]` (or the normalized-symmetric family structure that provides it) as a hypothesis.
