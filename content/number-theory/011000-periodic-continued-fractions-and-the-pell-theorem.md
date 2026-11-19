# 011000 — Periodic Continued Fractions and the Complete Pell Theorem

**Track:** Number Theory from First Principles. **Background:** integer arithmetic, the continued-fraction algorithm and convergents (005000), elementary divisibility. **Theme:** why an infinite pattern produces every positive solution of an integer equation.

<!-- BEGIN SPOKEN LECTURE -->

# Periodic Continued Fractions and the Complete Pell Theorem

Consider the equation x squared minus two times y squared equals one. Three squared minus two times two squared is one, so three and two are a solution. But they are not the last solution. Seventeen squared minus two times twelve squared is one. Then there are ninety-nine and seventy. The numbers grow quickly. What connects them, and how can we know that we have not missed any?

The answer involves two different ideas. The square root of two has a continued fraction that repeats. And the expression x plus y times the square root of two can be multiplied, carrying solutions of the equation into new solutions. We have seen examples of both ideas. Now we will prove a general existence theorem and then classify **all** positive solutions, not just produce a few.

Let D be a positive integer that is not a perfect square. The equation under consideration is x squared minus D times y squared equals one, with x and y positive integers. The nonsquare hypothesis matters. If D were a square, the left side would factor into two ordinary integer factors; the infinite family we are seeking would disappear. When D is nonsquare, the square root of D is irrational, and rational fractions can approach it arbitrarily well without ever equaling it.

## An approximation that is secretly an equation

Suppose p over q is close to the square root of D, with q positive. The difference between p over q and that square root can be expressed exactly as the integer p squared minus D q squared divided by q squared times the sum of p over q and the square root of D. This identity follows simply by multiplying a difference of square roots by its conjugate.

So whenever p over q is extremely close to the square root of D, the integer p squared minus D q squared must be small. The numerator is an integer, though, and that is a severe restriction: it cannot drift continuously toward zero unless it eventually becomes zero, which is impossible here. Particularly good rational approximations may therefore solve an equation where the difference of two squares is one, or negative one, or another small integer.

Continued fractions provide precisely such approximations. Their convergents are formed by stopping the continued-fraction expansion after a finite number of entries. Each convergent has a numerator p and denominator q, both integers. The numerator and denominator of neighboring convergents satisfy a determinant identity: multiplying crosswise and subtracting gives positive or negative one. That identity will reappear as the reason a norm can be exactly one.

But why does the continued fraction of a square root repeat? It is not enough to look at the opening digits of square root two or square root three and guess.

## The states of the continued-fraction machine

Let a-zero be the integer part of the square root of D. Remove it, take the reciprocal of the positive fractional remainder, take the next integer part, and repeat. The numbers presented to the algorithm after the first step are called complete quotients.

Here is a remarkable restriction. Every complete quotient after that first step has the form square root of D plus an integer m, divided by a positive integer d. The integer d divides D minus m squared. This is not merely a convenient pattern observed in examples. Rationalizing a denominator proves it at every step, and the usual update rules keep m and d integral.

There is an even stronger restriction. Each such complete quotient is greater than one, while the expression obtained by replacing square root D with negative square root D lies strictly between negative one and zero. We can prove these inequalities at the first step directly. Every later step preserves them: subtract the integer part and take the reciprocal; the corresponding conjugate is again between negative one and zero.

Why do those inequalities matter? Together they force m to lie strictly between negative square root D and positive square root D. They also force the positive integer d to be less than twice square root D. Thus m and d come from finite sets. The algorithm can only enter finitely many different states.

Since the next state is determined by the current one, a state must eventually recur. That proves eventual repetition. There is a small subtlety: an eventually repeating sequence might have a nonrepeating tail. Here we can do better. The conjugate of the next complete quotient tells us the preceding integer part; its fractional remainder then recovers the preceding complete quotient. In other words, within the allowed states the procedure can be reversed uniquely. A finite, reversible process cannot have a tail leading into a cycle. Its very first complete quotient after a-zero is already on the cycle.

