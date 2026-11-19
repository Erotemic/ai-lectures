# When Two Quantities Evolve Together: Linear Systems and Eigenvector Solutions

<!-- BEGIN SPOKEN LECTURE -->

# When Two Quantities Evolve Together

Suppose we can describe the temperature of one object with an equation for its rate of change. What happens when there are two objects, and heat can flow from either one into the other? Or when a moving mass has both a position and a velocity, and knowing the position alone does not determine what happens next? We need more than one evolving quantity. Fortunately, most of the mathematics we already know about first-order equations still applies. It just needs to be organized so that the unknown at each instant is a vector instead of a single number.

Today we will construct two-dimensional linear systems, learn how a matrix generates their motion, and derive complete solutions using eigenvectors. Nothing about the word eigenvector should obscure the physical question. We want to find special starting configurations that keep their shape while their size changes exponentially. When those special configurations form a basis, every motion is built from them.

## A state is the information required to start again

Consider a spring whose displacement is called x and whose velocity is called v. A second-order differential equation for the displacement might say: the second derivative of x, plus three times its first derivative, plus twice x, is zero. This is a damped oscillator with a particular choice of units. To specify a motion, a displacement by itself is insufficient. We also need the velocity at the same instant.

So define the state to be the pair x and v. Its first component changes according to x prime equals v. Its second changes according to v prime equals negative two x minus three v. That is a system of two first-order equations. We have not changed the physical model; we have changed how we keep track of it.

A column vector is just an orderly way to put those two numbers together. Call it z. The derivative z prime is the column of the two rates. To compute it, multiply z by a matrix whose first row contains zero and one, and whose second row contains negative two and negative three. In short, z prime equals A z.

Why is this useful? Because the matrix A is a rule that can be applied to every possible state, not a list of unrelated coefficients. If we change the initial displacement and velocity, we change z at time zero but not the rule. If we add two solutions, their sum still obeys the same homogeneous linear system. That superposition property is a direct consequence of matrix multiplication distributing over addition.

Our system is autonomous: A does not depend explicitly on time. It is homogeneous: there is no external forcing term. We will later see what changes when a forcing is added.

## An eigenvector is a direction that does not turn

Imagine that at a certain instant the state z points along a vector w. Under the rule z prime equals A z, the instantaneous velocity of the point in state space is A w, scaled by however large z is. Usually A w points in a different direction. The state then turns as well as moves.

But suppose A w happens to be exactly lambda times w. The derivative points along the same line as the state. Starting on that line, the state never needs to leave it. Its size obeys the same scalar equation we know: the rate of the amplitude is lambda times the amplitude. So the motion is exponential of lambda t times w.

That is the reason to seek eigenvectors. It is not merely a technique for factoring a matrix. Each eigenvector describes a pattern of motion whose components maintain a fixed ratio. A negative lambda makes that pattern decay. A positive lambda makes it grow. Zero lambda gives a stationary pattern.

To find those patterns, solve A w equals lambda w. Subtract lambda w from both sides: A minus lambda times the identity matrix, applied to w, must be zero. A nonzero solution requires that matrix to be singular. For a two-by-two matrix, that condition says its determinant is zero, producing a quadratic equation in lambda.

Apply this procedure to our damped spring. The matrix has rows zero, one and negative two, negative three. Subtract lambda from the two diagonal entries. The determinant is lambda squared plus three lambda plus two, which factors into lambda plus one times lambda plus two. Thus the two eigenvalues are negative one and negative two.

For lambda equal to negative one, an eigenvector has first component one and second component negative one. Check it: the first component of A w becomes negative one, and the second becomes one, exactly negative one times the starting vector. For lambda equal to negative two, an eigenvector has components one and negative two. Again, direct multiplication checks the claim.

The corresponding solutions are exponential of negative t times the state with displacement one and velocity negative one, and exponential of negative two t times the state with displacement one and velocity negative two. Because the eigenvectors are linearly independent, we may add scaled copies and obtain every solution.

## A full solution from actual initial data

Let the spring start at displacement one with zero velocity. We seek constants c one and c two so that c one times the first eigenvector plus c two times the second equals the initial state. The displacement equation says c one plus c two equals one. The velocity equation says negative c one minus two c two equals zero. Subtracting the equations gives c two equals negative one and c one equals two.

