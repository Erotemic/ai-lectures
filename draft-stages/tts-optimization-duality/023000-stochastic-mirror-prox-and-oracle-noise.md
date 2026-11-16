# 023000 - Stochastic Mirror-Prox and the Cost of Noisy Oracles

**Track:** Optimization and Duality. **Background:** convex-concave games, monotone variational inequalities, proximal geometry, and stochastic gradients. **Central question:** what survives of an extragradient convergence theorem when each operator evaluation is noisy?

<!-- BEGIN SPOKEN LECTURE -->

# The two-step correction meets noisy data

A saddle-point problem asks us to minimize over one variable and maximize over another. When the objective is convex in the first variable and concave in the second, its associated variational-inequality operator is monotone. That monotonicity is weaker than ordinary convex minimization, because the operator can rotate around a solution instead of pointing straight toward it.

Mirror-Prox handles this rotation by evaluating the operator twice. The first evaluation predicts where the current step might go. The second evaluation, made at the predicted point, corrects the original iterate. In deterministic smooth problems, this extragradient structure yields an inverse-iteration convergence rate for a suitable averaged solution.

But in data-driven applications, an exact operator may be too expensive. We might estimate gradients from random samples, mini-batches, simulation outputs, or a stochastic oracle. The predictor and corrector then receive noisy vectors. The central question becomes whether the two-step benefit survives, and what new error term must be paid for randomness.

# Begin with the bilinear rotation

Consider the simplest saddle objective: x times y, minimized over x and maximized over y. Its variational-inequality operator sends the pair x, y to y, negative x. This operator is monotone, because the symmetric part of its Jacobian is zero, but it is not strongly monotone. Its arrows rotate around the origin.

From the point one, zero, ordinary simultaneous gradient descent–ascent takes a small step in the positive y direction. The new distance from the origin increases. Repeating the procedure creates a spiral outward if no constraint projection intervenes.

Mirror-Prox behaves differently. Its predictor moves to one, eta. Evaluating the rotating operator there and correcting from the original point gives one minus eta squared, eta. For a step size strictly between zero and one, the squared distance to the origin decreases.

This exact calculation isolates what the extra evaluation accomplishes. It corrects for rotation, not because the operator becomes a gradient of a convex potential, but because the second evaluation anticipates the direction change within a step.

# Add an unbiased stochastic oracle

Suppose an oracle returns an operator estimate whose conditional expectation equals the true operator at the query point. Assume its error has bounded second moment. These are mathematical assumptions about the sampling process, not automatic consequences of calling the oracle stochastic.

At each iteration, use one sample to construct the prediction and an appropriate fresh sample to evaluate the correction. The second evaluation occurs at a random point chosen using the first sample. Independence or suitable conditional unbiasedness is important here: reusing a correlated sample can create a biased estimate at the predicted point even when each fixed-point oracle call looks unbiased in isolation.

The method also needs a feasible set and a geometry for measuring distances. In Euclidean space, the prox step is ordinary projection. In a simplex, entropy-based Bregman geometry can produce multiplicative or mirror-style updates that respect positivity and normalization.

The resulting algorithm is called stochastic Mirror-Prox. It combines the deterministic rotation correction with an analysis that controls martingale noise.

# Why two errors appear in the convergence bound

There are two sources of inaccuracy. Even with exact evaluations, a finite number of iterations leaves a discretization or algorithmic error. For a Lipschitz monotone operator on a suitable compact convex set, the deterministic part of a gap bound decreases like the Lipschitz scale times a squared diameter divided by the number of iterations.

Sampling contributes a different term. When the noise has standard-deviation scale sigma, the stochastic contribution decreases roughly like sigma times the diameter divided by the square root of the number of iterations. The square root reflects accumulation of independent mean-zero fluctuations. It is not an artifact that can simply be removed by choosing a clever constant step size.

A standard expected-gap bound has the form of the deterministic inverse-iteration term plus the stochastic inverse-square-root term, with constants, mirror geometry, and step-size requirements specified by the theorem. If sigma is zero, the deterministic rate remains. If the noise is fixed and nonzero, the stochastic term eventually dominates.

This conclusion is about the appropriate averaged or ergodic iterate and a defined gap measure. It does not automatically give the same rate for the final raw iterate. Nor does an expected gap bound imply a high-probability guarantee without extra tail assumptions or a concentration argument.

