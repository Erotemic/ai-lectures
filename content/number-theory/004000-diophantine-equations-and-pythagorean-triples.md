# 004000 — Integer Equations, Rational Points, and Pythagorean Triples

**Track:** Number Theory from First Principles. **Background:** GCDs, Bézout's identity, modular arithmetic. **Theme:** how restricting solutions to integers changes an equation.

<!-- BEGIN SPOKEN LECTURE -->

# Integer Equations, Rational Points, and Pythagorean Triples

Consider the equation fifteen times x plus twenty-one times y equals six. If x and y may be any real numbers, the solutions form a straight line. There is no shortage of them. If x and y must be integers, the problem changes. We are no longer looking for any point on a line. We are looking for points where the line meets the integer lattice.

An equation in which we seek integer solutions is called a Diophantine equation. The name comes from the ancient mathematician Diophantus, but we will treat it primarily as a kind of mathematical question rather than as a historical category. The new ingredient is discreteness. Ordinary algebra tells us where real solutions can live; divisibility, congruences, and factorization determine which of those candidates actually have integer coordinates.

We will begin with linear equations, whose integer solutions can be completely classified, and then move to the equation describing right triangles with integer side lengths. That second problem will show how geometry, rational points on a circle, and prime factorization can cooperate.

## Every linear equation has a hidden G C D test

Take an equation a times x plus b times y equals c, with given integers a, b, and c. If the G C D of a and b is d, then d divides a and b. Consequently d divides every integer combination a x plus b y. Therefore d must divide c. This is a necessary condition for integer solutions.

Bézout's identity shows that it is also sufficient, provided a and b are not both zero. We know there are integers s and t with a s plus b t equal to d. If c is a multiple of d, multiply the entire identity by c divided by d. That produces an integer solution to the equation.

So a linear two-variable integer equation has a solution exactly when the G C D of its coefficients divides the right-hand side. Compare this with solving the same equation over the real numbers: unless both coefficients vanish, a real solution always exists. The divisibility condition captures the difference between a continuous line and a lattice.

Our example has coefficients fifteen and twenty-one, whose G C D is three. Three divides six, so integer solutions exist. One solution is x equal to negative one and y equal to one, because negative fifteen plus twenty-one equals six.

Now classify every solution. If x and y are another solution, subtract the known one. Fifteen times the quantity x plus one, together with twenty-one times the quantity y minus one, equals zero. Divide by three: five times the quantity x plus one equals negative seven times the quantity y minus one. Since five and seven are coprime, seven divides x plus one. Hence x equals negative one plus seven times an integer k, and y equals one minus five times the same k.

This is the whole family. Taking k equal to zero gives our original solution. Taking k equal to one gives x equal to six and y equal to negative four. Every other integer solution is obtained by a different integer k.

The general form is just as clean. Once one solution x naught, y naught is known, all solutions are x naught plus b divided by d times k, and y naught minus a divided by d times k. The proof uses exactly the same coprime-divisibility argument.

## Congruences can prove impossibility before we solve anything

Nonlinear equations rarely have such a complete elementary classification. Congruences are often the first test. The square of any integer leaves remainder zero or one modulo four. If the integer is even, its square is divisible by four. If it is odd, write it as two times k plus one; the square is four times k squared plus four times k plus one, leaving remainder one.

This immediately tells us that the equation x squared plus y squared equals three has no integer solutions. The left side, modulo four, could only be zero, one, or two. It cannot be three.

A modular obstruction is decisive: if there is no solution to an equation after reducing modulo some integer, there cannot be a solution among ordinary integers. But the converse is not automatic. A solution modulo every small modulus you happened to test does not prove that a global integer solution exists. Sometimes local congruence information suffices, sometimes it does not, and figuring out the dividing line leads deep into number theory.

This is a particularly useful reasoning pattern. We can disprove integer solvability by finding one obstruction. Proving solvability requires constructing a genuine integer solution, or giving another argument that guarantees one.

## A right triangle as a number-theory question

The Pythagorean equation says a squared plus b squared equals c squared. For real numbers it describes an enormous family of right triangles. For positive integers it asks for Pythagorean triples. Three, four, five is the familiar example. Five, twelve, thirteen is another. There are infinitely many. Can we describe them systematically rather than guess them?

A triple is called primitive when the three side lengths have greatest common divisor one. If a triple is not primitive, divide every side by the common factor and study the primitive core. A primitive triple cannot have both legs odd: then their squares are each one modulo four, so their sum is two modulo four, which cannot be a square. Nor can both legs be even, because the triple would share a factor of two. Thus exactly one leg is even. The hypotenuse is odd.

Call the odd leg a and the even leg b. Rearrange the Pythagorean equation as b squared equals c squared minus a squared, which factors as c minus a times c plus a. Both factors are even, so divide each by two. Let r be half of c plus a, and s be half of c minus a. Then r times s equals the square of b divided by two.

There is an important arithmetic observation: r and s are coprime. Any common divisor divides their sum, which is c, and their difference, which is a. But a and c are coprime in a primitive triple; otherwise a common prime would also divide b, because its square would divide b squared. Thus r and s have no common prime factor.

We have two coprime positive integers whose product is a perfect square. Unique prime factorization forces each one to be a perfect square. If a prime exponent were odd in either factor, it could not be repaired by the other factor, since no prime is shared. So write r as m squared and s as n squared.

Now undo the substitutions. The odd leg a equals m squared minus n squared. The even leg b equals two times m times n. The hypotenuse c equals m squared plus n squared. We have derived the classical parametrization of primitive Pythagorean triples.

