# Why Energy-Aware Integration Matters: Oscillators, Symplectic Steps, and Structure

<!-- BEGIN SPOKEN LECTURE -->

# Why Energy-Aware Integration Matters

Suppose we are simulating a frictionless spring. We start it moving, and then we leave it alone. The real system keeps exchanging kinetic and potential energy. At the center of the motion the mass moves fastest; at each extreme it stops briefly, storing its energy in the stretched or compressed spring. In the ideal model, the total energy stays constant forever.

Yet a numerical simulation can show the mass spiraling outward, as if someone is secretly adding energy. Another method can make the oscillations slowly die away, as if there were friction. Both can happen even when the differential equation contains neither driving nor damping. The artifact comes from how we advance time.

Error tolerance alone does not explain this. A method can be locally accurate over short intervals and still distort the long-term geometry of motion. This lecture compares four simple numerical approaches to the same oscillator: forward Euler, backward Euler, symplectic Euler, and a symmetric method often called Störmer–Verlet or velocity Verlet. We will see exactly what each does to energy, then separate honest numerical properties from promises those properties cannot make.

## One spring, two equations

Choose units so that the mass and spring stiffness are both one. Write position as q and velocity as p. The equations say that position changes at rate p, while velocity changes at rate negative q. Equivalently, position has second derivative negative itself. The exact solution moves around circles in the plane whose horizontal coordinate is q and whose vertical coordinate is p.

The energy is half the square of position plus half the square of velocity. Its time derivative is position times velocity plus velocity times negative position. The terms cancel, so energy does not change. Start at position one with velocity zero. Energy is one half, and the exact orbit is the unit circle.

This example is simple enough that we can analyze a numerical method not only by comparing a few decimal answers, but by examining the geometric map from one step to the next.

## Forward Euler: a spring that gains energy

Forward Euler uses the current position and velocity to predict both next values. Next position is current position plus step length times current velocity. Next velocity is current velocity minus step length times current position. With step length one half, the initial state one and zero becomes position one and velocity negative one half.

The new energy is half of one plus one quarter, or five eighths. It has increased from one half to five eighths in a single step. No physical force supplied that extra energy. The numerical method did.

We can calculate the effect for every possible starting point. Square the two Euler updates and add them. The cross terms cancel, but a factor of one plus the square of the step length remains. Thus, *every* forward Euler step multiplies oscillator energy by one plus the square of the step length. For any positive fixed step, this factor exceeds one. Repeat the step enough times and the numerical energy grows without bound.

That is a stronger statement than observing a few badly drawn circles. It tells us that forward Euler is structurally wrong for long-term undamped oscillation at every fixed positive step size, although it remains a valid convergent approximation on a finite time interval as the step length tends to zero.

## Backward Euler: a spring with imaginary friction

Backward Euler evaluates the rate at the unknown new state. Its equations say that next position is current position plus the step times next velocity, while next velocity is current velocity minus the step times next position. Solve those two linear equations together, and the result is a contraction and rotation.

If we square the new position and velocity and add, we find that energy has been divided by one plus the square of the step length. At step length one half, starting from the same energy one half, the next energy is two fifths, or zero point four. The solver has removed one fifth of the original energy in one step.

Backward Euler is excellent for many damped or stiff problems because that contraction suppresses fast decaying modes. But for an ideal conservative oscillator, it introduces artificial damping. A solver that is stable in the sense of not blowing up can still be physically misleading. Stability and preservation of the intended motion are not synonyms.

## A small change in update order

Now try a surprisingly different procedure. First update velocity using the current position. Then update position using the *new* velocity. This is sometimes called kick–drift symplectic Euler. Its equations are explicit: a velocity kick from the current spring force, followed by a position drift using the kicked velocity. Computationally it costs little more than ordinary Euler.

With step length one half, start from position one and velocity zero. The velocity after the kick is negative one half. The position after the drift is one minus one quarter, or three quarters. The physical energy after the step is half of nine sixteenths plus one quarter, which is thirteen thirty-seconds, about zero point four zero six. It changed: symplectic Euler is **not** an exactly energy-conserving method.

Nevertheless, it behaves very differently over many steps. The map of position and velocity has determinant one. In the two-dimensional phase plane, it preserves oriented area, unlike the expanding forward Euler map or the contracting backward Euler map. The exact oscillator flow also preserves phase-plane area, making this property a meaningful geometric comparison among integrators.

