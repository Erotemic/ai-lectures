# 006000 — The Mean Value Theorem: From Local Slopes to Global Bounds

**Track:** Analysis from First Principles. **Background:** derivatives, continuity, compact intervals, and the Extreme Value Theorem. **Theme:** a pointwise derivative controls changes between two different inputs.

<!-- BEGIN SPOKEN LECTURE -->

# The Mean Value Theorem: From Local Slopes to Global Bounds

Knowing a function's derivative at one point tells us how it responds to tiny changes near that point. But suppose we need something larger. We have measured a quantity at the beginning and end of an interval, and we want to know what happened in between. Or we know the derivative can never be larger than a certain number, and we want to bound the difference between two function values.

The Mean Value Theorem connects these kinds of information. Under specific continuity and differentiability assumptions, it says there is at least one point where the instantaneous slope equals the average slope over the entire interval. From that existence statement we can obtain global inequalities, monotonicity tests, and quantitative error bounds.

It is a theorem about the real line. Its proof depends on both the existence of extrema on closed intervals and the ability to compare real slopes. It is also a good demonstration that local analysis becomes powerful only when we can connect nearby behavior along a whole interval.

## A slope that must occur

Consider the square function on the interval from one to three. Its value changes from one to nine, a rise of eight over an input change of two. The average slope is therefore four. Meanwhile the derivative of the square function at x is twice x. At x equals two, that derivative is four, exactly the average slope.

Nothing about the calculation should make us assume that the matching point must always be the midpoint. The square function happens to make it easy. For a more complicated curve, the location could be near either endpoint, and there could be several such points.

The Mean Value Theorem states the precise guarantee. If a real function is continuous on the entire closed interval from a to b, and differentiable at every interior point, then there is some interior point c where the derivative equals the total change in function value divided by b minus a.

The hypotheses have different jobs. Continuity at the endpoints prevents the function from escaping the shape we have constrained on the closed interval. Differentiability in the interior makes local slopes available. Neither assumption can simply be omitted. The absolute-value function on the interval from negative one to one has equal values at the endpoints, so its average slope is zero, but its derivative is negative one on the left and positive one on the right. At the center, the derivative does not exist. No interior derivative equals zero.

## A simpler theorem hidden inside

Before proving the general statement, consider a function with equal endpoint values. Its average slope is zero. Rolle's theorem says that if the function is continuous on the closed interval and differentiable inside it, then somewhere inside the derivative must be zero.

Why should equal endpoint heights force a horizontal tangent? There are two possibilities. The function might be constant on the entire interval, in which case every interior derivative is zero. Otherwise, at least one interior value is strictly above the endpoint level or strictly below it.

Continuity on a closed, bounded interval guarantees that the function attains a maximum and a minimum. If some interior value is higher than the endpoints, the maximum cannot occur at an endpoint. There must be an interior point of maximum. If some interior value is lower than the endpoints, use a minimum instead.

At an interior maximum where the derivative exists, consider a small positive step. The difference quotient is at most zero, because the function cannot increase above the maximum. For a small negative step, the numerator is still at most zero, but the denominator is negative, so the quotient is at least zero. If the two-sided derivative exists, it must be both at most and at least zero. It is exactly zero. The same reasoning holds for an interior minimum.

This small argument is sometimes called Fermat's necessary condition for an interior differentiable extremum. The word necessary is important. A derivative of zero does not guarantee an extremum. The cube function at zero has derivative zero and yet keeps increasing through that point.

## Turning a level curve into a sloping one

Now suppose the endpoint values are different. Draw the straight line connecting the two endpoint values of the function. This secant line has constant slope equal to the function's average slope on the interval.

Subtract the secant line from the function. The new function measures how far the original curve stands above or below its endpoint-to-endpoint line. At each endpoint, that difference is zero, because the curve and line agree there. The difference is continuous throughout the closed interval and differentiable in its interior.

Rolle's theorem applies. Somewhere inside, the derivative of this difference is zero. But that derivative is the derivative of the original function minus the constant slope of the secant line. Setting it equal to zero tells us that, at that point, the derivative of the original function equals its average slope.

That is the Mean Value Theorem. The proof reduces a sloping-endpoint problem to an equal-endpoint problem by removing a line. The global shape of the curve is not prescribed; the conclusion is that at least one local slope matches the net change.

## A derivative bound becomes an output bound

