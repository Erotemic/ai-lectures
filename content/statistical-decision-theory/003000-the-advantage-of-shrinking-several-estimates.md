# 003000 — The Advantage of Shrinking Several Estimates

**Track:** Statistical Decision Theory and Bayesian Computation. **Preparation:** normal distributions, mean squared error, vectors, introductory Bayesian inference. **Theme:** estimating related quantities jointly can reduce total error even when every observation is unbiased.

<!-- BEGIN SPOKEN LECTURE -->

# The Advantage of Shrinking Several Estimates

Imagine a small organization that reports the performance of six independent teams. Each team has a measured score, and each score comes with substantial sampling noise. The obvious report is to publish each observed score as the corresponding team's best estimate. If the measurements are unbiased, what reason could there be to move them toward one another? Isn't that distorting the evidence?

There can be a very good reason. The task is to estimate six unknown quantities from six noisy measurements. A rule can accept a little bias in some circumstances while reducing enough variance to improve its overall expected squared error. If the quantities themselves have shared structure, shrinking extreme observations toward a common center can be especially effective. And even without assuming that shared structure is literally true, a remarkable frequentist theorem shows a uniform improvement for a particular multivariate normal problem.

To understand both claims, we need to separate two arguments that are often blended together. The first is ordinary Bayesian partial pooling under an explicit model for related parameters. The second is the James–Stein phenomenon, a frequentist risk result that does not require treating the unknown parameter vector as a draw from the chosen prior. They reach similar-looking formulas through different guarantees.

## Shrinkage under a known prior

Start with one unknown number theta. We observe X equal to theta plus normally distributed noise with mean zero and variance one. The raw estimate X is unbiased and has mean squared error one for every fixed theta. Now suppose we also posit a prior distribution for theta: normal, centered at zero, with variance four.

The prior is intentionally broader than the observation noise. It says that theta can vary substantially across applications, but values near zero are more plausible before seeing the observation. The likelihood and prior are both normal, so the posterior is normal. Combining their precisions gives posterior precision one plus one quarter, or five quarters. The posterior variance is therefore four fifths. The posterior mean is four fifths of X.

Why four fifths? The observation has precision one, the prior has precision one quarter, and the weighted average of the observation and the prior center uses those precision weights. The result retains eighty percent of the observed signal and pulls the remaining twenty percent toward zero. Under squared-error loss this posterior mean is the optimal Bayes action.

If X equals three, the estimate becomes two point four. We have not proved that theta is smaller than three. We have calculated the estimate that minimizes expected squared error given the model and this observation. For a fixed theta of five, the shrinkage introduces a downward bias. For theta near zero, it can substantially reduce error. Averaging over the stated prior gives Bayes mean squared error four fifths, compared with one for the raw observation.

That comparison is an average over the prior. The shrinkage estimator does not dominate the raw estimator at every fixed theta. For a constant shrinkage factor a, the frequentist risk under unit-variance observation noise is a squared plus one minus a squared times theta squared. At a equal to four fifths, the risk is zero point six four plus zero point zero four theta squared. This is smaller than one for theta whose absolute value is less than three, and larger than one for theta outside that range. The same shrinkage rule can help or hurt depending on the true value.

The example warns us not to confuse a Bayes-optimal decision under one prior with a uniform frequentist improvement. The mathematical statements are both useful, but their quantifiers are different.

## Multiple measurements and partial pooling

Now return to the six teams. We can model each true score theta sub i as a deviation from a common population center mu. A simple hierarchical model says that, conditional on mu and a between-team variance tau squared, the team scores follow normal distributions centered at mu. Each observed score is then its team score plus measurement noise.

If mu and tau were known, and the measurement variance were sigma squared, the posterior mean of a team score would be a weighted average of its observation and the common center. The weight on the observation is tau squared divided by tau squared plus sigma squared. When true team scores are believed tightly concentrated, tau is small and shrinkage is strong. When genuine between-team variation is large compared with measurement noise, tau is large and the observed score receives nearly all the weight.

