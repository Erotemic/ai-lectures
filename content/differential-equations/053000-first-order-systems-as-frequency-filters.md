# First-Order Systems as Frequency Filters: Solving with Periodic Inputs

<!-- BEGIN SPOKEN LECTURE -->

# First-Order Systems as Frequency Filters

Suppose you open and close a valve at a regular rhythm, switching the inflow to a tank from high to low and back again. The valve changes abruptly, but the liquid level cannot jump. A first-order differential equation turns that difference into a mathematical prediction. The forcing may have corners or jumps; the response need not have them.

We will solve a deliberately simple model in two ways. First, we will solve separately between the switching times and match the pieces. Then we will decompose the switching input into Fourier harmonics and calculate the response to each one. Both methods must describe the same physical trajectory. Comparing them shows what Fourier methods are actually doing and when their use is justified.

## A stable equation with an external input

Consider y prime plus two y equals f of t. Think of y as a deviation from an equilibrium level or temperature, and f as a suitably scaled input. When f is zero, the solution is a constant times the exponential of negative two t. Any initial deviation decays. The number two sets the response timescale: the unforced state loses a factor of e in half a unit of time.

If f is a constant, say positive one, the system approaches one half. If f is negative one, it approaches negative one half. The derivative contains two competing influences: the input pushes, while the term negative two y restores the state toward zero.

Now let f be a square wave with period two pi: positive one from zero to pi, then negative one from pi to two pi, repeating. The input jumps at every switching time, but the solution of a first-order equation with this bounded input remains continuous. Its slope changes abruptly; its level does not teleport.

We have enough elementary ODE machinery to solve this without mentioning Fourier series. During the positive half-cycle, y prime plus two y equals one. With y at time zero equal to some number a, the solution is one half plus a minus one half, multiplied by the exponential of negative two t. During the negative half-cycle, use the analogous formula with equilibrium negative one half, beginning from the value reached at pi.

This produces an exact piecewise solution for any initial condition. But after many cycles, the influence of the initial value fades. Any two solutions under the same input differ by a constant times the exponential of negative two t. So there is one attracting periodic response, and every other response approaches it.

## Find the periodic response by matching the halves

The forcing has a useful symmetry. Shift time forward by pi and the input changes sign. The unique periodic response must have the same half-wave antisymmetry: y at time t plus pi equals negative y at time t. We can use that to determine the starting value a without solving a long recurrence.

During the positive half, the value at pi is one half plus a minus one half, multiplied by q, where q is the exponential of negative two pi. Periodic half-wave symmetry requires that value to equal negative a. Solve for a: it is negative one half times one minus q divided by one plus q.

The fraction one minus q over one plus q is the hyperbolic tangent of pi. Thus the periodic solution begins at negative one half times hyperbolic tangent pi, approximately negative zero point four nine eight. By the end of the positive half, it has risen to positive zero point four nine eight. The state spends most of each half-cycle close to the appropriate equilibrium, with smooth exponential transitions after the switch.

This exact answer is a useful benchmark for a Fourier calculation. Whatever our harmonic method produces at time zero, it had better approach the same negative number.

## What happens to a single sinusoidal input?

Replace the square wave temporarily with a single sine wave of frequency n and amplitude B: y prime plus two y equals B times sine of n t. To find a particular response, try a sine with some coefficient A and a cosine with some coefficient C. We need both because differentiation swaps sine and cosine.

Differentiate the trial expression. Its sine coefficient after applying the operator 'differentiate, then add twice the original' is two A minus n C. Its cosine coefficient is n A plus two C. We want the sine coefficient to be B and the cosine coefficient to vanish.

Solving those two ordinary algebra equations gives A equal to two B divided by n squared plus four, and C equal to negative n B divided by n squared plus four. So the response is B divided by n squared plus four, multiplied by two sine of n t minus n cosine of n t.

This is the central calculation. The output oscillates at the same frequency as the input, but its amplitude is reduced to B divided by the square root of n squared plus four, and its phase lags behind the input. The lag angle has tangent n divided by two, with the angle between zero and a right angle for positive n.

