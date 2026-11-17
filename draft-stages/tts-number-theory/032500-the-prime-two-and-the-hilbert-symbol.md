# 032500 — The Prime Two: Eight Square Classes and the Hilbert Symbol

**Track:** Number Theory from First Principles. **Background:** 031250 (squares in Q_2), 032000 (unramified extensions), 032250 (norm definition of Hilbert symbols). **Aim:** prove the complete explicit formula for the quadratic Hilbert symbol over Q_2, without treating the prime two as an unexplained exception.

<!-- BEGIN SPOKEN LECTURE -->

# The Prime Two: Eight Square Classes and the Hilbert Symbol

At every odd prime, we calculated the Hilbert symbol with a formula involving Legendre symbols. Two units gave a positive symbol, even when both were nonsquares. At the prime two, that assertion is false. The Hilbert symbol of negative one with negative one, for example, is minus one. There is no nontrivial two-adic solution of x squared plus y squared plus z squared equals zero.

Why is two different? At odd primes, a unit is a square precisely when its residue in the finite field is a square. At the prime two, every odd unit has residue one in the field with two elements, so the first residue tells us almost nothing. We must look further down the two-adic expansion, especially modulo eight.

Our earlier classification showed that an odd two-adic unit is a square if and only if it is one modulo eight. Multiplying by squares therefore leaves four types of odd units, represented by one, three, five, and seven modulo eight. We also have to remember whether the valuation is even or odd. There are eight square classes in total, represented by one, negative one, five, negative five, two, negative two, ten, and negative ten.

The Hilbert symbol is multiplicative and depends only on these square classes. So an infinite problem reduces to a finite table. We will calculate that table from norm equations and congruences, then recover the general formula.

## An unramified quadratic field hiding at two

The first surprising ingredient is an unramified quadratic extension of Q-two. It is not obtained by reducing T squared minus a nonsquare unit and looking for an irreducible quadratic over the field with two elements: every nonzero residue is one, and the obvious square-root polynomial has repeated derivative in characteristic two.

Instead take the polynomial T squared minus T minus one. Modulo two it becomes T squared plus T plus one, which is irreducible over the two-element field and has derivative one. Adjoining a root gives an unramified quadratic extension with a residue field of four elements.

If alpha is a root, then two alpha minus one has square five. Thus this field is Q-two with the square root of five. Conversely, an odd unit congruent to five modulo eight is five times a two-adic square, so adjoining its square root gives the same extension. Every odd two-adic unit is a norm from Q-two with the square root of five. The lifting proof is worth checking at two: in the four-element residue field, the trace of alpha is alpha plus alpha squared, which equals one. Thus the residue trace is onto even though tracing the element one would give zero. The digit-by-digit norm correction from our odd-prime argument therefore applies without change and lifts the surjective finite-field norm to an exact norm of two-adic units.

This observation will settle most of the unit-versus-unit cases.

## Pairing two odd units

Take two odd units u and v. If either is one modulo eight, that input is a square and the Hilbert symbol is positive. If either is five modulo eight, it defines the unramified quadratic extension we just constructed, and the other unit is a norm. Once again the symbol is positive.

The only remaining possibility for a negative symbol is that both units are three modulo four: their residues modulo eight are three or seven. This case is genuinely obstructed. Suppose the conic z squared equals u x squared plus v y squared has a nontrivial solution. Scale x, y, and z by a common power of two until all are two-adic integers and at least one is odd.

Reduce the equation modulo four. A square modulo four is zero or one. If exactly one of x and y is odd, the right side is three modulo four and cannot be a square. If both are odd, the right side is two modulo four, also impossible. If both are even, then the right side is zero modulo four, forcing z even; but that contradicts our primitive choice. No case remains.

Therefore the symbol of two odd units is negative exactly when both are three modulo four. This can be written compactly with an exponent. For an odd unit u, take u minus one over two, viewed modulo two. It is odd exactly when u is three modulo four. Multiply that exponent by the corresponding one for v and take minus one to the result. That gives every unit-versus-unit symbol.

As a quick check, negative one is three modulo four. So the symbol of negative one with negative one is negative. The number five is one modulo four. So the symbol of negative one with five is positive. Both conclusions come from congruences and norms, not from a memorized table.

## Pairing two with an odd unit

