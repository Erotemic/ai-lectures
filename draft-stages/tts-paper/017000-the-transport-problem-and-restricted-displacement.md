# 017000 — The transport problem and restricted displacement

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** principal angles and the direct rotation; Ky Fan norms and dominance; min-max for singular values.

<!-- BEGIN SPOKEN LECTURE -->

The transport problem and restricted displacement

The perturbation theorems measure how far apart two subspaces are. Section 4 of the Davis–Kahan paper asks a different question about the same geometry: among all unitary maps that carry one subspace onto another, which moves things least? The direct rotation is the natural candidate. The answer depends on what is measured, and this is where the paper's correction and its matching theorem live. This lecture sets up the problem and proves the first and cleanest optimality result: the direct rotation minimizes the displacement of source vectors, in every unitarily invariant norm.

Here is what we will establish. First, the transport problem: a transporter is a unitary map W of the whole space with W P W star equal to Q, carrying the source subspace U onto the target V; every transporter is the direct rotation followed by a unitary that preserves U and its complement. Second, the displacement of a vector x is x minus W x, and for a unit vector its length is twice the sine of half the angle through which x moves. Third, Davis and Kahan compare three ways of measuring a transporter: the restricted displacement, the identity minus W, times P, which only tests source vectors; the squared full displacement; and the full displacement, the identity minus W, on the whole space. Fourth, Proposition 4.1: for every transporter, and every k, there are k orthonormal source vectors each moved through at least the k-th largest principal angle; equivalently, the k-th singular value of the restricted displacement is at least twice the sine of half the k-th principal angle, with equality for the direct rotation. Fifth, Corollary 4.1: the direct rotation minimizes every unitarily invariant norm of the restricted displacement.

Transporters

Let U and V be closed subspaces with projections P and Q, with U and V of the same dimension, and their complements of the same dimension. A transporter is a unitary map W of the whole space carrying U onto V, which is the same as W P equals Q W, or W P W star equals Q. It then also carries the complement of U onto the complement of V.

There are many transporters. If W is one and Z is any unitary that maps U onto itself, then W times Z is another, because Z first rearranges U within itself and W then carries it to V. Conversely, if W is a transporter and D is the direct rotation, then D inverse times W carries U back onto U, so W equals D times a unitary Z preserving U. Such a Z is block diagonal: a unitary Z zero on U and a unitary Z one on the complement. So the transporters are exactly the direct rotation composed with an arbitrary pair of unitaries, one acting within U and one within its complement.

Measuring motion

For a unit vector x, W x is another unit vector, and the displacement is the vector x minus W x. Its squared length is two minus twice the real part of the inner product of x with W x, which is two minus two cosine of the angle between x and W x. By the half-angle formula, that is four sine squared of half the angle. So a unit vector turned through angle phi is displaced by a chord of length two sine of phi over two. Turning through ninety degrees moves a unit vector by root two; turning through one hundred eighty degrees, to its negative, moves it by two.

Davis and Kahan measure the motion of a whole transporter in three ways.

The restricted displacement, the identity minus W, composed with P, records how far each source vector moves. Vectors perpendicular to U are ignored.

The full displacement, the identity minus W, records how far every vector of the space moves, including vectors in the complement of U.

The squared full displacement, the identity minus W, star, times the identity minus W, is a positive operator whose eigenvalues are the squares of the singular values of the full displacement.

Each is measured by a unitarily invariant norm, and the question is which transporter minimizes it. For the restricted displacement and for the squared full displacement, the direct rotation wins in every unitarily invariant norm. For the unsquared full displacement it does not, and that is the subject of the paper's Proposition 4.4 and of its correction.

A planar example

In the plane, let U be the horizontal axis and V the line at angle theta above it, and compare three transporters. The rotation through theta moves the horizontal unit vector through theta, a chord of two sine of theta over two. The reflection across the bisecting line, at angle theta over two, also sends the horizontal unit vector to the unit vector on V at angle theta, so on U it does exactly what the rotation does: same restricted displacement. The rotation through theta plus one hundred eighty degrees sends the horizontal unit vector to the opposite unit vector on V, a turn of one hundred eighty minus theta, with chord two cosine of theta over two, which is larger.

So on the source subspace the rotation and the reflection tie, and the long rotation loses. The restricted displacement has more than one minimizer, because it does not see what happens off U. The rotation and reflection differ on the vertical axis: the rotation turns it through theta, while the reflection turns it through one hundred eighty minus theta. That difference will matter for the full displacement.

Proposition 4.1

Let the principal angles be theta one at least theta two at least theta three, and so on, in decreasing order. In infinite dimensions Davis and Kahan assume the angle data are compact, so that this list exists. Proposition 4.1 says: for every transporter W, there are orthonormal source vectors v one, v two, and so on, such that the angle between v k and W v k is at least theta k, for every k. Equivalently, the k-th largest singular value of the restricted displacement of W is at least two sine of theta k over two, and for the direct rotation it equals two sine of theta k over two exactly.

The second form follows from the min-max principle. The k-th singular value of the restricted displacement is the smallest possible value, over subspaces Y of U of dimension k minus one, of the largest displacement of a unit vector of U perpendicular to Y. So it suffices to bound the displacement of individual unit source vectors from below.

