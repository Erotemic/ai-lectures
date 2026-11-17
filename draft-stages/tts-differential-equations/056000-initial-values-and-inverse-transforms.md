# Initial Values Become Algebra: Derivatives, Partial Fractions, and Inverse Transforms

<!-- BEGIN SPOKEN LECTURE -->

# Initial Values Become Algebra

Suppose the temperature of a cooling object changes according to a first-order differential equation. We know the temperature at the instant the experiment starts and we know the heating schedule afterward. In ordinary calculus, we might solve the equation using an integrating factor. Laplace transforms offer another route, and this route becomes increasingly attractive when the heating turns on abruptly or when a system has several coupled decay rates.

The decisive calculation is not any transform table entry. It is the transform of a derivative. We will derive that rule, solve a first-order initial-value problem from beginning to end, and then tackle a second-order example in which a repeated denominator records a resonant exponential response. We will reverse every transform and check the resulting differential equation, rather than treating algebra in the new variable as the final answer.

## The boundary term that remembers the initial value

Start with the one-sided Laplace transform of x prime. That is the integral from zero to infinity of the exponential of negative s t multiplied by the derivative of x. Assume x is differentiable enough and grows slowly enough relative to the exponential weight that integration by parts is legitimate.

Choose the derivative of x as the term to integrate. The boundary term is the exponential of negative s t times x, evaluated at infinity and at zero. The contribution at infinity vanishes in the region where our transform exists. At time zero the exponential is one, and the lower endpoint contributes negative x at zero. The remaining integral is s times the transform of x.

So the transform of x prime is s times X of s, minus x at zero. The initial value has appeared as a boundary term. We did not have to insert it afterward by hand.

Apply the same rule to x double prime. The transform is s times the transform of x prime, minus x prime at zero. Substitute the rule we just found. The result is s squared times X, minus s times the initial position, minus the initial velocity.

This is the computational heart of the method. A first derivative turns into multiplication by s plus a correction that carries one initial value. A second derivative turns into multiplication by s squared plus corrections for two initial values. For a constant-coefficient linear equation, every derivative therefore becomes an algebraic term in X.

There is an important qualification. We are working with ordinary derivatives of a sufficiently regular signal on the open intervals where the equation holds. If a signal jumps, its derivative in the sense of distributions includes an impulse. We will treat jumps and impulses deliberately rather than applying the smooth rule across a discontinuity without explanation.

## One first-order equation, three descriptions

Solve the initial-value problem x prime plus two x equals three, with x at zero equal to one. We can already reason qualitatively. The equilibrium is three halves because a state at three halves has zero derivative. Starting at one, the solution should rise toward three halves and should never overshoot in this simple first-order model.

Transform the entire equation. The derivative becomes s X minus one. The term two x becomes two X. The constant forcing three transforms to three over s. Collect the unknown terms: s plus two, multiplied by X, equals one plus three over s.

Solve for X. We obtain s plus three divided by s times s plus two. That looks less recognizable than the original problem, so now we use partial fractions. Look for constants A and B such that X is A over s plus B over s plus two. Multiplying through by the common denominator gives s plus three equal to A times s plus two, plus B times s.

Set s equal to zero. Three equals two A, so A is three halves. Set s equal to negative two. One equals negative two B, so B is negative one half. Therefore X is three halves over s, minus one half over s plus two.

Each term matches a transform we derived directly from the integral. Three halves over s corresponds to the constant three halves. One over s plus two corresponds to the exponential of negative two t. The solution is three halves minus one half times that exponential.

Check it. At zero the exponential is one, so x is one, exactly the given initial value. Differentiate: x prime is the exponential of negative two t. Add twice x: the exponential plus three minus the exponential, which is three. And for positive time the exponential decreases from one to zero, so the solution indeed rises monotonically toward three halves. An initial-value solution should satisfy the original problem, not just have a plausible transform.

