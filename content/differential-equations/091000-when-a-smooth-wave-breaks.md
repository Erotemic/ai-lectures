# When a Smooth Wave Breaks: The First Nonlinear Conservation Law

<!-- BEGIN SPOKEN LECTURE -->

# When a Smooth Wave Breaks

Imagine a long channel, viewed from the side. A hump of some transported quantity is moving to the right. The quantity might represent a velocity, a concentration in a simplified model, or another state that affects its own rate of transport. The front of the hump is steepening. Sooner or later a graph that began as a smooth hill appears to acquire a nearly vertical front.

That is a puzzle if we think of differential equations as instructions for producing smooth curves. Nothing has struck the wave. There is no external switch at the instant of steepening. The change comes from the equation itself: the transport speed depends on the value being transported.

We have already studied ordinary advection, where a fixed speed carries every point of a profile the same distance. Here we will take one step beyond it. Our model is Burgers' equation without viscosity. It is simple enough to solve along characteristic curves, yet it forces us to confront one of the central questions of partial differential equations: what should a solution mean after the classical derivatives cease to exist?

## When the cargo determines its own speed

For linear transport, the equation says that the time derivative of a quantity plus a fixed speed times its spatial derivative is zero. Follow a point moving at that speed. The quantity stays constant along its trajectory. Every characteristic line in the position–time plane has the same slope, so parallel trajectories remain parallel.

Burgers' equation changes only one ingredient. Instead of a fixed speed, use the value of the unknown itself. In smooth regions, the equation reads: the time derivative of u plus u times its spatial derivative equals zero. If u is two at some point, that part of the profile moves at speed two. If u is one, it moves at speed one. In this model the height of the graph is also its characteristic speed.

Along a characteristic, the value of u stays constant. Suppose the characteristic starts at position xi, where the initial value is u nought of xi. Its position at time t is xi plus t times that initial value. This is an explicit formula. To find u at a later position, trace the position back to its initial xi and read the unchanged initial value.

Try a simple decreasing stretch of initial data: u nought of xi equals one minus xi, for xi between zero and one. At the left end the value and speed are one; at the right end both are zero. The characteristic from xi equals zero travels along x equals t. The characteristic from xi equals one stays at x equals one. Intermediate characteristics travel along x equals t plus one minus t times xi.

At time one half, the original unit interval of initial positions has been compressed into a spatial interval only half as wide. At time nine tenths it has been compressed to one tenth of its initial width. At time one every one of those characteristics meets at position one. Beyond that time the naive characteristic formula would assign several different values of u to a single position. A classical, single-valued solution cannot continue by simply letting the characteristics pass through one another.

The problem is not that the value of u has become infinite. Its values can remain perfectly bounded between zero and one. The spatial slope is what becomes infinite in magnitude. On this linear initial stretch the slope is negative one divided by one minus t. As time approaches one from below, the denominator approaches zero. The graph steepens without bound.

This is finite-time gradient blow-up. It can occur while the transported quantity itself stays small and while the equation looks innocent compared with many physical models.

## The hidden conservation law

There is a second way to write Burgers' equation, and it matters enormously. For smooth u, the product u times its spatial derivative is the spatial derivative of one half u squared. So Burgers' equation is a conservation law: the time derivative of u plus the spatial derivative of the flux equals zero, where the flux is one half u squared.

The distinction between these two forms is invisible as long as u is differentiable. It becomes decisive at a jump. A discontinuous function does not possess an ordinary derivative at its jump, so multiplying its derivative by its discontinuous value is not straightforward. But the conservation statement still makes sense in an integrated form.

Take a fixed interval of the channel. Its stored amount of u is the integral over that interval. The rate of change of the stored amount equals the flux entering at the left end minus the flux leaving at the right end. That statement requires values of the flux at the ends, not a derivative at every interior point. It survives the appearance of a discontinuity.

Why insist on this form? Imagine a numerical algorithm that quietly creates a little u whenever a sharp front crosses a grid boundary. It might still draw a plausible picture of a moving wave, but it would not describe the original conservation law. We need a solution concept and a numerical method that agree on the amount transported, not just on the apparent direction of a front.

The integral law also tells us how a moving jump can behave. Picture a left state of two and a right state of zero. A sharp front separates them. The flux just left of the front is two; the flux just right is zero. For the balance to hold, the front must move to the right at speed one. If the front moved at speed two, it would sweep through too much stored material relative to the change in flux. If it stood still, the storage balance would also fail.

The precise speed follows by balancing a tiny moving control volume around the jump. It is the change in flux divided by the change in state. For the quadratic Burgers flux, this reduces to half the sum of the left and right states. Thus the jump from two to zero travels at speed one, intermediate between the characteristic speed two on its left and speed zero on its right.

## Compression is different from expansion

Now reverse the data. Put zero on the left and two on the right. The left characteristics stand still, and the right characteristics move at speed two. They diverge. There is room for intermediate values to fill the widening gap, rather than pressure for the two states to collapse into a single jump.

At positive time the physically selected solution is a spreading fan. To the left of position zero the solution remains zero. To the right of position two times t it remains two. Between these lines the solution is x divided by t. At each point of the fan, the local speed u equals x divided by t, exactly the speed of the characteristic ray through that point.

The formula is elementary, but its significance is not. We have found two very different responses to a jump in initial data. A downward jump produces a compressive shock; an upward jump produces a rarefaction fan. These are not choices made according to how pretty a plotted graph looks. They follow from characteristic geometry and an admissibility principle that we will make precise.

There is a temptation to use the jump-speed formula in both cases. It would assign a shock speed of one even for the upward jump. Surprisingly, that traveling jump does obey the integrated conservation law. So conservation alone will not determine which weak solution is physically relevant. We need another criterion.

