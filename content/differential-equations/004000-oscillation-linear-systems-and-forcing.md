# Oscillation, linear systems, and forcing

<!-- BEGIN SPOKEN LECTURE -->

# Oscillation, linear systems, and forcing

## Oscillators, Damping, and Resonance

A mass on a spring returns toward equilibrium when displaced. Push it, and it may oscillate. Add friction, and the motion dies out. Drive it with a repeating force, and the response may grow dramatically when the forcing frequency matches the system's preferred frequency. These behaviors all follow from a second-order differential equation.

The oscillator is more than a mechanical example. Variants appear in electrical circuits, structural vibration, optical systems, and the study of normal modes. It is also a good place to learn how characteristic roots, conserved energy, and forcing interact.

### The simplest oscillator

For a mass m attached to a linear spring of stiffness k, Newton's law gives mass times acceleration equal to negative k times displacement. After dividing by mass, write the equation as y-double-prime plus omega-zero squared times y equals zero, where omega-zero is the positive square root of k over m.

Try a solution y equal to cosine of omega-zero times t. Its second derivative is negative omega-zero squared times itself, so it satisfies the equation. Sine does too. Every solution is a linear combination A cosine omega-zero t plus B sine omega-zero t. Initial displacement determines A, and initial velocity determines B after accounting for the factor omega-zero in the derivative.

The period is two pi divided by omega-zero. If a spring is four times as stiff, with mass unchanged, omega-zero doubles and the period halves. The square root dependence is a concrete prediction of the model, not just a label for the frequency.

### Conservation in phase space

Multiply the equation y-double-prime plus omega-zero squared y equals zero by y-prime. The result is the derivative of one-half y-prime squared plus one-half omega-zero squared y squared equal to zero. Therefore that expression is constant along each solution.

It is an energy divided by the mass. The first term is kinetic energy per mass, and the second is elastic potential energy per mass. In the phase plane with horizontal coordinate y and vertical coordinate y-prime, a fixed positive energy corresponds to an ellipse. The state continually moves around the ellipse; it does not spiral inward or outward. The origin is a stable equilibrium in the sense that small initial disturbances remain small, but it is not asymptotically stable: a nonzero solution keeps oscillating instead of approaching the origin.

This is a useful distinction. Stability does not mean convergence to equilibrium. A system can keep bounded motion forever.

### Add damping

Suppose a friction-like force is proportional to velocity and opposes it. After dividing by mass, the equation becomes y-double-prime plus two gamma times y-prime plus omega-zero squared y equals zero, with gamma positive.

Try an exponential solution e to the r t. The characteristic equation is r squared plus two gamma r plus omega-zero squared equals zero. Its roots are negative gamma plus or minus the square root of gamma squared minus omega-zero squared.

If gamma is smaller than omega-zero, the roots have a negative real part and imaginary parts of opposite signs. The motion oscillates with a decaying exponential envelope. This is underdamping. If gamma equals omega-zero, the characteristic root is repeated. The general solution is an exponential decay times A plus B t; this is critical damping. If gamma exceeds omega-zero, the roots are distinct negative real numbers, and the motion is a combination of two decaying exponentials without oscillation; this is overdamping.

All three regimes approach the equilibrium as t increases. Critical damping is often described as the fastest return without oscillation, but that slogan depends on what initial conditions and response criterion are being compared. The precise mathematical distinction is the nature of the characteristic roots and the resulting solution families.

Energy gives a second view. With damping, the time derivative of the same energy expression is negative two gamma times the square of velocity. Energy never increases. It decreases whenever velocity is nonzero. This explains why damping can remove sustained oscillation even before the explicit solution is written.

### A periodic external force

Now apply a force proportional to cosine omega t, with amplitude F after dividing by mass. The ideal undamped equation becomes y-double-prime plus omega-zero squared y equals F cosine omega t.

