# 004000 — Backward Error: Which Nearby Problem Did the Algorithm Solve?

**Track:** Numerical Analysis and Reliable Computation. **Background:** scalar equations, derivatives, simple matrices. **Purpose:** define backward error precisely, derive a useful linear-system formula, and compare algebraically equivalent but numerically different algorithms.

<!-- BEGIN SPOKEN LECTURE -->

# Backward Error: Which Nearby Problem Did the Algorithm Solve?

When a numerical algorithm returns a number, we usually ask how far it lies from the exact answer. That is forward error. But there is another question that is often easier to answer rigorously: for what nearby input would the returned number be *exactly right*?

This reversal is the idea of backward error. Instead of chasing an unknown exact output, we examine what small change to the problem would explain the observed output. James Wilkinson and the subsequent literature on numerical linear algebra made this viewpoint central to the design and analysis of reliable algorithms.

An excellent algorithm does not necessarily solve the specified problem exactly in finite arithmetic. It may solve a slightly perturbed problem exactly, in a mathematical accounting of rounding. If the perturbation is as small as the input data's representation errors, the algorithm has not added much avoidable error. Yet the result can still be far from the original exact solution when the problem is ill-conditioned. Backward stability and conditioning work together: one describes the algorithm, the other describes the problem.

## Reverse the map

Suppose a function maps an input x to a target y, and the algorithm produces y-hat. A backward error asks us to find a perturbation of x that makes y-hat equal the exact function evaluated at the perturbed input. There may be several such perturbations, so we measure the smallest one under a specified norm. Sometimes no exact preimage exists; the definition must acknowledge that possibility instead of pretending every output is backwards explainable.

For scalar problems with a nonzero input, we may divide the input perturbation by its size and get a relative backward error. For vector data, we need a norm or componentwise scaling rule. These choices matter. Changing a tiny coefficient by a hundred percent can be inexpensive in a global norm if another coefficient is huge. In applications where each coefficient carries its own meaning, componentwise backward error may be more honest.

We can see backward error without any sophisticated algorithm. Suppose we want to solve the equation x squared equals two and an iteration returns an approximation x-hat. It satisfies the *nearby equation* x squared equals x-hat squared exactly. The change in the right-hand side is the residual x-hat squared minus two. Relative to the specified input two, its magnitude is a simple backward-error measure. The forward error in x-hat is different: it depends on the slope of the squaring map near the root.

This example also shows why a residual is not automatically a backward error. To call a residual a backward error, we must say which input data are allowed to change and how those changes are scaled. The residual becomes a quantitative data perturbation only after that choice.

## A formula for linear systems

Consider a square invertible matrix A, a right-hand side b, and a computed candidate x-hat. Form the residual by subtracting A times x-hat from b. If we keep A fixed and permit the right-hand side to change, the candidate is *exactly* the solution of A times x-hat equals b minus the residual. So the absolute backward error in the right-hand side, in the chosen norm, is precisely the residual norm. That statement does not need an inverse or an estimate of the true solution.

If instead both the matrix and right-hand side may be perturbed, we can ask for the smallest normalized perturbations that make the computed vector exact. A standard normwise expression compares the residual norm to the sum of the matrix norm times the candidate norm and the right-hand-side norm. With the same relative allowance for perturbing A and b, that ratio is the smallest possible allowance under an induced matrix norm. For a nonzero candidate, it quantifies how little the input data must change to explain the computed answer.

But estimating forward error requires more. The difference between the candidate and the true solution equals the inverse matrix applied to the negative residual, up to the sign convention. Therefore its norm can be as large as the inverse norm times the residual norm. A small backward error paired with a huge condition number can still produce a substantial forward error.

This is one reason a solver library that reports a low residual has not, by that fact alone, certified highly accurate solution components.

## Stability is a family of claims

A backward-stable algorithm returns, for each admissible input, an exact result for slightly perturbed data, with perturbations bounded in the stipulated model. This is a strong property, not a synonym for 'the output looks plausible.' The perturbation bound may depend on problem size, pivot growth, and input scale.

Some algorithms are forward stable without satisfying the simplest backward-stability definition. Others are mixed stable, accounting for perturbations in input and output. A theorem about one algorithm and arithmetic model does not automatically hold for an arbitrary implementation with different rounding behavior, overflow, or underflow.

A realistic stability claim has hypotheses. For example, a bound derived under floating-point rounding to nearest and normal finite operations does not automatically cover a process that overflows. A guarantee for Gaussian elimination with partial pivoting commonly includes a factor associated with element growth; it is not an unconditional promise that every matrix receives the same tiny normwise backward error.

The words 'numerically stable' become useful only when the measured error, the input perturbation model, and the range of inputs are made clear.

## An algebraic expression that sabotages itself

Solve the quadratic equation x squared plus one hundred million times x plus one equals zero. The two roots are negative. One has magnitude approximately one hundred million; the other has magnitude approximately one hundred-millionth.

The usual quadratic formula asks us to subtract a square root extremely close to one hundred million from that same large quantity when computing the small root. In binary64 arithmetic, the subtraction can lose nearly all meaningful information. For this particular coefficient scale, the directly evaluated small-root numerator may round to zero. The resulting root is zero, even though the exact small root is nonzero.

The polynomial's two roots have a different relationship: their product equals the constant coefficient divided by the leading coefficient, here one. This provides a better route. Compute the large root using a *sum of like-signed magnitudes* that avoids cancellation. Then compute the small root by dividing their product, one, by the large root. The two expressions are algebraically equivalent, but the second avoids the dangerous subtraction for the small root.