We have proved a special case of Lagrange's continued-fraction theorem: **the expansion of the square root of a positive nonsquare integer consists of its initial integer part followed by a purely periodic block**. The general theorem concerns every quadratic irrational, but we do not need that broader statement to solve Pell's equation.

For square root three, the computation begins with one. The first complete quotient is the reciprocal of square root three minus one. Its integer part is one; the next integer part is two; and these two entries repeat. We write the expansion in words as one, followed by the repeating block one, two. For square root two, the repeating block contains just the number two.

## The last entry of the repeating block

There is a reason the last entry of the period for a square root is always twice a-zero. The first complete quotient is the reciprocal of square root D minus a-zero. To find which complete quotient precedes it on the cycle, work backward. The conjugate tells us that the preceding integer part must be twice a-zero. Adding the reciprocal remainder back, we find that the preceding complete quotient is square root D plus a-zero.

This gives a particularly simple state at the end of the period: the integer denominator d is one. It may look like a bookkeeping detail, but it is the key to the equation we want.

Let L be the length of the repeating block. Consider the convergent that ends **just before** the final twice-a-zero entry has been used as the beginning of another period. More precisely, if we number convergents from zero, take the convergent with index L minus one. Let its numerator be P and its denominator Q.

A calculation with the determinant of neighboring convergents shows that P squared minus D Q squared equals negative one raised to the power L. The companion writes out that calculation. Its ingredients are the exact expression for a complete quotient, the continued-fraction identity for a convergent, and the cross-product determinant. The denominator d at the end of the period is one, which is why the result is one or negative one, rather than a different integer.

If the period length is even, we have immediately found a positive solution to the equation with right side one. If the period length is odd, we have found a solution with right side negative one. Multiply P plus Q square root D by itself. The new integer coefficients now have norm positive one, because negative one times negative one is positive one. Either way, **a nontrivial positive solution of Pell's equation exists for every positive nonsquare D**.

Check the two smallest examples. Square root two has period length one, and its first convergent is one over one. One squared minus two times one squared is negative one. Squaring one plus square root two gives three plus two square root two, and three squared minus two times two squared is one. Square root three has period length two; the convergent two over one already gives two squared minus three times one squared equals one.

Notice what we have and have not established. The periodic algorithm constructs a positive solution, so it proves existence. It does not follow just from that construction that we have already listed *every* solution. That requires a separate argument.

## Turn solutions into multiplicative objects

Call x plus y square root D a Pell unit if x and y are integers and x squared minus D y squared equals one. Its conjugate is x minus y square root D. Their product is exactly one, so the conjugate is its multiplicative inverse. The inverse again has integer coefficients. Products of Pell units are therefore Pell units.

For D equal to two, the unit three plus two square root two gives, on squaring, seventeen plus twelve square root two. Squaring again gives five hundred seventy-seven plus four hundred eight square root two. Another multiplication produces ninety-nine plus seventy square root two between those two powers. We are seeing powers of one positive unit, not independent miracles.

A unit bigger than one has a positive coefficient of square root D. To see this, write the unit as u. Its conjugate is one over u, a number between zero and one. The coefficient of square root D is the positive difference u minus one over u, divided by twice square root D. Its integer part x is likewise positive. Conversely every positive solution gives a unit bigger than one.

The set of positive solutions is not empty, by periodicity. Choose the solution giving the smallest unit bigger than one. We can make this choice because the x-coordinates of positive solutions are positive integers, and a larger x means a larger value of x plus y square root D. Call the least unit epsilon. For square root two, epsilon is three plus two square root two.

Now choose any other unit u bigger than one. There is a nonnegative integer k such that epsilon to the power k is at most u, while u is strictly smaller than epsilon to the power k plus one. Divide u by epsilon to the power k. Because the inverse of epsilon has integer coefficients, the quotient is still a Pell unit with integer coefficients. And the inequalities tell us that this quotient lies between one and epsilon, with one included and epsilon excluded.

