# 067000 — Quantum Differential Equations and Mirror Periods

**Track:** Abstract Algebra. **Background:** cohomology rings, Gromov–Witten invariants, differential equations, and quantum cohomology. **Central question:** why can the multiplication table of a geometric space become a differential equation whose solutions resemble period integrals on another space?

<!-- BEGIN SPOKEN LECTURE -->

# When multiplication starts depending on a parameter

The ordinary cohomology of the complex projective line is very simple. It has a unit and one generator, often called H, representing the class of a point. Multiplying H by itself gives zero because the projective line has no cohomology in degree four. The entire multiplication table fits in a few words.

Now introduce the quantum product. It changes multiplication by counting holomorphic curves. The same symbol H multiplied by itself no longer vanishes. Instead it equals a parameter q, times the unit. This statement sounds strange. Why should multiplying two cohomology classes produce a number that remembers curves?

The parameter q records the degree of a curve. At q equal to zero, contributions from positive-degree curves disappear and we recover ordinary cohomology. At nonzero q, the geometry of maps from the sphere is allowed to correct the multiplication table. For the projective line the correction is as simple as it could be: H times H equals q.

One can view the quantum product as a family of algebras. The structure constants move with q, but associativity survives. That persistence is not automatic from an arbitrary deformation of an algebra. It rests on the gluing properties of moduli spaces of stable maps, encoded in identities among Gromov–Witten invariants.

# From a multiplication matrix to a connection

There is a second object hiding inside the multiplication table. Multiplication by H is a linear operator on the two-dimensional space spanned by the unit and H. If a vector is written as a coefficient of the unit and a coefficient of H, multiplying by H exchanges those components, with a factor of q in one direction.

The matrix has zeroes on its diagonal, q in the upper-right corner, and one in the lower-left. Instead of treating that matrix only as an algebraic operation, we make it the coefficient of a differential equation. Introduce another parameter, commonly called z. The quantum differential equation says that z times q times the derivative with respect to q of a section equals multiplication by H applied to that section.

This is a connection: a rule for transporting vectors as q changes. The connection contains the same quantum-product data, but asks a dynamic question. Given an initial vector, how does it evolve around a path in parameter space? Analytic continuation can have nontrivial monodromy, and solutions can have singular behavior near special values.

The transition is useful because differential equations come with a mature theory: regular and irregular singular points, asymptotic expansions, special functions, and monodromy representations. Enumerative geometry becomes accessible to those tools.

# Eliminate a component on the projective line

Write a section as a times the unit plus b times H. The quantum equation splits into two first-order equations. The derivative of a, with the prescribed q weighting and z factor, equals q times b. The corresponding derivative of b equals a.

Eliminate a. The second equation says a is z times q times the derivative of b. Substituting into the first gives a second-order differential equation. The square of z times the operator q times derivative with respect to q, applied to b, equals q times b.

This is a particularly transparent equation because it has a power-series solution with coefficients that can be computed recursively. Start with b equal to one at q equal to zero, then add a coefficient times q, another times q squared, and so on. At degree d, the weighted second derivative introduces d squared. The recurrence says that the coefficient at degree d is the coefficient at degree d minus one divided by z squared times d squared.

The resulting series has coefficients one divided by z to the power twice d times the square of d factorial. No curve counting appears explicitly in the recurrence, yet the series is determined by the quantum multiplication of the projective line. The factorials are the arithmetic fingerprint of the differential equation.

# Mirror symmetry offers another interpretation

Mirror symmetry predicts, and in many classes of examples proves, that solutions of quantum differential equations can be described using integrals associated with a mirror space or a Landau–Ginzburg potential. Instead of counting holomorphic maps to one space, one integrates an oscillatory expression on another.

For the projective line, a standard mirror potential has the form x plus q divided by x, where x is a nonzero complex coordinate. Integrals of the exponential of that potential divided by z, along suitable cycles with appropriate convergence or formal interpretation, satisfy a related differential equation.

This is not merely a similarity of formulas. Under the correct choice of cycles, normalization, and variables, the hypergeometric solutions from the quantum connection match mirror periods. The coefficients of a generating series of curve counts can therefore be found by solving a differential equation or evaluating a mirror integral. Which side is easier depends on the geometry.

But the word mirror must not conceal assumptions. The construction uses a specified mirror family, a chosen connection, and analytic or formal conventions. The projective line is an especially tractable toric example. One should not assume every variety has an equally elementary potential, or that every period integral counts curves without further identifications.

# A curve-counting identity is not a solution to every geometry problem

The equation knows something powerful and something limited. It knows quantum multiplication by H and its associated flat connection. It does not, by itself, tell us every higher-genus invariant, every derived-category correspondence, or every enumerative number of every target. Those require extra structures and arguments.

Nor does writing the series down automatically prove the enumerative interpretation. For the projective line the quantum ring is known independently, and the resulting power series is an exact consequence. In more involved targets, a mirror theorem identifies a candidate hypergeometric series with the geometric generating function, often after a change of coordinates called the mirror map.

The projective line gives a fully calculable bridge. A cohomology ring is corrected by curves. The corrected multiplication becomes a matrix. The matrix becomes a differential equation. The equation yields a factorial series. Mirror symmetry recovers related series through oscillatory integrals. Each transformation keeps track of the same geometry, but exposes a different kind of structure.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Small quantum cohomology of `P^1` over a Novikov ring has `QH^*(P^1)=Q[H,q]/(H*H-q)`, with grading `deg H=2`, `deg q=4`. In ordered basis `(1,H)`, multiplication by H is `M_H=[[0,q],[1,0]]`. Let `D=q d/dq`. The quantum connection in one standard sign convention is
\[
 zD\binom{a}{b}=\begin{pmatrix}0&q\\1&0\end{pmatrix}\binom{a}{b},\qquad zDa=qb,\quad zDb=a.
\]
Eliminating a yields `(zD)^2 b= q b`. Setting `b=\sum_{d\ge0}c_d q^d`, `c_0=1`, gives `z^2d^2 c_d=c_{d-1}` and
\[
 b(q,z)=\sum_{d\ge0}\frac{q^d}{z^{2d}(d!)^2}=I_0(2\sqrt q/z).
\]
Here `I_0` is the modified Bessel function of order zero, and this equality is an identity of power series. The other independent solution is logarithmic at q=0. The simple Landau–Ginzburg mirror potential is `W(x)=x+q/x` on `C^*`; the relation to oscillatory integrals depends on cycles, z and sign conventions, and is not merely an arbitrary contour integral.

### Exercises with answers

1. Compute `H*H*H` in the small quantum ring. **Answer:** `qH` by associativity.
2. What is the coefficient of `q^3` in b when z=1? **Answer:** `1/(3!)^2=1/36`.
3. Why does setting q=0 recover ordinary cohomology? **Answer:** positive-degree curve corrections are suppressed and `H^2=0`.
4. Does the projective-line differential equation determine all higher-genus invariants? **Answer:** no, it encodes a genus-zero small quantum connection and requires additional structures for other enumerative theories.

### Reading and source notes

- [A. Givental, A mirror theorem for toric complete intersections](https://arxiv.org/abs/alg-geom/9701016), hypergeometric solutions of quantum differential systems and mirror identifications.
- [Alexander Givental, research and tutorial bibliography](https://math.berkeley.edu/~giventh/), quantum cohomology and mirror-period constructions.
- [Givental, Permutation-equivariant quantum K-theory VI: Mirrors](https://arxiv.org/abs/1509.07852), review of cohomological mirrors in the setting of toric varieties.
