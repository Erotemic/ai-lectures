# PDE evolution: transport, diffusion, waves, and energy

<!-- BEGIN SPOKEN LECTURE -->

# PDE evolution: transport, diffusion, waves, and energy

## Transport, diffusion, weak energy, and pattern onset

### Transport and Diffusion: Two Ways a Field Evolves

An ordinary differential equation describes the evolution of finitely many quantities, perhaps the position of a mass or the amount of a chemical species. But temperature and concentration are fields: their values depend on position as well as time. To describe how an entire field evolves, derivatives in both space and time become part of the equation. These are partial differential equations.

Two basic mechanisms appear almost everywhere: transport and diffusion. Transport moves a pattern from one place to another. Diffusion spreads a pattern, smoothing sharp variations. Their equations look similar at first glance, but the behavior they predict is fundamentally different.

#### Transport carries profiles

Consider a scalar field u depending on position x and time t. Suppose the field is carried along the line at constant speed c without changing shape. If the initial profile is a bump, after time t the bump has moved a distance c times t.

The exact expression says: to find u at x and t, look at the initial profile at x minus c times t. Differentiate this expression. The time derivative is negative c times the derivative of the initial profile, and the spatial derivative is that same profile derivative. Consequently u satisfies an equation that says the time derivative plus c times the spatial derivative equals zero.

This is the linear transport equation. Its solutions are constant along characteristic lines that move at speed c. A disturbance has a definite propagation direction. On the whole line, an initial bump simply translates. It does not become broader or shorter by the transport law alone.

If we work on a bounded interval, boundary conditions matter. For positive c, information flows into the interval through the left boundary, so prescribing data there is natural. Imposing arbitrary conditions independently at both ends would generally overdetermine the first-order transport problem. The direction of information flow is part of the mathematics.

#### Diffusion follows gradients

Now imagine a concentration field where material moves from regions of high concentration toward regions of low concentration. In a simple homogeneous model, the flux is proportional to the negative spatial gradient of the concentration. This is Fick's law. A positive gradient sends flux toward the negative x direction, and a negative gradient sends flux toward positive x.

Conservation says the rate of change in a short interval equals the net flux entering it. In differential form, the time derivative of concentration is minus the spatial derivative of flux. Substitute the gradient law, assume the diffusivity D is constant, and obtain the heat equation: the time derivative equals D times the second spatial derivative.

The second derivative measures local curvature. At a sharp local maximum, curvature is negative, and diffusion tends to lower the peak. At a local minimum, curvature is positive, and diffusion tends to raise the trough. Over time, a rough initial profile becomes smoother.

#### Understand smoothing one Fourier mode at a time

A sine wave is a useful test. Suppose u is initially a sine wave of spatial frequency k, and we look for a solution with the same spatial shape but a changing amplitude. Taking two spatial derivatives of that sine wave produces negative k squared times the original sine wave. The heat equation therefore tells us the amplitude decays exponentially at rate D times k squared.

Higher frequencies have larger k squared, so their amplitudes decay more rapidly. Very short-wavelength oscillations disappear faster than long-wavelength ones. This is the mathematical source of the familiar smoothing action of diffusion.

Compare transport. A sinusoidal wave under constant-speed transport has its phase shifted, but its amplitude remains the same. Transport changes position; diffusion changes the amplitudes of spatial modes. The distinction becomes central when both mechanisms appear together, as in advection-diffusion equations for heat or chemical species moving through a flow.

#### Boundary conditions change the answer

On a finite rod of length L, suppose the ends are held at zero temperature relative to a reference level. Those are Dirichlet boundary conditions. Sine waves that vanish at both endpoints fit the boundary. Their spatial frequencies are integer multiples of pi divided by L. Each mode decays at a rate proportional to the square of its mode number.

If instead the ends are insulated, the heat flux at each boundary is zero. Since flux is minus D times the gradient, this means the spatial derivative vanishes at the endpoints. These are Neumann boundary conditions. In that setting the spatially constant mode does not decay: total heat is conserved because nothing escapes through either endpoint.

Both are heat equations, but they describe different physical systems. An initial condition alone does not generally determine the evolution on a bounded domain without appropriate boundary conditions. Which conditions are appropriate depends on what the surroundings do to the field.

#### Energy provides a uniqueness argument

