# 075000 - Gamma Classes and Integral Structures in Quantum Cohomology

**Track:** Abstract Algebra. **Background:** characteristic classes, projective varieties, quantum cohomology, and flat connections. **Central question:** how can an enumerative quantum connection remember an integral lattice rather than only a complex vector space?

<!-- BEGIN SPOKEN LECTURE -->

# A complex differential equation can forget its arithmetic

A quantum differential equation is usually written over the complex numbers. Its solutions form a complex vector space, and analytic continuation moves those solutions around as parameters vary. But a complex vector space does not single out which linear combinations should count as integral. Two bases related by an arbitrary invertible complex matrix look equally legitimate from the differential equation alone.

Geometry often supplies more structure. An algebraic variety has vector bundles and coherent sheaves, and their K-theory classes form a lattice. Quantum cohomology, meanwhile, uses enumerative geometry to deform ordinary cup products. The question is whether K-theoretic information can be transported into the solution space of the quantum connection in a natural way.

The Gamma class is part of the answer. It modifies the more familiar characteristic classes through Euler's Gamma function. In suitable settings, this correction helps define an integral structure on the flat sections of a quantum connection. It also clarifies why integral monodromy statements are not automatic just because a differential equation came from algebraic geometry.

# Begin with ordinary cohomology of a line

Consider the complex projective line, the space of one-dimensional subspaces of a two-dimensional complex vector space. Its cohomology has a unit class and a class commonly called H, represented by a point in top degree. Multiplying H by itself gives zero in ordinary cohomology, because there is no cohomology in degree four on a complex curve.

Quantum cohomology changes exactly this relation. Curves of positive degree contribute enumerative corrections, and the small quantum product satisfies H multiplied quantumly by H equals a parameter q. We obtain a two-dimensional algebra with relation H squared equals q. When q approaches zero, the classical nilpotent relation returns.

This toy model has enough structure to see the problem. Multiplication by H becomes a q-dependent matrix, and a quantum connection converts that matrix into a differential equation. The solutions carry monodromy and asymptotic data, but the equation itself still does not tell us which flat sections correspond to actual geometric K-theory classes.

# The K-theory lattice is not the cohomology basis

On the projective line, the classes of the structure sheaf and the degree-one line bundle give a natural integral basis of K-theory. Their Chern characters are related to the cohomology basis by exponential expressions. Already this shows that the naive integral lattice spanned by the unit and H is not the same object as the image of K-theory under the Chern character.

The difference grows in higher dimensions. Characteristic classes include rational coefficients, and the quantum connection introduces additional transcendental constants through its asymptotics. A simple identification of integral K-theory with integer coefficients in the cohomology basis would usually misrepresent the geometry.

What we need is a map that begins with a genuine K-class, applies characteristic-class corrections, and then uses a fundamental solution of the quantum connection to produce a flat section. The exact formula depends on grading and normalization conventions. The important ingredients are a Chern character, a Gamma-class factor, and the quantum connection's fundamental solution.

# Why the Gamma function appears

Euler's Gamma function extends the factorial through complex analysis. It also has a power-series expansion whose coefficients involve Euler's constant and special values of the zeta function. The Gamma class uses this function on the formal Chern roots of the tangent bundle.

For the projective line, the tangent bundle has first Chern class twice H. Since H squared is zero in ordinary cohomology, the Gamma class truncates after the linear term. In a standard convention it is one minus twice Euler's constant times H. This elementary calculation reveals something important: the correction is not an ordinary polynomial with integer coefficients, even in the smallest useful example.

In more dimensions, higher powers of Chern roots survive, and zeta values enter the coefficients. These are not decorative constants. They appear naturally in asymptotic solutions and in comparisons between different geometric descriptions of quantum cohomology. Integral structures built using the Gamma class are meant to respect that analytic information.

# Flatness and monodromy

A connection prescribes how vectors are transported when parameters change. A flat section is a vector-valued function whose covariant derivative vanishes. Continuing a flat section around a loop can return a different section, producing a monodromy transformation.

A complex connection has monodromy matrices in a complex general linear group after choosing a basis. If a geometric integral lattice of flat sections is preserved, the same transformation can be described by an integral matrix in the appropriate lattice basis. The lattice is additional structure; it is not visible from a random complex basis.

The Gamma-class construction gives a candidate bridge between K-theoretic automorphisms and analytic continuation. Under appropriate hypotheses, geometric operations on K-theory correspond to monodromy and Stokes transformations of the quantum connection. But precise integrality and categorical identifications are theorems or conjectures in specified settings, not unrestricted laws for every quantum differential equation.

