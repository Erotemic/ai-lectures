# Smoothing a Sharp Transport Plan: Entropy and Sinkhorn Scaling

<!-- BEGIN SPOKEN LECTURE -->

Exact optimal transport has a kind of sharpness. The cheapest plan often concentrates mass along a small collection of routes, leaving many cells at zero. This is satisfying as an optimization result, but it can make numerical computation demanding. The full transport linear program grows with the product of the numbers of source and destination points. Some applications need thousands of points on each side, or transport costs nested inside a larger learning problem. An exact sparse answer may be more than the calculation can afford.

One possible compromise is to slightly reward the use of a spread-out plan. We continue to pay for transporting mass, but add a smooth penalty that prefers a distribution of flows with more entropy. The result is entropically regularized optimal transport. Its optimizer has a special multiplicative form, and that form leads to an algorithm called Sinkhorn scaling.

The algorithm is simple to state: repeatedly rescale rows and columns of a positive matrix until their sums match the requested margins. The deeper story is why that apparently mechanical operation solves a well-defined optimization problem, what it sacrifices compared with exact transport, and how we know when the numerical iteration is trustworthy.

## A two-by-two transport problem

Consider two source points and two destination points, each with one half of the mass. Suppose staying in the corresponding position costs zero, while crossing to the other position costs one. The cost matrix has zeros on the diagonal and ones off the diagonal. Without any regularization, the best coupling is obvious. Put one half on each diagonal entry and zero on both off-diagonal entries. The total transport cost is zero.

A general coupling with these margins must have diagonal entries x and off-diagonal entries one half minus x. The permitted range is zero through one half. The unregularized transport cost is twice one half minus x, or one minus two x. We minimize by making x equal to one half. In this exact optimum, none of the mass crosses.

Now modify the objective. Add a positive parameter epsilon times the sum over all cells of P times the logarithm of P, using the usual convention that zero times log zero is zero. Since these terms are negative for probabilities strictly between zero and one, minimizing this extra term tends to favor greater entropy. More precisely, the negative of that sum is the Shannon entropy of the joint coupling. We are minimizing cost minus epsilon times entropy.

In the two-by-two case, the new objective is one minus two x plus two epsilon times x log x plus two epsilon times one half minus x times the log of one half minus x. At an interior optimum, differentiate with respect to x. The derivative of the transport part is negative two. The derivative of the entropy part is two epsilon times the logarithm of x divided by one half minus x. Set the sum to zero. We get that the ratio of diagonal mass to off-diagonal mass equals the exponential of one over epsilon.

At epsilon equal to one, the diagonal mass is approximately zero point three six five five, and each off-diagonal entry is about zero point one three four five. There is no longer a perfectly sharp match. Some mass now takes the more expensive routes. The *transport portion* of the new plan's cost is about zero point two six nine, even though the exact, unregularized transport cost was zero. This is not a numerical failure. It is the intended tradeoff introduced by regularization.

As epsilon approaches zero, the ratio between diagonal and off-diagonal mass becomes very large, and the regularized plan approaches the exact diagonal plan. As epsilon grows, the penalty for low entropy dominates, and the plan approaches the independent coupling with a quarter of the mass in every cell. The same two margins and the same ground costs lead to a family of solutions indexed by the regularization strength.

It is important to say which number an implementation returns. It might return the original transport cost of the regularized plan, or the full regularized objective including entropy, or some normalization of that objective. These are not interchangeable quantities. Even two software packages using the word 'Sinkhorn' can report different objective conventions.

## The exponential kernel

Why does entropy lead to repeated scaling? Write the finite regularized objective as the sum of shipping cost and epsilon times the sum of P log P. Add Lagrange multipliers for the required row and column sums. At an interior optimum, the derivative with respect to the entry P-i-j must vanish. It says that cost C-i-j plus epsilon times log P-i-j plus epsilon, minus the source potential and destination potential, equals zero.

Rearrange that equation. The optimum entry has the form of a source factor times the exponential of negative cost divided by epsilon times a destination factor. The extra constant from differentiating P log P can be absorbed into the factors. Define the Gibbs kernel K by K-i-j equal to the exponential of negative C-i-j over epsilon. Then the whole optimal coupling has the form diagonal-u times K times diagonal-v, for positive vectors u and v.

