# Two Ends, One Equation: Boundary Conditions from Scratch

<!-- BEGIN SPOKEN LECTURE -->

# Two Ends, One Equation

Suppose a metal rod is held at one temperature on its left end and a different temperature on its right. We want its temperature at every point between them, after it has settled into equilibrium. There is no starting time in that question. Neither end gives a starting instruction to march forward along the rod. Both ends constrain the same unknown shape.

That simple change is the entrance to boundary-value problems. In an initial-value problem, we supply enough information at one time to determine what happens afterward. In a boundary-value problem, we prescribe information at different places, perhaps at both ends of an interval. The differential equation still relates derivatives to the function. But the way we choose the constants of integration changes, and so do our existence and uniqueness questions.

We can learn a surprising amount from the most elementary second-order equation, without yet invoking functional analysis or partial differential equations. Our example will also explain what Dirichlet, Neumann, and Robin conditions really say, why a boundary problem sometimes has no solution, and how to replace a continuum of positions with a small linear system.

## An equation for a steady profile

Let x range from zero to one. Call the unknown profile u of x. Suppose the negative second derivative of u equals two. A second derivative measures curvature: a positive second derivative bends the graph upward; a negative one bends it downward. Our equation requires the graph to be concave down everywhere, with the same curvature.

Integrate once. The first derivative is negative two x plus a constant, which we will call C. Integrate again. The function is negative x squared plus C times x plus a second constant, D. Two integrations produce two constants, just as solving a second-order equation in time requires two initial pieces of data.

Now impose the conditions that u equals zero at x equal to zero, and also equals zero at x equal to one. At the left end, D must be zero. At the right end, negative one plus C equals zero, so C must be one. We obtain u of x equals x times one minus x.

Check all three requirements. At the left end, the function is zero. At the right end it is also zero. Its second derivative is negative two everywhere, so the negative second derivative is two. The maximum occurs halfway along the interval, where u is one quarter. These checks are not optional: we have solved an equation and two boundary conditions, not merely found an expression with the right curvature.

What if we had been given only the value at the left end? Then D would be fixed, but C could be anything. Knowing one endpoint value would not tell us how the shape should bend into the right endpoint. In an initial-value problem for a second-order equation we could specify both u and its first derivative at one location. Here we specify one value at each of two different locations. There are still two constraints, but they do not act in the same way.

## Why uniqueness must be checked

For this particular problem, the answer is unique. Here is the short proof that explains why. Suppose there were two different profiles, u and v, both satisfying the same second-derivative equation and the same zero values at the two endpoints. Subtract them. The difference, w, has second derivative zero, so w must be a straight line. It also vanishes at both endpoints. The only straight line through those two zero values is the zero line. Therefore the two profiles are identical.

Notice what made that proof work: the difference obeyed the homogeneous equation, and its only zero-boundary solution was trivial. Later, an eigenvalue problem will show that a homogeneous boundary problem can have nonzero solutions. At such a parameter value, uniqueness can fail, and a forced boundary problem may even become inconsistent. Boundary conditions are not an automatic guarantee of a solution.

Suppose instead that the left end is held at temperature ten and the right end at temperature twenty, while the same internal source acts. We can solve this without repeating all the integration. The straight line ten plus ten x joins the two prescribed temperatures. Add our previously calculated bowed profile, x times one minus x, which is zero at both ends. The resulting function is ten plus ten x plus x times one minus x. It has the right curvature and the right endpoint values. This trick is called lifting the boundary data: subtract a simple known function to convert nonzero boundary values into homogeneous ones.

The lifted problem is often easier, because adding and subtracting functions that vanish at the boundary preserves those conditions. We will use that fact when we construct solutions from sine waves.

## A boundary value can be a slope instead

Prescribing u itself at an endpoint is a Dirichlet condition. But some physical boundaries prescribe the slope, or, more precisely, a flux proportional to the slope. Think about heat conduction. In one dimension, Fourier's law says heat flows down the temperature gradient. The heat flux to the right is negative thermal conductivity times the spatial derivative of temperature. For a steady state with a source, conservation says that the spatial derivative of that flux equals the rate of heat supplied per unit length. With constant conductivity, the equation becomes a constant times the negative second derivative of temperature equals the source.

An insulated end allows no heat to cross, so the outward heat flux vanishes. When conductivity is positive and finite, that means the spatial derivative of temperature is zero at that end. Such a requirement on the derivative is a Neumann condition. It speaks about what crosses the boundary, not necessarily what temperature the boundary takes.

