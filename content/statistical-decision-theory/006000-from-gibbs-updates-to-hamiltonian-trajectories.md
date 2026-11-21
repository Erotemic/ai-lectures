# 006000 — From Gibbs Updates to Hamiltonian Trajectories

**Track:** Statistical Decision Theory and Bayesian Computation. **Preparation:** Metropolis–Hastings, conditional normal distributions, basic derivatives. **Theme:** sampler geometry, not just target correctness, determines the usefulness of posterior draws.

<!-- BEGIN SPOKEN LECTURE -->

# From Gibbs Updates to Hamiltonian Trajectories

A Metropolis–Hastings chain can have the correct stationary distribution and still move so slowly that an afternoon of computation tells us little. That is especially common when the posterior has strong dependencies among its parameters. One parameter can change only when another changes, but the sampler proposes moving them in ways that repeatedly collide with low-probability regions.

Two major families of sampling methods address the problem in different ways. Gibbs sampling uses conditional distributions to update one part of a parameter vector at a time. Hamiltonian Monte Carlo, or HMC, uses gradients to construct long, coordinated proposals through a continuous parameter space. Both can be mathematically correct, and both can fail to explore a difficult posterior well. Understanding the mechanisms helps us tell those cases apart.

## Gibbs sampling: use the conditionals you know

Suppose our target is a joint distribution for variables X and Y. We can sample X conditional on Y, and Y conditional on X, even if sampling the joint distribution directly is inconvenient. Gibbs sampling alternates these conditional draws. Given the current Y, draw a fresh X from the exact conditional distribution. Given that new X, draw a fresh Y from its exact conditional distribution. Then repeat.

Each conditional update preserves the joint target distribution. To understand why, suppose the current pair has the correct joint law. If we keep Y fixed and redraw X from the actual conditional distribution of X given that Y, the resulting pair still has that same joint law. The argument is simply the factorization of the joint probability into the marginal of Y times the conditional of X given Y. The same reasoning applies to the next update.

Notice the difference from proposing and possibly rejecting a change. An exact Gibbs update is accepted automatically because we draw directly from the correct conditional. Gibbs can also be understood as a special Metropolis-type update with acceptance probability one. But the ability to sample conditionals does not guarantee that alternating them explores the joint distribution quickly.

To see the limitation, use a bivariate normal target in which X and Y each have mean zero and variance one, with correlation rho. The conditional distribution of X given Y equal to y is normal with mean rho times y and variance one minus rho squared. The conditional distribution of Y given X has the analogous form.

Write one complete Gibbs sweep as two equations. First X new equals rho times Y old plus independent normal noise with standard deviation the square root of one minus rho squared. Then Y new equals rho times X new plus another independent noise term with the same standard deviation. Substitute the first equation into the second. The conditional expectation of Y new given Y old is rho squared times Y old.

Thus, in the sequence of completed sweeps, the old Y has coefficient rho squared in the new Y. If rho is nine tenths, that coefficient is zero point eight one. If rho is ninety-nine hundredths, it is zero point nine eight zero one. For the latter target, a deviation in Y is expected to diminish by only about two percent per sweep. The chain can be stationary while successive sweeps retain strong dependence.

The example suggests a geometric picture. A highly correlated bivariate normal looks like a narrow diagonal ellipse. Updating only the horizontal coordinate and then only the vertical coordinate traces a slow staircase along that ellipse. There may be no rejection at all, but exploration remains inefficient. Reparameterizing into directions aligned with the ellipse can drastically change mixing behavior.

## Block updates and hierarchical models

Gibbs sampling is especially attractive when a model has tractable conditional distributions. In hierarchical normal models, for example, one may be able to draw team-specific effects given hyperparameters and then hyperparameters given the team effects. Conjugacy can turn difficult integration into a sequence of simple conditional draws.

But a long chain of highly correlated components can create exactly the staircase problem. Updating each parameter separately may ignore the geometry of the joint posterior. Block Gibbs methods draw several related parameters together. Marginalizing latent variables can eliminate the strongest dependence. Noncentered parameterizations sometimes convert an awkward hierarchy into a geometry that is easier to traverse, although no single parameterization dominates in every data regime.

We should also be precise about invariance and reversibility. A single conditional Gibbs kernel satisfies detailed balance with respect to the target. A fixed sequence of different coordinate updates preserves the target because the composition of invariant kernels remains invariant. But that full deterministic-scan composition need not itself satisfy detailed balance. Stationarity is the property we actually need; reversibility is one sufficient route to it, not the definition.

