# Stochastic Differential Equations: Drift, Noise, and the Ito Correction

**Track:** Probability, Measure, and Statistical Reasoning  
**Lecture:** 034000  
**Preparation:** Brownian motion, derivatives through second order, and ordinary differential equations.  
**Companion:** Ito's formula, geometric Brownian motion, Euler-Maruyama, forward equations.

<!-- BEGIN SPOKEN LECTURE -->

An ordinary differential equation can describe a population that grows at a rate proportional to its current size, or a particle whose velocity depends on position. But many evolving systems are buffeted by disturbances that cannot be represented by a smooth force known in advance. We may know the average tendency and the size of random fluctuations without knowing the precise future disturbances. How do we write an evolution law that includes both?

The ordinary answer is to specify a drift and a noise intensity. A stochastic differential equation says, informally, that a small change in the evolving quantity X has a predictable part proportional to elapsed time, plus a random part proportional to a Brownian increment. We write this compactly as d X equals b of X and time times d t, plus sigma of X and time times d B. The coefficient b is the drift. The coefficient sigma controls the amplitude of noise. B is Brownian motion.

That notation is useful, but it is not an ordinary differential equation with an extra wildly fluctuating smooth input. Brownian paths have no classical derivative. The differential symbol d B cannot be interpreted as a finite random velocity multiplied by d t. Instead, an Ito stochastic differential equation means an integral equation. X at time t equals its initial value, plus the ordinary time integral of the drift, plus a stochastic integral of sigma against Brownian motion.

How can an integral with respect to a nowhere differentiable path make sense? The Ito construction begins with adapted step processes: at each interval, evaluate the integrand using information available at the interval's beginning, multiply by the Brownian increment, and sum. With suitable square-integrability conditions, these sums converge in mean square to a well-defined stochastic integral. The evaluation at the left endpoint is important. It means the coefficient is not allowed to use future Brownian information when deciding how to weight an increment.

There is an elementary identity behind why this construction behaves differently from ordinary calculus. Brownian increments over a short time delta t have variance delta t, so their typical magnitude is the square root of delta t. Their squares have expected size delta t. When we sum squared increments over many small intervals, the total does not vanish. It approaches elapsed time. By contrast, products of a smooth bounded velocity increment with itself would be of order delta t squared, which disappears after summing over a fixed interval.

This changes the chain rule. Suppose X follows a stochastic differential equation and we want to understand a smooth function f of X and time. Taylor expansion has a first derivative times the small change, plus one half the second derivative times the square of the change. In ordinary calculus the squared term vanishes at first order in time. Under Brownian forcing, the squared noise term contributes sigma squared times d t. The result is Ito's formula: the drift of f includes its ordinary time derivative, plus its first spatial derivative times b, plus one half its second spatial derivative times sigma squared. Its random term is the first spatial derivative times sigma times d B.

Let's see that correction in a problem where getting it wrong changes the answer. Suppose a positive quantity X is modeled by proportional drift and proportional noise: d X equals mu X d t plus sigma X d B, where mu and sigma are constants and the initial X is positive. This is geometric Brownian motion, a simplified model used in some descriptions of multiplicative random growth. If you naively write that the logarithm of X has drift mu, you miss the Ito correction.

Apply Ito's formula to the natural logarithm of X. Its first derivative is one over X, and its second derivative is negative one over X squared. The drift becomes mu minus one half sigma squared. The noise term becomes sigma d B. Integrate: log X at time t is log X at zero, plus mu minus half sigma squared times t, plus sigma times Brownian motion at time t. Exponentiating gives a positive process with an explicit formula.

The expected value of X at time t is the initial value times the exponential of mu t. The typical multiplicative growth of a single trajectory, reflected in the median, is instead governed by mu minus one half sigma squared. These statements are consistent. Random multiplicative growth can have an expectation pulled upward by occasional large outcomes even when the median path grows more slowly. Replacing expected growth by typical growth would silently change the question.

The distinction is valuable well beyond finance, where geometric Brownian motion is often introduced. Population models, reaction rates, and measurement processes may have noise whose magnitude depends on the current state. But the particular form sigma X can fail physically if the system has absorbing boundaries, resource limits, or jumps. A stochastic differential equation is a model to be checked, not a consequence of adding a Brownian term to every ordinary differential equation.

There is another way to interpret the same process. Instead of following one random trajectory, ask how the probability density of X changes over time. Under appropriate smoothness and boundary assumptions, the density satisfies a deterministic partial differential equation called the Fokker-Planck, or forward Kolmogorov, equation. The drift contributes a transport term involving minus the spatial derivative of b times the density. The noise contributes half the second spatial derivative of sigma squared times the density. If the drift is zero and sigma is a constant equal to the square root of twice D, this reduces exactly to the heat equation with diffusion coefficient D.

This completes a bridge from random walks to differential equations. At the microscopic level we followed a random particle. At the process level we obtained Brownian motion and stochastic differential equations. At the distribution level we recovered a deterministic diffusion equation. The same sigma affects all three descriptions, but a sample path, a probability law, and a density are different objects.

