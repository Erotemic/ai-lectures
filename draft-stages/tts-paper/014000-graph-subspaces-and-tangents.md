# 014000 — Graph subspaces and tangents

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** tangent-double-angle. **Audience:** principal angles and principal planes, the angle operator, Halmos's form, the direct rotation.

<!-- BEGIN SPOKEN LECTURE -->

Graph subspaces and tangents

The sine of an angle measures how much of a unit vector escapes a subspace. It never exceeds one, so a bound on the sine says nothing once the bound reaches one, and it cannot distinguish an angle of eighty-nine degrees from ninety. The tangent does. This lecture develops the geometry behind the tangent of the angle operator: describing one subspace as the graph of an operator over another, with the tangent of the angle as the slope.

Here is what we will establish. First, a line through the origin in the plane, other than the vertical one, is the graph of multiplication by its slope over the horizontal axis, and the slope is the tangent of its angle. Second, a subspace V is the graph of a bounded operator T from U to the complement of U exactly when the pair is acute in the strong sense that the norm of P minus Q is less than one; then V consists of the vectors u plus T u, for u in U. Third, the singular values of T are the tangents of the principal angles; in Halmos's coordinates T is the sine of the angle times the inverse of its cosine, the tangent of Theta. Fourth, a right angle is exactly what prevents V from being a graph over U, and a bound on the tangent therefore excludes right angles, while a bound on the sine cannot. Fifth, in the Davis–Kahan paper, the directed tangent of Theta zero, and the full tangent of Theta, are built from the blocks of the direct rotation, and their norms agree.

Lines as graphs

In the plane, take U to be the horizontal axis. A line through the origin at angle theta above it, with theta less than ninety degrees, consists of the points x, tangent theta times x. So it is the graph of the map from the horizontal axis to the vertical axis that multiplies by tangent theta. The slope of the line is the tangent of its angle.

At thirty degrees the slope is about zero point five eight. At sixty degrees it is about one point seven three. At eighty-nine degrees it is about fifty-seven. And at ninety degrees, the vertical line, there is no slope: the vertical line is not the graph of any function of the horizontal coordinate, because above the origin there is a whole line of points and above every other horizontal point there are none.

Compare the sines: one half at thirty degrees, about zero point eight seven at sixty, and about zero point nine nine nine eight at eighty-nine. The sine barely changes near ninety degrees. The tangent grows without bound. That is the difference that makes tangent estimates stronger.

Subspaces as graphs

Now let U and V be closed subspaces of a Hilbert space, with projections P and Q. Say V is the graph of an operator T over U if T maps U into the complement of U and V consists exactly of the vectors u plus T u, with u in U. Each vector of V then has a unique decomposition into a part in U and a part in its complement, and the second part is determined by the first through T.

When is this possible with T bounded? Every vector of V must have a nonzero part in U, otherwise it would lie in the complement and could not be written as u plus T u with u nonzero. So no nonzero vector of V may be perpendicular to U. And the parts in U must fill all of U. More quantitatively, the part in U of a unit vector of V must never be too short, or T would have to stretch it into a long part in the complement. Putting these together, V is the graph of a bounded operator over U exactly when the norm of P minus Q is less than one, which is the condition that every angle stays bounded away from ninety degrees.

In finite dimensions, with U and V of the same dimension, the condition simplifies: V is a graph over U exactly when no vector of V is perpendicular to U, that is, exactly when there is no principal angle of ninety degrees.

The slope operator and the tangents of the principal angles

Use the principal-plane picture. For each principal angle theta i, there is a unit vector x i in U, a unit vector w i in the complement of U, and the target principal vector y i equal to cosine theta i times x i plus sine theta i times w i. If cosine theta i is not zero, divide by it: the vector x i plus tangent theta i times w i lies in V. So the slope operator T sends x i to tangent theta i times w i.

The x's are orthonormal and the w's are orthonormal, so this says T has singular values tangent theta i. The slope operator of V over U has the tangents of the principal angles as its singular values, exactly as the sine of the angle operator has their sines.

In the four-dimensional example with angles of thirty and sixty degrees, U is spanned by e one and e two, and V by e one tilted thirty degrees toward e three and e two tilted sixty degrees toward e four. The slope operator sends e one to tangent thirty times e three, and e two to tangent sixty times e four. Its singular values are about zero point five eight and one point seven three, while the sines are one half and about zero point eight seven.

In Halmos's form, the generic part of V consists of the pairs C h, S h, where C and S are the cosine and sine of the generic angle operator. If C is invertible, which on the generic part means the angles stay away from ninety degrees, this is the set of pairs k, S times C inverse times k. So the slope operator on the generic part is S times C inverse: the tangent of Theta, defined by functional calculus. On the common directions the slope is zero.

Right angles obstruct graphs

What exactly fails at a right angle? Suppose some unit vector v of V is perpendicular to U. Then v lies in the complement of U, so its part in U is zero, and if V were the graph of T, v would have to equal zero plus T of zero, which is zero. Contradiction. So V is not a graph over U.

What if no angle equals ninety degrees, but angles approach it, as in an infinite-dimensional example with angles ninety degrees minus one over n radians? Then V is still the set of vectors u plus T u, but only for u in a dense subspace of U, and T is unbounded, because its singular values, the tangents of the angles, grow without limit. The norm of P minus Q is one, the supremum of the sines, even though no right angle is attained.

