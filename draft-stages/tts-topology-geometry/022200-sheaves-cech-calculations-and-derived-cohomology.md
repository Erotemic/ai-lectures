# Sheaves, Cech calculations, and derived cohomology

<!-- BEGIN SPOKEN LECTURE -->

# Sheaves, Cech calculations, and derived cohomology

## Sheaves: Local Information That Knows How to Glue

Suppose we want to solve a differential equation on a circle. On every short arc we may find a solution. But these local solutions may disagree on overlapping arcs. Even if they agree locally in pairs, the global problem can have an obstruction when we return to the starting point. What language can express local existence, agreement on overlaps, and failure to construct a global object?

A sheaf does this in a remarkably economical way. It assigns a collection of objects to each open set, lets us restrict them to smaller open sets, and specifies when compatible local objects glue uniquely into one on a union.

### Assign information to an open set

Take a smooth manifold. For every open region U, let F of U be the set of smooth real-valued functions defined on U. If V lies inside U, restricting a smooth function from U to V gives a function on V. Restriction from U to itself does nothing, and a sequence of restrictions agrees with direct restriction.

This is a presheaf: a systematic assignment of data to open regions with restriction maps that compose correctly. The word may sound technical, but the operation is as familiar as cropping a map to a smaller neighborhood.

A sheaf is a presheaf that also satisfies two gluing principles. First, if two global objects have the same restrictions on every member of an open cover, they are equal. Second, if we have an object on every member of a cover and all the objects agree on overlaps, there is one global object restricting to each of them.

For smooth functions both principles hold. Agreement on overlaps lets us define a function on the union point by point, and smoothness is a local property. The same logic works for continuous functions, smooth differential forms, and sections of a fixed vector bundle.

### A presheaf that is not a sheaf

Consider an assignment that gives the real numbers to every nonempty open set, interpreted as one globally constant number, with identity restriction maps wherever possible. Take an open set consisting of two disconnected intervals. On the first interval choose the number one. On the second choose the number two. The overlap is empty, so compatibility imposes no relation. But the original assignment permits only one number for the whole disconnected union.

The gluing axiom fails. The associated sheaf repairs this defect by allowing locally constant functions, which can take different values on different connected components. This example separates the words constant and locally constant in a way that becomes important when we compute cohomology.

For a connected circle, a locally constant real function is constant everywhere. On a disconnected union it need not be. The sheaf remembers this difference without changing the definition of restriction.

### Look at germs near a point

Sometimes we care only about a function's behavior arbitrarily close to one point. Two functions defined on possibly different neighborhoods have the same germ at p if they agree on some smaller neighborhood of p. The set of all such germs is the stalk of the sheaf at p.

For the sheaf of smooth functions, a stalk is the collection of smooth-function germs, not merely numerical values at p. The functions x and x squared have the same value zero at the origin but different germs. Their derivatives and higher local behavior distinguish them.

A stalk is assembled as a direct limit over shrinking neighborhoods. This construction turns the restriction maps into a precise notion of infinitesimal local information. A morphism of sheaves is an isomorphism if and only if it is an isomorphism on every stalk. Exactness of sequences of sheaves can also be tested on stalks.

### Sections of a line bundle

Take a nontrivial complex line bundle over the sphere. On two disks it has local frames, and a section can be described by one function on each disk. On their overlap, the functions are related by the line bundle's transition function. The sheaf of sections packages these local descriptions without demanding one global frame.

This connects sheaves to the earlier bundle-gluing lectures. The transition function tells us how local coordinates compare. The sheaf tells us which local sections exist and whether compatible sections glue. A line bundle and its sheaf of sections carry closely related information, but it is useful to distinguish them: the sheaf tracks sections on every open set, not just the bundle's fibers.

### Local solutions may not become global solutions

Consider the differential equation df equals a closed one-form alpha. On a small enough contractible neighborhood, the Poincaré lemma supplies a local primitive f. On overlaps, two primitives differ by a constant. Their constants may fail to fit into a globally consistent collection.

On a circle, the one-form d theta has local primitives, but no single-valued global primitive. If there were one, integrating its derivative around the circle would be zero, whereas the integral of d theta is one full turn. The difference between local solvability and global solvability is not a minor exception: it is a central reason cohomology exists.

