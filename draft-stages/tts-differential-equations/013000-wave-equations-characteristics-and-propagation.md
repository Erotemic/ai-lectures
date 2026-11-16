# 013000 — Wave Equations, Characteristics, and Finite Propagation Speed

**Track:** Differential Equations and Dynamical Systems. **Background:** PDEs, second derivatives, initial-value problems, energy conservation. **Central question:** why do disturbances in a wave equation travel at finite speed, and what initial data determine a later observation?

<!-- BEGIN SPOKEN LECTURE -->

# Wave Equations, Characteristics, and Finite Propagation Speed

If you pluck a stretched string, the disturbance travels outward. You can watch the pulse move before distant points respond. That behavior differs from the ideal heat equation, where a localized temperature change influences the mathematical solution everywhere immediately, even though the distant influence may be extremely small.

The wave equation captures a mechanism with finite propagation speed. It belongs to the hyperbolic family of partial differential equations. Today we derive its one-dimensional solution, identify its characteristic lines, and use an energy law to explain why the behavior is stable under the right assumptions.

## Where the wave equation comes from

Imagine a thin string held under approximately constant tension and undergoing small transverse displacements. A small piece of string has mass, and the vertical components of tension at its two ends need not balance. Newton's law equates that net transverse force with the mass times acceleration.

For small slopes, the tension contribution is proportional to the difference in slopes across the segment. Dividing by its length and passing to a limit gives an equation where the second derivative in time is a positive constant times the second derivative in position. Write that constant as c squared. Then the wave equation says the acceleration of the displacement equals c squared times its spatial curvature.

The speed c depends on tension and mass per unit length in this simplified string model. Higher tension increases speed; greater mass density reduces it. The derivation also tells us the model's boundaries: large slopes, varying tension, damping, nonlinear material behavior, and bending stiffness can require different equations.

## What must be specified initially?

A second-order time equation requires two pieces of initial data. We must specify the initial displacement f of x, and the initial velocity g of x. These are independent pieces of information. A string can begin straight but already moving, or deformed but momentarily at rest.

The domain also matters. On the whole real line, no endpoint conditions are necessary. On a finite string, boundary conditions at the endpoints affect reflections and standing waves. We will begin with the whole line, where the clearest formula is available.

## Factoring the differential operator

The one-dimensional wave operator can be factored into two first-order operators. One uses the time derivative plus c times the space derivative, and the other uses the time derivative minus c times the space derivative. Because the coefficients are constant, these factors commute, and their product is exactly the wave operator.

This factorization suggests two families of characteristic lines: x minus c times t is constant, and x plus c times t is constant. Along one family information travels to the right; along the other it travels to the left.

If the initial velocity is zero, the solution is particularly simple. Half of the initial displacement travels to the right at speed c, and half travels to the left at speed c. The formula adds f evaluated at x minus c t and f evaluated at x plus c t, then divides by two.

When initial velocity is not zero, there is another term: one divided by twice c, multiplied by the integral of g from x minus c t to x plus c t. Together these terms form d'Alembert's formula. One can verify it by differentiating twice, checking the differential equation, and evaluating the initial displacement and initial time derivative.

## An explicit pulse

Suppose the initial displacement is a smooth localized bump, supported between positions negative one and one, and the initial velocity is zero. At time t the right-moving contribution is supported between c t minus one and c t plus one. The left-moving contribution is supported between negative c t minus one and negative c t plus one.

For sufficiently large time the two pulses no longer overlap. They retain their shapes in the ideal one-dimensional equation, each with half the original amplitude. No point outside the region reached by those traveling supports can respond. The original disturbance has not been smeared instantaneously over the real line.

If the initial velocity is supported in the same interval, its contribution uses an integral over the interval between x minus c t and x plus c t. The full solution is still zero outside the expanding interval from negative one minus c t to one plus c t. The exact geometry of its support inside that interval may differ, but influence cannot outrun speed c.

## Domains of dependence

Ask the question in reverse. What initial information determines the displacement at a given location x and later time t? D'Alembert's formula uses initial displacement only at two points, x minus c t and x plus c t, and initial velocity across the interval joining them. Everything outside that interval is irrelevant to the answer at this point and time.

That interval is the domain of dependence on the initial line. In a space-time diagram, it is the base of a cone bounded by the two characteristics through the observation point. Changes in initial data outside the cone cannot affect that observation in the ideal model.

The word cone remains in higher-dimensional wave equations, where the domain of dependence lies inside a light-cone-like region. The exact shape of the solution inside the region depends on dimension and boundary conditions. Finite propagation speed does not automatically imply a perfectly sharp disturbance located only at the wavefront.