For the harmonic oscillator, we can go further. The kick–drift method exactly preserves a *modified* quadratic energy: half of position squared plus velocity squared minus step length times position times velocity. At step length one half, this modified energy stays exactly one half for our initial condition. It differs slightly from the physical energy, which can wobble around. When the step length is smaller than two in our chosen oscillator units, the modified quadratic form is positive definite. That bounds the computed orbit instead of letting its amplitude spiral outward or shrink to zero.

The bound has a condition: this argument uses our simple oscillator and a step small enough for the modified energy to be positive definite. Being symplectic does not guarantee stable behavior for an arbitrarily large step or for every Hamiltonian system. The point is that a structural property creates a much more faithful long-term behavior in a setting where forward Euler provably fails.

## A symmetric second-order step

Symplectic Euler has a preferred order: kick then drift. Reverse those updates and you get a related method, but not the same one. There is a way to balance the two operations. Apply half of the velocity kick, drift the position over a full step using that halfway velocity, then apply the other half kick using the new position. This is the velocity Verlet method.

It is second-order accurate for smooth forces. It is also time reversible in the following numerical sense: reversing the sign of the step and applying the same update rule undoes a forward step, in exact arithmetic. Forward Euler does not have that property. Velocity Verlet also preserves the relevant symplectic structure for separable Hamiltonian systems such as a mass moving in a potential.

Let's compute one step of our oscillator with length one half. The initial position is one, and the velocity is zero. The half kick gives velocity negative one quarter. Drift by half a second to get position seven eighths. The last half kick subtracts one quarter times seven eighths, giving final velocity negative fifteen thirty-seconds. The new physical energy is about zero point four nine two seven, close to the original one half but not equal.

The merit of Verlet is not that it magically returns exact positions or perfectly conserves every physical energy. For suitably smooth Hamiltonian problems, with adequate step sizes and away from serious resonances or singular behavior, its time symmetry and symplectic structure can give excellent qualitative performance over long intervals. Its energy error often oscillates rather than exhibiting the systematic drift of ordinary Euler.

It is useful to contrast this with the implicit midpoint method. For our quadratic oscillator energy, implicit midpoint preserves the *actual* quadratic energy exactly, because the midpoint change in energy can be written as the average gradient dotted with the displacement, and that dot product vanishes for the skew-symmetric oscillator dynamics. That exact result depends on a quadratic invariant and the method; it is not a claim that midpoint conserves every nonlinear Hamiltonian exactly.

## Accuracy, stability, and structure answer different questions

We now have enough examples to reject a common simplification: choose the method with the highest nominal order and the smallest stated tolerance, and everything will be fine. A high-order Runge–Kutta method may give extremely accurate trajectories over a modest interval. A symplectic method may give more faithful qualitative behavior in a long conservative simulation. An implicit dissipative method may be appropriate for stiff decay. An event-handling method may be essential for collisions. These are different mathematical demands.

If energy is physically conserved, monitor its numerical behavior. If it is physically dissipated by drag or damping, energy should normally decrease in the correct way. A method that rigidly conserves energy in a dissipative system would also be wrong. If a system has holonomic constraints, preserving them may require a specialized projection or constrained integrator. If impacts remove energy discontinuously, a smooth symplectic step cannot by itself model the jumps.

A geometric numerical method is therefore not an incantation for physical truth. It is an algorithm chosen to respect a property that the continuous model genuinely has. Symplecticity, time reversibility, momentum preservation, positivity, and controlled dissipation are distinct properties. We choose which matters by inspecting the equations and the outputs we wish to trust.

## A practical comparison worth running

If you have access to a numerical environment, try this experiment. Simulate the same undamped oscillator with a fixed step of one half and initial state position one, velocity zero. Run forward Euler, backward Euler, symplectic Euler, and velocity Verlet for many cycles. Plot position against velocity, not just position against time. The exact orbit is a circle. Watch the forward Euler points spiral outward and the backward Euler points spiral inward. Watch the symplectic trajectories stay near closed curves, though they need not lie on the exact circle. Plot physical energy as well.

Then reduce the step and repeat. Short-time error should improve for consistent methods, but the long-time patterns retain their characteristic differences. To be fair, compare computational costs and force evaluations too. If you switch to variable step sizes, you must re-examine geometric properties: arbitrary adaptive time stepping does not automatically preserve the simple fixed-step symplectic structure. Specialized adaptive geometric methods exist, but an error controller attached blindly to a geometric scheme can remove its advantage.

