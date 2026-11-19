# Modular arithmetic, polynomial rings, and field extensions

<!-- BEGIN SPOKEN LECTURE -->

# Modular arithmetic, polynomial rings, and field extensions

## Divisibility, the Euclidean Algorithm, and Arithmetic Modulo n

There is a practical question hiding inside a simple-looking congruence. Suppose we want to solve seven times x gives remainder one on division by twenty-six. Is there such an integer x? If so, how do we find it? And why can a similar-looking question, six times x gives remainder one modulo twenty-six, have no solution at all?

The answer combines divisibility, the Euclidean algorithm, and a theorem about writing greatest common divisors as combinations of integers. It leads directly to the distinction between rings and fields.

### Divisibility is a statement about existence

We say a divides b if b equals a times some integer. For example, four divides twenty-eight because twenty-eight is four times seven. The statement “a divides b” is not a request to calculate a decimal quotient. It asserts that an integer witness exists.

A common divisor of a and b divides both. The greatest common divisor, when a and b are not both zero, is the largest positive integer with that property. Because the greatest common divisor is defined using positive integers, signs do not affect it. The greatest common divisor of twenty-six and seven is one: they share no positive factor larger than one.

The Euclidean algorithm computes the greatest common divisor by repeatedly taking remainders. Twenty-six equals three times seven plus five. Seven equals one times five plus two. Five equals two times two plus one. Two equals two times one plus zero. The last nonzero remainder, one, is the greatest common divisor.

Why does the algorithm work? If a equals q times b plus r, any integer dividing both a and b also divides r, because r is a minus q times b. Conversely, any integer dividing b and r divides a. So a and b have exactly the same common divisors as b and r. Each remainder is smaller in absolute value than the previous positive divisor. Eventually the remainders must reach zero, and the last nonzero remainder is the desired greatest common divisor. That is a proof of termination and correctness, not merely a convenient recipe.

### Read the divisions backward

The calculation contains more information than the greatest common divisor. Starting from the equation one equals five minus two times two, replace two by seven minus five. We obtain one equals three times five minus two times seven. Replace five by twenty-six minus three times seven. The result is one equals three times twenty-six minus eleven times seven.

This displays the greatest common divisor as an integer combination of the original inputs. In this example, three times twenty-six plus negative eleven times seven equals one. Such a statement is called Bézout's identity. More generally, the Euclidean algorithm can be run backward to express the greatest common divisor of a and b as an integer combination of a and b.

There is also a converse: every integer combination of a and b is divisible by their greatest common divisor. Consequently, if an integer combination equals one, the greatest common divisor must be one. These two directions make Bézout's identity a powerful characterization of coprimality.

We can now solve our opening congruence. The identity says negative eleven times seven differs from one by negative three times twenty-six. So seven times negative eleven has remainder one modulo twenty-six. Reducing negative eleven modulo twenty-six gives fifteen. Check: seven times fifteen is one hundred five, which leaves remainder one after subtracting four twenty-sixes.

In other words, fifteen is a multiplicative inverse of seven modulo twenty-six.

### Two operations on remainder classes

The integers modulo n form a group under addition. But they also have multiplication: multiply any representatives and reduce the result modulo n. The result does not depend on the representative choices. If a and a prime differ by a multiple of n, and b and b prime do as well, their products differ by a multiple of n because the difference can be expanded into terms each containing n.

A set with addition and multiplication obeying the usual ring rules, including distributivity, is called a ring. The integers themselves are a ring. So are the residue classes modulo n. We usually require an additive identity, additive inverses, associative multiplication, and distributivity; here we also have a multiplicative identity and commutative multiplication. Rings do not require every nonzero element to have a multiplicative inverse.

Our inverse calculation suggests the exact criterion for a residue class to be invertible modulo n: its representative a must have greatest common divisor one with n. If that gcd equals one, Bézout gives integers u and v such that u a plus v n equals one; reduction modulo n shows u is an inverse of a. Conversely, if a u is congruent to one, then a u minus one is a multiple of n, and we have an integer combination of a and n equal to one. Therefore their gcd is one.

Try a equal to six and n equal to twenty-six. Their gcd is two. Every product six times x is even, and so is every multiple of twenty-six. Their difference can never equal the odd number one. No inverse exists. This is not a defect in our algorithm; the algebra forbids a solution.

