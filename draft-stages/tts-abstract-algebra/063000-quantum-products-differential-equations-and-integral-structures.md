# Quantum products, differential equations, and integral structures

<!-- BEGIN SPOKEN LECTURE -->

# Quantum products, differential equations, and integral structures

## Quantum Cohomology: When Curves Change Multiplication

Ordinary cohomology packages geometric intersections into a multiplication. If two classes represent conditions on a space, their cup product records where those conditions meet. For the complex projective line, there is a degree-two class representing a point. The square of that class vanishes: there is no nonzero cohomology in degree four on a space of real dimension two.

Quantum cohomology changes exactly that multiplication rule. On the projective line the point class, call it H, satisfies H times H equals q rather than zero. The symbol q is a formal record of the degree of a rational curve. The new product contains not only the intersection behavior of static subspaces, but also the contribution of maps from a sphere into the target.

It is worth asking why a count of curves should define an associative multiplication. Ordinary cup products are associative for topological reasons. A curve-counting product could easily fail that basic algebraic law. The answer comes from looking at the moduli space of four marked points on a sphere and how the sphere degenerates into two components.

## Three constraints define a structure constant

Fix a smooth projective target. Consider genus-zero stable maps with three marked points. At each mark, we can demand that its image lie in a cycle representing a cohomology class. If the dimensions match the virtual dimension of the moduli space, the intersection of these conditions gives a number: a three-point Gromov–Witten invariant.

To build a product, pair this three-point count with the Poincaré duality metric. Given two input classes, we define their quantum product by requiring its pairing with a third class to equal the generating series of these invariants, summed over curve degrees and weighted by corresponding formal variables. Degree zero recovers the usual cup product. Positive degrees are the correction terms.

The adjective virtual matters. Stable-map moduli spaces may be singular, have components of unexpected dimension, or contain maps with automorphisms. The intersection number is taken against a virtual fundamental class, not obtained by naively enumerating all parameterized maps. Curves may contribute multiplicities or rational weights. The resulting algebra is a mathematically organized curve count, not always an elementary cardinality.

## The projective line from start to finish

On the projective line there are just two ordinary cohomology generators: the identity and the point class H. In classical cohomology, H squared is zero. To determine its quantum square, pair it with H again. The relevant invariant asks for degree-one maps from a marked sphere to the projective line that send three specified marks to three given points.

A degree-one map is a projective transformation. Once three distinct marked source points and three distinct target points are specified, there is exactly one such transformation, after accounting for the natural equivalence of marked maps. The corresponding genus-zero, degree-one invariant is one. Higher-degree terms cannot contribute to this particular multiplication because the grading rules them out.

Thus H multiplied by H equals q. The full small quantum cohomology ring becomes polynomials in H and q, with the relation H squared equals q, over the chosen coefficient or Novikov ring. Set q to zero and the classical relation returns. Set q to a nonzero value and the algebra changes: at generic q the polynomial H squared minus q factors into two distinct roots over a suitable field extension.

This is a deformation of a ring, not of the underlying topological space. The target is still the projective line. What has changed is the multiplication used to organize its intersection data.

## Why four marked points guarantee associativity

Consider now four cohomology classes and a sphere with four marked points. Different ways of grouping four factors correspond to different boundary degenerations: the sphere can break into two spheres with the first two marks on one component, or with the first and third marks together. Both boundary configurations appear as special points in the moduli space of four-marked genus-zero curves.

These boundary points are rationally equivalent. Pull that equivalence back through the stable-map construction, and use the splitting axiom, which says that a stable map on a nodal curve is built by gluing maps on the two components and pairing their common evaluation class. The two degenerations produce the two orders of multiplication. Their equality is the WDVV equation.

The equality of these gluing expressions makes the quantum product associative. In other words, associativity is not inserted as a hope; it is a theorem forced by the geometry of the boundary of a moduli space.

The WDVV equation also gives nontrivial relations among curve counts. Knowing a small number of invariants and the classical intersection pairing can sometimes determine many others recursively. Quantum cohomology becomes a computational tool rather than only a new definition.

## Formal parameters are not optional decoration

The q variable keeps track of curve degree and preserves a grading. For the projective line, H has cohomological degree two and q has degree four. That makes the equation H squared equals q homogeneous. For targets with several independent effective curve classes, one needs several degree variables or a Novikov completion to manage possibly infinite sums.

There is also a distinction between small and big quantum cohomology. Small quantum cohomology deforms the product using the basic three-point theory. Big quantum cohomology lets an additional cohomology parameter enter, summing invariants with further insertions. The resulting product varies over a parameter space and gives a Frobenius-manifold structure under appropriate assumptions.

One must not treat a formal series automatically as a convergent numerical function. The algebraic product often makes sense formally even when analytic convergence has not been established. Confusing the two obscures the rigor of the construction.

## A ring that stores geometry in its structure constants

The projective line calculation is small enough to memorize but rich enough to contain the idea. Classical multiplication sees intersections of static cycles. Quantum multiplication adds the ways a rational curve can meet those cycles. The geometric degeneration of a four-marked sphere enforces associativity. Degree variables remember how much curve geometry was used.

This is why a single relation, H squared equals q, carries more information than a clever polynomial identity. It is the algebraic shadow of enumerative geometry, and it explains how the geometry of maps can modify the ring we use to study a space.

## Quantum Differential Equations and Mirror Periods

The ordinary cohomology of the complex projective line is very simple. It has a unit and one generator, often called H, representing the class of a point. Multiplying H by itself gives zero because the projective line has no cohomology in degree four. The entire multiplication table fits in a few words.

Now introduce the quantum product. It changes multiplication by counting holomorphic curves. The same symbol H multiplied by itself no longer vanishes. Instead it equals a parameter q, times the unit. This statement sounds strange. Why should multiplying two cohomology classes produce a number that remembers curves?

