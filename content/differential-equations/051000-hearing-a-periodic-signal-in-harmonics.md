# Hearing a Periodic Signal in Harmonics: Fourier Coefficients from Scratch

<!-- BEGIN SPOKEN LECTURE -->

# Hearing a Periodic Signal in Harmonics

Imagine a motor that pulls for half a second, pushes for half a second, and repeats. The force is periodic, but it is not a sine wave. If you want to predict how a spring responds, you could try to solve the differential equation separately on every half-second interval and match the solutions at every switch. That works, but there is another possibility: describe the repeating force as a combination of simpler repeating forces, solve for each one, and add the results.

Why would that help? A sinusoidal force is especially convenient for a linear differential equation with constant coefficients. Differentiate a sine and you get a cosine; differentiate again and you get the negative of the original sine. The equation stays within a small family of functions. Fourier series let us use this advantage even when the actual force has corners, sudden jumps, or a complicated repeating pattern.

To understand them, we first need to know what the coefficients mean. They are not mysterious numbers pulled out of a table. They come from measuring how strongly the function lines up with each possible harmonic.

## Period, frequency, and a family of building blocks

Take a function that repeats every two pi units of time. Two pi is its period. Its fundamental angular frequency is one radian per unit time. A sine wave of twice that frequency completes two cycles during the same interval; a sine wave of three times the frequency completes three cycles. We call these higher frequencies the second and third harmonics.

For a signal with a general period T, the fundamental angular frequency is two pi divided by T. The n-th harmonic is n times that angular frequency. We also need a constant term, because the signal might spend more time above zero than below it.

A proposed Fourier description consists of a constant, followed by a cosine and sine at the fundamental frequency, then a cosine and sine at twice that frequency, then at three times it, and so on. At first this is just a proposed way of describing a signal. We have not yet proved that every reasonable periodic function can be reconstructed from these terms, nor have we explained what reconstruction means at a jump.

Start with a finite collection. Imagine choosing some coefficients and trying to fit a recorded repeating signal. How would you tell how much of the first sine wave to use, without contaminating the answer with the other frequencies?

## Why the harmonics do not interfere when averaged

Multiply sine of t by sine of two t, and average the product over a full two-pi period. The positive and negative contributions cancel. The result is zero. The same thing happens for sine waves of any two different positive integer frequencies. Two cosine waves at different harmonic frequencies also average to zero. Sine and cosine waves average to zero against one another, even at the same frequency.

But a sine wave multiplied by itself has a positive average: one half. So does a cosine multiplied by itself. The constant function one has average one, and its average product with every nonconstant harmonic is zero.

This property is called orthogonality. In ordinary geometry, perpendicular vectors have a zero dot product. Here the role of a dot product is played by the average, over one period, of the product of two functions. The functions are our vectors. We are not merely borrowing a word: the same geometric calculation that finds a component of a vector along an axis finds a Fourier coefficient along a sine or cosine.

Suppose the signal is f of t. To find its constant contribution, average f over one period. To find the coefficient of cosine of n t, multiply f by that cosine, integrate over one complete period, and divide by pi. Do the same with sine to obtain its coefficient. The division by pi corrects for the fact that the integral of sine squared, or cosine squared, over a two-pi interval is pi.

Notice the conventions. In the usual notation, the constant is written a-zero divided by two. Then a-zero itself is one divided by pi times the integral of f, while the actual average is a-zero divided by two. The sine and cosine coefficients use one divided by pi times their respective integrals. Different books sometimes call the average itself a-zero. Both conventions are valid; confusing them produces an immediate factor-of-two error.

## A square wave built from sines

Our example will be an idealized alternating force. Let f be negative one between negative pi and zero, and positive one between zero and pi, then repeat every two pi. Its values at the switching instants do not affect any of the integrals, so we can set those isolated values to zero if we want a convention.

This signal is odd: reflect time across zero and the sign changes. Cosine is even, so the positive and negative pieces of f times cosine cancel. All cosine coefficients vanish. The average also vanishes. Only sine terms remain.

