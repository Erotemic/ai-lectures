# 005000 — The Derivative as a Local Linear Approximation

**Track:** Analysis from First Principles. **Background:** limits of functions and continuity on real intervals. **Theme:** a derivative is not merely a slope; it is a guarantee that a linear prediction captures the first-order change.

<!-- BEGIN SPOKEN LECTURE -->

# The Derivative as a Local Linear Approximation

Imagine measuring the position of a moving object at two moments. If its position changes by twelve meters over three seconds, its average velocity over that interval is four meters per second. That number describes the interval as a whole. It does not tell us how fast the object was moving at the first moment, or at the last, or when it briefly turned around.

To speak of velocity at a single instant, we have to make the observation interval smaller. But shrinking the interval introduces a difficulty. An average velocity divides a change in position by a change in time. At an interval of exactly zero length, that quotient divides zero by zero. We cannot simply substitute zero. We must ask whether the quotients, computed for nonzero intervals, approach a definite number as the intervals shrink.

That question produces the derivative. More importantly, the derivative tells us when a function can be replaced, for a sufficiently small change of input, by a straight-line prediction with an error smaller than the change itself. This local approximation viewpoint explains both the computational rules of differentiation and their limitations.

## A quadratic experiment

Take a function that squares its input. Let the input start at three and move by an amount h, which may be positive or negative. The original output is nine. The new output is nine plus six times h plus h squared. The output change is therefore six times h plus h squared.

When h is not zero, divide this change by h. The result is six plus h. At h equals one, the average slope is seven. At h equals one tenth, it is six point one. For a negative change of one tenth, it is five point nine. As h approaches zero from either side, the slopes approach six.

We say the derivative of the squaring function at three is six. Notice exactly what this means. It does not say that the function always changes six units for one unit of input. The actual output change contains the extra term h squared. It says that six is the limiting ratio of output change to input change when the input change tends to zero.

The distinction matters because a finite step has a finite error. With a step of one tenth, the linear prediction says the output changes by six tenths. The actual change is sixty-one hundredths. The error is one hundredth. With a step of one hundredth, that error becomes one ten-thousandth. The prediction becomes disproportionately better as the step shrinks.

This is what it means for the straight line to be the correct first-order model of the curve near a point.

## The definition, and what the limit must control

Let f be a real-valued function defined on an open interval around a point a. For every sufficiently small nonzero input change h, we can form the difference between f at a plus h and f at a, divided by h. If these difference quotients approach one finite real number as h tends to zero, we call that number the derivative of f at a.

The interval must let us approach from both sides. At an endpoint of a domain we may define a one-sided derivative, but that is a separately specified notion. And the derivative, as defined here, is a finite number. A quotient that grows without bound does not provide a finite derivative merely because the graph has something that looks like a vertical tangent.

To see why the two-sided condition is important, consider the absolute-value function at zero. On the positive side, its output changes by exactly the same amount as its input, so the difference quotient is positive one. On the negative side, its output is the negative of its input, so the quotient is negative one. There is no single number approached by both sides. The function is continuous at zero, but it is not differentiable there.

Continuity asks whether nearby outputs approach the output at the point. Differentiability asks for a much more precise statement: whether the output change has a consistent first-order ratio to the input change. A continuous graph can have a corner, so continuity alone cannot supply a derivative.

## Why a derivative is a linear model

Return to the square function. Its output change near three was six times h plus h squared. We can separate the change into a linear part, six times h, and an error, h squared. Divide the error by the size of the step. Its magnitude becomes the magnitude of h, which tends to zero.

This is the general pattern. If a function has derivative m at a, its output at a plus h equals its output at a, plus m times h, plus an error. The critical fact is that the error, divided by the magnitude of h, approaches zero as h approaches zero. An error that is merely small in absolute terms is not enough. It must become small relative to the first power of the step.

Conversely, if a function admits such a linear model with a remainder negligible compared with the step, then dividing by the step recovers m as the limit of the difference quotients. So the derivative definition and the local linear approximation are two expressions of the same property.