One motivation comes from adding a small amount of viscosity. The viscous equation has an extra positive multiple of the second spatial derivative. It smooths steep fronts and prevents literal crossings of smooth characteristic curves. We can solve with positive viscosity and then imagine taking that coefficient toward zero. For compressive data the smooth transition layer becomes thin and approaches a shock. For expansive data it spreads into a fan. This procedure is called vanishing viscosity, and it selects the entropy solution in the scalar Burgers problem.

The word entropy here has a mathematical role even when we are not describing thermodynamic heat. It rules out a conserved but inadmissible moving jump. We will derive a test for it with ordinary algebra.

## A smooth wave is not the same as a weak wave

We should keep three statements separate. First, the characteristic construction solves the equation wherever it remains smooth. Second, a weak solution satisfies the conservation balance even if it has jumps. Third, an entropy solution is a weak solution satisfying an additional inequality that selects the physically appropriate direction of shocks and rarefactions.

Those distinctions are essential when designing a finite-volume algorithm. If an algorithm updates cell amounts by differences of a single shared face flux, it can conserve exactly. But conservation by itself does not guarantee that the method chooses the entropy solution. The choice of what happens at a face must respect whether the local wave is compressive or expansive.

The next practical question is therefore no longer how to draw a characteristic through an arbitrary point. We need to learn how to solve the tiny initial-value problem posed at a single interface between two constant states, and how to decide whether that interface produces a shock or a fan. That small problem will become the building block of a numerical solver on an entire grid.

Before leaving the smooth calculation, notice its value as a diagnostic. If the initial profile has a negative spatial slope, faster values behind slower values can catch them. The steepening time is tied to that initial slope. The numerical grid is not responsible for the sharp front; the continuous model predicts it. A useful numerical method must handle the front without inventing oscillations or violating conservation.

We began with an elementary formula for motion along straight lines. It led us to a finite-time failure of classical differentiability, an integrated conservation law, a shock speed, and a spreading fan. Each step came from taking the original differential equation seriously, including the point at which its familiar derivative-based form stopped being adequate.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: characteristics, shock formation, and a moving jump

Let
\[
u_t + \bigl(f(u)\bigr)_x=0,\qquad f(u)=\frac{u^2}{2}.
\]
For smooth solutions this is \(u_t+u u_x=0\). Along \(x=x(t)\), take \(x'=u\), so \(d u(x(t),t)/dt=u_t+x'u_x=0\). Initial label \(\xi\) gives
\[
x(t;\xi)=\xi+t u_0(\xi),\quad u(x(t;\xi),t)=u_0(\xi),\quad
\partial_\xi x=1+t u_0'(\xi).
\]
Implicit differentiation gives the exact smooth gradient
\[
u_x(x(t;\xi),t)=\frac{u_0'(\xi)}{1+t u_0'(\xi)}.
\]
If \(u_0(\xi)=1-\xi\) on \(0\le\xi\le1\), then \(x=t+(1-t)\xi\) and \(u_x=-1/(1-t)\) for \(0\le t<1\). For globally defined smooth data this formula is valid along the selected initial interval until another part of the data interferes; we are not prescribing the nonsmooth linear profile globally.

For a jump \(u_L\) (left) to \(u_R\) (right) moving at speed \(s\), conservation across a moving small interval yields the **Rankine–Hugoniot condition**
\[
s[u]=[f(u)],\qquad [u]=u_R-u_L,\quad [f]=f(u_R)-f(u_L).
\]
For Burgers, \(s=(u_L+u_R)/2\). The entropy shock occurs for \(u_L>u_R\). For \(u_L<u_R\), the rarefaction is
\[
u(x,t)=\begin{cases}u_L,&x/t<u_L,\\x/t,&u_L\le x/t\le u_R,\\u_R,&x/t>u_R,\end{cases}\qquad t>0.
\]
The physical flux at a cell interface is not necessarily \(f(u_L)\) or \(f(u_R)\): a transonic rarefaction takes the sonic state \(u=0\) at \(x/t=0\).

For viscous Burgers \(u_t+(u^2/2)_x=\varepsilon u_{xx}\), a traveling profile \(u(x,t)=U(x-st)\) with end states \(u_L>u_R\) satisfies, after one integration,
\[
\varepsilon U'=\frac{(U-u_L)(U-u_R)}2,
\]
with \(s=(u_L+u_R)/2\), so \(U'<0\) between the end states.

### Exercises with worked answers

1. If \(u_0'(\xi)=-2\) along some interval, when can its smooth characteristic map first lose invertibility? **Answer:** at \(t=1/2\), because \(1+t(-2)=0\).
2. A Burgers jump has \(u_L=3\) and \(u_R=1\). Find its conservative speed. **Answer:** \(s=(3+1)/2=2\).
3. A Burgers Riemann problem has \(u_L=0\), \(u_R=2\). What is \(u(1,1)\)? **Answer:** one, in the interior of the rarefaction fan.
4. Why do the smooth forms \(u_t+u u_x=0\) and \(u_t+(u^2/2)_x=0\) cease to be interchangeable naively at a jump? **Answer:** a discontinuous multiplier times a distributional derivative is not canonically defined, while the divergence form has an integrated weak meaning.
5. Does the Rankine–Hugoniot condition by itself rule out an upward shock? **Answer:** no; it enforces conservation but not entropy admissibility.

### Sources and further reading

- [LeVeque, Ketcheson and del Razo, *Riemann Problems and Jupyter Solutions*: Burgers' Equation](https://www.clawpack.org/riemann_book/html/Burgers.html).
- [Stanford Math 220A, conservation-law lecture notes](https://web.stanford.edu/class/math220a/lecturenotes.html).
- [Wikipedia: Burgers' equation](https://en.wikipedia.org/wiki/Burgers%27_equation).
