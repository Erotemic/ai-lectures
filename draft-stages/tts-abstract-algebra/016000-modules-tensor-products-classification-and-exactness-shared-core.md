# Exact sequences, resolutions, and flatness

<!-- BEGIN SPOKEN LECTURE -->

# Exact sequences, resolutions, and flatness

## Exact Sequences and Resolutions: Measuring Lost Information

A homomorphism can lose information in two distinct ways. Different inputs may produce the same output, creating a kernel. And some possible outputs may never be reached, leaving a cokernel. Homological algebra organizes these two failures into chains of maps and asks when they fit together perfectly.

Take three modules A, B, and C with a map from A to B followed by a map from B to C. The sequence is exact at B if the image of the first map is exactly the kernel of the second. Every element arriving from A is killed by the second map, and every element killed by the second map can be explained as arriving from A. The word exactly is the critical part. Mere inclusion is not enough.

The simplest useful complete statement is a short exact sequence, written in words as zero to A to B to C to zero. Exactness at A forces the first map to be injective. Exactness at C forces the second map to be surjective. Exactness at B says the first map identifies A with the kernel of the second, so C is isomorphic to B modulo that embedded copy of A.

### A concrete short exact sequence

Start with the integers. Multiply an integer by two and regard the result as an integer. This map is injective. Next reduce an integer modulo two. That map is surjective. The integers killed by reduction modulo two are exactly the even integers, which are exactly the image of multiplication by two.

So zero, integers, integers, integers modulo two, zero is a short exact sequence with those maps. It says that the integers modulo two are what remains when we identify every even difference with zero. The same data appear in the quotient construction, but the sequence records how that quotient is produced.

Not every short exact sequence can be decomposed as a direct sum of its ends. Consider the sequence we just built. If it split as a sequence of abelian groups, the integers would contain a copy of the integers modulo two as a subgroup. But the integers have no nonzero element of finite order. The extension is not split.

Compare this with finite-dimensional vector spaces over a field. Every short exact sequence of vector spaces splits: choose a basis for the subspace and extend it to a basis of the middle space. For modules over arbitrary rings, that basis argument may be unavailable. Extensions can contain real structure not visible from the end modules alone.

### Chains and the meaning of homology

Extend our picture to a sequence of modules with maps between consecutive terms, such that each composite of two consecutive maps is zero. This is a chain complex. Because the composite vanishes, every element produced by one map is automatically killed by the next. Thus the image is contained in the next kernel.

A complex need not be exact. Its homology at a position is the kernel of the outgoing map divided by the image of the incoming map. It measures those elements that are killed by the outgoing map but cannot be explained as coming from the previous stage.

For a geometric example, imagine orienting the edges of a triangle and summing them around the boundary. The boundary of the triangle is a closed loop: taking its boundary produces zero, because each vertex appears once positively and once negatively. If the filled triangle is present as a two-dimensional face, that loop is itself the boundary of a face, and it disappears in first homology. If we retain only the three edges and vertices, the loop is still closed but is no longer a boundary of anything present. First homology detects that hole.

This is the same kernel modulo image pattern, whether the objects represent algebraic modules or the chains of a geometric space. Different applications give different modules and boundary maps; the logical shape is shared.

### Projective modules and the lifting problem

What kind of module behaves enough like a vector space that maps out of it can be lifted through surjections? A module P is projective if, whenever a module B maps surjectively onto C and we have a map from P to C, there is a map from P to B whose composition with the surjection is the original map.

Every free module is projective. To lift a map from a free module, choose a basis. Each basis vector has an image in C. Surjectivity lets us choose a preimage in B. Those choices extend linearly, producing the required lift. A direct summand of a free module is also projective, and in fact every projective module is a direct summand of some free module.

The module of integers modulo two is not projective as a module over the integers. If the reduction map from integers to integers modulo two admitted a lift of the identity map on integers modulo two, that lift would send its nonzero element to an integer of order dividing two. There is no such nonzero integer. So a required lift does not exist.

Projectivity characterizes a special kind of flexibility. It is also connected to exactness: the functor that takes a module M to the homomorphisms from P into M preserves short exact sequences precisely when P is projective.

### Build a resolution

