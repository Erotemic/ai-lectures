# Riemann-Roch from curves to derived pushforwards

<!-- BEGIN SPOKEN LECTURE -->

# Riemann-Roch from curves to derived pushforwards

## Algebraic Curves, Genus, and Riemann–Roch

Suppose you are allowed to build a rational function on a curve, but you must obey a strict rule about its poles. At one point you may allow a pole of order two; at another you forbid poles altogether. How many linearly independent functions meet those constraints?

On the projective line, the answer is almost embarrassingly concrete. Permit a pole of order at most three at infinity and no poles elsewhere. Then every allowable rational function is a polynomial of degree at most three. The functions one, x, x squared, and x cubed form a basis. Four degrees of freedom come directly from the pole allowance, plus a constant.

But most smooth projective curves are not projective lines. A torus-shaped complex algebraic curve, for example, has rational functions that obey subtler restrictions. A prescription for poles might not be realizable by the number of functions suggested by simple counting. Riemann–Roch identifies the precise correction.

### Turning a pole budget into a vector space

Let C be a smooth, projective, connected algebraic curve over an algebraically closed field. Specify a divisor D: finitely many points with integer coefficients. For each nonzero rational function f, count the order of f at each point. A positive order means a zero; a negative order means a pole.

The condition that the divisor of f plus D be effective means that every pole of f is allowed by the budget D. Together with zero, the eligible functions form a vector space, conventionally called L of D. Its dimension is denoted little ell of D.

The degree of D is the sum of its coefficients. It seems plausible that permitting one additional pole order should add one degree of freedom. On the projective line, that intuition works. On an arbitrary curve, it needs a correction depending on the genus, a global invariant describing the curve's topology over the complex numbers and, algebraically, the dimension of a first cohomology group.

### The hidden constraints

There is a special divisor K, called canonical, arising from differential one-forms. A meromorphic differential may have zeros and poles, just as a rational function does. The degree of K is twice the genus minus two.

Riemann–Roch says: the dimension of L of D, minus the dimension of L of K minus D, equals the degree of D plus one minus the genus. The second term is not an arbitrary nuisance. It measures a dual family of constraints. In the language of sheaves, it is the dimension of the first cohomology group of the line bundle associated with D.

Why should a dual space appear? A list of local pole conditions does not guarantee that the locally allowable expressions fit together into a global rational function. The missing functions are measured by a global obstruction. On curves, duality identifies that obstruction with differential forms satisfying a complementary bound.

When D has degree greater than twice the genus minus two, the divisor K minus D has negative degree. A nonzero rational function cannot have an effective divisor of negative degree. The correction therefore vanishes, and the simple answer returns: the space of allowed functions has dimension degree D plus one minus genus.

### Three curves, three kinds of behavior

On the projective line, genus is zero and a canonical divisor has degree minus two. For a divisor consisting of m times the point at infinity, the allowable functions are exactly polynomials of degree at most m, when m is nonnegative. There are m plus one of them. Riemann–Roch reproduces that answer.

On a genus-one curve, the canonical divisor has degree zero. Any divisor of degree one has one independent global section. One degree of allowed pole does not suddenly yield a nonconstant function, because the constant function already uses that dimension. Indeed, a nonconstant rational function with exactly one simple pole on a smooth projective genus-one curve would give a degree-one map to the projective line, forcing the curve itself to be the projective line. That is impossible.

For a curve of genus two, a canonical divisor has degree two. Give a divisor degree five. It exceeds twice the genus minus two, so the correction vanishes and the allowable function space has dimension four. The genus has effectively removed two degrees of freedom relative to the naïve projective-line count.

### What the theorem does and does not count

Riemann–Roch counts dimensions, not individual functions. It also does not say that two divisors of the same degree have identical spaces of functions when the correction term can be nonzero. The exact geometry and divisor class matter in the small-degree range. Nor can one freely carry this curve formula over to higher-dimensional varieties: there, more cohomology groups appear, and a different theory is needed.

The striking part is that one global invariant, genus, and one dual correction govern an enormous collection of local pole problems. Algebraic curves become accessible through linear algebra, yet the formula knows exactly where linear counting alone fails. That is the bridge from divisors to cohomology.

