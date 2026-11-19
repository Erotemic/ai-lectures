# Four-manifold invariants, family indices, and genus bounds

<!-- BEGIN SPOKEN LECTURE -->

# Four-manifold invariants, family indices, and genus bounds

## Donaldson Invariants and the Smooth Topology of Four-Manifolds

Two spaces can be homeomorphic yet fail to be diffeomorphic. Homeomorphism preserves topological continuity; diffeomorphism also preserves smooth coordinate changes. In most elementary geometry, we rarely separate these concepts because the standard examples offer one obvious smooth structure.

Four-dimensional manifolds make the distinction impossible to ignore. A topological four-manifold can support smooth structures that are not equivalent by diffeomorphism. Donaldson's gauge theory opened a way to study the difference by using the geometry of connections on bundles.

The starting object is not a combinatorial triangulation. It is a nonlinear differential equation: the anti-self-dual Yang–Mills equation. Its solutions, organized into a moduli space and then integrated against cohomology classes, produce invariants of smooth four-manifolds.

## The instanton equation

Choose an oriented Riemannian four-manifold and a principal bundle with structure group SU two, or an equivalent suitable rank-two bundle description. A connection describes how to differentiate sections. Its curvature is a two-form taking values in a Lie algebra.

In four dimensions, the Hodge star on two-forms squares to the identity. Thus two-forms split into self-dual and anti-self-dual parts. An anti-self-dual connection has zero self-dual curvature component.

This is a first-order nonlinear elliptic equation after fixing gauge appropriately. The solutions have infinite-dimensional descriptions before quotienting by gauge transformations, because one can alter a connection by changes of bundle frame. The moduli space identifies connections related by such transformations.

At an irreducible regular solution, the moduli space behaves locally like a finite-dimensional smooth manifold. The expected dimension comes from the index of an elliptic deformation complex. The dimension formula connects bundle topology to the intersection form of the underlying four-manifold.

## A dimension calculation on a K3 surface

Consider a K3 surface with its standard orientation. It is simply connected and has three independent positive directions in its second cohomology intersection form. For an SU-two bundle with second Chern number k, the expected dimension of the anti-self-dual moduli space is eight times k minus three times one plus the positive Betti number, in the simply connected case.

For k equal to three, that gives twenty-four minus twelve, or twelve. This is an index calculation. It does not mean the moduli space is guaranteed to be nonempty, compact, or smooth for every metric. It tells us the dimension we expect at regular irreducible connections under the stated conditions.

The number twelve can then be paired with cohomology classes from the original four-manifold. A two-dimensional homology class gives a degree-two cohomology class on the instanton moduli space via the so-called mu map. Six such insertions have total cohomological degree twelve. In a suitable compactified and oriented setting, their product can be evaluated to give a number.

This number is not obtained merely by observing that the degrees add up. We still require transversality, compactification, and control of boundary contributions. The dimension check tells us which evaluations can be meaningful.

## Why a moduli integral can be invariant

The anti-self-dual equation uses a Riemannian metric, so the solutions themselves change when the metric changes. How can integrating over their moduli space yield a smooth-topological invariant?

The answer is to consider a family of metrics and the corresponding family of equations. If the moduli spaces fit into an appropriate oriented cobordism and no uncontrolled solutions escape through boundaries, the integrals of closed cohomology classes remain unchanged. Uhlenbeck compactness is central here: curvature can concentrate and form bubbles, so the naive moduli space need not be compact.

Donaldson's construction handles this geometry through careful compactification and dimension arguments. Under standard conditions, including positive Betti number greater than one, the resulting polynomial invariants are independent of generic metric choices. When the positive Betti number equals one, wall-crossing between chambers can occur and must be accounted for separately.

The conditions are essential. One should not simply say that every instanton count on every four-manifold is automatically an invariant.

## The intersection form becomes rigid

The intersection form of a closed oriented four-manifold measures how second-dimensional homology classes intersect. Donaldson's diagonalization theorem shows that the intersection form of a smooth, closed, simply connected, definite four-manifold is equivalent over the integers to a diagonal form with entries all plus one or all minus one, according to orientation.

This is a surprising restriction. Topological four-manifold theory allows definite unimodular forms that cannot be realized by smooth simply connected closed four-manifolds. Gauge-theoretic analysis therefore distinguishes possibilities invisible to a naive classification by homeomorphism alone.

The polynomial invariants go further. They can distinguish certain smooth manifolds that share many ordinary topological invariants. Later Seiberg–Witten theory gave another approach using different gauge equations, often with simpler moduli spaces, but it did not erase the geometric content of instanton theory.

## What the invariant is actually counting

