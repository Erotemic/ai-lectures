# 009000 — Numerical Integration: Accuracy, Quadrature, and Honest Error Estimates

**Track:** Numerical Analysis and Reliable Computation. **Background:** interpolation, derivatives, finite precision, and approximation error. **Question:** how can finitely many samples estimate a continuous integral, and when can that estimate be trusted?

<!-- BEGIN SPOKEN LECTURE -->

# Numerical Integration: Accuracy, Quadrature, and Honest Error Estimates

An integral describes accumulated area, mass, probability, or total work. But in scientific computing, the function being integrated may be available only through a simulation, an experiment, or an expensive numerical routine. We cannot take infinitely many samples. We must choose a finite number of evaluation points and weights, calculate a weighted sum, and decide how much faith to put in it.

This is numerical quadrature. Its central question is not simply which rule produces a good approximation in an example. It is what properties of the integrand justify an error estimate, and what can go wrong when those properties are absent.

## The trapezoid rule from interpolation

Suppose we want the integral of a function f from a to b. Approximate f by the straight line joining its endpoint values. The area under that line is the interval width times the average of the endpoint heights. This is the trapezoid rule.

Consider f of x equal to x squared from zero to one. The true integral is one-third. With just the endpoints, the trapezoid rule gives one-half, an error of one-sixth. Now divide the interval into two equal panels and apply a trapezoid to each. Sampling at zero, one-half, and one gives three-eighths, or zero point three seven five. The absolute error is one twenty-fourth, four times smaller than before.

That reduction is not accidental. For a twice continuously differentiable function on the interval, a uniform composite trapezoid rule with panel width h has an absolute error bounded by the interval length times h squared over twelve times the maximum absolute second derivative. In the x squared example, the second derivative is the constant two, and the bound is exact. Halving the panel width reduces the bound by a factor of four.

Notice the hypothesis. The rule does not know whether the function is smooth from its sample values alone. The error theorem requires an independent statement about the second derivative. If the function has a sharp unresolved spike, uniform samples can miss it completely.

## Higher-order polynomial approximation

Instead of drawing a line through two endpoints, Simpson's rule fits a quadratic through three equally spaced points. Over a panel with midpoint m, its approximation is the panel width divided by six times f at the left endpoint plus four times f at the midpoint plus f at the right endpoint.

For x squared, Simpson's rule gives the exact integral with one panel, because the interpolating quadratic is the original function. In fact the rule is exact for every polynomial of degree at most three, even though the interpolation uses only a degree-two polynomial. The extra degree of exactness comes from symmetry: the interpolation error for a cubic is odd about the midpoint and integrates to zero.

For sufficiently smooth functions, the composite Simpson rule has an error bound proportional to h to the fourth power, with a bound involving the fourth derivative. If an integrand is smooth and function evaluations are well behaved, doubling the number of panels can reduce truncation error substantially faster than for trapezoids.

But higher polynomial degree is not a universal improvement. Interpolation at badly chosen nodes can become unstable, and numerical integration may be dominated by nonsmooth features rather than by polynomial approximation order. The lesson from the interpolation lecture applies again: approximation schemes are good only in relation to the regularity and structure of the problem.

## Choosing sample points deliberately

A Gaussian quadrature rule chooses both nodes and weights to maximize polynomial exactness. With n appropriately chosen nodes on an interval and a suitable weight function, Gauss quadrature integrates polynomials of degree up to two n minus one exactly. This is more than a rule using fixed equally spaced nodes can generally promise with the same number of evaluations.

For the simplest two-point Gauss rule on the interval from negative one to one, sample at positive and negative one over the square root of three, and add the two values with weight one each. Constant and linear functions are integrated correctly. So are quadratics and cubics. For x to the fourth, however, the true integral is two-fifths, while the rule gives two-ninths. No finite rule is exact for every smooth function.

Why is the degree of exactness doubled? The Gauss nodes are roots of an orthogonal polynomial of degree n. Any polynomial of degree at most two n minus one can be divided by that orthogonal polynomial, leaving a remainder of degree less than n. Orthogonality makes the integral of the polynomial multiple vanish, while evaluation at the roots makes its quadrature sum vanish. The remainder is integrated exactly by the chosen n weights. Both parts therefore agree between the exact integral and the quadrature rule.

The construction is elegant, but it rests on the correct interval, weight function, and orthogonal polynomial family. There is no single universal list of Gaussian nodes for every integration problem.

## Local refinement and adaptive quadrature

Uniform sampling spends the same effort everywhere. If a function is nearly flat over most of an interval but changes rapidly in one small region, it is more efficient to refine locally.

Adaptive quadrature typically begins by computing an estimate over a panel and comparing it with estimates obtained from subdivided panels. A large discrepancy suggests the panel needs further subdivision. A small discrepancy suggests the panel may be adequate. An adaptive rule recursively allocates samples where its error indicators report difficulty.

The word indicator is important. Comparing two approximations does not automatically give a rigorous upper bound on the true error. Both estimates may miss the same narrow peak. For example, a smooth bump supported in a tiny interval between all sampled points can make every observed function value zero while the exact integral is positive. No algorithm that samples only those points can distinguish this bump from the zero function without additional assumptions.

A defensible error certificate therefore needs a condition on the function, such as a derivative bound, analyticity information, an interval enclosure, or a trusted adaptive estimator operating under validated assumptions. Empirical agreement between refinements is useful evidence, but not the same as a proof.

## Extrapolation and its limits

If we know the leading trapezoid error behaves like a constant times h squared plus higher-order terms, then evaluating the rule at widths h and h over two lets us cancel the leading term. Four times the fine estimate minus the coarse estimate, divided by three, eliminates the h-squared contribution. This is Richardson extrapolation, and its idea appears in higher-order quadrature schemes and error estimation.

The phrase *if we know* is carrying substantial weight. The cancellation argument assumes a valid asymptotic error expansion and a sufficiently small h. Applying it to a discontinuous or singular integrand may not deliver the advertised order. Even for smooth functions, subtracting nearly equal floating-point numbers can make roundoff important when refinement is pushed too far.

A complete numerical-integration error budget also includes the accuracy of the function evaluations themselves. If a simulator returns values with uncertainty, the quadrature method does not magically recover digits the simulator never supplied. Uncertainty in sample values is propagated through the weights, and for weights of mixed signs that propagation can amplify errors.

## Integrating with an argument, not just a number

The trapezoid rule, Simpson's rule, and Gaussian quadrature each exploit polynomial structure differently. Adaptive methods exploit uneven difficulty across the domain. Error certificates exploit mathematical information about the integrand. These are complementary tools, not a ranking in which one method always wins.

A trustworthy numerical integral comes with the integrand's domain and assumptions, the evaluation strategy, a distinction between estimated and certified error, and a stopping rule tied to the question being asked. The goal is not only to get close to the true integral. It is to know what warrants the claim that we are close.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Apply one trapezoid to \(f(x)=x^2\) on \([0,1]\). **Answer:** \(1/2\), versus exact \(1/3\).
2. Apply composite trapezoid with \(n=2\). **Answer:** \(3/8\), absolute error \(1/24\).
3. Does two-point Gauss–Legendre integrate \(x^3\) exactly? **Answer:** yes; both integral and approximation are zero.
4. Why doesn't agreement of two adaptive estimates prove a bound? **Answer:** both may miss a narrow feature between samples.

### Reading

MIT OCW 18.330, numerical integration lecture notes; Trefethen, *Approximation Theory and Approximation Practice*, chapters on Gauss and Clenshaw–Curtis quadrature; Burden, Faires and Burden, *Numerical Analysis*.