Even if a module is not projective, we can describe it using projective modules. Start with a surjection from a free module onto M. Take the kernel and find a free module that surjects onto that kernel. Repeat. The result is a projective resolution: a chain of projective modules that is exact everywhere except for the final augmentation recording M.

For the integers modulo two, the short exact sequence with multiplication by two is already such a resolution. Both copies of the integers are free and hence projective. It has only one nonzero step before the target module.

Why bother replacing a module with a sequence of larger, easier modules? Because a construction that fails to preserve exactness on arbitrary modules can be applied to the projective resolution. The new homology then quantifies the lost exactness.

### Tor detects a failure of tensoring

We saw that tensoring the injection multiplication by two on the integers with integers modulo two turns the injection into the zero map. There is information that the tensor product erases.

Apply tensoring with integers modulo two to the projective resolution of integers modulo two. After tensoring, the first two modules become integers modulo two and the multiplication-by-two map becomes zero. The kernel of that zero map is the entire integers modulo two. There is no earlier nonzero map contributing an image. Thus the first homology of the tensored resolution is integers modulo two.

This group is called Tor one of integers modulo two with integers modulo two. It is nonzero precisely because tensoring has failed to preserve the injection we started with. In this example, homological algebra has turned an abstract failure of exactness into a concrete group with two elements.

Projective resolutions are not unique constructions, but the resulting Tor groups are independent of which projective resolution we choose, up to canonical isomorphism. Proving that independence uses comparison maps between resolutions and chain homotopies. The central conceptual point is already present: replace a difficult object by an exact complex of easier objects, apply a functor, and measure the homology that remains.

There is a parallel construction called Ext that measures failures involving homomorphism functors and extensions. Together Tor and Ext connect module theory, topology, number theory, and representation theory. They do so by taking kernels, images, and quotients seriously enough to track what our ordinary constructions forget.

## Flat Modules: When Tensor Products Preserve Exactness

Tensor products let us change coefficients. A vector space over the reals becomes a complex vector space when we tensor with the complex numbers. An integer module can be turned into a rational vector space by tensoring with the rationals. In geometry, the same operation lets us pass from a global ring to a ring of functions near one point.

But tensor products do not always preserve the information we started with. A nonzero element can disappear after changing coefficients. An injection can stop being an injection. The precise condition that prevents this failure is flatness.

### The warning example: reducing modulo two

Start with the inclusion of the even integers into all integers. We can identify it with the map from the integers to themselves that multiplies by two. This map is injective: if twice an integer is zero, that integer must be zero.

Now tensor the entire map over the integers with the integers modulo two. Both source and target become two-element groups. But the induced map is multiplication by two modulo two, and that is the zero map. It sends every element to zero; in particular it is no longer injective.

Nothing went wrong in the mechanics of tensoring. The issue is that reducing coefficients modulo two discards exactly the distinction that made multiplication by two injective. The tensor functor is right exact: whenever a map is onto, its tensor version remains onto, and cokernels are preserved. What may fail is preservation of kernels, and therefore preservation of injections.

### Flatness stated as a test

Let R be a commutative ring and M an R-module. We say M is flat when tensoring an exact sequence of R-modules with M keeps it exact. Because tensor product is always right exact, it is enough to check that tensoring any injection stays injective.

Every free module is flat. Indeed, tensoring with one copy of R changes nothing, and tensoring with a direct sum of copies of R forms a direct sum of the original sequence. Direct sums preserve exactness for modules. Every projective module is flat as well, since a projective module is a direct summand of a free one.

The converse is false. Flat modules need not be projective, and they certainly need not be free. This is more than a technical wrinkle: localization gives a prominent source of flat modules that are often not projective.

### Why localization is flat

Let S be a multiplicatively closed subset of R, with zero excluded in the nondegenerate case. Localizing a module N means allowing denominators from S. There is a natural isomorphism between the localization of N and the tensor product of N with the localized ring S inverse R. Therefore we can express localization as a change of coefficients.

Suppose a map from A to B is injective. Why is the induced map between their localizations also injective? An element a over s becomes zero in B localized at S only if some t in S annihilates its image in B. Because the original map was injective, the same t must annihilate a already in A. Therefore a over s was zero in the localization of A. Injectivity survives.

This argument does not require the original ring to be a domain. It proves the general fact that localization is an exact functor and that S inverse R is flat as an R-module.

