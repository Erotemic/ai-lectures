# 043000 — Deformation Theory: Tangent Directions and Obstructed Lifts

**Track:** Abstract Algebra. **Background:** affine schemes, polynomial ideals, local rings, Ext, differential forms. **Central question:** which infinitesimal motions of an algebraic solution can be extended to genuine nearby solutions?

<!-- BEGIN SPOKEN LECTURE -->

# Deformation Theory: When an Infinitesimal Solution Will Not Continue

A geometric object is rarely studied in isolation. We might move the coefficients of an equation, perturb a curve, vary a representation, or deform a vector bundle. But not every conceivable first-order change can actually be carried out. Sometimes a direction of motion exists to first order and then encounters an obstruction at the very next step.

Deformation theory gives this question a common language. Its starting point is deliberately modest. Replace a numerical parameter by something that can register a first derivative without registering a second derivative. Algebraically, introduce a symbol epsilon whose square is zero, but which is not itself zero. The resulting ring is called the ring of dual numbers.

A point whose coordinate lies in this ring can carry a tiny direction. For example, an ordinary point a of the affine line may be replaced by a plus v times epsilon. A polynomial evaluated at this point has only two pieces: its value at a and its derivative at a multiplied by v and epsilon. All higher powers of epsilon vanish. So the condition that a polynomial equation continue to hold is exactly the familiar linearized equation from calculus.

## Tangent vectors from equations

Consider an affine plane curve defined by an equation relating x and y. At a smooth point, the gradient gives one nontrivial linear condition on a pair of infinitesimal velocities. The tangent space is therefore one-dimensional. The point may move along the curve, at least infinitesimally, in the direction perpendicular to the gradient.

Now consider the cusp whose equation is y squared equals x cubed. At the origin, both partial derivatives vanish. Its linearized equation imposes no restriction at all. The Zariski tangent space has two dimensions even though the curve itself has dimension one. This is an algebraic signal of singularity: first-order data overestimates the number of independent directions that come from a smooth nearby motion.

That observation does not say every tangent direction is impossible. It says the first derivative is insufficient to decide. To see a direct failure, it helps to study an even simpler nonreduced scheme.

## A direction that cannot be lifted

Take the equation x squared equals zero. Its only ordinary point over a field has x equal to zero. But over the dual numbers, choosing x equal to epsilon satisfies the equation, because epsilon squared vanishes. We have found a nonzero infinitesimal tangent vector.

Ask whether that first-order solution can be continued one step further. Use a thicker ring in which epsilon cubed is zero but epsilon squared is not. A candidate lift of x equals epsilon must have the form epsilon plus a times epsilon squared. Squaring it produces epsilon squared, which does not vanish in the thicker ring. No choice of a can repair the failure. The first-order motion is obstructed at second order.

This is the central phenomenon. The tangent space describes candidate first-order motions, not a guarantee that each motion integrates to an actual family. Smooth objects have stronger lifting properties. Singular and nonreduced objects can possess tangent vectors that do not extend.

## The role of differentials and the cotangent complex

For an algebra defined by polynomial equations, the module of Kähler differentials packages first derivatives. A derivation is a compatible assignment of infinitesimal changes, and the universal property of differentials turns derivations into module homomorphisms. That is why tangent vectors can be understood as maps out of the cotangent module.

But ordinary differentials alone can forget relations among relations. A better object is the cotangent complex. It remembers not only differentials of generators but also how the equations depend on one another, in the language of homological algebra.

For a problem about lifting a map across a square-zero thickening, the cotangent complex produces an obstruction class in an Ext group. If the class vanishes, lifts may exist, and the collection of lifts is governed by a lower-degree Ext group. For deformation of an entire scheme rather than a given map, the relevant degree shifts. One must specify the deformation problem before naming the obstruction group.

This is a reason homological algebra is so useful in geometry. A relation that appears harmless at first order can reveal itself as a nonzero cohomology class at the next step. The complex records exactly where a hoped-for continuation stops.

