# The Chain Rule Run Backward: Gradients, Backpropagation, and Adjoint Sensitivity

<!-- BEGIN SPOKEN LECTURE -->

# The Chain Rule Run Backward: Gradients, Backpropagation, and Adjoint Sensitivity

A computer model may accept a million parameters and produce one number: an energy, an error, a financial loss, or a score measuring agreement with data. We want to change the parameters to improve that number. Calculating the output once may be straightforward. Calculating how it changes with every parameter can sound like a million additional calculations.

The chain rule gives a way out. It tells us how derivatives compose as we pass through a sequence of operations. But it can be used in two directions. We may push a small input displacement forward to see how every intermediate quantity changes. Or we may pull a measurement of the final output backward to learn how sensitive it is to each earlier quantity. The second method underlies reverse-mode automatic differentiation, backpropagation, and many adjoint methods in scientific computing.

The key is to understand what travels in each direction. Forward propagation carries vectors of possible changes. Reverse propagation carries covectors: linear measurements of how later changes affect the final output. The distinction between vectors and covectors is not a philosophical decoration. It is the reason a transpose appears in the backward rule.

## Follow a small calculation in the forward direction

Start with a simple model. A number x enters an affine transformation, which multiplies it by parameter a and then adds parameter b. Call the result z. Next square z to obtain one intermediate result. Also take the sine of z to obtain another. Add the two intermediate values to obtain the final output F.

Set x equal to three, a equal to two, and b equal to one. Then z is seven, and the output is forty-nine plus the sine of seven. We would like the derivatives of that output with respect to a and b. A little algebra could do this directly, but we will reason through the computation as a chain of operations so the same method will work on a much larger network.

First change a by a small amount while holding b and x fixed. Because z equals a times x plus b, the change in z is approximately x times the change in a. With x equal to three, a one-hundredth increase in a causes a three-hundredth increase in z.

Now consider the final operation. When z changes a little, the square changes by approximately two z times that change. The sine changes by approximately cosine z times that change. Their sum therefore changes by approximately two z plus cosine z, multiplied by the change in z.

At z equal to seven, the output sensitivity with respect to z is fourteen plus cosine seven. Chain the two changes together: the derivative of F with respect to a is three times fourteen plus cosine seven. The derivative with respect to b is fourteen plus cosine seven, because changing b changes z at unit rate.

This forward argument is already the chain rule. We carried a proposed input change through the computation and watched its effect on the output.

## Run the same calculation backward

Now suppose we want both derivatives at once. Rather than select a change in a, propagate it through the network, then select a change in b and repeat, begin at the final output. Ask how the output changes when each immediate predecessor changes.

At the addition step, the output changes one-for-one with each summand. At the square step, the derivative with respect to z is two z. At the sine step, it is cosine z. The two branches meet at z, so their contributions add. The total sensitivity assigned to z is two z plus cosine z.

Next pass this sensitivity through the affine step. Since z changes by x times a change in a, the sensitivity assigned to a is the sensitivity at z multiplied by x. Since z changes one-for-one with b, the sensitivity at b is unchanged. We have recovered both derivatives from one backward pass through the graph.

This is reverse-mode differentiation in miniature. It accumulates contributions from every downstream use of an intermediate quantity, then distributes their combined sensitivity to earlier inputs. The same intermediate z can feed hundreds of later branches; those branches contribute additively to the derivative at z.

The procedure is not a numerical approximation of a derivative by a finite difference. Given differentiable elementary operations and exact arithmetic, it applies the chain rule exactly to the represented computational graph. In floating-point arithmetic the calculated derivatives are still subject to rounding and numerical conditioning, and the graph may itself approximate a continuous model.

## Why reverse mode can save enormous work

Suppose a map takes n parameters and produces one scalar. Its full derivative is a linear functional on an n-dimensional parameter space. A forward-mode calculation efficiently computes the effect of one chosen parameter-direction vector, sometimes called a Jacobian-vector product. To obtain every coordinate derivative by forward mode, we could repeat the calculation for n different basis directions.

Reverse mode begins with the one scalar output and pulls its unit sensitivity backward through the graph. It computes a contribution for every parameter, typically in a small multiple of the cost of evaluating the graph itself, although memory management and shared computations matter. This can be a major advantage when n is large and the output dimension is small.

