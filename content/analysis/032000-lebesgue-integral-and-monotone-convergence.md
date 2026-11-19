# 032000 — The Lebesgue Integral: Building an Area That Survives Limits

**Track:** Analysis from First Principles. **Background:** measures, simple measurable functions, countable additivity, Riemann integration and pointwise limits. **Question:** How can we define an integral for measurable functions and justify passing a monotone limit through it?

<!-- BEGIN SPOKEN LECTURE -->

# The Lebesgue Integral: Building an Area That Survives Limits

Suppose you want to measure the total mass of a material spread along an interval. The density might be smooth, in which case elementary calculus works perfectly. But perhaps it is zero at every irrational position and one at every rational position. That density is discontinuous everywhere. Riemann integration refuses to assign it an integral, because every interval contains both kinds of points. Yet all the nonzero values lie on a countable set of length zero. A mass measure that treats countable sets as negligible ought to assign total mass zero.

The Lebesgue integral does exactly that. But it is important not to treat this as a clever trick for one pathological example. Its real power comes from how it behaves under limits. If we approximate a nonnegative measurable function increasingly by simpler functions, the integrals increase toward the integral of the limit. No uniform convergence, boundedness of the sequence, or finite total measure is needed for that particular theorem.

We will build the definition, prove the central monotone convergence principle, and then examine the dangerous temptation to remove the word *monotone*.

## Start with a function whose heights are easy to count

Imagine a map divided into three disjoint measurable regions. On the first region the density is two units of mass per unit length, on the second it is five, and on the remaining region it is zero. To obtain total mass, multiply each density by the measure of its region and add. That is all.

A nonnegative *simple function* is any measurable function taking only finitely many nonnegative values. Every such function can be written by taking each distinct value and multiplying it by the indicator of the set on which that value occurs. Because those level sets are disjoint, the integral is the finite sum of height times measure.

One must be slightly careful when a region has infinite measure. If a simple function is zero on an infinite region, that region contributes zero, not an ambiguous zero times infinity. A positive height on an infinite-measure region contributes infinity. With this convention, the integral of every nonnegative simple function is a well-defined number in the extended nonnegative real line.

Take a concrete example on the unit interval. Define a function that equals three on the interval from zero to one quarter, equals one from one quarter to one half, and equals zero elsewhere. The first region has measure one quarter, giving three quarters of a unit of mass. The second has measure one quarter, giving another quarter. The total integral is one. Moving an endpoint from one piece to the other changes the function on only a singleton, so it changes no Lebesgue integral. This apparent indifference to isolated points is built into the measure of the level sets.

Notice the direction of this construction. Riemann integration slices the *domain* into intervals and samples function values there. We are dividing the *range* into a finite menu of heights, then measuring the domain regions assigned to those heights. Both approaches express area, but they use different kinds of approximations.

## From simple functions to every nonnegative measurable function

For a general nonnegative measurable function, our earlier lecture supplied a sequence of nonnegative simple functions that increases toward it. Each simple function is easy to integrate. We might define the integral as the limit of the integrals of those approximations.

There is an even better definition, because we do not want to commit to a particular rounding scheme. Consider *every* nonnegative measurable simple function that lies below the function we wish to integrate. Calculate the integral of each candidate simple function. Take the supremum of those values. That supremum, possibly infinite, is the Lebesgue integral of our nonnegative function.

What makes the definition robust is that it depends only on the target function, not on a favored sequence of approximations. If the target function is itself simple, its integral under the new definition agrees with the original finite sum. If one function is no larger than another, every simple function lying below the first also lies below the second, so the integral cannot decrease. That is monotonicity of the integral.

The all-important question is whether an increasing simple approximation sequence actually recovers this supremum. It does. In fact a stronger result holds for an increasing sequence of *arbitrary* nonnegative measurable functions. The proof will explain why the integral is constructed the way it is.

## The monotone convergence theorem

Imagine a sequence of nonnegative measurable functions. At each fixed point, the values never decrease as the sequence progresses. Suppose they rise to a limiting function. The monotone convergence theorem says that the integrals of the approximations rise to the integral of that limit. The integral of the limit is allowed to be infinite, and the underlying measure space may have infinite total measure.

