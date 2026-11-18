# Trigonometry as Rotation, Motion, and Signal

**Track:** Functions, Scales, and Mathematical Modeling  
**Lecture:** 003000  
**Preparation:** Coordinates, functions, circles, and proportions.  
**Companion:** Radians, phase, angular frequency, and aliasing.

<!-- BEGIN SPOKEN LECTURE -->

Imagine a point moving around the rim of a wheel at a steady rate. Put a lamp beside the wheel and watch the point's shadow moving up and down a wall. The point travels along a circle; the shadow travels back and forth along a line. The shadow slows near its highest and lowest positions and speeds up near the middle. Its motion is smooth, repeating, and described by one of the most important functions in mathematics: sine.

Trigonometry can begin with triangles, but the rotating wheel gives us a more general foundation. Draw a circle of radius one centered at the origin of the coordinate plane. Start at the point with horizontal coordinate one and vertical coordinate zero. Rotate counterclockwise by an angle theta. The new point's horizontal coordinate is cosine of theta, and its vertical coordinate is sine of theta. In other words, sine and cosine are the two coordinate functions of rotation on a unit circle.

A full turn is three hundred sixty degrees, or two pi **radians**. A radian measures an angle by the length of the arc it cuts off on the unit circle. On a circle of radius r, an arc of length s corresponds to an angle of s divided by r radians. Unlike degrees, radians interact directly with the geometry of lengths and with the derivatives of trigonometric functions. When we write sine of t in calculus, t is interpreted as a dimensionless angle in radians unless a convention is explicitly supplied.

At an angle of zero, cosine is one and sine is zero. At a quarter-turn, cosine is zero and sine is one. At a half-turn, cosine is negative one and sine is zero. At three quarters of a turn, sine is negative one. The circle makes the signs and repetitions understandable without memorizing a table of isolated values.

Rotate the point by one full turn and the coordinates return to their earlier values. So sine and cosine repeat whenever the angle increases by two pi. This repetition is their **periodicity**. A function has period P if shifting its input by P never changes its output. It may have several periods; for a nonconstant sine wave, two pi is its smallest positive period as a function of the angle in radians.

What if the wheel rotates twice as quickly? The angle accumulated after time t becomes two times what it was before. The vertical shadow is sine of two t if time is measured so that the original angular speed was one radian per time unit. That shadow completes its cycles twice as fast. More generally, a signal is modeled by A times sine of the quantity omega t plus phi, with perhaps a constant vertical offset. A sets the amplitude, omega sets the angular frequency, and phi shifts the phase. The amplitude is the distance from the midline to a peak, not the full distance from trough to peak.

There are two related measures of frequency. Ordinary frequency f counts cycles per second, measured in hertz. Angular frequency omega measures radians per second. Since one cycle is two pi radians, omega equals two pi times f. A five-hertz tone completes five oscillations each second; its angular frequency is ten pi radians per second. Mixing these units introduces an error by a factor of two pi.

Phase requires care too. The expression sine of the quantity omega t plus phi has a phase offset phi in radians. A time shift of tau instead gives sine of omega times the quantity t minus tau. These are equivalent descriptions if phi equals negative omega tau. One second of delay means a different phase angle at one hertz than at one hundred hertz. Phase is not simply another word for delay.

Now consider two rotating wheels. One might have a larger radius, giving a taller shadow. One might rotate more rapidly. If we add their shadows, the resulting motion can be more intricate than either individual sine wave. Adding two oscillations with the same frequency can still produce a single oscillation at that frequency, with a changed amplitude and phase. Adding oscillations at different frequencies generally produces a shape that is not a single sine wave. That fact is one of the doorways to Fourier analysis: a complicated signal can often be represented by a sum of simpler periodic components.

A trigonometric identity can be understood as geometry. Cosine squared plus sine squared equals one because every point on the unit circle satisfies the equation horizontal coordinate squared plus vertical coordinate squared equals one. The addition formulas come from composing rotations: rotating by angle a and then angle b is the same as rotating once by their sum. Identities are not just arbitrary symbols to manipulate. They record facts about transformations.

