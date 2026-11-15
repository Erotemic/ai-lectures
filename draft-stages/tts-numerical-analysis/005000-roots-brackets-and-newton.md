# 005000 — Finding Roots: Brackets, Newton's Method, and Honest Stopping Rules

**Track:** Numerical Analysis and Reliable Computation. **Background:** continuity, derivatives, and arithmetic. **Purpose:** distinguish guaranteed enclosures from fast local convergence, and justify stopping conditions rather than merely observing iterates.

<!-- BEGIN SPOKEN LECTURE -->

# Finding Roots: Brackets, Newton's Method, and Honest Stopping Rules

Suppose an equation has a root and no formula you can write down for it. You can still find the root numerically, but the phrase 'find the root' hides at least three different tasks. First, establish that some root exists. Second, construct a sequence of approximations. Third, decide when the approximation is sufficiently accurate. The third task is not a clerical step after the algorithm. It is part of the mathematics.

Root finding provides a compact laboratory for numerical reasoning. A very safe method can be slow. A very fast method can converge to the wrong place or fail outright. A small equation residual can be misleading near a multiple root. And finite arithmetic can invalidate a sign test unless we pay attention to how the function was evaluated.

Let us look at what each method actually guarantees.

## A root held between two numbers

The simplest reliable idea uses continuity. If a continuous real-valued function is negative at one endpoint of an interval and positive at the other, the Intermediate Value Theorem guarantees at least one root between them. We do not need a formula for the root. We need only continuity and trustworthy endpoint signs.

For the equation x squared equals two, start with the interval from one to two. At one, x squared minus two is negative. At two it is positive. So a root lies somewhere inside.

Now split the interval at its midpoint, one point five. Its square is two point two five, above two, so the root lies in the lower half, from one to one point five. Split again. At one point two five the square is one point five six two five, below two, so the root lies in the upper half, from one point two five to one point five. Repeat.

This method, bisection, has an invariant: the retained interval brackets a root. Every step halves the interval length. If the original width is one, after ten successful halvings its width is one divided by one thousand twenty-four. The midpoint differs from at least one bracketed root by no more than half that width. Unlike a vague convergence graph, this is a certified absolute-error statement, provided the sign decisions and arithmetic operations preserve the bracket.

Bisection does not claim to find every root. A function that merely touches zero without changing sign may elude it. Nor does a sign change prove there is only one root in the interval. We can add monotonicity to guarantee uniqueness, but the basic method does not require it.

## What can go wrong in floating arithmetic?

A textbook often treats midpoint formation as exact. A computer cannot. If the endpoints are very large, evaluating their sum before halving might overflow, even though their midpoint is representable. A safer expression is a plus half of b minus a, with further precautions where subtraction may overflow or where the interval crosses extreme scales.

As the bracket becomes very narrow, its midpoint may round to one of the existing endpoints. Then there is no new representable floating-point number strictly between them. An implementation must recognize this and stop or use a more precise representation. Otherwise it may repeat the same step forever.

More seriously, evaluating the function with ordinary floating-point arithmetic does not automatically determine its exact sign. Near a root, cancellation may make a computed value zero or give the wrong sign for the mathematical function. If a verified enclosure is required, evaluate signs with controlled error, exact arithmetic when available, or interval arithmetic whose bounds enclose the true function value.

A bracket theorem about exact real numbers is not, by itself, a proof that a particular machine program preserves the bracket.

## Tangent lines as a root-finding engine

Bisection divides intervals blindly. Newton's method uses the local slope of the function. At a current guess, replace the graph by its tangent line, and take the point where that line crosses zero as the next guess. In algebra, subtract the function value divided by the derivative from the current estimate.

For x squared minus two, this produces a beautiful averaging formula: take the current positive guess, add two divided by that guess, and divide by two. Starting at one point five, the next value is approximately one point four one six six seven. The next is approximately one point four one four two one five seven. Another iteration is accurate to many more digits.

Why is Newton so much faster in this example? Near a simple root, if the function has a sufficiently regular derivative and the initial guess is close enough, the error after a Newton step is proportional to the *square* of the previous error. The number of correct digits roughly doubles once the iteration reaches this local regime. This is called local quadratic convergence. It is a theorem with hypotheses, not a guarantee for arbitrary starting points.

Consider a function whose derivative is zero at your starting guess. The Newton formula would require division by zero. Consider one whose tangent happens to cross the axis far outside the region where the original model is valid. A Newton step can leap into an irrelevant region. Some functions make Newton iterates cycle, and a function with a multiple root commonly loses quadratic convergence under ordinary Newton iteration.

A fast sequence is wonderful when it works, but speed must not be confused with certification.

## Another route: avoid derivatives, but not assumptions

Newton uses a derivative to build a tangent. The secant method estimates that slope from two recent function values, then takes the zero of the resulting secant line. This can be useful when derivatives are expensive or unavailable. Near a simple root, under regularity assumptions and good initial guesses, it converges faster than linear but generally slower than Newton's quadratic rate. Like Newton, it is not globally guaranteed to find a desired root from arbitrary guesses.

Fixed-point iteration offers a broader viewpoint. Rearrange an equation as x equals a function of x, then repeatedly apply that function. If the rearranged function is a contraction on a complete interval that maps into itself, the contraction theorem proves existence, uniqueness, and convergence. Another rearrangement of the *same equation* can fail to be contractive and drive the iteration away. In exact algebra the rearrangements are equivalent; as algorithms they behave differently.

For example, solving x squared equals two by iterating x becomes two divided by x is a poor stand-alone idea: it jumps between the starting guess and two divided by that guess forever, unless the guess was already the correct square root. Averaging x with two divided by x produces Newton's convergent step from suitable positive guesses. The transformation, not just the equation, determines the iteration's dynamics.