One direction is immediate. Each approximation is bounded above by the limiting function. Monotonicity of integration therefore bounds every approximate integral by the final integral. So the increasing sequence of integrals has a limit that is no greater than the answer we want.

The reverse direction contains the proof's idea. Pick any nonnegative simple function s lying below the limit. We want the approximate functions to capture almost all of the mass represented by s. They may never dominate s *exactly* at any finite stage, because they might approach s from below forever. So instead choose a number c slightly less than one. We ask where the Nth approximation has reached at least c times s.

At a point where s is positive, the approximations rise to a value at least s, so eventually they exceed c times s. At a point where s is zero, the inequality is true from the start because the approximations are nonnegative. Thus the regions where the approximations dominate c times s form an increasing collection whose union is the whole space.

On each of these regions, the Nth function is at least c times s. Therefore its integral is at least c times the integral of s restricted to that region. Because s has only finitely many heights and the regions increase to cover the space, countable additivity and continuity from below tell us that these restricted simple-function integrals rise to the full integral of s.

So the limiting approximate integral is at least c times the integral of s. Let c approach one, and it is at least the integral of s itself. But s was an arbitrary simple function below the final function. Taking the supremum over all such s gives the reverse inequality. Together the two inequalities prove that the limit of the integrals is exactly the integral of the limit.

The proof is worth remembering for its architecture. It did not assume anything about a formula for the functions. It used their monotone pointwise behavior, a test simple function under the limit, a slight relaxation by multiplying by c, and continuity from below for measured sets. The measure axioms and the integral construction fit one another.

## A familiar series becomes an integral theorem

Consider an infinite collection of disjoint measurable sets, each with its own nonnegative weight. At stage N, add the weighted indicators of only the first N sets. The resulting simple functions increase to the weighted function supported on the union. By monotone convergence, integrating the limit gives the sum of the individual weights multiplied by the measures of their sets.

This is a functional version of countable additivity. In particular, if you have nonnegative measurable functions f one, f two, and so on, you may form their pointwise series. The integral of that nonnegative series equals the series of the integrals, with infinity allowed on either side.

Notice what we have *not* proved. For functions that take both positive and negative values, rearranging an infinite series and passing integrals through it can be dangerous. Infinite positive mass and infinite negative mass do not cancel to make a well-defined finite answer. Nonnegativity is what protects the present exchange of an infinite sum and an integral.

The same protection explains why the integral of the rational-indicator function on the unit interval is zero. Its support is measurable and has length zero. As a simple function it equals one times that indicator, so its integral is the measure of the rationals in the interval, namely zero. The Riemann obstruction has disappeared, not because we ignored the function's discontinuities, but because we now know exactly what measure they occupy.

## Why pointwise convergence is not enough

Now let us deliberately try to break the theorem. On the unit interval, define the Nth function to be N on the tiny interval between zero and one over N, and zero everywhere else, including at zero. Its graph is a rectangle becoming narrower and taller. The area of every rectangle is one: height N times width one over N.

Fix any input x greater than zero. Once N is large enough that one over N is smaller than x, the function at x becomes zero forever. At zero we assigned zero from the start. So these functions converge pointwise *everywhere* to zero. The limit has integral zero. Yet every function in the sequence has integral one.

There is no contradiction with monotone convergence because the functions are not increasing pointwise. The mass concentrates into taller and narrower spikes, and then disappears in the pointwise limit. A fixed observation point eventually misses every spike, but the integral continues to see mass one at each stage.

This example exposes a central limit-exchange danger. Pointwise convergence follows individual inputs through a sequence. The integral is a global quantity that can register mass moving toward a vanishingly small region. Additional assumptions are needed to prevent that mass from escaping detection in the pointwise limit.

A second example makes the danger even more dramatic. Translate a unit-height indicator farther and farther to the right on the entire real line. Every fixed point eventually sees zero, while every function has integral one. The mass does not concentrate; it escapes to infinity. Both mechanisms defeat naive interchange of limit and integral.

