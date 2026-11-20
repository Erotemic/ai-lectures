# A Polynomial Is Not Just an Equation: Division, Ideals, and New Fields

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic  
**Lecture:** 092000  
**Preparation:** Rings and fields, modular arithmetic, quotient groups, and basic polynomial manipulation.  
**Companion:** Euclidean algorithm in F[x], Bézout identities, polynomial quotients, the Chinese remainder theorem, and the four-element field.

<!-- BEGIN SPOKEN LECTURE -->

When we first learn polynomials, they appear as expressions to factor or equations to solve. We ask which numbers make x squared plus one equal zero. We divide one polynomial by another, perhaps only to simplify a fraction. These are useful calculations, but they conceal a richer possibility: polynomials can themselves be the elements of a number system.

We can add polynomials, subtract them, multiply them, form ideals of polynomials, and collapse those ideals to construct new rings and fields. The passage from arithmetic with integers to arithmetic with polynomials is one of the most productive moves in algebra. And the familiar long-division algorithm turns out to be a powerful structural theorem—but only under the right hypotheses.

Let's begin by deciding exactly what a polynomial is.

## Coefficients, not merely values

A polynomial over a field F is a finite list of coefficients, conventionally displayed as a sum of coefficients multiplied by powers of x. Two polynomials are equal when their corresponding coefficients are equal. Adding polynomials adds coefficients; multiplying them uses convolution: to obtain the coefficient of a given power of x, add the products of coefficient pairs whose exponents sum to that power.

That definition might seem excessively careful if we imagine polynomials as functions. Over the real numbers, a nonzero polynomial cannot vanish at infinitely many points, so distinct real polynomials define distinct functions on the real line. But this fact depends on having an infinite field. Over a finite field, different polynomials can define exactly the same function.

For example, over the field with two elements, the polynomial x squared plus x is not the zero polynomial. Its coefficient of x squared is one. Yet it evaluates to zero at both possible inputs: at zero, obviously; at one, one plus one equals zero because arithmetic is modulo two. So as a function on that two-element set, it is the zero function.

This distinction affects algorithms and formal proofs. If we represent a polynomial only by its values on the field, we have forgotten information needed for division, factorization, and degree. The polynomial ring retains coefficients and formal powers. Evaluation is a useful map out of that ring, not its definition.

## Why division works over a field

Consider polynomials f and g over a field F, with g nonzero. There is a division algorithm: we can write f as q times g plus r, where the remainder r is zero or has smaller degree than g. Moreover, the quotient q and remainder r are unique.

The proof uses a descending measure. If the degree of f is at least the degree of g, compare their leading terms. The leading coefficient of g is nonzero and therefore invertible in F. Choose a monomial whose product with g cancels the leading term of f. Subtract it. The remainder has strictly smaller degree than f, and repeating eventually produces a remainder of degree below that of g. Degrees are nonnegative integers for nonzero polynomials, so the process cannot continue indefinitely.

The field hypothesis is doing real work. Over the integers, we cannot always divide one leading coefficient by another and stay inside the coefficient ring. There is no polynomial with integer coefficients whose product with the constant polynomial two gives the constant polynomial one. So the field version of long division does not apply unchanged to all of Z of x.

Take a concrete example over the rationals. Let f equal x cubed minus one, and let g equal x squared minus one. Subtract x times g from f. What remains is x minus one. Thus f equals x times g plus x minus one. The remainder has degree one, smaller than the divisor's degree two.

Now divide g by x minus one. Because x squared minus one factors as x minus one times x plus one, the remainder is zero. We have reached the end of the Euclidean algorithm: the monic greatest common divisor is x minus one.

In a field's polynomial ring, the greatest common divisor is defined up to multiplication by a nonzero constant, because nonzero constants are units. Choosing the monic version—leading coefficient one—makes it unique. The greatest common divisor is not merely the polynomial with the largest degree among common divisors; it is a divisor of both which is itself divisible by every common divisor, and the Euclidean algorithm constructs it.

## Bézout's identity returns

The calculation gave us f minus x times g equals x minus one. That is a polynomial Bézout identity: a linear combination of f and g equals their greatest common divisor.

The general extended Euclidean algorithm does the same thing. At every remainder step, we can write the current remainder as a linear combination of the original two polynomials. The last nonzero remainder is therefore such a combination. This is exactly the mechanism by which the integer Euclidean algorithm finds modular inverses.

Why is it useful? Suppose a polynomial m is irreducible over F. It has no nonconstant proper divisors. For any polynomial a not divisible by m, the greatest common divisor of a and m is one. Bézout then supplies polynomials u and v with u times a plus v times m equal to one. Reduce this equality modulo m. The term containing m disappears, leaving u times a equal to one in the quotient. So every nonzero residue class has a multiplicative inverse.

