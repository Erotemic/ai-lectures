# 005000 — Continued Fractions, Rational Approximation, and Pell Equations

**Track:** Number Theory from First Principles. **Background:** Euclidean division, fractions, irrationality, and basic algebra. **Theme:** the Euclidean algorithm as a theory of approximation.

<!-- BEGIN SPOKEN LECTURE -->

# Continued Fractions, Rational Approximation, and Pell Equations

A rational number is a fraction of integers, so fractions can approximate real numbers. But not all denominators are equally useful. If you need to approximate the square root of two using a fraction whose denominator is modest, how should you choose it? Three halves is close. Seven fifths is closer. Seventeen twelfths is closer still. These fractions are not random guesses. They arise from the same division algorithm that computes greatest common divisors.

Continued fractions turn repeated division into a representation of a number. They reveal why certain fractions are exceptionally accurate, and they produce integer solutions to equations that initially look difficult to approach. Our main example will be the equation x squared minus twice y squared equals one, a special case of Pell's equation.

## Seeing division inside a fraction

Take the rational number four hundred fifteen divided by ninety-three. Divide four hundred fifteen by ninety-three. The quotient is four and the remainder is forty-three. So the fraction is four plus forty-three divided by ninety-three, or four plus one divided by ninety-three over forty-three.

Now divide ninety-three by forty-three. The quotient is two and the remainder is seven. Continue: forty-three divided by seven gives quotient six and remainder one, and seven divided by one gives quotient seven and remainder zero.

We have expressed the original fraction using a sequence of integer quotients: four, two, six, seven. It can be read as four plus the reciprocal of two plus the reciprocal of six plus the reciprocal of seven. The nested structure matters. We call this a finite continued fraction.

The Euclidean algorithm has reappeared almost unchanged. At each step we peel off an integer part and invert the fractional remainder. When the original number is rational, the remainders eventually terminate, just as in G C D computation. For an irrational number, the process does not terminate: if it did, reversing a finite chain of integer arithmetic would express that number as a rational fraction.

The first few partial versions of a continued fraction are called convergents. For our example, the first is four. The second is four plus one-half, or nine halves. The third is fifty-eight thirteenths. The fourth recovers four hundred fifteen ninety-thirds exactly.

Notice how small the denominators stay while the approximations improve. The continued fraction does not enumerate every possible fraction. It follows a deterministic path from integer division to especially efficient rational approximations.

## The recurrence hiding in the nesting

Nested fractions are difficult to read aloud and awkward to calculate directly. There is a convenient recurrence. Denote a convergent by p over q. Start with the first integer quotient. Each time another quotient a enters the continued fraction, the new numerator is a times the preceding numerator plus the numerator before that. The denominator obeys the same rule.

For our example, the integer quotients are four, two, six, seven. The convergents go four over one, nine over two, fifty-eight over thirteen, then four hundred fifteen over ninety-three. Check the third: six times nine plus four is fifty-eight, and six times two plus one is thirteen. Check the fourth: seven times fifty-eight plus nine is four hundred fifteen; seven times thirteen plus two is ninety-three.

There is a crucial invariant. Consecutive convergents have cross-products differing by exactly one. In the last pair, four hundred fifteen times thirteen minus fifty-eight times ninety-three is one. This implies the numerator and denominator of every convergent are coprime. It also says consecutive convergents are extremely close: their difference is exactly one divided by the product of their denominators.

For a real irrational number, convergents alternate around the target and satisfy a useful error bound: the absolute error is strictly less than one divided by the denominator squared. A general proof uses the recurrence and the fact that the unexplored tail of a continued fraction is positive. The bound explains why large denominators arrive with unusually strong precision.

The word unusually requires a qualification. A convergent is particularly good relative to other fractions of comparable denominator, but not every possible statement about best approximation is true with the same comparison range or strictness. When a proof depends on the exact extremal property, specify which denominators are allowed and whether the comparison is absolute error or error after multiplying by the denominator. For now, the explicit bound and neighboring-determinant identity give us reliable information without overselling the slogan.

## The continued fraction of the square root of two

The square root of two lies between one and two. Remove its integer part, one. The remaining positive fraction is the square root of two minus one. Invert it. Multiplying numerator and denominator by the square root of two plus one shows that its reciprocal is the square root of two plus one, which is between two and three. Remove the integer part two, and the new fractional remainder is again the square root of two minus one.

The pattern repeats forever. The continued fraction for the square root of two starts with one, followed by an endless sequence of twos. Its convergents begin one, three halves, seven fifths, seventeen twelfths, and forty-one twenty-ninths.

Square some of these approximations and compare the numerator squared with twice the denominator squared. For three halves, nine minus eight is one. For seven fifths, forty-nine minus fifty is negative one. For seventeen twelfths, two hundred eighty-nine minus two hundred eighty-eight is one. The difference is tiny, even as the numerator and denominator grow.

This is not a numerical coincidence. The approximation error for p over q is related to the integer p squared minus twice q squared. Factor the difference of squares: p squared minus two q squared equals p minus q times the square root of two, multiplied by p plus q times the square root of two. If p over q is close to the square root of two, the first factor is small. The second is large, but the continued-fraction approximation is accurate enough to keep their product small.

The target quantity is always an integer. An estimate that traps an integer very near zero, one, or negative one can force an exact Diophantine conclusion. This is a recurring number-theoretic method: use continuous approximation to discover an exact discrete identity.

## Pell's equation and an infinite family

Now consider x squared minus twice y squared equals one, with positive integers x and y. The pair three and two works, because nine minus eight equals one. The pair seventeen and twelve works, because two hundred eighty-nine minus two hundred eighty-eight equals one. We would like a mechanism that generates more solutions without checking integers one by one.

