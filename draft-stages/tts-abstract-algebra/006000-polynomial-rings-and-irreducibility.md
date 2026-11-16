# 006000 — Polynomial Rings, Factorization, and Irreducibility

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** rings, ideals, quotients, and the Euclidean algorithm for integers. **Question:** why can a polynomial become zero without collapsing the whole arithmetic system?

<!-- BEGIN SPOKEN LECTURE -->

# Polynomial Rings, Factorization, and Irreducibility

Suppose we want a number whose square is two. Inside the rational numbers, no such number exists. We could simply introduce a symbol called the square root of two and begin calculating, but how can we know which calculations remain legitimate? How can we ensure that dividing by a nonzero expression will not produce a contradiction?

Polynomial arithmetic provides a systematic answer. We can make a new field in which the polynomial x squared minus two equals zero. The crucial condition is that the polynomial be irreducible: it cannot be factored into two polynomials of smaller positive degree over the original field.

## Polynomials as arithmetic objects

A polynomial over a field F is a finite expression formed from a variable x with coefficients in F. We add coefficients of like powers, and multiply by distributing and collecting powers. It is important that x is initially a formal variable: an expression in the polynomial ring is not yet the result of plugging in a number. Two polynomials are equal when their coefficient lists agree.

Degree measures the highest power with nonzero coefficient. For nonzero polynomials over a field, the degree of a product is the sum of the degrees. We need the nonzero condition because the zero polynomial has no ordinary degree, and we need a field—or at least an integral domain—to avoid a leading coefficient disappearing through multiplication.

The first surprise is that polynomials over a field have their own division algorithm. Given a polynomial f and nonzero g, there are unique polynomials q and r such that f equals q g plus r, with r zero or having smaller degree than g. The reason is the same as long division. Divide the leading coefficient of f by the leading coefficient of g, subtract an appropriate multiple of g to cancel the leading term, and repeat. Each step decreases degree, so the process terminates.

For a simple example, divide x squared plus one by x minus two, working over the rational numbers. The quotient is x plus two, because multiplying x minus two by x plus two gives x squared minus four. The remainder is five. Replacing x by two therefore gives five. This is the remainder theorem: division by x minus a leaves remainder f evaluated at a.

## Roots, factors, and the limits of the root test

A polynomial has a root a in F exactly when x minus a divides it. One direction follows by evaluation. For the other, polynomial division writes f as the product of x minus a and some q, plus constant remainder f of a. If the remainder vanishes, the division is exact.

A nonconstant polynomial is reducible over F if it is a product of two polynomials each of positive degree. Otherwise it is irreducible. For a degree-two or degree-three polynomial over a field, reducibility forces a linear factor, because two positive degrees adding to two or three must include a one. So for quadratic and cubic polynomials, finding or ruling out a root decides irreducibility.

But this test is not generally sufficient in degree four. The polynomial x to the fourth plus four, over the rationals, has no rational root, yet it factors as x squared minus two x plus two, multiplied by x squared plus two x plus two. Multiplying these expressions confirms the identity. This is an essential warning: no roots does not mean irreducible when the degree is at least four.

The field matters, too. The polynomial x squared minus two is irreducible over the rationals. If a reduced rational fraction a over b squared to two, then a squared would equal twice b squared, forcing a even and then b even, contradicting that the fraction was reduced. Over the real numbers, the same polynomial factors into linear terms using the square root of two. Irreducibility is always relative to a coefficient field.

## Greatest common divisors for polynomials

Because long division works in F of x, we can repeat the Euclidean algorithm. For two polynomials f and g, the last nonzero remainder, normalized to have leading coefficient one, is their greatest common divisor. Back substitution expresses that greatest common divisor as u f plus v g for some polynomials u and v.

This immediately tells us why irreducible polynomials play a role like prime integers. If p is irreducible and does not divide a, their greatest common divisor must be one. Bézout's identity gives polynomials u and v with u p plus v a equal to one. If p divides a b, reduce the identity times b modulo p. The term involving p vanishes; because a b is divisible by p, the remaining term forces p to divide b. Thus irreducibles satisfy Euclid's lemma in a polynomial ring over a field.

It follows by induction that every nonzero nonconstant polynomial factors into irreducibles, with the factors unique up to multiplication by nonzero constants and reordering. This is unique factorization in one variable over a field. The proof depends on the degree as a termination measure and Euclid's lemma as the uniqueness mechanism.

