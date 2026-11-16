# Monotone splitting, inexact proximal steps, and stochastic games

<!-- BEGIN SPOKEN LECTURE -->

# Monotone splitting, inexact proximal steps, and stochastic games

## Monotone Operators, Resolvents, and Splitting Methods

Imagine minimizing an objective made of two parts. One part measures fit to data. The other imposes sparsity, smoothness, or a constraint. Each part is easy to handle by itself, but their sum is awkward. A common computational strategy is to alternate between the two. Monotone operator theory explains when that alternation is more than a heuristic.

For a differentiable convex function, a minimizer is a point where the gradient is zero. For a nonsmooth convex function, the gradient is replaced by a set of possible subgradients. The optimality condition becomes that zero belongs to the subdifferential. This is an inclusion problem, not just an equation.

A monotone operator extends the familiar idea of an increasing function. Given two input points and one output value chosen from the operator at each input, the inner product of the difference in outputs with the difference in inputs must be nonnegative. In one dimension, this reduces to the observation that moving to the right cannot make a monotone graph move downward.

The subdifferential of a proper, lower-semicontinuous convex function is a maximal monotone operator. Maximal means its graph cannot be enlarged while preserving monotonicity. This property matters because it guarantees a well-defined way to invert the identity plus a positive multiple of the operator.

### A resolvent is an implicit step

Take a maximal monotone operator A. Given a point z, seek a point x such that z equals x plus a positive step size times an output of A at x. The map sending z to x is called the resolvent of A.

For a convex subdifferential, the resolvent is exactly the proximal operator. It asks for the point that balances the objective value against the cost of moving away from z. Instead of taking a gradient step that may be undefined at a corner, the proximal map solves an implicit local optimization problem.

Consider the absolute-value function on the real line. Its proximal operator is soft thresholding. A positive input is reduced toward zero by the threshold, a negative input is increased toward zero, and anything with magnitude at most the threshold becomes exactly zero. The corner at zero is not a numerical obstacle. The resolvent treats it as part of the solution.

For the indicator function of a closed convex set, the proximal operator is simply Euclidean projection onto that set. Sparsity and feasibility thus become two examples of the same operator construction.

### Why resolvents are stable

Monotonicity gives the resolvent a remarkable inequality. The distance between two outputs cannot exceed the distance between their inputs. More strongly, the squared output distance is bounded by the inner product of the output difference with the input difference. This property is called firm nonexpansiveness.

It follows directly from the defining inclusion for the resolvent. Subtract the two inclusion relations and apply monotonicity to the operator outputs. The resulting inequality is the key estimate behind many fixed-point convergence arguments.

Ordinary nonexpansiveness alone would not force every iterative scheme to converge. The stronger averaged structure and the existence of a solution are part of what makes suitable splitting algorithms work.

### Separating two operators

Suppose the optimality condition is that zero belong to A of x plus B of x. Each operator has an easy resolvent, but the resolvent of their sum is expensive. Douglas–Rachford splitting constructs a fixed-point iteration using only the resolvents of A and B and a reflection through one of them.

The iteration works in an auxiliary variable z. At each step, first apply one resolvent, reflect that result across z, apply the other resolvent, then correct z by the difference. Under standard maximal-monotonicity, solvability, and related regularity hypotheses, the iterates converge in the appropriate weak sense, and in finite-dimensional settings the projected, or shadow, iterates approach a solution.

There is an important subtlety. The auxiliary variable z need not itself be the minimizer. The solution is recovered through a resolvent. Confusing the internal fixed point with the primal solution can make a correct algorithm look incorrect.

Another familiar method, forward–backward splitting, applies a gradient step to the smooth part and a proximal step to the nonsmooth part. It takes advantage of extra smoothness and step-size bounds rather than solving both steps implicitly. ADMM is closely related to Douglas–Rachford splitting through the dual problem, although the raw primal and dual iterates should not be identified without the proper transformation.

### Limits of the framework

If the objective is nonconvex, the subdifferential may not be maximal monotone and the same convergence proof does not automatically apply. If the two operators have no common zero, a fixed-point iteration cannot be expected to recover one. Even with convexity, splitting parameters and the ability to compute the resolvents accurately matter.

The central insight is not that alternating two arbitrary operations is safe. It is that an optimization problem can be rewritten as a monotone inclusion, whose component resolvents have strong geometric properties. The algorithm then inherits convergence from those properties rather than from the appearance of progress in a numerical log.

## Inexact Proximal Algorithms: Convergence When Inner Solves Are Imperfect

