# 017000 — Traveling Waves and Front Propagation

**Track:** Differential Equations and Dynamical Systems. **Background:** diffusion equations, phase planes, reaction–diffusion models, linear stability. **Central question:** how does a stationary wave profile move across space without changing shape?

<!-- BEGIN SPOKEN LECTURE -->

# Traveling Waves and Front Propagation

Picture a flame advancing along a narrow strip of material. Behind the front the material has reacted; ahead of it, it has not. The flame's position changes, but its local shape may remain almost the same. A population invading new territory can show a similar advancing front. So can a chemical reaction or a change in phase. These phenomena lead to a mathematical question: can a solution of a partial differential equation move at a constant speed while preserving its profile?

Such a solution is called a traveling wave. The idea is simple enough to state in words: instead of describing a different shape at every time, find one shape and translate it. This converts a problem in time and space into an ordinary differential equation for the profile.

## Moving coordinates

Consider a quantity u depending on position x and time t. Let z mean x minus c times t, where c is a constant speed. Suppose u at position x and time t is a function U of z alone. Then the time derivative is minus c times the derivative of U, and the second spatial derivative is the second derivative of U. The moving coordinate has removed explicit time dependence.

In a diffusion-reaction equation, diffusion tries to smooth a profile and the reaction term can amplify or suppress it locally. The traveling-wave substitution creates an ODE balancing the two effects against transport at speed c. A heteroclinic trajectory of this ODE may connect two different constant states as z goes from negative infinity to positive infinity. That connection is the wave front.

The phase-plane viewpoint matters because the ODE is second order. We can treat the profile and its spatial derivative as a two-dimensional dynamical system. The desired front is an orbit connecting equilibrium states under specified limits at either end of space. It is therefore not enough to choose any solution curve; it must have the correct asymptotic behavior and usually the right sign or monotonicity.

## The Fisher–KPP front

A classical example describes diffusion plus logistic growth. At very low density, growth is approximately proportional to the population. At high density, it saturates at a carrying capacity. The equation combines a diffusion coefficient D with a positive growth rate r and a carrying capacity K.

We seek a front with density approximately K far behind and zero far ahead. The profile decreases as the moving coordinate increases. Substituting the traveling profile gives a second-order ODE containing diffusion, a first-derivative term multiplied by the speed, and the logistic reaction.

The leading edge gives a useful calculation. Far ahead of the front, the density is small, so the nonlinear reaction is approximately r times the density. Suppose the tail decays exponentially with rate lambda. Substitution into the linearized profile equation gives a quadratic relationship among D, lambda, r, and c.

For a positive exponential decay rate, the relation can be written as speed equals D times lambda plus r divided by lambda. Arithmetic-geometric mean, or simple calculus, shows that this expression is at least twice the square root of D times r. Thus the leading-edge calculation predicts a minimum admissible speed.

For the classical scalar Fisher–KPP equation on the line, monotone traveling fronts connecting K to zero exist for speeds at least this threshold, and not for smaller positive speeds. Under the standard assumptions for sufficiently localized nontrivial initial data, the long-time invasion selects the minimum speed. That last statement concerns a class of initial-value problems, not every imaginable initial tail: sufficiently slowly decaying initial data can select faster propagation.

The distinction between existence of a whole family of fronts and selection of one speed by initial data is essential. An equation may permit many traveling solutions, while a particular physical preparation chooses only some of them.

## When nonlinear reactions choose the speed

The minimum-speed calculation relies on the behavior near the unstable state zero and on the Fisher–KPP reaction structure. It is not a universal law for moving interfaces.

Consider a bistable reaction instead. Now the reaction has two locally stable constant states, with an unstable state between them. A front can connect the stable states. In that setting, the direction and speed can depend on the signed area under the reaction function between those states.

To see why, multiply the traveling-wave ODE by the derivative of the profile and integrate across the entire front. The diffusion term becomes a derivative of the square of the profile's slope and contributes zero when the slope decays at both ends. The transport term is speed times the integral of the square of the slope, which has a definite sign. The reaction term becomes the integral of the reaction function along the transition between states.

The balance ties the sign of the propagation speed to which stable state has the greater area advantage. If the signed area vanishes, a stationary interface can appear. This calculation shows that the whole nonlinear reaction, not merely the linear growth rate at one end, may determine front motion.

