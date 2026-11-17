# 033000 — Hilbert Reciprocity: One Identity Across Every Prime and Infinity

**Track:** Number Theory from First Principles. **Background:** 007000 (quadratic reciprocity and its supplementary laws), 032250–032750 (Hilbert symbols and local quadratic forms). **Aim:** prove the rational Hilbert reciprocity product formula directly from explicit local symbols and quadratic reciprocity, including the place at infinity.

<!-- BEGIN SPOKEN LECTURE -->

# Hilbert Reciprocity: One Identity Across Every Prime and Infinity

We have built a test for the solvability of a quadratic norm equation over every p-adic field. At odd primes the test uses Legendre symbols; at two it uses residues modulo four and eight. Every place has its own rule, and it may seem that the answers at different places are unrelated.

But suppose the coefficients are rational numbers. Then the local Hilbert symbols cannot vary independently. Multiply all their signs together, including one extra sign from the real numbers, and the product is always positive one.

This is Hilbert reciprocity over the rational numbers. It is not a new assumption added to the story. We can prove it from the quadratic reciprocity law that we established earlier. In fact, it packages quadratic reciprocity and its two supplementary laws into one identity that gives two equal roles to the odd primes and gives the prime two and the infinite place an explicit place in the formula.

## The real place is another local calculation

Over the real numbers, the symbol of a and b is defined by the same equation: z squared equals a x squared plus b y squared. When both a and b are negative, the right side is nonpositive and can equal the nonnegative left side only when all variables vanish. So the symbol is minus one.

If at least one of a and b is positive, we can produce a nontrivial real solution. For instance, if a is positive, choose x equal to one, y equal to zero, and z equal to the positive square root of a. Thus the real symbol is positive unless both coefficients are negative.

The real numbers belong in the product just as much as Q-two or Q-seven. Their obstruction is the familiar distinction between positive and negative, but their algebraic role is identical.

## Why there are only finitely many signs to multiply

Let a and b be nonzero rational numbers. Write each as a sign times a product of integer powers of primes, allowing negative powers for denominators. At any odd prime that divides neither numerator nor denominator of either number, both inputs are p-adic units. We proved that the symbol of two units at an odd prime is always positive.

So only finitely many odd primes can contribute a negative factor. Together with the prime two and the real place, this means that the product over all places makes sense. It is an ordinary product of finitely many negative signs and infinitely many positive ones.

Because the Hilbert symbol is multiplicative in each argument, it is enough to prove the product formula on generators of the rational multiplicative group modulo squares. These generators are negative one, the prime two, and each positive odd prime. We must check their possible pairings. Symmetry saves us from reversing every case.

## Pairings involving negative one

Begin with negative one against negative one. At every odd prime, both are units, so their symbol is positive. At two, we proved that the symbol is negative, because both are three modulo four. At the real place, both inputs are negative, so that symbol is negative as well. Two negative factors give a positive product.

Next pair negative one with two. The real symbol is positive because two is positive. The two-adic symbol of two with negative one is positive, because negative one is seven modulo eight. At every odd prime, both are units. There is no negative factor at all.

Now pair negative one with an odd positive prime p. The real symbol is positive. All odd primes other than p give a positive symbol. At p, the symbol is the Legendre symbol of negative one modulo p. At two, the unit-pair formula produces minus one to the power p minus one over two. But Euler's criterion tells us that this is exactly the Legendre symbol of negative one modulo p. The two potentially negative factors agree and their product is positive.

These cases already show why the infinite place and the prime two should not be omitted. Without them, the product formula would fail for negative one paired with itself.

## Pairings involving two

Now pair two with two. At all odd primes they are both units; at infinity at least one input is positive; and we explicitly proved that the two-adic symbol of two with two is positive. The product is positive.

Pair two with an odd positive prime p. Only two and p can matter. At the prime p, the odd-prime formula says the symbol is the Legendre symbol of two modulo p. At the prime two, our formula says the symbol is minus one to the power p squared minus one over eight. The supplementary law of quadratic reciprocity asserts that the Legendre symbol of two modulo p is exactly that sign. The two factors cancel.

This example contains the whole prime-two supplement, not as a separate arbitrary convention but as the local factor needed to make the global product equal one.

## Pairings of odd primes

Take an odd prime p against itself. At every odd prime other than p, both inputs are units. At infinity, the symbol is positive. At p, the odd-prime formula gives the Legendre symbol of negative one modulo p. At two, the formula for two odd units gives minus one to the power of the square of p minus one over two. The parity of that square equals the parity of p minus one over two, so the two factors again agree. Their product is positive.

Finally take two *distinct* odd primes p and q. At all primes other than two, p, and q, both inputs are units and the symbols are positive. At p, the symbol is the Legendre symbol of q modulo p. At q, it is the Legendre symbol of p modulo q. At two, it is minus one to the product of p minus one over two and q minus one over two. The real symbol is positive.

We have reached the classical quadratic reciprocity law itself. It says exactly that the product of these three signs is positive one. Therefore the Hilbert product formula holds for two distinct odd primes as well.

