# When Does an Initial Value Determine a Trajectory? Existence, Uniqueness, and Dependence

<!-- BEGIN SPOKEN LECTURE -->

# When Does an Initial Value Determine a Trajectory?

You are handed a rate law and an initial state. It is tempting to assume that there is exactly one possible future. In many familiar equations that is true. But a differential equation does not automatically come with a guarantee of existence, uniqueness, or indefinite continuation. Those are mathematical questions about the rate law.

Why care about them in an introductory course? Because they explain when a solved formula is complete, when a numerical simulation is approximating a well-defined trajectory, and when two nearly identical starting conditions must lead to nearly identical outcomes for at least a short time. We can understand the main arguments using only single-variable calculus and a little patience with inequalities.

## Three different promises

The first promise is existence: there is at least one differentiable curve passing through the specified initial point and obeying the rate law. The second is uniqueness: no second curve obeys the same equation and passes through the same point at the same time. The third is continuous dependence: small changes in the initial condition lead to small changes in the solution on a common finite time interval, while the solutions remain in a region where suitable bounds hold.

Existence alone does not give uniqueness. Uniqueness near the initial time does not say how long a solution continues. Continuous dependence on a fixed interval is not the same as saying errors remain small forever. Each statement has its own hypotheses.

Let's name the mathematical object. An initial-value problem specifies y prime equals f of t and y, together with y at time t zero equal to y zero. Think of f as a machine. Feed it a time and a state, and it returns the slope that a solution must have there.

If f is continuous in a rectangle around the starting point, a local existence theorem guarantees at least one solution. For a standard uniqueness guarantee, we ask for some control over how sharply f can change as y changes. A convenient condition is that there is a constant L such that the difference between f at two states, at the same time, is no larger than L times the distance between those states. This is called a Lipschitz condition in the state variable.

It is a quantitative bound on the rate law's sensitivity. For example, f equal to negative three y is Lipschitz with constant three everywhere. The rate law f equal to y squared is Lipschitz on every bounded interval but not with one fixed constant for all real y. That distinction between local and global control will matter.

## Why a continuous rate law can fail uniqueness

Consider the equation y prime equals the square root of y, with nonnegative states and initial value zero at time zero. The zero curve solves the equation, because its derivative and its square root are both zero. But here is another solution: remain at zero until time one; after time one, let y equal one quarter times the square of t minus one.

Verify it. Before time one, the derivative is zero. After time one, the derivative is one half times t minus one. The square root of y is also one half times t minus one. At time one, the curve and its derivative join continuously. So the same initial value has produced two distinct solutions.

We can change the waiting time from one to two, three, or any nonnegative number. An infinity of trajectories emerges. The problem is not a hidden sign error. The rate law is continuous, but near zero its slope with respect to y becomes arbitrarily steep. It does not satisfy a local Lipschitz bound there.

This example tells us why 'we can draw the slope field' does not by itself mean the slope field determines one unique curve through each point. At the zero equilibrium the field permits a curve to wait and then peel away. The absence of uniqueness is a property of the mathematical model.

By contrast, consider y prime equals y squared with y at zero equal to one. Here f is smooth, so local uniqueness holds. The solution, one over one minus t, nonetheless becomes infinite as t approaches one. It exists and is unique near time zero, but does not exist as a finite solution for all future time. This example separates uniqueness from global existence.

## Turn the derivative equation into an integral equation

To see how a theorem can actually construct a solution, use the fundamental theorem of calculus. If y prime equals f of t and y, then the change from the initial value to the value at time t equals the integral of f along the unknown curve from t zero to t.

Conversely, if a continuous candidate y satisfies that integral equation and f is continuous, differentiating gives the original ODE. The derivative problem and the integral problem are two expressions of the same request.

This suggests an algorithm. Begin with a guessed curve, perhaps the constant curve equal to the initial value. Insert it into the integral on the right to produce a new curve. Insert that new curve to produce another. Repeat. This is Picard iteration.

Take y prime equals t plus y, with y at zero equal to zero. Begin with the constant guess zero. The first integral gives one half t squared. The next iteration integrates t plus one half t squared, giving one half t squared plus one sixth t cubed. The third adds one twenty-fourth t to the fourth power. The power series is beginning to appear, not because we guessed an exponential, but because the equation itself is refining our initial guess.

