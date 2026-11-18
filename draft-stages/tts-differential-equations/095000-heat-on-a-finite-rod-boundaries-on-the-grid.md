# Heat on a Finite Rod: Putting Boundaries on the Grid

<!-- BEGIN SPOKEN LECTURE -->

# Heat on a Finite Rod: Putting Boundaries on the Grid

Imagine heating the right end of a metal rod while holding its left end at a fixed temperature. The middle responds gradually. At first the temperatures near the hot end climb, then the warming spreads, and eventually the rod approaches a straight temperature profile. We know the differential equation for heat flow, and we know how to replace spatial derivatives by differences. What is easy to miss is that the two end conditions are not decorations on that calculation. They are part of the numerical problem. Change them, and the very meaning of the answer changes.

To make this concrete, take a rod running from position zero to position one. Let its temperature be U of position and time. Assume the heat diffusivity is one in our chosen units. The temperature's rate of change equals its second spatial derivative. We will use a grid with four equal subintervals. Its five positions are zero, one quarter, one half, three quarters, and one. Each grid point stores a temperature, and the distance between neighbors is one quarter.

Here is the first decision: suppose the left endpoint is kept at zero and the right endpoint at one. These are *Dirichlet boundary conditions*. The temperature at those two points is known, not predicted by the heat equation. At every time step, the endpoint entries stay at zero and one. The other three entries must be computed.

## Three unknown temperatures, not five

For an interior point, approximate the second derivative by the left neighbor's temperature minus twice the center's temperature plus the right neighbor's, divided by the square of the spacing. Since the spacing is one quarter, division by its square means multiplication by sixteen. The first interior point has the fixed zero endpoint on its left. The last interior point has the fixed one endpoint on its right. So the two boundary values enter the equations for nearby interior points, even though the endpoints are not unknowns.

Write the interior temperatures as a column with three entries. The matrix of second differences has negative thirty-two down its diagonal and sixteen immediately above and below the diagonal. There is also a forcing column whose first two entries are zero and whose last entry is sixteen. That last sixteen is the contribution from the hot right boundary. If you omit it, the code is solving a different problem: one with zero temperature at both ends.

Let's solve a small time step by hand. Suppose the interior of the rod initially has temperature zero, while the right endpoint is maintained at one. Take a time step of one sixty-fourth. The dimensionless ratio of time step to squared grid spacing is one quarter. Forward Euler says: new interior temperature equals old temperature plus one quarter times left neighbor minus twice center plus right neighbor.

At the first step, only the point at three quarters warms. Its new temperature is one quarter. The other two interior values remain zero. At the second step, the middle point reaches one sixteenth, and the three-quarter point reaches three eighths. The numbers are small, but the mechanism is visible. The boundary information travels inward through the nearest-neighbor couplings; the continuum heat equation has immediate influence everywhere, while a single explicit grid step consults only its adjacent nodes.

What should happen after many steps? The steady temperature satisfies a zero second derivative, so it is a straight line from zero to one. At the grid positions the answer is one quarter, one half, and three quarters. This particular linear profile is also an exact steady solution of the discrete equations. Checking that it makes every right-hand side zero is a useful test of the boundary implementation.

## A different physical experiment: insulating the ends

Now replace the fixed-temperature conditions by insulated ends. An insulated endpoint has no heat flux through it. For constant conductivity, that means the spatial temperature derivative vanishes at the endpoint. This is a *Neumann boundary condition*. We no longer know the endpoint temperatures in advance. They evolve with the rest of the rod, but their slopes at the boundary must be zero.

How can we approximate a second derivative right at an endpoint when the centered formula seems to need a point outside the rod? One standard device is a *ghost point*. At the left endpoint introduce a fictional grid point one step to the left. A centered approximation to zero slope says that the ghost value equals the temperature one step inside the rod. Substituting that ghost value into the usual second-difference formula produces twice the difference between the first interior temperature and the boundary temperature, divided by the squared spacing. At the right endpoint the construction is symmetric.

