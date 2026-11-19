# 018000 — Basis square sums of sines

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** the transport problem and restricted displacement; principal angles and the angle operator; the Hilbert–Schmidt norm.

<!-- BEGIN SPOKEN LECTURE -->

Basis square sums of sines

Proposition 4.1 measured how far each source vector moves, by the chord between the vector and its image. Proposition 4.2 of the Davis–Kahan paper measures something slightly different: the sine of the angle through which each vector turns, squared and summed over an orthonormal basis of the source subspace. The result is a clean lower bound that holds for every transporter and every basis, and its proof is a short trace calculation. It also shows a distinction that will matter when we reach the full displacement: the sine of a turning angle cannot tell turning a vector from turning its line.

Here is what we will establish. Proposition 4.2: for every unitary W carrying U onto V, and every orthonormal basis v one, v two, and so on, of U, the sum over k of the squared sine of the angle between v k and W v k is at least the sum of the squared sines of the principal angles, including the case where that sum is infinite. The proof has two steps. For each unit source vector v, the squared sine of the angle between v and W v is at least the squared length of the part of v outside V. And summing the squared length of that part over any orthonormal basis gives the same answer, the squared Hilbert–Schmidt norm of the sine of Theta zero, because it is a trace. The direct rotation, with the principal basis, attains the bound. So does any transporter that turns each principal vector through either theta or one hundred eighty degrees minus theta, which shows what this measure cannot see.

The angle between a vector and its image

For nonzero vectors x and y, Davis and Kahan define the angle between them as the arc cosine of the real part of the inner product of x with y, divided by the product of their lengths. This angle lies between zero and one hundred eighty degrees. It is the angle between vectors, not lines: x and minus x are at one hundred eighty degrees. This convention keeps the law of cosines, the squared length of x plus y equal to the squared length of x plus the squared length of y plus twice the product of lengths times the cosine of the angle.

The sine squared of that angle is one minus the squared cosine. Notice that sine squared does not distinguish an angle phi from one hundred eighty degrees minus phi: both have the same squared sine. So the squared sine of the angle between v and W v is small both when W v is close to v and when W v is close to minus v.

Step one: one vector

Let v be a unit vector in U and W a transporter, so W v is a unit vector in V. The cosine of the angle between v and W v is the real part of their inner product, which is at most the absolute value of the inner product. Since W v lies in V, the inner product of v with W v equals the inner product of Q v with W v, which by the Cauchy–Schwarz inequality is at most the length of Q v.

So the squared cosine is at most the squared length of Q v, and the squared sine is at least one minus the squared length of Q v. That last quantity is the squared length of the part of v perpendicular to V, the identity minus Q, applied to v. In words: however W carries v into V, the squared sine of its turning angle is at least the squared length of the part of v that does not lie in V.

This argument works even when the turning angle is more than ninety degrees, because it bounds the absolute value of the cosine, not the angle.

Step two: summing over a basis

Now add over an orthonormal basis v one, v two, and so on, of U. The sum of the squared sines is at least the sum of the squared lengths of the identity minus Q, applied to v k.

That sum does not depend on which orthonormal basis of U we use. The squared length of the identity minus Q, applied to v k, is the inner product of v k with P times the identity minus Q, times P, applied to v k. Summing such diagonal entries over an orthonormal basis gives the trace of the operator P times the identity minus Q, times P, restricted to U. That operator is the sine squared of Theta zero, so the trace is the sum of the squared sines of the principal angles, when there is a list of them, and in general the squared Hilbert–Schmidt norm of the sine of Theta zero. A trace of a positive operator is the same in every orthonormal basis.

Putting the steps together: for every transporter W and every orthonormal basis of U, the sum of the squared sines of the turning angles is at least the sum of the squared sines of the principal angles. If the sine of Theta zero is not Hilbert–Schmidt, both sides are infinite, and the inequality still holds in the extended sense.

When equality holds

For the direct rotation and the basis of principal vectors, each principal vector u k is turned through exactly theta k, onto its partner in V. So its squared sine is sine squared theta k, and the sum is the sum of the squared sines of the principal angles: equality.