Now fix the first input to be two and take an odd unit v as the second. We ask whether v is a norm from Q-two with the square root of two. Such a norm has the form x squared minus two y squared.

If the norm is odd, then x must be odd. Modulo eight, its square is one. If y is even, twice y squared is zero modulo eight, and the norm is one modulo eight. If y is odd, twice y squared is two modulo eight, and the norm is seven modulo eight. These are necessary possibilities.

They are sufficient too. If v is one modulo eight, then v itself is a two-adic square: choose y equal to zero. If v is seven modulo eight, then v plus two is one modulo eight, and therefore a square: choose y equal to one. In either case x squared minus two y squared equals v exactly.

Thus the Hilbert symbol of two and v is positive for v congruent to one or seven modulo eight, and negative for v congruent to three or five modulo eight. Notice the contrast with the unit-versus-unit computation. Here the distinction depends on the full residue modulo eight, not just modulo four.

An elegant exponent records the same pattern. For an odd v, the integer v squared minus one over eight is even when v is one or seven modulo eight and odd when v is three or five modulo eight. So the symbol of two and v is minus one to the power of that integer.

Finally the symbol of two with two is positive. This is immediate from the explicit norm of two plus the square root of two: four minus two equals two. So two is itself a norm from the quadratic field obtained by adjoining its square root.

Before multiplying these base cases, we must justify bilinearity at the prime two, rather than borrowing it from the odd-prime calculation. It is enough to show that the norm subgroup of *each* nonsquare quadratic extension has index two. If a is the odd nonsquare unit five, its extension is unramified, so the norms are exactly the elements with even valuation. If a is an odd unit congruent to three modulo four, the unit norms are exactly the units congruent to one modulo four, as our preceding argument showed. The norm of one plus the square root of a is one minus a, which has valuation exactly one. This supplies a norm of odd valuation, so again the norm classes have index two. Finally, if a is two times an odd unit u, the unit norms x squared minus two u y squared have residues one or one minus two u modulo eight. Both possibilities occur, by the square criterion. They are exactly two of the four unit square classes. The norm of the square root of two u is negative two u, of valuation one; multiplying by it determines the norm classes of odd valuation. Again there are four norm square classes out of eight.

That covers every nonsquare a, since its valuation has even or odd parity and its odd unit part has one of the four classes modulo eight. The norm subgroup always has index two. Its membership sign is a multiplicative character, and symmetry supplies bilinearity. We have now earned the right to multiply the base symbols.

## Assemble the formula

Every nonzero two-adic number a can be written as two to an integer power alpha times an odd unit u. Write b similarly, with exponent beta and odd unit v. Since the Hilbert symbol ignores squares, only the parity of alpha and beta matters. By multiplicativity we can decompose the symbol of a and b into four contributions: the symbol of two with two, two with v, u with two, and u with v.

The first contribution is always positive. The unit-pair contribution contributes the product of the two exponents u minus one over two and v minus one over two. The two mixed contributions involve alpha times v squared minus one over eight and beta times u squared minus one over eight.

Add these three integer exponents and raise minus one to the result. That is the complete two-adic Hilbert symbol formula. It is as explicit as the odd-prime formula, but the data are different: instead of Legendre symbols, we use residues modulo four and eight.

Let's test it. The symbol of two with five is negative, since five squared minus one over eight is three, an odd exponent. The symbol of two with seven is positive, since seven squared minus one over eight is six. The symbol of three with three is negative because both odd inputs are three modulo four. The symbol of three with five is positive because five is one modulo four.

None of these answers require approximating an infinite two-adic number. A finite amount of residue information determines the exact answer.

## A pairing with no invisible square classes

There is one more structural fact worth seeing. The symbol defines a symmetric bilinear pairing on the eight square classes, thought of as a three-dimensional vector space over the two-element field. It is nondegenerate: if a class pairs positively with every class, then that class must be a square.

We can check this using only three generators: negative one, five, and two. Negative one pairs negatively with itself but positively with five and two. Five pairs negatively with two. Two pairs negatively with five. So if a product of powers of these generators pairs positively with all three, each exponent must be even. That product is a square.

