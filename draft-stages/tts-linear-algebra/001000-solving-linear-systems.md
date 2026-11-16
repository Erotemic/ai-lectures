# 001000 — Solving Linear Systems: From Equations to Elimination

**Track:** Linear Algebra from First Principles. **Background:** arithmetic, algebraic equations and coordinates. **Question:** when do several linear measurements determine an unknown uniquely?

<!-- BEGIN SPOKEN LECTURE -->

# Solving Linear Systems: From Equations to Elimination

Imagine you need to determine two unknown prices from two shopping receipts. One receipt says that two apples and one pear cost seven units. Another says that one apple and three pears cost eleven units. Call the apple price x and the pear price y. We have two times x plus y equals seven, and x plus three times y equals eleven. The challenge is not simply to find two numbers. It is to develop a method that continues to work when there are a thousand unknowns, or when there is no solution, or infinitely many.

A linear equation says that a weighted sum of unknowns equals a specified number. The important restriction is that we never multiply unknowns together or take their squares. The unknowns enter only to the first power. For two variables, each nontrivial equation describes a line in the plane. Solving the system means finding the point, or points, common to all those lines.

## Remove a variable without changing the answers

Return to our receipts. Multiply the second equation by two. It now says two x plus six y equals twenty-two. Subtract the first equation from that, and five y equals fifteen. So y equals three, and the first equation gives x equals two. Check rather than trust the algebra: two apples at two units and one pear at three make seven; one apple and three pears make eleven.

This is elimination. We replace one equation with a combination of equations that preserves exactly the same solutions. There are three elementary operations: exchange two equations; multiply an equation by a nonzero scalar; and add a multiple of one equation to another. Each can be undone. The restriction that the multiplier be nonzero matters: replacing an equation with zero equals zero would erase information.

For our system we can also record just the coefficients and right-hand side. The first row is two, one, seven. The second is one, three, eleven. A vertical line before the last number separates coefficients from results. That rectangle is an augmented matrix. The algebraic operations on equations become row operations on the matrix. A matrix is therefore initially a compact record of a system of linear measurements, not an object that needs mystical properties.

## Pivots and free choices

Consider a different system: x plus y plus z equals four, and two x plus two y plus two z equals eight. The second statement is twice the first. It does not add an independent condition. We may choose y and z freely, then set x equal to four minus y minus z. There are infinitely many solutions. The place where a leading variable is determined is called a pivot position; a variable without a pivot can be chosen freely.

Now replace eight by nine. The equations would require the same sum to equal both four and four and a half. Row reduction produces a row of zero coefficients and a nonzero right-hand side. That row says zero equals one. No choices of the variables can satisfy it. Such a system is inconsistent.

So there are three possibilities. If all variables receive pivots and the equations are consistent, the solution is unique. If some variables are free and the equations are consistent, there are infinitely many solutions over the real numbers. If reduction produces a contradiction, there is no solution at all.

This classification gives more insight than the old rule that one needs as many equations as unknowns. Two equations can be copies of each other. Three equations can contradict one another. The meaningful quantity is the number of independent constraints, not the raw number of rows.

## A geometric interpretation

A single equation in three variables usually describes a plane. Two independent equations intersect along a line. Three independent equations can meet at a point. But planes can be parallel, or can coincide. Row reduction discovers which geometric configuration we have without asking us to draw a picture in a space of dozens of dimensions.

If the right-hand side is zero in every equation, the system is called homogeneous. It always has at least the all-zero solution. In a homogeneous system, any two solutions may be added, and any solution may be scaled, to obtain another. This closure is the beginning of the idea of a vector space: a collection where addition and scaling make sense without leaving the collection.

A nonhomogeneous system, when it has any solutions, is instead a shifted copy of the homogeneous solution set. Choose one particular solution. Add to it any homogeneous solution, and you get another solution. Subtract two particular solutions from each other, and the result solves the homogeneous equations. We will use that principle repeatedly: first solve one instance; then understand the directions in which we can move without changing the measured result.

## Elimination is a proof as well as an algorithm

Why does elimination work? Because it records logical equivalences. Every permitted operation changes the written equations but preserves the set of possible answers. When a reduced row says a variable has a certain value, that is a necessary condition. When a final choice is substituted back and works, it is sufficient. Together they certify the answer.

There is also a practical lesson. A pivot may be zero, so we sometimes exchange rows to find a nonzero coefficient. On computers, a pivot can be nonzero but dangerously small; choosing a better pivot often makes a floating-point computation much more reliable. That numerical issue is separate from the exact algebra taught here. It is a reason to understand the algebra before treating a solver as a black box.

Linear algebra starts with the ability to transform simultaneous constraints into a readable form. From elimination we will acquire the ideas of independent information, free directions, dimension, and invertibility. The goal is not to memorize a collection of elimination tricks. It is to learn to recognize exactly what a system of linear observations does and does not determine.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a system \(Ax=b\), elementary row operations are multiplication on the left by invertible elementary matrices; hence \(Ax=b\) and \(EAx=Eb\) have identical solution sets. For the receipt example,
\[
\left[\begin{array}{cc|c}2&1&7\\1&3&11\end{array}\right]
\to\left[\begin{array}{cc|c}1&3&11\\0&-5&-15\end{array}\right]
\to\left[\begin{array}{cc|c}1&0&2\\0&1&3\end{array}\right].
\]
For \(Ax=b\) consistent, the complete set of solutions is \(x_0+\ker A\). A contradiction row \([0\ \cdots\ 0\mid c]\), \(c\ne0\), rules out all solutions. Over an infinite field, a nontrivial kernel yields infinitely many solutions. Over a finite field it yields multiple but finitely many.

### Exercises with answers

1. Solve \(x+y=5\), \(2x-y=1\). **Answer:** \(x=2,y=3\).
2. Does \(x+y=1,2x+2y=3\) have a solution? **Answer:** no; doubling the first equation contradicts the second.
3. Solve \(x+2y+z=0\). **Answer:** \((x,y,z)=(-2s-t,s,t)\) for arbitrary real \(s,t\).
4. Why are row swaps reversible? **Answer:** exchanging the same pair a second time restores the original system.

### Sources and further reading

- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), systems and Gauss's method.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), lectures on elimination and nullspaces.
- [System of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations).
