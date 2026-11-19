# Weak Solutions: When the Integral Equation Is the Right Equation

**Track:** Multivariable Calculus from First Principles. **Focus:** test functions, weak derivatives, energy spaces, coercivity, a one-dimensional Lax–Milgram argument, and interface flux continuity.

<!-- BEGIN SPOKEN LECTURE -->

# Weak Solutions: When the Integral Equation Is the Right Equation

A string made of two different materials can have a visible change of slope where the materials meet. That change is not automatically a defect. It may be exactly what force balance requires. But a formula that demands a classical second derivative at every point can reject such a string, even when the physical energy is finite and the forces balance correctly.

The weak formulation of a differential equation handles this situation by shifting the question. Rather than ask whether an equation holds pointwise with every derivative defined in the classical sense, we ask whether an integral identity holds against every admissible test function. The identity comes from multiplying the equation by a test function and integrating by parts. In a variational problem, it also comes from setting the first variation of an energy to zero.

The word weak does not mean vague or approximate. A weak solution satisfies a mathematically exact requirement. What becomes weaker is the demand for pointwise differentiability. That gain in flexibility is essential for proving existence and for constructing numerical approximations using functions with corners.

## Which derivatives does the problem require?

Start with a familiar boundary-value problem on the interval from zero to one. We want negative u double prime to equal a given load f, with u fixed at zero at both endpoints. For a smooth solution, multiply the equation by a smooth test function v that also vanishes at the endpoints. Integrate. One integration by parts turns the equation into the statement that the integral of u prime times v prime equals the integral of f times v.

Only first derivatives of u appear now. This is not merely shorthand for the second-derivative equation. It tells us how to state the problem on a larger class of functions. A continuous, piecewise linear function has slopes on each interval and finite squared-slope energy, though its slope jumps at mesh nodes. We cannot give its second derivative an ordinary pointwise interpretation at those nodes. Yet the integral of its slope times the slope of a test function is perfectly meaningful.

To make this precise, we use weak derivatives. A function w is a weak first derivative of u if integration by parts against every smooth, compactly supported test function produces the same identity that a classical derivative would produce. When u is smooth, the weak derivative agrees with its ordinary derivative. When u has a corner, a weak first derivative can still exist and be square integrable. The integrated relation is the criterion, not a fictitious derivative value at the corner.

The space called H one consists, on an interval, of square-integrable functions whose first weak derivatives are also square integrable. The subspace H naught one adds zero boundary trace. This is the natural space for our pinned-string energy. The word trace is deliberate: in higher dimensions, a boundary value need not be defined by naïvely evaluating an arbitrary representative at every point. Appropriate Sobolev trace theory makes the boundary condition meaningful.

## Test every allowable direction

Write the weak boundary-value problem as follows: find u in H naught one such that the integral of u prime times v prime equals the integral of f times v, for every v in H naught one. The unknown is one function. The demand is an infinite family of scalar equations, one for each test function.

Why insist on every test function? Suppose a numerical approximation has an error localized to one small interval. A single global test, such as the constant function or a broad sine wave, might miss that error by cancellation. A rich family of test functions can probe different regions and directions. The phrase for every test function is the mathematical mechanism that makes the condition selective enough to determine a solution.

We may first establish the identity using compactly supported smooth tests and then extend to the entire energy space by density and continuity. That extension is more than bookkeeping. It lets us use the solution itself, or a difference of two solutions, as a test function. Those choices are essential for energy estimates and uniqueness proofs.

The weak equation can also be read as a balance law. Its left side records the pairing of gradients; its right side records how the applied load acts on possible virtual displacements. The field does not have to possess a classical second derivative for this balance to make sense.

## Existence, uniqueness, and a stability estimate

It would be disappointing if we had merely invented a larger set of admissible candidates without any assurance that one satisfies the equation. The advantage of the energy formulation is that it gives us conditions under which a unique weak solution exists.

Let us allow the material stiffness to depend on location. Call it a of x. Assume it is measurable and bounded above by a finite number beta, and bounded below by a strictly positive number alpha, almost everywhere. Those assumptions permit jumps between materials, but exclude zero or negative stiffness in this model. Take f to be square integrable. The weak equation becomes: the integral of a times u prime times v prime equals the integral of f times v, for every zero-boundary test function v.

There are two inequalities behind the argument. First, the left-hand bilinear expression is bounded: its magnitude cannot exceed beta times the product of the two derivative norms. Second, when we put the same function in both slots, it is at least alpha times the squared derivative norm. The second property is called coercivity, and it is the infinite-dimensional analogue of a positive-definite matrix having its eigenvalues bounded away from zero.

We still need a norm on our space. For functions fixed to zero at both endpoints, Poincaré's inequality says the ordinary size of the function is controlled by the size of its slope. Thus the derivative norm controls the full H one norm on this space. It follows that our bilinear expression is bounded and coercive on a Hilbert space.

