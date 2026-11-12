# 020500 — Generalizations of the sine theorem

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sine-theta. **Audience:** the sine-theta theorem and its proof; the angle operator Theta and the identity that the absolute value of P minus Q is sine Theta; Ky Fan norms and dominance.

<!-- BEGIN SPOKEN LECTURE -->

Generalizations of the sine theorem

The sine-theta theorem bounds the directed angle from a trial subspace toward an exact subspace, for an isometric trial frame. Section 6 of the Davis–Kahan paper asks how far that can be pushed. Can the same hypotheses bound the full, two-sided angle between the subspaces in terms of the perturbation? No, and the paper gives a two by two example. What extra hypothesis repairs it? A second gap, on the other pair of blocks. And what if the trial frame is not exactly orthonormal? Then a lower frame bound enters as a factor. Along the way the paper proves two lemmas about block operators that are used again and again: a direct-sum comparison and a reflection pinching inequality.

Here is what we will establish. First, the one-sided hypotheses do not imply delta times the size of the full sine of Theta at most the size of H; the paper's two by two example violates this in the Hilbert–Schmidt norm. Second, Lemma 6.2: for any orthogonal projections, keeping the two diagonal blocks of an operator and discarding the off-diagonal ones cannot increase any unitarily invariant norm, because the kept part is the average of the operator and a reflected copy. Third, Lemma 6.1: if each diagonal block of one operator is dominated by the corresponding block of another, in every unitarily invariant norm, then so is the block-diagonal sum. Fourth, Proposition 6.1: if the trial operator is separated from the unwanted exact block and also the complementary trial block is separated from the wanted exact block, both by delta, then delta times the size of the full sine of Theta is at most the size of H, in every unitarily invariant norm. Fifth, Theorem 6.1: if the trial frame satisfies only E zero star E zero at least epsilon squared, then delta times epsilon times the size of the sine of Theta zero is at most the size of the residual, and the trial and exact subspaces may have different dimensions.

The one-sided theorem does not bound the full angle

Take the plane. Let A be the diagonal matrix with entries one and zero, so the reference blocks are A zero equal to one, on the horizontal axis, and A one equal to zero, on the vertical axis. Let H be the symmetric matrix with entries minus one, one, one, zero. Then A hat, equal to A plus H, has zeros on the diagonal and ones off the diagonal. Its eigenvalues are plus one and minus one, with eigenvectors along the two diagonals.

Take the trial subspace to be the horizontal axis with trial operator A zero equal to one. The residual is H applied to the horizontal unit vector, which is the vector minus one, one, with length root two. Choose the exact wanted subspace to be the eigenvector of A hat for plus one, the diagonal line at forty-five degrees. Then Lambda one is minus one. The gap between A zero, which is one, and Lambda one, which is minus one, is two, in the interval and exterior shape. The angle between the trial line and the exact line is forty-five degrees.

The sine-theta theorem holds, with equality: delta times the sine of forty-five degrees is two times one over root two, which is root two, the length of the residual.

Now ask about the full angle operator Theta, which compares the subspaces in both directions and also compares their complements. In the plane its two angles are both forty-five degrees, so its sine has two singular values, each one over root two, and its Hilbert–Schmidt norm is one. Delta times that is two. But the Hilbert–Schmidt norm of H is the square root of one plus one plus one, root three, which is less than two. So delta times the Hilbert–Schmidt norm of the full sine exceeds the Hilbert–Schmidt norm of H. The one-sided hypotheses do not give a two-sided conclusion. Davis and Kahan give this warning explicitly.

The reason is visible in the data. The full angle also compares the complement of the trial subspace, the vertical axis, where A acts as zero, with the exact wanted subspace, where A hat acts as plus one. The separation between those blocks is only one, not two. The one-sided theorem never looked at that pair.

Pinching by a reflection

Before the repair, two lemmas about block operators.

Let Omega and Upsilon be orthogonal projections, on the output and input sides of an operator K. Split K into four blocks: Omega K Upsilon, Omega K times the identity minus Upsilon, and so on. Lemma 6.2 says: the sum of the two diagonal blocks, Omega K Upsilon plus the identity minus Omega, times K, times the identity minus Upsilon, has every unitarily invariant norm at most that of K.

The proof is one averaging step. Let J one be the reflection two Omega minus the identity, and J two the reflection two Upsilon minus the identity. Both are unitary. Conjugating K by them, J one K J two, keeps the diagonal blocks and negates the off-diagonal ones. So the average of K and J one K J two is exactly the sum of the diagonal blocks. By the triangle inequality and unitary invariance, the norm of the average is at most half the norm of K plus half the norm of J one K J two, which is the norm of K.

The lemma also applies to off-diagonal blocks, by choosing the projections appropriately: if Omega projects onto one output block and Upsilon onto the other input block, the two blocks kept are the off-diagonal ones. In words: discarding blocks in a checkerboard pattern cannot increase any unitarily invariant norm.

Comparing direct sums