The remaining task is to find the scaling factors so that the row sums equal the source weights and the column sums equal the destination weights. If the current destination factors are fixed, each source factor should equal the desired source mass divided by the corresponding row sum of K weighted by those destination factors. With the source factors fixed, each destination factor should equal the desired destination mass divided by its corresponding weighted column sum.

These are the two alternating updates in Sinkhorn's algorithm. Start with positive destination factors, rescale all rows, rescale all columns, and repeat. After one row update the rows are correct, but the columns may have changed. After the next column update the columns are correct, but the rows may have changed. With a strictly positive kernel and positive margins, the classical matrix-scaling theory establishes convergence of this alternating process to the required scaling, up to the familiar global factor ambiguity.

The two-by-two example makes the formula visible. With epsilon one, the kernel is one on the diagonal and the exponential of negative one off diagonal. Because the two margins are symmetric, the required plan is a normalized copy of this kernel. Each row must sum to one half, so divide every kernel entry by twice one plus the exponential of negative one. The diagonal entries become about zero point three six five five; the off-diagonal entries about zero point one three four five. These match the calculus derivation exactly.

The numerical operation at each iteration is dominated by multiplying a matrix by a vector, which takes work proportional to the number of stored entries for a dense matrix. That is attractive compared with a general-purpose linear-program solve on large dense transport tables. But one Sinkhorn iteration is not a complete algorithmic cost bound. The number of iterations required for a requested accuracy depends on the instance, regularization strength, and stopping rule. Small epsilon makes the exponential kernel more sharply peaked and can create severe numerical conditioning problems.

## Two conventions for the entropy term

There is a subtle bookkeeping issue. Instead of adding the negative entropy term, many authors add epsilon times the Kullback–Leibler divergence from P to the independent coupling formed by the product of the two margins. With fixed, positive margins, these two regularizers differ by a constant independent of P. Therefore they produce the same minimizing coupling. Their reported objective values differ by that constant.

This equivalence is useful because the KL form has an information-theoretic interpretation. It penalizes a coupling for departing from independent pairing. The parameter epsilon tunes the preference for independence relative to transport cost. The entropy form emphasizes the amount of spread in the joint table. Both lead to the same scaling equations in the strictly positive finite setting, but care is required with zero marginals and with implementation-specific normalizations.

The corresponding dual problem is smooth, with exponentials replacing the hard inequalities of unregularized Kantorovich duality. The source and destination factors can be interpreted as exponentials of scaled dual potentials. The additive freedom in the ordinary transport potentials becomes a multiplicative freedom in u and v: multiply one scaling vector by a constant and divide the other by the same constant, leaving the plan unchanged.

The plan for positive margins and finite costs has positive entries under strictly positive epsilon, so the exact zeros in a sharp linear-program solution have disappeared. This may make derivatives with respect to inputs easier to handle. But the regularized optimizer is not an optimal coupling for the original unregularized problem except in special cases. Regularized correctness and unregularized correctness are different proof obligations.

## Numerical stability and what can be certified

The exponential kernel contains entries of the form exponential of negative cost over epsilon. If a cost is large relative to epsilon, the entry may underflow to zero in floating-point arithmetic. That is dangerous: a theoretically positive kernel may become a numerically sparse matrix with missing connections. Some implementations therefore work in the logarithmic domain, using stable log-sum-exp operations and dual potentials rather than forming all tiny exponentials directly. Others decrease epsilon gradually, using a previous solution to initialize the next computation.

Stopping also needs thought. A small change in scaling factors does not always certify a small error in the transport objective. A reported plan should be checked for marginal residuals, nonnegativity, and an appropriate primal-dual gap or regularized optimality residual when these are available. The distinction between satisfying constraints approximately and optimizing the objective approximately is the same one encountered in exact linear programming, now with numerical tolerances attached.

There is a further semantic issue. The optimal *regularized cost* of transporting a measure to itself can be positive when expressed as the transport portion of the regularized plan, because the smoothed optimizer need not stay entirely on zero-cost diagonal entries. Thus it is generally wrong to call the raw entropic transport objective a metric on probability distributions. A commonly used correction, the Sinkhorn divergence, subtracts half the self-transport regularized cost of each input from the cross-transport cost, using a consistent objective convention. Under suitable hypotheses it removes the self-bias and defines a useful nonnegative divergence; one should not automatically assume it satisfies the triangle inequality.

