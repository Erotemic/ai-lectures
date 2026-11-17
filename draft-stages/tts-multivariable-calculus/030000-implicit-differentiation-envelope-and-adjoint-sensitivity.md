# Differentiating an Optimizer: Implicit Functions, Envelope Theorems, and Adjoints

**Track:** Multivariable Calculus from First Principles. **Focus:** differentiate equality-constrained optimality conditions, derive value sensitivities and adjoint formulas, and diagnose singular or switching solution maps.

<!-- BEGIN SPOKEN LECTURE -->

# Differentiating an Optimizer: Implicit Functions, Envelope Theorems, and Adjoints

Imagine an engineer tuning a model to experimental data. The fitted parameters are the result of an optimization problem. Tomorrow the experiment is repeated, and one measurement changes slightly. The engineer wants to know how the fitted parameters will change, perhaps to estimate uncertainty or to design a better experiment.

One approach is to solve the entire optimization problem again after every small change. That is a valid numerical experiment, and sometimes the simplest one. But for many input parameters, repeatedly solving a large constrained problem becomes expensive. It also obscures a useful mathematical question: is the optimized solution a smooth function of the data, and if so can we calculate its derivative directly?

The surprising answer is that the matrix needed to differentiate a regular constrained optimizer is the same KKT matrix used for Newton's method. We will build that connection explicitly, derive a shortcut for the optimized objective value, and explain the adjoint technique used when an optimizer sits inside a larger learning or design system. We will also find a case where the optimizer is unique and yet its derivative does not exist.

## Turn an optimizer into an implicit equation

Let p stand for a vector of input parameters: measured data, model coefficients, or a design choice. We want to minimize an objective f of x and p subject to equality constraints c of x and p equal to zero. Assume the objective and constraints are smooth enough to differentiate the quantities we will use.

At a regular local solution, there is a multiplier lambda such that the gradient of the Lagrangian with respect to x is zero and the constraint vector is zero. These equations depend on x, lambda, and p. Treat them as a single residual function F. Its unknowns are x and lambda; p is the external input. The optimizer solves F equals zero.

Now imagine moving p by a tiny amount. If there is a differentiable branch of solutions, both x and lambda move to keep F equal to zero. Apply the chain rule. The derivative of F with respect to the unknowns, multiplied by the change in x and lambda, plus the derivative of F with respect to p multiplied by the input change, must equal zero.

The derivative with respect to the unknowns is exactly the KKT matrix: Lagrangian Hessian in the upper left, constraint Jacobian transpose in the upper right, constraint Jacobian in the lower left, and zero in the lower right. The derivative with respect to p supplies a new right-hand side. Solving this linear system gives the derivative of the optimizer and its multipliers with respect to p.

This derivation has a crucial condition. The implicit function theorem requires that the KKT matrix be nonsingular at the solution, with the residual sufficiently smooth. Under this hypothesis it gives a locally unique differentiable branch of stationary KKT solutions. It does not, by itself, establish that every branch point is a local minimum, much less the global one. To know that our stationary solution remains a strict local minimizer, we can combine the rank condition with positive Lagrangian curvature on the tangent space and the appropriate continuity assumptions.

If the matrix is singular, we cannot simply replace its inverse by a pseudoinverse and declare that we have found the true derivative. There may be multiple solution branches, a corner, or no smooth branch at all. Numerical regularization may produce a useful surrogate, but it is not a substitute for a differentiability theorem.

## A complete constrained sensitivity calculation

Consider minimizing one half of x squared plus one half of y squared, subject to the sum x plus y equaling a parameter p. The objective favors the origin, while the equality says the two variables must share a prescribed total. By symmetry, the optimal choice is x equals p over two and y equals p over two. The multiplier, for a Lagrangian with lambda times x plus y minus p, is negative p over two.

The optimized value is p squared over four. It is easy to differentiate these explicit formulas, but we will pretend we do not know them and use the implicit system instead. The two stationarity equations are x plus lambda equals zero and y plus lambda equals zero. The constraint equation is x plus y minus p equals zero.

Differentiate all three equations with respect to p. The first gives x prime plus lambda prime equals zero. The second gives y prime plus lambda prime equals zero. The third gives x prime plus y prime equals one. Therefore x prime and y prime each equal one half, while lambda prime equals negative one half.

