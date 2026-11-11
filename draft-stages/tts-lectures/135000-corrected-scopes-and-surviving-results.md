# 135000 — Corrected scopes and surviving results

**Draft status:** audio-first mathematical lecture. **Prerequisites:** `130000–134000`. **Next:** `136000`.

<!-- BEGIN SPOKEN LECTURE -->

# Corrected scopes and surviving results

Imagine four directions in space. A transporter moves each of them by a distance just under point eight. Another transporter moves two directions by about one point four and fixes two completely. Which motion is cheaper? If the cost is the largest displacement, the first one wins. If the cost is the sum of squared displacements, the first also wins. If the cost is the sum of the displacement lengths, the second wins.

These are the actual singular-value patterns in a four-dimensional subspace transport example with two principal angles of forty-five degrees. They give us a practical way to distinguish the theorems that hold from a printed claim about unsquared ambient transport that does not.

## The geometric data do not determine the cost function

Let U and V be subspaces of equal finite dimension in a real or complex inner-product space, and let W range over unitary or orthogonal maps carrying U onto V. When the appropriate direct rotation D exists, it is an especially symmetric choice. Its action is fixed by the principal-angle geometry.

To tell whether W is economical, we must decide which movement is being charged. We might charge only vectors that **start in the source U**. We might instead measure how far an orthonormal source frame tilts away from the target. Or we might charge movement in **every ambient direction**, including those perpendicular to U.

For whole-space movement, there is one more choice. We can square displacement lengths first, forming the positive Gram operator of identity minus W, or we can measure unsquared displacement directly. Those choices lead to different comparisons.

This gives a hierarchy of questions. First: which input directions count? Second: how are their movements combined? The word optimal must answer both questions before we can state a theorem.

## Restricted movement has the strongest pointwise control

For a source unit vector x, the canonical principal match has a displacement chord of length twice the sine of half its angle. The restricted theorem formalizes this across all directions in U. It says the ordered singular values of identity minus D restricted to U are no larger than those for identity minus W restricted to U.

This is a pointwise statement about an ordered list, so it immediately controls every invariant norm of the restricted map. It has no claim about the independent motion of W on U perpendicular.

For a simple example, take two perpendicular lines in separate principal planes, both at forty-five degrees to their targets. Restricted to the two-dimensional source, D has two equal singular values of approximately point seven six five. A transporter can agree with D on the source while rotating or reflecting the source complement very differently. Its restricted cost remains the same, but its full displacement can change.

The other source-only result concerns angular error of an orthonormal frame. For each source basis vector x, its sine-angle error relative to its transported image dominates the length of the component of x perpendicular to V. Summing the squares of those projection escapes over the source basis gives the sum of the squared principal sines. This is an energy lower bound, not a pointwise eigenvalue assertion for full displacement.

## Squared whole-space movement uses a second argument

To include the whole ambient space, count directions in U and also directions perpendicular to U. Because W carries U onto V, it carries the perpendicular pieces onto one another as well. So the restricted singular-value comparison applies **twice**.

Squaring these two comparisons gives control of the two diagonal blocks of the positive Gram operator of full displacement. But the competitor may still have cross terms connecting the blocks. Merely combining the two diagonal eigenvalue lists would overlook those terms.

Pinching supplies the missing step. Reflect across the split into U and its perpendicular complement, conjugate the competitor's Gram operator by that reflection, and average the result with the original. The cross terms cancel. Averaging cannot increase any Ky Fan sum, meaning the sum of the largest chosen number of eigenvalues.

The direct rotation's Gram operator already respects the split, so it is unchanged by this average. Comparing the two source halves, merging their eigenvalue lists, and then applying pinching gives the whole-space result. We get control of the *prefix sums of squared singular values*. That conclusion is weaker than controlling each unsquared singular value separately, and it is exactly strong enough for the next class of norms.

This is what the whole-space squared-displacement theorem proves. Its proof supplies weak-majorization control of squared singular values, not pointwise control of unsquared singular values.

## Which full-displacement norms inherit the result?

