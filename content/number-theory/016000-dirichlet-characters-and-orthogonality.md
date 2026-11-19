# 016000 — Dirichlet Characters and Arithmetic Fourier Filters

**Track:** Number Theory from First Principles. **Background:** congruences and unit groups, primitive roots, complex numbers and their elementary roots of unity. **Theme:** construct a finite set of multiplicative filters that can recognize any invertible residue class.

<!-- BEGIN SPOKEN LECTURE -->

# Dirichlet Characters and Arithmetic Fourier Filters

When we counted primes in particular remainder classes, we treated those classes one at a time. We proved that infinitely many primes are three modulo four, then that infinitely many are one modulo four. The arguments were ingenious, but each was tailored to its own remainder. What could handle the problem for every modulus and every remainder relatively prime to it?

We need a mathematical filter. Ideally, it should equal one when an integer n leaves a chosen remainder a modulo q, and zero otherwise. That much is easy to define directly, but a direct yes-or-no condition does not interact particularly well with multiplication and prime factorization. We want to rebuild the filter out of functions whose values multiply when their inputs multiply.

Such functions are called Dirichlet characters. They look like a finite arithmetic Fourier system. We will construct them and prove their two orthogonality laws. The name may sound advanced, but the starting point is the modular arithmetic we already know.

## Start with the units

Fix a positive integer q, usually at least two. A residue class modulo q is a unit when it is relatively prime to q. The units form a finite group under multiplication. Its size is Euler's totient of q, written phi of q. Modulo five, the units are one, two, three and four. Modulo eight, the units are one, three, five and seven. Nonunits are not in that group, which is important in a moment.

A character on the unit group assigns to each unit a complex number of absolute value one. It has two rules. The value at one is one. And the value of a product is the product of the values. If we denote our character by chi, the second rule says, in words, chi of a times b equals chi of a times chi of b.

We allow complex numbers because their roots of unity offer more flexibility than just plus one and minus one. The fourth roots of unity are one, i, negative one, and negative i, where i squared equals negative one. These values form a small multiplicative circle, precisely what we need when a unit group contains an element of order four.

Every unit in a finite group has finite order. If a unit u has order r, then u to the r equals one, and therefore chi of u to the r also equals one. So chi of u must be an rth root of unity. The roots of unity are not a decorative complication; their possible orders are forced by the multiplication law.

To extend chi from units to all integers, set chi of n to zero whenever n is not relatively prime to q, and otherwise let its value depend only on n modulo q. The resulting function is periodic modulo q and completely multiplicative. If either factor is a nonunit, the product is also a nonunit and both sides of the multiplication law vanish. If both factors are units, we are using the group law we started with.

This extension also clarifies a common mistake. The principal character is not the constant function one on all integers. It is one on the integers coprime to q and zero on the others. For modulus six, it is zero on every even integer and every multiple of three.

## A complete example modulo five

The unit group modulo five has a generator: two. Its powers are two, four, three and then one. So it has order four. We can define a character merely by choosing the value of chi at two, provided that value is a fourth root of unity.

There are four choices. Let chi sub zero send two to one; this is the principal character. Let chi sub one send two to i. Let chi sub two send two to negative one. Let chi sub three send two to negative i. The value at every other unit follows by taking powers. For instance, three is the third power of two modulo five, so chi sub one of three is i cubed, which is negative i. And four is the second power of two, so chi sub one of four is negative one.

We have now built four distinct multiplicative functions, one for each of the four units. In a useful sense there are exactly as many characters as units. For any fixed unit u, sum the values chi of u over all four characters. If u is one, every character contributes one and the sum is four. If u is two, three or four, the result is zero: the sum is a geometric progression in a nontrivial fourth root of unity.

Look at u equal to two. The four values are one, i, negative one and negative i. Their sum is zero. We have made the multiplication structure of the residue classes cancel precisely where we wanted it to cancel.

Now suppose we want to recognize integers that are three modulo five. Take each character value at n, multiply it by the complex conjugate of that character's value at three, add over all four characters, and divide by four. If n leaves remainder three, every product is one, so the average is one. If n leaves any other unit remainder, the average is zero by the geometric cancellation we just saw. And if n is divisible by five, every character value at n is zero, so the average is again zero.

A condition about a particular residue has become an average of multiplicative functions. This is the feature that will make Euler products useful.

## First orthogonality: averaging over residues

There is another cancellation law. Take a nonprincipal character, and add its values over a complete set of unit residues modulo q. The sum is zero.