## Surface Riemann–Roch, Intersection Numbers, and Genus

On an algebraic curve, Riemann–Roch relates the degree of a divisor to the dimensions of spaces of sections and their obstructions. It turns a question about global functions into a numerical formula involving degree and genus. What happens if the underlying variety has two dimensions rather than one?

The answer uses intersection theory. On a surface, two divisors can meet in finitely many points, and their intersection number counts those meetings with multiplicities. Where the curve version of Riemann–Roch involves one integer called degree, the surface version involves a quadratic expression in divisor classes. That change is not accidental: a surface has room for divisors to intersect one another.

Imagine a smooth projective surface S and a line bundle associated with a divisor D. We want to know how many independent global sections it admits. The first difficulty is familiar from curves: the global-section dimension does not behave as a simple polynomial in D for every D. Higher cohomology can intervene. The right quantity to compute first is the Euler characteristic, an alternating sum of three cohomology dimensions.

### A quadratic formula

For a smooth projective surface, the surface Riemann–Roch theorem expresses the Euler characteristic of the line bundle associated to D in terms of the intersection of D with D minus the canonical divisor, plus the Euler characteristic of the structure sheaf.

The canonical divisor represents differential two-forms, the top-degree forms on the surface. Its appearance signals that duality and orientation-like structure are woven into the count. Self-intersection of D provides the quadratic term, while intersection with the canonical divisor supplies a linear correction.

There are three cohomology groups to remember: degree zero for global sections, degree one for a first obstruction, and degree two for a further obstruction. The formula concerns their alternating sum. It does not say that the number of global sections alone equals the quadratic expression. That simplification becomes valid only when suitable vanishing theorems or direct computations eliminate the higher terms.

### Plane curves and an exact count

Take the projective plane. Its divisor classes are generated by the class H of a line. Two general lines intersect once, so H has self-intersection one. The canonical divisor is minus three times H, and the Euler characteristic of the structure sheaf is one.

Now choose D equal to d times H. Substitute this into surface Riemann–Roch. The resulting polynomial is one half of d squared plus three d, and then one. It can also be written as the binomial coefficient d plus two choose two.

For nonnegative d this is exactly the number of degree-d homogeneous monomials in three variables. Each such monomial defines a global section of the line bundle O of d. We have recovered an elementary counting result through intersection theory and sheaf cohomology.

For d equal to two, the six sections correspond to the three squares and three mixed products of the projective coordinates. For d equal to three, ten monomials describe cubic plane equations. For negative d, the polynomial remains the Euler characteristic, but it is no longer simply the count of global sections. Higher cohomology restores the equality.

This is a useful check on an abstract theorem. We have both a geometric derivation through divisor intersections and a concrete basis-counting derivation through monomials. They agree on the cases where cohomology vanishing permits the comparison.

### The genus of a smooth plane curve

We can push the example further. Let C be a smooth plane curve of degree d, regarded as a divisor on the projective plane. The adjunction formula relates the canonical divisor of C to the sum of the canonical divisor of the surface and C itself, restricted back to C.

On a curve the degree of the canonical divisor is twice the genus minus two. On the plane, intersections are straightforward. The calculation gives twice the genus minus two equal to d times d minus three. Solving yields genus equal to one half of d minus one times d minus two.

So a smooth line has genus zero, a smooth conic also has genus zero, a smooth cubic has genus one, and a smooth quartic has genus three. This is a strong bridge between an elementary datum—the degree of a defining homogeneous polynomial—and a global topological invariant of the curve.

The word smooth is essential. A singular plane cubic can have a normalization of genus zero even though the smooth cubic formula gives genus one. The formula is computing the arithmetic genus of a plane curve; singularities change the relationship between arithmetic and geometric genus. Intersection multiplicities and the normalization process account for the discrepancy.

### A glimpse of characteristic classes

The more general Hirzebruch–Riemann–Roch theorem packages this numerical information into characteristic classes. One multiplies the Chern character of the line bundle by the Todd class of the tangent bundle, then takes the top-degree part and integrates over the variety. On a surface, expanding that expression gives the familiar quadratic formula.