Proximal algorithms are useful because they separate two kinds of structure. We may have a smooth objective whose gradient is easy to calculate, and a nonsmooth penalty whose proximal operator is easy to evaluate. A proximal-gradient step first moves in the negative gradient direction, then solves a small regularized optimization problem to incorporate the nonsmooth penalty.

For an absolute-value penalty, the proximal operator is soft thresholding, which has a closed formula. But for more complicated penalties or constraints, the proximal subproblem may require its own iterative solver. Then each outer iteration depends on an approximate inner solution. The mathematical algorithm asks for an exact proximal point, but the computer returns one with residual error.

Does the outer algorithm still converge? There is no single answer independent of how the error is measured. We need to distinguish an error in the returned point, an error in the subproblem objective, and a residual in its first-order optimality condition. These are not interchangeable without assumptions.

## The exact step as a reference point

Consider an objective made of a smooth convex part and a proper closed convex penalty. Assume the smooth part has a Lipschitz-continuous gradient. For a sufficiently small step size, the exact proximal-gradient update decreases the objective and moves toward a minimizer, under the usual existence assumptions.

The proximal operator minimizes the penalty plus a quadratic distance from the gradient step. That quadratic term makes the proximal subproblem strongly convex, so the proximal point is unique. The update balances the local linear approximation of the smooth function against the exact nonsmooth penalty.

There is also a natural stationarity measure called the proximal-gradient mapping. It is the current point minus its exact proximal-gradient update, divided by the step size. This mapping vanishes precisely when the first-order optimality condition for the convex composite objective is satisfied.

Thus an exact update provides both a descent step and a way to assess convergence. If we approximate the update, we must also quantify how far the reported stationarity measure might be from the true one.

## A simple example with a known answer

Take a one-dimensional smooth objective equal to half the square of x minus three, and add the absolute value of x with coefficient one. The exact minimizer is x equals two. For a unit step size, the gradient move always lands at three, regardless of the previous iterate. The proximal map soft-thresholds three by one and returns two.

Now imagine an inner solver returns two point zero zero one instead. The objective value is only slightly above optimal. The first-order stationarity residual is also small: the smooth derivative at that point is approximately minus zero point nine nine nine, while the derivative of the absolute value penalty is one. Their sum is zero point zero zero one.

This is a simple instance where we can compute the error exactly. In a large problem, we may not know the true minimizer, so we should try to calculate a verifiable inner residual or a bound on the distance from the true proximal point.

## Absolute summability and accumulated error

A common convergence principle is that errors which are absolutely summable can be absorbed into the analysis of a nonexpansive or averaged iteration. If the sum of the sizes of the errors over all iterations is finite, their total accumulated disturbance is controlled.

For exact proximal point iterations and closely related firmly nonexpansive maps, summable perturbations permit useful convergence theorems under appropriate assumptions, including existence of fixed points. In finite-dimensional convex composite settings, one can obtain related results for inexact proximal-gradient methods, but additional conditions may be needed depending on whether the error is measured as a point perturbation, a subproblem residual, or an objective tolerance.

The phrase 'the error goes to zero' is weaker than summability. An error of size one divided by the square root of the iteration count tends to zero but its sum diverges. Some algorithms still converge under weaker conditions, but that requires a different theorem. We should not simply assert that any vanishing inner tolerance is sufficient.

## Why feasibility matters

Suppose the nonsmooth penalty is the indicator of a constraint set. It is zero for feasible points and infinite for infeasible points. The exact proximal operator becomes a projection onto that set.

An approximate point may be close to the projection in Euclidean distance yet lie just outside the constraint set. Reporting it as though it were a valid optimization iterate can make the objective undefined or infinite. So a pointwise approximation guarantee alone may not preserve feasibility.

An implementer should either require a feasible approximate proximal point or use a theorem explicitly designed for infeasible or approximate projections. In constrained problems, the distance to feasibility and the stationarity residual serve different purposes. Both may be needed.

## Stopping criteria and certificates

Suppose a numerical solver reports that its update is very small. That is not by itself a proof of near-optimality. A small step can arise from a genuinely near-stationary point, but also from a poorly solved proximal subproblem, a tiny step size, or a numerical failure.

A better diagnostic evaluates the proximal-gradient mapping, or an upper bound on its norm if the proximal operator was approximated. For convex objectives, an actual first-order stationarity residual has a clear interpretation. With stronger assumptions such as strong convexity, we may convert a residual bound into a distance or objective-gap estimate. Without those assumptions, a residual norm is not necessarily a numerical upper bound on the global objective gap.

It is also useful to distinguish a theorem of asymptotic convergence from a finite stopping certificate. Convergence says what happens if we continue the algorithm indefinitely under the stated error conditions. A stopping certificate justifies a claim about the finite approximate solution we currently hold. These are different questions.