### Prime moduli are different

If p is prime, every residue class other than zero has a representative not divisible by p, and hence has greatest common divisor one with p. Every nonzero class has a multiplicative inverse. A commutative ring with one in which every nonzero element is invertible is a field. Therefore the residues modulo a prime p form a field.

If n is composite, write n as a product of two integers strictly between one and n. Neither factor is zero modulo n, but their product is zero modulo n. These are zero divisors. A field cannot have zero divisors: if a times b equals zero and a is nonzero, multiply by the inverse of a to conclude b equals zero. Thus residues modulo a composite integer cannot be a field.

This gives an exact classification for positive moduli greater than one: the ring of integers modulo n is a field if and only if n is prime.

An instructive contrast is modulo six. Two times three is zero modulo six although neither factor is zero. So the cancellation law familiar from nonzero real-number multiplication fails. If two times x equals two times y modulo six, x and y need not be equal; for instance two times zero and two times three have the same residue. Cancellation works only when the factor being canceled is a unit, meaning it has an inverse.

### Congruences as a structural tool

A congruence a equals b modulo n means their difference is divisible by n. It is compatible with addition and multiplication, so calculations may be carried out using representatives and reduced whenever convenient. We are not “approximating” an integer by a remainder. We are choosing to ask a question in a quotient structure where multiples of n have been identified with zero.

This distinction matters for solving linear congruences. The equation a x equals b modulo n has a solution exactly when the greatest common divisor of a and n divides b. We can see necessity from the equation a x minus n k equals b: the gcd divides the left side and therefore b. For sufficiency, Bézout expresses the gcd as a combination of a and n. Multiply that identity by b divided by the gcd, and it becomes an integer solution of the congruence.

For example, six times x equals four modulo twenty-six does have solutions, because the gcd is two and two divides four. Dividing the integer equation by two leads to three times x equals two modulo thirteen, where three has an inverse. One solution is x equal to five, since six times five is thirty, congruent to four modulo twenty-six. Adding thirteen gives another solution, eighteen, modulo twenty-six. The equation has exactly two residue solutions modulo twenty-six, matching the gcd.

### A small algorithm, a large distinction

The Euclidean algorithm is a model of what good mathematics and good computation share: a finite process, a proof that it terminates, a preserved invariant, and an independently checkable answer. Bézout's identity upgrades its output into a certificate. Modular arithmetic then turns that certificate into an inverse, or explains why none exists.

We have also crossed from groups into rings and fields. Addition alone supplies a group. Addition and multiplication interact in a ring. In a field, every nonzero multiplier can be undone. The difference determines which cancellations and equations are legitimate. Abstract algebra keeps track of those permissions instead of allowing familiar arithmetic intuition to smuggle them in.

## Rings, Ideals, and Quotients: Which Arithmetic Can Be Collapsed?

In ordinary integer arithmetic, we are free to replace a number by its remainder modulo five, add two remainders, multiply them, and reduce again. The answer is independent of the integer representatives we chose. But what authorizes this maneuver? Why is congruence modulo five compatible with two different operations, while a partition of the integers into even and odd classes is only one of many possible ways to identify numbers?

The key is an *ideal*. An ideal tells us which differences may be treated as zero without breaking multiplication. Once we understand that demand, the correspondence between algebraic maps and quotients becomes precise.

### Two operations, one structure

For now, a ring will mean a set with addition, subtraction, and multiplication, with associative multiplication, distributivity over addition, and a multiplicative identity. Addition makes an abelian group. We will focus mainly on commutative rings, such as the integers, rather than rings of matrices where multiplication can depend on the order.

The integers are a ring; the rational numbers are a ring with the extra property that every nonzero element is invertible. So are polynomials with rational coefficients. The difference between a ring and a field matters: multiplication in a ring may have no inverse operation for many elements.

Consider a ring homomorphism. It is a map preserving addition and multiplication, and in our convention preserving the element one. The familiar map sending each integer to its remainder class modulo five is a ring homomorphism. So is the map from rational polynomials to rational numbers that evaluates a polynomial at two. Evaluation commutes with addition and multiplication: evaluating a sum gives the sum of evaluations, and evaluating a product gives the product of evaluations.