It is tempting to describe Donaldson invariants as literal counts of instantons. Sometimes zero-dimensional moduli spaces do permit signed counts. In positive dimension, however, the construction evaluates cohomology classes on a fundamental cycle of the moduli space. Geometric cycles and cut-down moduli spaces can turn such integrals into signed intersection counts, but only with transversality and orientation in place.

This is a general lesson in moduli theory. A number associated with a space of solutions is not necessarily the cardinality of that space. It is often an intersection number after imposing enough geometric conditions to reach dimension zero.

Gauge theory converts an analytic problem into differential topology through a sequence of ideas: the curvature equation, elliptic index, moduli-space compactification, cohomological insertions, and deformation invariance. Its force comes from the combination. Removing the analytic control breaks the topological conclusion; removing the topology loses the significance of the solutions.

Donaldson invariants are therefore a model of a powerful mathematical strategy: study a space by placing a nonlinear equation on it, then ask what properties of the equation's complete solution space survive all permissible geometric changes.

## A Family Index and Determinant Line by Hand: One Zero, One Twist

The numerical index of an operator is the dimension of its kernel minus the dimension of its cokernel. That number is stable under suitable deformations. But a family can contain topology invisible in this number. We will construct a finite-dimensional model in which every map has numerical index zero, yet the associated virtual bundle and determinant line are nontrivial.

This model is not yet an infinite-dimensional elliptic family. Its advantage is that we can see exactly what a families index and a determinant line are recording before analytic complications enter.

### The parameter space is a sphere

Let the parameter space B be the complex projective line, topologically a two-sphere. Over B, take two complex line bundles. The domain bundle E is trivial. The target bundle F is O of one, the degree-positive line bundle whose first Chern number is one.

At each parameter point b, we want a complex-linear map from the one-dimensional space E at b to the one-dimensional space F at b. Such a family of maps is the same thing as a section of the Hom bundle from E to F. Because E is trivial, that Hom bundle is simply O of one.

Choose a holomorphic section s of O of one with exactly one simple zero. In homogeneous coordinates, a coordinate linear form gives such a section. At a point where s does not vanish, our fiberwise map is multiplication by a nonzero element of a complex line and is therefore an isomorphism. At the one zero, the map is the zero linear map between one-dimensional vector spaces.

### Kernels and cokernels jump together

Away from the zero, the map is invertible. Its kernel and cokernel both have dimension zero. At the zero, both have dimension one. Thus the numerical index is zero for every b, including the singular parameter.

If we tried to form a kernel bundle by collecting the kernels, we would fail: the dimension jumps from zero to one. The same happens to cokernels. This is exactly the difficulty that appears for families of elliptic differential operators when an eigenvalue passes through zero.

Yet the formal difference between the domain bundle and target bundle is meaningful for the entire family. Its K zero class is the trivial line minus O of one. That is the negative of the sphere's reduced K-theory generator. It has rank zero and nonzero first Chern class.

Numerically, the family has zero index everywhere. Topologically, its index class has a nonzero twist. Both statements are true.

### Construct the determinant line

For a single Fredholm map, its determinant line is the top exterior power of the kernel tensor the dual of the top exterior power of the cokernel. For a finite-dimensional map from E to F, this line can be identified canonically with the determinant of E tensor the dual of the determinant of F. Because our E and F are lines, the resulting determinant line over B is E tensor F dual, namely O of minus one.

The first Chern number of this determinant line is minus one. That is already a witness that it is not trivial. Notice that this sign follows from our convention: the determinant line belongs to the virtual bundle E minus F, not F minus E.

There is also a naturally associated determinant *section*, but it lives in the dual determinant line. The determinant of the fiberwise linear map is an element of the line Hom of E to F. Here that dual determinant line is O of one, and its section is precisely s.

This is a point at which conventions matter. If we call the determinant line det kernel tensor det cokernel dual, the map's scalar determinant is naturally a section of the *dual* line. Confusing the line and its dual reverses the first Chern class.

### Count the zero as a Chern number

Our section s of O of one vanishes once, with positive multiplicity, because it is holomorphic and has one simple zero. The zero count represents the first Chern number of O of one, which is plus one. The determinant line defined using kernel minus cokernel is its dual and has Chern number minus one.

Here the algebraic topology of the family has become a count we can draw. The family is invertible except at one parameter, where kernel and cokernel appear together. A local trivialization of the dual determinant line identifies s near that parameter with a complex coordinate. Its argument winds once around the origin on a small loop.

This local winding is the obstruction to extending a nowhere-vanishing determinant section across the sphere. It is exactly the obstruction recorded by the first Chern class.

