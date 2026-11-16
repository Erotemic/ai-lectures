# Intersections, sheaf cohomology, descent, and deformations

<!-- BEGIN SPOKEN LECTURE -->

# Intersections, sheaf cohomology, descent, and deformations

## Local Intersection Multiplicity and Completion

Draw a horizontal line and a parabola that merely touches it at the origin. Both curves pass through the origin. But the encounter is different from two lines crossing there. If we describe intersections only as sets of points, both situations contain one point. Something has been lost. Local intersection multiplicity recovers how strongly the two equations meet.

Take the line defined by y equal to zero and the parabola defined by y equal to x squared. To solve them simultaneously, substitute zero for y. The remaining equation is x squared equals zero. As an ordinary set of solutions, only x equal to zero survives. But the quotient algebra still remembers a nonzero class represented by x, whose square is zero.

That little nilpotent is not a blemish to discard. Its presence says this contact has multiplicity two. Two transverse lines, by comparison, give a quotient in which both local coordinates vanish immediately; the resulting algebra has dimension one over the base field.

### Length as a measure of intersection

Suppose we work over an algebraically closed field and look at two plane curves near an isolated common point P. Localize the polynomial ring at the maximal ideal corresponding to P, then divide by the two defining equations. If the curves have no common local component, the resulting module has finite length. That length is the local intersection multiplicity.

For the line and parabola, after eliminating y the quotient behaves like polynomials in x modulo x squared, with basis one and x. Length two. For the horizontal and vertical axes, the quotient is just the field of constants. Length one. For the line and the curve y equal to x cubed, the same substitution leaves x cubed equal to zero, and the length is three.

What makes this useful is that it is invariant under changes of local coordinates. We did not define multiplicity by judging how flat a picture looks. We counted successive layers of algebra in the local ring. A change of coordinates changes the description but not the module length.

### Tangent directions are only the first test

If two smooth plane curves meet with distinct tangent directions, their first-order equations are independent. Locally, those equations can serve as coordinates, so the intersection multiplicity is one. We call the intersection transverse.

If their tangent directions coincide, the multiplicity is at least two, assuming the intersection remains isolated. Yet tangent agreement alone does not tell us whether the multiplicity is two, three, or more. The higher-order terms decide. This is exactly what happened when we changed x squared to x cubed.

Singularities demand extra care. A cusp described by y squared equal to x cubed meets the line y equal to zero with multiplicity three at the origin. But the cusp itself is not smooth there. One must resist explanations that appeal only to the number or slope of smooth branches. Local length remains meaningful under the proper finite-intersection conditions, including at singular points.

### Why completion is an ally

Near P, many questions depend only on increasingly fine polynomial information around that point. Completion replaces the local polynomial ring by a formal power-series ring. Expressions become infinite series, but finite-length local intersection calculations are preserved. When the quotient is annihilated by a sufficiently high power of the maximal ideal, only a finite jet matters anyway.

For example, the formal power series ring in x and y modulo y and y minus x squared reduces again to the series ring in x modulo x squared. Its basis is one and x. The completion has not altered the answer; it has made the local shape easier to manipulate.

This is not permission to replace all geometry by power series without conditions. Formal expansions encode local information, not the global location of the curve or its entire set of rational points. Completion can illuminate a singularity without determining the global curve on which it sits.

### From a point to a global count

There is a global companion to these local measurements. Two projective plane curves of degrees m and n over an algebraically closed field, with no common irreducible component, have total intersection multiplicity m times n. This is Bézout's theorem. Some intersections may occur at infinity, and tangencies must be counted with their multiplicities.

A line and a parabola have total projective intersection number two. If the line is tangent to the parabola at a single finite point, that single point accounts for both units. A set-theoretic count of one intersection would make the theorem appear false. The local algebra fixes the discrepancy.

We have arrived at an important pattern: a geometric object may look like one point but carry several layers of algebra. The length of a local ring quotient turns those layers into a number. This is how commutative algebra becomes a reliable measuring instrument for geometry.

## Sheaf Cohomology and the Failure of Global Sections to Be Exact

Sometimes every part of a mathematical problem has a solution, but the solutions refuse to agree. On each coordinate chart we can choose the function or section we want. On an overlap the choices differ. We try to correct them, only to find that the corrections themselves cannot be chosen consistently.

Sheaves organize such local data. Cohomology measures the obstructions to patching them into global data. In algebraic geometry it is also the mechanism behind the correction term in Riemann–Roch. To understand that connection, begin with a simple failure of exactness.