Ask which inputs a homomorphism sends to zero. For reduction modulo five, they are the multiples of five. For evaluation at two, they are the polynomials with two as a root. The two examples live in different rings, yet their kernels obey the same rules.

### Why the kernel is an ideal

If elements a and b map to zero, then their difference maps to zero. The kernel is therefore an additive subgroup. But there is more. If a maps to zero and r is any ring element, the product r times a also maps to zero. Its image is the image of r multiplied by zero.

This multiplication property distinguishes an ideal from a mere additive subgroup. In a commutative ring, an ideal is an additive subgroup closed under multiplication by arbitrary elements of the ambient ring. In a noncommutative ring, a two-sided ideal must absorb multiplication on both the left and the right; that is what supports the ordinary quotient ring construction.

The integer multiples of five form an ideal. All integer ideals are sets of multiples of some nonnegative integer. That assertion itself follows from division with remainder: if a nonzero ideal contains a least positive integer d, divide any element of the ideal by d; the remainder belongs to the ideal, so minimality forces it to be zero.

Contrast the even integers inside the ring of integers with the set of all integer multiples of a polynomial's *value* at two. The latter description depends on what ring we are working in. We should not confuse the numbers that appear as evaluations with the polynomials being evaluated. In the polynomial ring, the kernel of evaluation at two is the ideal of multiples of the polynomial x minus two. The factor theorem proves this: a polynomial vanishes at two precisely when x minus two divides it.

### Constructing a quotient ring

Given an ideal I in a commutative ring R, declare a equivalent to b when their difference lies in I. The equivalence classes are cosets, just as in quotient groups. Define addition and multiplication on classes by adding or multiplying representatives.

To see why multiplication is legal, suppose a differs from a-prime by an element of I, and b differs from b-prime by an element of I. The difference a b minus a-prime b-prime is the sum of a times b minus b-prime and b-prime times a minus a-prime. Both terms are in I by the absorption property. Hence the product's class is independent of representatives.

Notice exactly where the ideal hypothesis was used. The additive-group quotient needs only additive closure. The ring quotient needs closure under multiplication by *everything in the ring*, because representatives can be multiplied by arbitrary elements.

The resulting quotient is written R modulo I. In the integers, modulo the ideal of multiples of five gives the five residue classes. In rational polynomials, modulo the ideal generated by x minus two gives a structure in which the variable x becomes equal to two. The entire quotient is naturally just the rational numbers.

### A structure theorem for maps

Let phi be a ring homomorphism from R to S. Its kernel consists of exactly those differences that phi cannot distinguish. Map the coset of an element r, modulo the kernel, to phi of r. This is well defined: two representatives differ by a kernel element exactly when their images are equal. It preserves addition, multiplication, and one. It is injective, because the only coset sent to zero is the kernel coset, and it is surjective onto the image of phi by construction.

So R modulo the kernel is isomorphic to the image. This is the first isomorphism theorem for rings. It is not a complicated coincidence. The quotient removes exactly the information the map loses, and no more.

For example, evaluate integer polynomials at zero, then reduce the integer result modulo two. The map takes a polynomial to the parity of its constant term. Its kernel includes every polynomial with an even constant term; in fact the kernel is the ideal generated by two and x. The quotient has exactly two elements, corresponding to even and odd constant terms. Even when an ideal has more than one generator, the same principle applies.

### Prime and maximal ideals

A ring quotient can contain zero divisors. Modulo six, the nonzero classes two and three multiply to zero. Two different ideals explain two different ways this can happen.

For a commutative ring with identity, an ideal P is called prime when it is proper and the product a b lies in P only if at least one of a and b lies in P. Exactly when P is prime, the quotient R modulo P has no zero divisors. A proper ideal M is maximal when no proper ideal lies strictly between M and the whole ring. Exactly when M is maximal, the quotient is a field.

Here is the reason for the maximal-ideal criterion. In the quotient, take any nonzero class a. Its representative is not in M. The ideal generated by M together with a strictly contains M; maximality therefore makes that ideal the whole ring. So one can write one as m plus r times a, with m in M. Reduce modulo M and we obtain an inverse for the class of a. The converse follows because a field has no nontrivial proper ideals: a nonzero element in an ideal has an inverse, which forces one to belong to that ideal.

