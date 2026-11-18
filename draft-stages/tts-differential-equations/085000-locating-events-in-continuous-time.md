# Locating Events in Continuous Time: Roots, Impacts, and Hybrid Dynamics

<!-- BEGIN SPOKEN LECTURE -->

# Locating Events in Continuous Time

Imagine simulating a ball thrown upward from a balcony. The differential equation determines its changing height and velocity. An adaptive integrator chooses its own sequence of times. But the question we care about is not necessarily the height at those times. We may want to know exactly when the ball hits the ground.

The impact time will almost never coincide with an accepted numerical time step. A solver could produce excellent approximations at one second and two seconds while leaving the collision somewhere between them. If we simply wait until the reported height becomes negative, we have found a late event, not the physical impact. If we pretend the collision occurred at the nearest output point, we may introduce an error much larger than the integrator's trajectory error.

The solution is to treat an event as another mathematical equation. We integrate the differential equation to describe the trajectory, and solve a scalar root-finding problem to locate the event on that trajectory. The two calculations must be coordinated, but they serve different purposes.

## A ground impact with an exact answer

Let the ball start two meters above the ground with an upward velocity of five meters per second. Use a constant downward gravitational acceleration of ten meters per second squared. We choose round numbers to keep the arithmetic visible.

Height changes at the current velocity, and velocity changes at negative ten meters per second each second. Integrating gives height equal to two plus five times time minus five times time squared. Velocity equals five minus ten times time. The ball initially rises; its velocity reaches zero at half a second, when the ball is momentarily at the top of its path. Later, the height decreases.

To find the impact, set height equal to zero. The resulting quadratic has one positive root. It occurs at five plus the square root of sixty-five, all divided by ten seconds: about one point three zero six two seconds. At that moment the velocity is downward and its magnitude is the square root of sixty-five, about eight point zero six two meters per second.

Now suppose a numerical solver gives us accepted states at one second and two seconds. The heights are two meters and negative eight meters. The signs differ, so somewhere in that interval the continuous height must be zero, assuming it varies continuously. The interval *brackets* the impact.

A crude linear interpolation of the endpoint heights predicts an impact at one point two seconds. That is closer than simply choosing one or two seconds, but it is still about a tenth of a second early. A more accurate continuous approximation to the trajectory can do better. For constant acceleration, a quadratic interpolant built from consistent position and velocity information recovers the exact impact time. For a general numerical method, the interpolant is approximate and has an error of its own.

The lesson is that event time is a root of a function, not merely a time-step label.

## The event function

For a ground impact, define an event function whose value is the height above the ground. The event occurs when that function is zero. Other event functions are possible. A chemical reaction may stop when a concentration crosses a threshold. A pendulum may complete a swing when its angular displacement passes zero in a chosen direction. An orbital calculation may record closest approach when the radial velocity becomes zero, although that zero must be distinguished from the opposite kind of turning point.

Each case reduces to a scalar function of time and the evolving state. The integration method approximates the state, and the event detector watches the scalar function. If consecutive accepted endpoints have opposite event-function signs, a root is bracketed. A root-finding algorithm then uses a continuous approximation of the state inside the step to narrow the interval.

This leads to a practical question: where does the approximate state inside the step come from? A modern Runge–Kutta solver may build a polynomial continuous extension using the same intermediate stages employed in the step. This is called *dense output*. It is more useful than drawing a straight line between stored endpoints, especially when the trajectory is curved. Other integrators construct their own continuous extensions or interpolants.

Dense output does not grant perfect knowledge between endpoints. Its order and smoothness must be considered, and any event time extracted from it inherits approximation error. Nonetheless, it lets a solver locate events without forcing a tiny fixed output grid over the entire simulation.

## Direction matters

Our ball passes through a horizontal height twice if the threshold lies below its peak and above its starting position: once going up and once coming down. If our event is an impact with the ground, only a downward crossing is physical. A good detector can be configured to recognize crossings from positive height to negative height, ignoring the opposite direction. For an orbital periapsis, the relevant radial-velocity crossing similarly distinguishes inward motion turning outward from outward motion turning inward.

Direction information avoids some false events, but it does not solve every detection problem. If an event function crosses zero twice within one large step, its values at both endpoints can have the same sign. A sign-change detector will miss both crossings. If the function touches zero tangentially and turns back without changing sign, it may miss that zero too.

For a simple example, consider an event function that equals time minus one multiplied by time minus two. It crosses zero at one second and again at two seconds. At time zero it is positive, and at time three it is also positive. A single attempted step from zero to three shows no endpoint sign change, although two events occurred within it. Another event function equal to the square of time minus one touches zero at one second but is never negative. Endpoint signs cannot reveal that tangency.

A solver may need shorter steps, analytical information about the event, specialized root searches, or a different event function. No generic sign-change algorithm is guaranteed to detect every zero of an arbitrary function.

## What happens after impact?

Finding the impact is only the first half of a bouncing-ball model. At the event time the trajectory undergoes a rule that the smooth flight ODE does not describe. A simple bounce model keeps the height at zero and reverses the velocity, multiplying its magnitude by a coefficient of restitution between zero and one. The ball loses kinetic energy at each impact unless the coefficient equals one.

Suppose the coefficient is zero point eight. Just before our first impact, velocity is negative square root of sixty-five. Immediately after, velocity is positive zero point eight times square root of sixty-five, or about six point four five meters per second upward. The flight equations resume from height zero with that new upward velocity. In the same idealized constant-gravity model, the time until the next impact is twice that upward speed divided by ten, about one point two nine seconds after the bounce.