Monotone convergence cannot suffer either phenomenon. If the approximations only rise, none of the mass they have already captured can disappear at a later stage. The theorem's assumption is not technical decoration. It prevents exactly the losses these examples illustrate.

## Fatou's lemma: an inequality that survives the loss of monotonicity

Even without monotonicity, nonnegative functions satisfy a useful one-sided inequality. Fatou's lemma says that the integral of the pointwise limit inferior is no greater than the limit inferior of the integrals. If the functions converge pointwise, the integral of their limit is no greater than the lower limiting value of their integrals.

Why is the inequality one-sided? The spike example shows that mass can disappear in the pointwise limit, so the final integral may be smaller. Fatou's lemma says nonnegative mass cannot mysteriously appear in the limit in a way that makes the final integral larger than the eventual lower integral bound.

Its proof reduces the nonmonotone situation to the theorem we already have. For each N, look at the pointwise infimum of all functions from stage N onward. As N increases, the tail gets shorter, so these tail infima can only increase. Their pointwise limit is exactly the limit inferior of the original functions. Apply monotone convergence to the tail infima. Each tail infimum is bounded by every function in its tail, hence its integral is no greater than any corresponding tail integral. Taking limits gives Fatou's inequality.

The proof is a good example of what analysis often does when a powerful theorem has restrictive hypotheses. Instead of discarding the theorem, construct an auxiliary object that satisfies them. Tail infima have monotonicity even when the original functions do not.

We should not reverse Fatou's inequality. With the concentrating spikes, the integral of the limit is zero and the lower limit of the integrals is one. Strict inequality occurs. Nor can we automatically subtract two infinite nonnegative integrals: infinity minus infinity is undefined, not a number we can use to rescue equality.

## Signed functions and the meaning of integrable

To integrate a real-valued measurable function that may be negative, separate it into its positive and negative parts. The positive part is the larger of the function and zero. The negative part is the larger of the negative of the function and zero. Both are nonnegative measurable functions, and the original function equals positive part minus negative part.

Define the signed integral as the integral of the positive part minus the integral of the negative part, provided these two integrals are not both infinite. If they are both infinite, the expression is undefined. A finite real-valued integral exists when both parts have finite integrals; this is equivalent to the integral of the absolute value being finite. In that case we call the function Lebesgue integrable, or say it belongs to L one.

This convention matters. For the function one over x on the interval from zero to one, the nonnegative Lebesgue integral is infinite. No amount of changing the value at zero makes it finite. For a function whose positive and negative contributions both diverge, a principal-value cancellation may sometimes be defined by a special symmetric limiting procedure, but that is not the Lebesgue integral. We should not silently change definitions to obtain a preferred answer.

When an ordinary bounded function is Riemann integrable on a compact interval, it is also Lebesgue integrable and the two values agree. The newer theory does not invalidate the earlier one; it extends it and provides better limit theorems. The rational-indicator example lies outside the Riemann-integrable class, yet its Lebesgue integral exists and equals zero.

## What the construction has earned

We began by measuring simple functions as height times measure. We extended the integral of a nonnegative measurable function by taking a supremum over all simple functions below it. That definition gave monotonicity immediately, and the structure of measure allowed us to prove the monotone convergence theorem.

Fatou's lemma then showed what remains true without increasing approximations: a one-sided inequality. The spike and translation examples showed why pointwise convergence alone cannot justify interchanging a limit and an integral. Finally, separating positive and negative parts explained why signed integration needs absolute integrability for a finite answer.

The next major theorem will answer a natural question raised by the spike example: what common bound on a sequence of functions prevents mass from concentrating or escaping while they converge almost everywhere? Dominated convergence gives a powerful answer when one integrable function controls the absolute size of every term. Later, the same ideas will make L-p spaces into complete function spaces and support Fourier analysis, probability, and operator theory.

The central lesson of the Lebesgue integral is not that we can now integrate every imaginable graph. Some functions are not measurable, and some measurable functions have infinite or undefined signed integrals. Its achievement is a precisely defined integral whose assumptions interact cleanly with sequential limits. That interaction is the reason measure theory became part of the foundation of modern analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### The definition

