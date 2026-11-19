# 025000 — Constructing Finite Fields, and Proving They Are Unique

**Track:** Number Theory from First Principles. **Background:** elementary congruences, the polynomial division algorithm, and the finite-field multiplicative-group result developed in lecture 014000. **Aim:** prove existence and uniqueness up to isomorphism of a field of every prime-power cardinality.

<!-- BEGIN SPOKEN LECTURE -->

# Constructing Finite Fields, and Proving They Are Unique

We know that integers modulo seven form a field: every nonzero remainder has a multiplicative inverse. But integers modulo eight do not. Two times four is zero modulo eight, even though neither factor is zero. How, then, can there be a field with eight elements?

There is one. In fact there is, up to relabeling its elements in a way that respects addition and multiplication, exactly one field with eight elements. The same is true for nine elements, sixteen elements, twenty-seven elements, and every other prime power. But there is no field with six elements, ten elements, or any other size that is not a prime power.

This theorem is often compressed into a single sentence: finite fields exist precisely in prime-power orders, and there is one up to isomorphism for each order. Today our goal is to earn that sentence. We will build examples you can calculate with, explain why their sizes must be prime powers, prove that every allowable size actually occurs, and prove that different constructions of the same size yield the same abstract field.

## Why the size must be a prime power

A field has two arithmetic operations. Its addition has an identity called zero, its multiplication has an identity called one, and every nonzero element has a multiplicative inverse. A field cannot have zero divisors: if a times b equals zero and a is nonzero, multiply by the inverse of a to conclude b is zero.

Suppose a field F has only finitely many elements. Add one to itself repeatedly. Because there are finitely many possible sums, eventually one of these sums is zero. Let p be the smallest positive number of copies of one that add to zero.

This number p must be prime. If p were a product of two smaller positive numbers a and b, then the element a copies of one times the element b copies of one would be p copies of one, which is zero. Neither factor is zero by minimality. That contradicts the no-zero-divisors rule.

The repeated sums of one therefore form a copy of the ordinary field of integers modulo p, usually denoted F p. This is called the prime subfield. Every element of our finite field can be multiplied by the scalars from that subfield.

Now view F as a vector space over F p. A basis means a list of elements such that every element of F has one and only one expression as a linear combination of those basis elements with coefficients in F p. Because F is finite, the basis has some finite length n.

Each coefficient in such an expression has p choices. There are n independent coefficients. So the number of elements in F is exactly p to the n. We have proved that a finite field cannot have six or ten elements, for those numbers are not powers of a single prime.

Notice the direction of this argument. We have shown only that every finite field has prime-power size. We have **not** shown that a field of every prime-power size exists. That requires a construction.

## Why dividing by a polynomial works

Recall ordinary modular arithmetic. We begin with integers, declare two integers equivalent when their difference is divisible by a modulus, and work with the resulting remainder classes. If the modulus is prime, the result is a field. If the modulus is composite, zero divisors appear.

We can do something parallel with polynomials. Take polynomials whose coefficients lie in F p. Fix a polynomial f of degree n, and declare two polynomials equivalent if their difference is a multiple of f. Every equivalence class has a unique remainder of degree less than n when divided by f.

Therefore there are p to the n distinct classes: one choice of coefficient for each of the n powers from constant through degree n minus one. Addition and multiplication mean adding or multiplying representatives and reducing the result modulo f.

Will these operations make a field? Exactly when f is irreducible over F p. Irreducible here means that f cannot be factored into two polynomials of smaller positive degree with coefficients in F p.

The reason is the polynomial Euclidean algorithm. If f is irreducible and a nonzero remainder a has degree below that of f, then a and f have polynomial gcd one. Bézout's identity gives polynomials u and v such that u times a plus v times f equals one. Reducing modulo f leaves u times a equal to one. So every nonzero class has an inverse.

Conversely, if f factors as g times h with both factors of positive degree less than n, then g and h represent nonzero residue classes whose product is zero. That cannot happen in a field.

This is the correct replacement for the failed idea of working modulo eight. We work modulo an **irreducible polynomial**, not modulo a composite integer. The new field contains an element that behaves like a formal root of the chosen polynomial.

## A field with eight elements, built by hand

