# 003900 — Principal angles between subspaces

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** geometry. **Audience:** linear algebra, the singular value decomposition, inner-product notation.

<!-- BEGIN SPOKEN LECTURE -->

Principal angles between subspaces

Davis–Kahan theory measures how far one subspace is from another. An approximate eigenspace is compared with an exact one; an eigenspace before a perturbation is compared with the eigenspace after it. Before any operator enters the story, we need to know what it means for two subspaces to be at an angle.

For two lines through the origin the answer is one number. For higher-dimensional subspaces, one number is not enough, and the correct replacement is a list of numbers called the principal angles. Here is what we will establish. Two subspaces of the same finite dimension k have exactly k principal angles, each between zero and ninety degrees, and these angles do not depend on which bases we use to describe the subspaces. They can be computed as the singular values of a small overlap matrix: those singular values are the cosines of the angles. Each principal angle lives in its own plane, and these planes are mutually perpendicular, so the whole configuration splits into independent two-dimensional pictures. Finally, the two orthogonal projections onto the subspaces are determined, up to a rotation of the whole space, by the principal angles together with a few dimensions; in particular, every norm of the difference of the projections is a formula in the angles. The sines of the angles are the error that the Davis–Kahan theorems bound.

Throughout, the scalars may be real or complex. When I write a star after a matrix or an operator, I mean its adjoint: the transpose in the real case and the conjugate transpose in the complex case.

One angle for two lines

Take two lines through the origin, and choose a unit vector on each, say x on the first line and y on the second. The angle between the lines is the angle theta whose cosine is the absolute value of the inner product of x and y. The absolute value is there because a line does not care about the sign of its unit vector. Replacing x by minus x flips the inner product, but the line is unchanged. So the angle between two lines always lies between zero and ninety degrees. Zero means the lines coincide, and ninety degrees means they are perpendicular.

It helps to say the same thing using a projection. Let Q be the orthogonal projection onto the second line. Projecting the unit vector x onto that line produces a vector of length cosine theta, and the part of x that is left over, the part perpendicular to the second line, has length sine theta. These two lengths, cosine for the part that lands and sine for the part that escapes, are the two quantities we will generalize.

Two planes that meet only at the origin

Now move to two planes. In three-dimensional space, two different planes through the origin always share a line, because two equations in three unknowns always have a nonzero solution. So in three dimensions a pair of planes has an angle of zero along the shared line, and a second angle, the familiar dihedral angle, across it. Already we need two numbers.

In four dimensions, two planes can meet only at the origin, and then the picture is more interesting. Let us build a specific pair, which will serve as our running example. Use coordinates one through four. The source plane U is spanned by the first two coordinate directions, e one and e two. The target plane V is spanned by two vectors. The first, v one, is cosine thirty degrees times e one plus sine thirty degrees times e three. In coordinates it is the square root of three over two, zero, one half, zero. The second, v two, is cosine sixty degrees times e two plus sine sixty degrees times e four. In coordinates it is zero, one half, zero, the square root of three over two.

So v one is e one tilted thirty degrees toward the third axis, and v two is e two tilted sixty degrees toward the fourth axis. No nonzero vector lies in both planes: a combination of v one and v two lies in U only if its third and fourth coordinates vanish, and that forces both coefficients to be zero.

What is the angle between these planes? A natural first attempt is to ask, for a single unit vector u in U, how close it can get to V. The closest unit vector in V is found by projecting. If Q is the orthogonal projection onto V, then for any unit vector v in V, the inner product of u with v equals the inner product of Q u with v, which is at most the length of Q u. Equality holds when v points along Q u. So the best partner for u in V makes an angle whose cosine is the length of Q u. This is the same rule as for lines: the cosine is the length of the part that lands.

Let us compute it. Write a unit vector of U as cosine phi times e one plus sine phi times e two, where phi is any angle. Because v one and v two are orthonormal, the squared length of Q u is the sum of the squares of the inner products of u with v one and with v two. The first inner product is cosine phi times cosine thirty degrees, and the second is sine phi times cosine sixty degrees. Squaring and adding, the squared length of Q u is three quarters times cosine squared phi, plus one quarter times sine squared phi.