This also proves that differentiability implies continuity. The linear term goes to zero with h, and the remainder goes to zero even faster relative to h. Their sum, which is the entire change in output, must go to zero. A differentiable function cannot jump at the point where its derivative exists.

The converse, as absolute value demonstrates, is false. Continuity controls the size of the change but need not provide a consistent linear part.

## The derivative is a function too

For the square function, the calculation at three worked at any starting input a. The output change is twice a times h plus h squared, so the limiting quotient is twice a. Each input has its own derivative value. Collect those values into a new function: the derivative function.

At input three the slope is six. At input one the slope is two. At input zero the slope is zero. If the input is negative, the slope is negative. One formula describes how all these local slopes vary.

It is tempting to assume that, because the original function was smooth enough to possess a derivative, the derivative function must be continuous. That is not guaranteed. There are differentiable functions whose derivatives oscillate without approaching a limit at a point. Differentiation gives a new function, but it does not automatically give that new function all the regularity properties we might want.

We should therefore distinguish three questions. Does the original function have a limit? Is it continuous? Does it have a derivative? Each question imposes stronger local control than the previous one, and the stronger implications do not simply run backward.

## Why the product and chain rules are plausible

Suppose two quantities, f and g, both depend on the same input. Their product changes for two reasons: f changes while g is held near its old value, and g changes while f is held near its old value. There is also a small interaction between the two changes. If both functions are differentiable, each individual change is approximately linear in the input step, so the interaction is of second order and disappears after division by the step.

The first-order change of the product therefore consists of the derivative of f multiplied by the current value of g, plus the current value of f multiplied by the derivative of g. This is the product rule. Its two terms record two ways the product can change. Leaving out either one would miss part of the first-order behavior.

Now consider a composition. First an input x is transformed by g. Then the result of g becomes the input to another function f. A tiny change in x produces an approximate change in g equal to the derivative of g times the original step. That intermediate change produces an approximate change in f equal to the derivative of f, evaluated at the intermediate value, times the change in g.

Multiplying these first-order effects gives the chain rule: differentiate the outer function at the current inner output, and multiply by the inner derivative.

For a concrete example, take the function obtained by squaring x, adding one, and then cubing the result. At x equals one, the inner quantity is two. Its rate of change is two. Cubing has rate of change three times the square of its input, so at input two that rate is twelve. Multiply twelve by two: the composite derivative at one is twenty-four.

Notice that the two derivatives live at different input locations. The derivative of the outer cubing function is evaluated at two, not at one. That detail is not notation trivia; it reflects the physical order in which the two transformations act.

## When linearization helps, and when it misleads

A derivative is useful whenever we need a prediction for a small change. If a measurement y depends on x and its derivative at a is m, then a small measurement error in x produces an output error approximately equal to m times the input error. A large magnitude of m signals sensitivity; a small magnitude signals local insensitivity.

But the approximation has a range of trust determined by the neglected remainder. The derivative alone does not certify a good approximation over a large step. For our square function at three, the omitted error is exactly h squared. If h equals one, the error is one, hardly negligible. No theorem permits us to keep the tiny-step accuracy while enlarging the step arbitrarily.

There is another trap: a derivative of zero does not mean the function is locally constant. For the cube function at zero, the derivative is zero. Yet the function passes through zero and continues increasing. Its first-order approximation is flat there; the meaningful change appears at a higher order. A zero derivative also does not, by itself, establish a maximum or minimum.

Even a finite numerical difference quotient can be deceptive. If a computer subtracts two nearly equal floating-point outputs and divides by an extremely small step, rounding error may overwhelm the very change we are trying to measure. A smaller finite-difference step is not always a more accurate numerical estimate. The mathematical limit and the finite calculation are related but different objects.

## A proof worth remembering

For the square function at a, the derivative is twice a, and the exact output formula separates into a linear term and a quadratic error. This one example contains the structure of the whole definition: a locally valid linear model, plus an error that disappears after division by the input change.

