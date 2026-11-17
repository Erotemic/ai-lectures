# 025500 — Frobenius, Subfields, and Testing Irreducibility

**Track:** Number Theory from First Principles. **Background:** construction and uniqueness of finite fields, polynomial gcds, Möbius inversion. **Aim:** prove Frobenius-orbit and subfield structure, count irreducible polynomials, and derive a practical irreducibility criterion.

<!-- BEGIN SPOKEN LECTURE -->

# Frobenius, Subfields, and Testing Irreducibility

We can build a field with eight elements by adjoining a root of an irreducible cubic over the two-element field. We can build fields of every prime-power size, and any two fields of the same size are isomorphic. Those facts raise a practical question. Given a large polynomial over a finite field, how can we know whether it is irreducible without attempting every possible factorization?

The answer begins with an operation that looks almost too simple to be useful: raise every element to the power equal to the size of the starting field. This operation is called the Frobenius map. It connects field arithmetic, polynomial roots, the geometry of finite extensions, and an efficient way to certify irreducibility.

We will work over a field with q elements, where q is a power of a prime p. This includes ordinary prime fields and extension fields. Suppose we have an extension with q to the n elements. We will show how Frobenius acts there, which smaller fields it contains, how irreducible polynomials are distributed by degree, and how to detect an irreducible polynomial by modular exponentiation and gcds.

## Why raising to the q-th power is a symmetry

In characteristic p, the p-th power of a sum is the sum of the p-th powers. That follows from the binomial theorem: all intermediate binomial coefficients are divisible by p. Apply the same identity repeatedly when q is a power of p. We obtain that the q-th power of a plus b equals a to the q plus b to the q.

The q-th power also preserves products and the multiplicative identity. Therefore the map sending a to a to the q is a field homomorphism. It is injective because if a to the q and b to the q are equal, then a minus b has q-th power zero, so a equals b. On a finite field, an injective map is automatically surjective. Thus this homomorphism is an automorphism: a perfect internal symmetry of the field.

On the original field with q elements, every element is fixed by the map. For nonzero a, its multiplicative order divides q minus one, so a to the q equals a. Zero is fixed as well.

On a larger field, the map may move elements. In our eight-element field over F two, alpha satisfies alpha cubed equals alpha plus one. The Frobenius map raises alpha to the second power. It takes alpha to alpha squared, then to alpha to the fourth, and then to alpha to the eighth. But alpha to the eighth equals alpha, because alpha is nonzero and its seventh power is one. So alpha travels around a cycle of length three.

That cycle is not just a numerical curiosity. It tells us something about the polynomial of alpha. The elements alpha, alpha squared and alpha to the fourth are roots of the same irreducible cubic. Their product as linear factors gives a polynomial with coefficients in the two-element field, even though the individual roots lie in the larger field.

## Frobenius cycles recover minimal polynomials

Take an element alpha in a finite extension of F q. Apply Frobenius repeatedly: alpha, alpha to the q, alpha to the q squared, and so on. Because the field is finite, eventually a value repeats. And because Frobenius is invertible, the first repetition closes a cycle returning to alpha. Let d be the length of that cycle.

Construct a polynomial by multiplying one linear factor for each member of the cycle: x minus alpha, x minus alpha to the q, continuing up to the last distinct conjugate. Its coefficients are fixed under Frobenius, because Frobenius merely rotates the factors. The elements fixed by the q-th-power map are precisely the q elements of the base field: they are exactly the roots of x to the q minus x. So our product polynomial has coefficients in F q.

There is a deeper statement. The polynomial just built is the **minimal polynomial** of alpha over F q. If any polynomial with coefficients in the base field vanishes at alpha, then applying Frobenius shows that it also vanishes at every member of alpha's cycle. A polynomial with d distinct roots must have degree at least d. But our product has degree d and already vanishes at alpha. It is therefore the unique monic polynomial of smallest degree annihilating alpha, and is irreducible.

For the eight-element example, alpha has a three-element Frobenius orbit. The cubic x cubed plus x plus one is its minimal polynomial, so the orbit consists exactly of its three roots in the eight-element field. We have not guessed the other roots; Frobenius generated them for us.

Now take an element already in F q. Frobenius fixes it on the first step, so its minimal polynomial has degree one. More generally, an element has minimal-polynomial degree d exactly when its Frobenius orbit has length d. This gives a computational interpretation of polynomial degree, not just an algebraic definition.

## A hierarchy of fields inside fields

The extension field with q to the n elements has an especially regular set of subfields. For every positive divisor d of n, there is a unique subfield with q to the d elements. And there are no such subfields for values of d that fail to divide n.