Look at what happens as phi varies. When phi is zero, u is e one, the squared cosine is three quarters, and the angle from u to V is thirty degrees. When phi is ninety degrees, u is e two, the squared cosine is one quarter, and the angle is sixty degrees. When phi is forty-five degrees, u points halfway between e one and e two, the squared cosine is one half, and the angle is forty-five degrees. As u turns inside U, its angle to V moves continuously between thirty and sixty degrees.

So there is no single angle between U and V. Different vectors of U see V at different angles. What is intrinsic is the range of values, and in particular its two extremes, thirty and sixty degrees. Those extremes are the principal angles of this pair.

Jordan's definition

Camille Jordan, in his 1875 essay on geometry in n dimensions, made this into a general definition. The construction is a sequence of best choices.

Suppose U and V each have dimension k. First, look for the closest possible pair: a unit vector in U and a unit vector in V whose inner product is as large as possible. Call them x one and y one. The angle between them is the first principal angle, theta one, the smallest angle that any vector of U makes with any vector of V.

Next, remove those directions. Restrict attention to the vectors of U perpendicular to x one and the vectors of V perpendicular to y one, and again look for the closest pair. That gives x two, y two, and the second principal angle theta two, which is at least as large as the first. Continue until the k dimensions are used up.

In our example, the closest pair is e one and v one, at thirty degrees. Removing those leaves e two in U and v two in V, at sixty degrees. The list of principal angles is thirty and sixty degrees.

Two questions arise immediately. Does the answer depend on the choices made along the way, when the best pair is not unique? And why restrict to perpendicular directions at each step, rather than some other way of excluding what was already found? Both questions are answered by recasting the construction in terms of matrices.

The overlap matrix

Represent each subspace by an orthonormal basis, arranged as the columns of a matrix. Let X be the matrix whose columns form an orthonormal basis of U, and Y the matrix whose columns form an orthonormal basis of V. Each is an isometry from k-dimensional coordinate space into the ambient space: it takes a list of k coefficients and returns the corresponding combination of basis vectors, without changing lengths. That is the content of the identity X star X equals the identity.

The overlap matrix is X star Y. It is a k by k matrix whose entry in row i and column j is the inner product of the i-th basis vector of U with the j-th basis vector of V. In our example, with the bases e one, e two for U and v one, v two for V, the overlap matrix is diagonal, with entries the square root of three over two and one half. Those are the cosines of thirty and sixty degrees.

That diagonal form was a lucky consequence of good bases. Suppose instead we describe U by the rotated basis e one plus e two over root two, and e one minus e two over root two. Every entry of the overlap matrix changes. The first row becomes the square root of three over two and one half, each divided by root two; the second row becomes the square root of three over two and minus one half, again divided by root two. None of these four entries is a cosine of a principal angle.

But the singular values have not changed. Any other orthonormal basis of U has the form X times G, where G is a k by k unitary matrix, and any other basis of V has the form Y times H, with H unitary. The overlap matrix becomes G star, times X star Y, times H. Multiplying a matrix by unitary matrices on either side does not change its singular values. So the singular values of the overlap matrix belong to the pair of subspaces, not to the bases.

Now use the singular value decomposition the other way around. Write the overlap matrix as W times Sigma times Z star, with W and Z unitary and Sigma diagonal, its entries sigma one through sigma k in decreasing order. Change bases: replace X by X W and Y by Y Z. The new overlap matrix is Sigma itself. In these bases, the i-th basis vector of U and the i-th basis vector of V have inner product sigma i, and any two basis vectors with different indices are perpendicular.

These singular values are at most one. Each is an inner product between two unit vectors, so the Cauchy–Schwarz inequality bounds it by one. And the largest singular value is the largest possible inner product between a unit vector of U and a unit vector of V, because the largest singular value of any matrix is the maximum of its bilinear form over pairs of unit vectors. That is exactly Jordan's first step. The remaining singular values arise the same way after restricting to vectors perpendicular to the singular vectors already found. So Jordan's construction computes the singular values of the overlap matrix, and the principal angles are defined by the rule: the cosine of the i-th principal angle is the i-th singular value of X star Y.

This settles both questions. The angles do not depend on the choices made along the way, because they are singular values. And perpendicularity is the right exclusion, because singular vectors for different singular values are orthogonal.

Principal vectors and principal planes

