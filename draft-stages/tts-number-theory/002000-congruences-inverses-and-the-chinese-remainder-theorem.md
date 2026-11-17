# 002000 — Congruences, Inverses, and the Chinese Remainder Theorem

**Track:** Number Theory from First Principles. **Background:** divisibility and the greatest common divisor. **Theme:** doing arithmetic with remainders without losing logical precision.

<!-- BEGIN SPOKEN LECTURE -->

# Congruences, Inverses, and the Chinese Remainder Theorem

Imagine two clocks. One has a twelve-hour dial, the other a seven-hour dial. Suppose the first reads five and the second reads three. What time, counted in whole hours from a shared starting point, could explain both readings? There is a systematic way to solve this problem. But before we find the time, we need to understand what it means to work with numbers that are allowed to differ by a complete cycle.

An integer leaves a remainder when divided by a positive number n. All integers with the same remainder belong to the same residue class modulo n. For example, fourteen and two belong to the same class modulo twelve, because their difference is twelve. So do negative ten and two. We write that fourteen is congruent to two modulo twelve; the statement means exactly that twelve divides fourteen minus two.

Congruence is an equivalence relation. Every integer is congruent to itself, the relationship is symmetric, and congruences can be chained. More importantly, congruence respects addition and multiplication. If two numbers differ by a multiple of n, replacing one by the other in any sum or product changes the result by another multiple of n. This is why a clock calculation can be performed on the dial, without tracking every full turn of the hour hand.

## A small arithmetic universe

Consider arithmetic modulo five. There are exactly five possible classes, represented by zero, one, two, three, and four. Six acts like one; seven acts like two. Three plus four acts like two because seven leaves remainder two. Three times four also acts like two because twelve leaves remainder two.

It is tempting to regard these classes as ordinary numbers with an odd rule for wrapping around. A more useful view is that each class stands for infinitely many integers. When we add classes, we can choose any representatives, add them, and take the resulting class. The answer does not depend on our representatives. That independence is what makes modular addition and multiplication well defined.

The modulus matters. Modulo five, multiplying by three can be undone, because three times two is congruent to one. Modulo six, multiplying by three cannot be undone: every multiple of three is congruent to zero or three, never one. Thus modular arithmetic resembles ordinary arithmetic in some settings and differs radically in others.

A residue class a has a multiplicative inverse modulo n precisely when a and n are coprime. For one direction, if a times x is congruent to one, then a times x minus one is a multiple of n. Rearranging gives an integer combination of a and n equal to one, so their greatest common divisor is one. For the other direction, if their G C D is one, Bézout's identity produces integers x and y such that a times x plus n times y equals one. Reducing that identity modulo n shows that x is an inverse of a.

This is where a proof about integer combinations becomes an algorithm about modular arithmetic. The extended Euclidean algorithm finds the inverse if one exists. You do not need to guess it by trial and error.

## Why cancellation sometimes lies

In ordinary integer arithmetic, if three times x equals three times y, we cancel three to get x equals y. In modular arithmetic, that move may be invalid. Modulo six, three times one and three times three are both congruent to three, yet one and three are not congruent modulo six.

The safe rule is: multiplication by a is cancellable modulo n exactly when a and n are coprime. Then a has an inverse, and multiplying both sides by that inverse justifies the cancellation. If they are not coprime, we may recover only a weaker congruence with a smaller modulus.

Consider the equation three times x congruent to six modulo nine. The G C D of three and nine is three, and three divides six, so solutions exist. Divide the entire integer divisibility condition by three: we get x congruent to two modulo three. That means the distinct solutions modulo nine are two, five, and eight. We have three solutions, not one. If the original right-hand side had been seven, no solution would exist because three does not divide seven.

In general, the linear congruence a times x congruent to b modulo n is solvable exactly when the G C D of a and n divides b. If that common divisor is d, there are exactly d incongruent solutions modulo n. Divide a, b, and n by d to obtain a congruence with an invertible coefficient, solve it modulo n divided by d, then lift the answer back to the original modulus.

This theorem clarifies a recurring theme: equations can be solved only when their divisibility constraints fit together. Even a one-line congruence may secretly have several answers or none.

## Two clocks and a simultaneous answer

Now return to our clocks. Suppose an unknown integer t leaves remainder five upon division by twelve and remainder three upon division by seven. Write t as five plus twelve times k. The second clock demands that five plus twelve times k be congruent to three modulo seven. Since twelve behaves like five modulo seven, we need five times k congruent to five. Five has inverse three modulo seven, so k is congruent to one modulo seven. Hence t is seventeen plus eighty-four times any integer.

Seventeen is the smallest nonnegative solution. It reads five modulo twelve and three modulo seven. After eighty-four hours both dials return to their joint original readings. We have solved the two-clock problem, and we know every solution.

Why did the method work so cleanly? Twelve and seven are coprime. When moduli have no shared prime factor, their remainder constraints can be imposed independently. The Chinese remainder theorem formalizes this observation.

For pairwise coprime positive moduli, any selected remainders occur together in exactly one residue class modulo the product of the moduli. Two parts need proof: a common solution exists, and any two common solutions differ by a multiple of the product.

Uniqueness is easier. If x and y satisfy the same remainder constraints, each modulus divides x minus y. Since the moduli are pairwise coprime, their product divides the difference. Hence the two solutions are congruent modulo that product.

