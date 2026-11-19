# 032250 — Norms and Hilbert Symbols at Odd Primes

**Track:** Number Theory from First Principles. **Background:** 006000–007000 (Legendre symbols and reciprocity), 031250 (local squares), 031750–032000 (local extensions). **Aim:** define the quadratic Hilbert symbol, prove its norm interpretation and bilinearity, and derive the explicit formula at every odd prime.

<!-- BEGIN SPOKEN LECTURE -->

# Norms and Hilbert Symbols at Odd Primes

Consider the equation x squared minus a y squared equals b. Over the rationals we might hunt for rational solutions, use congruences to exclude them, or invoke a theorem about representations by quadratic forms. Over the p-adic numbers something sharper is possible. For any nonzero a and b, we can attach a single sign: plus one if the equation is solvable and minus one if it is not. When p is odd, that sign can be calculated entirely from two valuations and two quadratic-residue tests.

This sign is called the quadratic Hilbert symbol. It is important partly because it turns questions about equations into multiplication of signs. But its definition is more concrete than its name may suggest. We can build it from the local field extensions just studied.

## The symbol and the norm equation

Fix an odd prime p. Let a and b be nonzero elements of Q-p. Say the Hilbert symbol of a and b at p equals plus one if the equation z squared equals a x squared plus b y squared has a solution with x, y, and z not all zero. Otherwise the symbol is minus one.

What does that conic equation have to do with a norm? Suppose a is not a square in Q-p, and form the quadratic field L by adjoining the square root of a. The norm of x plus y times the square root of a is x squared minus a y squared. So the condition that b be a norm is exactly that the equation x squared minus a y squared equals b have a solution.

To pass from the conic to this norm equation, divide by the square of the variable that multiplies b. If that variable were zero, a nonsquare would be a quotient of two squares, which is impossible unless the solution were trivial. Therefore the division is legitimate. Conversely, a norm equation gives the conic with that variable equal to one. If a is already a square, both the Hilbert symbol and the norm test are automatically positive, using the split algebra interpretation.

We have proved the first useful equivalence: the Hilbert symbol of a and b equals plus one exactly when b is a norm from Q-p with the square root of a. The symbol is symmetric, as its conic definition shows by interchanging a with b and x with y.

The set of nonzero norms from a quadratic field is a multiplicative subgroup. Norms multiply, and inverses of norms are norms. But there is an important logical detail: the mere existence of a subgroup does not imply that the sign for membership is multiplicative. We must prove that the norm subgroup has index two. We will do that by describing the norms explicitly in the two possible quadratic extension types. Once the index is two, the sign is the character of the two-element quotient, and it is multiplicative. Symmetry of the conic then gives multiplicativity in the other input. Multiplying either input by a nonzero square does not change the answer.

We could stop at this abstract structure. But for an odd prime we can calculate the sign exactly.

## Units whose residues are nonsquares

First suppose a is a p-adic unit. If its residue is a square modulo p, Hensel's lemma says a is itself a square in Q-p, and the symbol is always plus one.

If the residue is a nonsquare, adjoining the square root of a gives an unramified quadratic extension. We proved that such an extension has residue degree two and ramification index one. The norm of the base uniformizer p, viewed as an element of the quadratic extension, is p squared. Therefore every norm has even p-adic valuation.

Is that the only restriction? Yes. Every p-adic unit is a norm from an unramified quadratic extension. Here is the constructive reason. The norm map between the finite residue fields, from the field with p squared elements to the field with p elements, is onto because both nonzero multiplicative groups are cyclic. Start with an extension unit whose norm has the desired residue.

Now improve the answer one p-adic digit at a time. Suppose our current norm agrees with a target unit through p to the power r. Multiply the chosen extension element by one plus p to the r times t. Its norm changes, modulo the next power of p, by one plus p to the r times the trace of t in the residue field. The residue-field trace is onto, so choose t to repair the next digit. Repeat. The correction factors tend to one, their product converges, and continuity of the norm gives the exact desired unit. This argument uses the same completeness mechanism as Hensel lifting, but applies to a multiplicative equation.