If the quotient were strictly bigger than one, it would be a positive solution smaller than the smallest positive solution. That is impossible. Therefore the quotient is exactly one, and u equals epsilon to the power k.

This proves the classification: **every positive integer solution of x squared minus D y squared equals one comes from a unique positive power of the least unit epsilon**. Uniqueness follows because epsilon is bigger than one, so its powers are strictly increasing. The trivial solution one and zero corresponds to the zeroth power.

The periodic continued fraction gave existence; the least-unit argument gave completeness. It is worth keeping the two responsibilities distinct.

## The right side negative one behaves differently

For some nonsquare D there are integer solutions to x squared minus D y squared equals negative one; for other D there are none. Square root two provides one and one. Square root three provides none: squares modulo three are zero or one, so x squared minus three y squared cannot be negative one, which is two modulo three.

Our period construction explains both examples. An odd period produces a negative-one solution. Conversely, a negative-one solution forces an odd period; that converse requires an additional result about how exceptionally close rational approximations appear as convergents. The companion records the standard precise theorem and where its extra approximation lemma enters. We need no such converse to prove existence and completeness for the positive-one equation.

There is also a distinction between the ring of expressions x plus y square root D and the full ring of algebraic integers in the field generated by square root D. When D is one modulo four, that larger ring contains elements with half-integer-looking coefficients. We are classifying integer pairs solving the stated Pell equation, so we remain in the former ring. A classification of all algebraic units in the larger ring is a related but different question.

## What the repeated digits really tell us

We began with a short list of large integer pairs. We now have a reason those pairs exist at all, and a precise rule for finding every one of them. An infinite continued fraction may look like an endless approximation process; for a square root, its internal states are forced to recur. A determinant turns that recurrence into norm positive or negative one. Finally, the order of positive units shows that there is a smallest positive generator and no room for other solutions between its powers.

This is an example of a recurring theme in number theory: an apparently infinite search is controlled by finite states, and a classification of solutions emerges from finding the right operation on those solutions.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Continued-fraction recurrence and periodicity

Let \(D\ge2\) be a nonsquare integer, \(a_0=\lfloor\sqrt D\rfloor\). Set \(m_0=0,d_0=1\) and define

\[
 m_{n+1}=d_n a_n-m_n,\qquad d_{n+1}=\frac{D-m_{n+1}^2}{d_n},\qquad
 a_{n+1}=\left\lfloor\frac{a_0+m_{n+1}}{d_{n+1}}\right\rfloor.
\]

The *complete quotient* is \(\alpha_n=(\sqrt D+m_n)/d_n\) (for \(n\ge1\)), with \(\alpha_{n+1}=1/(\alpha_n-a_n)\). The recurrence preserves integrality and the divisibility \(d_n\mid D-m_n^2\). At \(n=1\),
\[
\alpha_1=\frac{1}{\sqrt D-a_0}>1,
\qquad \alpha'_1=-\frac{1}{\sqrt D+a_0}\in(-1,0).
\]