Lemma 6.1 concerns block-diagonal operators. Suppose K and L are each the sum of two diagonal blocks, with respect to the same pair of decompositions, and that in every unitarily invariant norm the first block of K is no larger than the first block of L, and the second block of K is no larger than the second block of L. Then the whole of K is no larger than the whole of L, in every unitarily invariant norm.

Here is why. By Ky Fan dominance it suffices to compare Ky Fan norms. The singular values of a block-diagonal operator are the singular values of the two blocks merged together. So the sum of the k largest singular values of K is the largest value, over ways of splitting k into j plus k minus j, of the Ky Fan j-norm of the first block plus the Ky Fan k minus j norm of the second. Each of those terms is dominated by the corresponding term for L, so the maximum is too.

The converse can fail, because a direct sum can hide which block is responsible for a large singular value. Davis and Kahan prove the converse when the two blocks of K have the same singular values as each other, and likewise for L.

Proposition 6.1: the symmetric sine theorem

Now the repair. Let A be self-adjoint, with reducing blocks A zero on the trial subspace and A one on its complement. Let A hat equal A plus H, with H bounded, and with reducing blocks Lambda zero on the exact wanted subspace and Lambda one on its complement. Assume two gap conditions of the sine-theorem type, each with separation delta: one between A zero and Lambda one, and one between A one and Lambda zero. Then delta times the size of the full sine of Theta is at most the size of H, in every unitarily invariant norm.

The proof uses both lemmas. Write the frames E zero and E one for the trial subspace and its complement, and F zero and F one for the exact wanted subspace and its complement.

There are two Sylvester equations. Applying F one star on the left and E zero on the right to H, which is A hat minus A, gives F one star H E zero equals Lambda one X zero minus X zero A zero, where X zero is F one star E zero. That is the familiar equation. Applying F zero star and E one in the same way gives F zero star H E one equals Lambda zero X one minus X one A one, where X one is F zero star E one: the coordinates, in the wanted exact space, of the trial complement. Each gap condition bounds one of these: delta times the size of X zero is at most the size of F one star H E zero, and delta times the size of X one is at most the size of F zero star H E one.

Next, write the difference of the two projections, P minus Q, in these frames: inputs in the E coordinates, outputs in the F coordinates. Its diagonal blocks vanish, and its off-diagonal blocks are X zero and minus X one. So P minus Q has the same singular values as the block-diagonal operator made of X zero and X one. And the absolute value of P minus Q is the sine of Theta. So the size of the full sine equals the size of the direct sum of X zero and X one.

Write H in the same frames. Its two off-diagonal blocks are F one star H E zero and F zero star H E one, the right-hand sides of the two Sylvester equations. By Lemma 6.2, the direct sum of those two blocks is no larger than H.

Finally, Lemma 6.1 combines the two Sylvester bounds: since delta times X zero is dominated by the first off-diagonal block of H, and delta times X one by the second, in every norm, delta times the direct sum of X zero and X one is dominated by the direct sum of the two blocks of H. Chaining: delta times the size of the full sine of Theta, which is delta times the size of the direct sum of the X's, is at most the size of the direct sum of the off-diagonal blocks of H, which is at most the size of H.

In the two by two example, the second gap, between A one equal to zero and Lambda zero equal to one, is only one. With delta equal to one, Proposition 6.1 gives one times the Hilbert–Schmidt norm of the full sine, which is one, at most root three. It holds, and the failure with delta equal to two is explained: one of the two required gaps was smaller.

Theorem 6.1: frames that are not orthonormal

In computation, a basis for a trial subspace is rarely exactly orthonormal. Theorem 6.1 drops the assumption that E zero is an isometry and assumes only a lower frame bound: E zero star E zero is at least epsilon squared times the identity, for some positive epsilon. Equivalently, every trial coordinate vector x is mapped to a vector of length at least epsilon times the length of x.

The residual is defined exactly as before, R equal to A hat E zero minus E zero A zero, and the Sylvester equation still holds for X equal to F one star E zero, because its derivation never used that E zero is an isometry. So delta times the size of F one star E zero is at most the size of R.

What changes is the relation between X and the angle. Factor E zero by its polar decomposition, E zero equals W times the modulus of E zero, where W is an isometry onto the trial subspace and the modulus of E zero is at least epsilon. Then F one star E zero is F one star W times the modulus of E zero. F one star W is the X of an orthonormal frame, and its size is the size of the sine of Theta zero. Multiplying it by the modulus of E zero, which has an inverse of norm at most one over epsilon, can shrink its size by at most a factor epsilon. So epsilon times the size of the sine is at most the size of F one star E zero. Combining, delta times epsilon times the size of the sine of Theta zero is at most the size of R.

The factor epsilon is necessary on scaling grounds. Multiply E zero by two. The trial subspace and its angles do not change, the residual doubles, and epsilon doubles. The inequality is consistent only because epsilon appears on the left.

Theorem 6.1 also states the dimension freedom explicitly. The trial subspace and the exact wanted subspace need not have the same dimension. The directed sine of Theta zero is any operator with the same singular values as P times the identity minus Q, where P and Q project onto the trial and exact subspaces. When the dimensions differ, this directed sine is the meaningful measure, as the line lying inside a plane showed.

