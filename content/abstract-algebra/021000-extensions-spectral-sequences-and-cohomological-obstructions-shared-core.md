# Extensions, spectral sequences, base change, and projectives

<!-- BEGIN SPOKEN LECTURE -->

# Extensions, spectral sequences, base change, and projectives

## Ext, Long Exact Sequences, and the Algebra of Extensions

Suppose you know the two ends of a short exact sequence, a module A sitting inside a larger module E, and a quotient B. Do A and B tell you what E must be? In linear algebra over a field, the answer is yes up to isomorphism. Choose a basis of A, extend it to a basis of E, and the sequence splits. For modules over a general ring, that basis-extension argument can fail. The way the pieces attach is new information.

The group called Ext one of B with A measures that information. A zero element represents a split sequence. A nonzero element represents a nonsplit attachment. The power of this definition is not just that it names a phenomenon. Ext can be calculated from a presentation, fitted into a long exact sequence, and used to prove that certain extensions cannot exist.

### Start with ordinary abelian groups

Every abelian group is a module over the integers. This gives us an example where no exotic coefficients are needed. Consider the group of integers modulo four. It contains the subgroup consisting of zero and two, isomorphic to the integers modulo two. The quotient by that subgroup is again the integers modulo two. So we have a short exact sequence with two copies of the two-element group at its ends and the four-element cyclic group in the middle.

Compare it with the split sequence whose middle group is the direct product of two copies of the two-element group. The ends are identical in both sequences. But in one middle group there is an element of order four; in the other, every nonzero element has order two. No isomorphism can erase that difference.

These are two different extension classes. If we classify only the composition factors, both groups look like two copies of the same simple piece. Ext records the glue.

### Calculating Ext from a free resolution

Let B be the integers modulo n. There is an exact sequence of integer modules: one copy of the integers maps to another by multiplication by n, and the second maps onto the integers modulo n. The integers are free, so the first two terms provide a projective resolution of B.

To compute Ext one of B with A, apply the Hom functor into A. A homomorphism from the integers into A is determined by the image of one, so Hom from the integers to A is naturally A itself. The map induced by multiplying by n becomes multiplication by n on A. The first Ext group is the cokernel of that map: A modulo the subgroup of n-fold multiples.

For A equal to the integers modulo m, the answer is a cyclic group whose order is the greatest common divisor of n and m. In particular, Ext one of the two-element group with itself has two elements. One is the split class. The other is represented by our four-element cyclic group.

Notice a subtle point about the order of the inputs. Ext is computed by resolving its first argument, B, and then taking Hom into its second argument, A. In general, swapping those arguments is not an innocent operation. The groups need not agree.

### Why a sequence becomes a long sequence

Hom is left exact. It detects kernels correctly, but taking Hom does not always preserve a surjection. An extension that fails to split is precisely the sort of obstruction that appears when a desired lifting map cannot be constructed.

Start with a short exact sequence from A prime into A onto A double prime, and fix a target module T. Taking Hom into T produces arrows in the opposite direction: first Hom from A double prime into T, then Hom from A into T, then Hom from A prime into T. Those first terms form an exact sequence, but the last map may fail to be onto.

What comes after that failure? A connecting homomorphism sends a map from A prime to T to an element of Ext one of A double prime with T. If you continue, you obtain a long exact sequence involving Ext one, Ext two, and the higher derived groups. The connecting maps do not merely pad out a diagram: they turn failures of lifting into computable obstructions.

There is a complementary long exact sequence obtained by fixing the first argument and varying the target module in a short exact sequence. Because Hom into that target is covariant, its arrows have the forward direction. Always check which argument you are varying before writing the diagram.

### The connecting map as a concrete operation

Consider a short exact sequence from A prime into A onto A double prime. Suppose someone gives us a homomorphism from A prime to a target T, and asks whether it extends to a homomorphism from all of A to T. If it does, the obstruction is zero. If not, we can form an extension of A double prime by T by taking a pushout along the given map. The new middle module is built by identifying the copy of A prime inside A with its image in T.