For a nonnegative simple measurable function \(s=\sum_{j=1}^m a_j1_{A_j}\) with pairwise disjoint measurable \(A_j\) and \(a_j\ge0\), define
\[
\int_Xs\,d\mu=\sum_{j=1}^m a_j\mu(A_j),\qquad 0\cdot\infty:=0.
\]
For arbitrary measurable \(f:X\to[0,\infty]\),
\[
\int_Xf\,d\mu=\sup\left\{\int_Xs\,d\mu:\ s\text{ nonnegative simple measurable},\ 0\le s\le f\right\}.
\]

### Monotone convergence proof

Suppose \(0\le f_n\uparrow f\) pointwise. Monotonicity gives \(\lim_n\int f_n\le\int f\). Choose simple \(s\le f\) and \(0<c<1\); put \(E_n=\{f_n\ge c s\}\). Then \(E_n\uparrow X\) and
\[
\int f_n\ge c\int s1_{E_n}\xrightarrow[n\to\infty]{}c\int s.
\]
For simple \(s\), the limit follows from continuity from below of \(\mu\) on each of its finitely many level sets. Let \(c\uparrow1\), then take the supremum over \(s\le f\), obtaining \(\lim_n\int f_n\ge\int f\). Hence
\[
\boxed{\int_X\lim_{n\to\infty}f_n\,d\mu=\lim_{n\to\infty}\int_X f_n\,d\mu}\quad (0\le f_n\uparrow).
\]

### Fatou's lemma

For measurable \(f_n\ge0\), let \(g_n=\inf_{k\ge n}f_k\). Then \(g_n\uparrow\liminf_nf_n\) and \(\int g_n\le\inf_{k\ge n}\int f_k\). Consequently,
\[
\boxed{\int_X\liminf_n f_n\,d\mu\le\liminf_n\int_X f_n\,d\mu}.
\]
Strict inequality occurs for \(f_n=n1_{(0,1/n)}\) on \([0,1]\): the functions converge pointwise to 0 but \(\int f_n=1\) for all \(n\).

### Signed integration

Define \(f^+=\max(f,0)\), \(f^-=\max(-f,0)\) for finite real-valued measurable \(f\). The signed integral \(\int f=\int f^+-\int f^-\) is defined when the two nonnegative integrals are not both infinite. It is finite iff \(\int|f|<\infty\). Functions in this latter class constitute \(L^1(\mu)\) as pointwise representatives; the Banach-space \(L^1\) is their quotient by almost-everywhere equality.

### Exercises with answers

1. **A simple integral.** If \(s=3\cdot1_{[0,1/4]}+1_{(1/4,1/2]}\), find \(\int_0^1s\,dm\). **Answer:** \(3/4+1/4=1\).
2. **Rational indicator.** What is \(\int_0^1 1_{\mathbb Q}\,dm\)? **Answer:** Zero, since \(\mathbb Q\cap[0,1]\) has measure zero.
3. **Spikes.** Show that \(f_n=n1_{(0,1/n)}\) converges pointwise to zero but not in integrals. **Answer:** Every fixed \(x\in[0,1]\) eventually lies outside \((0,1/n)\), yet \(\int f_n=1\).
4. **Series of nonnegative functions.** If \(f_k\ge0\) are measurable, justify \(\int\sum_{k=1}^\infty f_k=\sum_{k=1}^\infty\int f_k\). **Answer:** Apply monotone convergence to partial sums and finite additivity of the nonnegative integral.
5. **Undefined cancellation.** Why is \(\int_{\mathbb R} x\,dx\) not a Lebesgue integral? **Answer:** Both \(\int x^+\) and \(\int x^-\) over \(\mathbb R\) are infinite; subtracting them would require the undefined expression \(\infty-\infty\).

### Sources

- Sheldon Axler, *Measure, Integration & Real Analysis*, chapters on integration and convergence theorems.
- MIT OpenCourseWare, *18.125 Measure and Integration*, lectures 2–5 (simple functions, integral definition, monotone convergence, Fatou, signed integrals).