That exhausts the cases: negative one with itself, with two, and with an odd prime; two with itself and with an odd prime; an odd prime with itself; and two distinct odd primes. Multiplicativity extends the result to products and quotients of all of these generators, which are all nonzero rational numbers.

We have proved Hilbert reciprocity: for every nonzero rational a and b, the product of the local symbols over the real place and every prime p equals positive one.

## A global restriction, not yet a global solution

The product law tells us that local quadratic obstructions must occur in a compatible pattern. For example, consider the conic x squared plus y squared equals three z squared, which corresponds to the Hilbert symbol of negative one and three. We found a negative symbol at p equal to three and another at p equal to two. Every other local symbol, including infinity, is positive. The product is therefore one, just as reciprocity predicts.

It would be a mistake to interpret the product law as claiming that a rational solution exists whenever the negative signs appear in pairs. Two negative signs can mean two places where the equation has no solution; that is exactly what happened in this example. The product formula is a *constraint on the obstructions*, not a method for making them disappear.

The Hasse–Minkowski theorem supplies a different kind of statement. For a quadratic form over the rationals, it says that if there is a nontrivial zero over the reals and over every p-adic field, then there is one over the rationals. The easy direction, from rational to local solutions, is automatic. The hard direction takes a proof that we have not yet given.

Hilbert reciprocity is one indispensable ingredient in the broader theory, but we have proved it here as an independent theorem, without borrowing Hasse–Minkowski. It also makes clear how the familiar nineteenth-century quadratic reciprocity law is recast in the language of twentieth-century local fields: every prime contributes a sign, the real place contributes another, and their product is forced to be one.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(v=\infty\), set \(\mathbb Q_v=\mathbb R\) and
\[
(a,b)_\infty=-1\iff a<0\text{ and }b<0.
\]
For finite primes use 032250–032500. If \(p\nmid 2ab\) (numerators and denominators of a,b), then \((a,b)_p=1\), so the product is finite:
\[
\boxed{\prod_{v\in\{\infty,2,3,5,\ldots\}}(a,b)_v=1\quad(a,b\in\mathbb Q^\times).}
\]

### Generator check

Bimultiplicativity and symmetry reduce the claim to \(a,b\in\{-1,2\}\cup\{p:p\text{ odd prime}\}\). The potentially nontrivial local symbols are:

| Pair | Nontrivial places and signs | Why product is +1 |
|---|---|---|
| \((-1,-1)\) | \(v=2:-1\); \(v=\infty:-1\) | two minus signs |
| \((-1,2)\) | none | \((2,-1)_2=+1\) |
| \((-1,p)\) | \(v=p:(-1/p)\); \(v=2:(-1)^{(p-1)/2}\) | supplementary law for −1 |
| \((2,2)\) | none | \((2,2)_2=+1\) |
| \((2,p)\) | \(v=p:(2/p)\); \(v=2:(-1)^{(p^2-1)/8}\) | supplementary law for 2 |
| \((p,p)\) | \(v=p:(-1/p)\); \(v=2:(-1)^{((p-1)/2)^2}\) | supplementary law for −1 |
| \((p,q),\ p\neq q\) odd | \(v=p:(q/p)\); \(v=q:(p/q)\); \(v=2:(-1)^{(p-1)(q-1)/4}\) | quadratic reciprocity |

All other places contribute +1 in each row. Negative exponents of primes cause no difficulty since each symbol is its own inverse. This proves the product formula for all nonzero rational inputs.

### A concrete two-obstruction example

\[
(-1,3)_2=-1,\quad(-1,3)_3=-1,\quad(-1,3)_v=1\quad(v\neq 2,3).
\]
These obstructions show \(x^2+y^2=3z^2\) has no nontrivial rational solution, while the product formula still holds. It does **not** prove the Hasse–Minkowski converse.

### Exercises

1. Reproduce the row \((-1,p)\) from the two Hilbert formulas rather than from the table.
2. Verify the product formula explicitly for \(a=6\) and \(b=15\), listing every nontrivial local factor.
3. Use quadratic reciprocity to verify the pair \((3,7)\), including its factor at two.
4. Explain why an equation with no Q_2-solution and no Q_3-solution is consistent with global Hilbert reciprocity.
5. State the difference between the Hilbert product identity and Hasse–Minkowski as two logically distinct assertions.

### Reading and source notes

- Ming-Lun Hsieh, National Taiwan University, [Hilbert symbol notes](https://www.math.ntu.edu.tw/~mlhsieh/teaching/L4.pdf), explicit formulas and reciprocity theorem.
- Keith Conrad, [History of class field theory](https://kconrad.math.uconn.edu/blurbs/gradnumthy/cfthistory.pdf), the historical reinterpretation of quadratic reciprocity as Hilbert's product formula.
- Wikipedia: [Hilbert symbol](https://en.wikipedia.org/wiki/Hilbert_symbol), [Quadratic reciprocity](https://en.wikipedia.org/wiki/Quadratic_reciprocity), [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem).