In the integers, the ideal of multiples of a prime number p is maximal, and the quotient is a finite field. The ideal of multiples of six is neither prime nor maximal. In a polynomial ring over a field, an ideal generated by a nonconstant irreducible polynomial is maximal. That observation will make it possible to construct fields by declaring a chosen polynomial to be zero.

### Quotients are controlled forgetfulness

A quotient ring is not an arbitrary act of identifying symbols. It is an agreement about which differences count as zero, disciplined by the requirement that all legal computations respect the agreement.

The distinction between subgroups and ideals answers our opening question. A group quotient must preserve composition. A ring quotient must preserve addition and multiplication together. The ideal absorbs arbitrary multipliers because otherwise multiplication on classes would depend on a representative that is supposed to have been forgotten. This is the algebraic idea behind modular arithmetic, polynomial evaluation, and the construction of new number systems.

## Polynomial Rings, Factorization, and Irreducibility

Suppose we want a number whose square is two. Inside the rational numbers, no such number exists. We could simply introduce a symbol called the square root of two and begin calculating, but how can we know which calculations remain legitimate? How can we ensure that dividing by a nonzero expression will not produce a contradiction?

Polynomial arithmetic provides a systematic answer. We can make a new field in which the polynomial x squared minus two equals zero. The crucial condition is that the polynomial be irreducible: it cannot be factored into two polynomials of smaller positive degree over the original field.

### Polynomials as arithmetic objects

A polynomial over a field F is a finite expression formed from a variable x with coefficients in F. We add coefficients of like powers, and multiply by distributing and collecting powers. It is important that x is initially a formal variable: an expression in the polynomial ring is not yet the result of plugging in a number. Two polynomials are equal when their coefficient lists agree.

Degree measures the highest power with nonzero coefficient. For nonzero polynomials over a field, the degree of a product is the sum of the degrees. We need the nonzero condition because the zero polynomial has no ordinary degree, and we need a field—or at least an integral domain—to avoid a leading coefficient disappearing through multiplication.

The first surprise is that polynomials over a field have their own division algorithm. Given a polynomial f and nonzero g, there are unique polynomials q and r such that f equals q g plus r, with r zero or having smaller degree than g. The reason is the same as long division. Divide the leading coefficient of f by the leading coefficient of g, subtract an appropriate multiple of g to cancel the leading term, and repeat. Each step decreases degree, so the process terminates.

For a simple example, divide x squared plus one by x minus two, working over the rational numbers. The quotient is x plus two, because multiplying x minus two by x plus two gives x squared minus four. The remainder is five. Replacing x by two therefore gives five. This is the remainder theorem: division by x minus a leaves remainder f evaluated at a.

### Roots, factors, and the limits of the root test

A polynomial has a root a in F exactly when x minus a divides it. One direction follows by evaluation. For the other, polynomial division writes f as the product of x minus a and some q, plus constant remainder f of a. If the remainder vanishes, the division is exact.

A nonconstant polynomial is reducible over F if it is a product of two polynomials each of positive degree. Otherwise it is irreducible. For a degree-two or degree-three polynomial over a field, reducibility forces a linear factor, because two positive degrees adding to two or three must include a one. So for quadratic and cubic polynomials, finding or ruling out a root decides irreducibility.

But this test is not generally sufficient in degree four. The polynomial x to the fourth plus four, over the rationals, has no rational root, yet it factors as x squared minus two x plus two, multiplied by x squared plus two x plus two. Multiplying these expressions confirms the identity. This is an essential warning: no roots does not mean irreducible when the degree is at least four.

The field matters, too. The polynomial x squared minus two is irreducible over the rationals. If a reduced rational fraction a over b squared to two, then a squared would equal twice b squared, forcing a even and then b even, contradicting that the fraction was reduced. Over the real numbers, the same polynomial factors into linear terms using the square root of two. Irreducibility is always relative to a coefficient field.

### Greatest common divisors for polynomials

Because long division works in F of x, we can repeat the Euclidean algorithm. For two polynomials f and g, the last nonzero remainder, normalized to have leading coefficient one, is their greatest common divisor. Back substitution expresses that greatest common divisor as u f plus v g for some polynomials u and v.