This pushout extension represents the connecting Ext class. Its class vanishes exactly when the original map extends, under the usual module-category hypotheses. Thus an algebraic element records a very ordinary question: can a map defined on a submodule be extended?

That viewpoint gives the long exact sequence a reason to exist. Its arrows link specific extension and lifting questions; exactness says that an obstruction vanishes precisely when a prior step succeeds.

### The Yoneda description

There is another way to meet Ext one without mentioning resolutions. Take all short exact sequences with fixed ends A and B. Two sequences are equivalent if there is an isomorphism between the middle modules making the endpoint maps commute and fixing those endpoint identifications. Equivalence matters: merely knowing that two middle modules are isomorphic is not enough when the embeddings and quotients differ.

These equivalence classes can be added by a construction called the Baer sum. One combines two extensions using a pullback over B and a pushout along addition in A. The split extension is the identity. With this addition, the extension classes form an abelian group, naturally isomorphic to Ext one of B with A.

For higher Ext, equivalence classes of longer exact sequences give the Yoneda interpretation. Composing extensions resembles composing obstructions. The resolution calculation and the extension-class construction are two views of the same invariant.

### What Ext cannot tell you by itself

An Ext group classifies extensions only after the ring and both end modules have been specified. Knowing that an Ext group is nonzero does not mean every middle module is indecomposable. Knowing it is zero means every short exact sequence with those ends splits, not that every module in the category is semisimple. And the underlying set of extensions is not classified just by the sizes of their endpoints: module structure, maps, and the equivalence relation are essential.

The practical lesson is that failure to split is structured, not accidental. Free resolutions convert it into a cokernel computation. Long exact sequences transport it along other exact sequences. The Yoneda viewpoint says what the computation means: it classifies ways of fitting one module inside another. The algebraic glue can be computed as precisely as the pieces it joins.

## Spectral Sequences: Recovering Homology in Stages

A chain complex packages a sequence of maps whose successive compositions are zero. Its homology detects classes killed by one map but not produced by the preceding map. In simple examples we can compute all kernels and images directly. In a large filtered complex, or in a double complex with two differentials, that direct calculation may be impractical.

A spectral sequence is a method for solving such a calculation in stages. It does not magically make difficult homology disappear. Instead it organizes approximations to the answer, together with a succession of correction maps that remove apparent classes that do not survive in the full complex.

### Begin with a filtration

Suppose we have a cochain complex C, so its differential raises degree by one. Give it a decreasing filtration: C is built from subcomplexes F zero containing F one containing F two, and so on. Because each F p is a subcomplex, the differential preserves the filtration. We first look at the associated graded pieces: each F p divided by F p plus one.

Think of the filtration as layers of an archaeological site. On one layer we see a particular class, but part of the relation that kills it may lie in another layer. The associated graded complex forgets some interactions between layers. It is easier to compute, but it can show classes that are not genuine classes of the total complex.

The first page, often called E zero, is built from those associated graded pieces with the part of the differential that stays within one layer. Taking the cohomology of that first page gives E one. The later pages are obtained by taking the cohomology of correction differentials. A class surviving one page can still be killed by a differential that changes filtration level further.

### A two-term example where the first answer is wrong

Consider a cochain complex over a field k with one generator x in degree zero and one generator y in degree one. The differential sends x to y. Because that map is an isomorphism, the total cohomology is zero in both degrees.

Now filter the complex so y occupies the deeper layer: F zero is the whole complex; F one contains y but not x; F two is zero. The first associated graded page contains x in the first layer and y in the second. On that associated graded page, the differential is zero, because the map from x to y jumps across the filtration. So both x and y initially look like cohomology classes.

But the first correction differential sees the very map we had hidden. It sends the class of x to the class of y. It is an isomorphism. On the following page, both classes disappear. The limiting page is zero, matching the true cohomology of the original complex.

This is the essential behavior of a spectral sequence in miniature. A page is a provisional calculation. A class on page one is not necessarily a class of the total object. We must let the permitted differentials act before claiming survival.

### The indices carry information

One common convention for a decreasing filtration of a cochain complex labels terms E r with two indices, p and q. Their sum is the total cohomological degree. The page-r differential moves p to p plus r and moves q to q minus r plus one. It therefore raises total degree by one, as a cochain differential must.