Introduce the expression x plus y times the square root of two. Pair it with x minus y times the square root of two. Their product is x squared minus twice y squared. Therefore Pell's equation says that this product equals one.

Multiply two expressions of the form x plus y root two. The product has the same form, because root two squared is two. And the corresponding products with their conjugates multiply as ordinary numbers do. So if two expressions each have product one with their conjugate, their product also has product one with its conjugate.

The particular number three plus two root two has conjugate three minus two root two, and their product is one. Raise three plus two root two to successive positive integer powers. Each result has integer coefficients x and y, and each solves x squared minus twice y squared equals one.

The first power gives three and two. The square gives seventeen and twelve. The cube gives ninety-nine and seventy. We have constructed infinitely many solutions, and the coefficients grow each time because multiplying a positive expression greater than one by three plus two root two increases its size.

There is even a simple recurrence. If x and y solve our equation, multiply x plus y root two by three plus two root two. The new x is three x plus four y. The new y is two x plus three y. Starting with x equal to one and y equal to zero, one application gives three and two; the next gives seventeen and twelve; the next ninety-nine and seventy.

The square-root expression is not a decorative trick. It packages a nonlinear two-variable equation into multiplication in a larger number system. Later algebra will call this a norm: the product of an expression and its conjugate. Norms convert a hard additive-looking relation into a multiplicative invariant.

## Why this is more than a method for one square root

For any positive nonsquare integer D, Pell's equation asks for integer solutions to x squared minus D times y squared equals one. A classical theorem says there are nontrivial positive integer solutions, and the continued fraction of the square root of D provides a systematic route to them. Proving the full theorem—including the periodicity of continued fractions for quadratic irrationals—takes more work than the example we have developed. Our example establishes the mechanism in a case where every step is visible.

The distinction between this example and the general theorem matters. We have proved an infinite sequence of solutions for D equal to two, using a concrete multiplicative generator. We have not yet proved that this construction produces every positive solution, nor that a similar generator can always be found for every nonsquare D. Those questions belong to the broader theory, and continued fractions supply the tools to answer them.

Continued fractions also connect to dynamical systems, lattice geometry, approximating frequencies in oscillatory motion, and exact rational reconstruction. If an approximate floating-point number is suspected to come from a fraction with a small denominator, continued fractions are a disciplined way to search for it. But a finite floating-point sample alone never proves that the hidden exact number is rational, let alone identifies it uniquely, unless an independent error bound and denominator constraint are available.

## The bridge between discrete and continuous mathematics

Number theory is often described as purely discrete, concerned only with integers. Continued fractions show that this description misses an important connection. An irrational number, a continuous quantity, is analyzed by integer division. Its best rational approximations satisfy exact recurrence identities. And those approximations can reveal genuine integer solutions to nonlinear equations.

The Euclidean algorithm started as a way to find common divisors. In continued fractions it becomes a way to extract information from a real number. In Pell equations it becomes a path from approximation to exact integer structure. The same simple operation—divide, record a quotient, continue with a remainder—links all three.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Continued fractions and determinant identity

For \(\alpha=[a_0;a_1,a_2,\ldots]\), initialize

\[
p_{-2}=0,\ p_{-1}=1,\ q_{-2}=1,\ q_{-1}=0,
\quad p_k=a_kp_{k-1}+p_{k-2},\quad q_k=a_kq_{k-1}+q_{k-2}.
\]

Then \(p_k/q_k\) is the \(k\)-th convergent and

\[
p_kq_{k-1}-p_{k-1}q_k=(-1)^{k-1}\quad(k\ge1).
\]

For an irrational \(\alpha\), the standard convergent estimate is \(|\alpha-p_k/q_k|<1/q_k^2\).

Examples:

\[
\frac{415}{93}=[4;2,6,7],\qquad
\sqrt2=[1;\overline2],
\]

with square-root-two convergents \(1,3/2,7/5,17/12,41/29,\ldots\).

### Pell-type norm and recurrence

Let \(N(x+y\sqrt2)=(x+y\sqrt2)(x-y\sqrt2)=x^2-2y^2\). It is multiplicative. Since \(N(3+2\sqrt2)=1\), powers yield solutions. The recurrence is

\[
\binom{x_{k+1}}{y_{k+1}}=
\begin{pmatrix}3&4\\2&3\end{pmatrix}
\binom{x_k}{y_k},\qquad (x_0,y_0)=(1,0).
\]

This constructs infinitely many solutions for \(D=2\); it does not alone prove the general Pell solvability theorem or classify all solutions.

### Practice and reasoning checks

1. Compute the continued fraction and convergents of \(84/31\) directly from Euclidean division.
2. Verify the determinant identity for three consecutive convergents of \(\sqrt2\).
3. Derive the first five positive pairs \((x,y)\) in the power construction for \(x^2-2y^2=1\).
4. Explain why a close decimal approximation to \(\sqrt2\) is not by itself proof of any Pell solution.
5. Show that if \(N(u)=N(v)=1\) for expressions \(u=x+y\sqrt2\), \(v=a+b\sqrt2\), then \(N(uv)=1\).

### Sources and further reading

- MIT OpenCourseWare, *18.781 Theory of Numbers*, lectures 20–23: continued fractions, quadratic irrationalities, and Pell equations: https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/pages/lecture-notes/
- William Stein, *Elementary Number Theory: Primes, Congruences, and Secrets*, continued fractions: https://www.wstein.org/ent/
- Wikipedia background: [Continued fraction](https://en.wikipedia.org/wiki/Continued_fraction), [Simple continued fraction](https://en.wikipedia.org/wiki/Simple_continued_fraction), [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation), [Quadratic irrational number](https://en.wikipedia.org/wiki/Quadratic_irrational_number).
