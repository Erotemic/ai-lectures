# 010000 — Interior-Point Methods: Central Paths, Barriers, and Newton Systems

**Track:** Optimization, Convexity, and Duality. **Background:** convexity, linear-programming duality, Newton's method, KKT conditions. **Central question:** how can a constrained optimizer approach the boundary of a feasible region while staying strictly inside it?

<!-- BEGIN SPOKEN LECTURE -->

# Interior-Point Methods: Central Paths, Barriers, and Newton Systems

Imagine optimizing a linear objective over a polygon. If you could only walk along the edges, you might travel from corner to corner until reaching the best one. But there is another strategy: move through the interior, guided by a function that becomes increasingly costly as you approach the boundary. Gradually reduce that artificial boundary penalty, and the path of minimizers approaches an optimum of the original constrained problem.

This is the central idea behind barrier and interior-point methods. Their importance is not that they always produce fewer arithmetic operations than every alternative algorithm. It is that they turn constraints into a sequence of smooth problems, provide a powerful primal-dual interpretation, and, with suitable barrier geometry, support polynomial-time complexity guarantees.

## A one-dimensional barrier calculation

Minimize x subject to x being at least one. The optimum is plainly x equals one, right on the boundary. For a logarithmic barrier, keep x strictly greater than one and minimize t times x minus the logarithm of x minus one. Here t is a positive parameter controlling how strongly we care about the original objective relative to the barrier.

Differentiate. The derivative is t minus one divided by x minus one. Setting it equal to zero gives x equal to one plus one divided by t. The minimizer remains strictly feasible and approaches one as t grows. Its objective value exceeds the true optimum by exactly one divided by t.

We have obtained a central path explicitly. Each value of t defines an interior point. The path is not a sequence of arbitrary guesses near the optimum; it is a family of minimizers of well-defined smooth problems.

There is a price for remaining interior. The second derivative of the logarithmic barrier is one divided by the square of x minus one. It grows rapidly near the boundary. Newton's method can exploit the curvature, but careless undamped steps may leave the feasible region. Practical interior-point methods control step lengths and use a suitable measure of distance from the central path.

## The barrier for many inequalities

Suppose we want to minimize a convex differentiable function subject to inequality constraints. A logarithmic barrier adds a negative logarithm of each positive slack to the objective. It is defined only in the strict interior, where all slacks are positive. As a slack approaches zero from above, the penalty diverges to positive infinity.

For a problem with m inequality constraints, under standard convexity and constraint-qualification assumptions, the objective gap along a central path can be related to m divided by t. This is a duality-based statement, not a claim that all barrier approximations have the same actual primal error. The bound is derived from constructed dual variables and weak duality.

Increasing t pushes the barrier minimizers closer to constrained optima, but it also changes the conditioning of the Newton system. The art of an interior-point implementation is to advance the parameter at a rate the Newton corrections can track.

## Linear programming in primal-dual form

Consider a standard-form linear program: minimize c dotted with x, subject to A x equals b and x componentwise nonnegative. Its dual maximizes b dotted with y, subject to A transpose y being at most c. Define dual slack s as c minus A transpose y. Dual feasibility requires s to be nonnegative.

At an exact optimum, primal-dual complementarity says x sub i times s sub i equals zero for every coordinate, provided the usual optimality hypotheses hold. A central-path point instead has strictly positive x and s, and replaces each zero product by the same positive parameter mu. In other words, x sub i times s sub i equals mu.

The central-path equations are A x equals b, A transpose y plus s equals c, and x times s equals mu times the all-ones vector, with x and s strictly positive. As mu tends to zero, these equations approach the KKT complementarity conditions. They offer a different view of barrier minimization: it is a continuously perturbed primal-dual optimality system.

The duality gap along such a primal-dual feasible central path is n times mu, where n is the number of nonnegative coordinates. This follows by subtracting the dual objective from the primal objective and using the primal and dual equalities. The gap is the sum of all the x sub i times s sub i products.

That gives an explicit certificate of progress. Because the dual objective is a lower bound on the primal optimum, the gap bounds primal suboptimality. It does not, however, certify feasibility or numerical accuracy by itself unless the equalities and inequalities are actually satisfied to verified tolerances.

## Newton steps for the perturbed KKT system

We rarely solve the central-path equations exactly at each mu. Instead, we linearize them around the current approximate iterate and compute a Newton correction. The linear equations involve the primal residual A x minus b, the dual residual A transpose y plus s minus c, and the complementarity residual consisting of the products x sub i s sub i minus mu.

