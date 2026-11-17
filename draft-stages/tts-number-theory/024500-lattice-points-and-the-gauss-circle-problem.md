# 024500 — Counting Lattice Points in a Growing Circle

**Track:** Number Theory from First Principles. **Background:** the two-square representation count, elementary area, asymptotic notation, and basic power series. **Aim:** prove the elementary lattice-point asymptotic and identify the stronger Gauss circle problem.

<!-- BEGIN SPOKEN LECTURE -->

# Counting Lattice Points in a Growing Circle

Imagine the square grid drawn on an enormous sheet of paper. Place a compass at the origin and draw a circle of radius ten. How many intersections of grid lines lie on or inside that circle? Now double the radius. How quickly does the answer grow, and how accurate is the simplest guess based on the area of a disk?

This is a different question from asking how many solutions there are to a squared plus b squared equals a particular integer n. One equation describes a single circle. We will count all grid points whose squared distance from the origin is at most a cutoff. In doing so we will sum the two-square representation function and discover why its average behavior can be simple even though individual values are irregular.

## From a circle to a sum

Let N of R denote the number of integer lattice points, meaning points with both coordinates integers, whose distance from the origin is no greater than R. The origin counts once. For every positive integer n up to R squared, the points whose squared distance is exactly n number r two of n, the function developed from Gaussian integers.

Therefore N of R is one plus the sum of r two of n for positive n no greater than R squared. The sum stops at the integer part of R squared when that number is not an integer. Nothing is approximated here. This is an exact partition of the points by their squared distances.

For radius two, the eligible squared distances are zero, one, two, three and four. At zero we get the origin. At one there are four points on the axes. At two there are four points with coordinates plus or minus one. At three there are none. At four there are four more axis points. That makes thirteen.

For radius three, the count is twenty-nine. For radius ten, it is three hundred seventeen. Compare the disk areas: four pi is about twelve point six, nine pi is about twenty-eight point three, and a hundred pi is about three hundred fourteen point two. The areas seem to predict the right scale, even though individual circles can have more or fewer grid points than their areas suggest.

The precise estimate we will prove is that N of R differs from pi R squared by at most a constant times R, once R is at least one. In asymptotic notation the error is big O of R. It is a rigorous estimate, not a curve fit from those three examples.

## Give each point a little square of territory

Here is a proof that needs no analytic number theory. Around every integer lattice point place a unit square centered at that point, extending half a unit in every coordinate direction. These squares tile the plane, apart from shared boundaries, and each has area one.

Collect the squares centered at lattice points that lie inside our disk of radius R. Call the resulting union U. The interiors of these unit squares do not overlap, so the area of U is exactly N of R.

Now ask how far a corner of one of these squares can lie from its center. It is half a unit horizontally and half a unit vertically away. By the Pythagorean theorem, the maximum distance is the square root of two divided by two. Let's call that small constant delta.

If a square is centered at a point of distance at most R from the origin, every point in that square lies within distance R plus delta. Thus U is contained in the disk of radius R plus delta. This is the easy half of the comparison.

For the reverse direction, take any point whose distance from the origin is at most R minus delta. It lies in some unit square of the tiling. The center of that square is at most delta from our point, so the center lies within distance R. That square was included in U. Therefore the entire disk of radius R minus delta is contained in U, provided R is at least delta.

We have trapped the union of unit squares between two disks. The smaller has area pi times R minus delta, squared; the larger has area pi times R plus delta, squared. Since the union's area is exactly N of R, those two disk areas are lower and upper bounds for the integer count.

Expand the squares. The lower bound is pi R squared minus two pi delta R plus pi delta squared. The upper bound is pi R squared plus two pi delta R plus pi delta squared. In particular the difference between N of R and pi R squared is no larger than a fixed constant times R plus another fixed constant. For R at least one, that is bounded by a constant times R.

We have proved the estimate. The argument does not require primes, the Gaussian integers, or even the divisor formula for r two. It is an elementary comparison between the area of tiles and the area of the shape they occupy.

## Translate geometry back into arithmetic

Now replace the radius R by the square root of a positive real number X. Every lattice point counted by N of the square root of X corresponds to a sum of two squares at most X. Our exact decomposition yields a sum of r two of n through X, with the origin subtracted.

