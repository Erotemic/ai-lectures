# Sensitivity, robust uncertainty, and distributional risk

<!-- BEGIN SPOKEN LECTURE -->

# Sensitivity, robust uncertainty, and distributional risk

## Optimization Sensitivity: Perturbation Bounds and Shadow Prices

Suppose we have solved an optimization problem: minimize cost while satisfying a collection of resource limits. Now a customer offers to relax one limit slightly, or a regulator tightens it. How much should the optimal cost change? Do we need to solve the entire problem again to answer that question?

Convex duality offers an elegant first answer. The multipliers associated with constraints do more than certify optimality. Under the right conditions, they measure the sensitivity of the optimal value to changes in those constraints. But sensitivity is a local or bounded statement about a mathematically specified perturbation, not a license to treat every multiplier as a constant market price for arbitrary changes.

### Build a perturbed problem

Begin with a convex minimization problem. Let the objective be f zero of x. Let its inequality constraints be f i of x at most zero, and its equality constraints be h j of x equal to zero, with the equality functions affine.

Introduce parameters u and v. Replace each inequality bound zero with u i, and each equality bound zero with v j. The optimal value now becomes a function of these perturbations, called p star of u and v.

Positive u means relaxing an inequality: a constraint of the form f i of x at most u i admits a larger feasible set. Thus, if only one inequality is relaxed, the minimum cost cannot increase. A negative u tightens it and may raise cost or destroy feasibility. Equality perturbations are not naturally ordered in the same way.

This simple definition matters. The sign and interpretation of a multiplier depend on how the constraints were written. A resource lower bound, written as a negative inequality, gives the opposite apparent sign from a resource upper bound. Always return to the actual perturbation convention before interpreting a shadow price.

### Dual variables produce an affine bound

The Lagrangian adds each inequality violation, multiplied by a nonnegative multiplier lambda, and each equality residual multiplied by an unrestricted multiplier nu. When the right-hand sides shift to u and v, the Lagrangian picks up an additional constant: negative lambda dotted with u, minus nu dotted with v.

Assume the original problem has strong duality and an attained optimal dual solution, lambda star and nu star. Keep these multipliers fixed while we perturb the constraints. The resulting dual objective gives a lower bound on the perturbed primal optimum. That lower bound is the original optimal value minus lambda star dotted with u, minus nu star dotted with v.

This is a global affine lower bound on the perturbed optimal-value function, wherever that value is defined in the extended-real sense. It tells us how much improvement a relaxation can possibly buy relative to a known dual certificate. But by itself it is not an exact prediction of the new optimum.

### Sensitivity as a derivative

If the optimal-value function is differentiable at zero perturbation, the same multipliers identify its derivative. The partial derivative with respect to an inequality bound u i is negative lambda i star. The derivative with respect to an equality right-hand side v j is negative nu j star.

This is the mathematical meaning of a shadow price. A positive inequality multiplier describes the first-order decrease in cost as the corresponding upper bound is relaxed. If the constraint is inactive and standard complementary slackness applies, the multiplier is zero: a small relaxation of an already slack constraint does not provide immediate value through that multiplier.

If the value function is not differentiable, an optimal dual multiplier may still define a subgradient of the convex perturbation-value function, with a negative sign. Different optimal multipliers can encode different supporting slopes. In that case asking for a unique derivative may be the wrong question.

### A complete one-variable example

Minimize x squared subject to x being at least one. The optimal solution is x equal to one and the optimal value is one. Write the constraint as one minus x at most zero. The Lagrangian is x squared plus lambda times one minus x, where lambda must be nonnegative.

The stationarity condition requires twice x minus lambda to be zero. At the optimum x equals one, so lambda equals two. This multiplier predicts that relaxing the inequality upper bound by a small positive amount u reduces the optimal value at first order by two times u.

Check directly. The perturbed constraint is one minus x at most u, or x at least one minus u. For sufficiently small u, the new minimizer is one minus u, so the optimal value is one minus u, squared. Expand: one minus twice u plus u squared. The derivative at zero is negative two, exactly the negative of the multiplier.

We can also see why the multiplier is not an exact price for large changes. If u reaches one, the point x equal to zero becomes feasible, and the optimal cost becomes zero. Relaxing beyond that does not reduce it further. The linear prediction would keep decreasing without bound, which is impossible here. The affine inequality remains a valid lower bound; the first-order approximation has stopped being accurate.

### The optimal point can be much less stable than the value

