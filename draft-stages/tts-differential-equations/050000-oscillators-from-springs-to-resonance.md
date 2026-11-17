# Oscillators from Springs to Resonance: A First Worked Second-Order Course

<!-- BEGIN SPOKEN LECTURE -->

# Oscillators from Springs to Resonance

A weight on a spring is pulled away from its resting position and released. At first it moves toward the middle. At the middle it is moving fastest, so it overshoots. It reverses and comes back. The position is changing, but knowing only the position is not enough to predict what happens next. We must also know the velocity.

That is the new ingredient in a second-order differential equation. The acceleration depends on the state, and the state now includes two quantities: position and velocity. Oscillators are a useful place to learn this because the mathematics has a clear mechanical interpretation, and because the same equations recur in electrical circuits, sound, feedback systems, and many other settings.

## From forces to an equation

Let x be displacement from equilibrium. The simplest spring law says that the force points back toward equilibrium and has magnitude proportional to displacement. In words, force equals negative k times x, where k is a positive spring stiffness. Newton's second law says force equals mass times acceleration. Combining them, mass times x double prime plus k times x equals zero.

Divide through by mass. Write omega zero squared for k divided by mass. Our equation becomes x double prime plus omega zero squared times x equals zero. The constant omega zero has units inverse seconds and is called the natural angular frequency. It is not the same as ordinary frequency in cycles per second. One cycle uses two pi radians, so the ordinary frequency is omega zero divided by two pi.

Before solving, see what the law predicts. If x is positive, the acceleration is negative, toward the center. If x is negative, acceleration is positive. But neither statement says whether the mass is moving left or right at that instant. That requires velocity. A second-order initial-value problem therefore needs two initial numbers, such as position at time zero and velocity at time zero.

## Why sines and cosines appear

The cosine function has a special property: differentiate it twice and the result is negative the original cosine, multiplied by the square of the frequency. The sine function has the same property. So any combination of a cosine at angular frequency omega zero and a sine at that frequency solves the oscillator equation.

Write the general solution as A times cosine of omega zero t plus B times sine of omega zero t. The constants A and B encode the two pieces of initial data. At time zero, cosine is one and sine is zero, so x at zero is A. Differentiate: the velocity at time zero is omega zero times B. Hence A is the starting displacement and B is the starting velocity divided by omega zero.

For a concrete example, let omega zero equal two radians per second. Start one meter to the right of equilibrium with zero velocity. Then A equals one and B equals zero. The position is cosine of two t. The velocity is negative two times sine of two t. At time zero the position is one meter, the velocity zero, and acceleration negative four meters per second squared. At time one quarter of the period, the position is zero and the velocity is negative two meters per second.

The period is two pi divided by omega zero, so here it is pi seconds. After pi seconds the mass has completed one full oscillation. If you mistakenly took omega zero equal to two to mean two complete cycles per second, you would predict the wrong period by a factor of two pi.

## Energy checks the motion

An ideal spring stores potential energy equal to one half k times displacement squared. The mass has kinetic energy equal to one half mass times velocity squared. Add them to obtain total mechanical energy.

Differentiate this total energy with respect to time. The derivative is mass times velocity times acceleration plus k times displacement times velocity. Factor out velocity. What remains is mass times acceleration plus k times displacement, which is zero by the oscillator equation. So the total energy stays constant.

In our example with mass one and k equal to four, the total energy initially is two joules: all in the stretched spring and none in motion. At the center, displacement is zero and velocity has magnitude two, so the kinetic energy is also two joules. Energy has moved from potential to kinetic and back, without disappearing.

This energy calculation is more than an illustration. It independently checks the exact solution. If you derive a candidate that gains energy while supposedly obeying an undamped and unforced ideal spring equation, something is wrong with your calculation or assumptions.

## Damping: when the oscillation dies away

Real systems often lose energy to friction or resistance. A common approximation adds a force proportional to velocity and opposite to the motion. With mass one, write the equation as x double prime plus two beta times x prime plus omega zero squared times x equals zero. Beta is positive and has units inverse seconds.

The mathematical structure changes. We now look for exponential solutions. Substituting an exponential of r times t gives a quadratic equation for r: r squared plus two beta r plus omega zero squared equals zero. Its roots determine what the motion looks like.

If beta is smaller than omega zero, the roots have negative real part and a nonzero imaginary part. The motion oscillates with an exponentially shrinking envelope. We call it underdamped. If beta equals omega zero, the roots coincide and the solution has an exponential multiplied by a linear function of time. We call it critically damped. If beta exceeds omega zero, both roots are real and negative: a sum of two decays, without oscillation. That is overdamping.

