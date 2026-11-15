# 003000 — Conditioning: When the Problem Amplifies Small Errors

**Track:** Numerical Analysis and Reliable Computation. **Background:** derivatives, basic algebra; matrix norms introduced from first principles. **Purpose:** separate the unavoidable sensitivity of a mathematical problem from numerical errors made by an implementation.

<!-- BEGIN SPOKEN LECTURE -->

# Conditioning: When the Problem Amplifies Small Errors

There are two ways for a calculation to disappoint us. We might use a poor algorithm on a perfectly reasonable question. Or the question itself might be so sensitive that tiny changes in what we know produce enormous changes in the answer. Those are different failures. The first invites a better algorithm. The second may require better information, a different formulation, or a more modest conclusion.

Conditioning is the mathematical study of the second issue. We freeze the algorithm entirely. Imagine that an oracle gives the exact answer to whatever problem we submit. We perturb the input slightly and ask how much the oracle's answer changes. If the answer barely changes, the problem is well-conditioned on that scale. If it changes enormously, it is ill-conditioned. Neither judgment depends on whether our computer uses three digits or three hundred.

The subtlety is that the scale matters. An absolute error of one second can be huge when measuring a microsecond and negligible when measuring a millennium. A meaningful condition number describes input and output perturbations relative to selected units or norms. There is no single unit-free measure of difficulty for every task.

## Subtraction as an experiment

Consider subtracting one quantity from another. If the inputs are five and four, their difference is one. A change of a hundredth in either input changes the answer by at most a few hundredths. But if the numbers are one point zero zero zero zero zero zero one and one, their difference is a ten-millionth. An error of a hundredth would swamp it. Even an error of a few parts in a hundred million may be significant relative to the difference.

For subtraction of positive nearly equal values, a standard relative condition number is the sum of the magnitudes of the two inputs, divided by the magnitude of their difference. This ratio grows when the denominator approaches zero. It is not saying that the hardware subtraction instruction is always inaccurate. Under suitable conditions, floating-point subtraction of close stored numbers can be exact. The sensitivity belongs to the *mathematical mapping from uncertain inputs to a difference*.

Suppose the inputs were measured rather than computed. If each was reported to seven significant digits, and their difference depended on the eighth digit, no rearrangement of subtraction can recover the missing measurement. By contrast, if the inputs were computed by formulas that introduced unnecessary rounding before subtraction, a reformulation might help. Conditioning tells us what the data permit; stability tells us what the algorithm preserves.

## The derivative is a local condition estimate

For a differentiable scalar function, the derivative measures how the output changes under a small input perturbation. Near a nonzero input x and nonzero output f of x, the magnitude of x times the derivative, divided by the magnitude of f of x, is a local relative condition number. For a sufficiently small relative input change, multiplying it by this condition number estimates the relative output change to first order.

Take the function that squares its input. Its derivative is twice the input. For nonzero x, the relative condition number is two. A one-percent change in the input produces approximately a two-percent change in its square. That is a moderate sensitivity. For the square-root function on positive inputs, the relative condition number is one half: a one-percent change in the input makes about half a percent change in the output, locally.

Now take the logarithm near one. The logarithm of one is zero. Relative output error becomes a poor measure there, and the relative condition number tends to infinity as the input approaches one. Yet the absolute derivative of the logarithm near one is close to one. An absolute condition measure says that small absolute input changes produce small absolute output changes. Neither story is a contradiction. They answer different questions.

A carefully specified accuracy requirement must choose a sensible scale before condition numbers become useful.

## The shape of a root matters

Suppose a root is defined implicitly as the solution of an equation. A small change to the equation's coefficients may move the root. If the graph crosses the horizontal axis steeply, the root often moves only a little. If it nearly touches the axis, the same perturbation can move the root a great deal.

For a simple root, the derivative of the function at the root is nonzero. A small change in the function's value typically moves the root by about that change divided by the derivative. If the derivative is tiny, the root can be sensitive. At a double root, the derivative vanishes, and the usual linear approximation breaks down.

