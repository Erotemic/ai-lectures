# 004000 — Divisibility, the Euclidean Algorithm, and Arithmetic Modulo n

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** integer arithmetic and the basic idea of a quotient group. **Question:** why can a calculation about remainders certify the existence of inverses?

<!-- BEGIN SPOKEN LECTURE -->

# Divisibility, the Euclidean Algorithm, and Arithmetic Modulo n

There is a practical question hiding inside a simple-looking congruence. Suppose we want to solve seven times x gives remainder one on division by twenty-six. Is there such an integer x? If so, how do we find it? And why can a similar-looking question, six times x gives remainder one modulo twenty-six, have no solution at all?

The answer combines divisibility, the Euclidean algorithm, and a theorem about writing greatest common divisors as combinations of integers. It leads directly to the distinction between rings and fields.

## Divisibility is a statement about existence

We say a divides b if b equals a times some integer. For example, four divides twenty-eight because twenty-eight is four times seven. The statement “a divides b” is not a request to calculate a decimal quotient. It asserts that an integer witness exists.

A common divisor of a and b divides both. The greatest common divisor, when a and b are not both zero, is the largest positive integer with that property. Because the greatest common divisor is defined using positive integers, signs do not affect it. The greatest common divisor of twenty-six and seven is one: they share no positive factor larger than one.

The Euclidean algorithm computes the greatest common divisor by repeatedly taking remainders. Twenty-six equals three times seven plus five. Seven equals one times five plus two. Five equals two times two plus one. Two equals two times one plus zero. The last nonzero remainder, one, is the greatest common divisor.

Why does the algorithm work? If a equals q times b plus r, any integer dividing both a and b also divides r, because r is a minus q times b. Conversely, any integer dividing b and r divides a. So a and b have exactly the same common divisors as b and r. Each remainder is smaller in absolute value than the previous positive divisor. Eventually the remainders must reach zero, and the last nonzero remainder is the desired greatest common divisor. That is a proof of termination and correctness, not merely a convenient recipe.

## Read the divisions backward

The calculation contains more information than the greatest common divisor. Starting from the equation one equals five minus two times two, replace two by seven minus five. We obtain one equals three times five minus two times seven. Replace five by twenty-six minus three times seven. The result is one equals three times twenty-six minus eleven times seven.

This displays the greatest common divisor as an integer combination of the original inputs. In this example, three times twenty-six plus negative eleven times seven equals one. Such a statement is called Bézout's identity. More generally, the Euclidean algorithm can be run backward to express the greatest common divisor of a and b as an integer combination of a and b.

There is also a converse: every integer combination of a and b is divisible by their greatest common divisor. Consequently, if an integer combination equals one, the greatest common divisor must be one. These two directions make Bézout's identity a powerful characterization of coprimality.

We can now solve our opening congruence. The identity says negative eleven times seven differs from one by negative three times twenty-six. So seven times negative eleven has remainder one modulo twenty-six. Reducing negative eleven modulo twenty-six gives fifteen. Check: seven times fifteen is one hundred five, which leaves remainder one after subtracting four twenty-sixes.

In other words, fifteen is a multiplicative inverse of seven modulo twenty-six.

## Two operations on remainder classes

The integers modulo n form a group under addition. But they also have multiplication: multiply any representatives and reduce the result modulo n. The result does not depend on the representative choices. If a and a prime differ by a multiple of n, and b and b prime do as well, their products differ by a multiple of n because the difference can be expanded into terms each containing n.

A set with addition and multiplication obeying the usual ring rules, including distributivity, is called a ring. The integers themselves are a ring. So are the residue classes modulo n. We usually require an additive identity, additive inverses, associative multiplication, and distributivity; here we also have a multiplicative identity and commutative multiplication. Rings do not require every nonzero element to have a multiplicative inverse.