The new basis vectors are called principal vectors. Write x i and y i for the i-th principal vectors of U and V. We have three kinds of perpendicularity. The x's are orthonormal among themselves. The y's are orthonormal among themselves. And x i is perpendicular to y j whenever i and j differ. Only the matched pairs overlap, with inner product cosine theta i.

Now consider the span of x i and y i. Call it the i-th principal plane. Every vector in this plane is a combination of x i and y i, and both of those are perpendicular to x j and to y j for any other index j. So different principal planes are perpendicular to each other.

Inside one principal plane, the picture is the picture of two lines: a source line through x i and a target line through y i, meeting at the angle theta i. When scalars are complex, the singular value decomposition has already chosen the phases so that the inner product of x i and y i is a nonnegative real number, so the same planar picture holds.

Two special cases deserve names. If theta i is zero, then x i equals y i: the plane collapses to a single line that lies in both subspaces. These are common directions. If theta i is ninety degrees, then x i is perpendicular to all of V, and y i is perpendicular to all of U. These right angles will matter a great deal when the subspaces are far apart.

So the entire configuration decomposes into perpendicular pieces: the common directions, one plane for each principal angle strictly between zero and ninety degrees, the right-angle pairs, and whatever part of the ambient space is perpendicular to both subspaces. In our example the two principal planes are the plane of e one and e three, and the plane of e two and e four. They are perpendicular, and they fill all four dimensions.

This decomposition has an immediate consequence. Rotate each principal plane through its own angle, turning x i onto y i, and leave everything perpendicular to the principal planes fixed. The result is an orthogonal or unitary map that carries U onto V. It is a natural candidate for the cheapest way of moving one subspace onto the other, and the transport part of the Davis–Kahan paper examines exactly which measures of cost it minimizes.

What the projections see

In operator form, a subspace is described by its orthogonal projection. Let P be the projection onto U and Q the projection onto V. In terms of the bases, P is X times X star, and Q is Y times Y star. Any quantity built from P and Q that is unchanged when the whole space is rotated can be computed from the principal angles and the dimensions involved. Three such quantities appear repeatedly in the paper.

The first is the compression of Q to U. Take a unit vector u in U and ask for the squared length of Q u. Writing u as X a, for a unit coefficient vector a, this squared length is a quadratic form in a, given by the matrix X star Q X. That matrix equals the overlap matrix times its adjoint, so its eigenvalues are the squared cosines of the principal angles. This is the matrix behind our earlier calculation, where the squared length of Q u was three quarters times cosine squared phi plus one quarter times sine squared phi. The eigenvalues three quarters and one quarter are the squared cosines of thirty and sixty degrees.

The second is the complementary compression, X star times the identity minus Q, times X. It measures the squared length of the part of u that escapes V, and its eigenvalues are the squared sines of the principal angles. Its positive square root is the sine of the angle operator on the coordinates of U. When U is the trial subspace in a perturbation problem and V is the exact subspace, this is precisely the operator whose size the sine-theta theorem controls. Its largest eigenvalue gives the largest sine: no unit vector of U has a component outside V longer than the sine of the largest principal angle.

The third is the difference of the projections, P minus Q. Look at it inside one principal plane. Place the source line along the first axis of the plane and the target line at angle theta. In that plane, P is the two by two matrix with a one in the top left and zeros elsewhere. Q has entries cosine squared, cosine times sine, cosine times sine, and sine squared. Subtracting, and using one minus cosine squared equals sine squared, the difference has entries sine squared, minus sine times cosine, minus sine times cosine, and minus sine squared. Every entry contains a factor of sine theta. Factor it out, and what remains is the matrix with entries sine, minus cosine, minus cosine, minus sine. That matrix is symmetric, its columns are orthonormal, and its trace is zero. It is a reflection, with eigenvalues plus one and minus one.

So inside each principal plane, the difference of the two projections is sine theta times a reflection, with eigenvalues plus sine theta and minus sine theta. On the common directions, and on the part of space perpendicular to both subspaces, P and Q agree, and their difference is zero.

When the subspaces have equal dimension, this gives the complete spectrum of P minus Q: plus and minus the sine of each principal angle, and zeros. Each common way of measuring the size of an operator then becomes a formula in the angles. The operator norm of P minus Q is the sine of the largest principal angle. The squared Frobenius norm is twice the sum of the squared sines. The trace norm, the sum of the absolute values of the eigenvalues, is twice the sum of the sines.