## Why multiple roots resist naïve tests

Take the function that squares x minus one. Its root is one, but the graph merely touches the horizontal axis there. Starting from a point near one, Newton's method moves halfway toward the root at each step. That is linear convergence, not the quadratic convergence we saw for the square root of two.

Suppose the current x is one point zero zero one. The error is one thousandth, but the function residual is one millionth. If a program stops whenever the residual drops below one millionth, the reported root might be farther away than a user who interprets that threshold as an error tolerance expects.

To convert a residual to a root error, we need slope information. If the derivative does not vanish and stays at least some positive magnitude throughout a verified bracket, the Mean Value Theorem gives a bound: root error is no more than residual magnitude divided by that derivative lower bound. Near a multiple root, there is no such positive bound uniform around the root.

This is not an argument against residuals. It is an argument for interpreting them correctly.

## A hybrid method combines strengths

Imagine starting with a valid bracket and using Newton steps whenever they fall safely within it and produce progress. If a Newton step would leave the interval or violate a safeguard, use bisection instead. Each successful sign evaluation updates the bracket, so we retain a global guarantee of containment while often enjoying fast local convergence.

There are many versions of safeguarded Newton and Brent-style methods. Their details differ, but the design principle is the same: allow a fast local model to accelerate a method with a robust global invariant.

A numerical root solver should tell us whether it has found a sign-changing bracket, whether it assumes a unique or simple root, whether derivative information is trustworthy, and what its stopping status means. 'Maximum iterations reached' is not the same as 'desired tolerance certified.' Nor is 'the last two iterates happened to agree' a proof of convergence.

## How to choose a stopping rule

A good rule depends on the contract. If we need a guaranteed absolute error for a continuous scalar function, bracket width is natural. If we need the function value to satisfy a physical balance law to an acceptable residual, a residual criterion may be the right target, even if root location remains uncertain. If we are solving a system, a backward-error estimate and an appropriate condition estimate may give the most meaningful combined statement.

A relative root error near zero is problematic; use an absolute scale or a mixed criterion. Termination can also occur because floating-point resolution has been exhausted, a derivative is too small, the function cannot be evaluated reliably, or the algorithm left its assumptions. These deserve distinct statuses rather than a generic success flag.

For the square root of two, a bracket that has been narrowed to less than one millionth gives a straightforward enclosure. We might take Newton steps to reach that bracket quickly, but the certificate comes from the bracket. If accurate digits matter, the proof of the enclosure matters more than how impressive the iteration history looks.

## The essential distinction

Root finding is not just the act of pushing a number toward zero. It is the construction of a relationship between approximate computation and the exact zeros of a function. Bisection provides a geometric enclosure when continuity and signs cooperate. Newton provides rapid local improvement when derivatives and initial conditions cooperate. Error bounds explain which conclusions the returned approximation supports.

Choosing a method is choosing a balance between assumptions, speed, and certainty. Making the assumptions explicit is how a numerical result becomes trustworthy.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Bisection guarantee.** If \(f\) is continuous on \([a_0,b_0]\) and \(f(a_0)f(b_0)<0\), after \(n\) exact sign-preserving bisections, the bracket width is \((b_0-a_0)/2^n\). Its midpoint \(m_n\) lies within
\[
|m_n-r|\le (b_0-a_0)/2^{n+1}
\]
of at least one root \(r\) in the retained bracket. A monotonicity assumption is needed for uniqueness, not existence.

**Newton iteration and local quadratic error.** For \(f\in C^2\), \(f(r)=0\), \(f'(r)\ne0\), and iterates in a neighborhood where \(|f'|\ge m>0\), \(|f''|\le M\),
\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)},\qquad
|x_{n+1}-r|\le \frac{M}{2m}|x_n-r|^2.
\]
This estimate uses Taylor's theorem with a remainder and a nonzero derivative at the current iterate.

**Example:** \(f(x)=x^2-2\) yields \(x_{n+1}=(x_n+2/x_n)/2\). With \(x_0=3/2\), \(x_1=17/12\), \(x_2=577/408\), and \(x_3=665857/470832\).

**Multiple root:** \(f(x)=(x-1)^2\) gives \(x_{n+1}=(x_n+1)/2\) for \(x_n\ne1\), so \(|x_{n+1}-1|=|x_n-1|/2\). The residual is the square of forward error.

**Certificate from a derivative bound.** If \(r,\hat x\in I\), \(f(r)=0\), \(f\in C^1(I)\), and \(|f'|\ge m>0\) on \(I\), then \(|\hat x-r|\le |f(\hat x)|/m\).

### Exercises with answers

1. **Bisection:** How many halvings of \([1,2]\) make the midpoint's worst-case absolute root error at most \(2^{-11}\)? **Answer:** Ten.
2. **Multiple roots:** Why is a residual of \(10^{-12}\) not a \(10^{-12}\) root error for \(f(x)=(x-1)^2\)? **Answer:** The error can be \(10^{-6}\).
3. **Newton:** What goes wrong when \(f'(x_n)=0\)? **Answer:** The tangent-line update is undefined; safeguarded methods must use a different step.
4. **Hardware:** Why might an exact-sign bisection theorem fail to describe ordinary floating-point code? **Answer:** Sign evaluation, midpoint rounding, overflow or stagnation can break the invariant unless accounted for.

### References

- MIT OpenCourseWare, *18.330 Introduction to Numerical Analysis*, root-finding notes and exercises.
- Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, chapter 1.
- Richard L. Burden and J. Douglas Faires, *Numerical Analysis*, chapters on solutions of nonlinear equations.
