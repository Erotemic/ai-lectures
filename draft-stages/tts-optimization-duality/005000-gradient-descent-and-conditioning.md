# 005000 — Gradient Descent, Smoothness, and the Price of Poor Conditioning

**Track:** Optimization, Convexity, and Duality. **Background:** derivatives, vectors, convexity, and objective functions. **Question:** when does following the negative gradient actually make certified progress?

<!-- BEGIN SPOKEN LECTURE -->

# Gradient Descent, Smoothness, and the Price of Poor Conditioning

Suppose an optimization problem has a smooth objective and millions of variables. We may not be able to solve the first-order stationarity equations in closed form, nor can we inspect every feasible candidate. A simple algorithm suggests itself: evaluate the gradient at our current point and move a little in the opposite direction.

That is gradient descent. But “move downhill” is not yet a convergence theorem. How far should we move? Can a step go too far? What mathematical quantity does the algorithm improve? And when does a stationary point certify that we have found a global solution rather than a local trap?

The answers involve smoothness, convexity, conditioning, and a proof that turns each descent step into a quantitative inequality.

## Why the gradient points uphill

For a differentiable function of several real variables, the gradient collects its partial derivatives. For a small displacement d, the first-order change is approximately the dot product of the gradient and d. Among unit vectors, the negative gradient direction gives the most negative first-order change in the ordinary Euclidean geometry, provided the gradient is not zero.

This is a local statement. It does not say that a very long move in that direction will decrease the objective. A curved surface can bend upward again after a short descent. Gradient descent therefore introduces a step size, often called a learning rate, and updates the current point by subtracting the step size times the current gradient.

At a stationary point the gradient is zero, so the algorithm stays put. If the objective is convex and differentiable on the entire space, a point with zero gradient is a global minimizer. If the objective is nonconvex, a stationary point may be a saddle or a local maximum. The algorithm itself does not erase that distinction.

## Smoothness controls how far the surface can bend

We need a bound on how rapidly the gradient can change. Say the gradient is L-Lipschitz if the difference between gradients at any two points has norm at most L times the distance between those points. The constant L quantifies the largest permitted change in local slope per unit displacement.

From that hypothesis we can derive the descent lemma. Along a straight path from x to x plus d, integrate the directional derivative. Subtract the linear prediction at x. The error involves the difference between gradients along the path and the gradient at x. The Lipschitz bound says this difference is at most L times the fraction of the traveled distance. Integrating that fraction from zero to one produces one half. The result is a bound on the next objective value by the current objective, plus the gradient dotted with the displacement, plus one half L times the squared displacement length.

Now choose the displacement to be the negative gradient divided by L, assuming L is positive. Substituting this choice into the descent lemma leaves the current objective minus one over two L times the squared gradient norm. In words: each step reduces the objective by at least the squared gradient magnitude divided by twice L.

This is a genuine progress certificate. If the gradient is large, the guaranteed decrease is large relative to L. If the gradient is small, the guaranteed decrease is small; we may be near a solution, or we may be in a flat region, and additional structure is needed to decide which.

The step one over L is a conservative choice supported by the global smoothness bound. Better local step sizes may be possible through line search or curvature information. We should not confuse a safe simple theorem with a claim that this is always the fastest choice.

## A quadratic valley

Consider an objective equal to one half times the sum of one hundred times x squared and y squared. Its level sets are very elongated ellipses. Along the x direction the curvature is one hundred; along the y direction it is one. The gradient has components one hundred x and y. The global Lipschitz constant for this gradient in Euclidean norm is one hundred.

Start from any point and use step size one over one hundred. The next x coordinate is x minus x, so it becomes zero in one step. The y coordinate becomes y minus one hundredth of y, or ninety-nine hundredths of its previous value. The high-curvature direction is corrected quickly, while the low-curvature direction decays slowly.

The ratio of largest curvature to smallest positive curvature is one hundred. It is the condition number for the positive-definite quadratic Hessian. Poor conditioning means one universal step size must be small enough for the steepest direction, even though that makes progress sluggish in a flatter direction.

If we increased the step size beyond two over one hundred for this quadratic, the x update factor would have magnitude greater than one, so any nonzero x component would grow in magnitude rather than converge. The “downhill direction” did not prevent divergence because the step overshot the valley. On the other hand, rescaling coordinates so both curvatures are comparable can dramatically improve behavior. This motivates preconditioning and methods that adapt to local geometry.

## Convexity turns progress into a rate

A descent inequality only tells us the objective falls. To relate the objective value to the global optimum, suppose the objective is convex, has an L-Lipschitz gradient, and attains a minimum at a point x star.

Convexity gives a lower bound on the objective at x star using the tangent plane at the current point. Combining that lower bound with the descent lemma and the gradient step, we obtain another inequality: the new objective minus the optimal value is no more than one half L times the decrease in squared distance to x star caused by the update.

The significance is that these distance terms telescope. Add the inequality for the first N steps. Every intermediate squared-distance term cancels with its opposite from the neighboring step. What remains is at most one half L times the initial squared distance to a minimizer.