If the driving frequency omega differs from omega-zero, try a particular solution proportional to cosine omega t. Substituting gives amplitude F divided by omega-zero squared minus omega squared. The denominator records how closely the forcing frequency matches the natural frequency. As omega approaches omega-zero, this particular-solution amplitude becomes large.

At exactly equal frequencies, the proposed cosine response fails. It lies in the solution space of the homogeneous equation, so applying the differential operator to it gives zero, not the required forcing. The correct particular solution is F divided by two omega-zero times t times sine omega-zero t. Differentiation verifies that it produces F cosine omega-zero t.

The key feature is the factor t. The forcing is bounded for all time, yet the ideal undamped response can grow linearly in amplitude. This is resonance. It does not violate energy conservation, because energy is being supplied continually by the external driver. Our earlier conservation law applied only when there was no forcing and no damping.

### What damping changes about resonance

With both damping and forcing, the equation is y-double-prime plus two gamma y-prime plus omega-zero squared y equals F cosine omega t. After transients decay, the response oscillates at the driving frequency with a phase lag and a steady amplitude equal to F divided by the square root of the sum of two squares: omega-zero squared minus omega squared, squared, and two gamma omega, squared.

At a nonzero damping coefficient, that denominator does not vanish for positive driving frequency. Therefore the steady periodic response has finite amplitude. Near resonance the response may still be large, and it depends sensitively on damping. But there is no unbounded linear growth in the long-time steady solution of the damped, linearly forced system.

We should distinguish the natural frequency of free undamped oscillation from the frequency where the forced, damped amplitude is maximal. They need not coincide. For sufficiently weak damping, the amplitude peak occurs near omega-zero; at stronger damping the notion of a sharp resonant peak can disappear.

### What this model does and does not prove

A real spring can behave nonlinearly at large displacements. A bridge, a machine, or an electrical circuit may have many coupled modes rather than one. The linear oscillator makes a precise local or idealized model, not an automatic guarantee about physical failure thresholds. Its predictions are still powerful: identify the natural frequencies, determine damping, and calculate the response to forcing.

In mathematical terms, we have learned three complementary methods. Characteristic roots classify free solutions. An energy identity reveals stability and dissipation. Particular solutions describe how an input drives the system, and the special resonant case shows why solving a forced equation cannot always use the same trial function as the forcing. These ideas extend to systems of differential equations, where a matrix replaces the single frequency and multiple modes may interact.

## Linear Systems, Eigenvalues, and Matrix Exponentials

One differential equation describes the evolution of one quantity. Many real systems have several quantities influencing one another: two populations, coupled masses, a collection of chemical concentrations, or an electrical network. A linear system writes their rates of change as a matrix times the state vector. Even with constant coefficients, the coordinates may be coupled so that we cannot solve them one at a time.

There is a single object that solves every constant-coefficient linear initial-value problem of this kind: the matrix exponential. Understanding it also clarifies what eigenvalues reveal about stability, and what they do not.

### From a scalar exponential to a matrix exponential

For a scalar equation saying y prime equals a times y, with constant a, the solution is y at time zero multiplied by e to the a t. Replace the scalar a with a square matrix A and the scalar state with a vector x. We hope that an expression called e to the A t will solve x prime equals A x.

Define the matrix exponential by the same infinite power series as the ordinary exponential: identity matrix plus A t plus one half A squared t squared, and so on, with the k-th term being A to the k-th power times t to the k-th power divided by k factorial. This series converges for every finite matrix and every real t. Because each term is a power of the same matrix A, term-by-term differentiation works and gives A times the original series. At time zero the sum is the identity matrix.

Thus x of t equals e to the A t times the initial state x zero is a solution. Standard uniqueness for linear differential equations says it is the only one with that initial state. We call the matrix exponential the state-transition operator: it maps an initial state to its later value.

There is a group law in time. Evolving for time s and then for time t is the same as evolving for time s plus t. The matrix identity is e to the A s times e to the A t equals e to the A times s plus t. The two factors commute because they are functions of the same matrix. We must not generalize this blindly to two unrelated matrices: e to the A times e to the B need not equal e to the A plus B if A and B do not commute.

