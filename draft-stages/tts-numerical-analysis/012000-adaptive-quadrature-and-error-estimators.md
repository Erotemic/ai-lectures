# 012000 — Adaptive Quadrature: Spend Computation Where the Integral Is Difficult

**Track:** Numerical Analysis and Reliable Computation. **Background:** Simpson's rule, local truncation error, and floating-point conditioning. **Central question:** how can an integrator choose where to sample, and when should we trust its error estimate?

<!-- BEGIN SPOKEN LECTURE -->

# Adaptive Quadrature: Spend Computation Where the Integral Is Difficult

Suppose we want the area under a function over a long interval. On most of that interval the function changes gently, but in one small region it rises into a narrow peak. Sampling every part of the interval at the same fine resolution wastes effort in the smooth regions. Sampling uniformly at a coarse resolution may miss the peak altogether. This is the problem adaptive quadrature tries to solve: spend more work where the numerical approximation appears unreliable.

But the word appears is crucial. An adaptive integrator has information only at the points it samples. It must estimate the unseen error from those observations. If the assumptions behind the estimate fail, the integrator can confidently report an answer that is wrong.

## Start with two approximations

Consider Simpson's rule on an interval from a to b. Evaluate the function at the left endpoint, midpoint, and right endpoint. Combine those values with weights one, four, and one, then multiply by the interval length divided by six. For a polynomial of degree at most three, this rule is exact in exact arithmetic.

Now divide the interval into two halves. Apply Simpson's rule to each half separately and add the results. The new approximation uses additional samples at the quarter points. We have a coarse estimate and a refined estimate of the same integral.

If the function is smooth enough, the dominant Simpson error on an interval scales with the fifth power of its length. Splitting an interval into two halves reduces the leading total error by a factor of sixteen. The difference between the refined estimate and the coarse estimate is therefore about fifteen times the refined estimate's leading error, with the sign determined by the function's curvature at higher order.

This motivates a local error estimator: take the absolute difference between the coarse and refined Simpson results, then divide by fifteen. If that quantity is smaller than the allowed error budget for the interval, accept the refined result. Otherwise subdivide again and repeat.

The division by fifteen is not a universal law of integration. It comes from a smoothness assumption and the leading-order error model for Simpson's rule. If the integrand has a kink, an endpoint singularity, sharp oscillations, or a narrow feature that sampling misses, the estimate may be misleading.

## An example with a checkable answer

Integrate x to the fourth power from zero to one. The exact answer is one fifth, or 0.2. A single Simpson panel gives approximately 0.208333. Splitting into two Simpson panels gives approximately 0.200521. The difference is 0.0078125. Divide by fifteen and obtain about 0.000520833. That is exactly the error of the refined Simpson result for this polynomial.

There is a reason for the exact agreement in this example. The fourth derivative of x to the fourth power is constant, so the leading Simpson error model has no higher-order variation to hide. We could even use the estimated signed correction to improve the refined answer to exactly 0.2 in exact arithmetic.

On a general smooth function, the correction is an asymptotic estimate, not an identity. It becomes reliable when the leading error term dominates and the function is adequately resolved. The example shows how refinement can provide information about error, while also showing why that information has mathematical assumptions.

## How recursion allocates effort

A practical adaptive Simpson algorithm starts with a total absolute error budget. It estimates the local error on the whole interval. If the error looks acceptable, it returns a result. Otherwise it splits the interval, assigns a portion of the error budget to each child, and applies the same reasoning recursively.

If the individual accepted local errors truly do not exceed their assigned budgets, the triangle inequality bounds the total absolute error by the sum of those budgets. One common implementation gives each half half of the parent's budget, so the sum of budgets remains controlled. But that conclusion is conditional on the reliability of each local error bound. The computed Simpson differences are usually estimators, not proven upper bounds.

This distinction separates two problems. The algorithmic scheduling problem asks where to place additional samples. The certification problem asks whether the reported uncertainty rigorously encloses the true integral. Adaptive subdivision helps with the first. It does not, by itself, solve the second.

## A sampled function can hide information

Imagine a smooth function with a narrow peak centered at a point none of our initial samples hit. If the function is nearly zero at all the sampled points, the coarse and refined estimates may both be nearly zero. Their difference is also nearly zero. The algorithm sees no reason to refine and can completely miss the integral of the peak.

This is not just a hypothetical worry. Numerical integration libraries warn that finite sampling cannot guarantee accuracy for an arbitrary integrand. SciPy's integration tutorial gives a Gaussian example on an extremely wide interval where the adaptive routine returns a nearly zero integral because it misses the region where the function is concentrated. Changing the interval to focus on the significant region resolves the issue.

The lesson is not that adaptive quadrature is unreliable in normal use. It is that a numerical estimator is evidence about behavior at sampled scales, not omniscience about all unobserved scales. If we know where a function changes rapidly, splitting at that location or providing breakpoints is often more valuable than merely requesting a smaller tolerance.

