# 072500 — Weak, strong, and uniform convergence in Hilbert spaces

**Draft status:** audio-first mathematical lecture. **Prerequisites:** Hilbert spaces, orthogonal projections, and bounded operators. **Related:** `072000` infinite-dimensional examples, `082000` spectral cutoffs, `091500` strong resolvent convergence.

<!-- BEGIN SPOKEN LECTURE -->

# Three ways a sequence can approach its limit

A sequence of vectors may look smaller and smaller when tested against any fixed direction, while never becoming shorter. A sequence of operators may give increasingly accurate answers for each fixed vector, while its worst-case error never decreases. These two observations force us to distinguish several meanings of convergence in Hilbert space.

Start with the space of square-summable sequences. Its vectors are infinite lists of numbers whose squares have finite sum. The length of a vector is the square root of that sum. The first coordinate direction has one in its first position and zero elsewhere. The second coordinate direction has one in its second position, and so on. Call the direction in position n the n-th basis vector.

Every one of these basis vectors has length one. The sequence of basis vectors therefore never approaches zero in length. Yet for any single fixed square-summable vector, its inner product with the n-th basis vector approaches zero. The inner product simply reads off the n-th coordinate, and the coordinates of a square-summable vector must approach zero. We have found convergence detected by inner products, without convergence detected by lengths.

## Weak convergence of vectors

A sequence of vectors converges weakly to x if, for every fixed test vector y, the inner products of the sequence members with y approach the inner product of x with y. The order of quantifiers is important. Choose y once; then allow n to increase. There is no demand that the convergence happen uniformly over every unit test vector.

Convergence in norm is stronger: the lengths of the differences from x approach zero. The Cauchy–Schwarz inequality shows why norm convergence implies weak convergence. The absolute inner product of a difference with y is at most the length of that difference times the length of y.

Our coordinate example shows the converse fails in infinite dimensions. Each basis vector is weakly convergent to zero, since its inner product with every fixed test vector tends to zero, but its norm stays one.

Notice one more distinction. Weak convergence does not force the norms to converge. It does imply that the norm of the weak limit is no larger than the lower limit of the sequence's norms. One can see the basic reason directly: a fixed unit vector in the direction of the weak limit detects its length through inner products.

## Strong convergence of operators

Now replace a sequence of vectors by a sequence of bounded linear operators. We say the operators converge strongly to T if, for each fixed vector x, their outputs converge in norm to T x. The operators themselves act on the same Hilbert space, and the limit is again a bounded operator when a suitable uniform-boundedness hypothesis is present; in fact a strongly convergent sequence of bounded operators is uniformly bounded by the uniform boundedness principle.

For a concrete example, let P n keep only the first n coordinates of a square-summable sequence and set all remaining coordinates to zero. It is an orthogonal projection onto the span of the first n basis vectors.

For a fixed input x, the error between x and P n x consists of the tail of its coordinate list. Its squared length is the sum of the squares after coordinate n. Because the whole square-sum converges, that tail tends to zero. Thus P n converges strongly to the identity operator.

But each P n kills the next basis vector. Apply the difference between the identity and P n to that unit vector. The output still has length one. Consequently the operator norm of that difference is one for every n. Strong convergence has not reduced the worst-case error.

## Uniform convergence in operator norm

Operator-norm convergence to T requires the maximum output error over all unit inputs to approach zero. It is sometimes called uniform operator convergence. The difference from strong convergence is whether the test vector may vary with n.

With the coordinate projections, the troublesome vector does vary: at stage n, take the next basis direction, which the approximation has not yet included. Every fixed input is eventually well approximated in norm, but there is always another direction witnessing a full unit of error.

In a finite-dimensional space this distinction disappears for bounded linear operators. Check the finitely many coordinate basis vectors. If every basis output error approaches zero, the error on any unit input is bounded by a constant times the sum of those finitely many errors. That argument relies on having only finitely many directions.

## Weak convergence of operators

There is also a weaker notion for operators: T n converges to T in the weak operator sense if, for each fixed pair x and y, the inner product of T n x with y approaches that of T x with y. Strong operator convergence implies this by Cauchy–Schwarz.