The Lax–Milgram theorem now states that the weak equation has exactly one solution and that its size is bounded by the size of the applied load. This is not a universal theorem for every differential equation. Its hypotheses are doing the work: a suitable complete space, boundedness, coercivity, and a bounded linear right-hand side. Here they are satisfied.

We can see the stability estimate directly. Use the unknown solution itself as the test function. Coercivity bounds the left side below by alpha times the squared slope norm. The right side, by Cauchy–Schwarz and Poincaré, is no more than the norm of f times the Poincaré constant times the slope norm. Cancel the nonzero slope norm and we find that the slope norm of u is no larger than the Poincaré constant divided by alpha, times the norm of f. If the load is zero and the endpoints are pinned, the solution must be zero.

For uniqueness, suppose two functions satisfy the same weak equation and boundary values. Subtract their equations and test with their difference. We obtain an integral of a times the square of the derivative of their difference equal to zero. Positive stiffness forces that derivative to vanish, and the boundary values force the difference itself to vanish. This proof avoids any claim that a classical second derivative exists.

## A material interface that a strong equation can misread

Now consider a string or conducting bar with two materials, but no distributed source. Prescribe u equal to zero at the left end and one at the right. In the left half, let stiffness a equal one. In the right half, let stiffness equal two. We seek the minimizer of one half the integral of a times squared slope.

Away from the material interface, the strong equation says that the derivative of a times u prime is zero. Because a is constant on each half, u must be linear separately on the two halves. There is no reason its slopes must match where a jumps. What must match is the flux: a times the slope.

To find the solution, call the shared flux q. On the left the slope is q, while on the right the slope is q divided by two. The total change in height is the left slope times one half, plus the right slope times one half. Set that change equal to one. We obtain three quarters of q equals one, so q is four thirds.

Therefore the slope on the left is four thirds and the slope on the right is two thirds. The height at the interface is two thirds. The curve is continuous, reaches height one at the right endpoint, and has a genuine corner in the middle. Its classical second derivative at the interface is not an ordinary number.

Nevertheless this is an exact weak solution. Multiply the piecewise constant flux by the derivative of a zero-endpoint test function and integrate. Because the flux is the same four thirds on both halves, the integral is four thirds times the difference between the test function's endpoint values. That difference is zero. The weak equation is satisfied for every allowed test function.

This calculation exposes what would go wrong with a naïve rule that demanded u prime be continuous across the interface. That rule would impose the wrong physical transmission condition. The correct condition is continuity of the weighted flux, unless an additional concentrated source is present at the interface.

We can derive the same condition by integrating by parts separately on the two halves. The interface contributions combine into the difference between the fluxes, multiplied by the test function's value at the interface. Because that value can vary, stationarity forces the flux jump to be zero. Weak formulations preserve precisely the boundary and interface information that a pointwise equation might overlook.

The example also shows why we must distinguish a global strong equation from a set of equations valid only away from exceptional points. Saying negative a times u double prime equals zero on each material piece ignores the derivative of a and fails to specify the transmission condition. Saying the derivative of a times u prime vanishes in the weak sense captures both pieces and their interface.

## Why uniqueness can fail when assumptions change

Return to the same derivative energy but remove all prescribed values. If there is no source, every constant function has zero slope and the same minimal energy. Coercivity fails on the full space because the energy cannot see a constant. The weak problem can determine only the derivative, not the absolute height.

If there is a source, a compatibility condition also appears. Test the pure Neumann weak equation with the constant function one, which is now admissible. The derivative on the left vanishes, so the total source, with any boundary flux contributions, must balance to zero. If it does not, no weak solution can satisfy the full problem. If it does, we may fix the mean value to remove the additive ambiguity.

Similarly, if a is allowed to approach zero or change sign, the positive coercivity estimate can fail. The same formal integration-by-parts expression may still be writable, but the existence and uniqueness theorem we used no longer applies without new analysis. The assumptions are not decoration around a proof. They describe what kind of mathematical problem we have.

Not every weak equation is a minimization condition, either. A nonsymmetric transport operator can have a weak formulation without coming from a simple positive quadratic energy. For our symmetric, positive stiffness model, the weak solution also uniquely minimizes a strictly convex energy. That equivalence depends on the structure of the operator.

## The bridge to computation

We now have three versions of one problem. For smooth u, the strong equation relates pointwise second derivatives to a source. The weak equation tests first derivatives against every admissible function. The variational equation says the first derivative of an energy vanishes in every admissible direction. Under our assumptions, these viewpoints agree where all their expressions make sense, but the weak and energy viewpoints remain meaningful for functions the strong equation cannot describe classically.

A numerical method cannot test infinitely many directions. Instead, it chooses a finite-dimensional subspace and requires the weak equation only for directions in that space. The resulting approximate solution is not the exact weak solution in general. Yet the same coercivity and orthogonality ideas that proved uniqueness will tell us how to measure and control its error. That is the mathematical basis of the finite-element method.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Weak problem and coercivity