We must not let a smooth ODE integrator silently continue through the impact with the pre-impact velocity. Doing so sends the ball underground. Nor should we modify the velocity at the beginning or end of the enclosing accepted step. The jump belongs at the located event time. A sound numerical algorithm stops there, records the pre-impact state, applies the jump rule, and restarts the integration with the post-impact state.

This combination of continuous evolution and discrete updates is called a *hybrid dynamical system*. The same pattern appears in switching circuits, contact mechanics, threshold-triggered control, and models with abrupt changes in policy or operating mode. The discontinuity is not a small perturbation to be absorbed by local truncation error. It is part of the equation's definition.

## A difficulty with many fast events

Consider a ball that loses speed at each ideal bounce. Bounce intervals become shorter and shorter. In the simplest perfectly rigid point-impact model with a restitution coefficient strictly between zero and one, the sum of those intervals can converge to a finite time. In mathematical terms, infinitely many bounce events may accumulate in finite time. This is often called *Zeno behavior* in hybrid systems.

No ordinary event loop can process an actual infinity of discrete updates. A physical model must eventually incorporate resting contact, compliance, friction, or another mechanism that resolves the idealization. A numerical implementation might declare the ball settled below an appropriate velocity threshold and change to a resting-contact model. The threshold and rule should be justified by the physical question, not concealed as an arbitrary emergency patch.

Events can also occur near a derivative discontinuity, like a switch that turns a heater on or off. A robust model treats a known switch time as a boundary between integrations. If a switching condition is state-dependent, event detection locates it; then the model changes branch and the solver restarts. The continuous extension from the *old* dynamics should not be used indiscriminately after the switch.

## Event accuracy is a separate question

Suppose you need the projectile's impact time accurate to one millisecond. That is an event-time requirement. A solver tolerance that keeps the height estimates within one centimeter does not automatically guarantee the impact time to a millisecond. Near a transverse crossing, a height error divided by the magnitude of downward velocity gives a rough impact-time error. If the ball is moving downward quickly, a small height error shifts the root only a little. If it barely touches a surface, the same height error may shift the apparent contact time dramatically or even change whether contact is detected.

This connects numerical analysis with geometry. A transverse root is well conditioned when the event function changes rapidly through zero. A tangential root is more sensitive. Improving local trajectory accuracy helps, but the conditioning of the event equation matters too.

There are therefore two convergence tests worth performing when an event is central. Tighten the integration tolerances and see whether the event time settles. Then, if possible, compare with an independent root calculation or physical invariant. For our constant-acceleration ball, the quadratic formula supplies the exact benchmark. In more complex models, one might compare event times computed by methods of different orders or monitor the event residual and crossing direction.

## The principle

A differential equation tells us how the state changes until an event. An event function tells us when a particular condition is met. A jump or switching rule tells us what happens next. These are three different pieces of a mathematical model, and keeping them separate makes a numerical simulation more trustworthy.

Adaptive integration can follow the smooth trajectory efficiently. Dense output and root finding can locate events between accepted steps. Explicit transition rules can then handle collisions or switching without hiding discontinuities inside an ordinary derivative calculation. Once we understand those roles, event-driven simulations stop being a bag of special cases: they become ordinary differential equations linked by precise mathematical conditions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: event roots and jump maps

For \(y'=v,\ v'=-10\), \(y(0)=2\), \(v(0)=5\),
\[
 y(t)=2+5t-5t^2,\qquad v(t)=5-10t.
\]
The positive ground-impact root is
\[
 t_* = \frac{5+\sqrt{65}}{10}\approx1.3062257748,\qquad
 v(t_*)=-\sqrt{65}\approx-8.0622577483.
\]
At \(t=1\), \(y=2\); at \(t=2\), \(y=-8\). Secant interpolation yields \(t_{\mathrm{lin}}=1+2/(2+8)=1.2\). The precise event time is found by solving \(g(t,y(t))=0\) on a continuous extension of the trajectory, rather than simply choosing a stored endpoint.

An impact with restitution \(e\in[0,1]\) has jump map
\[
(y^+,v^+)=(0,-e v^-), \quad v^-<0.
\]
With \(e=0.8\), \(v^+=0.8\sqrt{65}\approx6.4498061986\) and the next flight duration is \(\Delta t=2v^+/10\approx1.2899612397\).

If a smooth event function \(G(t)=g(t,y(t))\) has a simple root \(t_*\) with \(|G'(t_*)|\ge m>0\) in a neighborhood, a small perturbation \(\delta G\) produces a first-order root perturbation \(\delta t_*\approx-\delta G(t_*)/G'(t_*)\). This sensitivity relation does not apply with a finite condition number at a tangency \(G'(t_*)=0\).

### Exercises and worked answers

1. Verify the two endpoint heights used in the secant example. **Answer:** \(y(1)=2\), \(y(2)=-8\).
2. Show why an event function \(G(t)=(t-1)(t-2)\) may be missed by a step from zero to three. **Answer:** both endpoint values equal two; the function crosses zero twice in between.
3. Give an event whose zero has no sign change. **Answer:** \(G(t)=(t-1)^2\) touches zero at one second and remains nonnegative.
4. Find the upward speed after a bounce with \(e=1/2\) in the projectile example. **Answer:** \(\sqrt{65}/2\) meters per second.
5. Why is a rigid collision modeled as a jump instead of a smooth acceleration in this idealization? **Answer:** the ideal contact changes velocity instantaneously; an ordinary finite smooth acceleration law would require a finite contact interval or different contact model.

### Sources and further reading

- [SciPy `solve_ivp`: events, terminal conditions, crossing direction and dense output](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
- [Wikipedia: Hybrid system](https://en.wikipedia.org/wiki/Hybrid_system).
- [Wikipedia: Event detection for differential equations](https://en.wikipedia.org/wiki/Event_detection).