If the coefficient of x has the opposite sign, choose the other sign in the quadratic formula for the large-magnitude root. A common implementation sets q to minus one half times b plus the sign of b times the square root of the discriminant; then the roots are q divided by a and c divided by q, with separate treatment when q or other quantities vanish. This is a method, not a universal formula to apply blindly at zero discriminant or with overflowed intermediate products.

The example teaches two things. First, exact algebraic equality does not imply equal numerical behavior. Second, good numerical design can exploit structure such as the product of polynomial roots to avoid subtracting almost equal quantities.

## Why a stable evaluation still needs a separate residual check

We should not conclude that every algebraic reformulation is automatically stable because one cancellation was removed. The large-root calculation in the quadratic example can still overflow if the coefficient b squared overflows when forming the discriminant. If the discriminant is close to zero, its subtraction of four a c from b squared may itself be sensitive. If the coefficients are on vastly different scales, intermediate quantities can underflow. A robust implementation may scale the coefficients, compute the discriminant more carefully, and branch on degenerate cases.

We can examine the computed roots independently. Substitute each one into the original polynomial and evaluate the residual with controlled rounding. Check their sum and product against the coefficient identities. These checks test consistency, not automatically forward accuracy: a nearly repeated root can move substantially under a small coefficient perturbation while preserving a tiny residual.

The engineering lesson is to seek a chain of guarantees rather than a magical stable expression. First understand the problem's conditioning. Then choose a method for which we can bound its arithmetic error. Finally check whether the returned value meets the user's requested notion of error. Each layer answers a different question.

## Backward stability and ill-conditioning are compatible

Return to a linear system whose equations are nearly redundant. A backward-stable solver can compute a result that exactly solves a system with coefficients altered only in tiny relative terms. If many nearby systems have widely varying exact solutions, the result still cannot be expected to pin down the answer to many digits. That is not an embarrassment or contradiction. It is the interaction of algorithmic stability with problem sensitivity.

Now imagine replacing the solver with a poorly designed one that introduces an avoidable perturbation much larger than input rounding. Even a well-conditioned system might then produce an inaccurate result. Conditioning cannot save an unstable algorithm, just as stability cannot turn ambiguous data into a precise answer.

A reliable report should establish both sides: what nearby problem was solved, and how different its exact answer can be from the original target.

## Reading a numerical certificate

A backward-error certificate should answer concrete questions. Which data may change? Matrix entries, the right-hand side, or both? Are the changes measured in an absolute norm, a global relative norm, or componentwise? Does the residual calculation itself have controlled rounding? Does the certificate require the matrix to be nonsingular? What condition information is needed to translate it into forward accuracy?

If you can answer these questions, a decimal output becomes a mathematical statement. It says not merely 'this is what the program printed,' but 'this vector solves a specified nearby problem, and here is how near.' That is the bridge between finite algorithms and exact mathematical models.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Backward error for \(y=f(x)\).** For \(x\ne0\), an input-relative backward error is
\[
\eta(\hat y;x,f)=\inf\left\{\frac{\|\Delta x\|}{\|x\|}: f(x+\Delta x)=\hat y\right\},
\]
with \(\eta=+\infty\) when no such \(\Delta x\) exists. Distinguish this from forward error \(\|\hat y-f(x)\|\).

**Linear-system residual and backward error.** For \(A\hat x\approx b\), let \(r=b-A\hat x\). The candidate exactly solves \(A\hat x=b-r\); if only \(b\) may vary, absolute backward error is \(\|r\|\). If both \(A\) and \(b\) may change under a common relative bound and induced norm, the normwise backward error is
\[
\eta=\frac{\|r\|}{\|A\|\|\hat x\|+\|b\|},
\]
provided the denominator is positive. A matching perturbation exists by a rank-one operator argument or by distributing the residual between \(\Delta A\hat x\) and \(\Delta b\).

**Residual-to-forward-error conversion.** With \(Ax_*=b\) and nonsingular \(A\),
\[
\hat x-x_*=-A^{-1}r,\quad
\|\hat x-x_*\|\le\|A^{-1}\|\|r\|,\quad
\frac{\|\hat x-x_*\|}{\|x_*\|}\le\kappa(A)\frac{\|r\|}{\|b\|}
\]
for nonzero \(b\) and \(x_*\). A computed residual needs its own rounding allowance for a rigorous certificate.

**Stable quadratic evaluation.** For \(ax^2+bx+c=0\), \(a\ne0\), \(D=b^2-4ac\ge0\), let
\[
q=-\frac12\left(b+\operatorname{sign}(b)\sqrt D\right),\qquad
x_1=q/a,\quad x_2=c/q.
\]
For \(b=0\), \(q=0\), or problematic discriminant evaluation, select a separately derived safe branch. The discriminant itself may need scaling or fused arithmetic to avoid spurious overflow/cancellation. For \((a,b,c)=(1,10^8,1)\), the roots are approximately \(-10^8\) and \(-10^{-8}\), with product 1.

### Exercises with answers

1. **Right-hand-side backward error:** For \(A\hat x=b-r\), what perturbation to \(b\) makes \(\hat x\) exact? **Answer:** \(\Delta b=-r\) under the convention \(r=b-A\hat x\), so \(A\hat x=b-r\). The absolute size is \(\|r\|\).
2. **Residual:** Why do residual norms not by themselves establish small forward error? **Answer:** The inverse matrix may amplify the residual by \(\|A^{-1}\|\).
3. **Quadratic:** Why compute the small root from the product of roots? **Answer:** It avoids subtracting large nearly equal values in the direct quadratic formula.
4. **Hypotheses:** Does a stability theorem under round-to-nearest automatically cover overflow? **Answer:** No. The arithmetic model must cover the actual operations and exceptional cases.

### References

- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, chapters 1–2.
- James Demmel, *Applied Numerical Linear Algebra*, chapters 1–2.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, lectures 12–15 and 20–22.
