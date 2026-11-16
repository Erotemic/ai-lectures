# 022000 - Mirror-Prox: Solving Monotone Games Without Rotating Forever

**Track:** Optimization and Duality. **Background:** convex analysis, saddle-point problems, monotone operators, and Bregman divergences. **Central question:** why does an extra gradient evaluation stabilize a method for monotone saddle-point problems?

<!-- BEGIN SPOKEN LECTURE -->

# A game where naive gradients spiral outward

Consider the simplest possible two-player zero-sum game. One player chooses x and tries to minimize the product of x and y. The other chooses y and tries to maximize the same product. The unique saddle point, when the variables are unrestricted, is at x and y both zero.

If we perform simultaneous gradient descent in x and gradient ascent in y, something strange happens. The update continually rotates the pair of variables around the origin. More precisely, with a constant positive step size, its distance from the origin grows instead of shrinks. The derivatives point in directions that are individually sensible for each player, yet the combined algorithm moves away from the equilibrium.

This failure has nothing to do with a nonconvex objective. The payoff is linear in each variable: convex for the minimizing player and concave for the maximizing player. The underlying operator is monotone. The difficulty is that monotonicity does not mean the operator points directly toward the solution. A skew-symmetric rotation is monotone, but it has no radial component.

Mirror-Prox remedies this by evaluating the operator once at a predicted point and then correcting the update using the new information. The correction is small, but its effect on rotational dynamics is decisive.

# Rewrite the game as an operator equation

For a convex-concave saddle function, form an operator by taking the gradient with respect to the minimizing variable and the negative gradient with respect to the maximizing variable. The saddle condition becomes a variational inequality over the feasible set.

The operator is monotone when the smooth saddle function is convex in the first variable and concave in the second. This means that the difference of operator values at two points has a nonnegative inner product with the difference of those points.

In our bilinear game, the operator takes the pair x,y to y,negative x. Geometrically it rotates vectors through a right angle. The inner product of the operator difference with the point difference is exactly zero, so monotonicity holds without any strong radial force.

The ordinary simultaneous gradient step subtracts this rotated vector. It therefore combines the identity transformation with a rotation. Its squared distance multiplier is one plus the square of the step size. That exceeds one for every nonzero step size. No fixed positive step size makes this unconstrained explicit method contract toward the saddle.

# Look ahead before committing

The extragradient idea first takes a provisional step from the current point, using the operator evaluated there. Instead of accepting that provisional point, it evaluates the operator again at the provisional point and makes the actual update from the original current point.

For the bilinear example we can calculate the effect exactly. The operator applied twice is negative the identity. Substituting the provisional point into the second evaluation therefore produces a corrected update: the original vector multiplied by one minus the square of the step size, together with a rotation term.

The squared distance multiplier is now one minus the step-size squared plus the step-size to the fourth. For step sizes strictly between zero and one this is less than one. The iterates contract toward the saddle instead of spiraling outward.

This example is a local algebraic illustration of why the second evaluation matters. It is not a general proof that every extragradient method converges linearly. The bilinear operator here is a particularly simple linear rotation; for general merely monotone operators, the usual guarantee is on an averaged variational-inequality gap.

# Projection keeps constraints in view

Real saddle-point problems often have constraints. Strategies may lie in probability simplexes. Matrix variables may be required to remain positive semidefinite. A simple Euclidean extragradient method handles convex constraints by projecting the predicted point back into the feasible set and projecting the corrected point as well.

Now the intermediate point is computed from the original current iterate and its operator value. The final point is also based on the original current iterate, but it uses the operator at the intermediate point. This distinction is important: taking two ordinary gradient steps in succession is not the same algorithm.

Projection is natural for Euclidean geometry, but it can be expensive or poorly matched to the shape of the feasible set. On a probability simplex, Euclidean projection is sometimes less natural than a multiplicative, entropy-based update. This leads us from extragradient to Mirror-Prox.

# Bregman divergences adapt the geometry

Choose a strongly convex distance-generating function. Its Bregman divergence measures the error made when approximating that function by its tangent plane at the current point. Unlike squared Euclidean distance, a Bregman divergence need not be symmetric and need not satisfy the triangle inequality. Yet strong convexity makes it useful for analyzing proximal updates.

Define a prox step by minimizing the inner product with a candidate operator vector plus the Bregman divergence from the current point. The first Mirror-Prox stage uses the operator at the current point. The second uses the operator at the predicted point, but both prox problems are centered at the original point.