The operator norm does: the largest squared singular value is the square of the largest singular value. The Hilbert–Schmidt norm does too: its square is the trace of the positive Gram operator. More generally, the Schatten p norms for p at least two satisfy the same pattern. Their squares are invariant norms of the Gram operator with exponent p over two.

The norms whose squares can be written as invariant norms of the positive Gram operator are called Q-norms. For these norms, the squared-displacement theorem does give exact optimality of the direct rotation, under the hypotheses that provide the direct rotation and the restricted bounds. There is no separate universal sixty-degree restriction in this result.

Here is the practical meaning. If we care about the single worst displacement, or about the sum of squared displacements, direct rotation wins. If we care instead about the sum of unsquared lengths, we have changed the question.

Go back to the two four-element displacement lists. The direct rotation gives about point seven six five in every position. The coupled transporter gives about one point four one four in two positions and zero in the other two.

The maximum entry favors the direct rotation. So does the sum of squares. But trace norm adds the entries directly: about three point zero six one for the direct rotation, versus two point eight two eight for the coupled map.

These are three answers to three different questions about the same motions. Before applying an optimality theorem, we must ask whether it measures the largest movement, total squared movement, or total movement length.

Thus the printed general statement about **every** invariant norm of unsquared ambient displacement cannot be correct. An acute two-subspace pair in real four-space refutes it, and an equal-angle family gives the same failure at every strictly positive angle.

## A universal lower bound and a controlled approximation

Even when D does not minimize a chosen unsquared norm, the difference of source and target projections gives a universal lower bound. If P and Q are those projections and W transports U onto V, then for every invariant norm N, the norm of P minus Q is no greater than the norm of identity minus W.

The proof uses the source and target reflections, twice their projections minus identity. Their conjugacy under W expresses twice the projection difference as a commutator involving W minus identity. The triangle inequality gives the bound with constant one, because the factor of two from the reflection difference cancels the factor of two from the commutator estimate.

For D itself, each positive principal angle theta contributes two displacement singular values, each equal to twice the sine of half theta. For P minus Q, it contributes two singular values equal to the sine of theta. The ratio is one divided by the cosine of half theta.

If the largest principal angle is at most sixty degrees, each ratio is at most two divided by the square root of three. Symmetric-gauge monotonicity therefore gives an approximation guarantee: the norm of identity minus D is at most that factor times the norm of identity minus W for every competitor W. It does **not** say D minimizes the norm.

The four-dimensional equal-angle example shows this factor is attained in trace norm at theta equal to sixty degrees. The direct trace cost is four, while the coupled map costs two times the square root of three and attains the projection-difference lower bound. Their ratio is exactly two divided by the square root of three. This makes the approximation constant sharp for the stated short-angle comparison.

## Real and complex transport have different choices

There is one last distinction: we can carry subspaces over the real numbers or over the complex numbers. In complex space, multiplying every vector in a complex line by the same unit-magnitude phase does not change the line. It does change how far individual vectors travel. So complex transport has an extra way to adjust full displacement.

On one complex principal plane of angle theta, take the ordinary direct rotation, interpreted as a unitary map. Its two eigenphases are plus theta and minus theta. Now multiply the whole two-dimensional block by the complex phase corresponding to minus theta. The two eigenphases become zero and minus twice theta. The map still carries the source complex line to the target complex line, because multiplying all its outputs by a scalar phase does not change that line.

One eigenphase is now zero, so one singular value of displacement vanishes. The other is twice the sine of theta. The trace cost on this plane is therefore twice the sine of theta, equal to the trace norm of the difference between the two rank-one projections. We have concentrated the motion into one complex direction instead of distributing it across two.

Do this independently on each complex principal plane, with identity on common directions. In finite dimension, the resulting unitary transporter attains the projection-difference trace lower bound and is therefore globally trace-optimal. The canonical direct rotation generally does not have that trace cost.

In real space, multiplying a two-dimensional block by an arbitrary complex phase is unavailable. In the minimal plane, the competing choices are a rotation and a reflection; weak majorization yields the sixty-degree threshold for the direct rotation to beat reflection in every invariant norm. In four real dimensions, separate principal planes can be coupled. That is the first ambient dimension where the corresponding universal claim fails.