The situation reverses when a map has only a few inputs but thousands of outputs. A forward pass in a chosen input direction efficiently predicts changes in all the outputs. A reverse pass with a chosen output weighting efficiently computes a weighted sum of output sensitivities with respect to inputs. Neither mode dominates every problem. The shape of the derivative and the question we want answered determine which operation is economical.

In matrix notation, the Jacobian of a composition is the product of Jacobians in the order dictated by the chain rule. A forward displacement is multiplied by those matrices from the input side toward the output. A linear measurement of the output is multiplied by the transpose matrices in reverse order. This is called a vector-Jacobian product in many software systems. Mathematically it is the pullback of a covector through a differentiable map.

## An implicit problem: the output of a solver

Computational graphs are not always explicit chains of arithmetic operations. Sometimes the model output is defined as the solution of an equation. For example, a parameter theta determines a matrix A and a right-hand side b. The state u is defined by the linear system A times u equals b. An observer then measures a scalar quantity c transpose times u.

Changing theta changes A, perhaps b, and consequently the solution u. We could solve the linear system again for a slightly different theta and estimate the derivative by a finite difference. That may be expensive or inaccurate. Instead, differentiate the defining equation.

At a parameter value where A is invertible and depends smoothly on theta, the differentiated equation says: A times the change in u, plus the change in A acting on u, equals the change in b. Rearrange it. A times the change in u equals the change in b minus the change in A acting on u.

If theta is a single parameter, we can solve a new linear system for the derivative of u. If theta is a long vector of parameters and we only want one scalar output, doing a separate state-derivative solve for each parameter can be wasteful. The adjoint method replaces them with a solve that depends on the scalar output, not on the number of parameters.

Define the adjoint vector lambda by solving the transposed system: A transpose times lambda equals c. The change in the scalar output c transpose u is c transpose times the change in u, when c is fixed. Because c equals A transpose lambda, this becomes lambda transpose A times the change in u. Substitute our differentiated state equation. The output change is lambda transpose times the change in b minus the change in A acting on u.

This expression is the adjoint sensitivity formula. Solve the original system once for u, solve the transposed system once for lambda, and then evaluate how A and b depend on each parameter. The potentially expensive state solves no longer have to be repeated for each parameter direction. When the output measurement c also depends on theta, an additional explicit derivative term is required.

## A complete two-by-two adjoint example

Let A be diagonal. Its first diagonal entry is one, and the second is two plus theta. Let b have entries one and two. We ask for the sum of the two components of u, so c has both entries one. Work at theta equal to zero.

The state equation gives u with entries one and one. The reported sum is two. If we solve the problem for general theta, the second state component is two divided by two plus theta. Its derivative at zero is minus one half. That direct calculation gives us a target to check.

Now take the adjoint route. At theta zero, A is diagonal with entries one and two. The adjoint system A transpose times lambda equals one, one. Its solution has entries one and one half. The derivative of A with respect to theta is a diagonal matrix with entries zero and one. Applying it to u produces the vector zero, one. The vector b does not change with theta, so its derivative is zero.

The adjoint formula says the derivative of the reported sum is minus lambda dotted with zero, one. That is minus one half, exactly the direct answer. For this tiny system the adjoint method is longer than differentiation by hand. For a large discretized physical system with many parameters and only a few measurements, the change in computational cost can be substantial.

## What the adjoint does not promise

The differentiated system presumes a locally unique, differentiable state. If A becomes singular, state sensitivity can blow up or cease to be defined. A nearly singular A can make the adjoint and forward sensitivities enormous. This is a conditioning problem, not a failure of automatic differentiation.

A program may also contain decisions: a maximum operation, a branch taken when a quantity crosses a threshold, a sorting step, or an iterative solver that stops after a variable number of iterations. A derivative of the executed instructions may not be a derivative of the ideal mathematical problem a scientist intended to solve. At a nonsmooth boundary, different one-sided derivatives can exist without one ordinary derivative. For iterative algorithms, differentiating the finite run and differentiating a fully converged solution can be different operations.

Reverse-mode algorithms must retain or reconstruct intermediate values needed during the backward pass. This leads to memory and checkpointing tradeoffs. These implementation questions are important, but they come after the mathematical question: which function or solution map is actually being differentiated?