Sheaf cohomology generalizes this situation. It records obstructions to gluing and higher relations among local pieces. But before introducing higher cohomology, the sheaf axioms tell us exactly what the basic objects and their local behavior are.

A sheaf is neither merely a collection of functions nor a synonym for a bundle. It is a disciplined account of what can be known locally, how that information restricts, and what it takes to make a consistent global object. That is the missing language behind many constructions in geometry, analysis, and algebraic topology.

## Čech Cohomology by Calculation: Recovering the Circle's One Hole

A sheaf gives us local sections and rules for matching them. Čech cohomology takes a further step: it organizes the disagreements on overlaps into a chain complex. The procedure resembles simplicial cohomology, but its entries are sections of a sheaf on intersections of open sets rather than numbers assigned to abstract simplices.

We will calculate the first cohomology of the circle with coefficients in the constant real sheaf. The answer will be one copy of the real numbers, but we will see exactly where that copy comes from.

### Cover a circle with two long arcs

Choose two open arcs U and V, each slightly longer than a semicircle, arranged so their union is the full circle. Each arc is connected and contractible. Their intersection is not connected: it has two disjoint short arcs, call them A and B, on opposite sides of the circle.

A section of the constant real sheaf on a connected arc is one constant real number. A section on the disconnected intersection consists of two numbers, one on A and one on B.

A zero-cochain is a choice of local section on each member of the cover. Therefore it is a pair of real numbers: a on U and b on V. A one-cochain assigns a section to their intersection. Because the intersection has two components, it is a pair of real numbers, which we may call c on A and d on B.

The Čech coboundary measures the difference between the two local constants. With a fixed sign convention, it sends the pair a,b to the pair b minus a, b minus a. The same difference appears on both components because each local section was constant on its entire connected arc.

### Compute the kernel and quotient

A zero-cochain is a cocycle when its coboundary vanishes. That happens exactly when a equals b. So degree-zero cohomology consists of the diagonal pairs, one real parameter, corresponding to a globally constant function on the connected circle.

In degree one, there are no nonempty triple intersections involving three distinct cover members because we have only two sets. With the usual alternating Čech complex, all one-cochains are cocycles. The first cohomology is therefore the two-dimensional vector space of pairs c,d, divided by the one-dimensional subspace of diagonal pairs produced by coboundaries.

The quotient has dimension one. A convenient coordinate on it is d minus c. That difference cannot be changed by adding the same number to both entries, which is precisely what a coboundary does.

We have just computed first Čech cohomology of the circle as one copy of the real numbers. The class is not simply a number attached to either overlap component. It is the *relative disagreement* between the two components, after accounting for arbitrary changes of local sections on U and V.

### What the one-dimensional answer means

Imagine choosing local primitives of a closed one-form on U and V. On each overlap component, their difference is a constant. We might have one constant on A and another on B. Changing the primitive on U by a constant and on V by another constant shifts both overlap differences by the same amount. Their difference survives these changes.

That surviving number is the period of the original closed one-form around the circle, up to orientation and normalization. It is the same information described by integration around a loop in de Rham cohomology.

For the angular one-form normalized to have period one, the corresponding Čech class can be represented by overlap differences zero and one. A different choice of local primitives may change both numbers, but it cannot change their difference. In that very concrete sense, the circle's cohomology is the obstruction to gluing the local primitives.

### Why the cover matters, and why it eventually does not

We used a particular cover with a disconnected overlap. If instead we choose a cover with many small arcs and connected intersections, there are more cochains and more differentials. The resulting cohomology should still describe the same global hole, provided the cover is sufficiently well behaved for the coefficients involved.

That qualification is important. For arbitrary sheaves and arbitrary covers, a single Čech complex does not always compute derived sheaf cohomology. A useful sufficient condition is that the higher cohomology of the sheaf vanish on every nonempty finite intersection of the chosen cover. Such a cover is called acyclic for the sheaf. Then the Čech computation agrees with sheaf cohomology.

Our arc cover is acyclic for the constant real sheaf because each nonempty intersection component is contractible, and its components have no higher constant-sheaf cohomology. It is a genuine computation of the sheaf's first cohomology, not just a calculation depending on an arbitrary drawing of two arcs.