## Choosing the inner accuracy schedule

In practice, there is a tradeoff. Solving every proximal subproblem to extreme accuracy wastes work early, when the outer iterate is still far from the optimum. Solving them too crudely late may prevent further progress.

An adaptive approach asks for coarse inner solves at first and tighter solves as the outer stationarity measure falls. But any rigorous complexity or convergence guarantee must connect the schedule to a precise error model. We can use certificates from the inner solver, such as primal-dual gaps or optimality residuals, to make this connection explicit.

The main lesson is a disciplined separation of levels. The outer objective has a mathematical minimizer. The exact proximal algorithm has an ideal update. The inner numerical routine returns an approximation to that update. Each arrow between these objects needs an error estimate. Once those estimates are explicit, inexact proximal methods become analyzable rather than a matter of trusting a solver's iteration count.

## Mirror-Prox: Solving Monotone Games Without Rotating Forever

Consider the simplest possible two-player zero-sum game. One player chooses x and tries to minimize the product of x and y. The other chooses y and tries to maximize the same product. The unique saddle point, when the variables are unrestricted, is at x and y both zero.

If we perform simultaneous gradient descent in x and gradient ascent in y, something strange happens. The update continually rotates the pair of variables around the origin. More precisely, with a constant positive step size, its distance from the origin grows instead of shrinks. The derivatives point in directions that are individually sensible for each player, yet the combined algorithm moves away from the equilibrium.

This failure has nothing to do with a nonconvex objective. The payoff is linear in each variable: convex for the minimizing player and concave for the maximizing player. The underlying operator is monotone. The difficulty is that monotonicity does not mean the operator points directly toward the solution. A skew-symmetric rotation is monotone, but it has no radial component.

Mirror-Prox remedies this by evaluating the operator once at a predicted point and then correcting the update using the new information. The correction is small, but its effect on rotational dynamics is decisive.

## Rewrite the game as an operator equation

For a convex-concave saddle function, form an operator by taking the gradient with respect to the minimizing variable and the negative gradient with respect to the maximizing variable. The saddle condition becomes a variational inequality over the feasible set.

The operator is monotone when the smooth saddle function is convex in the first variable and concave in the second. This means that the difference of operator values at two points has a nonnegative inner product with the difference of those points.

In our bilinear game, the operator takes the pair x,y to y,negative x. Geometrically it rotates vectors through a right angle. The inner product of the operator difference with the point difference is exactly zero, so monotonicity holds without any strong radial force.

The ordinary simultaneous gradient step subtracts this rotated vector. It therefore combines the identity transformation with a rotation. Its squared distance multiplier is one plus the square of the step size. That exceeds one for every nonzero step size. No fixed positive step size makes this unconstrained explicit method contract toward the saddle.

## Look ahead before committing

The extragradient idea first takes a provisional step from the current point, using the operator evaluated there. Instead of accepting that provisional point, it evaluates the operator again at the provisional point and makes the actual update from the original current point.

For the bilinear example we can calculate the effect exactly. The operator applied twice is negative the identity. Substituting the provisional point into the second evaluation therefore produces a corrected update: the original vector multiplied by one minus the square of the step size, together with a rotation term.

The squared distance multiplier is now one minus the step-size squared plus the step-size to the fourth. For step sizes strictly between zero and one this is less than one. The iterates contract toward the saddle instead of spiraling outward.

This example is a local algebraic illustration of why the second evaluation matters. It is not a general proof that every extragradient method converges linearly. The bilinear operator here is a particularly simple linear rotation; for general merely monotone operators, the usual guarantee is on an averaged variational-inequality gap.

## Projection keeps constraints in view

Real saddle-point problems often have constraints. Strategies may lie in probability simplexes. Matrix variables may be required to remain positive semidefinite. A simple Euclidean extragradient method handles convex constraints by projecting the predicted point back into the feasible set and projecting the corrected point as well.

Now the intermediate point is computed from the original current iterate and its operator value. The final point is also based on the original current iterate, but it uses the operator at the intermediate point. This distinction is important: taking two ordinary gradient steps in succession is not the same algorithm.

Projection is natural for Euclidean geometry, but it can be expensive or poorly matched to the shape of the feasible set. On a probability simplex, Euclidean projection is sometimes less natural than a multiplicative, entropy-based update. This leads us from extragradient to Mirror-Prox.

## Bregman divergences adapt the geometry

Choose a strongly convex distance-generating function. Its Bregman divergence measures the error made when approximating that function by its tangent plane at the current point. Unlike squared Euclidean distance, a Bregman divergence need not be symmetric and need not satisfy the triangle inequality. Yet strong convexity makes it useful for analyzing proximal updates.