The bias is not merely an abstract warning. Our two-point example has zero exact self-transport cost but a positive transport component after smoothing. If we compare two datasets with a regularized transport quantity, the choice of epsilon influences both numerical effort and the meaning of the resulting score.

## The bargain we made

Regularization trades one kind of difficulty for another. A sharp linear-programming optimum may be expensive to compute but has a clean complementary-slackness certificate. Adding entropy creates a smooth, unique plan in the positive finite setting and exposes the multiplicative matrix structure that Sinkhorn scaling can exploit. But the plan now spends mass on routes that exact transport might never use, and the method introduces regularization bias and numerical conditioning questions.

The correct mathematical statement is not that Sinkhorn magically solves the original transport problem quickly and exactly. It efficiently computes a different, nearby optimization problem, and the relationship to the unregularized problem becomes more faithful as epsilon decreases, subject to numerical and computational limits.

This is a useful pattern far beyond transport. Smoothing can turn a difficult combinatorial choice into a differentiable optimization problem, sometimes with an algorithm whose updates are surprisingly simple. The proof begins by identifying the precise objective being solved. The implementation must then preserve its marginal constraints and numerical meaning. Only after both are clear can we decide whether the approximation serves the application.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For strictly positive probability vectors \(a,b\), finite C, and \(\varepsilon>0\), entropic OT minimizes
\[
J_\varepsilon(P)=\langle C,P\rangle+\varepsilon\sum_{ij}P_{ij}\log P_{ij},\qquad P\in\Pi(a,b),
\]
using \(0\log0=0\). The optimizer is unique and has form \(P^*=\operatorname{diag}(u)K\operatorname{diag}(v)\), where \(K_{ij}=\exp(-C_{ij}/\varepsilon)\). Sinkhorn updates are
\[
u\leftarrow a/(Kv),\qquad v\leftarrow b/(K^Tu)
\]
(componentwise division). Work per dense iteration is \(O(mn)\), not a uniform guarantee on iterations required for a target precision.

**Explicit solution.** For \(a=b=(1/2,1/2)\), \(C=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), all couplings are \(\left(\begin{smallmatrix}x&1/2-x\\1/2-x&x\end{smallmatrix}\right)\). Optimizing yields \(x/(1/2-x)=e^{1/\varepsilon}\), hence
\[
x=\frac{1}{2(1+e^{-1/\varepsilon})},\quad
1/2-x=\frac{e^{-1/\varepsilon}}{2(1+e^{-1/\varepsilon})}.
\]
At \(\varepsilon=1\), \(x\approx0.365529\) and the unregularized transport component is \(1-2x\approx0.268941\). As \(\varepsilon\to0\), the plan approaches the diagonal coupling; as \(\varepsilon\to\infty\), it approaches \(ab^T\).

For fixed marginals, \(\mathrm{KL}(P\Vert ab^T)=\sum_{ij}P_{ij}\log P_{ij}-\sum_i a_i\log a_i-\sum_jb_j\log b_j\), so replacing negative entropy with KL changes the objective by a constant but not its optimizer. Definitions of software-reported loss must still be checked.

**Exercises with solutions.** (1) What does large epsilon do in the two-point example? *It drives the plan toward the independent coupling with all entries one quarter.* (2) Why can one scaling vector be multiplied by k and the other divided by k? *Their product in each plan cell is unchanged.* (3) Does small marginal error alone prove small objective error? *No; primal feasibility and objective optimality are distinct numerical assertions.*

### Reading

- Marco Cuturi, *Sinkhorn Distances: Lightspeed Computation of Optimal Transport* (NeurIPS 2013): https://mlanthology.org/neurips/2013/cuturi2013neurips-sinkhorn/
- Peyré and Cuturi, *Computational Optimal Transport* (2019): https://research.google/pubs/computational-optimal-transport/
- POT quickstart and solver-convention notes: https://pythonot.github.io/quickstart.html