### Eigenvectors are the normal modes

Suppose A has an eigenvector v with eigenvalue lambda. Starting on the line through v, the solution is e to the lambda t times v. The direction remains the same; only its scale changes. Such a direction is a mode. If a real matrix can be diagonalized over the reals, a general initial state is a sum of eigenmodes, each evolving at its own exponential rate.

Take a two-dimensional system with rates x one prime equals negative x one and x two prime equals negative three times x two. Its matrix is diagonal. The solution is x one at zero times e to the negative t, and x two at zero times e to the negative three t. Both modes decay, but the second does so faster. A trajectory tends to the origin, and after sufficient time its direction is typically dominated by the slowest decaying mode.

Now consider the matrix with entries negative one and one in the first row, and zero and negative two in the second. It is upper triangular. The second state decays as e to the negative two t. That second state also drives the first. Starting from first coordinate zero and second coordinate one, the solution becomes first coordinate e to the negative t minus e to the negative two t, and second coordinate e to the negative two t. Even though both eigenvalues are negative, the first coordinate initially increases from zero before eventually decaying. Stability concerns long-run behavior; it does not imply every coordinate decreases at every instant.

### Complex modes and rotations

A real matrix may have complex eigenvalues. In a two-dimensional example, let A rotate every vector counterclockwise at unit angular speed: its first row is zero, negative one, and its second row is one, zero. The eigenvalues are plus and minus the imaginary unit. The matrix exponential is the ordinary rotation matrix through angle t. The solution goes around a circle, never approaching the origin and never escaping to infinity.

If we subtract a small positive multiple of the identity matrix from this rotation generator, each trajectory spirals inward while rotating. The eigenvalues then have negative real parts. If instead we add a positive multiple of the identity, they spiral outward. This is why real parts of eigenvalues control exponential growth or decay and imaginary parts describe oscillatory behavior, at least at the level of linear modes.

But there is another issue: a matrix might not have enough eigenvectors to form a basis.

### Defective matrices and polynomial factors

Take a matrix whose diagonal entries are both negative one, whose upper-right entry is one, and whose lower-left entry is zero. It has only one independent eigenvector. Write the matrix as negative identity plus N, where N is nonzero but N squared equals zero. The exponential factors because the identity and N commute. We obtain e to the negative t multiplied by identity plus t times N.

Starting from a vector with second coordinate one, the first coordinate is t times e to the negative t. The factor t is not an exponential mode. It arises from a generalized eigenvector and is characteristic of a Jordan block. Nevertheless, t times e to the negative t still tends to zero. Negative exponential decay eventually dominates any fixed polynomial factor.

In general, finite-dimensional constant-coefficient systems are asymptotically stable if and only if every eigenvalue of A has strictly negative real part. Even if A is not diagonalizable, any Jordan polynomial factors are overwhelmed by those negative exponentials.

If some eigenvalue has positive real part, the equilibrium is unstable. If the largest real part is exactly zero, no single conclusion follows from eigenvalues alone without looking at Jordan blocks. A pure rotation is stable in the Lyapunov sense but not asymptotically stable. A nontrivial Jordan block attached to an imaginary-axis eigenvalue can produce unbounded polynomial growth and is unstable.

### Non-normal growth despite stable eigenvalues

Even a diagonalizable stable matrix can show large transient amplification if its eigenvectors are nearly parallel. This is common for non-normal matrices, where the matrix does not commute with its transpose in the appropriate real inner product. A concrete family is the upper-triangular matrix with negative one and negative two on the diagonal and a large positive number K in the upper-right position. Starting from the second coordinate one and the first zero, the first coordinate becomes K times the difference between e to the negative t and e to the negative two t. The amplitude can be as large as K divided by four at time log two, despite both eigenvalues being strictly negative.

