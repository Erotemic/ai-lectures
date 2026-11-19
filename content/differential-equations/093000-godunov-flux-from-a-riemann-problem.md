# One Face, One Riemann Problem: Building the Godunov Flux

<!-- BEGIN SPOKEN LECTURE -->

# One Face, One Riemann Problem

Suppose a computer holds four numbers representing the average state in four adjacent cells. It is asked to advance a nonlinear conservation law by a small time step. The computer cannot see a perfectly smooth curve between the cell centers. It only knows the amounts stored in the cells and the equation that dictates how those amounts may flow.

How should it calculate what crosses a shared boundary?

For constant-speed advection, we answered by looking upwind. If the speed was positive, we took the state from the cell on the left. For negative speed, we took the state on the right. But in the nonlinear Burgers equation, the characteristic speed is the state itself. At a face where the left and right states differ, there may be two speeds, a shock speed, or a whole fan of speeds. Simply checking the sign of one cell average is not enough.

The construction we need is Godunov's method. Its central idea is almost literal: put the two neighboring cell states on either side of the face, solve that tiny Riemann problem, and evaluate the physical flux through the stationary face. Use exactly that one flux for both adjacent cells. This local rule combines our analytical shock and rarefaction solutions with the finite-volume conservation formula.

## What a face needs to know

Consider Burgers' conservation law, where the physical flux is one half the state squared. At a fixed interface, call the state immediately to the left L and the state immediately to the right R. The Riemann problem begins with L for negative positions and R for positive positions, then evolves according to the PDE.

We need the state of that exact entropy solution at the stationary ray, position divided by time equals zero. Call it the interface state. The numerical flux is the physical flux evaluated at that state. It is a number, not two competing guesses from the two cells.

Start with a compressive pair: L equals two and R equals zero. Because L exceeds R, the Riemann solution is a shock. Its speed is one half of their sum, which is one. The shock travels right. At the stationary interface, we remain to the left of the shock for positive times, so the interface sees the left state two. Its flux is one half times four, or two.

Change the pair to L equals one and R equals negative two. It is still a compressive shock, but now its speed is negative one half. It moves left. The stationary interface is to the right of the shock and sees the right state negative two. The flux is one half times four, again two.

Notice the distinction: characteristic speeds on the two sides are one and negative two, but the shock itself moves at negative one half. We choose the flux by the direction of the shock, not by guessing which endpoint velocity looks more relevant. At a stationary shock, the two endpoint fluxes agree by Rankine–Hugoniot, so the interface flux is well defined even though the state jumps there.

## A rarefaction needs three cases

If L is smaller than R, the solution is a spreading rarefaction fan. Think of its characteristic speeds, which range continuously from L to R.

If both states are nonnegative, every characteristic in the fan travels right or stays still. The stationary interface sees the left state. For L equals one and R equals three, the flux is one half.

If both states are nonpositive, the fan travels left. The interface sees the right state. For L equals negative three and R equals negative one, the flux is one half, because the right state is negative one.

The third case is the one that catches naive methods. If L is negative and R positive, the fan contains both left-moving and right-moving characteristics. The stationary ray falls inside it, at state zero. The exact Godunov flux is therefore zero. With L equal to negative one and R equal to one, a formula that always uses the left endpoint would give one half, and a formula that always uses the right endpoint would also give one half. Both would be wrong, although they might still be inserted into a formally conservative update.

There is a compact way to express this for a convex flux. In an expanding Riemann problem, choose the minimum physical flux over all states between L and R. In a compressive one, choose the maximum flux between R and L. For the quadratic flux, a compressive interval's maximum occurs at one of its endpoints. An expanding interval that crosses zero has its minimum at zero. This min-or-max expression reproduces every case we have just reasoned through geometrically.

It is a particularly useful formula because it does not require us to draw a fan or a shock for every face in a code. But understanding the waves first prevents us from misusing the formula when we change to a nonconvex flux, a system of equations, or a different equation.