We have proved that F of x modulo the ideal generated by an irreducible polynomial is a field. A familiar algorithm has become a construction principle for entirely new arithmetic systems.

## When reducing a polynomial creates a field

Let's do the construction explicitly with the field of two elements. Consider the polynomial m equal x squared plus x plus one. It has degree two. A quadratic over a field is reducible if and only if it has a root in that field. Substituting zero gives one; substituting one gives one plus one plus one, which is one modulo two. Neither input is a root. Therefore m is irreducible.

Form the quotient field F two of x modulo m. In this new field, we identify m with zero. Denote the residue class of x by alpha. The relation alpha squared plus alpha plus one equals zero becomes alpha squared equals alpha plus one, because minus one and plus one coincide in characteristic two.

Every polynomial class has a unique remainder of degree less than two, so every element can be written as a plus b alpha with coefficients a and b each either zero or one. There are exactly four elements: zero, one, alpha, and alpha plus one.

We can multiply them using the relation. For instance, alpha times alpha plus one is alpha squared plus alpha. Replace alpha squared by alpha plus one, obtaining alpha plus one plus alpha, which equals one. So alpha plus one is the multiplicative inverse of alpha. Similarly, alpha squared equals alpha plus one, and alpha cubed equals one. The three nonzero elements form a cyclic multiplicative group of order three.

This four-element field is not the integers modulo four. In integers modulo four, two is nonzero but two times two is zero. That makes two a zero divisor. A field cannot have zero divisors. Instead, the four-element field has characteristic two, so one plus one is zero, and it has two independent directions over its two-element subfield: the basis one and alpha.

The construction illustrates the purpose of a quotient relation. Declaring x squared plus x plus one equal zero does not merely pick a numerical root we already knew. It introduces an element alpha subject to that algebraic equation, while retaining enough information to perform consistent arithmetic.

## Why irreducibility is the dividing line

What happens if we quotient by a reducible polynomial instead? Consider rational polynomials modulo x squared minus one. In the quotient, the class of x minus one times the class of x plus one equals zero, because their product is precisely x squared minus one. Neither factor is the zero class: each has degree one, too small to be a multiple of the degree-two modulus.

Thus the quotient has nonzero zero divisors. It cannot be a field. The difference is visible in the factorization of the modulus. An irreducible modulus gives a field; a reducible, nonconstant modulus gives a quotient ring that is not a field.

Over a field F, the polynomial ring F of x is a principal ideal domain: every ideal is generated by a single polynomial. This follows from division. In a nonzero ideal, choose a nonzero polynomial m of smallest degree and make it monic. Divide any other ideal element f by m. Both f and the multiple q m belong to the ideal, so their difference r does too. But r has degree smaller than m, so minimality forces r to be zero. Every f is a multiple of m.

A nonzero ideal generated by m is maximal precisely when m is irreducible. If m factors into nonunits, its quotient has zero divisors and is not a field. If it is irreducible, Bézout's identity gives inverses to every nonzero class. We have translated a factoring property of one polynomial into a structural property of a quotient ring.

This argument should not be transferred blindly to Z of x. The ideal generated by two and x in Z of x is not principal. It consists of polynomials whose constant coefficient is even. It is a proper ideal because the constant polynomial one is not in it. No single polynomial can generate it: such a generator would have to divide both the constant polynomial two and the polynomial x, forcing a constant unit, which would generate the whole ring. So the clean principal-ideal statement relies on coefficients in a field.

## The Chinese remainder theorem for polynomials

Now consider the quotient of rational polynomials by x squared minus one once more. We saw that it is not a field. But we can describe it very explicitly. The polynomial x squared minus one factors as x minus one times x plus one, and those factors are coprime over the rationals. Their difference is two, which is invertible in the coefficient field.

Evaluate a polynomial at one and at negative one. This gives a ring homomorphism from rational polynomials to pairs of rational numbers. Its kernel consists of polynomials divisible by both x minus one and x plus one, which, because the factors are coprime, is exactly the ideal generated by their product. The first isomorphism theorem for rings therefore suggests that our quotient ring is isomorphic to a direct product of two copies of the rational numbers.

We can prove surjectivity directly. Given a desired pair of rational values, say a at one and b at negative one, take the linear polynomial whose constant coefficient is half of a plus b, and whose coefficient of x is half of a minus b. At x equals one, the two halves add to a. At x equals negative one, they add to b.

So every pair is realized. In symbols, rational polynomials modulo x squared minus one form the same ring structure as rational pairs under componentwise addition and multiplication.

Now the zero divisors are obvious. The pair one, zero and the pair zero, one are both nonzero, but their componentwise product is zero, zero. The factorization of the modulus has split a ring into independent components. More generally, coprime polynomial factors give product decompositions, and repeated factors give different behavior because nilpotent elements may appear. For example, in the quotient by x squared, the class of x is nonzero, but its square is zero.