The area estimate becomes: the sum of r two of n for n from one through X equals pi X plus an error bounded by a constant times the square root of X. In symbols we would write pi X plus big O of square root X. It follows immediately that the average number of ordered signed representations among the positive integers through X approaches pi.

This does **not** mean that a typical integer has about three representations. Many integers have none, while some have many, because the prime factorization condition is restrictive. The mean is sensitive to the integers with representations and to how many those integers have. The difference between an average and a typical value is especially important here.

Recall the exact divisor identity: r two of n equals four times the sum of chi four of d over positive divisors d of n. Summing over n no greater than X gives a double count. Every occurrence of a divisor d corresponds to a multiple of d no greater than X, and there are exactly the integer part of X divided by d such multiples. Thus the same circle count is four times the sum, over d up to X, of chi four of d multiplied by the integer part of X over d.

That is an exact arithmetic expression for a geometric quantity. It offers another route to analyzing the count, although estimating it sharply is less immediate than simply placing squares around lattice points. The lesson is methodological: an exact algebraic identity is not automatically the shortest proof of an asymptotic estimate. Sometimes the geometry itself proves the first bound more transparently.

## Where does pi come from in a divisor sum?

There is another bridge worth crossing carefully. For complex s with real part greater than one, the Dirichlet series of the representation count is four times zeta of s times the Dirichlet L-series for chi four. The factor zeta becomes large as s approaches one from the right. In fact, its leading growth is one over s minus one.

The other factor has a finite limit at one. That limit is the alternating reciprocal series one minus one third plus one fifth minus one seventh, continuing forever. A familiar calculus identity, the arctangent series evaluated at one, says that this sum is pi divided by four. Thus the coefficient four times L of one, chi four, is precisely pi.

The same pi has now emerged twice: as the area of the unit disk, and as four times a special value of an L-series. We can check the agreement independently. The square-tiling argument proves the leading geometric coefficient pi; the arithmetic series identifies a matching special value. Neither observation needs the full prime number theorem or a sophisticated contour integral.

A qualification matters. The alternating reciprocal series converges conditionally. We cannot substitute s equals one into the absolutely convergent Euler products as though nothing changed. The value at one comes from the alternating-series theorem, or from the convergent arctangent expansion, together with the separately justified limit as s decreases to one. Keeping the analytic domain visible is part of the argument, not a technical afterthought.

## A second generating series, based on circles instead of divisors

There is also an ordinary power series that packages all circles at once. Consider the sum over every integer m of q raised to m squared, where q has absolute value less than one. Multiplying that series by itself chooses an integer a from one copy and an integer b from the other. Their product term is q raised to a squared plus b squared.

Collect terms with the same exponent. The coefficient of q to the n is precisely r two of n. The constant coefficient, coming only from a and b both zero, is one. This is the square of the classical theta series. We do not need to study modular forms yet to understand its basic coefficients: multiplication of two convergent series is just encoding all integer pairs.

This produces two different transforms of the same representation function. The Dirichlet series is a product of zeta and a character L-function. The ordinary theta series is a square because a two-dimensional lattice has two independent coordinates. Each transform emphasizes a different structure: multiplication of integers in the first case, addition of squares in the second.

## The boundary between a first estimate and a hard problem

We proved that the error in the lattice count is at most a constant times the radius. Could the fluctuations be bounded by a much smaller power of the radius? That question is called Gauss's circle problem. Our method does not settle it.

The unit squares are a deliberately blunt instrument. They let us bound discrepancies by examining a band of fixed width around the circle, whose area grows like its circumference. But the grid points near different parts of the boundary do not all err in the same direction. Better estimates exploit cancellation that the simple area sandwich ignores.

It would be a mistake to turn the elementary estimate into the claim that the error is *of order* R, with a matching lower bound. We have proved an upper bound. We have not proved that it is best possible, and it is not the sharpest known bound.

The virtue of the proof is its clarity. A circle contains roughly its area in integer points because unit squares tile the plane, and only squares near the boundary complicate the comparison. From that geometric fact follows the mean value of a multiplicative representation function. The same quantity can be viewed as a divisor sum, a Dirichlet series, or the coefficient of a theta series. Number theory grows by moving between these viewpoints, but each move must preserve the exact statement being made.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Exact decompositions

