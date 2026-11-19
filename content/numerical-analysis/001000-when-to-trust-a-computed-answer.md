# 001000 — When to Trust a Computed Answer: Models, Data, Approximation, and Tolerances

**Track:** Numerical Analysis and Reliable Computation. **Background:** algebra and basic functions. **Purpose:** distinguish the target of a calculation from the calculation's output, and make an error claim precise.

<!-- BEGIN SPOKEN LECTURE -->

# When to Trust a Computed Answer

A bridge model predicts that a beam will bend by two point four millimeters under a specified load. Is that an answer? Certainly. Is it a trustworthy answer? Not until we know which bridge, which load, and what the number means. If the beam's stiffness was estimated from a test specimen, there is uncertainty in the input. If the model assumes a perfectly uniform material, there is model discrepancy. If the governing equations were solved on a finite grid, there is approximation error. If the arithmetic used a finite number of binary digits, there is rounding. And if a solver stopped before it had converged, there is iteration error.

These are not five synonyms for the same problem. They have different causes, different mathematical descriptions, and different remedies. Increasing floating-point precision cannot repair an incorrect model of the bridge. Refining a grid cannot recover a load measurement that was never accurate. Running an iterative solver longer cannot fix a badly chosen stopping condition. Numerical analysis begins by refusing to confuse the number printed by a machine with the quantity we intended to know.

Let us build a way of thinking that works for a small equation, a simulation, and a much larger scientific computation.

## Choose the target before the algorithm

Suppose we want the positive number whose square is two. There is an exact mathematical target: the positive square root of two. One decimal approximation is one point four one four. Its square is one point nine nine nine three nine six. It is close to two, but not equal. We can check how close without knowing every digit of the square root.

This is the simplest version of an error specification. The exact answer, call it x, is fixed by the problem; an algorithm returns an approximation, call it x-hat. Their absolute error is the distance between x-hat and x. Relative error scales that distance by the magnitude of x when x is nonzero. If the target is zero, ordinary relative error is undefined, so an absolute or properly scaled criterion is needed.

Now change the task. Suppose someone asks for the square root of the *measured* value two point zero zero, reported to two decimal places. Is the intended answer the mathematical square root of exactly two? Or a prediction conditioned on a measurement interval? If the measurement was rounded to the nearest hundredth, the underlying quantity might be anywhere from roughly one point nine nine five to two point zero zero five, subject to the measurement procedure. There is no single exact physical input implied by the displayed decimal alone.

It matters whether a number is an exact parameter, a measurement, a rounded storage value, or a statistical estimate. An error bound about an exact computational model is not automatically a statement about physical truth.

## Four arrows between the question and the number

Imagine an intended physical quantity on one side and the displayed answer on the other. The first arrow chooses a model: perhaps a differential equation for temperature or motion. The second substitutes data such as material constants and boundary conditions. The third replaces the mathematical model by something finite: a grid, a polynomial, a truncated series, or a system of linear equations. The fourth runs an algorithm in finite arithmetic and stops it.

We can compare the output at each stage with the previous one. Model error asks whether the model's quantity represents the physical quantity. Data uncertainty asks how much the model's answer changes when the input values vary over their plausible ranges. Discretization or truncation error asks how far the finite problem lies from the mathematical problem. Iteration error asks how much remains after the current algorithmic steps. Rounding error asks what finite arithmetic changed.

One can sometimes bound the final error by adding bounds for the individual differences. That follows from the triangle inequality, but only when all quantities have been compared in a compatible norm and to the same meaningful target. Errors can cancel, so adding their upper bounds is usually conservative. Independence assumptions used for statistical uncertainty do not automatically apply to deterministic error bounds.

A good computation therefore has an error budget, not just a declaration that its floating-point type has enough digits.

## A residual is not the same as an error

Take the square-root example again. We are not able to subtract an unknown exact root from x-hat in ordinary computation. But we can calculate a residual: x-hat squared minus two. A residual tells us how well our proposed number satisfies an equation. If that equation is evaluated accurately enough, the residual is useful evidence.

Yet a tiny residual does not always mean a tiny error in the answer. Consider the equation x squared equals zero. If x-hat is one millionth, the residual is one trillionth, which sounds spectacularly small. But the error in x is one millionth, not one trillionth. The squaring operation suppresses small numbers. Near a multiple root, residual size alone can seriously understate the error.

