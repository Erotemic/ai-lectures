# Reaction-diffusion modes, pattern onset, and traveling fronts

<!-- BEGIN SPOKEN LECTURE -->

# Reaction-diffusion modes, pattern onset, and traveling fronts

## Reaction–Diffusion Systems and Turing Instability

Diffusion usually smooths differences. Put dye in water and its concentration spreads until sharp boundaries fade. One might therefore suppose that adding diffusion to a stable chemical system can only make it more stable. But two reacting species can behave differently: their combined reaction and diffusion can make a uniform equilibrium unstable to some spatial disturbances even when it is stable to disturbances that are uniform everywhere.

Alan Turing analyzed this possibility in his 1952 paper, The Chemical Basis of Morphogenesis. The mathematical mechanism is now called a Turing instability. It provides a model for how spatial structure can arise from locally uniform reaction rules. The mechanism is precise, but deriving a linear instability is not the same as proving that a particular stable biological pattern must emerge.

### Begin with reactions at one point

Let u and v denote the concentrations of two chemical species. Ignore space temporarily. Suppose their rates of change are given by functions f of u and v, and g of u and v. A homogeneous equilibrium is a pair of concentrations u star, v star where both reaction rates are zero.

To study small perturbations, linearize around this equilibrium. The result is a two-by-two Jacobian matrix J. Its entries record how each reaction rate changes when one concentration changes. Call them a and b in the first row, c and d in the second.

For a real two-by-two system, the equilibrium is linearly asymptotically stable if the trace a plus d is negative and the determinant a d minus b c is positive. These inequalities ensure that both eigenvalues have negative real parts. Without spatial effects, small disturbances decay.

### Add spatial diffusion

Now let concentrations vary with position. Suppose u diffuses with coefficient D u and v with coefficient D v, both positive. The equations add D u times the Laplacian of u to the first rate law, and D v times the Laplacian of v to the second.

Diffusion alone damps Fourier modes. A spatial mode with wave number q has a Laplacian contribution of negative q squared. After linearization, the matrix controlling that mode becomes the reaction Jacobian minus q squared times the diagonal matrix of diffusion coefficients.

At q equal to zero this reduces to the original reaction Jacobian. We assumed that this homogeneous mode is stable. At nonzero q, however, the two diagonal entries are shifted by different amounts. If the diffusion coefficients differ sufficiently and the species influence one another in the right way, an eigenvalue can cross into the positive half-plane.

The system becomes stable to uniform disturbances but unstable to disturbances with selected spatial wavelengths. That is the central mathematical surprise.

### Derive the instability test

The trace for wave number q is the original trace minus the sum of diffusion coefficients times q squared. Since the original trace was negative, the new trace stays negative for all nonnegative q squared. Therefore instability cannot arise by making the trace positive in this two-species setting.

The determinant provides the opening. Expand it. The result is the original positive determinant, minus q squared multiplied by a times D v plus d times D u, plus the product D u D v times q to the fourth power.

Think of this as an upward-opening quadratic in q squared. At q zero it is positive. At very large q it is positive again. For it to become negative in between, its minimum must lie at a positive value of q squared and fall below zero. That requires a times D v plus d times D u to be positive, and its square to exceed four times the product of the diffusion coefficients and the determinant of J.

Those inequalities give a clear necessary and, for continuously available positive wave numbers, sufficient linear diffusion-driven instability condition, assuming the original homogeneous equilibrium was linearly stable. On a finite domain, only particular spatial wave numbers are allowed by the geometry and boundary conditions. Even if a continuous band would be unstable, the finite domain may have no admissible mode in that band.

### Work through actual numbers

Take the reaction Jacobian with first row one and negative two, and second row two and negative three. Its trace is negative two, and its determinant is one. So the homogeneous equilibrium is linearly stable.

Let u diffuse with coefficient one and v with coefficient twenty. For a spatial mode with q squared equal to one quarter, the mode matrix has first diagonal entry three quarters and second diagonal entry negative eight. The off-diagonal entries remain negative two and two. Its determinant is negative two. The trace is negative seven and one quarter.

A negative determinant means the two eigenvalues have opposite signs. One is positive. Thus this spatial mode grows, even though the original homogeneous reaction system was stable. On a periodic interval of length four pi, a mode with wave number one half is admissible, so this example genuinely demonstrates a finite-domain linear instability.

The fast-diffusing v component acts like a spatially distributed influence. Each individual diffusion term damps its own concentration's spatial variation, but the reaction coupling can turn those unequal damping rates into amplification of the combined mode.

