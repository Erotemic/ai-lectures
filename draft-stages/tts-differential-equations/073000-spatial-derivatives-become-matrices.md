# Spatial Derivatives Become Matrices: Finite Differences from Taylor's Formula

<!-- BEGIN SPOKEN LECTURE -->

# Spatial Derivatives Become Matrices

Suppose we have a one-meter rod with both ends held at a fixed temperature. We know that diffusion depends on the second derivative of temperature with respect to position. But what if our only temperature measurements are at three sensors inside the rod, together with the two known endpoint temperatures? How can we estimate a second derivative between measurements when we do not even know the full temperature curve?

A finite-difference method answers by replacing a derivative with a comparison of nearby values. The approximation is simple enough to calculate with pencil and paper. The deeper mathematics explains when it is accurate, how boundary values enter, why its matrix has the signs it does, and which properties of diffusion survive after we replace a smooth function by finitely many numbers.

The essential tool is Taylor's formula. We will use it to derive, not merely quote, three difference formulas. Then we will build a matrix for a small boundary-value problem, test its error on functions whose derivatives we know, and show why discrete sine waves behave like the exact modes of a continuous rod.

## Three nearby measurements

Let h denote the positive spacing between measurement points. At a location x, we have a value of a smooth function u. At the next point to the right, x plus h, Taylor's formula says u changes by h times its first derivative, plus h squared over two times its second derivative, followed by smaller terms. Divide that change by h. The result is the familiar forward difference, which estimates the derivative using the current and next values.

The leading error in the forward difference is proportional to h. If we halve the spacing, we expect its leading error to roughly halve, assuming the derivatives remain controlled. The analogous backward difference uses the current and previous values. It has a leading error of the opposite sign in the same simple Taylor expansion.

That suggests an improvement. Subtract the value at x minus h from the value at x plus h, then divide by two h. The second-derivative contributions cancel because they are the same on both sides. The remaining leading error is proportional to h squared, not h. This is the centered first difference.

Try the numbers on a concrete curve. Let u be x squared, and ask for its slope at x equal to one half with h equal to one quarter. The true derivative is one. The forward difference gives one point two five, and the backward difference gives point seven five. Their average, the centered difference, gives exactly one. That exactness is not a coincidence: the centered formula is exact for any quadratic polynomial's first derivative at its center.

For a cubic, centered difference is not exact. Let u be x cubed at the same point and spacing. Its true derivative is three quarters. The centered formula gives thirteen sixteenths, which is point eight one two five. The difference is one sixteenth, precisely h squared. The method is second-order accurate, not magically exact for every function. Comparing such simple functions is an effective way to check the claimed truncation error.

## Why a second derivative uses three points

A second derivative measures how a slope changes. One could approximate the slope on the left interval and on the right interval, then subtract those two slopes and divide by h. The result is the familiar combination: value to the right, minus twice the value at the center, plus value to the left, all divided by h squared.

Taylor's formula explains its accuracy. Add the expansions of u at x plus h and x minus h. The first-derivative terms cancel. The third-derivative terms cancel too. After subtracting twice the center value, the leading term is h squared times the second derivative. Divide by h squared, and the leading error is h squared times the fourth derivative divided by twelve, provided the function is sufficiently smooth.

That symmetry matters. A second derivative built this way is exact for any polynomial of degree at most three. For x to the fourth power at x equal to one half and spacing one quarter, the true second derivative is three. The three-point difference gives three point one two five. The error of one eighth is exactly the Taylor correction two h squared in this example. It is an error we can predict before computing the grid values.

An estimate of error should always say what limit is being considered. Here h approaches zero while the function remains smooth on the relevant neighborhood. If u has a corner or a jump, the fourth derivative may not exist. Then this second-order error statement does not follow. A good numerical method can still be useful for nonsmooth data, but the proof and sometimes the observed rate must change.

## A rod with a finite number of interior values

Place a grid on the interval from zero to one with spacing one quarter. There are five grid points: zero, one quarter, one half, three quarters, and one. Suppose the endpoint temperatures are fixed at zero. Then only the three interior values are unknown. Call their column vector capital U, with entries at the three interior sensors.

At the first interior point, the second difference uses the left endpoint value, the first interior temperature twice, and the second interior temperature. Because the left endpoint is known to be zero, the unknown coefficients in that row are minus two, one, and zero, all multiplied by one over h squared. The middle row has one, minus two, one. The last row has zero, one, minus two. This tridiagonal matrix is the discrete second derivative.

