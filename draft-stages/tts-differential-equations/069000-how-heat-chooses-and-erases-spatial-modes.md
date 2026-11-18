# How Heat Chooses and Erases Spatial Modes

<!-- BEGIN SPOKEN LECTURE -->

# How Heat Chooses and Erases Spatial Modes

Put a thin metal rod between two temperature-controlled reservoirs. Heat can move along the rod. In some regions its temperature may initially be higher than in others. Over time, the temperature becomes smoother. If the two ends are held at the same temperature and there is no continuing heat source, the entire rod eventually approaches that temperature.

Can we derive that behavior rather than merely describe it? The heat equation is a simple and important partial differential equation. It has a time derivative and a second derivative in space. We will build it from a balance law, use boundary conditions to select a family of spatial shapes, and reduce the evolution of each shape to a first-order ordinary differential equation. Then we will work all the way through a nontrivial initial temperature profile to a Fourier series whose coefficients can be checked by direct integration.

This is a bridge from calculus and elementary ODEs to partial differential equations. We do not need a theory of Sobolev spaces to start. We do need to be clear about what varies in space, what varies in time, and which information lives on a boundary.

## From heat conservation to a differential equation

Let u of x and t be the temperature of a rod. Assume it has constant cross section and material properties, and that heat moves predominantly along its length. A small segment stores thermal energy in proportion to its length and its temperature change. The proportionality contains density and specific heat capacity.

Heat can enter the segment at its left face, leave at its right face, and be produced inside it. Fourier's law says the conductive heat flux points down the temperature gradient. When the right side is hotter than the left, the temperature rises with x and the rightward heat flux is negative: heat actually travels left. This sign is a physical check on the law, not a cosmetic convention.

Apply conservation to the segment and shrink it to a point. The rate of change of stored heat equals minus the spatial derivative of conductive flux, plus any internal heating. With constant conductivity and no internal source, we obtain u sub t equals kappa times u sub x x. The coefficient kappa, thermal diffusivity, is conductivity divided by density times heat capacity. Its units are length squared divided by time. Large kappa means changes in temperature spread more quickly over a fixed distance.

The notation u sub t means the derivative with respect to time while holding position fixed. The notation u sub x x means the second spatial derivative while holding time fixed. Keeping those roles separate matters. The equation is first order in time, so it needs one initial temperature profile; it is second order in space, so it also needs suitable information at the two endpoints of a finite rod.

There are several possible boundary experiments. We can hold both ends at zero relative temperature. We can insulate both ends so their slopes vanish. Or we can hold one end at a fixed temperature and insulate the other. We will begin with zero temperatures at both ends, because that is exactly the fixed-end eigenvalue problem whose sine functions we can derive with a few lines of algebra.

## Separate space from time

Consider the unit interval from zero to one, with u equal to zero at both endpoints. Try a special kind of solution: a spatial shape X of x multiplied by an amplitude T of t. This is not a claim that every solution is a single product. It is a way to search for building blocks that can later be added together.

Substitute X times T into the heat equation. Its time derivative is X times T prime. Its second spatial derivative is X double prime times T. Divide by the product where it is nonzero. We find T prime divided by kappa times T equals X double prime divided by X.

The left side can depend only on time; the right side can depend only on position. If the equality holds throughout an open region, each side must equal the same constant. It is convenient to call that constant negative lambda. The spatial equation is negative X double prime equals lambda X. The temporal equation is T prime equals negative kappa lambda times T.

The boundary conditions on u become zero boundary conditions on X, provided T is not identically zero. We already know the allowed spatial shapes: sine of n pi x, for positive integers n. Their lambda values are n squared pi squared. The equation for each temporal amplitude is one of the first ODEs we ever solved. Its solution decays exponentially, with exponent negative kappa n squared pi squared times t.

