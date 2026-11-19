# 008000 — The Fundamental Theorem of Calculus: Recovering Change from Rates

**Track:** Analysis from First Principles. **Background:** continuity, differentiability, the Mean Value Theorem, and Riemann integration. **Theme:** under the right hypotheses, accumulating a rate and differentiating an accumulation undo one another.

<!-- BEGIN SPOKEN LECTURE -->

# The Fundamental Theorem of Calculus: Recovering Change from Rates

Imagine that we know the velocity of a moving object at every moment, but have forgotten its position measurements. Could we reconstruct how far it moved? We could cut time into short pieces, multiply an estimated velocity by each piece's duration, and add those small displacements. That is integration.

Now suppose we have done precisely that calculation, beginning at a fixed starting time, and keep extending the ending time. The accumulated displacement is itself a function of time. What happens if we differentiate this new function? Do we recover the original velocity?

The Fundamental Theorem of Calculus gives two related answers. Accumulating a continuous rate produces a function whose derivative is that rate. And if we already know a function whose derivative is the rate, then we can compute the accumulated change by subtracting its endpoint values.

These statements are often presented as one calculation rule, but they answer different questions. One constructs a new antiderivative from an integral. The other evaluates an integral using any antiderivative. Seeing their proofs clarifies why the rules work, and where they stop working.

## Accumulation as a function

Let f describe a rate on a closed interval from a to b. Choose the starting point a once and for all. For each current position x between a and b, add the contributions of f from a up to x. Call the result A at x. Thus A is the accumulated total up to x.

For an ordinary nonnegative rate, A increases as the upper endpoint moves right, but the construction also works with negative rates. If the rate becomes negative, accumulated signed change can decrease. The starting value A at a is zero because the integration interval has zero length.

We can first see what should happen in a simple example. Take f at time t to be twice t, for times between zero and two. We already know from finite sums that the accumulation from zero to x is x squared. Its derivative is twice x, which is exactly the rate we started with.

That example is encouraging, but it is not a proof for arbitrary continuous f. We need to understand the change in A when we move its upper endpoint by a small amount h.

## The small extra strip

The difference between A at x plus h and A at x is the integral of f over the small interval from x to x plus h. This follows from additivity of the integral. It is true even when h is negative, if reversing integration limits changes the sign as usual.

Divide that accumulated change by h. The quotient is the average value of f over the short interval, taken with its appropriate orientation. If f were exactly constant on that little interval, the quotient would equal f at x immediately.

When f is continuous at x, its values on a sufficiently short interval near x all lie close to f at x. The average value lies close too. More explicitly, the magnitude of the quotient minus f at x is no larger than the largest deviation of f from f at x on the small interval. As h tends to zero, continuity forces that deviation to zero.

So the difference quotient of A approaches f at x. Therefore the derivative of the accumulation function A at every interior point x is exactly f at x.

This is the first part of the Fundamental Theorem of Calculus. The hypothesis that f is continuous is crucial to the argument as stated. It lets us replace a local average of f by the value of f at the point in the limit.

Notice the direction of reasoning. We did not assume that integration reverses differentiation. We defined accumulation using Riemann sums, examined the extra strip gained by moving the endpoint, and proved that its average rate converges to the instantaneous rate. The derivative emerged from the independently defined integral.

## What is an antiderivative?

We call a differentiable function F an antiderivative of f on an interval if its derivative equals f at every interior point of that interval. An antiderivative is not a number. It is a function whose local rate of change is the function we have been given.

For instance, the derivative of x squared is twice x, so x squared is an antiderivative of the function twice x. But x squared plus seven is another antiderivative, and so is x squared minus a thousand. Adding a constant does not change a derivative.

Are there other antiderivatives with the same derivative that are not related by a constant? Not on a connected interval. If F and G have the same derivative, the derivative of their difference is zero everywhere inside that interval. The Mean Value Theorem forces their difference to be constant throughout the interval.

This is why indefinite integral notation ordinarily includes an arbitrary constant. The symbol stands for a family of functions, whereas a definite integral from a to b is a single number. Confusing those two objects can hide what is being proved.

The accumulation function A is a particularly convenient antiderivative because it has a specified starting value: zero at a. If another antiderivative F is available, A and F differ by a constant. We can find that constant just by looking at the starting point.

## Computing an integral from endpoint values