This immediately tells us why irreducible polynomials play a role like prime integers. If p is irreducible and does not divide a, their greatest common divisor must be one. Bézout's identity gives polynomials u and v with u p plus v a equal to one. If p divides a b, reduce the identity times b modulo p. The term involving p vanishes; because a b is divisible by p, the remaining term forces p to divide b. Thus irreducibles satisfy Euclid's lemma in a polynomial ring over a field.

It follows by induction that every nonzero nonconstant polynomial factors into irreducibles, with the factors unique up to multiplication by nonzero constants and reordering. This is unique factorization in one variable over a field. The proof depends on the degree as a termination measure and Euclid's lemma as the uniqueness mechanism.

### A field made from a polynomial

Now take an irreducible polynomial p over F. Consider the quotient ring F of x modulo the ideal generated by p. Inside this quotient, p is equal to zero. The class of x acts like a new element alpha satisfying p of alpha equals zero.

Why is the quotient a field? Take any polynomial a whose class is nonzero. That means p does not divide a. Since p is irreducible, the greatest common divisor of p and a is one. Bézout gives u p plus v a equal to one. In the quotient the u p term vanishes, so the class of v is the inverse of the class of a. Every nonzero class has an inverse.

When p has degree n, the division algorithm also says every class has one unique representative of degree less than n. So the quotient is an n-dimensional vector space over F with basis the classes of one, x, up through x to the power n minus one. Here dimension is measuring how much arithmetic we added.

Take rational coefficients and p equal to x squared minus two. Every class has the form a plus b alpha, with rational a and b, and alpha squared equals two. Multiplication is controlled by this relation. The inverse of a plus b alpha, when the expression is nonzero, is a minus b alpha divided by a squared minus two b squared. The denominator is nonzero for rational a and b unless both vanish, because otherwise two would be the square of a rational number. This produces the field usually called Q adjoin square root of two.

An equally concrete example starts from the field with two elements. In that field, x squared plus x plus one has no root: plugging in zero gives one and plugging in one gives one. Being quadratic, it is irreducible. The quotient has four elements: zero, one, alpha, and one plus alpha. The defining relation says alpha squared plus alpha plus one equals zero; in characteristic two, subtraction and addition agree, so alpha squared equals alpha plus one. There is a field with four elements, even though there is no field formed by reducing ordinary integers modulo four.

### Repeated roots and derivatives

The formal derivative of a polynomial is computed by the familiar power rule. If f factors as x minus a squared times another polynomial, then both f and its derivative vanish at a. Conversely, over any field, if f and its derivative share a nonconstant factor, then f has a repeated irreducible factor in an algebraic closure. This gcd criterion is a useful algebraic test.

There is a subtlety in positive characteristic. In characteristic p, the derivative of x to the p minus c is identically zero, even though the polynomial need not be constant. Differentiation has not failed; coefficients such as p are zero in that field. Later field theory will distinguish separable and inseparable polynomials precisely because roots and derivatives behave differently in some characteristics.

Polynomial arithmetic has given us a method for adjoining new elements with controlled relations. Division, factorization, greatest common divisors, and quotients all work together. A root need not be found somewhere in the old field; it can be constructed in a larger one. The hard requirement is not that our symbol looks like a familiar number, but that the equations defining it are compatible with valid arithmetic.

## Field Extensions, Minimal Polynomials, and Degrees

The familiar expression square root of two behaves like a number. But it is also the result of a precise construction: begin with the rational numbers, introduce an element alpha, impose the relation alpha squared equals two, and form a field from the resulting expressions. Once we have done that, a deeper question appears. How much larger is the new field? Can we adjoin several elements and still keep track of what changes?

Field extensions answer this by treating fields as vector spaces over smaller fields. That lets algebraic equations acquire a notion of dimension.

### Enlarging the available numbers

A field extension L over K means K is a subfield of L, using the same addition and multiplication. Every element of L can be multiplied by elements of K, so L is a vector space over K. Its dimension, if finite, is written the degree of L over K.

For rational numbers with the square root of two adjoined, every element is a plus b times square root of two, with a and b rational. The elements one and square root of two are linearly independent over the rationals. If a plus b square root of two equals zero and b were nonzero, the square root of two would be rational, which it is not. Consequently the degree of this extension is two.