In our example, the operator norm of P minus Q is the sine of sixty degrees, about zero point eight seven. The squared Frobenius norm is twice the sum of one quarter and three quarters, which is two. The trace norm is twice the sum of one half and root three over two, which is one plus root three, about two point seven three. If instead both principal angles were equal to the same angle theta, the trace norm of P minus Q would be four times sine theta. That number reappears as the smallest possible trace-norm displacement in the counterexample to the paper's Proposition four point four.

Subspaces of different dimensions

Everything so far assumed equal dimensions. Suppose instead that U has dimension k and V has a larger dimension l. The overlap matrix X star Y is now k by l. It still has k singular values, so there are k principal angles, still defined as the arc cosines of those singular values.

But the symmetric picture breaks. Because V is larger, some unit vector of V is perpendicular to all of U. For that vector, P maps it to zero and Q leaves it alone, so P minus Q sends it to minus itself. The operator norm of P minus Q is therefore one, regardless of the principal angles. The simplest case is a line lying inside a plane. Its single principal angle is zero, because the line is contained in the plane, and yet the difference of the projections has norm one.

The useful quantity in this situation is directed. Ask how far U is from lying inside V: take the norm of the identity minus Q, composed with P. That is the length of the longest escaping component of a unit vector of U, and it equals the sine of the largest principal angle from U to V. For the line inside the plane it is zero, as it should be. When the dimensions are equal, this directed quantity, the same quantity with U and V interchanged, and the norm of P minus Q all coincide.

Directed angles are the natural language of the Davis–Kahan theorems. A trial subspace and an exact spectral subspace need not have the same dimension, and the sine-theta theorem measures the directed sine from the trial subspace toward the exact one.

The target written in source coordinates

There is one more way to read the same data, and it leads to the cosine–sine decomposition. Take a principal vector y i of V, with angle theta i strictly between zero and ninety degrees. Split it into its part in U and its part perpendicular to U. The part in U is cosine theta i times x i. The perpendicular part has length sine theta i; divide it by that length to obtain a unit vector, call it w i, lying in the orthogonal complement of U. Then y i equals cosine theta i times x i, plus sine theta i times w i.

The w's are orthonormal, by the same perpendicularity relations as before. So in a suitable orthonormal basis of the whole space, made of the x's, then the w's, then whatever remains, the target basis has a very simple form: a diagonal block of cosines on top, a diagonal block of sines below it, and zeros beneath. The cosine block and the sine block satisfy cosine squared plus sine squared equals the identity, which restates that the columns of Y are unit vectors.

Extending this to a full unitary matrix partitioned into two-by-two blocks gives the cosine–sine decomposition. Paige and Wei's history of the decomposition traces it from Jordan's geometry, through the principal ideas assembled by Davis and Kahan in their 1970 paper, to G. W. Stewart, who completed and explicitly formulated the matrix decomposition in 1977.

The same angles appear in statistics. Harold Hotelling's 1936 paper on relations between two sets of variates introduced canonical correlation analysis. It looks for a linear combination of the first set of variables and a linear combination of the second set that are as highly correlated as possible, and then repeats under the constraint of being uncorrelated with the combinations already found. For a sample, center each variable. A linear combination of the first set is then a vector in the column space of the first data matrix, and its correlation with a combination of the second set is the cosine of the angle between the two vectors. Hotelling's procedure is Jordan's construction applied to the two column spaces, and the sample canonical correlations are the cosines of their principal angles.

On the computational side, Åke Björck and Gene Golub gave numerical methods in 1973 for computing principal angles and vectors from orthonormal bases and the singular value decomposition, which is how the angles are computed in practice. One practical point follows from the formulas we have already seen. A cosine near one carries little information about a small angle, since cosine theta differs from one only by about theta squared over two. For small angles it is more accurate to compute the sines directly, as the singular values of the escaping part, the identity minus X X star, times Y.

Why the sines are the error

Return to the setting of the paper. There is an exact spectral subspace of a self-adjoint operator, and a trial subspace that we hope approximates it. The trial subspace is the range of an isometry, which the paper calls E zero; the exact wanted subspace is the range of another isometry, F zero. The principal angles between these two subspaces are the natural measure of the approximation error. Orthonormal bases of an exact eigenspace are far from unique, especially when eigenvalues repeat, and an error measure that changed with the basis would be measuring our choices rather than the geometry.

