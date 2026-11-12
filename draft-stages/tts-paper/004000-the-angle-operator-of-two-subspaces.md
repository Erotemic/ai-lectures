# 004000 — The angle operator of two subspaces

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** geometry. **Audience:** principal angles in finite dimensions, orthogonal projections, positive operators and square roots.

<!-- BEGIN SPOKEN LECTURE -->

The angle operator of two subspaces

In finite dimensions, two subspaces of equal dimension have a list of principal angles. The cosines are the singular values of an overlap matrix, each angle lives in its own principal plane, and every norm of the difference of the two projections is a formula in the angles. The subspaces in the Davis–Kahan paper are usually not like that. An exact spectral subspace of an operator on an infinite-dimensional Hilbert space can itself be infinite-dimensional, and the list of angles may not exist. This lecture builds the object that replaces the list: an angle operator.

Here is what we will establish. For closed subspaces U and V of a Hilbert space, with orthogonal projections P and Q, the compression of Q to U is a positive operator on U with norm at most one. Its positive square root is the cosine of a directed angle operator, called Theta zero, which acts on U and has spectrum between zero and ninety degrees. The same construction applied to the orthogonal complements gives a second operator, Theta one, and together they form the full angle operator Theta. The square of P minus Q commutes with both projections, and the positive square root of that square is exactly the sine of Theta, so the norm of P minus Q is the sine of the largest angle. Finally, when the first subspace is described by an isometric frame, as a trial subspace is in the sine-theta theorem, the sine of Theta zero is the modulus of a rectangular operator, and therefore has exactly the same singular values. That last fact is the first step in the proof of the sine-theta theorem.

The scalars are real or complex throughout, and a star denotes the adjoint.

A continuum of angles

Let us start with an example in which there is no list of principal angles, yet the geometry is perfectly clear.

The ambient space consists of pairs of square-integrable functions on the interval from zero to one. An element is a pair f, g, and its squared length is the integral of the squared absolute value of f plus the integral of the squared absolute value of g. At each point t of the interval, the values f of t and g of t form a vector in a plane. So we can think of this space as a family of planes, one for each point t, glued together by integration.

The source subspace U consists of the pairs whose second function is zero: all pairs of the form f, zero. In each plane, U picks out the first axis.

For the target subspace V, choose an angle function phi of t equal to sixty degrees times t, so phi rises steadily from zero at the left end of the interval to sixty degrees at the right end. The target V consists of all pairs of the form cosine phi of t times h of t, and sine phi of t times h of t, where h is any square-integrable function. In the plane at the point t, V picks out the line at angle phi of t above the first axis.

So pointwise, this is the picture of two lines in a plane, with the angle between them varying continuously with t. Let us project. Take a source vector, a pair f, zero, and project it onto V. The projection acts point by point, since it is projection onto a line in each plane. At the point t, the first axis vector f of t lands on the target line with length cosine phi of t times the absolute value of f of t. So the squared length of Q applied to our source vector is the integral of cosine squared phi of t times the squared absolute value of f of t.

Now ask the finite-dimensional question: what are the principal angles? Is there a unit source vector at the smallest possible angle to V? The smallest pointwise angle is zero, at t equal to zero. But a single point carries no length in this space. Any unit vector f must spread its length over a set of positive measure, and on that set phi is positive. So every unit source vector makes a positive angle with V, while there are source vectors, concentrated near t equal to zero, with angles as small as we like. The infimum is zero and it is not attained. The same thing happens at the other end: angles approach sixty degrees and never reach it. No pair of principal vectors exists, and no list of principal angles describes the configuration.

Yet one object describes it completely: the operator on U that multiplies f of t by phi of t. Applying this operator to a source vector multiplies its value at each point by the angle at that point. It has no eigenvectors, because an eigenvector would have to be concentrated where phi takes a single value, which is a single point. Its spectrum is the whole interval from zero to sixty degrees. This multiplication operator is the angle operator of the pair, and the rest of this lecture constructs it in general.

Compressing one projection to the other subspace

Let E be a Hilbert space, and let U and V be closed subspaces with orthogonal projections P and Q. In finite dimensions, the squared cosines of the principal angles were the eigenvalues of a compression: the quadratic form recording how much of a unit vector of U lands in V. That quadratic form is available in any dimension.

