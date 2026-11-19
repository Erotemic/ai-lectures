# 008000 — The Sylvester equation

**Track:** G3 audio paper track. **Draft:** new G3 lecture, 12 November 2026. **Section:** sylvester. **Audience:** trial residuals and exact decompositions, the angle operator and its modulus identity, unitarily invariant norms and the contraction law.

<!-- BEGIN SPOKEN LECTURE -->

The Sylvester equation

The bridge from a residual to an angle is a single operator equation. This lecture derives it from the trial and exact data, explains why a spectral gap makes its solution small, and proves the first of the paper's Sylvester estimates, Theorem 5.1, which already gives the sine-theta theorem with constant one when the trial spectrum lies in an interval and the unwanted spectrum stays outside it.

Here is what we will establish. First, with X equal to F one star E zero, the coordinates of the trial vectors in the unwanted space, the residual identity becomes Lambda one X minus X A zero equals F one star R. This is a Sylvester equation, with coefficients the unwanted block and the trial operator. Second, when both coefficients are diagonal, the equation divides each entry of the right-hand side by an eigenvalue difference; a distance gap then controls the Hilbert–Schmidt norm of X with constant one. Third, Theorem 5.1: if one coefficient has norm at most a and the other has an inverse of norm at most one over a plus delta, then delta times the norm of X is at most the norm of the right-hand side, in every norm compatible with operator multiplication. Fourth, after shifting by the center of the trial interval, the interval and exterior gap hypothesis is exactly this situation, and the sine-theta inequality follows.

From the residual to an equation for the angle

Recall the data. E zero is an isometric frame for the trial subspace and A zero is the self-adjoint trial operator, with residual R equal to A hat E zero minus E zero A zero. F zero and F one are isometric frames for the exact wanted subspace and its complement, and Lambda one is the self-adjoint operator on the complement, so that A hat F one equals F one Lambda one.

The angle is measured by how much of each trial vector lies in the unwanted space. In coordinates of the unwanted space, that is X, defined as F one star E zero. It takes trial coordinates, builds the trial vector, and reads off its unwanted coordinates. From the angle-operator lecture, the modulus of X is the sine of Theta zero, so every unitarily invariant norm of X equals the same norm of the sine.

Now apply F one star to the residual. The second term gives F one star E zero A zero, which is X A zero. For the first term, take the adjoint of the intertwining equation: since A hat and Lambda one are self-adjoint, A hat F one equals F one Lambda one implies F one star A hat equals Lambda one F one star. So F one star A hat E zero equals Lambda one F one star E zero, which is Lambda one X. Therefore F one star R equals Lambda one X minus X A zero.

In words: the residual, seen from the unwanted space, equals the unwanted block acting on the leaked part, minus the leaked part acted on by the trial operator. If the trial subspace were exactly the wanted spectral subspace, X would be zero and so would this part of the residual. When the operators are unbounded, the equation holds on the domain of A zero, and part of the work in a complete proof is checking that X carries that domain into the domain of Lambda one; the right-hand side is bounded, because R is.

An equation of the form C X minus X B equals Y, with X unknown, is called a Sylvester equation, after James Joseph Sylvester, who studied its matrix form in 1884. The rest of the sine-theta proof is a single question: how large can X be, given Y, under a spectral gap between B and C?

The scalar case and the diagonal case

When everything is a number, the equation reads c times x minus x times b equals y, so x equals y divided by c minus b. If c and b differ by at least delta, the absolute value of x is at most the absolute value of y divided by delta. This is the forty-degree example from the residual lecture: the unwanted part of the residual equals the unwanted eigenvalue minus the trial value, times the unwanted component of the trial vector.

Now let B and C be diagonal matrices, with diagonal entries b j and c i. The equation decouples entry by entry. The entry of C X in row i and column j is c i times x i j, and the corresponding entry of X B is x i j times b j. So c i minus b j, times x i j, equals y i j, and each entry of X is the corresponding entry of Y divided by an eigenvalue difference.

If every c i differs from every b j by at least delta, each entry of X is at most the entry of Y divided by delta in absolute value. Squaring and summing, the Hilbert–Schmidt norm of X is at most the Hilbert–Schmidt norm of Y divided by delta. For self-adjoint matrices, which can be diagonalized by unitaries that leave the Hilbert–Schmidt norm unchanged, this gives a general fact: a distance gap of delta between the spectra gives the Hilbert–Schmidt estimate with constant one. Davis and Kahan record this as their inequality 5.1.

The operator norm is different, because entrywise division by differences does not respect the operator norm. Davis and Kahan's example uses C diagonal with entries one and minus one, B diagonal with entries zero and two, and Y the symmetric matrix with rows three, three and three, minus three. The differences are one, minus one, minus one, and minus three, so X has rows three, minus three and minus three, one. The spectra are a distance one apart, but the operator norm of X is two plus root ten, about five point one six, while the operator norm of Y is three root two, about four point two four. So no operator-norm estimate with constant one follows from distance alone. The spectra here interlace: zero lies between minus one and one.

Theorem 5.1: a window gives constant one