The exact answer is the exponential of t minus t minus one. Differentiate: its derivative is the exponential of t minus one. Add t plus y: t plus exponential of t minus t minus one gives the same expression. At time zero it is zero. The successive Picard curves approach that answer on sufficiently short intervals, and in this simple example on every bounded interval.

## Why iteration converges locally

What stops this process from chasing its own tail? Suppose we work in a small rectangle where f is bounded and Lipschitz in y. Two guessed curves that are close to each other have rate values differing by at most L times their distance. After integration over a time step of length h, their new curves differ by at most L times h times their old distance.

If we choose h small enough that L times h is less than one, the integral operation shrinks differences. This is a contraction. Repeating a contraction in a complete space of continuous curves converges to a fixed point: a curve that the operation no longer changes. That fixed point satisfies the integral equation and hence the ODE. The same contraction argument gives uniqueness in that small region.

There are technical details: we must choose the short interval so that each iterate stays inside the rectangle where our bounds hold. But the mechanism is accessible. Local existence comes from repeated integration. Local uniqueness comes from showing that two candidate curves cannot maintain a nonzero separation under a map that repeatedly shrinks differences.

The theorem is a tool, not a universal description of every solvable ODE. Some equations have unique solutions even when an easy Lipschitz condition is unavailable. A sufficient condition is not a necessary one.

## How differences in initial data grow

Suppose two trajectories obey the same rate law and begin a small distance apart. Write their difference as d of t. We may not know its exact formula. But if f is Lipschitz with constant L in the region traversed by both trajectories, the magnitude of the rate difference is at most L times the magnitude of the state difference.

Integrating that inequality leads to a remarkable bound: at time t, the distance between trajectories is no larger than their initial distance multiplied by the exponential of L times elapsed time. This is a form of Gronwall's inequality.

It answers a limited but important question. On a fixed finite interval, if the initial difference tends to zero, then the bound tends to zero as well. The solution depends continuously on its initial state. This does not mean the trajectories must remain close for an arbitrarily long time. Even the bound permits exponential amplification, and nonlinear systems can have substantially more complex long-time behavior.

For the very simple rate law y prime equals negative two y, the difference between two solutions actually decays like the exponential of negative two t. If they start at one and one point zero one, their difference after time t is one hundredth times that decaying exponential. The general Gronwall bound using L equal to two goes the other direction and allows growth. It is safe but far from sharp for a contracting system. General estimates often trade sharpness for broad applicability.

What if the rate laws themselves differ slightly? If one model's rate differs from another's by at most a small amount, and both are controlled by the same Lipschitz bound in the relevant region, a similar inequality shows how that modeling error accumulates over time. This is the mathematical distinction between a sensitive prediction and a robust one.

## Uniqueness and crossing curves

One consequence is particularly geometric. Suppose an autonomous scalar equation has an equilibrium at some value c, and the rate law is locally Lipschitz. The constant curve y equals c is a solution. Another solution cannot cross through c at a finite time, because at the crossing point it would share an initial condition with the constant curve. Uniqueness would force the two curves to agree locally and, where defined, along their common interval.

The same idea prevents two solution graphs of a locally unique first-order equation from crossing at the same time and state. This is why direction fields often look like families of strands that never intersect. If you see a numerical plot where two such trajectories appear to cross, it may be a plotting artifact or a hint that uniqueness assumptions fail.

## What the theorem does not say

A well-posed local initial-value problem is not a promise of a useful prediction for all times. Solutions might blow up. The rate law might cease to be defined. A small initial error might grow rapidly over long intervals. And a mathematical model may omit a physical mechanism entirely.

Still, the local theorem is foundational. It tells us that under checkable conditions, there is a definite curve for a numerical method to approximate. It justifies treating an initial state as selecting a trajectory. It explains why continuous rate laws need extra care, and why globally valid formulas require more than local smoothness. Our next task will be to apply these ideas to oscillations, where the changing state includes both position and velocity.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