The sine of each principal angle is the length of the part of a principal trial vector that escapes the exact subspace. Collecting the sines into the directed sine operator, the different norms of that operator correspond to different ways of combining the list. The operator norm takes the largest sine. The Frobenius norm takes the square root of the sum of squared sines. The trace norm adds the sines. The Davis–Kahan sine theorem bounds all of these at once, in each case by the corresponding norm of a residual divided by a spectral gap.

To summarize what we have established. Two subspaces of equal finite dimension k have k principal angles in the interval from zero to ninety degrees. Their cosines are the singular values of the overlap matrix of any two orthonormal bases, and so do not depend on those bases. The principal vectors pair up in mutually perpendicular planes, one angle per plane, together with common directions and right-angle directions. Inside each plane the difference of the two projections is the sine of the angle times a reflection, so the operator, Frobenius, and trace norms of that difference are the largest sine, root two times the root sum of squared sines, and twice the sum of the sines. When the dimensions differ, the symmetric difference of projections has norm one, and the directed sine is the meaningful measure.

The finite list is a finite-dimensional luxury. In an infinite-dimensional Hilbert space, the extremes in Jordan's construction need not be attained. Take infinitely many mutually perpendicular planes, and in the n-th plane draw a source line and a target line meeting at an angle of one over n radians. Let the source subspace be the closed span of all the source lines, and the target the closed span of all the target lines. The angles become as small as we like, so the smallest angle should be zero; yet no nonzero vector of the source lies in the target, so no pair of vectors attains it. More generally, the compression of one projection to the other subspace can have continuous spectrum, with no eigenvectors at all. There the list of principal angles is replaced by an angle operator, defined through the same compressions we used here.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Definitions and the main identities

Let \(U,V\) be subspaces of a finite-dimensional real or complex inner-product space \(E\), with \(\dim U=k\le\dim V=l\). Let \(X\in\mathbb K^{n\times k}\), \(Y\in\mathbb K^{n\times l}\) have orthonormal columns spanning \(U\) and \(V\), so \(X^*X=I_k\), \(Y^*Y=I_l\), \(P=XX^*\), \(Q=YY^*\).

- **Principal cosines.** \(\cos\theta_i=\sigma_i(X^*Y)\), \(i=1,\dots,k\), with \(0\le\theta_1\le\dots\le\theta_k\le\pi/2\). Replacing \(X\to XG\), \(Y\to YH\) with \(G,H\) unitary gives \(G^*(X^*Y)H\), which has the same singular values.
- **Jordan's recursion.** \(\cos\theta_1=\max\{|\langle u,v\rangle|: u\in U,\ v\in V,\ \|u\|=\|v\|=1\}\); later angles maximize over vectors orthogonal to the previously chosen principal vectors. This is the variational characterization of the singular values of \(X^*Y\).
- **Principal vectors.** If \(X^*Y=W\Sigma Z^*\), then \(x_i=XWe_i\), \(y_i=YZe_i\) satisfy \(\langle x_i,y_j\rangle=\delta_{ij}\cos\theta_i\). The planes \(\Pi_i=\operatorname{span}\{x_i,y_i\}\) are mutually orthogonal.
- **Compressions.** \(X^*QX=(X^*Y)(X^*Y)^*\) has eigenvalues \(\cos^2\theta_i\); \(X^*(I-Q)X=I-(X^*Y)(X^*Y)^*\) has eigenvalues \(\sin^2\theta_i\). Its square root is the directed sine on \(U\)-coordinates; in the paper's notation \(\sin\Theta_0=(I-E_0^*P_{\mathrm{exact}}E_0)^{1/2}\).
- **Projection difference in a principal plane.** With \(c=\cos\theta\), \(s=\sin\theta\),
  \[
  P-Q=\begin{pmatrix}1&0\\0&0\end{pmatrix}-\begin{pmatrix}c^2&cs\\cs&s^2\end{pmatrix}
  =s\begin{pmatrix}s&-c\\-c&-s\end{pmatrix},
  \]
  and the last matrix is a symmetric orthogonal reflection with eigenvalues \(\pm1\).
