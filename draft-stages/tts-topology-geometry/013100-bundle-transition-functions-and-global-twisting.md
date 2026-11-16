# 013100 - Bundle Transition Functions and Global Twisting

**Track:** Topology and Geometry. **Background:** manifolds, smooth charts, linear algebra. **Question:** how can every local fiber look like a product while the entire bundle is twisted?

<!-- BEGIN SPOKEN LECTURE -->

# Bundle Transition Functions and Global Twisting

Hold a narrow strip of paper, give it half a twist, and join its ends. The result is a Mobius band. At every small patch of the central circle, the band looks like an ordinary interval attached to a piece of the circle. But as we travel around once, the transverse direction has been reversed. This is the simplest image of a fiber bundle that is locally ordinary and globally twisted.

A fiber bundle has a base space and a fiber sitting above each point. For a vector bundle, every fiber is a vector space of the same finite dimension. Over a sufficiently small open set, we can choose a trivialization: a smooth way to identify all the fibers there with a fixed vector space. The word local matters. The entire bundle need not admit one such identification covering the whole base.

## Two local descriptions of the same fiber

Suppose two trivializations overlap. Each one assigns coordinates to vectors in the same fiber. On the overlap, converting from one set of coordinates to the other is an invertible linear map. The map depends smoothly on the base point. Such maps are called transition functions.

For a real line bundle, the transition function is a nonzero real number at each point of the overlap. For a complex line bundle, it is a nonzero complex number. For a rank-r real vector bundle, it is an invertible r-by-r real matrix. These are not extra arbitrary decorations on top of a bundle. They encode how the different local product pictures fit together.

If three trivializations overlap, converting coordinates from the first to the third directly must agree with converting through the second. This compatibility is the cocycle condition. Without it, a journey through different charts could produce inconsistent fiber coordinates depending on the sequence of charts used. With it, one can build a global bundle by gluing local products according to the transition functions.

## The Mobius line bundle

Think of the Mobius band as a real line bundle over a circle, with the fiber an entire copy of the real line rather than only a narrow paper interval. Start from the product of an interval of angles and the real line, and identify the two ends so that the fiber coordinate changes sign: the vector t at the first end is identified with the vector negative t at the other end.

Locally nothing went wrong. Every short arc of the circle has a product neighborhood. Globally, after one complete circuit, the chosen real basis of the fiber reverses orientation. Could we choose a continuous, nowhere-zero vector in each fiber, making a global basis? Suppose we could. In the interval description it would be a continuous nonzero real-valued function that must change sign between the endpoints under the gluing rule. By the intermediate value theorem, it would have to vanish somewhere. That contradiction shows there is no global nonzero section, and therefore no global product trivialization as a real line bundle.

Notice a refinement. For two overlapping arcs covering the circle, their intersection has two disconnected pieces. One can use a transition function with opposite signs on those components. It would be wrong to summarize the Mobius twist as one globally defined nonzero real function that continuously changes from positive to negative on a connected overlap. Such a sign change would have to pass through zero and cease to be invertible. The disconnected overlap is how the topology enters.

## Gauge choices are not physical twists

A local trivialization is not unique. On any patch we may change the basis of the fiber by a smoothly varying invertible matrix. This changes the transition functions according to the corresponding basis changes. Two sets of transition data related in this way describe isomorphic bundles. A complicated transition matrix may be removable by choosing better frames. Its mere complexity does not establish genuine global twisting.

For a real line bundle over the circle, the important information is the sign accumulated around a circuit. A real line bundle with no sign reversal is trivial; one with sign reversal is the Mobius type. Complex line bundles over the circle behave differently: because nonzero complex numbers can be continuously rotated from one phase to another, all complex line bundles over the circle are topologically trivial. The scalar field changes the possible twisting.

## A two-dimensional base can support another kind of twist

Now cover a sphere by northern and southern disk-like patches whose overlap is an equatorial band. Consider complex line fibers and choose a frame on each patch. On the overlap, let the southern frame rotate in complex phase once as we go around the equator, relative to the northern frame. The phase does not come back having traced a contractible loop in the nonzero complex numbers: its winding number is one.

This construction produces a nontrivial complex line bundle over the sphere. Different integers of phase winding produce different isomorphism classes of complex line bundles over the sphere. This is the clutching construction. Its invariant will later appear as the first Chern number, obtained by integrating a curvature two-form over the sphere.

Why does a complex line bundle over the circle trivialize while a complex line bundle over the sphere may not? The sphere construction glues two disks along an overlap whose essential loop carries the transition map. Its winding cannot necessarily be removed by changing frames over the disks. The topology of the base and the structure group of the fibers interact. We cannot infer one case from the other merely by saying both have circular directions somewhere in the picture.

## Sections and the tangent bundle

A section assigns one vector in the fiber above each point. A vector field on a manifold is a section of its tangent bundle. A local coordinate chart supplies coordinate basis vector fields and therefore a local frame of the tangent bundle. On overlaps, these frames are related by Jacobian matrices. That makes the tangent bundle a particularly important example of transition-function gluing.

Whether a bundle admits a global frame is a global topological question. The tangent bundle of the sphere has local frames in every chart, but there is no smooth nowhere-zero tangent vector field on the two-sphere. That fact, often pictured by the impossibility of combing a hairy ball without a cowlick, is a genuine theorem. It reminds us that a global choice of basis can fail even though every local patch looks harmless.

Bundles separate two kinds of information. The fiber tells us what kind of object can live at a point: a line, a plane, or another vector space. The transition functions tell us how local coordinates on those fibers are identified. The pattern of those identifications determines whether a global trivialization exists. This is what it means for geometry to be locally simple but globally twisted.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Choose local frames \(e_i\) on \(U_i\subset M\) and write \(e_j=e_i g_{ij}\) on overlaps, with \(g_{ij}:U_i\cap U_j\to GL(r,\mathbb F)\). Then
\[g_{ii}=I,\quad g_{ji}=g_{ij}^{-1},\quad g_{ij}g_{jk}=g_{ik}\text{ on triple overlaps}.\]
A change of frame \(e'_i=e_i h_i\) yields \(g'_{ij}=h_i^{-1}g_{ij}h_j\). The equivalence class of transition data, not an individual matrix entry, represents the bundle.

**Mobius line bundle:** \(E=([0,2\pi]\times\mathbb R)/((0,t)\sim(2\pi,-t))\). A nonvanishing section would yield a nonzero continuous function \(f:[0,2\pi]\to\mathbb R\) with \(f(2\pi)=-f(0)\), impossible by the intermediate value theorem.

**Complex lines on \(S^2\):** two disk trivializations glue on the equator through \(g:S^1\to U(1)\), \(g(e^{i\phi})=e^{in\phi}\). The homotopy class is its integer degree \(n\); fixing orientation and frame conventions fixes the sign of the associated Chern number.

### Check your understanding

1. Why must transition matrices be invertible? **Answer:** they describe changes of basis within the same fiber.
2. Is a nonconstant transition function automatically evidence of a nontrivial bundle? **No:** a change of local frames may simplify it to the identity.
3. Why is the complex Mobius-looking gluing over \(S^1\) trivializable? **Answer:** the complex frame can rotate continuously to absorb the sign; complex line bundles over \(S^1\) are trivial.

### Reading and sources

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html), transition functions, clutching construction and characteristic classes.
- Overview: [Vector bundle](https://en.wikipedia.org/wiki/Vector_bundle), [Clutching construction](https://en.wikipedia.org/wiki/Clutching_construction), [Mobius strip](https://en.wikipedia.org/wiki/M%C3%B6bius_strip).
