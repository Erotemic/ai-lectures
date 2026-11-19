# The Direct Method: Proving a Nonlinear Minimizer Exists

**Track:** Multivariable Calculus from First Principles. **Focus:** coercivity, weak lower semicontinuity, compactness of nonlinear terms, convexity versus existence, and nonlinear Euler–Lagrange equations.

<!-- BEGIN SPOKEN LECTURE -->

# The Direct Method: Proving a Nonlinear Minimizer Exists

There is a difference between writing down an equation that a minimum would satisfy and proving that a minimum exists. In elementary calculus, that difference may be hidden because a continuous function on a closed bounded interval automatically attains its minimum. In a space of functions, there are infinitely many directions, and a sequence of increasingly good candidates need not converge in the norm we initially chose.

The direct method in the calculus of variations provides an existence proof that does not start by solving a differential equation. We construct candidates whose energies approach the greatest lower bound, show that their energies prevent them from escaping, extract an appropriate limit, and prove that this limit actually attains the lower bound. Each step has its own hypothesis. None can be replaced by a vague statement that the energy looks positive or that a numerical solver seems to settle down.

We will do the proof for a specific nonlinear functional. It combines a derivative penalty, a fourth-power response to displacement, and a constant external load. Unlike a purely quadratic problem, its Euler–Lagrange equation is nonlinear. Nevertheless, we can establish existence and uniqueness before trying to solve it. Then we will change the potential to a double-well energy and see what survives when uniqueness is lost.

## Choose the space before minimizing

Work on the interval from zero to one, with both endpoints fixed at zero. Our admissible functions belong to H naught one: functions with a square-integrable weak derivative and zero boundary trace. In one dimension they have continuous representatives, so the endpoint condition also has an ordinary interpretation.

Assign to a candidate u three contributions. The first is one half the integral of its squared slope. This penalizes deformation and provides control of the H naught one norm. The second is one quarter the integral of the fourth power of u. It grows faster than the quadratic term at large amplitudes, and it is never negative. The third is minus the integral of u, representing work done by a constant positive load that rewards positive displacement.

Call the total E of u. In words, E is the squared-slope cost, plus the fourth-power displacement cost, minus the total displacement. A function may lower energy by moving upward under the load, but large slopes and large amplitudes are costly. The functional is well-defined on H naught one of an interval because those functions are continuous and bounded, so their fourth powers are integrable.

The first thing we need is a lower bound for E. The negative load term is the only part that could make the energy go to negative infinity. Since the interval has length one, its absolute value is at most the L two norm of u. Poincaré's inequality bounds that by a constant times the L two norm of u prime. Denote the slope norm by A. The energy is therefore at least one half A squared minus a constant times A. The fourth-power term only improves the bound, since it is nonnegative.

A positive quadratic eventually dominates a linear term. The expression one half A squared minus C times A is bounded below, and it goes to positive infinity as A goes to infinity. Thus E is bounded below and coercive on our energy space. Coercive means that a candidate cannot send its norm toward infinity while keeping energy near the infimum.

This is stronger than saying the formula contains a positive term. If our boundary conditions allowed constant shifts with no derivative penalty controlling them, the load could break the lower bound. The Poincaré estimate and the choice of admissible space are doing genuine work.

## Build an infimizing sequence without finding a solution

Let m denote the infimum of E over all admissible functions. We know m is a finite real number. By the definition of an infimum, for each positive integer n we can choose an admissible u n whose energy is less than m plus one over n. Such a sequence is called a minimizing sequence.

We have not claimed that any member of the sequence solves the Euler–Lagrange equation. In principle the functions could have corners, high-frequency oscillations, or rather irregular shapes. The definition only asks that their energies approach m.

Because E of u n stays near a fixed finite value, coercivity tells us their H naught one norms are bounded. There is a single constant M that controls the L two norm of every derivative, at least after discarding a finite initial portion. We are now entitled to use weak compactness in a Hilbert space. Some subsequence converges weakly in H naught one to a function u star in that same space.

The weak limit satisfies the zero boundary condition because H naught one is the space in which we took the weak limit. This is one reason the function space must be built into the problem from the beginning. If we had taken arbitrary pointwise limits without a convergence theorem, preserving the boundary condition and the derivative bound would require separate arguments and might fail.