A short exact sequence of sheaves says, roughly, that one collection of local sections injects into another and that a third collection is obtained as a quotient. Surjectivity here is a local statement: a section in the quotient may have a lift on every sufficiently small neighborhood. But it may lack a single lift over the entire space.

Take global sections of that exact sequence. Injectivity survives. What fails is the expectation that the final global-section map is necessarily surjective. Local solutions exist, but the lifts disagree on overlaps. This is the precise gap that the first cohomology group records.

### An algebraic example on the projective line

The projective line has two standard affine coordinate charts. On either one, many calculations are easy: modules over the chart's coordinate ring replace abstract sheaf sections. The difficulty lies in compatibility across their overlap, where the coordinate is invertible.

Consider a line bundle whose transition function imposes a negative twist. On each affine chart it is locally just a free rank-one module. Yet the bundle called O of minus two has no nonzero global section. Its first cohomology group, however, is one-dimensional.

We can calculate that dimension explicitly using Laurent polynomials on the overlap. Sections on the two charts provide two families of Laurent terms. After we subtract terms arising from either chart, one Laurent monomial survives as an obstruction. The apparent freedom to work locally has left one globally irreducible mismatch.

This is not pathological behavior. It is the simplest concrete instance of derived global sections. The first cohomology group is not another collection of ordinary global sections; it is the quotient of overlap discrepancies by those discrepancies that can be repaired with local choices.

### From a functor to a sequence of obstructions

The global-section operation is called a left-exact functor. Homological algebra supplies its right derived functors, denoted H zero, H one, H two, and so on. H zero is the familiar space of global sections. Higher groups record increasingly structured failures of gluing.

A short exact sequence of sheaves produces a long exact sequence of cohomology groups. The connecting map takes a global section of the quotient, chooses local lifts, and turns their differences into a first-cohomology class. When that class vanishes, the local lifts can be adjusted to agree globally. When it does not vanish, the proposed global lift does not exist.

On an affine scheme, higher cohomology of quasi-coherent sheaves vanishes. This is one reason affine algebraic geometry behaves so well: the local-to-global obstruction disappears for that class of sheaves. But projective spaces are covered by affine charts without themselves being affine, and the overlap information can survive.

One must keep both qualifications. The vanishing statement concerns quasi-coherent sheaves, not arbitrary sheaves. And a cover by affine charts is not the same as the space itself being affine. The difference is exactly where the gluing problem lives.

### Recovering Riemann–Roch

On a smooth projective curve, cohomology of a line bundle only occurs in degrees zero and one. The difference between their dimensions is its Euler characteristic. For the line bundle associated to a divisor, Riemann–Roch computes that difference as the degree of the divisor plus one minus the genus.

So the dimension of permitted rational functions is not magically corrected by genus. The correction is the dimension of a genuine obstruction space. Serre duality then identifies that space with sections of a complementary line bundle related to differential forms.

This provides a coherent picture. Divisors specify local pole conditions. Line bundles encode how their local descriptions glue. Global sections are actual solutions. First cohomology measures why certain locally conceivable solutions fail to exist. Riemann–Roch balances the two dimensions.

The same derived-functor method extends far beyond curves. On a surface, second cohomology can contribute; on higher-dimensional schemes, still more groups appear. The curve formula is special precisely because there are only two terms to balance.

## Faithfully Flat Descent: Recovering Objects from a Larger Ring

Suppose an equation, a vector bundle, or a module is much easier to study after extending the scalars. We might solve a real equation over the complex numbers, or describe a geometric object on a collection of coordinate charts. But a solution over a larger ring is not automatically a solution over the original one. We must know both which data came from the smaller ring and whether two descriptions agree whenever they refer to the same point.

That is the purpose of descent. It turns the intuitive instruction, “solve locally and glue,” into a precise mathematical theorem. The first surprise is that gluing requires more than matching objects on their own. We must supply a comparison on overlaps, and those comparisons must satisfy a compatibility condition on triple overlaps.

Begin with a familiar example. A complex vector space may be obtained from a real vector space by allowing complex coefficients. But knowing only its complex dimension does not tell us which real vectors were present. One can recover the real vector space when the complex space is equipped with a compatible conjugation operation. A vector is real precisely when conjugation fixes it. An arbitrary complex-linear basis need not be a real basis, but a basis of the fixed vectors produces the original complex space by extending coefficients.

The conjugation is not cosmetic. It is descent data: information that identifies the two ways of regarding an object over the double overlap of the extension. With no such data, an object over the larger field might have several possible origins, and in more complicated settings it might have none.

### What flatness buys us

