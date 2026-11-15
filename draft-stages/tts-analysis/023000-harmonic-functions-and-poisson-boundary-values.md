# 023000 — Harmonic Functions: A Value Determined by Its Neighbors

**Track:** Analysis from First Principles. **Background:** real partial derivatives, complex differentiation, Cauchy's integral formula, maximum principles. **Question:** Why does the average of nearby values exactly reproduce a harmonic function, and what is the role of the domain's holes?

<!-- BEGIN SPOKEN LECTURE -->

# Harmonic Functions: A Value Determined by Its Neighbors

Picture a thin plate whose edge is held at prescribed temperatures. After heat has flowed long enough for the temperature to settle, where are the hottest and coldest points? If there is no internal heat source, a steady-state temperature cannot have a strictly hotter spot hidden inside than every point along the edge. Each interior value is balanced by its neighbors.

That physical picture leads to harmonic functions. They appear in electrostatics, ideal fluid flow, potential theory, and complex analysis. In two dimensions they are especially tractable because they are closely related to holomorphic functions. The relation is strong, but it is not unconditional. A local harmonic function can have a holomorphic partner in every small disk while failing to have a single-valued partner on a region with a hole. We will see both the local balance law and the global obstruction.

## A simple surface with competing directions

Consider a real function of two coordinates: the first coordinate squared minus the second coordinate squared. In the horizontal direction the surface rises as we move away from zero; in the vertical direction it falls. At the origin it has neither a local maximum nor a local minimum, but a saddle.

Compute its second derivative in the horizontal direction: it is two. Compute its second derivative in the vertical direction: it is negative two. Add them. The result is zero. The opposite curvatures cancel.

This cancellation is the defining equation of a harmonic function in the plane. A twice continuously differentiable real-valued function is harmonic when the second derivative in one coordinate direction plus the second derivative in the perpendicular direction equals zero at every point. This sum is the Laplacian. Being harmonic means the Laplacian vanishes.

The name of the differential equation may sound technical, but the condition has a direct consequence. A surface that bends upward in one direction must, at that point, bend downward enough in other directions to keep the sum balanced. A harmonic function has no isolated pocket where every nearby direction bends toward a strict interior extremum. To turn that intuition into a theorem, though, we need more than a drawing of a saddle.

## Where holomorphic functions enter

Suppose f is holomorphic on a complex domain. Write its output as a real part u and an imaginary part v. The Cauchy–Riemann equations link the coordinate derivatives: the horizontal derivative of u equals the vertical derivative of v, and the vertical derivative of u is the negative of the horizontal derivative of v.

Differentiate once more. Because holomorphic functions have continuous higher derivatives, mixed partial derivatives commute. Adding the two second derivatives of u gives two terms that cancel. Thus the Laplacian of u is zero. The same calculation works for v. Both parts of a holomorphic function are harmonic.

This gives an easy way to manufacture examples. The function z squared has real part x squared minus y squared, exactly the saddle from our opening. Its imaginary part is two times x times y, another harmonic function. The complex exponential gives yet another: its real part is an ordinary exponential in the horizontal coordinate multiplied by a cosine of the vertical coordinate. Those two pieces by themselves look quite different, but their combined second derivatives cancel.

There is an important reverse question. If I hand you a harmonic real-valued function u, can you find a real-valued function v so that u plus i times v is holomorphic? On a small enough disk, yes. On a simply connected domain, also yes. On an arbitrary region with holes, not always. Understanding the failure is as informative as understanding the local construction.

## Recovering the missing imaginary part

To create v, the Cauchy–Riemann equations tell us what its directional derivatives must be. Moving horizontally, v must change at a rate equal to minus the vertical derivative of u. Moving vertically, v must change at a rate equal to the horizontal derivative of u.

Now imagine walking from a starting point to another point along a path. If we integrate those prescribed rates along the path, we obtain a candidate change in v. But is the answer independent of which path we choose? If walking around a closed loop produces a nonzero net change, no single-valued v can exist globally.

Harmonicity gives a compatibility condition. The small change prescribed by moving right then up agrees, to first order, with moving up then right. More formally, the associated differential form is closed because the Laplacian of u is zero. On a simply connected planar domain, closed forms of this kind have zero integral around every closed loop, so they have globally defined potentials. That potential is v.

For the saddle u equal to x squared minus y squared, the prescription says v must change horizontally at twice y and vertically at twice x. The function two x y works. The resulting holomorphic function is z squared. We have not guessed the partner; we have integrated the derivatives demanded by complex differentiability.

Two harmonic conjugates of the same u differ by a constant on a connected domain. That is because their difference has zero horizontal and vertical derivatives. So the missing imaginary part is determined, apart from one arbitrary vertical shift in the output plane.

## A hole that obstructs the construction

Take the function given by the natural logarithm of the distance from the origin. It is defined everywhere in the plane except at the origin. If you compute its Laplacian away from that missing point, it is zero. Thus this is a harmonic function on the punctured plane.