We must not infer front existence from the area identity alone. It is a necessary relation for a sufficiently regular front with the stated limits. Establishing that the corresponding heteroclinic orbit exists requires further dynamical analysis.

## Fronts, pulses, and patterns

Not every traveling wave is a front. A traveling pulse may rise above a background level and return to that same level at both ends. Solitary-wave solutions of dispersive equations provide other examples, often governed by conservation and dispersion rather than reaction and diffusion. Periodic traveling waves repeat a pattern as they move.

The shared mathematical technique is the moving coordinate. The resulting profile equation and the correct boundary conditions determine which of these structures are possible. A pulse is typically a homoclinic-type orbit in profile phase space, while a front corresponds to a heteroclinic connection between distinct equilibria.

This language gives us a way to compare problems that look physically different. The motion of an invasion, a reaction interface, and a concentration pulse may all be investigated through orbits of related dynamical systems, with different source terms and conservation laws.

## What controls the observed front?

The existence of a traveling profile is only the beginning. We must also ask whether nearby profiles stay close, whether perturbations change the speed, whether the medium is homogeneous, and whether an initial condition converges to one of the admissible fronts. A moving front in a finite domain may interact with boundaries; in several spatial dimensions, curvature can alter the propagation law.

For Fisher–KPP propagation, the leading edge gives an unusually informative speed bound. For bistable systems, an energy-type integral identifies the direction of motion. Both calculations reduce a spatial-temporal process to a shape problem, but neither licenses applying its formula outside the specified model.

Traveling waves make an important idea concrete: motion need not mean that the geometry of a solution is changing. Sometimes all the dynamics can be absorbed into translation, leaving a stationary profile whose existence, stability, and speed become questions in ordinary differential equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(u_t=D u_{xx}+f(u)\) on \(\mathbb R\) with \(D>0\), use \(u(x,t)=U(z)\), \(z=x-ct\). Then
\[D U''+cU'+f(U)=0.\]
A **front** has \(U(-\infty)=b\), \(U(+\infty)=a\) for distinct roots \(f(a)=f(b)=0\), and often \(U'\to0\) at both infinities.

**Fisher–KPP:** \(f(u)=ru(1-u/K)\), with \(r,K>0\). For a positive monotone front \(K\to0\), let \(U\sim e^{-\lambda z}\) as \(z\to+\infty\). The characteristic relation is
\[D\lambda^2-c\lambda+r=0,\qquad c=D\lambda+r/\lambda\ge2\sqrt{Dr}.\]
Monotone fronts exist for \(c\ge2\sqrt{Dr}\) and not below. Selection of \(c=2\sqrt{Dr}\) by localized nontrivial data requires the standard Fisher–KPP hypotheses.

**Bistable area identity:** if U connects b on the left to a on the right and \(U',U''\to0\), multiply the profile ODE by U' and integrate:
\[c\int_{\mathbb R}(U')^2\,dz=\int_a^b f(s)\,ds.\]
This identifies the sign of c for a nonconstant front but does not by itself establish existence or stability. For a **pulse**, the two limiting states may coincide instead.

### Exercises with answers

1. For \(D=4\), \(r=9\), what is the Fisher–KPP minimum speed? **Answer:** \(2\sqrt{4\cdot9}=12\).
2. Why does the moving-coordinate ansatz convert a PDE to an ODE? **Answer:** both independent variables enter only through \(z=x-ct\), so \(u_t=-cU'\) and \(u_{xx}=U''\).
3. If \(\int_a^b f(s)ds=0\) and a nonconstant bistable front exists, what is its speed? **Answer:** zero, by the area identity.
4. Does every initial condition select the Fisher–KPP minimum speed? **Answer:** no; selection needs hypotheses on the initial data, especially on its leading-edge decay.

### Reading and source notes

- [Fisher–KPP equation notes](https://mathsbio.com/spatial-mathematical-biology/fisher-kpp-equation/), front ODE and speed calculation.
- Lawrence C. Evans, [*Partial Differential Equations*](https://bookstore.ams.org/gsm-19-r), diffusion-reaction theory and PDE foundations.
- [MIT OpenCourseWare, Nonlinear Dynamics and Chaos](https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/), phase-plane and heteroclinic-connection methods.
