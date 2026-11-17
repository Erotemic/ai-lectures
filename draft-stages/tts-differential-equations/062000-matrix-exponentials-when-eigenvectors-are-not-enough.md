# Matrix Exponentials When Eigenvectors Are Not Enough: Jordan Chains and Forcing

<!-- BEGIN SPOKEN LECTURE -->

# Matrix Exponentials When Eigenvectors Are Not Enough

Our method for two-dimensional linear systems began by finding two independent eigenvectors. Each one gave us an exponential mode, and we added those modes to match the initial state. But a perfectly ordinary real matrix may have only one independent eigenvector, even though its state has two components. What should we do with the missing solution?

The answer is not to give up, or to invent a second eigenvector. The missing motion is still there. It contains an exponential multiplied by time. That extra factor is the simplest manifestation of a generalized eigenvector. It also points toward a larger idea: every constant-coefficient linear system has a matrix exponential that advances its state, whether or not the matrix can be diagonalized.

We will derive both of these claims rather than taking them on faith, and then use the same machinery to solve a forced system. Along the way we will encounter a caution about stability: all the eigenvalues can indicate eventual decay while a component, or even the norm of the entire state, grows for a while.

## One eigenvector where we need two

Take the system x prime equals negative x plus y, and y prime equals negative y. Its matrix has negative one on both diagonal entries, one above the diagonal, and zero below.

The second equation can be solved first: y equals its initial value times exponential of negative t. Now put that into the first equation. We have x prime plus x equals the initial y value times exponential of negative t. Multiply by exponential of t. The left side becomes the derivative of exponential of t times x. The right side becomes a constant: the initial y value. Integrating yields x equal to exponential of negative t times the initial x plus t times the initial y.

So the full answer is easy to write down. If the state starts at zero and one, then y equals exponential of negative t and x equals t times exponential of negative t. The second coordinate decays immediately, while the first initially grows from zero, reaches its maximum at time one, and eventually decays as well.

Now let us see why a naive eigenvector calculation gets stuck. The characteristic polynomial is lambda plus one, squared, so negative one is a repeated eigenvalue. The matrix A plus the identity has only one nonzero entry, in the upper right. Solving A plus the identity times w equals zero forces the second component of w to be zero. There is only one eigenvector direction: the horizontal axis.

We can certainly write an eigenvector solution, exponential of negative t times the vector one and zero. But any multiple of that vector begins with y equal to zero. It cannot possibly match an initial state whose y coordinate is one. We need another independent solution, and the one we just found by integrating factors provides it: exponential of negative t times the vector t and one.

## The generalized eigenvector explains the time factor

Let v be the ordinary eigenvector one and zero. Let w be the vector zero and one. The relationship is A plus the identity times v equals zero, while A plus the identity times w equals v. The vector w is called a generalized eigenvector: it is not an eigenvector, but applying A minus the eigenvalue times the identity sends it to one.

Try the vector-valued function exponential of negative t times w plus t v. Differentiate it. We get exponential of negative t times negative w minus t v plus v. Now apply A instead. Because A v equals negative v and A w equals negative w plus v, multiplication produces the same expression. So this really is a solution of the matrix differential equation.

The first solution is exponential of negative t times v. The second is exponential of negative t times w plus t v. At time zero, their initial states are v and w. These are independent, so their linear combinations can match every initial state. We have recovered a complete solution method without pretending a repeated eigenvalue always comes with two ordinary eigenvectors.

This also explains a familiar fact about critically damped springs. The scalar equation x double prime plus two x prime plus x equals zero has a double characteristic root at negative one. Its solutions have the form a plus b times t, multiplied by exponential of negative t. Set its state to displacement and velocity, and the same generalized-eigenvector structure appears in the two-dimensional first-order system. The factor of t is not an arbitrary rule for a repeated root. It comes from the missing independent direction.

## The matrix exponential as an evolution operator

For a scalar equation y prime equals a y, the answer from initial value y zero is exponential of a t times y zero. We want a matrix-valued analogue that acts on an initial vector and returns the evolved vector.

Define the exponential of A t using the same power series as the ordinary exponential: the identity matrix plus t A plus t squared A squared over two factorial plus t cubed A cubed over three factorial, and so on. The series converges for every finite matrix and every finite time. Differentiating term by term shows that its derivative is A times the matrix exponential. At time zero, all terms except the identity disappear.

Consequently, for a constant matrix A, the unique solution of z prime equals A z and z at zero equals z zero is z of t equals exponential of A t times z zero. We often call the matrix exponential an evolution operator or a fundamental solution matrix. It tells us where any starting state goes, not just where one chosen initial condition goes.