Adding a number does not always enlarge a field. The square root of four is already rational, so adjoining it leaves the field unchanged. The square root of two is different: it obeys the polynomial equation x squared minus two equals zero, but no linear polynomial with rational coefficients has it as a root. The smallest polynomial relation is what tells us how far the old field must be extended.

### The minimal polynomial

An element alpha of L is algebraic over K if it satisfies some nonzero polynomial with coefficients in K. Otherwise it is transcendental over K. For an algebraic element, choose the monic polynomial of least positive degree that vanishes at alpha. This is its minimal polynomial.

The minimal polynomial must be irreducible. If it factored into two lower-degree polynomials, their values at alpha would multiply to zero. Fields have no zero divisors; at least one factor would vanish at alpha, contradicting minimality.

Moreover, any polynomial that vanishes at alpha is divisible by the minimal polynomial. Divide it by the minimal polynomial, leaving a smaller-degree remainder. Evaluate at alpha. The original polynomial and the multiple of the minimal polynomial both vanish, so the remainder vanishes. Its degree is too small unless it is zero.

This means that evaluation at alpha gives a homomorphism from K polynomials to L whose kernel is generated by the minimal polynomial. The first isomorphism theorem identifies the field K of alpha—meaning the smallest subfield containing K and alpha—with the polynomial quotient by that minimal polynomial. Every element of K of alpha has a unique expression as a linear combination of one, alpha, up to alpha to the power n minus one, where n is the degree of the minimal polynomial. Thus extension degree equals minimal-polynomial degree.

For the cube root of two over the rationals, the minimal polynomial is x cubed minus two. It has no rational root: if a rational cube in lowest terms equaled two, the numerator and denominator would again have a common factor two. A cubic without a root over a field is irreducible. So the extension has degree three, with basis one, cube root of two, and its square.

For an element transcendental over K, no nonzero polynomial evaluates to zero, and the evaluation map is injective. Adjoining a transcendental element instead produces a rational-function field, not a finite-dimensional extension. This is a different kind of enlargement.

### The tower law

Suppose K sits inside L, and L sits inside M, with both steps finite. Then the degree of M over K is the product of the degree of M over L and the degree of L over K.

The proof is constructive. Choose a K-basis b-one through b-m for L, and an L-basis c-one through c-n for M. We claim that the m times n products b-i times c-j form a K-basis of M. For spanning, write an element of M as an L-linear combination of the c-j and then expand each L-coefficient in the b-i basis. For independence, suppose a K-linear combination of all those products vanishes. Group by the c-j. Independence over L makes each grouped L-coefficient zero. Independence of the b-i over K makes every original coefficient zero. That establishes the product formula.

This theorem provides a test for proposed intermediate fields. If an extension of the rationals has degree three, it cannot contain an intermediate field of degree two over the rationals, since two would have to divide three. The statement is about fields, not about the number of elements we happened to write down.

### Adjoining more than one root

Consider the field obtained by adjoining both square root of two and square root of three to the rationals. First adjoin square root of two, a degree-two step. Does square root of three already belong to that field? If it did, there would be rational a and b with a plus b square root of two equal to square root of three. Squaring gives three equals a squared plus two b squared plus two a b square root of two. Since the right side is rational only when a b is zero, either a is zero or b is zero. If b is zero, three is a rational square. If a is zero, three divided by two is a rational square. Neither can happen. Thus the second adjoining also has degree two.

The tower law says the final degree is four. A basis consists of one, square root of two, square root of three, and square root of six. Every expression involving these two radicals can be reduced to a rational linear combination of those four terms.

There is a useful surprise: sometimes one element generates a field originally described by several. Let beta be square root of two plus square root of three. Since the reciprocal of beta is square root of three minus square root of two, both radicals can be recovered by adding and subtracting beta and its reciprocal. So the field generated by beta already contains both square roots. The degree of beta over the rationals is four, and it satisfies the quartic polynomial x to the fourth minus ten x squared plus one. This equation comes from beta squared equals five plus two square root of six, followed by squaring after subtracting five.

### Constructing enough roots

Adjoining one root of a polynomial does not necessarily make all its roots appear. The polynomial x cubed minus two provides an example. Adding the real cube root of two gives a degree-three subfield of the real numbers. The other two complex cube roots are not real, so they are not in that field.

