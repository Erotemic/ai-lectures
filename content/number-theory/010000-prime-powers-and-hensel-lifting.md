# 010000 — Prime Powers, Simple Roots, and Hensel Lifting

**Track:** Number Theory from First Principles. **Background:** modular arithmetic, polynomial expansion, modular inverses and the Chinese remainder theorem. **Theme:** improving a solution one power of a prime at a time.

<!-- BEGIN SPOKEN LECTURE -->

# Prime Powers, Simple Roots, and Hensel Lifting

Suppose someone has found a solution of an equation modulo seven. For example, three squared is two modulo seven, because nine and two differ by seven. Does that solution tell us anything about the same equation modulo forty-nine, or modulo three hundred forty-three, or modulo ever higher powers of seven?

This is not a routine change of notation. A congruence modulo forty-nine is stricter than one modulo seven. Every solution modulo forty-nine becomes a solution modulo seven when reduced, but a solution modulo seven need not survive unchanged. The question is whether we can adjust the solution without losing what we have already achieved.

For many polynomial equations, we can. The method is called **Hensel lifting**. Its elementary form takes a solution modulo a prime and corrects it, digit by digit, to obtain a compatible solution modulo each higher prime power. The proof is a short and precise calculation. Its conditions are also precise: the relevant root must be simple, meaning that a certain derivative is nonzero modulo the prime.

## What changes when the modulus is a prime power?

Modulo a prime p, every nonzero residue is invertible. This fails modulo p squared. For example, three is nonzero modulo nine, but it has no multiplicative inverse there. Every product of three with another integer is divisible by three, so it cannot be congruent to one modulo nine.

The invertible residues modulo p to the power k are exactly the residue classes not divisible by p. This follows from the same greatest-common-divisor criterion used for arbitrary moduli: a has a modular inverse precisely when a and the modulus are coprime. For a prime power, that simply means p does not divide a.

There are p to the k-th power residues in all. Exactly p to the (k minus one)-th power are divisible by p, since one residue out of every block of p is a multiple of p. So the number of units modulo p to the k-th power is p to the k-th power minus p to the (k minus one)-th power. This is the formula for Euler's totient of a prime power.

That count illustrates a recurring distinction. Working modulo a prime gives a field: nonzero classes can all be divided by. Working modulo a prime power gives a ring with nonzero elements that can multiply to zero. Polynomial equations can therefore have different root counts, and familiar field arguments cannot simply be copied without checking where inverses were used.

## From seven to forty-nine

Let us recover our square-root example. We want an integer x whose square is congruent to two modulo forty-nine. We already have x equal to three modulo seven. Any integer retaining that residue can be written as three plus seven times t, where t is an integer.

Square it. The result is nine plus forty-two t plus forty-nine times t squared. Modulo forty-nine, the final term disappears. To make this square congruent to two, we need seven plus forty-two t to be divisible by forty-nine. Divide by seven. We need one plus six t divisible by seven.

Six has an inverse modulo seven, namely six, because six times six is thirty-six, which leaves remainder one. Solving gives t congruent to one modulo seven. Choose t equal to one. Our corrected root is three plus seven, or ten. And ten squared is one hundred, which differs from two by ninety-eight, exactly twice forty-nine.

Notice the shape of the calculation. We were not searching all forty-nine residue classes. We knew the answer modulo seven and searched among the seven candidates that reduce to that known answer. Moreover, after expanding the square, the correction t appeared **linearly**. That is what makes lifting efficient.

We can repeat the improvement. Starting with ten modulo forty-nine, write the next candidate as ten plus forty-nine t. Its square, modulo three hundred forty-three, equals one hundred plus nine hundred eighty t. Subtract two, divide by forty-nine, and reduce modulo seven. The condition becomes two plus six t congruent to zero modulo seven. Its unique solution is t congruent to two modulo seven. Take t equal to two, obtaining one hundred eight. Indeed, one hundred eight squared differs from two by eleven thousand six hundred sixty-two, which is exactly thirty-four times three hundred forty-three.

So we have compatible solutions: three modulo seven, ten modulo forty-nine, and one hundred eight modulo three hundred forty-three. The consistency is important. Reducing one hundred eight modulo forty-nine gives ten, and reducing ten modulo seven gives three. We are constructing one coherent sequence, not unrelated guesses at each modulus.

## A derivative without limits

To generalize the method, we need a compact way to describe how a polynomial changes under a small correction. Take a polynomial f with integer coefficients. For each power of x, a correction from a to a plus h produces a term proportional to h, plus other terms involving h squared, h cubed, and so on. The coefficient of the first-power term is what we call the **formal derivative** of f at a.

For x squared minus two, the formal derivative is two x. For x cubed plus four x, it is three x squared plus four. This is the familiar polynomial derivative rule, but our argument uses only the binomial theorem; no limits or continuous functions are required.

Suppose a already satisfies f of a congruent to zero modulo p to the power k, where k is at least one. Try to improve it by adding p to the power k times t. Expand f at the new input. The result is f of a, plus p to the power k times t times the formal derivative of f at a, plus terms containing at least the square of p to the power k.