This links algebraic geometry to differential geometry. Curvature and characteristic classes describe how bundles twist, while sheaf cohomology measures global sections and obstructions. Riemann–Roch is a theorem connecting these two ways of measuring the same object.

The practical lesson is to distinguish what an Euler characteristic tells us from what we really want to count. Intersection theory produces a robust polynomial index. To turn that index into a dimension of actual sections, we must also understand the higher cohomology. That is exactly why geometry, algebra, and homological methods have developed together.

The Riemann-Roch formulas compare alternating dimensions with geometric classes. To organize these comparisons under pushforward, we need an object that retains a whole complex while forgetting an arbitrary choice of resolution.

## Derived Categories and Perfect Complexes on Schemes

In ordinary linear algebra an object is a vector space, and a map is a linear transformation. In homological algebra an object can be a sequence of modules with maps between them. Each map is followed by another, and the composition of consecutive maps is zero. We call this a chain complex. It contains the data of cycles, boundaries, and cohomology, but often much more data than those groups alone reveal.

A simple example comes from multiplication by an integer n. Put a copy of the integers in one position, another copy in the next, and connect them by multiplication by n. When n is nonzero the only cohomology is the integers modulo n in degree zero. The complex is a resolution of that quotient module. It is not the quotient module written in a more complicated font: it is a concrete way to compute operations that are not exact.

Why not simply replace every complex with its cohomology groups? Because those groups do not always determine how the complex interacts with other complexes. Extensions can be encoded in the placement and attachment of pieces. We need a notion of equivalence that forgets irrelevant choices of resolutions but retains information needed for derived operations.

### Quasi-isomorphisms and the derived category

A map of complexes is called a quasi-isomorphism if it induces an isomorphism on every cohomology group. In the derived category we formally allow such maps to be inverted. The point is not that every chain map acquires a literal inverse. Rather, objects are compared by chains of maps whose induced cohomology maps are isomorphisms, and we construct a category in which those comparisons become genuine isomorphisms.

This is why projective resolutions are useful. A module and any projective resolution of it represent the same object of the derived category. We can choose a resolution suited to calculation, without pretending that a particular choice is part of the underlying mathematical object.

What survives the passage to the derived category is more than just a table of cohomology dimensions. For instance, the derived tensor product keeps track of higher Tor groups. Tensoring the two-term resolution of integers modulo n with integers modulo n turns the multiplication-by-n differential into zero. Now there is cohomology in two adjacent degrees. One copy is the ordinary tensor product; the second records Tor. If we had applied ordinary tensor product without resolving, we would have missed that second contribution.

### Cones and exact triangles

In ordinary homological algebra a short exact sequence leads to a long exact sequence in cohomology. The derived category packages this phenomenon using a mapping cone. Given a map from complex A to complex B, its cone measures how far that map is from being an equivalence. A map is a quasi-isomorphism precisely when its cone has zero cohomology.

The cone fits into a distinguished triangle: A goes to B, B goes to the cone, and the cone goes to the shifted complex A. The word triangle does not mean a diagram of three ordinary short exact sequences. It describes a structure with a shift operation and axioms designed to encode long exact cohomology sequences.

One useful mental model is that an ordinary quotient works when a subobject is embedded cleanly, while the mapping cone provides a homological quotient even when the original map is not injective. This analogy is suggestive, not a substitute for the construction.

### Perfect complexes as finite objects

On an affine scheme built from a ring R, a perfect complex is an object equivalent to a bounded complex of finitely generated projective R-modules. The terms can occupy several degrees, but there are only finitely many, and each behaves like a finite vector bundle. On a general scheme, perfection is a local condition: locally, the complex must have a bounded finite-rank vector-bundle resolution.

The adjective perfect signals strong finiteness. Perfect complexes survive derived tensor products well. They have duals and support traces and determinants under appropriate constructions. They provide the correct language for K-theory and for pushforward theorems in algebraic geometry.

It is tempting to claim every coherent sheaf is perfect. That is true on a regular Noetherian scheme, but not in general. On a singular affine scheme a finite module may require an infinite projective resolution. The dual numbers provide a compact example: over the ring of dual numbers, the residue field has a repeating free resolution. It is coherent but not perfect.