### The algebraic pattern to retain

The first Čech cohomology group is the space of compatible overlap data, modulo overlap data that came from changing local sections. Higher cochains live on triple and larger intersections, and their coboundaries record alternating compatibility conditions. The entire pattern has the same kernel modulo image structure as any chain complex.

The circle computation is particularly memorable because every piece is elementary: two numbers for local sections, two for overlap sections, one diagonal coboundary direction, and one surviving direction. We have converted a geometric loop into a quotient of small vector spaces.

That method extends to line bundles, holomorphic functions, local systems, and obstructions in algebraic geometry. The formulas become richer, but the foundational question remains: which local disagreements can be removed by changing local data, and which survive every such change?

## Why Sheaf Cohomology Is Derived: A Global Logarithm That Fails

We often take a local fact and assume it remains true globally. Sheaf theory provides a precise warning against that assumption. A sequence of sheaves can be exact at every point, meaning every local problem has the expected solution, while the sequence of their global sections is no longer exact.

The higher cohomology groups of a sheaf measure that failure. They are called the right derived functors of global sections. We will motivate the terminology using a circle-valued function that has local logarithms but no global real logarithm.

### The exponential sequence

On a smooth manifold M, consider smooth real-valued functions. Exponentiating two pi i times such a function produces a smooth function into the unit circle. The kernel consists of integer-valued smooth functions. Since an integer-valued smooth function is locally constant, the kernel is the constant sheaf of integers.

Locally, every smooth circle-valued function has a smooth real argument. To see this, restrict to a small arc of the target circle where an angle can be chosen continuously. Thus the exponential map is surjective on stalks: every local circle-valued section has a local real lift.

We obtain a short exact sequence of sheaves: locally constant integers, then smooth real functions, then smooth circle-valued functions. The word exact is a local statement here.

### A global lift can fail

Take M itself to be a circle. Consider the function that sends each point to itself on the unit circle. It has winding number one. On small arcs we can choose real angles for it, but after going once around we would need the angle to increase by one full turn, not return to its original real value.

There is no globally defined smooth real function f whose exponential equals this identity circle map. If there were, it would lift a degree-one map through the real line, forcing a contradiction with winding number.

Thus a map of global sections that is locally surjective is not globally surjective. The missing information is topological. The exact sequence of sheaves makes the failure precise rather than leaving it as an isolated curiosity.

### How cohomology detects the obstruction

A short exact sequence of abelian sheaves produces a long exact sequence in sheaf cohomology. The first portion begins with global sections, then a connecting map into first cohomology of the kernel sheaf.

For the exponential sequence, a global circle-valued function is sent by the connecting map to an integer cohomology class. This class measures how its locally chosen real logarithms differ on overlaps. On the circle, the identity map goes to the generator of first integral cohomology.

If that class vanishes, the overlap differences can be corrected by changing the local real lifts, and a global real logarithm exists. If it does not vanish, no choice of local branches will fix the obstruction.

Notice how closely this resembles our previous Čech calculation with two overlapping arcs. There, one surviving difference between overlap constants measured a hole. Here the differences are integers because two real arguments of the same circle-valued function differ by a whole number of turns.

### Why the global-section functor needs repair

The functor taking a sheaf to its global sections is left exact: injectivity and exactness at the first stages survive. But surjectivity can fail. To measure its failure systematically, algebraic homological methods replace the sheaf by a resolution of better-behaved sheaves, for example injective sheaves, and take global sections of the resulting complex.

The zero-th cohomology of that complex is ordinary global sections. The higher groups record the information lost by demanding global sections too early. This is what it means to derive the global-section functor.

The language is abstract, but the problem it solves is concrete. We are not making a mysterious new kind of cohomology. We are applying the kernel-modulo-image construction to a resolution chosen so that local exactness can be studied globally without discarding obstruction data.

### Acyclic sheaves and useful resolutions

Some sheaves have no higher sheaf cohomology. On a paracompact smooth manifold, the sheaf of smooth real-valued functions is fine: partitions of unity allow local corrections to be assembled. Fine sheaves are acyclic for global sections under the standard hypotheses.

This makes the exponential sequence especially informative. Its connecting homomorphism associates to a circle-valued function a class in first integral cohomology, and that class accounts for the global logarithm obstruction. More generally, exact sequences and acyclic resolutions produce long exact sequences that allow one to compute unknown cohomology from known pieces.

