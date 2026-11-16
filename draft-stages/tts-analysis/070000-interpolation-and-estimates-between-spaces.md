# 070000 — Interpolation: Estimates Between the Norms We Already Know
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# Interpolation: Estimates Between the Norms We Already Know

Suppose a function has a controlled total mass and also a controlled maximum height. Can we bound its square-integral without doing another integral from scratch? Yes, and the reasoning is elementary. A square is the product of a quantity with itself. One copy can be controlled by the maximum, while the other is integrated as mass. That gives a bound on the square-integral in terms of the mass and the maximum. This simple observation is the doorway to interpolation theory.

Different function norms measure different aspects of a signal. The L-one norm pays attention to total mass, the L-two norm to energy, and the L-infinity norm to peak size. If we have estimates at two ends of this scale, an intermediate norm often obeys an estimate obtained by mixing them with powers. Hölder's inequality supplies the precise powers. We do not choose them by taste; they must make the reciprocal exponents balance.

For example, imagine a function with L-one norm equal to eight and L-four norm equal to two. Can we bound its L-two norm? L-two lies between L-one and L-four. The correct interpolation weights are one third of the L-one information and two thirds of the L-four information. The resulting bound is eight to the power one third times two to the power two thirds. This calculation is about the shape of an admissible estimate, not about claiming the function must be smooth.

Interpolation is particularly useful for an operator. Suppose a linear procedure does not increase the L-one norm of its input, and also does not increase the L-infinity norm. For many familiar operators, such as averaging with a nonnegative probability kernel, it follows that the operator does not increase intermediate L-p norms either. There is a major theorem, often called Riesz–Thorin interpolation, that systematizes this reasoning under specified endpoint bounds and complex-linearity assumptions.

Consider smoothing by convolution with a Gaussian probability density. The output at each point is a weighted average of nearby values. It cannot exceed the input's maximum absolute value. Nor can its total absolute mass exceed the input's total absolute mass. An interpolation theorem then gives contractivity in every L-p space between the endpoints. Plancherel gives an independent check at p equal to two because the Fourier multiplier has magnitude at most one.

Not every interpolation inequality is an operator norm inequality. Sometimes we want an estimate on the derivatives of a single function. A Gagliardo–Nirenberg inequality bounds an intermediate derivative norm in terms of a lower-order norm and a higher-order derivative norm, with powers determined by the dimension and derivative orders. The scaling of a concentrated test function is a quick way to reject an impossible inequality. If rescaling one side changes its size faster than the other, the proposed constants cannot work uniformly.

Take the simplest one-dimensional example. When a function is square-integrable and has a square-integrable derivative, its peak is controlled by a combination of the function's total energy and derivative energy, under standard whole-line or boundary assumptions. Intuitively, a large peak either spreads out, increasing L-two mass, or becomes narrow, increasing the derivative. This tradeoff is a form of interpolation. It is also what makes certain nonlinear products controllable in one dimension.

There is a warning here. Interpolation cannot create information from nothing. Knowing L-one and L-infinity bounds does not automatically imply differentiability. And the precise domain and measure space matter: on a finite-measure domain, some L-p embeddings are automatic, while on the whole real line they are not. An argument valid for one function space may fail if its norm does not encode enough information about tails at infinity.

A second warning concerns endpoints. A theorem might cover all exponents strictly between two values while failing at one endpoint. In harmonic analysis, endpoint estimates can require weak-L-p spaces, logarithmic corrections, or additional cancellation. The fact that a family of estimates approaches an endpoint does not mean the limiting estimate holds unchanged.

Interpolation is a practical way to organize the information we already possess. Rather than proving a separate bound at every exponent, we identify strong estimates at convenient positions and then fill in the space between them, always tracking hypotheses and powers. That skill will be used repeatedly when we ask whether a nonlinear term is controlled by the same function norm as a differential equation's solution.
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(1\le p_0<p<p_1\le\infty\), choose \(0<\theta<1\) with \(1/p=\theta/p_0+(1-\theta)/p_1\). Hölder gives
\[\|f\|_p\le\|f\|_{p_0}^{\theta}\|f\|_{p_1}^{1-\theta}.\]
For \((p_0,p,p_1)=(1,2,4)\), \(1/2=\theta+(1-\theta)/4\), giving \(\theta=1/3\). Hence \(\|f\|_2\le\|f\|_1^{1/3}\|f\|_4^{2/3}\).

The Riesz–Thorin theorem: if linear \(T\) is bounded \(L^{p_0}\to L^{q_0}\) with norm \(M_0\) and \(L^{p_1}\to L^{q_1}\) with norm \(M_1\), under its standard compatibility hypotheses, then interpolated exponents \(p_\theta,q_\theta\) satisfy \(\|T\|_{L^{p_\theta}\to L^{q_\theta}}\le M_0^{1-\theta}M_1^{\theta}\).

For nonnegative \(K\in L^1(\mathbb R^d)\) with \(\int K=1\), Young's inequality gives \(\|K*f\|_p\le\|f\|_p\) for \(1\le p\le\infty\). No regularity conclusion follows without properties of K and/or weighted derivatives.

### Exercises with answers

1. **Weights.** Find \(\theta\) in \(1/2=\theta/1+(1-\theta)/4\). **Answer:** One third.
2. **Averaging.** If \(K\) is a nonnegative probability kernel, can convolution increase the L-infinity norm? **Answer:** No, because it is a weighted average and Young's inequality applies.
3. **Endpoint caveat.** Does an L-two norm bound imply that a function is continuous? **Answer:** No, such a norm gives no pointwise regularity by itself.

### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, interpolation and Sobolev estimates](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