The factor of two has a simple physical interpretation. A boundary node represents only half as much rod as an interior node when we use the trapezoidal rule to measure total heat. For the same heat crossing the adjacent interface, a half-sized boundary volume changes temperature twice as rapidly. That picture connects the ghost-node formula to a finite-volume construction.

Here is a three-node example, using just two subintervals so the arithmetic fits in our heads. The spacing is one half. Initially, the left endpoint has temperature one and the center and right endpoint have temperature zero. Both ends are insulated. Choose a time step with the diffusion ratio equal to one quarter. The left boundary loses half its temperature and ends at one half. The middle gains one quarter. The right endpoint stays zero. If we just add the three node values, their sum has changed from one to three quarters. Does that mean heat disappeared?

No. Adding node temperatures with equal weights is the wrong calculation for these nodes. Give the endpoints half weight and the middle full weight, then multiply by the grid spacing. Initially the weighted sum is one quarter. After the step it is still one quarter: the left half weight contributes one quarter, and the middle contributes another one quarter before multiplication by one half. More explicitly, the weighted bracket is one half at both times, and its product with the half-unit spacing is one quarter. The insulation condition is doing exactly what it should: no heat entered or left.

This is worth distinguishing from the fixed-temperature rod. When a hot boundary reservoir holds its temperature at one, energy may flow into the rod from that reservoir. Conservation of the rod's total heat is then not expected. A correct fixed-temperature solver and a correct insulated solver should pass different physical checks.

## What happens when a boundary flux is prescribed?

An endpoint can also have a specified nonzero heat flux. For example, a heater can inject a known amount of energy per unit time. Mathematically, one may specify the spatial derivative or, more physically, the outward heat flux. These differ by a sign and by the conductivity. It is dangerous to write 'positive flux' in an implementation without saying which direction positive means.

With the convention that the derivative from left to right is given, the rate of change of total heat is diffusivity times the right-end derivative minus the left-end derivative, plus any internal heat sources. This follows directly by integrating the heat equation over the rod. A consistent ghost-point discretization reproduces the same balance, with an appropriate weighted grid sum. That is a stronger test than merely obtaining a smooth-looking temperature plot.

We can even have a constant flux at one end and zero flux at the other. Then there is a net gain or loss of heat, so a steady temperature generally cannot exist without some compensating source or sink. This is the time-dependent cousin of the compatibility condition for a steady Neumann boundary-value problem.

## Why boundary rows deserve their own tests

A grid implementation often places its boundary logic in a few lines of code. Those lines do enormous work. The interior second difference can be perfectly correct while the boundary rows leak mass, inject energy, or impose the wrong physical condition. A first-order one-sided approximation to a derivative may also reduce the overall accuracy of a nominally second-order interior scheme. Ghost nodes are one way to retain a centered construction, but they are not the only way; finite volumes and carefully derived boundary stencils are alternatives.

Three tests are particularly informative. First, check a known steady solution, like the straight line connecting fixed endpoint temperatures. Second, check a conserved quantity under insulated conditions, using the correct endpoint weights. Third, compare a computed solution with a manufactured exact solution whose time dependence and boundary values are known. A small residual in the interior is not enough if the boundary equation is wrong.

We have now made the phrase 'solve the heat equation on a grid' much more precise. We have to decide what the grid stores, which values are prescribed, how the boundary acts on neighboring unknowns, and which balance law the entire assembly should respect. The spatial second-difference formula is only one piece. In the next stage of understanding, we can ask whether repeated updates preserve physical inequalities and whether they amplify or dissipate disturbances. Those are questions of stability and energy, and they depend on the boundary construction we have just made.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: Dirichlet and Neumann boundary rows

For the heat equation on \(0<x<L\),
\[
 u_t=\kappa u_{xx}+f(x,t),\qquad x_i=ih,\qquad h=L/N,
\]
the centered interior difference is \((D_{xx}U)_i=(U_{i-1}-2U_i+U_{i+1})/h^2\).

