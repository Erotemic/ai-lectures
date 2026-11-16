# 005000 — Rings, Ideals, and Quotients: Which Arithmetic Can Be Collapsed?

**Track:** Abstract Algebra: Structure, Symmetry, and Arithmetic. **Background:** groups, kernels, and arithmetic modulo an integer. **Question:** what replaces a normal subgroup when we want a quotient that still supports multiplication?

<!-- BEGIN SPOKEN LECTURE -->

# Rings, Ideals, and Quotients: Which Arithmetic Can Be Collapsed?

In ordinary integer arithmetic, we are free to replace a number by its remainder modulo five, add two remainders, multiply them, and reduce again. The answer is independent of the integer representatives we chose. But what authorizes this maneuver? Why is congruence modulo five compatible with two different operations, while a partition of the integers into even and odd classes is only one of many possible ways to identify numbers?

The key is an *ideal*. An ideal tells us which differences may be treated as zero without breaking multiplication. Once we understand that demand, the correspondence between algebraic maps and quotients becomes precise.

## Two operations, one structure

For now, a ring will mean a set with addition, subtraction, and multiplication, with associative multiplication, distributivity over addition, and a multiplicative identity. Addition makes an abelian group. We will focus mainly on commutative rings, such as the integers, rather than rings of matrices where multiplication can depend on the order.

The integers are a ring; the rational numbers are a ring with the extra property that every nonzero element is invertible. So are polynomials with rational coefficients. The difference between a ring and a field matters: multiplication in a ring may have no inverse operation for many elements.

Consider a ring homomorphism. It is a map preserving addition and multiplication, and in our convention preserving the element one. The familiar map sending each integer to its remainder class modulo five is a ring homomorphism. So is the map from rational polynomials to rational numbers that evaluates a polynomial at two. Evaluation commutes with addition and multiplication: evaluating a sum gives the sum of evaluations, and evaluating a product gives the product of evaluations.

Ask which inputs a homomorphism sends to zero. For reduction modulo five, they are the multiples of five. For evaluation at two, they are the polynomials with two as a root. The two examples live in different rings, yet their kernels obey the same rules.

## Why the kernel is an ideal

If elements a and b map to zero, then their difference maps to zero. The kernel is therefore an additive subgroup. But there is more. If a maps to zero and r is any ring element, the product r times a also maps to zero. Its image is the image of r multiplied by zero.

This multiplication property distinguishes an ideal from a mere additive subgroup. In a commutative ring, an ideal is an additive subgroup closed under multiplication by arbitrary elements of the ambient ring. In a noncommutative ring, a two-sided ideal must absorb multiplication on both the left and the right; that is what supports the ordinary quotient ring construction.

The integer multiples of five form an ideal. All integer ideals are sets of multiples of some nonnegative integer. That assertion itself follows from division with remainder: if a nonzero ideal contains a least positive integer d, divide any element of the ideal by d; the remainder belongs to the ideal, so minimality forces it to be zero.

Contrast the even integers inside the ring of integers with the set of all integer multiples of a polynomial's *value* at two. The latter description depends on what ring we are working in. We should not confuse the numbers that appear as evaluations with the polynomials being evaluated. In the polynomial ring, the kernel of evaluation at two is the ideal of multiples of the polynomial x minus two. The factor theorem proves this: a polynomial vanishes at two precisely when x minus two divides it.

## Constructing a quotient ring

Given an ideal I in a commutative ring R, declare a equivalent to b when their difference lies in I. The equivalence classes are cosets, just as in quotient groups. Define addition and multiplication on classes by adding or multiplying representatives.

To see why multiplication is legal, suppose a differs from a-prime by an element of I, and b differs from b-prime by an element of I. The difference a b minus a-prime b-prime is the sum of a times b minus b-prime and b-prime times a minus a-prime. Both terms are in I by the absorption property. Hence the product's class is independent of representatives.

Notice exactly where the ideal hypothesis was used. The additive-group quotient needs only additive closure. The ring quotient needs closure under multiplication by *everything in the ring*, because representatives can be multiplied by arbitrary elements.