### What changes for elliptic operators

An elliptic family consists of maps between infinite-dimensional spaces of sections. Its individual kernels and cokernels are finite-dimensional but may jump in dimension. Analytic Fredholm theory allows a finite-dimensional stabilization, and the stable formal difference of the resulting bundles defines an index class in K zero of the parameter space.

The determinant line of this class continues to make sense even as kernel dimensions jump. Under additional analytic structure, such as a family of Dirac operators, one can define metrics and connections on the determinant line. The curvature of suitable natural connections is related to fiber integrals of characteristic forms, as developed by Bismut and Freed following work of Quillen and others.

Our finite-dimensional model does not prove those curvature formulas. It demonstrates the topology that the formulas must respect: an index bundle may have zero rank at every parameter but nonzero first Chern class, and its determinant line remembers that nonzero class.

### The conceptual takeaway

Three pieces of information must not be conflated. A numerical index belongs to one operator. An index *bundle class* belongs to a family and can twist over parameter space. Its determinant line is a one-dimensional shadow of that twisting. A scalar determinant may vanish at singular parameters, while the determinant line remains well defined and nontrivial.

One zero of a section over the sphere gave us all three features in a calculation we can verify. That is the foundation needed before studying determinant bundles of elliptic families, Berry connections, and gauge-theoretic orientation lines.

## Families Index Theory and Determinant Line Bundles

The index of a Fredholm operator is the dimension of its kernel minus the dimension of its cokernel. For a single elliptic operator, the Atiyah–Singer index theorem relates this analytic number to topological characteristic classes.

But differential operators often come in families. Imagine changing a metric, a connection, or a parameter on which a geometric problem depends. The dimension of the kernel can jump at special parameter values. If we tried to assemble the kernels into one vector bundle over the parameter space, the varying dimensions could make that impossible.

The families index theorem resolves this by using a virtual vector bundle. Instead of demanding a kernel bundle and a cokernel bundle separately, it constructs their formal difference in K-theory. That difference can vary continuously in the correct topological sense even when the two dimensions jump together.

## The smallest family has a singular-looking point

Consider the family of linear maps from the real line to itself that multiply by a real parameter t. For every nonzero t, the map is invertible. Its kernel and cokernel both have dimension zero. At t equal to zero, the map is the zero map. Its kernel and cokernel both have dimension one.

If we recorded only the kernel dimension, we would see a sudden jump. Yet the index is zero for every t. The kernel and cokernel jump by the same amount. A virtual difference captures the information that stays stable.

A single constant index is still not the whole families theory. Over a parameter space with nontrivial topology, a family of Fredholm operators can carry a nontrivial K-theory class even if its numerical index is zero at every point. How the operators vary around loops and higher-dimensional cycles contains information that cannot be read from any one operator in isolation.

## The index bundle

For a well-behaved continuous family of Fredholm operators over a compact parameter space, one can choose finite-dimensional auxiliary data that stabilize the family. The resulting virtual bundle class is independent of these choices. It is the index bundle.

The families Atiyah–Singer theorem computes its Chern character using the geometry of the fibers. When the operators are, for example, spin-c Dirac operators along the fibers of a smooth proper family, a fiber-integration formula involves the characteristic class of the vertical tangent bundle and the Chern character of the twisting bundle.

This is a stronger statement than the ordinary index theorem. The ordinary theorem recovers one integer on each connected component of the parameter space. The families theorem can recover cohomology classes of several degrees on the entire base.

The word “families” does not mean merely repeating the ordinary index calculation for many parameter choices. It means retaining the topology of how those choices fit together.

## A determinant line from kernel and cokernel

There is a particularly concrete one-dimensional shadow of the index bundle: the determinant line. At an operator D, form the top exterior power of the kernel and tensor it with the dual of the top exterior power of the cokernel.

At a point where the dimensions jump, this construction may look as though its rank-one factors have changed. Yet through the determinant-line formalism the resulting one-dimensional lines glue into a line bundle over the parameter space.

A line bundle can have nontrivial holonomy or first Chern class. In geometric families, natural metrics and connections on determinant lines allow local curvature formulas. Thus the determinant line packages not only the integer index but also how the family twists over the base.

One should distinguish the determinant line from choosing a nonzero numerical determinant of each operator. Differential operators are infinite dimensional, and eigenvalues can pass through zero. Analytic determinant constructions require regularization and choices; the determinant line is the geometric home in which those constructions live.

## A family of Dolbeault operators

Consider a fixed elliptic curve, now meaning a smooth complex curve of genus one, and degree-zero holomorphic line bundles on it. Each line bundle defines a Dolbeault operator. Its index is the holomorphic Euler characteristic, the dimension of holomorphic sections minus the dimension of the first cohomology group.

