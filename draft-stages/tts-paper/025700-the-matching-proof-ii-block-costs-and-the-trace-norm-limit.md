# 025700 — The matching proof, II: block costs and the trace-norm limit

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** transport. **Audience:** the matching theorem statement; part one of its proof, which splits a minimizer into one-angle and two-angle blocks; planar rotations and reflections.

<!-- BEGIN SPOKEN LECTURE -->

The matching proof, part two: block costs and the trace-norm limit

The first half of the proof showed that a global minimizer of the smoothed cost, the sum of the p-th powers of the displacement singular values with p between one and two, splits into perpendicular blocks: fixed directions, planes carrying one principal angle, and four-dimensional blocks carrying two. This lecture finishes the proof. We compute the cheapest transporter on a one-angle plane and on a two-angle block, show that the minimum over transporters equals the minimum over matchings for the smoothed cost, and then let p decrease to one to recover the trace norm, where the block costs become the singleton costs and pair costs of the theorem.

Here is what we will establish. Step four: on a one-angle plane the cheapest choice is the shorter of rotating through the angle and reflecting. On a two-angle block, every transporter is the block's direct rotation followed by a pair of planar orthogonal maps; those with determinant one have their cost governed by a single parameter r between the half-difference h and the half-sum m of the two angles, with cost twice phi of m plus r plus twice phi of m minus r, where phi of t is two sine of t over two to the power p; those with determinant minus one reflect one plane and rotate the other. Step five: every matching gives a transporter with the matching's cost, and every minimizer gives a matching with its cost, so the two minima are equal. Step six: as p decreases to one, all costs converge uniformly; the one-angle minimum becomes the minimum of four sine of theta over two and two, and the two-angle expression becomes eight sine of m over two times cosine of r over two, which is smallest at r equal to m, giving four sine m, the pair cost.

Step four, part one: a single angle

A block carrying one principal angle theta is a plane containing a source line and a target line at angle theta. Its transporters are the planar orthogonal maps carrying one line to the other: two rotations and two reflections.

The shorter rotation turns through theta. Its displacement has two equal singular values, two sine of theta over two, so its smoothed cost is twice phi of theta. The longer rotation turns through one hundred eighty degrees minus theta, which is at least theta, and since phi increases on the interval from zero to one hundred eighty degrees, it costs at least as much.

A reflection carrying the source line to the target line has eigenvalues plus one and minus one, so its displacement has singular values zero and two, and its smoothed cost is two to the p.

So the one-angle minimum, call it a of p, is the smaller of twice phi of theta and two to the p.

Step four, part two: two angles, determinant one

Now a four-dimensional block with two principal angles, theta i at least theta j. Let m be their half-sum and h their half-difference. Then h is between zero and m, and m plus h, which is theta i, is at most ninety degrees.

In principal coordinates, the block's direct rotation has diagonal blocks C, the diagonal matrix of cosines, and off-diagonal blocks S and minus S, with S the diagonal matrix of sines. Every transporter on the block is this direct rotation followed by a map that preserves the source plane and its complement, that is, a pair of planar orthogonal maps U zero and U one. This parametrization allows the two principal planes to mix.

Suppose the transporter has determinant one. Then U zero and U one are both rotations or both reflections. Its eigenvalues come in conjugate pairs, and a calculation with the trace and the trace of the square determines them. Writing the two rotation angles of U zero and U one as r plus s and r minus s, one defines two angles x and y by cosine formulas. For two rotations, cosine x is cosine m times cosine s, and cosine y is cosine h times cosine r. The eigenvalues of the transporter are then e to the plus or minus i times x plus y, and e to the plus or minus i times x minus y. The case of two reflections has analogous formulas.

The characteristic polynomial makes this precise. Because the transporter is orthogonal with determinant one, its characteristic polynomial is reciprocal, and it factors into two quadratics whose roots are exactly those conjugate pairs. The displacement cost is therefore twice phi of x plus y, folded into the interval up to one hundred eighty degrees, plus twice phi of the absolute value of x minus y.

The cosine formulas constrain x and y. They force x to lie between m and one hundred eighty degrees minus m, and y between h and one hundred eighty degrees minus h. Using those constraints and the fact that phi is increasing, one shows that the cost is at least twice phi of m plus r tilde, plus twice phi of m minus r tilde, for some r tilde between h and m. And every such r tilde is attained, by taking U zero and U one to be the same rotation, through an angle whose cosine is cosine r tilde divided by cosine h.

So the determinant-one minimum on a two-angle block is the minimum, over r tilde between h and m, of twice phi of m plus r tilde plus twice phi of m minus r tilde. Call it b of p.