Sensitivity of the optimal value is different from sensitivity of the optimizer itself. Consider minimizing a shallow quadratic: epsilon over two times x squared, minus b times x, where epsilon is a small positive number and b is a parameter. The minimizer is b divided by epsilon.

Change b by a small amount delta. The minimizer moves by delta divided by epsilon. If epsilon is tiny, even a modest input perturbation can move the optimizer dramatically. The objective is strictly convex and has a unique minimum, yet the location of that minimum is poorly conditioned with respect to the linear coefficient.

This is not a failure of convexity. Strict convexity guarantees uniqueness in this simple example. Strong curvature, or an appropriate second-order growth condition, is what provides quantitative stability. A small duality gap alone also does not guarantee an accurate optimizer when the objective is nearly flat.

### Constraints can change their active set

Real optimization problems often have multiple competing constraints. A small change may cause a previously inactive constraint to become active, or make an active one slack. Near such a transition, the value function can have a kink. Multipliers may fail to be unique, and derivatives may need to be replaced with directional derivatives or subgradients.

Constraint qualifications matter as well. Strong duality, dual attainment, and regularity are conditions to check, not assumptions to smuggle in because a numerical solver returned a vector called a multiplier. Degenerate constraints can give misleadingly large or nonunique multipliers even when the underlying optimal value is well behaved.

For numerical work, complementarity residuals, primal feasibility, dual feasibility, and conditioning must all be considered before attaching an economic interpretation to computed shadow prices. Units and scaling matter: doubling the units in which a constraint is measured changes the numerical multiplier inversely.

### Turning optimization output into useful knowledge

The dual certificate supplies a global inequality for the value of nearby or distant perturbed problems. Differentiability turns a multiplier into an exact first-order sensitivity. Strong curvature and regularity can make the optimizer stable as well. Without these additional hypotheses, a solver's reported multiplier is a potentially useful diagnostic, not an unconditional forecast.

This is how duality extends beyond proving that one solution is optimal. It can tell us what a small relaxation is worth, which constraints are binding, and where a computation is sensitive to uncertain input. The essential discipline is to distinguish a rigorous supporting bound, a local derivative, and an extrapolated prediction. They answer different questions.

## Perturbations, worst-case uncertainty, transport ambiguity, and tail risk

Sensitivity asks how an optimum responds to a specified perturbation. Robust optimization changes the decision question: can one choice withstand every perturbation in a stated uncertainty set?

### Robust Optimization: Worst-Case Constraints and Tractable Reformulations

Many optimization problems are solved with numbers that are only estimates. A supplier quotes a range of possible costs. A physical system has uncertain material parameters. A sensor calibration is known only up to an error tolerance. Optimizing as though every coefficient were exact may produce a solution that looks ideal in the model but violates a constraint in reality.

Robust optimization takes a direct approach. Instead of selecting one presumed coefficient value, it specifies a set of possible values and requires the constraints to hold for all of them. This changes the question from, “What is optimal for the nominal model?” to, “What remains feasible under every allowed realization?”

The resulting model can be conservative, but it is mathematically clear. The guarantee is conditional on the uncertainty set: if reality lies outside that set, the robust feasibility certificate no longer applies.

#### A simple uncertain capacity constraint

Suppose the amount of a resource consumed per item is uncertain. The nominal estimate is three units per item, but the actual value can be anywhere from two to four. We have twelve units of resource available and want to produce as many items as possible.

If we trust the nominal coefficient three, we might plan four items. But at the worst allowed coefficient four, those items consume sixteen units and violate capacity. Requiring feasibility for every coefficient in the interval forces us to plan no more than three items.

The arithmetic is simple, yet the model illustrates the essential distinction. A nominal optimum is a property of one selected scenario. A robust optimum is a property of the entire prescribed uncertainty set.

An important choice is which quantities are uncertain. If an uncertain coefficient multiplies a nonnegative decision, the worst coefficient is its upper endpoint. With decisions that can be negative, the endpoint maximizing the product can switch. The correct robust formula is obtained by optimizing over the uncertainty set, not by mechanically replacing every coefficient with its maximum.

#### Support functions remove the infinity of constraints

Consider a linear inequality whose coefficient vector can vary within a set. The robust requirement contains an apparently infinite family of inequalities: one for every allowed vector. Convex analysis provides a compact description through the support function of the uncertainty set.

Suppose the uncertain coefficient vector equals a nominal vector plus a matrix times a disturbance vector. If the disturbance may lie in the unit Euclidean ball, then the worst possible additional contribution to a decision vector x is the Euclidean norm of the matrix transpose times x.

The robust inequality becomes a nominal linear term plus a norm term bounded by the capacity. That is a second-order cone constraint, a standard convex constraint that can be handled by conic optimization methods.