This failure tells us that singularities can be detected homologically. A module that looks finite from the outside may have infinite projective complexity when seen over a singular ring.

### Why this is geometry, not bookkeeping

Suppose we study a family of algebraic varieties and a complex of sheaves on that family. Fibers may gain or lose individual cohomology dimensions, while an alternating Euler characteristic remains stable under suitable proper and flat hypotheses. Perfect complexes make this variation manageable. They are the natural input for determinant lines, K-theoretic classes, and derived deformation theory.

The central distinction is between an arbitrary presentation and an invariant object. The derived category discards the choice of resolution but retains the higher interactions that resolutions expose. Perfect complexes then identify the finite objects for which those interactions are especially well controlled. That prepares us to understand why Riemann-Roch theorems and deformation calculations use complexes rather than only vector bundles or dimensions.

## Grothendieck-Riemann-Roch and Pushforwards

Riemann-Roch on a curve predicts an Euler characteristic from degree and genus. On a surface it predicts an Euler characteristic from divisor intersections. Grothendieck-Riemann-Roch puts these calculations into a single statement about maps between spaces. It asks not only how many sections live on a variety, but how a family of geometric objects behaves when we send it to another variety.

Take a proper map from X to Y. A vector bundle on X contains local linear data. When we push it forward along the map, the fibers over points of Y collect the sections that live above them. But ordinary pushforward is not generally exact. Some data moves into higher direct images. This is exactly the setting where derived categories become necessary rather than decorative.

The correct pushforward class is an alternating combination of the higher direct images. In K-theory it is the class of the derived pushforward. A second kind of pushforward acts on geometric cycles and characteristic classes. Grothendieck-Riemann-Roch relates the two, but a correction factor appears.

### Why a correction factor is needed

The Chern character turns a vector bundle into a sum of rational characteristic classes. It behaves well with direct sums and tensor products, so it translates questions about bundles into calculations in a cohomology or Chow ring. One might hope that the Chern character commutes with pushforward without adjustment.

It does not. The discrepancy is measured by the Todd class of the tangent bundle. For a proper morphism between smooth varieties, the theorem says that pushing forward the Chern character multiplied by the Todd class of X gives the Chern character of the K-theoretic pushforward multiplied by the Todd class of Y.

That extra factor is not an arbitrary normalization. Integration along fibers changes dimensions, and the tangent bundles carry information about that change. The Todd class compensates for it. In the formulation using the virtual relative tangent bundle, the correction is the Todd class of the relative tangent data.

The theorem takes place after passing to rational coefficients, because characteristic-class formulas involve denominators. In the general form, one also needs appropriate hypotheses ensuring that the pushforward is defined. We will work with a smooth proper map between smooth quasi-projective varieties over a field, where the familiar formula is available.

### The projective line as a test

Let X be the projective line and Y a point. Choose the line bundle O of d. Its Euler characteristic is the number of independent global sections minus the dimension of the first cohomology group. Grothendieck-Riemann-Roch now says that this alternating dimension is the degree-one component of the Chern character of O of d multiplied by the Todd class of the tangent bundle of the projective line.

Write H for the class of a point. In the Chow ring, H squared is zero. The Chern character of O of d is one plus d times H. The Todd class of the tangent bundle is one plus H, since the tangent bundle has degree two. Multiply and keep the coefficient of H. The answer is d plus one.

For nonnegative d this is the familiar dimension of homogeneous polynomials of degree d in two variables. But the same Euler characteristic formula remains true for negative d. When d is minus two, there are no global sections, while first cohomology has dimension one, so the Euler characteristic is minus one. The calculation and the cohomology agree.

This is an important difference between an index and a count. The theorem computes an alternating sum robustly even when individual cohomology dimensions change.

### Pushforward through a family

Now imagine Y is not a point. Over each y in Y, the fiber X over y may have a space of sections. Some fibers can have more sections than others; higher cohomology can also jump. If the higher direct images are bundles under suitable base-change hypotheses, we can work with their alternating K-theory class. Its Chern character lives on Y. The theorem predicts that class using characteristic data on X and geometric pushforward along the map.

