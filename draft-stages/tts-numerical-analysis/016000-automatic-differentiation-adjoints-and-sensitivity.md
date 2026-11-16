# 016000 — Automatic Differentiation and Adjoint Sensitivity

**Track:** Numerical Analysis and Reliable Computation. **Background:** derivatives, chain rule, linear systems, numerical solvers, optimization. **Central question:** how can we differentiate a computation with thousands of intermediate steps without forming its full Jacobian?

<!-- BEGIN SPOKEN LECTURE -->

# Automatic Differentiation and Adjoint Sensitivity

A numerical model may involve millions of arithmetic operations. Perhaps it solves a fluid equation, fits a physical parameter, or predicts the output of a complicated network. Now suppose we want to know how its final answer changes when one input parameter changes. We could rerun the model after nudging the input. But repeated perturbations may be expensive, inaccurate, or numerically unstable. Automatic differentiation offers another approach: differentiate the computation itself.

The key point is that a complicated numerical program is composed of elementary operations. If we know the derivative rule for each operation, the chain rule can propagate derivative information through the entire computation. We do not need to invent a new symbolic formula for the whole program, nor approximate the derivative by subtracting two nearly equal outputs.

## Forward differentiation follows the calculation

Imagine a computation as a sequence of intermediate variables. Each variable is produced from earlier ones by addition, multiplication, division, or a smooth elementary function. Forward-mode automatic differentiation carries an ordinary value and a directional derivative together through those operations.

For multiplication, the derivative follows the product rule. For sine, it follows the cosine rule. A convenient mathematical model is a dual number: an ordinary scalar plus a small formal component whose square is zero. Multiplying dual numbers automatically enforces the first-order product rule, because all terms involving the square of that formal component disappear exactly.

This is not the same as evaluating a function with a tiny numerical perturbation. The formal component is bookkeeping for the derivative, not a floating-point step size to be chosen. Forward mode computes a Jacobian-vector product: it tells us how the outputs vary in one specified input direction.

If there are only a few input parameters and many outputs, forward mode can be very effective. We propagate one direction at a time, or a collection of directions in parallel, without constructing a symbolic derivative expression.

## Reverse differentiation follows the dependence backward

Suppose instead there are a million inputs but only one scalar objective. Running forward mode once per input would be wasteful. Reverse mode takes advantage of the fact that all inputs contribute to the same final scalar.

First evaluate the program normally, recording or reconstructing the intermediate values needed for derivatives. Then propagate sensitivity backward from the final scalar. At an addition node, the incoming derivative contributes to both inputs. At a multiplication node, the derivative passed to either input is multiplied by the other input's forward value. The derivative contributions from different downstream paths are accumulated.

This is reverse-mode automatic differentiation, also called backpropagation in many machine-learning settings. Its computational cost for a scalar output is often a small multiple of the original evaluation, rather than a multiple proportional to the number of input variables. The tradeoff is storage or recomputation: the backward pass needs information from the forward calculation.

Take a small example. Let the objective equal x squared times y plus sine of x times y. To compute it, form x squared, multiply by y, form x times y, take its sine, and add the two branches. Reverse accumulation returns the partial derivative with respect to x as twice x times y plus y times the cosine of x times y. The derivative with respect to y is x squared plus x times that same cosine. Every term follows from a local chain-rule operation on the computation graph.

The example may look easy enough to differentiate by hand, but the point is that the same algorithm scales to graphs containing thousands or millions of such operations.

## Differentiating a solved equation

Many scientific computations are not explicit formulas. They solve an equation, such as a linear system, and use the solution in an objective. It is possible to differentiate every iteration of the chosen solver. But often a more stable and efficient route is to differentiate the equation defining the exact solution.

Suppose a parameter theta determines a nonsingular matrix A and a right-hand side b, and the state u solves A times u equals b. Differentiating the equation gives the derivative of A times u, plus A times the derivative of u, equal to the derivative of b. Rearranging, the state derivative is the solution of another linear system with the same matrix A.

If theta has many components, solving one such sensitivity system per component may again be expensive. Instead, suppose the output we care about is a scalar objective depending on u and possibly theta directly. Introduce an adjoint vector by solving the transposed linear system with the derivative of the objective with respect to u on the right-hand side.

Once we have this adjoint, the derivative of the scalar objective with respect to theta can be computed by pairing the adjoint with the derivative of b minus the derivative of A applied to u, then adding any direct dependence of the objective on theta. One adjoint solve can support sensitivities with respect to many parameters.

This is the same reverse accumulation principle at the level of an implicit numerical model. Rather than propagating all parameter variations forward, we propagate the influence of the scalar objective backward through the governing equation.