The index r measures how far the differential jumps between filtration layers. The first page handles local information; later pages handle more distant interactions. This is why a spectral sequence can stop quickly when the grading forces all potential targets of later differentials to be zero.

On each page, a class is meaningful only modulo the classes that entered as boundaries on that page. After taking cohomology, the next page contains classes that survived that test. This repeated quotienting is precisely what makes the calculation systematic.

### Convergence does not mean literal equality

Under suitable boundedness and convergence hypotheses, the pages stabilize to E infinity. It is tempting to say E infinity *is* the cohomology of the total complex. That is often too strong. E infinity is generally the associated graded object of a filtration on the total cohomology.

Knowing the graded pieces need not tell us how they fit together as an unfiltered object. For abelian groups, two graded pieces each isomorphic to the integers modulo two might assemble to the direct sum of two copies, or to the integers modulo four, depending on extension data. The Ext description of nonsplitting tells us how to describe exactly that ambiguity.

Over a field, finite-dimensional filtered vector spaces split noncanonically, so dimensions can often be reconstructed by adding graded dimensions. But even then the splitting is not a canonical identification. Over rings the extension problem can change the isomorphism type.

### Double complexes give two routes

A double complex has objects arranged in a grid and two differentials, one moving horizontally and the other vertically, with the required anticommutation relation. By combining them with signs we form a total complex whose differential squares to zero.

We can filter the total complex by columns or by rows. Each choice leads to a spectral sequence. With a column filtration, one often computes vertical cohomology first, then learns how the horizontal maps act on it. With a row filtration, the order is reversed.

The two spectral sequences may look different at the beginning yet, under appropriate boundedness conditions, they converge to the same total cohomology. This ability to choose the cheaper first calculation is a major practical advantage. In geometry and homological algebra it often turns a large combined problem into a sequence of tractable local calculations.

### What a proof must check

Before using a spectral sequence, ask four questions. What exact complex is filtered? Which convention is used for indices and differentials? What hypotheses ensure convergence to the intended object? And, once E infinity is obtained, are there unresolved extension problems?

A diagram of boxes with arrows is not a proof without those answers. The method is powerful precisely because its conventions and convergence statements have exact mathematical content.

We can now see why spectral sequences appear whenever a mathematical object is assembled in layers: a filtered complex, a fibration, a group extension, or a derived functor composed with another. The first approximation finds candidate classes. Successive differentials decide which survive. The limiting information describes the graded pieces of the answer, and extension data may finish the reconstruction. A spectral sequence is a disciplined way to keep track of what each layer conceals about the others.

## Flat Base Change and Tor Spectral Sequences

Suppose we have solved a problem over one ring and want to solve its counterpart over another. We might reduce integer coefficients modulo a prime, extend scalars from real to complex numbers, or specialize a polynomial parameter. Tensor products are the algebraic machinery behind these operations. But there is a trap: transporting objects is easier than transporting the exact relationships between them.

The word flatness names the condition that avoids that trap. When flatness fails, Tor groups keep track of the correction. When several layers of corrections interact, spectral sequences organize them.

### A short exact sequence that breaks

Start with the integers and the map that multiplies an integer by two. This map is injective. Its cokernel is the integers modulo two, so we have a short exact sequence: integers, multiplied by two into integers, followed by reduction modulo two.

Now tensor each term with the integers modulo two. Both copies of the integers become the two-element module. Multiplication by two becomes the zero map. The resulting sequence cannot be exact at its first nonzero term: a zero map is not injective.

The failure is structural, not a small computational error. Tensor product always preserves cokernels and hence right exactness. It does not, in general, preserve injections. A module F is called flat when tensoring with F preserves every short exact sequence. A flat change of scalars therefore keeps the exact relationships that define kernels, images, and quotients.

Localization is a basic source of flat modules. Passing from the integers to the rational numbers, or inverting powers of a chosen integer, preserves exact sequences. But preservation is not the same as preserving every nonzero element: localization can kill torsion. An injection remains an injection after flat base change, even if both sides of a particular torsion sequence become zero.

### Tor records the missing information