For any degree-zero line bundle on this elliptic curve, the index is zero. For a nontrivial degree-zero line bundle, both cohomology groups vanish. For the trivial line bundle, the constant functions give one holomorphic section, and the first cohomology group also has dimension one.

The dimensions therefore jump from zero and zero to one and one. The numerical index stays zero. This is the geometric counterpart of the elementary multiplication-by-t family, with a far richer parameter space: the degree-zero Picard variety of the elliptic curve.

Such families show why it is dangerous to identify the families index with the collection of individual kernels. A stable virtual class survives precisely where a naive vector bundle of kernels fails.

## Curvature and anomalies

Determinant lines also occur in mathematical physics, where phases of fermionic partition functions can behave as sections of a line bundle rather than as globally defined complex numbers. A nontrivial determinant line can obstruct choosing phases consistently around a parameter loop.

The relevant curvature and holonomy are governed by geometric data of a family of Dirac operators. Depending on the problem, this is described by Quillen metrics, Bismut–Freed connections, or related constructions. Those theories require precise analytic assumptions and regularization; a formal infinite product of eigenvalues is not a substitute.

The same mathematics therefore explains an abstract K-theory index, a concrete line-bundle obstruction, and the failure of a naive determinant to be globally single-valued. It is a good example of topology arising not from the space on which one operator acts, but from the whole collection of operators.

## The lesson of a jumping kernel

A kernel jump may signal special geometry: an extra holomorphic section, a zero mode, or a symmetry appearing at one parameter. The jump should not be erased. But it also should not lead us to conclude that no continuous invariant can be built.

Families index theory records exactly the information that remains invariant when dimensions rearrange. The determinant line distills part of it into a bundle whose twisting can be observed geometrically. A single index integer cannot see that twisting; a family K-theory class can.

The important conceptual move is to stop asking for each changing solution space to form an ordinary bundle. Instead, encode the balance between solutions and obstructions. That balance can remain geometrically coherent across the very parameter values where individual dimensions fail to behave continuously.

## Seiberg-Witten Monopoles and Four-Manifolds

Classifying a surface topologically is a tractable problem. Genus tells us much of what we need. Four-dimensional manifolds behave differently. Their topology, differentiable structure, and geometry interact in ways that cannot be reduced to a single Euler characteristic or intersection form.

Gauge theory provided new tools for this difficulty. Donaldson's theory studies connections whose curvature is anti-self-dual. Seiberg–Witten theory instead couples an abelian connection to a spinor, a field that transforms under a spin representation. The equations are nonlinear, but their moduli spaces are often more compact and manageable than the corresponding spaces of nonabelian instantons.

The reward is a numerical invariant that can remain unchanged while one changes the metric used to define the equations. It is then an invariant of the smooth four-manifold together with additional topological data and orientation choices.

## The ingredients of a monopole

Begin with a closed oriented smooth four-manifold. Choose a spin-c structure, which supplies two bundles of spinors, commonly called positive and negative spinors, and a determinant line bundle. A unitary connection on that line bundle defines a Dirac operator taking positive spinors to negative ones.

A Seiberg–Witten solution consists of a connection and a positive spinor obeying two linked equations. First, the Dirac operator annihilates the spinor. Second, the self-dual part of the connection's curvature equals a quadratic expression in the spinor, possibly with a prescribed perturbation.

Why self-duality? In four dimensions the Hodge star splits two-forms into two eigenspaces, positive and negative. That splitting exists for an oriented metric, and it lets the curvature equation select one half of the available two-form data.

Gauge transformations alter the local description of the connection and spinor without altering their physical or geometric class. Thus the object of study is not the raw solution set but the quotient by gauge transformations: a moduli space.

## Counting solutions after understanding dimension

The expected dimension of this moduli space is governed by topological quantities. It uses the square of the first Chern class of the determinant line, the Euler characteristic, and the signature of the four-manifold. When the expected dimension is zero and perturbations produce a regular compact moduli space with no reducible complications, signed counting of solutions can define an integer invariant.

There are several qualifications in that sentence. The count depends on an orientation. Reducible solutions require care. When the dimension of the positive part of second cohomology is one, chamber choices can matter. When it is larger than one, a better metric-independence statement is available under the standard conditions.

This is why Seiberg–Witten invariants are not merely counts of whatever a numerical solver happens to find. They arise after geometric analysis establishes compactness, transversality, and control of the gauge quotient.

## A check on a K3 surface

