# Green's Functions: An Elliptic Equation as an Integral Operator

**Track:** Multivariable Calculus from First Principles. **Focus:** point-source responses, the exact Dirichlet Green function on an interval, boundary correction, fundamental solutions, reciprocity, and spectral inverses.

<!-- BEGIN SPOKEN LECTURE -->

# Green's Functions: An Elliptic Equation as an Integral Operator

Suppose we know how to solve a differential equation when the source is concentrated at just one place. Could we then solve the equation for an arbitrary distributed source by adding all those single-location responses together?

For linear differential equations, that is often exactly the right idea. A Green's function is a catalog of responses to idealized point sources. The equation's solution is built by integrating the source against that catalog. It is the continuum analogue of writing the inverse of a matrix one column at a time.

That analogy is more than a metaphor. If a matrix maps a vector of unknowns to a vector of loads, the j-th column of its inverse tells us the response to a unit load at coordinate j. For a differential operator, the source location ranges over every point in a domain. We replace a matrix column index by a continuous variable, and a matrix-vector product by an integral.

We will derive a complete example on an interval, including its signs and boundary conditions. That one calculation contains most of the structure that remains useful in higher dimensions.

## A point source makes a kink

Start with negative u double prime equals f on the interval from zero to one, with u zero at the endpoints. Select a point y strictly between those endpoints. Instead of a smooth f, imagine a unit point load concentrated at y. We call that load the Dirac delta at y. It is not an ordinary function. Its defining property is that integrating a test function against the delta selects the test function's value at y.

Away from y, the source is zero. Therefore the response must have second derivative zero on the interval to the left and on the interval to the right. It is a straight line on each side. The two lines meet continuously at the source location, but their slopes need not agree. In fact, the slope jump is what encodes the point load.

Let G of x comma y denote the response measured at x to a point source at y. The left boundary condition requires the left line to be a multiple of x. The right boundary condition requires the right line to be a multiple of one minus x. Continuity at y and the integrated differential equation determine the two multipliers.

The result is pleasantly simple. If x is no farther right than y, G is x times one minus y. If x is to the right of y, G is y times one minus x. Equivalently, G is the smaller of x and y times one minus the larger of x and y.

Check the numbers. Put the source at y equal to one quarter. To its left, the response is three quarters times x. To its right, the response is one quarter times one minus x. At x equal to one quarter, both formulas give three sixteenths. The slope is three quarters on the left and negative one quarter on the right. It drops by exactly one. Thus the negative second derivative, interpreted as a distribution, has a positive unit delta there.

This is the crucial sign check. The Green function is nonnegative, and its slope decreases at the applied positive load. Reversing the sign of the operator would reverse which kernel solves the equation.

## Build a solution from all point sources

Now let f be a genuine source distributed across the interval. For every possible source location y, imagine a tiny load of size f of y times a tiny interval width. Its contribution at x is that load multiplied by G of x comma y. Adding all the contributions and taking the continuum limit gives the integral of G of x comma y times f of y, with respect to y from zero to one.

Why does this solve the equation? Because the differential operator acts on the x variable. It passes through the integral and replaces the negative second derivative of G by the delta at y. Integrating that delta against f returns f of x. Also, each G vanishes at both endpoints, so the integral has the correct boundary values.

Let's use the constant source two. The formula has two pieces, because the Green function changes expression when y passes x. From y equal to zero up to x, the integrand is two times y times one minus x. From x to one, it is two times x times one minus y. The first integral contributes x squared times one minus x. The second contributes x times the square of one minus x. Adding them gives x times one minus x.

We recovered the parabola from the maximum-principle example, but by a completely different route. There we used a differential inequality and a barrier to bound or characterize the solution. Here we have reconstructed the solution as the sum of responses to elementary loads.

Observe the sign information built into this representation. If f is everywhere nonnegative, the Green function is nonnegative, so the integral cannot be negative. The comparison principle has become visible as positivity of the kernel. For the Dirichlet Laplacian on a suitable bounded domain, the same relation holds. But not every inverse operator has a nonnegative kernel; positivity is a theorem about this differential operator and its boundary conditions, not a generic property of matrix inversion.

## The boundary condition is part of the kernel

It is tempting to call any solution to the point-source equation a Green function and stop there. But the boundary condition determines which point-source response we need.