# Where the derived category enters

Vector bundles are only part of the story. Derived categories organize coherent sheaves and the extensions between them. Their Grothendieck group gives K-theory, while exceptional collections can provide distinguished sets of classes. Quantum differential equations often admit special asymptotic bases, called Stokes bases, when singularities are irregular.

Gamma conjectures relate such analytic bases and asymptotic behavior to geometric and categorical structures for certain classes of varieties. These statements have been established in some important examples and remain conjectural in others. It is essential to distinguish the definition of a Gamma class from the truth of any proposed relationship with a particular exceptional collection.

The projective line gives a useful testing ground. Its derived category has simple line-bundle generators, and its quantum product can be written in a two-dimensional basis. One can calculate characteristic classes explicitly, solve the differential equation, and then examine whether the geometric lattice behaves as expected under continuation.

# A check that keeps conventions straight

The formula for the quantum product uses a coordinate q that measures curve degree. A fundamental solution also involves a parameter often called z, which plays the role of a grading or connection parameter. Different authors place z in different parts of the connection, use inverse fundamental solutions, and include powers of two pi i in the integral structure.

A safe comparison records these conventions before matching matrices. An apparent disagreement in signs, Gamma factors, or transposes can be a convention mismatch rather than a mathematical contradiction. The cohomology ring, K-theory lattice, and solution space are three distinct objects; a map between them must be specified rather than silently assumed.

A strong worked calculation should therefore include four steps: identify the K-class, compute its Chern character, multiply by the specified Gamma class, and then transport through the chosen quantum fundamental solution. Only after that should one ask whether resulting sections generate an integral monodromy-invariant lattice.

# What this construction contributes

The Gamma class places analytic constants into a setting that initially looked purely algebraic. It offers a route from enumerative curve counts to integral structures, asymptotic bases, and categorical symmetries. It also teaches a useful discipline: the complex differential equation is only one layer of the structure.

In the projective-line example, quantum multiplication replaces a nilpotent relation by H squared equals q. K-theory offers an integral basis not identical to the naive cohomology basis. The Gamma class supplies a transcendental correction, and the quantum connection turns corrected characteristic data into flat sections. Understanding how these pieces fit gives more than a formula; it shows how topology, arithmetic, and asymptotic analysis can occupy the same mathematical object.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For `X=P^1`, write `H in H^2(X,Z)` with `H^2=0` in ordinary cohomology and `c_1(TX)=2H`. Small quantum cohomology has `H*H=q`. Its multiplication operator in basis `(1,H)` is
\[
M_H=\begin{pmatrix}0&q\\1&0\end{pmatrix},\qquad
M_H\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}qb\\a\end{pmatrix},
\quad H*(a+bH)=qb+aH.
\]
under the stated column convention. The Gamma class of the tangent bundle is
\[
\widehat\Gamma_X=\Gamma(1+2H)=1-2\gamma H
\]
using the ordinary cohomology relation `H^2=0` and `Gamma'(1)=-gamma` (Euler's constant). This calculation is independent of which quantum product convention is used.

`K^0(P^1)` has integral generators `[O]` and `[O(1)]`, whose Chern characters are `1` and `1+H`. A Gamma-integral structure involves corrected Chern characters and quantum fundamental solutions, plus normalization/gradation factors that must be specified before making exact monodromy matrix claims. The gamma conjectures and categorical identifications require individual hypotheses and are not general consequences of the definition.

### Exercises with answers

1. Why does the series for `Gamma(1+2H)` truncate after a linear term on `P^1`? **Answer:** `H^2=0` in ordinary cohomology.
2. What is `ch(O(1))` on `P^1`? **Answer:** `e^H=1+H`.
3. Does `H*H=q` hold in ordinary cup cohomology? **Answer:** no; ordinary `H cup H=0`.
4. Why must a monodromy lattice be specified in addition to a complex connection? **Answer:** arbitrary complex changes of basis do not preserve integrality.

### Reading and source notes

- [Iritani, Gamma Classes and Quantum Cohomology](https://arxiv.org/abs/2307.15938), modern review of Gamma-integral structures and gamma conjectures.
- [Iritani, Gamma Classes and Quantum Cohomology, ICM chapter](https://ems.press/books/standalone/276/5480), open-access treatment of integral structures and monodromy.
