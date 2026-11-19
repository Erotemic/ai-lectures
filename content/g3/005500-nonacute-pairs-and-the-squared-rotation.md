# 005500 — Nonacute pairs and the squared rotation

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** geometry. **Audience:** the direct rotation, Halmos's decomposition, defect spaces.

<!-- BEGIN SPOKEN LECTURE -->

Nonacute pairs and the squared rotation

The direct rotation turns one subspace onto another the shortest way. When some source vector is perpendicular to the entire target, there is no shortest way for that vector: turning it by plus ninety degrees and by minus ninety degrees are equally short. This lecture settles what happens then, and proves one more structural fact that will matter for the double-angle theorems.

The results are these. First, Davis and Kahan's Proposition 3.2: for an arbitrary pair of closed subspaces, a direct rotation exists if and only if the two defect spaces have the same dimension. Here the source defect, D zero, consists of the source vectors perpendicular to the whole target, and the target defect, D one, consists of the target vectors perpendicular to the whole source. When the defects are nonzero, the direct rotation is not unique; on the defects every direct rotation squares to minus the identity. Second, the paper's standing convention: from this point on, Davis and Kahan assume the defects have equal dimension, so a direct rotation always exists. Third, Proposition 3.4: if every angle from U to V is at most forty-five degrees, then the square of the direct rotation is itself a direct rotation, from the mirror image of V across U onto V.

P and Q are the projections onto U and V, and the block notation is the one from the definition of a direct rotation: C zero and C one are the diagonal blocks on U and on its complement, S zero is the block from U to the complement, and minus S zero star is the block back.

The right-angle case in the plane

Start with the simplest nonacute pair. In the plane, let U be the horizontal axis and V the vertical axis. Every vector of U is perpendicular to V, so the source defect is all of U. Every vector of V is perpendicular to U, so the target defect is all of V.

Which orthogonal maps carry the horizontal axis onto the vertical axis? The rotation through plus ninety degrees does, sending the horizontal unit vector to the vertical one. So does the rotation through minus ninety degrees, sending it to the downward vertical vector. So do the reflections across the two diagonal lines.

Check the definition of a direct rotation. Both rotations have zeros on the diagonal. Zero is a positive operator, in the sense that its quadratic form is nonnegative, so both diagonal conditions hold. The off-diagonal entries of a rotation are opposite, so the third condition holds too. Both rotations are direct rotations. The reflections have off-diagonal entries that are equal rather than opposite, so they are not. And the square of each rotation through ninety degrees is the rotation through one hundred eighty degrees, which is minus the identity.

So at a right angle, the direct rotation exists but is not unique, and it squares to minus one. These are exactly the features that persist in general.

What a direct rotation does to the defects

Let W be any direct rotation from U to V. Its diagonal block on U is forced. Since W carries U onto V, W P W star equals Q. Compute C zero times C zero star, which is P W P W star P. Using W P W star equals Q, this is P Q P on U, the squared cosine compression. Positivity of C zero makes it self-adjoint, so C zero squared equals cosine squared Theta zero, and by uniqueness of positive square roots, C zero equals cosine Theta zero. In words: any direct rotation acts within U as the cosine of the angle operator. The same argument on the complement gives C one equals cosine Theta one.

Now take a vector x in the source defect. Its angle to V is ninety degrees, so cosine Theta zero kills it, and therefore the component of W x in U is zero. On the other hand W x lies in V, because W carries U onto V. So W x is a vector of V perpendicular to U: it lies in the target defect. A direct rotation maps the source defect into the target defect. By the symmetric argument applied to the complement, it maps the target defect into the source defect. Since W preserves lengths and is invertible, it identifies the two defects with each other. A unitary identification of two Hilbert spaces exists only when they have the same dimension. So a direct rotation can exist only if the source defect and the target defect have the same dimension.

What happens to a defect vector under two applications? The first application sends x in D zero to W x in D one, through the crossing block S zero. The second sends W x back to D zero through the crossing block minus S zero star. So W squared x equals minus S zero star S zero x. Because W is unitary and x has no component that stays in U, S zero acts isometrically on the defect, and S zero star S zero is the identity there. So W squared x equals minus x. Every direct rotation acts on the sum of the two defects as a quarter turn whose square is minus the identity.

