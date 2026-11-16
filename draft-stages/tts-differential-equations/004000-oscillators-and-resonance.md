# 004000 — Oscillators, Damping, and Resonance

**Track:** Differential Equations and Dynamical Systems. **Background:** elementary differentiation, first-order equations, and basic trigonometry. **Question:** why can a bounded periodic force create an arbitrarily large response in an ideal oscillator?

<!-- BEGIN SPOKEN LECTURE -->

# Oscillators, Damping, and Resonance

A mass on a spring returns toward equilibrium when displaced. Push it, and it may oscillate. Add friction, and the motion dies out. Drive it with a repeating force, and the response may grow dramatically when the forcing frequency matches the system's preferred frequency. These behaviors all follow from a second-order differential equation.

The oscillator is more than a mechanical example. Variants appear in electrical circuits, structural vibration, optical systems, and the study of normal modes. It is also a good place to learn how characteristic roots, conserved energy, and forcing interact.

## The simplest oscillator

For a mass m attached to a linear spring of stiffness k, Newton's law gives mass times acceleration equal to negative k times displacement. After dividing by mass, write the equation as y-double-prime plus omega-zero squared times y equals zero, where omega-zero is the positive square root of k over m.

Try a solution y equal to cosine of omega-zero times t. Its second derivative is negative omega-zero squared times itself, so it satisfies the equation. Sine does too. Every solution is a linear combination A cosine omega-zero t plus B sine omega-zero t. Initial displacement determines A, and initial velocity determines B after accounting for the factor omega-zero in the derivative.

The period is two pi divided by omega-zero. If a spring is four times as stiff, with mass unchanged, omega-zero doubles and the period halves. The square root dependence is a concrete prediction of the model, not just a label for the frequency.

## Conservation in phase space

Multiply the equation y-double-prime plus omega-zero squared y equals zero by y-prime. The result is the derivative of one-half y-prime squared plus one-half omega-zero squared y squared equal to zero. Therefore that expression is constant along each solution.

It is an energy divided by the mass. The first term is kinetic energy per mass, and the second is elastic potential energy per mass. In the phase plane with horizontal coordinate y and vertical coordinate y-prime, a fixed positive energy corresponds to an ellipse. The state continually moves around the ellipse; it does not spiral inward or outward. The origin is a stable equilibrium in the sense that small initial disturbances remain small, but it is not asymptotically stable: a nonzero solution keeps oscillating instead of approaching the origin.

This is a useful distinction. Stability does not mean convergence to equilibrium. A system can keep bounded motion forever.

## Add damping

Suppose a friction-like force is proportional to velocity and opposes it. After dividing by mass, the equation becomes y-double-prime plus two gamma times y-prime plus omega-zero squared y equals zero, with gamma positive.

Try an exponential solution e to the r t. The characteristic equation is r squared plus two gamma r plus omega-zero squared equals zero. Its roots are negative gamma plus or minus the square root of gamma squared minus omega-zero squared.

If gamma is smaller than omega-zero, the roots have a negative real part and imaginary parts of opposite signs. The motion oscillates with a decaying exponential envelope. This is underdamping. If gamma equals omega-zero, the characteristic root is repeated. The general solution is an exponential decay times A plus B t; this is critical damping. If gamma exceeds omega-zero, the roots are distinct negative real numbers, and the motion is a combination of two decaying exponentials without oscillation; this is overdamping.

All three regimes approach the equilibrium as t increases. Critical damping is often described as the fastest return without oscillation, but that slogan depends on what initial conditions and response criterion are being compared. The precise mathematical distinction is the nature of the characteristic roots and the resulting solution families.

Energy gives a second view. With damping, the time derivative of the same energy expression is negative two gamma times the square of velocity. Energy never increases. It decreases whenever velocity is nonzero. This explains why damping can remove sustained oscillation even before the explicit solution is written.

## A periodic external force

Now apply a force proportional to cosine omega t, with amplitude F after dividing by mass. The ideal undamped equation becomes y-double-prime plus omega-zero squared y equals F cosine omega t.

If the driving frequency omega differs from omega-zero, try a particular solution proportional to cosine omega t. Substituting gives amplitude F divided by omega-zero squared minus omega squared. The denominator records how closely the forcing frequency matches the natural frequency. As omega approaches omega-zero, this particular-solution amplitude becomes large.