Since A and F have the same derivative, their difference is constant. At the starting point a, A is zero. Therefore A at any x equals F at x minus F at a.

Set x equal to b. We obtain the second part of the Fundamental Theorem of Calculus: the definite integral of f from a to b equals F at b minus F at a, whenever f is continuous on the interval and F is an antiderivative there.

In the example f equals twice x, choose F equal to x squared. The integral from one to three is therefore three squared minus one squared: nine minus one, or eight. We have replaced a limit of many finite sums with two evaluations of an antiderivative.

The result is much more efficient when a convenient antiderivative is known. It is also conceptually stronger than a shortcut. It says that the accumulation computed by the Riemann integral is exactly the net change of a quantity whose derivative is the rate.

One can prove the endpoint rule a second way, without first constructing A as a derivative. Partition the interval into small pieces. For each piece, the Mean Value Theorem says that the change in F across that piece equals f at some interior sample point times the piece's width. Add all those changes. The left side telescopes to F at b minus F at a. The right side is a tagged Riemann sum for f. As the mesh goes to zero, integrability makes that sum converge to the definite integral.

This second proof brings out a striking fact. The Mean Value Theorem turns each small displacement of F into a local rate times a time increment. The Riemann integral adds those rate contributions. The intermediate changes cancel, leaving only the total endpoint difference.

## A rate need not be positive

For motion, suppose velocity is positive for part of a journey and negative for another part. The integral of velocity gives net displacement: final position minus initial position. It does not necessarily give the total distance traveled. Distance involves the integral of the magnitude of velocity under suitable regularity assumptions.

A toy example is velocity equal to twice t minus two over the time interval from zero to two. An antiderivative is t squared minus two t. The endpoint difference between zero and two is zero. The object has zero net displacement, but it has not remained still: it traveled backward during the first half of the interval and forward during the second.

Indeed, the total distance is obtained by splitting at time one, where the velocity changes sign. The magnitude of the velocity contributes one unit of distance on each half, for a total of two units. The distinction between signed and unsigned accumulation is not an optional interpretation. It is built into which function we integrate.

## The chain rule with a moving endpoint

Now imagine that the upper endpoint is not x itself but another differentiable quantity g of x. Define an accumulated quantity by integrating f from a fixed starting point up to g of x, and assume the entire moving integration range stays in an interval where f is continuous.

There are two transformations. The outside operation takes an endpoint y and returns the accumulated integral up to y. The inside operation moves that endpoint according to g of x. We know the derivative of the outside accumulation at y is f at y. Applying the chain rule gives f evaluated at g of x, multiplied by the derivative of g.

For example, the derivative with respect to x of the integral of twice t from zero to x squared is twice x squared, multiplied by two x. That is four times x cubed. We could confirm the result by evaluating the integral as x to the fourth power and differentiating directly, but the chain-rule argument works without first finding a closed-form antiderivative.

This illustrates a general advantage of the theorem. We can differentiate an integral with a variable endpoint even when the integral itself has no convenient elementary formula. The theorem supplies the derivative directly from the integrand.

## Why continuity cannot just be erased

Suppose a rate equals one everywhere except at zero, where its value is two. That single changed value does not affect its Riemann integral. The accumulation from zero up to x is simply x, so its derivative at zero is one. Yet the original rate at zero was defined to be two.

Thus the conclusion that the derivative of an accumulation equals f at every point fails if we allow this discontinuity. The accumulation only sees the function through how it contributes across intervals. It does not preserve an isolated point value.

This does not mean discontinuous functions can never have antiderivatives, or that the Fundamental Theorem of Calculus has no extensions. It means we must state which version we are using and what regularity ensures its conclusion. There are more general forms involving integrability and different notions of differentiability, but they require careful wording.

There is also a distinction between knowing that an antiderivative exists and knowing how to write it with familiar elementary functions. The first part of the theorem constructs an antiderivative for every continuous rate on an interval. That antiderivative may be defined by the integral itself, without a shorter formula in terms of polynomials, exponentials, logarithms, or trigonometric functions.

So the theorem is a guarantee of existence and identity, not a promise that symbolic integration will always be easy.

## What differentiation and integration each contribute

Differentiation compares a function's output change to a small input change. Integration accumulates the contributions of a rate across many small intervals. These constructions seem to point in opposite directions, one taking ratios and the other taking sums.