Tensoring is right exact, so homological algebra derives it on the left. Choose a projective or free resolution of one input, tensor that resolution with the other, and compute homology. In degree zero the result is the ordinary tensor product. In higher degrees the groups are called Tor.

Take the earlier resolution of the integers modulo two, using multiplication by two between two copies of the integers. Tensor with the integers modulo two. The differential becomes zero, so its first homology is another copy of the integers modulo two. That group is Tor in degree one. It measures exactly the injection that tensoring destroyed.

If an input is flat, its positive-degree Tor groups vanish against every module. Conversely, vanishing of all first Tor groups against a module characterizes flatness. This makes flatness observable by a family of homological tests.

### A change of rings has two routes

Let R map to a ring S. Suppose M is an R-module, while N is an S-module, and therefore also an R-module by restriction. We can try to calculate Tor over R between M and N directly. Or first transport M from R to S, and then calculate Tor over S.

If we simply replace M by its ordinary tensor product with S, the second approach may lose information. The base change itself could have higher Tor. The correct first stage is derived tensoring, which remembers an entire complex rather than only its degree-zero quotient.

There is a change-of-rings spectral sequence whose second page consists of Tor over S applied to the Tor groups over R of M with S. It converges, with standard boundedness conventions, to Tor over R of M with N. The page has two indices because one index measures the cost of base change and the other measures the Tor computation performed afterward.

This formula is not a mysterious extra theorem bolted onto tensor product. Build a free resolution of M over R. Tensor it with S, then resolve the resulting S-complex when necessary and tensor with N. The resulting double complex can be read in two directions. One filtration computes the intermediate Tor groups; the other leads to the desired total homology. A spectral sequence is the bookkeeping system for comparing the two routes.

### The smallest counterexample

Here is a calculation that makes the correction visible. Take R to be the polynomial ring in one variable over a field k. Let S be the quotient obtained by setting that variable to zero, so S is k. Take M and N both to be k, with their natural module structures.

Over R, the module k has a two-term free resolution: multiplication by the polynomial variable between two copies of R. After tensoring with k, the variable acts as zero, and we obtain two nonzero Tor groups, one in degree zero and one in degree one.

But over S, which is itself the field k, higher Tor groups vanish. If we first replaced M by its ordinary base change, we would see only the degree-zero k and miss the degree-one result entirely.

The change-of-rings spectral sequence retains the missing k in a second row. There are no possible further differentials in this simple example, so the two classes survive and reproduce the calculation over R. The added homological grading has paid for itself.

### Flat base change simplifies the picture

When S is flat over R, Tor over R of M with S vanishes in positive degrees. Then the change-of-rings spectral sequence collapses to its single remaining row. Under the usual module conditions, Tor over R of M with N can be computed as Tor over S of the base-changed M with N.

There is a related flat-base-change statement for a pair of R-modules M and N: after tensoring their Tor groups with a flat R-algebra S, one obtains the corresponding Tor groups over S of their scalar extensions. The exact formulation depends on which variables are being transported, but the principle is constant. Flatness means no hidden derived corrections appear merely because the coefficient ring changed.

This is why flatness is central in algebraic geometry, where families are studied over varying base rings. It marks a setting in which algebraic behavior changes without unpredictable loss of exactness.

### Why retain the machinery

A module is not just a collection of elements. Its relations are part of the object. Plain tensor products may erase some relations in ways that destroy kernels, while derived tensor products remember the loss. Tor makes the correction measurable. Spectral sequences make multiple corrections composable.

So the right question after a change of coefficients is not merely, “What do the generators become?” It is, “Which exact properties survive, and what derived information measures what did not?” The distinction becomes indispensable in algebraic geometry, topology, and modern approaches to computation with chain complexes.

## Projective Modules, Vector Bundles, and the First Idea of K-Theory

In elementary linear algebra, a finite-dimensional vector space has a basis. Over a general ring, a module need not have any basis at all. Yet some modules behave enough like vector spaces that one can perform almost all the same constructions locally. These are projective modules.