Constructing direct rotations when the defects match

Conversely, suppose the source defect and the target defect have the same dimension, and choose any unitary map G from D zero onto D one. Define W on the two defects as follows. A vector x of D zero goes to G x in D one. A vector y of D one goes to minus G star y in D zero. This is the plane's rotation through ninety degrees, carried out on many planes at once.

Check the definition. On the defects, the diagonal blocks are zero, which counts as positive. The crossing block from U to the complement is G, and the block back is minus G star, so the off-diagonal condition holds. W maps the source defect, part of U, into the target defect, part of V. It maps the target defect, part of the complement of U, into the source defect, part of the complement of V. So it carries U's share of the defects onto V's share.

On the rest of the space the pair has no defects, and the acute construction applies: the polar factor of the intertwiner T, which is the identity on the common and exterior parts and the operator rotation with blocks C, minus S, S, C on the generic part. Assembling the pieces gives a direct rotation of the whole space.

This proves Proposition 3.2: a direct rotation from U to V exists if and only if the source and target defects have the same dimension. The construction also exposes the freedom. Every choice of the unitary G gives a direct rotation, different choices give different ones, and away from the defects there is no freedom at all, because the diagonal blocks are forced to be cosine Theta zero and cosine Theta one, and in the acute part those determine everything. In the real plane with perpendicular axes, each defect is a line, G is plus or minus one, and the two resulting direct rotations are the rotations through plus and minus ninety degrees. Over the complex numbers with a one-dimensional defect, G can be multiplication by any unit complex number, and there is a whole circle of direct rotations.

The same freedom appears in the square-root description. The product of the reflections through V and through U equals minus the identity on the defects, and minus one has many unitary square roots with spectrum on the imaginary axis, which is the boundary of the right half-plane. Proposition 3.3 accepts such a square root as a direct rotation exactly when it carries the source defect onto the target defect.

When equal dimensions are not enough

In finite dimensions, if U and V have the same dimension, the defects automatically have the same dimension. Count dimensions in U: the common part, plus the source defect, plus the generic source part. Count in V: the common part, plus the target defect, plus the generic target part, which has the same dimension as the generic source part. Subtracting, the defects match.

In infinite dimensions they need not, and the example is worth holding in mind. Consider square-summable sequences indexed by all the integers. Let U consist of the sequences vanishing at every negative index, and V of the sequences vanishing at every index up to and including zero. The shift, which moves every entry one place to the right, is a unitary map carrying U onto V and the complement of U onto the complement of V. So in the sense relevant to unitaries, U and V have the same size, and so do their complements. But V lies inside U with exactly one direction to spare, the sequence concentrated at index zero. That direction is a source vector perpendicular to V, so the source defect has dimension one. The target defect is zero, since V lies inside U. The defects do not match, and by Proposition 3.2 no direct rotation carries U onto V. The shift carries U onto V, but its diagonal blocks are not positive; no unitary with positive diagonal blocks can do it.

After proving Proposition 3.2, Davis and Kahan adopt a standing convention for the rest of the paper: unless stated otherwise, they assume both that U and V, and their complements, have matching dimensions, and that the two defects have the same dimension. Every later result that does not restate its dimension conditions is read under both assumptions. In particular a direct rotation always exists, and the perturbation theorems can speak of the angle operator and the direct rotation without separate existence hypotheses.

Squaring the direct rotation

The last result of this lecture concerns the square of the direct rotation, and it is the geometric fact behind the doubled-angle theorems.

Start in the plane. Let U be the horizontal axis and V the line at angle theta above it, with theta between zero and ninety degrees. The direct rotation W turns through theta, and W squared turns through two theta. Which pair of lines does W squared carry onto each other? It carries the line at angle minus theta onto the line at angle plus theta. The line at minus theta is the mirror image of V across U. Its reflection through U is the operator J times Q times J, where J is two P minus the identity; call the mirrored subspace V minus.