Define a prox step by minimizing the inner product with a candidate operator vector plus the Bregman divergence from the current point. The first Mirror-Prox stage uses the operator at the current point. The second uses the operator at the predicted point, but both prox problems are centered at the original point.

With the quadratic distance-generating function, this reduces to Euclidean extragradient. With negative entropy on a simplex, the update takes a multiplicative form involving exponentials and normalization. That geometry is especially natural when the variables are probability distributions and the feasible set has many coordinates.

The technique is called mirror because the gradient of the distance-generating function provides a different coordinate system. We move in that dual geometry and map back to the feasible set through the prox problem.

## What monotonicity and smoothness buy us

Suppose the feasible set is compact and convex, the operator is monotone and Lipschitz continuous, and the distance-generating function is strongly convex relative to the chosen norm. With a suitable fixed step size based on the Lipschitz constant, Mirror-Prox yields a variational-inequality gap that decays on the order of one over the number of iterations for an average of its predicted points.

This is an ergodic guarantee. It says that a carefully chosen average has a small residual in the variational-inequality sense. It does not automatically say each individual iterate converges at that rate, or that the variables approach one unique solution in ordinary Euclidean distance. Those stronger claims need additional assumptions such as strong monotonicity or special problem structure.

The distinction matters in game solving. Multiple equilibria may exist. A small primal-dual gap certifies near-optimal play even if the actual strategy vector moves among near-equivalent equilibria.

## Where the O one-over-T rate comes from

The proof compares each prox update with an arbitrary test point in the feasible set. Strong convexity of the Bregman generator provides a positive distance term. Lipschitz continuity controls the error caused by evaluating the operator at the intermediate point rather than at the original point.

After a suitable step-size choice, the one-step inequality is a difference of Bregman divergences plus a controlled nonpositive remainder. Sum over iterations. The divergences telescope, leaving an initial diameter-like term divided by the number of iterations.

Monotonicity then converts the accumulated operator comparisons into the variational-inequality gap of the averaged point. The result is an order-one-over-T estimate. The rate is not obtained from contracting the distance to a solution at every step. It is obtained from a telescoping inequality and a gap definition appropriate to monotone problems.

## A probability simplex example

Suppose a zero-sum matrix game has many pure actions. Each player chooses a probability vector over those actions. The saddle payoff is bilinear, and the associated operator is monotone and Lipschitz with respect to suitable norms.

Using negative entropy as the distance-generating function, a Mirror-Prox update reweights actions multiplicatively. Actions with relatively favorable gradient coordinates are emphasized, and the weights are normalized to sum to one. Because the update works in a geometry adapted to probabilities, it can avoid some of the inefficiency of repeatedly projecting dense vectors in Euclidean space.

But this convenience also has hypotheses. Entropic Bregman divergences are finite only on the appropriate relative interior or with suitable boundary conventions. Numerical implementations must handle exponentials and very small probabilities carefully. The theoretical O one-over-T guarantee presumes accurately solved prox steps or explicitly controlled prox error.

## Why the extra evaluation is worth it

Mirror-Prox embodies a broader lesson of optimization. In a minimization problem, a gradient often points downhill. In a saddle problem, the joint operator can rotate, and an algorithm that blindly follows it may fail even when the problem is convex-concave.

The predictive evaluation detects some of that rotation and compensates for it. Bregman geometry then adapts the correction to the feasible set. The resulting method handles an important class of monotone variational inequalities with a sharp first-order ergodic rate, rather than relying on a mistaken assumption that simultaneous descent and ascent behave like ordinary optimization.

## Stochastic Mirror-Prox and the Cost of Noisy Oracles

A saddle-point problem asks us to minimize over one variable and maximize over another. When the objective is convex in the first variable and concave in the second, its associated variational-inequality operator is monotone. That monotonicity is weaker than ordinary convex minimization, because the operator can rotate around a solution instead of pointing straight toward it.

Mirror-Prox handles this rotation by evaluating the operator twice. The first evaluation predicts where the current step might go. The second evaluation, made at the predicted point, corrects the original iterate. In deterministic smooth problems, this extragradient structure yields an inverse-iteration convergence rate for a suitable averaged solution.

But in data-driven applications, an exact operator may be too expensive. We might estimate gradients from random samples, mini-batches, simulation outputs, or a stochastic oracle. The predictor and corrector then receive noisy vectors. The central question becomes whether the two-step benefit survives, and what new error term must be paid for randomness.

## Begin with the bilinear rotation