Why do divisors appear? If a subfield has q to the d elements, then our large field is a vector space over that subfield. Its number of elements is q to the d raised to an integer dimension. Since the large field has q to the n elements, d must divide n. This proves necessity.

For sufficiency, assume d divides n. The polynomial x to the q to the d minus x has exactly q to the d distinct roots in a splitting field. Every such root also satisfies x to the q to the n equals x, because repeated q to the d powers eventually reach the q to the n power. Therefore those roots already lie inside the field with q to the n elements. As in the existence proof, the root set is closed under the field operations. It is our desired subfield.

Why is it the only one? Every element of a subfield with q to the d elements must satisfy x to the q to the d equals x. Thus that subfield is contained in the root set we just constructed. Both contain exactly q to the d elements, so they coincide.

For example, the field with sixteen elements contains the field with four elements, because two divides four when we view sixteen as two to the fourth and four as two to the second. But it does not contain the field with eight elements, because three does not divide four. The field with sixty-four elements contains both the four-element and eight-element fields, since two and three both divide six.

This is already a miniature version of a general phenomenon from field theory: inclusions of fields correspond to algebraic symmetries. Here the correspondence can be read off from exponents and Frobenius powers without introducing the full language of Galois groups.

## Factor a famous polynomial without finding all its coefficients

Consider x to the q to the n minus x, this time as a polynomial over F q. Its roots are exactly the elements of the field with q to the n elements. Its derivative is negative one, so no root occurs twice.

Now take a monic irreducible polynomial f over F q of degree d. Adjoin one root alpha. The resulting field has q to the d elements, and every element there satisfies a to the q to the d equals a. Frobenius therefore returns alpha after d steps, and not before, because its minimal polynomial has degree d.

Thus alpha is a root of x to the q to the n minus x precisely when d divides n. Equivalently, the irreducible polynomial f divides that big polynomial precisely when its degree divides n.

We arrive at an exact factorization statement: x to the q to the n minus x is the product, each occurring once, of **all monic irreducible polynomials over F q whose degrees divide n**. In particular, this product is squarefree.

The statement is much more structured than a list of factors. A single polynomial of very high degree contains within it every irreducible of many smaller degrees, but only the degrees selected by divisibility.

For q equal to two and n equal to three, x to the eighth minus x has the two linear factors x and x plus one, along with exactly two irreducible cubic factors: x cubed plus x plus one, and x cubed plus x squared plus one. Two degrees appear, one and three, precisely the divisors of three.

For n equal to four, irreducible degrees one, two, and four appear. Degree three does not. If a cubic over the two-element field divided x to the sixteenth minus x, a root would generate an eight-element subfield of a sixteen-element field. We already proved that no such subfield exists. The factorization and subfield viewpoints are saying the same thing.

## Count irreducible polynomials using Möbius inversion

Let N sub q of n mean the number of monic irreducible polynomials of degree n over F q. We have an exact polynomial factorization, so we can compare degrees on both sides.

The left side has degree q to the n. On the right, every monic irreducible polynomial of degree d contributes d to the total, and d ranges over the positive divisors of n. Hence q to the n equals the sum, over d dividing n, of d times N sub q of d.

This is a divisor-sum relation. The Möbius inversion theorem applies directly. It gives n times N sub q of n equals the sum over divisors d of n of the Möbius function at d times q to the power n over d. Divide by n to obtain an exact count.

For cubics over F two, the divisors of three are one and three. The formula gives eight minus two, divided by three. That is two. We have already seen the two cubic polynomials. For quartics over F two, the result is sixteen minus four, divided by four, which is three. Thus exactly three monic irreducible quartics exist over the two-element field.

The formula can also be used to prove that irreducible polynomials exist in every positive degree, though the field-construction argument already did that. It gives more information: not just that at least one exists, but how many there are.

This is a striking appearance of Möbius inversion. The same tool that disentangles divisor sums in elementary number theory now disentangles the degree structure of polynomials. The base numbers q to the n are counting field elements, and inversion isolates the elements whose minimal polynomial has exactly degree n.

## From theory to an irreducibility test

Suppose someone hands us a monic polynomial f of degree n over F q and asks whether it is irreducible. Our factorization theorem leads to a test without brute-force trial division by every smaller polynomial.

First check that x to the q to the n is congruent to x modulo f. In other words, f divides x to the q to the n minus x. If that fails, f is not irreducible of degree n.

But that condition alone is insufficient. A product of several distinct irreducibles, each of degree dividing n, can also divide x to the q to the n minus x. We need to rule out all proper-degree factors.

