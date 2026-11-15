# 016000 — Cauchy's Theorem and Integral Formula: How a Boundary Controls the Interior

**Track:** Analysis from First Principles. **Background:** complex differentiation, contour integrals, compactness, uniform convergence, and power series. **Theme:** complex differentiability forces cancellation around contractible loops and reconstruction of interior values from boundary data.

<!-- BEGIN SPOKEN LECTURE -->

# Cauchy's Theorem and Integral Formula: How a Boundary Controls the Interior

Suppose you know a function's values all the way around a circle. Could that information tell you what the function does at the center? For an arbitrary continuous function of two real variables, the answer is emphatically no. You could keep the boundary values fixed and change the interior almost however you liked. You could add a bump that vanishes at the circle but reaches a large peak in the middle.

For a holomorphic function, something very different happens. Its values inside the circle are tied so tightly to the boundary that an integral around the boundary recovers the value at any interior point. Not just approximately, and not only for special polynomials: exactly. From that one formula we will obtain derivatives of every order, power-series expansions, and even the fact that every nonconstant complex polynomial has a complex root.

These consequences are why the definition of a complex derivative was worth the trouble. A derivative is a local limit, determined by what happens very close to a point. Yet requiring that derivative to exist everywhere on an open region gives us global information about contour integrals and interior values. We need to understand the bridge from the local condition to the global conclusion.

That bridge has two stages. Cauchy's theorem makes integrals vanish when a curve can be filled by a region on which the function is holomorphic. Cauchy's integral formula then applies that cancellation to a function with a controlled singularity in its integrand. The first result expresses path independence in suitable domains. The second expresses the extraordinary rigidity of holomorphic functions.

## First isolate the hypothesis

Begin with a closed triangle lying inside an open set. Suppose f has a complex derivative at every point in an open neighborhood of that filled triangle. Cauchy–Goursat tells us that the integral of f around the triangle's boundary is zero.

The theorem makes no separate assumption that the complex derivative is continuous. It only assumes holomorphicity on an appropriate open set. This is stronger than a theorem that merely follows by inserting Cauchy–Riemann equations into Green's theorem, because Green's theorem in its familiar form asks for continuous partial derivatives. We have no right, at this stage, to assume that a holomorphic function already has a continuous derivative. Proving such regularity will itself be one of the consequences of the integral formula.

The triangle formulation is a careful starting point because a triangle has straight edges, and it can be subdivided into smaller triangles in a controlled way. We will prove this formulation directly. The proof is an example of what analysis often does when a global quantity seems hard to bound: subdivide the problem repeatedly until the local differentiability hypothesis becomes powerful enough to control it.

## Why subdividing a triangle should help

Call the integral around our starting triangle I. Divide the triangle by joining the midpoints of its sides. This produces four smaller triangles, each with half the original side lengths. Give each small triangle the counterclockwise boundary orientation.

When we add the four small boundary integrals, the contributions along the interior edges cancel. Every interior edge belongs to two triangles and is traversed in opposite directions. Only the original outer boundary survives. So the sum of the four small integrals equals I.

At least one of the four small integrals must have magnitude at least a quarter of the magnitude of I. Otherwise all four would be too small for their sum to equal I, by the triangle inequality. Choose such a triangle and repeat the subdivision within it. At the next stage, choose a subtriangle whose integral has at least a quarter of its parent's magnitude.

After n stages we have a nested sequence of triangles. The integral around the selected triangle has magnitude at least the magnitude of I divided by four to the n. Its perimeter is the original perimeter divided by two to the n, and its diameter is the original diameter divided by two to the n.

These nested triangles are closed and bounded, hence compact. Their diameters shrink to zero. Consequently, they share exactly one limiting point, call it a. Every sufficiently late triangle lies very close to a.

Now the derivative at a comes into play. Complex differentiability says that near a, f of z can be written as f at a plus its derivative at a times z minus a, plus an error. The magnitude of that error is at most a small number times the distance from z to a, provided z is sufficiently close to a.

The first two terms in that approximation contribute zero to a closed contour integral. The constant term has primitive a constant times z. The linear term has a quadratic primitive. The only contribution comes from the error.