What if an exact solution is unavailable? One simple numerical approximation is Euler-Maruyama. Choose a time step. Update the current state by adding drift times the step and diffusion intensity times an independent normal random increment with variance equal to the time step. Repeat. This resembles the forward Euler method for an ordinary differential equation, but the noise increments scale with the square root of the time step, not the time step itself.

There are two kinds of numerical accuracy to distinguish. Strong error asks whether a simulated path stays close to the true path under a suitable coupling using the same Brownian driving noise. Weak error asks whether expectations of test functions of the simulated state are close to the true expectations. Under standard global Lipschitz and growth assumptions, Euler-Maruyama often has strong order one half; with additional smoothness, weak order one is typical for sufficiently regular test functions. Those orders are not universal guarantees for every coefficient, every boundary, or every observable. Discontinuous coefficients, superlinear growth, rare events, and absorbing boundaries can require different analysis or schemes.

Simulation can also confuse statistical and numerical uncertainty. A thousand Monte Carlo paths of a coarse time-stepping scheme may estimate the mean of that approximate numerical model precisely while the model itself remains biased relative to the intended stochastic differential equation. Increasing sample count reduces sampling error but does not necessarily fix discretization error. Refining the time step reduces some discretization errors but increases computational work. The two error sources should be evaluated separately.

We should not imply that every coefficient choice defines a well-behaved process. Existence and uniqueness theorems commonly assume, for example, coefficients that are Lipschitz in the state and satisfy appropriate growth conditions. More general theories exist, but the hypotheses matter. A stochastic model may have boundary behavior, blow-up possibilities, or multiple interpretations. The Ito and Stratonovich conventions also differ for state-dependent noise: converting between them adds a drift correction. One should never switch conventions while retaining the same displayed drift coefficient without checking the relation.

There is a larger conceptual point. Randomness in a dynamical law is not simply uncertainty about a deterministic initial condition. A random initial condition with deterministic evolution produces a distribution of trajectories, but once the initial state is fixed there is no new forcing. A stochastic differential equation receives fresh random increments over time. It encodes how information about the future arrives as the process unfolds.

We have now earned the meaning of the compact formula d X equals b d t plus sigma d B. It describes an integral equation driven by Brownian increments. The square of those increments survives in the limit, producing the Ito correction. A distribution of trajectories evolves through a deterministic forward equation, and numerical paths require explicit error reasoning. What initially looked like an ordinary differential equation plus a noise term is a different kind of calculus, constructed to respect the geometry of random variation through time.

<!-- END SPOKEN LECTURE -->

## Mathematical companion

For the Ito SDE \(dX_t=b(t,X_t)dt+\sigma(t,X_t)dB_t\), the integral interpretation is
\[
X_t=X_0+\int_0^t b(s,X_s)\,ds+\int_0^t\sigma(s,X_s)\,dB_s.
\]
For \(f\in C^{1,2}\), Ito's formula is
\[
df(t,X_t)=\left(f_t+bf_x+\frac12\sigma^2 f_{xx}\right)dt+\sigma f_x\,dB_t.
\]
For \(dX_t=\mu X_tdt+\sigma X_tdB_t\) and \(X_0>0\):
\[
X_t=X_0e^{(\mu-\sigma^2/2)t+\sigma B_t},\quad E[X_t]=X_0e^{\mu t},\quad\operatorname{median}(X_t)=X_0e^{(\mu-\sigma^2/2)t}.
\]
Under sufficient regularity the density solves \(\partial_t p=-\partial_x(bp)+\tfrac12\partial_{xx}(\sigma^2p)\), with appropriate initial and boundary conditions.

**Euler-Maruyama.** For \(\Delta B_n\sim N(0,h)\) independent across steps, set \(X_{n+1}=X_n+b(t_n,X_n)h+\sigma(t_n,X_n)\Delta B_n\). The standard strong \(L^2\) rate for globally Lipschitz coefficients is order \(h^{1/2}\), with the usual integrability assumptions. Strong and weak rates measure different errors.

### Exercises and answers

1. **Log transform.** For geometric Brownian motion, what is the drift of log X? **Answer:** Mu minus one half sigma squared, not mu.
2. **Noise scale.** At step size one hundredth, what is the standard deviation of a standard Brownian increment? **Answer:** One tenth.
3. **Density versus path.** Can a smooth density evolve by a heat equation while individual sample paths are nowhere differentiable? **Answer:** Yes; the smoothness statements concern different objects.
4. **Error.** Do more Monte Carlo trajectories remove time-discretization bias? **Answer:** Not necessarily; sample count and step-size errors require separate analysis.

### Reading and attribution

- MIT OpenCourseWare, *Theory of Probability* (18.175), for Brownian and martingale foundations: https://ocw.mit.edu/courses/18-175-theory-of-probability-spring-2014/pages/lecture-slides/.
- Bernt Oksendal, *Stochastic Differential Equations: An Introduction with Applications*, Springer, for Ito calculus and SDE theory.
- The logarithmic derivation and the distinction between weak and strong simulation error are original teaching explanations of standard results.