There is a useful proof that the heat equation is stable in a broad sense. Work on a finite interval with homogeneous zero-temperature boundary conditions. Multiply the heat equation by u and integrate over the interval. The time derivative of half the integral of u squared equals D times the integral of u times its second derivative.

Integrate by parts. The boundary term vanishes because u is zero at the ends. The remainder is minus D times the integral of the square of the spatial derivative. This quantity cannot be positive. Therefore the squared-size, or energy, of the temperature profile cannot increase.

Apply the same argument to the difference between any two solutions with the same initial and boundary data. That difference has zero initial energy and cannot gain energy, so it remains zero. This proves uniqueness within the regularity class in which the calculation is valid. Similar energy methods extend to weaker notions of solution with careful functional-analytic definitions.

Transport has a different conservation property. With periodic boundaries, constant-speed transport preserves the integral of u squared rather than dissipating it. Its profiles travel; diffusion loses spatial variation.

#### A warning about numerical time steps

Diffusion is especially demanding for explicit numerical solvers. On a uniform spatial grid, approximate the second derivative by comparing each value with its two neighbors. If the time step is too large relative to the square of the spatial spacing, the explicit update can become unstable. In one dimension, a standard forward-Euler centered-difference scheme is stable in its usual maximum-principle sense when the dimensionless ratio D times the time step divided by the spacing squared does not exceed one half.

Refine the spatial grid by a factor of two, and the stable explicit time step becomes at most one quarter as large. This resembles stiffness: very fast decay of high spatial frequencies creates stringent numerical restrictions even when the visible temperature profile changes slowly. Implicit methods can relax the restriction, though their accuracy still needs attention.

#### Two models, two kinds of information

For transport, a solution follows characteristics and preserves the profile along them. For diffusion, the solution smooths and dissipates variations; its mathematical model can spread an initially localized effect beyond any fixed distance at every positive time. That last feature is a property of the ideal heat equation, not a claim that physical thermal signals transmit infinitely fast at arbitrary microscopic scales. The diffusion equation is a continuum approximation with a domain of validity.

These equations establish two basic modes of PDE thinking. We can track information along paths, or we can understand how gradients and curvature reorganize a field. Their analysis combines differential equations, conservation laws, boundary conditions, and numerical stability. From here we can study waves, nonlinear conservation laws, weak solutions, and the geometries of higher-dimensional fields.

### Boundary Value Problems, Weak Solutions, and Energy Estimates

A differential equation is often introduced as a pointwise requirement: differentiate a function, substitute into an equation, and check that the identity holds at every point. For ordinary smooth functions this is natural. But physical materials have corners, coefficients may jump across an interface, and approximate numerical solutions may only be piecewise differentiable. A theory restricted to perfectly smooth functions would discard many of the problems we most want to solve.

Weak solutions provide a disciplined alternative. Instead of demanding every derivative pointwise, we ask the equation to hold after integration against a family of test functions. Integration by parts moves derivatives from the unknown solution onto better-behaved terms. The resulting formulation is weaker in its regularity requirements, but stronger as a framework for existence, stability, and computation.

#### A rod fixed at both ends

Consider a one-dimensional rod occupying the interval from zero to one. Suppose its equilibrium temperature or displacement is governed by the equation that the negative second derivative of u equals a given source function f. At both ends we prescribe zero displacement or temperature relative to a reference: u of zero and u of one are zero.

If u is twice differentiable, we can solve this boundary value problem directly in some simple cases. Take f equal to one. Then the second derivative of u is negative one. Integrating twice and enforcing the boundary conditions gives u of x equals one half times x times one minus x. That is a smooth solution, and it arches upward between two fixed endpoints.

But look at how the equation behaves under integration. Multiply both sides by a smooth test function v that vanishes at the endpoints, and integrate across the interval. Integrating the second derivative term by parts removes one derivative from u. The boundary terms vanish because v is zero at both ends. We obtain the identity: the integral of u prime times v prime equals the integral of f times v.

That identity can make sense even when u has only a square-integrable first weak derivative, so long as the integrals exist. We can use it as the definition of a weak solution.

#### What a weak derivative is

A function u has a weak derivative g if integrating u against the derivative of any smooth compactly supported test function gives minus the integral of g against that test function. For a smooth u, integration by parts proves that g is the ordinary derivative. But the definition extends to functions with corners.

Consider the absolute-value function on an interval around zero. Its classical derivative fails to exist at zero. Yet it has a weak derivative equal to negative one on the negative side and positive one on the positive side. The condition is equality inside every test-function integral; the value assigned at the single point zero is irrelevant in the usual almost-everywhere sense.