Choose coefficients modulo two. There are only two coefficients, zero and one. Consider the cubic polynomial x cubed plus x plus one. A cubic over a field is irreducible if and only if it has no root in that field, because any nontrivial factorization of a cubic would include a linear factor.

At zero, our polynomial equals one. At one, it equals one plus one plus one, which is one modulo two. Neither is a root. So the polynomial is irreducible.

Let alpha denote the residue class of x modulo this cubic. The defining relation says alpha cubed plus alpha plus one equals zero. In characteristic two, subtraction equals addition, so alpha cubed equals alpha plus one.

Every element of the new field is uniquely one of the eight expressions a plus b alpha plus c alpha squared, where a, b, c are zero or one. Addition is coefficientwise modulo two. Multiplication uses the relation alpha cubed equals alpha plus one to reduce every higher power.

For example, alpha times alpha squared is alpha cubed, or alpha plus one. And alpha squared times alpha squared is alpha to the fourth, which reduces to alpha squared plus alpha. The relation prevents powers from escaping the eight-element set.

We can go further. Starting from alpha, its successive nonzero powers are alpha, alpha squared, alpha plus one, alpha squared plus alpha, alpha squared plus alpha plus one, alpha squared plus one, and then one. All seven nonzero elements appear. So alpha generates the multiplicative group of this field.

This gives a concrete arithmetic world with eight elements. It is not integers modulo eight. Its addition is a three-bit vector addition, and its multiplication is polynomial multiplication followed by reduction. Both operations belong to the definition; merely listing eight labels would not tell us the field structure.

## Nine elements show that the construction is not unique

Now take coefficients modulo three and the polynomial x squared plus one. This polynomial has no root modulo three because the only square residues are zero and one, while negative one is two. Hence x squared plus one is irreducible.

Call the class of x by the name beta. Then beta squared equals negative one, which is two in F three. Every element of the resulting field is a plus b beta, with a and b chosen from zero, one, two. Nine distinct elements result.

Here beta itself has multiplicative order four, since beta squared is negative one and beta to the fourth is one. But the field has eight nonzero elements. Therefore beta is **not** a generator of the entire nonzero multiplicative group. The element one plus beta is such a generator: its powers run through all eight nonzero elements before returning to one.

This distinguishes two claims that are easy to confuse. The multiplicative group of every finite field is cyclic; that does not imply every nonzero element is a generator. Nor does it imply that the class of x in every polynomial construction must be a primitive element.

We could construct a nine-element field using a different irreducible quadratic, such as x squared plus x plus two. Its expressions and multiplication rules would look different. Are these actually different fields, or merely different descriptions of the same field?

## Existence for every prime power

There is a gap in what we have proved so far. We found special irreducible polynomials of degree two and degree three. What assures us that we can find irreducible polynomials of **every** positive degree over **every** prime field?

We will prove something stronger first. Given a prime p and a positive integer n, write q for p to the n. Consider the polynomial x to the q minus x over F p. We want a field in which all of its roots exist.

A basic construction from polynomial arithmetic produces a splitting field. Start with F p. If our polynomial has an irreducible factor that is not yet linear, adjoin a root by forming the quotient by that factor. In the enlarged field, one linear factor can be removed from the original polynomial. Repeat this process on the remaining factors. Because the degree drops each time a root is adjoined and removed, finitely many steps suffice. The resulting field contains all the roots. We do not yet claim that it has q elements; it may initially be larger.

Inside this splitting field, consider **the set of roots** of x to the q minus x. We will show the set itself is a field.

The critical observation is the freshman's dream in characteristic p: the p-th power of a plus b equals the p-th power of a plus the p-th power of b. All intermediate binomial coefficients are multiples of p. Applying this repeatedly, raising to the q-th power also preserves sums. It plainly preserves products. Therefore, if a and b each satisfy their own q-th-power equals themselves, then so do a plus b and a times b. Negatives are preserved as well. One is a root, zero is a root, and if a is a nonzero root, taking inverses in the splitting field gives a to the negative q equal to a inverse. So its inverse is a root too.

We have closure under all field operations. The root set is a subfield.