Holomorphic functions behave differently from smooth functions. There are no arbitrary smooth partitions of unity that preserve holomorphicity. Consequently the sheaf of holomorphic functions can have nonzero higher cohomology, even on compact complex manifolds. That difference is exactly why complex geometry produces interesting indices and line-bundle cohomology.

### The general lesson

The phrase exact locally is not the phrase solvable globally. A sheaf sequence can be exact on every stalk and still fail after applying global sections. Derived sheaf cohomology preserves the lost information and places it into higher degrees.

The identity map of a circle is a complete foundational example: local logarithms exist, their discrepancies are integer-valued, and a winding number prevents their global merger. Whenever a later lecture invokes an obstruction class, a connecting map, or a derived functor, it is using this local-to-global pattern in a richer setting.

## Holomorphic Line Bundles on the Projective Line: Counting H-Zero and H-One

An index formula can seem distant from the objects it counts. For a Dolbeault operator on a complex curve, the index is the number of independent holomorphic sections minus the number of independent first-cohomology obstructions. We will calculate both numbers for every holomorphic line bundle O of k on the complex projective line, using only two coordinate charts and Laurent series.

This is a calculation that can be checked at each step. It also explains the k plus one in Riemann–Roch, including negative values of k.

### Two charts and one transition function

The complex projective line has a chart U zero where the first homogeneous coordinate is nonzero, with affine coordinate z equal to Z one divided by Z zero. It has another chart U infinity where the second homogeneous coordinate is nonzero, with coordinate w equal to Z zero divided by Z one. On the overlap, w equals one over z.

Both charts look like the complex plane, and their overlap looks like the punctured complex plane. The line bundle O of k is given by a transition factor z to the k between the two local trivializations, with a fixed convention for which chart's coefficient is being expressed in which frame.

A holomorphic global section consists of holomorphic functions f zero of z and f infinity of w that agree through this transition. In our convention, f zero of z equals z to the k times f infinity of one over z. We must find all pairs satisfying this identity.

### Positive k gives polynomials

Suppose k is a nonnegative integer. Expand f infinity as a power series near w equals zero. After replacing w by one over z and multiplying by z to the k, we obtain a Laurent series in z with powers k, k minus one, k minus two, and so on.

For the expression to extend holomorphically across z equals zero, all negative powers must cancel. Thus only the first k plus one coefficients may remain. The resulting f zero is a polynomial of degree at most k.

There are k plus one independent monomials: one, z, through z to the k. So the vector space of holomorphic global sections has dimension k plus one. For k equals zero, only constants remain. For k equals one, we get two independent linear sections. For k equals two, three quadratic sections.

If k is negative, the matching condition demands a holomorphic function at z equals zero represented by only negative powers. The only such function is zero. Thus there are no nonzero global holomorphic sections when k is negative.

### Where first cohomology appears

To compute H one, use the two-chart Čech complex. A one-cochain is a holomorphic function on the overlap, expressed in the U zero trivialization. Because the overlap is punctured complex plane, it has a Laurent series with positive and negative powers.

A coboundary is the difference between a holomorphic function on U zero and a transformed holomorphic function on U infinity. The first supplies every nonnegative power of z. The second supplies powers k, k minus one, k minus two, and so on.

Which Laurent powers cannot be removed by those two kinds of terms? They must be negative, because U zero handles all nonnegative powers. They must also be greater than k, because U infinity handles powers k and below.

When k is minus one or greater, there is no integer strictly between k and zero. Every one-cochain is a coboundary, so H one vanishes.

When k equals minus two, exactly one power survives: z to the minus one. Therefore H one has dimension one. When k equals minus three, two powers survive: z to the minus two and z to the minus one. In general, if k is at most minus two, H one has dimension minus k minus one.

This calculation is not just formal cancellation of finite Laurent polynomials. Holomorphic Laurent series converge on the overlap, and splitting them into the relevant parts supplies holomorphic representatives on the two charts. The cover is acyclic for these coherent holomorphic sheaves, by the Stein nature of its nonempty intersections and the appropriate vanishing theorem. Those facts justify using the Čech complex for sheaf cohomology.