So the displacement at time t is two times exponential of negative t, minus exponential of negative two t. The velocity is negative two times exponential of negative t plus two times exponential of negative two t.

Several checks are available. At t equals zero, the displacement is two minus one, which is one. The velocity is negative two plus two, which is zero. Differentiate the displacement, and we get exactly the stated velocity. Differentiate the velocity, and the result equals negative two times the displacement minus three times the velocity. Each equation is satisfied, not just the initial data.

The two exponential terms decay at different rates. At late times, the faster term has nearly disappeared, leaving the slower exponential. In the state plane, the trajectory eventually points almost along the eigenvector with eigenvalue negative one. In physical space, the mass approaches equilibrium without oscillating: our damping is strong enough that the eigenvalues are real and negative.

It is worth emphasizing that the state plane is not the physical room. Its horizontal coordinate is displacement; its vertical coordinate is velocity. The path through that plane records which displacement and velocity occur together at each moment. One physical motion becomes one curve in state space.

## A genuinely coupled first-order example

Now consider two quantities x and y that follow the equations x prime equals negative x, and y prime equals two x minus two y. Think of x as a concentration in an upstream compartment that decays or drains away, while y is a downstream concentration receiving input from x and losing material at its own rate. The equations are only an illustrative linear model; the numbers are chosen for clarity.

The first equation solves immediately: x is its initial value times exponential of negative t. Suppose x begins at one and y begins at zero. Then x equals exponential of negative t. Substitute that into the second equation. We obtain y prime plus two y equals two times exponential of negative t. Multiply by the integrating factor exponential of two t. After integrating from zero, y equals two times exponential of negative t minus two times exponential of negative two t.

The downstream amount begins at zero and rises even though no new material is being supplied upstream. Its rate starts positive because x is initially present. Eventually it falls because both compartments empty. These facts can be seen from the formula, but they are easier to anticipate from the equations.

Let us solve the same problem with eigenvectors. The matrix has rows negative one, zero and two, negative two. For eigenvalue negative one, an eigenvector is the pair one and two. For eigenvalue negative two, an eigenvector is zero and one. The initial state, one and zero, equals the first eigenvector minus twice the second. Therefore the solution is exponential of negative t times the vector one and two, minus twice exponential of negative two t times the vector zero and one. Its components match the integrating-factor solution exactly.

This second calculation is not redundant. It demonstrates the same answer from two viewpoints. Scalar elimination is often easiest for a triangular system. Eigenvectors reveal the independent modes, and their method extends to many systems that do not decouple by simply solving one variable first.

## What changes when we have two equations rather than one?

For a scalar linear equation, an initial value specifies one number. For our system, the initial state specifies two. We therefore need two independent solution patterns to express arbitrary initial states. When a matrix has two distinct real eigenvalues, the corresponding eigenvectors are automatically independent, so that works.

But we have made two assumptions that deserve attention. First, the coefficients are constant. If the matrix varies with time, a fixed eigenvector of one instant need not be preserved at the next. Second, we found two real eigenvectors. Other matrices have complex eigenvalues, which correspond to rotating and oscillating motions, or a repeated eigenvalue with only one independent eigenvector. We will learn to solve those without pretending that the easy diagonalizable case covers everything.

There is also a useful sanity check for any proposed solution. If we write a state as a linear combination of exponential modes, differentiate it, and check that each mode satisfies A w equals lambda w, then the whole combination satisfies the differential equation by linearity. Matching the initial state completes the verification. That is usually safer than trying to recognize a solution by appearance.

## A procedure you can actually use

When handed two linear constant-coefficient equations, first identify a state vector and write the coefficient matrix carefully. Next, try to understand the model directly. What would happen if one coordinate were zero? Which signs indicate loss, gain, or coupling? Then compute the characteristic polynomial, find real eigenvalues and corresponding eigenvectors, and form exponential modes. If you have two independent modes, match the initial state by solving a two-by-two linear system. Finally, verify by differentiation.

This method already handles a substantial class of models. It also explains why the language of linear algebra becomes natural in differential equations: eigenvectors are not abstract decorations but motions whose proportions remain constant, and eigenvalues give their growth or decay rates.