How many elements does it have? Our polynomial has degree q. Its formal derivative is q times x to the q minus one, minus one. In characteristic p, q is zero, so this derivative is simply negative one. Consequently no root is repeated: a repeated root would also be a root of the derivative, which is impossible. Since the polynomial splits completely in our splitting field and has no repeated roots, it has exactly q distinct roots.

The root set is therefore a field with exactly p to the n elements. Existence is proved for every prime power.

Now the irreducible-polynomial construction is justified for arbitrary degree as well. The multiplicative group of this new field is cyclic, so choose a generator gamma of its nonzero elements. Every field element is a polynomial expression in gamma. The smallest nonzero polynomial over F p that vanishes at gamma is irreducible, and its degree must be n: the field it generates has p to the power of that degree elements, and that is the entire field of size p to the n. Thus irreducible polynomials of every degree exist.

This reasoning explains a subtle logical ordering. It would be circular to assume that an irreducible polynomial of every degree exists in order to construct all finite fields, and then cite finite fields to prove that those polynomials exist. Instead we constructed the field as a set of roots in a splitting field, and only afterward extracted an irreducible polynomial of the desired degree.

## Why two fields of the same size must be isomorphic

Finally we prove uniqueness, not of literal labels, but of the arithmetic structure.

Let F and E be any two fields with q elements, where q is p to the n. Both contain the same kind of prime subfield, F p. Every element of either field satisfies x to the q equals x, because every nonzero element belongs to a multiplicative group of size q minus one.

Choose a generator gamma of the nonzero multiplicative group of F. Its minimum polynomial f over F p has degree n, since gamma generates all of F. That polynomial divides x to the q minus x, because gamma is a root of the latter.

Now look in E. Every one of its q elements is a root of x to the q minus x. So that polynomial splits there into q distinct linear factors. Since f divides it, f must also have a root in E. Call such a root beta.

Sending gamma to beta defines a homomorphism from the field built out of polynomial expressions in gamma into the field built out of polynomial expressions in beta. The same irreducible polynomial f supplies all the relations on each side, so the map is well-defined and respects addition and multiplication. Its image has p to the n elements, exactly q. But E itself has q elements. The image must be all of E.

We have constructed a field isomorphism from F onto E. Therefore there is, up to isomorphism, exactly one field of every prime-power size. It is standard to write F sub q for that isomorphism class, even though a computer implementation still has to choose a particular representation and multiplication rule.

This proof also tells us why the isomorphism need not be unique. A minimal polynomial can have several roots in the target field, each giving a different possible image for gamma. A field can have nontrivial symmetries that fix its prime subfield.

Consider again the two cubic constructions over the two-element field. One uses x cubed plus x plus one, and another uses x cubed plus x squared plus one. Inside the first field, alpha plus one is a root of the second cubic. Mapping the generator of the second presentation to alpha plus one identifies their elements and operations. Two different-looking multiplication tables, one field.

There is a useful boundary to our conclusion. The field of eight elements is unique **up to isomorphism**, not identical to every set of eight symbols someone might invent. The construction does not give a canonical way to label its nonzero elements, and it certainly does not turn the ordinary remainder ring modulo eight into a field.

The existence-and-uniqueness theorem is a foundation for coding theory, exact arithmetic, and much of algebra. But its central idea is simpler than its applications: to construct finite division, replace an integer modulus by a prime-field polynomial modulus; to prove that every size exists, use roots of x to the q minus x; and to prove uniqueness, realize that the roots enforce the same arithmetic in any field with q elements.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Prime-power necessity

A finite field \(F\) has characteristic \(p\) prime (otherwise \((a\cdot1)(b\cdot1)=0\) with neither factor zero). Its prime subfield is \(\mathbb F_p\). If \(n=\dim_{\mathbb F_p}F\), then \(\boxed{|F|=p^n}\).

### Polynomial quotient construction

For \(f\in\mathbb F_p[X]\) monic, \(\deg f=n\), the quotient \(\mathbb F_p[X]/(f)\) has \(p^n\) classes, represented uniquely by \(a_0+\cdots+a_{n-1}X^{n-1}\). It is a field iff \(f\) is irreducible. For \(g\not\equiv0\pmod f\), irreducibility implies \(\gcd(f,g)=1\), so the polynomial Bézout relation \(uf+vg=1\) supplies inverse \(v\) to \(g\bmod f\). If \(f=gh\) with both degrees positive, then \([g][h]=0\) with both classes nonzero.