### The index is always k plus one

Now subtract dimensions. For nonnegative k, H zero has dimension k plus one and H one vanishes, so the difference is k plus one.

For k equals minus one, both groups vanish, and the difference is zero, again k plus one. For k at most minus two, H zero vanishes while H one has dimension minus k minus one, so zero minus that number is k plus one.

The same formula holds for every integer k. The negative results are meaningful: the cokernel of the Dolbeault operator can have larger dimension than its kernel.

We can compare with the topological Riemann–Roch calculation. The Chern character of O of k contributes k times the positive generator of second cohomology. The Todd class of the projective line contributes one additional copy. Their product integrates to k plus one. We have verified that the topological integral counts exactly the same alternating dimensions as the explicit holomorphic Čech complex.

### Why the example belongs in several subjects

The calculation is simultaneously a demonstration of sheaf cohomology, complex analysis, line-bundle geometry, and elliptic index theory. The same line bundle is represented by a clutching function, by its first Chern number, by transition functions for holomorphic sections, and by a Dolbeault operator.

The power of the index theorem becomes clearer when the simple coordinates disappear. On an arbitrary compact complex manifold, we may not be able to write the global sections as elementary polynomials. But characteristic classes and a pushforward can still calculate their alternating total, provided the relevant hypotheses hold.

The essential bridge is now explicit: holomorphic sections are global compatible local functions; first sheaf cohomology measures overlap classes that cannot be corrected; their difference is the elliptic index. Riemann–Roch computes that difference from topological data.

## Fine Resolutions: Why de Rham and Dolbeault Compute Sheaf Cohomology

There is a tension in the study of cohomology. Sheaf cohomology begins by examining all open sets and their compatibility, while differential-form cohomology begins with globally defined forms and a differential operator. Why should the two constructions ever agree?

The answer comes from a particular kind of resolution. Locally, the Poincaré lemma makes the de Rham complex exact after the constants. Globally, partitions of unity make the sheaves of smooth forms acyclic. Put those two facts together, and global differential forms calculate the sheaf cohomology of the constant real sheaf.

### Exactness is a local statement

Take a smooth manifold. The de Rham sequence begins with locally constant real functions, then smooth functions, then smooth one-forms, two-forms, and so on, connected by the exterior derivative.

The exterior derivative of a constant function is zero. Conversely, a smooth function whose exterior derivative vanishes is locally constant. More generally, the Poincaré lemma says that a closed differential k-form is locally exact for positive k: near any point, on a sufficiently small contractible coordinate neighborhood, it has a local primitive.

So as a sequence of sheaves, the constant real sheaf followed by the de Rham complex is exact. We have resolved a sheaf by sheaves of differential forms.

But taking global sections does not necessarily preserve exactness. That is the entire source of interesting de Rham cohomology. On a circle, a globally closed one-form may have no global primitive. Its local primitives exist, but their overlap differences cannot be globally corrected.

### Why smooth forms are easy to assemble

A smooth partition of unity is a collection of smooth functions adapted to an open cover whose sum is one. It lets us blend local constructions into global ones. Multiplying a differential form by a partition-of-unity function preserves smoothness, so the sheaf of smooth differential forms is fine.

On a paracompact smooth manifold, fine sheaves have vanishing higher cohomology. This is their key computational property. A resolution by such sheaves is acyclic for the global-section functor. Therefore the derived cohomology of the original constant sheaf can be computed simply by taking global sections of the de Rham complex and finding its cohomology.

That conclusion is the de Rham theorem in a sheaf-theoretic form. The first cohomology of the constant real sheaf is the quotient of globally closed one-forms by globally exact one-forms. On a circle, both viewpoints give one real generator.

### Holomorphic functions create a parallel story

On a complex manifold, consider the sheaf of holomorphic functions. A smooth complex-valued function is holomorphic exactly when its derivative in the antiholomorphic directions vanishes. This operator is written d bar, or partial bar.

The Dolbeault complex starts with smooth complex-valued functions, then smooth forms of type zero-one, zero-two, and so on, connected by partial bar. The local partial-bar Poincaré lemma makes this complex a resolution of the holomorphic-function sheaf.