Critical damping does not mean that the system always reaches equilibrium at a finite time. It still approaches equilibrium asymptotically. In a standard spring-mass model it marks the boundary between oscillatory and nonoscillatory responses. Saying that it is 'the fastest possible return' without specifying the initial conditions and the metric for return would be too imprecise.

Here is an exact example. Take x double prime plus four x prime plus four x equals zero. The repeated root is negative two. The general solution is an exponential of negative two t multiplied by C plus D times t. If x starts at one with zero velocity, the constants are C equal to one and D equal to two. The motion is one plus two t, multiplied by the exponential of negative two t. It stays positive and declines toward zero, without overshooting.

For an underdamped example, take x double prime plus two x prime plus five x equals zero, again with initial displacement one and zero velocity. Its roots are negative one plus or minus two times the imaginary unit. The actual real-valued motion is the exponential of negative t multiplied by cosine of two t plus one half sine of two t. You can differentiate it at time zero and confirm that the two terms cancel in the velocity. Its oscillations continue but their envelope decays.

Damping also has a clean energy interpretation. For the damped equation, the derivative of mechanical energy is negative two beta times mass times velocity squared. It is nonpositive. Energy is being removed whenever the mass moves. This explains decay without relying only on the algebra of quadratic roots.

## Forcing: the outside world pushes back

Suppose a motor or periodic external force keeps nudging the system. The equation becomes x double prime plus four x equals a forcing function of time. We'll first ignore damping so we can see the most important phenomenon clearly.

Let the forcing be cosine of t. Its frequency is one radian per second, different from the system's natural frequency two. Try a response proportional to cosine of t. Substitution gives three times the unknown coefficient, so one-third cosine of t is a particular response.

If the mass starts at rest at the center, the total solution must also include a natural oscillation to satisfy the initial conditions. The answer is one-third cosine of t minus one-third cosine of two t. Check it: at time zero the two terms cancel, and their derivatives vanish. Apply the operator 'differentiate twice, then add four times the original': the natural-frequency term cancels out, leaving cosine of t. We have separately identified the forced motion and the adjustment required by the initial state.

Now drive the system at its own natural frequency: x double prime plus four x equals cosine of two t. Our earlier trial, a constant times cosine of two t, fails because cosine of two t is already a solution of the homogeneous equation. The operator kills it. Instead, multiply by time. A particular solution is one quarter t times sine of two t.

Start at the center with zero velocity, and this particular solution already satisfies both initial conditions. The amplitude grows in proportion to time while the motion oscillates. That is resonance in the ideal undamped model. The external force repeatedly injects energy with a favorable timing, and without damping there is no mechanism balancing that input.

Actual devices do not generally grow without limit under an arbitrarily long sinusoidal drive. Damping, nonlinearities, material limits, or changes in the forcing eventually matter. The unbounded growth is a property of the idealized linear undamped equation, not a literal prediction for a physical spring forever.

## Damped forcing and a preferred response

Add damping back. For a sinusoidal input at a fixed frequency, the long-time response of a stable damped oscillator is sinusoidal at that same frequency. Its amplitude and phase depend on the difference between driving frequency and natural frequency, and on the damping strength. The transient part remembers the initial state, but decays away.

There is a direct analogy with the first-order equation y prime plus y equals t. In both cases, the general solution is a particular response to the input plus a decaying response determined by initial data. The difference is that an oscillator can exchange energy between two state variables and display resonance.

Why does this lead naturally toward Fourier methods? Because a complicated repeating input can be decomposed into sinusoidal components. For a linear oscillator, we can determine the response to each component and add the responses. Fourier series organize that decomposition. The oscillator gives a physical reason to care about sine waves before we learn the full mathematics of Fourier analysis.

## A second-order equation is a two-state system

There is one final conceptual bridge. Define velocity v as x prime. Then the oscillator equation becomes two first-order equations: x prime equals v, and v prime equals negative omega zero squared times x, with damping or forcing terms added as appropriate.

Position and velocity together form the state. This is why two initial conditions are needed. It is also how linear algebra enters differential equations: the rule for change can be written as a matrix acting on the state vector, and the matrix's eigenvalues encode oscillation and decay. We do not need that matrix machinery to understand the spring, but the spring makes the machinery meaningful when we meet it.