So eigenvalues correctly predict eventual decay, but they do not bound intermediate amplification without additional information about eigenvector geometry or the matrix exponential norm. Transient amplification can make an eventually stable system hazardous in numerical simulation or control. If disturbances are amplified a thousandfold before decaying, the eventual stability statement may be inadequate for design.

### What the exponential actually buys us

The matrix exponential solves the complete homogeneous system, with diagonalizable, defective, real, or complex eigenvalues. It also tells us exactly how perturbations to initial data propagate: the difference between two trajectories is the matrix exponential applied to the initial difference.

From there we can ask a new question. What happens when the system is continuously pushed by a time-dependent external force rather than merely starting away from equilibrium? The answer will integrate the matrix exponential against the forcing, revealing the principle of superposition in its most useful form.

## Forced Systems, Variation of Constants, and Green's Functions

A vibrating instrument continues moving after the initial strike. It can also be driven while it moves: someone repeatedly plucks the string, pushes a mass, or changes an applied voltage. The first behavior comes from the state already present. The second comes from a continuing input. For a linear system, we can separate these effects exactly.

Write the state equation as x prime equals A x plus b of t, where A is a constant square matrix and b is a continuous forcing vector. The initial state is x zero at time zero. The solution has two pieces. The first is e to the A t times x zero, just as for the unforced system. The second is the integral, from zero to t, of e to the A times t minus s multiplied by b of s. This is the variation-of-constants formula, sometimes called variation of parameters or Duhamel's principle.

### Deriving the integral, not guessing it

First multiply the equation by e to the negative A t. Differentiate the product e to the negative A t times x of t. By the product rule, one contribution is negative A e to the negative A t times x. The other is e to the negative A t times x prime. Substitute x prime equals A x plus b. The A terms cancel because A commutes with its own exponential. We are left with e to the negative A t times b of t.

Integrate both sides from zero to t. At time zero, the exponential is the identity, so the initial value is x zero. Finally multiply by e to the A t. The result is precisely the two-part solution described above.

There is a physical interpretation behind each factor in the integral. At time s, the external input adds a small increment of state, proportional to b of s times the small time step. That increment then evolves freely for the remaining time t minus s, under the operator e to the A times t minus s. Adding up the contributions from all earlier input times produces the integral.

This explains causality in the formula. The state at time t depends only on inputs at earlier times, from zero through t. No future input is required to calculate it.

### A one-dimensional example

Take the scalar equation x prime equals negative a x plus f of t, with positive constant a. The unforced system decays at rate a. The solution is x zero times e to the negative a t plus the integral of e to the negative a times t minus s multiplied by f of s.

For a constant input F, the integral can be evaluated explicitly. The state approaches F divided by a, and the transient difference from that equilibrium decays exponentially. The exact solution is F divided by a plus the initial offset, x zero minus F divided by a, times e to the negative a t.

Now compare a constant input with a brief input concentrated near one moment. A brief impulse makes a quick change in the state followed by the usual natural decay. The effect of that impulse at later times is determined by the exponential decay kernel. When we model an idealized impulse using a Dirac delta distribution, its response is the same kernel, understood with the appropriate jump condition. We should not treat the delta as an ordinary continuous function; it is a useful idealization whose integral effect is precise.

### Green's functions and impulse responses

A Green's function is a kernel that translates forcing at one time or location into a response at another. For the scalar decay equation, the causal kernel is zero before the forcing time and e to the negative a times the elapsed time after it. The solution of the zero-initial-value problem is the integral of this kernel times the input.

For a vector system with an input matrix B and an input vector u of t, the corresponding kernel is e to the A times elapsed time multiplied by B for nonnegative elapsed time. The response is the convolution of that matrix-valued impulse response with u. Convolution means that all delayed copies of the impulse response are weighted by the past input and summed.

We can see superposition directly. If input u one produces a response x one from zero initial state, and input u two produces x two, then the sum of the inputs produces the sum of the responses. Scaling an input scales its response. These properties are not approximations; they follow from linearity and uniqueness.