How large can the error integral be? Use the length estimate from contour integration. On the selected small triangle, the error is bounded by a small number times its diameter. Multiply this bound by the triangle's perimeter. Both diameter and perimeter have been divided by two to the n, so their product has been divided by four to the n.

We therefore have two opposing bounds on the same small-triangle integral. The selection process says its magnitude is at least the magnitude of I divided by four to the n. Local differentiability says its magnitude is at most the chosen small number times a fixed geometric constant, also divided by four to the n.

Cancel the common factor. The original integral I is at most an arbitrarily small number times that constant. Since the small number can be chosen as close to zero as we wish, I must be zero.

That is the heart of Goursat's argument. No derivative of f was assumed continuous. We only used the existence of a local first-order approximation at the single limiting point selected by the nested triangles, together with the cancellation of interior edges. The proof extracts a global zero-integral statement from arbitrarily fine local control.

## From triangles to useful domains

On a convex open region, such as a disk, every filled triangle with vertices in the region also lies in the region. Subdivision and cancellation let us extend the triangle result to polygonal paths and then, by approximation or a local primitive construction, to piecewise smooth closed paths. In particular, a holomorphic function on a disk has a primitive there, so all of its closed contour integrals inside that disk vanish.

There is a broader version: on a simply connected domain, a holomorphic function has a primitive, and its integral around every closed piecewise smooth contour vanishes. A simply connected domain has no topological hole that prevents a loop from contracting to a point within the domain. The extension from triangles to arbitrary loops requires a geometric argument, not a new differentiability assumption. We will use that version, while keeping the direct triangle proof as the analytic engine behind it.

The word simply connected cannot be dropped without replacing it by a condition on the curve. One divided by z is holomorphic on the punctured plane, but its integral around the unit circle is two pi i, as a direct calculation shows. The missing origin lies inside that circle. Cauchy's theorem does not claim the integral is zero, because the region needed to fill the loop is not part of the domain of holomorphicity.

We can now articulate a practical criterion. When applying Cauchy's theorem to a simple closed contour, verify that the function is holomorphic on an open neighborhood of the entire enclosed region and its boundary. Or use a valid homotopy or simply connected domain theorem. It is not enough to check that the function is holomorphic at the points along the boundary itself.

## A nonzero integral built from a zero integral

Here is the move that produces Cauchy's integral formula. Let f be holomorphic on an open region containing a closed disk. Choose an interior point a. Consider the contour integral around the disk's boundary of f of z divided by z minus a.

At first sight, this integrand appears to violate the hypotheses of Cauchy's theorem, because the denominator vanishes at a inside the circle. That is exactly the point. We will separate the integrand into a singular part whose circle integral we already know, plus a remainder that stays bounded near a.

Write f of z as f of a plus the difference between f of z and f of a. After division by z minus a, the first term is f of a divided by z minus a. Its integral around a positively oriented circle enclosing a is two pi i times f of a. The second term is the difference quotient of f at a, evaluated away from a.

Because f has a complex derivative at a, that second term tends to a finite limit as z approaches a. So it remains bounded near a. It need not yet be declared holomorphic at the missing point; we do not want to sneak in a theorem we have not proved. Instead, use a small circle centered at a and compare its integral with the integral over the large circle. In the annular region between the circles the difference-quotient term is holomorphic, and the contours can be connected by subdivisions. Their integrals agree. The small-circle integral is bounded by the maximum magnitude of the quotient near a times the circumference of the tiny circle. The quotient stays bounded while the circumference tends to zero, so the integral vanishes in the limit.

Therefore the remainder contributes nothing to the outer boundary integral. Only the first, explicitly computable term survives.

We have arrived at the Cauchy integral formula. The value of f at an interior point a equals one divided by two pi i times the integral around the boundary circle of f of z divided by z minus a. The circle is traversed counterclockwise. The function must be holomorphic on an open neighborhood of the closed disk.

Listen to what this says before memorizing it. A function's value at an interior point is a weighted average of its boundary values, but the weights are complex and depend on where that interior point lies. The boundary information completely determines the interior value. There is no freedom to add an interior bump that leaves the boundary unchanged while preserving holomorphicity.

## Calculate once to see the formula operate

Take f of z equal to z squared. Choose a circle centered at zero with radius two, and choose the interior point a equal to one. The formula predicts that the contour integral of z squared divided by z minus one equals two pi i, because f at one is one.