For a grid with spacing one quarter, one over h squared is sixteen. Thus the matrix has negative thirty-two on its main diagonal and positive sixteen immediately above and below it. Its many zero entries are important. Each interior location interacts directly only with its neighbors. As we add more measurement points, the matrix becomes larger but stays sparse.

The same construction works for a stationary boundary-value problem. Suppose the unknown temperature or displacement satisfies negative u double prime equals a known source f, with zero values at both ends. Replace the continuous second derivative by our matrix. The differential equation becomes a linear system for the interior values. Solve the system, and we obtain a discrete approximation to the boundary-value solution.

Take the source f equal to two at every point. The exact solution with zero endpoint values is u of x equal to x times one minus x. Evaluate it at the three interior grid locations. The values are three sixteenths, one quarter, and three sixteenths. Insert these values into the discrete system. Every row gives the source value two exactly. The reason is that the solution is quadratic, and the centered second difference differentiates a quadratic exactly. This example verifies the sign, the h squared factor, and the boundary handling in one calculation.

Do not conclude that all finite-difference boundary-value solutions are exact. We deliberately chose a quadratic case. A more realistic profile with nonzero fourth derivative produces a spatial truncation error. Later we will see how that error combines with the error from advancing time.

## The matrix remembers diffusion's sign

The continuous second derivative with zero endpoint values has a useful energy property. Multiply u double prime by u and integrate by parts. The result is minus the integral of the squared slope. Apart from the zero function, that quantity is negative. This underlies the decay of heat modes and the uniqueness of many boundary-value solutions.

The discrete matrix has a parallel identity. Take any vector of interior values and extend it with zero endpoint values. Multiply the vector by the matrix and then take the dot product with the original vector. After collecting neighboring terms, the result is minus one over h squared times the sum of squared differences between adjacent values. Every square is nonnegative, so the entire expression is nonpositive. Because both endpoints are zero, it vanishes only when every interior value is zero.

Thus our discrete second-derivative matrix is symmetric and negative definite. Its eigenvalues are real and negative, just as we want for a model that damps spatial temperature variations. We did not impose this by an arbitrary numerical rule. The difference operator inherited an energy sign from the underlying derivative and boundary conditions.

For nonzero prescribed endpoint values, the matrix acting on the unknown interior vector is the same, but the known boundary contributions move to a forcing vector. A Neumann condition specifying a derivative rather than a value requires a different boundary treatment. One can use a ghost point or a flux balance, but it is important to distinguish the boundary formula from the interior formula and to check whether a constant solution should be allowed. A zero-flux boundary has different conservation properties from a fixed-temperature boundary.

## Check the discrete spectrum against the exact one

The continuous fixed-end eigenfunctions are sine waves. On an evenly spaced grid, evaluate a sine wave at the interior nodes. The same sampled sine vector turns out to be an eigenvector of the tridiagonal second-difference matrix. Its eigenvalue is negative four over h squared times the square of a sine of half the discrete phase step.

For the first mode on our quarter-spaced grid, the exact continuous second-derivative eigenvalue is negative pi squared, approximately negative nine point eight seven. The discrete eigenvalue is about negative nine point three seven. The difference reflects the spatial approximation; the discrete matrix is not secretly the exact continuous operator.

As h decreases while the physical interval remains fixed, the discrete first eigenvalue moves toward negative pi squared. The high-frequency grid modes behave differently because their wavelengths are comparable to the grid spacing. A mesh cannot accurately represent spatial changes that occur between its samples. This fact will become critical when we decide how small the time step must be in a numerical heat solver.

The matrix also has a largest-magnitude negative eigenvalue whose size grows roughly like one over h squared. A finer spatial grid therefore introduces faster numerical decay modes. More spatial resolution means more numerical unknowns and some very fast dynamics. That is why a time-step size that was stable on a coarse grid can become unstable after refining the spatial grid—even if the physical diffusion coefficient has not changed.

## Variable conductivity and conservation

The centered three-point matrix assumes a constant coefficient in front of the second derivative. Real materials may have conductivity that depends on position. Then the physically conservative diffusion operator is not generally conductivity times u double prime. It is the spatial derivative of conductivity times the spatial gradient.

The corresponding grid idea is straightforward. Approximate the heat flux across the right face of a small cell from the difference between its center and its right neighbor. Do the same across the left face. The net outward flux is the right flux minus the left flux. Divide by the cell width to obtain the rate of change caused by conduction. Interior face fluxes cancel when we sum over cells, because heat leaving one cell enters the next.

