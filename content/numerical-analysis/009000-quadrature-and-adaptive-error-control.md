# Quadrature and adaptive error control

<!-- BEGIN SPOKEN LECTURE -->

# Quadrature and adaptive error control

## Numerical Integration: Accuracy, Quadrature, and Honest Error Estimates

An integral describes accumulated area, mass, probability, or total work. But in scientific computing, the function being integrated may be available only through a simulation, an experiment, or an expensive numerical routine. We cannot take infinitely many samples. We must choose a finite number of evaluation points and weights, calculate a weighted sum, and decide how much faith to put in it.

This is numerical quadrature. Its central question is not simply which rule produces a good approximation in an example. It is what properties of the integrand justify an error estimate, and what can go wrong when those properties are absent.

### The trapezoid rule from interpolation

Suppose we want the integral of a function f from a to b. Approximate f by the straight line joining its endpoint values. The area under that line is the interval width times the average of the endpoint heights. This is the trapezoid rule.

Consider f of x equal to x squared from zero to one. The true integral is one-third. With just the endpoints, the trapezoid rule gives one-half, an error of one-sixth. Now divide the interval into two equal panels and apply a trapezoid to each. Sampling at zero, one-half, and one gives three-eighths, or zero point three seven five. The absolute error is one twenty-fourth, four times smaller than before.

That reduction is not accidental. For a twice continuously differentiable function on the interval, a uniform composite trapezoid rule with panel width h has an absolute error bounded by the interval length times h squared over twelve times the maximum absolute second derivative. In the x squared example, the second derivative is the constant two, and the bound is exact. Halving the panel width reduces the bound by a factor of four.

Notice the hypothesis. The rule does not know whether the function is smooth from its sample values alone. The error theorem requires an independent statement about the second derivative. If the function has a sharp unresolved spike, uniform samples can miss it completely.

### Higher-order polynomial approximation

Instead of drawing a line through two endpoints, Simpson's rule fits a quadratic through three equally spaced points. Over a panel with midpoint m, its approximation is the panel width divided by six times f at the left endpoint plus four times f at the midpoint plus f at the right endpoint.

For x squared, Simpson's rule gives the exact integral with one panel, because the interpolating quadratic is the original function. In fact the rule is exact for every polynomial of degree at most three, even though the interpolation uses only a degree-two polynomial. The extra degree of exactness comes from symmetry: the interpolation error for a cubic is odd about the midpoint and integrates to zero.

For sufficiently smooth functions, the composite Simpson rule has an error bound proportional to h to the fourth power, with a bound involving the fourth derivative. If an integrand is smooth and function evaluations are well behaved, doubling the number of panels can reduce truncation error substantially faster than for trapezoids.

But higher polynomial degree is not a universal improvement. Interpolation at badly chosen nodes can become unstable, and numerical integration may be dominated by nonsmooth features rather than by polynomial approximation order. The lesson from the interpolation lecture applies again: approximation schemes are good only in relation to the regularity and structure of the problem.

### Choosing sample points deliberately

A Gaussian quadrature rule chooses both nodes and weights to maximize polynomial exactness. With n appropriately chosen nodes on an interval and a suitable weight function, Gauss quadrature integrates polynomials of degree up to two n minus one exactly. This is more than a rule using fixed equally spaced nodes can generally promise with the same number of evaluations.

For the simplest two-point Gauss rule on the interval from negative one to one, sample at positive and negative one over the square root of three, and add the two values with weight one each. Constant and linear functions are integrated correctly. So are quadratics and cubics. For x to the fourth, however, the true integral is two-fifths, while the rule gives two-ninths. No finite rule is exact for every smooth function.

Why is the degree of exactness doubled? The Gauss nodes are roots of an orthogonal polynomial of degree n. Any polynomial of degree at most two n minus one can be divided by that orthogonal polynomial, leaving a remainder of degree less than n. Orthogonality makes the integral of the polynomial multiple vanish, while evaluation at the roots makes its quadrature sum vanish. The remainder is integrated exactly by the chosen n weights. Both parts therefore agree between the exact integral and the quadrature rule.

The construction is elegant, but it rests on the correct interval, weight function, and orthogonal polynomial family. There is no single universal list of Gaussian nodes for every integration problem.

### Local refinement and adaptive quadrature