For a vector u in U, the squared length of Q u equals the inner product of Q u with u, because Q is self-adjoint and Q squared equals Q. Since u is in U, we can also write u as P u. So the squared length of Q u equals the inner product of P Q P u with u. The operator P Q P, restricted to U, maps U into U, and its quadratic form gives the squared length of the landing part of each source vector.

Two properties follow at once. This compression is positive, since its quadratic form is a squared length. And it has norm at most one, since the landing part of u is never longer than u. A positive operator has a unique positive square root, obtained by functional calculus. Define the cosine operator, cosine of Theta zero, to be the positive square root of P Q P restricted to U.

This definition has a concrete meaning. For every u in U, the length of cosine Theta zero applied to u equals the length of Q u. The cosine operator does not land in V, it acts on U, but it stretches each source vector to exactly the length of the part of that vector that lands in V.

The complementary compression does the same for the escaping part. Restrict P times the identity minus Q, times P, to U. Its quadratic form is the squared length of the part of u perpendicular to V. Its positive square root is the sine operator, sine of Theta zero, and the length of sine Theta zero applied to u equals the length of the part of u that escapes V. Since the two compressions add up to P, which is the identity on U, we have the operator form of the Pythagorean identity: cosine squared Theta zero plus sine squared Theta zero equals the identity on U.

Finally, the angle operator itself. The cosine operator is positive with spectrum between zero and one, so we can apply the arc cosine function to it by functional calculus. The result, Theta zero, is a self-adjoint operator on U with spectrum between zero and ninety degrees, and applying cosine and sine to it recovers the two operators we started with. That last step uses the scalar fact that the sine of the arc cosine of x is the square root of one minus x squared, for x between zero and one.

What functional calculus means here is concrete. If the self-adjoint operator has an eigenbasis, apply the function to each eigenvalue and keep the eigenvectors. If it is a multiplication operator, apply the function to the multiplier. In our continuum example, the compression P Q P on U multiplies f of t by cosine squared phi of t. Its square root multiplies by cosine phi of t, its arc cosine multiplies by phi of t, and that is the angle operator we found before.

In finite dimensions, with equal dimensions and orthonormal bases, the eigenvalues of Theta zero are the principal angles. In the four-dimensional pair with angles of thirty and sixty degrees, where U is spanned by e one and e two, Theta zero is the diagonal operator with entries thirty and sixty degrees in that basis, and sine Theta zero has entries one half and the square root of three over two.

What the directed angle sees

Theta zero is directed. It looks out from U toward V. Its norm is the largest angle at which a vector of U sits relative to V, and the norm of sine Theta zero equals the norm of the identity minus Q, composed with P: the longest escaping component of a unit vector of U.

A source vector perpendicular to all of V has a cosine of zero, and so it lies in the eigenspace of Theta zero for the angle ninety degrees. These right angles are recorded without any assumption about dimensions. U may be a single line and V infinite-dimensional, or the other way around; the compression is defined either way.

What Theta zero cannot see is a direction of V that is perpendicular to all of U. Such a direction contributes nothing to the compression on U. Recall the line lying inside a plane. The line's only direction lies in the plane, so Theta zero is zero, while the plane has a direction perpendicular to the line, which the directed angle from the line ignores.

Comparing the complements

To capture what Theta zero misses, compare the orthogonal complements. The complement of U and the complement of V are also closed subspaces, with projections the identity minus P and the identity minus Q. Apply the same construction: compress the identity minus Q to the complement of U, take the square root, and take the arc cosine. The result is a second directed angle operator, Theta one, acting on the complement of U.

Return to the line inside the plane. The plane's extra direction is perpendicular to the line, so it lies in the complement of U. It is also perpendicular to the complement of the plane, since it lies in the plane. So, relative to the complement of V, it makes a right angle, and Theta one has the eigenvalue ninety degrees on it. Directions of V perpendicular to U appear as right angles in Theta one.

The full angle operator Theta is the block-diagonal operator on the whole space that acts as Theta zero on U and as Theta one on the complement of U. When we write Theta less than or equal to some number c, we mean that the operator norm of Theta is at most c, which says that both blocks have all their angles at most c.