## Four cells, every flux computed

Let us do a complete grid update. Take four cells of equal width one, arranged periodically in a ring. Their current averages, in order, are two, zero, negative one, and one. Use a time step of one quarter. All numbers are dimensionless for this example.

A periodic grid has four distinct interfaces. At the first interface, between cell one with value two and cell two with value zero, we have the right-moving compressive shock already solved. Its flux is two.

At the second interface, between zero and negative one, we have a compressive shock with speed negative one half. The interface samples the right state negative one, giving flux one half.

At the third interface, between negative one and one, there is a transonic rarefaction. Its flux is zero.

At the fourth interface, crossing the periodic boundary from value one back to value two, there is a right-moving rarefaction. Its interface state is the left value one, giving flux one half.

Those four values are all the information needed for the conservative update. A cell's new average equals its old average plus time-step divided by width times incoming flux minus outgoing flux.

For cell one, the incoming periodic flux is one half and the outgoing flux is two. Its new value is two plus one quarter times one half minus two, which is one point six two five.

For cell two, the incoming flux is two and the outgoing flux one half. Its new value is zero plus one quarter times two minus one half, or zero point three seven five.

For cell three, the incoming flux is one half and the outgoing flux zero. Its new value is negative one plus one eighth, or negative zero point eight seven five.

For cell four, the incoming flux is zero and the outgoing periodic flux is one half. Its new value is one minus one eighth, or zero point eight seven five.

Add the old values: two plus zero minus one plus one equals two. Add the new values: one point six two five plus zero point three seven five minus zero point eight seven five plus zero point eight seven five also equals two. The change is zero because each interior flux appears once as an outgoing amount and once as an incoming amount. Periodicity closes the final face in the same way.

The cancellation does not depend on these numbers being exactly representable in decimal or on our Burgers flux being quadratic. It follows algebraically from using a single shared face flux in a finite-volume balance. That is the conservation property we wanted.

## Stability is a separate question

The largest characteristic speed in our initial four-cell state has magnitude two. Multiplying by time step one quarter and dividing by cell width one gives a Courant number of one half. That lies within the usual first-order scalar Godunov stability restriction.

The restriction has a physical meaning. A face update assumes its local Riemann solution supplies the interface flux over the time step, before information from more distant faces changes that local problem. If a numerical step is too large relative to cell width and wave speed, we cannot pretend that separate face problems remain independent throughout it.

The face flux is nonlinear, so a bound on the characteristic speed should account for the relevant states, including reconstructed states if we later build a higher-order scheme. A fixed time step that was safe at the beginning may stop being safe if the solution develops larger speeds. A practical solver recomputes its allowable step size from the evolving state.

We should also resist a common overclaim: exact conservation does not guarantee accuracy. A first-order Godunov method may smear a shock across several cells. It typically avoids the violent spurious oscillations of an unrestrained centered discretization, but front thickness and smooth-region accuracy still matter. The next improvement will address those defects without surrendering the shared-flux principle.

## A conservative flux is not automatically an entropy flux

Imagine defining the interface flux merely as the average of the two physical endpoint fluxes. The same averaged value can be used by both neighboring cells, so the total amount still telescopes. Yet for the pair negative one and positive one, that average is one half, while the correct Riemann flux is zero. The method has conserved the wrong interface transport.

Godunov's construction uses the entropy solution of each local Riemann problem. That is the extra mathematical input beyond flux balance. For Burgers, we know exactly which wave is selected: a compressive shock for decreasing states, or a rarefaction for increasing states. If we chose an inadmissible expansion shock at a transonic interface, we could advance a perfectly conservative but physically incorrect computation.

The grid calculation therefore joins three previously separate ideas. The conservation law determines how cell amounts change. The Riemann problem determines which state governs flux at a face. The CFL restriction determines how far a local explicit step may safely advance. A solver needs all three.