The wave picture has practical limits. A real pendulum does not move with a perfect sine wave at large angular amplitudes. Its equation involves the sine of its angle, and the familiar simple harmonic approximation replaces that sine by the angle itself when the angle is small. The trigonometric function appears in the underlying geometry, but the time course of the motion is approximately sinusoidal only under the stated approximation.

A more surprising limit comes from observation. Suppose we sample a periodic signal ten times every second, recording the values at times zero, one tenth of a second, two tenths, and so on. A one-hertz sine wave and an eleven-hertz sine wave have the same values at all those sample times: the extra ten cycles per second contribute a whole number of turns between samples. Without further assumptions, the sampled data cannot distinguish them. This is an instance of **aliasing**.

The problem is not that the measuring device is inaccurate. Even exact samples can be ambiguous. To reconstruct a signal from uniform samples, we need a limit on the frequencies present and a sampling rate high enough relative to that limit, together with the hypotheses of the reconstruction theorem. In practice this is why recording systems use anti-aliasing filters before sampling. It is also why a spinning wheel may appear to turn backward in a film: successive images can represent several different motions between frames.

Trigonometry is therefore a language of coordinate geometry, of circular motion, of oscillation, and of signals. The same sine and cosine functions will later appear as solutions of differential equations, as vectors in spaces of functions, and as eigenfunctions of operations such as differentiation and translation. But the foundation remains concrete: one angle, one rotating point, two coordinates, and a repeatable way to describe change.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(\theta\) in radians, define \((\cos\theta,\sin\theta)\) as coordinates of the unit-circle point at angle \(\theta\). Then \(\cos^2\theta+\sin^2\theta=1\), and the rotation matrix is \(R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}\), with \(R_aR_b=R_{a+b}\).

For \(y(t)=b+A\sin(2\pi f t+\phi)\), where \(t\) is seconds: \(A\) is a signed coefficient, amplitude is \(|A|\), \(f>0\) is cycles/second, period is \(1/f\), and \(\phi\) is a dimensionless phase in radians. Writing \(y(t)=b+A\sin(\omega t+\phi)\) uses \(\omega=2\pi f\) in radians/second.

**Aliasing calculation.** At samples \(t_n=n/f_s\), \(\sin(2\pi(f+k f_s)t_n)=\sin(2\pi f n/f_s+2\pi kn)=\sin(2\pi f n/f_s)\) for every integer k. For \(f_s=10\) Hz, 1 Hz and 11 Hz sine waves sampled at the same phases agree. Shannon sampling guarantees require a bandwidth restriction and appropriate sampling hypotheses; the algebra above only demonstrates nonuniqueness without them.

### Exercises and solutions

1. **Period.** Find the period of \(3\sin(4\pi t)\) for \(t\) in seconds. **Solution:** \(f=2\) Hz, so \(P=1/2\) second.
2. **Rotation.** What is \(\sin(\pi/2)\) and why? **Solution:** one, the height of the unit-circle point after a quarter-turn.
3. **Phase and time.** Express \(\sin(2\pi(t-0.25))\) as \(\sin(2\pi t+\phi)\). **Solution:** \(\phi=-\pi/2\) (modulo \(2\pi\)).
4. **Aliasing.** At a sampling rate of 8 samples/second, give two positive frequencies that yield identical sampled sine values. **Solution:** 1 and 9 Hz at the same phase, since their difference is 8 Hz.

### Reading and attribution

- OpenStax, *Precalculus 2e*, Chapters 5–8, unit-circle, trigonometric functions, and identities: https://openstax.org/books/precalculus-2e/pages/preface.
- MIT OpenCourseWare, *Signals and Systems*, introductory Fourier and sampling notes: https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/.
- The shadow-on-a-wall explanation and sample-frequency example are original exposition.