## An energy identity

Wave motion also has a conserved energy. For the whole-line equation with sufficiently regular, decaying data, define the total energy as one-half the integral of velocity squared plus c squared times slope squared. These terms represent kinetic and elastic energy after appropriate normalization.

Differentiate in time. Replace the second time derivative using the wave equation. Integrate the term involving the second spatial derivative by parts. The two interior terms cancel, leaving only a flux contribution at the boundaries. On the whole line, for suitably decaying data, the boundary flux vanishes. Total energy is constant.

This energy law gives more than physical interpretation. It provides an a priori estimate and a uniqueness argument. If two solutions share identical initial data, their difference solves the wave equation with zero initial displacement and zero initial velocity. Its energy remains zero. With the appropriate regularity and normalization, that forces the difference to vanish.

On a bounded interval the boundary flux need not vanish automatically. A fixed-end or reflecting boundary condition can yield energy conservation, while a driven endpoint can inject energy. Damping adds a negative contribution and makes the energy decrease. The equation and the boundary conditions together determine the energy balance.

## Contrast with diffusion

The heat equation is first-order in time and diffuses spatial gradients. Its fundamental solution for positive time has Gaussian tails extending over all space. A compactly supported nonnegative initial temperature distribution that is not identically zero produces a positive temperature everywhere for every positive time on the whole line. The wave equation instead has characteristics and finite propagation.

These are ideal mathematical properties, not claims that actual physical heat signals transmit measurable information instantaneously. Both PDEs arise as approximations under different assumptions. Their contrasting mathematical domains of dependence tell us which questions each model is suited to answer.

Today's result is a complete prototype: a physical balance law leads to a hyperbolic PDE; characteristics lead to an exact solution; the formula identifies a finite domain of dependence; and the energy identity explains stability and uniqueness. These tools will reappear in multidimensional waves, variable-coefficient equations, and numerical hyperbolic solvers.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(\mathbb R\times[0,\infty)\), with \(c>0\), solve
\[u_{tt}=c^2u_{xx},\qquad u(x,0)=f(x),\quad u_t(x,0)=g(x).\]
For \(f\in C^2\) and \(g\in C^1\) with appropriate regularity for the differentiations, d'Alembert's formula is
\[u(x,t)=\frac{f(x-ct)+f(x+ct)}2+\frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds.\]
The operator factors as \((\partial_t-c\partial_x)(\partial_t+c\partial_x)u=0\). The value \(u(x,t)\) depends only on \(f\) at the characteristic endpoints and \(g\) over \([x-ct,x+ct]\). If \(f,g\) vanish outside \([a,b]\), then \(u(\cdot,t)\) vanishes outside \([a-ct,b+ct]\).

For smooth decaying solutions,
\[E(t)=\frac12\int_{\mathbb R}(u_t^2+c^2u_x^2)\,dx,\quad
\partial_t\Bigl(\tfrac12(u_t^2+c^2u_x^2)\Bigr)=c^2\partial_x(u_tu_x),\quad E'(t)=0.\]
On a bounded interval \([a,b]\), \(E'(t)=c^2[u_tu_x]_{a}^{b}\); boundary conditions determine whether the flux vanishes. A zero-energy difference of solutions has \(u_t=u_x=0\), and its initial value zero fixes the additive constant, establishing uniqueness.

### Exercises with answers

1. For \(g=0\) and \(f(x)=e^{-x^2}\), write \(u(x,t)\). **Answer:** \(\tfrac12[e^{-(x-ct)^2}+e^{-(x+ct)^2}]\).
2. At \((x,t)\), which part of the initial velocity can affect the solution? **Answer:** only \(g\) on \([x-ct,x+ct]\).
3. If \(f,g\) are compactly supported, can their influence appear outside the expanding interval at time \(t\)? **No:** d'Alembert's formula makes that impossible.
4. Does the energy identity guarantee conservation for arbitrary driven endpoints? **No:** boundary flux can inject or remove energy.

### Reading and source notes

- MIT OpenCourseWare, [18.303 Linear Partial Differential Equations](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/pages/syllabus/), wave and diffusion equations.
- A. K. Nandakumaran and P. S. Datti, [*One-Dimensional Wave Equation*](https://www.cambridge.org/core/books/abs/notes-problems-and-solutions-in-differential-equations/onedimensional-wave-equation/CCE77FB5DEDBFF85449B7290F61C5A2A), d'Alembert formula and domain of dependence.
- Lawrence C. Evans, *Partial Differential Equations*, second edition (AMS, 2010), energy estimates and hyperbolic PDEs.