For a ring map from A to B, extending a module M means forming the tensor product of B with M over A. An especially valuable feature is flatness: short exact sequences of A-modules remain exact after tensoring with B. Kernels and relations therefore behave predictably under this change of scalars.

But flatness alone is not enough. Consider the projection from the product ring k times k onto its first factor. It is flat, but it entirely forgets a module supported on the second factor. Nothing in the image can tell us that the missing component ever existed.

Faithful flatness adds the ability to detect whether a module or a map was zero, injective, or surjective by checking after extension. It is flatness with a guarantee that we have not accidentally discarded part of the problem. Ordinary localization is flat, but generally not faithful, because it can kill modules supported where the inverted element vanishes.

A faithfully flat extension is thus an appropriate analogue of a covering family in geometry. Every part of the original object remains visible somewhere after pullback.

### Why overlap data are necessary

Let us imagine that a B-module N is proposed as the extension of some unknown A-module. There are two natural ways to pull N back to the ring formed by tensoring B with itself over A. If N really comes from M, these two pullbacks agree by a canonical isomorphism: they are both ways of describing M after two successive changes of scalars.

For an arbitrary N we must choose such an isomorphism. Then, after extending to three copies of B, there are two routes for comparing the first copy with the third. A valid descent datum demands that the two routes agree. This is the cocycle condition.

Think of three overlapping coordinate charts. Going from chart one to chart three directly must give the same identification as going from chart one to chart two, then chart two to chart three. Without that rule, local choices cannot define a coherent global object.

The faithfully flat descent theorem says that a B-module equipped with compatible descent data comes from an A-module, uniquely up to the appropriate isomorphism. More strongly, morphisms between descended objects can also be recovered. It is an equivalence of categories, not merely an existence theorem for some individual examples.

### A concrete reconstruction over the real numbers

Return to the extension from real scalars to complex scalars. Let the complex vector space be just one complex dimension, with ordinary conjugation as its real structure. The fixed elements are the real numbers. If we extend those fixed elements back to complex coefficients, we recover the original complex line. Conjugation tells us which scalar multiples were already real and which arose only after extension.

With two complex coordinates, ordinary coordinatewise conjugation similarly recovers the real plane. More general compatible conjugate-linear involutions can recover different real subspaces, but after choosing an appropriate basis each is a real form whose scalar extension is the complex space. The involution must square to the identity; an arbitrary conjugate-linear map is not sufficient.

This example also shows the role of a covering group in descent. For a finite Galois extension of fields, compatible actions of the Galois group express the overlap conditions. The familiar language of Galois symmetry becomes a mechanism for reconstructing linear algebra.

### From modules to geometry

For schemes, coordinate rings on charts are replaced by quasi-coherent sheaves. A faithfully flat, quasi-compact covering permits us to specify sheaves upstairs together with isomorphisms on fiber-product overlaps, and then descend them. Vector bundles are locally free sheaves, so their transition functions are examples of the same idea.

The theorem does not say that every kind of geometric object descends under every cover. Different categories require their own descent statements and hypotheses. Nor does it say that a module over a faithfully flat extension has a unique origin without a chosen descent datum. The origin is recovered from the object plus its coherent comparisons.

The value of descent is that it tells us when local computation is logically complete. A calculation in convenient coordinates, or after enlarging the coefficient field, can produce a genuine global theorem if we carry the compatibility information along with it. The larger world makes the problem tractable; descent tells us exactly what belongs to the smaller one.

## Étale Fundamental Groups: The Symmetries of Finite Covers

In ordinary topology, a loop can be lifted to a covering space. Start at one point upstairs, walk around the loop downstairs, and see which point you reach upstairs. That movement permutes the sheets of the covering. The fundamental group organizes all those permutations.

Algebraic geometry has spaces in which paths are a poor language. A spectrum of a field, viewed with its Zariski topology, consists of only one point. Yet it may have many nontrivial finite field extensions. Each finite separable extension carries information invisible to the ordinary point-set topology.

Grothendieck's étale fundamental group answers a striking question: can we recover a version of the fundamental group from finite algebraic covers alone? The answer is yes, if we choose the right class of covers and remember how their fibers fit together.

### Which covers count?

A finite étale morphism is a finite algebraic map that is locally free of finite rank and has no infinitesimal branching. Over a field, its coordinate algebra is a finite product of finite separable field extensions. This gives a useful guide: étale means separable, in a geometric form; finite means there are only finitely many sheets.

Consider the map from the multiplicative line to itself which raises a nonzero coordinate to its n-th power. If the characteristic of the base field does not divide n, this is a finite étale cover of degree n. Every nonzero point has n distinct geometric preimages. The same formula on the full affine line is ramified at zero. Restricting the base to nonzero coordinates removes that branching point.

