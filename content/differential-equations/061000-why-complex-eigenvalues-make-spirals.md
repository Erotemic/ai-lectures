# Why Complex Eigenvalues Make Spirals: Rotation, Damping, and Real Solutions

<!-- BEGIN SPOKEN LECTURE -->

# Why Complex Eigenvalues Make Spirals

A spring can move back and forth while its oscillations gradually shrink. We have already described that using sine, cosine, and a decaying exponential. Now imagine that instead of watching the spring on a line, we put its displacement on one axis and its velocity on the other. The pair moves around the origin as it decays. A single oscillation has become a spiral in a two-dimensional state space.

Why does a real system with real coefficients produce this rotation? When we compute its eigenvalues, we may encounter complex numbers. Those numbers are not an indication that the physical position or velocity has become imaginary. They are a compact way to encode two real motions that cycle into one another. By the end of this lecture we will obtain actual real-valued formulas, determine the direction and period of rotation, and see the difference between a stable spiral and a center that never decays.

## Start with the simplest rotating rule

Consider two quantities x and y following the equations x prime equals negative two y, and y prime equals two x. Suppose the state starts at one and zero. At that point, x prime is zero and y prime is positive two. So the initial arrow points upward. A quarter-turn later, when the state is near zero and one, its derivative points left. The arrows keep turning counterclockwise around the origin.

The exact solution is x equals cosine of two t and y equals sine of two t. Differentiate x and we get negative two sine of two t, which is negative two y. Differentiate y and we get two cosine of two t, which is two x. The equations and the initial values are both satisfied.

Why does the state stay on the unit circle? Differentiate x squared plus y squared. The result is two x times x prime plus two y times y prime. Substitute the differential equations: we get negative four x y plus four y x, exactly zero. So distance squared from the origin is constant. The motion is pure rotation, with angular speed two radians per unit time and full period pi.

The coefficient matrix has zeroes on its diagonal, negative two in the upper right, and two in the lower left. Its characteristic polynomial is lambda squared plus four. There are no real roots. The eigenvalues are positive two i and negative two i, where i is the square root of negative one. Those imaginary eigenvalues correspond to the circular motion we just solved entirely with real functions.

## Adding decay without changing the rotation mechanism

Now add a loss term to both equations. Let x prime equal negative x minus two y, and y prime equal two x minus y. The matrix is the earlier rotation matrix minus the identity matrix.

The exact solution from the same initial state is x equal to exponential of negative t times cosine of two t, and y equal to exponential of negative t times sine of two t. The trigonometric pair is still turning, but its size is multiplied by exponential of negative t. Differentiating the product checks the equations. The radius equals exponential of negative t; the state spirals inward and approaches equilibrium.

There is also a direct energy calculation. Differentiate the squared radius x squared plus y squared. The rotational terms cancel as before, and the two negative diagonal terms contribute negative two times the radius squared. Thus the squared radius decays as exponential of negative two t. Taking its square root gives exponential of negative t. We can understand the decay rate without solving either coordinate separately.

For the general matrix with diagonal entries a and off-diagonal entries negative b and b, the equations describe rotation at angular speed b and a radial rate a. The eigenvalues are a plus i b and a minus i b. If a is negative, the circles contract into an attracting spiral. If a is positive, they expand into a repelling spiral. If a is zero, every nonzero trajectory is a circle in these specially chosen coordinates. That last case is a center: stable in the sense that sufficiently small starting states remain small, but not asymptotically stable because their distances never shrink to zero.

If b is negative, the rotation is clockwise. The sign of the imaginary part matters for orientation only after we have specified a real coordinate system and the matrix that acts on it. Merely listing the two conjugate eigenvalues does not tell you the direction in which an arbitrarily oriented system turns.

## Why complex exponentials help

The calculus identity behind all this is Euler's formula: exponential of i times an angle equals cosine of that angle plus i times sine of that angle. This identity makes the derivatives of sine and cosine appear as multiplication by i.