On the entire real line, negative second derivative equals a delta is solved, among other choices, by negative one half times the absolute distance from x to y. Its derivative jumps downward by one. Yet this function does not vanish at zero and one, and so it is not our interval's Dirichlet Green function. We had to add a piecewise linear homogeneous correction that enforces the boundary values. The correction is not a minor implementation detail: changing the boundary changes the inverse operator.

In higher dimensions there is a standard starting point called a fundamental solution. In three dimensions, the fundamental solution of negative Laplacian is one divided by four pi times the distance to the source. In two dimensions it is negative one over two pi times the logarithm of that distance. Both are singular at the source, and their Laplacians equal a point delta in the distributional sense.

On a bounded domain, an appropriate Dirichlet Green function is obtained by subtracting a harmonic correction whose boundary trace agrees with the fundamental solution. This correction removes the unwanted boundary values. The singularity still records the point source, while the regular part records how the boundary redirects its influence.

If the boundary itself is held at a nonzero temperature, there is also a boundary contribution to the representation. For a smooth domain and sufficiently regular data, that contribution involves the outward normal derivative of the Green function. It is not included in the zero-boundary integral we just computed. The safest habit is to state the domain, the operator, and the boundary condition whenever we introduce a Green function.

## A source at one point is not an ordinary energy load

There is a subtle functional-analysis issue. In one dimension, point evaluation of an H-one function is a continuous functional, so a delta load can be handled naturally in the weak energy framework. In dimensions two and higher, point evaluation is not continuous on ordinary H-one spaces. A Dirac delta need not belong to the dual space H minus one. The Green function is then typically singular enough that it is not an H-one solution at the source.

This does not make the construction invalid. It means the singular point-source response is understood distributionally, or through an approximation by smooth concentrated loads, and then used under appropriate integrability conditions. The final solution for a sufficiently regular distributed f can be much smoother than each singular building block.

That distinction is worth keeping. Inverse kernels can exist in a broader sense than an inverse defined on a chosen Hilbert-space dual. A careless appeal to Lax–Milgram with a delta load in three dimensions would misapply the theorem even though the familiar one-over-distance fundamental solution is perfectly meaningful as a distribution.

## Reciprocity and the spectral picture

Return to our explicit interval kernel. Swap x and y. Nothing changes: the smaller and larger of the two numbers are the same regardless of order. Thus G of x comma y equals G of y comma x. This symmetry is called reciprocity.

It reflects the self-adjointness of the negative Dirichlet Laplacian. In a finite-dimensional analogy, a symmetric positive-definite matrix has a symmetric inverse. In the continuum, the inverse is a self-adjoint integral operator, and its kernel is symmetric when the representation is justified. For a nonsymmetric drift-diffusion operator, the forward Green kernel need not be symmetric. Its transpose relation involves the Green kernel of the adjoint operator instead.

The interval also has a spectral description. Its zero-boundary eigenfunctions are sine waves. The n-th sine wave has negative-Laplacian eigenvalue n squared times pi squared. To invert the operator, divide each Fourier sine coefficient of the source by that eigenvalue. In other words, a high-frequency component is reduced by a factor proportional to one over n squared.

The Green kernel can therefore be expressed as a sum of products of sine functions, each weighted by the reciprocal eigenvalue. The kink formula and the sine-series formula describe the very same operator. One emphasizes where a source is located; the other emphasizes its frequency content. The first explains positivity and spatial influence. The second explains smoothing and spectral decay.

This is also why the constant mode becomes important in a Neumann problem. For Neumann conditions, constants lie in the kernel of the Laplacian. The inverse does not exist on the full space. We must restrict to mean-zero sources, fix the solution's additive constant, and use a normalized or generalized Green kernel. That kernel need not be everywhere positive, because it must account for the removed constant mode.

## What a Green function can and cannot tell us

A positive Green kernel gives a comparison-friendly picture of an elliptic response. A symmetric kernel reveals reciprocity. A singularity identifies the local effect of a point source. Boundary corrections record the geometry of the domain. And the eigenfunction expansion connects the inverse PDE operator to the spectral calculus of positive operators.

But none of these observations says that the kernel is easy to compute on an arbitrary domain, that its singularity is harmless in every norm, or that a bounded energy solution can always be evaluated at a particular point. The hypotheses and function spaces matter just as they did for maximum principles and regularity.