So when a is a unit with nonsquare residue, the Hilbert symbol of a and b is positive exactly when b has even valuation. The square or nonsquare status of the unit part of b is irrelevant. This is our first entry in the local symbol table, and it exhibits a norm subgroup of index two.

## A ramified quadratic extension

Now let a equal p times a unit u. It has odd valuation, so it is not a square. The extension obtained by adjoining its square root is ramified. Its square root is a uniformizer, with norm negative p times u.

Consider the norm of an extension unit. Write it as x plus y times the square root of p u, with x and y p-adic integers and x a unit. Its norm is x squared minus p u y squared. Modulo p this is x squared, so a unit norm has square residue. Conversely, if a p-adic unit has square residue, Hensel tells us it is a square in Q-p and therefore a norm already. Thus the unit norms from this ramified quadratic extension are exactly the units whose residues are squares.

Take an arbitrary b equal to p to the beta times a unit v. The norm of our ramified uniformizer is negative p u. Divide b by the beta-th power of that norm. What remains is a unit. It will be a norm exactly when its residue is a square. This says the sign of the Hilbert symbol is the Legendre symbol of v, multiplied by the beta-th power of the Legendre symbol of negative u.

This is the second entry in the table. Again the allowed norms form exactly half of the square classes: for each valuation parity, one of the two unit-residue classes is allowed. Thus this norm subgroup too has index two, and our sign is multiplicative in its second input. The symmetry of the conic makes it multiplicative in the first input as well. We can now extend the table to every pair a and b. Write a as p to the alpha times a unit u. Because squares do not affect the symbol, only the parity of alpha matters. Separate p from u, and likewise separate p from the unit part of b.

The resulting formula has three factors. First, minus one raised to the product alpha times beta times p minus one over two. Second, the Legendre symbol of u raised to beta. Third, the Legendre symbol of v raised to alpha. All exponents may be reduced modulo two. The formula handles positive and negative valuations; a negative exponent changes nothing beyond its parity, because the signs are their own inverses.

There is no hidden analysis in this final expression. Everything comes from the finite-field residue test, the parity of valuations, norm multiplicativity, and the lifting argument for unramified units.

## Three calculations

Take p equal to three, a equal to three, and b equal to two. The valuation of a is one and the valuation of b is zero. Two is a nonsquare modulo three. Thus the Hilbert symbol is minus one, and the equation x squared minus three y squared equals two has no solution over Q-three. The obstruction is genuinely local: attempting to solve it modulo three already reveals the nonsquare residue.

Next, consider the symbol of three with three at the prime three. Both valuations are one. The first factor is minus one, since three minus one over two is odd. Both unit residues are one, so the other two factors are positive. The answer is minus one. In contrast, at the prime five the symbol of five with five is plus one, because minus one is a square modulo five. The same-looking norm problem can behave differently at different primes.

For a third example, choose two p-adic units at an odd prime. Their Hilbert symbol is always positive, even when both units are nonsquares. This is a striking consequence of the unramified norm theorem. A single nonsquare unit defines the unramified quadratic extension, and all base units are norms from it.

This last statement will fail at the prime two. There, some pairs of odd units give minus one. The prime two deserves its own argument; importing the odd-prime formula and simply replacing a Legendre symbol by a similar-looking function would give false answers.

## Why this is more than a sign convention

A Hilbert symbol is an obstruction to the existence of a point on a conic over a local field. It is also a norm test from a quadratic field extension. The two interpretations agree, and each makes something difficult easy: the conic definition makes symmetry visible, while the norm definition makes multiplication visible.

At odd primes we have now proved the complete explicit formula. For every pair a and b, we can decide local solubility by checking the valuation of each input and two residues in the finite field with p elements. There is no need to search through infinitely many p-adic digits.

