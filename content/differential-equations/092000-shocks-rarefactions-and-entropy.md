# Shocks, Rarefactions, and the Entropy Test

<!-- BEGIN SPOKEN LECTURE -->

# Shocks, Rarefactions, and the Entropy Test

There is a tiny problem that appears again and again in nonlinear wave calculations. Imagine a straight line, with one constant state to the left of the origin and another constant state to the right. At time zero, the two states meet at a jump. What happens immediately afterward?

This is called a Riemann problem. It is not the same as the integral in a calculus course that also carries Riemann's name. It is an initial-value problem for a conservation law with piecewise constant data. The simplicity is deliberate: the two values let us resolve the wave pattern without having to solve a complicated initial profile all at once.

For Burgers' equation, the answer can be found using the characteristic speed and a conservation calculation. More importantly, it teaches us to distinguish conservation from entropy admissibility. Both are needed if we want a numerical solution to represent the intended equation.

## An interface viewed under a microscope

Set the left state to three and the right state to one. In the smooth regions, each left characteristic travels at speed three and each right characteristic at speed one. The faster characteristics behind the jump approach the slower ones ahead. The jump is compressive.

Suppose the jump moves along a straight line with speed s. The amount stored to its left and right is changing as the jump sweeps through space. Apply conservation to a small interval enclosing the jump. The net influx must equal the rate of change of the stored amount. When the width of that interval shrinks, this balance requires s times the change in state to equal the change in flux.

That is the Rankine–Hugoniot condition. For Burgers' flux, one half u squared, it simplifies to s equals one half the sum of the two states. With left value three and right value one, the front moves at speed two. At time one half it has reached position one. Behind it the value is three; ahead it is one. The front's speed lies between the characteristic speeds three and one, so characteristics enter it from both sides in the appropriate moving frame.

A discontinuous front may sound like an approximation to a steep but continuous wave. In inviscid conservation laws it is often the exact form of the relevant weak solution. It has a sharply defined position and speed. What fails is the classical pointwise derivative across that position, not the integral conservation law.

## Why one balance law is not enough

Reverse the states. Set the left value to one and the right to three. The same jump-speed calculation gives speed two, and a discontinuity moving at speed two obeys Rankine–Hugoniot. But its characteristics run away from it: the left state moves at speed one, more slowly than the putative front, while the right state moves at speed three, more quickly. In the moving frame, material spreads away from the discontinuity instead of feeding into it.

We can produce a different solution from the same initial data: a fan filling the gap. At time t, the left state occupies positions left of t and the right state occupies positions right of three t. Inside, the value is position divided by time. At position two t the value is two. Every value in the interval from one to three travels along a characteristic ray with that same speed.

This fan is continuous for every positive time, with corners at its two edges. It also satisfies conservation in the weak sense and has the proper initial left and right states. We therefore have a genuine ambiguity if we only ask for weak solutions.

The extra requirement is called entropy admissibility. For strictly convex Burgers flux, a shock is admissible only when the left state exceeds the right state. If the left state is smaller, the admissible solution is the rarefaction fan. We can understand that rule geometrically, but there is also an inequality that we can calculate.

## An entropy inequality with numbers

For the Burgers equation, choose an entropy density equal to one half u squared. In smooth solutions, multiply the equation by u. The result becomes another conservation equation: the time derivative of one half u squared plus the spatial derivative of one third u cubed equals zero.

Across an admissible discontinuity, that second equality becomes an inequality. The entropy density can be dissipated by a shock; it may not spontaneously increase by concentrating an expanding fan into a sharp front. In words, the time rate of entropy density plus the spatial divergence of its entropy flux must be nonpositive in the distributional sense.

Let's calculate rather than merely quote the rule. Take a downward shock from two on the left to zero on the right. Its speed is one. The entropy density drops from two to zero, a change of negative two. The entropy flux drops from eight thirds to zero, a change of negative eight thirds. The jump contribution to the entropy balance is the change in entropy flux minus shock speed times the change in entropy density. That equals negative eight thirds plus two, or negative two thirds. It is nonpositive, so the shock passes the entropy test.

Reverse the states: zero on the left, two on the right. The hypothetical sharp front still moves at speed one and still conserves u. But the entropy contribution becomes positive two thirds. It fails the inequality. The correct entropy solution is the fan, not that expanding shock.

The algebra illustrates a general warning. It is possible to satisfy the equation's weak conservation balance and nevertheless obtain the wrong weak solution. A computational scheme should not be judged only by whether it conserves the total sum on a grid.

## The most revealing fan crosses zero speed

Now choose left state negative one and right state positive one. The left characteristics move left; the right characteristics move right. The rarefaction fan spans positions between negative t and positive t. Inside it, u equals x divided by t.

Stand at the original interface, position zero. For any positive time, the fan has value zero there. Therefore the physical flux through that stationary interface is one half times zero squared: zero. That is not what one gets by simply evaluating the physical flux at either initial endpoint. The flux of negative one and the flux of positive one are both one half.

This is the transonic rarefaction, meaning that characteristic speeds within the fan cross zero. It exposes a weakness of naive interface approximations. If we replace the fan by an artificial stationary jump, Rankine–Hugoniot does not complain: the endpoint fluxes are equal, so its speed is zero. But the interface flux would be one half rather than zero. A finite-volume update using that flux would push the wrong amount across the face even though it looks conservative algebraically.

A correct exact interface solver identifies the state along the stationary ray through the Riemann solution. If that ray passes through a rarefaction, we evaluate the flux at the corresponding fan value. If it falls to the left or right of a moving shock, we use the appropriate constant state instead. This simple idea leads directly to Godunov's method.