The objective values decrease at every step. Therefore the gap at the final step is no larger than the average gap across all previous steps. Combining these observations yields a bound of L times the initial squared distance to a minimizer, divided by twice the number of completed steps. In other words, ordinary gradient descent has an objective-value convergence guarantee on the order of one divided by the iteration count for this smooth convex setting.

This is a worst-case guarantee, not a prediction that every problem converges at exactly that speed. Many easy quadratics converge faster. Strong convexity gives stronger rates: if the Hessian is bounded below by a positive curvature parameter in a smooth quadratic, the error shrinks geometrically at a rate controlled by the ratio of that lower curvature to L. The conditioning of the problem now appears as a rate parameter, not just as a numerical annoyance.

## What remains true without convexity

If the function is smooth, bounded below, and its gradient is L-Lipschitz, the descent lemma still holds, even when the function is nonconvex. Add its guaranteed decreases over N steps. Because the objective cannot fall below its lower bound, the sum of squared gradient norms is bounded. It follows that at least one of the first N gradients must have squared norm on the order of one divided by N or smaller.

That gives a stationarity guarantee: some iterate has a small gradient. It does not provide a global optimality guarantee. A small gradient may occur near a saddle or a nonglobal local minimum. Even an exactly zero gradient is only a first-order condition in the nonconvex setting.

This distinction also matters for solver output. An optimizer that reports successful convergence because the gradient norm is below a tolerance has reported an approximate first-order stationary point. If the problem is known to be convex, the report is more meaningful, but a quantitative objective gap still requires an error bound, conditioning information, or a primal-dual certificate.

## Constraints change the step

So far we allowed x to range over all of Euclidean space. For a constrained convex set, moving along the negative gradient may leave the feasible region. A simple adjustment is projected gradient descent: take the ordinary gradient step and then project the result back onto the feasible set in Euclidean distance.

For closed convex sets, projection is well-defined and unique. Yet the analysis no longer uses just the unconstrained gradient equation. A constrained optimum may have a nonzero gradient balanced by the geometry of the boundary, as we saw with KKT multipliers. The appropriate stopping signal is a projected-gradient condition or another certificate of constrained optimality.

If the objective contains a nonsmooth convex penalty, an ordinary gradient may not even exist at the most important points. Subgradients and proximal operators provide the next generalization. Those methods preserve the spirit of a simple update while changing the mathematical object that certifies progress.

## Algorithm, theorem, and measurement

Gradient descent is appealing because its update is short. The work lies in proving what that update means. The negative gradient gives local decrease to first order. Lipschitz smoothness makes a controlled finite step possible. Convexity connects the descent to a global optimum. Strong convexity and conditioning explain faster or slower convergence. Without convexity we usually obtain stationarity, not global correctness.

A reliable optimization algorithm is not simply a repeated instruction to move downhill. It is a method whose assumptions justify its step sizes, whose convergence theorem matches the property we need, and whose stopping rule supports the claim we make about the answer.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Suppose \(\nabla f\) is \(L\)-Lipschitz in Euclidean norm with \(L>0\). The descent lemma is
\[
f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\frac L2\|y-x\|^2.
\]
For \(x_{k+1}=x_k-\nabla f(x_k)/L\),
\[
f(x_{k+1})\le f(x_k)-\frac1{2L}\|\nabla f(x_k)\|^2.
\]
If \(f\) is convex and a minimizer \(x_*\) exists, a standard descent-and-convexity argument yields
\[
f(x_{k+1})-f(x_*)\le\frac L2
\bigl(\|x_k-x_*\|^2-\|x_{k+1}-x_*\|^2\bigr),
\]
so by monotonicity and telescoping,
\[
f(x_N)-f(x_*)\le\frac{L\|x_0-x_*\|^2}{2N}
\quad (N\ge1).
\]
For a nonconvex \(L\)-smooth \(f\) bounded below by \(f_{\inf}\),
\[
\min_{0\le k<N}\|\nabla f(x_k)\|^2
\le\frac{2L(f(x_0)-f_{\inf})}{N}.
\]
These are exact-arithmetic mathematical guarantees; finite-precision implementations require separate consideration.

**Quadratic:** \(f(x,y)=\tfrac12(100x^2+y^2)\), \(L=100\), step \(1/L\) gives \(x_{k+1}=0\), \(y_{k+1}=0.99y_k\). For a positive-definite quadratic, the Hessian condition number is the largest eigenvalue divided by the smallest.

### Exercises with answers

1. For \(f(x)=x^2/2\) and step size one, what happens after one iteration? **Answer:** \(x_1=x_0-x_0=0\), the minimizer.
2. Why is a small gradient not a global certificate for a nonconvex function? **Answer:** Saddles and nonglobal minima can have zero gradient.
3. What happens to the x-coordinate in the quadratic example with step size \(0.03\)? **Answer:** It is multiplied by \(1-100(0.03)=-2\), so its magnitude doubles each step unless initially zero.
4. Where does convexity enter the \(O(1/N)\) objective bound? **Answer:** It bounds the difference between the current objective and the optimum using the tangent plane at the current point.

### Reading

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, chapters 9–10, first-order methods and descent analysis; Stanford EE364A Convex Optimization I lecture materials.