Consider the simplest saddle objective: x times y, minimized over x and maximized over y. Its variational-inequality operator sends the pair x, y to y, negative x. This operator is monotone, because the symmetric part of its Jacobian is zero, but it is not strongly monotone. Its arrows rotate around the origin.

From the point one, zero, ordinary simultaneous gradient descent–ascent takes a small step in the positive y direction. The new distance from the origin increases. Repeating the procedure creates a spiral outward if no constraint projection intervenes.

Mirror-Prox behaves differently. Its predictor moves to one, eta. Evaluating the rotating operator there and correcting from the original point gives one minus eta squared, eta. For a step size strictly between zero and one, the squared distance to the origin decreases.

This exact calculation isolates what the extra evaluation accomplishes. It corrects for rotation, not because the operator becomes a gradient of a convex potential, but because the second evaluation anticipates the direction change within a step.

## Add an unbiased stochastic oracle

Suppose an oracle returns an operator estimate whose conditional expectation equals the true operator at the query point. Assume its error has bounded second moment. These are mathematical assumptions about the sampling process, not automatic consequences of calling the oracle stochastic.

At each iteration, use one sample to construct the prediction and an appropriate fresh sample to evaluate the correction. The second evaluation occurs at a random point chosen using the first sample. Independence or suitable conditional unbiasedness is important here: reusing a correlated sample can create a biased estimate at the predicted point even when each fixed-point oracle call looks unbiased in isolation.

The method also needs a feasible set and a geometry for measuring distances. In Euclidean space, the prox step is ordinary projection. In a simplex, entropy-based Bregman geometry can produce multiplicative or mirror-style updates that respect positivity and normalization.

The resulting algorithm is called stochastic Mirror-Prox. It combines the deterministic rotation correction with an analysis that controls martingale noise.

## Why two errors appear in the convergence bound

There are two sources of inaccuracy. Even with exact evaluations, a finite number of iterations leaves a discretization or algorithmic error. For a Lipschitz monotone operator on a suitable compact convex set, the deterministic part of a gap bound decreases like the Lipschitz scale times a squared diameter divided by the number of iterations.

Sampling contributes a different term. When the noise has standard-deviation scale sigma, the stochastic contribution decreases roughly like sigma times the diameter divided by the square root of the number of iterations. The square root reflects accumulation of independent mean-zero fluctuations. It is not an artifact that can simply be removed by choosing a clever constant step size.

A standard expected-gap bound has the form of the deterministic inverse-iteration term plus the stochastic inverse-square-root term, with constants, mirror geometry, and step-size requirements specified by the theorem. If sigma is zero, the deterministic rate remains. If the noise is fixed and nonzero, the stochastic term eventually dominates.

This conclusion is about the appropriate averaged or ergodic iterate and a defined gap measure. It does not automatically give the same rate for the final raw iterate. Nor does an expected gap bound imply a high-probability guarantee without extra tail assumptions or a concentration argument.

## Mini-batches trade data for accuracy

Suppose each oracle evaluation averages m independent samples with bounded variance. Its variance is reduced by a factor of m, so the stochastic scale falls like one over the square root of m.

In an expected-gap bound, the noise term then behaves like sigma times diameter divided by the square root of m times the number of iterations. That sounds attractive, but each iteration uses more samples. If total sample budget is fixed, enlarging batches may not improve the leading sample complexity, even though it can reduce synchronization or communication costs.

The deterministic term still depends on the number of iterations, not the number of samples. Thus batching can be helpful when iteration latency is expensive and parallel sampling is cheap. In a sequential oracle model, its benefit must be evaluated against the total number of operator samples.

This illustrates a general principle in stochastic optimization. Iteration complexity and sample complexity are not interchangeable. A method can converge in fewer iterations while consuming more data or simulation calls.

## Projection and mirror geometry matter

If the feasible set is a Euclidean ball or box, projection is a convenient prox operation. If the variables are probabilities on a simplex, Euclidean geometry can be poorly matched to their scale and constraints. An entropy-based distance-generating function may control the problem more naturally.

Mirror-Prox uses a Bregman divergence rather than requiring ordinary squared Euclidean distance. Its proof relies on a three-point prox inequality and monotonicity of the operator. In stochastic analysis, the same inequality also provides a place to isolate martingale differences and their second moments.

Not every choice of mirror map works without qualification. The generating function must satisfy the needed convexity and domain assumptions, and the oracle's dual norm must match the chosen geometry. If coordinates can approach the boundary where an entropy gradient diverges, implementation and analysis must handle the corresponding interior behavior.

## Stochastic does not mean automatically unbiased