## Hamiltonian Monte Carlo: move with the gradient

Hamiltonian Monte Carlo begins with a different idea. Suppose our posterior has a differentiable density proportional to the exponential of minus a potential energy U of theta. Usually U is simply negative log unnormalized posterior, up to an irrelevant constant. Introduce an auxiliary momentum variable r with a Gaussian distribution. The resulting joint target for position and momentum is proportional to the exponential of minus the Hamiltonian H, where H is the sum of potential energy U of theta and kinetic energy, one half r transposed times the inverse mass matrix times r.

If we could follow the exact Hamiltonian equations of motion, the trajectory would preserve H and move through the joint target without the random-walk behavior of small independent proposals. The equations say that the time derivative of position is the inverse mass matrix times momentum, while the time derivative of momentum is the negative gradient of U. Gradient information steers movement along the posterior's contours instead of proposing blind jumps.

Actual computers cannot usually solve those differential equations exactly. They use a numerical integrator called leapfrog. One leapfrog step moves the momentum a half step using the gradient, moves the position a full step using the current momentum, then moves momentum another half step using the gradient at the new position. Repeating these steps traces an approximate trajectory.

The numerical integrator changes energy slightly. To restore the correct stationary distribution, HMC adds a Metropolis accept-or-reject correction based on the change in Hamiltonian energy. The acceptance probability is the smaller of one and the exponential of old energy minus new energy. In the standard construction, reversible and volume-preserving leapfrog dynamics, a momentum reversal where needed, and the Metropolis correction combine to give the desired invariant joint distribution. Resampling momentum between trajectories makes the chain explore new directions.

The distinction between continuous Hamiltonian dynamics and its numerical approximation is central. Exact dynamics preserve the energy level and volume. Leapfrog approximates that behavior with carefully structured error. The acceptance step corrects finite integration error; it does not make an arbitrarily inaccurate trajectory computationally efficient. A step size that is too large causes large energy errors and frequent rejection, while a tiny step size can require excessive gradient evaluations.

## Why gradients help, and where they do not

Imagine a long narrow posterior ellipse. A random-walk proposal must be small enough to avoid falling off the narrow direction, but small steps are inefficient along the long direction. HMC uses the local gradient to move coherently, potentially covering a substantial distance in one accepted proposal. A well-chosen mass matrix rescales coordinates so that the numerical trajectories are better matched to the posterior geometry.

This is not a theorem that HMC always beats Gibbs or random-walk Metropolis. Posterior distributions with abrupt boundaries, discontinuous densities, disconnected regions, discrete parameters, or extreme geometric variation can be difficult for ordinary HMC. Nondifferentiable models may need reformulation or a different sampler. Complex hierarchical geometries can create narrow funnels in which an integrator that works at one scale becomes inaccurate at another.

The no-U-turn sampler, commonly abbreviated NUTS, adapts trajectory length rather than requiring the user to choose a fixed number of leapfrog steps. It has a carefully constructed transition rule; the adaptation of step size and mass matrix during warm-up is another algorithmic component. One should not assume that arbitrary trajectory tuning during stationary sampling leaves the target unchanged without the corresponding correctness argument.

## Diagnostics are about finite computation

The result of an MCMC run is a finite collection of dependent draws. We need to know whether that collection supports the numerical claims we want to make. A trace plot can reveal drift or chains stuck in separate regions. Multiple chains with dispersed initial values can show disagreement. But a plot that looks like a fuzzy cloud is not a mathematical convergence certificate.

One widely used diagnostic, R-hat, compares within-chain and between-chain variation. Modern implementations use splitting and rank normalization and can compare folded transformations to detect differences in scale as well as location. Values noticeably greater than one indicate that chains have not mixed well relative to each other. A value close to one is reassuring but cannot prove that all important modes have been discovered.

Effective sample size estimates how much information the dependent draws contain about a particular functional of the posterior. Bulk and tail effective sample sizes focus on different parts of the distribution. A sampler can estimate the center of a distribution with reasonable accuracy while providing very poor tail probabilities. For decisions driven by rare outcomes, tail behavior deserves direct scrutiny.

Hamiltonian samplers expose additional warnings. A divergent transition indicates that the numerical trajectory encountered a region where the integrator's behavior was problematic at the chosen settings. Divergences can signal important regions the sampler is not exploring faithfully. Merely discarding divergent draws is not a principled repair. One may need a better parameterization, stronger model identification, a different metric, or smaller step sizes, and must then recheck the computation.