The two ends of the interval have clear meanings. At r tilde equal to h, the two phases are m plus h and m minus h, which are theta i and theta j: this is the direct rotation, each plane rotated separately, with cost twice phi of theta i plus twice phi of theta j. At r tilde equal to m, the phases are two m, which is theta i plus theta j, and zero: the transporter fixes two directions and rotates the other two through the sum of the angles. That is the pair transporter, generalizing the competitor in the Proposition 4.4 counterexample. Values of r tilde in between interpolate.

Step four, part three: two angles, determinant minus one

If the transporter has determinant minus one, then one of U zero and U one is a rotation and the other a reflection, and the eigenvalues are plus one, minus one, and a conjugate pair e to the plus or minus i t. The trace of such a transporter is at most twice cosine theta j in absolute value, while the trace equals two cosine t, so t is at least theta j. The cheapest such transporter costs two to the p, for the minus one, plus twice phi of theta j, for the rotation pair, and it is attained by reflecting the larger-angle plane and rotating the smaller-angle plane.

Combining the cases, the unrestricted minimum on a two-angle block is the smaller of b of p and the sum of the two one-angle minima, a i of p plus a j of p. The endpoint r tilde equal to h gives two rotations, the determinant minus one case gives one reflection and one rotation, and two reflections cost at most twice two to the p; each of these is a pair of independent singleton choices, and none beats the smaller of the paired cost and the two separate singleton minima. So a four-dimensional block offers either a genuine pairing, at cost b of p, or two independent singletons.

Step five: equal minima

Define the cost of a matching, for the exponent p, as the sum of b of p over its pairs plus the sum of a of p over its unmatched labels.

First, every matching gives a transporter with exactly that cost. Use the principal-angle decomposition: mutually perpendicular principal planes for the positive angles. On the sum of the two planes of each matched pair, place an optimal pair transporter. On the plane of each unmatched label, place the cheaper of the rotation and the reflection. On common directions and everything else, use the identity. The result carries K onto L, and by additivity its cost is the matching's cost.

Second, every global minimizer gives a matching with its cost. By part one of the proof, the minimizer splits into fixed directions, one-angle planes, and two-angle blocks. On each block, it must be an optimal transporter for that block's own angles; otherwise, replacing it on that block alone would keep it feasible and lower the total cost. By step four, each plane contributes a singleton cost, and each four-dimensional block contributes either a pair cost or two singleton costs. Each angle label occurs in exactly one block, so no label is used twice: this is a matching, and its cost equals the minimizer's cost.

One detail: could pairing a positive angle with a zero angle, a common direction, ever help? Pairing theta with zero gives h equal to m equal to theta over two, and the paired cost becomes twice phi of theta, which is at least the singleton cost. So zero angles never help, and only the positive labels need be matched.

The two inequalities together give: for each p between one and two, the minimum over feasible transporters of the smoothed cost equals the minimum over matchings of the smoothed matching cost.

Step six: the trace-norm limit

Finally let p decrease to one. Every displacement singular value lies between zero and two. On that interval, s to the p converges to s uniformly as p decreases to one. So for every feasible transporter, the smoothed cost differs from the trace norm by at most n times the largest difference between s to the p and s on the interval, which tends to zero, uniformly over transporters. Hence the minimal smoothed cost converges to the minimal trace norm.

The block costs converge too. The one-angle minimum, the smaller of twice phi of theta and two to the p, converges to the smaller of four sine of theta over two and two, which is the singleton cost s i of the theorem. For the pair, at p equal to one, twice phi of m plus r tilde, plus twice phi of m minus r tilde, is four sine of half of m plus r tilde, plus four sine of half of m minus r tilde. By the sum-to-product identity, that equals eight sine of m over two times cosine of r tilde over two. As r tilde increases from h to m, cosine of r tilde over two decreases, so the expression is smallest at r tilde equal to m, where it equals eight sine of m over two times cosine of m over two, which is four sine m, the pair cost e i j. The minimum of a continuous function over the fixed interval from h to m converges as the function converges uniformly, so b of p converges to e i j.

There are only finitely many matchings, so the minimum over matchings converges as well. Taking the limit on both sides of the equality from step five gives the matching theorem: the minimum trace norm of the displacement, over real orthogonal maps carrying K onto L, equals the minimum over matchings of the pair costs four sine of half the sum of the angles plus the singleton costs, the minimum of four sine of half the angle and two. Compactness of the feasible set provides an attaining transporter for the trace norm itself.