Several practical effects can break the model. A simulation gradient may include numerical discretization bias. A learned surrogate may have systematic approximation error. Clipping a noisy vector generally changes its expectation. Data chosen adaptively from a feedback loop may not provide the conditional independence assumed in a proof.

Such errors can create a residual bias floor that does not vanish at the inverse-square-root rate. A useful convergence statement must therefore identify the oracle model, the exact conditioning in the unbiasedness assertion, and whether the variance bound is uniform over the feasible set.

The predictor-corrector structure is also sensitive to how randomness is coupled. Common random numbers can reduce variance in some applications, but the mathematical proof may need to be changed when predictor and corrector noise are correlated. Reusing samples is an algorithmic choice, not an invisible implementation optimization.

## From saddle games to stochastic feasibility

Stochastic Mirror-Prox applies to many monotone variational inequalities, including saddle-point optimization and some semidefinite feasibility formulations. It is particularly useful when operator evaluations are high-dimensional but unbiased samples are accessible.

The guarantee is strongest when its conditions match the problem: convex compact feasible geometry, monotone Lipschitz operator, a prox mapping that can be computed accurately, and a specified stochastic oracle. Extensions address unbounded domains, composite terms, strong monotonicity, and variance reduction, but each demands its own analysis.

The bilinear rotation remains the simplest explanation of the algorithm. Ordinary descent–ascent follows the rotating field outward. Mirror-Prox uses a look-ahead to counteract that rotation. Noise adds a statistical price that decays more slowly than the deterministic error. Both mechanisms are visible in a single convergence bound, and neither should be hidden behind the phrase “the stochastic version works too.”

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Monotone Operators, Resolvents, and Splitting Methods

**Track:** Optimization and Duality. **Background:** convex subgradients, proximal maps, Hilbert spaces, fixed-point iteration. **Central question:** how can a difficult optimality condition be solved using simpler operators one at a time?

#### Mathematical companion (not spoken)

For a real Hilbert space H and set-valued \(A:H\rightrightarrows H\), monotonicity means \(\langle x-y,a-b\rangle\ge0\) whenever \(a\in Ax,b\in Ay\). A is **maximal monotone** if its graph has no proper monotone extension. Its resolvent is
\[J_{\gamma A}=(I+\gamma A)^{-1},\qquad\gamma>0.\]
For maximal monotone A, the resolvent is single valued, everywhere defined, and firmly nonexpansive:
\[\|Jx-Jy\|^2\le\langle Jx-Jy,x-y\rangle.\]
Proof: \((x-Jx)/\gamma\in A(Jx)\) and \((y-Jy)/\gamma\in A(Jy)\), so apply monotonicity and rearrange.

If f is proper, lower-semicontinuous and convex, \(\partial f\) is maximal monotone and \(J_{\gamma\partial f}=\operatorname{prox}_{\gamma f}\). For \(f(x)=|x|\) in R,
\[\operatorname{prox}_{\gamma f}(z)=\mathrm{sign}(z)\max(|z|-\gamma,0).\]
For the indicator \(\iota_C\) of a nonempty closed convex set C, \(\operatorname{prox}_{\gamma\iota_C}=P_C\).

**Douglas–Rachford splitting:** for proper lsc convex f,g in finite dimensions and parameters \(\gamma>0\), define
\[u_k=\operatorname{prox}_{\gamma g}(z_k),\quad v_k=\operatorname{prox}_{\gamma f}(2u_k-z_k),\quad z_{k+1}=z_k+v_k-u_k.\]
Under standard solution-existence and operator-sum regularity assumptions, z_k converges to a fixed point and the shadow sequence u_k approaches a minimizer of f+g. For a differentiable convex f with L-Lipschitz gradient, **forward–backward** is \(x_{k+1}=\operatorname{prox}_{\gamma g}(x_k-\gamma\nabla f(x_k))\) with suitable \(0<\gamma<2/L\) and a nonempty solution set.

##### Exercises with answers

1. Compute \(\operatorname{prox}_{2|\cdot|}(1.5)\). **Answer:** zero, since the threshold 2 exceeds the input magnitude.
2. What is the proximal map of the indicator of [0,1] at z=3? **Answer:** 1, the Euclidean projection.
3. Why is every resolvent of a maximal monotone operator nonexpansive? **Answer:** firm nonexpansiveness implies \(\|Jx-Jy\|\le\|x-y\|\) by Cauchy–Schwarz.
4. Is a Douglas–Rachford fixed point necessarily itself the minimizer? **Answer:** no; a resolvent of the fixed point yields a primal solution.

##### Reading and source notes

