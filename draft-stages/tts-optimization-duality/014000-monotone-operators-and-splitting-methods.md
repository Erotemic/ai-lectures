# 014000 — Monotone Operators, Resolvents, and Splitting Methods

**Track:** Optimization and Duality. **Background:** convex subgradients, proximal maps, Hilbert spaces, fixed-point iteration. **Central question:** how can a difficult optimality condition be solved using simpler operators one at a time?

<!-- BEGIN SPOKEN LECTURE -->

# Monotone Operators, Resolvents, and Splitting Methods

Imagine minimizing an objective made of two parts. One part measures fit to data. The other imposes sparsity, smoothness, or a constraint. Each part is easy to handle by itself, but their sum is awkward. A common computational strategy is to alternate between the two. Monotone operator theory explains when that alternation is more than a heuristic.

For a differentiable convex function, a minimizer is a point where the gradient is zero. For a nonsmooth convex function, the gradient is replaced by a set of possible subgradients. The optimality condition becomes that zero belongs to the subdifferential. This is an inclusion problem, not just an equation.

A monotone operator extends the familiar idea of an increasing function. Given two input points and one output value chosen from the operator at each input, the inner product of the difference in outputs with the difference in inputs must be nonnegative. In one dimension, this reduces to the observation that moving to the right cannot make a monotone graph move downward.

The subdifferential of a proper, lower-semicontinuous convex function is a maximal monotone operator. Maximal means its graph cannot be enlarged while preserving monotonicity. This property matters because it guarantees a well-defined way to invert the identity plus a positive multiple of the operator.

## A resolvent is an implicit step

Take a maximal monotone operator A. Given a point z, seek a point x such that z equals x plus a positive step size times an output of A at x. The map sending z to x is called the resolvent of A.

For a convex subdifferential, the resolvent is exactly the proximal operator. It asks for the point that balances the objective value against the cost of moving away from z. Instead of taking a gradient step that may be undefined at a corner, the proximal map solves an implicit local optimization problem.

Consider the absolute-value function on the real line. Its proximal operator is soft thresholding. A positive input is reduced toward zero by the threshold, a negative input is increased toward zero, and anything with magnitude at most the threshold becomes exactly zero. The corner at zero is not a numerical obstacle. The resolvent treats it as part of the solution.

For the indicator function of a closed convex set, the proximal operator is simply Euclidean projection onto that set. Sparsity and feasibility thus become two examples of the same operator construction.

## Why resolvents are stable

Monotonicity gives the resolvent a remarkable inequality. The distance between two outputs cannot exceed the distance between their inputs. More strongly, the squared output distance is bounded by the inner product of the output difference with the input difference. This property is called firm nonexpansiveness.

It follows directly from the defining inclusion for the resolvent. Subtract the two inclusion relations and apply monotonicity to the operator outputs. The resulting inequality is the key estimate behind many fixed-point convergence arguments.

Ordinary nonexpansiveness alone would not force every iterative scheme to converge. The stronger averaged structure and the existence of a solution are part of what makes suitable splitting algorithms work.

## Separating two operators

Suppose the optimality condition is that zero belong to A of x plus B of x. Each operator has an easy resolvent, but the resolvent of their sum is expensive. Douglas–Rachford splitting constructs a fixed-point iteration using only the resolvents of A and B and a reflection through one of them.

The iteration works in an auxiliary variable z. At each step, first apply one resolvent, reflect that result across z, apply the other resolvent, then correct z by the difference. Under standard maximal-monotonicity, solvability, and related regularity hypotheses, the iterates converge in the appropriate weak sense, and in finite-dimensional settings the projected, or shadow, iterates approach a solution.

There is an important subtlety. The auxiliary variable z need not itself be the minimizer. The solution is recovered through a resolvent. Confusing the internal fixed point with the primal solution can make a correct algorithm look incorrect.

Another familiar method, forward–backward splitting, applies a gradient step to the smooth part and a proximal step to the nonsmooth part. It takes advantage of extra smoothness and step-size bounds rather than solving both steps implicitly. ADMM is closely related to Douglas–Rachford splitting through the dual problem, although the raw primal and dual iterates should not be identified without the proper transformation.

## Limits of the framework

If the objective is nonconvex, the subdifferential may not be maximal monotone and the same convergence proof does not automatically apply. If the two operators have no common zero, a fixed-point iteration cannot be expected to recover one. Even with convexity, splitting parameters and the ability to compute the resolvents accurately matter.

The central insight is not that alternating two arbitrary operations is safe. It is that an optimization problem can be rewritten as a monotone inclusion, whose component resolvents have strong geometric properties. The algorithm then inherits convergence from those properties rather than from the appearance of progress in a numerical log.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Compute \(\operatorname{prox}_{2|\cdot|}(1.5)\). **Answer:** zero, since the threshold 2 exceeds the input magnitude.
2. What is the proximal map of the indicator of [0,1] at z=3? **Answer:** 1, the Euclidean projection.
3. Why is every resolvent of a maximal monotone operator nonexpansive? **Answer:** firm nonexpansiveness implies \(\|Jx-Jy\|\le\|x-y\|\) by Cauchy–Schwarz.
4. Is a Douglas–Rachford fixed point necessarily itself the minimizer? **Answer:** no; a resolvent of the fixed point yields a primal solution.

### Reading and source notes

- [Parikh and Boyd, Proximal Algorithms](https://web.stanford.edu/~boyd/papers/pdf/prox_algs.pdf), resolvents and splitting schemes.
- [Boyd et al., ADMM](https://stanford.edu/~boyd/admm), operator splitting and its relation to constrained optimization.
- [Giselsson and Boyd, Douglas–Rachford and ADMM scaling](https://stanford.edu/~boyd/papers/pdf/diag_scaling_DR_ADMM.pdf), firm nonexpansiveness and proximal operators.