Sobolev spaces package this idea. The space H one consists of square-integrable functions whose first weak derivatives are square-integrable. H naught one consists, roughly speaking, of H one functions with zero boundary trace. On a suitably regular bounded domain, this trace is a well-defined extension of the classical notion of vanishing at the boundary.

Weak does not mean approximate or inaccurate. It refers to the sense in which differentiation and equality are interpreted.

#### An energy appears automatically

For the negative second-derivative equation, define the energy of a candidate u as one half of the integral of the square of u prime, minus the integral of f times u. Its first variation in a direction v is the integral of u prime times v prime minus the integral of f times v. Setting this variation to zero for every admissible v gives exactly the weak equation.

Thus the solution can be characterized as a minimizer of an energy. This is useful because minimization can be well posed under conditions where the original pointwise equation is not obviously meaningful.

There is a key inequality lurking here. If u vanishes at both endpoints, the size of u can be controlled by the size of its derivative. This is a Poincaré inequality. Intuitively, a function pinned to zero cannot become very large without having substantial variation somewhere. The inequality makes the derivative-based energy coercive: it controls the whole H one norm of u within the zero-boundary space.

Coercivity is the condition that prevents approximate minimizers from escaping to infinity while maintaining low energy. In the linear setting, it is also what allows Lax–Milgram theory to turn a bounded forcing functional into a unique weak solution.

#### The existence and uniqueness argument

On a bounded Lipschitz domain, consider the equation negative Laplacian of u equals f, with u equal to zero on the boundary. For f square-integrable, the weak problem asks for u in H naught one such that the integral of the gradient of u dotted with the gradient of v equals the integral of f times v, for every v in H naught one.

The bilinear form on the left is continuous. On H naught one it is coercive by Poincaré's inequality. The right-hand side is a continuous linear functional by Cauchy–Schwarz and Poincaré. The Lax–Milgram theorem then yields existence and uniqueness of the weak solution.

Uniqueness is easy to glimpse directly. If u and w are both solutions, their difference z satisfies the homogeneous weak equation. Take v equal to z. The integral of the squared gradient of z must be zero. So its gradient is zero almost everywhere. A function with zero gradient is constant on each connected component, and the zero boundary condition forces those constants to zero. Therefore u equals w.

This is an energy argument: test a difference equation with the difference itself and use a nonnegative integral to eliminate every possibility except zero.

#### Why boundary conditions change the problem

If instead we prescribe the normal derivative at the boundary, the Neumann problem, constants may be added to any solution without changing its gradient. Then uniqueness fails unless we choose a normalization such as zero average. There is also a compatibility condition between the source and the boundary flux. The equations cannot determine an absolute potential from derivative data alone.

This matters in physics. Fixing a temperature at the boundary and prescribing heat flux through the boundary are different experiments. They have different well-posedness conditions, and treating them interchangeably would erase the part of the model that describes how the system interacts with its surroundings.

#### From weak solutions to finite elements

A finite element method chooses a finite-dimensional space of test and trial functions, often piecewise polynomial over a mesh, and asks the weak identity to hold for every function in that finite-dimensional space. The result is a system of algebraic equations. Its stiffness matrix records integrals of gradients of basis functions, and its right-hand side records the source's action on those basis functions.

The same energy structure guides convergence analysis. The exact solution satisfies the weak equation for all admissible test functions; the discrete solution satisfies it for the chosen finite-dimensional subspace. Subtracting the two identities gives Galerkin orthogonality, a foundation for error estimates. There are still approximation and regularity hypotheses to check; simply assembling a linear system does not guarantee that it converges at a claimed rate.

Weak formulations do not abandon the differential equation. They preserve its essential balance laws in a form robust under limits and approximation. A classical solution, when smooth enough, is also a weak solution. Conversely, extra regularity theorems can show when a weak solution recovers classical derivatives. The gain is a stable bridge between physical models, functional analysis, and algorithms that operate on finite meshes.

## Wave Equations, Characteristics, and Finite Propagation Speed

If you pluck a stretched string, the disturbance travels outward. You can watch the pulse move before distant points respond. That behavior differs from the ideal heat equation, where a localized temperature change influences the mathematical solution everywhere immediately, even though the distant influence may be extremely small.