Try a problem with both ends insulated: negative u double prime equals two x minus one, and u prime equals zero at both zero and one. The source is positive in the right half and negative in the left half. Its total integral over the interval is zero: one half is a source, the other half a sink.

Integrating the equation gives u prime equals x minus x squared plus C. The left derivative condition makes C zero; the right one is then satisfied automatically, because one minus one is zero. Another integration gives u equals x squared divided by two, minus x cubed divided by three, plus any constant D. Every value of D works. The slopes and the source determine the shape but not its overall vertical level.

This is not a numerical defect or an error in our integration. If adding a constant does not change the equation or the boundary slopes, no measurement of those slopes can determine the constant. We could choose the average temperature, or prescribe u at one point, to fix it. If we choose the average to be zero, the constant is negative one twelfth. But that is extra information, not something implied by insulation.

## When an insulated problem is impossible

Why did the right derivative condition work automatically? Integrate the original equation from zero to one. The integral of negative u double prime is negative u prime at one plus u prime at zero. If both slopes must be zero, that expression must be zero. Therefore the total source must integrate to zero. This is the compatibility condition for a pure Neumann problem.

Replace the source two x minus one with the constant source one. The total source is one, not zero. A rod receiving heat everywhere but losing none through either end cannot be in a stationary equilibrium with that source, in this simplified model. Mathematically, no steady solution satisfies both zero-flux conditions. Integrating the equation exposes the contradiction immediately.

Compare the three outcomes. Our zero-value Dirichlet problem had one solution. The compatible insulated Neumann problem had an entire family differing by constants. The incompatible insulated problem had no solution. All three are elementary second-order differential equations. It is the combination of the equation and boundary conditions that determines what we may conclude.

A third common kind of condition combines the value and its outward derivative. Suppose an endpoint exchanges heat with surrounding air. In a simple linear heat-transfer model, outgoing conductive flux is proportional to the temperature difference between the endpoint and the air. This becomes a condition involving both the endpoint temperature and its outward derivative. Such a condition is called Robin, or mixed, boundary data. It interpolates, in a modeling sense, between strongly controlling the temperature and nearly insulating an end. We must use the outward normal carefully: on the left end it points left, and on the right it points right. A single sign copied uncritically to both ends can reverse the physics.

## Boundary conditions can be computed with a matrix

We have so far integrated exact formulas. Most realistic sources or coefficients do not lead to such convenient antiderivatives. One practical approach samples the rod at evenly spaced locations. A second derivative at an interior point is approximately the value to its left minus twice the value at the point plus the value to its right, divided by the square of the spacing. That is the central second-difference formula.

Let us use only two unknown interior temperatures, located one third and two thirds of the way along the rod, with zero at both endpoints. The spacing is one third. For negative u double prime equal to two, the first interior equation says nine times twice the first unknown minus nine times the second equals two. The second says nine times twice the second unknown minus nine times the first equals two.

The two equations are symmetric. Subtract them and see that both unknowns are equal. Substitute back: nine times either unknown equals two, so both are two ninths. Compare with our exact parabola, x times one minus x. At one third, it gives one third times two thirds, or two ninths; at two thirds, the same. The finite-difference computation happens to be exact at these sample points because a central second difference reproduces the second derivative of a quadratic exactly.

Do not generalize that exactness to arbitrary curves. Higher derivatives generate approximation error. Yet this little calculation shows how the differential equation and endpoint information become an ordinary linear algebra problem. The boundary values enter the equations beside the unknown interior values. A different boundary type changes the first and last rows, and it may change whether the resulting matrix is invertible.

There is an especially useful distinction between solving by shooting and solving all the interior equations together. Shooting guesses the missing initial slope at the left endpoint, integrates the ordinary differential equation across the interval, and adjusts the guess until the right endpoint is satisfied. The finite-difference method imposes the two boundaries simultaneously. Either can work for an elementary problem. Neither can restore a solution when the underlying boundary conditions are inconsistent.

## What these examples teach us to check

The most important lesson is not a list of boundary-condition names. It is a way of thinking about the whole problem. First identify the domain: which positions count as interior? Then identify the equation there, including the sign of its second derivative and any sources or coefficients. Next translate what the boundaries physically or mathematically prescribe. Finally ask separately about existence, uniqueness, and a procedure for computing a solution.

For the fixed-end, constant-source problem, there was one bowed profile. For insulated ends, the total source had to balance, and even then the vertical level remained free. Those are structural conclusions we obtained before applying any advanced theorem.