**Dirichlet data.** If \(U_0=a(t)\), \(U_N=b(t)\), the interior ODEs are
\[
 \dot{\mathbf U}=\kappa h^{-2}\begin{bmatrix}-2&1&&\\1&-2&1&\\&\ddots&\ddots&1\\&&1&-2\end{bmatrix}\mathbf U+\kappa h^{-2}(a,0,\ldots,0,b)^T+\mathbf f.
\]
For \(L=1,N=4,\kappa=1,a=0,b=1\), the interior matrix is \(16\operatorname{tridiag}(1,-2,1)\) and the forcing is \((0,0,16)^T\). The unique steady grid function is \((U_1,U_2,U_3)=(1/4,1/2,3/4)\). At \(r=\kappa\Delta t/h^2=1/4\) with zero interior initial values, two forward Euler steps give
\[
 \mathbf U^0=(0,0,0),\quad\mathbf U^1=(0,0,1/4),\quad\mathbf U^2=(0,1/16,3/8).
\]

**Neumann data.** Write spatial derivatives \(u_x(0,t)=g_L(t)\), \(u_x(L,t)=g_R(t)\). The centered ghost relations are \(U_{-1}=U_1-2hg_L\) and \(U_{N+1}=U_{N-1}+2hg_R\). Thus
\[
 \dot U_0=\kappa\left(\frac{2(U_1-U_0)}{h^2}-\frac{2g_L}{h}\right)+f_0,\qquad
 \dot U_N=\kappa\left(\frac{2(U_{N-1}-U_N)}{h^2}+\frac{2g_R}{h}\right)+f_N.
\]
Define the trapezoidal mass \(M_h=h[U_0/2+\sum_{i=1}^{N-1}U_i+U_N/2]\). Multiply the nodal ODEs by their trapezoidal weights; the interior differences telescope, leaving
\[
 \frac{dM_h}{dt}=\kappa(g_R-g_L)+h\left(f_0/2+\sum_{i=1}^{N-1}f_i+f_N/2\right).
\]
For homogeneous Neumann data and zero source, \(M_h\) is exactly conserved by both the semidiscrete ODE and its forward Euler step. With \(N=2,h=1/2,r=1/4\), initial \((1,0,0)\) becomes \((1/2,1/4,0)\); both weighted masses equal \(1/4\).

**Boundary subtlety.** The outward physical flux is \(q\cdot n=-k\partial_n u\), not simply \(\partial_xu\). At a left boundary the outward normal is negative and at a right boundary positive. Also, the ghost boundary formula has a centered spatial derivative but a boundary truncation error that must be analyzed with the full scheme; naming a stencil 'centered' does not automatically establish a global accuracy order for arbitrary boundary data.

### Exercises with worked answers

1. With fixed endpoint values \(a=2,b=6\) on a unit rod, what is the steady interior temperature at \(x=1/4,1/2,3/4\)? **Answer:** \((3,4,5)\), the linear interpolation of the boundary data.
2. With \(h=1/4,\kappa=2\), what is \(r\) for \(\Delta t=1/128\)? **Answer:** \(r=2(1/128)/(1/16)=1/4\).
3. For insulated boundaries with \(N=2\), why should the endpoint temperature not be assigned the same mass weight as the center? **Answer:** the endpoints represent half control volumes; trapezoidal weights ensure adjacent fluxes cancel in the total heat balance.
4. Suppose \(u_x(0)=1\), \(u_x(1)=0\), \(\kappa=1\), and \(f=0\). What is \(dM_h/dt\)? **Answer:** \(-1\) with the stated left-to-right derivative convention. The loss is through the left boundary.
5. Why is fixing \(U_0\) and \(U_N\) inappropriate for a physically insulated rod? **Answer:** it imposes temperature reservoirs rather than zero flux and generally destroys the correct conserved heat balance.

### Sources and further reading

- [Hans Petter Langtangen and Svein Linge, *Finite Difference Computing with PDEs*, open-access book, Chapters on wave and diffusion equations](https://link.springer.com/book/10.1007/978-3-319-55456-3).
- [MIT OpenCourseWare, 18.086 *Mathematical Methods for Engineers II*, finite differences and wave/heat equations](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/resources/lecture-videos/).
- [Wikipedia: Neumann boundary condition](https://en.wikipedia.org/wiki/Neumann_boundary_condition).