Is W squared the direct rotation from V minus to V? The angle between those two lines is two theta. If two theta is at most ninety degrees, the shortest turn carrying the first onto the second is the rotation through two theta, which is W squared. If two theta exceeds ninety degrees, for example theta equal to fifty degrees so that two theta is one hundred degrees, the lines meet at an acute angle of eighty degrees on the other side, and the direct rotation turns through minus eighty degrees instead. W squared turns the long way and is not direct.

Davis and Kahan's Proposition 3.4 states the general version. Suppose that C zero squared is at least one half times the identity, which means every angle from U to V is at most forty-five degrees. Then W squared is the direct rotation carrying the mirror image of V across U onto V.

Here is why the hypothesis is the right one. The square of the direct rotation is the product of the two reflections, through V and through U. That product carries the mirrored subspace V minus onto V. On the generic part, in Halmos's coordinates, W is the operator rotation with blocks cosine Theta, minus sine Theta, sine Theta, cosine Theta, and W squared is the same matrix with Theta replaced by two Theta, by the double-angle formulas, which hold for commuting functions of one operator. Relative to the mirrored subspace, the angle that W squared turns through is two Theta, and its diagonal blocks are built from cosine of two Theta. Cosine of two Theta is positive exactly when Theta is at most forty-five degrees. So the positivity conditions in the definition hold precisely in that range.

This is the source of the factor two in the doubled-angle theorems. A reflection through an approximate subspace converts an angle into twice that angle, and Proposition 3.4 guarantees that, when the angles are at most forty-five degrees, the doubled configuration is again governed by a direct rotation. The same threshold of forty-five degrees reappears in the branch-selection theorems, where the angle operator must be shown to stay below a quarter turn.

To summarize. Any direct rotation acts within U as cosine Theta zero and within the complement as cosine Theta one. Consequently it maps the source defect isometrically onto the target defect and back, with square equal to minus the identity there. A direct rotation exists exactly when the two defects have the same dimension; the direct rotations are then parametrized by the unitary identifications of one defect with the other, and are unique only when the defects are zero. In finite dimensions equal dimensions of U and V force equal defects, but the shift on sequences indexed by the integers shows that in infinite dimensions they do not, and for that pair no direct rotation exists. Davis and Kahan assume equal defect dimensions throughout the rest of their paper. And when every angle is at most forty-five degrees, the square of the direct rotation is the direct rotation from the mirror image of V onto V.

The forty-five degree hypothesis cannot be dropped. Beyond it, the square of the direct rotation turns the long way around, and the doubled picture is no longer a direct rotation of anything.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Forced diagonal blocks

For any unitary \(W\) with \(WPW^*=Q\) and \(C_0=PWP|_U\ge0\):
\[
C_0C_0^*=PWPW^*P=PQP|_U=\cos^2\Theta_0\ \Rightarrow\ C_0=\cos\Theta_0;
\]
likewise \(C_1=\cos\Theta_1\).

### Proposition 3.2

With \(D_0=U\cap V^\perp\), \(D_1=U^\perp\cap V\):

- **Necessity.** \(x\in D_0\Rightarrow \cos\Theta_0x=0\Rightarrow PWx=0\), and \(Wx\in V\), so \(Wx\in D_1\). Symmetrically \(W D_1\subseteq D_0\). Hence \(W|_{D_0}:D_0\to D_1\) is unitary and \(\dim D_0=\dim D_1\). On \(D_0\oplus D_1\): \(W^2=-I\).
- **Sufficiency and parametrization.** For a unitary \(G:D_0\to D_1\), set \(W=\begin{pmatrix}0&-G^*\\G&0\end{pmatrix}\) on \(D_0\oplus D_1\) and the acute direct rotation (polar factor of \(T\)) on \((D_0\oplus D_1)^\perp\). Distinct \(G\) give distinct direct rotations.
- **Planar example.** \(U=\operatorname{span}e_1\), \(V=\operatorname{span}e_2\): \(D_0=U\), \(D_1=V\); direct rotations are the rotations by \(\pm90^\circ\); reflections across the diagonals are not direct.
- **Shift example.** \(\ell^2(\mathbb Z)\), \(U=\{a_n=0,\ n<0\}\), \(V=\{a_n=0,\ n\le0\}\): \(\dim D_0=1\), \(\dim D_1=0\); the bilateral shift carries \(U\to V\) but no direct rotation exists.
- **Standing convention** (after Proposition 3.2): (1.5) \(\dim U=\dim V\), \(\dim U^\perp=\dim V^\perp\), and (3.5) \(\dim D_0=\dim D_1\) are assumed unless stated otherwise.