Why the endpoint is a pair map

At p equal to one, the best r tilde is the largest possible, m, which concentrates all of the motion of the block into one rotation plane through the sum of the angles and leaves the other plane fixed. This is the trace norm's preference for zero singular values, the same preference that makes the trace norm favor sparse solutions in other settings. For exponents above one the optimum r tilde can be interior, which is why the smoothed problem has smooth critical points while the trace-norm problem does not, and why the proof works with p above one and passes to the limit.

To summarize. On a one-angle plane the cheapest transport is the shorter rotation or a reflection. On a two-angle block, transporters are the direct rotation followed by two planar maps; with determinant one their cost is twice phi of m plus r tilde plus twice phi of m minus r tilde for some r tilde between the half-difference and the half-sum, attained for every such value, with r tilde equal to h the direct rotation and r tilde equal to m the pair transporter; with determinant minus one they reflect one plane and rotate the other. Every matching yields a transporter of the same cost, and every minimizer, having been split into blocks, yields a matching of the same cost, so the minima agree for each p. Letting p decrease to one, the costs converge uniformly, the pair expression becomes eight sine of m over two cosine of r tilde over two, minimized at r tilde equal to m with value four sine m, and the matching formula follows.

The proof establishes the value of the minimum and an attaining transporter. Computing the best matching for a given list of angles is then a finite combinatorial problem, and the theorem says nothing about it beyond its formulation as maximum-weight matching.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Step 4

\(\varphi(t)=(2\sin\tfrac t2)^p\). One angle: \(a_i(p)=\min\{2\varphi(\theta_i),2^p\}\).
Two angles, \(\theta_i\ge\theta_j\), \(m=\tfrac{\theta_i+\theta_j}2\), \(h=\tfrac{\theta_i-\theta_j}2\): \(D=\begin{pmatrix}C&-S\\S&C\end{pmatrix}\), \(W=D\operatorname{diag}(U_0,U_1)\), \(U_0,U_1\in O(2)\).

| case | \(\cos x\) | \(\cos y\) |
|---|---|---|
| two rotations (angles \(r\pm s\)) | \(\cos m\cos s\) | \(\cos h\cos r\) |
| two reflections | \(-\sin h\cos r\) | \(\sin m\cos s\) |

\(\operatorname{tr}W=4\cos x\cos y\), \(\det(zI-W)=\prod_{\epsilon=\pm1}(z^2-2\cos(x+\epsilon y)z+1)\); cost \(2(\varphi(\min\{x+y,2\pi-x-y\})+\varphi(|x-y|))\).
\[
b_{ij}(p)=\min_{\tilde r\in[h,m]}2\bigl(\varphi(m+\tilde r)+\varphi(m-\tilde r)\bigr),\quad\text{attained by }U_0=U_1=R_\gamma,\ \cos\gamma=\cos\tilde r/\cos h .
\]
Determinant \(-1\): \(|\operatorname{tr}W|\le2\cos\theta_j\Rightarrow t\ge\theta_j\); minimum \(2^p+2\varphi(\theta_j)\). Unrestricted block minimum \(\min\{b_{ij}(p),a_i(p)+a_j(p)\}\).

Numerical check (brute force over two planar rotations): \((50^\circ,20^\circ)\), \(p=1.5\): \(1.9635\); \(p=1\): \(2.2943=4\sin35^\circ\).

### Steps 5–6

\(\min_{\mathcal F}\Phi_p=\min_M\bigl(\sum_{M}b_{ij}(p)+\sum_{\rm unmatched}a_i(p)\bigr)\), \(1<p<2\).
\(\sup_W|\Phi_p(W)-\|I-W\|_1|\le n\sup_{0\le s\le2}|s^p-s|\to0\).
\(p=1\): \(2(\varphi(m+\tilde r)+\varphi(m-\tilde r))=8\sin\tfrac m2\cos\tfrac{\tilde r}2\), minimized at \(\tilde r=m\): \(4\sin m=e_{ij}\); \(a_i(1)=s_i\).

### Lean correspondence

`DavisKahan/FiniteDimensional/DirectRotation/`: `RealFourCoordinates.lean`, `RealFourPositive.lean`, `RealFourOptimization.lean` (all two-angle competitors and the scalar edge reduction); `SchattenRealAngleCosts.lean` (angle costs); `SchattenRealMatchingWeights.lean`, `RealMatchingAttainment.lean` (matching and attainment; `exists_minimizing_real_schatten_transport_matching`); `RealNuclearMatching.lean` (endpoint, `exists_minimizing_real_nuclear_transport_matching`).