This flux-difference construction is central to conservative finite-volume methods, and it also guides good finite differences for variable coefficients. We are not developing the full machinery here. The essential lesson is that choosing a discrete formula is not just a matter of copying derivatives. We should preserve the governing balance laws whenever possible.

We now have a spatial approximation with a clear error order, an explicit sparse matrix, an energy identity, and a discrete set of sine modes. That is enough to construct a numerical time-dependent heat solver. Instead of trying to solve a partial differential equation directly at every point in space and time, we will let the grid values form a vector and solve an ordinary differential equation for that vector. The time integrators we already studied will do the rest—but they will have to respect the fast eigenvalues of the spatial matrix.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: Taylor formulas and the discrete Laplacian

For sufficiently smooth \(u\):
\[
D_+u(x)=\frac{u(x+h)-u(x)}{h}=u'(x)+\frac h2u''(x)+O(h^2),
\]
\[
D_0u(x)=\frac{u(x+h)-u(x-h)}{2h}=u'(x)+\frac{h^2}{6}u'''(x)+O(h^4),
\]
\[
D_{xx}u(x)=\frac{u(x+h)-2u(x)+u(x-h)}{h^2}=u''(x)+\frac{h^2}{12}u^{(4)}(x)+O(h^4).
\]
For \(u=x^3,x=1/2,h=1/4\), \(u'=3/4\), \(D_0u=13/16\). For \(u=x^4\), \(u''=3\), \(D_{xx}u=25/8=3.125\).

With \(h=1/4\), \(x_i=ih\), \(i=0,1,2,3,4\), and homogeneous Dirichlet endpoints, the interior second difference is
\[
A_h=\frac1{h^2}\begin{pmatrix}-2&1&0\\1&-2&1\\0&1&-2\end{pmatrix}.
\]
The discrete Poisson equation \(-A_hU=2(1,1,1)^T\) has solution \(U=(3/16,1/4,3/16)^T\), samples of \(u=x(1-x)\).

For \(v_0=v_4=0\), the discrete summation-by-parts identity is
\[
\mathbf v^T A_h\mathbf v=-\frac1{h^2}\sum_{i=0}^{3}(v_{i+1}-v_i)^2<0
\quad\text{for nonzero interior }\mathbf v.
\]
For an interval with \(N\) equal subintervals, \(h=L/N\), discrete sine vectors \(v_i^{(m)}=\sin(m\pi i/N)\), \(m=1,\ldots,N-1\), satisfy
\[
A_hv^{(m)}=\lambda_{h,m}v^{(m)},\quad
\lambda_{h,m}=-\frac4{h^2}\sin^2\!\left(\frac{m\pi}{2N}\right).
\]
At \(L=1,N=4,m=1\), \(\lambda_{h,1}=-64\sin^2(\pi/8)\approx-9.37258\), while the continuum eigenvalue is \(-\pi^2\approx-9.86960\).

For conductivity \(a(x)>0\), the conservative divergence-form operator is \((a(x)u_x)_x\). A face-flux approximation is
\[
(A_h^{(a)}U)_i=\frac1h\left[a_{i+1/2}\frac{U_{i+1}-U_i}{h}-a_{i-1/2}\frac{U_i-U_{i-1}}{h}\right].
\]

### Exercises with worked answers

1. Use forward and centered first differences for \(u=x^2\), at \(x=1/2,h=1/4\). **Answer:** forward \(5/4\), centered \(1\), exact derivative \(1\).
2. Check the middle row of \(-A_hU=2\mathbf1\) with \(U=(3/16,1/4,3/16)^T\). **Answer:** \(-16(3/16-2/4+3/16)=2\).
3. Why is \(A_h\) invertible under zero Dirichlet boundary conditions? **Answer:** its quadratic form is strictly negative for every nonzero interior vector, so its kernel is trivial.
4. What is the leading truncation-error order of a centered second derivative for smooth \(u\)? **Answer:** order \(h^2\), with leading term \(h^2u^{(4)}/12\).
5. If the number of grid subintervals doubles on the same rod, what happens to the magnitude of the most negative eigenvalue? **Answer:** it grows by roughly a factor of four, since it scales as \(1/h^2\).

### Sources and further reading

- [Gilbert Strang, MIT 18.086, Finite Difference Methods](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/pages/lecture-notes/).
- [TU Delft, MUDE Numerical Methods for PDEs, Diffusion Equation](https://mude.citg.tudelft.nl/book/2025/numerical_methods_for_PDEs/diffusion_equation.html).
- [Wikipedia, Finite difference](https://en.wikipedia.org/wiki/Finite_difference), for Taylor expansions and centered difference formulas.