The parameter q records the degree of a curve. At q equal to zero, contributions from positive-degree curves disappear and we recover ordinary cohomology. At nonzero q, the geometry of maps from the sphere is allowed to correct the multiplication table. For the projective line the correction is as simple as it could be: H times H equals q.

One can view the quantum product as a family of algebras. The structure constants move with q, but associativity survives. That persistence is not automatic from an arbitrary deformation of an algebra. It rests on the gluing properties of moduli spaces of stable maps, encoded in identities among Gromov–Witten invariants.

## From a multiplication matrix to a connection

There is a second object hiding inside the multiplication table. Multiplication by H is a linear operator on the two-dimensional space spanned by the unit and H. If a vector is written as a coefficient of the unit and a coefficient of H, multiplying by H exchanges those components, with a factor of q in one direction.

The matrix has zeroes on its diagonal, q in the upper-right corner, and one in the lower-left. Instead of treating that matrix only as an algebraic operation, we make it the coefficient of a differential equation. Introduce another parameter, commonly called z. The quantum differential equation says that z times q times the derivative with respect to q of a section equals multiplication by H applied to that section.

This is a connection: a rule for transporting vectors as q changes. The connection contains the same quantum-product data, but asks a dynamic question. Given an initial vector, how does it evolve around a path in parameter space? Analytic continuation can have nontrivial monodromy, and solutions can have singular behavior near special values.

The transition is useful because differential equations come with a mature theory: regular and irregular singular points, asymptotic expansions, special functions, and monodromy representations. Enumerative geometry becomes accessible to those tools.

## Eliminate a component on the projective line

Write a section as a times the unit plus b times H. The quantum equation splits into two first-order equations. The derivative of a, with the prescribed q weighting and z factor, equals q times b. The corresponding derivative of b equals a.

Eliminate a. The second equation says a is z times q times the derivative of b. Substituting into the first gives a second-order differential equation. The square of z times the operator q times derivative with respect to q, applied to b, equals q times b.

This is a particularly transparent equation because it has a power-series solution with coefficients that can be computed recursively. Start with b equal to one at q equal to zero, then add a coefficient times q, another times q squared, and so on. At degree d, the weighted second derivative introduces d squared. The recurrence says that the coefficient at degree d is the coefficient at degree d minus one divided by z squared times d squared.

The resulting series has coefficients one divided by z to the power twice d times the square of d factorial. No curve counting appears explicitly in the recurrence, yet the series is determined by the quantum multiplication of the projective line. The factorials are the arithmetic fingerprint of the differential equation.

## Mirror symmetry offers another interpretation

Mirror symmetry predicts, and in many classes of examples proves, that solutions of quantum differential equations can be described using integrals associated with a mirror space or a Landau–Ginzburg potential. Instead of counting holomorphic maps to one space, one integrates an oscillatory expression on another.

For the projective line, a standard mirror potential has the form x plus q divided by x, where x is a nonzero complex coordinate. Integrals of the exponential of that potential divided by z, along suitable cycles with appropriate convergence or formal interpretation, satisfy a related differential equation.

This is not merely a similarity of formulas. Under the correct choice of cycles, normalization, and variables, the hypergeometric solutions from the quantum connection match mirror periods. The coefficients of a generating series of curve counts can therefore be found by solving a differential equation or evaluating a mirror integral. Which side is easier depends on the geometry.

But the word mirror must not conceal assumptions. The construction uses a specified mirror family, a chosen connection, and analytic or formal conventions. The projective line is an especially tractable toric example. One should not assume every variety has an equally elementary potential, or that every period integral counts curves without further identifications.

## A curve-counting identity is not a solution to every geometry problem

The equation knows something powerful and something limited. It knows quantum multiplication by H and its associated flat connection. It does not, by itself, tell us every higher-genus invariant, every derived-category correspondence, or every enumerative number of every target. Those require extra structures and arguments.

Nor does writing the series down automatically prove the enumerative interpretation. For the projective line the quantum ring is known independently, and the resulting power series is an exact consequence. In more involved targets, a mirror theorem identifies a candidate hypergeometric series with the geometric generating function, often after a change of coordinates called the mirror map.

The projective line gives a fully calculable bridge. A cohomology ring is corrected by curves. The corrected multiplication becomes a matrix. The matrix becomes a differential equation. The equation yields a factorial series. Mirror symmetry recovers related series through oscillatory integrals. Each transformation keeps track of the same geometry, but exposes a different kind of structure.

## Quantum Connections, Monodromy, and Stokes Matrices

Ordinary cohomology gives a ring of topological classes. Quantum cohomology modifies that multiplication by counting curves. One might think the story ends once all multiplication tables are known. But a ring that varies with parameters can be regarded as a family, and a family invites us to ask how vectors change as the parameters move.

This leads to the quantum connection. It is a differential equation built from quantum multiplication. Its flat sections record how cohomology classes are transported through the parameter space. Around a closed loop, a flat section need not return unchanged; its transformation is called monodromy. At an irregular singularity, even the asymptotic series used to represent a solution can change when we cross certain rays. These jumps are encoded by Stokes matrices.

We will see all three ideas in the quantum cohomology of the projective line. That example is small enough to calculate by hand, but rich enough to display the distinction between classical monodromy and irregular Stokes behavior.

## The projective line has a two-dimensional cohomology

The complex projective line has a unit class and a degree-two class, conventionally called H. In ordinary cohomology, multiplying H by itself gives zero because there is no degree-four cohomology. Quantum cohomology changes this: multiplying H by H gives a parameter q times the unit. The parameter records a degree-one rational curve contribution.

In the basis consisting of the unit and H, multiplication by H is a two-by-two matrix. It sends the unit to H and sends H to q times the unit. As q changes, this matrix changes. A quantum differential equation asks for a vector-valued function whose logarithmic derivative in q is given, up to a scale z, by this multiplication matrix.

