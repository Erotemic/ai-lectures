# Reaction fronts: selected speeds, pinning, and slow motion

<!-- BEGIN SPOKEN LECTURE -->

# Reaction fronts: selected speeds, pinning, and slow motion

## Reaction Fronts: Comparison Principles and Selected Speeds

Suppose a population occupies part of a long habitat and gradually invades the empty region beside it. Local reproduction increases population density; diffusion spreads individuals into nearby space. Under suitable assumptions, the boundary between occupied and unoccupied regions moves at a nearly constant speed, forming a traveling front.

A standard model is the Fisher–KPP equation. It has a diffusion term and a logistic reaction term: growth is approximately proportional to density when the population is rare, but decreases as density approaches a carrying capacity. The simple equation already raises three different questions. Does a front-shaped solution exist? How fast can it travel? And if the front is perturbed, does it recover its shape?

Those questions are related but not identical. Finding a wave profile does not prove that an arbitrary initial population approaches that profile. Linear analysis near an empty state can predict a candidate speed, but that calculation alone does not establish the full nonlinear existence theorem.

### Why two constant solutions matter

The logistic reaction has two equilibria: density zero and density one after normalizing carrying capacity. The constant one solution represents the populated state, while zero represents the empty state. With nonnegative initial density at most one, the parabolic comparison principle ensures the solution stays between these two bounds under the usual regularity assumptions.

The comparison principle says that if one solution begins below another and the appropriate differential inequalities hold, their ordering is preserved. For scalar reaction–diffusion equations, this is a powerful replacement for explicit solution formulas. We can build simple upper and lower solutions and trap the true evolution between them.

The principle should not be used indiscriminately on systems of coupled equations. Comparison for scalar parabolic equations relies on order-preserving structure; a multi-species reaction system may lack it unless special quasimonotonicity conditions are satisfied.

### The leading edge selects a speed

Seek a right-moving profile that depends on position minus speed times time. Far ahead of the advancing front, the population is very small. The nonlinear logistic term is then approximately a linear growth term. Suppose the leading edge decays exponentially with distance from the moving front.

Substituting an exponential decay into the linearized equation gives a quadratic relation among the decay rate, the diffusion coefficient, the growth rate, and the speed. For the decay rate to be real and positive, the speed must be at least twice the square root of diffusion times growth.

This is the characteristic minimal speed of a Fisher–KPP front. The algebra is revealing: stronger diffusion spreads the leading edge more quickly, while faster reproduction amplifies the tiny population at that leading edge. Both effects increase the invasion speed.

But we must not elevate the quadratic calculation into a complete theorem by itself. It is a necessary leading-edge condition for a monotone exponential tail. Establishing existence of traveling waves at and above that speed, and excluding waves below it, uses nonlinear ODE and comparison arguments. The equation's special KPP structure matters.

### Building a barrier

An exponential moving profile can also be used as an upper barrier. Choose a speed sufficiently large relative to a positive decay rate. The exponential then satisfies the appropriate supersolution inequality for the logistic PDE. A comparison argument shows that sufficiently localized initial data cannot send a significant amount of population arbitrarily far ahead of such a moving barrier.

By optimizing over the decay rate, we recover the same critical speed. A matching lower-spreading result requires a different construction, using subsolutions and the nonlinear dynamics behind the leading edge. Together the upper and lower results explain why localized nontrivial populations spread asymptotically at the characteristic Fisher–KPP speed.

That statement still needs its assumptions. Initial data with a very slowly decaying tail can select faster propagation, and other reaction laws can support pushed fronts whose speed is not determined solely by the linear growth rate at zero.

### What does front stability mean?

There is one unavoidable complication when asking whether a traveling front is stable. If U of z is a profile, then U of z minus a constant shift is also a profile. The equation does not privilege a particular origin of the moving coordinate. A small perturbation may change the front's position permanently while leaving its shape intact.

Therefore convergence to exactly the original translated profile is generally too strong a demand. A more appropriate notion is orbital stability: the perturbed solution stays near the family of translated fronts, perhaps converging toward a member with a shifted phase.