### Linear instability is not a finished pattern

An eigenvalue with positive real part tells us that sufficiently small perturbations in its eigendirection initially grow. It does not determine their eventual amplitude, their nonlinear shape, or whether the long-time state is steady, oscillatory, chaotic, or unstable in another way.

Nonlinear terms become important as growth proceeds. The solution may settle into a stable spatial pattern, but it may also develop traveling waves, oscillations, coarsening structures, or other dynamics depending on kinetics, geometry, and parameters. Additional bifurcation and nonlinear PDE analysis are needed to establish the final behavior.

Likewise, the presence of two species with one diffusing much faster than the other does not by itself guarantee a Turing instability. The reaction Jacobian must satisfy the inequalities, and an admissible spatial mode must lie in the unstable band.

### Relating this to the other PDE families

The wave equation from the preceding lecture propagates disturbances along characteristics at finite speed. A reaction–diffusion equation contains parabolic diffusion, which smooths spatial modes and does not have the same finite domain of dependence. Yet coupled nonlinear reaction terms can make certain modes grow over time.

These two mechanisms should not be conflated. Waves transport information. Diffusion dissipates gradients, while reaction coupling may amplify selected modes. Their mathematical stability analyses ask different questions.

Turing's contribution was to show that local reaction rules and unequal diffusion can produce a route from homogeneous chemistry toward spatial organization. The compelling idea survives only when we retain the precise conditions: stable homogeneous kinetics, diffusion-driven instability of some nonzero spatial mode, and a separate nonlinear analysis of what happens after the initial growth.

## Spectral Methods for PDEs: Boundary Eigenproblems and Mode Evolution

Imagine a metal rod heated unevenly. Its ends are held at zero temperature, and its interior begins with a complicated temperature profile. Over time the temperature smooths out. Small alternating hot and cold regions vanish quickly, while broad patterns persist much longer.

The heat equation explains this behavior quantitatively. But there is a particularly revealing way to solve it: decompose the initial temperature into spatial modes, let each mode evolve according to its own simple ordinary differential equation, and then add them back together.

The method is called an eigenfunction expansion. It connects partial differential equations to spectral theory, and it also leads naturally to numerical spectral methods.

### The spatial operator comes first

Consider a rod of length L, with temperature zero at both ends. Let u of x and t be its temperature at position x and time t. The heat equation says its time derivative equals a positive diffusivity times its second spatial derivative.

Try a solution whose space and time dependence separate: a product of a spatial shape X of x and an amplitude T of t. Substitution into the equation leaves a spatial differential equation on one side and a temporal differential equation on the other. Since they depend on different variables, they must both equal the same constant, with the sign chosen conveniently.

The spatial problem becomes minus the second derivative of X equals lambda times X, with X zero at both endpoints. This is an eigenvalue problem for the negative second-derivative operator. Its eigenfunctions are sine waves that fit the interval exactly. The first mode makes half an oscillation along the rod; the second makes two half oscillations; the nth has n half oscillations. Their eigenvalues grow like n squared.

Each mode respects the endpoint conditions. That is essential. A Fourier basis chosen without regard for the boundary can produce the wrong physical problem, even if the algebra looks familiar.

### Time evolution of each mode

Once the spatial eigenfunction is fixed, the corresponding time amplitude satisfies a first-order ordinary differential equation. Its decay rate is the diffusivity multiplied by the spatial eigenvalue. So the nth sine mode decays exponentially, with an exponent proportional to negative n squared times time.

This is the precise reason fine-scale temperature variations fade rapidly. A tenth mode decays one hundred times as fast in its exponential rate as the first mode. Give the initial rod a broad single hump and a small ripple that oscillates ten times faster. After even a modest period, the ripple may have nearly vanished while the broad hump remains.

An arbitrary square-integrable initial profile can be expanded as a sine series. The coefficients are obtained by taking its inner products with the normalized spatial modes. The heat solution is the sum of those same modes multiplied by their respective decaying exponentials.

The meaning of convergence changes with the regularity of the initial data. For an arbitrary square-integrable profile, the series makes sense in an appropriate square-integrable sense at initial time. At positive time the heat equation smooths the profile, and the rapidly decaying coefficients make the series much better behaved.

### Energy provides an independent check

We can verify the direction of the dynamics without solving the series. Multiply the heat equation by u and integrate over the rod. Integration by parts, together with the zero endpoint conditions, says the time derivative of the squared temperature norm is negative two times the diffusivity times the squared spatial-gradient norm.