Here is a particularly useful consequence. Suppose a differentiable function has derivative whose magnitude is never larger than five anywhere between two inputs. The Mean Value Theorem says their output difference equals some derivative value times the distance between the inputs, with an appropriate sign. Taking magnitudes, the output difference cannot exceed five times the input distance.

This converts local information into an inequality valid for any two points in the interval. We can think of a derivative bound as a speed limit for the function. If the function's slope never has magnitude greater than five, the function cannot change by more than five units per unit of input, no matter how unevenly it moves.

The same reasoning works for any bound M. When the function is continuous on a closed interval and differentiable inside it, and the magnitude of its derivative is bounded above by M throughout the interior, the change in output is bounded by M times the change in input.

Such an estimate is called a Lipschitz bound. In numerical work it quantifies sensitivity. If the input has uncertainty of at most one thousandth, and the derivative has magnitude at most five on the relevant interval, then the corresponding output uncertainty is at most five thousandths. This is a guarantee rather than merely a first-order approximation.

A useful example is the sine function. Its derivative is cosine, whose magnitude never exceeds one. Therefore the difference between the sines of any two real numbers is no greater in magnitude than the difference between those numbers. The inequality holds even when the two numbers are not close.

## How derivatives control direction

A derivative also determines how a function moves across an interval. If its derivative is positive at every interior point, take any two different inputs with the first smaller than the second. The Mean Value Theorem provides an intermediate point whose derivative equals the average slope. Since that derivative is positive, the average slope is positive. Therefore the second output is larger than the first.

So a strictly positive derivative throughout an interval implies that the function is strictly increasing there. A strictly negative derivative implies it is strictly decreasing. A derivative equal to zero everywhere on an interval implies that the function is constant.

The last conclusion is stronger than a collection of statements that the function is locally flat. Without a theorem, saying zero slope at each point and concluding global constancy would conceal the role of the interval. The Mean Value Theorem links any two points to an intermediate derivative, so zero at every point forces every pair of function values to be equal.

There are converse pitfalls. A strictly increasing differentiable function need not have positive derivative at every point: the cube function is strictly increasing, yet its derivative at zero is zero. And the derivative-zero-implies-constant statement requires a connected interval. On two separated pieces of a domain, a function could take different constants without violating zero derivative on either piece.

## Bounding approximation errors

Differentiability at a point gives a linear approximation with an error smaller than the first power of the step. To quantify the error for a finite step, we can apply the Mean Value Theorem to the difference between the function and its tangent-line approximation.

Suppose the derivative itself varies slowly: whenever we move away from a point a to some nearby point x, the derivative changes by no more than K times the distance from a to x. Then the error of the tangent-line prediction is at most K times the square of the step. That bound is already useful, although a sharper factor of one half can be obtained under suitable second-derivative assumptions.

For a function with a continuous second derivative whose magnitude stays below K on the interval, the familiar second-order Taylor remainder gives an error no larger than one half K times the square of the step. This is not just the statement that the error becomes small. It is a numerical guarantee for each allowed step.

Consider again the square function at x equals three. The tangent-line prediction for a step h has error exactly h squared. Its second derivative is the constant two. The bound from Taylor's theorem is one half times two times h squared: precisely h squared. In this example, the general estimate is attained exactly.

For other functions, the bound can be conservative, but its hypotheses tell us what information is needed. A bound on the first derivative controls how far output values can separate. A bound on the second derivative controls how far a tangent-line approximation can miss.

## Failure cases are part of the theorem

Consider the absolute-value function again. On the interval from negative one to one, it is continuous and its endpoint values agree. But there is no point of zero derivative inside the interval. The sharp corner at zero is exactly where differentiability fails, and Rolle's conclusion fails with it.

A different problem arises with a jump. Define a function that is zero everywhere before the right endpoint and one at the right endpoint. Its derivative is zero at every interior point, but the total change over the closed interval is one. The function is not continuous at the right endpoint. Once that endpoint continuity hypothesis is removed, the interior derivatives no longer have to account for the jump.

These examples make the mechanism clearer. The theorem does not say a collection of derivative values automatically describes any arbitrarily specified pair of outputs. It says the derivative values describe output changes when the function is connected to its endpoints by the exact regularity assumptions.

## What the theorem really buys us

The Mean Value Theorem begins as an existence claim: at least one instantaneous slope matches the average slope. But its most enduring uses often do not require finding that point. We can bound its possible derivative value instead. From a single bound that holds across an interval, we deduce an inequality about every pair of inputs on that interval.