Let's calculate one of them instead of accepting a memorized result. The coefficient of sine of n t is one divided by pi times the integral of f times sine of n t from negative pi to pi. Because the product is even, this becomes two divided by pi times the integral of sine of n t from zero to pi. Its antiderivative is negative cosine of n t divided by n. Evaluate at the endpoints: we get two divided by pi n, multiplied by one minus negative one to the power n.

That last factor decides everything. For even n, negative one to the power n is positive one, so the coefficient is zero. For odd n, the factor is two, so the coefficient is four divided by pi n. The square wave is therefore represented by four divided by pi times sine of t, plus one third sine of three t, plus one fifth sine of five t, and the remaining odd harmonics.

The first harmonic has amplitude about one point two seven. It must be larger than one because a single sine wave rounds away the flat top of the square wave and compensates by rising a little higher near the middle. Adding the third and fifth harmonics reshapes it, flattening much of the top and sharpening the transitions. The signs of those terms vary over time, so adding more harmonics does not simply raise the graph everywhere.

We have learned a structural fact: an alternating signal with a sharp switch contains arbitrarily high odd frequencies. That is why a motor or electronic circuit that appears to switch at a single repetition rate can excite several different vibration modes.

## Symmetry saves work

Before integrating any coefficient, look at the shape. If a signal is even around the chosen time origin, its sine coefficients vanish; if it is odd, its cosine coefficients and average vanish. If it has half-wave symmetry, meaning that advancing by half a period reverses its sign, all even-numbered harmonics vanish. Our square wave has both odd symmetry and half-wave symmetry, so the calculation could hardly be simpler.

Time origin matters. Shift the same square wave a quarter period, and what used to be a sine series may become a cosine series. The physical waveform has not changed, but its coefficients relative to the clock have. A time shift changes the phases of harmonics. The sizes of the harmonics stay the same.

For a practical force measured in newtons, the Fourier coefficients also have units of newtons. The sines and cosines themselves are dimensionless. The angular frequency has units inverse time, commonly radians per second, whereas ordinary frequency counts cycles per second. Keeping those units straight will matter when we compare a driving frequency to the natural frequency of a spring.

## A gentler example: a triangular shape

Not every periodic signal has a jump. Consider the function that equals the absolute value of t from negative pi to pi, then repeats. Its graph descends toward a pointed minimum at zero and rises toward a maximum at each end of the interval. The function is continuous at the join because both ends have the same value, but its slope changes suddenly there.

This function is even, so only cosines appear. Its average is pi divided by two. Integrating t times cosine of n t by parts gives a cosine coefficient equal to two divided by pi n squared times negative one to the power n minus one. The coefficient vanishes for even n and equals negative four divided by pi n squared for odd n.

So this triangular signal has a constant of pi divided by two, followed by negative four over pi times cosine of t, plus one ninth cosine of three t, plus one twenty-fifth cosine of five t, and so forth, with the negative factor applying to the entire parenthesis.

Compare the two examples. The square wave's nonzero harmonic amplitudes shrink like one divided by n. The continuous triangular wave's shrink like one divided by n squared. This is a hint of a much wider principle: smoother signals generally have weaker high-frequency components. But do not promote that hint into a universal theorem without hypotheses. The precise decay depends on how derivatives behave and which boundary values match across the period.

## What have we actually built?

We have calculated a list of coefficients. We have not yet proved that infinitely many terms really reconstruct the square wave at every point. At a switching instant, a continuous sum of a finite number of sine waves cannot make an exact jump. With more and more terms, a narrow oscillatory region develops near that discontinuity. We need to understand convergence before trusting what the series says there.

Still, the central construction is now clear. Periodicity tells us which frequencies can appear. Orthogonality extracts their coefficients. Symmetry eliminates many unnecessary integrals. The square wave and triangular wave show how much information about shape is carried in the relative sizes of the harmonics.

