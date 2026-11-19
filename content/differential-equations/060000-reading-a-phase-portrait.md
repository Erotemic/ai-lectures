# Reading a Phase Portrait: Stable Nodes, Saddles, and the Directions of Motion

<!-- BEGIN SPOKEN LECTURE -->

# Reading a Phase Portrait

A solution formula tells us where one trajectory goes. But suppose we want to know what happens to a thousand different starting states. Will they all approach equilibrium? Are some initial conditions safe while nearby ones escape? Which direction will the motion approach from? And can we answer those questions without calculating a thousand individual solutions?

A phase portrait compresses an entire system's behavior into a picture of its state space. The arrows show how the state would begin to move from any point. Curves following the arrows are solution trajectories. Today we will learn to read this geometry from real eigenvalues and eigenvectors. The key information is not just whether eigenvalues are positive or negative. It is which lines in the plane those eigenvalues act upon, and how the other trajectories bend between them.

## The arrows are derivatives, not destinations

Take a two-dimensional autonomous system: the derivative of x equals some function of x and y, and the derivative of y equals another function. At any particular state, those two derivatives form an arrow. If the arrow is long, the system changes rapidly in the units of that drawing. If it points upward, y is increasing at that moment. If it points rightward, x is increasing. An arrow is not where the state jumps next. It is the instantaneous tangent direction to a smooth trajectory.

For a constant-coefficient linear system, the arrow at the vector z is the vector A z. The origin is always an equilibrium, because multiplying the zero vector by any matrix gives zero. When the determinant of A is nonzero, the origin is the only equilibrium. If the determinant vanishes, there may be a whole line of equilibria. We will concentrate first on invertible matrices with real eigenvalues.

The uniqueness theorem for these linear systems gives another geometric rule. Through a given starting point, there is exactly one solution. Two distinct trajectories cannot cross at the same state and time; indeed, for an autonomous system, two distinct phase curves cannot cross geometrically in the plane either, because either curve can be shifted in time to pass through the alleged intersection. At an equilibrium the solution simply stays there. A portrait that shows several different arrows emerging from one ordinary state is not a valid portrait of a smooth autonomous differential equation.

## A diagonal system: the entire picture is visible

Begin with x prime equals negative x, and y prime equals negative three y. The solution from initial state a and b is x equals a times exponential of negative t, and y equals b times exponential of negative three t.

Both quantities approach zero. The origin is an attracting equilibrium. We call its portrait a stable node when the eigenvalues are real, distinct, and negative. The coordinate axes are special: a point on the horizontal axis stays there; a point on the vertical axis also stays there. They are the eigenvector lines.

But most initial states begin off both axes. Their y coordinate decays three times as fast in its exponent as x. At large positive time, the state comes very close to the horizontal eigenvector line before reaching the origin. Unless a happened to be zero, the slowly decaying x mode determines the final direction of approach.

This is a useful distinction between magnitude and geometry. Both components may be decreasing in absolute value, while the direction of the state vector changes substantially. A trajectory can curve even when it is built from two perfectly straight eigenvector motions.

We can also remove time and inspect the shape of a curve. Where x is positive, x equals a exponential of negative t implies exponential of negative t equals x divided by a. Substitute into y: y equals b times x over a, cubed. So a family of trajectories resembles cubic curves near the origin. This relation depends on the coordinate axes being eigenvectors; after a change of basis the curves are tilted or sheared, but the attracting-node behavior remains.

## A non-diagonal example with visible curvature

Consider the system x prime equals negative two x plus y, and y prime equals x minus two y. Its matrix has diagonal entries negative two and off-diagonal entries one. The eigenvector along the diagonal line y equals x has eigenvalue negative one. The eigenvector along the other diagonal, y equals negative x, has eigenvalue negative three.

Start at state two and zero. That initial state is one copy of the vector one and one, plus one copy of one and negative one. So the solution has x equal to exponential of negative t plus exponential of negative three t, and y equal to exponential of negative t minus exponential of negative three t.