But the direct rotation is not the only transporter that achieves equality. In the plane, with U the horizontal axis and V the line at angle theta, the rotation through theta plus one hundred eighty degrees sends the horizontal unit vector to the opposite end of V, turning it through one hundred eighty minus theta. Its squared sine is sine squared theta, the same as for the short rotation. The reflection across the bisecting line also achieves it. As far as the squared sine of turning angles is concerned, these maps are equally good, even though the long rotation moves the horizontal unit vector by a chord of two cosine of theta over two, much more than the short rotation's two sine of theta over two.

So squared sines of turning angles measure how far each vector's line turns, not how far the vector travels. Lines are what subspaces are made of, and for that reason the squared sine is a natural measure of subspace error. For measuring the motion of a map, chords, the singular values of the identity minus W, are the natural measure, and with chords the direct rotation is distinguished from the long rotation.

The four-dimensional example

With principal angles thirty and sixty degrees, the sum of squared sines of the principal angles is one quarter plus three quarters, which is one. Any transporter, and any orthonormal basis of the source plane, gives a sum of squared sines of turning angles of at least one. For example, take the basis e one plus e two over root two, and e one minus e two over root two, and the direct rotation. Each basis vector has a fraction of its length in each principal plane, and its turning angle is the angle whose cosine is the average of cosine thirty and cosine sixty, about forty-six point nine degrees, with squared sine about zero point five three. The sum over the two basis vectors is about one point zero seven, which is at least one, as the proposition requires. With the principal basis the sum is exactly one.

Why the result is useful

Proposition 4.2 gives a bound with no choice of norm and no choice of basis. In a computation, one often has some orthonormal basis of an approximate eigenspace and some way of matching it to the exact eigenspace. The proposition says that no matching can make the total squared sine of the individual vector errors smaller than the squared Hilbert–Schmidt norm of the sine of the angle between the subspaces. The subspace error is a floor under every vector-by-vector error.

To summarize. For every transporter W and every orthonormal basis of the source subspace, the sum of squared sines of the angles between the basis vectors and their images is at least the sum of squared sines of the principal angles. Each term is at least the squared length of the part of the basis vector outside the target, by Cauchy–Schwarz, and the sum of those squared lengths over any orthonormal basis is a trace, equal to the squared Hilbert–Schmidt norm of the sine of Theta zero. The direct rotation with the principal basis attains the bound, but so do maps that turn vectors the long way, because the squared sine of an angle does not distinguish phi from one hundred eighty degrees minus phi.

Squared sines see lines rather than vectors. A statement about how far a transporter moves vectors, in every unitarily invariant norm, has to be made with the displacement itself, and there the comparison between transporters becomes more delicate.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Proposition 4.2

Angle (1.14): \(\angle(x,y)=\arccos\dfrac{\operatorname{Re}\langle x,y\rangle}{\|x\|\|y\|}\in[0,\pi]\).

For every transporter \(W\) (\(WPW^*=Q\)) and orthonormal basis \(\{v_k\}\) of \(U\):
\[
\sum_k\sin^2\angle(v_k,Wv_k)\ \ge\ \sum_k\sin^2\theta_k\quad(=\|\sin\Theta_0\|_{\rm HS}^2,\ \text{possibly }\infty).
\]
Proof: \(\cos^2\angle(v,Wv)\le|\langle Qv,Wv\rangle|^2\le\|Qv\|^2\Rightarrow\sin^2\angle(v,Wv)\ge\|(I-Q)v\|^2\); \(\sum_k\|(I-Q)v_k\|^2=\operatorname{tr}\bigl(P(I-Q)P|_U\bigr)=\operatorname{tr}\sin^2\Theta_0\) (basis independent).

Equality: \(U_{\rm dr}\) with the principal basis; also transporters turning principal vectors through \(\pi-\theta_k\).

Example (\(30^\circ,60^\circ\)), basis \((e_1\pm e_2)/\sqrt2\), direct rotation: \(\cos\phi=\tfrac12(\cos30^\circ+\cos60^\circ)\approx0.683\), \(\sin^2\phi\approx0.534\), sum \(\approx1.067\ge1\).

### Lean correspondence

`namespace TauCeti.DavisKahan1970`: `proposition4_2_compact_nonacute`, `proposition4_2_compact_nonacute_real`, `proposition4_2_infiniteDimensional`, and the series inequality `tsum_displacementAngleSineSqR_ge_tsum_sq_sin_principalAngleSequence` (`dev/davis-kahan-1970-formalization-result-inventory.json`, `DK-4.2-prop`).