Thus the total squared temperature cannot increase. The Poincaré inequality gives an explicit lower bound on the gradient energy in terms of the temperature energy. Together they imply exponential decay at least at the rate associated with the lowest spatial eigenvalue.

The spectral solution and the energy estimate describe the same mechanism from different angles. One diagonalizes the operator; the other proves a monotonicity law directly. Comparing the two is a powerful guard against a misplaced sign or an incorrect boundary condition.

### The wave equation uses the same modes differently

Now replace the heat equation with the wave equation for a string fixed at both ends. Its second time derivative equals a positive wave-speed squared times its second spatial derivative.

The spatial sine eigenfunctions are unchanged because the boundary operator is unchanged. But each temporal coefficient now satisfies an oscillator equation, not a decay equation. Its frequency is the wave speed multiplied by the square root of the spatial eigenvalue.

If the initial displacement and velocity are expanded in sine modes, each mode oscillates with its own frequency. Their superposition gives the motion of the string. Smoothness does not suddenly improve the way it does for the heat equation; hyperbolic wave evolution transports and oscillates energy rather than diffusing it away.

This comparison teaches something important. The same spatial operator can participate in very different dynamics. Its eigenfunctions describe the geometry of allowed shapes. The PDE's time derivative determines whether those shapes decay, oscillate, or grow.

### From an infinite series to a numerical method

An exact expansion has infinitely many modes. A numerical spectral method retains only finitely many. Choose the first N eigenfunctions and approximate the solution as a linear combination with time-dependent coefficients. Substitute that approximation into the PDE and require the residual to be orthogonal to the retained subspace. This is a Galerkin method.

For a constant-coefficient linear problem with matching boundary eigenfunctions, the resulting system is diagonal and particularly simple. For variable coefficients or nonlinear terms, the modes interact, producing a coupled system of ordinary differential equations. The finite-dimensional problem can then be integrated by the time-stepping methods used in numerical analysis.

High regularity often leads to rapidly decaying spectral coefficients and therefore very accurate approximations with relatively few modes. However, discontinuities and sharp gradients can ruin that advantage. A truncated Fourier representation of a jump can exhibit oscillations near the discontinuity, including the Gibbs phenomenon. Spectral accuracy is conditional on the smoothness of what is being approximated and the suitability of the chosen basis.

### Beyond an interval

On more complicated regions, the analogous spatial problem involves the Laplacian with specified boundary conditions. Under suitable self-adjointness and compactness conditions, there is a discrete sequence of eigenvalues and an orthonormal family of eigenfunctions. These modes can expand square-integrable data and reduce linear PDE evolution to scalar equations.

On unbounded domains the spectrum may be continuous, and sums can be replaced or augmented by integrals. For non-self-adjoint operators, orthogonality can fail, eigenvectors may be incomplete, and spectral expansions require additional care.

So the spectral method is not the claim that every PDE is a Fourier series. It is a strategy: find a spatial operator adapted to the domain and its boundary conditions, understand its spectral structure, and use that structure to simplify time evolution. The resulting connection between PDEs and linear algebra is one of the most productive ideas in mathematical physics and scientific computation.

## Traveling Waves and Front Propagation

Picture a flame advancing along a narrow strip of material. Behind the front the material has reacted; ahead of it, it has not. The flame's position changes, but its local shape may remain almost the same. A population invading new territory can show a similar advancing front. So can a chemical reaction or a change in phase. These phenomena lead to a mathematical question: can a solution of a partial differential equation move at a constant speed while preserving its profile?

Such a solution is called a traveling wave. The idea is simple enough to state in words: instead of describing a different shape at every time, find one shape and translate it. This converts a problem in time and space into an ordinary differential equation for the profile.

### Moving coordinates

Consider a quantity u depending on position x and time t. Let z mean x minus c times t, where c is a constant speed. Suppose u at position x and time t is a function U of z alone. Then the time derivative is minus c times the derivative of U, and the second spatial derivative is the second derivative of U. The moving coordinate has removed explicit time dependence.

In a diffusion-reaction equation, diffusion tries to smooth a profile and the reaction term can amplify or suppress it locally. The traveling-wave substitution creates an ODE balancing the two effects against transport at speed c. A heteroclinic trajectory of this ODE may connect two different constant states as z goes from negative infinity to positive infinity. That connection is the wave front.