### Proposition 3.4

If \(C_0^2\ge\tfrac12I\) (all angles of \(\Theta_0\) at most \(\pi/4\)), then with \(J=2P-I\) and \(Q_-=JQJ\),
\[
W^2=(2Q-I)(2P-I)\quad\text{is the direct rotation from }\operatorname{ran}Q_-\text{ onto }\operatorname{ran}Q.
\]
On the generic part \(W=\begin{pmatrix}\cos\Theta&-\sin\Theta\\\sin\Theta&\cos\Theta\end{pmatrix}\), \(W^2=\begin{pmatrix}\cos2\Theta&-\sin2\Theta\\\sin2\Theta&\cos2\Theta\end{pmatrix}\); positivity of the new diagonal blocks requires \(\cos2\Theta\ge0\). Planar counterexample beyond \(\pi/4\): \(\theta=50^\circ\), \(W^2\) turns \(100^\circ\) while the direct rotation from the \(-50^\circ\) line to the \(+50^\circ\) line turns \(-80^\circ\).

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/Section3Proposition32.lean`, `namespace TauCeti.DavisKahan1970`:

```lean
theorem proposition3_2_exists_iff_crossedDefectsEquivalent :
    (∃ T : H →L[𝕜] H, IsDirectRotation U V T) ↔
      CrossedDefectsEquivalent U V

theorem proposition3_2_not_unique
    (hdefect : CrossedDefectsEquivalent U V) (hnonacute : ¬ Submodule.IsAcute U V) :
    ∃ T₁ T₂ : H →L[𝕜] H,
      IsDirectRotation U V T₁ ∧ IsDirectRotation U V T₂ ∧ T₁ ≠ T₂
```

with (`DavisKahan/Geometry/Halmos/GenericRotationPredicates.lean`)

```lean
def CrossedDefectsEquivalent
    (U V : Submodule 𝕜 H) [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection] : Prop :=
  Nonempty
    (halmosSourceDefect U V ≃ₗᵢ[𝕜] halmosTargetDefect U V)
```

`DavisKahan/Sources/DavisKahan1970/Section3Proposition34.lean` (complex form; a real form `proposition3_4_full_real` also exists):

```lean
theorem proposition3_4_full_complex
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]
    (W : H →L[ℂ] H)
    (hunitary : W ∈ unitary (H →L[ℂ] H))
    (hintertwines : W * U.starProjection = V.starProjection * W)
    (hcrossed : Uᗮ.starProjection * W * U.starProjection =
      -star (U.starProjection * W * Uᗮ.starProjection))
    (hsource_pos : (U.starProjection * W * U.starProjection).IsPositive)
    (hcomplement_pos : (Uᗮ.starProjection * W * Uᗮ.starProjection).IsPositive)
    (hcos : ∀ x ∈ U, ‖x‖ ^ 2 / 2 ≤ ‖V.starProjection x‖ ^ 2) :
    (W * W) ∈ unitary (H →L[ℂ] H) ∧
      (W * W) * (reflectedSubspace U V).starProjection =
        V.starProjection * (W * W) ∧
      ((reflectedSubspace U V).starProjection * (W * W) *
        (reflectedSubspace U V).starProjection).IsPositive ∧
      ...
```

**Mapping notes.**

- `CrossedDefectsEquivalent` (a unitary identification of the two defects) is the formal version of “equal dimension”; `crossedDefectsEquivalent_iff_finrank_eq` and the separable variants translate it to dimension counts.
- `proposition3_2_parameterized_nonuniqueness` formalizes the injective parametrization of direct rotations by unitaries \(D_0\to D_1\).
- `hcos` is the hypothesis \(C_0^2\ge\tfrac12\) stated as \(\|x\|^2/2\le\|Qx\|^2\) on \(U\); `reflectedSubspace U V` is \(\operatorname{ran}(JQJ)\). The docstring records that no acuteness, compactness, finite-dimensionality or separability hypothesis is used.