Take m equal to two and n equal to one. We get three, four, five. Take m equal to three and n equal to two. We get five, twelve, thirteen. These are not isolated miracles; they come from the same formula.

For a primitive triple, m and n must be coprime and of opposite parity, and m must exceed n. Conversely, any such pair produces a primitive positive triple. If m and n shared a factor, all three sides would share a factor. If both were odd, the even leg and the two odd-square expressions would all be even. Their coprimality and opposite parity rule out those defects.

## Where did the formulas come from geometrically?

There is another way to see the same construction. Divide a Pythagorean equation by c squared. The resulting rational numbers x equal to a divided by c and y equal to b divided by c satisfy x squared plus y squared equals one. Thus integer right triangles correspond, after normalization, to rational points on the unit circle.

Fix the point negative one, zero on the circle. Draw a line through it with rational slope t. The line has equation y equals t times x plus one. Substitute this line into the circle equation. One intersection is the fixed point. The other has coordinates x equal to one minus t squared divided by one plus t squared, and y equal to two t divided by one plus t squared.

Choose t equal to n divided by m. After clearing denominators, we recover the formulas a equals m squared minus n squared, b equals two m n, and c equals m squared plus n squared. So the integer parametrization is also the rational-slope parametrization of a circle.

This idea generalizes. A curve with a known rational point may admit a parametrization by rational lines, turning a geometric problem into rational algebra. Sometimes it works, sometimes the curve has more complicated arithmetic. The right triangle is an ideal first example because the geometry and the integer factorization agree exactly.

## Irrationality and infinite descent

Not every square-root problem has integer or rational answers. Suppose the square root of two were rational. We could write it as a fraction a over b, with positive integers a and b sharing no common factor. Squaring gives a squared equal to two times b squared. Therefore a squared is even, hence a itself is even. Write a as two times k. Substituting gives four times k squared equals two times b squared, so b squared equals two times k squared. Then b is also even. But a and b were supposed to have no common factor, and both are divisible by two. Contradiction.

This is an infinite descent in miniature. A hypothetical fraction in lowest terms would have to contain an even numerator and denominator, which means it was not in lowest terms after all. The argument is not that we failed to find a fraction for the square root of two. It is that any proposed fraction would violate its own reduced form.

A related descent technique can be used to rule out integer solutions to more complicated equations: assume a smallest positive solution exists, then build a strictly smaller one. Since positive integers cannot decrease indefinitely, the assumed solution cannot exist. Such arguments depend crucially on identifying a genuine size measure and proving that it decreases.

## A geometric and arithmetic perspective

We began with lines through the integer lattice and obtained an exact solvability test from the G C D. We then used modular arithmetic to obstruct impossible square equations, and a combination of parity, unique factorization, and rational geometry to classify primitive right triangles.

The common principle is to preserve the integer restriction rather than solve over the reals and hope the answers are whole numbers. A real curve may contain infinitely many points while having no integer points, a handful of them, or infinitely many with a describable structure. Number theory asks which situation actually occurs, and what in the equation makes it so.

These techniques are basic but durable. Divisibility supplies feasibility conditions. Congruences provide fast impossibility tests. Coprime factorization can turn a product equation into separate square equations. Rational parametrization exposes hidden families. Descent can close the door on entire classes of proposed solutions. Each is a way to reason about the arithmetic texture of an equation, not merely its algebraic shape.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Statements and worked formulas

Let \(d=\gcd(a,b)\) with \((a,b)\ne(0,0)\). The equation

\[
ax+by=c,\qquad x,y\in\mathbb Z
\]

is solvable iff \(d\mid c\). Given one solution \((x_0,y_0)\), all solutions are

\[
x=x_0+\frac bd t,\qquad y=y_0-\frac ad t,\qquad t\in\mathbb Z.
\]

Example: \(15x+21y=6\) has \((x,y)=(-1+7t,1-5t)\).

The primitive positive Pythagorean triples, up to swapping legs, have the form

\[
(a,b,c)=(m^2-n^2,2mn,m^2+n^2),\quad m>n>0,\quad\gcd(m,n)=1,
\]

with \(m,n\) of opposite parity. The rational parametrization of the unit circle is

\[
\biggl(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\biggr),\qquad t\in\mathbb Q.
\]

The equation \(x^2+y^2=3\) has no integral solution because each square is \(0\) or \(1\pmod4\).

### Practice and reasoning checks

1. Classify all integer solutions to \(28x+35y=7\). Then explain why the equation \(28x+35y=8\) has none.
2. Derive the triple \((20,21,29)\) by finding suitable \(m,n\), and explain the parity conditions.
3. Explain why a common divisor of the odd leg and hypotenuse of a primitive Pythagorean triple must be one.
4. Is the existence of solutions modulo each of two chosen integers sufficient to infer an integer solution? Give a reasoned answer.
5. Give a proof that \(\sqrt{3}\) is irrational, making explicit which divisibility fact replaces parity.

### Sources and further reading

- MIT OpenCourseWare, *18.781 Theory of Numbers*, lectures 1, 23–26: Diophantine equations, Pythagorean triples, rational conics, descent: https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/
- William Stein, *Elementary Number Theory: Primes, Congruences, and Secrets*, classical arithmetic and Diophantine applications: https://www.wstein.org/ent/
- Wikipedia background: [Diophantine equation](https://en.wikipedia.org/wiki/Diophantine_equation), [Pythagorean triple](https://en.wikipedia.org/wiki/Pythagorean_triple), [Infinite descent](https://en.wikipedia.org/wiki/Proof_by_infinite_descent), [Rational point](https://en.wikipedia.org/wiki/Rational_point).