In spectral language, translation produces a neutral mode. Differentiating the wave profile with respect to its position gives a direction in which the linearized operator has zero eigenvalue. Seeing this zero mode is not a sign that the front is unstable. It reflects a symmetry that must be handled correctly in any stability theorem.

The position of a spreading front can also have slow corrections beyond its leading speed. For the classical Fisher–KPP equation and sufficiently localized initial data, a logarithmic delay appears in the front location. Thus statements about convergence and speed should specify the norm, the reference frame, and the class of initial data.

### The broader method

Reaction fronts appear in combustion, ecology, chemical kinetics, and phase transitions. The same basic tools recur: identify equilibria, construct traveling waves, analyze their leading and trailing edges, use maximum or comparison principles to control solutions, and account for symmetry when defining stability.

Not every medium is scalar, homogeneous, or one-dimensional. Heterogeneous diffusion, systems of reacting species, and nonlocal dispersal can change both the existence theory and the selected speed. Yet the Fisher–KPP model remains a useful training ground because each mathematical mechanism is visible separately.

The key lesson is to resist collapsing three theorems into one. A wave profile exists under specified conditions. A population spreads at a speed under specified initial conditions. And a wave is stable under a specified perturbation notion. Comparison principles, leading-edge analysis, and spectral methods answer different parts of that story.

## Front Pinning: When a Traveling Wave Stops

A reaction–diffusion front separates regions in different states. Imagine a chemical reaction that has already converted the material on the left but not on the right. Diffusion spreads the chemicals, while reaction terms favor one state or the other. In a uniform medium, a front may propagate with a fixed shape and speed.

But what if the medium varies from place to place? A region with lower reaction rates or different local stability can slow the front. A sufficiently strong defect may hold the interface in place. This is front pinning. When a control parameter crosses a threshold and the front starts moving again, the transition is called depinning.

These terms describe mathematically distinct phenomena. A stationary front can exist because two states are exactly balanced in a uniform medium. Pinning by heterogeneity is different: an otherwise moving front can become trapped by spatial variation.

### A bistable reaction model

A convenient model is a scalar equation with diffusion plus a cubic reaction term. The reaction has three uniform equilibria: zero, an intermediate value a between zero and one, and one. The outer states are locally stable, while the middle state is unstable.

Seek a traveling profile U depending only on position minus speed times time. A decreasing front runs from state one on the left to state zero on the right. Its motion is governed by a second-order ordinary differential equation. In the classical cubic model there is an explicit logistic-shaped profile and an exact speed.

The speed is proportional to one minus twice a. If a is below one half, state one invades state zero in our chosen orientation. If a is above one half, the front moves the other way. At a equals one half, the two stable states are balanced and the front is stationary.

This exact example is useful because it separates profile shape from the direction of travel. Diffusion sets the front's width. The imbalance between the two stable states determines the sign of its speed.

### Where the speed formula comes from

There is a qualitative energy argument behind the exact formula. Multiply the traveling-wave equation by the derivative of the profile and integrate across the real line. The diffusion term becomes a boundary contribution and vanishes for a front whose derivative decays at both ends. The speed term becomes the speed times an integral of the squared profile derivative. The reaction term becomes an integral of the reaction function from one state to the other.

The integral of the reaction term measures the difference between the wells of the associated reaction potential. At the balanced value a equals one half, the integral vanishes and the front's speed is zero. Away from that balance, its sign decides which state invades.

This makes one point precise: the front's speed is connected to a global difference in potential, not only to the local slope of the reaction near either equilibrium.

### A heterogeneous medium

Suppose the intermediate threshold a varies with position. Now the equation is no longer invariant under translations. We cannot expect every translate of a fixed wave profile to remain a solution. The front may have preferred locations where the local reaction environment balances the force that would otherwise move it.

To understand the possibility of pinning, we can approximate the motion by a collective coordinate X, the current center of the front. In a weakly heterogeneous problem, a solvability calculation based on the translation mode of the uniform front can lead to an effective equation for X. The front speed is replaced by a function of position.

Consider the illustrative reduced model in which X prime equals c zero minus epsilon times sine X. Here c zero is the speed of the unperturbed front and epsilon is the strength of a periodic inhomogeneity. A stationary position must satisfy sine X equals c zero divided by epsilon. Such a position exists only if the absolute value of c zero is no greater than epsilon.