The phase-plane viewpoint matters because the ODE is second order. We can treat the profile and its spatial derivative as a two-dimensional dynamical system. The desired front is an orbit connecting equilibrium states under specified limits at either end of space. It is therefore not enough to choose any solution curve; it must have the correct asymptotic behavior and usually the right sign or monotonicity.

### The Fisher–KPP front

A classical example describes diffusion plus logistic growth. At very low density, growth is approximately proportional to the population. At high density, it saturates at a carrying capacity. The equation combines a diffusion coefficient D with a positive growth rate r and a carrying capacity K.

We seek a front with density approximately K far behind and zero far ahead. The profile decreases as the moving coordinate increases. Substituting the traveling profile gives a second-order ODE containing diffusion, a first-derivative term multiplied by the speed, and the logistic reaction.

The leading edge gives a useful calculation. Far ahead of the front, the density is small, so the nonlinear reaction is approximately r times the density. Suppose the tail decays exponentially with rate lambda. Substitution into the linearized profile equation gives a quadratic relationship among D, lambda, r, and c.

For a positive exponential decay rate, the relation can be written as speed equals D times lambda plus r divided by lambda. Arithmetic-geometric mean, or simple calculus, shows that this expression is at least twice the square root of D times r. Thus the leading-edge calculation predicts a minimum admissible speed.

For the classical scalar Fisher–KPP equation on the line, monotone traveling fronts connecting K to zero exist for speeds at least this threshold, and not for smaller positive speeds. Under the standard assumptions for sufficiently localized nontrivial initial data, the long-time invasion selects the minimum speed. That last statement concerns a class of initial-value problems, not every imaginable initial tail: sufficiently slowly decaying initial data can select faster propagation.

The distinction between existence of a whole family of fronts and selection of one speed by initial data is essential. An equation may permit many traveling solutions, while a particular physical preparation chooses only some of them.

### When nonlinear reactions choose the speed

The minimum-speed calculation relies on the behavior near the unstable state zero and on the Fisher–KPP reaction structure. It is not a universal law for moving interfaces.

Consider a bistable reaction instead. Now the reaction has two locally stable constant states, with an unstable state between them. A front can connect the stable states. In that setting, the direction and speed can depend on the signed area under the reaction function between those states.

To see why, multiply the traveling-wave ODE by the derivative of the profile and integrate across the entire front. The diffusion term becomes a derivative of the square of the profile's slope and contributes zero when the slope decays at both ends. The transport term is speed times the integral of the square of the slope, which has a definite sign. The reaction term becomes the integral of the reaction function along the transition between states.

The balance ties the sign of the propagation speed to which stable state has the greater area advantage. If the signed area vanishes, a stationary interface can appear. This calculation shows that the whole nonlinear reaction, not merely the linear growth rate at one end, may determine front motion.

We must not infer front existence from the area identity alone. It is a necessary relation for a sufficiently regular front with the stated limits. Establishing that the corresponding heteroclinic orbit exists requires further dynamical analysis.

### Fronts, pulses, and patterns

Not every traveling wave is a front. A traveling pulse may rise above a background level and return to that same level at both ends. Solitary-wave solutions of dispersive equations provide other examples, often governed by conservation and dispersion rather than reaction and diffusion. Periodic traveling waves repeat a pattern as they move.

The shared mathematical technique is the moving coordinate. The resulting profile equation and the correct boundary conditions determine which of these structures are possible. A pulse is typically a homoclinic-type orbit in profile phase space, while a front corresponds to a heteroclinic connection between distinct equilibria.

This language gives us a way to compare problems that look physically different. The motion of an invasion, a reaction interface, and a concentration pulse may all be investigated through orbits of related dynamical systems, with different source terms and conservation laws.

### What controls the observed front?

The existence of a traveling profile is only the beginning. We must also ask whether nearby profiles stay close, whether perturbations change the speed, whether the medium is homogeneous, and whether an initial condition converges to one of the admissible fronts. A moving front in a finite domain may interact with boundaries; in several spatial dimensions, curvature can alter the propagation law.

For Fisher–KPP propagation, the leading edge gives an unusually informative speed bound. For bistable systems, an energy-type integral identifies the direction of motion. Both calculations reduce a spatial-temporal process to a shape problem, but neither licenses applying its formula outside the specified model.

Traveling waves make an important idea concrete: motion need not mean that the geometry of a solution is changing. Sometimes all the dynamics can be absorbed into translation, leaving a stationary profile whose existence, stability, and speed become questions in ordinary differential equations.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Reaction–Diffusion Systems and Turing Instability