### Existence for every prime power

Let \(q=p^n\). A splitting field \(K\supseteq\mathbb F_p\) of \(X^q-X\) is obtained by successively adjoining roots using irreducible quotient extensions. The set
\[
S=\{a\in K:a^q=a\}
\]
is closed under addition, subtraction, multiplication, and nonzero inversion, since \((a+b)^q=a^q+b^q\) in characteristic \(p\). Moreover
\[
(X^q-X)'=qX^{q-1}-1=-1,
\]
so there are no repeated roots. The split degree-\(q\) polynomial has exactly \(q\) roots. Thus \(\boxed{S\text{ is a field of size }p^n}\).

A generator \(\gamma\) of \(S^\times\) (cyclicity proved in 014000) generates \(S\) over \(\mathbb F_p\), hence its minimal polynomial is irreducible of degree \(n\); therefore irreducibles of every degree exist.

### Uniqueness via an explicit field embedding

If \(F,E\) both have size \(q=p^n\), choose \(\gamma\in F^\times\) with \(F=\mathbb F_p(\gamma)\). Its minimal polynomial \(f\) has degree \(n\) and satisfies \(f\mid (X^q-X)\). Every element of \(E\) is a root of \(X^q-X\); therefore the latter splits in \(E\), and so does \(f\). Choose a root \(\beta\in E\) of \(f\). The well-defined embedding
\[
\mathbb F_p[X]/(f)\hookrightarrow E,\qquad [X]\longmapsto\beta
\]
has image of size \(p^n=q\), so it is an isomorphism. This relies on the cyclicity theorem from 014000, not an unproved general uniqueness-of-splitting-fields claim.

### Models with eight and nine elements

\[
\mathbb F_8\cong\mathbb F_2[\alpha]/(\alpha^3+\alpha+1),\qquad \alpha^3=\alpha+1.
\]
The nonzero powers of \(\alpha\) are
\[
\alpha,\ \alpha^2,\ \alpha+1,\ \alpha^2+\alpha,\ \alpha^2+\alpha+1,\ \alpha^2+1,\ 1.
\]
The other irreducible cubic \(X^3+X^2+1\) has a root \(\alpha+1\) in this model, showing an explicit isomorphism between the two presentations.

\[
\mathbb F_9\cong\mathbb F_3[\beta]/(\beta^2+1),\qquad\beta^2=2.
\]
Here \(\operatorname{ord}(\beta)=4\), while \(\operatorname{ord}(1+\beta)=8\). Distinguish the algebraic generator \(\beta\), which generates the field by polynomial expressions, from a multiplicative primitive element.

### Exercises

1. Verify directly that \(X^3+X+1\) has no root in \(\mathbb F_2\) and write a multiplication table for \(1,\alpha,\alpha^2\).
2. Check \((\alpha+1)^3+(\alpha+1)^2+1=0\) in \(\mathbb F_8\).
3. Show that \(X^2+1\) is irreducible in \(\mathbb F_3[X]\) but reducible in \(\mathbb F_5[X]\).
4. Prove every nonzero element of a field of size \(q\) satisfies \(x^{q-1}=1\).
5. Explain precisely where irreducibility, cyclicity, and separability are each used in the proof of existence and uniqueness.

### Reading and source notes

- Keith Conrad, [Finite Fields](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf), Sections 1–2: polynomial-quotient constructions, prime-power size, root-field existence and uniqueness.
- Brian Conrad, [Elementary Explanation of Finite Field Mysteries](https://math.stanford.edu/~conrad/210BPage/handouts/math210b-elementary-finite-fields.pdf), explicit elementary uniqueness arguments.
- Wikipedia: [Finite field](https://en.wikipedia.org/wiki/Finite_field), [Field extension](https://en.wikipedia.org/wiki/Field_extension), [Splitting field](https://en.wikipedia.org/wiki/Splitting_field), [Irreducible polynomial](https://en.wikipedia.org/wiki/Irreducible_polynomial).