Locally, its harmonic conjugate is an angle: the argument of the complex number. In a small region that does not wrap around zero, we can choose a continuous angle and form a local holomorphic logarithm. But follow a closed circle around the origin. The angle increases by one full turn, or two pi radians, even though we return to the same input point. The candidate imaginary part has not returned to its original value.

This is why there is no globally single-valued harmonic conjugate for the logarithm of the distance on the punctured plane. The function u itself is perfectly single-valued, continuous, and harmonic. What fails is the ability to attach a globally consistent imaginary coordinate. The obstruction comes from a loop circling a missing point, not from a failure of the Laplace equation.

This example makes a broader principle concrete: a local differential condition controls infinitesimal behavior, while a global potential also depends on the topology of the domain. Simply connected domains have no essential holes for the relevant closed-loop integrals. Multiply connected domains may have nonzero periods, which must be checked before claiming a global conjugate.

## The mean-value property: exact balance on circles

Return to a disk and forget the puncture for a moment. A harmonic function on a neighborhood of a closed disk has a local harmonic conjugate there, so on that disk it is the real part of a holomorphic function. Apply Cauchy's integral formula at the center and take real parts. The value of u at the center equals the arithmetic average of u around the circle.

That is the mean-value property. It is not a rough approximation that becomes accurate as the radius shrinks. It is an exact equality for every sufficiently small circle contained in the harmonic domain.

Test it on our saddle. Around a circle centered at the origin, x squared minus y squared alternates between positive and negative values. Its average is zero, exactly the center value. Around a circle centered at some other point, the average reproduces the value at that new center as well. The cancellation of the second derivatives is reflected in exact angular averaging.

An arbitrary continuous function does not have this property. Consider the squared distance from the origin. Its value at the center is zero, but its value along a circle of radius one is always one. The average is one, not zero. Its Laplacian is positive rather than zero. The function is subharmonic, not harmonic, and it allows an interior minimum.

A converse is available under suitable regularity: a continuous real-valued function that satisfies the circle mean-value property for every sufficiently small disk is harmonic. We do not have to assume second derivatives at the start. The averaging law itself forces the smooth behavior expressed by the Laplace equation.

## Why the largest and smallest values live on the boundary

The mean-value property also proves the maximum and minimum principles. Suppose a harmonic function u achieves a local maximum at an interior point. On a small surrounding circle, every value is at most the center value. But their average equals the center value. The only way all those inequalities can average to equality is for the circle values all to equal the center value. That makes the function locally constant, and the corresponding uniqueness principle extends constancy throughout a connected domain.

In particular, if a harmonic function is continuous on the closure of a bounded domain, then its largest and smallest values are attained on the boundary, unless the function is constant, in which case they are attained everywhere. The argument requires compactness to know that extrema are attained, and connectedness for the strong local statement.

This has an immediate consequence for boundary-value problems. Suppose two harmonic functions have the same continuous boundary values on a bounded domain. Subtract them. The difference is harmonic and is zero on the boundary. Its maximum is at most zero and its minimum at least zero. Therefore it is zero everywhere. The two solutions are identical.

That proves uniqueness *if a solution exists*. It does not by itself prove existence on every geometrically complicated region or for arbitrary boundary data. To construct a solution, we need another idea.

## The disk's boundary tells us the entire interior

For the unit disk, there is an explicit solution formula: the Poisson integral. Think of it as a weighted average of the temperature values around the boundary circle. At the very center, the weights are all equal, so we recover the ordinary average. Away from the center, the weights give greater influence to nearby boundary points, but remain positive and still add up to one.

For example, prescribe boundary temperatures that follow a cosine of twice the boundary angle. The harmonic extension inside the disk is the square of the distance to the center times the cosine of twice the interior angle. In Cartesian coordinates, it is x squared minus y squared. At the rim it matches the prescribed temperatures; at the center it is zero; inside it smoothly interpolates without inventing a new high or low beyond the boundary extremes.

The appearance of the square is not arbitrary. The two-angle oscillation is a second angular harmonic. In general, a cosine wave with frequency n on the boundary extends inward with a radial factor equal to the distance raised to the n-th power. High-frequency fluctuations along the boundary fade rapidly as we move toward the center. This is a concrete form of smoothing: the interior is much less sensitive to fine boundary oscillations than points close to the edge.

This same mechanism explains why harmonic functions are so regular. Their values are determined by an averaging process with a smooth kernel. Under appropriate boundary hypotheses, the Poisson formula yields the unique harmonic function continuous up to the closed disk with prescribed continuous boundary data.

## One pair of coordinates, two geometries

When u and v are harmonic conjugates, their level curves have a remarkable relationship. Away from points where their gradients vanish, a curve along which u is constant meets a curve along which v is constant at a right angle. The Cauchy–Riemann equations rotate the gradient of one function by a quarter turn to give the gradient of the other.

For z squared, the level curves of x squared minus y squared are families of hyperbolas, while level curves of two x y are a transverse family. The curves are perpendicular wherever the derivative is nonzero. For fluid flow or electrostatic potential, this is why analytic functions can encode a potential and its stream function simultaneously, at least locally and under suitable modeling assumptions.

