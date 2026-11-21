# A Distance Between Distributions: Wasserstein Metrics and Quantiles

<!-- BEGIN SPOKEN LECTURE -->

Two probability distributions can look similar in one sense and far apart in another. Put one unit of probability at position zero. Move it a thousandth of a unit to the right. The new distribution assigns probability one to a different point. If we use total variation distance, these two point masses are maximally separated: they put all their mass on disjoint singletons. Yet in the geometry of the real line they are extremely close.

Now move that point mass a hundred units away. Total variation still gives the same maximal separation. It cannot distinguish the tiny displacement from the enormous one. A geometry-aware distance should distinguish them. The Wasserstein distances do exactly that: they consider how expensive it would be to move one distribution into the other, given a metric on the underlying space.

The word distance now has a precise claim attached to it. It means nonnegativity, symmetry, separation of different distributions, and the triangle inequality. A minimum shipping cost for an arbitrary cost matrix need not satisfy these properties. We will see why a metric ground cost, raised to a suitable power and followed by an appropriate root, does.

## Different ways to price a movement

Let mu and nu be probability measures on a metric space, and let p be a real number at least one. Consider every coupling of mu and nu. For each coupling, measure the expected p-th power of the distance from its first coordinate to its second. Minimize that expectation and then take its p-th root. The result is the p-Wasserstein distance, commonly written W-p.

We restrict attention to measures with finite p-th moments, so these expressions are finite and behave well. For discrete distributions, the integral is just a weighted sum over a coupling matrix. For general measures, the definition uses an integral, and existence of minimizers requires the usual conditions on the space and cost. On standard complete separable metric spaces, the Wasserstein space of finite-p-moment probability measures supports the metric theory we want.

At p equal to one, there is no outside root. The objective is the mean travel distance of the best coupling. At p equal to two, long journeys are penalized quadratically inside the optimum, and we take a square root afterward. This is not a cosmetic convention: taking the root is necessary for the triangle inequality in the familiar form.

For a point mass at x and a point mass at y, there is only one coupling. It puts all mass on the pair x,y. Therefore W-p equals the ground distance between x and y for every p. In particular, W-p between the point masses at zero and a thousandth is a thousandth; between those at zero and a hundred it is a hundred. The geometry of points has been embedded into the geometry of probability distributions.

This extension is not free. A small Wasserstein distance tells us something about observations that vary smoothly with location, but need not imply that probabilities of individual sets are close. Our two nearby point masses already demonstrate that. The metric we choose changes the meaning of closeness.

## Calculate two Wasserstein distances

Return to two discrete distributions on a line. The source has half its mass at zero and half at two. The target has one quarter at one and three quarters at three. A coupling is determined by a number t between zero and a quarter, with table entries t, one half minus t, one quarter minus t, and one quarter plus t.

For the one-Wasserstein cost, the four distances are one, three, one, and one. The objective is two minus two t, so its minimum is one and a half at t equal to one quarter. Therefore W-one is one and a half.

For the two-Wasserstein problem, the four *squared* distances are one, nine, one, and one. The objective is five minus eight t. Its minimum is three, again at t equal to one quarter. But W-two is not three. It is the square root of three. The two answers are different because they penalize long journeys differently and because the definition of W-two includes a square root.

In this example the same plan optimizes both costs. That need not happen for arbitrary configurations in higher dimensions, where changing the cost exponent can change the optimal pairing. Even on a line, costs with strictly convex powers can select among plans differently when ties are present. What we can safely say here is that the explicit linear programs have the same minimizing endpoint.

A general inequality gives another consistency check. For any nonnegative random variable D on a probability space, its mean is at most the square root of its mean square. Hence for any coupling, expected distance is at most the square root of expected squared distance. Take a coupling minimizing the squared distance. The optimal mean distance is no larger than that coupling's mean distance. Thus W-one is at most W-two when both are finite. Our values, one and a half and the square root of three, respect this.

## Why the triangle inequality is a coupling theorem

Nonnegativity and symmetry are immediate from nonnegative symmetric ground distance. If two distributions are identical, couple every point with itself and pay zero. Conversely, if an optimal coupling has zero cost, it must be concentrated on pairs of equal points, so its marginals are the same. The interesting metric axiom is the triangle inequality.

Suppose we want to compare mu with rho, but we have already found a good coupling between mu and nu and another good coupling between nu and rho. Can we compose the two plans? Yes, provided we arrange for them to share the same intermediate random variable.

In a finite example, imagine an intermediate point y has mass b-y under nu. One coupling assigns some incoming mass from each x to y. The other assigns some outgoing mass from y to each z. Conditional on the shared y, choose the starting x and ending z independently with the conditional probabilities specified by the two couplings. The joint mass on the triple x,y,z is the first coupling's mass on x,y times the second coupling's mass on y,z, divided by b-y. If b-y is zero, there is no mass to distribute there and we omit that term.

This produces a joint distribution of X,Y,Z whose X,Y marginal is the first coupling and whose Y,Z marginal is the second. Forget Y and we obtain a coupling of X and Z. This construction is a finite form of the *gluing lemma*. In general probability spaces the same idea uses conditional distributions under appropriate hypotheses.

The ground metric says that the distance from X to Z is no more than the distance from X to Y plus the distance from Y to Z. For p equal to one, expectations immediately give the triangular bound. For p greater than one, apply Minkowski's inequality to the p-th roots of the expectations. The resulting X,Z coupling may not be optimal, but its cost is an upper bound on W-p from mu to rho. Taking couplings as close to optimal as needed proves that W-p of mu and rho is at most W-p of mu and nu plus W-p of nu and rho.