The new variable z has an important role. It controls the semiclassical or asymptotic regime of the connection. Holding q away from zero and letting z approach zero makes the equation rapidly varying. Holding z fixed and moving q around zero instead reveals ordinary local monodromy. Confusing these two limits is a common source of mistaken statements about the singularities.

## A scalar equation hides inside the matrix equation

Write a flat section as a(q) times the unit plus b(q) times H. Quantum multiplication gives two coupled differential equations. The logarithmic derivative of a is proportional to q times b, and the logarithmic derivative of b is proportional to a. Eliminate a. Then b satisfies a second-order scalar equation in which the square of the logarithmic derivative is multiplication by q, with z-squared as the scale.

A power-series solution can be found without any general theory. Suppose b is a sum of coefficients times successive powers of q. Applying the logarithmic derivative twice multiplies the coefficient of q to the d by d squared. Consequently the recurrence says the coefficient at degree d is the preceding coefficient divided by z squared times d squared.

Starting at one, we obtain the series one plus q over z squared plus q squared over four z to the fourth, and so on. In general the coefficient is one divided by the square of d factorial and by z to the power two d. This is a familiar Bessel-type hypergeometric series. Its appearance is not a numerical accident: enumerative curve counting has produced a differential equation whose solutions are special functions.

## Walking once around q equal to zero

At q equal to zero, the scalar equation has a regular singular point with repeated exponent zero. One solution is the power series we just derived. A second linearly independent local solution has a logarithm of q times the first solution plus a regular series.

Move q once counterclockwise around the origin. The ordinary power-series solution returns to itself. The logarithm, however, gains two pi times the imaginary unit. Thus the logarithmic solution is shifted by a constant multiple of the analytic solution. Relative to a suitable basis, the monodromy is unipotent: its diagonal entries are one, and one off-diagonal entry is nonzero.

This is monodromy in the parameter q, and it follows from analytic continuation around a regular singularity. We have not yet encountered a Stokes matrix. The distinction matters because not every nontrivial continuation of a solution is a Stokes phenomenon.

## What changes when z is small

Now keep q nonzero. Quantum multiplication by H has two eigenvalues: plus and minus the square root of q. In the small-z regime, the associated exponential factors have leading behavior involving plus and minus two square roots of q divided by z. They grow or decay at dramatically different rates in different angular sectors of the z-plane.

Asymptotic solutions built around these exponentials generally have divergent formal expansions. Within a sector, a suitable analytic solution matches one chosen asymptotic expansion. Rotate the sector across a Stokes ray and the preferred analytic basis may jump by a triangular matrix. That matrix records how exponentially small contributions become visible relative to dominant ones.

The underlying flat connection did not suddenly become discontinuous. Rather, the sectorial bases adapted to asymptotic growth changed. Stokes matrices relate those bases. Their entries depend on the normalization and ordering of the eigenvalue sectors, so quoting a numerical Stokes matrix without specifying conventions is incomplete.

## Why geometry determines analytic data

In the semisimple regime of a Frobenius manifold, quantum multiplication is diagonalizable at a generic parameter value. Its eigenvalues provide local canonical coordinates. The corresponding quantum connection has rich asymptotic structure, with Stokes matrices, central connection matrices, and monodromy data.

In favorable geometric examples, those analytic invariants can be related to intersection pairings and derived-category data. Such correspondences are powerful, but they require hypotheses, choices of exceptional collections, and normalization conventions. It would be wrong to claim that every quantum cohomology ring automatically carries the same fixed Stokes matrix.

The projective line makes the principle concrete. A relation in a tiny quantum ring leads to a Bessel-type differential equation. Its logarithmic solution creates unipotent monodromy around a parameter singularity. Its distinct small-z exponential scales create Stokes jumps. Thus the same multiplication law has algebraic, topological, and asymptotic interpretations.

## What a connection knows beyond a ring

A ring gives rules for multiplying elements at a specified parameter. A flat connection gives a rule for transporting them, for comparing solutions along paths, and for extracting global analytic information from local equations. Once curve counts enter quantum multiplication, those counts control differential equations, and the differential equations generate monodromy and Stokes data.

This provides one of the cleanest examples of a theme running through modern geometry: enumerative information can be translated into differential equations, and the singularities of those equations can reveal structure not visible from a single multiplication table.

## Gamma Classes and Integral Structures in Quantum Cohomology

A quantum differential equation is usually written over the complex numbers. Its solutions form a complex vector space, and analytic continuation moves those solutions around as parameters vary. But a complex vector space does not single out which linear combinations should count as integral. Two bases related by an arbitrary invertible complex matrix look equally legitimate from the differential equation alone.

Geometry often supplies more structure. An algebraic variety has vector bundles and coherent sheaves, and their K-theory classes form a lattice. Quantum cohomology, meanwhile, uses enumerative geometry to deform ordinary cup products. The question is whether K-theoretic information can be transported into the solution space of the quantum connection in a natural way.

The Gamma class is part of the answer. It modifies the more familiar characteristic classes through Euler's Gamma function. In suitable settings, this correction helps define an integral structure on the flat sections of a quantum connection. It also clarifies why integral monodromy statements are not automatic just because a differential equation came from algebraic geometry.

## Begin with ordinary cohomology of a line

Consider the complex projective line, the space of one-dimensional subspaces of a two-dimensional complex vector space. Its cohomology has a unit class and a class commonly called H, represented by a point in top degree. Multiplying H by itself gives zero in ordinary cohomology, because there is no cohomology in degree four on a complex curve.

Quantum cohomology changes exactly this relation. Curves of positive degree contribute enumerative corrections, and the small quantum product satisfies H multiplied quantumly by H equals a parameter q. We obtain a two-dimensional algebra with relation H squared equals q. When q approaches zero, the classical nilpotent relation returns.