For each distinct prime divisor r of n, compute the polynomial gcd of f with x to the q to the n divided by r minus x. Require this gcd to be one. Why do only prime divisors of n suffice? If f had an irreducible factor of degree d less than n, and d divided n, then n divided by d would exceed one. Some prime r divides n divided by d. Consequently d divides n divided by r, so that factor would divide x to the q to the n divided by r minus x, making the gcd nontrivial.

Conversely, an irreducible polynomial of degree n satisfies both tests. Its roots lie in the field with q to the n elements, but they do not lie in a smaller subfield with degree n divided by r for any prime divisor r of n. The gcd is one in every case.

This is commonly called Rabin's irreducibility criterion. It turns the question into modular polynomial exponentiation and Euclidean gcd computations, both operations we already know how to perform.

Over F two, take x cubed plus x plus one again. Since it is irreducible, x to the eighth is congruent to x modulo the cubic. The only prime divisor of degree three is three, so the auxiliary exponent is two to the first power. The gcd with x squared minus x is one, because the cubic has no root in F two. Both conditions pass.

Contrast this with x to the fourth plus x over F two. Every irreducible factor has degree one or two. Its factors are x, x plus one, and x squared plus x plus one. The polynomial does divide x to the sixteenth minus x, so it passes the first test. But its gcd with x to the fourth minus x is the entire polynomial, not one. The second condition catches the reducibility.

A practical caution: these tests concern irreducible polynomials over **finite fields**. A polynomial can be irreducible modulo one prime and reducible modulo another. And polynomial irreducibility is not the same task as testing whether an integer is prime, even if both employ modular arithmetic and finite fields.

## Trace and norm: summarize an extension element

There is one more valuable construction. Take an element alpha of the degree-n extension field F q to the n over F q. Add all its Frobenius conjugates, counting n terms: alpha plus alpha to the q plus alpha to the q squared, and so on. This sum is called the trace of alpha down to F q.

Instead of adding, multiply the same conjugates. This product is called the norm of alpha down to F q. Both lie in the base field because Frobenius cycles their factors or summands, leaving the result unchanged. The trace preserves addition, while the norm preserves multiplication.

For example, in the four-element field made by adjoining beta with beta squared plus beta plus one equal to zero, the trace of beta to F two is beta plus beta squared. Since beta squared equals beta plus one, the trace is one. Its norm is beta times beta squared, which is beta cubed, also one.

These operations generalize familiar constructions. The Gaussian norm of a plus b times i is the product with its complex conjugate. In a quadratic finite-field extension, the norm is likewise the product with the Frobenius conjugate. The analogy is structural, not an assertion that the two fields have the same geometry.

We now have a coherent chain. A finite field extension comes with a canonical symmetry. The symmetry groups roots into orbits. The orbits give minimal polynomials, and their lengths reveal subfields. The polynomial x to the q to the n minus x packages all irreducibles of allowed degrees. Möbius inversion counts them, while gcds and modular exponentiation let us test one candidate. Trace and norm compress an extension element back to the base field. Each of these ideas begins with the same elementary identity about powers of sums in characteristic p.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Frobenius and its orbits

Let \(E=\mathbb F_{q^n}\supseteq\mathbb F_q\), where \(q=p^k\). The map
\[
\sigma:E\to E,\qquad \sigma(a)=a^q
\]
is an automorphism fixing \(\mathbb F_q\). The binomial identity in characteristic \(p\) proves additivity; injectivity and finiteness prove bijectivity. Since \(a^{q^n}=a\) for all \(a\in E\), \(\sigma^n=1\). If \(0<m<n\), then \(\sigma^m\ne1\): otherwise the degree-\(q^m\) polynomial \(X^{q^m}-X\) would have \(q^n>q^m\) roots. Thus the order of \(\sigma\) is exactly \(n\).

For \(\alpha\in E\) with minimal positive Frobenius period \(d\),
\[
m_\alpha(X)=\prod_{j=0}^{d-1}(X-\alpha^{q^j})\in\mathbb F_q[X].
\]
Frobenius permutes roots, so the coefficients are fixed and lie in \(\mathbb F_q\). Every \(f\in\mathbb F_q[X]\) annihilating \(\alpha\) annihilates every conjugate; hence its degree is \(\ge d\). The displayed product is therefore the monic irreducible minimal polynomial.

### Subfield theorem

Inside a common algebraic closure,
\[
\boxed{\mathbb F_{q^d}\subseteq\mathbb F_{q^n}\iff d\mid n.}
\]
If \(d\mid n\), each root of \(X^{q^d}-X\) is a root of \(X^{q^n}-X\), giving the unique \(q^d\)-element subfield. If such a subfield exists, the tower dimension formula gives \(n=d[E:\mathbb F_{q^d}]\). Uniqueness follows because every member of any \(q^d\)-element subfield must be a root of \(X^{q^d}-X\).

