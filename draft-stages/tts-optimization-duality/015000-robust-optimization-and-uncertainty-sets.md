# 015000 — Robust Optimization: Worst-Case Constraints and Tractable Reformulations

**Track:** Optimization and Duality. **Background:** linear programming, convexity, norms, support functions and conic optimization. **Central question:** how should we optimize when the coefficients of a constraint are not known exactly?

<!-- BEGIN SPOKEN LECTURE -->

# Robust Optimization and the Geometry of Uncertainty

Many optimization problems are solved with numbers that are only estimates. A supplier quotes a range of possible costs. A physical system has uncertain material parameters. A sensor calibration is known only up to an error tolerance. Optimizing as though every coefficient were exact may produce a solution that looks ideal in the model but violates a constraint in reality.

Robust optimization takes a direct approach. Instead of selecting one presumed coefficient value, it specifies a set of possible values and requires the constraints to hold for all of them. This changes the question from, “What is optimal for the nominal model?” to, “What remains feasible under every allowed realization?”

The resulting model can be conservative, but it is mathematically clear. The guarantee is conditional on the uncertainty set: if reality lies outside that set, the robust feasibility certificate no longer applies.

## A simple uncertain capacity constraint

Suppose the amount of a resource consumed per item is uncertain. The nominal estimate is three units per item, but the actual value can be anywhere from two to four. We have twelve units of resource available and want to produce as many items as possible.

If we trust the nominal coefficient three, we might plan four items. But at the worst allowed coefficient four, those items consume sixteen units and violate capacity. Requiring feasibility for every coefficient in the interval forces us to plan no more than three items.

The arithmetic is simple, yet the model illustrates the essential distinction. A nominal optimum is a property of one selected scenario. A robust optimum is a property of the entire prescribed uncertainty set.

An important choice is which quantities are uncertain. If an uncertain coefficient multiplies a nonnegative decision, the worst coefficient is its upper endpoint. With decisions that can be negative, the endpoint maximizing the product can switch. The correct robust formula is obtained by optimizing over the uncertainty set, not by mechanically replacing every coefficient with its maximum.

## Support functions remove the infinity of constraints

Consider a linear inequality whose coefficient vector can vary within a set. The robust requirement contains an apparently infinite family of inequalities: one for every allowed vector. Convex analysis provides a compact description through the support function of the uncertainty set.

Suppose the uncertain coefficient vector equals a nominal vector plus a matrix times a disturbance vector. If the disturbance may lie in the unit Euclidean ball, then the worst possible additional contribution to a decision vector x is the Euclidean norm of the matrix transpose times x.

The robust inequality becomes a nominal linear term plus a norm term bounded by the capacity. That is a second-order cone constraint, a standard convex constraint that can be handled by conic optimization methods.

Why does a norm appear? Because the largest inner product between a fixed vector and a unit vector is the length of the fixed vector, achieved when the unit vector points in the same direction. Cauchy–Schwarz is doing the entire worst-case calculation.

If the uncertainty is instead a box, with each component independently allowed to vary within a specified interval, the support function produces a sum of absolute values. Different uncertainty sets therefore produce different optimization penalties. Geometry of uncertainty becomes geometry of a norm or support function in the robust counterpart.

## A worked two-coordinate example

Imagine a nominal constraint with coefficients two and one on two nonnegative decisions. Suppose both coefficients have independent uncertainty of radius one half. A box uncertainty set allows each coefficient to move to its unfavorable endpoint independently. The robust constraint then becomes two and a half times the first decision plus one and a half times the second, bounded by the same capacity.

If instead the two coefficient errors must lie in a Euclidean ball of radius one half, they cannot both attain their individual maximum at once. The robust penalty is half the Euclidean length of the two-decision vector. For many decisions this is smaller than the box penalty.

Neither model is universally better. The box expresses independent worst-case component bounds. The ball expresses a coupled restriction on the total disturbance size. Choosing between them should reflect the information available about the uncertain parameters, not a desire for whichever optimization answer looks most favorable.

## Robust feasibility is not probability

A robust constraint holds for every member of its uncertainty set. It does not say how likely those members are. By contrast, a chance constraint allows a specified small probability of violation under an explicit probability distribution. Stochastic programming often optimizes an expected cost over scenarios.