Combine the two pieces. For each positive integer n, the function sine of n pi x multiplied by that exponential is a solution of the heat equation and satisfies both endpoint conditions. Check it directly: the time derivative multiplies the function by negative kappa n squared pi squared; two spatial derivatives multiply it by negative n squared pi squared. Multiplying the latter by kappa gives exactly the same result.

Now compare the first and third modes. The first decays at a rate proportional to one. The third decays at a rate proportional to nine. Fine spatial changes, which require large mode numbers, disappear faster than broad smooth changes. This is a mathematical explanation of why heat diffusion smooths temperature profiles.

## A single temperature profile can contain many modes

Our initial temperature generally will not be a single sine wave. Let us choose a familiar smooth shape that is zero at both ends: f of x equals x times one minus x. It is a parabola peaking at one quarter in the middle. Its Fourier sine coefficients can be found from orthogonality. Multiply by sine of n pi x, integrate from zero to one, and multiply by two.

Two integrations by parts give a remarkably simple answer. For even n, the coefficient is zero. For odd n, it is eight divided by n cubed times pi cubed. So the parabola consists of the first sine mode, plus one twenty-seventh of that coefficient times the third sine, plus one one-hundred-twenty-fifth times the fifth, and so on, with positive coefficients for odd n.

The sign pattern is worth checking against the function. The sine of three pi x is positive near the left end, negative in the central third, and positive near the right. The higher modes correct the rounded first-sine shape so their sum becomes exactly the parabola. Their coefficients rapidly decrease because the initial profile is smooth inside the interval and already matches the zero endpoint values.

To evolve this initial temperature, let every sine coefficient decay according to its own spatial eigenvalue. The first coefficient receives the factor exponential of negative kappa pi squared t. The third gets exponential of negative nine kappa pi squared t. The fifth gets exponential of negative twenty-five kappa pi squared t. The result is an infinite sum of exact heat-equation modes.

At time zero, all exponentials equal one, and the sum reconstructs the original parabola. At later times, the highest modes are suppressed much faster. Eventually the first sine mode dominates the shape, even though its amplitude also tends toward zero. This is what we mean by the slowest decaying mode. It is slow only relative to the other nonconstant modes; its temperature still vanishes in the long run under zero Dirichlet conditions.

The formula is not just a mnemonic. Each term satisfies the PDE and both boundaries. For positive time, the exponential factors make the differentiated series converge very well for this smooth initial profile. We may therefore differentiate it term by term and verify the PDE. The initial limit is supported by Fourier convergence, rather than by pretending that an arbitrary infinite sum can always be differentiated without justification.

## A two-mode calculation you can do in your head

For an even simpler initial profile, let the initial temperature be sine of pi x plus point four times sine of three pi x. This is allowed to be negative in places because we can regard u as temperature relative to a reference level rather than absolute temperature.

After time t, the first amplitude becomes exponential of negative kappa pi squared t. The third becomes point four times exponential of negative nine kappa pi squared t. Divide the third amplitude by the first. The ratio is point four times exponential of negative eight kappa pi squared t. It shrinks exponentially. The broad first mode outlasts the finer third mode.

Suppose we choose a time at which kappa pi squared t equals one. The first amplitude is about point three six eight. The third is point four times exponential of negative nine, less than one ten-thousandth. At that time the profile is visually almost a pure first sine wave, even though the initial condition contained a sizable third harmonic. You do not need to solve a new PDE to see the change; the eigenvalues tell you how the two components compete.

A common error is to treat the time factor as the same for all Fourier coefficients. That would preserve the initial shape while merely scaling it, and it would not represent diffusion of a general profile. The n squared in the decay rate is essential. Another error is to choose the sine basis without checking the boundary conditions. Sines fit zero temperatures at both endpoints, not every possible physical setup.

## Insulated ends preserve a different quantity