The wave equation captures a mechanism with finite propagation speed. It belongs to the hyperbolic family of partial differential equations. We can derive its one-dimensional solution, identify its characteristic lines, and use an energy law to explain why the behavior is stable under the right assumptions.

### Where the wave equation comes from

Imagine a thin string held under approximately constant tension and undergoing small transverse displacements. A small piece of string has mass, and the vertical components of tension at its two ends need not balance. Newton's law equates that net transverse force with the mass times acceleration.

For small slopes, the tension contribution is proportional to the difference in slopes across the segment. Dividing by its length and passing to a limit gives an equation where the second derivative in time is a positive constant times the second derivative in position. Write that constant as c squared. Then the wave equation says the acceleration of the displacement equals c squared times its spatial curvature.

The speed c depends on tension and mass per unit length in this simplified string model. Higher tension increases speed; greater mass density reduces it. The derivation also tells us the model's boundaries: large slopes, varying tension, damping, nonlinear material behavior, and bending stiffness can require different equations.

### What must be specified initially?

A second-order time equation requires two pieces of initial data. We must specify the initial displacement f of x, and the initial velocity g of x. These are independent pieces of information. A string can begin straight but already moving, or deformed but momentarily at rest.

The domain also matters. On the whole real line, no endpoint conditions are necessary. On a finite string, boundary conditions at the endpoints affect reflections and standing waves. We will begin with the whole line, where the clearest formula is available.

### Factoring the differential operator

The one-dimensional wave operator can be factored into two first-order operators. One uses the time derivative plus c times the space derivative, and the other uses the time derivative minus c times the space derivative. Because the coefficients are constant, these factors commute, and their product is exactly the wave operator.

This factorization suggests two families of characteristic lines: x minus c times t is constant, and x plus c times t is constant. Along one family information travels to the right; along the other it travels to the left.

If the initial velocity is zero, the solution is particularly simple. Half of the initial displacement travels to the right at speed c, and half travels to the left at speed c. The formula adds f evaluated at x minus c t and f evaluated at x plus c t, then divides by two.

When initial velocity is not zero, there is another term: one divided by twice c, multiplied by the integral of g from x minus c t to x plus c t. Together these terms form d'Alembert's formula. One can verify it by differentiating twice, checking the differential equation, and evaluating the initial displacement and initial time derivative.

### An explicit pulse

Suppose the initial displacement is a smooth localized bump, supported between positions negative one and one, and the initial velocity is zero. At time t the right-moving contribution is supported between c t minus one and c t plus one. The left-moving contribution is supported between negative c t minus one and negative c t plus one.

For sufficiently large time the two pulses no longer overlap. They retain their shapes in the ideal one-dimensional equation, each with half the original amplitude. No point outside the region reached by those traveling supports can respond. The original disturbance has not been smeared instantaneously over the real line.

If the initial velocity is supported in the same interval, its contribution uses an integral over the interval between x minus c t and x plus c t. The full solution is still zero outside the expanding interval from negative one minus c t to one plus c t. The exact geometry of its support inside that interval may differ, but influence cannot outrun speed c.

### Domains of dependence

Ask the question in reverse. What initial information determines the displacement at a given location x and later time t? D'Alembert's formula uses initial displacement only at two points, x minus c t and x plus c t, and initial velocity across the interval joining them. Everything outside that interval is irrelevant to the answer at this point and time.

That interval is the domain of dependence on the initial line. In a space-time diagram, it is the base of a cone bounded by the two characteristics through the observation point. Changes in initial data outside the cone cannot affect that observation in the ideal model.

The word cone remains in higher-dimensional wave equations, where the domain of dependence lies inside a light-cone-like region. The exact shape of the solution inside the region depends on dimension and boundary conditions. Finite propagation speed does not automatically imply a perfectly sharp disturbance located only at the wavefront.

### An energy identity

Wave motion also has a conserved energy. For the whole-line equation with sufficiently regular, decaying data, define the total energy as one-half the integral of velocity squared plus c squared times slope squared. These terms represent kinetic and elastic energy after appropriate normalization.

Differentiate in time. Replace the second time derivative using the wave equation. Integrate the term involving the second spatial derivative by parts. The two interior terms cancel, leaving only a flux contribution at the boundaries. On the whole line, for suitably decaying data, the boundary flux vanishes. Total energy is constant.