Our inverse calculation suggests the exact criterion for a residue class to be invertible modulo n: its representative a must have greatest common divisor one with n. If that gcd equals one, Bézout gives integers u and v such that u a plus v n equals one; reduction modulo n shows u is an inverse of a. Conversely, if a u is congruent to one, then a u minus one is a multiple of n, and we have an integer combination of a and n equal to one. Therefore their gcd is one.

Try a equal to six and n equal to twenty-six. Their gcd is two. Every product six times x is even, and so is every multiple of twenty-six. Their difference can never equal the odd number one. No inverse exists. This is not a defect in our algorithm; the algebra forbids a solution.

## Prime moduli are different

If p is prime, every residue class other than zero has a representative not divisible by p, and hence has greatest common divisor one with p. Every nonzero class has a multiplicative inverse. A commutative ring with one in which every nonzero element is invertible is a field. Therefore the residues modulo a prime p form a field.

If n is composite, write n as a product of two integers strictly between one and n. Neither factor is zero modulo n, but their product is zero modulo n. These are zero divisors. A field cannot have zero divisors: if a times b equals zero and a is nonzero, multiply by the inverse of a to conclude b equals zero. Thus residues modulo a composite integer cannot be a field.

This gives an exact classification for positive moduli greater than one: the ring of integers modulo n is a field if and only if n is prime.

An instructive contrast is modulo six. Two times three is zero modulo six although neither factor is zero. So the cancellation law familiar from nonzero real-number multiplication fails. If two times x equals two times y modulo six, x and y need not be equal; for instance two times zero and two times three have the same residue. Cancellation works only when the factor being canceled is a unit, meaning it has an inverse.

## Congruences as a structural tool

A congruence a equals b modulo n means their difference is divisible by n. It is compatible with addition and multiplication, so calculations may be carried out using representatives and reduced whenever convenient. We are not “approximating” an integer by a remainder. We are choosing to ask a question in a quotient structure where multiples of n have been identified with zero.

This distinction matters for solving linear congruences. The equation a x equals b modulo n has a solution exactly when the greatest common divisor of a and n divides b. We can see necessity from the equation a x minus n k equals b: the gcd divides the left side and therefore b. For sufficiency, Bézout expresses the gcd as a combination of a and n. Multiply that identity by b divided by the gcd, and it becomes an integer solution of the congruence.

For example, six times x equals four modulo twenty-six does have solutions, because the gcd is two and two divides four. Dividing the integer equation by two leads to three times x equals two modulo thirteen, where three has an inverse. One solution is x equal to five, since six times five is thirty, congruent to four modulo twenty-six. Adding thirteen gives another solution, eighteen, modulo twenty-six. The equation has exactly two residue solutions modulo twenty-six, matching the gcd.

## A small algorithm, a large distinction

The Euclidean algorithm is a model of what good mathematics and good computation share: a finite process, a proof that it terminates, a preserved invariant, and an independently checkable answer. Bézout's identity upgrades its output into a certificate. Modular arithmetic then turns that certificate into an inverse, or explains why none exists.

We have also crossed from groups into rings and fields. Addition alone supplies a group. Addition and multiplication interact in a ring. In a field, every nonzero multiplier can be undone. The difference determines which cancellations and equations are legitimate. Abstract algebra keeps track of those permissions instead of allowing familiar arithmetic intuition to smuggle them in.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Find the inverse of three modulo eleven. **Answer:** Four, because three times four is twelve, congruent to one.
2. Why can't two be canceled from \(2x\equiv2y\pmod6\)? **Answer:** Two is not a unit modulo six; for instance \(x=0\), \(y=3\) satisfy the equality.
3. Does \(6x\equiv5\pmod{26}\) have a solution? **Answer:** No, because the gcd is two, which does not divide five.
4. Find both solutions of \(6x\equiv4\pmod{26}\). **Answer:** Five and eighteen modulo twenty-six.

### Reading

Judson, *Abstract Algebra: Theory and Applications*, integers, modular arithmetic, and rings; MIT 6.042J *Mathematics for Computer Science*, sections on number theory, divisibility, and modular arithmetic.