Notice how the proof works. We do not assume optimal transport itself composes cleanly, as though two separately optimal routes automatically create an optimal third route. We only construct a feasible composed coupling, and feasibility is enough for an upper bound. This is a common mathematical pattern: a construction need not be optimal to prove a triangle inequality.

## One-dimensional transport can be sorted

On the real line there is a beautiful simplification. Define the quantile function of a probability distribution as the position below which a given fraction of its mass has accumulated, using the usual generalized inverse convention. Draw a uniform random number U between zero and one. Then the source quantile at U has distribution mu, and the target quantile at the same U has distribution nu. So using the *same* U constructs a coupling that matches equal quantile levels.

For the cost absolute distance raised to any p at least one, this monotone quantile coupling is optimal on the real line. The intuitive exchange argument is that if two routes cross in their order, uncrossing them does not increase the sum of convex distance costs. Repeatedly removing crossed pairings produces an order-preserving solution. A full proof extends this argument to measures, but the finite exchange is the essential mechanism.

For our source, the first half of quantile levels produce zero and the second half produce two. For the target, the first quarter produce one and the remaining three quarters produce three. Divide the unit interval into three pieces: from zero to one quarter, the paired points are zero and one; from one quarter to one half, they are zero and three; from one half to one, they are two and three.

The one-Wasserstein cost is one quarter times one, plus one quarter times three, plus one half times one. That is one and a half. The squared cost is one quarter times one, plus one quarter times nine, plus one half times one. That is three. We have recovered both optima without invoking a general linear-programming algorithm.

This gives an exact formula in one dimension: W-p to the power p is the integral over quantile levels of the p-th power of the difference between source and target quantiles. For W-one there is another formula involving the area between cumulative distribution functions. These formulas are powerful because they turn a transport problem into sorting and one-dimensional integration. They do not extend in this simple form to arbitrary high-dimensional distributions, where there is no universal way to sort points along a single axis without losing geometry.

## What kind of convergence does transport see?

Imagine measures mu-n that put mass one minus one over n at zero and mass one over n at the point n. For every bounded continuous test function, the contribution of the escaping mass becomes negligible, so mu-n converges weakly to the point mass at zero. But its W-one distance from the point mass at zero is always one: the tiny mass must travel distance n, and the product of mass and distance stays one. Its W-two distance is the square root of n, which even grows.

This is not a defect. Wasserstein distances record geometry in the tails. On Euclidean space, convergence in W-p is equivalent to weak convergence together with convergence of the p-th moments, under the standard finite-moment conditions. Weak convergence alone permits small masses to escape far enough to spoil transport costs.

The example also shows why the p value changes the questions we can answer. W-two reacts much more strongly to rare distant outliers than W-one. When using these distances in statistics, optimization, or machine learning, the choice of ground metric and exponent is part of the modeling decision. There is no context-free rule that one exponent is universally better.

A Wasserstein distance is therefore a geometry of probability laws, not merely a new name for a shipping cost. It measures the least expensive joint realization of two distributions, respects the geometry of individual points, composes through glued couplings, and tracks the cost of distant mass. Its one-dimensional form can be calculated by sorting; its higher-dimensional form opens the door to combinatorial and continuous optimization.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a Polish metric space \((X,d)\) and \(p\ge1\), let \(\mathcal P_p(X)\) be probability measures with finite p-th moment relative to some (hence every) fixed reference point. Define
\[
W_p(\mu,\nu)=\left[\inf_{\pi\in\Pi(\mu,\nu)}\int_{X\times X}d(x,y)^p\,d\pi(x,y)\right]^{1/p}.
\]
For the running example with \(x=(0,2),y=(1,3)\): \(W_1=3/2\), \(W_2=\sqrt3\). The one-dimensional quantile formula is
\[
W_p(\mu,\nu)^p=\int_0^1|F_\mu^{-1}(t)-F_\nu^{-1}(t)|^p\,dt.
\]
One-dimensional monotone rearrangement is optimal for convex power costs \(|x-y|^p\), \(p\ge1\).

**Finite gluing.** Given \(\pi_{xy}\in\Pi(a,b)\), \(\sigma_{yz}\in\Pi(b,c)\), define \(\tau_{xyz}=\pi_{xy}\sigma_{yz}/b_y\) where \(b_y>0\) (zero otherwise). Its \((x,y)\) and \((y,z)\) marginals are \(\pi\) and \(\sigma\). Then Minkowski implies the triangle inequality after forgetting y.

**Exercises with solutions.** (1) Find \(W_p(\delta_0,\delta_7)\). *It is seven for every p at least one.* (2) Explain why small total variation is not necessary for small W-one. *Distinct point masses at positions \(0\) and \(\varepsilon\) have maximal total variation but W-one equal to \(\varepsilon\).* (3) For \(\mu_n=(1-1/n)\delta_0+(1/n)\delta_n\), find W-one and W-two from \(\delta_0\). *They are \(1\) and \(\sqrt n\), respectively, while \(\mu_n\) converges weakly to \(\delta_0\).*

### Reading

- Peyré and Cuturi, *Computational Optimal Transport* (2019), Wasserstein metrics and one-dimensional transport: https://research.google/pubs/computational-optimal-transport/
- Cédric Villani, *Optimal Transport: Old and New* (2009), Wasserstein metric and topology of measure spaces.
