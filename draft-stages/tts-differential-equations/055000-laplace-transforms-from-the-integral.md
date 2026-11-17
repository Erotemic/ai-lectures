# Laplace Transforms from the Integral: Seeing a Signal through Exponential Weighting

<!-- BEGIN SPOKEN LECTURE -->

# Laplace Transforms from the Integral

Suppose a tank begins to fill when a valve opens. For a while the inflow is steady; then it doubles; then the pump shuts off. There is no repeating cycle. We want to predict the tank level from an initial level and from everything the valve does afterward.

Our Fourier lectures broke repeating signals into harmonics. That approach is powerful when the input repeats. But this tank problem has a beginning and a sequence of one-time events. It suggests a different question: could we encode the entire history after time zero in one function, so that differentiation becomes an algebraic operation and initial conditions are not forgotten?

That encoding is the one-sided Laplace transform. It is not merely a table of tricks for differential equations. The defining integral tells us what information is being collected, why exponential growth changes where the integral converges, and why the transform is so convenient for an initial-value problem.

## The definition, first with an ordinary real number

Let f of t describe a signal for time t greater than or equal to zero. For a positive real number s, multiply the signal at time t by the exponential of negative s times t. Then integrate that weighted signal from zero all the way to infinity. Call the answer F of s.

Why this particular weight? If s is large, the factor decays rapidly. Contributions from the distant future count very little. If s is small but positive, the weight decays slowly, and the integral feels a longer portion of the signal. Each value of s measures the history at a different exponential time scale.

This is a picture, not yet a proof that the transform always exists. An infinite integral might diverge. We must check whether the exponential weight decays faster than the signal grows. Later we can allow s to be complex, which also records oscillation. But nearly every first calculation makes sense using real s.

Begin with the simplest signal: f of t equals one. Its transform is the integral of the exponential of negative s t from zero to infinity. An antiderivative is negative one over s times that same exponential. Since the exponential tends to zero for positive s, the answer is one over s. We must state the condition: for zero or negative real s, this particular improper integral does not converge.

Now replace one with the exponential of a times t. The integrand becomes the exponential of negative the quantity s minus a, times t. Exactly the same calculation gives one divided by s minus a, but only when s is greater than a. A growing input, with positive a, is perfectly transformable provided the weight decays faster. The transform is not defined everywhere simply because the answer is a neat rational expression.

For example, the transform of an exponentially decaying signal, the exponential of negative two t, is one divided by s plus two. The integral converges whenever real s is greater than negative two. The familiar pole at negative two marks the boundary of this elementary region of convergence.

## Why differentiation in s gives powers of time

The transform of t is one divided by s squared. We can see this without memorizing it. Integrate t times the exponential of negative s t by parts. Choose t as the factor to differentiate and the exponential as the factor to integrate. The boundary term vanishes when s is positive, and the remaining integral is one over s times the transform of one. That is one over s squared.

Do it again for t squared. Each integration by parts lowers the power of t by one and supplies another factor of one over s. We obtain two divided by s cubed. For a nonnegative integer n, the pattern is n factorial divided by s to the power n plus one. This family is important because a time-dependent force may ramp upward rather than arrive as a sinusoid.

Another way to remember the pattern is to differentiate the transform with respect to s. The derivative of the weighting factor, exponential of negative s t, introduces a factor of negative t. Under the conditions that allow differentiation under the integral, the transform of t times f of t is the negative derivative of F with respect to s. It is a rule with a reason, not an isolated entry in a table.

## Find the sine and cosine transforms

We also need oscillations, because even a nonperiodic experiment can contain a ringing spring or circuit. Let I be the integral of the exponential of negative s t times cosine of b t. Let J be the corresponding integral with sine of b t, with s positive and b real.

Integrate by parts once. For cosine, the boundary contribution is one over s, and the remaining part involves sine. For sine, the boundary contribution vanishes, and the remaining part involves cosine. The resulting two linear equations say: s times I equals one minus b times J, and s times J equals b times I. Solving them gives I equal to s divided by s squared plus b squared, and J equal to b divided by that same denominator.

Notice what we just did. We did not solve any differential equation. We evaluated two ordinary improper integrals. The algebraic denominators arose because differentiation swaps sine and cosine. That relationship is exactly what will make the same denominators appear when solving oscillators.

We now have a useful elementary table in words. A constant one transforms to one over s. An exponential of a t transforms to one over s minus a. A ramp t transforms to one over s squared. Cosine of b t transforms to s over s squared plus b squared. Sine of b t transforms to b over s squared plus b squared. Each entry comes with a convergence condition.

The transform is linear because the integral is linear. If a signal is two plus three times exponential of negative two t, minus cosine of three t, its transform is two over s, plus three over s plus two, minus s over s squared plus nine. We can handle the pieces separately because the integrals can be added wherever they all converge.

## The complex variable and the forgotten condition

So far s has been real. In the complete theory, s can have a real part and an imaginary part. Write s as sigma plus i omega. Then the weighting factor is a decaying exponential determined by sigma, multiplied by an oscillatory factor determined by omega. The transform can describe decay and frequency at once.

For an exponential of a t, where a is real, the convergence condition becomes that the real part of s is greater than a. We call this a half-plane of convergence. The rational expression one over s minus a can be evaluated algebraically at many points outside that half-plane, but those evaluations are not values of the defining one-sided integral there. The formula and its region of convergence are a pair.

For continuous signals with suitable growth, knowing F for all sufficiently large real s already determines the original signal. In practical calculations we recover f by recognizing known transform pairs, taking partial fractions, or applying convolution. We will not attempt the general inversion theorem here. The essential point is that the encoding has not discarded the original time behavior, even though it changes its form.