Consider the family of equations saying that the square of the quantity x minus one equals a parameter epsilon. For positive epsilon, there are roots at one plus or minus the square root of epsilon. Their displacement from one scales like the square root of the parameter, not like the parameter itself. At epsilon zero, the root has multiplicity two. A perturbation of one millionth can shift a root by one thousandth. The square root makes the sensitivity visible.

This is why reporting a root solver's tiny residual without discussing root conditioning can be misleading. If the problem has a nearly multiple root, an apparently insignificant perturbation in the model may cause substantial uncertainty in the root location.

## Matrices make the same idea geometric

Now consider a system of simultaneous linear equations, written as a matrix times an unknown vector equals a given vector. Geometrically, the matrix maps space into space. If it strongly squeezes some directions, then reversing the mapping must magnify errors in those directions.

An invertible matrix has an inverse, so the exact solution is the inverse applied to the right-hand side. If the right-hand side changes by a small vector, the solution changes by the inverse applied to that perturbation. A large inverse norm means there are directions in which small input changes can yield large solution changes.

A common condition number is the matrix norm times the norm of its inverse. In the Euclidean norm it equals the ratio of the largest singular value to the smallest singular value. This connects conditioning to geometry: the matrix stretches one direction much more than another. Near singularity, its smallest singular value approaches zero and the condition number grows without bound.

Here is a two-equation example. The first equation says x plus y equals two. The second says x plus one point zero zero one times y equals two point zero zero one. The exact solution is x equals one, y equals one. Subtract the first equation from the second: one thousandth of y equals one thousandth. That subtraction exposes the fragility. If the second right-hand side were changed by one thousandth, y could change by one. It is not a failure of Gaussian elimination. The mathematical equations almost repeat the same information.

An ill-conditioned system can still be solved backward stably. The result is then the exact solution to a very nearby system. But that nearby system may have a substantially different solution. Backward stability is not a promise of small forward error.

## When the matrix itself is uncertain

So far we changed the right-hand side while keeping the matrix fixed. In an experiment, matrix entries may also be measurements. Suppose a matrix A is perturbed by a small matrix E. If A is invertible and the product of its inverse with E has norm strictly below one, then the perturbed matrix is also invertible. Why? We can factor it as A times the identity plus A inverse times E. The latter factor has an inverse given by a convergent geometric series, a matrix analogue of one over one minus a small number.

That observation gives a finite-perturbation bound: the solution change depends on both the relative right-hand-side error and the relative matrix error, multiplied by the condition number, and divided by a safety margin. As the relative matrix perturbation multiplied by the condition number approaches one, the denominator approaches zero. A tiny relative perturbation to an extremely ill-conditioned matrix can threaten invertibility itself.

This is a different conclusion from simply applying a first derivative formula. It explains why an uncertainty budget must consider how much data perturbation is actually permitted. Local sensitivity is a useful warning, but a certified range needs hypotheses that hold over the full uncertainty set.

## Local versus global sensitivity

A derivative gives only local information. If the input uncertainty is large enough to cross a singularity, switch branches, change the active constraints in an optimization problem, or alter the number of real roots, a linearized condition estimate may be disastrously optimistic.

For example, the function one divided by x is locally well-behaved at x equal one, but no fixed small-error claim can cover a range that includes zero. A formula may also have different output representations that make absolute or relative error more natural. Errors in probabilities near zero, in angles modulo a full turn, or in normalized eigenvectors require carefully chosen metrics.

The lesson is not that every problem should be assigned a single condition number. The lesson is to ask what perturbations are plausible, what output differences matter, and whether the solution mapping is stable over that set.

## A conditioning audit before computation

