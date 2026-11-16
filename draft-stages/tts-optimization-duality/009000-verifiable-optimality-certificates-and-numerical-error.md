# 009000 — Verifiable Optimization Certificates: From Solver Output to Proof

**Track:** Optimization, Convexity, and Duality. **Background:** linear and semidefinite programming, weak duality, and numerical conditioning. **Central question:** when does a numerical optimum become an independently checkable mathematical claim?

<!-- BEGIN SPOKEN LECTURE -->

# Verifiable Optimization Certificates: From Solver Output to Proof

An optimization solver can print the word optimal next to a number with many decimal digits. That tells us something about what the solver computed under its tolerances and assumptions. It does not, by itself, provide a proof that no feasible point has a better objective value.

A stronger result is a certificate: a collection of objects that a separate, relatively simple checker can inspect and use to establish a mathematical bound. Convex duality provides a natural source of certificates. Numerical analysis tells us when their verification must account for rounding, constraint residuals, and the conditioning of the problem.

## Upper and lower bounds meet

Consider a minimization problem. Any feasible candidate gives an upper bound on the optimum, because the optimum cannot be worse than a candidate. A valid dual-feasible point gives a lower bound by weak duality. Put the two together, and the true optimum lies in an interval.

If the bounds coincide, the candidate is optimal. If they differ by a small amount, we have a quantitative optimality gap. This conclusion does not require us to trust the internal iteration history of a solver. We need only verify feasibility of the candidate, feasibility of the dual object, and the objective values.

For linear programming, this can become an exact arithmetic proof. Suppose the objective is to minimize x plus y, where both variables are nonnegative, and x plus twice y must be at least four. The feasible point x equals zero, y equals two has cost two.

Now multiply the constraint x plus twice y at least four by one half. We obtain half x plus y at least two. Since x is nonnegative, x plus y is at least half x plus y. Therefore every feasible objective is at least two. We have a lower bound of two and a feasible point with objective two. The optimum is exactly two.

This proof is tiny, but it contains the essence of dual certification. The half is a nonnegative multiplier on the inequality. Its combination of constraints is dominated by the objective coefficients. The resulting weighted constraint supplies a lower bound equal to the candidate's cost.

## Separate discovery from verification

A numerical optimizer might discover the candidate and its dual multiplier using thousands of iterations, matrix factorizations, or heuristic choices. The checker only needs to verify a handful of inequalities. The process that finds a certificate can be complex; the process that validates it can be simple.

For an exact rational linear program, we can represent the proposed primal and dual variables as rational numbers, then check the linear inequalities and equalities with exact integer arithmetic after clearing denominators. If those checks pass, weak duality gives an exact interval for the optimum. This is the useful distinction between a numerical guess and a proof-carrying result.

But many solvers return floating-point numbers. A reported zero residual may mean a quantity was smaller than a tolerance, not that it was mathematically zero. A variable printed as zero may actually be slightly negative. And a dual inequality evaluated with rounding may have the opposite sign from its exact mathematical value.

A numerical certificate is therefore not complete until we understand how feasibility is checked. We can sometimes round solver output to rational numbers and verify those numbers exactly. In other problems we use interval arithmetic with outward rounding to enclose every relevant expression. If the enclosure proves an inequality has the required sign, the certificate is established. If the interval crosses zero, the checker must report uncertainty, refine the computation, or find a different certificate. It must not quietly assume the sign.

## Infeasibility can also be certified

Optimality is not the only claim worth checking. Suppose a system of linear equations asks for a nonnegative vector x satisfying A times x equals b. An appropriate vector y can prove that no such x exists.

Specifically, if every component of A transposed times y is nonnegative but the dot product of b with y is negative, then any feasible nonnegative x would give a contradiction. On one hand, the dot product b with y equals x dotted with A transposed y, which would be nonnegative. On the other hand, the proposed certificate says it is negative.

For the simplest example, suppose x must be nonnegative but also equal negative one. Take the single equation x equals negative one and the multiplier y equal one. The coefficient side is nonnegative while the right-hand side multiplier is negative, so infeasibility follows immediately.

Such a witness is an instance of Farkas' lemma. The general lesson is that a solver may report no solution, but a certificate makes the absence of solutions a verifiable algebraic statement.

## Positive semidefinite certificates

Semidefinite programming replaces scalar inequalities with constraints that matrices are positive semidefinite. The duality principle is similar, but a checker must verify that certain symmetric matrices really have no negative quadratic directions.

For instance, the matrix with diagonal entries one and off-diagonal entries negative one is positive semidefinite. We can verify it exactly by observing that its quadratic form on a vector with coordinates a and b equals the square of a minus b. Every real square is nonnegative. This is a proof, not a floating-point eigenvalue estimate.

For larger matrices, one might verify an exact factorization or use carefully bounded spectral estimates. Positive definiteness, where all eigenvalues are strictly positive, can be numerically easier to certify when there is a known gap above zero. Semidefiniteness on the boundary is harder: an eigenvalue very close to zero may be slightly positive or slightly negative, and ordinary floating-point rounding can conceal the distinction.