For existence, focus first on two coprime moduli m and n. Bézout gives integers u and v with u times m plus v times n equal to one. Multiply that identity by carefully chosen remainders, and you can construct a number that has remainder a modulo m and remainder b modulo n. One convenient choice is a times v times n plus b times u times m. Modulo m, the first coefficient v times n behaves like one and the other term vanishes. Modulo n, the roles reverse. For more moduli, repeat the two-modulus construction inductively.

## A three-clock example

Find a number that leaves remainder two modulo three, remainder three modulo five, and remainder two modulo seven. We can combine the first two conditions by inspection: eight works modulo three and five. Every common solution is eight plus fifteen times k. We now require eight plus fifteen k to be congruent to two modulo seven. Since eight is one modulo seven and fifteen is also one modulo seven, k must be one modulo seven. This gives twenty-three, plus multiples of one hundred five.

Check it directly. Twenty-three leaves two after division by three, three after division by five, and two after division by seven. Any other simultaneous solution differs by a multiple of three, five, and seven; because they are pairwise coprime, that difference is a multiple of one hundred five.

This result has a striking computational interpretation. Knowing a large integer modulo one hundred five is equivalent to knowing three smaller remainders, modulo three, five, and seven. Addition and multiplication in the large system can be performed independently in the small systems, then recombined. This is not merely an analogy. The correspondence preserves both operations, making it a concrete instance of a ring isomorphism.

## What changes when moduli share factors?

The pairwise-coprime condition cannot be discarded without replacement. Suppose we ask for a number congruent to one modulo four and two modulo six. Numbers in the first class are odd. Numbers in the second class are even. No integer can satisfy both.

The exact compatibility condition for two arbitrary moduli m and n is that the requested remainders differ by a multiple of their G C D. Why? Any common solution x would make x minus a a multiple of m and x minus b a multiple of n. Subtract these relationships and we find that a minus b must be divisible by every common divisor, including the G C D. Conversely, if that divisibility condition holds, write x as a plus m times k. The second requirement becomes a linear congruence in k, solvable by the criterion we have just proved.

If the conditions are compatible, their combined solutions form one residue class modulo the least common multiple, not necessarily modulo the product. For example, a number congruent to one modulo four and three modulo six can be nine; the complete answer is nine plus a multiple of twelve. The common divisor of four and six is two, and the requested remainders differ by two, so compatibility holds.

This is why the Chinese remainder theorem is better understood as a theorem about combining partial information than as a memorized formula. We can reconstruct a number from remainders when the pieces of information do not contradict each other. Coprimality guarantees compatibility for every possible combination. Without coprimality we have to check.

## The deeper lesson of modular arithmetic

Working modulo n means deliberately forgetting how many complete cycles occurred. The surprising fact is that we can forget this information consistently: sums and products still make sense. But division becomes conditional, and simultaneous constraints demand compatibility.

These ideas appear far beyond clock puzzles. Computers use remainders for efficient integer computation. Algebra studies quotient structures whose operations are well defined for exactly the same reason. Number theorists use local congruence restrictions to rule out impossible integer equations before attempting harder arguments. The Chinese remainder theorem lets us decompose arithmetic modulo a product into smaller independent pieces.

We have learned not only how to calculate a residue, but what authorizes each move: a divisibility definition for congruence, a Bézout witness for inverses, a G C D test for linear equations, and a construction and uniqueness proof for simultaneous congruences. That is the algebra hiding inside a clock face.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Precise definitions and proofs

Fix \(n\ge2\). Write \(a\equiv b\pmod n\) iff \(n\mid(a-b)\). The classes \(\mathbb Z/n\mathbb Z\) carry well-defined addition and multiplication. A class \([a]\) is invertible iff \(\gcd(a,n)=1\).

The linear congruence \(ax\equiv b\pmod n\) is solvable iff \(d=\gcd(a,n)\mid b\); in that case it has \(d\) classes of solutions modulo \(n\). Example: \(3x\equiv 6\pmod9\) has \(x\equiv2,5,8\pmod9\).

If \(\gcd(m,n)=1\) and \(um+vn=1\), then

\[
 x=avn+bum \quad\text{satisfies}\quad x\equiv a\pmod m,\quad x\equiv b\pmod n.
\]

For pairwise coprime \(n_i\), reduction induces

\[
\mathbb Z/(n_1\cdots n_k)\mathbb Z\ \cong\ \prod_{i=1}^k\mathbb Z/n_i\mathbb Z.
\]

For two possibly noncoprime moduli, a common solution to \(x\equiv a\pmod m\), \(x\equiv b\pmod n\) exists iff \(\gcd(m,n)\mid(a-b)\); when it exists it is unique modulo \(\operatorname{lcm}(m,n)\).

### Practice and reasoning checks

1. Find all solutions to \(14x\equiv 21\pmod{35}\); explain why there are exactly seven classes or why there are none. *Hint:* compute \(\gcd(14,35)=7\).
2. Solve \(x\equiv3\pmod8\), \(x\equiv4\pmod5\), and check your answer.
3. Show exactly where cancelling a factor of two fails modulo eight.
4. Give one compatible and one incompatible pair of congruences with moduli six and ten.
5. Explain why the Chinese remainder theorem is a statement about arithmetic operations, not only a way to solve puzzles.

### Sources and further reading

- MIT OpenCourseWare, *18.781 Theory of Numbers*, lectures 3–5: congruences, inverse arithmetic, linear congruences, Chinese remainder theorem: https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/
- William Stein, *Elementary Number Theory: Primes, Congruences, and Secrets*, modular arithmetic: https://www.wstein.org/ent/
- Wikipedia background: [Modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic), [Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem), [Linear congruence theorem](https://en.wikipedia.org/wiki/Linear_congruence_theorem).