- **Norms (equal dimensions).** The nonzero eigenvalues of \(P-Q\) are \(\pm\sin\theta_i\), so
  \(\|P-Q\|_{\mathrm{op}}=\sin\theta_k\), \(\|P-Q\|_F^2=2\sum_i\sin^2\theta_i\), \(\|P-Q\|_1=2\sum_i\sin\theta_i\).
- **Unequal dimensions.** If \(k<l\), some unit \(v\in V\) has \(Pv=0\), so \((P-Q)v=-v\) and \(\|P-Q\|_{\mathrm{op}}=1\). The directed gap \(\|(I-Q)P\|_{\mathrm{op}}=\sin\theta_k\) (largest angle from \(U\) to \(V\)). For \(k=l\), \(\|(I-Q)P\|=\|(I-P)Q\|=\|P-Q\|\).
- **CS form.** For \(0<\theta_i<\pi/2\), \(y_i=\cos\theta_i\,x_i+\sin\theta_i\,w_i\) with \(w_i\in U^\perp\) orthonormal. In the basis \((x_i),(w_i),\dots\), \(Y=\begin{pmatrix}C\\S\\0\end{pmatrix}\) with \(C^2+S^2=I\).

### Running example

\(U=\operatorname{span}\{e_1,e_2\}\subset\mathbb R^4\), \(v_1=\cos30^\circ e_1+\sin30^\circ e_3=(\tfrac{\sqrt3}{2},0,\tfrac12,0)\), \(v_2=\cos60^\circ e_2+\sin60^\circ e_4=(0,\tfrac12,0,\tfrac{\sqrt3}{2})\), \(V=\operatorname{span}\{v_1,v_2\}\).