To summarize. The sine-theta theorem's one-sided gap does not control the full angle in terms of the perturbation: the paper's two by two example has gap two, angle forty-five degrees, and two times the Hilbert–Schmidt norm of the full sine exceeds the Hilbert–Schmidt norm of H, root three. Lemma 6.2 says discarding blocks in a checkerboard pattern does not increase any unitarily invariant norm, because the kept part averages the operator with a reflected copy. Lemma 6.1 compares block-diagonal sums blockwise through Ky Fan norms. Proposition 6.1 assumes a second gap, between A one and Lambda zero, writes the full sine as the direct sum of two Sylvester solutions, and concludes delta times the size of the full sine at most the size of H. Theorem 6.1 replaces the isometry by a lower frame bound epsilon and allows unequal dimensions, at the cost of a factor epsilon.

Each generalization pays with a hypothesis. The symmetric conclusion needs both gaps, and the smaller of the two is what enters; the non-orthonormal frame loses a factor equal to its smallest stretch.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Ambient limitation (source, before Proposition 6.1)

\(A=\operatorname{diag}(1,0)\), \(H=\begin{pmatrix}-1&1\\1&0\end{pmatrix}\), \(\widehat A=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), \(\sigma(\widehat A)=\{\pm1\}\). Trial \(E_0=e_1\), \(A_0=1\), \(R=HE_0=(-1,1)\), \(\|R\|=\sqrt2\). Exact wanted \(\operatorname{span}\{(1,1)\}\), \(\Lambda_1=-1\), \(\delta=2\), \(\theta=\pi/4\). Directed: \(\delta\sin\theta=\sqrt2=\|R\|\). Ambient: \(\|\sin\Theta\|_{\rm HS}=1\), \(\delta\|\sin\Theta\|_{\rm HS}=2>\sqrt3=\|H\|_{\rm HS}\). Second gap \(|A_1-\Lambda_0|=|0-1|=1\).

### Lemmas

- **6.2:** \(J_1=2\Omega-I\), \(J_2=2\Upsilon-I\): \(\tfrac12(K+J_1KJ_2)=\Omega K\Upsilon+\Omega^\perp K\Upsilon^\perp\), so \(N(\Omega K\Upsilon+\Omega^\perp K\Upsilon^\perp)\le N(K)\).
- **6.1:** \(N(K_1)\le N(L_1)\) and \(N(K_2)\le N(L_2)\ \forall N\Rightarrow N(K_1\oplus K_2)\le N(L_1\oplus L_2)\ \forall N\), via \(\|K_1\oplus K_2\|_{(k)}=\max_{j}(\|K_1\|_{(j)}+\|K_2\|_{(k-j)})\). Converse if the blocks of \(K\) are equisingular and those of \(L\) are equisingular.

### Proposition 6.1

\(\mathrm{SineGap}_\delta(A_0,\Lambda_1)\), \(\mathrm{SineGap}_\delta(A_1,\Lambda_0)\), \(H\) bounded (common domain). \(X_0=F_1^*E_0\), \(X_1=F_0^*E_1\):
\[
F_1^*HE_0=\Lambda_1X_0-X_0A_0,\qquad F_0^*HE_1=\Lambda_0X_1-X_1A_1,
\]
\[
F^*(P-Q)E=\begin{pmatrix}0&-X_1\\X_0&0\end{pmatrix},\quad N(\sin\Theta)=N(|P-Q|)=N(X_0\oplus X_1),
\]
\[
\delta N(\sin\Theta)=\delta N(X_0\oplus X_1)\le N(F_1^*HE_0\oplus F_0^*HE_1)\le N(F^*HE)=N(H).
\]

### Theorem 6.1

\(E_0^*E_0\ge\varepsilon^2I\), \(\mathrm{SineGap}_\delta(A_0,\Lambda_1)\); \(E_0=W|E_0|\), \(|E_0|\ge\varepsilon\): \(N(F_1^*W)\le N(F_1^*E_0)\,\||E_0|^{-1}\|\le N(F_1^*E_0)/\varepsilon\), hence
\[
\delta\varepsilon N(\sin\Theta_0)\le\delta N(F_1^*E_0)\le N(R).
\]
\(\sin\Theta_0\) has the singular values of \(P(I-Q)\); no equal-dimension hypothesis.

### Lean correspondence

All in `namespace TauCeti.DavisKahan1970` (see `dev/davis-kahan-1970-formalization-result-inventory.json`):

- Lemma 6.1: `lemma6_1`, `lemma6_1_converse` (and `_sourceExact`, real/complex variants).
- Lemma 6.2: `lemma6_2`, `lemma6_2_whereDefinedUIN_rclike`.
- Proposition 6.1: `proposition6_1_complex`, `proposition6_1_real`, `proposition6_1_projectorDifference_complex`, `proposition6_1_commonDomain_complex`.
- Theorem 6.1: `theorem6_1_complex`, `theorem6_1_real`, `theorem6_1_commonDomain`; `lowerFrameBound_iff_operator_inequality` relates the pointwise lower frame bound to \(E_0^*E_0\ge\varepsilon^2I\).