The Fundamental Theorem of Calculus says that, for continuous real rates on closed intervals, they meet exactly. If we integrate the rate up to a moving endpoint and differentiate the result, we recover the rate. If we differentiate a quantity and integrate that rate, we recover the quantity's total change between two endpoints.

That is why a velocity can determine displacement, why a continuously varying flow can determine total volume, and why an antiderivative lets us evaluate a definite integral without explicitly taking the limit of its Riemann sums.

But the hypotheses remain visible. We need an integrable rate to make the accumulation meaningful. Continuity gives the pointwise derivative recovery in the standard form. And we need an antiderivative on an interval to use endpoint subtraction. Within those conditions, the local and global descriptions of change are not merely compatible. They are mathematically the same accounting of change, viewed from opposite sides.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**FTC, accumulation form.** If \(f\in C([a,b])\), define
\[
 A(x)=\int_a^x f(t)\,dt,\qquad x\in[a,b].
\]
Then \(A\) is continuous on \([a,b]\), differentiable on \((a,b)\), and \(A'(x)=f(x)\) for \(x\in(a,b)\). One-sided derivatives agree with corresponding endpoint values when defined.

**Proof estimate.** For \(x,x+h\in[a,b]\), \(h\ne0\),
\[
 \left|\frac{A(x+h)-A(x)}{h}-f(x)\right|
 =\left|\frac{1}{h}\int_x^{x+h}\bigl(f(t)-f(x)\bigr)\,dt\right|
 \le \sup_{t\in [\min(x,x+h),\max(x,x+h)]}|f(t)-f(x)|\to0.
\]

**FTC, endpoint form.** If \(f\in C([a,b])\) and \(F' = f\) on \((a,b)\), with \(F\in C([a,b])\), then
\[
 \int_a^b f(t)\,dt=F(b)-F(a).
\]
Proof: \(A'=f=F'\), so \((F-A)'=0\) on \((a,b)\). By the Mean Value Theorem \(F-A\) is constant. Evaluate at \(a\).

**Independent MVT proof.** For a partition \(P\), the MVT supplies \(\xi_i\in(x_{i-1},x_i)\) with \(F(x_i)-F(x_{i-1})=f(\xi_i)\Delta x_i\). Summing yields \(F(b)-F(a)=S(f,P,\xi)\). Let \(\|P\|\to0\).

**Variable endpoint.** If \(g\) is differentiable and \(g(x)\in(a,b)\), then
\[
 \frac{d}{dx}\int_a^{g(x)} f(t)\,dt=f(g(x))g'(x).
\]

**Single-point modification.** Let \(f(t)=1\) for \(t\ne0\) and \(f(0)=2\). It is Riemann integrable on every compact interval, and \(\int_0^x f(t)\,dt=x\), whose derivative at zero equals \(1\ne f(0)\).

**Signed displacement example.** \(v(t)=2t-2\), \(t\in[0,2]\). Then
\[
 \int_0^2 v(t)\,dt=0,\qquad
 \int_0^2 |v(t)|\,dt=2.
\]

### Exercises and guided answers

1. **Recover the rate:** Let \(A(x)=\int_1^x \cos t\,dt\). What is \(A'(x)\)? **Answer:** \(\cos x\) for interior \(x\).
2. **Evaluate a definite integral:** Find \(\int_1^3 2t\,dt\). **Answer:** \([t^2]_1^3=8\).
3. **Moving endpoint:** Differentiate \(\int_0^{x^2} (1+t^2)\,dt\). **Answer:** \((1+x^4)2x\).
4. **Constant ambiguity:** If \(F'=G'\) on \((a,b)\) and both are continuous on \([a,b]\), what can be said about \(F-G\)? **Answer:** It is constant on \([a,b]\) by the Mean Value Theorem.
5. **Discontinuity:** Does every Riemann-integrable \(f\) satisfy \((d/dx)\int_0^x f(t)\,dt=f(x)\) at every point? **Answer:** No; changing one point value of a constant function gives a counterexample.

### References

- OpenStax, *Calculus Volume 1*, section 5.3, “The Fundamental Theorem of Calculus”: https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus
- Wikipedia, “Fundamental theorem of calculus”: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
- Stephen Abbott, *Understanding Analysis*, the Fundamental Theorem of Calculus.
- Terence Tao, *Analysis I*, relationship between integration and differentiation.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lecture 19: both forms of the Fundamental Theorem of Calculus.