Notice what we computed. A unit increase in the required total is shared equally between x and y. The multiplier changes because the balance between the objective gradient and constraint normal changes. Our derivative came from a three-by-three linear system and is valid at every p in this example because the KKT matrix is constant and invertible.

In a nonlinear example, the same procedure produces a local derivative at the current solution. The system need not have constant coefficients, and the computed derivative changes with the parameter. At any given regular point, though, it still comes from a linear solve rather than a fresh nonlinear optimization for every perturbation.

## Be careful when the parameter enters more than one place

The right-hand side of the sensitivity system is not merely the derivative of the equality-constraint vector. The input p may also change the objective, the constraint Jacobian, and therefore the stationarity equation. The correct upper component is the mixed derivative with respect to x and p of the full Lagrangian, holding the current multiplier fixed for that partial derivative. The lower component is the direct parameter derivative of the constraints.

For example, suppose we minimize one half of x minus p squared plus one half of y squared while keeping x plus y equal to one. The solution is x equal to the quantity one plus p, divided by two, and y equal to the quantity one minus p, divided by two. The multiplier is the quantity p minus one, divided by two. As p increases, x increases at rate one half and y decreases at rate one half; the fixed-sum constraint makes their derivatives add to zero.

If we differentiated only the constraint equation, we would learn that x prime plus y prime equals zero, but we would not know how that change is shared. The derivative of stationarity, including the effect of p on the objective gradient, supplies the missing information. Ignoring the upper right-hand side would incorrectly predict both variables to be stationary with respect to p.

## The envelope theorem: a shortcut for the optimal value

Sometimes the question is not how every optimal parameter changes, but how the best achievable objective value changes. Define v of p as the objective evaluated at the optimizer. Differentiate using the chain rule: v prime is the direct derivative of f with respect to p plus the objective gradient dotted with the derivative of the optimizer.

The stationarity equation lets us replace the objective gradient by minus the constraint Jacobian transpose times lambda. Differentiated feasibility tells us that the constraint Jacobian times x prime is minus the direct parameter derivative of c. Combine them, and every occurrence of x prime cancels. The result is strikingly short: the derivative of the optimal value is the partial derivative with respect to p of the Lagrangian, evaluated at the optimum and multiplier.

In our first example the constraint is x plus y minus p. Its partial derivative with respect to p is negative one, and the objective has no direct p dependence. Therefore the optimized-value derivative is minus lambda. Since lambda is negative p over two, we get p over two, exactly the derivative of p squared over four.

This explains one interpretation of multipliers as shadow prices. With a constraint written as x plus y minus p equals zero, minus lambda measures the first-order cost of increasing the right-hand side p. The sign depends on how the constraint was written; an unexplained sign change can reverse the economic interpretation. The value function need not be globally smooth merely because a multiplier can be computed at one parameter value.

In the second example, the constraint does not directly depend on p, but the objective does. The derivative of the optimal value is then just the explicit p derivative of the objective at the optimizer. The value is one quarter of the square of the quantity one minus p, and its derivative is the quantity p minus one, divided by two. That agrees with the objective's partial derivative after substituting the optimal x.

The envelope formula is useful because it avoids computing the entire vector x prime when all we want is one scalar value derivative. It still depends on having the relevant regular solution and a differentiable value branch; at active-set changes, global nonuniqueness, or other degeneracies, we must check what form of directional derivative actually exists.

## The adjoint method for a different scalar output

Now suppose our downstream question is some scalar quantity Q of x and p that is not the optimized objective value. Perhaps x is a fitted state used to predict a physical observable, or perhaps Q is a validation loss that an outer training loop wants to differentiate. The envelope theorem no longer eliminates x prime automatically.

We could compute x prime separately for every component of p, then apply the chain rule to Q. If p has a million components, that can require a million linear solves. But Q is only one scalar output. We can reverse the computation using an adjoint.

Let u collect both the primal variables and the multipliers, so the KKT equation is F of u and p equals zero. We have u prime equal to minus K inverse times the parameter derivative of F. The total derivative of Q is its direct parameter derivative plus its derivative with respect to u times u prime. Substituting the implicit formula gives the direct term minus a row-vector product involving K inverse.