A K3 surface supplies a useful exact calculation. Its Euler characteristic is twenty-four and its signature is negative sixteen. Twice the Euler characteristic plus three times the signature is forty-eight minus forty-eight, which is zero.

For the spin-c structure with trivial determinant line, the first Chern class is zero. Its square is zero too. Therefore the expected Seiberg–Witten dimension is zero.

That dimension calculation does not alone count the monopoles. But it explains why the corresponding invariant is numerical rather than a higher-degree class. In the standard orientation and appropriate chamber-independent setting, the zero basic class of a K3 surface has a nonzero Seiberg–Witten invariant.

This is a powerful pattern in geometry. A characteristic number predicts how many degrees of freedom a solution space ought to have; analysis turns that prediction into a moduli problem; topology extracts a deformation-invariant answer.

## What the invariant can and cannot distinguish

Seiberg–Witten invariants have proved useful for detecting smooth phenomena invisible to coarser topological data. They yield genus bounds for embedded surfaces and restrictions on the existence of certain geometric structures. Their relationship to symplectic geometry is especially strong through Taubes's results connecting Seiberg–Witten and pseudoholomorphic-curve counts.

Yet the invariant is not a complete classifier of smooth four-manifolds. Different manifolds may have identical Seiberg–Witten data, and vanishing of an invariant does not imply that the manifold is geometrically trivial. The choice of spin-c structure and the hypotheses for metric independence have to be retained.

## A nonlinear route to topology

The surprising step is to use a field equation as a measuring instrument for smooth structure. We choose a metric to write a Dirac equation and a curvature equation. Then, under controlled conditions, the resulting signed count no longer depends on that metric. What began as analytic data becomes a smooth-topological invariant.

Four-dimensional topology is full of such transitions: a connection encodes curvature, a spinor constrains it, the gauge group identifies redundant descriptions, and a moduli space yields an invariant. Seiberg–Witten theory demonstrates that a nonlinear equation can tell us something about the space on which it is posed, rather than merely about a field moving through that space.

## Adjunction Inequalities and Smooth Genus Bounds

Suppose a two-dimensional surface sits smoothly inside a four-dimensional manifold. It determines a homology class. But homology alone does not tell us the genus of the surface. We might represent the same class by surfaces with additional handles, increasing the genus without changing the class.

The more difficult question runs in the opposite direction. How simple can the surface be? Is there a lower bound on its genus that depends only on the homology class and the smooth structure of the ambient four-manifold?

The answer is often yes. Gauge theory supplies adjunction inequalities that constrain the minimal genus. These inequalities are striking because they connect a geometric field equation, which lives on the entire four-manifold, to the topology of a particular embedded surface.

## Start with the complex adjunction formula

For a smooth complex curve inside a complex surface there is an exact formula. The canonical class of the ambient complex surface, evaluated on the curve, plus the self-intersection of the curve, equals twice the genus minus two.

Self-intersection needs explanation. Push the curve slightly in a normal direction and count the signed intersections with the original curve. This number is also the Euler number of the oriented normal bundle. In a complex surface the normal bundle has a natural complex structure, which makes the algebraic and topological descriptions agree.

The canonical class records the first Chern class of the bundle of holomorphic two-forms. The adjunction formula says that the canonical bundle of the curve is obtained by restricting the ambient canonical bundle and tensoring with the curve's normal bundle. Taking degrees gives the numerical identity.

On a K3 surface the canonical class is zero. Consequently a smooth holomorphic curve of genus g has self-intersection twice g minus two. An elliptic curve has self-intersection zero. A smooth genus-two curve has self-intersection two. These are equalities, not approximations.

## Why a smooth surface needs an inequality

A smooth embedded surface in a four-manifold need not be complex. There may be no preferred holomorphic tangent line, so the complex adjunction formula no longer applies as an identity.

Seiberg–Witten theory can nevertheless recover a lower bound. Let K be a Seiberg–Witten basic class. Under the usual hypotheses—including a closed oriented four-manifold with sufficiently large positive second Betti number and a connected embedded surface of positive genus with nonnegative self-intersection—an adjunction inequality says that twice the genus minus two is at least the self-intersection plus the absolute value of the pairing with K.

The absolute value appears because the bound must not depend on choosing an orientation for the surface in a way that artificially improves the inequality. This formula has variants with different hypotheses, and it must not be applied indiscriminately to spheres of negative self-intersection or four-manifolds with wall-crossing complications.

## Work through K3 again

Take a K3 surface, whose Seiberg–Witten basic class zero is nontrivial. The inequality reduces to twice the genus minus two being at least the self-intersection, for a connected positive-genus surface of nonnegative self-intersection.

