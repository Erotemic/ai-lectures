# 072000 — Banach Fixed Points and Picard Iteration: Constructing a Solution
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# Banach Fixed Points and Picard Iteration: Constructing a Solution

An equation can sometimes be solved by looking for something that does not change under a certain procedure. If we write a problem as u equals F of u, a solution is a fixed point of F. We might begin with a guess, apply F, apply F again, and hope the guesses approach a limit. But hoping is not a proof. The Banach fixed-point theorem tells us exactly what makes such an iteration work.

Imagine a map that always brings any two points closer by the same fixed percentage. If their original distance is one, their distance after applying the map is at most a half. After another application, at most a quarter. Every new correction becomes smaller at a geometric rate. In a complete metric space, the sequence of guesses is Cauchy and therefore converges. Continuity then shows that its limit is a fixed point. And if there were two fixed points, the map would have to bring them closer while leaving both unchanged, which is possible only if they are identical.

Two conditions are essential: the space must be complete, and the map must send the closed set under consideration back into itself with a contraction constant strictly less than one. A map that merely has Lipschitz constant one may have many fixed points or none. A map that shrinks distances but sends the proposed set outside itself does not give the required iteration either.

Now apply this to a differential equation. Consider a quantity whose rate of change equals its square, beginning with value one. We know from calculus that any sufficiently smooth solution satisfies an integral equation: its value at time t is one plus the integral, from zero to t, of the square of its earlier values. Conversely, a continuous function satisfying this integral equation is differentiable and solves the original equation. This is the integral formulation we can iterate.

Choose the complete space of continuous functions on a short time interval with the maximum norm. Restrict attention to the closed ball of functions whose maximum absolute value is at most two. For any function in that ball, its square is at most four, so the integral map produces a function whose size is at most one plus four times the interval length. If we keep the interval short enough, that stays within the ball.

We must also compare two guesses. Their squares differ by the difference of the guesses multiplied by their sum. Since each guess has size at most two, the sum has size at most four. Integrating over a short interval shows that the map shrinks the maximum distance by at most four times the interval length. On an interval of length one eighth, this contraction factor is at most one half. Both conditions hold. A unique continuous fixed point exists there, and therefore so does a unique solution of the differential equation.

What does the iteration look like? Start with the constant function one. The next guess is one plus time. The next replaces the square inside the integral with the square of one plus time, producing more terms in a power series. Every iteration uses the previous curve to construct a better one. The contraction argument proves this process approaches the actual solution, not just a plausible formal series.

The exact solution is one divided by one minus time. It grows without bound at time one. So local existence does not automatically imply global existence. The fixed-point construction worked on a short interval because the map stayed in a bounded ball. As the solution approaches blow-up, no fixed bounded ball can contain the continuation on an interval reaching beyond time one.

In a Banach space, the same idea works for many systems of ordinary differential equations and semilinear evolution equations. The challenge is to choose a space in which the nonlinear map is locally Lipschitz and the integral operator is small for short times. When the space is a Sobolev space, the product estimates we derived earlier supply the needed Lipschitz constants.

A fixed-point proof therefore has a logical order: select a complete solution space; establish that the map preserves the chosen ball; estimate the difference between two outputs; and choose the time or other parameter to make the contraction constant smaller than one. The conclusion is both an existence theorem and a uniqueness theorem, with a concrete iteration that can be implemented numerically.
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Banach's contraction principle: if \((X,d)\) is complete and \(F:X\to X\) satisfies \(d(Fx,Fy)\le qd(x,y)\) with \(0\le q<1\), then F has a unique fixed point \(x_*\), and \(d(F^nx,x_*)\le q^n d(x,x_*)\). For a contraction on a closed subset \(B\subset X\), use completeness of B.

For \(u'=u^2,\ u(0)=1\), put \(X=C([0,T])\) and \((Fu)(t)=1+\int_0^tu(s)^2ds\). On \(B=\{u:\|u\|_\infty\le2\}\), \(\|Fu\|_\infty\le1+4T\) and \(\|Fu-Fv\|_\infty\le4T\|u-v\|_\infty\). With \(T=1/8\), the ball is invariant and F is a contraction. The exact maximal solution is \(u(t)=(1-t)^{-1}\), defined for \(t<1\).

Picard iterates: \(u_0=1\); \(u_1=1+t\); \(u_2=1+t+t^2+t^3/3\). Do not confuse these partial approximants with exact power-series truncations at every stage.

### Exercises with answers

1. **Contraction factor.** For T equal to one eighth, what is the Lipschitz factor of F on the radius-two ball? **Answer:** At most one half.
2. **Second iterate.** Starting from \(u_0=1\), compute \(u_1\) and \(u_2\). **Answer:** \(u_1=1+t\) and \(u_2=1+t+t^2+t^3/3\).
3. **Global behavior.** Does local existence imply the solution survives past time one? **Answer:** No; the exact solution \(1/(1-t)\) blows up at time one.

### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, nonlinear existence](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [MIT OpenCourseWare, Introduction to Functional Analysis](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