We need one final step. Does the limit have energy at most m? Weak convergence by itself is not enough to justify replacing u n by u star inside a fourth power. We must use the appropriate convergence result for each term.

## Pass each term to the limit honestly

Start with the squared-slope term. Since u n converges weakly in H naught one, its derivatives converge weakly in L two. The squared L two norm is weakly lower semicontinuous. The derivative energy of u star is no larger than the limit inferior of the derivative energies along the subsequence. It may be strictly smaller, and that is acceptable.

Next, the nonlinear fourth-power term. On our bounded interval, an H one bound supplies a uniformly bounded and equicontinuous family of functions. By the compact embedding proved in the Sobolev setting, a further subsequence converges uniformly to u star. We can make this subsequence selection without losing the weak limit. Uniform convergence on a compact interval implies that the fourth powers converge uniformly, and therefore their integrals converge.

The load term also converges. It is a bounded linear functional on our energy space, so weak convergence would have been enough; uniform convergence certainly suffices too.

Putting the three terms together, the energy of u star is no greater than the limit inferior of the energies of the selected u n. But the selected energies approach m. Therefore E of u star is at most m. Since m is the infimum of all admissible energies, E of u star is also at least m. It must equal m exactly.

We have proved that the nonlinear energy has a minimizer without knowing its formula. The proof was not an invocation of a general theorem with unexplained conditions. We checked the exact conditions: the right function space, a coercive lower bound, a weakly convergent subsequence, compactness for the nonlinear term, and lower semicontinuity for the derivative term.

The logic also reveals what could break in a different problem. On an infinite interval, compactness may fail because functions translate away. In a higher-dimensional setting with a critical nonlinearity, concentration may prevent the strong convergence we relied on. If the derivative part is not weakly lower semicontinuous, energy can jump upward at the weak limit. An existence theorem is only as strong as the weakest of these links.

## From a proven minimizer to a nonlinear differential equation

Now we can differentiate the energy. Take a smooth, zero-endpoint perturbation eta, and replace u by u plus a small scalar times eta. The first variation of the slope term is the integral of u prime times eta prime. The derivative of one quarter u to the fourth is u cubed times eta. The load contributes minus the integral of eta.

At our minimizer, the first variation is zero in every admissible direction. Hence the integral of u prime eta prime, plus the integral of u cubed eta, equals the integral of eta for every zero-endpoint test function.

Integrating the derivative term by parts, when justified, gives the differential equation: negative u double prime plus u cubed equals one. The endpoint values remain zero. This is a semilinear boundary-value problem. It contains a linear highest-derivative term and a nonlinear lower-order term.

The argument so far guarantees a weak solution. In one dimension, we can also recover additional regularity. We know u is bounded and continuous; thus u cubed minus one is square-integrable. The weak equation says the second derivative of u, interpreted as a distribution, equals u cubed minus one. Standard one-dimensional regularity then gives a square-integrable second weak derivative, and in fact a continuously differentiable representative. We can now interpret much more of the differential equation classically.

Notice the order. Existence came first, as an energy argument. The equation and regularity came afterward. This prevents us from mistaking a formal solution of a differential equation for a guaranteed minimizer.

## Is the minimizer the zero function?

We can answer without solving the nonlinear equation. Test the energy on the simple curve x times one minus x, multiplied by a small positive constant t. This curve vanishes at both endpoints and bulges upward between them.

Its squared-slope integral contributes a positive term proportional to t squared. The fourth-power term contributes a still smaller positive term proportional to t to the fourth. The negative load contributes a term linear in negative t. For sufficiently small positive t, the linear decrease wins. This trial function has negative energy.

The zero function has energy zero. Since our minimizer has energy no larger than that of any trial function, it must have negative energy and cannot be zero. We have shown that the nonlinear boundary-value problem has a nontrivial weak solution, without ever writing a closed formula for it.

This is often the right level of conclusion in nonlinear analysis. A theorem can establish existence, a sign property, an energy estimate, and uniqueness even when an elementary expression for the solution is unavailable. Numerical approximation can then be justified as a method for approaching a solution known to exist.

## Uniqueness comes from a different argument

Our energy is not only coercive and lower semicontinuous. It is strictly convex. The squared derivative norm is strictly convex on H naught one because two different zero-boundary functions cannot have the same derivative almost everywhere. The fourth-power integral is convex as well, and the linear load does not affect convexity.