With the quadratic distance-generating function, this reduces to Euclidean extragradient. With negative entropy on a simplex, the update takes a multiplicative form involving exponentials and normalization. That geometry is especially natural when the variables are probability distributions and the feasible set has many coordinates.

The technique is called mirror because the gradient of the distance-generating function provides a different coordinate system. We move in that dual geometry and map back to the feasible set through the prox problem.

# What monotonicity and smoothness buy us

Suppose the feasible set is compact and convex, the operator is monotone and Lipschitz continuous, and the distance-generating function is strongly convex relative to the chosen norm. With a suitable fixed step size based on the Lipschitz constant, Mirror-Prox yields a variational-inequality gap that decays on the order of one over the number of iterations for an average of its predicted points.

This is an ergodic guarantee. It says that a carefully chosen average has a small residual in the variational-inequality sense. It does not automatically say each individual iterate converges at that rate, or that the variables approach one unique solution in ordinary Euclidean distance. Those stronger claims need additional assumptions such as strong monotonicity or special problem structure.

The distinction matters in game solving. Multiple equilibria may exist. A small primal-dual gap certifies near-optimal play even if the actual strategy vector moves among near-equivalent equilibria.

# Where the O one-over-T rate comes from

The proof compares each prox update with an arbitrary test point in the feasible set. Strong convexity of the Bregman generator provides a positive distance term. Lipschitz continuity controls the error caused by evaluating the operator at the intermediate point rather than at the original point.

After a suitable step-size choice, the one-step inequality is a difference of Bregman divergences plus a controlled nonpositive remainder. Sum over iterations. The divergences telescope, leaving an initial diameter-like term divided by the number of iterations.

Monotonicity then converts the accumulated operator comparisons into the variational-inequality gap of the averaged point. The result is an order-one-over-T estimate. The rate is not obtained from contracting the distance to a solution at every step. It is obtained from a telescoping inequality and a gap definition appropriate to monotone problems.

# A probability simplex example

Suppose a zero-sum matrix game has many pure actions. Each player chooses a probability vector over those actions. The saddle payoff is bilinear, and the associated operator is monotone and Lipschitz with respect to suitable norms.

Using negative entropy as the distance-generating function, a Mirror-Prox update reweights actions multiplicatively. Actions with relatively favorable gradient coordinates are emphasized, and the weights are normalized to sum to one. Because the update works in a geometry adapted to probabilities, it can avoid some of the inefficiency of repeatedly projecting dense vectors in Euclidean space.

But this convenience also has hypotheses. Entropic Bregman divergences are finite only on the appropriate relative interior or with suitable boundary conventions. Numerical implementations must handle exponentials and very small probabilities carefully. The theoretical O one-over-T guarantee presumes accurately solved prox steps or explicitly controlled prox error.

# Why the extra evaluation is worth it

Mirror-Prox embodies a broader lesson of optimization. In a minimization problem, a gradient often points downhill. In a saddle problem, the joint operator can rotate, and an algorithm that blindly follows it may fail even when the problem is convex-concave.

The predictive evaluation detects some of that rotation and compensates for it. Bregman geometry then adapts the correction to the feasible set. The resulting method handles an important class of monotone variational inequalities with a sharp first-order ergodic rate, rather than relying on a mistaken assumption that simultaneous descent and ascent behave like ordinary optimization.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Is `F(z)=Jz` strongly monotone for the skew rotation J? **Answer:** no; its monotonicity inner product is zero for every pair of points.
2. For gamma=1/2, what is the squared-distance multiplier of extragradient in the bilinear example? **Answer:** `1-1/4+1/16=13/16`.
3. Which point centers the second Mirror-Prox step? **Answer:** the original iterate z_t, not the predictor w_t.
4. Does an ergodic gap rate establish that every last iterate contracts geometrically? **Answer:** no; stronger conditions are needed for a last-iterate or linear rate.

### Reading and source notes

- [Arkadi Nemirovski, Prox-Method with Rate O(1/t) for Lipschitz Monotone Variational Inequalities](https://www2.isye.gatech.edu/~nemirovs/SIOPT_MP_2004.pdf), the original Mirror-Prox method and proof.
- [European Mathematical Society, Survey of Monotone Stochastic Variational Inequalities](https://euromathsoc.org/magazine/articles/112), extragradient and Mirror-Prox formulations.
- [Bauschke and Combettes, Convex Analysis and Monotone Operator Theory in Hilbert Spaces](https://link.springer.com/book/10.1007/978-3-319-48311-5), proximal geometry and monotone operators.