**Preparation:** Fundamental theorem of calculus, continuity and derivatives, exponential functions. **Distinctions:** local existence, local uniqueness, continuous dependence, global continuation.

### Picard–Lindelöf construction

Consider \(y'=f(t,y)\), \(y(t_0)=y_0\). Assume \(f\) is continuous on a rectangle \(R=[t_0-a,t_0+a]\times[y_0-b,y_0+b]\), bounded there by \(M\), and Lipschitz in \(y\) on \(R\) with constant \(L\). Choose \(h\) with \(h\le a\), \(Mh\le b\), and \(Lh<1\). On the closed set of continuous functions with \(\sup_{|t-t_0|\le h}|y(t)-y_0|\le b\), define
\[
(Ty)(t)=y_0+\int_{t_0}^t f(s,y(s))\,ds.
\]
Then \(T\) maps the set into itself and \(\|Ty-Tz\|_\infty\le Lh\|y-z\|_\infty\). The contraction mapping theorem yields a unique fixed point, a solution on the short interval. If \(L=0\), any sufficiently small \(h\) works.

### Picard iterates for an explicit example

For \(y'=t+y,\ y(0)=0\), start \(y_0(t)=0\):
\[
 y_1(t)=t^2/2,\quad y_2(t)=t^2/2+t^3/6,\quad
 y_3(t)=t^2/2+t^3/6+t^4/24,\quad y(t)=e^t-t-1.
\]

### Dependence bound

Suppose \(y,z\) solve the same equation and lie in a common Lipschitz region for \(t_0\le t\le T\). Then
\[
|y(t)-z(t)|\le |y(t_0)-z(t_0)|e^{L(t-t_0)}.
\]
If their vector fields differ by at most \(\delta\) while both trajectories stay in the region, then for \(L>0\),
\[
|y(t)-z(t)|\le |y(t_0)-z(t_0)|e^{L(t-t_0)}+\frac{\delta}{L}\left(e^{L(t-t_0)}-1\right).
\]
For \(L=0\), replace the second term with \(\delta(t-t_0)\). This is a finite-time bound, not a global uniform guarantee.

### Nonuniqueness and finite escape

For \(y'=\sqrt{y}\), \(y(0)=0\), \(y\ge0\), for each \(a\ge0\),
\[
 y_a(t)=\begin{cases}0&t\le a,\\(t-a)^2/4&t>a.\end{cases}
\]
The derivative matches at \(a\). The square root is continuous but not locally Lipschitz at zero.
For \(y'=y^2,\ y(0)=1\), the unique maximal solution is \(y=(1-t)^{-1}\) on \(( -\infty,1)\); the smoothness of the right-hand side does not imply global existence.

### Exercises with answers

1. Does continuity in \((t,y)\) alone guarantee a locally unique solution? **Answer:** No; it guarantees local existence in finite dimensions, but \(y'=\sqrt{y}\) at \(y_0=0\) is not unique.
2. Compute two Picard iterates for \(y'=2y+1,\ y(0)=0\) starting at zero. **Answer:** \(y_1(t)=t\), \(y_2(t)=t+t^2\); the exact solution is \((e^{2t}-1)/2\).
3. Two solutions remain in a region with Lipschitz constant 3 for \(0\le t\le2\) and begin \(0.01\) apart. Give a valid worst-case bound at \(t=2\). **Answer:** \(0.01e^6\), not necessarily sharp.
4. Why is \(y'=y^2\), \(y(0)=1\), not a counterexample to Picard–Lindelöf? **Answer:** The theorem promises local existence and uniqueness, not finite values for every future time.

### Reading and references

- Jeremy Orloff, MIT 18.03 (Spring 2024), *Existence and Uniqueness Theorem*, including a Picard-iteration outline: https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/mites_1803_s24_exist_uniq.pdf
- MIT OpenCourseWare, 18.03 lecture notes on existence, uniqueness, and phase-line reasoning: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/pages/lecture-notes/
- Wikipedia: [Picard–Lindelöf theorem](https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem), [Gronwall's inequality](https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality), [Peano existence theorem](https://en.wikipedia.org/wiki/Peano_existence_theorem).