For the repeated-eigenvalue example, write A as negative the identity plus a matrix N that has one above the diagonal and zero everywhere else. Multiplying N by itself gives the zero matrix. The identity and N commute, so exponential of A t is exponential of negative t times exponential of N t. But the series for exponential of N t stops after the first power, because N squared is zero. Therefore exponential of A t is exponential of negative t times the matrix with ones on the diagonal and t above the diagonal.

Multiply that matrix by the initial vector x zero, y zero. We immediately recover x equal to exponential of negative t times x zero plus t y zero, and y equal to exponential of negative t times y zero. The time factor is visible as a term in the matrix exponential.

For a diagonalizable matrix, the same definition simplifies in a different way. If A equals P D P inverse, with D diagonal, then exponential of A t equals P times the exponential of D t times P inverse. Exponentiating D means exponentiating each diagonal entry. That is exactly the eigenvector method we used earlier, now written as a single matrix formula. Both methods describe the same evolution operator.

## Why stable eigenvalues do not forbid a temporary surge

In our repeated-root example, both eigenvalues equal negative one. Every solution ultimately tends to zero, because exponential decay wins over any fixed power of t as t becomes large. Yet from initial state zero and one, the x coordinate first rises from zero to one over e. Nothing about a negative eigenvalue says that each coordinate must decrease immediately.

We can make this effect stronger by replacing the one above the diagonal with a large positive number K. The matrix still has negative one as its only eigenvalue, repeated twice. Starting at zero and one, the solution becomes x equals K times t times exponential of negative t, while y equals exponential of negative t.

Choose K equal to ten. At time one, x is ten over e, which is more than three, even though the norm of the original state was one. The entire state has grown substantially before it decays. This is called transient amplification, and it matters in numerical analysis, control, and systems with strong nonnormal coupling. Eigenvalues give long-time exponential rates for constant finite-dimensional systems, but not a universal bound on how large the state can get along the way.

Compare this with the diagonal matrix negative the identity. It has exactly the same two eigenvalues, but every vector simply shrinks as exponential of negative t, with no transient amplification of its Euclidean norm. The two matrices share a spectrum and differ drastically in their short-time behavior. The matrix exponential reveals the difference directly.

## Adding a forcing term

Real systems often have inputs: a heater is switched on, material enters a compartment, or an external force acts on a spring. Write the equation as z prime equals A z plus b of t, where b is an input vector. The homogeneous matrix exponential still tells us how a state evolves after an input has arrived.

The complete solution is the free response, exponential of A t times z zero, plus an integral. Inside the integral, the forcing at an earlier time s is multiplied by exponential of A times t minus s. Then we integrate from zero to t. This is the vector version of the convolution formula we derived for scalar systems.

One way to obtain it is to differentiate exponential of negative A t times z of t. The terms involving A cancel, leaving exponential of negative A t times the input b of t. Integrating and multiplying back by exponential of A t gives the formula. For a constant matrix, these exponentials commute with A, and the algebra is exact.

Try it for our repeated-root system, but add a constant input of one to the y equation. The equations are now x prime equals negative x plus y, and y prime equals negative y plus one. Start from zero and zero. The second equation yields y equals one minus exponential of negative t. Substitute into the first: x prime plus x equals one minus exponential of negative t. Using the integrating factor gives x equal to one minus one plus t times exponential of negative t. To avoid ambiguity, that means one minus the entire quantity one plus t, multiplied by exponential of negative t.

Check it. At time zero, x and y are both zero. The derivative of x is t exponential of negative t, and negative x plus y simplifies to the same expression. As time grows, both coordinates approach one. That limiting state makes sense: at equilibrium, the y equation requires y equal to one, and the x equation then requires x equal to y.

The integral formula gives the same answer. Each small piece of the constant input arrives in the y coordinate and then propagates through the off-diagonal coupling into x. The matrix exponential tells us precisely how that influence depends on the time elapsed since the input arrived.

## What has been gained, and what is next

We now have a complete conceptual picture of real two-dimensional constant-coefficient linear systems. Distinct real eigenvalues give exponential modes along fixed lines. Complex eigenvalues create real rotating modes. Repeated eigenvalues may require generalized eigenvectors and terms like t times an exponential. The matrix exponential brings all three situations under one definition and gives a practical formula for forced problems.

The evolution operator also has a useful time-composition rule. For constant A, evolving for time s and then for time t is the same as evolving for time s plus t. In symbols, exponential of A t times exponential of A s equals exponential of A times t plus s. This is the matrix counterpart of the familiar exponential multiplication rule, and it relies on the same fixed generator A being used for both intervals. For a genuinely time-dependent matrix A of t, simply writing exponential of the integral of A is generally not valid unless the matrices at different times commute.