Why does a norm appear? Because the largest inner product between a fixed vector and a unit vector is the length of the fixed vector, achieved when the unit vector points in the same direction. Cauchy–Schwarz is doing the entire worst-case calculation.

If the uncertainty is instead a box, with each component independently allowed to vary within a specified interval, the support function produces a sum of absolute values. Different uncertainty sets therefore produce different optimization penalties. Geometry of uncertainty becomes geometry of a norm or support function in the robust counterpart.

#### A worked two-coordinate example

Imagine a nominal constraint with coefficients two and one on two nonnegative decisions. Suppose both coefficients have independent uncertainty of radius one half. A box uncertainty set allows each coefficient to move to its unfavorable endpoint independently. The robust constraint then becomes two and a half times the first decision plus one and a half times the second, bounded by the same capacity.

If instead the two coefficient errors must lie in a Euclidean ball of radius one half, they cannot both attain their individual maximum at once. The robust penalty is half the Euclidean length of the two-decision vector. For many decisions this is smaller than the box penalty.

Neither model is universally better. The box expresses independent worst-case component bounds. The ball expresses a coupled restriction on the total disturbance size. Choosing between them should reflect the information available about the uncertain parameters, not a desire for whichever optimization answer looks most favorable.

#### Robust feasibility is not probability

A robust constraint holds for every member of its uncertainty set. It does not say how likely those members are. By contrast, a chance constraint allows a specified small probability of violation under an explicit probability distribution. Stochastic programming often optimizes an expected cost over scenarios.

These are different mathematical questions. A robust model may impose severe restrictions to protect against unlikely combinations of errors. A chance-constrained model may accept carefully controlled failure probability, but only if its probabilistic assumptions are credible. A distributionally robust model goes further by allowing uncertainty about the probability distribution itself.

The nominal model, the uncertainty set, and the risk criterion should therefore be treated as separate modeling decisions. A solver can verify an exact robust counterpart without validating whether the uncertainty set corresponds to the physical world.

#### Convexity, certificates, and limits

When a robust linear constraint is obtained by intersecting linear inequalities over all uncertainty realizations, the feasible set remains convex. If the uncertainty set has a tractable support function, we can often write a finite convex formulation and solve it using algorithms already developed for conic optimization.

But not every robust optimization model is easy. Uncertainty entering nonlinear or matrix-valued expressions can make worst-case evaluation difficult, and the geometry of the uncertainty set may prevent a simple reformulation. Some models are tractable only through conservative approximations rather than an exact equivalent problem.

The careful workflow is to define the uncertainty set, derive the worst-case expression, decide whether the reformulation is exact or approximate, and then compute the optimum together with a certificate of feasibility. If those steps are separated, we know exactly which part of the guarantee comes from mathematics and which part comes from our assumptions about uncertainty.

Robust optimization is ultimately a form of honest modeling. It does not eliminate unknown parameters. It turns the unknowns into explicit sets and asks how a decision behaves across them. Convex duality and support functions make that demanding requirement computationally manageable in many important cases.

### Wasserstein Distributionally Robust Optimization: Decisions under Uncertain Laws

Suppose a manufacturer must decide how much inventory to hold. Demand is random, and we have observed demand on several past days. We could estimate a probability distribution from those observations and minimize the expected cost under that one fitted distribution.

But the fitted distribution is itself uncertain. A small sample may misrepresent the true frequency of rare events or place too much mass on a few observed values. A different probability law, still reasonably close to the empirical data, could give a different expected cost.

Distributionally robust optimization treats the probability law as the uncertain object. Rather than guard against one unfavorable demand value, we guard against a family of plausible probability distributions. We choose a decision whose worst expected cost over that family is as small as possible.

The subtle part is deciding what it means for two distributions to be close. Wasserstein distance offers one answer by measuring how much work it takes to transport probability mass from one location to another.

### The transport picture

Imagine two piles of sand laid out along a number line. Each pile represents a probability distribution, with total mass one. To turn the first into the second, we move some mass left and some right. Each movement costs the amount of mass moved times the distance traveled.

The Wasserstein-one distance is the least possible total transport cost. In higher dimensions, the cost depends on a specified metric or norm on the space of uncertain outcomes. A larger distance means the distributions are harder to transform into one another under that metric.

This is different from total variation distance, which counts how much probability mass must change membership between sets but does not record how far the mass moved. Moving a small amount of mass a huge distance can have low total variation but appreciable transport cost, depending on the product of mass and distance.

