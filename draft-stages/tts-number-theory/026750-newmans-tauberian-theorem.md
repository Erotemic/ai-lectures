# 026750 - Newman's Tauberian Theorem: A Contour That Recovers a Limit

**Track:** Number Theory from First Principles. **Background:** 015000 (summation and convergence), 026000 (Cauchy and contours), 026500 (zeta's zero-free boundary). **Aim:** prove a complete bounded-function Tauberian theorem, with every contour and error estimate accounted for, before using it in the prime number theorem.

<!-- BEGIN SPOKEN LECTURE -->

# Newman's Tauberian Theorem: A Contour That Recovers a Limit

Imagine you could listen to a function without seeing its values directly. You feed it into a transform, and the transform reports how its values are averaged, with observations far in the future given less weight. If you know this weighted information for every positive rate of decay, have you learned what happens when the weight is removed entirely? Not necessarily. A function can oscillate, and a formal substitution of zero for the decay rate can conceal a divergent integral.

This problem lies between our last result about the Riemann zeta function and a proof of the prime number theorem. The zeta function has been continued across the line with real part one, except for a known pole, and it does not vanish on that line. We can therefore describe an analytic transform of the distribution of prime powers at the boundary. What remains is to justify removing a smoothing factor and recovering the actual prime count.

We will prove a theorem that accomplishes exactly this for bounded functions. The essential argument is due to Donald Newman. It is a contour argument, but not a mysterious invocation of a theorem that does all the work. We will build the contour, explain a kernel chosen to control its troublesome points, and account for the limits in the right order.

## What the transform knows

Take a complex-valued function f defined for nonnegative real times. Assume its absolute value never exceeds some constant H, and assume it is integrable on each finite interval. Piecewise continuous functions are enough for the examples we need, including the step functions produced by prime powers.

For a complex number z with positive real part, form the Laplace transform G of z: integrate f of t times the exponential of negative z times t, from zero to infinity. The integral converges absolutely: the exponential magnitude decays geometrically in continuous time, and f remains bounded. The integral also defines a holomorphic function of z in that half-plane. Differentiation adds factors of t, and on a smaller closed half-plane those factors remain dominated by exponential decay.

Suppose something stronger occurs. Imagine that G has a holomorphic continuation not merely up to isolated points on the imaginary axis, but across every point of the entire closed right half-plane, into a small open neighborhood of each point. The neighborhoods can be thinner as we move up or down the axis; we do not assume one fixed-width strip.

The conclusion is that the ordinary, unsmoothed improper integral of f from zero to infinity actually converges. Its value is the continued function G evaluated at zero.

The conclusion is stronger than the casual claim that setting z equal to zero ought to work. It says that an honest limit of finite integrals exists. Boundedness of f is indispensable to the proof: analytic continuation by itself does not grant unlimited control over unweighted tails.

## Separate what is finite from what is infinite

Fix a time T. Let G sub T be the integral of f times the exponential of negative z times t, but only from zero to T. It is defined for every complex z, with no convergence issue. Because the integration interval is finite, G sub T is an entire function: one may differentiate it arbitrarily many times with respect to z.

Our goal is to show that G sub T at zero tends to G at zero as T goes to infinity. In plain language, G sub T at zero is exactly the integral of f from zero to T. Thus proving this convergence proves the theorem.

We would like to apply Cauchy's formula to the difference G minus G sub T. There is a catch. G is only known to continue a little way into the left half-plane around the imaginary axis. It may have singularities deeper on the left. We are therefore not allowed to integrate G around an enormous full circle centered at the origin.

This is why we use two contours rather than one. One contour encloses the origin using the right half of a large circle and a narrow path just to the left of the imaginary axis. The other contour is the full circle, used only for the entire function G sub T. Their difference will place exactly the functions we can estimate on the paths where we can estimate them.

## Two contours and a kernel

Pick a positive radius R. The right semicircle runs from the point negative i R to positive i R, passing through positive real R. The left semicircle runs back from positive i R to negative i R, passing through negative real R. Together they form the positively oriented boundary of a disk.

Because G is holomorphic across every point of the finite imaginary-axis segment from negative i R to positive i R, compactness allows us to choose a small positive delta so that G is holomorphic throughout a narrow rectangle from real part negative delta to real part zero, between those heights. Join the top of the right semicircle horizontally to negative delta plus i R, travel vertically down to negative delta minus i R, and return horizontally to the bottom of the semicircle. Call that three-sided path the left detour. The right semicircle and this detour enclose zero in a region where G is holomorphic except for the pole we are about to introduce through a kernel.

The kernel is exponential of T z, divided by z, multiplied by one plus z squared over R squared. At z equal to zero, its residue is one. Its exponential factor compensates for the exponential that appears in our tail estimate. The final factor is the clever part. On the circular arcs, one plus z squared over R squared vanishes at the two endpoints where real part of z is zero. In fact, its magnitude is exactly twice the absolute real part of z, divided by R.

Why does this matter? The estimates for a Laplace transform contain the reciprocal of the real part of z. Near the top and bottom of a semicircle, that reciprocal appears to blow up. Multiplying by this kernel makes the apparent singularity cancel exactly. We gain a uniform bound even arbitrarily close to the endpoints.

Apply Cauchy's residue formula to G times the kernel on the right-semicycle-and-detour contour. Its integral equals two pi i times G at zero. Apply the same formula to G sub T times the kernel on the full circle. Its integral equals two pi i times G sub T at zero. Subtract the two identities. We get three pieces: an integral of G minus G sub T over the right semicircle; an integral of G over the narrow left detour; and the negative of an integral of G sub T over the left semicircle.

There are no concealed boundary terms. The kernel's pole at zero has residue one, and each curve encircles that point exactly once.

## Estimate the right half

At any point z on the right semicircle away from its endpoints, let sigma be its positive real part. G minus G sub T is the integral of f from T to infinity with the exponential damping. Since f is bounded by H, the absolute value of this tail is at most H times exponential of negative T sigma, divided by sigma.

Now multiply by the kernel. Its exponential of T sigma cancels the decaying exponential in the tail. Its factor one over z contributes one over R on the circle. And the magnitude of one plus z squared over R squared contributes twice sigma over R. The sigma in the denominator disappears. The resulting bound is twice H divided by R squared, uniformly along the arc.

The arc has length pi R. Divide its integral by two pi, as in the residue formula, and its total absolute contribution is at most H divided by R. Notice what has happened: the bound has no dependence on T, no dependence on how near we get to the imaginary axis, and decreases when R grows.

## Estimate the left half

For G sub T on the left semicircle, sigma is negative. We must not use an infinite Laplace integral there, since that integral would diverge. But G sub T is finite, so direct integration gives a bound of H times exponential of negative T sigma divided by negative sigma. The minus sign matters: sigma is negative, so the exponential now grows rapidly with T.

Again the kernel contains exponential of T sigma, which cancels that growth. Again one over z has magnitude one over R, and the endpoint factor gives twice the absolute value of sigma over R. We obtain the same uniform bound, twice H over R squared. Thus this second semicircle also contributes at most H over R after the residue normalization.

We have now neutralized the two large circular pieces. All that remains is the thin detour on the left, and it is of a very different character.

## Make the left detour disappear

For each fixed R, we chose a fixed delta and hence a fixed finite detour. It lies inside the region where G is holomorphic, so G is bounded on that compact path. The factor one over z is bounded too because the path avoids zero. The polynomial factor is harmless.

Every interior point of this detour has strictly negative real part. Therefore the exponential of T z tends to zero as T increases. On the path, its absolute value is at most one; the endpoints have real part zero, but individual endpoints contribute no length to a contour integral. By dominated convergence along this finite path, the entire detour contribution tends to zero.

This order of limits deserves care. We first fix R and choose delta. We then let T tend to infinity so the detour disappears. Only after this limit do we allow R to grow. There is no assumption that the same delta will work for arbitrarily large R.

For each fixed R, the two semicircular estimates therefore show that the eventual difference between G at zero and G sub T at zero has magnitude at most twice H divided by R. But we were free to choose R as large as we wished. Let R increase without bound. The only nonnegative quantity bounded by twice H divided by every R is zero.

So G sub T at zero converges to G at zero. Since G sub T at zero is the unweighted integral through T, the proof is complete.

## Why the theorem is Tauberian

The argument earns the name Tauberian because it reverses a typically one-way smoothing operation. If an ordinary integral converges and f is bounded, it is often straightforward to show that a suitably damped integral approaches the same number as the damping vanishes. The converse fails without additional information. Here the extra information is the analytic extension of the entire family of weighted averages, plus boundedness of f. The contour proof converts those hypotheses into the converse.

It is worth testing the boundaries of the statement. The constant function f equal to one is bounded, and its transform equals one over z for positive real part. But that transform has a pole at zero and cannot satisfy the holomorphic-continuation hypothesis. Its ordinary integral diverges, exactly as the theorem predicts it may. The function sine of t is also bounded; its transform has poles at plus and minus i, so it does not continue holomorphically across the entire imaginary axis. Again its ordinary improper integral does not converge. These are not technical embarrassments: the boundary singularities remember the obstruction to removing the weight.

A less familiar bounded function can have a convergent ordinary improper integral thanks to oscillation. The theorem does not require f to be nonnegative or monotone. Its power lies precisely in allowing such signs and oscillations while controlling them through analyticity.

## The bridge we have constructed

We now have a fully proved analytic tool. The remaining arithmetic application is to find the right bounded f. It will come from the weighted count of prime powers: take the accumulated von Mangoldt weights up to exponential of t, divide by exponential of t, and subtract one. Chebyshev's estimate makes this bounded. Its Laplace transform can be expressed in terms of negative zeta prime over zeta, with the known pole canceled by the subtraction of one.

Our last lecture proved that zeta has no zeros on the boundary line. That is exactly what ensures the transform is holomorphic at every imaginary-axis point after the pole is removed. This theorem will then tell us that a certain integral of the normalized prime-power count converges. One final, entirely elementary comparison using monotonicity will turn convergence of that integral into an actual limit of the normalized count.

We did not assume the prime number theorem to prove this lemma. We proved the missing analytic passage separately, with every estimate tied to an explicit path. The next step can now finish the arithmetic argument without hiding a theorem inside the words "let the smoothing disappear."

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Exact statement and hypotheses

**Newman's bounded-function Tauberian theorem.** If \(f:[0,\infty)\to\mathbb C\) is bounded by \(H\), locally Lebesgue-integrable, and
\[
G(z)=\int_0^\infty f(t)e^{-zt}\,dt \quad(\Re z>0)
\]
continues holomorphically to an open set containing \(\{z:\Re z\ge0\}\), then
\[
\lim_{T\to\infty}\int_0^T f(t)\,dt=G(0).
\]
Holomorphic continuation only has to hold in an open neighborhood of **each** point of the closed half-plane; no fixed-width strip is assumed.

Let \(G_T(z)=\int_0^T f(t)e^{-zt}\,dt\), entire. Fix \(R>0\). Let \(C_+\) be the right semicircle \(|z|=R\) from \(-iR\) to \(+iR\), \(C_-\) the left semicircle from \(+iR\) to \(-iR\), and \(\Gamma_-\) the three-segment path from \(+iR\) via \(-\delta+iR\), \(-\delta-iR\), to \(-iR\), for sufficiently small \(\delta>0\). All these curves have positive orientation when combined as \(C_++C_-\) and \(C_++\Gamma_-\).

Define
\[
K_T(z)=\frac{e^{Tz}}z\left(1+\frac{z^2}{R^2}\right),\qquad
\operatorname{Res}_{z=0}K_T=1.
\]
Subtract the two residue identities:
\[
2\pi i\,[G(0)-G_T(0)]=
\int_{C_+}(G-G_T)K_T\,dz+
\int_{\Gamma_-}GK_T\,dz-
\int_{C_-}G_TK_T\,dz.
\tag{N1}
\]
For \(|z|=R\), \(\sigma=\Re z\),
\[
\left|1+\frac{z^2}{R^2}\right|
=\frac{2|\sigma|}{R},\quad |z|=R.
\tag{N2}
\]
Right arc (\(\sigma>0\)):
\[
|G(z)-G_T(z)|\le \frac{He^{-T\sigma}}\sigma,
\quad |(G-G_T)K_T|\le\frac{2H}{R^2}.
\]
Left arc (\(\sigma<0\)):
\[
|G_T(z)|\le\frac{H(e^{-T\sigma}-1)}{-\sigma}
\le\frac{He^{-T\sigma}}{-\sigma},
\quad |G_TK_T|\le\frac{2H}{R^2}.
\]
Each semicircle has length \(\pi R\), hence each integral in (N1), after dividing by \(2\pi\), costs at most \(H/R\). On \(\Gamma_-\), \(e^{Tz}\to0\) at every interior point, \(|e^{Tz}|\le1\), and other factors are bounded on the fixed compact curve. Dominated convergence yields
\[
\limsup_{T\to\infty}|G(0)-G_T(0)|\le\frac{2H}{R}.
\]
Take \(R\to\infty\) **after** \(T\to\infty\). The continuation neighborhood provides a possibly different \(\delta\) for each fixed \(R\).

### Counterexample checks

1. \(f(t)=1\) has \(G(z)=1/z\), not holomorphic at zero; \(\int_0^T f=T\).
2. \(f(t)=\sin t\) has \(G(z)=1/(z^2+1)\); poles on the imaginary axis; \(\int_0^T\sin t\,dt=1-\cos T\) has no limit.
3. The theorem allows signed or complex-valued \(f\). Positivity is **not** among its hypotheses.

### Exercises

1. Derive (N2) by writing \(z=Re^{i\theta}\), and explain why the zero at the endpoints is needed.
2. Prove that \(G_T\) is entire by differentiating under the finite integral; find its \(m\)-th derivative.
3. Why is the assumption "\(G\) extends across \(z=0\)" insufficient? Construct a second singularity somewhere on the imaginary axis that makes the argument fail.
4. Reconstruct the contour identity (N1) from two applications of the residue theorem and check both orientations.
5. Explain why letting \(R\to\infty\) before fixing \(\delta\) would ask for a stronger, unproved hypothesis.

### Reading and source notes

- Don Zagier, [Newman's Short Proof of the Prime Number Theorem](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2975232/fulltext.pdf), *American Mathematical Monthly* **104** (1997), pp. 705–708, especially the contour proof on pp. 707–708. This proof belongs historically to D. J. Newman; Zagier presents it and credits the earlier development.
- Romyar Sharifi, [Algebraic Number Theory](https://www.math.ucla.edu/~sharifi/notes/algnum-ch02.html), for a parallel example of how precise ring hypotheses are tracked in another branch of this course.
- Wikipedia: [Tauberian theorems](https://en.wikipedia.org/wiki/Tauberian_theorems), [Laplace transform](https://en.wikipedia.org/wiki/Laplace_transform), [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).