Uniform sampling spends the same effort everywhere. If a function is nearly flat over most of an interval but changes rapidly in one small region, it is more efficient to refine locally.

Adaptive quadrature typically begins by computing an estimate over a panel and comparing it with estimates obtained from subdivided panels. A large discrepancy suggests the panel needs further subdivision. A small discrepancy suggests the panel may be adequate. An adaptive rule recursively allocates samples where its error indicators report difficulty.

The word indicator is important. Comparing two approximations does not automatically give a rigorous upper bound on the true error. Both estimates may miss the same narrow peak. For example, a smooth bump supported in a tiny interval between all sampled points can make every observed function value zero while the exact integral is positive. No algorithm that samples only those points can distinguish this bump from the zero function without additional assumptions.

A defensible error certificate therefore needs a condition on the function, such as a derivative bound, analyticity information, an interval enclosure, or a trusted adaptive estimator operating under validated assumptions. Empirical agreement between refinements is useful evidence, but not the same as a proof.

### Extrapolation and its limits

If we know the leading trapezoid error behaves like a constant times h squared plus higher-order terms, then evaluating the rule at widths h and h over two lets us cancel the leading term. Four times the fine estimate minus the coarse estimate, divided by three, eliminates the h-squared contribution. This is Richardson extrapolation, and its idea appears in higher-order quadrature schemes and error estimation.

The phrase *if we know* is carrying substantial weight. The cancellation argument assumes a valid asymptotic error expansion and a sufficiently small h. Applying it to a discontinuous or singular integrand may not deliver the advertised order. Even for smooth functions, subtracting nearly equal floating-point numbers can make roundoff important when refinement is pushed too far.

A complete numerical-integration error budget also includes the accuracy of the function evaluations themselves. If a simulator returns values with uncertainty, the quadrature method does not magically recover digits the simulator never supplied. Uncertainty in sample values is propagated through the weights, and for weights of mixed signs that propagation can amplify errors.

### Integrating with an argument, not just a number

The trapezoid rule, Simpson's rule, and Gaussian quadrature each exploit polynomial structure differently. Adaptive methods exploit uneven difficulty across the domain. Error certificates exploit mathematical information about the integrand. These are complementary tools, not a ranking in which one method always wins.

A trustworthy numerical integral comes with the integrand's domain and assumptions, the evaluation strategy, a distinction between estimated and certified error, and a stopping rule tied to the question being asked. The goal is not only to get close to the true integral. It is to know what warrants the claim that we are close.

## Adaptive Quadrature: Spend Computation Where the Integral Is Difficult

Suppose we want the area under a function over a long interval. On most of that interval the function changes gently, but in one small region it rises into a narrow peak. Sampling every part of the interval at the same fine resolution wastes effort in the smooth regions. Sampling uniformly at a coarse resolution may miss the peak altogether. This is the problem adaptive quadrature tries to solve: spend more work where the numerical approximation appears unreliable.

But the word appears is crucial. An adaptive integrator has information only at the points it samples. It must estimate the unseen error from those observations. If the assumptions behind the estimate fail, the integrator can confidently report an answer that is wrong.

### Start with two approximations

Consider Simpson's rule on an interval from a to b. Evaluate the function at the left endpoint, midpoint, and right endpoint. Combine those values with weights one, four, and one, then multiply by the interval length divided by six. For a polynomial of degree at most three, this rule is exact in exact arithmetic.

Now divide the interval into two halves. Apply Simpson's rule to each half separately and add the results. The new approximation uses additional samples at the quarter points. We have a coarse estimate and a refined estimate of the same integral.

If the function is smooth enough, the dominant Simpson error on an interval scales with the fifth power of its length. Splitting an interval into two halves reduces the leading total error by a factor of sixteen. The difference between the refined estimate and the coarse estimate is therefore about fifteen times the refined estimate's leading error, with the sign determined by the function's curvature at higher order.

This motivates a local error estimator: take the absolute difference between the coarse and refined Simpson results, then divide by fifteen. If that quantity is smaller than the allowed error budget for the interval, accept the refined result. Otherwise subdivide again and repeat.

The division by fifteen is not a universal law of integration. It comes from a smoothness assumption and the leading-order error model for Simpson's rule. If the integrand has a kink, an endpoint singularity, sharp oscillations, or a narrow feature that sampling misses, the estimate may be misleading.

