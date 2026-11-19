# Critical Sobolev Exponents: How Concentration Defeats Compactness

**Track:** Multivariable Calculus from First Principles. **Focus:** scaling, the critical embedding exponent, explicit concentrating bumps, limits of Palais–Smale arguments, and the distinction between subcritical and critical nonlinearities.

<!-- BEGIN SPOKEN LECTURE -->

# Critical Sobolev Exponents: How Concentration Defeats Compactness

Our mountain-pass existence proof for a one-dimensional string depended on a very useful fact. Functions with bounded squared-slope energy and fixed endpoints have a uniformly convergent subsequence. That let us pass to the limit in a cubic nonlinearity and upgrade weak convergence to strong convergence.

If we move the same kind of problem into three or more spatial dimensions, the situation changes. Bounded gradient energy still gives important control, but it no longer makes the functions uniformly close. At a precise exponent, we can squeeze a function into a narrower and narrower region without changing its gradient energy or its nonlinear integral. The functions approach zero almost everywhere, yet their nonlinear mass refuses to disappear.

This phenomenon is the reason the words *critical Sobolev exponent* appear in advanced nonlinear PDE papers. We will derive the exponent rather than memorize it, construct a concentrating sequence explicitly, and identify the step of our earlier existence proof that fails.

## Start with a scaling question

Let us work in n spatial dimensions, with n at least three. Consider a smooth function w that is zero outside a small ball and not identically zero. You can imagine it as a rounded bump. We place the bump at a point inside a domain and squeeze its width by a factor epsilon, where epsilon is a small positive number.

When we squeeze the width, we also increase its height. The height multiplier is epsilon raised to minus one half of n minus two. That exponent may look artificial. It is chosen so the integral of the squared gradient stays unchanged as epsilon shrinks.

Let us check the bookkeeping. Differentiating a function squeezed by epsilon introduces another factor of one divided by epsilon. Squaring the gradient doubles all the exponents. But the region where the bump lives has volume proportional to epsilon to the n-th power. The gain from the smaller volume exactly cancels the loss from the taller, steeper bump. The squared-gradient integral remains the same.

This simple balance already says something important: a bounded energy budget cannot exclude increasingly narrow peaks in dimension three and higher. The amplitude can grow while the peak occupies a shrinking region.

## Which powers of the function survive the squeeze?

Now examine the integral of the absolute value of the bump raised to a power q. Under our scaling, that integral is multiplied by epsilon to the power n minus q times n minus two divided by two.

If that exponent is positive, the integral tends to zero as epsilon shrinks. If the exponent is zero, the integral stays constant. Solve for the power that makes it zero. The answer is two n divided by n minus two. This is the critical Sobolev exponent for the first-derivative, square-integrable setting.

In three dimensions, the critical exponent is six. In four dimensions, it is four. In six dimensions, it is three. As the spatial dimension grows, the exponent approaches two from above.

For powers strictly below the critical exponent, the squeezed bump loses its mass in that integral. At the critical exponent, it retains the same mass while becoming concentrated into a smaller and smaller ball. This is the dividing line between a compact embedding and a merely continuous one on a bounded, sufficiently regular domain.

We need to distinguish that statement from dimensions one and two. In one dimension, bounded first-derivative energy controls uniform continuity and boundedness, as we used for the string. In two dimensions, first-derivative square-integrability embeds into every finite L-p space on a bounded regular domain, but not into all bounded functions with a uniform supremum estimate. There is no finite critical power analogous to six in three dimensions. The endpoint problem in two dimensions involves a different, exponential type of integrability.

## A sequence that converges weakly but not strongly

Keep the concentrating bumps strictly inside a fixed bounded domain, so their boundary values are zero. Their squared-gradient integrals stay constant. Thus their energy-space norms stay bounded and nonzero.

At any point away from the center, the bump eventually vanishes. In fact the support shrinks to a single point, so the sequence approaches zero almost everywhere. Its ordinary square-integral also tends to zero: under this scaling the squared-value integral carries a factor of epsilon squared. On a bounded domain, the sequence converges weakly in the first-order energy space to zero.

But the integral of its critical power stays constant and positive. Consequently it does not converge strongly to zero in the critical L-p space. Nor does it converge strongly in the energy norm, because its gradient norm never decreases. We have built an explicit bounded sequence for which the familiar compactness conclusion fails.

Nothing mysterious is happening to the equations. It is just the scale invariance we calculated. The limiting function sees zero almost everywhere, while a nonzero amount of gradient energy and critical-power mass is squeezed into a smaller region. The missing mass is often described as concentration.

This also clarifies a frequent misconception. A sequence with a bounded energy norm is not necessarily an almost-critical sequence for a particular nonlinear functional. Our rescaled bumps prove failure of compact embedding. To prove failure of Palais–Smale compactness for a specified energy, one additionally needs its derivatives to approach zero. Those are different claims.