Suppose a real matrix A has a complex eigenvalue a plus i b, together with a complex eigenvector w. The formal complex solution is exponential of a plus i b, times t, multiplied by w. Because A is real, the real part and the imaginary part of any complex-valued solution each satisfy the original real differential equation. They are two real solutions, not imaginary physical states.

To see their structure, write w as a real vector u plus i times a real vector v. Multiply by the complex exponential. Its real part is exponential of a t times u cosine of b t minus v sine of b t. Its imaginary part is exponential of a t times u sine of b t plus v cosine of b t. Those vectors rotate through the plane spanned by u and v, while their overall size scales by the real exponential.

The two real solutions are independent when the complex eigenvalue is genuinely nonreal and A is a real two-by-two matrix. By combining them with real constants, we obtain every real initial-value solution. This is the bridge between complex algebra and real motion. The complex notation avoids doing almost identical sine-and-cosine calculations twice.

## What if the orbit is not a circle?

Consider x prime equals negative x minus four y, and y prime equals x minus y. The matrix has eigenvalues negative one plus two i and negative one minus two i. If we tried to use x squared plus y squared as the energy, the rotational terms would not cancel. The picture in the original coordinates is not a circular spiral.

But scale the first coordinate by one half. Call X equal to x divided by two, and Y equal to y. Then X prime equals negative X minus two Y, and Y prime equals two X minus Y. In the scaled coordinates we have the very spiral solved a moment ago.

Start with x equal to two and y equal to zero. The solution is x equal to two exponential of negative t times cosine of two t, and y equal to exponential of negative t times sine of two t. The quantity x squared divided by four plus y squared equals exponential of negative two t. Its level sets are ellipses in the original coordinates. As they contract, the trajectory winds inward along an elliptical spiral.

The general lesson is that a change of coordinates may turn circles into ellipses. It does not change the eigenvalues or the exponential rate of attraction. It changes what Euclidean distance and angle look like in the displayed coordinates. Consequently, the eigenvalues tell us oscillation frequencies and asymptotic growth or decay, but do not determine the precise shape of a portrait by themselves.

## The connection back to a damped spring

Consider a second-order equation: displacement double prime plus two times displacement prime plus five times displacement equals zero. Set v equal to displacement prime. The state equations are x prime equals v and v prime equals negative five x minus two v.

The characteristic polynomial of the state matrix is lambda squared plus two lambda plus five. Its roots are negative one plus two i and negative one minus two i. Therefore the displacement must be exponential of negative t times a linear combination of cosine of two t and sine of two t.

Suppose the spring starts at displacement one and velocity zero. The cosine coefficient is one because x at zero equals one. Differentiate the proposed expression. The derivative at zero is negative one plus two times the sine coefficient. Set that equal to zero, and the sine coefficient is one half. The displacement is thus exponential of negative t times cosine of two t plus one half sine of two t. A direct substitution into the second-order equation verifies the answer.

This formula explains the qualitative motion. The spring oscillates with a damped angular frequency of two, and its oscillation envelope decays at rate one. The trajectory in displacement-velocity space is an inward spiral, although its shape need not be circular. Under different damping and stiffness, the roots might be real, producing a node instead. The characteristic polynomial decides which kind of behavior is possible.

## A reliable classification and its boundary

For a real two-by-two matrix, a negative discriminant of the characteristic polynomial means a complex conjugate eigenvalue pair. Their shared real part is half the trace. So a negative trace gives an attracting spiral, a positive trace gives a repelling spiral, and zero trace gives a linear center, provided the discriminant is negative. In that last case, the matrix has purely imaginary nonzero eigenvalues and is similar over the real numbers to a rotation matrix.

It is tempting to carry that center classification straight into nonlinear equations. Resist that temptation. Near a nonlinear equilibrium, the linearized matrix with purely imaginary eigenvalues does not determine whether nonlinear trajectories drift slowly inward, drift outward, or form closed orbits. The higher-order terms may matter. When the real part is strictly negative or strictly positive, the linearized behavior is much more decisive locally.