This toy model has enough structure to see the problem. Multiplication by H becomes a q-dependent matrix, and a quantum connection converts that matrix into a differential equation. The solutions carry monodromy and asymptotic data, but the equation itself still does not tell us which flat sections correspond to actual geometric K-theory classes.

## The K-theory lattice is not the cohomology basis

On the projective line, the classes of the structure sheaf and the degree-one line bundle give a natural integral basis of K-theory. Their Chern characters are related to the cohomology basis by exponential expressions. Already this shows that the naive integral lattice spanned by the unit and H is not the same object as the image of K-theory under the Chern character.

The difference grows in higher dimensions. Characteristic classes include rational coefficients, and the quantum connection introduces additional transcendental constants through its asymptotics. A simple identification of integral K-theory with integer coefficients in the cohomology basis would usually misrepresent the geometry.

What we need is a map that begins with a genuine K-class, applies characteristic-class corrections, and then uses a fundamental solution of the quantum connection to produce a flat section. The exact formula depends on grading and normalization conventions. The important ingredients are a Chern character, a Gamma-class factor, and the quantum connection's fundamental solution.

## Why the Gamma function appears

Euler's Gamma function extends the factorial through complex analysis. It also has a power-series expansion whose coefficients involve Euler's constant and special values of the zeta function. The Gamma class uses this function on the formal Chern roots of the tangent bundle.

For the projective line, the tangent bundle has first Chern class twice H. Since H squared is zero in ordinary cohomology, the Gamma class truncates after the linear term. In a standard convention it is one minus twice Euler's constant times H. This elementary calculation reveals something important: the correction is not an ordinary polynomial with integer coefficients, even in the smallest useful example.

In more dimensions, higher powers of Chern roots survive, and zeta values enter the coefficients. These are not decorative constants. They appear naturally in asymptotic solutions and in comparisons between different geometric descriptions of quantum cohomology. Integral structures built using the Gamma class are meant to respect that analytic information.

## Flatness and monodromy

A connection prescribes how vectors are transported when parameters change. A flat section is a vector-valued function whose covariant derivative vanishes. Continuing a flat section around a loop can return a different section, producing a monodromy transformation.

A complex connection has monodromy matrices in a complex general linear group after choosing a basis. If a geometric integral lattice of flat sections is preserved, the same transformation can be described by an integral matrix in the appropriate lattice basis. The lattice is additional structure; it is not visible from a random complex basis.

The Gamma-class construction gives a candidate bridge between K-theoretic automorphisms and analytic continuation. Under appropriate hypotheses, geometric operations on K-theory correspond to monodromy and Stokes transformations of the quantum connection. But precise integrality and categorical identifications are theorems or conjectures in specified settings, not unrestricted laws for every quantum differential equation.

## Where the derived category enters

Vector bundles are only part of the story. Derived categories organize coherent sheaves and the extensions between them. Their Grothendieck group gives K-theory, while exceptional collections can provide distinguished sets of classes. Quantum differential equations often admit special asymptotic bases, called Stokes bases, when singularities are irregular.

Gamma conjectures relate such analytic bases and asymptotic behavior to geometric and categorical structures for certain classes of varieties. These statements have been established in some important examples and remain conjectural in others. It is essential to distinguish the definition of a Gamma class from the truth of any proposed relationship with a particular exceptional collection.

The projective line gives a useful testing ground. Its derived category has simple line-bundle generators, and its quantum product can be written in a two-dimensional basis. One can calculate characteristic classes explicitly, solve the differential equation, and then examine whether the geometric lattice behaves as expected under continuation.

## A check that keeps conventions straight

The formula for the quantum product uses a coordinate q that measures curve degree. A fundamental solution also involves a parameter often called z, which plays the role of a grading or connection parameter. Different authors place z in different parts of the connection, use inverse fundamental solutions, and include powers of two pi i in the integral structure.

A safe comparison records these conventions before matching matrices. An apparent disagreement in signs, Gamma factors, or transposes can be a convention mismatch rather than a mathematical contradiction. The cohomology ring, K-theory lattice, and solution space are three distinct objects; a map between them must be specified rather than silently assumed.

A strong worked calculation should therefore include four steps: identify the K-class, compute its Chern character, multiply by the specified Gamma class, and then transport through the chosen quantum fundamental solution. Only after that should one ask whether resulting sections generate an integral monodromy-invariant lattice.

## What this construction contributes

The Gamma class places analytic constants into a setting that initially looked purely algebraic. It offers a route from enumerative curve counts to integral structures, asymptotic bases, and categorical symmetries. It also teaches a useful discipline: the complex differential equation is only one layer of the structure.

In the projective-line example, quantum multiplication replaces a nilpotent relation by H squared equals q. K-theory offers an integral basis not identical to the naive cohomology basis. The Gamma class supplies a transcendental correction, and the quantum connection turns corrected characteristic data into flat sections. Understanding how these pieces fit gives more than a formula; it shows how topology, arithmetic, and asymptotic analysis can occupy the same mathematical object.

## Quantum Lefschetz, Hypergeometric Periods, and Gamma Classes

Projective space contains many algebraic curves. Now cut out a hypersurface by setting a homogeneous polynomial equal to zero. Which of those curves lie in the hypersurface, and how many should be counted after allowing curves to degenerate?

Ordinary Lefschetz theorems compare the cohomology of a smooth hypersurface with that of its ambient space. Quantum Lefschetz asks for an analogous comparison of curve-counting invariants. It is much subtler. Curves must carry stable-map data, and the equation defining the hypersurface imposes conditions on sections along each map.

One consequence is a striking hypergeometric expression. The factorial patterns that arise from imposing the hypersurface equation become coefficients of solutions to quantum differential equations. For the quintic threefold in projective four-space, the first such coefficients are one hundred and twenty and one hundred and thirteen thousand four hundred. These numbers are not, by themselves, counts of rational curves. They are period coefficients that must be transformed before extracting enumerative information.

## Why a degree-five equation produces five factors

