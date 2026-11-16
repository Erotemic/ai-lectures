# 013000 — Interval Arithmetic: From Plausible Answers to Verified Enclosures

**Track:** Numerical Analysis and Reliable Computation. **Background:** floating-point error, conditioning, Newton iteration, numerical quadrature. **Central question:** what does a computation need to do before we can claim it encloses the exact mathematical answer?

<!-- BEGIN SPOKEN LECTURE -->

# Interval Arithmetic: From Plausible Answers to Verified Enclosures

A numerical program returns a number. How do we know the true answer is near it? Sometimes we compare several step sizes and observe convergence. Sometimes a solver prints a residual. Those are useful diagnostics, but they do not automatically prove an upper bound on the error. Interval arithmetic takes a different approach: compute a range that is guaranteed to contain the exact result, provided the mathematical input and each interval operation are represented correctly.

The idea sounds simple. Instead of carrying one approximate number, carry a lower and upper bound. But to make those bounds rigorous on a finite machine, every arithmetic operation must be implemented with the right rounding direction. The width of the interval must account for all uncertainties being represented, not just the ones convenient to model.

## Intervals as sets

An interval from a to b means the set of all real numbers between a and b, including the endpoints. If X and Y are intervals, their exact interval sum is the set of all x plus y with x in X and y in Y. Its endpoints are the sums of the respective lower and upper endpoints. Multiplication is a little more involved: inspect all four products of endpoint choices and take the smallest and largest.

In exact real arithmetic, these set operations enclose every possible result. On a floating-point machine, though, the exact mathematical endpoint may not have a representable binary value. If we round the lower endpoint toward the nearest representable number, we might round upward and accidentally exclude the true result. A rigorous interval addition instead rounds the lower endpoint down and the upper endpoint up. The same outward-rounding principle applies to multiplication, division, and transcendental functions using certified enclosures.

Without this distinction, an interval-looking data structure is not automatically validated arithmetic. A pair of ordinary floating-point numbers is just a pair until the operations maintain the enclosure invariant.

## Why input conversion matters

Consider the decimal number one tenth. Its exact rational value cannot be represented exactly by a finite binary floating-point fraction. If a program converts that decimal into a nearest floating-point value and then wraps the result in an interval with equal endpoints, the interval contains the rounded binary number, not necessarily the mathematical decimal one tenth.

To enclose the original decimal exactly, the conversion must produce lower and upper representable neighbors around the rational value, or retain the rational value symbolically. Similar care is needed for measured input data. If a length is known only to within a millimeter, outward floating-point rounding alone does not capture that physical uncertainty; the starting interval must include the measurement range too.

Validated arithmetic can certify a statement about the model it was given. It cannot certify that an uncertain model describes reality more accurately than its assumptions permit.

## The dependency problem

A guaranteed enclosure can still be frustratingly wide. Take X to be the interval from zero to one. The mathematical function f of x equals x minus x is identically zero. Its exact range is just zero. But evaluate the expression using independent interval occurrences of X: X minus X gives the interval from negative one to one.

The interval operation has done nothing incorrect. It allowed the first x and the second x to vary independently, even though in the mathematical expression they are the same variable. That lost relationship is called the dependency problem.

It gets worse in long expressions. Repeated uses of a variable can inflate a natural interval evaluation far beyond the true range. Algebraic simplification, centered forms, Taylor models, or subdivision can restore useful tightness. This is a reminder that rigorous and sharp are different properties. A huge enclosing interval may be correct but practically uninformative.

## An interval Newton step

Consider the equation x squared equals two. We know one positive root lies between one and two. Ordinary Newton iteration takes an approximate midpoint, evaluates a derivative there, and predicts a better point. Interval Newton replaces the point derivative with an interval enclosing derivatives throughout the current candidate range.

Start with the interval from one to two and choose its midpoint, one and a half. The function value at the midpoint is one quarter. Over the full interval, the derivative two x ranges from two to four. Dividing one quarter by that derivative interval gives values from one sixteenth to one eighth. Subtract from one and a half, and we obtain the interval from one and three eighths to one and seven sixteenths.

In decimals, that is from 1.375 to 1.4375. It contains the positive square root of two. More importantly, the interval Newton theorem gives a route to certify both existence and uniqueness when the computed Newton image is contained strictly in the interior of the original interval and the required differentiability and nonzero-derivative conditions hold. Here those conditions are met. The enclosure can then be refined with further outward-rounded steps.

The calculation has not merely generated more digits. It has constructed a statement about all possible roots in the initial interval. In higher dimensions the analogous methods involve interval Jacobians, fixed-point or contraction arguments, and additional care with matrix inverses and conditioning.