One more distinction will organize what follows. The solution we have computed gives the location of one trajectory at each time. A phase portrait asks what all possible trajectories do. We will begin with the geometry of the same eigenvectors and exponential modes, then learn to recognize saddles, nodes, and the stable directions they imply.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact construction and verification

For a constant real matrix \(A\), consider
\[
\mathbf z'(t)=A\mathbf z(t),\qquad \mathbf z(0)=\mathbf z_0.
\]
If \(A\mathbf w=\lambda\mathbf w\), then \(\mathbf z(t)=e^{\lambda t}\mathbf w\) satisfies the equation. Distinct eigenvalues supply independent eigenvectors. If \(A=P\operatorname{diag}(\lambda_1,\lambda_2)P^{-1}\), then
\[
\mathbf z(t)=P\begin{pmatrix}e^{\lambda_1t}&0\\0&e^{\lambda_2t}\end{pmatrix}P^{-1}\mathbf z_0.
\]
This representation is intended here for the diagonalizable case; defective and complex cases are developed later in this route.

### Second-order equation as a state system

\[
 x''+3x'+2x=0,\quad \mathbf z=(x,v)^T,\quad A=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}.
\]
\[
\det(A-\lambda I)=\lambda^2+3\lambda+2=(\lambda+1)(\lambda+2),
\quad \mathbf w_1=(1,-1)^T,\quad \mathbf w_2=(1,-2)^T.
\]
For \(\mathbf z(0)=(1,0)^T=2\mathbf w_1-\mathbf w_2\),
\[
\boxed{x(t)=2e^{-t}-e^{-2t},\quad v(t)=-2e^{-t}+2e^{-2t}.}
\]

### Coupled triangular example

\[
A=\begin{pmatrix}-1&0\\2&-2\end{pmatrix},\quad (x(0),y(0))=(1,0).
\]
Its eigenpairs are \((-1,(1,2)^T)\) and \((-2,(0,1)^T)\). Hence
\[
\boxed{(x(t),y(t))=(e^{-t},\;2e^{-t}-2e^{-2t}).}
\]
Equivalently \(y'+2y=2e^{-t}\); integrating factor \(e^{2t}\) gives the same result.

### Exercises and worked answers

1. **Convert a second-order initial-value problem.** Write \(x''+5x'+6x=0\) as a first-order system. **Answer:** \(\mathbf z=(x,v)\), \(\mathbf z'=\begin{pmatrix}0&1\\-6&-5\end{pmatrix}\mathbf z\). Eigenvalues are \(-2,-3\).
2. **Check a mode.** For \(A=\begin{pmatrix}2&1\\0&-1\end{pmatrix}\), find an eigenvector for eigenvalue \(-1\). **Answer:** solve \(3x+y=0\): \((1,-3)^T\) works, so \(e^{-t}(1,-3)^T\) is a solution.
3. **Solve for coefficients.** Given \(\mathbf w_1=(1,1)^T\), \(\mathbf w_2=(1,-1)^T\), write \((3,1)^T\) in this basis. **Answer:** \(2\mathbf w_1+\mathbf w_2\).
4. **Predict the slow mode.** A diagonalizable system has eigenvalues \(-1\) and \(-5\). Which exponential typically dominates at large positive time? **Answer:** the \(e^{-t}\) mode, unless its coefficient happens to vanish.
5. **Check the downstream peak.** For the triangular example above, find the time when \(y\) is maximal. **Answer:** \(y'=2e^{-t}(-1+2e^{-t})=0\) at \(t=\ln 2\); \(y(\ln2)=1/2\).

### Sources and further reading

- MIT OpenCourseWare, *18.03SC Differential Equations*, [Linear Systems](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/linear-systems-introduction/).
- MIT OpenCourseWare, *18.03SC Differential Equations*, [Matrix Methods: Eigenvalues and Normal Modes](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/matrix-methods-eigenvalues-and-normal-modes/).
- Wikipedia: [Linear differential equation](https://en.wikipedia.org/wiki/Linear_differential_equation), [State-space representation](https://en.wikipedia.org/wiki/State-space_representation).