### An example with a checkable answer

Integrate x to the fourth power from zero to one. The exact answer is one fifth, or 0.2. A single Simpson panel gives approximately 0.208333. Splitting into two Simpson panels gives approximately 0.200521. The difference is 0.0078125. Divide by fifteen and obtain about 0.000520833. That is exactly the error of the refined Simpson result for this polynomial.

There is a reason for the exact agreement in this example. The fourth derivative of x to the fourth power is constant, so the leading Simpson error model has no higher-order variation to hide. We could even use the estimated signed correction to improve the refined answer to exactly 0.2 in exact arithmetic.

On a general smooth function, the correction is an asymptotic estimate, not an identity. It becomes reliable when the leading error term dominates and the function is adequately resolved. The example shows how refinement can provide information about error, while also showing why that information has mathematical assumptions.

### How recursion allocates effort

A practical adaptive Simpson algorithm starts with a total absolute error budget. It estimates the local error on the whole interval. If the error looks acceptable, it returns a result. Otherwise it splits the interval, assigns a portion of the error budget to each child, and applies the same reasoning recursively.

If the individual accepted local errors truly do not exceed their assigned budgets, the triangle inequality bounds the total absolute error by the sum of those budgets. One common implementation gives each half half of the parent's budget, so the sum of budgets remains controlled. But that conclusion is conditional on the reliability of each local error bound. The computed Simpson differences are usually estimators, not proven upper bounds.

This distinction separates two problems. The algorithmic scheduling problem asks where to place additional samples. The certification problem asks whether the reported uncertainty rigorously encloses the true integral. Adaptive subdivision helps with the first. It does not, by itself, solve the second.

### A sampled function can hide information

Imagine a smooth function with a narrow peak centered at a point none of our initial samples hit. If the function is nearly zero at all the sampled points, the coarse and refined estimates may both be nearly zero. Their difference is also nearly zero. The algorithm sees no reason to refine and can completely miss the integral of the peak.

This is not just a hypothetical worry. Numerical integration libraries warn that finite sampling cannot guarantee accuracy for an arbitrary integrand. SciPy's integration tutorial gives a Gaussian example on an extremely wide interval where the adaptive routine returns a nearly zero integral because it misses the region where the function is concentrated. Changing the interval to focus on the significant region resolves the issue.

The lesson is not that adaptive quadrature is unreliable in normal use. It is that a numerical estimator is evidence about behavior at sampled scales, not omniscience about all unobserved scales. If we know where a function changes rapidly, splitting at that location or providing breakpoints is often more valuable than merely requesting a smaller tolerance.

### Embedded rules and Gaussian ideas

Adaptive Simpson is easy to derive, but modern integrators often use more efficient pairs of quadrature rules. A Gauss rule chooses sample points and weights to integrate polynomials of high degree exactly. A Kronrod extension supplements a Gauss rule with additional points, creating two approximations of different nominal accuracy that share work.

The difference between these approximations becomes an error indicator. An adaptive routine then decides which subinterval has the largest estimated contribution to the total error, subdivides it, and repeats. This allocation is global in the sense that the integrator can compare competing intervals and spend effort where the estimated payoff is largest.

For smooth functions, such methods can converge rapidly. Their performance changes for oscillatory functions, discontinuities, improper integrals, cancellation, or integrable singularities. Different transformations or specialized quadrature rules may be appropriate in those regimes.

### Floating-point error joins truncation error

Refinement cannot continue indefinitely without cost. Each added function evaluation incurs rounding, and subtracting nearby coarse and refined approximations can lose significant digits. If the quadrature error has become smaller than the floating-point noise, the estimated difference may stop improving meaningfully. Function evaluations themselves may be noisy or costly, especially when each evaluation invokes a simulation or iterative solver.

Stopping decisions should therefore consider absolute tolerance, relative tolerance, evaluation budgets, and warning flags. A relative tolerance alone is difficult when the true integral is near zero, because any small absolute error can correspond to an enormous relative error. An absolute tolerance provides an independent scale.

A solver's claim that it met a requested tolerance is normally a statement about its internal estimator and numerical model. It is not automatically a formal proof that the mathematical error lies inside that tolerance. For rigorous certification one needs stronger information, such as proven derivative bounds, interval enclosures, analytically controlled tails, or a validated numerical method.