At low frequency, the system nearly follows its instantaneous equilibrium: output roughly equals input divided by two. At high frequency, it cannot keep up. The amplitude shrinks roughly like B divided by n, and the phase lag approaches a quarter cycle. We call this a low-pass response: slow changes pass more strongly than rapid ones.

## Now put the square wave back

The alternating input is four divided by pi times sine of t, plus one third sine of three t, plus one fifth sine of five t, and so on through the odd harmonics. Because the differential equation is linear, we can apply the single-harmonic response calculation to each component and add the results.

For an odd harmonic n, the input coefficient is four divided by pi n. Its response has sine coefficient eight divided by the product of pi, n, and n squared plus four; its cosine coefficient is negative four divided by the product of pi and n squared plus four. In ordinary words: each harmonic's output is smaller than its input, and the amount of attenuation depends on frequency.

The first harmonic has input amplitude about one point two seven, but output amplitude only four divided by the product of pi and the square root of five, about zero point five seven. The third harmonic's input amplitude is roughly zero point four two, but its output amplitude is only about zero point one two. The fifth is smaller still. Most of the rounded output shape is carried by its lowest frequencies.

This is why an abruptly switched valve can produce a smoothly changing state. The physical equation acts as a filter on the high harmonics that are needed to create the input's sharp edge.

There is a mathematical bonus. The square-wave coefficients decay like one divided by n; the first-order system adds another factor that behaves like one divided by n at large n. The response coefficients therefore decay like one divided by n squared. The resulting series converges uniformly and absolutely for the output itself. The output is continuous, matching the piecewise solution we constructed. Its derivative is not continuous at a switch, so differentiating the infinite series exactly at the jump still needs care.

## A surprising identity at the switching time

At time zero, all sine terms vanish, so the Fourier expression for the periodic output contains only the cosine contributions. They sum to negative four divided by pi times the sum, over positive odd n, of one divided by n squared plus four.

But our piecewise calculation already found the same output: negative one half times hyperbolic tangent pi. Equating the answers gives an exact infinite-series identity. In effect, solving the same elementary ODE two different ways evaluates a sum that would otherwise look unrelated to the original model.

We do not need that identity to use the method. Its importance is as an independent check. The point-by-point solution and the frequency-by-frequency solution agree. We have not merely drawn two plausible-looking graphs; we have matched exact formulas for the same periodic trajectory.

If we start the physical system at y equal to zero instead of at its periodic starting value, there is one more ingredient. We must add a decaying multiple of the exponential of negative two t to the periodic response, chosen to make the initial value correct. The Fourier series gives the periodic particular solution, not automatically the solution of an arbitrary initial-value problem.

## The boundary between linear and nonlinear reasoning

Why did adding the responses work? The differential operator L defined by y prime plus two y is linear: L of a sum is the sum of L applied to each part. Multiplying an input by a constant also multiplies the corresponding particular response by that constant. This is the superposition principle.

If the model instead included a term like y squared, the response to the sum of two sine waves would not generally equal the sum of the two separate responses. The square introduces products of frequencies, which create additional harmonics. Fourier representations are still useful for nonlinear equations, but simple independent harmonic response is no longer an exact solution method.

The method also depends on stability and on what sense of convergence we can justify. For our positive decay coefficient, bounded periodic forcing produces a unique attracting periodic output. That statement is not true for every linear differential equation. A linear oscillator without damping, for example, can resonate with a harmonic and grow without bound.