Take a smooth degree-five hypersurface in projective four-space. Its defining polynomial is a section of the line bundle called O of five. A stable map from a rational curve to projective space pulls that bundle back to a line bundle of degree five times the curve degree.

In a favorable genus-zero situation, imposing that the map land in the hypersurface amounts to the vanishing of the pulled-back defining section. Virtual intersection theory packages this constraint through an Euler class. In torus-equivariant or hypergeometric language, the Euler class introduces a product of factors indexed through five times the curve degree. The ambient projective-space contribution gives denominator factors repeated five times.

This contrast—five times the degree upstairs, five ambient coordinates downstairs—is visible in the quintic I-function. It is the source of the factorial ratios in the simplest coefficient calculation.

## Two coefficients that can be checked by hand

Ignore the cohomology variable for a moment and look only at the scalar hypergeometric period. The coefficient in degree d is the factorial of five d, divided by the fifth power of d factorial.

For degree one, that is five factorial, or one hundred and twenty. For degree two, it is ten factorial divided by two factorial raised to the fifth power, giving one hundred and thirteen thousand four hundred. The resulting series begins with one, then one hundred and twenty times q, then one hundred and thirteen thousand four hundred times q squared.

A power series with such large integer coefficients is not automatically an enumerative generating function. The mirror coordinate is not generally the naive q. A mirror map and a normalization relate the hypergeometric expression to the quantum connection and the actual Gromov–Witten invariants. One must also distinguish primary invariants, descendants, and the integrality transformations that appear when discussing counts of curves.

This is a place where casual exposition easily overclaims. One hundred and twenty is a period coefficient; it is not the number of lines on a generic quintic. The latter is a different, classical enumerative calculation.

## The Gamma class carries a different correction

The quantum connection does not only have formal power-series solutions. One can ask for a preferred integral structure on its solutions, linked to K-theory. Here the Gamma class appears.

For a vector bundle with formal Chern roots, its Gamma class is formed by multiplying values of the Gamma function at one plus each root, with the customary normalization choices understood. This construction mixes characteristic-class information with special values of the Riemann zeta function when expanded in cohomology.

For the quintic threefold, the tangent-bundle exact sequence comes from subtracting the normal bundle O of five from the ambient tangent bundle. In the resulting formal characteristic-class computation, the Gamma class has a ratio with five copies of Gamma at one plus the hyperplane class in the numerator, and Gamma at one plus five times that class in the denominator.

These are two related but distinct stories. Quantum Lefschetz modifies the ambient curve-counting series by the hypersurface constraint. The Gamma class corrects the comparison between quantum flat sections and integral K-theory data. Their coexistence matters in mirror symmetry, but they should not be merged into one unexplained factor.

## A warning about genus and positivity

The cleanest hypergeometric quantum Lefschetz picture concerns genus-zero theories under positivity or convexity assumptions suited to the chosen target and twisting bundle. In higher genus, a naive rule that simply inserts the same Euler factors generally fails. The virtual geometry of maps contains additional obstruction contributions.

Even in genus zero, saying that the I-function equals the J-function without qualification can miss a mirror change of variables and scalar normalization. A rigorous calculation records which twisting and equivariant conventions are used and what transformation identifies the hypergeometric series with the target's quantum data.

This distinction is not pedantic. A wrong identification can produce plausible-looking series with wrong coefficients or wrong enumerative interpretations. The method is powerful precisely because it provides a controlled way to transport information from the ambient space into the hypersurface.

## Three ways to read one formula

The same quintic hypergeometric series can be read geometrically, analytically, and arithmetically. Geometrically, the numerator encodes the hypersurface condition imposed along stable maps. Analytically, the resulting series solves a differential equation coming from periods and quantum connections. Arithmetically, its coefficients are explicit integers with strong divisibility properties.

The Gamma class adds a fourth reading, connecting characteristic classes and special functions to integral structures. None of these readings replaces the others. A good proof tracks the exact object being transported at each step: an Euler class, a cohomology-valued series, a flat section, or a K-theory class.

Quantum Lefschetz is therefore not simply a slogan that hypersurface invariants come from projective space. It is a disciplined method for imposing equations on families of maps while preserving the virtual multiplicities they carry. The hypergeometric products are the visible computational reward for doing that geometry carefully.

## Quantum K-Theory and Difference Connections

In ordinary cohomology, geometric invariants are often obtained by multiplying classes and integrating over a moduli space. K-theory keeps track of vector bundles and coherent sheaves instead. Its pushforward to a point is not an integral of a differential form, but an alternating sum of dimensions of sheaf-cohomology groups: the Euler characteristic.

Quantum K-theory applies this viewpoint to moduli spaces of curves in a target variety. The resulting curve-counting theory has a different mathematical texture from quantum cohomology. Instead of differential equations in the Novikov variables alone, q-difference equations become natural. Shifting a variable by a factor of q plays the role that differentiation plays in many cohomological formulas.

We can see the distinction without building an entire moduli theory. The projective line is simple enough to compute its classical K-ring and to write a hypergeometric difference equation explicitly.

## The classical projective line

Let L be the class of the tautological line bundle of degree negative one on the projective line. In topological or algebraic K-theory, the projective-line ring is generated by L with the relation that one minus L has square zero.

That is not the cohomology relation written with different letters. The generator L is the class of a genuine line bundle, and multiplication is tensor product. To obtain a numerical answer from a sheaf one can take its Euler characteristic. For example, the line bundle of degree d has Euler characteristic d plus one, even when negative d makes its higher cohomology appear.

Consider degree negative two. It has no global sections, but its first cohomology is one-dimensional. So the Euler characteristic is negative one. An alternating cohomological count differs from simply asking how many global sections exist. That negative answer is not a negative dimension; it is a difference of dimensions.

## A generating series with a shift