Within that range, stable and unstable fixed positions alternate. A small perturbation of a stable pinned position moves the front back toward the defect. If the driving speed exceeds epsilon in magnitude, no equilibrium remains, and the reduced front drifts through the medium.

This toy differential equation captures a depinning threshold and the loss of equilibria, often through a saddle-node mechanism. It is not a universal exact reduction of every reaction–diffusion equation. The actual threshold and the reduced forcing function depend on the spatial profile, the front's adjoint mode, the domain, and the size of the heterogeneity.

### Pinning is a stability question

Even if a stationary front exists, we must ask whether it is stable. A stationary interface might be delicately balanced and move away after a small disturbance. To analyze this, we linearize the full PDE around the stationary profile and inspect its spectrum or construct energy estimates appropriate to the problem.

In a uniform medium, translation invariance typically produces a neutral eigenfunction: shifting the front slightly gives another stationary or traveling profile. Heterogeneity breaks this invariance and can move that neutral mode into a stable or unstable direction. Pinning can therefore be understood as a change in the dynamics of the translation mode.

There are additional complications. Strong heterogeneity can distort the front's shape; it may create multiple stationary interfaces, or make fronts interact with boundaries. In more than one dimension, curvature and geometry also influence motion. A single coordinate X cannot describe every deformation of the interface.

Yet the reduced model provides a meaningful conceptual guide. If the unperturbed front has a net drive, a defect can oppose it. When the maximal opposing effect is strong enough, the front can stop. When the drive overcomes that effect, the front moves again. The precise result must come from the PDE and its hypotheses, not from drawing a sine curve alone.

Front pinning shows how spatial structure changes dynamics. A uniform equation offers a family of translates and a constant wave speed. A heterogeneous equation chooses locations, introduces thresholds, and can replace continuous drift with stable stationary states. The study of traveling waves becomes the study of how geometry and local material properties select motion or rest.

## Pattern-Forming Interfaces: Stability Beyond an Exact Front

Imagine a material with two preferred states. On the left it is in one state, and on the right it is in the other. Between them is a narrow transition layer. A reaction–diffusion equation can describe how such an interface evolves under diffusion and local preference for one state or the other.

A stationary interface is an exact solution that keeps the same profile over time. But exact stationarity does not answer the stability question. If we slightly perturb the profile, does it recover? Does it drift? Does it develop waves or new spatial patterns? Or does it collapse toward one uniform phase?

The Allen–Cahn equation is an ideal model for separating these questions. In one dimension, the rate of change of a scalar field equals its second spatial derivative plus the field minus its cube. The uniform states plus one and minus one are stable equilibria of the local reaction term. The state zero is unstable.

Between the two stable states, there is a smooth stationary front. Its shape is the hyperbolic tangent of x divided by the square root of two. At the far left it approaches minus one; at the far right it approaches plus one.

## Why the hyperbolic tangent appears

To find a stationary solution, set the time derivative to zero. The remaining second-order equation balances diffusion against the double-well reaction force. It resembles the equation of a particle moving in a potential if the spatial coordinate is reinterpreted as time.

Multiply the stationary equation by the spatial derivative of the profile. The terms combine into an exact derivative. Integrating once gives a first-order relationship between the slope and the double-well potential. For a front connecting minus one to plus one with vanishing derivatives at infinity, the integration constant is fixed.

The first-order equation can be separated. Its solution is the hyperbolic tangent profile. The front's width is set by the competition between diffusion and reaction. Making diffusion stronger would broaden the transition; strengthening the reaction relative to diffusion would narrow it.

This explicit formula is useful because every stability calculation can be checked against it. We know the profile, its derivative, the states at infinity, and the energy it carries.

## Energy makes the flow directional

Allen–Cahn is a gradient flow for an energy with two contributions. Spatial gradients cost energy, and values away from the two preferred phases cost potential energy. The potential has two wells, one at plus one and the other at minus one.

Differentiate the energy along a smooth decaying solution. Integration by parts produces minus the integral of the square of the time derivative. The energy cannot increase. It falls unless the system is stationary.