**Track:** Differential Equations and Dynamical Systems. **Background:** PDE diffusion, linear systems, eigenvalues, stability and bifurcation. **Central question:** how can two individually diffusing chemical species destabilize a uniform equilibrium and select spatial patterns?

#### Mathematical companion (not spoken)

For \(D_u,D_v>0\), consider
\[u_t=f(u,v)+D_u\Delta u,\qquad v_t=g(u,v)+D_v\Delta v.\]
At a homogeneous equilibrium, write \(J=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), \(\tau=a+d\), \(\Delta_0=ad-bc\). Homogeneous linear asymptotic stability requires \(\tau<0\), \(\Delta_0>0\).

For a Laplacian eigenmode \(-q^2\), the evolution matrix is \(M(q)=J-q^2\operatorname{diag}(D_u,D_v)\), with
\[\operatorname{tr}M(q)=\tau-(D_u+D_v)q^2<0,\]
\[\det M(q)=\Delta_0-(aD_v+dD_u)q^2+D_uD_vq^4.\]
With continuously available \(q^2>0\), there is a diffusion-driven unstable band iff
\[aD_v+dD_u>0,\qquad (aD_v+dD_u)^2>4D_uD_v\Delta_0,\]
in addition to homogeneous stability. On bounded domains, a mode in the unstable band must actually belong to the Laplacian spectrum with the specified boundary conditions.

**Worked example:** \(J=\begin{pmatrix}1&-2\\2&-3\end{pmatrix}\), \((D_u,D_v)=(1,20)\), so \(\tau=-2\), \(\Delta_0=1\). At \(q^2=1/4\), \(M(q)=\begin{pmatrix}3/4&-2\\2&-8\end{pmatrix}\), \(\operatorname{tr}M=-29/4\), \(\det M=-(6)+4=-2\). On a periodic interval of length \(4\pi\), the Fourier mode \(q=1/2\) is available. One eigenvalue is positive. Nonlinear saturation and long-time pattern existence are not proved by this linearization.

##### Exercises with answers

1. For \(J\) in the worked example, is the spatially uniform mode stable? **Yes:** trace \(-2<0\) and determinant \(1>0\).
2. If the determinant of a real two-by-two mode matrix is negative, what happens? **Answer:** its eigenvalues are real with opposite signs, so one mode grows exponentially.
3. Does a fast inhibitor alone guarantee patterns? **No:** reaction inequalities and admissible spatial eigenmodes are also required.
4. What does Turing's linear test *not* establish? **Answer:** existence and nonlinear stability of a particular finite-amplitude steady pattern.

##### Reading and source notes