This is the polynomial Chinese remainder theorem. It shows that quotients can create fields, split rings into products, or retain nilpotent information, depending on the ideal by which we quotient.

## Evaluation, ideals, and the road to extensions

Notice how the ideas have come together. Evaluation at a number is a ring homomorphism. Its kernel is an ideal. Polynomial division describes those kernels, and quotient rings describe the information left after we identify polynomials with the same image. If a modulus is irreducible, the quotient supplies a new field; if it factors into coprime pieces, the quotient separates into components.

In a formalization, these are distinct claims. One must define coefficientwise equality, prove a division algorithm, establish that the proposed relation is an ideal, show quotient operations are well-defined, and then prove the field property or product decomposition. The code that computes a remainder is not by itself a proof of the structural theorem. Conversely, a structural theorem about the quotient does not automatically give an efficient factoring algorithm.

The new field built from x squared plus x plus one contains an element satisfying an equation that had no solution in the original two-element field. That is the first model for a field extension. We do not need to imagine the new element as a mysterious number. It is an equivalence class of polynomials, and its arithmetic is governed by a precise reduction rule.

Long division, Bézout's identity, irreducibility, quotient ideals, and the Chinese remainder theorem are sometimes presented as separate chapters. They are one story. Division identifies what can be reduced. An ideal identifies what we are declaring to be zero. The quotient records what survives. And the surviving algebra can be a new field in which equations gain solutions that did not previously exist.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a field \(F\), polynomial equality in \(F[x]\) is coefficientwise equality. The degree of a nonzero polynomial is the largest exponent with nonzero coefficient. Degree of \(0\) is convention-dependent; avoid using it in strict-degree inequalities except as a separate case.

**Division and Bézout:** For \(f,g\in F[x]\), \(g\ne0\), unique \(q,r\) satisfy \(f=qg+r\) with \(r=0\) or \(\deg r<\deg g\). The Euclidean algorithm computes a monic gcd \(d=uf+vg\). Example:
\[
x^3-1=x(x^2-1)+(x-1),\qquad x^2-1=(x+1)(x-1),
\]
so \(\gcd(x^3-1,x^2-1)=x-1=(x^3-1)-x(x^2-1)\).

**Irreducibility and quotients:** If \(m\in F[x]\) is nonconstant, \(F[x]/(m)\) is a field iff \(m\) is irreducible (equivalently, \((m)\) is maximal). For \(m=x^2+x+1\in\mathbb F_2[x]\), let \(\alpha=[x]\). Then
\[
\mathbb F_4=\{0,1,\alpha,1+\alpha\},\qquad \alpha^2=\alpha+1,\qquad\alpha(\alpha+1)=1.
\]
By contrast \(\mathbb Z/4\mathbb Z\) has a nonzero zero divisor, \(2^2=0\).

**Non-principal integer polynomial ideal:** \((2,x)\subset\mathbb Z[x]\) is proper because reduction of the constant coefficient mod 2 sends both generators to zero but sends \(1\) to one. A generator would divide \(2\) and \(x\), forcing a constant unit (if a constant divisor \(\pm2\) were used, it would not divide \(x\)). Thus it is not principal.

**Polynomial CRT:** Since \((x-1)+(x+1)=(1)\) over \(\mathbb Q[x]\), evaluation gives
\[
\mathbb Q[x]/(x^2-1)\overset{\sim}{\longrightarrow}\mathbb Q\times\mathbb Q,
\qquad[f]\longmapsto (f(1),f(-1)).
\]
The inverse on \((a,b)\) is the class of \(\tfrac{a+b}{2}+\tfrac{a-b}{2}x\). The nonzero classes of \(x-1\) and \(x+1\) multiply to zero.

**Worked checks and exercises**

1. Verify over \(\mathbb F_2\) that \(x^2+x\) induces the zero *function* but is not the zero *polynomial*.
2. Find the inverse of \(\alpha\) in \(\mathbb F_4\). *Answer:* \(\alpha+1\).
3. Why is \(\mathbb F_2[x]/(x^2+1)\) not a field? *Answer:* \(x^2+1=(x+1)^2\) over \(\mathbb F_2\), and the nonzero class of \(x+1\) has square zero.
4. Prove every ideal of \(F[x]\) is principal by selecting a nonzero polynomial of least degree in the ideal and applying division.
5. Compute the class corresponding to \((2,7)\) under the polynomial CRT isomorphism. *Answer:* \((9-5x)/2\) modulo \(x^2-1\).

**Source notes:** Judson, *Abstract Algebra: Theory and Applications*, https://judsonbooks.org/abstract-algebra-theory-and-applications/ ; Keith Conrad, expository algebra notes, https://kconrad.math.uconn.edu/blurbs/ ; MIT OCW Algebra II, https://ocw.mit.edu/courses/18-702-algebra-ii-spring-2011/pages/readings/ . The broad survey is `abstract-algebra:004000`.