This does not mean every solution converges to the particular front centred at zero. The equation is invariant under spatial translation. Shifting the front left or right produces another stationary solution with exactly the same energy. There is no mechanism requiring the interface to return to the original location after a perturbation that simply moves it.

The correct stable object is the family of translated fronts, not one isolated profile.

## Linearize around the front

Write the evolving field as the exact front plus a small perturbation. Retain the terms linear in the perturbation. The resulting operator is a second spatial derivative plus one minus three times the square of the front.

Differentiate the stationary front equation with respect to position. That derivative solves the linearized equation with eigenvalue zero. The reason is symmetry: moving the front a little to the right or left costs no restoring energy. The derivative of the front is the infinitesimal translation direction.

Other perturbations need not behave that way. In this model the remaining spectrum of the linearized operator lies strictly to the left of zero. There is one additional isolated eigenvalue at negative three halves, and the essential spectrum begins at negative two and extends toward more negative values.

This is a spectral-gap statement after translation is factored out. Small perturbations transverse to the family of shifts decay. The neutral translation mode remains. Therefore a solution near the front can approach some shifted front, rather than the same front with which it began.

## Modulation tracks the drifting location

To make this precise, one may write the evolving field as a translated front plus a remainder. The translation amount becomes a time-dependent variable. We choose it so that the remainder is orthogonal to the neutral eigenfunction.

This condition removes the ambiguity in how much of the perturbation is a simple shift. Spectral estimates then control the remainder, while an evolution equation controls the translation parameter. This is called modulation.

The same idea appears in the stability theory of traveling waves, solitons, periodic patterns, and interfaces in fluids. Symmetries create neutral directions. A stability theorem must either work in a quotient by those symmetries or explicitly track their parameters.

## A front is not an isolated oscillatory pattern

A single monotone Allen–Cahn front has no internal oscillation. It is useful to distinguish it from a train of stripes, spots, or Turing patterns produced by reaction–diffusion instabilities. Those patterns may have several critical wave numbers and more than one neutral mode.

If there are two well-separated interfaces, they may interact through the exponentially small tails of their profiles. Each isolated front looks stable, but the pair can drift slowly and eventually collide. This is metastability: the system remains close to a family of patterns for a long time without being at a stable equilibrium forever.

In higher spatial dimensions, a planar interface can wrinkle. The curvature of the interface influences its motion, and transverse Fourier modes contribute additional decay or instability depending on the model. Geometry and spectral analysis must be combined.

The two-phase Allen–Cahn example provides a baseline rather than a universal answer to every pattern-forming PDE. Other reaction kinetics can make fronts unstable, create pinned interfaces, or support oscillatory modes. Stability is a property of a specified equation and a specified wave, not an adjective that follows from knowing an exact formula.

## The proof has several layers

First, construct the profile and verify the stationary equation. Second, identify a Lyapunov energy if one is available. Third, calculate the linearized operator and its spectrum, paying attention to neutral symmetry modes. Fourth, use nonlinear estimates to show that small remainders remain controlled and decay toward the translated family.

A spectral gap is suggestive but not sufficient all by itself. One must know the relevant function spaces, the regularity of the nonlinear flow, and how the nonlinear error terms compare with the linear decay. Conversely, an energy inequality may establish stability even when exact spectral calculations are unavailable.

This sequence of ideas is useful far beyond Allen–Cahn. Interfaces are central in phase transitions, combustion, biological pattern formation, and materials science. The exact front gives a reference shape. The stability analysis tells us whether the shape has predictive power under perturbation and what kinds of motion remain possible.

## Metastable Multi-Front Motion in Allen-Cahn Equations

Watch a numerical simulation of a reaction–diffusion equation for a modest interval of time. Several sharp interfaces separate regions in two stable phases. The interfaces seem stationary. It is tempting to conclude that the pattern is a stable equilibrium.

But extend the simulation enormously, and an interface may drift toward a neighbor. Two interfaces can annihilate. A pattern that survived every practical observation window can eventually simplify to a uniform state. This is metastability: motion so slow that the system spends a long time near a family of states that are not exact equilibria.