This gives partial pooling a concrete meaning. Complete pooling treats all teams as having the same underlying parameter. No pooling estimates each team separately. Partial pooling borrows information about the population center and variation while allowing team-specific values. The amount of borrowing is derived from the modeled signal-to-noise ratio.

But in practice we rarely know mu and tau. Estimating them from the same observations introduces another layer of uncertainty. If we replace them with point estimates and then act as if those values were known, our team-level intervals may be too narrow. Full hierarchical Bayesian inference integrates over uncertainty in the hyperparameters. Empirical Bayes methods plug in estimates and can work well, but need their own risk and uncertainty analysis.

Pooling can also be harmful if teams are not exchangeable in the way the model assumes. Suppose one team operates in a genuinely different environment. Shrinking its result toward a common average may hide a real difference. Introducing covariates, groups, time dependence, or a heavy-tailed population model may be more faithful than forcing every team toward the same center.

## A result that looks impossible

The stranger story starts when we stop assigning a prior to theta. Consider d unknown real numbers, assembled into a vector theta. Observe a noisy vector X whose components are independent normal observations with means theta sub i and known variance one. Under total squared-error loss, the obvious vector estimate is X itself. Its frequentist risk is d, for every theta. Every coordinate contributes expected squared error one.

In one or two dimensions, this estimator is admissible under the usual unrestricted normal-mean problem. Starting in dimension three, something changes. There is a different estimator whose expected total squared error is strictly smaller at every theta, including parameter vectors arbitrarily far from the origin.

For dimension d at least three, the James–Stein estimator multiplies X by one minus d minus two divided by the squared length of X. If X happens to be zero, we define the estimate to be zero; under the continuous normal model this event has probability zero. The factor depends on the observed length. When X is far from the origin, it is close to one and shrinkage is mild. When X is near the origin, shrinkage is much stronger and the untruncated factor can even become negative.

Let's take three observations, two, one, and two. Their squared length is nine. Since d minus two is one, the factor is eight ninths. The new estimate is sixteen ninths, eight ninths, and sixteen ninths. It moves all three coordinates toward zero. This is not a claim that zero is the most likely true vector. It is a construction designed to reduce total frequentist risk.

How can we prove it helps everywhere? The proof uses Stein's identity, an integration-by-parts formula for the normal distribution. If a vector estimator has the form X plus a differentiable adjustment g of X, the difference between its risk and the risk of X can be written as the expectation of the squared length of g plus twice the divergence of g. The divergence is the sum of the partial derivatives of the adjustment's coordinates with respect to the corresponding observations.

Choose g of X to be minus d minus two, times X, divided by the squared length of X. The squared length of g contributes the square of d minus two, divided by the squared length of X. The divergence contributes a negative term of precisely twice that size. The sum is negative the square of d minus two divided by the squared length of X. Taking expectation, the James–Stein risk is d minus the square of d minus two times the expected reciprocal squared length of X.

For dimension at least three, that reciprocal expectation is finite and positive under the stated normal model. Therefore the new risk is strictly less than d for every fixed theta. This is a genuine uniform dominance theorem. It does not rely on a prior average and does not assume theta is close to zero.

The proof also shows where the dimension restriction enters. In one or two dimensions, the corresponding reciprocal moment fails to have the needed finiteness, and the algebra does not deliver the same theorem. The James–Stein phenomenon is about estimating several components jointly under a specified total loss, not about changing the accuracy of one isolated measurement for free.

## What the theorem does not promise

There is an immediate temptation to announce that shrinkage is always better. That would be too broad. The result assumes independent normal measurement errors with a known common variance, unrestricted mean vectors, and total squared-error loss. Changing the loss to a worst-coordinate error, adding model constraints, using strongly correlated or heavy-tailed noise without the necessary modifications, or changing how many parameters are estimated can invalidate the displayed result.

Even within the theorem's setting, dominance is an expectation statement. On one realized dataset, the James–Stein estimate can be farther from theta than X. This is not a contradiction. A procedure can improve expected loss over repeated samples while being worse on some individual samples.

One might also worry that shrinkage toward zero depends on the arbitrary origin of the coordinate system. That concern is legitimate in applications. We can translate or transform the target if the loss and covariance structure justify it. There are generalized shrinkage estimators and hierarchical models that encode a scientifically meaningful center. But choosing a center after browsing the data introduces another selection step and should not silently inherit the original risk proof.