If \(\alpha_n>1\) and \(-1<\alpha'_n<0\), the recurrence gives the same inequalities for \(n+1\). Therefore
\[
-\sqrt D<m_n<\sqrt D,\qquad 0<d_n<\sqrt D+m_n<2\sqrt D.
\]
Only finitely many integral pairs \((m_n,d_n)\) are possible. Reversibility within reduced states follows from
\[
 a_n=\left\lfloor-\frac1{\alpha'_{n+1}}\right\rfloor,
 \qquad \alpha_n=a_n+\frac1{\alpha_{n+1}}.
\]
Thus the states from \(\alpha_1\) are periodic, not merely eventually periodic. If \(L\) is their period length, the predecessor of \(\alpha_1\) has integer part \(2a_0\) and equals \(\sqrt D+a_0\). Consequently \(m_L=a_0,d_L=1,a_L=2a_0\).

### Exact norm identity for convergents

Use \(p_{-2}=0,p_{-1}=1,q_{-2}=1,q_{-1}=0\), and \(p_n=a_np_{n-1}+p_{n-2}\), \(q_n=a_nq_{n-1}+q_{n-2}\). Then
\[
p_kq_{k-1}-p_{k-1}q_k=(-1)^{k-1}.
\]
The complete quotient identity
\[
\sqrt D=\frac{p_{n-1}\alpha_n+p_{n-2}}{q_{n-1}\alpha_n+q_{n-2}}
\]
yields, after multiplying by \(d_n\) and equating rational and irrational parts,
\[
p_{n-1}-m_nq_{n-1}=d_nq_{n-2},\quad
m_np_{n-1}-Dq_{n-1}=-d_np_{n-2}.
\]
Multiply the first by \(p_{n-1}\), the second by \(q_{n-1}\), and add:
\[
 \boxed{p_{n-1}^2-Dq_{n-1}^2=(-1)^n d_n.}
\]
At \(n=L\), \(d_L=1\), hence \(p_{L-1}^2-Dq_{L-1}^2=(-1)^L\). If \(L\) is odd, squaring \(p_{L-1}+q_{L-1}\sqrt D\) produces norm \(+1\).

### Examples and solution classification

| \(D\) | Continued fraction | Period | Constructed norm | Least positive norm-one unit |
|---:|---|---:|---:|---|
| 2 | \([1;\overline2]\) | 1 | \(1^2-2\cdot1^2=-1\) | \(3+2\sqrt2\) |
| 3 | \([1;\overline{1,2}]\) | 2 | \(2^2-3\cdot1^2=1\) | \(2+\sqrt3\) |
| 7 | \([2;\overline{1,1,1,4}]\) | 4 | \(8^2-7\cdot3^2=1\) | \(8+3\sqrt7\) |

Let \(\epsilon=x_1+y_1\sqrt D>1\) be the least norm-one element with integral coefficients. For any norm-one \(u=x+y\sqrt D>1\), choose \(k\ge0\) such that \(\epsilon^k\le u<\epsilon^{k+1}\). Since \(\epsilon^{-1}=x_1-y_1\sqrt D\) has integral coefficients, \(v=u\epsilon^{-k}\) is an integral norm-one unit in \([1,\epsilon)\). Minimality implies \(v=1\), so \(u=\epsilon^k\). **This classifies every positive solution**, independent of whether the period construction initially yields the smallest unit.

The stronger criterion \(x^2-Dy^2=-1\) solvable \(\Longleftrightarrow L\) odd uses the convergent criterion \(|\alpha-p/q|<1/(2q^2)\Rightarrow p/q\) is a convergent, and a further analysis of period positions. It is listed here as further reading, **not proved in this narration**.

### Practice and reasoning checks

1. Compute the complete quotient states for \(D=6\), find the period and exhibit a solution of \(x^2-6y^2=1\).
2. Verify \((3+2\sqrt2)^3=99+70\sqrt2\) and check its norm.
3. Show from the inequalities on \(\alpha_n\) and \(\alpha'_n\) that there are only finitely many possible \((m_n,d_n)\), even if some \(m_n\) are negative.
4. Explain exactly why the existence proof does not require that \(p_{L-1}+q_{L-1}\sqrt D\) be the least positive norm-one unit.
5. For \(D=3\), show without continued fractions why \(x^2-3y^2=-1\) has no integer solutions.

### Sources and further reading

- Stanford's open [Pell equation notes](https://crypto.stanford.edu/pbc/notes/contfrac/pell.html), on periods, convergents and solution classification.
- MIT 18.781 [course materials](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/) and William Stein, [*Elementary Number Theory*](https://www.wstein.org/ent/).
- Wikipedia background: [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation), [Periodic continued fraction](https://en.wikipedia.org/wiki/Periodic_continued_fraction), [Lagrange's theorem (continued fractions)](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(continued_fractions)), [Quadratic irrational](https://en.wikipedia.org/wiki/Quadratic_irrational).
