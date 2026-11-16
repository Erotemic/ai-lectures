# 016000 — Exact Sequences and Resolutions: Measuring Lost Information

**Track:** Abstract Algebra. **Background:** modules, kernels, cokernels, quotient modules, and tensor products. **Question:** how can a sequence of maps record whether information is missing, and why do projective resolutions repair failures of exactness?

<!-- BEGIN SPOKEN LECTURE -->

# Exact Sequences and Resolutions: Measuring Lost Information

A homomorphism can lose information in two distinct ways. Different inputs may produce the same output, creating a kernel. And some possible outputs may never be reached, leaving a cokernel. Homological algebra organizes these two failures into chains of maps and asks when they fit together perfectly.

Take three modules A, B, and C with a map from A to B followed by a map from B to C. The sequence is exact at B if the image of the first map is exactly the kernel of the second. Every element arriving from A is killed by the second map, and every element killed by the second map can be explained as arriving from A. The word exactly is the critical part. Mere inclusion is not enough.

The simplest useful complete statement is a short exact sequence, written in words as zero to A to B to C to zero. Exactness at A forces the first map to be injective. Exactness at C forces the second map to be surjective. Exactness at B says the first map identifies A with the kernel of the second, so C is isomorphic to B modulo that embedded copy of A.

## A concrete short exact sequence

Start with the integers. Multiply an integer by two and regard the result as an integer. This map is injective. Next reduce an integer modulo two. That map is surjective. The integers killed by reduction modulo two are exactly the even integers, which are exactly the image of multiplication by two.

So zero, integers, integers, integers modulo two, zero is a short exact sequence with those maps. It says that the integers modulo two are what remains when we identify every even difference with zero. The same data appear in the quotient construction, but the sequence records how that quotient is produced.

Not every short exact sequence can be decomposed as a direct sum of its ends. Consider the sequence we just built. If it split as a sequence of abelian groups, the integers would contain a copy of the integers modulo two as a subgroup. But the integers have no nonzero element of finite order. The extension is not split.

Compare this with finite-dimensional vector spaces over a field. Every short exact sequence of vector spaces splits: choose a basis for the subspace and extend it to a basis of the middle space. For modules over arbitrary rings, that basis argument may be unavailable. Extensions can contain real structure not visible from the end modules alone.

## Chains and the meaning of homology

Extend our picture to a sequence of modules with maps between consecutive terms, such that each composite of two consecutive maps is zero. This is a chain complex. Because the composite vanishes, every element produced by one map is automatically killed by the next. Thus the image is contained in the next kernel.

A complex need not be exact. Its homology at a position is the kernel of the outgoing map divided by the image of the incoming map. It measures those elements that are killed by the outgoing map but cannot be explained as coming from the previous stage.

For a geometric example, imagine orienting the edges of a triangle and summing them around the boundary. The boundary of the triangle is a closed loop: taking its boundary produces zero, because each vertex appears once positively and once negatively. If the filled triangle is present as a two-dimensional face, that loop is itself the boundary of a face, and it disappears in first homology. If we retain only the three edges and vertices, the loop is still closed but is no longer a boundary of anything present. First homology detects that hole.

This is the same kernel modulo image pattern, whether the objects represent algebraic modules or the chains of a geometric space. Different applications give different modules and boundary maps; the logical shape is shared.

## Projective modules and the lifting problem

What kind of module behaves enough like a vector space that maps out of it can be lifted through surjections? A module P is projective if, whenever a module B maps surjectively onto C and we have a map from P to C, there is a map from P to B whose composition with the surjection is the original map.

Every free module is projective. To lift a map from a free module, choose a basis. Each basis vector has an image in C. Surjectivity lets us choose a preimage in B. Those choices extend linearly, producing the required lift. A direct summand of a free module is also projective, and in fact every projective module is a direct summand of some free module.

The module of integers modulo two is not projective as a module over the integers. If the reduction map from integers to integers modulo two admitted a lift of the identity map on integers modulo two, that lift would send its nonzero element to an integer of order dividing two. There is no such nonzero integer. So a required lift does not exist.

Projectivity characterizes a special kind of flexibility. It is also connected to exactness: the functor that takes a module M to the homomorphisms from P into M preserves short exact sequences precisely when P is projective.

## Build a resolution

Even if a module is not projective, we can describe it using projective modules. Start with a surjection from a free module onto M. Take the kernel and find a free module that surjects onto that kernel. Repeat. The result is a projective resolution: a chain of projective modules that is exact everywhere except for the final augmentation recording M.

For the integers modulo two, the short exact sequence with multiplication by two is already such a resolution. Both copies of the integers are free and hence projective. It has only one nonzero step before the target module.

Why bother replacing a module with a sequence of larger, easier modules? Because a construction that fails to preserve exactness on arbitrary modules can be applied to the projective resolution. The new homology then quantifies the lost exactness.

## Tor detects a failure of tensoring

We saw that tensoring the injection multiplication by two on the integers with integers modulo two turns the injection into the zero map. There is information that the tensor product erases.

Apply tensoring with integers modulo two to the projective resolution of integers modulo two. After tensoring, the first two modules become integers modulo two and the multiplication-by-two map becomes zero. The kernel of that zero map is the entire integers modulo two. There is no earlier nonzero map contributing an image. Thus the first homology of the tensored resolution is integers modulo two.

This group is called Tor one of integers modulo two with integers modulo two. It is nonzero precisely because tensoring has failed to preserve the injection we started with. In this example, homological algebra has turned an abstract failure of exactness into a concrete group with two elements.

Projective resolutions are not unique constructions, but the resulting Tor groups are independent of which projective resolution we choose, up to canonical isomorphism. Proving that independence uses comparison maps between resolutions and chain homotopies. The central conceptual point is already present: replace a difficult object by an exact complex of easier objects, apply a functor, and measure the homology that remains.

There is a parallel construction called Ext that measures failures involving homomorphism functors and extensions. Together Tor and Ext connect module theory, topology, number theory, and representation theory. They do so by taking kernels, images, and quotients seriously enough to track what our ordinary constructions forget.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

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

### Exercises with answers

1. In the sequence \(\mathbb Z\xrightarrow{\times3}\mathbb Z\to\mathbb Z/3\), what is the kernel of the second map? **Answer:** \(3\mathbb Z\), exactly the first image.
2. Does \(0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0\) split as abelian groups? **No.** A section would force an element of order two in \(\mathbb Z\).
3. Why is \(H_n\) well-defined? **Because** \(d_n d_{n+1}=0\) gives \(\operatorname{im}d_{n+1}\subseteq\ker d_n\).
4. Compute \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/3,\mathbb Z/6)\). **Answer:** \(\mathbb Z/3\).

### Reading

Keith Conrad, [expository papers on algebra](https://kconrad.math.uconn.edu/blurbs/), modules and exact sequences; Pavel Etingof and collaborators, [MIT 18.712 notes](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/pages/lecture-notes/), general representation and module constructions. For a full treatment of derived functors, see Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38.
