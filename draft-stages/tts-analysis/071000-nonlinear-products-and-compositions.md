# 071000 — Nonlinear Products in Sobolev Spaces: When Multiplication Is Safe
**Track:** Analysis from First Principles. **Background:** L-p spaces, basic Hilbert spaces and weak derivatives as introduced earlier in this course. **Central question:** What assumptions make this construction rigorous?

<!-- BEGIN SPOKEN LECTURE -->
# Nonlinear Products in Sobolev Spaces: When Multiplication Is Safe

In a linear differential equation, adding two solutions often creates another solution. In a nonlinear equation, the solution may be squared or cubed, multiplied by its own derivative, or passed through a nonlinear function. Before we can solve such an equation, we need a basic test: if the unknown belongs to our chosen function space, does the nonlinear expression belong to the space we need? This question is about products, not about clever algebraic manipulations.

For ordinary numbers, a product is easy to bound. The magnitude of a product equals the product of the magnitudes. For functions, we must specify which norm measures size. If one function is bounded in absolute value and the other is square-integrable, their product is square-integrable: the first function can be pulled out as a maximum. But if both functions are merely square-integrable, their product is guaranteed only to be integrable. That may be too weak for a differential equation posed in L two.

A simple example exposes the difficulty. On a short interval near zero, a function can be square-integrable while becoming arbitrarily large at zero. Two copies of the same function may produce a square that is no longer square-integrable. Thus an L-two space is not automatically closed under multiplication. We cannot assume that a nonlinear map preserves a function space just because each term can be written down pointwise.

Derivative information can rescue the situation. On a bounded interval, a first-order Sobolev function has a continuous representative, and its maximum is controlled by its Sobolev norm. If two such functions are multiplied, their product has a weak derivative given by the familiar product rule. Each derivative term is a bounded function times a square-integrable derivative. The result belongs to the same first-order Sobolev space, with a product norm bounded by a constant times the product of the original norms. We say this Sobolev space is an algebra under pointwise multiplication.

We can use that statement to study a cubic nonlinear term. Suppose a function u belongs to the first-order Sobolev space on a bounded interval. Its cube also belongs to the space. More importantly, on a bounded ball of that space, taking cubes is locally Lipschitz. To compare the cubes of u and v, factor their difference into u minus v times a sum of quadratic terms. Apply the product estimate. The result is a constant depending on the size of the ball, multiplied by the Sobolev distance between u and v. This is exactly the kind of estimate a fixed-point theorem needs.

The same argument does not work without change in high dimensions. First-order Sobolev regularity no longer guarantees a bounded representative when the dimension is large enough. In two dimensions, first-order L-two control does not by itself give a uniform pointwise bound; in three dimensions, the situation is still more restrictive. Products that preserve H-one in one dimension may fail to preserve H-one in three dimensions.

That does not mean all cubic nonlinearities fail in higher dimensions. We can choose different input and output spaces. In three dimensions, Sobolev embedding puts a first-order L-two function in L-six. Cubing it gives an L-two function. So the cubic map makes sense from H-one to L-two, and on bounded sets it is locally Lipschitz with respect to suitable norms. But this is not the same as saying the cube lies in H-one. Choosing the correct target space is part of designing a proof.

It is tempting to say that smooth nonlinear functions always preserve Sobolev regularity. The honest statement requires bounds on the argument, differentiability of the nonlinear function, and careful use of a chain rule. For instance, the derivative of the sine of u is cosine of u times the derivative of u, which is safe because cosine is bounded. For a polynomial, the derivative involves powers of u that may not be bounded. The dimension and the Sobolev order decide what estimates are available.

This is one reason nonlinear PDEs can be harder than linear PDEs even before questions of blow-up or instability arise. The first obstacle is closing the estimates: can we map a candidate solution back into a space where the equation makes sense? Once that is true, a second obstacle appears: can we bound the difference between two nonlinear terms strongly enough to prove uniqueness or to drive an iterative construction?

A good way to read a nonlinear PDE proof is to underline the line where a product estimate or composition estimate is used. Ask what dimension is assumed, what Sobolev exponent is present, and which output norm is controlled. Those details determine whether the subsequent existence argument is legitimate.
<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On a bounded interval \(I\), \(H^1(I)\hookrightarrow L^\infty(I)\). Using \((uv)'=u'v+uv'\) in the weak sense,
\[\|uv\|_{H^1(I)}\le C_I\|u\|_{H^1(I)}\|v\|_{H^1(I)}.\]
Thus \(H^1(I)\) is a Banach algebra. If \(\|u\|_{H^1},\|v\|_{H^1}\le R\), then
\[\|u^3-v^3\|_{H^1}\le C_{I,R}\|u-v\|_{H^1},\]
from \(u^3-v^3=(u-v)(u^2+uv+v^2)\).

A failure in \(L^2(0,1)\): \(u(x)=x^{-1/3}\) lies in L-two because \(\int_0^1x^{-2/3}dx<\infty\), but \(u^2=x^{-2/3}\notin L^2\) because \(\int_0^1x^{-4/3}dx=\infty\).

In \(d=3\), \(H^1(\mathbb R^3)\hookrightarrow L^6\); \(u^3\in L^2\) with \(\|u^3\|_2\le C\|u\|_{H^1}^3\), while \(H^1\) is not generally an algebra under multiplication. Local Lipschitz into L-two follows from Hölder and the factorization of cubes.

### Exercises with answers

1. **L-two failure.** Check whether \(x^{-1/3}\) and its square lie in L-two on \((0,1)\). **Answer:** The original does; its square does not.
2. **Product rule.** What is the weak derivative of \(uv\) for \(u,v\in H^1(I)\)? **Answer:** \(u'v+uv'\), since both products are in L-two by the one-dimensional embedding.
3. **Dimension.** Why can the same proof fail in three dimensions? **Answer:** H-one no longer embeds into L-infinity, so the product estimate used in one dimension is unavailable.

### Reading and source notes

- [John K. Hunter, Notes on Nonlinear Evolution Equations, Sobolev and Gagliardo–Nirenberg inequalities](https://www.math.ucdavis.edu/~hunter/notes/nonlinev.pdf)
- [Di Nezza, Palatucci and Valdinoci, Fractional Sobolev spaces](https://www.instmath.rwth-aachen.de/~heiko/lehre/varisemWS11-12/hitchikers_guide_fractional_sobolev_4_2011.pdf)