## What constitutes a certificate

A certified numerical result should say exactly what is enclosed. It might assert that a polynomial has exactly one real root in a stated interval. It might assert that a computed integral differs from an exact integral by at most a certain amount under a specific regularity assumption. It might bound the solution of a linear system when coefficients and right-hand sides belong to known intervals.

Different problems require different proof ingredients. Outward-rounded evaluation alone may bound the range of a function on a box, but it does not automatically prove a root exists there. A zero appearing inside f of X says only that zero has not been excluded by the range bound. Existence generally requires a sign argument, an interval Newton inclusion, topological degree, or another theorem. Similarly, a small residual does not automatically imply a small solution error unless the inverse sensitivity is controlled.

We should also distinguish an interval method that encloses the exact answer to the stated finite-dimensional equations from a validated solution of a continuous differential equation. The latter may require explicit discretization-error estimates in addition to floating-point control. Certifying the algebraic solve is only one part of certifying a numerical model of a PDE.

## Reproducibility and libraries

The details of machine arithmetic matter. IEEE floating-point environments support specified rounding behavior, but how a language or compiler exposes and preserves directed rounding must be checked. Some interval libraries use hardware rounding modes; others implement conservative endpoint operations through software. Transcendental bounds, exceptional values, overflow, and interval division through zero all require defined treatment.

The goal is not to mistrust every decimal approximation. Ordinary floating-point methods are often extremely effective, and an error estimate may be more useful than a heavy certificate when decisions tolerate uncertainty. The goal is to know which claim we are making. If we say the exact answer lies in a particular interval, then every stage must preserve that inclusion. The strength of interval arithmetic is that it makes the burden of proof explicit: an enclosure is a theorem the computation has to maintain, not a visual impression of numerical accuracy.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

An interval \(X=[\underline x,\overline x]\) denotes a set of real numbers. Exact set addition is
\[
X+Y=[\underline x+\underline y,\overline x+\overline y].
\]
A validated floating-point implementation rounds the lower endpoint **downward** and the upper **upward** for every primitive operation. Multiplication encloses all four endpoint products. If \(0\in Y\), interval division by \(Y\) requires a specified extended-interval or failure policy; naive reciprocal formulas are invalid.

**Dependency example:** for \(X=[0,1]\), \(X-X=[-1,1]\), whereas \(\{x-x:x\in X\}=\{0\}\). Inclusion does not imply a tight enclosure.

**Interval Newton:** for \(f(x)=x^2-2\), \(X=[1,2]\), midpoint \(m=3/2\), and derivative enclosure \(f'(X)=[2,4]\),
\[
N(X)=m-\frac{f(m)}{f'(X)}=\frac32-\frac{1/4}{[2,4]}
=[11/8,23/16]=[1.375,1.4375]\subset\operatorname{int}(X).
\]
The interval-Newton inclusion and nonzero derivative certify a unique zero of \(f\) in \(X\), with all displayed rational endpoints exactly representable in binary. Further interval iteration contracts the enclosure.

A validated result must specify the mathematical input uncertainty, outward-rounded implementation, treatment of exceptional operations, and any analytic hypotheses used to infer roots, uniqueness, or discretization error. IEEE 1788-2015 specified a standard interval arithmetic model, but its status and actual implementations should be verified for a given project.

### Exercises with answers

1. What does natural interval evaluation give for \(X-X\) when \(X=[2,3]\)? **Answer:** \([-1,1]\), even though the exact range of \(x-x\) is \(\{0\}\).
2. Does \(0\in f(X)\) prove \(f\) has a root in \(X\)? **No:** interval overestimation may include zero even when the actual range does not.
3. Why can a single nearest-rounded floating point value fail to enclose the decimal \(0.1\)? **Answer:** the rounded binary value generally differs from the exact rational \(1/10\).
4. Does a certified small residual suffice to bound a linear-system solution error? **Not by itself:** the inverse or condition of the operator must be bounded too.

### Reading and source notes

- IEEE Standards Association, [IEEE 1788-2015 Standard for Interval Arithmetic](https://standards.ieee.org/ieee/1788/4431/), interval operation semantics (standards status subject to change).
- Siegfried M. Rump, *Verification Methods: Rigorous Results Using Floating-Point Arithmetic*, Acta Numerica 19 (2010), https://doi.org/10.1017/S096249291000005X.
- Ramon E. Moore, R. Baker Kearfott, and Michael J. Cloud, *Introduction to Interval Analysis* (SIAM, 2009).