### Build an ambiguity set around data

Take observed outcomes and put equal probability at each one. This is the empirical distribution. Choose a radius rho in Wasserstein distance. The ambiguity set contains all probability laws whose distance from the empirical law is at most rho.

For any decision, compute the expected loss under each law in the ambiguity set, then select the largest. This worst expected loss is the distributionally robust risk of the decision. Finally choose the decision minimizing that risk, perhaps together with a deterministic regularization or operating cost.

If rho is zero, the ambiguity set contains just the empirical law, assuming our distance is a proper metric on the selected class of probability measures. We recover empirical risk minimization. As rho grows, the family of laws grows, and the worst-case risk for a fixed decision cannot decrease.

There is no universally correct radius. It may be chosen using statistical concentration results, domain knowledge, sensitivity analysis, or a specific decision objective. The resulting robustness guarantee is conditional on the assumed ambiguity set containing the law we care about.

### An exact one-dimensional calculation

Consider two observed values, negative one and positive two. Their empirical mean is one half. Suppose our loss at outcome z is two times z. The empirical expected loss is therefore one.

Now allow Wasserstein-one distance at most one quarter, using ordinary absolute distance as the transport cost. The loss is Lipschitz with constant two: moving z by an amount h changes the loss by at most two times the absolute value of h.

The transport inequality tells us that the expected loss under any distribution within radius one quarter is at most the empirical expectation plus two times one quarter. That is one and a half.

Is the upper bound attainable? Yes, because our uncertain outcome is allowed to range over the entire real line. Shift each empirical observation to the right by one quarter. The transport cost is one quarter, and the new expected loss is one and a half. So the worst expected loss is exactly one and a half in this example.

The calculation is a useful model. Wasserstein robustness turns the slope of a loss function with respect to uncertain data into an explicit cost of distributional ambiguity.

### The dual view

The worst-case expectation is an optimization over all probability distributions in a ball. That appears infinite-dimensional. Under suitable regularity assumptions, transport duality transforms it into a problem involving a nonnegative transport-price parameter and a worst-case pointwise expression around each observed datum.

For a globally Lipschitz loss on an unrestricted metric space, this dual expression yields a simple upper bound: empirical expected loss plus Lipschitz constant times rho. For an affine loss on the real line, the upper bound is exact under the conditions of our example.

This dual form makes many distributionally robust optimization problems computationally tractable. Depending on the loss, domain, and cost function, the reformulation may be a convex program or sometimes a linear program. It is not true that every Wasserstein robust problem has a small convex reformulation without assumptions.

### A counterexample: quadratic losses with the wrong metric

Suppose the empirical distribution places all its mass at zero, and we use squared loss z squared. Choose a tiny probability mass epsilon and move it to a very distant point R, leaving the rest at zero.

The transport cost in Wasserstein-one distance is epsilon times R. We can keep that cost fixed at rho by choosing epsilon equal to rho divided by R. But the expected squared loss is epsilon times R squared, which equals rho times R. That tends to infinity as R grows.

So if the uncertain outcome is unbounded, a Wasserstein-one ambiguity ball around a point mass gives an infinite worst-case quadratic expectation. A finite radius does not automatically make every loss well behaved.

Possible remedies include a bounded support set, a transport cost that penalizes distant mass more strongly, or a class of losses with appropriate growth. The correct choice depends on the actual uncertainty model. This example demonstrates why specifying the transport metric and the loss growth is essential, not a technical footnote.

### Robustness is a modeling claim

A distributionally robust optimum answers a conditional question: among all distributions in the chosen ambiguity set, how bad can the expected loss be, and which decision minimizes that worst case?

It does not certify that the empirical data were sampled without bias, that the chosen distance matches the physical meaning of uncertainty, or that the true distribution lies inside the chosen ball. Those are separate statistical and modeling questions.

The mathematical benefit is clarity. The data define an empirical center, transport distance defines plausible deviations, duality makes the worst-case expectation analyzable, and optimization selects the decision. When those pieces are chosen explicitly, distributional uncertainty becomes a problem we can reason about rather than an invisible assumption inside an estimated expectation.

### Entropic Risk, CVaR, and Distributional Ambiguity

Suppose a machine failure causes a loss of ten units and happens with probability one tenth. Otherwise the loss is zero. The expected loss is one unit. That average is correct, but it says little about what happens in the most expensive outcomes.

Risk measures summarize different aspects of this distribution. Conditional value at risk asks about the average loss in the worst specified fraction of outcomes. Entropic risk uses an exponential weighting that amplifies high losses. Both can be convex in the underlying loss, under their standard conditions, but they encode different attitudes to the tail.