But superposition does *not* say any nonlinear system can be decomposed in the same way. When the matrix A depends on the state, adding two solutions will generally not give another solution. When A depends on time rather than remaining constant, a time-dependent transition matrix replaces the simple exponential of a time difference; the convolution structure is no longer automatically time-translation invariant.

### Resonance and long-lived forcing

A stable system gradually forgets its initial state, but it can have a strong response to certain driving frequencies. Consider the undamped harmonic oscillator: x double prime plus omega zero squared times x equals a forcing F times cosine of omega times t. When the driving frequency differs from the natural frequency, one can seek a particular solution oscillating at the drive frequency, with amplitude proportional to one divided by omega zero squared minus omega squared.

As the driving frequency approaches the natural frequency, that denominator tends to zero. At exact resonance the simple sinusoidal trial fails. The correct particular solution includes a factor of time times sine of the natural frequency times t, showing linearly growing amplitude in the ideal undamped model. This does not require the system to have an unstable homogeneous solution; the undamped homogeneous motion remains bounded. Sustained resonant forcing injects energy so coherently that the forced response grows.

Damping changes the story. With positive damping, the steady periodic response has a finite amplitude at every fixed nonzero damping value. The largest response may still be substantial, but exact unbounded linear growth disappears in the standard damped oscillator. In applications, finite input duration, nonlinearities, and physical limits also constrain growth. The ideal linear equation isolates the mechanism.

### From time domain to frequency domain

For a stable linear system driven by a complex exponential input, try a response with the same frequency. If the input is B times a fixed vector times e to the imaginary frequency times t, substitute a solution of the same form. The unknown amplitude must satisfy the linear equation obtained by subtracting A from the imaginary-frequency multiple of the identity. When that matrix is invertible, its inverse times B is the frequency-response operator.

This is a compact way to predict which frequencies are amplified or attenuated without solving an integral anew each time. A pole or near-singularity of the frequency-response operator signals a strong interaction between forcing and the system's natural modes. For a stable matrix A, there are no poles on the imaginary axis, so the steady-state sinusoidal response is well-defined. If A has imaginary-axis eigenvalues, resonance and polynomial growth can reappear, and there may be no bounded steady state.

### Why this formula is more general than a trick

Variation of constants solves a broad class of linear forced initial-value problems. It makes the distinct roles of initial data, natural dynamics, and external forcing explicit. It also creates a bridge to numerical time-stepping, signals, control, and partial differential equations, where response kernels and operators appear in larger spaces.

Most importantly, the integral is not mysterious. Every forcing event contributes a little state, and every contribution follows the same evolution law afterward. A complex response is the cumulative sum of simple propagated contributions. That principle is the enduring content of Green's functions and linear superposition.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Oscillators, Damping, and Resonance

**Track:** Differential Equations and Dynamical Systems. **Background:** elementary differentiation, first-order equations, and basic trigonometry. **Question:** why can a bounded periodic force create an arbitrarily large response in an ideal oscillator?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. What is the period when \(\omega_0=2\)? **Answer:** \(\pi\).
2. Is the undamped origin asymptotically stable? **Answer:** no; nontrivial trajectories follow closed energy ellipses.
3. Differentiate \(\frac{F}{2\omega_0}t\sin\omega_0t\) twice and check the resonant forcing. **Answer:** \(y_p''+\omega_0^2y_p=F\cos\omega_0t\).
4. What is \(E'\) for \(\gamma>0\)? **Answer:** \(-2\gamma(y')^2\le0\).

##### Reading

MIT OCW 18.03, second-order equations, oscillations, damping, and resonance; Arthur Mattuck, *18.03 Notes and Exercises*.

### Linear Systems, Eigenvalues, and Matrix Exponentials

**Track:** Differential Equations and Dynamical Systems. **Background:** first-order ODEs, matrices, eigenvalues. **Question:** how can a matrix determine an entire family of trajectories, including when it cannot be diagonalized?

#### Mathematical companion (not spoken)