## A concrete optimization setting

Suppose a heat-transfer model depends on a conductivity parameter, and the objective measures the mismatch between predicted temperatures and sensor readings. The forward solve computes the temperature field. The adjoint solve computes how the mismatch responds to perturbations of the field. The conductivity gradient is then obtained by combining the forward and adjoint fields with the derivative of the discretized operator.

There are two distinct derivatives here. One is the derivative of the finite-dimensional discretized problem actually solved by the computer. The other is the derivative of the underlying continuum model. If we differentiate the discrete system, the result may be accurate for that discretization while still differing from the continuum sensitivity. Refining the mesh, checking consistency, and analyzing numerical errors remain necessary.

## The pitfalls are mathematical, not only computational

Automatic differentiation computes derivatives of the executed differentiable operations. It does not make a nondifferentiable program differentiable. A branch that changes abruptly, a maximum with a tie, a pivot choice, an iteration stopping criterion, or a change in the active set of an optimization problem may create discontinuities or derivative conventions that require careful interpretation.

Similarly, an implicit differentiation formula assumes the matrix or Jacobian being inverted is nonsingular. Near a singular point, sensitivities may become enormous. This is genuine conditioning, not an error caused by automatic differentiation. A correct algorithm can accurately report an extremely sensitive problem.

Memory is another practical issue. Reverse mode may need intermediate values from a very long calculation. Checkpointing trades extra recomputation for less storage. For time-dependent models, an adjoint calculation may run backward through the history while reconstructing forward states as needed. That requires deliberate numerical design, especially for chaotic or highly unstable dynamics.

## Why derivatives are now part of the model

Finite differences ask what happens after we change an input and rerun the model. Automatic differentiation follows the chain rule through the model's operations. Adjoint methods exploit the structure of an implicit equation to compute many parameter sensitivities from a small number of linearized solves.

Together, these techniques make gradients accessible for large simulations, inverse problems, and optimal control. But they do not remove the need to distinguish an implemented function from a continuous mathematical model, or numerical stability from differentiability. The best use of automatic differentiation is to combine exact chain-rule structure with the same conditioning and error analysis we apply to every serious numerical algorithm.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(F:\mathbb R^n\to\mathbb R^m\), forward AD computes a **Jacobian-vector product** \(J_F(x)v\); reverse AD computes a **vector-Jacobian product** \(w^\top J_F(x)\). Dual numbers \(a+b\varepsilon\), \(\varepsilon^2=0\), implement first-order forward propagation.

**Worked graph:** \(f(x,y)=x^2y+\sin(xy)\). Then
\[\partial_x f=2xy+y\cos(xy),\qquad\partial_y f=x^2+x\cos(xy).\]
For x=2, y=3: \(\nabla f=(12+3\cos6,\ 4+2\cos6)\).

**Implicit adjoint:** assume a differentiable, nonsingular \(A(\theta)\), differentiable \(b(\theta)\), and state \(u(\theta)\) satisfying \(A(\theta)u=b(\theta)\). For a differentiable scalar objective \(J(u,\theta)\), set \(A(\theta)^\top\lambda=\nabla_u J\). For a scalar parameter \(\theta\),
\[\frac{dJ}{d\theta}=\frac{\partial J}{\partial\theta}+\lambda^\top\left(\frac{db}{d\theta}-\frac{dA}{d\theta}u\right).\]
For multiple parameters, replace derivatives by corresponding directional derivatives or collect the resulting gradient components. This is differentiation of the exact algebraic solution, not automatically of a finite-iteration stopping rule.

### Exercises with answers

1. What does forward AD compute for a direction v? **Answer:** \(J_F(x)v\), without forming the full Jacobian.
2. Why is reverse mode attractive for one scalar objective with many parameters? **Answer:** one backward accumulation computes the full gradient at a cost typically proportional to a small multiple of the primal evaluation.
3. If \(A\) does not depend on theta but b does, what remains of the adjoint formula? **Answer:** \(dJ/d\theta=\partial_\theta J+\lambda^\top b_\theta\).
4. What goes wrong near a singular A? **Answer:** implicit sensitivities can become ill-conditioned or fail to exist, irrespective of how derivatives are implemented.

### Reading and source notes

- [MIT 18.S096, Forward and Reverse-Mode Automatic Differentiation](https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/mit18_s096iap23_lec08.pdf), Jacobian products and storage tradeoffs.
- Andreas Griewank and Andrea Walther, [*Evaluating Derivatives*](https://epubs.siam.org/doi/book/10.1137/1.9780898717761), algorithmic differentiation foundations.
- [SciPy, sparse linear algebra documentation](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html), numerical solve context for adjoint systems.