## From backpropagation to optimality

There is a final connection. In constrained optimization, Lagrange multipliers measure how changes in constraints affect an objective. In inverse problems, an adjoint variable measures how changes to the governing equations affect an observed quantity. In reverse-mode differentiation, intermediate sensitivities measure how changes to internal nodes affect the final output. The algebra often involves transposed Jacobians because each situation pulls a final linear measurement backward through a chain of dependencies.

We began with a single scalar output built from one affine step, a square, a sine, and an addition. The forward chain rule computed one directional effect. The reverse chain rule collected all parameter sensitivities. The adjoint of a linear system showed how to do the same when the computational step is an implicit solve. These are not unrelated tricks. They are different manifestations of one structural fact: vectors carry possible changes forward, while covectors carry measurements of change backward.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Forward and reverse differentiation

For \(F=f_k\circ\cdots\circ f_1\), the Jacobian is \(DF=J_k\cdots J_1\). Forward mode computes \(J_k\cdots J_1v\); reverse mode computes \(J_1^T\cdots J_k^Tw\) for a chosen output covector \(w\).

The scalar computation

\[
z=ax+b,\quad F(a,b;x)=z^2+\sin z,
\quad \frac{\partial F}{\partial a}=x(2z+\cos z),\quad
\frac{\partial F}{\partial b}=2z+\cos z.
\]

At \((a,b,x)=(2,1,3)\), \(z=7\) and the derivative covector with respect to \((a,b)\) is \((3(14+\cos7),14+\cos7)\).

### Implicit solve and adjoint

Let \(A(\theta)u(\theta)=b(\theta)\), with \(A\) differentiable and invertible near the operating point, and \(\Phi(\theta)=c^Tu(\theta)\) for fixed \(c\). For an infinitesimal parameter direction \(h\):

\[
A\,du[h]=db[h]-dA[h]u,
\qquad A^T\lambda=c,
\qquad d\Phi[h]=\lambda^T\bigl(db[h]-dA[h]u\bigr).
\]

If \(c\) depends on \(\theta\), add \(dc[h]^Tu\); if the scalar objective is \(\phi(u,\theta)\), solve \(A^T\lambda=\nabla_u\phi\) and add the direct derivative \(\partial_\theta\phi[h]\).

Example: \(A(\theta)=\operatorname{diag}(1,2+\theta)\), \(b=(1,2)^T\), \(c=(1,1)^T\), at \(\theta=0\), \(u=(1,1)^T\), \(\lambda=(1,1/2)^T\), \(A'u=(0,1)^T\), so \(\Phi'=-1/2\).

### Exercises and solutions

1. **Shared intermediate.** For \(F=(x^2+1)^2+\cos(x^2+1)\), find the derivative without expanding. **Answer:** \((2(x^2+1)-\sin(x^2+1))(2x)\).
2. **Reverse Jacobian dimensions.** If \(f:\mathbb R^5\to\mathbb R^3\) has Jacobian \(J\), what are the shapes of \(Jv\) and \(J^Tw\)? **Answer:** three-vector from a five-vector, and five-vector from a three-vector, respectively.
3. **Direct derivative check.** For the two-by-two example, solve \(u(\theta)\) exactly and differentiate the scalar output. **Answer:** \(\Phi(\theta)=1+2/(2+\theta)\), \(\Phi'(0)=-1/2\).
4. **Variable right-hand side.** If \(b(\theta)=(1,2+\theta)^T\) with the same \(A\), what happens? **Answer:** the solution is always \((1,1)^T\) near zero, so \(\Phi'=0\); the adjoint terms \(db-A'u\) cancel.
5. **Failure condition.** What happens as \(\theta\to-2\) in the original two-by-two example? **Answer:** \(A\) becomes singular and the state/output derivative generally diverges.

### Sources and further reading

- [MIT OCW 18.02SC, *Multivariable Calculus*](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), chain rule and Jacobians.
- [Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), sensitivity and Lagrange multipliers.
- [Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*](https://nhigham.com/accuracy-and-stability-of-numerical-algorithms/), conditioning of linear solves.
- Related lectures: `multivariable-calculus:030000`, `numerical-analysis:016000`, `linear-algebra:012000`, `multivariable-calculus:067000`.