There is a more general lesson here. A pair of real differential equations can be easier to understand by temporarily solving a complex algebra problem. The imaginary part of an eigenvalue tells us the rate of oscillation. Its real part tells us the rate of exponential growth or decay. Real and imaginary parts of the resulting complex solution bring us back to two genuine real trajectories. Complex numbers are a computational language for rotation, not an extra physical dimension.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: complex modes and elliptical energy

For \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), \(J^2=-I\) and
\[
A=aI+bJ,\qquad e^{At}=e^{at}\left(I\cos bt+J\sin bt\right).
\]
Thus \(\mathbf z(0)=(1,0)^T\) gives \(\mathbf z(t)=e^{at}(\cos bt,\sin bt)^T\). Also
\[
\frac d{dt}\|\mathbf z\|^2=2a\|\mathbf z\|^2;
\]
for \(a=0\) the motion is a center, and for \(a<0\) an attracting spiral.

If \(A\mathbf w=(a+ib)\mathbf w\), \(\mathbf w=\mathbf u+i\mathbf v\), two real solutions are
\[
e^{at}(\mathbf u\cos bt-\mathbf v\sin bt),\qquad
 e^{at}(\mathbf u\sin bt+\mathbf v\cos bt).
\]

### An ellipse instead of a circle

\[
 A=\begin{pmatrix}-1&-4\\1&-1\end{pmatrix},\quad (x_0,y_0)=(2,0).
\]
With \(X=x/2\), \(Y=y\), the transformed coefficient matrix is \(-I+2J\). Hence
\[
 x(t)=2e^{-t}\cos 2t,\quad y(t)=e^{-t}\sin2t,
 \quad \boxed{\frac{x(t)^2}{4}+y(t)^2=e^{-2t}}.
\]
The portrait is an elliptical spiral, not a circular one.

### The spring system

\[
x''+2x'+5x=0,\quad x(0)=1,\quad x'(0)=0
\]
has state matrix \(\begin{pmatrix}0&1\\-5&-2\end{pmatrix}\) with eigenvalues \(-1\pm2i\). The solution is
\[
\boxed{x(t)=e^{-t}\left(\cos2t+\tfrac12\sin2t\right)}.
\]

### Exercises and answers

1. For \(A=\begin{pmatrix}0&-3\\3&0\end{pmatrix}\), find the period and the motion from \((1,0)\). **Answer:** \(2\pi/3\); \((\cos3t,\sin3t)\).
2. For \(A=\begin{pmatrix}-2&-1\\1&-2\end{pmatrix}\), classify the origin. **Answer:** stable spiral; eigenvalues \(-2\pm i\).
3. Find the radius of the motion for \(A=\begin{pmatrix}1&-2\\2&1\end{pmatrix}\), \(\|\mathbf z(0)\|=3\). **Answer:** \(3e^t\); unstable spiral.
4. Differentiate \(e^{-t}(\cos2t,\sin2t)\) and verify that it solves \(\mathbf z'=(-I+2J)\mathbf z\). **Answer:** \((-e^{-t}\cos2t-2e^{-t}\sin2t,\ 2e^{-t}\cos2t-e^{-t}\sin2t)\), which matches multiplication.
5. Does a linear center necessarily imply that a nearby nonlinear equilibrium is a center? **Answer:** no; first-order linearization has inconclusive stability information when eigenvalues have zero real part.

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Matrix Methods: Eigenvalues and Normal Modes](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/matrix-methods-eigenvalues-and-normal-modes/).
- MIT OpenCourseWare, *18.03SC*, [Qualitative Behavior: Phase Portraits](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/qualitative-behavior-phase-portraits/).
- Wikipedia: [Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula), [Focus (dynamical systems)](https://en.wikipedia.org/wiki/Focus_(dynamical_systems)).