Now introduce a formal curve-degree variable Q and a parameter q. Define a series whose degree-zero coefficient is one. Its degree-d coefficient is the reciprocal of a product, taken from r equals one through d, of one minus L times q to the r, with every factor squared.

This looks like a combinatorial gadget, but it is a standard K-theoretic hypergeometric expression associated with the projective line. The important feature is the ratio of consecutive coefficients. Multiplying the degree-d coefficient by the square of one minus L times q to the d produces the preceding coefficient.

Define a shift operator T: it replaces Q by q times Q. Acting on the term Q to the d, the shift multiplies it by q to the d. Therefore the operator one minus L times T, squared, acts coefficientwise by exactly the factor appearing in the recurrence.

The degree-zero term disappears because one minus L has square zero in the K-ring. Every positive-degree term becomes the coefficient from one degree earlier. The result is a compact exact equation: applying one minus L times T, squared, to the series gives Q times the original series.

It is a difference equation, not a differential equation. The parameter q acts by changing the argument rather than by infinitesimally varying it. This is the algebraic shape that distinguishes the theory.

## What the elementary identity does and does not prove

Our calculation is an identity of a particular formal hypergeometric series in a suitable completion of the K-ring. It illustrates the difference-operator mechanism and its connection to quantum K-theoretic constructions. By itself it does not prove the full quantum K-theory of the projective line, including all choices of insertions, stability conditions, and descendant conventions.

Likewise, sending q directly to one in the displayed series is not a legitimate derivation of quantum cohomology. Individual factors become singular, and a meaningful limit needs a change of variables, rescaling, or other comparison machinery. The two theories are related, but the relation is mathematical work, not a substitution of the number one.

## Why the difference viewpoint matters

A differential equation evolves through infinitesimal changes. A difference equation evolves by discrete shifts. When geometry is encoded by Euler characteristics of sheaves, the shifted viewpoint naturally arises in generating series of curve counts, flag varieties, and quantum-group constructions.

This also explains the appearance of difference versions of Toda integrable systems in quantum K-theory. The word quantum is being used in more than one subject, so the exact object matters: the quantum refers here to enumerative deformations of a K-theoretic product, not a claim that the projective line has been turned into a laboratory quantum particle.

The small projective-line computation exhibits the entire pattern. A genuine line bundle class satisfies a nilpotent relation. Curve degree becomes a generating variable. Consecutive coefficients are linked by a multiplicative factor. That factor is represented by a shift operator. Geometry has become an equation in finite differences, with cohomology's differential perspective replaced by a richer K-theoretic one.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Quantum Cohomology: When Curves Change Multiplication

**Track:** Abstract Algebra. **Background:** intersection theory, moduli of stable maps, Poincaré duality and Gromov–Witten invariants. **Central question:** how can counting rational curves deform ordinary cohomology into a new ring?

#### Mathematical companion (not spoken)

Let X be smooth projective and work in a suitable Novikov ring. With a homogeneous cohomology basis `{phi_a}` and Poincaré inverse metric `g^{ab}`, define the genus-zero quantum product by
\[
(\alpha * \beta,\gamma)=\sum_{d\in H_2(X)} q^d\langle\alpha,\beta,\gamma\rangle_{0,3,d},\qquad
\alpha*\beta=\sum_{d,a,b}q^d\langle\alpha,\beta,\phi_a\rangle_{0,3,d}g^{ab}\phi_b.
\]
For `X=P^1`, take `1,H` with `int_{P1}H=1`, `H^2=0` classically and `deg H=2`. The only nonzero correction to `H*H` in the small ring is the degree-one invariant `\langle H,H,H\rangle_{0,3,1}=1`. Therefore
\[
QH^*(\mathbf P^1)=\mathbb Q[H,q]/(H^2-q),\qquad \deg(q)=4.
\]
The equation arises from the virtual count of degree-one stable maps, not a literal count of all parameterized rational functions. For general X, WDVV follows from equality of the two boundary divisors in `\overline M_{0,4}` and the splitting axiom. Unrestricted assertions of convergence or integrality are not part of the formal genus-zero construction.

##### Exercises with answers

1. What happens to quantum cohomology of P1 when q is set to zero? **Answer:** the classical ring `Q[H]/(H^2)` is recovered.
2. Why does the multiplication `H*H=q` respect the quantum grading? **Answer:** both sides have degree four.
3. What geometric space supplies the associativity relation? **Answer:** the moduli space of four-marked genus-zero curves and its boundary splitting configurations.
4. Does the number of stable maps necessarily equal the number of embedded curves? **Answer:** no; automorphisms, multiple covers and virtual multiplicities can affect the invariant.

##### Reading and source notes

