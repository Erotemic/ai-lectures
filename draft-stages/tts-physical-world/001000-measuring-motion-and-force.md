# 001000 — How Can Motion Become a Law? Measurement, Models, and Forces

**Track:** The Physical World. **Background:** arithmetic, algebra, coordinate graphs. **Purpose:** learn to turn observations of motion into conditional, testable laws; distinguish a measurement from a model and a force from a velocity.

<!-- BEGIN SPOKEN LECTURE -->

# How Can Motion Become a Law? Measurement, Models, and Forces

Imagine two people watching the same cart roll across a floor. One says, “It was fast at first, and then it slowed.” The other starts a stopwatch, measures how far the cart traveled, and records its position at a series of times. Both have watched something real. But only the second has produced a record from which somebody else could test a quantitative prediction.

Physics starts with an act of selection. The real cart has scratches, uneven wheels, a temperature, a material history, and thousands of details. For a first model of motion we may care about its position, the time, its mass, and the forces acting on it. A good model is not a complete miniature of reality. It is a deliberately incomplete description that answers a stated question and makes itself vulnerable to measurements.

Suppose we place a strip of tape alongside a smooth track, mark distances in meters, and use a timer. We release a cart and record positions at equal time intervals. This is a proposed classroom experiment, not a report of measurements I have personally made. We might find positions of zero meters at zero seconds, one meter at one second, four meters at two seconds, and nine meters at three seconds. These invented numbers were chosen because their pattern is easy to inspect. They do not establish a physical law on their own.

Notice what makes this record different from “the cart sped up.” The first one-second interval covers one meter, the second covers three, and the third covers five. Its average speed over each interval increases. A rule that fits the four chosen observations is that position in meters equals the square of elapsed time in seconds, multiplied by an acceleration coefficient of one meter per second squared. If we want a rule capable of describing more than these four points, we must specify a time origin, a direction, and the conditions under which the rule applies.

The expression “meters per second squared” may sound peculiar. It is not distance divided by seconds and then squared. Acceleration means change in velocity per unit time. If a cart gains two meters per second of velocity every second, its acceleration is two meters per second per second. The seconds in the denominator appear twice because a change in a rate is itself being measured over time. In our invented position record, the smooth model gives the cart an acceleration of two meters per second squared and an initial speed of zero. At the end of two seconds its instantaneous speed would be four meters per second. Its average speed across the whole two-second interval is only two meters per second. These are different questions.

This distinction is worth holding onto. Position says where. Velocity says how fast and in which direction position is changing. Acceleration says how velocity changes. If a ball moves in a circle at constant speed, its velocity still changes continuously because its direction changes. It is accelerating even if the number on a speedometer stays fixed. Speed has no direction; velocity does.

A graph helps us read this without memorizing an enormous list of formulas. Plot position vertically and time horizontally. The steepness of a position-versus-time curve tells us velocity. Plot velocity against time instead, and the steepness tells us acceleration. A horizontal line on the velocity graph means constant velocity, not rest. A zero velocity at one instant does not imply zero acceleration: at the highest point of a ball tossed straight upward, its instantaneous vertical velocity is zero but gravity still acts downward.

Now return to the cart. If the floor has friction, the cart gradually stops. Does that mean motion needs force to persist? In everyday life, it can feel that way, because pushing and pedaling are often needed to overcome resistance. Newton's first law gives us a different starting point: in an inertial frame, an object with no net external force moves with constant velocity. The cart slows not because a mysterious supply of motion is running out, but because contact forces and air resistance alter its velocity.

The qualification “in an inertial frame” matters. A passenger in a turning car feels drawn sideways, but the car is an accelerating reference frame. To use the simple Newtonian law, we either analyze from a sufficiently inertial frame or account carefully for the apparent forces introduced by the accelerating frame. Even Earth's surface is only approximately inertial, and the approximation must be reconsidered for sensitive experiments or large-scale motions.

The law about forces is more specific than “push harder, go faster.” For a body of approximately constant mass at ordinary speeds, the net external force equals mass times acceleration. If a total net horizontal force of six newtons acts on a three-kilogram cart, the acceleration is two meters per second squared. If that same force acts on a six-kilogram cart, the acceleration is one meter per second squared. Notice the units: a newton is a kilogram times a meter per second squared. Force is not measured in kilograms; kilograms measure mass. Weight near Earth's surface is a force and is measured in newtons.

A useful check follows immediately. Suppose you calculate that a three-kilogram cart with a six-newton net force accelerates at eighteen meters per second squared. Multiplying mass by force has the wrong units for acceleration. Dividing force by mass gives newtons per kilogram, which simplifies to meters per second squared. A unit check cannot prove that your arithmetic or model is correct, but it can reject many answers before you trust them.

Forces must also be added as directions, not merely as positive numbers. Imagine two people pull the same cart horizontally, one to the right with six newtons, the other to the left with four. If friction is negligible, the net force is two newtons to the right. Treating the magnitudes as ten newtons would predict the wrong direction and the wrong acceleration. If the pulls are equally strong and opposed, the net force is zero even though both people exert forces. Zero net force permits constant velocity as well as rest.

Newton's third law is often misunderstood in the same way. When a cart pushes on a wall, the wall pushes back on the cart with an equal and opposite force. Those paired forces do not cancel in the cart's equation of motion, because they act on different objects. To know the cart's acceleration, we add forces acting on the cart. To know the wall's acceleration, we add forces acting on the wall. A statement about an interaction is not a license to combine the force diagrams of different bodies.