Consider the map from the integers to the rationals. The rationals are obtained by inverting all nonzero integers, so they form a flat module over the integers. Yet tensoring a finite torsion group with the rationals gives zero. Flatness does not promise that every nonzero module stays nonzero. That stronger requirement is called faithful flatness. The rational numbers are flat over the integers, but not faithfully flat.

### A computation with Tor

There is a useful derived functor that measures precisely the failure of tensor product to be left exact. It is called Tor. The simplest computation comes from resolving the cyclic module Z modulo n by a two-term free resolution: multiply the integers by n, then take the quotient.

Tensor that resolution with an arbitrary abelian group A. The induced differential is multiplication by n on A. Its kernel is exactly the elements of A killed by n. That kernel is Tor one of Z modulo n with A.

Choose A to be the integers modulo m. The elements annihilated by n form a cyclic group of order the greatest common divisor of n and m. Thus Tor one of Z modulo n with Z modulo m is Z modulo the greatest common divisor. In particular, Tor one of Z modulo two with itself is nonzero. The failure we saw with multiplication by two is not an accident; Tor measures it systematically.

For a flat module M, Tor one of every module with M vanishes. The full converse also holds in the ordinary module category: Tor one vanishing against all modules is a characterization of flatness.

### Over a PID, torsion-free is enough

There is a particularly useful simplification over the integers, and more generally over a principal ideal domain. An R-module is flat if and only if it is torsion-free. Here torsion-free means that multiplying a nonzero element of the module by a nonzero ring element cannot give zero.

One direction follows from the same injection test: if M is flat, then tensoring multiplication by a nonzero scalar on R must remain injective on M, so M has no such torsion. For the other direction, a PID has enough structure to test flatness using injections of finitely generated ideals, all of which are principal. Torsion-freeness supplies the required injectivity.

Do not carry this equivalence to every domain. Over more general integral domains, torsion-free modules can fail to be flat. An ideal need not be principal or projective. Flatness controls how *all* relations behave, not just whether a single scalar annihilates an element.

### Local tests and geometric meaning

Flatness is local. An R-module M is flat if and only if, for every prime ideal p, the localization M at p is flat over the local ring R at p. This is one reason flatness is so valuable in algebraic geometry: a property about all modules can be checked one neighborhood at a time.

Informally, a flat family of geometric objects avoids certain kinds of algebraic jumps as parameters vary. But flatness should not be identified simply with constant fiber dimension; that equivalence requires specific finiteness and geometric hypotheses. The exact definition is tensor exactness, not a visual slogan about smoothly varying shapes.

The lesson connects three parts of our curriculum. Tensor products change coefficients; Tor records what that change loses; flatness guarantees that injections and short exact sequences survive. It lets algebra move between global and local viewpoints without accidentally destroying the relations we are trying to study.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Exact Sequences and Resolutions: Measuring Lost Information

**Track:** Abstract Algebra. **Background:** modules, kernels, cokernels, quotient modules, and tensor products. **Question:** how can a sequence of maps record whether information is missing, and why do projective resolutions repair failures of exactness?

#### Mathematical companion (not spoken)

A sequence \(A\xrightarrow fB\xrightarrow gC\) is **exact at \(B\)** when \(\operatorname{im}f=\ker g\). A short exact sequence \(0\to A\xrightarrow fB\xrightarrow gC\to0\) has injective \(f\), surjective \(g\), and \(C\cong B/f(A)\).

A chain complex \((C_n,d_n)\) satisfies \(d_n d_{n+1}=0\) and has homology
\[
H_n(C)=\ker(d_n:C_n\to C_{n-1})/\operatorname{im}(d_{n+1}:C_{n+1}\to C_n).
\]
A module \(P\) is projective iff \(\operatorname{Hom}_R(P,-)\) takes short exact sequences to short exact sequences; equivalently, it has the lifting property for surjections.

**Projective resolution of \(\mathbb Z/2\).**
\[
0\longrightarrow \mathbb Z\xrightarrow{\times2}\mathbb Z\longrightarrow \mathbb Z/2\longrightarrow0.
\]
Tensoring the projective part with \(\mathbb Z/2\) gives
\[
0\longrightarrow\mathbb Z/2\xrightarrow{0}\mathbb Z/2\longrightarrow0.
\]
Therefore \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2\). More generally \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/m,\mathbb Z/n)\cong\mathbb Z/\gcd(m,n)\).