This is where quadratic reciprocity begins to take on a different form. Earlier, it related Legendre symbols at two distinct odd primes. The Hilbert symbol keeps track of both Legendre symbols and the missing information at the primes dividing the coefficients. The prime two and the real numbers complete the picture. Once we compute their symbols, quadratic reciprocity will reappear as a product formula over every place of the rational numbers.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(K=\mathbb Q_p\), define
\[
(a,b)_p=\begin{cases}1,&z^2=ax^2+by^2\text{ has a nonzero }K\text{-solution},\\-1,&\text{otherwise}.\end{cases}
\]
If \(a\notin K^{\times2}\), this is +1 iff \(b\in N_{K(\sqrt a)/K}(K(\sqrt a)^\times)\). The norm image is a subgroup. The two explicit norm classifications below show that for every nonsquare a this subgroup has index two; its membership sign is therefore multiplicative in b. Symmetry of the conic gives bilinearity. Square factors do not change the sign.

### Key norm cases for p odd

For \(u\in\mathbb Z_p^\times\) with nonsquare residue, \(K(\sqrt u)/K\) is unramified quadratic. Norms have even valuation, and every unit is a norm. Surjectivity on principal units comes from
\[
N(1+p^rt)\equiv 1+p^r\operatorname{Tr}(\bar t)\pmod{p^{r+1}}, \qquad r\ge 1,
\]
plus trace surjectivity \(\mathbb F_{p^2}\to\mathbb F_p\) and completeness.

For \(a=pu\) with \(u\in\mathbb Z_p^\times\), \(L=K(\sqrt{pu})\) is ramified. Units in \(L\) have norm with square residue; conversely all units with square residue are squares in K and therefore norms. Since \(N(\sqrt{pu})=-pu\),
\[
(pu,p^\beta v)_p=\left(\frac{-u}{p}\right)^\beta\left(\frac{v}{p}\right).
\]

### Explicit formula

Write \(a=p^\alpha u\), \(b=p^\beta v\), \(u,v\in\mathbb Z_p^\times\). For every odd prime p,
\[
\boxed{(a,b)_p=(-1)^{\alpha\beta(p-1)/2}
\left(\frac{u}{p}\right)^\beta
\left(\frac{v}{p}\right)^\alpha.}
\]
All exponents can be interpreted modulo 2, including negative \(\alpha,\beta\). In particular,
\[
(u,v)_p=1,\quad (u,p)_p=(u/p),\quad (p,p)_p=(-1/p).
\]

### Exercises

1. Derive the norm criterion directly from the homogeneous conic, covering the case when a is a square.
2. Show that the finite-field trace from \(\mathbb F_{p^2}\) to \(\mathbb F_p\) is surjective even when p divides the extension degree of a more general unramified extension.
3. Calculate \((3,2)_3,(3,3)_3,(5,5)_5,(5,2)_5,(7,-1)_7\).
4. Explain why odd p-adic unit norms from \(\mathbb Q_p(\sqrt{pu})\) have square residues, but a norm from an unramified quadratic extension can have any nonzero residue.
5. Verify the symmetry of the explicit formula without using the conic definition.

### Reading and source notes

- Ming-Lun Hsieh, National Taiwan University, [Hilbert symbol notes](https://www.math.ntu.edu.tw/~mlhsieh/teaching/L4.pdf), explicit formulas and norm criterion.
- Kiran S. Kedlaya, [Cohomology of local fields: some computations](https://kskedlaya.org/cft/sec_localcomp.html), norm surjectivity on units in unramified extensions.
- Wikipedia: [Hilbert symbol](https://en.wikipedia.org/wiki/Hilbert_symbol), [Norm (field theory)](https://en.wikipedia.org/wiki/Field_norm), [Legendre symbol](https://en.wikipedia.org/wiki/Legendre_symbol).