We are not claiming every higher direct image is automatically a vector bundle or that cohomology commutes with every base change. Those conclusions need additional assumptions. The derived pushforward remains the right object even when the naive vector-bundle picture breaks down.

### Where this leads

The result links algebraic geometry to topology and differential geometry. A curvature calculation may represent a characteristic class; an intersection calculation may evaluate that class; an algebraic cohomology calculation may produce the same integer by an alternating sum. Grothendieck-Riemann-Roch explains why these answers belong to the same structure.

Notice how the previous ideas line up. Perfect complexes give finite derived objects. K-theory records their additive classes. The Chern character converts those classes into intersection-theoretic data. The Todd class corrects pushforward. Riemann-Roch is not merely a formula to memorize; it is a compatibility theorem connecting several kinds of mathematical measurement.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Algebraic Curves, Genus, and Riemann–Roch

**Track:** Abstract Algebra. **Background:** smooth projective curves, divisors, line bundles, rational functions. **Central question:** how many independent rational functions can have poles bounded by a divisor?

#### Mathematical companion (not spoken)

Let C/k be a smooth, projective, geometrically connected curve over an algebraically closed field k, of genus g. For D in Div(C), define
\[L(D)=\{0\}\cup\{f\in k(C)^*: \operatorname{div}(f)+D\geq0\},\qquad \ell(D)=\dim_kL(D).\]
If K is a canonical divisor, then **Riemann–Roch** states
\[\ell(D)-\ell(K-D)=\deg D+1-g.\]
By Serre duality, \(\ell(K-D)=h^1(C,\mathcal O_C(D))\), and \(\deg K=2g-2\). For \(\deg D>2g-2\), \(\deg(K-D)<0\), hence \(\ell(K-D)=0\), yielding \(\ell(D)=\deg D+1-g\). For any divisor of negative degree, \(\ell(D)=0\).

**Projective line:** g=0, \(K\sim-2[\infty]\), and \(L(m[\infty])=\operatorname{span}_k\{1,x,\ldots,x^m\}\) for \(m\geq0\), so \(\ell=m+1\). **Genus one:** \(K\sim0\); for any degree-one D, \(\ell(D)=1\). **Genus two:** degree-five D has \(\ell(D)=4\).

**Why genus occurs.** The Euler characteristic of the invertible sheaf satisfies
\[\chi(C,\mathcal O_C(D))=h^0-h^1=\deg D+1-g.\]
This equality follows from the curve version of Riemann–Roch; proving it in general uses tools such as duality and local-to-global cohomology. It is not established merely by counting the poles individually.

##### Exercises with answers

1. Find \(\ell(6[\infty])\) on \(\mathbf P^1\). **Answer:** 7, represented by polynomials of degree at most six.
2. For genus four, what is \(\ell(D)\) when \(\deg D=10\)? **Answer:** 10+1-4=7 because 10>2g-2=6.
3. Can a divisor of degree minus one have a nonzero global section? **Answer:** no, since an effective divisor has nonnegative degree and principal divisors have degree zero.
4. Why is \(\ell(D)\) not generally determined by degree alone? **Answer:** the correction \(\ell(K-D)\) can depend on the divisor class.

##### Reading and source notes

