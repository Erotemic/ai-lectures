# 038000 — Algebraic Curves, Genus, and Riemann–Roch

**Track:** Abstract Algebra. **Background:** smooth projective curves, divisors, line bundles, rational functions. **Central question:** how many independent rational functions can have poles bounded by a divisor?

<!-- BEGIN SPOKEN LECTURE -->

# Algebraic Curves, Genus, and Riemann–Roch

Suppose you are allowed to build a rational function on a curve, but you must obey a strict rule about its poles. At one point you may allow a pole of order two; at another you forbid poles altogether. How many linearly independent functions meet those constraints?

On the projective line, the answer is almost embarrassingly concrete. Permit a pole of order at most three at infinity and no poles elsewhere. Then every allowable rational function is a polynomial of degree at most three. The functions one, x, x squared, and x cubed form a basis. Four degrees of freedom come directly from the pole allowance, plus a constant.

But most smooth projective curves are not projective lines. A torus-shaped complex algebraic curve, for example, has rational functions that obey subtler restrictions. A prescription for poles might not be realizable by the number of functions suggested by simple counting. Riemann–Roch identifies the precise correction.

## Turning a pole budget into a vector space

Let C be a smooth, projective, connected algebraic curve over an algebraically closed field. Specify a divisor D: finitely many points with integer coefficients. For each nonzero rational function f, count the order of f at each point. A positive order means a zero; a negative order means a pole.

The condition that the divisor of f plus D be effective means that every pole of f is allowed by the budget D. Together with zero, the eligible functions form a vector space, conventionally called L of D. Its dimension is denoted little ell of D.

The degree of D is the sum of its coefficients. It seems plausible that permitting one additional pole order should add one degree of freedom. On the projective line, that intuition works. On an arbitrary curve, it needs a correction depending on the genus, a global invariant describing the curve's topology over the complex numbers and, algebraically, the dimension of a first cohomology group.

## The hidden constraints

There is a special divisor K, called canonical, arising from differential one-forms. A meromorphic differential may have zeros and poles, just as a rational function does. The degree of K is twice the genus minus two.

Riemann–Roch says: the dimension of L of D, minus the dimension of L of K minus D, equals the degree of D plus one minus the genus. The second term is not an arbitrary nuisance. It measures a dual family of constraints. In the language of sheaves, it is the dimension of the first cohomology group of the line bundle associated with D.

Why should a dual space appear? A list of local pole conditions does not guarantee that the locally allowable expressions fit together into a global rational function. The missing functions are measured by a global obstruction. On curves, duality identifies that obstruction with differential forms satisfying a complementary bound.

When D has degree greater than twice the genus minus two, the divisor K minus D has negative degree. A nonzero rational function cannot have an effective divisor of negative degree. The correction therefore vanishes, and the simple answer returns: the space of allowed functions has dimension degree D plus one minus genus.

## Three curves, three kinds of behavior

On the projective line, genus is zero and a canonical divisor has degree minus two. For a divisor consisting of m times the point at infinity, the allowable functions are exactly polynomials of degree at most m, when m is nonnegative. There are m plus one of them. Riemann–Roch reproduces that answer.

On a genus-one curve, the canonical divisor has degree zero. Any divisor of degree one has one independent global section. One degree of allowed pole does not suddenly yield a nonconstant function, because the constant function already uses that dimension. Indeed, a nonconstant rational function with exactly one simple pole on a smooth projective genus-one curve would give a degree-one map to the projective line, forcing the curve itself to be the projective line. That is impossible.

For a curve of genus two, a canonical divisor has degree two. Give a divisor degree five. It exceeds twice the genus minus two, so the correction vanishes and the allowable function space has dimension four. The genus has effectively removed two degrees of freedom relative to the naïve projective-line count.

## What the theorem does and does not count

Riemann–Roch counts dimensions, not individual functions. It also does not say that two divisors of the same degree have identical spaces of functions when the correction term can be nonzero. The exact geometry and divisor class matter in the small-degree range. Nor can one freely carry this curve formula over to higher-dimensional varieties: there, more cohomology groups appear, and a different theory is needed.

The striking part is that one global invariant, genus, and one dual correction govern an enormous collection of local pole problems. Algebraic curves become accessible through linear algebra, yet the formula knows exactly where linear counting alone fails. That is the bridge from divisors to cohomology.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let C/k be a smooth, projective, geometrically connected curve over an algebraically closed field k, of genus g. For D in Div(C), define
\[L(D)=\{0\}\cup\{f\in k(C)^*: \operatorname{div}(f)+D\geq0\},\qquad \ell(D)=\dim_kL(D).\]
If K is a canonical divisor, then **Riemann–Roch** states
\[\ell(D)-\ell(K-D)=\deg D+1-g.\]
By Serre duality, \(\ell(K-D)=h^1(C,\mathcal O_C(D))\), and \(\deg K=2g-2\). For \(\deg D>2g-2\), \(\deg(K-D)<0\), hence \(\ell(K-D)=0\), yielding \(\ell(D)=\deg D+1-g\). For any divisor of negative degree, \(\ell(D)=0\).

**Projective line:** g=0, \(K\sim-2[\infty]\), and \(L(m[\infty])=\operatorname{span}_k\{1,x,\ldots,x^m\}\) for \(m\geq0\), so \(\ell=m+1\). **Genus one:** \(K\sim0\); for any degree-one D, \(\ell(D)=1\). **Genus two:** degree-five D has \(\ell(D)=4\).

**Why genus occurs.** The Euler characteristic of the invertible sheaf satisfies
\[\chi(C,\mathcal O_C(D))=h^0-h^1=\deg D+1-g.\]
This equality follows from the curve version of Riemann–Roch; proving it in general uses tools such as duality and local-to-global cohomology. It is not established merely by counting the poles individually.

### Exercises with answers

1. Find \(\ell(6[\infty])\) on \(\mathbf P^1\). **Answer:** 7, represented by polynomials of degree at most six.
2. For genus four, what is \(\ell(D)\) when \(\deg D=10\)? **Answer:** 10+1-4=7 because 10>2g-2=6.
3. Can a divisor of degree minus one have a nonzero global section? **Answer:** no, since an effective divisor has nonnegative degree and principal divisors have degree zero.
4. Why is \(\ell(D)\) not generally determined by degree alone? **Answer:** the correction \(\ell(K-D)\) can depend on the divisor class.

### Reading and source notes

- [Stacks Project, Riemann–Roch](https://stacks.math.columbia.edu/tag/0B5B), including the cohomological formulation.
- [Stacks Project, Algebraic Curves chapter](https://stacks.math.columbia.edu/tag/0BRV), for genus, canonical divisors, and linear series.