A deeper connection is waiting in the simple uniqueness argument. The difference of two solutions obeyed a homogeneous equation. If a homogeneous boundary problem admits a nonzero spatial shape, adding that shape may produce another solution. Exactly when does that happen? For the negative second-derivative operator, the answer involves specially chosen sine and cosine functions and a discrete set of eigenvalues. The basic boundary-value problem is therefore the doorway to Fourier modes, heat diffusion, and vibrating strings.

<!-- END SPOKEN LECTURE -->

## Mathematical companion: exact statements and calculations

### Dirichlet problem and lifting

On \(0<x<1\), solve
\[
-u''=2,\quad u(0)=u(1)=0.
\]
The general integrated solution is \(u=-x^2+Cx+D\); the conditions give \(C=1,D=0\), hence \(u=x(1-x)\). For the same source with \(u(0)=10,u(1)=20\), choose the lift \(g(x)=10+10x\). Then \(v=u-g\) has zero boundary data and \(-v''=2\), so \(u=g+x(1-x)\).

**Uniqueness:** If \(u,v\) solve the same Dirichlet problem, \(w=u-v\) satisfies \(w''=0,w(0)=w(1)=0\), hence \(w\equiv0\).

### Conservation law and Neumann compatibility

With constant conductivity \(k>0\), define rightward conductive flux \(q=-ku'\). Stationary balance with source \(f\) gives \(q'=f\), or \(-(ku')'=f\). Integrating on \([0,L]\) yields
\[
- k u'(L)+k u'(0)=\int_0^L f(x)\,dx.
\]
Thus homogeneous Neumann conditions at both ends require \(\int_0^L f=0\). For \(k=1,L=1,f(x)=2x-1\),
\[
u(x)=\frac{x^2}{2}-\frac{x^3}{3}+C,\quad u'(x)=x-x^2.
\]
The average of the polynomial part is \(1/12\), so the unique mean-zero representative has \(C=-1/12\). For \(f\equiv1\), both homogeneous Neumann conditions are inconsistent.

For an endpoint in contact with ambient temperature \(u_\infty\), a Newton cooling boundary model is
\[
-k\,\partial_n u=h(u-u_\infty),\qquad\text{equivalently}\qquad \partial_n u+(h/k)(u-u_\infty)=0,
\]
where \(\partial_n u=n u'\), with \(n=-1\) on the left and \(n=+1\) on the right.

### Two-node finite-difference example

Let \(h=1/3\) and \(U_0=U_3=0\). Central differences for \(-u''(x_i)=2\) give
\[
\frac1{h^2}\begin{bmatrix}2&-1\\-1&2\end{bmatrix}
\begin{bmatrix}U_1\\U_2\end{bmatrix}=
\begin{bmatrix}2\\2\end{bmatrix},\qquad
\begin{bmatrix}U_1\\U_2\end{bmatrix}=
\begin{bmatrix}2/9\\2/9\end{bmatrix}.
\]
For smooth \(u\), the centered second difference is \(u''(x_i)+(h^2/12)u^{(4)}(x_i)+O(h^4)\), explaining exactness on the quadratic test.

### Exercises with answers

1. Solve \(-u''=6\), \(u(0)=u(1)=0\). **Answer:** \(u=3x(1-x)\).
2. Solve \(-u''=0\), \(u(0)=2,u(1)=-1\). **Answer:** \(u=2-3x\).
3. Test \(-u''=x\) with \(u'(0)=u'(1)=0\). **Answer:** no solution, because \(\int_0^1x\,dx=1/2\neq0\).
4. For \(-u''=2x-1\), zero endpoint slopes, find the representative with \(u(1/2)=0\). **Answer:** \(u=x^2/2-x^3/3-1/12\) (since the polynomial part equals \(1/12\) at \(x=1/2\)).
5. State what data a second-order scalar initial-value problem normally requires at a single point. **Answer:** the value and the first derivative, rather than one value at each endpoint.

### Sources and further reading

- [Jiří Lebl, *Differential Equations for Engineers*, Sturm–Liouville problems](https://math.libretexts.org/Bookshelves/Differential_Equations/Differential_Equations_for_Engineers_%28Lebl%29/5%3A_Eigenvalue_problems/5.1%3A_Sturm-Liouville_problems).
- [MIT OpenCourseWare, ES.1803 Topic Notes, Topics 23–26](https://ocw.mit.edu/courses/es-1803-differential-equations-spring-2024/pages/topic-notes/).
- [William F. Trench, *The Heat Equation*](https://math.libretexts.org/Bookshelves/Differential_Equations/Elementary_Differential_Equations_with_Boundary_Value_Problems_%28Trench%29/12%3A_Fourier_Solutions_of_Partial_Differential_Equations/12.01%3A_The_Heat_Equation).