At exactly equal frequencies, the proposed cosine response fails. It lies in the solution space of the homogeneous equation, so applying the differential operator to it gives zero, not the required forcing. The correct particular solution is F divided by two omega-zero times t times sine omega-zero t. Differentiation verifies that it produces F cosine omega-zero t.

The key feature is the factor t. The forcing is bounded for all time, yet the ideal undamped response can grow linearly in amplitude. This is resonance. It does not violate energy conservation, because energy is being supplied continually by the external driver. Our earlier conservation law applied only when there was no forcing and no damping.

## What damping changes about resonance

With both damping and forcing, the equation is y-double-prime plus two gamma y-prime plus omega-zero squared y equals F cosine omega t. After transients decay, the response oscillates at the driving frequency with a phase lag and a steady amplitude equal to F divided by the square root of the sum of two squares: omega-zero squared minus omega squared, squared, and two gamma omega, squared.

At a nonzero damping coefficient, that denominator does not vanish for positive driving frequency. Therefore the steady periodic response has finite amplitude. Near resonance the response may still be large, and it depends sensitively on damping. But there is no unbounded linear growth in the long-time steady solution of the damped, linearly forced system.

We should distinguish the natural frequency of free undamped oscillation from the frequency where the forced, damped amplitude is maximal. They need not coincide. For sufficiently weak damping, the amplitude peak occurs near omega-zero; at stronger damping the notion of a sharp resonant peak can disappear.

## What this model does and does not prove

A real spring can behave nonlinearly at large displacements. A bridge, a machine, or an electrical circuit may have many coupled modes rather than one. The linear oscillator makes a precise local or idealized model, not an automatic guarantee about physical failure thresholds. Its predictions are still powerful: identify the natural frequencies, determine damping, and calculate the response to forcing.

In mathematical terms, we have learned three complementary methods. Characteristic roots classify free solutions. An energy identity reveals stability and dissipation. Particular solutions describe how an input drives the system, and the special resonant case shows why solving a forced equation cannot always use the same trial function as the forcing. These ideas extend to systems of differential equations, where a matrix replaces the single frequency and multiple modes may interact.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(\omega_0>0\):
\[
y''+\omega_0^2y=0,\qquad y(t)=A\cos(\omega_0t)+B\sin(\omega_0t).
\]
Energy per mass \(E=\frac12(y')^2+\frac12\omega_0^2y^2\) satisfies \(E'=0\). For damped motion,
\[
y''+2\gamma y'+\omega_0^2y=0,\quad E'=-2\gamma(y')^2\le0.
\]
Characteristic roots: \(r=-\gamma\pm\sqrt{\gamma^2-\omega_0^2}\). Underdamped if \(0<\gamma<\omega_0\); critically damped if \(\gamma=\omega_0\); overdamped if \(\gamma>\omega_0\).

Undamped forced response:
\[
y''+\omega_0^2y=F\cos(\omega t),\quad
 y_p=\begin{cases}\frac{F}{\omega_0^2-\omega^2}\cos(\omega t),&\omega\ne\omega_0,\\[4pt]
\frac{F}{2\omega_0}t\sin(\omega_0t),&\omega=\omega_0.
\end{cases}
\]
For damping \(\gamma>0\), steady-state amplitude is
\[
A(\omega)=\frac{|F|}{\sqrt{(\omega_0^2-\omega^2)^2+(2\gamma\omega)^2}}.
\]

### Exercises with answers

1. What is the period when \(\omega_0=2\)? **Answer:** \(\pi\).
2. Is the undamped origin asymptotically stable? **Answer:** no; nontrivial trajectories follow closed energy ellipses.
3. Differentiate \(\frac{F}{2\omega_0}t\sin\omega_0t\) twice and check the resonant forcing. **Answer:** \(y_p''+\omega_0^2y_p=F\cos\omega_0t\).
4. What is \(E'\) for \(\gamma>0\)? **Answer:** \(-2\gamma(y')^2\le0\).

### Reading

MIT OCW 18.03, second-order equations, oscillations, damping, and resonance; Arthur Mattuck, *18.03 Notes and Exercises*.