Now add a second uncertainty: perhaps the failure probability is not known exactly. Historical data suggest it is somewhere between five percent and twenty percent. The decision maker wants protection against every probability law in this ambiguity set. This is distributionally robust risk optimization.

The distinction between ordinary and distributionally robust risk is fundamental. One evaluates a risk functional under a fixed distribution; the other takes its worst value across a family of plausible distributions.

### Conditional value at risk as an optimization problem

For a loss L and confidence level alpha, upper-tail conditional value at risk can be written as a minimum over a threshold t. The objective is t plus the expected excess loss above t, divided by one minus alpha.

This variational formula handles both continuous and discrete distributions without needing to invent a unique quantile inside an atom. It also makes CVaR suitable for convex optimization: when the loss is convex in a decision variable, the positive-part construction preserves convexity under standard integrability conditions.

At confidence level ninety percent, we average the worst ten percent of outcomes, with fractional treatment of atoms when necessary. For our two-point loss distribution with failure probability ten percent, that worst ten percent consists entirely of failures. CVaR is therefore ten, even though the mean is one.

If failure probability were only five percent, the worst ten percent would contain five percent failures and five percent zero-loss outcomes. CVaR would then be five. The tail confidence level and the mass in the high-loss atom both matter.

### Entropic risk weights differently

For a positive risk-aversion parameter eta, entropic risk takes the logarithm of the expected exponential of eta times the loss, then divides by eta. Its exponential emphasis on large losses makes it sensitive to rare severe outcomes.

For our two-point distribution, the expectation inside the logarithm is one minus the failure probability, plus the failure probability times the exponential of ten eta.

As eta approaches zero, entropic risk approaches the ordinary expected loss, assuming sufficient integrability. As eta grows without bound for a bounded discrete loss, entropic risk approaches the largest possible loss with positive probability. For intermediate eta, it interpolates between those behaviors in a precise nonlinear way.

Unlike CVaR, entropic risk need not remain finite for every heavy-tailed distribution. If the exponential moment is infinite, the risk value is infinite. A robust ambiguity set containing such a distribution may make the worst-case entropic risk infinite even when every candidate has a finite mean.

### Add ambiguity about the probability

Let the failure probability vary between five percent and twenty percent. What is the worst expected loss? It is ten times the largest failure probability, or two.

What is the worst ninety-percent CVaR? When the failure probability is at least ten percent, the worst ten percent contains only ten-unit failures, so the CVaR equals ten. The worst-case value over our ambiguity interval is therefore ten.

For entropic risk with positive eta, increasing the failure probability increases the expected exponential because ten is the high outcome. The worst distribution uses failure probability twenty percent. Its entropic risk is one over eta times the logarithm of point eight plus point two times the exponential of ten eta.

We have three different numbers or functions from the same ambiguity set: worst mean two, worst ninety-percent CVaR ten, and a parameter-dependent worst entropic risk. None is incorrect. They answer different questions about uncertain losses.

### Why the ambiguity set matters

Our interval of possible failure probabilities is a very small distributional ambiguity set. In applications, the set may be defined by moment constraints, statistical confidence regions, an f-divergence, or a Wasserstein distance around an empirical distribution.

Each choice restricts which alternative probability laws the adversary is allowed to use. A Wasserstein ball constrains the transport cost of moving probability mass; a divergence ball restricts changes in weights relative to a reference law. These models are not interchangeable, and their behavior depends on the support assumptions and choice of distance or divergence.

For example, a Wasserstein ball on an unbounded outcome space may allow a small amount of probability to be moved very far. For a sufficiently rapidly growing loss, that can make a worst-case expectation infinite. A claim of robustness must therefore include the growth of the loss, the geometry of the support, and the radius of the ambiguity set.

### The order of optimization is an issue

Distributionally robust CVaR can be written as the supremum over distributions of CVaR under that distribution. Inside each CVaR is an infimum over a threshold t. It is tempting to exchange the supremum and infimum and solve one simpler-looking problem.

That exchange is a minimax step. It requires conditions such as appropriate convexity, concavity, compactness, and continuity, or another valid duality theorem. We should not silently commute the operations merely because both involve optimization.

In our finite two-point example, it is easy to check the worst case directly. For a large continuous ambiguity set, establishing a tractable and exact reformulation is part of the mathematical work.

### Robust decisions and certificates

If a decision variable changes the loss distribution, the objective might minimize worst-case CVaR, worst-case entropic risk, or a weighted combination with expected cost. Convexity can permit efficient solution methods, while duality can sometimes convert the adversarial distribution search into finite-dimensional constraints.