To make a polynomial split completely into linear factors, we may have to adjoin additional roots. A splitting field is an extension generated by all the roots of the polynomial in which it factors into linear terms. One can build a finite splitting field by successively adjoining roots of remaining irreducible factors. At each step, the polynomial quotient construction gives a field containing a new root; the degree may grow, but every step is finite.

Over the complex numbers, every nonconstant complex polynomial has a root—the fundamental theorem of algebra. Here we are not proving that theorem. Our field-extension construction answers a different question: given an arbitrary base field and a polynomial, how can an extension containing its roots be built algebraically, without waiting for a formula for those roots?

The arithmetic of roots is governed by the relations they satisfy. Minimal polynomials identify those relations. Vector-space degrees count how much the field has grown. The tower law makes successive constructions composable. Those three ideas will eventually let us study automorphisms that permute roots while fixing the original coefficients—the central idea of Galois theory.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Divisibility, the Euclidean Algorithm, and Arithmetic Modulo n

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** integer arithmetic and the basic idea of a quotient group. **Question:** why can a calculation about remainders certify the existence of inverses?

#### Mathematical companion (not spoken)

For integers \(a,b\), \(\gcd(a,b)>0\) unless both vanish, and Bézout's identity yields \(u,v\in\mathbb Z\) with \(ua+vb=\gcd(a,b)\).

Euclidean divisions and backward substitution:
\[
26=3\cdot7+5,\quad7=1\cdot5+2,\quad5=2\cdot2+1,
\]
\[
1=5-2(7-5)=3(26-3\cdot7)-2\cdot7=3\cdot26-11\cdot7.
\]
Thus \(7^{-1}\equiv -11\equiv15\pmod{26}\).

**Unit criterion:** \([a]\in(\mathbb Z/n\mathbb Z)^\times\iff\gcd(a,n)=1\). **Field criterion:** for \(n>1\), \(\mathbb Z/n\mathbb Z\) is a field iff \(n\) is prime. **Linear congruence:** \(ax\equiv b\pmod n\) is solvable iff \(\gcd(a,n)\mid b\), and has \(\gcd(a,n)\) distinct solution classes modulo \(n\) when solvable.

##### Exercises with answers

1. Find the inverse of three modulo eleven. **Answer:** Four, because three times four is twelve, congruent to one.
2. Why can't two be canceled from \(2x\equiv2y\pmod6\)? **Answer:** Two is not a unit modulo six; for instance \(x=0\), \(y=3\) satisfy the equality.
3. Does \(6x\equiv5\pmod{26}\) have a solution? **Answer:** No, because the gcd is two, which does not divide five.
4. Find both solutions of \(6x\equiv4\pmod{26}\). **Answer:** Five and eighteen modulo twenty-six.

##### Reading

Judson, *Abstract Algebra: Theory and Applications*, integers, modular arithmetic, and rings; MIT 6.042J *Mathematics for Computer Science*, sections on number theory, divisibility, and modular arithmetic.

### Rings, Ideals, and Quotients: Which Arithmetic Can Be Collapsed?

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** groups, kernels, and arithmetic modulo an integer. **Question:** what replaces a normal subgroup when we want a quotient that still supports multiplication?

#### Mathematical companion (not spoken)

Here all rings are commutative with identity and homomorphisms preserve identity. An ideal \(I\subset R\) is an additive subgroup satisfying \(rI\subseteq I\) for all \(r\in R\).

For \(a-a',b-b'\in I\),
\[
ab-a'b'=a(b-b')+(a-a')b'\in I.
\]
Hence \([a][b]:=[ab]\) is well defined in \(R/I\).

**First isomorphism theorem:** for \(\varphi:R\to S\), \(R/\ker\varphi\cong\operatorname{im}\varphi\) via \([r]\mapsto\varphi(r)\).

**Quotient tests:** if \(I\) is proper, \(I\) prime iff \(R/I\) is an integral domain, and \(I\) maximal iff \(R/I\) is a field.

**Worked kernels:**
\[
\ker(\mathbb Q[x]\xrightarrow{f\mapsto f(2)}\mathbb Q)=(x-2),
\]
\[
\ker(\mathbb Z[x]\xrightarrow{f\mapsto f(0)\bmod2}\mathbb F_2)=(2,x).
\]