To understand why they matter, think about a Möbius band. Near any single point of its central circle, the band looks like a product of a little interval with a line. But if you travel once around the circle, the line reverses its orientation. No single continuous choice of a nonzero vector along every fiber can be made consistent after the circuit.

The module of continuous sections of this line bundle will give us an example of a module that is locally free but not globally free. Algebra alone can record the twist.

### Splitting a free module

A module P over a ring R is projective when it is a direct summand of some free module. That means there is another module Q for which P direct sum Q is free. A finitely generated projective module is a direct summand of a finite-rank free module.

Why use this definition? A free module comes with independent coordinate directions. A direct summand can inherit many of its good properties without possessing global coordinates of its own. A familiar equivalent definition says that maps from P into quotients can be lifted across surjections. This is the categorical lifting property, and it explains why projectives support the resolutions used in homological algebra.

One way to build projective modules is through idempotent matrices. An idempotent is a matrix E whose square equals itself. Its image and kernel form complementary submodules of a free module. The image is projective, even if no global basis exists for that image. Conversely, every finitely generated projective module arises as the image of some finite idempotent matrix.

This turns an abstract algebraic property into a computational object. Rather than guessing a basis, we can specify a projection and ask what its image does at different points of the underlying space.

### A rotating line that never quite returns

Let R be the ring of continuous real-valued functions on the circle. A rank-one bundle over the circle can be described by a line in the plane that rotates through half a turn as we go once around the circle. The line returns to itself because a line has no preferred arrow, although any attempted choice of a unit vector returns with the opposite sign.

At angle theta, take the orthogonal projection onto the line making angle theta divided by two with the horizontal axis. Its matrix entries can be written using only sine and cosine of theta. Consequently they are continuous, periodic functions on the circle, even though a chosen unit vector with angle theta divided by two is not periodic.

The resulting matrix is idempotent at every point. Its image gives a finitely generated projective module of continuous sections of the Möbius line bundle. It cannot be free of rank one. If it were, one global basis section would give a nonvanishing continuous choice of vector around the circle, contradicting the twist.

Yet the module is a direct summand of a free module of rank two. The complementary image is another line bundle, and together they recover the trivial plane bundle. The apparent paradox is exactly the distinction between being free and being projective.

### Why topology and algebra meet

The Serre–Swan theorem makes this connection systematic. For a compact Hausdorff space X, finite-rank real or complex vector bundles correspond to finitely generated projective modules over the ring of continuous real or complex functions on X. Passing from a bundle to its module of sections is not just a source of examples; it establishes an equivalence of categories with appropriate conventions.

Thus the algebra of a ring of functions remembers how vectors twist over the space. Matrix idempotents encode vector bundles. Module operations become geometric operations: direct sum combines bundles fiberwise, and tensor product combines their fibers multiplicatively.

Notice the role of the coefficient field. The real Möbius line bundle is nontrivial. Complex line bundles on a circle are all trivial, so the same example would not witness nonfree rank-one complex projective modules over continuous complex-valued functions on the circle. The ring matters.

### Turning modules into an invariant

There are many projective modules, and adding them by direct sum does not immediately give a group: one cannot generally subtract an actual vector bundle from another. Grothendieck's idea is to formally add differences.

Start with isomorphism classes of finitely generated projective modules, with direct sum as addition. Construct its universal abelian group completion. This group is called K zero of the ring. A formal difference of projective modules represents an element of K zero, subject to relations expressing how direct sums behave.

For a field, every finite-dimensional vector space is determined by its dimension. K zero is therefore the integers. For rings of functions on spaces with nontrivial vector bundles, K zero can contain more information than rank.

The Möbius example gives a glimpse of that extra information. Its line bundle L is not trivial, yet L direct sum L is a trivial real plane bundle over the circle. In reduced real K-theory, the difference between L and the trivial line has order two. The torsion is a trace of the half-turn that no rank count can detect.

We should distinguish the two statements carefully. The equation in K-theory tells us about stable equivalence, where adding trivial bundles can make two objects comparable. It does not mean the original Möbius line has suddenly acquired a global frame.

### Why this is the right abstraction

Projective modules are the right replacement for finite-dimensional vector spaces when geometry can twist. They explain why resolutions have good lifting properties, why locally free objects can fail to be globally free, and why new invariants are needed beyond dimension.