The broader lesson is a practical one. Solve a simple input, understand its response, and use linearity to assemble more complicated inputs. Then restore whatever initial condition was actually specified. Fourier coefficients describe forcing; the differential equation determines how each frequency is transformed; the homogeneous solution carries the memory of the initial state. Those are three distinct pieces of the prediction.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** First-order linear ODEs, Fourier sine coefficients, exponential decay, basic trigonometry. **Equation:** \(y'+ay=f(t)\) with \(a>0\). We use \(a=2\) and a square wave for exact calculations.

### The response to one harmonic

For \(y'+ay=B\sin(nt)\), trial \(y=A\sin nt+C\cos nt\) gives
\[
 aA-nC=B,\quad nA+aC=0,\quad
 A=\frac{aB}{a^2+n^2},\quad C=-\frac{nB}{a^2+n^2}.
\]
The steady harmonic amplitude is \(|B|/\sqrt{a^2+n^2}\) and for \(B>0\) the lag is \(\phi=\arctan(n/a)\), i.e. \(y_p=\frac B{\sqrt{a^2+n^2}}\sin(nt-\phi)\). If the input is \(f(t)=\sum b_n\sin nt\), linearity yields a periodic response by summing these particular solutions when the series converges appropriately. The full IVP solution is \(y(t)=y_p(t)+[y(0)-y_p(0)]e^{-at}\).

### Exact response to square-wave switching

Let \(s(t)=+1\) for \(0<t<\pi\) and \(-1\) for \(\pi<t<2\pi\), periodically extended. With \(q=e^{-2\pi}\),
\[
 a_*=y_p(0)=-\frac12\frac{1-q}{1+q}=-\tfrac12\tanh\pi,
\quad y_p(t)=\frac12+(a_*-\frac12)e^{-2t}\quad (0\le t\le\pi),
\]
\[
 y_p(t)=-\frac12+(-a_*+\frac12)e^{-2(t-\pi)}\quad(\pi\le t\le2\pi).
\]
This is continuous and \(2\pi\)-periodic, and \(y_p(t+\pi)=-y_p(t)\). It is not differentiable at switching points: the derivative has a jump of the same size as the input jump.

From \(s(t)=(4/\pi)\sum_{n\ge1,\;n\,\mathrm{odd}}\sin(nt)/n\),
\[
 y_p(t)=\frac4\pi\sum_{n\ge1,\;n\,\mathrm{odd}}
\frac{2\sin(nt)/n-\cos(nt)}{n^2+4}.
\]
At \(t=0\):
\[
 -\frac4\pi\sum_{n\ge1,\;n\,\mathrm{odd}}\frac1{n^2+4}=-\frac12\tanh\pi,
\qquad \sum_{n\ge1,\;n\,\mathrm{odd}}\frac1{n^2+4}=\frac\pi8\tanh\pi.
\]
The harmonic series for \(y_p\) is absolutely and uniformly convergent (coefficients are \(O(n^{-2})\)). Differentiating at switching times is invalid in the classical pointwise sense; away from switches the ODE holds classically, and globally in the a.e./distributional sense.

### Exercises with answers

1. Solve \(y'+3y=2\cos t\) for its periodic response. **Answer:** \(y_p=(6\cos t+2\sin t)/10=\frac35\cos t+\frac15\sin t\). Check by differentiation.
2. For \(y'+2y=\sin(4t)\), find the output amplitude. **Answer:** \(1/\sqrt{20}\), while the input amplitude is one; the phase lag is \(\arctan 2\).
3. With square-wave forcing above, find the output at the end of the positive half-cycle. **Answer:** \(y_p(\pi)=\frac12\tanh\pi=-y_p(0)\).
4. If \(y(0)=0\) in the square-wave problem, what is the full solution? **Answer:** \(y(t)=y_p(t)+\frac12\tanh(\pi)e^{-2t}\), where \(y_p\) is the periodic function given above.

### Sources and additional reading

- MIT OpenCourseWare, *18.03SC*, ODEs with Periodic Input, Resonance: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/odes-with-periodic-input-resonance/
- MIT OpenCourseWare, *18.03SC*, Fourier Series: Basics: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/fourier-series-basics/
- Wikipedia: [Linear time-invariant system](https://en.wikipedia.org/wiki/Linear_time-invariant_system), [Low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter), [Fourier series](https://en.wikipedia.org/wiki/Fourier_series).