This energy law gives more than physical interpretation. It provides an a priori estimate and a uniqueness argument. If two solutions share identical initial data, their difference solves the wave equation with zero initial displacement and zero initial velocity. Its energy remains zero. With the appropriate regularity and normalization, that forces the difference to vanish.

On a bounded interval the boundary flux need not vanish automatically. A fixed-end or reflecting boundary condition can yield energy conservation, while a driven endpoint can inject energy. Damping adds a negative contribution and makes the energy decrease. The equation and the boundary conditions together determine the energy balance.

### Contrast with diffusion

The heat equation is first-order in time and diffuses spatial gradients. Its fundamental solution for positive time has Gaussian tails extending over all space. A compactly supported nonnegative initial temperature distribution that is not identically zero produces a positive temperature everywhere for every positive time on the whole line. The wave equation instead has characteristics and finite propagation.

These are ideal mathematical properties, not claims that actual physical heat signals transmit measurable information instantaneously. Both PDEs arise as approximations under different assumptions. Their contrasting mathematical domains of dependence tell us which questions each model is suited to answer.

Today's result is a complete prototype: a physical balance law leads to a hyperbolic PDE; characteristics lead to an exact solution; the formula identifies a finite domain of dependence; and the energy identity explains stability and uniqueness. These tools will reappear in multidimensional waves, variable-coefficient equations, and numerical hyperbolic solvers.

## Nonlinear PDE Stability and Energy Estimates

A reaction can amplify a disturbance while diffusion tries to smooth it. Which effect wins? The answer depends not only on the reaction law but also on the size of the domain and the boundary conditions. Energy estimates let us make that competition precise without solving the nonlinear partial differential equation explicitly.

Imagine a chemical concentration in a one-dimensional container. Its evolution has two parts. Diffusion, represented by a second spatial derivative, spreads concentration from high regions to low regions. A reaction function changes concentration locally, possibly increasing or decreasing it depending on the current value.

We would like to know whether two solutions that begin close together remain close, or even approach each other. Instead of finding each solution, subtract them. Call their difference w. It obeys a diffusion equation driven by the difference of the two reaction terms.

Now measure the squared size of w by integrating its square across the container. This is an energy, though not necessarily a physical thermodynamic energy. Differentiate it with respect to time. The diffusion term becomes negative after integration by parts, provided the boundary terms vanish. It is the negative of the integral of the squared spatial derivative of w.

### The key competition

Suppose the reaction term obeys a one-sided Lipschitz inequality. This says the product of the difference in reaction rates with the difference in states is bounded above by a constant L times the squared state difference. It does not require the reaction to be globally contractive. It tells us the maximum rate at which reaction can increase the squared distance between solutions.

The energy inequality now has one favorable term, from diffusion, and one potentially unfavorable term, from the reaction. We need a way to compare the spatial derivative energy to the ordinary energy of w.

On an interval of length ell with zero values prescribed at both endpoints, the Poincaré inequality does exactly that. It says the squared spatial derivative has integral at least pi squared divided by ell squared times the integral of w squared. In other words, a nonzero function pinned to zero at both ends must vary by a minimum amount.

If diffusion has coefficient D, the resulting contraction rate is at least D times pi squared divided by ell squared, minus the reaction's one-sided Lipschitz constant. When that expression is positive, the distance between the solutions decays exponentially.

This is a stability theorem derived entirely from inequalities. No closed-form solution of the nonlinear equation was required.

### An explicit nonlinear reaction

Consider the reaction f of u equal to u minus u cubed. Near zero, the linear term tries to amplify small disturbances. The negative cubic term restrains large positive or negative values. For any two real values a and b, the difference quotient of this reaction is one minus the sum of a squared, a times b, and b squared. The quadratic expression being subtracted is nonnegative, so the quotient is at most one.

Thus the reaction has one-sided Lipschitz constant one. With diffusion coefficient one, the energy estimate proves contraction between any two sufficiently regular solutions satisfying homogeneous Dirichlet boundary conditions if the interval is shorter than pi.

At the other end of the comparison, look at the zero equilibrium and linearize. The first spatial sine mode has growth rate one minus pi squared divided by ell squared. If the interval is longer than pi, this mode grows initially. The zero equilibrium is linearly unstable. The domain's size has changed which force dominates.

At the critical length pi, the linear rate is zero and this simple linear test is inconclusive. The cubic nonlinearity and higher-order analysis decide what happens. Treating the equality case as an automatic instability or stability result would go beyond the estimate.