K-theory begins with a surprisingly modest move: take objects we can add but not subtract, and construct a group that records their stable differences. What emerges is a bridge among matrix algebra, vector bundles, topology, and arithmetic. The same philosophy will recur whenever we want to compare complicated objects by how they fit into sums, extensions, and exact sequences.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Ext, Long Exact Sequences, and the Algebra of Extensions

**Track:** Abstract Algebra. **Background:** modules, exact sequences, projective resolutions, modular representations. **Central question:** how can we compute and compare ways of joining modules, including joins that do not split?

#### Mathematical companion (not spoken)

Fix a ring \(R\) and left \(R\)-modules \(B,A\). For a projective resolution \(P_\bullet\twoheadrightarrow B\),
\[
\operatorname{Ext}^i_R(B,A)=H^i\bigl(\operatorname{Hom}_R(P_\bullet,A)\bigr).
\]
Under the usual module-category hypotheses, Yoneda equivalence classes of short exact sequences \(0\to A\to E\to B\to0\) identify naturally with \(\operatorname{Ext}^1_R(B,A)\), with zero represented by split extensions.

Over \(R=\mathbb Z\), the resolution \(0\to\mathbb Z\xrightarrow{\times n}\mathbb Z\to\mathbb Z/n\to0\) yields
\[
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong A/nA,\qquad
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong\mathbb Z/\gcd(n,m).
\]
The \(n=m=2\) cases include \(0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0\) (nonzero class) and \(0\to\mathbb Z/2\to(\mathbb Z/2)^2\to\mathbb Z/2\to0\) (zero class).

For \(0\to A'\to A\to A''\to0\), the **contravariant first-variable** sequence begins
\[
0\to\operatorname{Hom}(A'',T)\to\operatorname{Hom}(A,T)\to\operatorname{Hom}(A',T)
\xrightarrow{\delta}\operatorname{Ext}^1(A'',T)\to\operatorname{Ext}^1(A,T)\to\cdots.
\]
The connecting map \(\delta(f)\) is represented by the pushout of the given extension along \(f:A'\to T\). It vanishes iff \(f\) extends to \(A\to T\). Higher derived terms continue this sequence. Similarly a short exact sequence in the **second** variable gives a covariant long exact sequence.

##### Exercises with answers

1. Compute \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/6,\mathbb Z/4)\). **Answer:** \((\mathbb Z/4)/6(\mathbb Z/4)\cong\mathbb Z/2\).
2. Is \(0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0\) split? **No:** there is no subgroup complementary to the unique order-two subgroup.
3. What happens when the first argument is a projective module \(P\)? **Answer:** \(\operatorname{Ext}^i_R(P,A)=0\) for every \(i>0\).
4. Why does the \(\operatorname{Hom}(-,T)\) sequence reverse arrows? **Answer:** it acts by precomposition, making Hom contravariant in its first argument.

##### Reading and source notes

- Charles A. Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), chapters on derived functors, connecting maps, and Yoneda Ext.
- Kiran Kedlaya, [MIT 18.726 homological algebra lecture](https://ocw.mit.edu/courses/18-726-algebraic-geometry-spring-2009/resources/mit18_726s09_lec16_homalg/).

### Spectral Sequences: Recovering Homology in Stages

**Track:** Abstract Algebra. **Background:** chain complexes, homology, long exact sequences, filtrations and quotient modules. **Central question:** how can a complicated homology calculation be assembled from simpler layers without losing the interactions between them?

#### Mathematical companion (not spoken)

Let \((C^\bullet,d)\) be a cochain complex with a decreasing filtration \(F^pC^\bullet\) by subcomplexes. A standard convention is
\[E_0^{p,q}=F^p C^{p+q}/F^{p+1}C^{p+q},\quad E_1^{p,q}=H^{p+q}(\operatorname{gr}^p_F C^\bullet),\quad d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}.\]
Each \(E_{r+1}\) is the cohomology of \((E_r,d_r)\). Under appropriate boundedness / exhaustive and separated convergence hypotheses, \(E_\infty^{p,q}\cong\operatorname{gr}^p_F H^{p+q}(C)\). This does **not** specify the extension classes necessary to reconstruct the unfiltered cohomology.