Davis and Kahan's first general estimate avoids diagonalization entirely. It holds in Banach spaces, for any norm on operators compatible with multiplication.

Suppose B is an operator with norm at most a, where a is at least zero, and C is an invertible operator whose inverse has norm at most one over a plus delta, with delta positive. Suppose C X minus X B equals Y. Then delta times the norm of X is at most the norm of Y.

The proof is three lines. Rearranging, C X equals Y plus X B. Apply the inverse of C: X equals C inverse times Y, plus C inverse times X B. Take norms, using compatibility with multiplication: the norm of X is at most one over a plus delta, times the norm of Y plus a times the norm of X. Multiply through by a plus delta: a plus delta, times the norm of X, is at most the norm of Y plus a times the norm of X. Subtract a times the norm of X from both sides. Delta times the norm of X is at most the norm of Y.

The hypotheses can also be interchanged, with B the operator having a large inverse and C the small one; the same argument works with the inverse applied on the right. And C may be unbounded, as long as it has a bounded inverse of the stated size and B and X are bounded.

What does compatible with multiplication mean? The norm of K times X times L must be at most the operator norm of K, times the norm of X, times the operator norm of L. Every unitarily invariant norm and every operator-ideal norm of the paper has this property; it is the contraction law. So Theorem 5.1 holds simultaneously in the operator norm, the Hilbert–Schmidt norm, the trace norm, and the rest. In fact, the argument uses only a left inverse of C with the stated bound, so the printed hypothesis can be weakened slightly.

From Theorem 5.1 to the sine-theta inequality

Now connect this to the interval and exterior gap. Suppose the spectrum of the trial operator A zero lies in an interval from beta to alpha, and the spectrum of Lambda one lies outside the larger interval from beta minus delta to alpha plus delta.

Let c be the center of the trial interval, beta plus alpha over two, and a its half-width, alpha minus beta over two. Shift both operators by c: replace A zero by A zero minus c times the identity, and Lambda one by Lambda one minus c times the identity. The Sylvester equation does not change, since c times X minus X times c is zero. After the shift, the trial operator is self-adjoint with spectrum in the interval from minus a to a, so its norm is at most a. The shifted Lambda one is self-adjoint with every spectral point at distance at least a plus delta from zero, so it is invertible and its inverse has norm at most one over a plus delta. These are exactly the hypotheses of Theorem 5.1.

Therefore delta times N of X is at most N of F one star R, for every unitarily invariant norm N. By the contraction law, N of F one star R is at most N of R, since F one star is a contraction. And N of X equals N of the sine of Theta zero. Putting the pieces together, delta times N of the sine of Theta zero is at most N of R. That is the sine-theta inequality, with constant one, for the interval and exterior configuration with a bounded trial operator, including the case where Lambda one is unbounded.

The same works with the roles exchanged: if the spectrum of Lambda one lies in the interval and the trial spectrum outside, the interchanged form of Theorem 5.1 applies.

A worked check

Use the three by three example. The matrix with rows two, one, zero; one, two, zero; zero, zero, five has the wanted plane of e one and e two, on which it acts with eigenvalues one and three, and the unwanted direction e three, with eigenvalue five. Take a trial operator with spectrum one and three. The trial interval runs from one to three, with center two and half-width one. After shifting by two, the trial operator has norm one and Lambda one becomes three, whose inverse has norm one third, which is one over one plus two. So delta is two.

In the free beam example, the trial operator is zero, so the interval is the single point zero, with half-width zero. The unwanted block of the perturbed beam has spectrum above five hundred, so its inverse has norm less than one over five hundred. The equation reduces to Lambda one X equals the unwanted part of the residual, and the norm of X is at most the norm of that part divided by five hundred. With the residual Gram matrix from the paper, whose larger eigenvalue is epsilon squared over thirty times eleven plus root seventy-six, the operator norm of R is about zero point eight one times epsilon, and so the largest sine is at most about zero point eight one times epsilon over five hundred.

What the window argument cannot do

Theorem 5.1 needs one coefficient to be bounded and the other to have a bounded inverse of the right size. That is a window: one spectrum in a bounded interval, the other outside it.

It cannot handle ordered separation with both operators unbounded, such as the trial operator multiplying the n-th entry by n plus delta and Lambda one multiplying by minus n. Neither operator is bounded, and no shift makes one of them bounded. That case needs a different argument: Theorem 5.2, which can be proved by representing the solution of the Sylvester equation as an integral of exponentials.

And it cannot handle distance-only separation, where the spectra interlace and no window exists. There, as the two by two example shows, the operator-norm constant one is false, and only the Hilbert–Schmidt estimate survives with constant one.

Where the equation comes from

Sylvester studied the matrix equation in 1884 and showed that it has a unique solution for every right-hand side exactly when the two coefficient matrices have no common eigenvalue: the linear map taking X to C X minus X B has eigenvalues equal to the differences of eigenvalues of C and B. Marvin Rosenblum extended solvability to bounded operators with disjoint spectra in 1956, and studied the equation with self-adjoint coefficients in 1969. Davis and Kahan needed a quantitative version: not whether the solution exists, but how large it can be, in every unitarily invariant norm, depending on the geometry of the gap.