### Boundary conditions matter

Why did the size of the interval enter? Because the fixed-zero boundary prevents constant nonzero differences. If we instead impose no-flux, or Neumann, boundary conditions, constant differences have zero spatial derivative. The Poincaré inequality with a strictly positive first eigenvalue no longer applies to arbitrary functions; we must separate out the spatial mean or impose another constraint.

The nonlinear equation has not changed, but the relevant function space has. That is why a stability statement that omits its boundary assumptions is incomplete.

### A priori bounds and actual solutions

An energy inequality is a powerful tool, but it must be used in the right order. First we need a solution in a class for which the manipulations are valid, or an approximation argument that justifies them. Then the inequality controls its size and helps establish uniqueness and continuous dependence. With suitable local-existence theory and a priori bounds, it may also contribute to proving global existence.

The estimate alone does not grant global existence for every nonlinear reaction. Some semilinear equations admit solutions that blow up in finite time. And an L-two bound need not automatically control every stronger norm that a nonlinear term requires.

The major idea is nevertheless general. Choose an energy adapted to the equation, differentiate it, use integration by parts, exploit coercivity or a spectral gap, and apply a differential inequality such as Grönwall's lemma. The result can explain why solutions converge or why disturbances grow, even when their exact shapes remain inaccessible.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Transport, diffusion, weak energy, and pattern onset

### Transport, diffusion, weak energy, and pattern onset

#### Companions, sources, and study material (not spoken)

##### Transport and Diffusion: Two Ways a Field Evolves

**Track:** Differential Equations and Dynamical Systems. **Background:** derivatives in space and time, conservation laws, and Fourier modes. **Central question:** why does advection preserve shapes while diffusion smooths them out?

###### Mathematical companion (not spoken)

**Transport.** On \(\mathbb R\), for sufficiently regular \(u_0\),
\[
u_t+c u_x=0,\quad u(x,0)=u_0(x)
\quad\Longrightarrow\quad u(x,t)=u_0(x-ct).
\]
Characteristics obey \(x(t)=x_0+ct\); \(u\) is constant along each characteristic.

**Diffusion.** Conservation \(u_t+F_x=0\) and Fick's law \(F=-D u_x\), for constant \(D>0\), give
\[
u_t=D u_{xx}.
\]
Fourier mode \(e^{ikx}\) decays as \(e^{-Dk^2t}e^{ikx}\). On \([0,L]\) with \(u(0,t)=u(L,t)=0\), separated solutions are \(\sin(n\pi x/L)e^{-D(n\pi/L)^2 t}\), \(n\ge1\).

**Energy identity** under homogeneous Dirichlet boundaries:
\[
\frac{d}{dt}\frac12\int_0^L u^2\,dx
=D\int_0^L u u_{xx}\,dx=-D\int_0^L (u_x)^2\,dx\le0.
\]
For two solutions with identical data, apply this to their difference to prove uniqueness for sufficiently regular solutions. For zero-flux Neumann conditions, \(\frac{d}{dt}\int_0^L u\,dx=D[u_x]_0^L=0\).

**Explicit finite differences.** For \(r=D\Delta t/(\Delta x)^2\),
\[
u_j^{n+1}=(1-2r)u_j^n+r u_{j-1}^n+r u_{j+1}^n.
\]
When \(0\le r\le1/2\), the update is a convex combination, ensuring a discrete maximum principle. This is the standard 1-D explicit diffusion restriction, not a universal CFL condition for every PDE discretization.

##### Exercises with answers

1. Where is an initial peak \(u_0(x)=e^{-x^2}\) centered after time \(t\) under \(u_t+3u_x=0\)? **Answer:** at \(x=3t\).
2. Which diffusion Fourier mode decays faster: frequency one or frequency four? **Answer:** frequency four, with decay rate sixteen times as large.
3. With no-flux boundaries, is total mass conserved? **Yes:** the net boundary flux is zero.
4. If \(\Delta x\) halves, what happens to the forward-Euler diffusion stability limit on \(\Delta t\)? **Answer:** it decreases by a factor of four.

##### Reading and source notes