The Allen–Cahn equation is a clean mathematical model for this effect. It has a double-well potential, diffusion that penalizes sharp gradients, and a parameter controlling interface thickness. Its dynamics are a gradient descent of an energy functional. Yet the energy landscape contains long, shallow directions corresponding to widely separated interfaces, so energy decrease can proceed at an exponentially small rate.

## The equation and its energy

Consider the scalar field u on an interval or line. Let its time derivative equal a small positive parameter squared times its second spatial derivative, plus u minus u cubed. The reaction term has stable constant states at plus one and minus one, with an unstable constant state at zero.

The associated energy has two pieces. One penalizes spatial gradients; the other penalizes values away from plus or minus one through a double-well potential. The time evolution is the negative gradient of this energy under the usual L-two inner product.

Differentiate the energy along a sufficiently regular solution with boundary conditions that remove boundary flux terms. The derivative equals minus the spatial integral of the time derivative squared. Thus energy never increases. If the solution is actually moving, energy decreases.

This identity alone does not reveal the speed of the motion. A quantity can decrease extremely slowly while remaining strictly decreasing. Understanding metastability requires estimating how small the energy gradient becomes near a configuration of separated interfaces.

## A single interface can be solved exactly

On the infinite line there is a stationary front increasing from minus one to plus one. It is the hyperbolic tangent of the spatial coordinate divided by the square root of two times the small parameter.

This is an exact solution, not merely an asymptotic approximation. Its width is proportional to the small parameter. Far from the center, the deviation from the limiting constant states decays exponentially in distance divided by that parameter.

The same front can be translated to any location because the equation on the infinite line is translation invariant. Differentiating with respect to the location produces a neutral mode of the linearized operator. In effect, there is a continuous family of equally energetic stationary states indexed by the interface position.

On a finite interval or in a multi-interface pattern, that exact symmetry is broken by boundaries and neighboring fronts. Yet when the interfaces are far apart compared with their thickness, the symmetry is only weakly broken. Small interactions turn the neutral motion into a very slow drift.

## Why two fronts can wait so long

Take a front rising from minus one to plus one, followed a long distance later by a front descending back to minus one. Between them lies a plateau of the plus phase. Their far tails overlap only slightly.

Each isolated front would be stationary. When superposed, the pair is not exactly stationary, because the exponentially small tails interact. The residual in the Allen–Cahn equation is controlled by an exponential in the negative separation divided by the interface width.

This leads to effective equations for interface positions whose leading velocities are exponentially small when the separation is much greater than the interface thickness. A distance of many interface widths can therefore create an enormous waiting time. Eventually, as fronts approach, the interaction strengthens and the final annihilation may be rapid on the original time scale.

The sign and magnitude of the motion depend on the phase ordering, boundary conditions, and interactions among all fronts. Alternating kink–antikink pairs often attract, but a universal law of attraction with one fixed coefficient would ignore these details.

## From a PDE to interface coordinates

A standard analysis starts by building an approximate manifold of multi-front profiles. Its coordinates are the interface locations. Solutions sufficiently near that manifold can be decomposed into an approximate profile plus a remainder orthogonal to suitable translational modes.

The remainder is controlled using spectral estimates for the linearized operator. The slowly evolving interface coordinates satisfy modulation equations obtained by projecting the PDE onto the near-neutral modes.

This separates two timescales. Shape errors that are not associated with translating the fronts can decay comparatively quickly. The front positions, however, change only through the weak interaction of tails or boundaries. It is possible for the profile to look exceptionally clean long before the interfaces have approached their eventual locations.

The reduction is not automatically justified for an arbitrary pattern or arbitrary initial condition. One must prove that the solution enters and remains in the neighborhood where the modulation description is valid and that the spectral gap away from the slow modes is controlled.

## Exponentially long means something precise

Suppose neighboring interfaces are separated by a length L and have thickness proportional to epsilon. The tail overlap is of order an exponential of a negative constant times L over epsilon. Effective velocities can be of that order. Hence significant interface displacement can require times growing exponentially with L over epsilon.

In a theorem, the constant, time interval, and norm depend on the chosen potential and boundary conditions. Carr and Pego's classical analysis shows how multiple layers can persist for exponentially long times in the one-dimensional Allen–Cahn setting under appropriate hypotheses.