The resulting quotient is written R modulo I. In the integers, modulo the ideal of multiples of five gives the five residue classes. In rational polynomials, modulo the ideal generated by x minus two gives a structure in which the variable x becomes equal to two. The entire quotient is naturally just the rational numbers.

## A structure theorem for maps

Let phi be a ring homomorphism from R to S. Its kernel consists of exactly those differences that phi cannot distinguish. Map the coset of an element r, modulo the kernel, to phi of r. This is well defined: two representatives differ by a kernel element exactly when their images are equal. It preserves addition, multiplication, and one. It is injective, because the only coset sent to zero is the kernel coset, and it is surjective onto the image of phi by construction.

So R modulo the kernel is isomorphic to the image. This is the first isomorphism theorem for rings. It is not a complicated coincidence. The quotient removes exactly the information the map loses, and no more.

For example, evaluate integer polynomials at zero, then reduce the integer result modulo two. The map takes a polynomial to the parity of its constant term. Its kernel includes every polynomial with an even constant term; in fact the kernel is the ideal generated by two and x. The quotient has exactly two elements, corresponding to even and odd constant terms. Even when an ideal has more than one generator, the same principle applies.

## Prime and maximal ideals

A ring quotient can contain zero divisors. Modulo six, the nonzero classes two and three multiply to zero. Two different ideals explain two different ways this can happen.

For a commutative ring with identity, an ideal P is called prime when it is proper and the product a b lies in P only if at least one of a and b lies in P. Exactly when P is prime, the quotient R modulo P has no zero divisors. A proper ideal M is maximal when no proper ideal lies strictly between M and the whole ring. Exactly when M is maximal, the quotient is a field.

Here is the reason for the maximal-ideal criterion. In the quotient, take any nonzero class a. Its representative is not in M. The ideal generated by M together with a strictly contains M; maximality therefore makes that ideal the whole ring. So one can write one as m plus r times a, with m in M. Reduce modulo M and we obtain an inverse for the class of a. The converse follows because a field has no nontrivial proper ideals: a nonzero element in an ideal has an inverse, which forces one to belong to that ideal.

In the integers, the ideal of multiples of a prime number p is maximal, and the quotient is a finite field. The ideal of multiples of six is neither prime nor maximal. In a polynomial ring over a field, an ideal generated by a nonconstant irreducible polynomial is maximal. That observation will make it possible to construct fields by declaring a chosen polynomial to be zero.

## Quotients are controlled forgetfulness

A quotient ring is not an arbitrary act of identifying symbols. It is an agreement about which differences count as zero, disciplined by the requirement that all legal computations respect the agreement.

The distinction between subgroups and ideals answers our opening question. A group quotient must preserve composition. A ring quotient must preserve addition and multiplication together. The ideal absorbs arbitrary multipliers because otherwise multiplication on classes would depend on a representative that is supposed to have been forgotten. This is the algebraic idea behind modular arithmetic, polynomial evaluation, and the construction of new number systems.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. Why is \(2\mathbb Z\) an ideal of \(\mathbb Z\)? **Answer:** differences of even integers are even, and any integer times an even integer is even.
2. Prove \((x^2+1)\subset\mathbb R[x]\) is maximal. **Answer:** \(x^2+1\) is irreducible over \(\mathbb R\); Euclidean division in \(\mathbb R[x]\) shows every ideal strictly containing it is the whole ring.
3. Is \((6)\) prime in \(\mathbb Z\)? **Answer:** no: \(2\cdot3\in(6)\) but neither factor is in \((6)\).
4. Identify \(\mathbb Z[x]/(x,2)\). **Answer:** \(\mathbb F_2\), by parity of the constant term.

### Reading

Judson, *Abstract Algebra: Theory and Applications*, chapters on rings and ideals; Keith Conrad, [Expository papers](https://kconrad.math.uconn.edu/blurbs/), sections on quotient rings and maximal ideals.