- MIT OCW [Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/), heat equation, separation of variables, Fourier series, and characteristics.
- University of Illinois [Stiff ODEs](https://heath.cs.illinois.edu/iem/ode/stiff/), numerical stability motivation.

##### Boundary Value Problems, Weak Solutions, and Energy Estimates

**Track:** Differential Equations and Dynamical Systems. **Background:** differentiation, integration by parts, linear algebra, introductory PDEs. **Central question:** what does it mean to solve a differential equation when a classical derivative may not exist everywhere?

###### Mathematical companion (not spoken)

For \(\Omega\subset\mathbb R^n\) bounded Lipschitz, \(f\in L^2(\Omega)\), the homogeneous Dirichlet problem \(-\Delta u=f\) has the weak formulation:
\[
\text{Find }u\in H_0^1(\Omega)\text{ such that }
\int_\Omega \nabla u\cdot\nabla v\,dx=\int_\Omega fv\,dx
\quad\forall v\in H_0^1(\Omega).
\]
The bilinear form \(a(u,v)=\int\nabla u\cdot\nabla v\) is bounded and coercive on \(H_0^1\) by Poincaré. Lax–Milgram ensures a unique weak solution. Testing with \(v=u\) and applying Poincaré gives an energy bound \(\|\nabla u\|_{L^2}\le C_\Omega\|f\|_{L^2}\) (with a domain-dependent constant).

For \(\Omega=(0,1)\), \(f=1\), the classical and weak solution is \(u(x)=x(1-x)/2\); \(-u''=1\) and \(u(0)=u(1)=0\). It also uniquely minimizes
\[
J(w)=\frac12\int_0^1|w'(x)|^2dx-\int_0^1 w(x)dx
\quad(w\in H_0^1(0,1)).
\]
For a conforming finite-element subspace \(V_h\subset H_0^1\), Galerkin orthogonality states \(a(u-u_h,v_h)=0\) for all \(v_h\in V_h\). Error estimates additionally require approximation properties, and regularity for specific rates.

##### Exercises with answers

1. Verify the stated one-dimensional solution. **Answer:** \(u''=-1\), and both boundary values vanish.
2. What is the weak derivative of \(|x|\) on \((-1,1)\)? **Answer:** \(-1\) for \(x<0\), \(+1\) for \(x>0\), almost everywhere.
3. Why does the homogeneous Dirichlet problem not allow a free additive constant? **Answer:** nonzero constants violate the zero boundary trace.
4. Why are Neumann solutions generally determined only up to constants? **Answer:** the PDE and normal derivatives are unchanged under adding a constant; a normalization and compatibility condition are needed.

##### Reading and source notes

- Lawrence C. Evans, *Partial Differential Equations*, 2nd edition, chapters on Sobolev spaces and weak elliptic solutions (American Mathematical Society).
- University of Toronto, [Partial Differential Equations II course outline](https://www.math.toronto.edu/roberth/pde2.html), Sobolev spaces, weak solutions, and energy estimates.

### Wave Equations, Characteristics, and Finite Propagation Speed

**Track:** Differential Equations and Dynamical Systems. **Background:** PDEs, second derivatives, initial-value problems, energy conservation. **Central question:** why do disturbances in a wave equation travel at finite speed, and what initial data determine a later observation?

#### Mathematical companion (not spoken)

On \(\mathbb R\times[0,\infty)\), with \(c>0\), solve
\[u_{tt}=c^2u_{xx},\qquad u(x,0)=f(x),\quad u_t(x,0)=g(x).\]
For \(f\in C^2\) and \(g\in C^1\) with appropriate regularity for the differentiations, d'Alembert's formula is
\[u(x,t)=\frac{f(x-ct)+f(x+ct)}2+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.\]
The operator factors as \((\partial_t-c\partial_x)(\partial_t+c\partial_x)u=0\). The value \(u(x,t)\) depends only on \(f\) at the characteristic endpoints and \(g\) over \([x-ct,x+ct]\). If \(f,g\) vanish outside \([a,b]\), then \(u(\cdot,t)\) vanishes outside \([a-ct,b+ct]\).

For smooth decaying solutions,
\[E(t)=\frac12\int_{\mathbb R}(u_t^2+c^2u_x^2)\,dx,\quad
\partial_t\Bigl(\tfrac12(u_t^2+c^2u_x^2)\Bigr)=c^2\partial_x(u_tu_x),\quad E'(t)=0.\]
On a bounded interval \([a,b]\), \(E'(t)=c^2[u_tu_x]_{a}^{b}\); boundary conditions determine whether the flux vanishes. A zero-energy difference of solutions has \(u_t=u_x=0\), and its initial value zero fixes the additive constant, establishing uniqueness.

##### Exercises with answers

1. For \(g=0\) and \(f(x)=e^{-x^2}\), write \(u(x,t)\). **Answer:** \(\tfrac12[e^{-(x-ct)^2}+e^{-(x+ct)^2}]\).
2. At \((x,t)\), which part of the initial velocity can affect the solution? **Answer:** only \(g\) on \([x-ct,x+ct]\).
3. If \(f,g\) are compactly supported, can their influence appear outside the expanding interval at time \(t\)? **No:** d'Alembert's formula makes that impossible.
4. Does the energy identity guarantee conservation for arbitrary driven endpoints? **No:** boundary flux can inject or remove energy.

##### Reading and source notes

- MIT OpenCourseWare, [18.303 Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/), wave and diffusion equations.
- A. K. Nandakumaran and P. S. Datti, [*One-Dimensional Wave Equation*](https://www.cambridge.org/core/books/abs/notes-problems-and-solutions-in-differential-equations/onedimensional-wave-equation/CCE77FB5DEDBFF85449B7290F61C5A2A), d'Alembert formula and domain of dependence.
- Lawrence C. Evans, *Partial Differential Equations*, second edition (AMS, 2010), energy estimates and hyperbolic PDEs.

### Nonlinear PDE Stability and Energy Estimates

**Track:** Differential Equations and Dynamical Systems. **Background:** diffusion, weak solutions, eigenfunctions, Grönwall inequalities, stability of equilibria. **Central question:** when can diffusion overcome nonlinear amplification?

#### Mathematical companion (not spoken)

For regular solutions to \(u_t=D u_{xx}+f(u)\) on \((0,\ell)\) with homogeneous Dirichlet data and \(D>0\), consider two solutions u,v existing on the interval of time being studied. Let w=u-v. Assume
\[(f(a)-f(b))(a-b)\le L_f(a-b)^2\quad\text{for all }a,b\in\mathbf R.\]
Then by integration by parts, Poincaré's inequality and Grönwall,
\[\frac12\frac d{dt}\|w\|_{L^2}^2=-D\|w_x\|_{L^2}^2+\int_0^\ell w(f(u)-f(v))dx\le -\left(D\frac{\pi^2}{\ell^2}-L_f\right)\|w\|_{L^2}^2,\]
so if \(\mu=D\pi^2/\ell^2-L_f>0\),
\[\|u(t)-v(t)\|_{L^2}\le e^{-\mu t}\|u(0)-v(0)\|_{L^2}.\]
The standard Poincaré inequality here is \(\|w_x\|_2^2\ge(\pi/\ell)^2\|w\|_2^2\) for w in H_0^1(0,ell).

**Allen–Cahn-type example:** \(f(u)=u-u^3\) has \((f(a)-f(b))/(a-b)=1-(a^2+ab+b^2)\le1\) when a≠b, so \(L_f=1\). With D=1, \(\ell<\pi\) gives contraction. Linearizing at u=0 yields eigenvalues \(1-(n\pi/\ell)^2\). For ell>pi the n=1 eigenmode grows linearly; ell=pi is the borderline case requiring nonlinear analysis. The linear instability claim is about the zero equilibrium, not about every solution or equilibrium.

**Caveats:** Neumann conditions permit constant modes, making the zero-boundary Poincaré constant invalid for arbitrary differences. Weak solutions require justified testing by w, typically through approximation or monotone/energy methods. The estimate holds on any time interval where such solutions exist; it does not independently prove global existence.

##### Exercises with answers

1. For D=4 and L_f=1, which interval lengths guarantee contraction? **Answer:** ell<2pi.
2. Why does integration by parts produce no boundary term with homogeneous Dirichlet conditions? **Answer:** w vanishes at both endpoints.
3. For ell=2pi, D=1, f(u)=u-u³, what is the first linearized growth rate? **Answer:** \(1-(\pi/2\pi)^2=3/4>0\).
4. Why can the contraction theorem fail with Neumann boundaries? **Answer:** a constant nonzero w has zero gradient, so diffusion supplies no coercive decay for that mode.

##### Reading and source notes

- [University of Chicago PDE notes](https://www.math.uchicago.edu/~luis/pdenotes.pdf), heat-equation energy methods and boundary dependence.
- [Lawrence C. Evans, Partial Differential Equations, AMS](https://bookstore.ams.org/gsm-19-r), functional analysis and nonlinear PDE estimates.