An estimated standard error from MCMC is also not the same as posterior standard deviation. The posterior standard deviation describes uncertainty about a parameter within the fitted model. The Monte Carlo standard error describes uncertainty in the numerical approximation to a particular posterior summary. Running longer can shrink Monte Carlo error, subject to sufficient mixing; it does not resolve the posterior's inherent uncertainty or repair a wrong scientific model.

## A hierarchy of proof obligations

There is a useful chain of guarantees behind every reported posterior interval. First, the statistical model defines a target posterior. Second, a transition kernel should have that posterior as invariant, and under suitable conditions should converge to it. Third, a finite computation must approximate the relevant expectations accurately enough. Fourth, the model's predictions should survive checks tied to the intended use. Finally, a decision based on those predictions must use a defensible loss function.

A perfectly correct stationary distribution does not imply fast convergence. Fast convergence does not imply that the likelihood models reality. A well-calibrated predictive model does not automatically choose the right action. These are distinct mathematical and empirical obligations. Understanding the distinctions lets us diagnose failure instead of merely turning a sampler's iteration count upward.

The bivariate normal example supplies a concrete closing thought. Its Gibbs updates are exact conditional samples. Every sweep preserves the target. Yet at correlation zero point nine nine, the persistence coefficient is zero point nine eight zero one, so consecutive sweeps remain strongly related. A cleverer coordinate system or sampler can make a major difference without changing the posterior itself. Bayesian computation is not only about defining what should be sampled. It is about designing, proving, and evaluating a procedure that can actually explore it.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Bivariate normal Gibbs.** If \((X,Y)\sim N(0,\Sigma)\), \(\Sigma=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\), \(|\rho|<1\), then
\[
 X\mid Y=y\sim N(\rho y,1-\rho^2),\quad
 Y\mid X=x\sim N(\rho x,1-\rho^2).
\]
One deterministic two-step sweep with independent standard normals \(Z_1,Z_2\) is
\[
 X_{t+1}=\rho Y_t+\sqrt{1-\rho^2}Z_1,\quad
 Y_{t+1}=\rho X_{t+1}+\sqrt{1-\rho^2}Z_2
=\rho^2Y_t+\rho\sqrt{1-\rho^2}Z_1+\sqrt{1-\rho^2}Z_2.
\]
Thus \(E[Y_{t+1}\mid Y_t]=\rho^2 Y_t\); persistence \(.81\) at \(\rho=.9\), \(.9801\) at \(\rho=.99\).

**HMC.** For differentiable \(\pi(\theta)\propto e^{-U(\theta)}\), momentum \(r\sim N(0,M)\),
\[
H(\theta,r)=U(\theta)+\frac12r^TM^{-1}r,\quad
\dot\theta=M^{-1}r,\quad\dot r=-\nabla U(\theta).
\]
Leapfrog with step \(\epsilon\) uses
\[
 r_{1/2}=r_0-\tfrac\epsilon2\nabla U(\theta_0),\quad
 \theta_1=\theta_0+\epsilon M^{-1}r_{1/2},\quad
 r_1=r_{1/2}-\tfrac\epsilon2\nabla U(\theta_1).
\]
With the required reversibility/volume conditions and momentum handling, Metropolis acceptance is \(\min(1,e^{H_{old}-H_{new}})\).

**Diagnostics.** Rank-normalized split \(\widehat R\) compares chains, effective sample size is functional-dependent, and divergent HMC transitions point to integration/geometric difficulties. No finite diagnostic proves convergence or correct model specification.

**Exercises and solutions.** (1) Why do exact conditional updates preserve the joint target? *They reproduce its conditional factorization.* (2) Can composing two reversible Gibbs kernels yield a nonreversible full-sweep kernel? *Yes; invariance is preserved but reversibility need not be.* (3) Why is an HMC accept step needed after leapfrog integration? *To correct the energy error introduced by numerical integration.* (4) Do large numbers of draws cure a misspecified prior or likelihood? *No.*

### Sources and further reading

- Stan Reference Manual, *MCMC Sampling*: https://mc-stan.org/docs/2_37/reference-manual/mcmc.html
- Stan, *How to Diagnose and Resolve Convergence Problems*: https://mc-stan.org/learn-stan/diagnostics-warnings.html
- Michael Betancourt, *A Conceptual Introduction to Hamiltonian Monte Carlo* (2017): https://arxiv.org/abs/1701.02434
- Related existing lecture: `probability-measure:009000` (stationarity, mixing and randomized computation).