Here is the entire argument. Because the character is not principal, some unit v has a character value different from one. Multiplication by v merely permutes all the units. Thus summing chi of u over all units produces the same answer as summing chi of v times u. But multiplicativity turns the second sum into chi of v times the first. A number equal to itself times a scalar different from one must be zero. That is the first orthogonality relation.

The principal character is the exception: its value is one at each of the phi of q units, so its sum is phi of q. Notice why the proof uses only units. Multiplication by a unit permutes the unit group, giving a clean symmetry that fails if we replace the group by arbitrary integer representatives without the proper zero convention.

This cancellation implies an estimate before any deep analytic work begins. The values of a nonprincipal character repeat every q integers, and the sum over a complete period is zero. A partial sum over any number of consecutive integers therefore consists of complete periods, which cancel, plus at most one incomplete period. Since each character value has absolute value at most one, that partial sum has absolute value at most q. It may oscillate, but it cannot grow indefinitely.

Combining this bound with summation by parts, we learn that the series of chi of n divided by n converges for a nonprincipal character. The corresponding principal series diverges, because on a fixed positive fraction of integers its terms equal one over n. This difference between principal and nonprincipal characters will eventually be the difference between a large main term and bounded corrections.

## Second orthogonality: averaging over characters

For the second law, we keep a unit u fixed and sum chi of u over all characters modulo q. If u is one, every term equals one, and there are phi of q terms. If u is not one, the sum is zero.

The cancellation proof resembles the first, but now we permute the characters. We need one character psi that notices the difference between u and one, meaning psi of u is not one. Multiply every character chi by psi. This produces another character, and multiplication by psi permutes the entire finite character set. If S is the sum of chi of u over all characters, the same sum after permutation equals psi of u times S. Since psi of u differs from one, S must vanish.

Why is there always a character that separates u from one? We can see it concretely from what we know about unit groups. For an odd prime power, the unit group is cyclic, so we can choose a generator and assign it the corresponding root of unity. A nonidentity power is detected by at least one such assignment. For powers of two at least eight, the unit group is generated by minus one and five, with independent orders two and a power of two. We can again assign roots of unity to those two generators. For a general modulus, the Chinese remainder theorem decomposes the unit group into these prime-power pieces. A unit that is not the identity fails to be the identity in at least one piece, where one of our characters detects it.

That construction also shows the number of characters is phi of q: each cyclic factor of order r contributes exactly r choices, and multiplying those numbers gives the size of the whole unit group. No larger abstract theory is needed once the structure of the prime-power unit groups has been established.

Now we can state the filter precisely. For any a relatively prime to q, the average over all characters of chi of n times the complex conjugate of chi of a equals one if n is congruent to a modulo q, and zero otherwise. It works for every integer n, including nonunits. This is character orthogonality in its most practical form.

## Why not just use ordinary trigonometry?

You may have seen another kind of Fourier filter: exponentials involving two pi i times n divided by q. Those exponentials are additive characters. They turn addition in the residue classes into multiplication of complex numbers. They are perfect for studying sums like n plus m or the distribution of residues of sums.

But primes are governed by multiplication. The integer twelve is three times four. In order to convert unique prime factorization into products over primes, we want the coefficient attached to twelve to equal the coefficient attached to three times the coefficient attached to four. Dirichlet characters have exactly that property. Additive exponentials generally do not.

Neither tool is universally better. The group operation dictates which Fourier transform is naturally adapted to a problem. For the primes in arithmetic progressions, multiplicative characters give a bridge between the modular question and the product over all primes.

## A second example: modulus eight

Modulo eight, every unit squares to one. There cannot be an element of order four, so the unit group is not cyclic. This is why our construction must allow more than a single generator.

Every unit can be written uniquely as a product of a power of negative one and a power of five, each exponent either zero or one. We can choose independently whether a character sends negative one to plus or minus one, and whether it sends five to plus or minus one. There are four combinations, hence four characters. Their values are all real. Orthogonality still works, even though the unit group is not cyclic.

This example protects us from a misleading shortcut. Dirichlet characters are not defined by choosing a primitive root modulo every q; such a root often does not exist. The correct starting object is the whole finite abelian unit group, with as many multiplicative characters as its elements.

## The arithmetic job these filters will perform

Take any sum over primes p satisfying p congruent to a modulo q. Replace the indicator of that condition by its character average. The sum becomes an average, across characters, of sums over primes weighted by chi of p. We have reduced one restricted prime sum to several unrestricted weighted prime sums.

The restriction has not vanished by magic: we have moved it into coefficients. But these coefficients are completely multiplicative, and that is exactly what a prime-product identity wants. In the following analytic argument, a principal character produces the main divergence, while nonprincipal characters must be shown not to cancel it.