A simulation at fixed epsilon may make the phenomenon visible only after very long integration. Numerical discretization can also distort it. An artificial grid-pinning force may hold interfaces still for the wrong reason, while time-stepping error can introduce spurious drift. Evidence of metastability should therefore include convergence checks and, where possible, comparison with asymptotic interface laws.

## Energy and front tension

The exact kink also lets us compute the cost of an interface. Substitute its profile into the Allen–Cahn energy. The gradient and potential contributions agree pointwise for this stationary heteroclinic. Integrating gives an interface energy proportional to epsilon, with coefficient two times the square root of two divided by three.

A multi-front pattern has energy approximately equal to the number of interfaces times that single-front cost, plus exponentially small interaction terms. Moving an isolated front barely changes the leading energy. Only the tiny interaction contribution creates a preferred direction of motion.

This is the energy-landscape explanation of metastability. The system can have a valid descent direction that is far too shallow to produce noticeable motion on moderate timescales. The PDE is not trapped at an exact local minimum; it is traveling along a nearly flat valley.

## What metastability teaches about dynamics

There is an important difference among equilibrium, asymptotic stability, and metastability. An equilibrium has zero time derivative. A stable equilibrium resists small perturbations in a specified sense. A metastable configuration may not be an equilibrium at all; it merely evolves so slowly that its eventual change is invisible on shorter observation windows.

Allen–Cahn fronts make the distinction quantitative. An exact isolated kink has a translation symmetry. Multiple well-separated fronts break that symmetry weakly. Their interactions are exponentially small, and their collective motion can last exponentially long. Energy decreases all the while.

This mechanism appears in phase separation, nucleation, transition layers, and slowly evolving coherent structures. The mathematical method is broadly reusable: identify a family of approximate equilibria, separate fast transverse relaxation from slow motion along that family, and prove an effective equation for the slow coordinates. That is how a frozen-looking picture becomes a carefully quantified dynamical phenomenon.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Reaction Fronts: Comparison Principles and Selected Speeds

**Track:** Differential Equations and Dynamical Systems. **Background:** reaction–diffusion PDEs, traveling waves, linearization, maximum principles. **Central question:** how do local growth and diffusion determine whether a propagating front survives?

#### Mathematical companion (not spoken)