Here is the key geometric fact. A unit source vector x is carried by W to a unit vector of V. The angle between x and any unit vector of V is at least the angle between x and the subspace V, because the closest unit vector of V to x is its normalized projection, Q x divided by the length of Q x. So W can never move x through less than the angle from x to V, and the displacement of x is at least two sine of half that angle.

The angle from x to V is controlled by the angle operator: its cosine is the length of Q x, and the squared length of Q x is the quadratic form of cosine squared Theta zero at x. Running the min-max principle on this quadratic form gives exactly the principal angles: whatever subspace Y of dimension k minus one we remove, some unit vector of U perpendicular to Y makes an angle of at least theta k with V, and the best choice of Y brings that largest remaining angle down to exactly theta k. Combining, the k-th singular value of the restricted displacement is at least two sine of theta k over two.

For the direct rotation there is equality. The direct rotation turns each principal source vector u k through exactly theta k, onto its partner in V, so the displacement of u k is two sine of theta k over two. The displaced vectors for different k lie in different principal planes and are perpendicular. So the singular values of the restricted displacement of the direct rotation are exactly two sine of theta k over two.

Corollary 4.1

Since every singular value of the restricted displacement of an arbitrary transporter is at least the corresponding singular value for the direct rotation, every Ky Fan sum is at least the corresponding sum, and by Ky Fan dominance, every unitarily invariant norm of the restricted displacement is at least the corresponding norm for the direct rotation. That is Corollary 4.1: the direct rotation minimizes the restricted displacement in every unitarily invariant norm.

In the four-dimensional example with principal angles of sixty and thirty degrees, the restricted displacement of the direct rotation has singular values two sine thirty degrees, which is one, and two sine fifteen degrees, about zero point five two. Any other transporter moves some unit source vector by at least one, and moves some source vector perpendicular to that one by at least zero point five two in the best case.

Where this comes from

Chandler Davis established extremal properties of the direct rotation in his 1958 paper on the separation of two linear subspaces, including the Hilbert–Schmidt case and finite-dimensional Schatten norms with exponent at least two. The 1970 paper by Davis and Kahan proves the singular-value minimality of the restricted displacement, which gives every unitarily invariant norm at once. Both results hold without assuming the pair is acute, under the compact angle hypothesis and the standing equal-defect assumption.

To summarize. Transporters from U to V are the direct rotation followed by a unitary preserving U and its complement. A unit vector turned through angle phi is displaced by two sine of phi over two. Since every transporter carries a unit source vector x to a unit vector of V, it moves x through at least the angle from x to V, and the min-max principle turns this into singular-value bounds: the k-th singular value of the restricted displacement is at least two sine of half the k-th principal angle, with equality for the direct rotation. By Ky Fan dominance, the direct rotation minimizes every unitarily invariant norm of the restricted displacement.

The restricted displacement only tests source vectors. In the plane, the reflection across the bisector ties with the rotation on the source line and differs from it on the perpendicular line. Questions about the whole space are different questions, and the next quantities, the squared and unsquared full displacements, see the difference.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Setup

Transporters: unitary \(W\) with \(WPW^*=Q\); \(W=U_{\rm dr}(Z_0\oplus Z_1)\). Chord: \(\|x-Wx\|^2=2-2\operatorname{Re}\langle x,Wx\rangle=4\sin^2(\varphi/2)\).
Objectives: restricted \((I-W)P\); squared full \((I-W)^*(I-W)\); full \(I-W\).

Plane: rotation \(\theta\) and reflection across \(\theta/2\) both send \(e_1\mapsto(\cos\theta,\sin\theta)\) (restricted displacement \(2\sin(\theta/2)\)); rotation \(\theta+\pi\): \(2\cos(\theta/2)\).

### Proposition 4.1 and Corollary 4.1

Compact angle data, \(\theta_1\ge\theta_2\ge\dots\). For every transporter \(W\): orthonormal \(v_k\in U\) with \(\angle(v_k,Wv_k)\ge\theta_k\); equivalently \(\lambda_k((I-W)|_U)\ge2\sin(\theta_k/2)\), equality for \(W=U_{\rm dr}\).
\[
\lambda_k=\inf_{\dim\mathcal Y=k-1}\ \sup_{x\in U\ominus\mathcal Y,\|x\|=1}\|(I-W)x\|\quad(4.1),\qquad \angle(x,Wx)\ge\arccos\|Qx\|\quad(4.2).
\]
Corollary 4.1: \(N((I-U_{\rm dr})P)\le N((I-W)P)\) for every unitarily invariant \(N\).
Example (\(60^\circ,30^\circ\)): \(2\sin30^\circ=1\), \(2\sin15^\circ\approx0.518\).

### Lean correspondence

All in `namespace TauCeti.DavisKahan1970` (`dev/davis-kahan-1970-formalization-result-inventory.json`):

- Proposition 4.1: `proposition4_1_compact_nonacute_complex`, `proposition4_1_compact_nonacute_real`, `proposition4_1_compact_nonacute_directRotationValues_complex`.
- Corollary 4.1: `corollary4_1_compact_nonacute_complex`, `corollary4_1_compact_nonacute_real`, `corollary4_1_infiniteDimensional_nonacute`, `corollary4_1_compact_nonacute_symmetricNorming_complex`.

The names record the scope: compact angle data, no acuteness assumption.