Solving the Newton system produces directions for x, y, and s. A line search or fraction-to-the-boundary rule chooses a step short enough to keep x and s positive. The algorithm also updates mu to encourage complementarity to shrink. Predictor-corrector variants use information about how the current path might change to improve practical performance.

The main numerical cost is often solving sparse linear systems derived from these Newton equations. Choosing whether to factor a normal-equations matrix or an augmented KKT matrix affects fill-in, conditioning, and stability. A mathematical iteration bound says little by itself about memory use or numerical reliability on a specific problem.

## Self-concordance and predictable steps

Why do logarithmic barriers work so reliably in theory? Their third derivatives are controlled by their second derivatives in a sense called self-concordance. This provides quantitative bounds on how fast the local Hessian geometry can change, so a Newton step that is safe in the current local norm stays meaningful nearby.

For suitable self-concordant barriers and regularity assumptions, path-following algorithms can reach a desired duality gap in a number of Newton iterations scaling with the square root of a barrier parameter times the logarithm of the accuracy requirement. The exact theorem depends on the feasible set, barrier, initialization and arithmetic model. It should not be interpreted as a universal running-time guarantee for every numerical implementation.

This is one of the striking achievements of convex optimization: geometry of the barrier supplies a bridge from local Newton steps to global algorithmic complexity.

## What an optimality report must include

An optimizer may report success because its primal residual, dual residual, and complementarity measure are small. Whether those values prove a claimed mathematical tolerance depends on scaling, conditioning, and the accuracy of the arithmetic. In ill-conditioned problems, small residuals can coexist with large errors in some variables. If strict certification is required, externally checkable primal and dual bounds, possibly supported by interval or rational arithmetic, are a separate stage from the floating-point solver's stopping criterion.

Interior-point methods do not remove the boundary. They organize the approach to it. Logarithmic penalties define a smooth interior geometry, the central path connects that geometry to exact KKT conditions, and primal-dual gaps explain why the iterates are improving. The method's theoretical strength comes from keeping those three layers together: optimization geometry, numerical linear algebra, and a verifiable statement about the remaining gap.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(x>1\), the barrier objective \(\phi_t(x)=t x-\log(x-1)\) has derivative \(t-1/(x-1)\) and minimizer \(x_t=1+1/t\). The original optimum is \(1\), with barrier primal gap \(1/t\).

For standard-form LP
\[
\begin{aligned}
\text{(P)}\quad &\min c^\top x &&\text{s.t. }Ax=b,\ x\ge0,\\
\text{(D)}\quad &\max b^\top y &&\text{s.t. }A^\top y+s=c,\ s\ge0,
\end{aligned}
\]
central-path equations at \(\mu>0\) are
\[
Ax=b,\quad A^\top y+s=c,\quad Xs=\mu\mathbf1,\quad x>0,s>0,
\]
with diagonal \(X=\operatorname{diag}(x)\). If these equations hold, the feasible primal-dual gap is
\[
c^\top x-b^\top y=x^\top s=n\mu.
\]
The Newton linearization for residuals \(r_p=Ax-b\), \(r_d=A^\top y+s-c\), \(r_c=Xs-\mu\mathbf1\) is
\[
A\Delta x=-r_p,\quad A^\top\Delta y+\Delta s=-r_d,\quad
S\Delta x+X\Delta s=-r_c.
\]
A damped step must preserve \(x+\alpha\Delta x>0\) and \(s+\alpha\Delta s>0\). Under suitable self-concordant barrier and feasibility hypotheses, path-following iteration complexity scales as \(O(\sqrt\nu\log(\nu/\varepsilon))\), with \(\nu\) the barrier parameter; this is not a generic floating-point runtime bound.

### Exercises with answers

1. Find the one-dimensional central-path point when \(t=10\). **Answer:** \(x=1.1\), with objective gap \(0.1\).
2. For a central-path LP with four nonnegative coordinates and \(\mu=0.01\), what is its duality gap? **Answer:** \(n\mu=0.04\), assuming exact primal and dual feasibility.
3. Why can a full Newton step be unacceptable? **Answer:** it may violate strict positivity of primal or dual slacks.
4. Does a small numerical duality gap alone certify an exact solution? **No:** independently controlled feasibility, rounding, and conditioning also matter.

### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), Chapter 11: Interior-point methods.
- Boyd and Vandenberghe, [Convex Optimization lecture slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf), central path and Newton equations.