In finite dimensions with equal dimensions, Theta one repeats the nonzero angles of Theta zero. In a principal plane, the source line and the target line meet at angle theta, and so do the lines perpendicular to them within the same plane. So the complementary angles are the same list, and Theta adds no new information. When dimensions differ, or in infinite dimensions, Theta one can carry right angles that Theta zero does not.

The sine of Theta is the absolute value of P minus Q

There is a remarkable way to see the full sine of Theta in one formula. Start with the square of the difference of the projections. Expanding, P minus Q, squared, equals P plus Q minus P Q minus Q P.

Multiply this on the left by P. Using P squared equals P, the four terms become P, plus P Q, minus P Q, minus P Q P, which simplifies to P minus P Q P. Now multiply it on the right by P instead. The four terms become P, plus Q P, minus P Q P, minus Q P, which also simplifies to P minus P Q P. The two products agree. So the square of P minus Q commutes with P, and by the symmetric calculation, with Q as well.

An operator that commutes with P maps U into U and the complement of U into the complement of U. So the square of P minus Q is block diagonal with respect to U and its complement. On U it equals P minus P Q P, which is the sine-squared compression, sine squared of Theta zero. On the complement of U, the same kind of calculation gives the identity minus P, times Q, times the identity minus P. That is the compression of Q to the complement of U. Its quadratic form measures how much of a vector perpendicular to U lands in V, which is exactly how much of it escapes the complement of V. So this block is sine squared of Theta one.

Therefore the square of P minus Q equals sine squared of Theta. Take positive square roots: the absolute value of P minus Q, meaning the positive square root of its square, is sine Theta. This gives a definition of the full angle that mentions neither block: Theta is the arc sine of the absolute value of P minus Q.

Two consequences follow. First, the operator norm of P minus Q equals the norm of sine Theta, and since sine is increasing between zero and ninety degrees, that is the sine of the norm of Theta: the sine of the largest angle. Second, the norm of Theta is strictly less than ninety degrees exactly when the norm of P minus Q is less than one. The journal paper calls such a pair acute. Davis and Kahan use the word acute for a weaker condition, that no vector of either subspace is perpendicular to the whole of the other; in finite dimensions the two agree. This threshold, the norm of P minus Q below one, is a hypothesis under which there is a unique canonical rotation, the direct rotation, carrying U onto V.

The formula also locates where the projections agree. P minus Q vanishes on the vectors that lie in both subspaces and on the vectors perpendicular to both. It equals plus one on vectors of U perpendicular to V, and minus one on vectors of V perpendicular to U. These two right-angle spaces, the source directions perpendicular to the target and the target directions perpendicular to the source, are called defect spaces, and they control whether one subspace can be rotated onto the other at all.

Check this against a single plane. There, P minus Q was the sine of theta times a reflection, and a reflection squares to the identity. So the square of P minus Q is sine squared theta times the identity on that plane, and its absolute value is sine theta times the identity, as the general formula predicts.

Frames: the angle in trial coordinates

In the sine-theta theorem, the subspaces are not given as subspaces. They are given by isometric coordinate maps. The trial subspace is the range of an isometry E zero, from a coordinate Hilbert space into the ambient space; E zero takes a list of coordinates and returns a trial vector without changing lengths. The exact wanted subspace is the range of another isometry, F zero, and its orthogonal projection is F zero times F zero star. I will call that projection P exact, to keep it distinct from the projections of the first part of the lecture.

The paper defines the angle on the trial coordinates. The cosine is the positive square root of E zero star, P exact, E zero, and the sine is the positive square root of the identity minus E zero star, P exact, E zero. These are the compressions we already know, transported to coordinates. E zero is a unitary identification of the coordinate space with the trial subspace, so this coordinate operator has the same spectrum as the directed angle operator on the trial subspace itself. Both are called Theta zero.

Now comes the observation the proof of the sine-theta theorem depends on. Define S to be the identity minus P exact, composed with E zero. S takes trial coordinates, builds the trial vector, and keeps only the part of it that escapes the exact subspace. Its input is the trial coordinate space, and its output lies in the ambient space. Compute S star S. It is E zero star, times the identity minus P exact, times E zero, because the identity minus P exact is a projection and squares to itself. And that equals the identity minus E zero star, P exact, E zero, because E zero star E zero is the identity. So S star S is sine squared of Theta zero.