- [Kontsevich and Manin, Gromov–Witten Classes, Quantum Cohomology, and Enumerative Geometry](https://arxiv.org/abs/hep-th/9402147), the genus-zero product and WDVV framework.
- [Cox and Katz, Mirror Symmetry and Algebraic Geometry](https://bookstore.ams.org/surv-68), examples of the small quantum product and enumerative constructions.
- [Stacks Project, Intersection Theory](https://stacks.math.columbia.edu/download/intersection.pdf), intersection classes and Gysin maps.

### Quantum Differential Equations and Mirror Periods

**Track:** Abstract Algebra. **Background:** cohomology rings, Gromov–Witten invariants, differential equations, and quantum cohomology. **Central question:** why can the multiplication table of a geometric space become a differential equation whose solutions resemble period integrals on another space?

#### Mathematical companion (not spoken)

Small quantum cohomology of `P^1` over a Novikov ring has `QH^*(P^1)=Q[H,q]/(H*H-q)`, with grading `deg H=2`, `deg q=4`. In ordered basis `(1,H)`, multiplication by H is `M_H=[[0,q],[1,0]]`. Let `D=q d/dq`. The quantum connection in one standard sign convention is
\[
 zD\binom{a}{b}=\begin{pmatrix}0&q\\1&0\end{pmatrix}\binom{a}{b},\qquad zDa=qb,\quad zDb=a.
\]
Eliminating a yields `(zD)^2 b= q b`. Setting `b=\sum_{d\ge0}c_d q^d`, `c_0=1`, gives `z^2d^2 c_d=c_{d-1}` and
\[
 b(q,z)=\sum_{d\ge0}\frac{q^d}{z^{2d}(d!)^2}=I_0(2\sqrt q/z).
\]
Here `I_0` is the modified Bessel function of order zero, and this equality is an identity of power series. The other independent solution is logarithmic at q=0. The simple Landau–Ginzburg mirror potential is `W(x)=x+q/x` on `C^*`; the relation to oscillatory integrals depends on cycles, z and sign conventions, and is not merely an arbitrary contour integral.

##### Exercises with answers

1. Compute `H*H*H` in the small quantum ring. **Answer:** `qH` by associativity.
2. What is the coefficient of `q^3` in b when z=1? **Answer:** `1/(3!)^2=1/36`.
3. Why does setting q=0 recover ordinary cohomology? **Answer:** positive-degree curve corrections are suppressed and `H^2=0`.
4. Does the projective-line differential equation determine all higher-genus invariants? **Answer:** no, it encodes a genus-zero small quantum connection and requires additional structures for other enumerative theories.

##### Reading and source notes

- [A. Givental, A mirror theorem for toric complete intersections](https://arxiv.org/abs/alg-geom/9701016), hypergeometric solutions of quantum differential systems and mirror identifications.
- [Alexander Givental, research and tutorial bibliography](https://math.berkeley.edu/~giventh/), quantum cohomology and mirror-period constructions.
- [Givental, Permutation-equivariant quantum K-theory VI: Mirrors](https://arxiv.org/abs/1509.07852), review of cohomological mirrors in the setting of toric varieties.

### Quantum Connections, Monodromy, and Stokes Matrices

**Track:** Abstract Algebra. **Background:** quantum cohomology, differential equations with regular and irregular singularities, and analytic continuation. **Central question:** what extra structure appears when quantum multiplication is treated as a differential equation?

#### Mathematical companion (not spoken)

For `QH^*(P^1)=C[H,q]/(H^2-q)` in basis `(1,H)`, `H*` has matrix
\[
M(q)=\begin{pmatrix}0&q\\1&0\end{pmatrix}.
\]
Using the convention `z D s=M(q)s`, `D=q d/dq` and `s=a(q)1+b(q)H`, we obtain `z D a=q b`, `z D b=a` and hence
\[
 (zD)^2 b=q b,\qquad b_0(q,z)=\sum_{d\ge0}\frac{q^d}{(d!)^2z^{2d}}.
\]
The recurrence is `z^2 d^2 c_d=c_(d-1)`. At q=0 the repeated exponent zero yields a logarithmic second solution, so monodromy around q=0 is unipotent. With q nonzero, the eigenvalues of M are `+sqrt(q)` and `-sqrt(q)`; their WKB exponentials, after integrating `d log(q)`, are locally `exp(+/- 2 sqrt(q)/z)` to leading order. Stokes matrices arise from sectorial asymptotics as `z->0`, not from the mere existence of regular-singular monodromy at q=0.

The sign convention for the connection and direction of analytic continuation changes certain matrices. State conventions before asserting particular Stokes matrix entries.

##### Exercises with answers

1. Find the eigenvalues of multiplication by H. **Answer:** `+sqrt(q)` and `-sqrt(q)`.
2. Compute the coefficient of `q^3` in the normalized power-series solution. **Answer:** `1/(36 z^6)`.
3. What happens to `log(q)` after one positive loop around q=0? **Answer:** it increases by `2*pi*i`.
4. Why is this logarithmic monodromy not itself a Stokes jump? **Answer:** it is analytic continuation around a regular singularity in q, rather than sectorial asymptotic switching in the small-z irregular problem.

##### Reading and source notes

- [Dubrovin, Geometry of 2D Topological Field Theories](https://arxiv.org/abs/hep-th/9407018), Frobenius manifolds, quantum connections, monodromy and Stokes data.
- [Givental, A Mirror Theorem for Toric Complete Intersections](https://arxiv.org/abs/alg-geom/9701016), hypergeometric solutions and enumerative geometry.
- [Givental, Equivariant Gromov-Witten Invariants](https://arxiv.org/abs/alg-geom/9603021), quantum differential equations and asymptotic structure.

### Gamma Classes and Integral Structures in Quantum Cohomology

**Track:** Abstract Algebra. **Background:** characteristic classes, projective varieties, quantum cohomology, and flat connections. **Central question:** how can an enumerative quantum connection remember an integral lattice rather than only a complex vector space?

#### Mathematical companion (not spoken)

For `X=P^1`, write `H in H^2(X,Z)` with `H^2=0` in ordinary cohomology and `c_1(TX)=2H`. Small quantum cohomology has `H*H=q`. Its multiplication operator in basis `(1,H)` is
\[
M_H=\begin{pmatrix}0&q\\1&0\end{pmatrix},\qquad
M_H\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}qb\\a\end{pmatrix},
\quad H*(a+bH)=qb+aH.
\]
under the stated column convention. The Gamma class of the tangent bundle is
\[
\widehat\Gamma_X=\Gamma(1+2H)=1-2\gamma H
\]
using the ordinary cohomology relation `H^2=0` and `Gamma'(1)=-gamma` (Euler's constant). This calculation is independent of which quantum product convention is used.

`K^0(P^1)` has integral generators `[O]` and `[O(1)]`, whose Chern characters are `1` and `1+H`. A Gamma-integral structure involves corrected Chern characters and quantum fundamental solutions, plus normalization/gradation factors that must be specified before making exact monodromy matrix claims. The gamma conjectures and categorical identifications require individual hypotheses and are not general consequences of the definition.

##### Exercises with answers

1. Why does the series for `Gamma(1+2H)` truncate after a linear term on `P^1`? **Answer:** `H^2=0` in ordinary cohomology.
2. What is `ch(O(1))` on `P^1`? **Answer:** `e^H=1+H`.
3. Does `H*H=q` hold in ordinary cup cohomology? **Answer:** no; ordinary `H cup H=0`.
4. Why must a monodromy lattice be specified in addition to a complex connection? **Answer:** arbitrary complex changes of basis do not preserve integrality.

##### Reading and source notes

- [Iritani, Gamma Classes and Quantum Cohomology](https://arxiv.org/abs/2307.15938), modern review of Gamma-integral structures and gamma conjectures.
- [Iritani, Gamma Classes and Quantum Cohomology, ICM chapter](https://ems.press/books/standalone/276/5480), open-access treatment of integral structures and monodromy.

### Quantum Lefschetz, Hypergeometric Periods, and Gamma Classes

**Track:** Abstract Algebra. **Background:** projective hypersurfaces, Gromov–Witten theory, quantum connections, and characteristic classes. **Central question:** how does the curve-counting theory of a hypersurface relate to the ambient projective space?

#### Mathematical companion (not spoken)

For the quintic `X_5 subset P^4`, a conventional genus-zero hypergeometric I-function has the form
\[
I(q,z)=e^{H\log q/z}\sum_{d\ge0}q^d\frac{\prod_{m=1}^{5d}(5H+mz)}{\prod_{m=1}^d(H+mz)^5},
\]
with `H` the ambient hyperplane class restricted to `X_5` and the usual empty-product convention. Setting `H=0,z=1` gives
\[
\Phi(q)=\sum_{d\ge0}\frac{(5d)!}{(d!)^5}q^d=1+120q+113400q^2+\cdots.
\]
The scalar series is **not** a direct curve count; mirror-map and normalization data intervene when matching I- and J-functions. Via `0 -> TX -> TP^4|_X -> O_X(5) -> 0`, the formal Gamma characteristic class is
\[
\widehat\Gamma(TX)=\frac{\Gamma(1+H)^5}{\Gamma(1+5H)}
\]
modulo the standard normalization/convention for Chern roots. Quantum Lefschetz and the Gamma integral structure are related but not identical constructions.

##### Exercises with answers

1. Compute the scalar degree-one coefficient of the quintic period. **Answer:** `5! = 120`.
2. Compute the degree-two coefficient. **Answer:** `10!/(2!)^5=113400`.
3. Why does the degree-five hypersurface impose `5d` in the numerator? **Answer:** the pulled-back normal line bundle has degree `5d` on a degree-`d` genus-zero map.
4. Are scalar I-function coefficients counts of rational curves? **Answer:** Not directly; normalization, mirror coordinates, and enumerative transformations must be specified.

##### Reading and source notes

- [Pandharipande, Rational Curves on Hypersurfaces (after Givental)](https://arxiv.org/abs/math/9806133), genus-zero hypergeometric construction.
- [Fan and Lee, Towards a Quantum Lefschetz Hyperplane Theorem in All Genera](https://doi.org/10.2140/gt.2019.23.493), limits of naive higher-genus transfer.
- [Iritani, Gamma Classes and Quantum Cohomology](https://arxiv.org/abs/2307.15938), quantum integral structures.

### Quantum K-Theory and Difference Connections

**Track:** Abstract Algebra. **Background:** Grothendieck groups, line bundles, quantum cohomology, and generating functions. **Central question:** what changes when curve counting remembers vector bundles rather than only cohomology classes?

#### Mathematical companion (not spoken)

Let `L=[\mathcal O_{\mathbb P^1}(-1)]`, so
\[
K^0(\mathbb P^1)\cong\mathbb Z[L,L^{-1}]/((1-L)^2).
\]
The identity `\chi(\mathbb P^1,\mathcal O(d))=d+1` is the genus-zero Riemann–Roch formula and holds for all integer `d` (for `d=-2`, `H^0=0`, `H^1\cong\mathbb C`, so `\chi=-1`).

Work in `K^0(\mathbb P^1)\otimes\mathbb Q(q)[[Q]]`, where the denominators below are invertible, and define the hypergeometric series
\[
F(Q)=\sum_{d\ge0}\frac{Q^d}{\prod_{r=1}^d(1-Lq^r)^2},\qquad T_qF(Q)=F(qQ).
\]
Writing `F_d=1/\prod_{r=1}^d(1-Lq^r)^2`, for `d\ge1` we have `(1-Lq^d)^2F_d=F_{d-1}`; for `d=0`, `(1-L)^2F_0=0`. Thus
\[
(1-LT_q)^2F(Q)=QF(Q).
\]
This is an exact *formal* identity for the chosen series. It is an example of a quantum-K-type difference equation; identifying a particular normalized J- or I-function requires specifying that convention. The limit `q\to1` cannot be taken naively coefficient by coefficient.

##### Exercises with answers

1. What is the coefficient of `Q` in `F(Q)`? **Answer:** `(1-Lq)^{-2}`.
2. Check the coefficient of `Q^2` after applying `(1-LT_q)^2`. **Answer:** `(1-Lq^2)^2F_2=F_1`.
3. Compute `\chi(\mathbb P^1,\mathcal O(-3))`. **Answer:** `-2`.
4. Why is the equation not simply an ODE in Q? **Answer:** `T_q` replaces `Q` by `qQ` rather than differentiating with respect to Q.

##### Reading and source notes

- [Givental and Lee, Quantum K-theory on Flag Manifolds, Finite-Difference Toda Lattices and Quantum Groups](https://arxiv.org/abs/math/0108105), foundational finite-difference setting.
- [Givental, On the WDVV Equation in Quantum K-Theory](https://arxiv.org/abs/math/0003158), genus-zero quantum K-theoretic structures.