### Know what the algorithm can observe

Adaptive quadrature is an example of intelligent resource allocation in numerical mathematics. We compare approximations, infer where our present representation is weak, and refine locally. But we must distinguish a detected discrepancy from a guarantee that no discrepancy remains.

For a trustworthy integral, pair the estimator with knowledge of the function. Ask whether there are narrow features, singularities, oscillations, or regions far from the sampled points that could matter. Check convergence under independent refinements or transformations when the answer is consequential. And when a proof is required, use a method that certifies a bound rather than one that merely estimates it.

The algorithm chooses where to look. Mathematical analysis tells us how much confidence that choice deserves.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Numerical Integration: Accuracy, Quadrature, and Honest Error Estimates

**Track:** Numerical Analysis and Reliable Computation. **Background:** interpolation, derivatives, finite precision, and approximation error. **Question:** how can finitely many samples estimate a continuous integral, and when can that estimate be trusted?

#### Mathematical companion (not spoken)

Let \(h=(b-a)/n\) and \(f_j=f(a+jh)\). The composite trapezoid rule is
\[
T_n=h\left(\tfrac12f_0+\sum_{j=1}^{n-1}f_j+\tfrac12f_n\right),\qquad
\left|\int_a^bf-T_n\right|\le\frac{(b-a)h^2}{12}\max_{[a,b]}|f''|.
\]
For even \(n\), composite Simpson:
\[
S_n=\frac h3\left(f_0+f_n+4\sum_{j\ \mathrm{odd}}f_j+2\sum_{0<j<n,\ j\ \mathrm{even}}f_j\right),
\]
\[
\left|\int_a^bf-S_n\right|\le\frac{(b-a)h^4}{180}\max_{[a,b]}|f^{(4)}|.
\]
These bounds require the indicated continuous derivatives.

**Two-point Gauss–Legendre:**
\[
\int_{-1}^{1}f(x)\,dx\approx f(-1/\sqrt3)+f(1/\sqrt3),
\]
exact for degree \(\le3\); for \(f(x)=x^4\), exact integral is \(2/5\) and approximation \(2/9\).

**Trapezoid Richardson combination:** \(R=(4T_{2n}-T_n)/3\), which cancels a leading \(c h^2\) term under a valid smooth-error expansion.

##### Exercises with answers

1. Apply one trapezoid to \(f(x)=x^2\) on \([0,1]\). **Answer:** \(1/2\), versus exact \(1/3\).
2. Apply composite trapezoid with \(n=2\). **Answer:** \(3/8\), absolute error \(1/24\).
3. Does two-point Gauss–Legendre integrate \(x^3\) exactly? **Answer:** yes; both integral and approximation are zero.
4. Why doesn't agreement of two adaptive estimates prove a bound? **Answer:** both may miss a narrow feature between samples.

##### Reading

MIT OCW 18.330, numerical integration lecture notes; Trefethen, *Approximation Theory and Approximation Practice*, chapters on Gauss and Clenshaw–Curtis quadrature; Burden, Faires and Burden, *Numerical Analysis*.

### Adaptive Quadrature: Spend Computation Where the Integral Is Difficult

**Track:** Numerical Analysis and Reliable Computation. **Background:** Simpson's rule, local truncation error, and floating-point conditioning. **Central question:** how can an integrator choose where to sample, and when should we trust its error estimate?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Why the factor fifteen for refinement from one Simpson panel to two? **Answer:** the leading fine error is \(1/16\) of the coarse error, making their difference \(15\) times the leading fine error in magnitude.
2. Can two agreeing quadrature rules prove there is no peak between their nodes? **No:** finite samples can miss concentrated features.
3. Why supplement relative error tolerance with absolute tolerance? **Answer:** a near-zero true integral can make relative error poorly scaled or undefined.
4. What makes an error *certificate* stronger than an estimator? **Answer:** an independently justified upper bound enclosing the true mathematical error under explicit hypotheses.

##### Reading and source notes

- SciPy, [Integration tutorial](https://docs.scipy.org/doc/scipy/tutorial/integrate.html), examples and warning about missed features.
- SciPy, [`integrate.quad` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html), error estimates, tolerance semantics, and adaptive routines.