The main lesson is that a second-order equation tells a story about acceleration, not merely position. Initial position and initial velocity select the trajectory. Energy explains conservative motion, damping explains loss, and forcing explains sustained response and resonance. With those ideas in place, more elaborate linear systems and Fourier methods become extensions of a model we already understand.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** First-order ODEs and initial data; sine, cosine, exponentials; basic algebra. **Question:** how do acceleration, damping, and forcing determine oscillatory motion?

### Ideal oscillator and energy

For \(m>0\), \(k>0\), \(mx''+kx=0\), let \(\omega_0=\sqrt{k/m}\). Then
\[
 x(t)=x_0\cos(\omega_0t)+\frac{v_0}{\omega_0}\sin(\omega_0t),\qquad
 T=\frac{2\pi}{\omega_0},\quad f=\frac{\omega_0}{2\pi}.
\]
Energy \(E=\tfrac12 mv^2+\tfrac12 kx^2\) satisfies \(E'=v(mx''+kx)=0\).

Example: \(m=1,k=4,x(0)=1,v(0)=0\) gives \(x=\cos2t\), \(v=-2\sin2t\), \(E=2\) joules, period \(\pi\) seconds.

### Damping

With linear viscous damping,
\[
 x''+2\beta x'+\omega_0^2x=0,\quad \beta>0,
\qquad r=-\beta\pm\sqrt{\beta^2-\omega_0^2}.
\]
- \(\beta<\omega_0\): \(e^{-\beta t}\bigl(A\cos\omega_dt+B\sin\omega_dt\bigr)\), \(\omega_d=\sqrt{\omega_0^2-\beta^2}\).
- \(\beta=\omega_0\): \((A+Bt)e^{-\beta t}\).
- \(\beta>\omega_0\): two decaying real exponentials.

\(x''+4x'+4x=0\), \(x(0)=1\), \(x'(0)=0\): \(x=(1+2t)e^{-2t}\). For \(x''+2x'+5x=0\) with the same initial data: \(x=e^{-t}(\cos2t+\tfrac12\sin2t)\). Mechanical energy with mass \(m\) and coefficient \(2m\beta\) satisfies \(E'=-2m\beta(x')^2\).

### Forcing and resonance

For \(x''+4x=\cos t\), \(x(0)=x'(0)=0\):
\[
 x(t)=\frac13(\cos t-\cos2t).
\]
For resonant forcing \(x''+4x=\cos2t\), \(x(0)=x'(0)=0\):
\[
 x(t)=\frac{t}{4}\sin2t.
\]
The first is bounded, and the second has a linearly growing amplitude envelope. For \(x''+2\beta x'+\omega_0^2 x=F\cos\omega t\), the asymptotic sinusoidal amplitude is
\[
 A(\omega)=\frac{|F|}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}}\quad (\beta>0).
\]
For \(m=1\), energy balance with forcing \(g(t)\) is \(E'=g(t)x'-2\beta(x')^2\).

### Exercises with answers

1. Solve \(x''+9x=0\) with \(x(0)=2,\;x'(0)=3\). **Answer:** \(x=2\cos3t+\sin3t\); period \(2\pi/3\).
2. Find the solution of \(x''+6x'+9x=0\) with \(x(0)=1,\;x'(0)=0\). **Answer:** \((1+3t)e^{-3t}\) (critical damping).
3. Solve \(x''+9x=\cos2t\), with both initial data zero. **Answer:** \(x=(\cos2t-\cos3t)/5\).
4. Explain why knowing \(x(0)=1\) alone does not fix a unique harmonic oscillator trajectory. **Answer:** \(x=\cos\omega_0t+B\sin\omega_0t\) works for any B; the missing initial velocity would fix \(B\).
5. What is the state-vector form of the undamped equation? **Answer:** \(\frac{d}{dt}\binom{x}{v}=\begin{pmatrix}0&1\\-\omega_0^2&0\end{pmatrix}\binom{x}{v}\).

### Reading and references

- MIT OpenCourseWare, *18.03 Differential Equations*, linear constant-coefficient equations, complex exponentials, mechanical resonance: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/
- Paul Dawkins, *Paul's Online Notes: Differential Equations*, second-order linear equations and mechanical vibrations: https://tutorial.math.lamar.edu/
- Wikipedia: [Harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator), [Damping](https://en.wikipedia.org/wiki/Damping), [Resonance](https://en.wikipedia.org/wiki/Resonance), [Fourier series](https://en.wikipedia.org/wiki/Fourier_series).