**Toy example:** \(C^0=k\langle x\rangle\xrightarrow{d}C^1=k\langle y\rangle\), \(d(x)=y\). Put \(F^0C=C\), \(F^1C^0=0\), \(F^1C^1=C^1\), \(F^2C=0\). Then \(d_0=0\) on the associated graded, \(E_1^{0,0}=k\langle[x]\rangle\), \(E_1^{1,0}=k\langle[y]\rangle\), and \(d_1([x])=[y]\) is an isomorphism. Therefore \(E_2=E_\infty=0=H^\bullet(C)\).

**Extension caution:** an associated graded abelian group with two successive quotients \(\mathbb Z/2\) need not determine whether the full group is \((\mathbb Z/2)^2\) or \(\mathbb Z/4\). Differential and filtration-index conventions vary across homological and cohomological versions; convert them explicitly when citing formulas.

##### Exercises with answers

1. Why is \(d_r\) of total cohomological degree one? **Answer:** its index changes total degree by \(r+(-r+1)=1\).
2. In the toy example, why does the E-one page have nonzero terms although total cohomology vanishes? **Answer:** the only differential raises filtration and is invisible to \(d_0\); it is detected by \(d_1\).
3. Does \(E_\infty\) uniquely determine \(H^\bullet(C)\) as an abelian group? **Not in general:** one must solve extension problems.
4. If a differential's target term is zero, can that differential kill the source class? **No:** but another page or an incoming differential may still affect the class unless all possibilities are ruled out.

##### Reading and source notes

- [Stacks Project, Section 12.24: Spectral sequences from filtered complexes](https://stacks.math.columbia.edu/tag/012K), precise grading and differential conventions.
- Allen Hatcher, [Algebraic Topology and supplementary spectral-sequence materials](https://pi.math.cornell.edu/~hatcher/), geometric spectral-sequence applications and convergence.
- Charles A. Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), spectral sequences and derived functors.

### Flat Base Change and Tor Spectral Sequences

**Track:** Abstract Algebra. **Background:** tensor products, short exact sequences, flatness, projective resolutions, spectral sequences. **Central question:** what must be corrected when an algebraic calculation is transported to a new ring?

#### Mathematical companion (not spoken)

For an \(R\)-module \(F\), flatness means \((-\otimes_R F)\) is exact, equivalently \(\operatorname{Tor}_1^R(M,F)=0\) for all \(M\). For a multiplicative set \(U\subset R\), the localization \(U^{-1}R\) is flat.

**Loss of injectivity:** \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) is exact. Tensoring with \(\mathbb Z/2\) gives a zero map \(\mathbb Z/2\xrightarrow{0}\mathbb Z/2\), so injectivity is lost and \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2\).

**Change-of-rings spectral sequence:** for a commutative ring map \(R\to S\), an \(R\)-module \(M\), and an \(S\)-module \(N\), a homological convention yields
\[E^2_{p,q}=\operatorname{Tor}^S_p(\operatorname{Tor}^R_q(M,S),N)\Longrightarrow\operatorname{Tor}^R_{p+q}(M,N).\]
Standard convergence/boundedness and indexing conventions apply. When \(S\) is \(R\)-flat this collapses to \(\operatorname{Tor}^R_n(M,N)\cong\operatorname{Tor}^S_n(M\otimes_R S,N)\).

**Worked example:** \(R=k[x]\), \(S=R/(x)=k\), \(M=N=k\). The free resolution \(0\to R\xrightarrow{x}R\to k\to0\) gives \(\operatorname{Tor}_0^R(k,k)=k\), \(\operatorname{Tor}_1^R(k,k)=k\), all higher Tor zero. Its base change to \(S\) has zero differential. Since \(\operatorname{Tor}_p^k(-,k)=0\) for \(p>0\), the spectral sequence has \(E^2_{0,0}=E^2_{0,1}=k\), matching the abutment.

##### Exercises with answers