Let us change the experiment. Insulate both endpoints so the spatial derivative of u is zero at zero and one. Integrate the heat equation over the rod. The time derivative of the integral of u equals kappa times the derivative of u at the right endpoint minus the derivative at the left. Both vanish. Therefore the integral of temperature over the interval stays constant. In this model that is conservation of total thermal energy up to a fixed heat-capacity factor.

The appropriate spatial eigenfunctions are now cosines, including the constant mode. The constant has eigenvalue zero, so its time amplitude does not decay. Every nonconstant cosine mode has a positive eigenvalue and decays exponentially. The solution therefore approaches the initial average, not zero, if the rod is insulated and has no heat source.

For example, start at temperature two plus cosine of pi x. This profile has derivative zero at both ends. Its average is two. The solution at time t is two plus exponential of negative kappa pi squared t times cosine of pi x. The spatial variation vanishes; the average persists.

This is the time-dependent counterpart of the steady Neumann problem. The source-free equation cannot determine or change an arbitrary additive constant under insulation. If a heat source is present, the average temperature changes according to the total input. It is essential to distinguish an isolated system with no source from a heated insulated system: the latter does not have to approach a constant equilibrium.

## Energy gives a check independent of the series

There is another way to show that diffusion dissipates variation. Multiply the heat equation by u, integrate over the interval, and integrate the second derivative term by parts. For fixed zero temperatures at both ends, the boundary term vanishes. One half the time derivative of the integral of u squared equals negative kappa times the integral of the spatial derivative squared.

This identity says the squared size of the temperature profile cannot increase. The right-hand side is never positive. It becomes zero only when the spatial derivative vanishes everywhere. Under zero Dirichlet boundary conditions, a constant temperature compatible with both ends must be zero. Under insulated conditions, any constant is permitted, and the same energy identity explains why the solution can settle to its mean.

The identity gives more than monotonicity. On the unit interval with zero endpoint values, a basic sine-series inequality says the integral of the spatial derivative squared is at least pi squared times the integral of u squared. Combined with the energy calculation, this gives a quantitative upper bound: the squared temperature norm decays at least as fast as an exponential with exponent negative two kappa pi squared t. The first eigenvalue controls the slowest possible decay of a nonzero spatial profile.

This argument checks the same rate that appeared in the explicit Fourier solution. The series is a constructive method; the energy inequality is a structural estimate. Agreement between them increases our confidence that the signs and rates are right.

## When the boundary temperatures are not zero

Real reservoirs are not obliged to have zero relative temperature. Suppose the left end is held at one and the right at three. The steady state with no source is the straight line one plus two x. To solve an evolving problem with these boundary values, subtract that steady line. The remainder has zero values at both endpoints and obeys the same heat equation, because the steady line has zero second derivative and no time dependence.

We can then expand the remainder in the sine eigenfunctions and let each coefficient decay. As time advances, the remainder disappears and the temperature approaches the straight line between the reservoirs. If we had tried to expand the full temperature using only zero-endpoint sine functions, we would have violated the prescribed boundary values immediately. The boundary lift must come before the series.

For an internal source, the steady state may be curved instead of straight. We first solve the stationary boundary-value equation and then subtract that solution. As long as the source and boundary data are time independent, the leftover transient solves a homogeneous equation. This simple decomposition—steady profile plus decaying transient—is one of the most reusable ideas in linear differential equations.

Heat evolution has brought several earlier foundations together: conservation laws, second-order boundary problems, eigenvalues, Fourier coefficients, and exponential ODE solutions. Each supplies one piece of the result. The physical boundary decides the modes; the initial condition decides how much of each mode is present; the heat equation decides how fast each decays. That is the complete mechanism behind the elementary Fourier solution of the heat equation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: derivation, modes and estimates

### Conservation and heat diffusivity

With density \(\rho\), specific heat \(c_p\), conductivity \(k\) and volumetric source \(Q\), Fourier's law and energy balance yield
\[
q=-k u_x,\qquad \rho c_p u_t=-q_x+Q=(k u_x)_x+Q.
\]
For constant coefficients and \(Q=0\), \(u_t=\kappa u_{xx}\), \(\kappa=k/(\rho c_p)>0\), with units length squared per time.