At the beginning, y is zero. Its derivative is two, so it immediately rises. Yet both eigenvalues are negative and the whole state eventually approaches the origin. There is no contradiction. Stability does not require every coordinate to decrease monotonically. It requires the distance from equilibrium to become small as time advances. In this symmetric example the squared Euclidean distance does decrease, because the matrix is negative definite, but the individual y coordinate first grows.

At late times, exponential of negative three t is negligible compared with exponential of negative t. The state approaches along the diagonal y equals x. That is precisely the slow eigenvector. From the picture alone we could identify the attracting equilibrium and its preferred final direction; from the eigenvalues we can quantify the decay rates.

## A saddle: stability in one direction, escape in another

Now change the first eigenvalue to positive one and the second to negative two. The simplest system is x prime equals x, and y prime equals negative two y. Its trajectories are x equals a exponential of t and y equals b exponential of negative two t.

The horizontal eigenvector line is unstable: any nonzero x component grows exponentially as we move forward in time. The vertical eigenvector line is stable: if the initial state lies exactly on it, the solution approaches zero. Every initial state with a nonzero horizontal component eventually leaves a bounded neighborhood of the origin. This configuration is a saddle.

In a saddle, a stable line does not make the equilibrium stable. Stability is a claim about all sufficiently close starting points, not just a privileged set of initial conditions. Start as close to the origin as you like with a tiny nonzero horizontal component. That component eventually grows beyond any fixed small threshold. Thus the saddle equilibrium is unstable even though one entire line of trajectories approaches it.

A sheared saddle is just as instructive. Take x prime equals x plus y, and y prime equals negative two y. The growing eigenvector is one and zero. The decaying eigenvector is one and negative three. If the initial state is zero and one, resolving it into eigenvectors gives one third of the growing mode minus one third of the decaying mode. The explicit solution is x equal to one third times exponential of t minus exponential of negative two t, and y equal to exponential of negative two t.

Notice that y decays from one toward zero while x starts at zero and grows. At first the state can look reassuring if we monitor only y. Its full state eventually escapes because of x. This is exactly why stability analysis must examine the entire state vector.

## Classify the portrait without guessing a picture

For a general real two-by-two matrix, the two eigenvalues are roots of a quadratic equation. That quadratic is lambda squared minus the trace times lambda plus the determinant. The trace is the sum of diagonal entries. The determinant, as usual, measures whether the matrix is invertible and encodes the product of the eigenvalues.

If the determinant is negative, the two eigenvalues are real and of opposite signs. The origin is a saddle. This conclusion requires no drawing and no explicit eigenvector calculation.

If the determinant is positive and the eigenvalues are distinct real numbers, they have the same sign. A negative trace then means both are negative: a stable node. A positive trace means both are positive: an unstable node. The discriminant, trace squared minus four times determinant, tells us whether those roots are real. Positive discriminant gives distinct real eigenvalues; negative discriminant gives a complex conjugate pair that we will handle separately.

A zero discriminant means a repeated eigenvalue. We must inspect the eigenvectors before deciding the precise portrait. And when the determinant is zero, the origin might not be isolated, so the simple saddle-node classification is incomplete. These edge cases are worth preserving rather than hiding in a chart.

The eigenvectors add the geometry that the trace and determinant alone cannot supply. Two matrices can have the same eigenvalues but different eigenvector directions. Their rates of growth and decay match, while the portrait is rotated or sheared. If we want the actual slopes of stable and unstable lines, we need eigenvectors.

## What a portrait can and cannot prove

The portrait of a linear homogeneous system tells us the fate of every initial state, provided we interpret its arrows in the forward time direction. It can display attracting nodes, repelling nodes, saddles, rotations, and combinations of these. It can also describe a nonlinear system near an equilibrium after we approximate the nonlinear field by its Jacobian. But the passage from a linear approximation to a nonlinear conclusion needs care. If every eigenvalue of the Jacobian has strictly negative real part, a sufficiently smooth nonlinear system has a locally asymptotically stable equilibrium. If an eigenvalue has strictly positive real part, the equilibrium is unstable. If some eigenvalue has zero real part and none has positive real part, linearization alone may not decide stability.