That is why this theorem sits at the center of real analysis. It converts infinitesimal, local information into finite, global control. It explains monotonicity, proves that a zero derivative forces constancy, and transforms derivative bounds into certified error estimates.

The same pattern will matter whenever we study accumulated change. Local rates can constrain an entire trajectory—but recovering the total change from those local rates requires a second construction, one that adds many tiny contributions rather than taking their ratio. The Mean Value Theorem gives us the bridge between local and global behavior; integration will give us a language for accumulation itself.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Fermat's necessary condition.** If \(f\) is differentiable at an interior local extremum \(c\), then \(f'(c)=0\). One-sided quotients at a local maximum have opposite weak signs and hence their common limit is zero.

**Rolle's theorem.** If \(f\in C([a,b])\), differentiable on \((a,b)\), and \(f(a)=f(b)\), then some \(c\in(a,b)\) satisfies \(f'(c)=0\). Apply the Extreme Value Theorem and Fermat's condition, unless \(f\) is constant.

**Mean Value Theorem.** Under the same continuity/differentiability assumptions,
\[
 \exists c\in(a,b):\quad f'(c)=\frac{f(b)-f(a)}{b-a}.
\]
Proof: set \(m=(f(b)-f(a))/(b-a)\) and \(g(x)=f(x)-m(x-a)\); then \(g(a)=g(b)\) and Rolle's theorem yields \(g'(c)=0\).

**Lipschitz consequence.** If \(|f'(x)|\le M\) on the interior of \([a,b]\), then
\[
 |f(y)-f(x)|\le M|y-x|\quad (x,y\in[a,b]).
\]
In particular, \(|\sin y-\sin x|\le |y-x|\).

**Monotonicity.** \(f'>0\) throughout an interval implies strict increase; \(f'=0\) everywhere implies constancy. Strict increase does not imply \(f'>0\) pointwise: \(f(x)=x^3\) is increasing with \(f'(0)=0\).

**Error bounds.** Suppose \(f\in C^2\) on an interval containing \(a\) and \(a+h\), and \(|f''|\le K\) there. Taylor's theorem with Lagrange remainder gives
\[
 f(a+h)=f(a)+f'(a)h+\tfrac12 f''(\xi)h^2
\]
for some \(\xi\) between \(a\) and \(a+h\), hence
\[
 |f(a+h)-f(a)-f'(a)h|\le\tfrac12 K h^2.
\]
Under merely \(|f'(x)-f'(a)|\le K|x-a|\), the Mean Value Theorem applied to \(g(x)=f(x)-f(a)-f'(a)(x-a)\) yields the weaker bound \(|g(a+h)|\le K h^2\) without invoking integration.

### Exercises and guided answers

1. **Average slope:** For \(f(x)=x^2\) over \([1,3]\), find an MVT point. **Answer:** Secant slope \(4\); \(f'(c)=2c=4\), so \(c=2\).
2. **Sharp corner:** Explain why Rolle's theorem cannot be applied to \(|x|\) on \([-1,1]\). **Answer:** The derivative does not exist at zero.
3. **Derivative bound:** Suppose \(|f'|\le7\) on \([0,2]\). How large can \(|f(1.2)-f(1.1)|\) be? **Answer:** At most \(0.7\).
4. **Derivative zero:** If \(f'(x)=0\) on \((2,5)\) and \(f\) is continuous on \([2,5]\), prove \(f(2)=f(5)\). **Answer:** MVT gives secant slope zero.
5. **Taylor error:** If \(|f''|\le4\) on a step of length \(0.1\), bound the tangent-line error. **Answer:** At most \((1/2)(4)(0.1)^2=0.02\).

### References

- OpenStax, *Calculus Volume 1*, section 4.4, “The Mean Value Theorem”: https://openstax.org/books/calculus-volume-1/pages/4-4-the-mean-value-theorem
- Wikipedia, “Mean value theorem”: https://en.wikipedia.org/wiki/Mean_value_theorem
- Stephen Abbott, *Understanding Analysis*, differentiation and the Mean Value Theorem.
- Terence Tao, *Analysis I*, mean value and derivative bounds.
- [MIT OpenCourseWare, 18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/pages/lecture-notes/) — MIT 18.100B, lectures 16–17: Rolle, MVT and Taylor estimates.