The qualification about nonzero gradients matters. At a critical point, the level curves may cross or branch, and there may be no unique tangent direction to compare. Orthogonality is a local regular-point statement, not a promise about every point in a drawing.

## The balance law and its limits

A harmonic function is not simply a nice smooth function. It satisfies an exact local balance law, which then forces boundary control and uniqueness. In a disk, that law goes further: the Poisson kernel reconstructs the entire interior from continuous boundary data. Complex analysis supplies the tools for understanding why this works, through harmonic conjugates and holomorphic averaging.

But the punctured-plane logarithm reminds us that a harmonic function need not be the real part of one globally defined holomorphic function on an arbitrary domain. We can always work locally; globally, we must account for loops and periods. That combination of very strong local structure and genuine global topological obstructions is one of the central themes of analysis.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Harmonicity, conjugates, and periods

A real-valued \(u\in C^2(\Omega)\), \(\Omega\subset\mathbb R^2\) open, is harmonic when
\[\Delta u=u_{xx}+u_{yy}=0.\]
If \(f=u+iv\) is holomorphic, the Cauchy–Riemann equations imply \(\Delta u=\Delta v=0\). Conversely for harmonic \(u\), define
\[\omega=-u_y\,dx+u_x\,dy,\qquad d\omega=(u_{xx}+u_{yy})\,dx\wedge dy=0.\]
Locally \(\omega=dv\); globally on a simply connected domain \(v\) exists (unique up to a real constant on each connected component). On a non-simply connected domain the periods \(\oint_\gamma\omega\) can obstruct global existence.

For \(u=\log|z|=\frac12\log(x^2+y^2)\), \(\omega=(-y\,dx+x\,dy)/(x^2+y^2)\), so \(\oint_{|z|=1}\omega=2\pi\). Thus no single-valued global conjugate on \(\mathbb C\setminus\{0\}\).

### Mean-value and maximum principles

For every closed disk \(\overline{D(a,r)}\subset\Omega\),
\[
u(a)=\frac1{2\pi}\int_0^{2\pi}u(a+re^{it})\,dt.
\]
On a domain, an interior local maximum or minimum forces harmonic \(u\) to be constant. If \(\Omega\) is bounded and \(u\in C(\overline\Omega)\) is harmonic in \(\Omega\), then
\[\min_{\partial\Omega}u\le u(z)\le\max_{\partial\Omega}u\quad(z\in\Omega).\]
Existence of a solution to the Dirichlet problem is not implied by this uniqueness statement.

### Poisson integral for the unit disk

For continuous boundary data \(g:S^1\to\mathbb R\), set
\[
u(re^{i\theta})=\frac1{2\pi}\int_0^{2\pi}
\frac{1-r^2}{1-2r\cos(\theta-t)+r^2}\,g(e^{it})\,dt,\quad 0\le r<1.
\]
Then \(u\) is harmonic in the disk, extends continuously to \(g\) on the closed disk, and is the unique such function. The Poisson kernel is positive with angular integral \(2\pi\).

For \(g(e^{it})=\cos(nt)\) and integer \(n\ge1\), \(u(re^{i\theta})=r^n\cos(n\theta)\). Likewise \(\sin(nt)\) extends to \(r^n\sin(n\theta)\). This makes damping of high angular frequencies explicit.

### Exercises with answers

1. Prove \(u(x,y)=x^3-3xy^2\) is harmonic. **Answer:** \(u_{xx}=6x\), \(u_{yy}=-6x\); it is \(\Re(z^3)\).
2. Find a harmonic conjugate of \(u=x^2-y^2\). **Answer:** \(v=2xy+C\).
3. Can \(u=\log|z|\) have a global harmonic conjugate on \(\{1<|z|<2\}\)? **Answer:** No: the conjugate differential has period \(2\pi\) around any concentric circle.
4. If two harmonic functions on the closed unit disk have the same boundary values, what can be concluded? **Answer:** Their difference vanishes on the boundary and is harmonic inside, so it vanishes everywhere.
5. The unit-circle boundary data are \(g(e^{it})=3+2\cos(3t)\). Find the interior harmonic extension. **Answer:** \(u(re^{i\theta})=3+2r^3\cos(3\theta)\).
6. Are level curves of conjugate harmonic functions perpendicular where both gradients vanish? **Answer:** The usual regular-level-set orthogonality statement does not apply at critical points.

### Sources and further reading

- MIT OCW, *18.112 Functions of a Complex Variable*, Lecture 16: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- Harvard Mathematics 55b complex analysis notes, harmonic functions: https://abel.math.harvard.edu/~ctm/home/text/class/harvard/55b/10/html/home/course/course.pdf.
- IIT Guwahati, *MA547 Complex Analysis*, harmonic conjugates and periods: https://fac.iitg.ac.in/rksri/MA547%20Complex%20Analysis%20lecture%20notes%202025.pdf.
- [Boris Khoruzhenko, Potential Theory (QMUL lecture notes)](https://webspace.maths.qmul.ac.uk/b.khoruzhenko/potential_th_notes.pdf) — Khoruzhenko, Potential Theory, lecture 1: harmonic functions, mean-value and maximum principles.