Those higher terms are divisible by p to the power two k. Since k is at least one, two k is at least k plus one. Therefore every higher term vanishes modulo p to the power k plus one.

So one lifting step boils down to a linear equation modulo p. Divide the already-small value f of a by p to the power k, obtaining an integer c. We require c plus t times the formal derivative of f at a to be zero modulo p.

If the derivative is not divisible by p, it has an inverse modulo p. The equation has exactly one solution for t modulo p. We get a unique correction in the chosen residue class. If the derivative is divisible by p, this argument cannot divide by it. The correction equation may have many solutions or no solutions, and the outcome needs separate analysis.

That is the heart of the simple-root form of Hensel's lemma.

## The theorem and why the construction continues

Here is the precise statement. Let p be prime and f a polynomial with integer coefficients. Suppose a is a root modulo p: f of a is divisible by p. Also suppose its formal derivative at a is **not** divisible by p. Then for every positive integer k there is exactly one solution modulo p to the power k that reduces to a modulo p. The solutions can be chosen compatibly, so that each reduces to the preceding one.

We already proved the extension step. The starting solution works modulo p. Assume a representative a sub k works modulo p to the power k. Solve the linear correction equation for t modulo p, and define a sub k plus one by adding p to the power k times that correction. The derivative modulo p does not change, because our successive corrections are themselves divisible by p. So its invertibility persists at every stage. Induction gives a unique compatible lift at all levels.

The word unique requires care. A polynomial may have several roots modulo p. Each simple root gives its own unique branch of lifts. The theorem does not say the polynomial has only one root in total. In our square-root example modulo seven, three and negative three are distinct simple roots. Both lift. Modulo forty-nine, the two roots of two are ten and thirty-nine, which are negatives of each other.

The theorem also does not say that one fixed ordinary integer solves the equation exactly. The representatives can grow as the modulus grows. Our sequence three, ten, one hundred eight does not become an ordinary integer whose square is two. Rather, the sequence describes an element of the seven-adic integers, a number system designed so that consistency modulo every power of seven is the meaningful notion of approximation. We need not construct that number system here to understand the finite theorem.

## A complete square-root classification for units at odd primes

We can combine Hensel lifting with the theory of quadratic residues. Let p be an odd prime, and let b be an integer not divisible by p. Ask whether x squared is congruent to b modulo p to the power k.

First reduce modulo p. If b is a nonsquare modulo p, there cannot be a root modulo any higher power, because reduction would produce an impossible root modulo p. If b is a square modulo p, there are exactly two distinct roots modulo p: a and negative a. Why exactly two? The difference of two squares factors, and in a field a nonzero quadratic polynomial has at most two roots. Since b is nonzero modulo p, the two roots cannot coincide.

At either root, the derivative of x squared minus b is two x. Because p is odd, two is invertible modulo p, and because b is nonzero, a is nonzero. Thus the derivative does not vanish modulo p. Both roots are simple, and each has exactly one lift to every higher prime power.

We have proved a complete statement: **for an odd prime p and b coprime to p, there are exactly two roots modulo p to the power k if b is a quadratic residue modulo p, and none if it is a nonresidue**. Here quadratic residue means a nonzero square class, as in our earlier lectures. The classification uses both the root count in a field and the uniqueness of lifts, not either ingredient alone.

For a modulus containing several different prime powers, the Chinese remainder theorem reconstructs solutions from the separate prime-power solutions. For example, solving a polynomial congruence modulo a product of coprime prime powers amounts to selecting a root in each factor and combining the congruences. This is a mathematical reduction; if the modulus has not been factored, the required factorization may itself be difficult to compute.

## Where the simple-root condition fails

The hypothesis about the derivative is substantial. Consider the equation x squared congruent to zero modulo twenty-five. Modulo five, the only root is zero, but the derivative two x is zero at that root modulo five. The simple-root theorem says nothing.

Direct examination gives five roots modulo twenty-five: zero, five, ten, fifteen and twenty. Every multiple of five has square divisible by twenty-five. Conversely, if the square is divisible by twenty-five, the number must be divisible by five. So a singular root modulo five has produced **more than one** lift.

Now change the target to five instead of zero. The equation x squared congruent to five modulo twenty-five has **no** solution. If x is divisible by five, its square is zero modulo twenty-five; if it is not divisible by five, its square is nonzero modulo five. Neither possibility gives five modulo twenty-five. So a derivative that vanishes does not always mean many lifts; it can also mean none.

The prime two demands care as well. For the polynomial x squared minus an odd b, the derivative two x is always divisible by two. Our simple-root theorem gives no information. Indeed, every odd square is congruent to one modulo eight, imposing a stronger condition than being a square modulo two. The classification of square roots modulo powers of two requires separate arguments, not wishful reuse of the odd-prime proof.

## What we have gained

This method shows how a local solution can be refined in a controlled way. We begin with one finite clock, add one new digit of prime-power precision, and solve a **linear** correction equation. A nonzero derivative guarantees that the correction is possible and unique. When that hypothesis fails, root behavior can branch or disappear.