Let \(R\ge0\), and let \(N(R)=\#\{(a,b)\in\mathbb Z^2:a^2+b^2\le R^2\}\). Then
\[
\boxed{N(R)=1+\sum_{1\le n\le R^2}r_2(n).}
\]
For integer \(R\ge0\), the first-quadrant decomposition yields an exact finite sum:
\[
\boxed{N(R)=1+4R+4\sum_{a=1}^{R}\left\lfloor\sqrt{R^2-a^2}\right\rfloor.}
\]
The first term is the origin; \(4R\) counts nonzero axis points; the sum counts the four sign choices when both coordinates are nonzero.

### Unit-square proof of the elementary error bound

Center a closed unit square \(C_z=z+[-\tfrac12,\tfrac12]^2\) at each \(z\in\mathbb Z^2\). Let \(U_R=\bigcup_{|z|\le R}C_z\) and \(\delta=\sqrt2/2\). Square interiors are disjoint, so \(\operatorname{area}(U_R)=N(R)\). For \(R\ge\delta\), the nearest lattice center is within \(\delta\) of any point in the plane, giving
\[
D_{R-\delta}\subseteq U_R\subseteq D_{R+\delta},
\]
and hence
\[
\pi(R-\delta)^2\le N(R)\le\pi(R+\delta)^2.
\]
Therefore for \(R\ge1\),
\[
\boxed{\left|N(R)-\pi R^2\right|\le 2\pi\delta R+\pi\delta^2 =\sqrt2\pi R+\frac\pi2.}
\]
For \(X\ge1\), subtract the origin and take \(R=\sqrt X\):
\[
\boxed{\sum_{n\le X}r_2(n)=\pi X+O(\sqrt X).}
\]
This is an *upper* error estimate, not a matching lower bound for the error magnitude.

### Divisor-sum and theta-series viewpoints

By the preceding counting theorem,
\[
N(\sqrt X)-1=4\sum_{n\le X}\sum_{d\mid n}\chi_4(d)
=4\sum_{d\le X}\chi_4(d)\left\lfloor\frac Xd\right\rfloor.
\]
For \(|q|<1\), define \(\theta(q)=\sum_{m\in\mathbb Z}q^{m^2}\). Absolute convergence gives
\[
\boxed{\theta(q)^2=\sum_{n\ge0}r_2(n)q^n
=1+4q+4q^2+4q^4+8q^5+\cdots.}
\]
For \(\Re(s)>1\), \(\sum_{n\ge1}r_2(n)n^{-s}=4\zeta(s)L(s,\chi_4)\). The conditionally convergent value
\[
L(1,\chi_4)=1-\frac13+\frac15-\cdots=\arctan(1)=\frac\pi4
\]
is obtained by Abel limits/arctangent calculus, not by substituting directly into an Euler product at its boundary.

### Worked small radii

| \(R\) | \(N(R)\) | \(\pi R^2\) (approx.) |
|---|---:|---:|
| 1 | 5 | 3.14 |
| 2 | 13 | 12.57 |
| 3 | 29 | 28.27 |
| 5 | 81 | 78.54 |
| 10 | 317 | 314.16 |

### Exercises

1. Verify the exact finite-sum formula at \(R=2\) and \(R=3\).
2. Check the inclusions \(D_{R-\delta}\subseteq U_R\subseteq D_{R+\delta}\) by using the nearest integer to each coordinate.
3. Show that \(\frac1X\sum_{1\le n\le X}r_2(n)\to\pi\) as \(X\to\infty\).
4. Derive the coefficient of \(q^5\) in \(\theta(q)^2\) directly from the pairs \((a,b)\).
5. Explain why an error estimate \(E(R)=O(R)\) does not imply \(|E(R)|\ge cR\) for infinitely many \(R\).

### Reading and source notes

- Eric W. Weisstein, [Gauss's Circle Problem, MathWorld](https://mathworld.wolfram.com/GausssCircleProblem.html), geometric count and boundary discrepancy.
- Eric W. Weisstein, [Sum of Squares Function, MathWorld](https://mathworld.wolfram.com/SumofSquaresFunction.html), relation to theta series, divisor sums and summatory counts.
- Wikipedia: [Gauss circle problem](https://en.wikipedia.org/wiki/Gauss_circle_problem), [Theta function](https://en.wikipedia.org/wiki/Theta_function), [Leibniz formula for pi](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80), [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation).