## Where the entropy inequality comes from

We can glimpse the mechanism without a full theory of distributions. Add a small viscosity term to Burgers' equation: positive epsilon times the second spatial derivative of u. Multiply the equation by u again. After applying the product rule, the entropy balance acquires two new terms: one is a spatial derivative of a viscous entropy flux, and the other is negative epsilon times the square of the spatial gradient.

That final term is never positive. It measures the dissipation produced by smoothing. If we let the viscosity approach zero while obtaining a suitable convergent family of smooth solutions, the limiting entropy inequality retains the nonpositive sign. A shock is allowed to lose entropy density in this mathematical sense. An expansion shock would require the wrong sign and is excluded.

Do not infer from this one computation that every physical system uses the same entropy density or that the entire uniqueness theory follows from checking a single quadratic inequality. For a general scalar conservation law, entropy admissibility is formulated using a suitable family of convex entropies, and systems demand more care. Our calculation is a clear diagnostic for the Burgers examples we are studying.

## Wave patterns are local building blocks

A complicated profile can contain many increasing and decreasing segments. Each generates local tendencies toward expansion or compression. Some shocks may catch other shocks. A shock may enter a rarefaction fan, changing speed because the state on one side changes. A smooth profile may develop its first shock only after a finite period of steepening.

At a numerical cell face, however, the reconstruction often supplies just a left and right state at one instant. Solving the Riemann problem for those two states is a manageable way to determine the instantaneous flux. The global wave pattern is built by repeating this local operation and advancing the cell averages.

The quantities to keep distinct are the conserved state, the physical flux of that state, the speed of a characteristic, and the speed of a shock. For Burgers they are u, one half u squared, u, and one half the sum of the two jump states. Confusing these values is an easy way to build an algorithm that conserves something but moves waves incorrectly.

We now know what the numerical interface must represent. It must count the amount passing through a fixed face according to the entropy-admissible shock or fan. We are ready to compute that amount exactly for Burgers' equation, and to use it in a small finite-volume grid calculation.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: weak jumps and the quadratic entropy pair

For scalar \(u_t+f(u)_x=0\), a shock \(x=s t\) between \(u_L\) and \(u_R\) satisfies
\[
s(u_R-u_L)=f(u_R)-f(u_L).
\]
For inviscid Burgers, \(f(u)=u^2/2\), \(s=(u_L+u_R)/2\). For convex quadratic entropy \(\eta(u)=u^2/2\), entropy flux \(q(u)=u^3/3\) satisfies \(q'=\eta' f'\). The entropy inequality is
\[
\eta(u)_t+q(u)_x\le0
\]
in distributions. For a traveling shock, its delta coefficient is
\[
[q]-s[\eta],\qquad [q]=q(u_R)-q(u_L),\quad [\eta]=\eta(u_R)-\eta(u_L).
\]
The admissibility condition is \([q]-s[\eta]\le0\). When \(u_L=2\), \(u_R=0\), this equals \(-8/3+2=-2/3\). When \(u_L=0\), \(u_R=2\), it equals \(8/3-2=2/3\), violating the inequality.

For \(u_L<u_R\), the rarefaction fan is
\[
u(x,t)=\begin{cases}u_L,&x<u_Lt,\\x/t,&u_Lt\le x\le u_Rt,\\u_R,&x>u_Rt.\end{cases}
\]
For \(u_L=-1\), \(u_R=1\), the entropy solution has \(u(0,t)=0\) and thus interface flux \(f(0)=0\), whereas a spurious stationary expansion jump would yield endpoint flux \(1/2\). The Rankine–Hugoniot equation alone does not distinguish these.

For viscous Burgers,
\[
u_t+(u^2/2)_x=\varepsilon u_{xx}, \qquad \varepsilon>0,
\]
multiplying by \(u\) gives
\[
\partial_t\!\left(\frac{u^2}{2}\right)+\partial_x\!\left(\frac{u^3}{3}-\varepsilon u u_x\right)=-\varepsilon (u_x)^2\le0.
\]
This supplies the sign intuition behind entropy admissibility; passing rigorously to a weak limit requires compactness and convergence results not established here.

### Exercises with worked answers

1. For \(u_L=3\) and \(u_R=1\), calculate the shock speed. **Answer:** two.
2. With \(u_L=1\), \(u_R=3\), calculate the rarefaction value at \(x=2t\). **Answer:** two.
3. Does a jump from \(-1\) to \(1\) moving at speed zero conserve \(u\) weakly? **Answer:** yes, as a discontinuous weak solution, but it is not entropy-admissible.
4. Why does the exact transonic interface flux equal zero for those states? **Answer:** the fan takes the state zero on \(x=0\), and \(f(0)=0\).
5. For the shock from two to zero, evaluate \([q]-s[\eta]\). **Answer:** \(-2/3\), consistent with the quadratic entropy inequality.
6. Why does one quadratic entropy calculation not replace all entropy conditions for arbitrary systems? **Answer:** different fluxes and multiple characteristic fields require other admissibility criteria; scalar uniqueness generally relies on a family of convex entropy inequalities.

### Sources and further reading

- [LeVeque, Ketcheson and del Razo, *Riemann Problems and Jupyter Solutions*: Burgers' Equation](https://www.clawpack.org/riemann_book/html/Burgers.html).
- [Clawpack Riemann book: Approximate Burgers solvers and transonic entropy fixes](https://www.clawpack.org/riemann_book/html/Burgers_approximate.html).
- [Stanford Math 220A, conservation-law lecture notes](https://web.stanford.edu/class/math220a/lecturenotes.html).