The positive-part James–Stein estimator addresses another practical feature. It truncates the shrinkage factor below at zero, avoiding sign reversal when X is very close to the origin. Under the standard normal-mean squared-error setting it dominates the ordinary James–Stein estimator. Its proof involves additional reasoning; we should not assume the smooth Stein identity applies unchanged at the truncation boundary.

## What have we learned about evidence?

The six-team problem now has three possible responses. Estimate every team independently, accepting high variance. Specify a hierarchical model and derive a posterior that borrows strength across teams. Or study a frequentist shrinkage rule whose risk can be proved to dominate the unpooled estimator under a particular multivariate normal model.

These choices do not have identical meanings. A hierarchical posterior answers a conditional-probability question under a generative model. The James–Stein dominance result compares long-run losses with theta held fixed. Both show that apparently separate estimates can benefit from being considered jointly, but neither gives permission to treat genuinely different populations as identical.

The surprise is not that bias can reduce variance. We already knew that. The surprise is that, in three or more dimensions under total squared error, a carefully chosen data-dependent shrinkage factor can beat the coordinatewise unbiased estimator at every possible true mean vector. Statistical decision theory gives that claim its exact form and its proof.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(X\mid\theta\sim N(\theta,\sigma^2)\), \(\theta\sim N(\mu,\tau^2)\),
\[
E[\theta\mid X]=\frac{\tau^2}{\tau^2+\sigma^2}X+\frac{\sigma^2}{\tau^2+\sigma^2}\mu,
\quad\operatorname{Var}(\theta\mid X)=\frac{\tau^2\sigma^2}{\tau^2+\sigma^2}.
\]
For \(\mu=0\), \(\tau^2=4\), \(\sigma^2=1\), posterior mean \(4X/5\), Bayes MSE \(4/5\). With fixed \(\theta\), risk of \(aX\) is \(a^2\sigma^2+(1-a)^2\theta^2\).

**James–Stein theorem (known spherical variance).** If \(X\sim N_d(\theta,\sigma^2 I_d)\), \(d\ge 3\), and loss \(\|\delta-\theta\|^2\), then
\[
\delta_{JS}(X)=\left(1-\frac{(d-2)\sigma^2}{\|X\|^2}\right)X,
\qquad R(\theta,\delta_{JS})=d\sigma^2-(d-2)^2\sigma^4\mathbb E_\theta\!\left[\frac1{\|X\|^2}\right]<d\sigma^2.
\]
Derivation: with \(\delta=X+g\), Stein's identity gives
\[
R(\theta,X+g)-d\sigma^2=E_\theta\left[\|g(X)\|^2+2\sigma^2\operatorname{div}g(X)\right].
\]
Set \(g(x)=-c x/\|x\|^2\), \(c=(d-2)\sigma^2\). Then \(\operatorname{div}g=-(d-2)c/\|x\|^2\), giving the displayed risk. Analytic justifications at the origin use truncation/limits; the reciprocal moment is finite for \(d>2\).

**Exercises and solutions.** (1) For \(\tau^2=1\), \(\sigma^2=4\), what is the posterior-mean weight on X? *One fifth.* (2) In the one-dimensional model with shrinkage factor \(4/5\), at what \(|\theta|\) does its risk equal one when \(\sigma^2=1\)? *Three.* (3) In dimension four with \(\sigma^2=1\) and \(\|X\|^2=8\), what is the James–Stein factor? *Three quarters.* (4) Does dominance guarantee lower squared error on the observed dataset? *No. The inequality concerns expected squared loss at each fixed theta.*

### Sources and further reading

- Berkeley STAT 210A, *The James–Stein Estimator*: https://stat210a.berkeley.edu/fall-2025/reader/jamesstein.html
- Charles Stein, *Inadmissibility of the usual estimator for the mean of a multivariate normal distribution* (1956).
- Efron and Morris, *Stein's Estimation Rule and Its Competitors—An Empirical Bayes Approach* (1973).