## Conclusion

Restricted displacement has pointwise singular-value control. Squared full displacement has Ky Fan prefix control. Q-norms carry that squared result back to selected unsquared norms. For an arbitrary unsquared invariant norm, the projection difference is a lower bound and the direct rotation has a quantitative approximation guarantee, but exact optimization depends on the scalar field and on the admissible ambient couplings. These statements answer distinct mathematical questions and can all be true simultaneously.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Numerical scope comparison and sharp short-angle ratio

For the real equal-angle pair \(\theta_1=\theta_2=\pi/4\), let
\(a=\sqrt{2-\sqrt2}\) and \(b=\sqrt2\). A canonical direct rotation
and a coupled admissible transport have displacement singular-value lists
\(a^{[4]}\) and \((b,b,0,0)\). Their costs are
\[
\begin{array}{c|cc}
& D & W\\\hline
\|I-\cdot\|_\infty & a & b\\
\|I-\cdot\|_2 & 2a & 2\\
\|I-\cdot\|_1 & 4a & 2b\\
\|\,(I-\cdot)^*(I-\cdot)\,\|_1 & 4a^2 & 4
\end{array}
\]
Thus the Q-norm comparisons and the reversed nuclear-norm ordering are
consistent on the same input pair.

For a principal angle \(\theta\), the two nonzero singular values of
\(I-D\) on its real principal plane are \(2\sin(\theta/2)\),
whereas those of \(P_U-P_V\) are \(\sin\theta\). Hence, for maximum angle
\(\theta_{\max}<\pi\) in the direct-rotation regime,
\[
\|I-D\|_N\le\sec(\theta_{\max}/2)\|P_U-P_V\|_N
\le\sec(\theta_{\max}/2)\|I-W\|_N.
\]
At \(\theta_{\max}=\pi/3\) the factor is \(2/\sqrt3\). The real
four-dimensional equal-angle family gives
\(\|I-D\|_1=4\), \(\|I-W\|_1=2\sqrt3\), with \(W\) attaining the
projection-difference lower bound: the factor is sharp.

For a **complex** principal plane, \(D_\theta\) has eigenvalues
\(e^{\pm i\theta}\). Multiplication by the complex scalar
\(e^{-i\theta}\) preserves the target complex line and gives a transporter
with eigenvalues \((1,e^{-2i\theta})\), displacement singular values
\((0,2\sin\theta)\), and trace cost equal to the rank-one projection
trace distance. Direct sums produce finite-dimensional complex trace attainers.
The real scalar field does not permit this phase multiplier.

For \(WU=V\), the source-supported inequalities include:
\[
\begin{aligned}
s_k((I-D)|_U)&\le s_k((I-W)|_U),\\
\| (I-D)^*(I-D)\|_{\mathcal I}&\le\|(I-W)^*(I-W)\|_{\mathcal I},\\
\|I-D\|_{Q}&\le\|I-W\|_{Q},\\
\|P_U-P_V\|_N&\le\|I-W\|_N.
\end{aligned}
\]
The second inequality requires a suitable invariant norm/ideal and its membership assumptions; the third requires the Q-norm property. The first is restricted displacement, the final two concern full displacement.

For finite-dimensional complex spaces, a **phase-corrected** transporter attains \(\min_{WU=V}\|I-W\|_1=2\sum_j\sin\theta_j=\|P_U-P_V\|_1\), but need not be the canonical direct rotation. The conventional real line/hyperplane result appears in `REAL_TRANSPORT_MINIMIZATION_NOTES.md` and is explicitly **not** certified there as a compiled Lean theorem. The `ℝ⁴` counterexample and Q-norm repair are compiled source results.

## Exact Lean declaration excerpts

**`directRotation_fullDisplacement_qnorm`.** The Q-norm repair applies to **unsquared full** displacement; without `IsQNorm`, the implication from squared-displacement optimality is unjustified.

`DavisKahan/FiniteDimensional/DirectRotation/QNorm.lean` — `directRotation_fullDisplacement_qnorm` (exact declaration header; proof body omitted):