1. Does tensoring preserve surjections? **Yes:** tensor product is right exact.
2. Can a flat base change kill a nonzero torsion module? **Yes:** \(\mathbb Z/2\otimes_{\mathbb Z}\mathbb Q=0\), but exactness is still preserved.
3. What is \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/n,A)\)? **Answer:** the \(n\)-torsion subgroup \(\{a\in A:na=0\}\).
4. Which term of the change-of-rings spectral sequence is missed if one simply substitutes \(M\otimes_R S\)? **Answer:** all \(q>0\) terms \(\operatorname{Tor}_q^R(M,S)\).

##### Reading and source notes

- [Stacks Project, Spectral sequences for Tor](https://stacks.math.columbia.edu/tag/061Y), change-of-rings spectral sequence with index conventions.
- [Stacks Project, Tor independence](https://stacks.math.columbia.edu/tag/065Y), derived versus ordinary base change.
- [Stacks Project, Computing Tor](https://stacks.math.columbia.edu/tag/064F), projective resolutions and derived tensor products.

### Projective Modules, Vector Bundles, and the First Idea of K-Theory

**Track:** Abstract Algebra. **Background:** modules and direct sums, tensor products, affine and topological vector bundles. **Central question:** can a module behave locally like a free module without admitting a global basis?

#### Mathematical companion (not spoken)

A module \(P\) over \(R\) is projective iff it is a direct summand of a free module, equivalently iff \(\operatorname{Hom}_R(P,-)\) is exact. Finite projectives correspond to images of idempotent matrices \(E\in M_n(R)\), \(E^2=E\): \(R^n=\operatorname{im}E\oplus\ker E\).

**Möbius projector:** take \(R=C(S^1,\mathbb R)\), with \(\theta\) an angular coordinate modulo \(2\pi\), and
\[E(\theta)=\frac12\begin{pmatrix}1+\cos\theta&\sin\theta\\\sin\theta&1-\cos\theta\end{pmatrix}.\]
It is continuous and periodic with \(E(\theta)^2=E(\theta)\), and projects onto the line spanned by \((\cos(\theta/2),\sin(\theta/2))\). This line is well-defined modulo sign and gives the Möbius real line bundle \(L\). \(L\) has no nowhere-vanishing global section, hence its module of sections is not free of rank one. The orthogonal complement line bundle is isomorphic to \(L\), and \(L\oplus L\cong\underline{\mathbb R}^2\).

The Grothendieck group \(K_0(R)\) is the group completion of isomorphism classes of finitely generated projectives under direct sum. For a field \(k\), \(K_0(k)\cong\mathbb Z\) via dimension. For \(C(S^1,\mathbb R)\), the reduced group \(\widetilde K_0\cong\mathbb Z/2\) detects the Möbius class. More generally the Serre–Swan equivalence identifies finite-rank bundles on compact Hausdorff \(X\) with finitely generated projective modules over \(C(X,\mathbb F)\), \(\mathbb F=\mathbb R\) or \(\mathbb C\).

##### Exercises with answers

1. If \(E^2=E\), why is \(R^n=\mathrm{im}E\oplus\ker E\)? **Answer:** write \(v=Ev+(v-Ev)\); the summands intersect trivially.
2. Why is a nontrivial line bundle over \(S^1\) not free as a rank-one section module? **Answer:** a free rank-one section would be a nowhere-vanishing global frame.
3. Why does \(L\oplus L\) being trivial not imply \(L\) trivial? **Answer:** direct-sum cancellation does not hold for arbitrary vector bundles; stable and actual triviality differ.
4. What does \(K_0(k)\) measure for a field \(k\)? **Answer:** the dimension, extended to virtual differences, giving \(\mathbb Z\).

##### Reading and source notes

- Richard G. Swan, [*Vector Bundles and Projective Modules*](https://www.math.unl.edu/~jkettinger2/swan.pdf), original proof of the compact Hausdorff correspondence.
- Allen Hatcher, [*Vector Bundles and K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), bundle examples, stable classes, and K-theoretic constructions.
- [Stacks Project, projective modules and direct summands](https://stacks.math.columbia.edu/tag/0ELQ), commutative algebra background.