Consider
\[u_t=D u_{xx}+r u(1-u),\qquad D,r>0,\quad x\in\mathbf R.\]
For bounded regular initial data \(0\le u_0\le1\), the comparison principle with stationary sub/supersolutions 0 and 1 gives \(0\le u(t,x)\le1\). A traveling wave \(u(t,x)=U(z)\), \(z=x-ct\), satisfies
\[D U''+cU'+rU(1-U)=0,\quad U(-\infty)=1,\ U(+\infty)=0.\]
At the leading edge take \(U\sim e^{-\lambda z}\), \(\lambda>0\). The linearized dispersion relation is \(D\lambda^2-c\lambda+r=0\), so a positive real rate requires \(c\ge2\sqrt{Dr}\). For the classical KPP nonlinearity, monotone waves exist for all \(c\ge2\sqrt{Dr}\); rigorous existence is not established by linearization alone.

For \(w=e^{-\lambda(x-ct)}\),
\[w_t-Dw_{xx}-rw(1-w)=(c\lambda-D\lambda^2-r)w+rw^2.\]
Thus if \(c\ge D\lambda+r/\lambda\), w is a positive supersolution; comparison and suitable bounded barriers yield upper-spreading estimates. The minimizer \(\lambda=\sqrt{r/D}\) gives \(c_*=2\sqrt{Dr}\). Linearizing in the moving frame around U yields an operator L with \(L U'=0\) due to translation invariance, so stability is formulated modulo translations. Statements about asymptotic speed, phase shifts, and logarithmic corrections require their own assumptions on initial tails.

##### Exercises with answers

1. Compute the minimal wave speed for \(D=4,r=9\). **Answer:** \(2\sqrt{36}=12\).
2. Why does a constant zero solution act as a lower barrier for nonnegative initial data? **Answer:** it solves the PDE and comparison preserves ordering.
3. Explain the zero eigenvalue in the linearization around a wave. **Answer:** translating the wave is a symmetry; its derivative \(U'\) is a neutral direction.
4. Does the dispersion relation alone prove convergence of any initial condition to a wave? **Answer:** no; existence, speed selection, and nonlinear stability are distinct.

##### Reading and source notes

- [Classical Fisher–KPP wave theory reviewed in Genetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3914622/), leading-edge analysis and speed selection.
- [Lawrence C. Evans, Partial Differential Equations](https://bookstore.ams.org/gsm-19-r), scalar parabolic comparison and maximum principles.

### Front Pinning: When a Traveling Wave Stops

**Track:** Differential Equations. **Background:** reaction–diffusion equations, traveling waves, phase planes, perturbation theory. **Central question:** why does a front that propagates through a uniform medium sometimes stop at a spatial defect?

#### Mathematical companion (not spoken)

For `D>0`, `0<a<1`, consider
\[
u_t=D u_{xx}+u(1-u)(u-a).
\]
The decreasing traveling wave `u(t,x)=U(x-ct)` has the explicit form
\[
U(z)=\frac{1}{1+e^{z/\sqrt{2D}}},\qquad
c=\sqrt{\frac D2}(1-2a).
\]
Indeed `U'=-U(1-U)/sqrt(2D)` and `D U''+cU'+U(1-U)(U-a)=0` at the stated c. Multiplying the traveling-wave equation by `U'` and integrating gives
\[
c\int_{\mathbb R}(U')^2 dz=\int_0^1 s(1-s)(s-a)\,ds=\frac{1-2a}{12},
\]
consistent with the explicit speed and with the sign convention that c is positive for a<1/2.

For the illustrative collective-coordinate ODE `X'=c_0-epsilon sin X` with `epsilon>0`, equilibria exist iff `|c_0|<=epsilon`. At an equilibrium, the derivative of the vector field is `-epsilon cos X`, so equilibria with `cos X>0` are asymptotically stable and those with `cos X<0` unstable. At `|c_0|=epsilon`, equilibria merge in a saddle-node threshold. This is a reduced model, not a theorem that the full heterogeneous PDE always reduces to a sinusoidally forced scalar ODE.

##### Exercises with answers

1. What happens to the explicit front speed at `a=1/2`? **Answer:** it becomes zero.
2. For `D=2,a=1/4`, what is c? **Answer:** `sqrt(2/2)*(1-1/2)=1/2`.
3. In `X'=0.3-0.5 sin X`, can pinned equilibria exist? **Answer:** yes, since `0.3<0.5`.
4. Does the existence of a stationary front guarantee stability? **Answer:** no; one must study perturbations or the linearized PDE.

##### Reading and source notes

- [Fife and McLeod, The Approach of Solutions of Nonlinear Diffusion Equations to Travelling Front Solutions](https://doi.org/10.1007/BF00250432), bistable front dynamics and stability.
- [Keener, Homogenization and Propagation in the Bistable Equation](https://doi.org/10.1016/S0167-2789(99)00151-7), spatial heterogeneity and front propagation.
- [Xin, Front Propagation in Heterogeneous Media](https://doi.org/10.1137/S0036144599364296), front behavior in inhomogeneous settings.

### Pattern-Forming Interfaces: Stability Beyond an Exact Front

**Track:** Differential Equations and Dynamical Systems. **Background:** reaction–diffusion equations, stationary fronts, spectra, and energy methods. **Central question:** when does an exact interface solution persist under perturbation, and how does translation symmetry change what stability means?

#### Mathematical companion (not spoken)

For `u_t=u_xx+u-u^3`, let `V(u)=(1-u^2)^2/4` and
\[
E[u]=\int_\mathbb R\left(\tfrac12u_x^2+V(u)\right)dx,\quad
\frac{dE}{dt}=-\int_\mathbb R u_t^2\,dx
\]
for sufficiently regular solutions with appropriate spatial decay and renormalized boundary conditions. The front `U(x)=tanh(x/sqrt(2))` solves `U''+U-U^3=0`. Its energy is `E[U]=2sqrt(2)/3` among heteroclinic maps from -1 to +1 (derive using `U'=(1-U^2)/sqrt(2)`).

Linearization `u=U+v` gives `v_t=Lv+O(v^2)` with
\[
L=\partial_x^2+1-3U^2=\partial_x^2-2+3\,\mathrm{sech}^2(x/\sqrt2),\quad LU'=0.
\]
On `L^2(R)` the spectrum is `(-infinity,-2] union {-3/2,0}`. The eigenvalue zero is simple and expresses translation symmetry; stability is *orbital*, modulo translations, not convergence to a preselected location. Claims of nonlinear orbital convergence require control of the nonlinear remainder and the modulation variable. For well-separated multi-front states, exponentially weak interactions can generate metastability.

##### Exercises with answers

1. Differentiate the front equation to prove `LU'=0`. **Answer:** differentiate `U''+U-U^3=0` to obtain `U'''+(1-3U^2)U'=0`.
2. Why does an initial translated front not converge to the front centred at zero? **Answer:** it is already stationary at its new centre, so translation symmetry prevents restoring motion.
3. Compute the front energy. **Answer:** `E=integral_{-1}^1 sqrt(2V(s))ds=(1/sqrt2)integral_{-1}^1(1-s^2)ds=2sqrt2/3`.
4. Does a negative spectrum apart from a zero mode prove stability for every nonlinear perturbation size? **Answer:** no; the conclusion is local and requires nonlinear estimates.

##### Reading and source notes

- [On the Metastability of the 1-d Allen–Cahn Equation](https://link.springer.com/article/10.1007/s10884-020-09874-z), front energy, spectral gap, and multi-front behavior.
- [Spectral Stability of Stationary Solutions of a Boussinesq System](https://www.researchgate.net/publication/220403043_Spectral_Stability_of_Stationary_Solutions_of_a_Boussinesq_System_Describing_Long_Waves_in_Dispersive_Media), Allen–Cahn spectral model in an appendix.
- [Sander and Wanner, Validated Saddle-Node Bifurcations and Applications to Lattice Dynamical Systems](https://epubs.siam.org/doi/10.1137/16M1061011), computationally verified pattern branches and pinning phenomena.

### Metastable Multi-Front Motion in Allen-Cahn Equations

**Track:** Differential Equations. **Background:** reaction–diffusion equations, gradient flows, stationary fronts, and spectral linearization. **Central question:** why can an evolving system appear frozen for an exponentially long time?

#### Mathematical companion (not spoken)

For `u_t=epsilon^2 u_xx+u-u^3`, the energy
\[
E_\epsilon[u]=\int\left[\tfrac{\epsilon^2}{2}u_x^2+\tfrac14(1-u^2)^2\right]dx
\]
satisfies `dE/dt=-int u_t^2 dx` when boundary terms vanish. The stationary heteroclinic is
\[
U(x)=\tanh\left(\frac{x}{\sqrt 2\epsilon}\right),
\quad E_\epsilon[U]=\frac{2\sqrt2}{3}\epsilon.
\]
The kink tails decay like `exp(-sqrt(2)|x|/epsilon)`. Interactions of well-separated fronts at distance `L>>epsilon` produce exponentially small residuals, often `O(exp(-c L/epsilon))` with model-dependent `c`, and under rigorous spectral/invariance hypotheses lead to exponentially slow interface motion. No claim is made that an arbitrary multi-front initial condition satisfies a universal velocity law or lifetime.

##### Exercises with answers

1. What are the stable constant states of the reaction term `u-u^3`? **Answer:** plus one and minus one.
2. Why is a single translated kink stationary on the infinite line? **Answer:** the equation is translation invariant.
3. What happens to the tail interaction as separation L grows at fixed epsilon? **Answer:** it decays exponentially.
4. Why does strictly decreasing energy not exclude metastability? **Answer:** the energy derivative can be negative yet exponentially small.

##### Reading and source notes

- [Carr and Pego, Metastable Patterns in Solutions of the Allen–Cahn Equation](https://doi.org/10.1002/cpa.3160420502), classical exponentially slow interface-motion analysis.
- [Fusco and Hale, Slow-Motion Manifolds, Dormant Instability, and Singular Perturbations](https://doi.org/10.1007/BF01048791), invariant-manifold viewpoint on slow layer motion.