When we return to differential equations, the gain is substantial. Instead of asking an oscillator to respond to a complicated periodic input all at once, we can ask how it responds to each sine wave separately. But that next calculation must respect both the mathematics of infinite sums and the physics of transients. A Fourier description of the input is only the beginning of a solution, not the whole solution.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** Integration by parts, parity, basic trigonometry, a first forced oscillator. **Convention:** period \(2\pi\); \(f\sim a_0/2+\sum_{n\ge1}(a_n\cos nt+b_n\sin nt)\).

### Frequencies and coefficients

For period \(T\), \(\omega_0=2\pi/T\). Over any interval of length \(T\),
\[
\frac{a_0}{2}=\frac1T\int_{t_0}^{t_0+T} f(t)\,dt,\quad
 a_n=\frac2T\int_{t_0}^{t_0+T}f(t)\cos(n\omega_0t)\,dt,\quad
 b_n=\frac2T\int_{t_0}^{t_0+T}f(t)\sin(n\omega_0t)\,dt.
\]
In the standard \(2\pi\)-periodic case this is \(a_n=\pi^{-1}\int_{-\pi}^{\pi}f\cos(nt)\), etc. Direct integration gives, for integers \(n,m\ge1\),
\[
\int_{-\pi}^{\pi}\sin(nt)\sin(mt)\,dt=\pi\delta_{nm},\quad
\int_{-\pi}^{\pi}\cos(nt)\cos(mt)\,dt=\pi\delta_{nm},\quad
\int_{-\pi}^{\pi}\sin(nt)\cos(mt)\,dt=0.
\]

### Square wave

Define \(s(t)=\operatorname{sgn}(\sin t)\) away from switching times. Then
\[
 a_0=a_n=0,\qquad b_n=\frac{2}{\pi n}(1-(-1)^n),\qquad
 s(t)\sim\frac4\pi\sum_{k=0}^\infty\frac{\sin((2k+1)t)}{2k+1}.
\]
The series converges to \(s(t)\) at continuity points and to \(0\) at jumps (the average of lateral limits). The value assigned to \(s\) at an isolated jump does not change its coefficients.

### Continuous triangular wave

For \(g(t)=|t|\) on \([-\pi,\pi]\), periodically extended,
\[
 \frac{a_0}{2}=\frac\pi2,\quad b_n=0,\quad
 a_n=\frac2{\pi n^2}((-1)^n-1),\quad
 g(t)=\frac\pi2-\frac4\pi\sum_{k=0}^\infty \frac{\cos((2k+1)t)}{(2k+1)^2}.
\]
The last series converges absolutely and uniformly. Its endpoints have the same value, making the periodic extension continuous.

### Exercises with answers

1. If \(T=4\) seconds, what are the first three positive angular frequencies? **Answer:** \(\pi/2,\pi,3\pi/2\) radians per second.
2. Let \(h(t)=2+3\cos(2t)-\sin(5t)\). List its Fourier coefficients in the \(a_0/2\) convention. **Answer:** \(a_0=4,a_2=3,b_5=-1\), all other coefficients zero.
3. What happens to \(s(t)\)'s coefficients when you replace it by \(s(t-\pi/2)\)? **Answer:** \(s(t-\pi/2)\) is even and has only odd cosine harmonics. More generally time shift \(\tau\) rotates each harmonic's pair of coefficients by angle \(n\tau\), preserving the magnitude \(\sqrt{a_n^2+b_n^2}\).
4. Show that \(g(0)=0\) follows from its Fourier series. **Answer:** \(0=\pi/2-(4/\pi)\sum_{k\ge0}(2k+1)^{-2}\); equivalently \(\sum_{k\ge0}(2k+1)^{-2}=\pi^2/8\).

### Sources and additional reading

- MIT OpenCourseWare, *18.03SC Differential Equations*, Fourier Series: Basics: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/fourier-series-basics/
- MIT OpenCourseWare, *18.03SC*, Operations on Fourier Series: https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/operations-on-fourier-series/
- Wikipedia: [Fourier series](https://en.wikipedia.org/wiki/Fourier_series), [Harmonic](https://en.wikipedia.org/wiki/Harmonic), [Orthogonality](https://en.wikipedia.org/wiki/Orthogonality).