That last warning is not a technicality. A rotating linear system can produce closed circles, while nonlinear terms that are invisible in its first derivative may cause slow spiraling inward or outward. We will first understand the rotating linear cases exactly, then be able to recognize what a first-order approximation does and does not say.

For now, when you encounter a new two-dimensional linear system, begin with four questions. Where are the equilibria? Which eigenvector lines are invariant? Along each line, does the motion grow or shrink? And for a typical state off those lines, which mode dominates at long times? Answer those questions before plotting points. The calculation will become a picture you can explain, rather than a picture you merely trust.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: phase-plane classification

Let \(\dot{\mathbf z}=A\mathbf z\) with \(A\in\mathbb R^{2\times2}\), \(\tau=\operatorname{tr}(A)\), \(\Delta=\det(A)\). Then
\[
p(\lambda)=\lambda^2-\tau\lambda+\Delta,\qquad D=\tau^2-4\Delta.
\]
When \(D>0\), eigenvalues are distinct and real. If \(\Delta<0\), there is a saddle; if \(\Delta>0\) and \(\tau<0\), a stable node; if \(\Delta>0\) and \(\tau>0\), an unstable node. Complex pairs, repeated roots and zero eigenvalues require additional analysis.

### An attracting node with rotated eigendirections

\[
A=\begin{pmatrix}-2&1\\1&-2\end{pmatrix},\quad A(1,1)^T=-(1,1)^T,\quad A(1,-1)^T=-3(1,-1)^T.
\]
With \(\mathbf z(0)=(2,0)^T\),
\[
\mathbf z(t)=e^{-t}(1,1)^T+e^{-3t}(1,-1)^T.
\]
Check \(\mathbf z'(0)=(-4,2)^T=A(2,0)^T\). Though \(y'(0)>0\), the origin attracts the entire trajectory.

### A sheared saddle

\[
A=\begin{pmatrix}1&1\\0&-2\end{pmatrix},\quad \mathbf w_u=(1,0)^T,\quad\mathbf w_s=(1,-3)^T.
\]
For \(\mathbf z(0)=(0,1)^T=\tfrac13\mathbf w_u-\tfrac13\mathbf w_s\),
\[
\boxed{\mathbf z(t)=\left(\frac{e^t-e^{-2t}}3,\ e^{-2t}\right)^T.}
\]
The stable eigenspace is \(\operatorname{span}(\mathbf w_s)\); the unstable one is \(\operatorname{span}(\mathbf w_u)\). A saddle is unstable even though its stable subspace contains nonzero states converging to zero.

### Exercises with answers

1. Classify \(A=\operatorname{diag}(-2,-5)\). **Answer:** stable node; generic trajectories approach tangent to the eigenvector for \(-2\).
2. Classify \(A=\operatorname{diag}(3,-1)\). **Answer:** saddle; stable line is the second coordinate axis.
3. For \(A=\begin{pmatrix}0&2\\1&-1\end{pmatrix}\), calculate trace and determinant. **Answer:** \(\tau=-1\), \(\Delta=-2\), so saddle; \(\lambda=1,-2\).
4. For \(A=\begin{pmatrix}-2&1\\1&-2\end{pmatrix}\), what is the late-time ratio \(y/x\) for initial condition \((2,0)\)? **Answer:** it tends to one, corresponding to the slow mode \((1,1)\).
5. Does decreasing of one coordinate imply attraction? **Answer:** no. In the sheared saddle example \(y(t)=e^{-2t}\to0\) but \(x(t)\to\infty\) for the indicated initial state.

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Qualitative Behavior: Phase Portraits](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/qualitative-behavior-phase-portraits/).
- MIT OpenCourseWare, *18.03SC*, [Matrix Methods: Eigenvalues and Normal Modes](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/matrix-methods-eigenvalues-and-normal-modes/).
- Wikipedia: [Phase portrait](https://en.wikipedia.org/wiki/Phase_portrait), [Stability theory](https://en.wikipedia.org/wiki/Stability_theory).