We can verify this without invoking the formula. Divide the polynomial: z squared divided by z minus one equals z plus one plus one divided by z minus one. The first two terms have primitives on the entire plane, so their integrals around the circle are zero. The last term has integral two pi i because the circle encloses one counterclockwise. The result agrees exactly.

This check is useful because it exposes all the hypotheses. If we moved the point a outside the circle, the reciprocal term would have a primitive in a disk containing the circle, and the contour integral would be zero. The Cauchy formula would not claim otherwise, because a would no longer be an interior point. If f had a singularity within the disk, the formula would not apply until we accounted for it.

## One derivative gives all derivatives

Now look again at the Cauchy formula. The value at a appears inside the kernel one divided by z minus a. Along the boundary circle, z stays a positive distance from interior points a. We can therefore differentiate that kernel with respect to a without making the denominator vanish, and the resulting bounds allow differentiation under the integral.

The first derivative of f at a is one divided by two pi i times the boundary integral of f of z divided by the square of z minus a. Differentiating again produces an additional factor and a higher power of the denominator. Continue, and we obtain an explicit integral formula for every derivative of f, of any positive integer order.

This is astonishing if we compare it with real calculus. A real function can have one derivative and fail to have a second derivative. It can have many derivatives without equalizing to its Taylor series. For a holomorphic complex function, the existence of the first complex derivative throughout a neighborhood forces derivatives of every order there. More is true: it forces a convergent power series representing the function near every interior point.

Why does the formula give a power series? Fix a center a and a circle of radius R on which f is holomorphic in a neighborhood. For a point w strictly inside the circle, the reciprocal of z minus w can be rewritten as the reciprocal of z minus a, multiplied by a geometric series in the ratio of w minus a to z minus a. On the boundary, the modulus of that ratio is strictly less than one. The geometric series converges uniformly there, so it can be integrated term by term.

Each resulting coefficient is a boundary integral. The derivative formula identifies it as the appropriate derivative of f at a divided by the factorial of its order. Thus f of w equals the sum of its Taylor series about a, for every w strictly inside that circle.

This is what it means to say holomorphic functions are analytic. We did not assume the existence of a Taylor series in the definition. We derived it from complex differentiability and contour integration. The theorem is not just a local approximation but an exact representation within a disk.

The power series also shows that the real and imaginary parts of a holomorphic function are infinitely differentiable as real functions. Their compatibility through the Cauchy–Riemann equations implies, on applying the equations again, that each real component satisfies the two-dimensional Laplace equation. That connection to harmonic functions will be worth exploring separately, rather than rushing past it as a footnote to Cauchy's formula.

## Estimates that control derivatives

The integral formula does not merely prove derivatives exist; it bounds them. Suppose the modulus of f is at most M on a circle of radius R centered at a. Apply the bound for contour integrals to the formula for the nth derivative at the center. The contour has length two pi R, and the denominator has modulus R raised to the n plus first power. After cancellation, the magnitude of the nth derivative is at most n factorial times M divided by R to the nth power.

These are Cauchy's estimates. They translate a bound on function values along a circle into a bound on derivatives at the center.

Think about a fixed function that is holomorphic everywhere in the complex plane, an entire function. If it is bounded in modulus by the same M everywhere, we can use circles of arbitrarily large radius centered at any chosen point. For the first derivative, Cauchy's estimate says its magnitude is at most M divided by R, no matter how large R becomes. Let R increase without bound. The derivative must be zero at every point. The function is constant.

This is Liouville's theorem: every bounded entire function is constant. It is another statement with no direct analogue for ordinary differentiable real functions. The sine function on the real line is bounded and infinitely differentiable but not constant. Its complex extension is entire, but it is not bounded on the whole complex plane; along imaginary inputs, the corresponding hyperbolic sine grows in magnitude. The added complex directions change the story.

## A consequence about all polynomial equations

We can now complete a promise that began with the geometry of complex numbers. Let P be a nonconstant polynomial with complex coefficients. Suppose, for contradiction, that P never equals zero anywhere in the complex plane.