- For \(u=\cos\varphi\,e_1+\sin\varphi\,e_2\): \(\|Qu\|^2=\tfrac34\cos^2\varphi+\tfrac14\sin^2\varphi\in[\tfrac14,\tfrac34]\); \(\varphi=45^\circ\) gives \(\tfrac12\), angle \(45^\circ\).
- \(X^*Y=\operatorname{diag}(\tfrac{\sqrt3}{2},\tfrac12)\). With the rotated basis \(X'=X\,\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\),
  \(X'^*Y=\tfrac1{\sqrt2}\begin{pmatrix}\sqrt3/2&1/2\\\sqrt3/2&-1/2\end{pmatrix}\), whose singular values are again \(\sqrt3/2,\ 1/2\).
- Principal planes \(\operatorname{span}\{e_1,e_3\}\), \(\operatorname{span}\{e_2,e_4\}\).
- \(\|P-Q\|_{\mathrm{op}}=\tfrac{\sqrt3}{2}\approx0.866\), \(\|P-Q\|_F^2=2\), \(\|P-Q\|_1=1+\sqrt3\approx2.732\).
- With both angles equal to \(\theta\): \(\|P-Q\|_1=4\sin\theta\), the global trace-norm transport minimum in the paper's Proposition 4.4 counterexample (§5 of the journal paper).

**Infinite-dimensional remark.** With orthonormal \(e_n,f_n\), \(U=\overline{\operatorname{span}}\{e_n\}\), \(V=\overline{\operatorname{span}}\{\cos t_n e_n+\sin t_n f_n\}\), \(t_n=1/n\): \(U\cap V=\{0\}\) but \(\inf_n t_n=0\) is not attained. In general \(P Q P|_U\) can have continuous spectrum; the paper then uses the angle operator \(\Theta_0\) defined by functional calculus.

### Lean correspondence

Tau Ceti (pinned revision `a67a65006c07449dcb2ebe1a3a8b6bf6e0b909f8`), `TauCeti/Analysis/InnerProductSpace/Projection/PrincipalAngle.lean`, in `namespace Submodule` with

```lean
variable {𝕜 E : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
variable (U V : Submodule 𝕜 E) [U.HasOrthogonalProjection] [V.HasOrthogonalProjection]

def cosThetaMap : E →L[𝕜] E :=
  V.starProjection ∘L U.starProjection

def sinThetaMap : E →L[𝕜] E :=
  Vᗮ.starProjection ∘L U.starProjection
```

and, under `[FiniteDimensional 𝕜 E]`,

```lean
def principalCosines : ℕ →₀ ℝ :=
  (U.cosThetaMap V : E →ₗ[𝕜] E).singularValues

def principalSines : ℕ →₀ ℝ :=
  (U.sinThetaMap V : E →ₗ[𝕜] E).singularValues

def principalAngles : ℕ →₀ ℝ :=
  (U.principalSines V).mapRange Real.arcsin Real.arcsin_zero

theorem sin_principalAngles (i : ℕ) :
    Real.sin (U.principalAngles V i) = U.principalSines V i

theorem principalSines_zero : U.principalSines V 0 = U.directedProjectionGap V

theorem principalCosines_comm : U.principalCosines V = V.principalCosines U

theorem principalSines_comm (h : finrank 𝕜 U = finrank 𝕜 V) :
    U.principalSines V = V.principalSines U

theorem principalAngles_eq_zero_iff : U.principalAngles V = 0 ↔ U ≤ V
```

For an isometry `X : F →L[𝕜] E` (the frame \(X\) above):

```lean
theorem principalCosines_range_eq_singularValues (hX : Isometry X) :
    X.range.principalCosines V =
      ((V.starProjection ∘L X : F →L[𝕜] E) : F →ₗ[𝕜] E).singularValues

theorem principalSines_range_eq_singularValues (hX : Isometry X) :
    X.range.principalSines V =
      ((Vᗮ.starProjection ∘L X : F →L[𝕜] E) : F →ₗ[𝕜] E).singularValues
```

`TauCeti/Analysis/InnerProductSpace/Projection/Gap.lean`, same namespace and variables:

```lean
def projectionGap : ℝ := ‖U.starProjection - V.starProjection‖
def directedProjectionGap : ℝ := ‖Vᗮ.starProjection ∘L U.starProjection‖

theorem projectionGap_eq_max :
    projectionGap U V = max (directedProjectionGap U V) (directedProjectionGap V U)

theorem projectionGap_eq_directedProjectionGap_of_finrank_eq [FiniteDimensional 𝕜 U]
    [FiniteDimensional 𝕜 V] (h : Module.finrank 𝕜 U = Module.finrank 𝕜 V) :
    projectionGap U V = directedProjectionGap U V
```

Davis–Kahan library, `DavisKahan/FiniteDimensional/DirectRotation/ComplexTracePrincipalAngles.lean`, `namespace TauCeti.DavisKahan.FiniteDimensional.ComplexTraceOptimality`, with `{H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]` (finite-dimensional):

```lean
theorem kyFanSum_projectionDifference_eq_two_sum_sin_principalAngles
    (U V : Submodule ℂ H) [U.HasOrthogonalProjection]
    [V.HasOrthogonalProjection]
    (hUV : finrank ℂ U = finrank ℂ V) :
    (U.starProjection.toLinearMap - V.starProjection.toLinearMap).kyFanSum (finrank ℂ H) =
      2 * ∑ j : Fin (finrank ℂ U), Real.sin (Submodule.principalAngles U V (j : ℕ))
```

**Mapping notes.**

- Tau Ceti defines the angles through singular values of the ambient maps \(P_VP_U\) and \(P_{V^\perp}P_U\), padded with zeros, rather than through \(X^*Y\). The lemmas `principalCosines_range_eq_singularValues` and `principalSines_range_eq_singularValues` give the frame form: \(P_VX\) has the same nonzero singular values as \(Y^*X\).
- **Index convention.** Both lists are nonincreasing. `principalSines V 0` is the largest sine, so `principalAngles U V 0` is the **largest** angle, while `principalCosines U V 0` is the largest cosine, that of the **smallest** angle. The lecture numbers angles increasingly, \(\theta_1\le\dots\le\theta_k\).
- `principalSines_zero` and the definition of `directedProjectionGap` are the statement “largest sine = \(\|(I-Q)P\|\).” `projectionGap_eq_directedProjectionGap_of_finrank_eq` is the equal-dimension identity \(\|P-Q\|=\|(I-Q)P\|\).
- The trace-norm formula \(\|P-Q\|_1=2\sum\sin\theta_i\) is formalized over \(\mathbb C\) as a Ky Fan sum of full length (`kyFanSum … (finrank ℂ H)` is the trace norm).
- The four-dimensional pair with two equal angles, used in the Proposition 4.4 counterexample, has its angles computed in `DavisKahan/FiniteDimensional/DirectRotation/SmallAngleCounterexample.lean` (`SmallAngleCounterexample.principalAngles_eq`).