For a different equation, such as ten billion times x equals ten billion, a modest residual might correspond to a very small error in x. The relationship between residual and answer error depends on the sensitivity of the equation. In one dimension, a derivative that stays safely away from zero often gives a usable conversion. For a linear system, the analogous object is an inverse operator or a condition number.

A computational report should therefore say whether it gives a residual, a forward-error bound, a backward-error bound, or merely an observed difference between successive iterates. These are not interchangeable certificates.

## What does tolerance actually mean?

People sometimes say, 'stop when the answer is accurate to six decimal places.' That sentence leaves several questions unanswered. Accurate in what units? Absolute error below one millionth, or relative error below one millionth? Does 'six places' refer to rounding to a decimal representation? Which uncertainty sources are included? How was the bound established?

Suppose we are computing a temperature difference of one thousandth of a degree. An absolute tolerance of one hundredth would accept zero as a satisfactory result, even though the entire temperature difference has been lost. At the other extreme, a relative tolerance cannot sensibly be imposed on a target that may be exactly zero. A common engineering criterion combines an absolute scale and a relative scale: accept an error only when it is below an absolute allowance plus a relative allowance times an appropriate size of the quantity. It is a useful rule only if the error being compared is actually bounded or reliably estimated.

A threshold applied to two successive iterates is *not* necessarily a bound on their distance from the solution. The iterates may stagnate, oscillate, or approach a wrong value. A robust algorithm ties stopping to a mathematical guarantee: a certified interval bracket, a residual converted to error using a lower derivative bound, or a convergence theorem with computable constants.

The numerical-analysis question is not only 'did the iteration stop?' but 'what conclusion does stopping logically permit?'

## An exact answer may still be the wrong answer

Imagine using an exact symbolic solver on a mathematical model with the wrong sign in one term. It returns a perfectly correct solution to the equation you supplied. No floating-point rounding was involved. The answer can still fail the purpose for which it was requested.

Conversely, a useful numerical calculation may deliberately return a rough approximation. Suppose the input measurement has uncertainty of a whole percent. Reporting fifteen apparent digits of an output does not create fifteen digits of physical information. Computing to tighter numerical tolerance can be useful for separating numerical error from measurement uncertainty, but it should not be presented as improved experimental knowledge.

This distinction appears in computer graphics, where visual plausibility may be the goal; in optimization, where a certificate of near-optimal objective value may matter more than exact coordinates; and in scientific modeling, where a range of outcomes under plausible parameters may matter more than a single high-precision answer. A reliable numerical method is relative to a *contract*.

## Independent checks are powerful, but not magic

How do we decide whether to trust a calculation? We can evaluate a residual using more accurate arithmetic, compare independent algorithms, refine the discretization, or compute an interval guaranteed to contain the exact answer of a specified model. Each checks a different link in the chain.

Comparing two algorithms is helpful, but they may share a modeling mistake or both be sensitive to the same poorly determined input. Watching results stabilize as we refine a grid is suggestive, but without a convergence argument the apparent plateau may be caused by rounding or a systematic bias. A small residual can be checked independently, but converting it into a forward-error estimate still requires conditioning information.

Validated numerics attempts to close that final gap. For instance, if a continuous function changes sign across an interval, the Intermediate Value Theorem guarantees a root somewhere inside. If a root-finding procedure preserves that bracket, the midpoint has an immediate absolute-error bound: at most half the bracket width. The guarantee depends on correct sign evaluation and the continuity hypothesis, but it is a genuine conclusion about the specified equation, not merely a hopeful output format.

A fully verified computation may need to include roundoff in the sign calculation, using outward-rounded intervals or exact arithmetic. Certification is not free, but it identifies what must be trusted.

## The order of uncertainty is a mathematical decision

Suppose the quantity we want is the square root of a positive measured input. We can represent the uncertainty by an interval of permissible inputs. Because the square-root function is increasing, its smallest and largest possible outputs occur at the interval endpoints. This observation gives an output range without inventing a probabilistic model and without relying on a first-order approximation.

If the input were genuinely known only to lie between one point nine nine five and two point zero zero five, the mathematical target could lie anywhere between the square roots of those endpoints. A computer that evaluates the square root of exactly two to fifteen digits gives a precise answer to one point inside that range; it does not reduce the range. A more informative report propagates the interval through the model, then adds a separately justified numerical enclosure for the endpoint evaluations.