## What changes in a nonlinear equation?

Consider a domain in three dimensions and an energy made from one half of the squared-gradient integral minus one sixth of the sixth-power integral. The Euler–Lagrange equation is negative Laplacian u equals u to the fifth power, with zero boundary values.

The quadratic gradient term and the sixth-power term have exactly the competing scaling we just studied. The energy has mountain-pass geometry. Small functions have positive energy because the quadratic term dominates. Along a large multiple of a fixed nonzero test function, the negative sixth-power term dominates and the energy becomes negative.

We might try to copy our one-dimensional proof. Produce an almost-critical sequence. Show it is bounded. Extract a weakly convergent subsequence. Then hope the nonlinear powers converge strongly enough to pass to a limit and obtain a nontrivial critical point.

The dangerous step is now obvious. In three dimensions the relevant embedding from the energy space into the sixth-power space is continuous but not compact. A weakly convergent sequence can carry a concentrated sixth-power contribution that is absent from its weak limit. The one-dimensional argument that relied on uniform convergence is simply unavailable.

A theorem may recover compactness by imposing an energy threshold, geometric restrictions, or additional structural conditions. Or the equation may have no nonzero solution in a particular domain even though its energy has the mountain-pass shape. We cannot infer existence solely from the geometry.

## Why the Talenti profile matters

The compactly supported bump was an elementary example. There are also exact, smooth profiles that are optimizers for the sharp Sobolev inequality in Euclidean space. They are often called Aubin–Talenti bubbles.

The profile has the shape of a rounded peak whose height grows as its width shrinks, with a specific algebraic decay away from the center. A suitable normalization makes it solve the critical nonlinear equation on all of Euclidean space. Changing its center and width does not change the key scale-invariant integrals. Those exact profiles help explain why near-solutions to critical equations can develop localized concentrations.

We should not claim that an arbitrary rescaled bump is an exact critical point or a Palais–Smale sequence. The special Talenti profile satisfies an equation; the generic bump does not. On a bounded domain, even a Talenti profile generally violates the boundary condition until it is cut off or projected, and the resulting error needs analysis. This is why rigorous critical-exponent existence proofs are substantially harder than the subcritical case.

## Three ways compactness can be lost

Concentration is one mechanism, but it is not the only one. On an unbounded domain a fixed bump can move farther and farther away while keeping the same energy. The functions do not concentrate; they *translate out of view*. On some problems, several widely separated concentrations can form, each carrying its own share of the energy. These possibilities are the subject of concentration–compactness methods associated especially with Pierre-Louis Lions.

A useful mental picture is that weak convergence records what stays visible in a fixed frame, but not necessarily everything carried by a sequence. Critical scaling can hide mass in a vanishing region. Translation can hide it at infinity. An existence proof needs to show that the energy level and the equation prevent the relevant escape mechanism—or explicitly account for whatever escapes.

This also explains why critical exponents are genuinely critical rather than merely large. The transition is controlled by scaling, not by an arbitrary technical choice of a power. Below the exponent, the nonlinear norm gains compactness on bounded regular domains. At the exponent, the scaling balance permits concentration without loss of nonlinear mass.

## The stopping point for this advanced route

The mountain-pass method taught us how to find a stationary state without finding a global energy minimum. The Palais–Smale condition told us how to turn an almost-critical sequence into an actual function. The one-dimensional boundary-value example verified every required step. Critical scaling now tells us exactly when that proof cannot be transplanted without new ideas.

There are further theories to develop: concentration–compactness, energy quantization, profile decompositions, and critical nonlinear PDE existence. But they are not the natural next step for everyone learning multivariable calculus. Before following those specialized arguments, it is worth making sure the listener can work confidently with derivatives, norms, weak convergence, Fourier modes, elementary boundary-value problems, and the basic tools of finite-dimensional optimization.

The central lesson is already complete. A nonlinear equation may have a solution because every path across its energy landscape encounters a barrier. But whether that barrier yields a genuine critical function depends on compactness, and compactness can fail at the exact power predicted by scaling.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Critical scaling, with proof of the exponents