Instead of applying K inverse separately to each input direction, solve one transposed linear system. Choose an adjoint vector w so that K transpose times w equals the transpose of the derivative of Q with respect to u. Then the entire gradient with respect to p is the direct derivative of Q minus w transpose times the parameter derivative of F.

This is the same linear-algebra trick that makes adjoint-state methods attractive in inverse problems and optimal control. One large transposed solve can replace a separate forward sensitivity solve for every input parameter, when the output is scalar. For many output quantities and few input parameters, the forward approach may instead be cheaper. Both methods depend on the same local regularity and the accuracy of the same underlying KKT matrix.

The KKT matrix for equality constraints is symmetric when we use an exact symmetric Lagrangian Hessian, so its transpose is the same matrix in exact arithmetic. In practical code there may still be reasons to treat transpose solves carefully, especially when derivatives are approximated, block orderings differ, or preconditioners are nonsymmetric.

## The corner where implicit differentiation breaks

Return to the elementary constrained fit: minimize one half of x minus p squared, with x nonnegative. The minimizer is zero for negative p and equals p for positive p. It is unique for every p. Its dependence on p is continuous and even Lipschitz, but it is not differentiable at zero.

Why does a naive smooth KKT derivation fail at zero? The active inequality has multiplier zero there. If we choose the active side and treat x equal to zero as a permanent equality, we obtain derivative zero. If we choose the inactive side, we obtain derivative one. Both are correct one-sided derivatives on their own branches, but neither is the derivative of the full optimizer at the switch. There is no ordinary derivative to recover.

Under an appropriate combination of smoothness, independent active constraint gradients, positive second-order curvature, and strict complementarity, a fixed active set can remain stable locally. Then the active constraints can be differentiated like equalities. But if strict complementarity fails, that simple fixed-set argument does not apply. Even when a derivative exists by some other theorem, it needs its own justification.

There are further warnings. Parameters that cannot be identified from data can make the KKT or normal-equation system singular. Multiple global minima can exchange which one is selected. A numerical optimizer that has not converged to an accurate KKT root may yield a derivative of the current approximate state rather than of the true solution. Differentiating every iteration of a solver and implicitly differentiating the converged fixed point are related approaches, but they are not automatically equivalent when the solver is truncated, nonsmooth, or uses changing active sets.

What we gain from the implicit perspective is a compact description of the dependency structure. The Newton solve says how to correct a point toward stationarity and feasibility. The sensitivity solve says how a regular stationary point must move when the data move. The envelope theorem extracts the derivative of the best value; the adjoint method extracts the gradient of another scalar output efficiently. All four computations depend on the geometry encoded by the same Lagrangian and the same constraint Jacobian.

The recurring question is therefore not simply whether we can take a derivative. It is whether the optimizer defines a locally well-behaved solution map, whether we have the correct KKT equations, and whether the relevant linear system is sufficiently well conditioned to trust the answer. When those conditions are met, constrained optimization becomes a differentiable mathematical component. When they fail, the failure itself tells us something about the inverse problem we are trying to understand.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### KKT implicit-function derivative

Let \(p\in\mathbb R^k\), \(u=(x,\lambda)\), and

\[
F(u,p)=\begin{bmatrix}\nabla_x L(x,\lambda,p)\\c(x,p)\end{bmatrix},\qquad
L=f(x,p)+\lambda^\top c(x,p).
\]

At a solution \(F(u_*,p_*)=0\) where the functions are sufficiently smooth and

\[
K=F_u=\begin{bmatrix}\nabla^2_{xx}L&J^\top\\J&0\end{bmatrix}
\]

is nonsingular, the implicit function theorem supplies a local \(C^1\) branch of KKT roots and

\[
D_pu_*=-K^{-1}F_p,\qquad
F_p=\begin{bmatrix}\nabla^2_{xp}L\\D_pc\end{bmatrix}.
\]

The mixed derivative \(\nabla^2_{xp}L\) includes contributions from the parameter dependence of \(f\) **and** the parameter dependence of the constraint Jacobian, at fixed \(\lambda\). Nonsingularity establishes a root branch; a stable local minimum additionally uses constrained second-order sufficiency.

### Exact value derivative and adjoint derivative

For the locally optimized value \(v(p)=f(x_*(p),p)\), differentiation of stationarity and feasibility gives the envelope identity