Suppose a homology class has square two. Then every such smooth connected representative must have genus at least two. A smooth holomorphic genus-two curve in that class reaches the bound exactly. That does not merely calculate the genus of the holomorphic example; it proves the holomorphic representative has minimal genus among all smooth connected representatives meeting the hypotheses.

This is the conceptual leap. Algebraic geometry constructs one surface and proves an equality for it. Gauge theory tells us that no smooth competitor in the same homology class can be simpler.

## What is visible to smooth topology

Why isn't this just an inequality about the intersection form? Because the basic class K enters from a smooth gauge-theoretic invariant. Different smooth structures on a topological four-manifold can support different gauge-theoretic constraints. Thus minimal genus can carry information beyond ordinary homology and intersection numbers.

But one should also avoid an opposite overstatement. Knowing a lower bound does not automatically construct a representative achieving it. Sometimes the bound is sharp, as in holomorphic examples. Sometimes a separate geometric construction is needed, or the true minimal genus is larger.

The result is also sensitive to the ambient hypotheses. If the four-manifold has positive second Betti number equal to one, the Seiberg–Witten invariant may depend on a chamber. If the surface has negative square, blow-up and exceptional-curve phenomena require a different formulation. A slogan about genus cannot replace the actual theorem.

## From a surface to a constraint on the manifold

Adjunction inequalities demonstrate a productive dialogue between topology and analysis. A surface presents a geometric challenge: can this homology class be realized with fewer handles? The Seiberg–Witten equations supply global restrictions. The canonical class and intersection pairing translate those restrictions into an integer inequality.

The K3 example is especially clear. Genus two and self-intersection two fit the complex adjunction formula exactly. The Seiberg–Witten inequality then forbids a connected smooth genus-one representative in that same class. We have learned something about all possible smooth representatives by studying one algebraic representative and a gauge invariant of the ambient space.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Donaldson Invariants and the Smooth Topology of Four-Manifolds

**Track:** Topology and Geometry. **Background:** four-manifolds, connections and curvature, instanton moduli, and intersection forms. **Central question:** how can counting solutions of a differential equation reveal the smooth structure of a manifold?

#### Mathematical companion (not spoken)

For a closed, simply connected, oriented smooth four-manifold `X`, and an `SU(2)` bundle with `c_2=k`, the expected dimension of the regular irreducible ASD moduli space is
\[
\operatorname{vdim}\mathcal M_k=8k-3(1+b_2^+(X)).
\]
More generally `8k-3(1-b_1+b_2^+)`. On standardly oriented `K3`, `b_1=0`, `b_2^+=3`, so for `k=3` the expected dimension is `24-12=12`. The `mu`-map associates degree-`4-j` classes to `j`-dimensional homology insertions. Six homology-2 insertions yield total degree 12; an actual invariant requires the moduli-space orientation, compactification, and regularity procedures, and the dimension count alone does **not** assert nonvanishing.

Donaldson's diagonalization theorem restricts definite intersection forms of closed smooth simply connected four-manifolds to integral diagonal forms with signs fixed by definiteness. Polynomial invariants have additional hypotheses; with `b_2^+=1`, chamber dependence may arise.

##### Exercises with answers

1. What is the formal ASD moduli dimension on `K3` when `k=2`? **Answer:** `16-12=4`.
2. How many `mu`-classes of degree two fill virtual dimension 12? **Answer:** six.
3. Why is a noncompact moduli space a problem for integration? **Answer:** sequences of solutions can escape; bubbling and boundary phenomena obstruct naive deformation invariance.
4. What does the index calculation not establish? **Answer:** existence, regularity, compactness, or nonzero invariant value.

##### Reading and source notes