The eight-class structure is the reason two-adic quadratic arithmetic needs more bookkeeping than the odd-prime case. But it remains a finite calculation, and we have proved the rules. We now possess the Hilbert symbol at every finite prime. We will add the real place, where the criterion is simply whether both inputs are negative, and then investigate how the local signs fit together for rational coefficients.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For an odd \(u\in\mathbb Z_2^\times\), squares are exactly \(u\equiv1\pmod8\), so
\[
\mathbb Q_2^\times/(\mathbb Q_2^\times)^2
=\{1,-1,5,-5,2,-2,10,-10\}.
\]
Use \(\varepsilon(u)=(u-1)/2\pmod2\) and \(\omega(u)=(u^2-1)/8\pmod2\).

### Base cases and proofs

\[
(u,v)_2=(-1)^{\varepsilon(u)\varepsilon(v)},\qquad
(2,u)_2=(-1)^{\omega(u)},\qquad (2,2)_2=1.
\]

- If an odd unit is 1 modulo 8 it is a square. If it is 5 modulo 8 it defines the unramified extension \(\mathbb Q_2(\sqrt5)\) because \(T^2-T-1\) reduces to an irreducible separable quadratic modulo 2. All base units are norms from an unramified extension; the residue trace is onto because a root of \(T^2+T+1\) has trace 1 in \(\mathbb F_4/\mathbb F_2\). This handles every unit pair except when both are 3 modulo 4.
- For \(u\equiv v\equiv3\pmod4\), the congruence \(z^2=ux^2+vy^2\pmod4\) has no primitive solution. This yields the negative case.
- A unit norm \(x^2-2y^2\) forces x odd; modulo 8 it is 1 or 7. Conversely, if u is 1 modulo 8 choose y=0, and if u is 7 modulo 8 choose y=1; the remaining required square lies in \(1+8\mathbb Z_2\).
- \(N_{\mathbb Q_2(\sqrt2)/\mathbb Q_2}(2+\sqrt2)=2\).

### Why bilinearity is justified over Q_2

For each nonsquare square class a, the norm subgroup has index two:

- a represented by 5: the unramified quadratic extension has norms exactly of even valuation.
- a an odd unit congruent to 3 modulo 4: norm units are precisely the units congruent to 1 modulo 4. Because \(v_2(1-a)=1\), the element \(1-a=N(1+\sqrt a)\) also supplies a norm with odd valuation. Thus there are four norm classes among the eight square classes.
- a=2u with u odd: unit norms \(x^2-2uy^2\) have residues \(1\) or \(1-2u\pmod8\); each occurs because a required square can be lifted from a residue 1 modulo 8. Multiplication by \(N(\sqrt{2u})=-2u\) gives the two norm classes of odd valuation. Again there are four norm classes.

In all cases the norm subgroup has index two. Hence its sign is multiplicative in the second input and symmetry makes the pairing bilinear. This is a proof, not an assumption imported from the odd-prime formula.

### Explicit general formula

For \(a=2^\alpha u\) and \(b=2^\beta v\), with odd units u,v and arbitrary integer exponents,
\[
\boxed{(a,b)_2=(-1)^{\varepsilon(u)\varepsilon(v)+\alpha\omega(v)+\beta\omega(u)}.}
\]
On generators \((-1,5,2)\), the exponent matrix over \(\mathbb F_2\) is
\[
\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},
\]
whose determinant is 1; hence the pairing on the three-dimensional square-class space is nondegenerate.

### Exercises

1. Prove that every odd unit square in Q_2 is 1 modulo 8, and recall the converse from 031250.
2. Compute all eight values of \((2,b)_2\) as b runs through the square-class representatives.
3. Explain why \(\mathbb Q_2(\sqrt5)\), unlike \(\mathbb Q_2(\sqrt3)\), is unramified.
4. Verify \((-1,-1)_2=-1\), \((3,3)_2=-1\), \((3,5)_2=1\), and \((2,7)_2=1\) directly from the proven base cases.
5. Show that the exponent matrix is nondegenerate without invoking any classification of general quadratic forms.

### Reading and source notes

- Ming-Lun Hsieh, National Taiwan University, [Hilbert symbol notes](https://www.math.ntu.edu.tw/~mlhsieh/teaching/L4.pdf), sections 1–2, square classes and explicit formulas.
- Wikipedia: [Hilbert symbol](https://en.wikipedia.org/wiki/Hilbert_symbol), [2-adic number](https://en.wikipedia.org/wiki/P-adic_number), [Quadratic residue](https://en.wikipedia.org/wiki/Quadratic_residue).