For any bounded operator B, the modulus of B is the positive square root of B star B. It acts on the input space of B, and it has the defining property that the length of the modulus of B applied to x equals the length of B x, for every x. What we have shown is that the modulus of S is sine Theta zero.

Why does this matter? The polar decomposition writes any bounded operator as a partial isometry times its modulus. So S equals some partial isometry, call it W, times sine Theta zero. The partial isometry relabels the outputs without changing any lengths on the relevant subspace. As a result, S and sine Theta zero have the same singular values; in finite dimensions, this is the statement that the singular values of S are the square roots of the eigenvalues of S star S. Every unitarily invariant norm, whether the operator norm, the Frobenius norm, the trace norm, or any of the norms in the paper, depends only on singular values. So each such norm of S equals the same norm of sine Theta zero.

The difference between these two operators matters when the proof is written out in full. Sine Theta zero acts on the trial coordinate space and returns trial coordinates. S starts on the trial coordinate space and ends in the ambient space. The theorem is stated for sine Theta zero, and the analytic estimates are proved for S and related rectangular maps. The modulus identity is the bridge between them.

There is a third face of the same sine. Let F one be an isometry onto the orthogonal complement of the exact subspace. Then the identity minus P exact equals F one times F one star, and so S equals F one times X, where X is F one star times E zero. X measures each trial vector in the coordinates of the unwanted space. Because F one is an isometry, X star X equals S star S, and the modulus of X is again sine Theta zero. The sine-theta proof bounds X, through a Sylvester equation in the coordinates of the unwanted space, and then reads off the bound for sine Theta zero.

Check it on the four-dimensional example, with E zero the frame e one, e two and the exact subspace spanned by v one and v two. The escaping part of e one is e one minus its projection onto the target, and has length one half, the sine of thirty degrees. The escaping part of e two has length the square root of three over two, the sine of sixty degrees. These escaping parts are perpendicular to each other, so S star S is the diagonal matrix with entries one quarter and three quarters, and its square root is sine Theta zero, with entries one half and the square root of three over two.

Where the idea comes from

The operator viewpoint on the relative position of two subspaces predates the Davis–Kahan paper. Jacques Dixmier studied the relative position of two closed subspaces of a Hilbert space in 1948, and Chandler Davis's 1958 paper on the separation of two linear subspaces placed the cosine and sine data in an operator-theoretic setting through closeness and separation operators. In their 1970 paper, Davis and Kahan define Theta as an operator from the start, precisely because the spectral subspaces they study need not be finite-dimensional.

To summarize. For closed subspaces U and V, the compression of Q to U is a positive contraction; its square root is cosine Theta zero, and the length of cosine Theta zero applied to u is the length of the part of u landing in V. Sine Theta zero measures the escaping part in the same way, and the two satisfy cosine squared plus sine squared equals the identity. Theta zero is directed; the complementary operator Theta one records target directions perpendicular to the source. Together they form Theta, and the absolute value of P minus Q is sine Theta, so the norm of P minus Q is the sine of the largest angle and the pair is acute exactly when that norm is below one. In trial coordinates, sine Theta zero is the modulus of the escaping block S, and also of its coordinates X in the unwanted space, so all three have the same unitarily invariant norms.

The angle operator is defined without any list of angles, and in general it has none. When its spectrum is continuous, as in the example on the interval, there are no principal vectors, only spectral subspaces of Theta. Whenever Theta happens to be compact, its eigenvalues recover a sequence of principal angles accumulating only at zero, and the finite-dimensional picture returns.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Definitions

Let \(U,V\subseteq\mathcal E\) be closed, \(P=P_U\), \(Q=P_V\).

- \(\cos^2\Theta_0 := PQP|_U\), \(\sin^2\Theta_0 := P(I-Q)P|_U\), \(\cos\Theta_0,\sin\Theta_0\) their positive square roots, \(\Theta_0:=\arccos(\cos\Theta_0)\), \(\sigma(\Theta_0)\subseteq[0,\pi/2]\). For \(u\in U\): \(\|\cos\Theta_0\,u\|=\|Qu\|\), \(\|\sin\Theta_0\,u\|=\|(I-Q)u\|\); \(\cos^2\Theta_0+\sin^2\Theta_0=I_U\).
- \(\Theta_1\): the same construction for \(U^\perp,V^\perp\), so \(\sin^2\Theta_1=(I-P)Q(I-P)|_{U^\perp}\).
- \(\Theta:=\Theta_0\oplus\Theta_1\) on \(U\oplus U^\perp\); \(\Theta\le c\) means \(\|\Theta\|\le c\).
- **Identity.** \((P-Q)^2=P+Q-PQ-QP\), and \(P(P-Q)^2=(P-Q)^2P=P-PQP\). Hence \((P-Q)^2\) commutes with \(P\) (and \(Q\)), and
  \[
  (P-Q)^2=\sin^2\Theta_0\oplus\sin^2\Theta_1=\sin^2\Theta,\qquad |P-Q|=\sin\Theta,\qquad \|P-Q\|=\sin\|\Theta\|.
  \]