- [Stacks Project, Riemann–Roch](https://stacks.math.columbia.edu/tag/0B5B), including the cohomological formulation.
- [Stacks Project, Algebraic Curves chapter](https://stacks.math.columbia.edu/tag/0BRV), for genus, canonical divisors, and linear series.

### Surface Riemann–Roch, Intersection Numbers, and Genus

**Track:** Abstract Algebra. **Background:** divisors, line bundles, sheaf cohomology, algebraic curves and intersections. **Central question:** how do intersection numbers predict the number of global sections on a surface?

#### Mathematical companion (not spoken)

On a **smooth projective surface** S over an algebraically closed field and a Cartier divisor D,
\[\chi(\mathcal O_S(D))=\sum_{i=0}^2(-1)^i h^i(S,\mathcal O_S(D))=\chi(\mathcal O_S)+\tfrac12D\cdot(D-K_S).\]
This is the surface Riemann–Roch formula (valid in the usual smooth/proper context); \(D\cdot E\) denotes intersection pairing of divisor classes. Riemann–Roch controls \(\chi\), not necessarily \(h^0\).

For \(S=\mathbf P^2_k\), \(H^2=1\), \(K_S=-3H\), \(\chi(\mathcal O)=1\), so for all integers d,
\[\chi(\mathcal O(d))=1+\tfrac12(dH)\cdot((d+3)H)=\tfrac12(d+1)(d+2).\]
For \(d\ge0\), \(h^0(\mathcal O(d))=\binom{d+2}{2}\) and \(h^1=h^2=0\). For \(d=-3\), \(\chi(\mathcal O(-3))=1\), \(h^0=h^1=0\), and \(h^2=1\) by Serre duality: a counterexample to identifying \(\chi\) with \(h^0\) for negative degree.

For a **smooth** plane curve \(C\subset\mathbf P^2\) of degree d, adjunction gives \(K_C=(K_{\mathbf P^2}+C)|_C\), hence
\[2g(C)-2=C\cdot(C+K_{\mathbf P^2})=d(d-3),\qquad g(C)=\frac{(d-1)(d-2)}2.\]
For a singular integral plane curve the same expression gives its arithmetic genus, while the genus of its normalization may be smaller. Hirzebruch–Riemann–Roch states \(\chi(E)=\int_S\mathrm{ch}(E)\mathrm{td}(T_S)\) in an appropriate characteristic-class theory.

##### Exercises with answers

1. Calculate \(h^0(\mathbf P^2,\mathcal O(4))\). **Answer:** \(\binom62=15\).
2. Find the genus of a smooth plane quintic. **Answer:** \((5-1)(5-2)/2=6\).
3. What is \(\chi(\mathbf P^2,\mathcal O(-3))\)? **Answer:** 1, contributed by \(H^2\), not global sections.
4. Why does a nodal or cuspidal cubic not contradict the smooth cubic genus formula? **Answer:** its arithmetic genus is 1, but normalization reduces the geometric genus.

##### Reading and source notes

- [Stacks Project, Riemann–Roch on curves](https://stacks.math.columbia.edu/tag/0B5B), the one-dimensional precursor.
- [Cambridge University Press, Lectures on Kähler Geometry: Chern classes](https://doi.org/10.1017/CBO9780511618666.017), curvature and characteristic classes entering Hirzebruch–Riemann–Roch.
- [Hartshorne, Algebraic Geometry](https://link.springer.com/book/10.1007/978-1-4757-3849-0), intersection theory and surface Riemann–Roch (publisher reference).

### Derived Categories and Perfect Complexes on Schemes

**Track:** Abstract Algebra. **Background:** chain complexes, exact sequences, Tor, projective modules, coherent sheaves. **Central question:** what must we preserve when two complexes give the same cohomology, and which complexes behave like finite-dimensional vector bundles?

#### Mathematical companion (not spoken)

Let a cochain complex have differential `d^i:C^i -> C^{i+1}` with `d^{i+1}d^i=0`, and `H^i(C)=ker(d^i)/im(d^{i-1})`. A quasi-isomorphism induces isomorphisms on all `H^i`. The derived category `D(R)` is obtained from complexes of R-modules by localizing at quasi-isomorphisms. A triangle `A -> B -> Cone(f) -> A[1]` gives a long exact cohomology sequence.

For an integer `n >= 2`, the complex `P^{-1}=Z --n--> P^0=Z` is a projective resolution of `Z/n`. Derived tensoring with `Z/n` yields `P tensor_Z Z/n` with zero differential. Thus
\[
H^0(P\otimes\mathbf Z/n)=\mathbf Z/n,\qquad H^{-1}(P\otimes\mathbf Z/n)=\mathbf Z/n;
\]
under the homological convention these are `Tor_0^Z(Z/n,Z/n)` and `Tor_1^Z(Z/n,Z/n)`. Quasi-isomorphic complexes need not remain quasi-isomorphic after *ordinary* tensoring with a nonflat module; derived tensor corrects that defect.

For a ring R, perfect means quasi-isomorphic to a bounded complex of finitely generated projective modules. For a scheme X, perfect means locally quasi-isomorphic to a bounded complex of finite-rank locally free sheaves. Regular Noetherian schemes have `D^b_coh(X)=Perf(X)`; on singular schemes containment may be strict. For `R=k[epsilon]/(epsilon^2)`, the residue field k has the infinite periodic resolution `... -> R --epsilon--> R --epsilon--> R -> k -> 0`, so k is not perfect as an R-complex.

##### Exercises with answers

1. What does a mapping cone detect? **Answer:** `Cone(f)` is acyclic exactly when f is a quasi-isomorphism.
2. Compute `Tor_1^Z(Z/6,Z/6)`. **Answer:** `Z/6`, using the two-term free resolution and reduction modulo 6.
3. Is every coherent sheaf on a singular Noetherian scheme perfect? **Answer:** no; the residue field over the ring of dual numbers is a counterexample.
4. Why is derived tensor used before reduction modulo n? **Answer:** ordinary tensor can destroy exactness and miss higher Tor groups.

##### Reading and source notes

- [Stacks Project, Perfect complexes](https://stacks.math.columbia.edu/tag/0656), definitions and finite projective resolutions.
- [Stacks Project, Characterizing perfect complexes](https://stacks.math.columbia.edu/tag/07LQ), compact objects and finite construction from R.
- [Stacks Project, Derived categories of schemes](https://stacks.math.columbia.edu/tag/08E0), sheaf-theoretic context.

### Grothendieck-Riemann-Roch and Pushforwards

**Track:** Abstract Algebra. **Background:** Riemann-Roch on curves and surfaces, K-theory, Chern classes, sheaf cohomology. **Central question:** how can pushforward of vector bundles be reconciled with pushforward of geometric cycles?

#### Mathematical companion (not spoken)

For a proper morphism `f:X -> Y` of smooth quasi-projective varieties over a field, with the relevant K-theory pushforward defined,
\[
\operatorname{ch}(f_![E])\operatorname{Td}(T_Y)
=f_*(\operatorname{ch}(E)\operatorname{Td}(T_X))
\quad\text{in }A^*(Y)_\mathbf Q,
\]
where `f_![E]=sum_i (-1)^i [R^if_*E]` in K-theory. A formulation using the virtual relative tangent bundle is `ch(f_!E)=f_*(ch(E) Td(T_f))` with the appropriate projection formula and orientations. Stating `ch(f_!E)=f_* ch(E)` alone is generally false.

For `X=P^1_k`, `H^2=0`, `integral_{P^1} H=1`, `c_1(T_{P^1})=2H`, and `Td(T_{P^1})=1+H`. Also `ch(O(d))=exp(dH)=1+dH`. Therefore
\[
\chi(\mathbf P^1,\mathcal O(d))=\int_{\mathbf P^1}(1+dH)(1+H)=d+1.
\]
For `d=-2`, `H^0=0`, `H^1` has dimension one, so `chi=-1`. Cohomology vanishing, not the GRR formula alone, converts an index into `h^0`.

The compact form presumes compatibility between the cycle-theoretic pushforward and K-theory pushforward; if using general schemes, perfectness, finite Tor dimension, and properness must be handled with the appropriate version of GRR.

##### Exercises with answers

1. Evaluate `chi(P^1,O(3))`. **Answer:** four, because `d+1=4`.
2. Evaluate `chi(P^1,O(-4))`. **Answer:** minus three; it is not a negative dimension of global sections.
3. What is missing from a naive formula that commutes Chern character with pushforward? **Answer:** the Todd-class correction.
4. Why is derived pushforward used? **Answer:** pushforward of sheaves is not exact; higher direct images contribute to the K-theory index.

##### Reading and source notes

- [Stacks Project, Grothendieck-Riemann-Roch](https://stacks.math.columbia.edu/tag/02UO), formula in a smooth proper setting.
- [Grothendieck, SGA 6, Expose 0](https://grothendiecksga.com/read/sga6/en/0.html), intersection-theoretic framework and pushforward.
- [Stacks Project, Perfect complexes](https://stacks.math.columbia.edu/tag/0656), relevant finite derived objects.