The deepest lesson is that integrating an equation is not merely adding up local slopes. It is repeatedly applying a map to the state. The map has algebraic and geometric properties of its own. Some maps systematically expand energy, some contract it, and others respect enough of the original dynamics to behave well over long times. Understanding that map lets us choose numerical methods for reasons stronger than a solver's popularity or a default tolerance.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: harmonic oscillator maps and modified energy

For \(q'=p,\ p'=-q\), let \(z=(q,p)^T\) and \(H(z)=\tfrac12(q^2+p^2)\). The generator is \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\), so \(H'=z^T J z=0\).

Forward Euler has map \(A_F=I+hJ=\begin{pmatrix}1&h\\-h&1\end{pmatrix}\). Then \(A_F^T A_F=(1+h^2)I\), so \(H(A_Fz)=(1+h^2)H(z)\).

Backward Euler has map \(A_B=(I-hJ)^{-1}=(1+h^2)^{-1}\begin{pmatrix}1&h\\-h&1\end{pmatrix}\), so \(H(A_Bz)=H(z)/(1+h^2)\).

Kick–drift symplectic Euler is
\[
 p_{n+1}=p_n-hq_n,\qquad q_{n+1}=q_n+h p_{n+1}.
\]
Its matrix is \(A_S=\begin{pmatrix}1-h^2&h\\-h&1\end{pmatrix}\), with \(\det A_S=1\). Let
\[
 K_h=\begin{pmatrix}1&-h/2\\-h/2&1\end{pmatrix},\quad
 \widetilde H_h(z)=\frac12 z^T K_h z=\frac12(q^2+p^2-hqp).
\]
Direct multiplication shows \(A_S^T K_h A_S=K_h\). The eigenvalues of \(K_h\) are \(1\pm h/2\), so \(\widetilde H_h\) is positive definite for \(0<h<2\), yielding a uniform bound on \(q_n,p_n\) at fixed such \(h\).

Velocity Verlet, for the same oscillator, uses
\[
 p_{n+1/2}=p_n-\frac h2 q_n,\quad
 q_{n+1}=q_n+h p_{n+1/2},\quad
 p_{n+1}=p_{n+1/2}-\frac h2 q_{n+1}.
\]
At \(h=1/2\), from \((q_0,p_0)=(1,0)\), it returns \((q_1,p_1)=(7/8,-15/32)\) and
\(H_1=\tfrac12((7/8)^2+(15/32)^2)=1009/2048\approx0.49267578125\).

For implicit midpoint, \(z_{n+1}-z_n=hJ(z_n+z_{n+1})/2\). Therefore
\[
 H(z_{n+1})-H(z_n)=\frac12(z_{n+1}+z_n)^T(z_{n+1}-z_n)
 =\frac h4 (z_{n+1}+z_n)^T J(z_{n+1}+z_n)=0.
\]
The exact preservation proof here uses the oscillator's quadratic energy and the skew-symmetric matrix \(J\), not an arbitrary nonlinear energy.

### Exercises and worked answers

1. For \(h=1/2\), compute the first forward-Euler energy starting from \((1,0)\). **Answer:** \(H_1=(1+1/4)H_0=5/8\).
2. Compute the first backward-Euler energy with the same data. **Answer:** \(H_1=(1/2)/(5/4)=2/5\).
3. Verify the first symplectic Euler step and its modified energy. **Answer:** \((q_1,p_1)=(3/4,-1/2)\), and \(\widetilde H_{1/2}=\tfrac12(9/16+1/4-(1/2)(3/4)(-1/2))=1/2\).
4. Why does area preservation not imply stability for every step? **Answer:** the same map can preserve area while having expanding and contracting directions; for the oscillator, \(K_h\) loses positive definiteness when \(h\ge2\).
5. Does symplectic Euler conserve the physical energy exactly? **Answer:** no. It preserves the written modified quadratic form for the harmonic oscillator at fixed \(h\), and the physical energy typically oscillates.
6. Why would exact energy conservation be the wrong goal for a damped spring? **Answer:** the continuous model dissipates energy, so numerical energy behavior should reflect that dissipation.

### Sources and further reading

- [Ernst Hairer, *Geometric Numerical Integration*, lecture notes on Hamiltonian systems](https://unige.ch/~hairer/poly_geoint/week1.pdf).
- [Hairer, Lubich and Wanner, *Geometric Numerical Integration*, second edition (Springer, 2006)](https://link.springer.com/book/10.1007/3-540-30666-8).
- [SciPy `solve_ivp`: choices of explicit and implicit integrators](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
- [Wikipedia: Symplectic integrator](https://en.wikipedia.org/wiki/Symplectic_integrator).