For constant \(A\in\mathbb R^{n\times n}\), define
\[
e^{At}=\sum_{k=0}^\infty\frac{A^k t^k}{k!},\quad \frac d{dt}e^{At}=Ae^{At},\quad e^{A(t+s)}=e^{At}e^{As}.
\]
The unique solution to \(x'=Ax\), \(x(0)=x_0\), is \(x(t)=e^{At}x_0\). The identity \(e^{A+B}=e^Ae^B\) requires \(AB=BA\) in general.

**Jordan block:** \(A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}=-I+N\), \(N^2=0\), so
\[
e^{At}=e^{-t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\]

**Non-normal transient:** for \(A=\begin{pmatrix}-1&K\\0&-2\end{pmatrix}\), \(x_0=(0,1)^T\),
\[
x(t)=\begin{pmatrix}K(e^{-t}-e^{-2t})\\e^{-2t}\end{pmatrix},\quad \max_{t\ge0}x_1(t)=K/4\ \text{at }t=\log2\text{ for }K>0.
\]
All eigenvalues have negative real parts, but transient amplification may be arbitrarily large as \(K\to\infty\).

##### Exercises with answers

1. What is \(e^{At}\) when \(A=\operatorname{diag}(-2,3)\)? **Answer:** \(\operatorname{diag}(e^{-2t},e^{3t})\).
2. Is the origin asymptotically stable for pure planar rotation? **Answer:** no; trajectories retain their radius.
3. Can a matrix with only negative-real-part eigenvalues amplify a state transiently? **Answer:** yes; the triangular example above does so.
4. What invalid shortcut is tempting for noncommuting matrices? **Answer:** replacing \(e^Ae^B\) by \(e^{A+B}\) without checking commutativity.

##### Reading

MIT OpenCourseWare, [Differential Equations lecture notes](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/), sessions on eigenvalues, phase portraits and matrix exponentials.

### Forced Systems, Variation of Constants, and Green's Functions

**Track:** Differential Equations and Dynamical Systems. **Background:** scalar integrating factors and the matrix exponential. **Question:** how does a system combine its natural evolution with inputs arriving at different times?

#### Mathematical companion (not spoken)

For \(x'(t)=Ax(t)+b(t)\), \(x(0)=x_0\), the **variation-of-constants formula** is
\[
x(t)=e^{At}x_0+\int_0^t e^{A(t-s)}b(s)\,ds.
\]
For \(b(t)=Bu(t)\), the causal impulse response is \(G(\tau)=e^{A\tau}B\) for \(\tau\ge0\) and zero for \(\tau<0\); from zero initial data, \(x=G*u\).

**Scalar decay:** \(x'=-ax+F\) for \(a>0\) has
\[
x(t)=\frac Fa+\left(x_0-\frac Fa\right)e^{-at}.
\]

**Undamped resonance:** for \(x''+\omega_0^2x=F\cos(\omega_0t)\), a particular solution is
\[
x_p(t)=\frac{F}{2\omega_0}t\sin(\omega_0t)\qquad(\omega_0\ne0).
\]
For stable \(A\), the steady complex frequency-response operator for \(x'=Ax+Bu\) is \((i\omega I-A)^{-1}B\).

##### Exercises with answers

1. What remains of the formula if the forcing is zero? **Answer:** \(x(t)=e^{At}x_0\).
2. For \(x'=-2x+4\) and \(x(0)=1\), find \(x(t)\). **Answer:** \(x(t)=2-e^{-2t}\).
3. Why must the impulse-response kernel depend only on \(t-s\) here? **Answer:** constant A makes the dynamics time-translation invariant.
4. Why may resonance occur in an undamped but not an asymptotically stable oscillator? **Answer:** the undamped system has imaginary-axis eigenvalues; stable damping moves them into the left half-plane, preventing a pole at real driving frequency.

##### Reading

MIT OpenCourseWare, [Differential Equations lecture notes](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/), linear systems, transfer functions, and convolution.