### Separation with zero Dirichlet data

On \((0,L)\), \(u(0,t)=u(L,t)=0\), seek \(u(x,t)=X(x)T(t)\). Then
\[
-X''=\lambda X,\qquad T'=-\kappa\lambda T,\qquad
\lambda_n=(n\pi/L)^2,
\]
\[
u(x,t)=\sum_{n=1}^\infty b_n\sin\left(\frac{n\pi x}{L}\right)
 e^{-\kappa(n\pi/L)^2t},\qquad
b_n=\frac2L\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)dx.
\]
For \(L=1\), \(f(x)=x(1-x)\), two integrations by parts give
\[
b_n=\frac{4(1-(-1)^n)}{n^3\pi^3}
=\begin{cases}8/(n^3\pi^3),& n\text{ odd},\\0,&n\text{ even}.\end{cases}
\]
At \(t=0\), the series equals \(f\) in \(L^2\) and pointwise for this continuous piecewise-smooth extension. For \(t>0\), the exponential factors justify termwise differentiation.

### Energy identity and decay

For homogeneous Dirichlet data,
\[
\frac12\frac d{dt}\int_0^L u^2dx
=\kappa\int_0^L uu_{xx}dx
=-\kappa\int_0^L u_x^2dx.
\]
The Dirichlet Poincaré inequality \(\int_0^L u_x^2\ge(\pi/L)^2\int_0^L u^2\) gives
\[
\|u(t)\|_{L^2}\le e^{-\kappa(\pi/L)^2t}\|u(0)\|_{L^2}.
\]
For Neumann data \(u_x(0,t)=u_x(L,t)=0\), the mean \(\bar u(t)=L^{-1}\int_0^L u\,dx\) is constant, and the same argument applies to \(u-\bar u\) with the first nonzero Neumann eigenvalue \((\pi/L)^2\).

### Exercises with answers

1. Solve \(u_t=2u_{xx}\) on \((0,1)\), zero endpoint values, \(u(x,0)=\sin(2\pi x)\). **Answer:** \(u=e^{-8\pi^2t}\sin(2\pi x)\).
2. What remains from the initial profile \(u(x,0)=3+2\cos(2\pi x)\) with insulated endpoints? **Answer:** \(u=3+2e^{-4\kappa\pi^2t}\cos(2\pi x)\), so the long-time mean is \(3\).
3. Find the steady state with boundary values one and three, and no source. **Answer:** \(u_*(x)=1+2x\).
4. For \(u(x,0)=\sin(\pi x)+0.4\sin(3\pi x)\), find the ratio of third-mode amplitude to first-mode amplitude at time \(t\). **Answer:** \(0.4e^{-8\kappa\pi^2t}\).
5. Why cannot a constant nonzero temperature satisfy homogeneous Dirichlet values at both ends? **Answer:** it would have to equal zero at those endpoints; the only compatible constant is zero.

### Sources and further reading

- [William F. Trench, *The Heat Equation*](https://math.libretexts.org/Bookshelves/Differential_Equations/Elementary_Differential_Equations_with_Boundary_Value_Problems_%28Trench%29/12%3A_Fourier_Solutions_of_Partial_Differential_Equations/12.01%3A_The_Heat_Equation).
- [Jiří Lebl, *PDEs, separation of variables, and the heat equation*](https://math.libretexts.org/Courses/East_Tennesee_State_University/Book%253A_Differential_Equations_for_Engineers_%28Lebl%29_Cintron_Copy/4%253A_Fourier_series_and_PDEs/4.6%253A_PDEs%252C_separation_of_variables%252C_and_the_heat_equation).
- [MIT OpenCourseWare, ES.1803 Topic Notes, Topic 25](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/pages/topic-notes/).