## Formal smoothness and its limits

A smooth morphism has the infinitesimal lifting property for square-zero thickenings, locally in the appropriate topology. When one perturbs a point in a smooth space, the first-order choices are not trapped by the kind of obstruction we encountered with x squared equals zero.

But formal lifting and actual convergence are different questions. A sequence of compatible solutions modulo higher and higher powers of a parameter is a formal solution. Turning it into an analytic family can require separate hypotheses, such as convergence or algebraization theorems. Deformation theory carefully distinguishes an infinitesimal calculation from an actual family of points.

The lesson is useful far beyond algebraic geometry. The same pattern appears when studying moduli spaces, representations of groups, or solutions to nonlinear equations: linearize to find possible directions, build higher-order compatibility equations, and identify a precise obstruction when extension fails. The tangent space tells us where change might begin. Obstruction theory tells us which beginnings can continue.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Let k be a field and \(D=k[\epsilon]/(\epsilon^2)\). A map \(k[x_1,\ldots,x_n]/(f_1,\ldots,f_m)\to D\) reducing to a k-point \(a\) is given by \(x_i\mapsto a_i+v_i\epsilon\), with conditions
\[\sum_i(\partial f_j/\partial x_i)(a)v_i=0\quad(j=1,\ldots,m).\]
Hence the Zariski tangent space \(T_aX\) is the kernel of the Jacobian at a, or \(\operatorname{Hom}_k(\mathfrak m_a/\mathfrak m_a^2,k)\) at a rational point.

For the cusp \(X=V(y^2-x^3)\subset\mathbf A^2\), \(T_{(0,0)}X\cong k^2\), since both partial derivatives vanish at the origin. The dimension of X at that point is 1. For \(X=\operatorname{Spec}k[x]/(x^2)\), the first-order map \(x\mapsto\epsilon\) to D exists. A lift to \(D_2=k[\epsilon]/(\epsilon^3)\) reducing to the same map would have \(x\mapsto\epsilon+a\epsilon^2\), but \((\epsilon+a\epsilon^2)^2=\epsilon^2\ne0\). Thus this particular first-order map is obstructed.

**Different problems, different Ext degrees.** For lifting a morphism across a square-zero thickening, the obstruction is of the form \(\mathrm{Ext}^1(f^*L_{X/S},I)\), and choices of lifts (if nonempty) are governed by \(\mathrm{Ext}^0\). For deformations of the space X itself with fixed ideal I and compatible base data, obstructions can lie in \(\mathrm{Ext}^2(L_{X/S},I)\), isomorphism classes of deformations in \(\mathrm{Ext}^1\), automorphisms in \(\mathrm{Ext}^0\). Hypotheses and deformation functors matter; do not swap these indices without changing the problem.

### Exercises with answers

1. Compute the tangent space at the origin of \(y-x^2=0\). **Answer:** the linearized equation is \(v_y=0\), so the tangent space has dimension 1.
2. What is the tangent space at the origin of \(x^2+y^2=0\) over a characteristic-zero field? **Answer:** two-dimensional, because the linear part vanishes; this does not imply the scheme has dimension 2.
3. Why does the lift of \(x\mapsto\epsilon\) fail modulo \(\epsilon^3\) for \(x^2=0\)? **Answer:** the coefficient of \(\epsilon^2\) in its square is 1 regardless of the second-order correction.
4. If the first-order tangent calculation succeeds, is a convergent family of solutions guaranteed? **Answer:** no; higher obstructions and analytic convergence are separate issues.

### Reading and source notes

- [Stacks Project, Deformations of rings](https://stacks.math.columbia.edu/tag/08S3), square-zero extensions and the naive cotangent complex.
- [Stacks Project, Deformations of ring maps and the cotangent complex](https://stacks.math.columbia.edu/tag/08SM), obstruction classes and liftability.
