# What Moves with the Flow: Characteristics and Conservation

<!-- BEGIN SPOKEN LECTURE -->

# What Moves with the Flow

Imagine putting a narrow streak of harmless dye into a long channel. The water moves to the right at a fixed speed. For the moment, neglect diffusion: a streak should travel without getting wider, shorter, or paler. If we measure dye concentration at a fixed point, it changes as the streak passes. But if we move beside the streak, the concentration stays constant. This simple difference between observing from the bank and traveling with the water is the starting point of transport equations.

The question is not merely how to write an equation for the moving dye. We want to understand what the equation predicts exactly, what conservation means, and which direction a numerical method must look when it tries to approximate the motion. Those questions will later determine whether a computed pulse travels, smears, or grows into a numerical oscillation.

## Follow the streak, not the fixed sensor

Let q of x and t denote concentration at position x and time t. Suppose the transport speed a is a positive constant, measured in distance per time. A particle that starts at x zero at time zero moves along the path x equals x zero plus a times t. Such a path is called a characteristic.

Along the moving path, we can differentiate the measured concentration using the chain rule. Its rate of change is the time derivative of q plus a times the spatial derivative of q. Our no-diffusion assumption says this sum is zero. In words: the local change seen by a fixed sensor is exactly offset by carrying the concentration profile past that sensor.

We have derived the constant-speed advection equation. Its exact solution is especially informative. If the initial concentration is a profile called q zero, then at time t the concentration at x equals the initial concentration at x minus a times t. Every feature has shifted right by the distance a times t. There is no change of shape.

Suppose the initial concentration is one between positions two and four and zero elsewhere. With speed three, after half a time unit the region of concentration one runs from three point five to five point five. This is true even though the profile has jump discontinuities. In that case the derivatives used to write the equation need interpretation, but the translated profile still satisfies the transport law in the weak, or integral, sense.

A smooth example says the same thing. Begin with a wave whose concentration is one plus half the sine of two pi x. Its peaks and troughs advance through space at speed a. A sensor at a fixed x sees a periodic signal, while a sensor moving with a characteristic sees a constant value. Frequency in time is produced by movement through a spatial pattern; no local oscillator has been introduced.

## What does it mean to conserve dye?

Let us derive the equation a different way. Choose two fixed positions, L and R, and add up all the dye between them. That amount, assuming unit cross-sectional area, is the integral of q from L to R. Dye can enter through the left endpoint or leave through the right endpoint. If the flow speed is a, the transported amount per unit time across a point is a times q. This amount per unit time is called a flux.

The time rate of the amount stored in our interval is therefore the incoming flux at L minus the outgoing flux at R. In symbols we would write the derivative of the integral equal to flux at L minus flux at R. Apply the fundamental theorem of calculus and, for a smooth q, the result is that the time derivative of q plus the spatial derivative of a q is zero.

When a is constant, this conservation form is exactly the advection equation we found by following a streak. But the integral argument is more fundamental in an important sense: it still says what the physical law means when q jumps abruptly and no ordinary derivative exists at the front.

Notice the units. Concentration has units of mass per length in this one-dimensional model. Multiplying by speed gives mass per time. Integrating concentration over a length gives mass. Each side of the balance law is a mass change per unit time. A formula with inconsistent units cannot be the conservation law for this model, however convincing its graph may look.

Imagine dividing the channel into six equal cells. At one instant their average concentrations are zero, zero, one, one, zero, zero. The total concentration multiplied by cell width is the represented dye mass. If the channel is periodic, dye leaving the last cell reenters the first. That total must stay unchanged at every time. A good transport scheme should inherit this conservation law exactly, even though its individual cell values are approximate.

## How boundary data are different from initial data

Now suppose the channel begins at x equals zero and extends to the right. With positive a, information travels into the domain from the left, not from the right. To predict the solution we need an initial profile along the channel and, as time passes, the dye concentration entering at the left boundary.

For a point x and time t, trace its characteristic backward. If the line reaches the initial time before reaching the left boundary, use the initial profile at position x minus a t. If it reaches the inlet first, use the inlet concentration from the earlier time t minus x divided by a. This construction provides a complete solution, subject to matching initial and boundary data at their meeting point when a continuous solution is desired.

It would be a mistake to prescribe an independent arbitrary concentration history at the right boundary as well. The equation transports values out through that endpoint. With a positive speed, the right boundary is an outflow boundary, not another control knob. For a negative speed, the roles reverse. The signs tell us which boundary supplies information.

This directionality also helps explain why numerical transport is different from numerical heat diffusion. A heat equation communicates smoothing information in both spatial directions. Pure advection follows characteristics. Choosing a spatial difference without respecting the sign of the speed can use information from the wrong side of the cell.

## What if the water speeds up?

So far a was constant. Suppose the flow speed increases with position, perhaps because the channel narrows. We must carefully distinguish two equations that looked identical only in the constant-speed case.

One equation says q time derivative plus a of x times q spatial derivative equals zero. It describes a quantity that stays constant along characteristics, with the characteristics satisfying position derivative equals a of x. This is appropriate, for example, for an idealized passive label carried along trajectories without a compression correction.

The other equation says q time derivative plus the spatial derivative of the product a q equals zero. This says the amount of q is locally conserved, including changes caused by convergence or divergence of the flow. Expand the derivative and you get an extra term: a spatial derivative times q. Along a moving characteristic, q now changes at a rate equal to negative a spatial derivative times q.

For a concrete example, take speed a of x equals one plus x on the part of the line where this speed is positive. Characteristics starting at x zero move so that one plus their position grows exponentially with time. Their separation also grows exponentially. Under the conservative equation the concentration along each path decreases like e to the negative t, exactly compensating for the stretching of an infinitesimal length element. Under the nonconservative equation the carried value remains constant. These are not interchangeable models.