We have now solved the same type of equation that an integrating factor can solve. Why bother with the transform? Because the calculation makes the initial state and the forcing appear as separate algebraic contributions. When the forcing becomes a switched signal or an impulse, the transform approach will keep the same structure.

## A repeated pole and a growing factor of time

Consider a second-order equation with damping: x double prime plus three x prime plus two x equals the exponential of negative t. Set x at zero equal to zero and its initial velocity equal to one.

We transform term by term. The second derivative becomes s squared X minus one, because the initial position is zero and the initial velocity is one. Three times the first derivative becomes three s X. The last term becomes two X. The forcing has transform one over s plus one.

Collect terms. The polynomial s squared plus three s plus two multiplies X, and there is a negative one on the left. Move it to the right, producing one plus one over s plus one. The polynomial factors as s plus one times s plus two. Combining the right-hand terms gives s plus two over s plus one. A factor of s plus two cancels, leaving X equal to one over s plus one squared.

We know that one over s squared is the transform of t. Replacing s by s plus one corresponds to multiplying the original time function by the exponential of negative t. So x of t equals t times exponential of negative t.

Pause over that result. The forcing itself decays exponentially. The solution has an extra factor of t. This is the response to forcing at a decay rate already present in the homogeneous dynamics. The double factor in the transform denominator records the same phenomenon that we encountered with resonant trial solutions for ordinary differential equations.

Again we check it in time. x at zero is zero. Differentiate t times exponential of negative t: x prime is one minus t, multiplied by the exponential. At zero the velocity is one. The second derivative is t minus two, multiplied by the same exponential. Combine x double prime plus three x prime plus two x. The polynomial coefficient is t minus two plus three minus three t plus two t, which simplifies to one. The result is exactly the exponential forcing.

The repeated factor was not an inconvenience to eliminate. It told us the time solution would contain a polynomial factor multiplying an exponential. A repeated denominator squared corresponds to t times an exponential; a power of three corresponds to one half t squared times that exponential, provided the transform exists on the appropriate half-plane.

## Partial fractions are a way of recognizing dynamics

A rational transform is a quotient of polynomials in s. The roots of the denominator often correspond to decay rates and oscillation frequencies of the underlying linear system. Partial fractions break a complicated quotient into pieces whose inverse transforms we know.

For distinct real factors, we use terms such as A over s plus one and B over s plus two. For a repeated factor, we must include every power: A over s plus one and B over s plus one squared, for example. For a quadratic corresponding to oscillation, such as s squared plus four, the numerator may involve a constant and a multiple of s. Those combinations correspond to sines and cosines.

Take one more compact example: x double prime plus four x equals zero, with initial displacement zero and initial velocity two. Transforming gives s squared X minus two plus four X equals zero. Thus X equals two over s squared plus four. The sine transform with frequency two is precisely two over s squared plus four. So x is sine of two t. This is a complete solution, not merely a steady-state guess, because the initial velocity was built into X.

A useful practical discipline is to inspect the transformed equation before inverting it. Does the algebraic numerator have the correct initial-data terms? Does the denominator factor correctly? Does a pole cancel because the forcing and initial conditions happen to align? And can we check the answer by direct substitution in time? These questions catch many errors that a table lookup cannot.

## What the algebra does not promise

Laplace transforms are especially comfortable with linear differential equations whose coefficients do not depend on time. If a coefficient itself varies with t, multiplication by that coefficient generally does not turn into multiplication by a simple number in s. If the equation contains x squared, the transform of that product is not just X squared. One cannot mechanically transform an arbitrary nonlinear equation into elementary algebra.

Even in the constant-coefficient case, the inverse may require more work than a few partial fractions. Nonrational inputs can produce nonrational transforms, and some inverse transforms are naturally represented by integrals. We will soon learn convolution, which gives a direct time-domain interpretation of those products.

Finally, the formula for a derivative encodes the value at the start of the observation interval. If we move the origin or switch a force at a later time, we must keep that timing straight. A step at time two is not the same as a new initial value at time zero.