We have proved the algebraic half of the mechanism: characters exist in the required number, they multiply correctly, their complete-period sums cancel, and their averages isolate any reduced residue class. The analytic half begins with an infinite product. It is the place where unique prime factorization and convergence meet.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Definition and the unit-group construction

For \(q\geq2\), put \(G=(\mathbb Z/q\mathbb Z)^\times\). A character is a homomorphism \(\chi:G\to\mathbb C^\times\), extended by \(\chi(n)=0\) when \(\gcd(n,q)>1\). Since G is finite, each nonzero character value is a root of unity and \(|\chi(n)|=1\) on G. The principal character \(\chi_0\) is the unit indicator.

For \(q=5\), the generator 2 has order 4. With \(\chi_j(2)=i^j\), the table is:

| \(n \bmod 5\) | \(\chi_0\) | \(\chi_1\) | \(\chi_2\) | \(\chi_3\) |
|---|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | \(i\) | −1 | \(-i\) |
| 3 | 1 | \(-i\) | −1 | \(i\) |
| 4 | 1 | −1 | 1 | −1 |
| 0 | 0 | 0 | 0 | 0 |

### Character existence and count for general q

CRT reduces \(G\) to the direct product of its prime-power unit groups. For odd prime powers, the preceding course proved these groups cyclic. For \(2^k\), \(k\geq3\), the units are generated by \(-1\) of order 2 and 5 of order \(2^{k-2}\). One can prove \(v_2(5^{2^j}-1)=j+2\) for \(j\geq0\) by induction: from \(a=5^{2^j}\equiv1\pmod4\), \(a^2-1=(a-1)(a+1)\) and \(v_2(a+1)=1\). The generated subgroup has size \(2^{k-1}\); powers of 5 are 1 modulo 4, while their negatives are 3 modulo 4, so it is the full group. For k=1 and k=2, the groups are trivial and cyclic of order 2, respectively.

For each cyclic component \(C_r=\langle g\rangle\), choose \(\chi(g)=e^{2\pi i j/r}\), with \(0\leq j<r\). Choices multiply across components. Thus \(|\widehat G|=|G|=\varphi(q)\), and distinct elements of G are distinguished by some character.

### Two orthogonality identities

For a character \(\chi\),
\[
\sum_{u\in G}\chi(u)=\begin{cases}|G|&\chi=\chi_0,\\0&\chi\neq\chi_0.\end{cases}
\]
For \(u\in G\),
\[
\sum_{\chi\in\widehat G}\chi(u)=\begin{cases}|G|&u=1,\\0&u\neq1.\end{cases}
\]
Both follow by multiplying and permuting the finite index group; the second uses separation of points by characters. The residue-class indicator, valid for every integer n and any unit a modulo q, is
\[
\mathbf1_{n\equiv a\pmod q}=\frac1{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n).
\]

### Character cancellation and convergence preparation

For any nonprincipal \(\chi\), \(\sum_{r=1}^q\chi(r)=0\). Hence \(A(x)=\sum_{n\leq x}\chi(n)\) has \(|A(x)|\leq q\). The Abel summation formula implies that \(\sum_n\chi(n)/n^s\) converges for every real \(s>0\), and for \(s=1\) its tail after N is \(O(q/N)\). Absolute convergence at s=1 generally fails because \(|\chi(n)|\) is periodic and equals 1 on a positive proportion of integers.

### Exercises and reasoning checks

1. Complete the character table for q=5 and verify the filter for the class 3 on n=3, 7, 10 and 13.
2. List the four characters modulo 8 by assigning signs to −1 and 5. Show directly that no unit has order four.
3. For the nonprincipal character modulo 3, calculate the sum of its values over every complete period and estimate the tail of \(\sum\chi(n)/n\).
4. Explain why \(e^{2\pi i n/q}\) is compatible with addition but not generally with multiplication of integers.
5. Prove that the pointwise product of two characters modulo q is a character, including on nonunits.

### Sources and further reading

- Terence Tao, [Elementary multiplicative number theory](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/), for the use of characters in Dirichlet's theorem.
- NIST Digital Library of Mathematical Functions, [Dirichlet L-functions](https://dlmf.nist.gov/25.15) and [Dirichlet characters](https://dlmf.nist.gov/27.8), for standard notation.
- Wikipedia background: [Dirichlet character](https://en.wikipedia.org/wiki/Dirichlet_character), [Character (mathematics)](https://en.wikipedia.org/wiki/Character_(mathematics)), [Orthogonality relations](https://en.wikipedia.org/wiki/Orthogonality_relations), [Multiplicative group of integers modulo n](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n).