**Split exactness.** A short exact sequence splits iff there is a section \(s:C\to B\) of \(g\) or a retraction \(r:B\to A\) of \(f\); then \(B\cong A\oplus C\). The sequence \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) does not split.

**Independence of resolutions.** A chain map lifting \(\mathrm{id}_M\) between projective resolutions exists and is unique up to chain homotopy. It induces canonical isomorphisms on homology after applying an additive functor such as \(-\otimes_R N\). This is the key step making derived functors well-defined.

##### Exercises with answers

1. In the sequence \(\mathbb Z\xrightarrow{\times3}\mathbb Z\to\mathbb Z/3\), what is the kernel of the second map? **Answer:** \(3\mathbb Z\), exactly the first image.
2. Does \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) split as abelian groups? **No.** A section would force an element of order two in \(\mathbb Z\).
3. Why is \(H_n\) well-defined? **Because** \(d_n d_{n+1}=0\) gives \(\operatorname{im}d_{n+1}\subseteq\ker d_n\).
4. Compute \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/3,\mathbb Z/6)\). **Answer:** \(\mathbb Z/3\).

##### Reading

Keith Conrad, [expository papers on algebra](https://kconrad.math.uconn.edu/blurbs/), modules and exact sequences; Pavel Etingof and collaborators, [MIT 18.712 notes](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), general representation and module constructions. For a full treatment of derived functors, see Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38.

### Flat Modules: When Tensor Products Preserve Exactness

**Track:** Abstract Algebra. **Background:** tensor products, modules, localization, exact sequences, Tor. **Central question:** what property of a module prevents tensoring from destroying injections?

#### Mathematical companion (not spoken)

For a commutative ring \(R\), an \(R\)-module \(M\) is **flat** iff \(-\otimes_R M\) is exact. Tensor is always right exact, so it suffices that it preserve monomorphisms. Free and projective modules are flat. For multiplicative \(S\subseteq R\),
\[S^{-1}N\cong N\otimes_R S^{-1}R,\]
and localization is exact, hence \(S^{-1}R\) is flat.

**Failure of left exactness:** tensor \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) with \(\mathbb Z/2\). The first map becomes \(0:\mathbb Z/2\to\mathbb Z/2\), not a monomorphism.

**Tor:** the free resolution \(0\to\mathbb Z\xrightarrow{\times n}\mathbb Z\to\mathbb Z/n\to0\) gives
\[\operatorname{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)=\ker(n:A\to A)=A[n].\]
For \(A=\mathbb Z/m\) this is isomorphic to \(\mathbb Z/\gcd(n,m)\). Flatness of \(M\) is equivalent to \(\operatorname{Tor}_1^R(N,M)=0\) for all \(R\)-modules \(N\).

**Cautions:** \(\mathbb Q\) is flat but not faithfully flat over \(\mathbb Z\): \((\mathbb Z/p)\otimes_{\mathbb Z}\mathbb Q=0\). Over a PID, flat is equivalent to torsion-free (including non-finitely generated modules). Over general domains, torsion-free need not imply flat. A standard local criterion is \(M\) flat over \(R\) iff \(M_{\mathfrak p}\) flat over \(R_{\mathfrak p}\) for each prime \(\mathfrak p\).

##### Exercises with answers

1. Is \(\mathbb Z/7\) flat as a \(\mathbb Z\)-module? **No:** it has nonzero torsion, and \(\mathbb Z\) is a PID.
2. Is \(\mathbb Z[1/6]\) flat over \(\mathbb Z\)? **Yes:** it is a localization.
3. Compute \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/8,\mathbb Z/12)\). **Answer:** \(\mathbb Z/4\), the subgroup killed by eight.
4. If localization kills an \(R\)-module, must the original module have been zero? **No:** \(\mathbb Z/2\) becomes zero over \(\mathbb Z[1/2]\).

##### Reading and source notes

- [Stacks Project, Section 10.39, Flat modules and flat ring maps](https://stacks.math.columbia.edu/tag/00H9), definitions, localization, and local flatness criteria.
- Charles A. Weibel, [*An Introduction to Homological Algebra*](https://doi.org/10.1017/CBO9781139644136), flatness, Tor, and derived functors.