To summarize. With X equal to F one star E zero, the residual identity becomes the Sylvester equation Lambda one X minus X A zero equals F one star R, and the modulus of X is the sine of Theta zero. For diagonal coefficients the equation divides entries by eigenvalue differences, which gives the Hilbert–Schmidt estimate under a distance gap, but not the operator-norm estimate. Theorem 5.1 gives delta times the norm of X at most the norm of the right-hand side whenever one coefficient has norm at most a and the other an inverse of norm at most one over a plus delta, in every norm compatible with multiplication. Shifting by the center of the trial interval turns the interval and exterior hypothesis into that form, and the sine-theta inequality follows with constant one.

The window argument is limited to configurations where one side is bounded. Ordered gaps between two unbounded operators require the integral method of Theorem 5.2.

<!-- END SPOKEN LECTURE -->

---

## Companion: mathematics and Lean correspondence (display only)

### Derivation

\(X=F_1^*E_0\), \(|X|=\sin\Theta_0\). From \(\widehat AF_1=F_1\Lambda_1\) and self-adjointness, \(F_1^*\widehat A=\Lambda_1F_1^*\) (on the appropriate domain), so
\[
F_1^*R=F_1^*\widehat AE_0-F_1^*E_0A_0=\Lambda_1X-XA_0\quad\text{on }\operatorname{dom}A_0 .
\]

### Diagonal case and (5.1)

\(B=\operatorname{diag}(b_j)\), \(C=\operatorname{diag}(c_i)\): \((c_i-b_j)x_{ij}=y_{ij}\). If \(|c_i-b_j|\ge\delta\): \(\delta\|X\|_{\rm HS}\le\|Y\|_{\rm HS}\) (Davis–Kahan (5.1)); and \(\delta\|X\|_{\rm op}\le\sqrt{\operatorname{rank}Y}\,\|Y\|_{\rm op}\) ((5.2)).
Example (Section 5): \(C=\operatorname{diag}(1,-1)\), \(B=\operatorname{diag}(0,2)\), \(Y=\begin{pmatrix}3&3\\3&-3\end{pmatrix}\), \(X=\begin{pmatrix}3&-3\\-3&1\end{pmatrix}\); \(\|X\|=2+\sqrt{10}>3\sqrt2=\|Y\|\).

### Theorem 5.1

\(\|B\|\le a\), \(\|C^{-1}\|\le(a+\delta)^{-1}\), \(CX-XB=Y\), \(N(KXL)\le\|K\|N(X)\|L\|\):
\[
X=C^{-1}Y+C^{-1}XB\ \Rightarrow\ N(X)\le\frac{N(Y)+aN(X)}{a+\delta}\ \Rightarrow\ \delta N(X)\le N(Y).
\]

### Interval/exterior sine-theta

\(\sigma(A_0)\subseteq[\beta,\alpha]\), \(\sigma(\Lambda_1)\cap(\beta-\delta,\alpha+\delta)=\varnothing\); \(c=\tfrac{\alpha+\beta}2\), \(a=\tfrac{\alpha-\beta}2\): \(\|A_0-c\|\le a\), \(\|(\Lambda_1-c)^{-1}\|\le(a+\delta)^{-1}\). Hence
\[
\delta N(\sin\Theta_0)=\delta N(X)\le N(F_1^*R)\le N(R).
\]
Examples: \(\sigma(A_0)=\{1,3\}\), \(\Lambda_1=5\): \(c=2,a=1,\delta=2\). Beam: \(A_0=0\), \(\sigma(\Lambda_1)\subset(500,\infty)\), \(\|R\|_{\rm op}=\varepsilon\sqrt{(11+\sqrt{76})/30}\approx0.811\varepsilon\), so \(\|\sin\Theta_0\|\le0.811\varepsilon/500\).

### Lean correspondence

`DavisKahan/Sources/DavisKahan1970/Section5BanachSylvester.lean`:

```lean
theorem theorem5_1_banach_sylvester
    (N : CompatibleCrossOperatorNorm (𝕜 := 𝕜) (X := X) (Y := Y))
    (A : Y →L[𝕜] Y) (B : X →L[𝕜] X)
    (T C : X →L[𝕜] Y) {gamma delta : ℝ}
    (hgamma : 0 ≤ gamma) (hdelta : 0 < delta)
    (hB : ‖B‖ ≤ gamma)
    (hleft : BoundedLeftInverseData A (gamma + delta)⁻¹)
    (hEq : A ∘L T - T ∘L B = C) :
    delta * N T ≤ N C
```

**Mapping notes.**

- Lean's `A, B, T, C` are the lecture's \(C, B, X, Y\) (the source writes \(AX-XB=C\)).
- The docstring records that only a bounded *left* inverse is used, so this reusable theorem is stronger than the printed one; `theorem5_1_banach_sylvester_exact` restores the two-sided inverse hypothesis for source auditing. Interchanged and unbounded-`A` variants: `theorem5_1_banach_sylvester_interchanged`, `banach_sylvester_lower_bound_unboundedA`.
- `CompatibleCrossOperatorNorm` is the formal version of “compatible with multiplication.”