Green's functions therefore sit at a productive crossroads. They turn differential equations into integral equations, convert positivity into kernel signs, connect boundary-value problems to potential theory, and expose the same inverse-operator viewpoint that drives numerical linear algebra. They also prepare a new question: if we cannot calculate the kernel explicitly, what estimates can we derive directly from the weak equation?

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Dirichlet kernel on the unit interval

For \(L=-d^2/dx^2\) on \((0,1)\) with zero Dirichlet data,
\[
G(x,y)=\begin{cases}x(1-y),&0\le x\le y\le1,\\y(1-x),&0\le y\le x\le1.\end{cases}
\]
For fixed \(y\), the one-sided derivatives in \(x\) are \(1-y\) and \(-y\), so \(G_x(y^+,y)-G_x(y^-,y)=-1\). Therefore \(-\partial_{xx}G(\cdot,y)=\delta_y\), \(G(0,y)=G(1,y)=0\).

### Constant source and eigenfunction expansion

\[
\begin{aligned}
u(x)&=\int_0^1G(x,y)\,2\,dy\\
&=2(1-x)\int_0^x y\,dy+2x\int_x^1(1-y)\,dy\\
&=x(1-x).
\end{aligned}
\]
With \(\varphi_n(x)=\sqrt2\sin(n\pi x)\), \(L\varphi_n=(n\pi)^2\varphi_n\), and
\[
G(x,y)=\sum_{n=1}^{\infty}\frac{2\sin(n\pi x)\sin(n\pi y)}{(n\pi)^2}.
\]
The series converges absolutely and uniformly on \([0,1]^2\). Symmetry is immediate termwise.

### Fundamental solutions, dimensions at least two

For \(d\ge3\), \(\Phi(x)=((d-2)|S^{d-1}|)^{-1}|x|^{2-d}\); for \(d=2\), \(\Phi(x)=-(2\pi)^{-1}\log|x|\). These satisfy \(-\Delta\Phi=\delta_0\) in distributions. On a sufficiently regular bounded domain, the Dirichlet kernel can be written \(G_\Omega(x,y)=\Phi(x-y)-h_y(x)\), where \(h_y\) is harmonic with boundary value \(\Phi(\cdot-y)\). For suitable smooth data,
\[
u(x)=\int_\Omega G_\Omega(x,y)f(y)\,dy-\int_{\partial\Omega}g(y)\,\partial_{n_y}G_\Omega(x,y)\,dS_y.
\]
Do not place a point delta in \(H^{-1}(\Omega)\) automatically in dimensions \(d\ge2\).

### Exercises and answers

1. **Slope test.** For \(y=1/4\), what is \(G(y,y)\)? **Answer:** \(3/16\), with derivative jump \(-1\).
2. **Symmetry.** Show directly that \(G(x,y)=G(y,x)\). **Answer:** Both equal \(\min(x,y)(1-\max(x,y))\).
3. **Integral solve.** What is the solution for source \(f\equiv1\)? **Answer:** \(u(x)=\tfrac12x(1-x)\).
4. **Boundary variation.** Why can't the free-space fundamental solution replace the interval kernel? **Answer:** It fails the prescribed endpoint values; a harmonic correction is required.
5. **Neumann kernel.** Why is the reciprocal of the zero eigenvalue unavailable? **Answer:** Constants form the nullspace. Impose mean-zero compatibility and a normalization before constructing a generalized inverse.

### Sources and further reading

- [Jared Speck, MIT OpenCourseWare, *Introduction to PDEs*, Lecture 8: Green Functions (2011)](https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/b4b519bd697528af7e9c83d130bb945b_MIT18_152F11_lec_08.pdf), boundary-corrected Green kernels and integral representations (note that these notes use the opposite sign convention for the Laplacian).
- [Wikipedia: Green's function](https://en.wikipedia.org/wiki/Green%27s_function), distributional inverse-kernel construction and boundary-value examples.
- [Wikipedia: Fundamental solution](https://en.wikipedia.org/wiki/Fundamental_solution), free-space singular kernels for the Laplacian.
- Companion in this library: `multivariable-calculus:045000` on regularity and `linear-algebra:019000` on matrix exponentials and spectral constructions.