\[
D_pv=\partial_p f(x_*,p)+\lambda_*^\top D_pc(x_*,p)=\partial_pL(x_*,\lambda_*,p).
\]

For another scalar output \(Q(u_*(p),p)\), solve

\[
K^\top w=(D_uQ)^\top.
\]

Then \(D_pQ=\partial_pQ-w^\top F_p\). For a scalar output depending only on \(x\) and \(p\), pad \(D_xQ\) with zeros in multiplier components. This is one adjoint linear solve for a scalar output, irrespective of the dimension of \(p\), after the solution and needed derivatives have been computed.

### Worked examples

**Changing constraint right-hand side:** \(\min\frac12(x^2+y^2)\) subject to \(x+y-p=0\). The stationary KKT equations are

\[
x+\lambda=0,\ y+\lambda=0,\ x+y-p=0,
\]

and hence \((x_*,y_*,\lambda_*)=(p/2,p/2,-p/2)\). Derivative: \((x_*',y_*',\lambda_*')=(1/2,1/2,-1/2)\). Optimal value \(v(p)=p^2/4\), so \(v'(p)=p/2=-\lambda_*\).

**Changing objective parameter:** \(\min\frac12((x-p)^2+y^2)\) subject to \(x+y=1\). The optimizer and multiplier are \(((1+p)/2,(1-p)/2,(p-1)/2)\), so the first two derivatives are \((1/2,-1/2)\). The optimal value is \((1-p)^2/4\); its derivative \((p-1)/2\) agrees with \(\partial_p f=-(x_*-p)\) at the solution.

**Active-set switch:** \(\min_{x\ge0}\frac12(x-p)^2\) has \(x_*(p)=\max(p,0)\), which is not differentiable at \(p=0\), where strict complementarity fails. No global Jacobian can be inferred from either one-sided active-set KKT system.

### Exercises with answers

1. **Envelope sign:** suppose \(c(x,p)=a^\top x-p\) and \(L=f+\lambda c\), with f independent of p. What is \(v'(p)\)? **Answer:** \(-\lambda_*\), at any regular differentiable local optimum branch.
2. **IFT check:** for \(\min\frac12(x^2+y^2)\) with \(x+y=p\), calculate \(\det K\). **Answer:** for \(K=\left[\begin{smallmatrix}1&0&1\\0&1&1\\1&1&0\end{smallmatrix}\right]\), the determinant is \(-2\ne0\). The local branch exists, and in fact is global.
3. **One output, many inputs:** if \(p\in\mathbb R^{1000}\) and \(Q\) is scalar, compare forward sensitivity and adjoint solves, assuming a factored KKT matrix. **Answer:** forward directional sensitivities require up to 1000 right-hand-side solves to obtain the full Jacobian; one adjoint solve computes the full gradient of Q after assembling \(F_p\). Factorization reuse can make multi-right-hand-side solves cheaper but does not reverse their count.
4. **False derivative:** why does the unique solution of \(\min_{x\ge0}\frac12(x-p)^2\) not have a derivative at \(p=0\)? **Answer:** left and right derivatives are zero and one. The active constraint has a zero multiplier at the switch, so the fixed-active-set hypothesis fails.

### Sources and further reading

- S. Boyd and L. Vandenberghe, [*Convex Optimization*, Chapter 10](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), for KKT linear systems and their regularity in equality-constrained Newton methods.
- [Optimization for Decision Science: Constraint Qualifications](https://ndcbe.github.io/optimization/notebooks/7/constraint-qualifications/), for the relevance of LICQ and active-set regularity.
- A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, and J. Z. Kolter, [*Differentiable Convex Optimization Layers*](https://locuslab.github.io/2019-10-28-cvxpylayers/), for implicit differentiation through optimality conditions and applications to learning systems.
- [Wikipedia: Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem) and [Envelope theorem](https://en.wikipedia.org/wiki/Envelope_theorem), for introductory statements and terminology.

*Teaching connections:* `multivariable-calculus:027000` develops tangent second-order conditions; `multivariable-calculus:028000` supplies the active-set caveats; `multivariable-calculus:029000` derives the same KKT matrix as a Newton correction; `optimization-duality:011000` develops broader robust and sensitivity problems.