Hensel lifting is a bridge between elementary modular arithmetic and p-adic analysis. It also supports practical algorithms for solving congruences modulo prime powers. But it does not replace finding a root modulo the original prime, and it does not magically solve singular cases. Its value lies in a sharp statement: if the initial root is simple, all higher levels are governed by a repeatable, provably correct correction rule.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Unit count modulo a prime power

For prime p and integer \(k\ge1\),

\[
(\mathbb Z/p^k\mathbb Z)^\times
=\{\bar a:p\nmid a\},
\qquad
\varphi(p^k)=p^k-p^{k-1}.
\]

The hypothesis \(p\nmid a\) is equivalent to \(\gcd(a,p^k)=1\).

### Elementary Hensel lemma: proof by one-digit correction

Let \(f\in\mathbb Z[x]\), let p be prime, and suppose \(f(a_1)\equiv0\pmod p\) and \(f'(a_1)\not\equiv0\pmod p\). Given \(a_k\) with \(f(a_k)\equiv0\pmod{p^k}\), write \(f(a_k)=p^k c_k\). Every lift of the residue class \(a_k\pmod{p^k}\) modulo \(p^{k+1}\) has form

\[
a_{k+1}=a_k+t p^k, \qquad t\in\{0,\ldots,p-1\}.
\]

By the binomial theorem, for \(k\ge1\),

\[
f(a_k+t p^k)\equiv f(a_k)+t p^k f'(a_k)
\pmod{p^{k+1}},
\]

because the omitted terms contain \(p^{2k}\) and \(2k\ge k+1\). Thus the required correction is the **unique** solution modulo p of

\[
\boxed{t\equiv-c_k(f'(a_k))^{-1}\pmod p.}
\]

The derivative remains nonzero modulo p because \(a_k\equiv a_1\pmod p\). Consequently the process continues indefinitely and yields exactly one compatible branch above each simple root modulo p.

### Worked example: \(x^2\equiv2\) modulo powers of seven

With \(f(x)=x^2-2\), \(p=7\):

| Precision | Root | Error divisible by modulus | Correction calculation |
|---|---:|---:|---|
| \(7\) | \(a_1=3\) | \(3^2-2=7\) | \(f'(3)=6\not\equiv0\pmod7\) |
| \(49\) | \(a_2=10\) | \(10^2-2=98=2\cdot49\) | \(1+6t\equiv0\pmod7\Rightarrow t=1\) |
| \(343\) | \(a_3=108\) | \(108^2-2=11662=34\cdot343\) | \(2+6t\equiv0\pmod7\Rightarrow t=2\) |

The second branch is \(-a_k\) modulo \(7^k\): roots modulo 49 are 10 and 39; roots modulo 343 are 108 and 235.

### Exact classification for unit square roots at odd primes

Let p be odd, \(p\nmid b\), and \(k\ge1\). Then the congruence \(x^2\equiv b\pmod{p^k}\) has zero roots if \(b\) is a nonresidue modulo p, and exactly two roots if \(b\) is a residue modulo p. The latter roots are lifts of the two roots \(a, -a\pmod p\), with \(2a\not\equiv0\pmod p\).

**Important exclusions:** This classification does not apply to \(p\mid b\) or to \(p=2\). For example, \(x^2\equiv0\pmod{25}\) has five residue-class solutions, whereas \(x^2\equiv5\pmod{25}\) has none. Every odd x satisfies \(x^2\equiv1\pmod8\).

### Practice and reasoning checks

1. Starting from \(x\equiv2\pmod5\), lift a root of \(x^2\equiv-1\pmod5\) to a root modulo \(25\) and then modulo \(125\).
2. Prove the binomial remainder formula for \(f(x)=x^3+2x+1\), then state the corresponding general polynomial argument.
3. For \(p=13\), decide whether \(x^2\equiv3\pmod{13^k}\) has roots for every \(k\ge1\). If it does, explain how many, without enumerating all roots.
4. Find all roots of \(x^2\equiv0\pmod{49}\) and compare with the simple-root theorem's hypotheses.
5. Explain the difference between a compatible root modulo every \(p^k\) and a single ordinary integer satisfying \(f(x)=0\) exactly.

### Sources and further reading

- MIT OpenCourseWare, [*18.781 Theory of Numbers*, lecture on primality, factoring, RSA and Hensel's lemma](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/).
- MIT, [*18.782 Introduction to Arithmetic Geometry*, Lecture Notes 8](https://math.mit.edu/classes/18.782/2013fa/LectureNotes8.pdf), section 8.3, the p-adic form of Hensel's lemma.
- William Stein, [*Elementary Number Theory*](https://www.wstein.org/ent/).
- Wikipedia orientation: [Hensel's lemma](https://en.wikipedia.org/wiki/Hensel%27s_lemma), [Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic), [P-adic number](https://en.wikipedia.org/wiki/P-adic_number), [Quadratic residue](https://en.wikipedia.org/wiki/Quadratic_residue).