```lean
theorem directRotation_fullDisplacement_qnorm
    (N : UnitarilyInvariantSeminorm 𝕜 E E) (hN : IsQNorm N)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V) (W : E ≃ₗᵢ[𝕜] E)
    (hmap : U.map W.toLinearMap = V) :
    N (LinearMap.id - (directRotation U V hacute).toLinearMap) ≤
      N (LinearMap.id - W.toLinearMap) :=
```

**`uiNorm_directRotation_le_two_div_sqrt_three_mul_displacement`.** This is an approximation-factor bound under a short-angle hypothesis, not a minimizer theorem.

`DavisKahan/FiniteDimensional/DirectRotation/SharpDisplacement.lean` — `uiNorm_directRotation_le_two_div_sqrt_three_mul_displacement` (exact declaration header; proof body omitted):

```lean
theorem uiNorm_directRotation_le_two_div_sqrt_three_mul_displacement
    (N : UnitarilyInvariantSeminorm 𝕜 E E)
    (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hacute : Submodule.IsAcute U V)
    (hgap : U.projectionGap V ≤ Real.sin (Real.pi / 3))
    (W : E ≃ₗᵢ[𝕜] E) (hmap : U.map W.toLinearMap = V) :
    N (LinearMap.id - (directRotation U V hacute).toLinearMap) ≤
      (2 / Real.sqrt 3) * N (LinearMap.id - W.toLinearMap) :=
```

**`exists_global_complex_trace_minimizer_with_principalAngles`.** Finite-dimensional **complex** spaces with equal-rank subspaces admit a phase-corrected trace-norm minimizer whose cost equals twice the sum of principal sines. It need not be the canonical direct rotation.

`DavisKahan/FiniteDimensional/DirectRotation/ComplexTracePrincipalAngles.lean` — `exists_global_complex_trace_minimizer_with_principalAngles` (exact declaration header; proof body omitted):

```lean
theorem exists_global_complex_trace_minimizer_with_principalAngles
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection]
    (hUV : finrank ℂ U = finrank ℂ V) :
    ∃ W : H ≃ₗᵢ[ℂ] H,
      U.map W.toLinearMap = V ∧
      (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) =
        (U.starProjection.toLinearMap - V.starProjection.toLinearMap).kyFanSum (finrank ℂ H) ∧
      (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) =
        2 * ∑ j : Fin (finrank ℂ U), Real.sin (Submodule.principalAngles U V (j : ℕ)) ∧
      ∀ Z : H ≃ₗᵢ[ℂ] H, U.map Z.toLinearMap = V →
        (LinearMap.id - W.toLinearMap).kyFanSum (finrank ℂ H) ≤
          (LinearMap.id - Z.toLinearMap).kyFanSum (finrank ℂ H) :=
```

**`proposition4_3_directRotation_sourceExact_complex`.** The source-facing squared-displacement theorem explicitly takes `IsSourceDirectRotation`, preserving the paper’s definition rather than weakening it to an arbitrary rotation predicate.

`DavisKahan/Sources/DavisKahan1970/Section4DirectRotationSource.lean` — `proposition4_3_directRotation_sourceExact_complex` (exact declaration header; proof body omitted):

```lean
theorem proposition4_3_directRotation_sourceExact_complex
    [TopologicalSpace.SeparableSpace H]
    (N : NormalizedUnitaryInvariantNorm.{0, v} ℂ)
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (hcompact : IsCompactOperator (TauCeti.principalSineOperator U V))
    (D : H →L[ℂ] H) (hD : DavisKahan.IsSourceDirectRotation U V D)
    (W : H →L[ℂ] H) (hWunitary : W ∈ unitary (H →L[ℂ] H))
    (hWmap : W * U.starProjection = V.starProjection * W)
    (hWmem : N.Mem ((1 - star W) * (1 - W))) :
    N.Mem ((1 - star D) * (1 - D)) ∧
      N.gauge ((1 - star D) * (1 - D)) ≤ N.gauge ((1 - star W) * (1 - W)) :=
```