To describe incompressible flow in more dimensions, one often takes a velocity field whose divergence is zero. Then the conservative and advective versions coincide for a passive scalar. In one dimension with a single spatial velocity, zero divergence means spatially constant velocity. The simplification we used at the start has a genuine physical assumption behind it.

## When characteristics meet

One more extension reveals why conservation is such a central idea. In some equations the speed itself depends on the transported quantity. For example, consider a flux equal to one half q squared. The conservation equation then says the time derivative of q plus the spatial derivative of half q squared equals zero. In a smooth region, a characteristic moves at speed q.

High-value parts can travel faster than low-value parts. A smooth descending front may steepen until different characteristics attempt to occupy the same location. At that point an ordinary smooth solution cannot continue. A jump, called a shock, may form. The conservation law still determines its speed from the jump in the flux divided by the jump in q. For the quadratic flux this speed is the average of the states on the two sides.

An integral conservation statement is still meaningful across that jump. But it does not, by itself, always select a unique physically relevant weak solution. An additional admissibility or entropy principle is needed. We will not solve nonlinear shock problems in this introductory route; the point is to understand why numerical conservation and choosing the right direction of information matter long before advanced shock theory enters.

## The computational question we have reached

We now know the exact result a numerical method should imitate for constant-speed flow. A pulse must travel with speed a. Its integral must stay constant if no dye crosses the domain boundary. The value at a location is determined by an upstream point, and a positive-speed inlet supplies data while the outlet does not.

Suppose we store only one concentration per grid cell and update it at discrete times. The exact translation may carry a boundary between cells by less than a full cell width. We cannot simply move the entries by an integer number of cells unless the distance traveled during a step happens to equal the cell width. We need to decide how much of each cell's contents crosses its face during the time step.

That leads to a numerical rule with a physical interpretation: take some of the concentration from the upstream cell and leave the rest where it was. The relative amount moved is speed times time step divided by cell width. This dimensionless ratio will be the Courant number. It also tells us how far a characteristic can travel in one time step relative to the resolution of our grid.

The essential distinction is now in place. Diffusion redistributes by smoothing, advection transports by moving, and conservation counts what crosses boundaries. A reliable numerical method needs to respect all three operations when a model contains them. We can begin with the simplest transport update because we already understand exactly what it ought to approximate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: characteristics, flux, and changing speed

For constant speed \(a\),
\[
q_t+a q_x=0,\qquad x(t)=x_0+at,\qquad q(x,t)=q_0(x-at).
\]
The conservative law is
\[
q_t+\partial_x(aq)=0,\qquad
\frac{d}{dt}\int_L^R q(x,t)\,dx=a q(L,t)-a q(R,t).
\]
For \(a>0\) on \(x>0\), inlet data \(g(t)=q(0,t)\) and initial data \(q_0(x)\) yield
\[
q(x,t)=\begin{cases}q_0(x-at),&x\ge at,\\g(t-x/a),&0<x<at.\end{cases}
\]
Continuity at \(x=at\) requires compatibility \(q_0(0)=g(0)\). These formulas also make sense as transported bounded piecewise-continuous data, with the contact point interpreted appropriately.

For a differentiable variable speed \(a(x)\), characteristics satisfy \(x'=a(x)\). Compare
\[
q_t+a(x)q_x=0\quad\Longrightarrow\quad\frac{dq}{dt}=0,
\]
with
\[
q_t+(a(x)q)_x=0\quad\Longrightarrow\quad\frac{dq}{dt}=-a'(x(t))q.
\]
If \(a(x)=1+x\), then \(1+x(t)=(1+x_0)e^t\), and for the conservative law \(q(x(t),t)=q_0(x_0)e^{-t}\).

For Burgers' conservation law \(q_t+(q^2/2)_x=0\), the Rankine–Hugoniot speed across states \(q_L,q_R\) is
\[
s=\frac{f(q_R)-f(q_L)}{q_R-q_L}=\frac{q_L+q_R}{2}.
\]
The entropy condition is essential for selecting admissible shocks; the jump relation alone is not sufficient.

### Exercises with worked answers

1. A pulse initially occupies \([2,4]\) and travels at \(a=3\). Where is it at \(t=1/2\)? **Answer:** \([3.5,5.5]\).
2. For \(a=2\), \(q_0(x)=x\) on \(x>0\), and \(g(t)=3\), calculate \(q(1,1)\) and \(q(4,1)\). **Answer:** \(q(1,1)=g(1/2)=3\), and \(q(4,1)=q_0(2)=2\). The data are not compatible at the initial corner, so a jump is transported from it.
3. Derive the interval mass balance from \(q_t+(a q)_x=0\). **Answer:** integrate on \([L,R]\) and use the fundamental theorem of calculus to get \(dM/dt=(a q)(L)-(a q)(R)\).
4. For \(a(x)=1+x\), why does a conserved concentration decay along a characteristic? **Answer:** the flow stretches lengths by \(e^t\); the concentration must fall by \(e^{-t}\) to conserve amount in a moving segment.
5. Which boundary supplies data for constant speed \(a=-4\) on \([0,1]\)? **Answer:** the right boundary \(x=1\), because characteristics move left.

### Sources and further reading

- [Randall J. LeVeque, *Finite Volume Methods for Hyperbolic Problems*, Cambridge University Press (2002)](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
- [Stanford Math 220A, Conservation Laws](https://web.stanford.edu/class/math220a/lecturenotes.html).
- [LeVeque, Cambridge University Press, Chapter 4: Finite Volume Methods](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