The derivative measures the first-order response of a function, not its complete behavior. It lets us compute slopes, velocities, and sensitivities; it justifies linearization; and it supplies the product and chain rules because first-order changes combine in predictable ways.

The central question to carry forward is precise: when we replace a nonlinear function by a line near a point, how do we control what that replacement loses? Differentiability gives an error that is smaller than the first power of the step. More powerful theorems will turn bounds on derivatives into guarantees over entire intervals.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

Assume that the indicated point is interior to the domain unless explicitly discussing a one-sided derivative.

**Definition and linearization equivalence.** For a function defined on a neighborhood of \(a\),

\[
 f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h=m\in\mathbb R
 \quad\Longleftrightarrow\quad
 f(a+h)=f(a)+mh+r(h),\qquad \lim_{h\to0}\frac{r(h)}h=0.
\]

Writing \(r(h)=o(|h|)\) is equivalent; in particular \(r(h)\to0\). Hence differentiability implies continuity at \(a\).

**Square function.** \(f(x)=x^2\), \(f(a+h)-f(a)=2ah+h^2\), \(f'(a)=2a\). At \(a=3\), the linearization is \(9+6h\) and its exact error is \(h^2\).

**Corner.** \(f(x)=|x|\) has right derivative \(+1\) and left derivative \(-1\) at \(0\); it is continuous but not differentiable there.

**Product rule.** For differentiable \(f,g\) at \(a\),
\[
 (fg)'(a)=f'(a)g(a)+f(a)g'(a).
\]
Proof: expand \(f(a+h)g(a+h)-f(a)g(a)\) as \([f(a+h)-f(a)]g(a+h)+f(a)[g(a+h)-g(a)]\), divide by \(h\), and use continuity of \(g\).

**Chain rule.** If \(g\) is differentiable at \(a\) and \(f\) at \(g(a)\), then
\[
 (f\circ g)'(a)=f'(g(a))g'(a).
\]
A proof avoiding division by \(g(a+h)-g(a)\) when it is zero: define \(\eta(k)\) by \(f(y+k)-f(y)=f'(y)k+\eta(k)k\), where \(\eta(k)\to0\) as \(k\to0\), with \(\eta(0)=0\). Substitute \(k=g(a+h)-g(a)\) and use the boundedness of \(k/h\) near zero.

**Composite example.** \(F(x)=(x^2+1)^3\), \(F'(x)=3(x^2+1)^2(2x)\), and \(F'(1)=24\).

**Derivative need not be continuous.** Define \(q(0)=0\) and \(q(x)=x^2\sin(1/x)\) for \(x\ne0\). Then \(q'(0)=0\), while for nonzero \(x\), \(q'(x)=2x\sin(1/x)-\cos(1/x)\), which has no limit as \(x\to0\).

### Exercises and guided answers

1. **Derivative from the definition:** For \(f(x)=x^2-4x\), compute \(f'(3)\) directly from difference quotients. **Answer:** \([f(3+h)-f(3)]/h=2+h\), so \(f'(3)=2\).
2. **Linearization error:** Approximate \((2+h)^2\) with a line at \(2\). **Answer:** \(4+4h\), with exact remainder \(h^2\).
3. **Nondifferentiable point:** Why does \(|x-1|\) fail to have a derivative at \(1\)? **Answer:** The left and right difference quotients converge to \(-1\) and \(+1\).
4. **Chain rule:** Differentiate \((3x+1)^4\) at \(x=0\). **Answer:** \(4(3x+1)^3\cdot3\), giving \(12\).
5. **Zero slope:** Does \(f'(0)=0\) imply a local maximum? **Answer:** No; \(f(x)=x^3\) is a counterexample.

### References

- OpenStax, *Calculus Volume 1*, section 3.1, “Defining the Derivative”: https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative
- Wikipedia, “Derivative”: https://en.wikipedia.org/wiki/Derivative
- Stephen Abbott, *Understanding Analysis*, differentiation chapter.
- Terence Tao, *Analysis I*, differentiability of real functions.