If the characteristic divides n, the derivative of the n-th power vanishes identically, so that same map is not étale. Counting geometric preimages without checking separability can therefore give the wrong answer.

### A base point that carries algebraic information

To talk about a fiber, choose a geometric point: a map from the spectrum of a separably closed field into the scheme. For every finite étale cover Y of a connected scheme X, take the finite set of points of Y lying above that geometric point. Doing this for every cover defines a fiber functor from finite étale covers to finite sets.

An automorphism of the fiber functor is not a permutation chosen independently for each cover. It is a compatible family of permutations that respects every map between covers. This compatibility is severe enough to determine a group, the étale fundamental group of X. It comes with the structure of a profinite group: an inverse limit of finite groups.

The key theorem says that finite étale covers of X are equivalent to finite sets equipped with a continuous action of this profinite group. Connected covers correspond to transitive actions. In this algebraic setting, the group is determined by the way all finite covers can be compared, rather than by explicit continuous loops.

### The field with one point but many covers

Let X be the spectrum of the real numbers, and take the geometric point defined by the complex numbers. Every finite étale real algebra is built from copies of the real and complex fields. The compatible permutations of fibers form the absolute Galois group of the real numbers, which has two elements: identity and complex conjugation.

So the usual topological space with a single point has trivial ordinary fundamental group, while its étale fundamental group has two elements. That is not a contradiction. The two constructions measure different classes of covers.

Over a finite field with q elements, every finite extension is again a finite field, and the Frobenius map raises an element to its q-th power. Powers of Frobenius govern all finite Galois extensions. The absolute Galois group is the profinite completion of the integers, with Frobenius as a distinguished topological generator. This group contains information about extension fields of every finite degree at once.

Over an algebraically closed field, by contrast, the spectrum of the field has no nontrivial connected finite étale covers. Its étale fundamental group is trivial. The difference among these three point-spaces is arithmetic, not topological.

### Geometry and arithmetic in one group

When X is a variety over a field that is not algebraically closed, there are two reasons for a cover to be nontrivial. A cover may arise from geometry after extending scalars to an algebraic closure. Or it may arise from the arithmetic of the base field itself. Under the standard geometric-connectedness hypotheses, these aspects form an exact sequence connecting the geometric fundamental group, the arithmetic fundamental group, and the field's absolute Galois group.

The analogy with the classical fundamental group is powerful, but it has limits. The étale group is profinite, so it remembers finite quotients and finite étale covers. It is not simply the ordinary fundamental group with its name changed. For a suitable complex algebraic variety there is a comparison with the profinite completion of the usual fundamental group, not generally with the whole discrete group.

The central lesson is that the collection of covers can be more informative than the collection of points. Galois theory studies symmetries of field extensions. Covering-space theory studies symmetries of sheets. The étale fundamental group places both in one framework, showing that arithmetic can play the role of geometric monodromy.

## Deformation Theory: Tangent Directions and Obstructed Lifts

A geometric object is rarely studied in isolation. We might move the coefficients of an equation, perturb a curve, vary a representation, or deform a vector bundle. But not every conceivable first-order change can actually be carried out. Sometimes a direction of motion exists to first order and then encounters an obstruction at the very next step.

Deformation theory gives this question a common language. Its starting point is deliberately modest. Replace a numerical parameter by something that can register a first derivative without registering a second derivative. Algebraically, introduce a symbol epsilon whose square is zero, but which is not itself zero. The resulting ring is called the ring of dual numbers.

A point whose coordinate lies in this ring can carry a tiny direction. For example, an ordinary point a of the affine line may be replaced by a plus v times epsilon. A polynomial evaluated at this point has only two pieces: its value at a and its derivative at a multiplied by v and epsilon. All higher powers of epsilon vanish. So the condition that a polynomial equation continue to hold is exactly the familiar linearized equation from calculus.

### Tangent vectors from equations

Consider an affine plane curve defined by an equation relating x and y. At a smooth point, the gradient gives one nontrivial linear condition on a pair of infinitesimal velocities. The tangent space is therefore one-dimensional. The point may move along the curve, at least infinitesimally, in the direction perpendicular to the gradient.

Now consider the cusp whose equation is y squared equals x cubed. At the origin, both partial derivatives vanish. Its linearized equation imposes no restriction at all. The Zariski tangent space has two dimensions even though the curve itself has dimension one. This is an algebraic signal of singularity: first-order data overestimates the number of independent directions that come from a smooth nearby motion.