- **Acuteness.** \(\|P-Q\|<1\iff\|\Theta\|<\pi/2\).
- **Kernel and \(\pm1\) eigenspaces.** \(\ker(P-Q)=(U\cap V)\oplus(U^\perp\cap V^\perp)\); \(P-Q=+I\) on \(U\cap V^\perp\), \(-I\) on \(U^\perp\cap V\) (the defect spaces).
- **Frames.** \(E_0:\mathcal F\to\mathcal E\), \(F_0:\mathcal H\to\mathcal E\) isometries, \(P_{\rm exact}=F_0F_0^*\), \(F_1\) an isometry onto \(\operatorname{ran}(F_0)^\perp\):
  \[
  \cos\Theta_0=(E_0^*P_{\rm exact}E_0)^{1/2},\quad \sin\Theta_0=(I-E_0^*P_{\rm exact}E_0)^{1/2},
  \]
  \[
  S=(I-P_{\rm exact})E_0,\quad S^*S=I-E_0^*P_{\rm exact}E_0,\quad |S|=\sin\Theta_0,
  \]
  \[
  X=F_1^*E_0,\quad S=F_1X,\quad X^*X=S^*S,\quad |X|=\sin\Theta_0 .
  \]
  Polar decomposition \(S=W|S|\) gives \(s_j(S)=s_j(\sin\Theta_0)\) and \(N(S)=N(\sin\Theta_0)\) for every unitarily invariant norm \(N\) (with membership on both sides equivalent).

### Examples

- **Continuum.** \(\mathcal E=L^2[0,1]\oplus L^2[0,1]\), \(U=\{(f,0)\}\), \(V=\{(\cos\varphi\,h,\sin\varphi\,h)\}\), \(\varphi(t)=\tfrac{\pi}{3}t\). \(V\) is closed (isometric image of \(L^2\)), \(U\cap V=\{0\}\). \(PQP|_U=M_{\cos^2\varphi}\), \(\Theta_0=M_\varphi\), \(\sigma(\Theta_0)=[0,\pi/3]\), no eigenvalues.
- **Four-dimensional pair** (angles \(30^\circ,60^\circ\)): \(E_0=[e_1\ e_2]\); \(\sin\Theta_0=\operatorname{diag}(\tfrac12,\tfrac{\sqrt3}{2})\); \(S^*S=\operatorname{diag}(\tfrac14,\tfrac34)\).
- **Plane.** \(P-Q=\sin\theta\cdot R\) with \(R^2=I\), so \((P-Q)^2=\sin^2\theta\,I\).

### Lean correspondence

Tau Ceti (pin `a67a6500`), `TauCeti/Analysis/InnerProductSpace/Modulus.lean`, `namespace ContinuousLinearMap`:

```lean
noncomputable def modulus (T : E →L[𝕜] F) : E →L[𝕜] E :=
  CFC.sqrt (T† ∘L T)

theorem norm_modulus_apply (T : E →L[𝕜] F) (x : E) : ‖T.modulus x‖ = ‖T x‖
theorem norm_modulus (T : E →L[𝕜] F) : ‖T.modulus‖ = ‖T‖
```

`TauCeti/Analysis/InnerProductSpace/Projection/AngleOperator.lean`, `namespace Submodule`, with
`{𝕜 E : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]` and `(U V : Submodule 𝕜 E) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]`:

```lean
def cosAngleOperator : E →L[𝕜] E :=
  (U.cosThetaMap V).modulus          -- |P_V P_U|

def sinAngleOperator : E →L[𝕜] E :=
  (U.starProjection - V.starProjection).modulus   -- |P_U - P_V|

theorem sinAngleOperator_sq :
    U.sinAngleOperator V ^ 2 = (U.starProjection - V.starProjection) ^ 2
theorem commute_starProjection_sinAngleOperator :
    Commute U.starProjection (U.sinAngleOperator V)
theorem sinAngleOperator_mul_starProjection :
    U.sinAngleOperator V * U.starProjection = (U.sinThetaMap V).modulus
theorem norm_sinAngleOperator : ‖U.sinAngleOperator V‖ = U.projectionGap V
theorem ker_sinAngleOperator : (U.sinAngleOperator V).ker = U ⊓ V ⊔ Uᗮ ⊓ Vᗮ
theorem sinAngleOperator_orthogonal : Uᗮ.sinAngleOperator Vᗮ = U.sinAngleOperator V
```

Davis–Kahan library, `DavisKahan/Geometry/Angle/OperatorAngleGeneric.lean`, `namespace TauCeti.DavisKahan.Angle`:

```lean
/-- The paper's Hermitian operator angle `Θ = arcsin |P_U - P_V|`. -/
def angleOperator (U V : Submodule 𝕜 E)
    [U.HasOrthogonalProjection] [V.HasOrthogonalProjection] : E →L[𝕜] E :=
  cfc Real.arcsin ((Submodule.sinAngleOperator U V))
```

`DavisKahan/Sources/DavisKahan1970/SineTheta/Presentation.lean`, `namespace TauCeti.DavisKahan1970`, `{𝕜 : Type u} [RCLike 𝕜]`, `{E F G H : Type v}` Hilbert spaces (`E` ambient, `F` trial coordinates, `H` exact coordinates):

```lean
noncomputable def sourceDirectedSineBlock
    (E₀ : F →L[𝕜] E) (F₀ : H →L[𝕜] E) : F →L[𝕜] E :=
  (ContinuousLinearMap.id 𝕜 E - F₀ ∘L F₀.adjoint) ∘L E₀          -- S = (I - P_exact) E₀

noncomputable def sourceDirectedSineModulus
    (E₀ : F →L[𝕜] E) (F₀ : H →L[𝕜] E) : F →L[𝕜] F :=
  ContinuousLinearMap.modulus (sourceDirectedSineBlock E₀ F₀)    -- |S|

noncomputable def sourceDirectedThetaOperator
    (E₀ : F →L[𝕜] E) (F₀ : H →L[𝕜] E) : F →L[𝕜] F :=
  cfc Real.arcsin (sourceDirectedSineModulus E₀ F₀)               -- Θ₀

noncomputable def sourceDirectedSinThetaOperator
    (E₀ : F →L[𝕜] E) (F₀ : H →L[𝕜] E) : F →L[𝕜] F :=
  cfc Real.sin (sourceDirectedThetaOperator E₀ F₀)                -- sin Θ₀

theorem sourceDirectedSinThetaOperator_eq_modulus
    (E₀ : F →L[𝕜] E) (F₀ : H →L[𝕜] E)
    (hE₀ : IsometricEmbedding E₀) (hF₀ : IsometricEmbedding F₀) :
    sourceDirectedSinThetaOperator E₀ F₀ =
      ContinuousLinearMap.modulus (sourceDirectedSineBlock E₀ F₀)
```

`IsometricEmbedding X` is `∀ x, ‖X x‖ = ‖x‖` (`DavisKahan/BoundedOperator/Problem.lean`).

**Mapping notes.**

- The lecture defines \(\Theta_0\) through the cosine (Davis–Kahan's convention, \(\Theta_0=\arccos\cos\Theta_0\)). The formal presentation reconstructs \(\Theta_0\) as \(\arcsin|S|\); the docstring of `sourceDirectedThetaOperator` points to `SineTheta/AngleIdentity.lean`, which proves the two agree for the canonical subspace coordinates.
- `sourceDirectedSinThetaOperator` is the object in the conclusion of the paper's headline sine-theta theorem (`sinTheta_unbounded_formGap_whereDefinedUIN_rclike`); `sourceDirectedSinThetaOperator_eq_modulus` is the bridge \(|S|=\sin\Theta_0\).
- The ambient angle `angleOperator U V` is defined as \(\arcsin|P_U-P_V|\), the identity \(|P-Q|=\sin\Theta\) derived in the lecture.