- [Donaldson and Kronheimer, The Geometry of Four-Manifolds](https://doi.org/10.1093/oso/9780198535539.001.0001), ASD moduli and Donaldson invariants.
- [Morgan, Gauge Theory and Four-Manifold Topology (lecture notes)](https://www.pdmi.ras.ru/EIMI/2013/morgan.pdf), index and invariant constructions.
- [Donaldson, An Application of Gauge Theory to Four-Dimensional Topology](https://doi.org/10.4310/JDG/1214437665), smooth intersection-form restrictions.

### A Family Index and Determinant Line by Hand: One Zero, One Twist

**Track:** Topology and Geometry. **Background:** K-theory, line bundles, kernels and cokernels, sheaf cohomology. **Central question:** how can every operator in a family have index zero while the determinant line of the family remains nontrivial?

#### Mathematical companion (not spoken)

Let `B=CP¹`, `E=1_B`, `F=O(1)`. Choose `s∈Γ(B,Hom(E,F))=Γ(B,O(1))` with one simple zero, and define `D_b:E_b→F_b` by `D_b(v)=v·s(b)`. All fiber maps have numerical index zero, since both source and target are one-dimensional. At the zero `b_0`, `dim ker D=dim coker D=1`; elsewhere both dimensions vanish.

The index K-class is `Ind(D)=[E]-[F]=-[O(1)]+[1]=-β∈\widetilde K^0(S²)`. Its determinant line under the convention `det(Ind)=det(ker D)⊗det(coker D)^*` is the canonically extended line

\[
\det(\operatorname{Ind}D)=\det E\otimes(\det F)^*
=O(-1),\qquad c_1=-h.
\]

The fiberwise ordinary determinant of `D` gives a section of its **dual** `O(1)` with one zero and positive local winding. This finite-dimensional model illustrates but is not a proof of the families Atiyah–Singer theorem or of Quillen/Bismut–Freed analytic metrics and connections.

##### Exercises with answers

1. What is the numerical index away from the zero? **Answer:** zero.
2. What is the numerical index at the zero? **Answer:** one minus one, still zero.
3. What is the Chern number of the index determinant line? **Answer:** minus one, under the convention det kernel tensor det cokernel dual.
4. Where does the ordinary determinant section live? **Answer:** in the *dual* determinant line `O(1)`.

##### Sources and further reading

- M. Atiyah and I. Singer, [The Index of Elliptic Operators: IV](https://doi.org/10.2307/1970756), families index theorem.
- J.-M. Bismut and D. Freed, [The Analysis of Elliptic Families I](https://doi.org/10.1007/BF01210930), determinant metrics and connections (1986).
- [Determinant line bundle](https://en.wikipedia.org/wiki/Determinant_line_bundle); [Index theory](https://en.wikipedia.org/wiki/Index_theory).

### Families Index Theory and Determinant Line Bundles

**Track:** Topology and Geometry. **Background:** Fredholm operators, vector bundles, elliptic index theory, and characteristic classes. **Central question:** how can the index of a smoothly varying differential operator remain meaningful when kernels suddenly change dimension?

#### Mathematical companion (not spoken)

For a family `D_b:E_b->F_b` of Fredholm operators over compact base `B`, the index defines `[ker D]-[coker D] in K^0(B)` after finite-dimensional stabilization; kernels need not individually be vector bundles. For the family `D_t:R->R`, `D_t(x)=tx`, both dimensions equal zero for `t !=0` and both equal one for `t=0`, so `ind D_t=0` throughout.

The determinant line, with a consistent dual convention, is
\[
\det D_b=\Lambda^{\max}\ker D_b\otimes\left(\Lambda^{\max}\operatorname{coker}D_b\right)^*.
\]
For a family of spin-c Dirac operators on fibers of `pi:M->B`, the cohomological families index formula is schematically
\[
\operatorname{ch}(\operatorname{Ind}D)=\pi_*\!\left(\widehat A(T^vM)e^{c_1(L)/2}\operatorname{ch}(E)\right),
\]
with the standard orientation/spin-c and twisting assumptions. For `L` of degree zero on an elliptic curve, `h^0(L)=h^1(L)=0` unless `L` is trivial, when both are one. Thus `chi(L)=0` regardless, but individual kernel and cokernel dimensions jump.

##### Exercises with answers

1. What is the index of `D_0:R->R` given by multiplication by zero? **Answer:** `dim ker - dim coker=1-1=0`.
2. Do constant numerical indices imply the family index class in `K^0(B)` is trivial? **Answer:** No; higher topological classes may remain.
3. What is the determinant line fiber of an invertible operator? **Answer:** canonically the one-dimensional scalar line, since kernel and cokernel are zero.
4. Why is a family of kernel spaces not always a vector bundle? **Answer:** kernel dimension can jump with the parameter.

##### Reading and source notes

- [Atiyah and Singer, The Index of Elliptic Operators: IV](https://doi.org/10.2307/1970756), the families index theorem.
- [Bismut and Freed, The Analysis of Elliptic Families: Metrics and Connections on Determinant Bundles](https://doi.org/10.1007/BF01210930), determinant-line geometry.
- [Freed, On Determinant Line Bundles](https://abel.math.harvard.edu/~dafr/detsur.pdf), detailed exposition of determinants and families.

### Seiberg-Witten Monopoles and Four-Manifolds

**Track:** Topology and Geometry. **Background:** differential geometry, bundles, Dirac operators, and characteristic classes. **Central question:** how can a nonlinear equation involving a spinor distinguish smooth structures on four-dimensional spaces?

#### Mathematical companion (not spoken)

Let `X` be a smooth closed oriented Riemannian four-manifold with spin-c structure `\mathfrak s`, determinant line `L`, and spinor bundles `W^\pm`. For a unitary connection `A` on `L` and `\psi\in\Gamma(W^+)`, the (schematic, convention-dependent) Seiberg–Witten equations are
\[
D_A\psi=0,\qquad F_A^+=q(\psi)+i\eta,
\]
where `q` is a trace-free quadratic form with appropriate normalization and `\eta` is a self-dual perturbation. Divide the solution space by `\mathrm{Map}(X,S^1)`. The virtual dimension is
\[
d(\mathfrak s)=\frac{c_1(L)^2-(2\chi(X)+3\sigma(X))}{4}.
\]
For K3, `\chi=24`, `\sigma=-16`, `2\chi+3\sigma=0`. For `c_1(L)=0`, `d=0`. K3 has `b_2^+=3`, so it lies in the chamber-independent regime of the standard integer-valued invariant (subject to orientations and regularity conventions).

The comparison with Donaldson invariants requires careful handling of `b_2^+`, reducibles, orientation, perturbation, and compactness; the standard Seiberg–Witten equations are `U(1)` rather than `SU(2)` gauge equations.

##### Exercises with answers

1. Compute `2\chi+3\sigma` for K3. **Answer:** `2(24)+3(-16)=0`.
2. What is the expected dimension for a determinant line with `c_1^2=8` on a manifold with `2\chi+3\sigma=0`? **Answer:** `2`.
3. Why divide solutions by gauge transformations? **Answer:** gauge-related fields represent the same geometric configuration.
4. Does expected dimension zero by itself establish an integer invariant? **Answer:** No; regularity, compactness, orientations, and reducibles require analysis.

##### Reading and source notes

- [Edward Witten, Monopoles and Four-Manifolds](https://arxiv.org/abs/hep-th/9411102), original Seiberg–Witten perspective on smooth topology.
- [Taubes, The Seiberg–Witten Invariants and Symplectic Forms](https://intlpress.com/site/pub/files/_fulltext/journals/mrl/1994/0001/0006/MRL-1994-0001-0006-a015.pdf), connections to symplectic structures and pseudoholomorphic curves.

### Adjunction Inequalities and Smooth Genus Bounds

**Track:** Topology and Geometry. **Background:** four-manifold intersection forms, Chern classes, and Seiberg–Witten invariants. **Central question:** how can gauge-theoretic invariants bound the genus of an embedded surface?

#### Mathematical companion (not spoken)

For a smooth irreducible complex curve `C\subset X` in a smooth complex projective surface, adjunction says `K_C\cong(K_X\otimes\mathcal O_X(C))|_C`. Taking degrees gives
\[
2g(C)-2=C^2+K_X\cdot C.
\]
For a K3 surface `K_X=0`, so `2g(C)-2=C^2`.

A standard Seiberg–Witten adjunction inequality: if `X` is a smooth closed oriented 4-manifold with `b_2^+(X)>1` and SW basic class `K`, and `\Sigma\subset X` is a smoothly embedded closed connected oriented surface with `g(\Sigma)>0`, `[\Sigma]^2\ge0`, then under the standard basic-class hypotheses,
\[
2g(\Sigma)-2\ge [\Sigma]^2+|\langle K,[\Sigma]\rangle|.
\]
The nonnegative self-intersection and positive-genus hypotheses are substantive; variants for negative squares and other `b_2^+` require additional conditions. For K3, the zero basic class yields `2g-2\ge [\Sigma]^2`. A class with square two therefore satisfies `g\ge2`; a smooth genus-two holomorphic curve realizes equality if that class admits one.

##### Exercises with answers

1. If a smooth holomorphic curve on a K3 has genus three, what is its square? **Answer:** `4`.
2. For a K3 class of square six, what genus lower bound does the inequality give? **Answer:** `g\ge4` for a connected positive-genus nonnegative-square representative.
3. Does the inequality by itself prove a representative attaining the bound exists? **Answer:** No.
4. Why not apply this formulation unchanged to an exceptional sphere of square `-1`? **Answer:** it violates both positive-genus and nonnegative-square hypotheses.

##### Reading and source notes

- [Edward Witten, Monopoles and Four-Manifolds](https://arxiv.org/abs/hep-th/9411102), Seiberg–Witten invariants and four-manifold constraints.
- [Konno, A Cohomological Seiberg–Witten Invariant Emerging from the Adjunction Inequality](https://doi.org/10.1112/topo.12215), modern extension and a discussion of adjunction constraints.
