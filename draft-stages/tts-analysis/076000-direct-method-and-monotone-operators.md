# 076000 — The Direct Method and Monotone Operators: Nonlinear Existence Without a Contraction
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# The Direct Method and Monotone Operators: Nonlinear Existence Without a Contraction

Not every nonlinear problem can be solved by making an iteration contract. Some nonlinearities are too steep, some maps are not sufficiently Lipschitz, and some natural solution spaces do not support the desired fixed-point estimate. There is another strategy: instead of repeatedly applying a map, find the state that minimizes a suitable energy.

Imagine a stretched elastic string, fixed at both ends, under an external load. Its potential energy includes a term that penalizes slopes. A large gradient costs energy, so the string resists sharp bends. If the string also experiences a nonlinear restoring force, we can add a positive quartic term to the potential. Finally the load contributes a term that rewards movement in the direction of the applied force. The equilibrium should minimize the combined energy.

Why is a minimum likely to exist? First we need a lower bound. Without one, the energy could keep decreasing without reaching a finite value. For a string fixed at both ends, Poincaré's inequality controls its overall size by the size of its derivative. Thus a sufficiently positive quadratic derivative term eventually dominates the linear work done by a fixed square-integrable load. The quartic term is also nonnegative. As the Sobolev norm grows, the energy grows. We call this coercivity.

Choose a sequence of string shapes whose energies approach the infimum. Coercivity prevents the sequence from running off to infinite Sobolev norm. Because this Sobolev space is reflexive, a bounded sequence has a weakly convergent subsequence. We now have a candidate limiting shape. The next task is to show that the limit does not have larger energy than the values approaching the infimum. This is weak lower semicontinuity, supplied here by convexity of the derivative and quartic terms and continuity of the load pairing.

If those ingredients hold, the limit actually minimizes the energy. We have constructed an equilibrium without solving a differential equation explicitly. The differential equation emerges when we vary the minimizer slightly and require that the first variation of energy vanish. The quadratic gradient term becomes the negative second derivative in the weak sense; the quartic potential contributes a cubic restoring force; and the external load appears on the other side. We arrive at a nonlinear boundary-value problem for the string.

There is also a way to understand uniqueness. The cubic function is increasing. If two candidate solutions are subtracted and the difference equation is tested against their difference, the gradient term is nonnegative. The cubic difference times the difference of its arguments is also nonnegative. The sum can vanish only when the two candidates are identical, once the zero boundary condition is imposed. This is a monotonicity argument, not a contraction argument.

Monotonicity generalizes the simple fact that an increasing scalar function preserves order. A nonlinear operator is monotone when the difference between its outputs has a nonnegative dual pairing with the difference between its inputs. Strict monotonicity may give uniqueness. Coercivity and suitable continuity properties can give existence by theorems associated with Minty and Browder. These theorems provide a general framework for nonlinear elliptic equations and convex optimization.

But convexity matters. A nonconvex energy can have multiple local minima and saddle points. A minimizing sequence might approach a global minimum, yet a different stationary point could also solve the Euler–Lagrange equation. Critical points are not automatically global minimizers. We should keep separate the claims of existence of a minimizer, uniqueness of a minimizer, and existence of arbitrary solutions to the stationary equation.

There is another distinction between the weak and classical formulations. A Sobolev minimizer initially satisfies an integral identity against test functions. Extra regularity is needed before we can interpret its second derivative pointwise. In a one-dimensional string problem, that additional smoothness is often obtainable for smooth loads. In rough domains or with rough coefficients, it may fail. The variational construction itself does not require classical second derivatives from the outset.

The direct method is a model of existence by compactness: bounded minimizing sequences, weak convergence, and lower semicontinuity. A fixed-point theorem is a model of existence by contraction: a map that repeatedly improves guesses. Energy estimates and monotonicity help establish uniqueness and stability. Together these approaches form a basic toolkit for understanding nonlinear equations, even when no closed-form solution is available.
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(I=(0,1)\) and \(f\in L^2(I)\), define \(J:H^1_0(I)\to\mathbb R\) by
\[J(u)=\frac12\int_I|u'|^2dx+\frac14\int_Iu^4dx-\int_Ifu\,dx.\]
In one dimension \(H^1_0(I)\hookrightarrow L^4(I)\). Poincaré and Young imply coercivity. The convex terms are weakly lower semicontinuous, and the load term is weakly continuous. By reflexivity and the direct method, J has a minimizer. Its first variation gives
\[\int_Iu'v'\,dx+\int_Iu^3v\,dx=\int_Ifv\,dx\qquad(v\in H^1_0(I)),\]
which is the weak form of \(-u''+u^3=f\) with zero trace.

If u and w solve the same problem, subtract and test by u-w:
\[\int_I|u'-w'|^2dx+\int_I(u^3-w^3)(u-w)\,dx=0.\]
Both integrands are nonnegative, so u=w. More generally an operator \(A:X\to X^*\) is monotone if \(\langle Au-Av,u-v\rangle\ge0\). The Minty–Browder theory supplies nonlinear existence under reflexivity, coercivity, monotonicity and suitable hemicontinuity assumptions; these hypotheses must not be omitted.

### Exercises with answers

1. **First variation.** What is the derivative of \(\frac14\int u^4\) in direction v? **Answer:** \(\int u^3v\).
2. **Monotonicity.** Why is \((a^3-b^3)(a-b)\ge0\) for real a,b? **Answer:** \((a-b)^2(a^2+ab+b^2)\ge0\).
3. **Counterexample.** Does every critical point of a nonconvex energy minimize it? **Answer:** No; a local maximum or saddle can also have zero first derivative.

### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, weak and variational problems](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [MIT OpenCourseWare, Introduction to Functional Analysis, weak compactness](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
