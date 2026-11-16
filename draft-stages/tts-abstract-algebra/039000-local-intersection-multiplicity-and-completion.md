# 039000 — Local Intersection Multiplicity and Completion

**Track:** Abstract Algebra. **Background:** local rings, smooth curves, ideals, lengths of modules, completion. **Central question:** how does algebra distinguish crossing from tangency?

<!-- BEGIN SPOKEN LECTURE -->

# Local Intersection Multiplicity and Completion

Draw a horizontal line and a parabola that merely touches it at the origin. Both curves pass through the origin. But the encounter is different from two lines crossing there. If we describe intersections only as sets of points, both situations contain one point. Something has been lost. Local intersection multiplicity recovers how strongly the two equations meet.

Take the line defined by y equal to zero and the parabola defined by y equal to x squared. To solve them simultaneously, substitute zero for y. The remaining equation is x squared equals zero. As an ordinary set of solutions, only x equal to zero survives. But the quotient algebra still remembers a nonzero class represented by x, whose square is zero.

That little nilpotent is not a blemish to discard. Its presence says this contact has multiplicity two. Two transverse lines, by comparison, give a quotient in which both local coordinates vanish immediately; the resulting algebra has dimension one over the base field.

## Length as a measure of intersection

Suppose we work over an algebraically closed field and look at two plane curves near an isolated common point P. Localize the polynomial ring at the maximal ideal corresponding to P, then divide by the two defining equations. If the curves have no common local component, the resulting module has finite length. That length is the local intersection multiplicity.

For the line and parabola, after eliminating y the quotient behaves like polynomials in x modulo x squared, with basis one and x. Length two. For the horizontal and vertical axes, the quotient is just the field of constants. Length one. For the line and the curve y equal to x cubed, the same substitution leaves x cubed equal to zero, and the length is three.

What makes this useful is that it is invariant under changes of local coordinates. We did not define multiplicity by judging how flat a picture looks. We counted successive layers of algebra in the local ring. A change of coordinates changes the description but not the module length.

## Tangent directions are only the first test

If two smooth plane curves meet with distinct tangent directions, their first-order equations are independent. Locally, those equations can serve as coordinates, so the intersection multiplicity is one. We call the intersection transverse.

If their tangent directions coincide, the multiplicity is at least two, assuming the intersection remains isolated. Yet tangent agreement alone does not tell us whether the multiplicity is two, three, or more. The higher-order terms decide. This is exactly what happened when we changed x squared to x cubed.

Singularities demand extra care. A cusp described by y squared equal to x cubed meets the line y equal to zero with multiplicity three at the origin. But the cusp itself is not smooth there. One must resist explanations that appeal only to the number or slope of smooth branches. Local length remains meaningful under the proper finite-intersection conditions, including at singular points.

## Why completion is an ally

Near P, many questions depend only on increasingly fine polynomial information around that point. Completion replaces the local polynomial ring by a formal power-series ring. Expressions become infinite series, but finite-length local intersection calculations are preserved. When the quotient is annihilated by a sufficiently high power of the maximal ideal, only a finite jet matters anyway.

For example, the formal power series ring in x and y modulo y and y minus x squared reduces again to the series ring in x modulo x squared. Its basis is one and x. The completion has not altered the answer; it has made the local shape easier to manipulate.

This is not permission to replace all geometry by power series without conditions. Formal expansions encode local information, not the global location of the curve or its entire set of rational points. Completion can illuminate a singularity without determining the global curve on which it sits.

## From a point to a global count

There is a global companion to these local measurements. Two projective plane curves of degrees m and n over an algebraically closed field, with no common irreducible component, have total intersection multiplicity m times n. This is Bézout's theorem. Some intersections may occur at infinity, and tangencies must be counted with their multiplicities.

A line and a parabola have total projective intersection number two. If the line is tangent to the parabola at a single finite point, that single point accounts for both units. A set-theoretic count of one intersection would make the theorem appear false. The local algebra fixes the discrepancy.

We have arrived at an important pattern: a geometric object may look like one point but carry several layers of algebra. The length of a local ring quotient turns those layers into a number. This is how commutative algebra becomes a reliable measuring instrument for geometry.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let \(k\) be algebraically closed and \(F,G\in k[x,y]\) have an isolated common zero \(P\). Put \(R=\mathcal O_{\mathbf A^2,P}\), the regular local ring of the ambient smooth plane at P. Define
\[I_P(F,G)=\operatorname{length}_R(R/(F,G)).\]
This is finite precisely when the intersection is zero dimensional at P (no common local component). For a finite-length local k-algebra supported at a k-rational P, length equals its k-vector-space dimension. Completion preserves the length:
\[\operatorname{length}_R(R/(F,G))=\operatorname{length}_{\widehat R}(\widehat R/(F,G)\widehat R).\]
Here \(\widehat R\simeq k[[x,y]]\) after translating P to the origin.

**Examples at the origin.** \((y,x)\) yields k, hence multiplicity 1. \((y,y-x^2)=(y,x^2)\) yields \(k[x]/(x^2)\), hence multiplicity 2. \((y,y-x^3)\) yields multiplicity 3. The cusp pair \((y,y^2-x^3)=(y,x^3)\) also has multiplicity 3.

For nonsingular curves with independent linear terms, the Jacobian of (F,G) at P has nonzero determinant, hence \(I_P=1\). In projective plane \(\mathbf P_k^2\), Bézout says \(\sum_P I_P(F,G)=mn\) if homogeneous F,G of degrees m,n have no common component. Count all algebraic intersection points including points at infinity; over non-algebraically-closed fields residue degrees enter the count.

### Exercises with answers

1. Compute the intersection multiplicity of \(y=x^4\) and \(y=0\) at the origin. **Answer:** 4 from \(k[[x]]/(x^4)\).
2. Compute it for \(y=x\) and \(y=-x\) over characteristic different from two. **Answer:** 1, since their tangent directions are independent; in characteristic two these equations coincide and the intersection is not isolated.
3. Why does taking the radical of \((y,x^3)\) lose information? **Answer:** its radical is \((x,y)\), whose quotient has length one instead of three.
4. A tangent line meets a nonsingular projective conic at a single point over an algebraically closed field. What is the local multiplicity? **Answer:** 2, by Bézout and absence of any other projective intersection.

### Reading and source notes

- [Stacks Project, Computing intersection multiplicities](https://stacks.math.columbia.edu/tag/0B01), including the local-length calculation.
- [Stacks Project, Algebraic Curves](https://stacks.math.columbia.edu/tag/0BRV), for multiplicities and smooth versus singular curves.
