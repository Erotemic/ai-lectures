# 019000 — Wasserstein Distributionally Robust Optimization: Decisions under Uncertain Laws

**Track:** Optimization and Duality. **Background:** convex duality, probability distributions, optimal transport, and robust optimization. **Central question:** how can an optimization decision remain defensible when the empirical distribution is only an approximation to the unknown population distribution?

<!-- BEGIN SPOKEN LECTURE -->

# What is uncertain: a number or a law?

Suppose a manufacturer must decide how much inventory to hold. Demand is random, and we have observed demand on several past days. We could estimate a probability distribution from those observations and minimize the expected cost under that one fitted distribution.

But the fitted distribution is itself uncertain. A small sample may misrepresent the true frequency of rare events or place too much mass on a few observed values. A different probability law, still reasonably close to the empirical data, could give a different expected cost.

Distributionally robust optimization treats the probability law as the uncertain object. Rather than guard against one unfavorable demand value, we guard against a family of plausible probability distributions. We choose a decision whose worst expected cost over that family is as small as possible.

The subtle part is deciding what it means for two distributions to be close. Wasserstein distance offers one answer by measuring how much work it takes to transport probability mass from one location to another.

# The transport picture

Imagine two piles of sand laid out along a number line. Each pile represents a probability distribution, with total mass one. To turn the first into the second, we move some mass left and some right. Each movement costs the amount of mass moved times the distance traveled.

The Wasserstein-one distance is the least possible total transport cost. In higher dimensions, the cost depends on a specified metric or norm on the space of uncertain outcomes. A larger distance means the distributions are harder to transform into one another under that metric.

This is different from total variation distance, which counts how much probability mass must change membership between sets but does not record how far the mass moved. Moving a small amount of mass a huge distance can have low total variation but appreciable transport cost, depending on the product of mass and distance.

# Build an ambiguity set around data

Take observed outcomes and put equal probability at each one. This is the empirical distribution. Choose a radius rho in Wasserstein distance. The ambiguity set contains all probability laws whose distance from the empirical law is at most rho.

For any decision, compute the expected loss under each law in the ambiguity set, then select the largest. This worst expected loss is the distributionally robust risk of the decision. Finally choose the decision minimizing that risk, perhaps together with a deterministic regularization or operating cost.

If rho is zero, the ambiguity set contains just the empirical law, assuming our distance is a proper metric on the selected class of probability measures. We recover empirical risk minimization. As rho grows, the family of laws grows, and the worst-case risk for a fixed decision cannot decrease.

There is no universally correct radius. It may be chosen using statistical concentration results, domain knowledge, sensitivity analysis, or a specific decision objective. The resulting robustness guarantee is conditional on the assumed ambiguity set containing the law we care about.

# An exact one-dimensional calculation

Consider two observed values, negative one and positive two. Their empirical mean is one half. Suppose our loss at outcome z is two times z. The empirical expected loss is therefore one.

Now allow Wasserstein-one distance at most one quarter, using ordinary absolute distance as the transport cost. The loss is Lipschitz with constant two: moving z by an amount h changes the loss by at most two times the absolute value of h.

The transport inequality tells us that the expected loss under any distribution within radius one quarter is at most the empirical expectation plus two times one quarter. That is one and a half.

Is the upper bound attainable? Yes, because our uncertain outcome is allowed to range over the entire real line. Shift each empirical observation to the right by one quarter. The transport cost is one quarter, and the new expected loss is one and a half. So the worst expected loss is exactly one and a half in this example.

The calculation is a useful model. Wasserstein robustness turns the slope of a loss function with respect to uncertain data into an explicit cost of distributional ambiguity.

# The dual view

The worst-case expectation is an optimization over all probability distributions in a ball. That appears infinite-dimensional. Under suitable regularity assumptions, transport duality transforms it into a problem involving a nonnegative transport-price parameter and a worst-case pointwise expression around each observed datum.

For a globally Lipschitz loss on an unrestricted metric space, this dual expression yields a simple upper bound: empirical expected loss plus Lipschitz constant times rho. For an affine loss on the real line, the upper bound is exact under the conditions of our example.

This dual form makes many distributionally robust optimization problems computationally tractable. Depending on the loss, domain, and cost function, the reformulation may be a convex program or sometimes a linear program. It is not true that every Wasserstein robust problem has a small convex reformulation without assumptions.

# A counterexample: quadratic losses with the wrong metric

Suppose the empirical distribution places all its mass at zero, and we use squared loss z squared. Choose a tiny probability mass epsilon and move it to a very distant point R, leaving the rest at zero.

The transport cost in Wasserstein-one distance is epsilon times R. We can keep that cost fixed at rho by choosing epsilon equal to rho divided by R. But the expected squared loss is epsilon times R squared, which equals rho times R. That tends to infinity as R grows.

So if the uncertain outcome is unbounded, a Wasserstein-one ambiguity ball around a point mass gives an infinite worst-case quadratic expectation. A finite radius does not automatically make every loss well behaved.

Possible remedies include a bounded support set, a transport cost that penalizes distant mass more strongly, or a class of losses with appropriate growth. The correct choice depends on the actual uncertainty model. This example demonstrates why specifying the transport metric and the loss growth is essential, not a technical footnote.

# Robustness is a modeling claim

A distributionally robust optimum answers a conditional question: among all distributions in the chosen ambiguity set, how bad can the expected loss be, and which decision minimizes that worst case?

It does not certify that the empirical data were sampled without bias, that the chosen distance matches the physical meaning of uncertainty, or that the true distribution lies inside the chosen ball. Those are separate statistical and modeling questions.

The mathematical benefit is clarity. The data define an empirical center, transport distance defines plausible deviations, duality makes the worst-case expectation analyzable, and optimization selects the decision. When those pieces are chosen explicitly, distributional uncertainty becomes a problem we can reason about rather than an invisible assumption inside an estimated expectation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. For affine loss `ell(a,z)=a z` over R, empirical mean 3, a=-2, rho=0.4, find worst-case expectation. **Answer:** `-6+0.8=-5.2`.
2. Why can the W1 robust quadratic loss diverge on unbounded support? **Answer:** small mass moved distance R costs order mass times R, while squared loss gains order mass times R squared.
3. What happens to fixed-decision worst-case risk when rho increases? **Answer:** it cannot decrease, since the ambiguity set expands.
4. Does minimizing worst-case loss prove that the true distribution lies in the selected ball? **Answer:** no; containment is a separate statistical assumption or guarantee.

### Reading and source notes

- [Mohajerin Esfahani and Kuhn, Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric](https://doi.org/10.1007/s10107-017-1172-1), Wasserstein ambiguity sets and convex reformulations.
- [EPFL open-access research record of Esfahani–Kuhn](https://infoscience.epfl.ch/entities/publication/a785a796-96d5-4510-84e1-8ab1b7f903b2), bibliographic record and author manuscript.
- [Kantorovich–Rubinstein duality, Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Kantorovich-Rubinstein_theorem), transport distance and Lipschitz test functions.