The sheaves of smooth forms of type zero-q are fine, because multiplication by a smooth partition of unity preserves their type as forms and does not need to preserve holomorphicity. Thus the Dolbeault complex is another acyclic resolution.

The result is Dolbeault's theorem: the q-th sheaf cohomology of holomorphic functions is isomorphic to the q-th cohomology of the global partial-bar complex.

### Why holomorphic functions are different from smooth functions

It is tempting to ask why we did not simply use partitions of unity inside the sheaf of holomorphic functions itself. The reason is that a nonconstant smooth bump function is not holomorphic. On a connected complex manifold, a holomorphic function that vanishes on a nonempty open set vanishes everywhere. We cannot freely localize holomorphic data using compactly supported holomorphic cutoffs.

This failure is not an inconvenience to be swept aside; it is where higher holomorphic sheaf cohomology gets room to exist. The sheaf of holomorphic functions is generally not fine. The smooth forms in its Dolbeault resolution are fine, and they calculate the missing higher groups.

Take the projective line with the holomorphic line bundle O of minus two. We already calculated that the space of global holomorphic sections is zero and the first sheaf cohomology has dimension one. Dolbeault's theorem says that the corresponding first Dolbeault cohomology group, built from global zero-one forms with values in O of minus two, is one-dimensional. A nontrivial global obstruction survives even though every local partial-bar problem can be solved.

### Twisting by a bundle

For a holomorphic vector bundle E, replace functions by holomorphic sections of E and ordinary zero-q forms by zero-q forms with values in E. The partial-bar operator uses the holomorphic structure of E. Its cohomology computes sheaf cohomology of the holomorphic section sheaf.

The elliptic operator partial bar plus its formal adjoint is a Dolbeault-type Dirac operator. On a compact complex manifold, its index is the alternating sum of the dimensions of the holomorphic sheaf cohomology groups. On the projective line with O of k, that alternating sum is k plus one.

This identifies the exact point where sheaf theory enters elliptic index theory. We can count analytic kernel and cokernel spaces, compute sheaf cohomology with a cover, or apply a topological characteristic-class formula. Each method describes a different aspect of the same invariant.

The reusable strategy is this: find a locally exact resolution of the sheaf of interest, choose terms whose higher cohomology vanishes, and take global sections to compute the derived information. de Rham and Dolbeault are two especially important versions of that strategy.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Sheaves: Local Information That Knows How to Glue

**Track:** Topology and Geometry. **Background:** topological spaces, functions on open sets, vector bundles. **Central question:** what extra structure turns local formulas into globally consistent objects?

#### Mathematical companion (not spoken)

A presheaf F assigns to each open U a set/group/module F(U) and to V⊂U a restriction `ρ_{UV}:F(U)→F(V)` with `ρ_{UU}=id` and `ρ_{VW}ρ_{UV}=ρ_{UW}`. A sheaf additionally satisfies uniqueness and existence of glued sections from matching families on an open cover. The stalk `F_p=colim_{p∈U}F(U)` consists of germs.

For smooth M, `U↦C∞(U)` and `U↦Ω^k(U)` are sheaves. The constant presheaf `U↦R` fails gluing over disconnected unions; its sheafification is the constant sheaf `R_M` of locally constant functions. A short exact sequence of sheaves is exact at stalks; it need not yield a short exact sequence of global sections.

##### Exercises with answers

1. Why is the presheaf of one constant number per open set not a sheaf on disconnected opens? **Answer:** compatible different constants on disjoint components cannot glue to one constant.
2. Are a function's value and its germ at a point the same? **Answer:** no, distinct local functions can agree at the point yet have distinct germs.
3. What makes a section over two overlapping bundle charts global? **Answer:** the local coordinate sections agree after applying the bundle transition function on the overlap.
4. Why can a closed one-form have local primitives but no global primitive? **Answer:** local primitives may differ by constants that fail a global compatibility condition, detected by a nonzero period.

##### Sources and further reading