How did such ideas become established? In the early modern period, Galileo studied falling bodies and motion on inclined planes. The incline made certain changes slower and easier to examine than free fall. His work linked mathematical patterns with actual physical questions, though we should not imagine a modern laboratory with perfect timers or pretend that every account of a famous experiment is a confirmed eyewitness record. Historians reconstruct the development from his published works, manuscripts, instruments, and the practices of his time. Newton later combined terrestrial and celestial dynamics into the laws articulated in his 1687 Principia. That synthesis was powerful; it was not an instantaneous discovery by a single person outside earlier traditions of mathematics and astronomy.

Let's design a better cart experiment than the four invented points. First, choose a question: does acceleration remain roughly constant down a fixed incline? Second, choose a measurement method. Modern video tracking can record positions against a calibrated scale, but the frame rate and scale introduce uncertainty. Third, take enough measurements to compare a curved position graph with the predicted constant-acceleration relation. Fourth, vary the incline angle or the cart's mass while keeping other conditions as controlled as practical. Finally, inspect deviations instead of deleting them because they spoil a neat curve.

You will need an uncertainty statement. Suppose each video position estimate is uncertain by two millimeters. If the cart moves one meter between widely separated frames, the position uncertainty may be relatively small. If it moves only one millimeter between adjacent frames, subtracting two uncertain positions may make a velocity estimate nearly meaningless. The best measurement procedure depends on the scale of the effect you hope to resolve. More decimal places in a spreadsheet do not make a measurement more precise.

There are other ways a plausible formula can fail. A constant-acceleration model may work on a short, nearly straight section of track but not when the cart hits a cushion. A point-particle model describes where the cart is but may fail to predict its rotation or tipping. Newtonian mechanics gives excellent results for many ordinary objects, but for velocities approaching light speed or for very small quantum systems, we need broader theories. Saying this does not make Newton's laws useless. It makes their range of reliable use part of the knowledge.

Models also make counterfactual predictions. If the net horizontal force is genuinely zero, a cart will not steadily gain horizontal velocity in an inertial frame. If the calculated acceleration depends on our choice of whether to call right positive or negative, rather than simply changing sign with the coordinates, we have made an error. If doubling the cart's mass while holding a fixed net force doubles its acceleration, we have contradicted the constant-mass model rather than confirmed it.

What turns an observation into a law, then? Not the prestige of an equation and not a tidy plot. We define quantities that other observers can measure; record how measurements are made; propose a mathematical relationship with assumptions; draw predictions that might turn out false; and compare those predictions with further observations. When a prediction misses, we ask whether our apparatus, our interpretation, or the proposed law needs revision.

The cart is still rolling on its track. We can describe its position, explain the change in its velocity, and estimate what forces are acting. But even a good motion model leaves another question unanswered. When the cart stops, its kinetic energy has not simply disappeared. To investigate that, we must learn to count transformations that go beyond motion itself. The same discipline of measurement and boundary-setting will carry us from force to work, heat, and energy.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Coordinates and kinematics.** For one-dimensional motion at constant acceleration,
\[
 x(t)=x_0+v_0t+\frac12 at^2,\qquad v(t)=v_0+at.
\]
The example \(x=t^2\,\mathrm{m}\) with \(t\) in seconds has \(v_0=0\) and \(a=2\,\mathrm{m/s^2}\). Position samples at \(t=0,1,2,3\) seconds yield \(x=0,1,4,9\) meters. These are **hypothetical model values**, not historical measurements.

**Forces and units.** In an inertial reference frame and for constant mass, \(\sum \mathbf F=m\mathbf a\). One newton equals one kilogram-meter per second squared. \(6\,\mathrm N / 3\,\mathrm{kg}=2\,\mathrm{m/s^2}\).

**Uncertainty and numerical differentiation.** If each of two independently measured positions has a standard uncertainty \(\sigma_x\), the difference has approximate standard uncertainty \(\sqrt2\sigma_x\); dividing by \(\Delta t\) gives a velocity-difference uncertainty \(\sqrt2\sigma_x/\Delta t\). This approximation assumes independent, unbiased errors and known time separation.

### Exercises with answers

1. A cart travels two meters in one second, then four meters in the next. Are its instantaneous accelerations determined? **No:** two interval averages do not uniquely determine a velocity function or acceleration.
2. A 2 kg body has rightward force 10 N and leftward force 6 N. Find its horizontal acceleration, neglecting other horizontal forces. **Answer:** \((10-6)/2=2\,\mathrm{m/s^2}\) rightward.
3. A ball tossed vertically upward has zero vertical velocity at the apex. Does its acceleration vanish? **No:** neglecting air drag, the acceleration is approximately \(-g\) throughout flight near Earth.
4. In a video experiment, why might estimating velocity from frames very close in time be unreliable? **Because** subtracting uncertain positions and dividing by a tiny time interval can amplify measurement noise.

### References

- Stanford Encyclopedia of Philosophy, “Galileo Galilei”: https://plato.stanford.edu/entries/galileo/
- Stanford Encyclopedia of Philosophy, “Newton’s *Principia*”: https://plato.stanford.edu/entries/newton-principia/
- OpenStax, *University Physics Volume 1*, chapters on motion and Newton’s laws: https://openstax.org/details/books/university-physics-volume-1
- NIST, “Definitions of SI Base Units”: https://www.nist.gov/si-redefinition/definitions-si-base-units