Before choosing an algorithm, define the input and output spaces. Identify the units or norms used to measure error. Decide whether the claim is local, based on derivatives and infinitesimal perturbations, or uniform over a finite uncertainty region. Check for singularities, near-multiple roots, cancellation, and nearly dependent equations. If a matrix is involved, estimate the scale of its smallest singular value or its inverse action, rather than inferring accuracy from a tiny residual alone.

And distinguish two legitimate conclusions. 'The algorithm is working as intended' is a statement about computation. 'The available data determine this answer to six digits' is a statement about the mathematical problem and the data. We can prove the former without being entitled to the latter.

Reliable numerical analysis treats conditioning as a property to understand, not an embarrassment to conceal. Sometimes a problem is ill-conditioned because the scientific question itself is underdetermined. In that situation, the most useful answer may be a sensitivity interval, a family of possible solutions, or a recommendation for a better measurement. That is a more honest mathematical result than a confident decimal string.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Scalar relative conditioning.** For differentiable \(f\) at \(x\ne0\) with \(f(x)\ne0\),
\[
\kappa_{\rm rel}(f,x)=\left|\frac{x f'(x)}{f(x)}\right|,\qquad
\frac{\Delta f}{f(x)}=\frac{x f'(x)}{f(x)}\frac{\Delta x}{x}+o(|\Delta x|)
\]
when \(\Delta x\to0\). The relative formula is not appropriate at zero inputs/outputs.

**Subtraction of two data values.** For \(f(a,b)=a-b\), with componentwise relative input perturbations \(|\Delta a|\le \epsilon|a|\), \(|\Delta b|\le\epsilon|b|\),
\[
\bigl|f(a+\Delta a,b+\Delta b)-f(a,b)\bigr|
 \le\epsilon(|a|+|b|), \quad
\kappa_{\rm rel}=\frac{|a|+|b|}{|a-b|}
\]
for \(a\ne b\).

**Simple roots and perturbations.** If \(F(r,t)=0\), \(F\) is \(C^1\) near \((r_0,t_0)\), and \(\partial_r F(r_0,t_0)\ne0\), the implicit function theorem gives \(dr/dt=-F_t/F_r\). At repeated roots this formula is unavailable.

**Matrix relative condition.** For nonsingular \(A\), the induced-norm condition number is \(\kappa(A)=\|A\|\|A^{-1}\|\). When \(A\) is fixed and only \(b\) changes,
\[
\frac{\|\Delta x\|}{\|x\|}\le\kappa(A)\frac{\|\Delta b\|}{\|b\|}, \quad Ax=b,\quad A(x+\Delta x)=b+\Delta b.
\]
In spectral norm, \(\kappa_2(A)=\sigma_{\max}(A)/\sigma_{\min}(A)\).

**Near dependent equations.** For \(\delta\ne0\), \(x+y=2\), \(x+(1+\delta)y=2+\delta\) has solution \((1,1)\). Perturb the second right-hand side by \(\delta\eta\); the solution becomes \((1-\eta,1+\eta)\). The input change has magnitude \(|\delta\eta|\), while the solution moves by \(|\eta|\) in each component.

### Exercises with answers

1. **Square root:** Find the local relative condition of \(f(x)=\sqrt{x}\) for \(x>0\). **Answer:** \(1/2\).
2. **Root sensitivity:** For \((r-1)^2=t\), how far can the real roots move when \(t\) changes from zero to \(10^{-6}\)? **Answer:** \(10^{-3}\), a square-root rather than linear response.
3. **Linear system:** Why can a tiny residual accompany a large solution error? **Answer:** Because \(\Delta x=A^{-1}r\); a large inverse norm amplifies residuals in sensitive directions.
4. **Zero output:** Why is relative condition unsuitable for \(f(x)=\log x\) near \(x=1\)? **Answer:** The output approaches zero, making relative output changes arbitrarily large while absolute changes remain controlled.

### References

- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, chapter 1.
- James Demmel, *Applied Numerical Linear Algebra*, chapter 2, conditioning and distance to ill-posedness.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra*, lectures on norms and condition numbers.