- [Parikh and Boyd, Proximal Algorithms](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf), resolvents and splitting schemes.
- [Boyd et al., ADMM](https://stanford.edu/~boyd/admm), operator splitting and its relation to constrained optimization.
- [Giselsson and Boyd, Douglas–Rachford and ADMM scaling](https://stanford.edu/~boyd/papers/pdf/diag_scaling_DR_ADMM.pdf), firm nonexpansiveness and proximal operators.

### Inexact Proximal Algorithms: Convergence When Inner Solves Are Imperfect

**Track:** Optimization and Duality. **Background:** convex composite optimization, proximal maps, first-order conditions and convergence estimates. **Central question:** how much error can we tolerate when each optimization step is itself solved approximately?

#### Mathematical companion (not spoken)

Let `F=f+g`, with f convex differentiable and `L`-Lipschitz gradient, and g proper, lower semicontinuous and convex. The proximal-gradient update for `0<alpha<=1/L` is
\[
z=T_\alpha(x):=\operatorname{prox}_{\alpha g}(x-\alpha\nabla f(x)),
\quad G_\alpha(x)=\frac{x-T_\alpha(x)}\alpha.
\]
Optimality of z gives `0 in partial g(z)+nabla f(x)+(z-x)/alpha`. Since g is convex and f is L-smooth, one obtains
\[
F(z)\le F(x)-\left(\frac1\alpha-\frac L2\right)\|z-x\|^2,
\]
when the function values are finite. `G_alpha(x)=0` if and only if `0 in nabla f(x)+partial g(x)`; for convex F, this is the global optimality condition.

If an approximate point `z_tilde` satisfies `||z_tilde-z||<=epsilon`, then the approximate mapping `G_tilde=(x-z_tilde)/alpha` obeys the certified comparison
\[
\|G_\alpha(x)-\widetilde G_\alpha(x)\|\le\epsilon/\alpha.
\]
A small `||G_tilde||` is only meaningful if epsilon is controlled. If g is an indicator, arbitrary point errors do not imply feasibility. A residual in the proximal optimality inclusion is a different error model from `||z_tilde-z||` and needs its own conversion theorem.

**Exact example.** `f(x)=(x-3)^2/2`, `g(x)=|x|`, `alpha=1`. For any x, `x-alpha f'(x)=3`, hence `T_1(x)=soft(3,1)=2`, the minimizer. At `x=2.001`, `f'(x)+g'(x)=x-3+1=0.001`.

With inexact nonexpansive fixed-point iterations, absolute summability `sum_k ||e_k||<infinity` is a common sufficient hypothesis in convergence theorems. Whether the same conclusion holds for a particular inexact proximal-gradient implementation depends on the exact iteration, domain, and error model. An `epsilon_k->0` condition by itself is not generally a substitute for a correct theorem.

##### Exercises with answers

1. If an approximate proximal point has error at most `10^-4` and `alpha=0.1`, how far can its gradient mapping be from the exact one? **Answer:** at most `10^-3` in norm.
2. Does an infeasible point close to a projection automatically have finite indicator-penalty objective? **Answer:** no.
3. What does `G_alpha(x)=0` mean for a convex composite problem? **Answer:** the convex first-order optimality condition holds, so x minimizes F.
4. Is `epsilon_k->0` identical to `sum epsilon_k<infinity`? **Answer:** no; for example `epsilon_k=1/sqrt(k)` tends to zero but is not summable.

##### Reading and source notes

- [Parikh and Boyd, Proximal Algorithms](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf), proximal operators, splitting and convergence.
- [Schmidt, Le Roux, and Bach, Convergence Rates of Inexact Proximal-Gradient Methods for Convex Optimization](https://arxiv.org/abs/1109.2415), explicit inexactness models and rates.
- [Beck and Teboulle, A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems](https://doi.org/10.1137/080716542), composite proximal-gradient methods and rates.

### Mirror-Prox: Solving Monotone Games Without Rotating Forever

**Track:** Optimization and Duality. **Background:** convex analysis, saddle-point problems, monotone operators, and Bregman divergences. **Central question:** why does an extra gradient evaluation stabilize a method for monotone saddle-point problems?

#### Mathematical companion (not spoken)

Let `F:Z->R^d` be monotone, `Z` compact convex, and `omega` a 1-strongly-convex distance generator (relative to a norm). Define `V_z(u)=omega(u)-omega(z)-<grad omega(z),u-z>` and
\[
\operatorname{Prox}_z(\xi)=\arg\min_{u\in Z}\{\langle\xi,u\rangle+V_z(u)\}.
\]
Mirror-Prox uses `w_t=Prox_(z_t)(gamma F(z_t))`, `z_(t+1)=Prox_(z_t)(gamma F(w_t))`; both steps are centered at z_t. With monotone L-Lipschitz F and appropriate gamma (for example conservative gamma <=1/(2L)), the averaged predictor `wbar=(1/T)sum w_t` enjoys an ergodic gap `O(L Omega/T)` for bounded Bregman diameter Omega, under standard VI assumptions.

For `phi(x,y)=xy`, `F(x,y)=(y,-x)=Jz`, `J^2=-I`, so naive gradient gives `z+ = (I-gamma J)z` and `||z+||^2=(1+gamma^2)||z||^2`. Unconstrained Euclidean extragradient gives
\[
 z_+=(I-\gamma J+\gamma^2J^2)z=((1-\gamma^2)I-\gamma J)z,
\]
with `||z+||^2=(1-gamma^2+gamma^4)||z||^2`, strictly smaller for `0<gamma<1`. This contraction is a property of the toy linear problem, **not** the general Mirror-Prox rate. For `omega(p)=sum_i p_i log(p_i)` on a simplex, prox has multiplicative/exponentiated-gradient form.

##### Exercises with answers

1. Is `F(z)=Jz` strongly monotone for the skew rotation J? **Answer:** no; its monotonicity inner product is zero for every pair of points.
2. For gamma=1/2, what is the squared-distance multiplier of extragradient in the bilinear example? **Answer:** `1-1/4+1/16=13/16`.
3. Which point centers the second Mirror-Prox step? **Answer:** the original iterate z_t, not the predictor w_t.
4. Does an ergodic gap rate establish that every last iterate contracts geometrically? **Answer:** no; stronger conditions are needed for a last-iterate or linear rate.

##### Reading and source notes

- [Arkadi Nemirovski, Prox-Method with Rate O(1/t) for Lipschitz Monotone Variational Inequalities](https://www2.isye.gatech.edu/~nemirovs/SIOPT_MP_2004.pdf), the original Mirror-Prox method and proof.
- [European Mathematical Society, Survey of Monotone Stochastic Variational Inequalities](https://euromathsoc.org/magazine/articles/112), extragradient and Mirror-Prox formulations.
- [Bauschke and Combettes, Convex Analysis and Monotone Operator Theory in Hilbert Spaces](https://link.springer.com/book/10.1007/978-3-319-48311-5), proximal geometry and monotone operators.

### Stochastic Mirror-Prox and the Cost of Noisy Oracles

**Track:** Optimization and Duality. **Background:** convex-concave games, monotone variational inequalities, proximal geometry, and stochastic gradients. **Central question:** what survives of an extragradient convergence theorem when each operator evaluation is noisy?

#### Mathematical companion (not spoken)

For convex-concave `L(x,y)=xy`, the monotone VI operator is `F(x,y)=(y,-x)`. Starting at `z=(1,0)`, with Euclidean unconstrained Mirror-Prox predictor `w=z-eta F(z)=(1,eta)` and corrector `z^+=z-eta F(w)=(1-eta^2,eta)`,
\[
\|z^+\|^2=1-\eta^2+\eta^4<1\quad(0<\eta<1),
\]
whereas a simultaneous descent-ascent step has squared norm `1+eta^2`.

For a compact convex feasible set of diameter scale `D`, monotone `L`-Lipschitz operator, and conditionally unbiased stochastic oracle of bounded second-moment noise scale `sigma`, appropriately tuned stochastic Mirror-Prox yields a typical **expected ergodic gap** order
\[
O(LD^2/T+\sigma D/\sqrt T).
\]
Constants, dual norms, prox geometry, two-oracle sampling rules, and assumptions differ by theorem. Mini-batches of m independent samples reduce noise variance from `sigma^2` to `sigma^2/m`. The result does not automatically hold for the last raw iterate or under biased/correlated oracle errors.

##### Exercises with answers

1. Compute the corrected iterate for `eta=1/2` in the bilinear example. **Answer:** `(3/4,1/2)`.
2. What is its squared distance from the origin? **Answer:** `9/16+1/4=13/16`, below one.
3. How does averaging m independent equal-variance oracle samples change standard deviation? **Answer:** divides it by `sqrt(m)`.
4. Why is an expected ergodic-gap bound not automatically a high-probability last-iterate bound? **Answer:** it controls a different random quantity and needs additional assumptions to strengthen.

##### Reading and source notes

- [Juditsky, Nemirovski, and Tauvel, Stochastic Mirror-Prox](https://arxiv.org/abs/0809.0815), stochastic variational inequality analysis and rates.
- [Bach and Levy, A Universal Algorithm for Variational Inequalities](https://proceedings.mlr.press/v99/bach19a/bach19a.pdf), comparison of deterministic and stochastic Mirror-Prox convergence terms.