##### Exercises with answers

1. Why is \(2\mathbb Z\) an ideal of \(\mathbb Z\)? **Answer:** differences of even integers are even, and any integer times an even integer is even.
2. Prove \((x^2+1)\subset\mathbb R[x]\) is maximal. **Answer:** \(x^2+1\) is irreducible over \(\mathbb R\); Euclidean division in \(\mathbb R[x]\) shows every ideal strictly containing it is the whole ring.
3. Is \((6)\) prime in \(\mathbb Z\)? **Answer:** no: \(2\cdot3\in(6)\) but neither factor is in \((6)\).
4. Identify \(\mathbb Z[x]/(x,2)\). **Answer:** \(\mathbb F_2\), by parity of the constant term.

##### Reading

Judson, *Abstract Algebra: Theory and Applications*, chapters on rings and ideals; Keith Conrad, [Expository papers](https://kconrad.math.uconn.edu/blurbs/), sections on quotient rings and maximal ideals.

### Polynomial Rings, Factorization, and Irreducibility

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** rings, ideals, quotients, and the Euclidean algorithm for integers. **Question:** why can a polynomial become zero without collapsing the whole arithmetic system?

#### Mathematical companion (not spoken)

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

##### Exercises with answers

1. Divide \(x^3+1\) by \(x+1\). **Answer:** quotient \(x^2-x+1\), remainder zero.
2. Is \(x^2+x+1\) irreducible over \(\mathbb F_2\)? **Answer:** yes; neither field element is a root.
3. In \(\mathbb Q(\sqrt2)\), invert \(1+\sqrt2\). **Answer:** \(\sqrt2-1\), since their product is one.
4. Is \(x^2-1\) irreducible over \(\mathbb Q\)? **Answer:** no, it factors as \((x-1)(x+1)\); the corresponding quotient is not a field.

##### Reading

Judson, *Abstract Algebra: Theory and Applications*, polynomial rings and fields; Keith Conrad, [Expository papers](https://kconrad.math.uconn.edu/blurbs/), irreducibility tests, roots, and irreducible polynomials.

### Field Extensions, Minimal Polynomials, and Degrees

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** polynomial division, irreducibility, and quotient rings. **Question:** how do we measure the new arithmetic introduced by adjoining a root?

#### Mathematical companion (not spoken)

An extension \(L/K\) is finite if \(\dim_K L<\infty\). For algebraic \(\alpha\in L\), its monic minimal polynomial \(m_{\alpha,K}\) is irreducible and
\[
K(\alpha)\simeq K[x]/(m_{\alpha,K}),\qquad [K(\alpha):K]=\deg m_{\alpha,K}.
\]
If \(K\subseteq L\subseteq M\) and both indicated degrees are finite, then
\[
[M:K]=[M:L][L:K].
\]

**Worked example:** \(\beta=\sqrt2+\sqrt3\); \(\beta^{-1}=\sqrt3-\sqrt2\), so
\[
\sqrt3=\frac{\beta+\beta^{-1}}2,\quad
\sqrt2=\frac{\beta-\beta^{-1}}2,\quad
\beta^4-10\beta^2+1=0.
\]
Because \(\mathbb Q(\beta)=\mathbb Q(\sqrt2,\sqrt3)\) has degree four, the displayed quartic is minimal.

##### Exercises with answers

1. What is \([\mathbb Q(i):\mathbb Q]\)? **Answer:** two, with minimal polynomial \(x^2+1\).
2. Can a degree-five extension over \(K\) contain a degree-two intermediate extension? **Answer:** no, by the tower law.
3. What is a basis for \(\mathbb Q(\sqrt2,\sqrt3)\) over \(\mathbb Q\)? **Answer:** \(1,\sqrt2,\sqrt3,\sqrt6\).
4. Why does adjoining the real cube root of two not split \(x^3-2\)? **Answer:** the two nonreal roots are missing from the real field obtained.

##### Reading

Judson, *Abstract Algebra: Theory and Applications*, field extensions; Keith Conrad, [Expository papers](https://kconrad.math.uconn.edu/blurbs/), roots, minimal polynomials, and splitting fields.