## A field made from a polynomial

Now take an irreducible polynomial p over F. Consider the quotient ring F of x modulo the ideal generated by p. Inside this quotient, p is equal to zero. The class of x acts like a new element alpha satisfying p of alpha equals zero.

Why is the quotient a field? Take any polynomial a whose class is nonzero. That means p does not divide a. Since p is irreducible, the greatest common divisor of p and a is one. Bézout gives u p plus v a equal to one. In the quotient the u p term vanishes, so the class of v is the inverse of the class of a. Every nonzero class has an inverse.

When p has degree n, the division algorithm also says every class has one unique representative of degree less than n. So the quotient is an n-dimensional vector space over F with basis the classes of one, x, up through x to the power n minus one. Here dimension is measuring how much arithmetic we added.

Take rational coefficients and p equal to x squared minus two. Every class has the form a plus b alpha, with rational a and b, and alpha squared equals two. Multiplication is controlled by this relation. The inverse of a plus b alpha, when the expression is nonzero, is a minus b alpha divided by a squared minus two b squared. The denominator is nonzero for rational a and b unless both vanish, because otherwise two would be the square of a rational number. This produces the field usually called Q adjoin square root of two.

An equally concrete example starts from the field with two elements. In that field, x squared plus x plus one has no root: plugging in zero gives one and plugging in one gives one. Being quadratic, it is irreducible. The quotient has four elements: zero, one, alpha, and one plus alpha. The defining relation says alpha squared plus alpha plus one equals zero; in characteristic two, subtraction and addition agree, so alpha squared equals alpha plus one. There is a field with four elements, even though there is no field formed by reducing ordinary integers modulo four.

## Repeated roots and derivatives

The formal derivative of a polynomial is computed by the familiar power rule. If f factors as x minus a squared times another polynomial, then both f and its derivative vanish at a. Conversely, over any field, if f and its derivative share a nonconstant factor, then f has a repeated irreducible factor in an algebraic closure. This gcd criterion is a useful algebraic test.

There is a subtlety in positive characteristic. In characteristic p, the derivative of x to the p minus c is identically zero, even though the polynomial need not be constant. Differentiation has not failed; coefficients such as p are zero in that field. Later field theory will distinguish separable and inseparable polynomials precisely because roots and derivatives behave differently in some characteristics.

Polynomial arithmetic has given us a method for adjoining new elements with controlled relations. Division, factorization, greatest common divisors, and quotients all work together. A root need not be found somewhere in the old field; it can be constructed in a larger one. The hard requirement is not that our symbol looks like a familiar number, but that the equations defining it are compatible with valid arithmetic.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(f,g\in F[x]\), \(g\ne0\), there are unique \(q,r\) with \(f=qg+r\) and \(r=0\) or \(\deg r<\deg g\). The factor theorem is
\[
(x-a)\mid f\quad\Longleftrightarrow\quad f(a)=0.
\]

**Counterexample to the root test in degree four:**
\[
x^4+4=(x^2-2x+2)(x^2+2x+2).
\]
It has no rational root but is reducible in \(\mathbb Q[x]\).

For irreducible \(p\in F[x]\) of degree \(n\),
\[
F[x]/(p)\text{ is a field},\qquad [F[x]/(p):F]=n.
\]
The degree claim uses representatives \(a_0+\cdots+a_{n-1}x^{n-1}\).

Example: \(\mathbb F_4=\mathbb F_2[\alpha]\) with \(\alpha^2+\alpha+1=0\), hence \(\alpha^2=\alpha+1\) and \(\alpha(\alpha+1)=1\).

### Exercises with answers

1. Divide \(x^3+1\) by \(x+1\). **Answer:** quotient \(x^2-x+1\), remainder zero.
2. Is \(x^2+x+1\) irreducible over \(\mathbb F_2\)? **Answer:** yes; neither field element is a root.
3. In \(\mathbb Q(\sqrt2)\), invert \(1+\sqrt2\). **Answer:** \(\sqrt2-1\), since their product is one.
4. Is \(x^2-1\) irreducible over \(\mathbb Q\)? **Answer:** no, it factors as \((x-1)(x+1)\); the corresponding quotient is not a field.

### Reading

Judson, *Abstract Algebra: Theory and Applications*, polynomial rings and fields; Keith Conrad, [Expository papers](https://kconrad.math.uconn.edu/blurbs/), irreducibility tests, roots, and irreducible polynomials.