Then one divided by P is holomorphic everywhere, because the denominator never vanishes. It is also bounded. For very large inputs, the highest-degree term of P dominates, so the modulus of P grows without bound and the reciprocal approaches zero. On the remaining closed disk, the reciprocal is continuous and therefore bounded by compactness. Combining the two regions gives one global bound.

Liouville's theorem says a bounded entire function must be constant. Thus one divided by P is constant, so P must be constant. That contradicts the assumption. Therefore P has at least one complex root.

By dividing P by the linear factor corresponding to that root and repeating the argument, we obtain a factorization into linear factors over the complex numbers, with multiplicities. This is the Fundamental Theorem of Algebra. It does not tell us a numerical method for finding the roots, and its name should not hide the fact that our proof used deep analytic ideas. But it establishes that the complex plane is algebraically complete for polynomial equations.

Notice the chain we followed. Complex differentiation led to Cauchy's theorem. Cauchy's theorem led to an integral formula. The integral formula led to derivative bounds. Derivative bounds led to Liouville's theorem. Liouville's theorem forced a polynomial to have a root. A geometric condition on infinitesimal changes has reached an apparently distant algebraic conclusion.

## Limits of the theorem, and the next questions

It is tempting, after this, to use Cauchy's formula everywhere. Resist that temptation. We required a holomorphic function on a neighborhood of the entire closed disk. A function with a pole inside the circle violates the hypothesis, even if it is smooth on the boundary. A loop in a multiply connected domain may fail to bound any region inside the domain. A formula derived for a positively oriented simple circle cannot be applied blindly to a curve that winds several times, crosses itself, or runs clockwise.

There are general versions involving winding numbers and contours that are not simple circles. Those generalizations deserve their own careful hypotheses and proofs. We will also need to understand what changes when a function is holomorphic except at isolated points. The contour integral of one divided by z told us that such exceptions leave detectable traces. Laurent series and residues will turn that observation into a systematic calculus of singularities.

For now, the two central ideas are clear. Cauchy's theorem describes cancellation when a holomorphic function is integrated around a contractible loop. Cauchy's integral formula reconstructs a holomorphic function from boundary values and forces it to have derivatives of all orders and a convergent local power series.

When you hear that complex analysis is more rigid than real analysis, this is the precise content behind the phrase. We are not talking about a mysterious personality of complex numbers. We are talking about a chain of proved implications whose hypotheses we can check: differentiability in every complex direction, an open region containing the necessary curves and interiors, and compactness and uniform estimates controlling the resulting integrals.

The next questions are now natural. Which functions have singularities that are removable, which have poles, and which behave more wildly? What information does a contour integral retain when we cannot fill the loop with a holomorphic region? And how can the argument of a function along a boundary count the zeros inside? The answers begin with Laurent expansions and residues, and they will build directly on the formula we have just proved.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

### Goursat's triangle theorem and subdivision proof