## Embedded rules and Gaussian ideas

Adaptive Simpson is easy to derive, but modern integrators often use more efficient pairs of quadrature rules. A Gauss rule chooses sample points and weights to integrate polynomials of high degree exactly. A Kronrod extension supplements a Gauss rule with additional points, creating two approximations of different nominal accuracy that share work.

The difference between these approximations becomes an error indicator. An adaptive routine then decides which subinterval has the largest estimated contribution to the total error, subdivides it, and repeats. This allocation is global in the sense that the integrator can compare competing intervals and spend effort where the estimated payoff is largest.

For smooth functions, such methods can converge rapidly. Their performance changes for oscillatory functions, discontinuities, improper integrals, cancellation, or integrable singularities. Different transformations or specialized quadrature rules may be appropriate in those regimes.

## Floating-point error joins truncation error

Refinement cannot continue indefinitely without cost. Each added function evaluation incurs rounding, and subtracting nearby coarse and refined approximations can lose significant digits. If the quadrature error has become smaller than the floating-point noise, the estimated difference may stop improving meaningfully. Function evaluations themselves may be noisy or costly, especially when each evaluation invokes a simulation or iterative solver.

Stopping decisions should therefore consider absolute tolerance, relative tolerance, evaluation budgets, and warning flags. A relative tolerance alone is difficult when the true integral is near zero, because any small absolute error can correspond to an enormous relative error. An absolute tolerance provides an independent scale.

A solver's claim that it met a requested tolerance is normally a statement about its internal estimator and numerical model. It is not automatically a formal proof that the mathematical error lies inside that tolerance. For rigorous certification one needs stronger information, such as proven derivative bounds, interval enclosures, analytically controlled tails, or a validated numerical method.

## Know what the algorithm can observe

Adaptive quadrature is an example of intelligent resource allocation in numerical mathematics. We compare approximations, infer where our present representation is weak, and refine locally. But we must distinguish a detected discrepancy from a guarantee that no discrepancy remains.

For a trustworthy integral, pair the estimator with knowledge of the function. Ask whether there are narrow features, singularities, oscillations, or regions far from the sampled points that could matter. Check convergence under independent refinements or transformations when the answer is consequential. And when a proof is required, use a method that certifies a bound rather than one that merely estimates it.

The algorithm chooses where to look. Mathematical analysis tells us how much confidence that choice deserves.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Single-panel Simpson rule on \([a,b]\):
\[
S[a,b]=\frac{b-a}{6}\left[f(a)+4f\left(\frac{a+b}{2}\right)+f(b)\right].
\]
Let \(m=(a+b)/2\), \(S_c=S[a,b]\), \(S_f=S[a,m]+S[m,b]\). Under sufficient smoothness in the asymptotic regime, the **estimated** fine-grid error is
\[
E_{\mathrm{est}}\approx\frac{|S_f-S_c|}{15}.
\]
This is not a rigorous upper bound without additional assumptions. For \(f(x)=x^4\) on \([0,1]\):
\[
I=\tfrac15=0.2,\quad S_c=\tfrac5{24}\approx0.2083333333,\quad
S_f=\tfrac{77}{384}\approx0.2005208333,
\]
\[
|S_f-S_c|/15=\tfrac1{1920}\approx0.0005208333,
\quad S_f-I=\tfrac1{1920}.
\]
The signed Richardson correction \(S_f+(S_f-S_c)/15=1/5\) is exact here because the leading fourth-derivative error is exact for a quartic.

**Global budgeting caveat.** If local errors satisfy proven \(|e_i|\le\varepsilon_i\) then \(|\sum e_i|\le\sum\varepsilon_i\). But replacing these proven inequalities with numerical **estimates** does not turn the global sum into a mathematical certificate.

**Practical limitations:** undersampling of narrow peaks; oscillatory cancellation; near-zero integrals under relative-error criteria; singularities; noisy function evaluations; roundoff floors. See the SciPy tutorial's wide-interval Gaussian counterexample.

### Exercises with answers

1. Why the factor fifteen for refinement from one Simpson panel to two? **Answer:** the leading fine error is \(1/16\) of the coarse error, making their difference \(15\) times the leading fine error in magnitude.
2. Can two agreeing quadrature rules prove there is no peak between their nodes? **No:** finite samples can miss concentrated features.
3. Why supplement relative error tolerance with absolute tolerance? **Answer:** a near-zero true integral can make relative error poorly scaled or undefined.
4. What makes an error *certificate* stronger than an estimator? **Answer:** an independently justified upper bound enclosing the true mathematical error under explicit hypotheses.

### Reading and source notes

- SciPy, [Integration tutorial](https://docs.scipy.org/doc/scipy/tutorial/integrate.html), examples and warning about missed features.
- SciPy, [`integrate.quad` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html), error estimates, tolerance semantics, and adaptive routines.