What is missing is better use of information inside each cell. So far every cell is treated as a constant rectangle, even when neighboring averages lie along a smooth ramp. We can instead reconstruct a line within each cell, use its edge values as Riemann data, and retain a conservative update. But a naive line can overshoot at a sharp front. The solution is not to abandon higher accuracy; it is to limit the reconstructed slopes when the data do not support them.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact Godunov flux and periodic four-cell update

For Burgers' \(f(u)=u^2/2\), set \(G(L,R)=f(u^*(0))\), where \(u^*\) is the entropy Riemann solution and \(u^*(0)\) denotes the state on the ray \(x/t=0\):
\[
G(L,R)=\begin{cases}
\min_{u\in[L,R]} f(u),&L\le R,\\
\max_{u\in[R,L]} f(u),&L>R.
\end{cases}
\]
For \(L>R\), let \(s=(L+R)/2\); then \(G=f(L)\) if \(s>0\), \(G=f(R)\) if \(s<0\), and both agree for \(s=0\). For \(L<R\), \(G=f(L)\) if \(L\ge0\), \(G=f(R)\) if \(R\le0\), and \(G=0\) if \(L<0<R\). In the equal-state case \(G(L,L)=f(L)\).

For equal cell width \(h\), step \(\Delta t\), conservative cell averages satisfy
\[
Q_i^{n+1}=Q_i^n-\frac{\Delta t}{h}\Bigl(G(Q_i^n,Q_{i+1}^n)-G(Q_{i-1}^n,Q_i^n)\Bigr).
\]
With periodic \(Q^n=(2,0,-1,1)\), \(h=1\), \(\Delta t=1/4\), the interfaces after cells 1,2,3,4 have fluxes \((2,1/2,0,1/2)\). Then
\[
Q^{n+1}=(13/8,3/8,-7/8,7/8),\quad
\sum_iQ_i^{n+1}=\sum_iQ_i^n=2.
\]
Here \(\Delta t\max_i|Q_i^n|/h=1/2\). This is a sufficient familiar scalar CFL check for the first-order example; stability and entropy convergence claims for general schemes require their own conditions.

Two possible numerical fluxes can both conserve after telescoping while selecting different interface transport. At \((L,R)=(-1,1)\), Godunov gives \(G=0\), whereas arithmetic endpoint flux averaging gives \(\{f(-1)+f(1)\}/2=1/2\).

### Exercises with worked answers

1. Find \(G(2,0)\). **Answer:** two, because the shock speed is one and the interface sees the left state.
2. Find \(G(1,-2)\). **Answer:** two, because the shock speed is negative one half and the interface sees state negative two.
3. Find \(G(-1,1)\). **Answer:** zero, because the interface lies at the sonic point of the rarefaction fan.
4. For the four periodic cells, verify the new value of cell three. **Answer:** \(-1+(1/4)(1/2-0)=-7/8\).
5. Why does total mass remain constant even if an interface flux has some numerical approximation error? **Answer:** the same face flux enters one neighbor with the opposite sign from the other; a periodic weighted sum telescopes.
6. Why is a shared numerical flux not by itself an entropy guarantee? **Answer:** consistency and telescoping do not determine the admissible solution of the local wave problem.

### Sources and further reading

- [Clawpack Riemann book: approximate solvers and Godunov's method](https://www.clawpack.org/riemann_book/html/Approximate_solvers.html).
- [Clawpack Riemann book: exact Burgers Riemann solutions](https://www.clawpack.org/riemann_book/html/Burgers.html).
- [Clawpack Riemann book: the transonic rarefaction entropy fix](https://www.clawpack.org/riemann_book/html/Burgers_approximate.html).
- [LeVeque, *Finite Volume Methods for Hyperbolic Problems*, Cambridge University Press](https://www.cambridge.org/core/books/abs/finite-volume-methods-for-hyperbolic-problems/finite-volume-methods/CB7B0A27A6D37AE3B906D4AE7C60A87E).