# Mini-batches trade data for accuracy

Suppose each oracle evaluation averages m independent samples with bounded variance. Its variance is reduced by a factor of m, so the stochastic scale falls like one over the square root of m.

In an expected-gap bound, the noise term then behaves like sigma times diameter divided by the square root of m times the number of iterations. That sounds attractive, but each iteration uses more samples. If total sample budget is fixed, enlarging batches may not improve the leading sample complexity, even though it can reduce synchronization or communication costs.

The deterministic term still depends on the number of iterations, not the number of samples. Thus batching can be helpful when iteration latency is expensive and parallel sampling is cheap. In a sequential oracle model, its benefit must be evaluated against the total number of operator samples.

This illustrates a general principle in stochastic optimization. Iteration complexity and sample complexity are not interchangeable. A method can converge in fewer iterations while consuming more data or simulation calls.

# Projection and mirror geometry matter

If the feasible set is a Euclidean ball or box, projection is a convenient prox operation. If the variables are probabilities on a simplex, Euclidean geometry can be poorly matched to their scale and constraints. An entropy-based distance-generating function may control the problem more naturally.

Mirror-Prox uses a Bregman divergence rather than requiring ordinary squared Euclidean distance. Its proof relies on a three-point prox inequality and monotonicity of the operator. In stochastic analysis, the same inequality also provides a place to isolate martingale differences and their second moments.

Not every choice of mirror map works without qualification. The generating function must satisfy the needed convexity and domain assumptions, and the oracle's dual norm must match the chosen geometry. If coordinates can approach the boundary where an entropy gradient diverges, implementation and analysis must handle the corresponding interior behavior.

# Stochastic does not mean automatically unbiased

Several practical effects can break the model. A simulation gradient may include numerical discretization bias. A learned surrogate may have systematic approximation error. Clipping a noisy vector generally changes its expectation. Data chosen adaptively from a feedback loop may not provide the conditional independence assumed in a proof.

Such errors can create a residual bias floor that does not vanish at the inverse-square-root rate. A useful convergence statement must therefore identify the oracle model, the exact conditioning in the unbiasedness assertion, and whether the variance bound is uniform over the feasible set.

The predictor-corrector structure is also sensitive to how randomness is coupled. Common random numbers can reduce variance in some applications, but the mathematical proof may need to be changed when predictor and corrector noise are correlated. Reusing samples is an algorithmic choice, not an invisible implementation optimization.

# From saddle games to stochastic feasibility

Stochastic Mirror-Prox applies to many monotone variational inequalities, including saddle-point optimization and some semidefinite feasibility formulations. It is particularly useful when operator evaluations are high-dimensional but unbiased samples are accessible.

The guarantee is strongest when its conditions match the problem: convex compact feasible geometry, monotone Lipschitz operator, a prox mapping that can be computed accurately, and a specified stochastic oracle. Extensions address unbounded domains, composite terms, strong monotonicity, and variance reduction, but each demands its own analysis.

The bilinear rotation remains the simplest explanation of the algorithm. Ordinary descent–ascent follows the rotating field outward. Mirror-Prox uses a look-ahead to counteract that rotation. Noise adds a statistical price that decays more slowly than the deterministic error. Both mechanisms are visible in a single convergence bound, and neither should be hidden behind the phrase “the stochastic version works too.”

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Compute the corrected iterate for `eta=1/2` in the bilinear example. **Answer:** `(3/4,1/2)`.
2. What is its squared distance from the origin? **Answer:** `9/16+1/4=13/16`, below one.
3. How does averaging m independent equal-variance oracle samples change standard deviation? **Answer:** divides it by `sqrt(m)`.
4. Why is an expected ergodic-gap bound not automatically a high-probability last-iterate bound? **Answer:** it controls a different random quantity and needs additional assumptions to strengthen.

### Reading and source notes

- [Juditsky, Nemirovski, and Tauvel, Stochastic Mirror-Prox](https://arxiv.org/abs/0809.0815), stochastic variational inequality analysis and rates.
- [Bach and Levy, A Universal Algorithm for Variational Inequalities](https://proceedings.mlr.press/v99/bach19a/bach19a.pdf), comparison of deterministic and stochastic Mirror-Prox convergence terms.