If you are beginning to study a new system, you can now ask the right questions before memorizing a formula. Is the matrix constant? What does its spectrum say about long-time behavior? Are its eigenvectors sufficient to describe all initial states? Might coupling produce transient growth? What input is present, and how does each past input contribute to the present state?

Those questions turn a first-order system from a collection of symbols into a model of motion. The next foundational tool will be numerical time stepping: how to approximate this evolution when exact eigenvalues or matrix exponentials are unavailable, and how to tell whether a computed trajectory is trustworthy.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: Jordan mode, matrix exponential, and Duhamel formula

Take
\[
A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}=-I+N,
\qquad N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad N^2=0.
\]
Ordinary eigenvector \(v=(1,0)^T\) and generalized eigenvector \(w=(0,1)^T\) obey
\[
(A+I)v=0,\qquad (A+I)w=v.
\]
Therefore \(e^{-t}v\) and \(e^{-t}(w+t v)\) are independent solutions. The full matrix exponential follows from its power series:
\[
 e^{At}=e^{-t}e^{Nt}=e^{-t}(I+tN)
 =e^{-t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\]
For arbitrary \((x_0,y_0)^T\),
\[
\boxed{\mathbf z(t)=e^{-t}(x_0+t y_0,\ y_0)^T.}
\]
Contrast the semisimple repeated eigenvalue case \(A=-I\), where \(e^{At}=e^{-t}I\) and there is no \(t e^{-t}\) term.

### Forced system and the variation-of-constants identity

For constant \(A\) and integrable input \(b(t)\),
\[
\boxed{\mathbf z(t)=e^{At}\mathbf z_0+\int_0^t e^{A(t-s)}b(s)\,ds.}
\]
If \(b(s)=(0,1)^T\), \(\mathbf z_0=0\), the input is constant and
\[
y(t)=1-e^{-t},\qquad x(t)=1-(1+t)e^{-t}.
\]
Directly, \(y'=-y+1\) and \(x'=-x+y\). The steady state is \((1,1)^T\).

### Transient amplification with stable eigenvalues

For \(A_K=\begin{pmatrix}-1&K\\0&-1\end{pmatrix}\) and initial state \((0,1)^T\),
\[
\mathbf z(t)=(Kt e^{-t},e^{-t})^T.
\]
All eigenvalues are \(-1\), yet for \(K=10\), \(\|\mathbf z(1)\|_2=\sqrt{101}/e>1=\|\mathbf z(0)\|_2\). This is finite transient amplification, not asymptotic instability.

### Exercises and worked answers

1. **Repeated eigenvalue check.** Show that \(A=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}\) has only one eigenvector direction. **Answer:** \(A+I=\begin{pmatrix}0&1\\0&0\end{pmatrix}\) has kernel \(\{(x,0)^T\}\).
2. **Critically damped oscillator.** Solve \(x''+2x'+x=0\), \(x(0)=0\), \(x'(0)=1\). **Answer:** \(x(t)=t e^{-t}\); its Laplace transform is \(1/(s+1)^2\).
3. **Forced triangular system.** Verify \(x(t)=1-(1+t)e^{-t}\), \(y(t)=1-e^{-t}\) in \(x'=-x+y,\ y'=-y+1\). **Answer:** \(x'=t e^{-t}=-(1-(1+t)e^{-t})+(1-e^{-t})\), \(y'=e^{-t}=-(1-e^{-t})+1\).
4. **Power-series calculation.** If \(N^2=0\), compute \(e^{Nt}\). **Answer:** \(I+tN\); all higher powers vanish.
5. **Transient growth.** Does \(\Re\lambda<0\) for every eigenvalue forbid \(\|e^{At}\|_2>1\) at some positive time? **Answer:** no; \(A_K\) above with \(K=10\) provides an explicit counterexample.

### Sources and further reading

- MIT OpenCourseWare, *18.03SC*, [Matrix Exponentials](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/matrix-exponentials/).
- MIT OpenCourseWare, *18.03SC*, [Matrix Methods: Eigenvalues and Normal Modes](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iv-first-order-systems/matrix-methods-eigenvalues-and-normal-modes/).
- Wikipedia: [Matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential), [Generalized eigenvector](https://en.wikipedia.org/wiki/Generalized_eigenvector), [Variation of parameters](https://en.wikipedia.org/wiki/Variation_of_parameters).