If \(U\subset\mathbb C\) is open, \(f\in\mathcal O(U)\), and the filled triangle \(T\) is contained in \(U\), then
\[
\int_{\partial T}f(z)\,dz=0.
\]
Set \(I=\int_{\partial T}f(z)\,dz\). Subdivide each triangle into four similar triangles. At level \(n\), select a nested triangle \(T_n\) with \(|I_n|\ge4^{-n}|I|\), diameter \(D_n=2^{-n}D\), perimeter \(L_n=2^{-n}L\). Nested compactness yields a unique common point \(a\). Complex differentiability at \(a\) yields
\[
f(z)=f(a)+f'(a)(z-a)+(z-a)\eta(z),\qquad \eta(z)\to0\ (z\to a).
\]
The first two terms have primitives and zero integrals around \(\partial T_n\). For sufficiently large \(n\), \(\sup_{z\in T_n}|\eta(z)|\le\varepsilon\), so
\[
|I_n|\le\varepsilon D_n L_n=\varepsilon DL\,4^{-n}.
\]
Therefore \(|I|\le\varepsilon DL\) for every \(\varepsilon>0\), hence \(I=0\). No continuity of \(f'\) was assumed.

### Cauchy's integral theorem and formula (disk version)

If \(f\) is holomorphic on an open neighborhood of the closed disk \(\overline{D(a,R)}\), then for the positively oriented circle \(\Gamma=\partial D(a,R)\):
\[
\oint_\Gamma f(z)\,dz=0,\qquad
f(w)=\frac{1}{2\pi i}\oint_\Gamma\frac{f(z)}{z-w}\,dz\quad(|w-a|<R).
\]
For the integral formula, decompose \(f(z)/(z-w)=f(w)/(z-w)+(f(z)-f(w))/(z-w)\). The first term integrates to \(2\pi i f(w)\). The second is holomorphic on the punctured disk and bounded near \(w\). By Cauchy–Goursat applied between the outer curve and a small circle \(|z-w|=r\), its integral is equal to its integral around the small circle; the latter has modulus \(O(r)\to0\). This avoids assuming a priori that the extended difference quotient is holomorphic at \(w\).

### Cauchy's derivatives and estimates

Under the same hypotheses, for \(|w-a|<R\) and each integer \(n\ge0\),
\[
f^{(n)}(w)=\frac{n!}{2\pi i}\oint_\Gamma\frac{f(z)}{(z-w)^{n+1}}\,dz.
\]
At the center \(a\), if \(M_R=\max_{|z-a|=R}|f(z)|\), then
\[
|f^{(n)}(a)|\le\frac{n!M_R}{R^n}.
\]
For \(|w-a|<R\) the geometric expansion of \(1/(z-w)\) on \(\Gamma\) is uniformly convergent, yielding
\[
f(w)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(w-a)^n.
\]

### Liouville and the Fundamental Theorem of Algebra

If \(f\) is entire and \(|f(z)|\le M\) for all \(z\), Cauchy's estimate gives \(|f'(a)|\le M/R\) for all \(R>0\). Hence \(f'(a)=0\) at every \(a\), so \(f\) is constant.

If a nonconstant polynomial \(P\) has no zero, \(1/P\) is entire. Since \(|P(z)|\to\infty\) as \(|z|\to\infty\), \(1/P\) is bounded outside a sufficiently large disk; continuity bounds it on the remaining compact disk. Liouville yields a contradiction. Polynomial division and induction give linear factorization over \(\mathbb C\).

### Worked exercises and answers

1. **Cauchy formula:** Evaluate \(\oint_{|z|=2}\frac{z^2}{z-1}\,dz\) counterclockwise. **Answer:** \(2\pi i\), by the value of \(z^2\) at \(1\).
2. **Derivative formula:** Evaluate \(\oint_{|z|=3}\frac{e^z}{z^3}\,dz\) counterclockwise. **Answer:** \((2\pi i/2!)\,(e^z)''|_{z=0}=\pi i\).
3. **Circle estimate:** If \(|f(z)|\le7\) for \(|z-a|=4\) and \(f\) is holomorphic in a neighborhood of the closed disk, bound \(|f''(a)|\). **Answer:** \(2!\cdot7/4^2=7/8\).
4. **Invalid invocation:** Why does Cauchy's theorem not force \(\oint_{|z|=1}dz/z=0\)? **Answer:** \(1/z\) is not holomorphic at 0, which lies in the filled disk.
5. **Liouville:** Why can \(\sin x\) be bounded on the real line while \(\sin z\) is not bounded on \(\mathbb C\)? **Answer:** Along \(z=iy\), \(\sin(iy)=i\sinh y\), whose modulus is unbounded as \(|y|\to\infty\).
6. **Where the proof uses a full neighborhood:** Why is holomorphicity just on a circular boundary insufficient for the Cauchy formula? **Answer:** The proof applies Cauchy–Goursat inside the boundary (apart from a deliberately isolated kernel singularity); without an interior holomorphic region, extra singularities may contribute.

### Further reading

- MIT OpenCourseWare, *18.112 Functions of a Complex Variable*, Lectures 9–10, https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- MIT OpenCourseWare, *18.04 Complex Variables with Applications*, Topics 3–4, https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/lecture-notes/.
- *A First Course in Complex Analysis*, section on Cauchy–Goursat, https://complexanalysis.org/web/sec_cauchy-goursat.html.
- Wikipedia, *Cauchy's integral formula*, https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula.
- [Robert B. Ash and W. P. Novinger, Complex Variables, 2nd ed.](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesMerged.pdf) — Ash & Novinger, Complex Variables, chapters 2–3: Cauchy theory and integral formula.