But a solver's output still needs interpretation. It may certify an optimum of a chosen ambiguity model, not that the model contains the true data-generating distribution. Statistical coverage of the ambiguity set is a separate question. A risk value also says nothing about individual losses beyond the properties guaranteed by that risk functional.

Distributionally robust risk is useful precisely because it makes two assumptions visible: what kinds of bad outcomes matter, and what probability laws are considered plausible. CVaR emphasizes upper-tail averages; entropic risk emphasizes exponential moments; the ambiguity set formalizes uncertainty about the law itself. Clear mathematics keeps those choices distinct instead of hiding them in one phrase such as “conservative optimization.”

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Optimization Sensitivity: Perturbation Bounds and Shadow Prices

**Track:** Optimization, Convexity, and Duality. **Background:** convex programs, Lagrange multipliers, KKT conditions, duality and interior-point methods. **Central question:** what can a dual solution tell us about how the optimal value changes when constraints are perturbed?

#### Mathematical companion (not spoken)

For a convex optimization problem with convex \(f_0,f_i\) and affine \(h_j\), define the perturbed value
\[p^\star(u,v)=\inf_x\{f_0(x):f_i(x)\le u_i,\ h_j(x)=v_j\}.\]
The Lagrangian is
\[L(x,\lambda,\nu;u,v)=f_0(x)+\sum_i\lambda_i(f_i(x)-u_i)+\sum_j\nu_j(h_j(x)-v_j),\quad\lambda\ge0.\]
If \(p^\star(0,0)\) is finite and the unperturbed dual optimum is attained at \((\lambda^\star,\nu^\star)\) with zero duality gap, weak duality with the same multipliers for perturbed data yields
\[p^\star(u,v)\ge p^\star(0,0)-\lambda^{\star T}u-\nu^{\star T}v.\]
Thus \((-\lambda^\star,-\nu^\star)\) is a subgradient of the convex value function at zero (where the latter is proper); if differentiable there, \(\nabla p^\star(0,0)=(-\lambda^\star,-\nu^\star)\).

**One-dimensional example:** minimize \(x^2\) subject to \(1-x\le u\). For \(u<1\), \(x^\star(u)=1-u\) and \(p^\star(u)=(1-u)^2\); for \(u\ge1\), the optimum is \(x=0\) and \(p^\star(u)=0\). At \(u=0\), \(\lambda^\star=2\), \(\frac{d}{du}p^\star(0)=-2\), and the global supporting line is \(p^\star(u)\ge1-2u\). The exact change has a quadratic correction for small \(u\), and extrapolation past the active-set change is inaccurate.

**Conditioning example:** for \(\varepsilon>0\), \(f(x;b)=\tfrac\varepsilon2x^2-bx\) has \(x^\star(b)=b/\varepsilon\). Parameter sensitivity \(\partial x^\star/\partial b=1/\varepsilon\) diverges as curvature \(\varepsilon\downarrow0\). Uniqueness alone does not imply numerical robustness.

##### Exercises with answers

1. With the convention \(f_i(x)\le u_i\), what sign does a nonnegative inequality multiplier give for the derivative of optimal value with respect to \(u_i\)? **Answer:** \(-\lambda_i^\star\), if the value function is differentiable and regularity assumptions hold.
2. Compute the new optimum for the one-variable example at \(u=1/2\). **Answer:** \(x^\star=1/2\), \(p^\star=1/4\); the linear lower bound is \(0\), so it is valid but not exact.
3. Does strict convexity alone guarantee that an optimizer changes little under parameter perturbations? **No:** the shallow quadratic has sensitivity \(1/\varepsilon\).
4. What does a nonunique optimal multiplier imply about interpreting one reported shadow price? **Answer:** differentiability and a unique sensitivity have not been established; consider subgradients and constraint degeneracy.

##### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*, Section 5.6 on perturbation and sensitivity](https://web.stanford.edu/~boyd/cvxbook/), dual lower bounds and local multiplier sensitivity.
- Stanford EE364A, [Convex Optimization course resources](https://web.stanford.edu/class/ee364a/), KKT and perturbation theory.
- [JuMP documentation: Tolerances and numerical issues](https://jump.dev/JuMP.jl/stable/tutorials/getting_started/tolerances/), numerical qualifications when reading solver certificates.

### Perturbations, worst-case uncertainty, transport ambiguity, and tail risk

### Perturbations, worst-case uncertainty, transport ambiguity, and tail risk

#### Companions, sources, and study material (not spoken)

##### Robust Optimization: Worst-Case Constraints and Tractable Reformulations

**Track:** Optimization and Duality. **Background:** linear programming, convexity, norms, support functions and conic optimization. **Central question:** how should we optimize when the coefficients of a constraint are not known exactly?

###### Mathematical companion (not spoken)

For uncertain coefficient \(a=a_0+Pu\), \(\|u\|_2\le1\), the robust linear inequality is
\[a^Tx\le b\quad\forall u:\|u\|_2\le1\iff a_0^Tx+\|P^Tx\|_2\le b.\]
Indeed \(\sup_{\|u\|_2\le1}u^T(P^Tx)=\|P^Tx\|_2\) by Cauchy–Schwarz. The right side is a convex second-order cone constraint in x. For box uncertainty \(a=a_0+\operatorname{diag}(\rho)u\), \(\|u\|_\infty\le1\), the robust counterpart is \(a_0^Tx+\sum_i\rho_i|x_i|\le b\) for \(\rho_i\ge0\).

**Scalar example:** optimize \(\max x\) subject to \(x\ge0\) and \(ax\le12\) for every \(a\in[2,4]\). The robust constraint is \(4x\le12\), giving \(x^*=3\), while the nominal choice a=3 gives x=4, which is not robust-feasible. Without \(x\ge0\), the exact robust inequality is \(3x+|x|\le12\), not automatically \(4x\le12\) for negative x.

**Two-coordinate example:** nominal \(a_0=(2,1)\), uncertainty \(\delta\in[-1/2,1/2]^2\) yields \(2x_1+x_2+\tfrac12(|x_1|+|x_2|)\le b\). If \(\|\delta\|_2\le1/2\), the exact reformulation is \(2x_1+x_2+\tfrac12\sqrt{x_1^2+x_2^2}\le b\). These sets encode different information about simultaneous errors.

A robust guarantee is conditional on \(a\in\mathcal U\); it is not a distribution-free empirical claim that physical coefficients actually lie there. For more general uncertain nonlinear programs, tractability and exactness require separate analysis.

##### Exercises with answers

1. Find the robust maximum x if \(x\ge0\), \(a\in[5,6]\), and \(ax\le30\) for all a. **Answer:** 5.
2. Evaluate \(\sup_{\|u\|_2\le1}u^Ty\). **Answer:** \(\|y\|_2\), with the maximum at \(u=y/\|y\|\) if y is nonzero.
3. What penalty results from independent componentwise uncertainties of radii \(\rho_i\)? **Answer:** \(\sum_i\rho_i|x_i|\).
4. Does robust feasibility with respect to a set imply a one-percent probability of failure? **Answer:** no; it has no probabilistic meaning without a probability model.

##### Reading and source notes

- [Ben-Tal and Nemirovski, Robust Convex Optimization](https://www2.isye.gatech.edu/~nemirovs/robmp.pdf), robust convex formulations and ellipsoidal uncertainty.
- [Ben-Tal and Nemirovski, Robust Solutions of Uncertain Linear Programs](https://www2.isye.gatech.edu/~nemirovs/stablpn.pdf), exact conic quadratic robust counterparts.

##### Wasserstein Distributionally Robust Optimization: Decisions under Uncertain Laws

**Track:** Optimization and Duality. **Background:** convex duality, probability distributions, optimal transport, and robust optimization. **Central question:** how can an optimization decision remain defensible when the empirical distribution is only an approximation to the unknown population distribution?

###### Mathematical companion (not spoken)

For empirical observations `xi_1,...,xi_N in Xi` and empirical law `P_hat=(1/N)sum_i delta_xi_i`, define the Wasserstein-one ball
\[
\mathcal P_\rho=\{P:W_1(P,\widehat P)\le\rho\},
\quad W_1(P,Q)=\inf_{\pi\in\Pi(P,Q)}\int d(z,z')\,d\pi(z,z').
\]
The distributionally robust objective is `min_{x in X} sup_{P in P_rho} E_P[ell(x,Z)]` when the expectations and minimax problem are well defined. If `ell(x,.)` is L(x)-Lipschitz, the Kantorovich–Rubinstein inequality implies
\[
\sup_{P\in\mathcal P_\rho}\mathbb E_P\ell(x,Z)
\le\frac1N\sum_i\ell(x,\xi_i)+L(x)\rho.
\]
Under standard strong-duality and upper-semicontinuity/growth assumptions, a generic transport dual reads
\[
\inf_{\lambda\ge0}\left[\lambda\rho+\frac1N\sum_i
\sup_{z\in\Xi}\bigl(\ell(x,z)-\lambda d(z,\xi_i)\bigr)\right].
\]
For `Xi=R`, `d(z,z')=|z-z'|`, and `ell(a,z)=a z`, this is exactly `a*mean(xi)+|a|rho`, because finite inner sup requires `lambda>=|a|`, and the value is attained by shifting the empirical law in the sign(a) direction by rho. Example: xi=(-1,2), a=2, rho=1/4 gives `2*(1/2)+2*(1/4)=3/2`.

**Growth counterexample.** If `P_hat=delta_0` and `ell(z)=z^2`, for any `R>=rho>0` set `P_R=(1-rho/R)delta_0+(rho/R)delta_R`. Then `W_1(P_R,delta_0)=rho` but `E_{P_R} Z^2=rho*R -> infinity`. Thus the worst-case W1 quadratic loss on unbounded R is infinite. A Wasserstein-2 ball, bounded support, or growth restrictions changes the analysis.

##### Exercises with answers

1. For affine loss `ell(a,z)=a z` over R, empirical mean 3, a=-2, rho=0.4, find worst-case expectation. **Answer:** `-6+0.8=-5.2`.
2. Why can the W1 robust quadratic loss diverge on unbounded support? **Answer:** small mass moved distance R costs order mass times R, while squared loss gains order mass times R squared.
3. What happens to fixed-decision worst-case risk when rho increases? **Answer:** it cannot decrease, since the ambiguity set expands.
4. Does minimizing worst-case loss prove that the true distribution lies in the selected ball? **Answer:** no; containment is a separate statistical assumption or guarantee.

##### Reading and source notes

- [Mohajerin Esfahani and Kuhn, Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric](https://doi.org/10.1007/s10107-017-1172-1), Wasserstein ambiguity sets and convex reformulations.
- [EPFL open-access research record of Esfahani–Kuhn](https://infoscience.epfl.ch/entities/publication/a785a796-96d5-4510-84e1-8ab1b7f903b2), bibliographic record and author manuscript.
- [Kantorovich–Rubinstein duality, Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Kantorovich-Rubinstein_theorem), transport distance and Lipschitz test functions.

##### Entropic Risk, CVaR, and Distributional Ambiguity

**Track:** Optimization and Duality. **Background:** convex risk measures, probability distributions, expectation constraints, and distributionally robust optimization. **Central question:** what changes when uncertainty concerns the probability law itself, not just the random loss under one fixed law?

###### Mathematical companion (not spoken)

For an integrable loss `L` and `alpha in (0,1)`,
\[
\operatorname{CVaR}_\alpha^P(L)
=\inf_{t\in\mathbb R}\left\{t+\frac{1}{1-\alpha}\mathbb E_P[(L-t)_+]\right\}.
\]
For `eta>0` with finite exponential moment,
\[
\rho_\eta^P(L)=\frac1\eta\log\mathbb E_P[e^{\eta L}].
\]
Let `L=10` with probability `p`, else `0`, with `p in [0.05,0.20]`. Then
\[
\sup_p\mathbb E[L]=2,\quad
\operatorname{CVaR}_{0.9}(L)=10\min(1,p/0.1),\quad
\sup_p\operatorname{CVaR}_{0.9}(L)=10,
\]
and
\[
\sup_p\rho_\eta^p(L)=\frac1\eta\log\left(0.8+0.2e^{10\eta}\right).
\]
The supremum of `inf_t` is not automatically `inf_t` of the supremum; any interchange needs a minimax theorem or direct verification. General distributional ambiguity sets can give infinite worst-case entropic risk when exponential moments are uncontrolled.

##### Exercises with answers

1. What is mean loss at `p=0.1`? **Answer:** one.
2. What is `CVaR_0.9` at `p=0.05`? **Answer:** five.
3. Which probability maximizes entropic risk over the interval for `eta>0`? **Answer:** `p=0.20`.
4. Does a worst-case optimum prove the ambiguity set contains the true law? **Answer:** No; statistical coverage is a separate claim.

##### Reading and source notes

- [Rockafellar and Uryasev, Optimization of Conditional Value-at-Risk](https://doi.org/10.21314/JOR.2000.038), variational CVaR formulation.
- [Cherukuri and Hota, Consistency of Distributionally Robust Risk- and Chance-Constrained Optimization](https://arxiv.org/abs/2012.08850), risk constraints under Wasserstein ambiguity.
- [Esfahani and Kuhn, Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric](https://arxiv.org/abs/1505.05116), tractable DRO principles and assumptions.