So a finite bound on the tangent of the angle operator is a strong statement. It says the angles stay uniformly below ninety degrees, the pair is acute in the strong sense, V is the graph of a bounded operator over U, and the direct rotation is given by the Sz.-Nagy–Kato formula. A bound on the sine below one gives the same conclusion, but a bound on the sine equal to or above one gives nothing, while a bound on the tangent is never vacuous: any finite bound excludes right angles.

Converting between the two: if the tangent of the largest angle is at most t, then its sine is at most t divided by the square root of one plus t squared, which is less than both t and one. So a tangent estimate with the same right-hand side as a sine estimate is always stronger.

Tangents in the Davis–Kahan paper

Davis and Kahan express the tangent through the direct rotation. In block form relative to U and its complement, the direct rotation has diagonal blocks cosine Theta zero and cosine Theta one, and crossing block S zero, which equals a partial isometry J zero times sine Theta zero. The directed tangent of Theta zero is sine Theta zero times the inverse of cosine Theta zero, an operator on U, defined when the cosine is invertible. The crossing block times the inverse cosine, S zero times the inverse of C zero, is J zero times tangent Theta zero, which is the slope operator itself, carried into the complement by J zero.

The full tangent of Theta, on the whole space, has off-diagonal blocks J zero times tangent Theta zero and minus J zero star times tangent Theta one, and zero diagonal blocks. Since J zero intertwines Theta zero and Theta one, the two off-diagonal blocks have the same singular values, and the norm of the full tangent equals the norm of the directed tangent. This is the identity Davis and Kahan use to pass from the directed tangent theorem to the full one.

The journal paper adds a precise convention: the full tangent is defined as a bounded operator exactly when the norm of P minus Q is less than one. That is the strong acuteness condition under which V is a bounded graph over U.

Why graphs suit perturbation theory

The graph description turns a question about subspaces into a question about a single operator. The exact spectral subspace of a perturbed operator, when close to the trial subspace, is the graph of a slope operator T over the trial subspace. The invariance of that graph under the perturbed operator becomes an equation for T. That equation is quadratic in T, but its linear part is a Sylvester equation, the same kind that appeared in the sine theorem. The tangent theorem bounds the slope operator directly.

To summarize. A subspace V is the graph of a bounded operator T over U, with V equal to the set of u plus T u, exactly when the norm of P minus Q is less than one. The singular values of T are the tangents of the principal angles, and on Halmos's generic part T is S times C inverse, the tangent of the angle operator. Right angles prevent V from being a graph, and angles approaching ninety degrees make the slope unbounded. A tangent bound is never vacuous and is always at least as strong as the corresponding sine bound. In the paper, the directed tangent is sine Theta zero times the inverse cosine, the slope operator is the crossing block of the direct rotation times the inverse cosine, and the full tangent has the same norm as the directed one.

The price of the stronger conclusion is a stronger hypothesis. A tangent estimate must exclude right angles, so it cannot hold under hypotheses that allow them; the tangent theorem needs an ordered gap and the Rayleigh–Ritz condition, where the sine theorem needed neither.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Graph subspaces

\(V=\{u+Tu:u\in U\}\), \(T:U\to U^\perp\) bounded \(\iff\|P-Q\|<1\). Finite equal dimensions: \(\iff V\cap U^\perp=\{0\}\).
Principal planes: \(y_i=\cos\theta_ix_i+\sin\theta_iw_i\Rightarrow x_i+\tan\theta_iw_i\in V\), \(Tx_i=\tan\theta_iw_i\), \(s_i(T)=\tan\theta_i\).
Halmos: \(V_{\rm gen}=\{(Ch,Sh)\}=\{(k,SC^{-1}k)\}\), \(T=SC^{-1}=\tan\Theta\).
Example (\(30^\circ,60^\circ\)): \(Te_1=\tan30^\circ e_3\approx0.577e_3\), \(Te_2=\tan60^\circ e_4\approx1.732e_4\).
\(\tan\theta\le t\Rightarrow\sin\theta\le t/\sqrt{1+t^2}<\min(t,1)\).

### Davis–Kahan (6.2)

\[
U_{\rm dr}\sim\begin{pmatrix}\cos\Theta_0&-J_0^*\sin\Theta_1\\J_0\sin\Theta_0&\cos\Theta_1\end{pmatrix},\quad J_0\Theta_0=\Theta_1J_0,
\]
\[
\tan\Theta\sim\begin{pmatrix}0&-J_0^*\tan\Theta_1\\J_0\tan\Theta_0&0\end{pmatrix},\qquad\|J_0\tan\Theta_0\|=\|J_0^*\tan\Theta_1\|=\|\tan\Theta_0\|.
\]
Journal paper, Appendix B: the ambient tangent is a bounded operator iff \(\|P_U-Q_V\|_{\rm op}<1\).

### Lean correspondence

The directed tangent is built from the trial-coordinate angle `sourceDirectedThetaOperator` (`DavisKahan/Sources/DavisKahan1970/SineTheta/Presentation.lean`) by continuous functional calculus; the tangent theorems are inventoried under `S2-tan-theta` and `DK-6.3-thm` in `dev/davis-kahan-1970-formalization-result-inventory.json`.