A strictly convex functional has at most one minimizer on a convex feasible set. Therefore the minimizer whose existence we just proved is unique. Its weak equation also has at most one solution: subtract the equations for two solutions, test by their difference, and use the fact that the cubic function is increasing. The resulting sum of nonnegative terms can vanish only when the two solutions agree.

These two methods of proving uniqueness reinforce one another. But uniqueness did not follow from compactness. Compactness produced existence; strict convexity supplied uniqueness. Keeping them separate prepares us for models where the energy remains coercive but develops several local or global minima.

## Change the potential: existence without uniqueness

Take a different energy on a longer interval, from zero to ten. Keep the squared-slope penalty and the pinned endpoints, but replace the positive fourth-power potential by the square of u squared minus one. This double-well potential is minimized when u is plus one or minus one. It is nonnegative but not convex as a function of u.

The direct method still works in one dimension. The derivative term bounds the H naught one norm through Poincaré's inequality. The total energy is nonnegative, and a minimizing sequence has bounded derivative norm. Compactness gives uniform convergence of a subsequence, which passes the continuous double-well potential to the limit. The squared derivative term is lower semicontinuous. So a minimizer exists.

But what shape minimizes the energy? The zero function has potential value one at every point, so its total energy is ten. A trial function that ramps linearly from zero to one over the first unit, stays at one through the middle eight units, and ramps down to zero over the last unit has much smaller energy. Its squared-slope contribution is one. The double-well potential contributes sixteen fifteenths, and the total is thirty-one fifteenths, well below ten.

Therefore a minimizer cannot be identically zero. Yet the energy is unchanged if we replace u by negative u. Whenever u is a nonzero minimizer, negative u is a different minimizer with the same energy. Existence survives; uniqueness fails. Neither conclusion is mysterious once we distinguish compactness from convexity.

For materials with phase transitions, pattern-forming energies, and nonlinear boundary-value problems, this distinction is central. Nonconvex does not mean there is no minimum. It means the standard uniqueness guarantee may disappear, and in more complicated functionals the lower semicontinuity step itself may become harder.

## The direct method as an engineering checklist

When facing a new variational problem, begin by asking what a candidate function is allowed to be and which norm makes its energy meaningful. Find the terms that control that norm, and prove a coercive estimate. Check that a minimizing sequence stays in a weakly closed feasible set, and identify the compactness theorem appropriate to that space and domain.

Then examine each term of the energy separately. A positive squared-gradient term is well suited to weak lower semicontinuity. A lower-order nonlinear term may need strong convergence, supplied by an embedding theorem. A nonconvex gradient term can require much more than a routine appeal to continuity, because weakly converging gradients need not converge pointwise or in norm.

Only after existence should we differentiate the energy and ask for regularity, uniqueness, or numerical error. That order gives a clean chain of reasoning from a finite energy budget to a function that actually attains the minimum. It is the bridge from finite-dimensional optimization to rigorous nonlinear differential equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### A nonlinear Dirichlet minimization problem

Let \(V=H_0^1(0,1)\), and define

\[
E(u)=\frac12\int_0^1|u'|^2\,dx
+\frac14\int_0^1|u|^4\,dx
-\int_0^1u\,dx.
\]