- Alan M. Turing, [*The Chemical Basis of Morphogenesis* (1952)](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf), original diffusion-driven instability mechanism and model limitations.
- [Andrew Hodges's bibliographic record of Turing's morphogenesis papers](https://www.turing.org.uk/sources/biblio3.html), historical attribution and 1952 publication details.
- [University of British Columbia teaching notes on reaction–diffusion and Turing patterns](https://personal.math.ubc.ca/~keshet/MCB2012/SlidesLEK/RDTuring_ppt.pdf), activator-inhibitor example and diffusion contrast.

### Spectral Methods for PDEs: Boundary Eigenproblems and Mode Evolution

**Track:** Differential Equations and Dynamical Systems. **Background:** heat and wave equations, linear algebra, Fourier series, boundary conditions. **Central question:** why can a PDE often be solved by following infinitely many uncoupled ordinary differential equations?

#### Mathematical companion (not spoken)

For \(0<x<L\), \(u_t=\kappa u_{xx}\), \(u(0,t)=u(L,t)=0\), and \(u(x,0)=f(x)\in L^2(0,L)\), the Dirichlet operator \(-\partial_{xx}\) has eigenpairs
\[\phi_n(x)=\sqrt{2/L}\sin(n\pi x/L),\qquad\lambda_n=(n\pi/L)^2,\quad n\ge1.\]
The mild solution is
\[u(t,x)=\sum_{n=1}^\infty\langle f,\phi_n\rangle_{L^2}\,e^{-\kappa\lambda_nt}\phi_n(x).\]
For sufficient smoothness, integration by parts gives \(\frac{d}{dt}\|u(t)\|_{L^2}^2=-2\kappa\|u_x(t)\|_{L^2}^2\le-2\kappa\lambda_1\|u(t)\|_{L^2}^2\). Thus \(\|u(t)\|_{L^2}\le e^{-\kappa\lambda_1t}\|f\|_{L^2}\).

For the Dirichlet wave equation \(u_{tt}=c^2u_{xx}\), each coefficient satisfies \(a_n''(t)+c^2\lambda_na_n(t)=0\), so \(a_n=A_n\cos(c\sqrt{\lambda_n}t)+B_n\sin(c\sqrt{\lambda_n}t)\), with \(B_n\) determined by initial velocity. A truncated Galerkin expansion \(u_N=\sum_{n=1}^Na_n(t)\phi_n(x)\) approximates the PDE while preserving the chosen boundary conditions.

##### Exercises with answers

1. How much faster does the tenth heat mode decay than the first? **Answer:** its exponential decay rate is \(\lambda_{10}/\lambda_1=100\) times larger.
2. If the initial data equal \(\phi_3\), which modes appear later in the linear heat equation? **Answer:** only \(\phi_3\), multiplied by \(e^{-\kappa\lambda_3t}\).
3. Why do the sine modes fail for nonzero fixed endpoint values without modification? **Answer:** they vanish at endpoints; first subtract a function satisfying the nonhomogeneous boundary data.
4. Does Fourier truncation near a discontinuity automatically produce small maximum error? **No:** Gibbs oscillations persist in amplitude near jumps, although convergence holds in appropriate integral senses.

##### Reading and source notes

- Lawrence C. Evans, [*Partial Differential Equations* (AMS textbook information)](https://www.ams.org/books/gsm/019/), separation, weak formulations, and spectral operators.
- [MIT 18.303 Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/), boundary eigenfunctions and mode expansions.
- [MIT 18.330 Introduction to Numerical Analysis](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/), numerical approximation and spectral discretizations.

### Traveling Waves and Front Propagation

**Track:** Differential Equations and Dynamical Systems. **Background:** diffusion equations, phase planes, reaction–diffusion models, linear stability. **Central question:** how does a stationary wave profile move across space without changing shape?

#### Mathematical companion (not spoken)

For \(u_t=D u_{xx}+f(u)\) on \(\mathbb R\) with \(D>0\), use \(u(x,t)=U(z)\), \(z=x-ct\). Then
\[D U''+cU'+f(U)=0.\]
A **front** has \(U(-\infty)=b\), \(U(+\infty)=a\) for distinct roots \(f(a)=f(b)=0\), and often \(U'\to0\) at both infinities.

**Fisher–KPP:** \(f(u)=ru(1-u/K)\), with \(r,K>0\). For a positive monotone front \(K\to0\), let \(U\sim e^{-\lambda z}\) as \(z\to+\infty\). The characteristic relation is
\[D\lambda^2-c\lambda+r=0,\qquad c=D\lambda+r/\lambda\ge2\sqrt{Dr}.\]
Monotone fronts exist for \(c\ge2\sqrt{Dr}\) and not below. Selection of \(c=2\sqrt{Dr}\) by localized nontrivial data requires the standard Fisher–KPP hypotheses.

**Bistable area identity:** if U connects b on the left to a on the right and \(U',U''\to0\), multiply the profile ODE by U' and integrate:
\[c\int_{\mathbb R}(U')^2\,dz=\int_a^b f(s)\,ds.\]
This identifies the sign of c for a nonconstant front but does not by itself establish existence or stability. For a **pulse**, the two limiting states may coincide instead.

##### Exercises with answers

1. For \(D=4\), \(r=9\), what is the Fisher–KPP minimum speed? **Answer:** \(2\sqrt{4\cdot9}=12\).
2. Why does the moving-coordinate ansatz convert a PDE to an ODE? **Answer:** both independent variables enter only through \(z=x-ct\), so \(u_t=-cU'\) and \(u_{xx}=U''\).
3. If \(\int_a^b f(s)ds=0\) and a nonconstant bistable front exists, what is its speed? **Answer:** zero, by the area identity.
4. Does every initial condition select the Fisher–KPP minimum speed? **Answer:** no; selection needs hypotheses on the initial data, especially on its leading-edge decay.

##### Reading and source notes

- [Fisher–KPP equation notes](https://mathsbio.com/spatial-mathematical-biology/fisher-kpp-equation/), front ODE and speed calculation.
- Lawrence C. Evans, [*Partial Differential Equations*](https://bookstore.ams.org/gsm-19-r), diffusion-reaction theory and PDE foundations.
- [MIT OpenCourseWare, Nonlinear Dynamics and Chaos](https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/), phase-plane and heteroclinic-connection methods.