Conic duality also requires proper attention to primal and dual feasibility. A tiny reported duality gap does not establish an optimum if either proposed point violates its constraints. A solver may use scaled residuals and stopping tolerances, while a mathematical claim concerns the original unscaled problem. Verification must return to that original formulation.

## Does a narrow objective gap locate the optimizer?

Even a rigorous objective-value interval does not always imply that the optimizer's coordinates are accurately determined. A nearly flat objective may have many widely separated points with almost identical cost. Strong convexity is one condition that connects objective error to distance.

If a differentiable objective is strongly convex with positive parameter mu, then a feasible candidate whose objective value is at most delta above the optimum lies within a distance proportional to the square root of delta divided by mu from the unique optimizer, under the standard convex-feasible-set hypotheses. A small mu makes this bound weak. Without an appropriate curvature or error-bound assumption, a tiny duality gap alone gives no comparable distance guarantee.

This distinction echoes condition numbers in numerical linear algebra. One must ask what has actually been certified: the value of the optimum, feasibility of the point, a distance to a minimizer, or sensitivity to perturbations in the problem data. Those are different mathematical conclusions.

## A trustworthy workflow

The strongest practical pattern separates the roles of discovery and proof. First use an effective numerical solver to find promising primal and dual candidates. Then export a well-specified certificate containing the original problem data, candidate variables, constraints, objective values, and precision assumptions. Finally run an independent checker that verifies the relevant inequalities in exact arithmetic or with justified enclosures.

If verification fails, that does not always mean the proposed solution is poor. It may mean that the reported precision is insufficient or that the certificate needs repair. Conversely, successful verification certifies the stated mathematical model, not automatically the accuracy of the model relative to the physical or economic system it represents.

Optimization becomes much more reliable when we ask not merely what number a solver printed, but what mathematical evidence the number came with. A certificate converts a complicated computation into a simple claim another system can check. The boundary between heuristic numerical confidence and proof is where feasible bounds and justified arithmetic meet.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Primal and dual LP.** Consider
\[
\begin{aligned}
(P)\quad &\min_{x\ge0} c^Tx\quad\text{subject to }Ax\ge b,\\
(D)\quad &\max_{\lambda\ge0} b^T\lambda\quad\text{subject to }A^T\lambda\le c.
\end{aligned}
\]
For any primal-feasible \(x\) and dual-feasible \(\lambda\),
\[
b^T\lambda\le\lambda^TAx=x^TA^T\lambda\le c^Tx.
\]
Thus \(b^T\lambda\le p^*\le c^Tx\), with a certified gap \(c^Tx-b^T\lambda\) when all feasibility and arithmetic checks are rigorous.

**Exact worked certificate.** Let \(c=(1,1)\), \(A=(1,2)\), \(b=4\), \(x=(0,2)\), \(\lambda=1/2\). Then \(Ax=4\), \(x\ge0\); \(A^T\lambda=(1/2,1)\le c\), \(\lambda\ge0\); both objectives are \(2\). The optimum is exactly \(2\).

**Farkas-type infeasibility.** If \(Ax=b\), \(x\ge0\) and some \(y\) satisfies \(A^Ty\ge0\) and \(b^Ty<0\), then feasibility is impossible, since \(b^Ty=x^TA^Ty\ge0\). Example: \(A=(1)\), \(b=-1\), \(y=1\).

**PSD witness.** \(S=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\succeq0\) because \((a,b)S(a,b)^T=(a-b)^2\ge0\). This is an exact nonnegativity certificate without approximate eigenvalues.

**Objective vs solution error.** If \(f\) is \(\mu\)-strongly convex on a convex feasible domain, \(\mu>0\), with minimizer \(x^*\), then \(f(x)-f(x^*)\ge\frac\mu2\|x-x^*\|^2\). A rigorous gap bound \(f(x)-f(x^*)\le\delta\) gives \(\|x-x^*\|\le\sqrt{2\delta/\mu}\). Without suitable curvature, objective accuracy need not imply location accuracy.

### Exercises with answers

1. Verify \(x=(0,2)\), \(\lambda=1/2\) in the worked LP. **Answer:** all sign and linear constraints hold exactly, both objective values equal two.
2. If a duality gap is numerically tiny but the dual multiplier violates feasibility, is it a proof of optimality? **No:** weak duality applies to feasible certificates.
3. What proves a PSD matrix \(S\succeq0\) exactly? **Answer:** for example, a verified decomposition \(S=B^TB\) over exact arithmetic, or another justified positivity argument.
4. Does a gap of \(10^{-6}\) guarantee the optimizer is within \(10^{-6}\) in Euclidean distance? **No:** that requires additional quantitative assumptions, such as strong convexity with known parameter.

### Reading and source notes

- Stephen Boyd and Lieven Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/), Chapter 5 on dual lower bounds, certificates, and suboptimality gaps.
- JuMP documentation, [Tolerances and numerical issues](https://jump.dev/JuMP.jl/stable/tutorials/getting_started/tolerances/), solver feasibility tolerances and reporting.