The one-dimensional Sobolev embedding ensures \(V\subset C([0,1])\), so all terms are finite. By Poincaré and Cauchy–Schwarz, with \(A=\|u'\|_2\),

\[
E(u)\ge\frac12A^2-C_PA.
\]

The right side is bounded below and coercive as \(A\to\infty\). Let \(u_n\) be minimizing. It is bounded in \(V\), so after extraction \(u_n\rightharpoonup u_*\) in \(V\). In one dimension a further subsequence converges uniformly to \(u_*\). Therefore

\[
\int|u_n|^4\to\int|u_*|^4,\quad \int u_n\to\int u_*;
\qquad
\int|u_*'|^2\le\liminf_n\int|u_n'|^2.
\]

Thus \(E(u_*)\le\liminf E(u_n)=\inf_VE\) and equality follows by definition of infimum.

### First variation, uniqueness, and regularity

For any \(v\in V\),

\[
DE(u)[v]=\int_0^1 u'v'\,dx+\int_0^1u^3v\,dx-\int_0^1v\,dx.
\]

The minimizer satisfies

\[
\int_0^1u_*'v'+u_*^3v\,dx=\int_0^1v\,dx\quad\forall v\in V,
\qquad -u_*''+u_*^3=1
\]

in the distributional sense. For two solutions \(u,w\), subtract the weak equations and test with \(v=u-w\):

\[
0=\int|u'-w'|^2\,dx+\int(u^3-w^3)(u-w)\,dx.
\]

Both integrands are nonnegative, hence \(u=w\). The same uniqueness follows from strict convexity of \(E\). Since \(u_*\in C([0,1])\), \(u_*^3-1\in L^2\); the distributional identity \(u_*''=u_*^3-1\) implies \(u_*\in H^2(0,1)\), hence \(u_*\in C^1([0,1])\) after choosing its representative.

For \(\phi(x)=x(1-x)\), exact integrations give

\[
\int_0^1(\phi')^2\,dx=\frac13,\quad
\int_0^1\phi\,dx=\frac16,\quad
\int_0^1\phi^4\,dx=\frac1{630},
\]

so
\[
E(t\phi)=\frac{t^2}{6}+\frac{t^4}{2520}-\frac{t}{6}<0
\]

for sufficiently small \(t>0\). Thus \(u_*\ne0\).

### A nonconvex energy with two global minimizers

Set \(V_{10}=H_0^1(0,10)\) and

\[
J(u)=\int_0^{10}\left[\frac12|u'|^2+(u^2-1)^2\right]dx.
\]

Since \(J\ge\frac12\|u'\|_2^2\), minimizing sequences are bounded in \(V_{10}\), and compactness in \(C([0,10])\) passes the continuous potential to the limit; a minimizer exists. The zero function has \(J(0)=10\). For

\[
w(x)=\begin{cases}
x&0\le x\le1,\\
1&1\le x\le9,\\
10-x&9\le x\le10,
\end{cases}
\]

we calculate

\[
\frac12\int_0^{10}|w'|^2\,dx=1,
\qquad\int_0^{10}(w^2-1)^2\,dx=2\int_0^1(x^2-1)^2\,dx=\frac{16}{15}.
\]

Hence \(J(w)=31/15<10\). Every minimizer is nonzero; since \(J(u)=J(-u)\), minimizers come in distinct sign-reflected pairs. Existence does not imply uniqueness.

### Exercises with answers

1. **Coercivity:** Why is \(A^2/2-CA\) bounded below? **Answer:** Complete the square: \((A-C)^2/2-C^2/2\).
2. **Trial function:** Compute \(E(t x(1-x))\). **Answer:** \(t^2/6+t^4/2520-t/6\), negative for sufficiently small positive \(t\).
3. **Uniqueness:** For \(a,b\in\mathbb R\), show \((a^3-b^3)(a-b)\ge0\). **Answer:** Factor it as \((a-b)^2(a^2+ab+b^2)\ge0\).
4. **Nonconvexity:** Does a double-well potential rule out existence? **Answer:** No. On a bounded interval, coercivity and compactness give existence for \(J\); the sign symmetry and the nonzero trial-function energy show nonuniqueness.

### Sources and further reading

- Thomas Schmidt, [*Calculus of Variations*, Hamburg lecture notes](https://www.math.uni-hamburg.de/home/schmidt/lectures/CalcVar.pdf), especially existence via the direct method, lower semicontinuity and uniqueness.
- J. C. Wei, [*The Direct Methods in the Calculus of Variations*, UBC lecture notes](https://personal.math.ubc.ca/~jcwei/MATH517-2018-Lectnotes2.pdf), for the abstract reflexive-space existence statement.
- Massimo Gobbino, [*Introduction to Calculus of Variations*, University of Pisa lecture notes](https://pagine.dm.unipi.it/gobbino/Home_Page/Files/HP_AD/CdV_17_Book.pdf), for examples separating compactness, lower semicontinuity and regularity.
- [Wikipedia: Direct method in the calculus of variations](https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations) and [Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), for standard terminology.

*Teaching connections:* `multivariable-calculus:035000` and `036000` establish the two convergence mechanisms used here; `031000` develops first and second variations, and `032000` derives Euler–Lagrange equations with boundary terms.