Weak operator convergence does not, by itself, imply strong convergence. Take a bounded operator T n that sends a fixed first basis vector to the n-th basis vector and sends every vector perpendicular to the first basis vector to zero. For any fixed x and y, the measured inner product tends to zero, because the n-th coordinate of y tends to zero. But the output on the first basis vector always has norm one. So the operators converge weakly to zero without converging strongly.

There are now three useful operator tests. A fixed pair of input and measurement directions tests weak convergence. A fixed input tests strong convergence through the entire output length. The largest error over all unit inputs tests operator-norm convergence.

## Why the distinction changes mathematical arguments

Suppose T n approaches the identity strongly, as our coordinate projections do. It would be incorrect to conclude that T n is eventually invertible. Every finite-coordinate projection has a nontrivial kernel, even though its strong limit is the identity.

Operator-norm convergence gives a different conclusion. If the norm of T n minus the identity is strictly less than one, then T n is invertible, using the geometric or Neumann series for its inverse. Thus norm convergence to the identity eventually guarantees invertibility.

This difference becomes important when using finite-dimensional approximations to study spectra. Approximation on each fixed vector may be exactly the convergence available, while conclusions about inverse operators require additional hypotheses.

## A domain warning for unbounded operators

If A is unbounded, applying A to the truncated vector P n x requires P n x to belong to the domain of A. Even if P n x tends to x in the Hilbert-space norm, it does not follow that A P n x tends to A x. The stronger graph norm requires both the inputs and their images under A to converge.

For the diagonal operator that multiplies coordinate k by k, the finite-coordinate projections have a particularly good property: they preserve its domain, and for each vector in that domain, both the discarded coordinates and their k-weighted versions have square-summable tails. Hence P n x approaches x in graph norm. That is an extra fact about the chosen operator and cutoffs, not a consequence of strong operator convergence alone.

A useful final test is to ask what remains fixed as n changes. A fixed vector? Two fixed vectors used in an inner product? Or the worst possible vector at each n? Those are, respectively, strong, weak-operator, and norm-operator perspectives. The coordinate examples show exactly why we need all three.

<!-- END SPOKEN LECTURE -->

---

## Mathematical companion (display only)

Let \(H=\ell^2(\mathbb N)\) with standard orthonormal basis \(e_n\). The vector sequence \(e_n\rightharpoonup 0\) because \(\langle e_n,y\rangle=y_n\to0\) for every \(y\in H\), whereas \(\|e_n\|=1\).

For \(P_nx=\sum_{k=1}^n\langle x,e_k\rangle e_k\),
\[
\|(I-P_n)x\|^2=\sum_{k>n}|x_k|^2\to0\quad(x\in H),
\qquad \|I-P_n\|_{\mathrm{op}}=1.
\]
Thus \(P_n\to I\) strongly but not in operator norm. For \(T_nx=\langle x,e_1\rangle e_n\), \(\langle T_nx,y\rangle=\langle x,e_1\rangle\langle e_n,y\rangle\to0\), while \(\|T_ne_1\|=1\). This gives weak-operator convergence without strong convergence.

**Implications:** operator norm \(\Rightarrow\) strong \(\Rightarrow\) weak operator; norm convergence of vectors \(\Rightarrow\) weak convergence of vectors. The stated converses fail in infinite dimension. Under \(\|T-I\|<1\), the Neumann series \(T^{-1}=\sum_{j\ge0}(I-T)^j\) converges in operator norm. No such conclusion follows for the strong sequence \(P_n\).

For \(A e_k= k e_k\) with \(D(A)=\{x\in\ell^2:\sum k^2|x_k|^2<\infty\}\), \(P_nD(A)\subset D(A)\), and \(\|P_nx-x\|_A^2=\sum_{k>n}(1+k^2)|x_k|^2\to0\) on \(D(A)\). This is **graph-norm** convergence, which needs a domain-preserving approximation.

No Lean declaration is asserted for these textbook calculations.