These are different mathematical questions. A robust model may impose severe restrictions to protect against unlikely combinations of errors. A chance-constrained model may accept carefully controlled failure probability, but only if its probabilistic assumptions are credible. A distributionally robust model goes further by allowing uncertainty about the probability distribution itself.

The nominal model, the uncertainty set, and the risk criterion should therefore be treated as separate modeling decisions. A solver can verify an exact robust counterpart without validating whether the uncertainty set corresponds to the physical world.

## Convexity, certificates, and limits

When a robust linear constraint is obtained by intersecting linear inequalities over all uncertainty realizations, the feasible set remains convex. If the uncertainty set has a tractable support function, we can often write a finite convex formulation and solve it using algorithms already developed for conic optimization.

But not every robust optimization model is easy. Uncertainty entering nonlinear or matrix-valued expressions can make worst-case evaluation difficult, and the geometry of the uncertainty set may prevent a simple reformulation. Some models are tractable only through conservative approximations rather than an exact equivalent problem.

The careful workflow is to define the uncertainty set, derive the worst-case expression, decide whether the reformulation is exact or approximate, and then compute the optimum together with a certificate of feasibility. If those steps are separated, we know exactly which part of the guarantee comes from mathematics and which part comes from our assumptions about uncertainty.

Robust optimization is ultimately a form of honest modeling. It does not eliminate unknown parameters. It turns the unknowns into explicit sets and asks how a decision behaves across them. Convex duality and support functions make that demanding requirement computationally manageable in many important cases.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For uncertain coefficient \(a=a_0+Pu\), \(\|u\|_2\le1\), the robust linear inequality is
\[a^Tx\le b\quad\forall u:\|u\|_2\le1\iff a_0^Tx+\|P^Tx\|_2\le b.\]
Indeed \(\sup_{\|u\|_2\le1}u^T(P^Tx)=\|P^Tx\|_2\) by Cauchy–Schwarz. The right side is a convex second-order cone constraint in x. For box uncertainty \(a=a_0+\operatorname{diag}(\rho)u\), \(\|u\|_\infty\le1\), the robust counterpart is \(a_0^Tx+\sum_i\rho_i|x_i|\le b\) for \(\rho_i\ge0\).

**Scalar example:** optimize \(\max x\) subject to \(x\ge0\) and \(ax\le12\) for every \(a\in[2,4]\). The robust constraint is \(4x\le12\), giving \(x^*=3\), while the nominal choice a=3 gives x=4, which is not robust-feasible. Without \(x\ge0\), the exact robust inequality is \(3x+|x|\le12\), not automatically \(4x\le12\) for negative x.

**Two-coordinate example:** nominal \(a_0=(2,1)\), uncertainty \(\delta\in[-1/2,1/2]^2\) yields \(2x_1+x_2+\tfrac12(|x_1|+|x_2|)\le b\). If \(\|\delta\|_2\le1/2\), the exact reformulation is \(2x_1+x_2+\tfrac12\sqrt{x_1^2+x_2^2}\le b\). These sets encode different information about simultaneous errors.

A robust guarantee is conditional on \(a\in\mathcal U\); it is not a distribution-free empirical claim that physical coefficients actually lie there. For more general uncertain nonlinear programs, tractability and exactness require separate analysis.

### Exercises with answers

1. Find the robust maximum x if \(x\ge0\), \(a\in[5,6]\), and \(ax\le30\) for all a. **Answer:** 5.
2. Evaluate \(\sup_{\|u\|_2\le1}u^Ty\). **Answer:** \(\|y\|_2\), with the maximum at \(u=y/\|y\|\) if y is nonzero.
3. What penalty results from independent componentwise uncertainties of radii \(\rho_i\)? **Answer:** \(\sum_i\rho_i|x_i|\).
4. Does robust feasibility with respect to a set imply a one-percent probability of failure? **Answer:** no; it has no probabilistic meaning without a probability model.

### Reading and source notes

- [Ben-Tal and Nemirovski, Robust Convex Optimization](https://www2.isye.gatech.edu/~nemirovs/robmp.pdf), robust convex formulations and ellipsoidal uncertainty.
- [Ben-Tal and Nemirovski, Robust Solutions of Uncertain Linear Programs](https://www2.isye.gatech.edu/~nemirovs/stablpn.pdf), exact conic quadratic robust counterparts.