Let \(n\geq3\), \(\Omega\subset\mathbb R^n\) contain a closed ball about \(x_0\), and let \(0\neq w\in C_c^\infty(B_1(0))\). For sufficiently small \(\varepsilon>0\), set
\[
 u_\varepsilon(x)=\varepsilon^{-(n-2)/2}\,w((x-x_0)/\varepsilon).
\]
Then \(u_\varepsilon\in H_0^1(\Omega)\) and substitution \(y=(x-x_0)/\varepsilon\) gives
\[
 \int_\Omega |\nabla u_\varepsilon|^2\,dx
 =\int_{\mathbb R^n}|\nabla w|^2\,dy,
 \qquad
 \int_\Omega |u_\varepsilon|^q\,dx
 =\varepsilon^{n-q(n-2)/2}\int_{\mathbb R^n}|w|^q\,dy.
\]
Thus \(2^*=2n/(n-2)\) makes the latter exponent zero. For any fixed \(q<2^*\), the \(L^q\) norm tends to zero, but \(\|u_\varepsilon\|_{2^*}\) is constant. Also \(\|u_\varepsilon\|_2^2=\varepsilon^2\|w\|_2^2\to0\), while \(\|\nabla u_\varepsilon\|_2\) stays fixed. Every weakly convergent \(H_0^1\) subsequence has weak limit zero because of strong \(L^2\) convergence, and the bounded full family is weakly convergent to zero. The embedding \(H_0^1(\Omega)\hookrightarrow L^{2^*}(\Omega)\) is therefore **not compact**.

### Critical energy and the missing implication

For \(n\geq3\),
\[
 I(u)=\frac12\int_\Omega|\nabla u|^2\,dx
 -\frac1{2^*}\int_\Omega |u|^{2^*}\,dx
\]
has \(I'(u)[v]=\int\nabla u\cdot\nabla v-\int |u|^{2^*-2}uv\). Sobolev's inequality establishes the mountain-pass barrier near zero, while any fixed nonzero ray leads to negative energy for large amplitude. The noncompact rescaled-bump family above does **not** itself prove failure of \((PS)_c\) for \(I\), because no derivative estimate has been established for those arbitrary bumps. Special normalized bubble profiles can be used for more refined investigations of critical-energy sequences, but the boundary and derivative errors must be estimated separately.

For \(n=3\), \(2^*=6\) and the Euler–Lagrange equation is \(-\Delta u=|u|^4u\), equivalently \(-\Delta u=u^5\) for real \(u\).

### Talenti bubble on Euclidean space

A standard positive solution of the critical equation on \(\mathbb R^n\) is
\[
 U_{a,\lambda}(x)=[n(n-2)]^{(n-2)/4}
  \left(\frac{\lambda}{1+\lambda^2|x-a|^2}\right)^{(n-2)/2},
 \qquad -\Delta U_{a,\lambda}=U_{a,\lambda}^{2^*-1},
\]
where \(a\in\mathbb R^n\), \(\lambda>0\). This is distinct from the arbitrary compactly supported \(w\) in the elementary noncompactness proof.

### Exercises with answers

1. **Scaling.** Why does \(\|\nabla u_\varepsilon\|_2\) not depend on \(\varepsilon\)? **Answer:** \(|\nabla u_\varepsilon|^2\) contributes \(\varepsilon^{-n}\) and the change of variable contributes \(\varepsilon^n\).
2. **Critical exponent.** Find \(2^*\) in dimensions three, four and six. **Answer:** six, four, and three.
3. **Below critical.** For \(n=3\), what is the scaling exponent of \(\int|u_\varepsilon|^4\)? **Answer:** \(3-4/2=1\), so it tends to zero.
4. **Compactness failure.** Does \(u_\varepsilon\to0\) strongly in \(L^6\) for \(n=3\)? **Answer:** no; its \(L^6\) norm is a fixed positive number.
5. **PS distinction.** Does noncompactness of the critical Sobolev embedding prove that every critical-power energy fails Palais–Smale? **Answer:** no; Palais–Smale includes a derivative condition and may hold at selected energy levels.
6. **Domain condition.** Why choose \(w\) compactly supported near an interior point? **Answer:** then the rescaled functions satisfy the zero boundary trace for all sufficiently small \(\varepsilon\).

### Sources and further reading

- [Giorgio Talenti (1976), *Best constant in Sobolev inequality*](https://math.jhu.edu/~js/Math646/talenti.sobolev.pdf), sharp constant and extremal profiles.
- [University of Turin, *Semilinear Elliptic Problems: The Compact Case*](https://math.i-learn.unito.it/mod/resource/view.php?id=81794), subcritical existence and the compactness/criticality distinction.
- [Wikipedia: Sobolev inequality](https://en.wikipedia.org/wiki/Sobolev_inequality), the conjugate exponent and compact versus continuous embeddings.
- [Pierre-Louis Lions (1984), *The concentration-compactness principle in the calculus of variations: The locally compact case. I*](https://doi.org/10.1016/S0294-1449(16)30428-0), primary source on concentration versus escape.
- [Wikipedia: Pierre-Louis Lions](https://en.wikipedia.org/wiki/Pierre-Louis_Lions), biographical context and bibliography.
- [Ambrosetti and Rabinowitz (1973)](https://doi.org/10.1016/0022-1236(73)90051-7), mountain-pass critical point theory.
- Library preparation: `multivariable-calculus:035000`, `036000`, `064000`, `065000`; `analysis:035000`–`038000`.