- Ravi Vakil, [The Rising Sea: Foundations of Algebraic Geometry](https://math.stanford.edu/~vakil/preprints.html), Chapter 2, on sheaves and stalks.
- [Sheaf (mathematics)](https://en.wikipedia.org/wiki/Sheaf_(mathematics)); [Stalk (sheaf)](https://en.wikipedia.org/wiki/Stalk_(sheaf)).

### Čech Cohomology by Calculation: Recovering the Circle's One Hole

**Track:** Topology and Geometry. **Background:** sheaf restrictions, open covers, linear algebra. **Central question:** how can a failure to glue local constants produce a cohomology class?

#### Mathematical companion (not spoken)

Let U,V be connected contractible arcs covering S¹ with `U∩V=A⊔B`, two contractible components. For the constant real sheaf R, the two-set alternating Čech complex is

\[
C^0=R(U)\oplus R(V)\cong\mathbb R^2
\xrightarrow{\delta}
C^1=R(U\cap V)\cong\mathbb R^2,\quad
\delta(a,b)=(b-a,b-a).
\]

Thus `ker δ=diag(R)`, `im δ=diag(R)`, and `\check H^1≈R²/diag(R)≈R`, with class represented by the difference of the two overlap coordinates. Here intersections are disjoint unions of contractible sets, so the cover is acyclic for the constant sheaf and this computes `H^1(S¹;R)`. For a general sheaf or general open cover, Čech and derived sheaf cohomology need comparison; they are not simply synonymous.

##### Exercises with answers

1. What are the dimensions of C-zero and C-one? **Answer:** both are two.
2. What is the rank of the coboundary map? **Answer:** one.
3. Why is the quotient dimension one? **Answer:** all one-cochains are cocycles and the image of δ has dimension one inside a two-dimensional space.
4. What is invariant when both overlap constants shift by the same amount? **Answer:** their difference, the Čech cohomology class.

##### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology, Section 20.11](https://stacks.math.columbia.edu/tag/01EO), comparison theorem and acyclic covers.
- Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), the circle's first cohomology.
- [Čech cohomology](https://en.wikipedia.org/wiki/%C4%8Cech_cohomology).

### Why Sheaf Cohomology Is Derived: A Global Logarithm That Fails

**Track:** Topology and Geometry. **Background:** sheaves, exact sequences, Čech one-cocycles. **Central question:** why can a sequence be exact locally but fail to be exact after taking global sections?

#### Mathematical companion (not spoken)

On a paracompact smooth M, the sheaf exponential sequence is exact on stalks:

\[
0\to\underline{\mathbb Z}_M\to\mathcal C_M^\infty(\mathbb R)
\xrightarrow{f\mapsto e^{2\pi if}}\mathcal C_M^\infty(S^1)\to0.
\]

The connecting morphism `δ:H^0(M,C∞(S¹))→H^1(M,Z)` sends a smooth circle-valued map to its homotopy/winding obstruction to a global logarithm. For M=S¹ and g(t)=e^{2πit}, δ[g] generates `H¹(S¹;Z)=Z`. Since `C∞_M(R)` is fine on paracompact smooth M, its higher sheaf cohomology vanishes, and the resulting long exact sequence describes such obstructions. In general `H^q(M,F)=R^qΓ(M,F)` for abelian sheaves F on a suitable site; this definition is not merely the Čech groups of one arbitrary cover.

##### Exercises with answers

1. Why is the exponential map surjective as a sheaf map? **Answer:** every point has a neighborhood on which a smooth circle-valued function admits a smooth real argument.
2. Why does the identity map S¹→S¹ lack a global real logarithm? **Answer:** its winding number is one.
3. What does the connecting homomorphism measure? **Answer:** the class of the overlap differences between local logarithms.
4. Why is a short exact sheaf sequence not necessarily short exact on global sections? **Answer:** taking global sections preserves left exactness but can lose surjectivity.

##### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology](https://stacks.math.columbia.edu/tag/01EO), sheaf-cohomology comparisons.
- Ravi Vakil, [The Rising Sea](https://math.stanford.edu/~vakil/preprints.html), sheaves and homological algebra.
- [Sheaf cohomology](https://en.wikipedia.org/wiki/Sheaf_cohomology); [Exponential sheaf sequence](https://en.wikipedia.org/wiki/Exponential_sheaf_sequence).

### Holomorphic Line Bundles on the Projective Line: Counting H-Zero and H-One

**Track:** Topology and Geometry. **Background:** sheaves, Čech cochains, projective coordinates, Laurent series. **Central question:** can we calculate an elliptic index by explicitly computing the sections and obstructions of a holomorphic line bundle?

#### Mathematical companion (not spoken)

On `CP¹`, use `U_0={Z_0≠0}`, `U_∞={Z_1≠0}`, `z=Z_1/Z_0`, `w=1/z`. Choose the transition convention `f_0(z)=z^k f_∞(1/z)` for O(k). Then

\[
h^0(\mathbb{CP}^1,\mathcal O(k))=\max(k+1,0),\qquad
h^1(\mathbb{CP}^1,\mathcal O(k))=\max(-k-1,0).
\]

The Čech one-cochains on the overlap are Laurent series modulo `f_0(z)-z^k f_∞(1/z)`. The obstruction exponents are integers `k<n<0`, giving `-k-1` surviving modes when k≤-2. These charts and all nonempty finite intersections are Stein, so Cartan's theorem B supplies cover acyclicity for coherent sheaves, and Čech equals derived cohomology here. The Dolbeault index is `χ(O(k))=h⁰-h¹=k+1`, equal to `∫_{CP¹}ch(O(k))Td(TCP¹)`.

##### Exercises with answers

1. Calculate h-zero and h-one for O(2). **Answer:** 3 and 0.
2. Calculate them for O(-1). **Answer:** 0 and 0.
3. Calculate them for O(-4). **Answer:** 0 and 3; the surviving Laurent exponents are -3,-2,-1.
4. What is chi of O(-4)? **Answer:** -3, consistent with k+1.

##### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology](https://stacks.math.columbia.edu/tag/01EO), acyclic-cover comparison.
- Ravi Vakil, [The Rising Sea](https://math.stanford.edu/~vakil/preprints.html), line bundles and projective geometry.
- [Cohomology of line bundles on projective space](https://en.wikipedia.org/wiki/Line_bundle#Line_bundles_on_projective_space); [Riemann–Roch theorem](https://en.wikipedia.org/wiki/Riemann%E2%80%93Roch_theorem).

### Fine Resolutions: Why de Rham and Dolbeault Compute Sheaf Cohomology

**Track:** Topology and Geometry. **Background:** local Poincaré lemma, sheaf cohomology, smooth and holomorphic forms. **Central question:** why can globally defined differential forms calculate an obstruction theory built from local sheaves?

#### Mathematical companion (not spoken)

For smooth paracompact M, the Poincaré lemma gives the exact sheaf resolution

\[
0\to\underline{\mathbb R}_M\to\Omega_M^0\xrightarrow d\Omega_M^1\xrightarrow d\cdots.
\]

The sheaves Ω^k are fine, hence acyclic for Γ. Therefore `H^q(M;R_M)≈H^q(Ω^*(M),d)`.

For a complex manifold X and a holomorphic vector bundle E, the Dolbeault resolution is

\[
0\to\mathcal O(E)\to\mathcal A^{0,0}(E)
\xrightarrow{\bar\partial_E}\mathcal A^{0,1}(E)\to\cdots,
\]

where the sheaves of smooth (0,q)-forms with values in E are fine. Consequently `H^q(X, O(E))≈H_{\bar∂}^{0,q}(X,E)`. On compact complex X, the Dolbeault index is `Σ_q (-1)^q dim H^q(X,O(E))`, subject to the usual Fredholm/elliptic hypotheses.

##### Exercises with answers

1. Why is the de Rham sequence exact as a sequence of sheaves? **Answer:** the local Poincaré lemma produces primitives on sufficiently small neighborhoods.
2. Why are smooth form sheaves fine? **Answer:** partitions of unity act on smooth forms and supply local-to-global endomorphisms.
3. Why does the holomorphic-function sheaf not admit the same partition-of-unity argument? **Answer:** smooth bump functions are generally not holomorphic.
4. What is `H_{\bar∂}^{0,1}(CP¹,O(-2))`? **Answer:** a complex vector space of dimension one.

##### Sources and further reading

- The Stacks Project, [Čech Cohomology and Cohomology](https://stacks.math.columbia.edu/tag/01EO), acyclic resolutions.
- [Dolbeault cohomology](https://en.wikipedia.org/wiki/Dolbeault_cohomology); [de Rham theorem](https://en.wikipedia.org/wiki/De_Rham_theorem).