That observation does not say every tangent direction is impossible. It says the first derivative is insufficient to decide. To see a direct failure, it helps to study an even simpler nonreduced scheme.

### A direction that cannot be lifted

Take the equation x squared equals zero. Its only ordinary point over a field has x equal to zero. But over the dual numbers, choosing x equal to epsilon satisfies the equation, because epsilon squared vanishes. We have found a nonzero infinitesimal tangent vector.

Ask whether that first-order solution can be continued one step further. Use a thicker ring in which epsilon cubed is zero but epsilon squared is not. A candidate lift of x equals epsilon must have the form epsilon plus a times epsilon squared. Squaring it produces epsilon squared, which does not vanish in the thicker ring. No choice of a can repair the failure. The first-order motion is obstructed at second order.

This is the central phenomenon. The tangent space describes candidate first-order motions, not a guarantee that each motion integrates to an actual family. Smooth objects have stronger lifting properties. Singular and nonreduced objects can possess tangent vectors that do not extend.

### The role of differentials and the cotangent complex

For an algebra defined by polynomial equations, the module of Kähler differentials packages first derivatives. A derivation is a compatible assignment of infinitesimal changes, and the universal property of differentials turns derivations into module homomorphisms. That is why tangent vectors can be understood as maps out of the cotangent module.

But ordinary differentials alone can forget relations among relations. A better object is the cotangent complex. It remembers not only differentials of generators but also how the equations depend on one another, in the language of homological algebra.

For a problem about lifting a map across a square-zero thickening, the cotangent complex produces an obstruction class in an Ext group. If the class vanishes, lifts may exist, and the collection of lifts is governed by a lower-degree Ext group. For deformation of an entire scheme rather than a given map, the relevant degree shifts. One must specify the deformation problem before naming the obstruction group.

This is a reason homological algebra is so useful in geometry. A relation that appears harmless at first order can reveal itself as a nonzero cohomology class at the next step. The complex records exactly where a hoped-for continuation stops.

### Formal smoothness and its limits

A smooth morphism has the infinitesimal lifting property for square-zero thickenings, locally in the appropriate topology. When one perturbs a point in a smooth space, the first-order choices are not trapped by the kind of obstruction we encountered with x squared equals zero.

But formal lifting and actual convergence are different questions. A sequence of compatible solutions modulo higher and higher powers of a parameter is a formal solution. Turning it into an analytic family can require separate hypotheses, such as convergence or algebraization theorems. Deformation theory carefully distinguishes an infinitesimal calculation from an actual family of points.

The lesson is useful far beyond algebraic geometry. The same pattern appears when studying moduli spaces, representations of groups, or solutions to nonlinear equations: linearize to find possible directions, build higher-order compatibility equations, and identify a precise obstruction when extension fails. The tangent space tells us where change might begin. Obstruction theory tells us which beginnings can continue.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Local Intersection Multiplicity and Completion

**Track:** Abstract Algebra. **Background:** local rings, smooth curves, ideals, lengths of modules, completion. **Central question:** how does algebra distinguish crossing from tangency?

#### Mathematical companion (not spoken)

Let \(k\) be algebraically closed and \(F,G\in k[x,y]\) have an isolated common zero \(P\). Put \(R=\mathcal O_{\mathbf A^2,P}\), the regular local ring of the ambient smooth plane at P. Define
\[I_P(F,G)=\operatorname{length}_R(R/(F,G)).\]
This is finite precisely when the intersection is zero dimensional at P (no common local component). For a finite-length local k-algebra supported at a k-rational P, length equals its k-vector-space dimension. Completion preserves the length:
\[\operatorname{length}_R(R/(F,G))=\operatorname{length}_{\widehat R}(\widehat R/(F,G)\widehat R).\]
Here \(\widehat R\simeq k[[x,y]]\) after translating P to the origin.

**Examples at the origin.** \((y,x)\) yields k, hence multiplicity 1. \((y,y-x^2)=(y,x^2)\) yields \(k[x]/(x^2)\), hence multiplicity 2. \((y,y-x^3)\) yields multiplicity 3. The cusp pair \((y,y^2-x^3)=(y,x^3)\) also has multiplicity 3.

For nonsingular curves with independent linear terms, the Jacobian of (F,G) at P has nonzero determinant, hence \(I_P=1\). In projective plane \(\mathbf P_k^2\), Bézout says \(\sum_P I_P(F,G)=mn\) if homogeneous F,G of degrees m,n have no common component. Count all algebraic intersection points including points at infinity; over non-algebraically-closed fields residue degrees enter the count.

##### Exercises with answers