There is a choice here. If measurements are random and we have a calibrated probability distribution, confidence or credible intervals may be appropriate, with distinct statistical meanings. If we know only a worst-case interval, a deterministic enclosure is appropriate. Treating those as interchangeable would silently add assumptions about the data that nobody supplied.

This illustrates why uncertainty propagation is not always a final correction applied after a large computation. It can change what computational question is worth solving in the first place.

## A numerical answer as a mathematical claim

Return to the bridge deflection. A useful report might say: under the stated elastic model, with parameters taken as exact input values, the discrete computation differs from the continuum model by no more than a given tolerance; the linear solve has a verified residual and a derived error bound; sensitivity analysis shows how the prediction changes over the measurement ranges. That does not prove the physical bridge will move by exactly that amount. It states what the mathematics and data do, and do not, establish.

Or return to the square root of two. An honest output might be an interval from one point four one four two to one point four one four three, established by squaring the endpoints exactly and checking which side of two each square lands on. The interval is much more informative than a long string of digits with no provenance.

Numerical analysis is the mathematics of that provenance. It asks what quantity we meant, what perturbations matter, what our algorithm actually did, and which claims survive finite computation. The answer on the screen is a beginning. Reliability comes from the chain of reasoning attached to it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Targets and error budgets.** Let \(q_{\rm phys}\) be the physical target, \(q_M\) the model result using ideal input, \(q_D\) the result using available input data, \(q_h\) the solution of a discretized problem, and \(\hat q\) the computed output. In one compatible norm,

\[
\|q_{\rm phys}-\hat q\| \le \|q_{\rm phys}-q_M\|+\|q_M-q_D\|+\|q_D-q_h\|+\|q_h-\hat q\|.
\]

The final term can be further subdivided into iteration and rounding errors, with care over the intermediate comparison quantity. The first term is usually *not* rigorously known from numerical analysis alone.

**Absolute and relative forward error.** \(e_{\rm abs}=\|\hat x-x\|\), \(e_{\rm rel}=\|\hat x-x\|/\|x\|\) when \(x\ne0\). A typical scale-aware goal is \(e\le \varepsilon_{\rm abs}+\varepsilon_{\rm rel}\|x\|\), but the quantity \(e\) must itself be bounded or otherwise justified.

**Residual.** For \(F(x)=0\), \(r=F(\hat x)\). If \(F\) is differentiable on the interval between \(x_*\) and \(\hat x\), and \(|F'(t)|\ge m>0\) there, the Mean Value Theorem gives \(|\hat x-x_*|\le |r|/m\). This assumes the residual is evaluated accurately enough for the claimed numerical bound.

**A root bracket with exact endpoint checks.**
\[
1.4142^2=1.99996164 < 2,\qquad 1.4143^2=2.00024449>2.
\]
Thus \(1.4142<\sqrt2<1.4143\), from monotonicity of squaring on positive reals. The interval width is \(10^{-4}\); its midpoint has absolute error at most \(5\cdot10^{-5}\).

**Small residual, larger error.** For \(F(x)=x^2\) and \(x_*=0\), \(\hat x=10^{-6}\), the residual has magnitude \(10^{-12}\), but the forward error is \(10^{-6}\). No positive lower derivative bound holds near the root.

### Exercises with answers

1. **Measurement:** A length is rounded to the nearest 0.01 meter. What can the printed value alone tell you? **Answer:** Under the specified rounding rule and absent other errors, the pre-rounded length lies within 0.005 meter of it; this is not a statement about instrument calibration or model uncertainty.
2. **Residual:** Why does \(\|Ax-b\|\) alone not bound \(\|x-x_*\|\) by a small number? **Answer:** \(x-x_*=A^{-1}(Ax-b)\); the inverse may have a large norm when \(A\) is ill-conditioned.
3. **Stopping:** Why might \(|x_{n+1}-x_n|<10^{-8}\) fail to certify a root? **Answer:** The iteration can stagnate or converge to the wrong fixed point, and there is no general error bound from one successive difference.
4. **Claim:** Does increasing arithmetic precision eliminate model error? **Answer:** No. It changes the arithmetic treatment of the given mathematical model, not the model's relationship to physical reality.

### References

- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd edition, SIAM (2002), chapter 1.
- James Demmel, *Applied Numerical Linear Algebra*, SIAM (1997), chapters 1–2.
- MIT OpenCourseWare, *18.330 Introduction to Numerical Analysis* (Spring 2012): course notes and problem sets.