Here is the essential idea to carry forward. A derivative becomes multiplication by s, corrected by boundary values that record the initial state. The differential equation becomes an algebraic equation for X. Inverting X converts algebraic factors back into time behavior. We still verify the original initial conditions and equation. That discipline will let us handle a forcing schedule with sharp changes without losing track of what actually happens at the switching times.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Prerequisites:** 055000, integration by parts, first-order linear ODEs, the characteristic equation for a constant-coefficient oscillator. **Convention:** \(X(s)=\mathcal L\{x(t)\}\) for \(t\ge0\).

### Derivative rules

Assume \(x,x'\) are piecewise smooth, of sufficient exponential order, with the appropriate boundary terms vanishing in the ROC. For ordinary solutions with no interior jumps,
\[
\mathcal L\{x'\}=sX(s)-x(0+),\qquad
\mathcal L\{x''\}=s^2X(s)-s x(0+)-x'(0+).
\]
The first formula follows from
\[
\int_0^\infty e^{-st}x'(t)\,dt=[e^{-st}x(t)]_0^\infty+s\int_0^\infty e^{-st}x(t)\,dt.
\]
When jump discontinuities are present, use appropriate interval-by-interval integration or distributional derivatives; do not silently apply a smooth identity through an interior jump.

### First-order full solution

For \(x'+2x=3\), \(x(0)=1\):
\[
(s+2)X=1+\frac3s,\quad X=\frac{s+3}{s(s+2)}=\frac{3}{2s}-\frac1{2(s+2)},
\]
\[
x(t)=\frac32-\frac12e^{-2t},\quad x(0)=1,\quad x'+2x=3.
\]

### Second-order repeated factor

For \(x''+3x'+2x=e^{-t}\), \(x(0)=0\), \(x'(0)=1\):
\[
\bigl(s^2+3s+2\bigr)X-1=\frac1{s+1},
\quad X=\frac{1+1/(s+1)}{(s+1)(s+2)}=\frac1{(s+1)^2},
\]
\[
x(t)=te^{-t},\quad x'(t)=(1-t)e^{-t},\quad x''(t)=(t-2)e^{-t}.
\]
Substitution yields \((t-2)+3(1-t)+2t=1\), so the equation holds. This is not an arbitrary cancellation; the initial conditions select the simple resonant form.

For \(n\ge1\), \(\mathcal L\{t^{n-1}e^{at}/(n-1)!\}=1/(s-a)^n\) for \(\operatorname{Re}s>a\).

### Exercises with answers

1. Solve \(y'+3y=6\), \(y(0)=0\). **Answer:** \(Y=6/[s(s+3)]=2/s-2/(s+3)\), hence \(y=2(1-e^{-3t})\).
2. Solve \(y''+4y=0\), \(y(0)=0\), \(y'(0)=2\). **Answer:** \(Y=2/(s^2+4)\), \(y=\sin(2t)\).
3. Find the inverse transform of \(2/(s+1)^3\). **Answer:** \(t^2e^{-t}\), because \(\mathcal L\{t^2e^{-t}\}=2/(s+1)^3\).
4. Determine \(\mathcal L\{x''+5x'\}\) if \(x(0)=3\) and \(x'(0)=-1\). **Answer:** \((s^2+5s)X-3s+1-15=(s^2+5s)X-3s-14\).
5. Is \(\mathcal L\{x(t)^2\}=[X(s)]^2\) generally true? **Answer:** No; products in time do not transform into ordinary pointwise products of their Laplace transforms.

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Laplace Transform: Solving Initial Value Problems](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/laplace-transform-solving-initial-value-problems/).
- MIT OpenCourseWare, *18.03SC*, [Partial Fractions and Inverse Laplace Transform](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/partial-fractions-and-inverse-laplace-transform/).
- Wikipedia: [Inverse Laplace transform](https://en.wikipedia.org/wiki/Inverse_Laplace_transform), [Partial fraction decomposition](https://en.wikipedia.org/wiki/Partial_fraction_decomposition).