1. Compute the intersection multiplicity of \(y=x^4\) and \(y=0\) at the origin. **Answer:** 4 from \(k[[x]]/(x^4)\).
2. Compute it for \(y=x\) and \(y=-x\) over characteristic different from two. **Answer:** 1, since their tangent directions are independent; in characteristic two these equations coincide and the intersection is not isolated.
3. Why does taking the radical of \((y,x^3)\) lose information? **Answer:** its radical is \((x,y)\), whose quotient has length one instead of three.
4. A tangent line meets a nonsingular projective conic at a single point over an algebraically closed field. What is the local multiplicity? **Answer:** 2, by Bézout and absence of any other projective intersection.

##### Reading and source notes

- [Stacks Project, Computing intersection multiplicities](https://stacks.math.columbia.edu/tag/0B01), including the local-length calculation.
- [Stacks Project, Algebraic Curves](https://stacks.math.columbia.edu/tag/0BRV), for multiplicities and smooth versus singular curves.

### Sheaf Cohomology and the Failure of Global Sections to Be Exact

**Track:** Abstract Algebra. **Background:** sheaves and quasi-coherent modules, homological algebra, the projective line. **Central question:** how do we measure the failure of locally solvable equations to have global solutions?

#### Mathematical companion (not spoken)

For a sheaf F of O_X-modules, \(\Gamma(X,F)=H^0(X,F)\) is left exact. Its right derived functors are \(R^i\Gamma(X,F)=H^i(X,F)\). From \(0\to F'\to F\to F''\to0\) one obtains
\[0\to H^0(F')\to H^0(F)\to H^0(F'')\xrightarrow{\delta}H^1(F')\to H^1(F)\to\cdots.\]
The connecting homomorphism \(\delta\) measures the obstruction to gluing local lifts. For quasi-coherent F on \(\operatorname{Spec}R\), \(H^i(X,F)=0\) for \(i>0\). This does **not** hold for every sheaf and is not a claim that all spaces covered by affines are acyclic.

**Čech computation on P^1.** Write \(P^1_k=U_0\cup U_1\), with \(U_0\simeq\operatorname{Spec}k[t]\), \(U_1\simeq\operatorname{Spec}k[t^{-1}]\), and overlap \(\operatorname{Spec}k[t,t^{-1}]\). Taking suitable trivializations of O(n), the Čech complex computes
\[h^0(\mathbf P^1,\mathcal O(n))=\max(n+1,0),\quad h^1(\mathbf P^1,\mathcal O(n))=\max(-n-1,0).\]
For O(-2), the quotient of the Laurent overlap sections by both chart images is one-dimensional, represented (in a standard convention) by the class of \(t^{-1}\). For O(-1) both cohomology groups vanish.

**Explicit failure of right exactness:** the standard exact sequence
\[0\longrightarrow\mathcal O(-2)\longrightarrow\mathcal O(-1)^{\oplus2}\xrightarrow{[x\ y]}\mathcal O\longrightarrow0\]
is exact as sheaves on P^1. The map on global sections \(H^0(\mathcal O(-1)^{\oplus2})=0\to H^0(\mathcal O)=k\) is not surjective; its connecting map identifies k with \(H^1(\mathcal O(-2))\). On a smooth projective curve C, \(\chi(O_C(D))=h^0-h^1=\deg D+1-g\).

##### Exercises with answers

1. What is \(h^1(P^1,O(-3))\)? **Answer:** 2.
2. Why can't local surjectivity of sheaves imply surjectivity on global sections? **Answer:** the local lifts may disagree on intersections; the obstruction is the connecting class in first cohomology.
3. Why is the analogous obstruction absent for quasi-coherent sheaves on an affine scheme? **Answer:** higher cohomology vanishes on affines for quasi-coherent sheaves.
4. Compute \(\chi(O_{P^1}(4))\). **Answer:** 5, with \(h^0=5\) and \(h^1=0\).

##### Reading and source notes

- [Stacks Project, Cohomology of quasi-coherent sheaves](https://stacks.math.columbia.edu/tag/03OY), covering affine vanishing and Čech comparisons.
- [Stacks Project, Cohomology and projective twists](https://stacks.math.columbia.edu/tag/0D8P), exercises on O(n) over projective space.
- [Stacks Project, Riemann–Roch](https://stacks.math.columbia.edu/tag/0B5B), Euler characteristics of line bundles on curves.

### Faithfully Flat Descent: Recovering Objects from a Larger Ring

**Track:** Abstract Algebra. **Background:** modules, tensor products, flatness, sheaves and line bundles. **Central question:** when can information computed after a change of rings be recovered without loss?

#### Mathematical companion (not spoken)

For a ring map \(A\to B\), faithful flatness means \(-\otimes_A B\) is exact and faithful. Equivalently it is flat and \(M\otimes_A B=0\Rightarrow M=0\). The projection \(k\times k\to k\) is flat but not faithful: \((0,k)\otimes_{k\times k}k=0\).

A descent datum on a B-module N is a \(B\otimes_A B\)-linear isomorphism
\[\varphi:p_1^*N\xrightarrow{\sim}p_2^*N\]
satisfying \(p_{23}^*\varphi\circ p_{12}^*\varphi=p_{13}^*\varphi\) over \(B\otimes_A B\otimes_A B\). If A→B is faithfully flat, descent data on B-modules form a category equivalent to A-modules. In one standard convention the descended module is the equalizer
\[M=\{n\in N:1\otimes n=\varphi(n\otimes1)\},\qquad B\otimes_A M\simeq N.\]
For a finite Galois field extension L/K with group G, the corresponding data on an L-vector space are a semilinear G-action; the descent module is \(V^G\), and \(L\otimes_K V^G\cong V\).

**Counterexample to a tempting simplification:** the existence of a B-module N is not sufficient descent data. Even for faithfully flat extensions the compatible gluing maps must be supplied. Faithfully flat descent for quasi-coherent sheaves applies to fpqc covers; it does not imply effective descent of all morphism or scheme classes without additional hypotheses.

##### Exercises with answers

1. Show that \(\mathbf C\otimes_{\mathbf R}\mathbf R^2\cong\mathbf C^2\). **Answer:** send \(z\otimes(a,b)\) to \((za,zb)\); conjugation fixes exactly \(\mathbf R^2\).
2. Why is localization \(\mathbf Z\to\mathbf Z[1/2]\) not faithfully flat? **Answer:** it kills the nonzero module \(\mathbf Z/2\mathbf Z\).
3. Describe the cocycle equation for transition matrices \(g_{ij}\). **Answer:** with a consistent convention, \(g_{ij}g_{jk}=g_{ik}\) on triple overlaps.
4. Does a B-module without a chosen gluing datum determine an A-module? **Answer:** not in general; descent is an equivalence between A-modules and *B-modules with descent data*.

##### Reading and source notes

- [Stacks Project, Faithfully flat descent](https://stacks.math.columbia.edu/tag/03O6), the fpqc descent theorem for quasi-coherent sheaves.
- [Stacks Project, Descent for modules](https://stacks.math.columbia.edu/tag/023N), the equivalence of categories and equalizer construction.

### Étale Fundamental Groups: The Symmetries of Finite Covers

**Track:** Abstract Algebra. **Background:** finite fields, Galois groups, étale morphisms, finite group actions, covering spaces. **Central question:** how can algebraic geometry remember loops without ordinary paths?

#### Mathematical companion (not spoken)

For a connected scheme X and geometric point \(\bar x\), the category \(\mathrm{F\acute Et}(X)\) consists of *finite étale* schemes over X. The fiber functor \(F_{\bar x}(Y)=\mathrm{Hom}_X(\bar x,Y)\) yields the profinite group
\[\pi_1^{\acute et}(X,\bar x)=\mathrm{Aut}(F_{\bar x}),\qquad \mathrm{F\acute Et}(X)\simeq\mathrm{FiniteContinuousSets}(\pi_1^{\acute et}).\]
A different geometric base point gives a group isomorphic noncanonically, generally up to inner automorphism.

If \(k\) is a field, \(\pi_1^{\acute et}(\mathrm{Spec}\,k)=\mathrm{Gal}(k^{\mathrm{sep}}/k)\). Thus \(\pi_1^{\acute et}(\mathrm{Spec}\,\mathbf R)=\mathbf Z/2\mathbf Z\), and \(\pi_1^{\acute et}(\mathrm{Spec}\,\mathbf F_q)\simeq\widehat{\mathbf Z}\). For \(\mathrm{char}(k)\nmid n\), the map \(\mathrm{Spec}\,k[t,t^{-1}]\to\mathrm{Spec}\,k[s,s^{-1}]\) with \(s=t^n\) is finite étale of degree n: the algebra has basis \(1,t,\ldots,t^{n-1}\), and \(ns/t\) is invertible at each geometric point after identifying \(s=t^n\).

For a geometrically connected finite-type k-scheme under the usual hypotheses, a geometric base point gives
\[1\to\pi_1^{\acute et}(X_{\bar k},\bar x)\to\pi_1^{\acute et}(X,\bar x)\to\mathrm{Gal}(\bar k/k)\to1.\]
Use the correct separable/algebraic closure conventions for imperfect fields. The comparison to a complex-analytic fundamental group identifies the étale group with a *profinite completion* under appropriate finiteness conditions, not with the full topological group.

##### Exercises with answers

1. Why does \(t\mapsto t^2\) fail to be étale at zero in characteristic zero? **Answer:** its derivative \(2t\) vanishes there, producing branching.
2. What is the étale fundamental group of \(\operatorname{Spec}\mathbf C\)? **Answer:** trivial, because C is algebraically closed.
3. What does connectedness of a finite étale cover imply about its associated finite group action? **Answer:** the action on its geometric fiber is transitive.
4. Why is \(t\mapsto t^p\) not an étale cover in characteristic p? **Answer:** its derivative is zero; the extension is inseparable.

##### Reading and source notes

- [Stacks Project, Fundamental groups](https://stacks.math.columbia.edu/tag/0BQ8), the fiber functor and Galois-category theorem.
- [Stacks Project, Finite étale morphisms](https://stacks.math.columbia.edu/tag/0BL6), the category of finite covers.
- [Stacks Project, Geometric and arithmetic fundamental groups](https://stacks.math.columbia.edu/tag/0BTU), base-field contributions to monodromy.

### Deformation Theory: Tangent Directions and Obstructed Lifts

**Track:** Abstract Algebra. **Background:** affine schemes, polynomial ideals, local rings, Ext, differential forms. **Central question:** which infinitesimal motions of an algebraic solution can be extended to genuine nearby solutions?

#### Mathematical companion (not spoken)

Let k be a field and \(D=k[\epsilon]/(\epsilon^2)\). A map \(k[x_1,\ldots,x_n]/(f_1,\ldots,f_m)\to D\) reducing to a k-point \(a\) is given by \(x_i\mapsto a_i+v_i\epsilon\), with conditions
\[\sum_i(\partial f_j/\partial x_i)(a)v_i=0\quad(j=1,\ldots,m).\]
Hence the Zariski tangent space \(T_aX\) is the kernel of the Jacobian at a, or \(\operatorname{Hom}_k(\mathfrak m_a/\mathfrak m_a^2,k)\) at a rational point.

For the cusp \(X=V(y^2-x^3)\subset\mathbf A^2\), \(T_{(0,0)}X\cong k^2\), since both partial derivatives vanish at the origin. The dimension of X at that point is 1. For \(X=\operatorname{Spec}k[x]/(x^2)\), the first-order map \(x\mapsto\epsilon\) to D exists. A lift to \(D_2=k[\epsilon]/(\epsilon^3)\) reducing to the same map would have \(x\mapsto\epsilon+a\epsilon^2\), but \((\epsilon+a\epsilon^2)^2=\epsilon^2\ne0\). Thus this particular first-order map is obstructed.

**Different problems, different Ext degrees.** For lifting a morphism across a square-zero thickening, the obstruction is of the form \(\mathrm{Ext}^1(f^*L_{X/S},I)\), and choices of lifts (if nonempty) are governed by \(\mathrm{Ext}^0\). For deformations of the space X itself with fixed ideal I and compatible base data, obstructions can lie in \(\mathrm{Ext}^2(L_{X/S},I)\), isomorphism classes of deformations in \(\mathrm{Ext}^1\), automorphisms in \(\mathrm{Ext}^0\). Hypotheses and deformation functors matter; do not swap these indices without changing the problem.

##### Exercises with answers

1. Compute the tangent space at the origin of \(y-x^2=0\). **Answer:** the linearized equation is \(v_y=0\), so the tangent space has dimension 1.
2. What is the tangent space at the origin of \(x^2+y^2=0\) over a characteristic-zero field? **Answer:** two-dimensional, because the linear part vanishes; this does not imply the scheme has dimension 2.
3. Why does the lift of \(x\mapsto\epsilon\) fail modulo \(\epsilon^3\) for \(x^2=0\)? **Answer:** the coefficient of \(\epsilon^2\) in its square is 1 regardless of the second-order correction.
4. If the first-order tangent calculation succeeds, is a convergent family of solutions guaranteed? **Answer:** no; higher obstructions and analytic convergence are separate issues.

##### Reading and source notes

- [Stacks Project, Deformations of rings](https://stacks.math.columbia.edu/tag/08S3), square-zero extensions and the naive cotangent complex.
- [Stacks Project, Deformations of ring maps and the cotangent complex](https://stacks.math.columbia.edu/tag/08SM), obstruction classes and liftability.