### Irreducible factors and exact counting formula

For every positive integer \(n\),
\[
\boxed{X^{q^n}-X=\prod_{d\mid n}\ \prod_{\substack{f\text{ monic irreducible}\\\deg f=d}}f(X).}
\]
The product is squarefree because its derivative is \(-1\). Comparing degrees,
\[
q^n=\sum_{d\mid n}dN_q(d),\qquad
\boxed{N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.}
\]
Examples: \(N_2(1)=2\), \(N_2(2)=1\), \(N_2(3)=2\), \(N_2(4)=3\), \(N_2(6)=9\).

### Rabin's irreducibility criterion

For monic \(f\in\mathbb F_q[X]\) of degree \(n\ge1\),
\[
\boxed{f\text{ irreducible}\iff
\begin{cases}
X^{q^n}\equiv X\pmod f,\\
\gcd(f,X^{q^{n/r}}-X)=1&\text{for every prime }r\mid n.
\end{cases}}
\]
First condition says each irreducible factor has degree dividing \(n\), without repeated factors. If \(f\) had a proper factor of degree \(d<n\) dividing \(n\), choose a prime \(r\mid(n/d)\). Then \(d\mid n/r\), so that factor violates the gcd condition. Conversely an irreducible degree-\(n\) polynomial divides \(X^{q^n}-X\) and has no factor of any smaller degree. In a program, use repeated modular Frobenius powers and polynomial gcds, not the expanded polynomial \(X^{q^n}-X\).

**Examples over \(\mathbb F_2\):** \(X^3+X+1\) satisfies \(X^8\equiv X\) modulo the polynomial and \(\gcd(f,X^2-X)=1\). The squarefree but reducible \(X^4+X=X(X+1)(X^2+X+1)\) divides \(X^{16}-X\) yet violates \(\gcd(f,X^4-X)=1\).

### Relative trace and norm

For \(\alpha\in\mathbb F_{q^n}\),
\[
\operatorname{Tr}_{q^n/q}(\alpha)=\sum_{j=0}^{n-1}\alpha^{q^j}\in\mathbb F_q,
\qquad
\operatorname{Nm}_{q^n/q}(\alpha)=\prod_{j=0}^{n-1}\alpha^{q^j}
=\alpha^{(q^n-1)/(q-1)}\in\mathbb F_q.
\]
Trace is \(\mathbb F_q\)-linear; norm is multiplicative. With \(\beta^2+\beta+1=0\) in \(\mathbb F_4\), \(\operatorname{Tr}_{4/2}(\beta)=\beta+\beta^2=1\), \(\operatorname{Nm}_{4/2}(\beta)=\beta^3=1\). The formulas include repeated conjugate values when \(\alpha\) belongs to a proper subfield; the relative degree \(n\), not the size of its orbit, determines the number of summands and factors.

### Exercises

1. In \(\mathbb F_8\) with \(\alpha^3=\alpha+1\), compute the Frobenius orbit of \(\alpha\), then multiply \((X-\alpha)(X-\alpha^2)(X-\alpha^4)\).
2. List the sizes of all subfields of \(\mathbb F_{2^{12}}\) containing \(\mathbb F_2\).
3. Compute \(N_3(2)\), \(N_2(5)\), and \(N_2(6)\) from Möbius inversion.
4. Use the Rabin criterion to determine whether \(X^4+X+1\) is irreducible over \(\mathbb F_2\).
5. Calculate trace and norm of \(1\) and of a primitive element in \(\mathbb F_4/\mathbb F_2\). Explain why trace of \(1\) can be zero.

### Reading and source notes

- Keith Conrad, [Finite Fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf), especially the Frobenius, subfield, and polynomial factorization sections.
- [FLINT documentation: Rabin's irreducibility test](https://flintlib.org/doc/algorithms/polynomials/irreducibility.html), exact gcd/exponent criterion and implementation ideas.
- Daniel Flores Galiote, [Irreducible polynomials over finite fields](https://danielfloresmath.github.io/notes/irreducible-polynomials.html), elementary proofs and Möbius counts.
- Wikipedia: [Frobenius endomorphism](https://en.wikipedia.org/wiki/Frobenius_endomorphism), [Finite field](https://en.wikipedia.org/wiki/Finite_field), [Minimal polynomial (field theory)](https://en.wikipedia.org/wiki/Minimal_polynomial_(field_theory)), [Field trace](https://en.wikipedia.org/wiki/Field_trace), [Field norm](https://en.wikipedia.org/wiki/Field_norm), [Möbius inversion formula](https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula).