Let \(a\in L^\infty(0,1)\) be real with \(0<\alpha\le a(x)\le\beta\) a.e. Let \(f\in L^2(0,1)\) and \(V=H_0^1(0,1)\). Define

\[
b(u,v)=\int_0^1 a(x)u'(x)v'(x)\,dx,\qquad
\ell(v)=\int_0^1 f(x)v(x)\,dx.
\]

With \(\|v\|_V=\|v'\|_{L^2}\), a norm on \(H_0^1\) equivalent to the standard Sobolev norm by Poincaré,

\[
|b(u,v)|\le\beta\|u\|_V\|v\|_V,\quad
b(v,v)\ge\alpha\|v\|_V^2,\quad
|\ell(v)|\le C_P\|f\|_{L^2}\|v\|_V.
\]

Lax–Milgram gives a unique \(u\in V\) satisfying \(b(u,v)=\ell(v)\) for all \(v\in V\), and

\[
\|u'\|_{L^2}\le\frac{C_P}{\alpha}\|f\|_{L^2}.
\]

For \(0< x <1\), zero endpoint traces, the sharp \(L^2\) Poincaré constant is \(C_P=1/\pi\). If the values at the ends are nonhomogeneous, work on an affine space \(g+V\) for a chosen lift \(g\), and test using \(V\).

### Exact discontinuous-coefficient problem

For \(f=0\), \(u(0)=0,u(1)=1\), and

\[
a(x)=\begin{cases}1,&0<x<1/2,\\2,&1/2<x<1,\end{cases}
\]

weak stationarity implies constant flux \(q=a u'\). As

\[
1=u(1)-u(0)=\int_0^1u'\,dx=q\left(\frac12+\frac14\right),
\]

we get \(q=4/3\), and

\[
u(x)=\begin{cases}\frac43x,&0\le x\le\frac12,\\
\frac23+\frac23(x-\frac12),&\frac12\le x\le1.
\end{cases}
\]

The derivative jumps from \(4/3\) to \(2/3\); the flux is continuous: \(1(4/3)=2(2/3)\). For \(v\in H_0^1\),

\[
\int_0^1a u'v'\,dx=\frac43\int_0^1v'\,dx=\tfrac43\big(v(1)-v(0)\big)=0.
\]

Thus \(u\) is an exact weak solution despite lacking a classical second derivative at the interface. Its energy is

\[
\tfrac12\int_0^1a|u'|^2\,dx=\frac23.
\]

### Why weak is exact, not approximate

A weak derivative \(w\) of \(u\) satisfies \(\int u\phi'=-\int w\phi\) for all \(\phi\in C_c^\infty(0,1)\). The weak equation for \(-(a u')'=f\) is \(\int a u'v'=\int fv\) for all \(v\in H_0^1\). A finite-element approximation satisfies it only for \(v\) in a chosen *finite* subspace; the exact weak solution satisfies all admissible tests.

### Exercises with answers

1. **Uniqueness:** If \(u_1,u_2\) share the same boundary values and \(b(u_i,v)=\ell(v)\), show \(u_1=u_2\). **Answer:** Test the difference equation with \(u_1-u_2\), use \(\alpha>0\), then zero boundary trace.
2. **Interface:** If the left half has stiffness \(k_1\) and right half \(k_2\), and the total height difference is one, what is the flux? **Answer:** \(q=2/(1/k_1+1/k_2)\).
3. **Energy:** Check \(\frac12\int a|u'|^2=2/3\) for the exact two-material solution. **Answer:** Half of \((1/2)(16/9)+(1/2)(2)(4/9)\) equals \(2/3\).
4. **Failed assumption:** What breaks if \(a(x)=0\) on a whole subinterval? **Answer:** Strict coercivity can fail; directions supported in that region have zero derivative energy.

### Sources and further reading

- Luca Heltai, [*Model Problems and the Ritz–Galerkin Method*](https://luca-heltai.github.io/nmpde/lectures/lecture-01/), especially its Lax–Milgram assumptions and variational framework.
- [*A primer on finite element methods*](https://www.math.ntnu.no/emner/MA8502/2024h/lectures/html/chapter_02/galerkin_methods.html), NTNU, for weak solutions, test spaces, and Galerkin stability.
- [Wikipedia: Weak solution](https://en.wikipedia.org/wiki/Weak_solution), [Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), and [Lax–Milgram theorem](https://en.wikipedia.org/wiki/Lax%E2%80%93Milgram_theorem), for introductory definitions.

*Teaching connections:* `differential-equations:010000` introduces weak equations and PDE evolution; `analysis:survey` provides the analytic background; `multivariable-calculus:031000`–`032000` explain how the weak equation arises as a first variation including boundary terms.