Why do we begin integration at zero? Because we are setting up an experiment with an initial time. A one-sided transform is not the same as a Fourier transform of a signal existing for all past and future time. In particular, the values at zero will enter automatically when we transform derivatives. That is the central benefit for initial-value equations.

## A consistency check from the first instant

There is a useful way to test our first transform table. Suppose f is continuous just after zero and has manageable growth. Make s very large. The weight exponential of negative s t rapidly suppresses every part of the signal except a narrow window near zero. In that window, f is close to its initial value. One expects s times F of s to approach f at zero from the right.

Our combined example begins at two plus three minus one, which is four. Its transform is two over s, plus three over s plus two, minus s over s squared plus nine. Multiply by s and let real s tend to positive infinity. The three contributions approach two, three, and negative one. The total is four, as expected.

This check does not mean that F of s is a point measurement of f. Every finite s still collects an entire weighted history. It only says the weighting concentrates near zero in a controlled limit. And it needs regularity near zero: a jump requires us to use the right-hand value, while more singular signals call for a different interpretation.

## Choosing a tool deliberately

How does this compare with Fourier series? Fourier coefficients ask how much of a particular repeating harmonic is present in a periodic function. The Laplace transform asks for an exponentially weighted history after an initial time. There is a connection between the two through complex frequencies, but neither is simply a synonym for the other.

If a pump switches on once, if a spring starts at a specified displacement, or if a circuit receives a brief pulse and then is left alone, the one-sided Laplace transform gives us a natural language for both the forcing and the initial state. It does not make nonlinear or variable-coefficient equations automatically solvable. And the existence of a transform does not guarantee an easy inverse.

The useful achievement is more modest and more powerful: we have derived a collection of exact transform pairs, learned to keep their convergence conditions attached, and seen why an integral over time can produce a rational function of a new variable. The next step is to find what this integral does to a derivative. That is where a differential equation turns into an algebraic one while retaining the information about how the motion began.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Prerequisites:** single-variable integration, exponentials, integration by parts, sine and cosine. **Convention:** one-sided Laplace transform on \(t\ge0\) for ordinary functions, with integration starting at \(0\).

### Definition and region of convergence

\[
F(s)=\mathcal L\{f\}(s)=\int_0^\infty e^{-st}f(t)\,dt,\quad s=\sigma+i\omega.
\]
If \(|f(t)|\le Me^{at}\) for sufficiently large \(t\), then the integral converges absolutely for \(\operatorname{Re}s>a\), assuming local integrability. This condition is sufficient, not necessary. The region of convergence is part of the transform data.

### Derived pairs

Each entry has its own half-plane of absolute convergence:
\[
\begin{array}{c|c|l}
f(t)&F(s)&\text{ROC}\\
\hline
1&1/s&\operatorname{Re}s>0\\
e^{at}&1/(s-a)&\operatorname{Re}s>a\\
t^n&n!/s^{n+1}&\operatorname{Re}s>0\\
\cos(bt)&s/(s^2+b^2)&\operatorname{Re}s>0\quad(b\ne0)\\
\sin(bt)&b/(s^2+b^2)&\operatorname{Re}s>0\quad(b\ne0)
\end{array}
\]
The polynomial rule for nonnegative integer \(n\) follows inductively by parts. If differentiation under the integral is justified, \(\mathcal L\{tf(t)\}(s)=-F'(s)\). For real \(s>0\), integration by parts gives \(sI=1-bJ\), \(sJ=bI\) for cosine/sine integrals \(I,J\); solve to obtain the last two pairs. If \(b=0\), use the zero/constant signal directly.

### Exact worked check

For \(f(t)=2+3e^{-2t}-\cos(3t)\),
\[
F(s)=\frac2s+\frac3{s+2}-\frac{s}{s^2+9},\qquad \operatorname{Re}s>0.
\]
Then \(\lim_{s\to+\infty}sF(s)=4=f(0+)\). More generally, this initial-value limit follows for continuous \(f\) near zero under an appropriate exponential-growth bound; it should not be applied naively to impulses.

### Exercises with answers

1. Compute \(\mathcal L\{4t+5\}\). **Answer:** \(4/s^2+5/s\), for \(\operatorname{Re}s>0\).
2. Compute \(\mathcal L\{e^{3t}\cos(2t)\}\). **Answer:** \((s-3)/((s-3)^2+4)\), with \(\operatorname{Re}s>3\), by replacing \(s\) with \(s-3\) in the cosine pair.
3. Does \(1/(s-2)\) equal the defining integral for \(f(t)=e^{2t}\) at \(s=1\)? **Answer:** No. The integral diverges; the rational expression alone is insufficient.
4. Use the definition to show that \(\mathcal L\{t\}=1/s^2\). **Answer:** Integration by parts gives \([-te^{-st}/s]_0^\infty+(1/s)\int_0^\infty e^{-st}\,dt=1/s^2\) for real \(s>0\).
5. For \(f(t)=3+2e^{-t}\), predict \(\lim_{s\to+\infty}sF(s)\). **Answer:** \(5\), its right-hand initial value.

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Laplace Transform: Basics](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/laplace-transform-basics/).
- MIT OpenCourseWare, *18.03SC*, [Fourier Series and Laplace Transform unit](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/).
- Wikipedia: [Laplace transform](https://en.wikipedia.org/wiki/Laplace_transform), [Region of convergence](https://en.wikipedia.org/wiki/Region_of_convergence).
