# Paths, winding, and covering spaces

<!-- BEGIN SPOKEN LECTURE -->

# Paths, winding, and covering spaces

## Homotopy: When Paths Count as the Same Route

A path around a lake can be long, short, smooth, or jagged. If we can slide it continuously without ever passing through the water, we might want to regard all those versions as the same essential route. But a path that winds around the lake once cannot simply shrink to a point while remaining on dry land. The obstacle is not the path's length or shape. It is the hole in the space of allowed positions.

Topology makes the idea precise with homotopy: a continuous family of paths or maps interpolating between two choices. From this apparently geometric operation we can build a group, and the group detects something that ordinary connectedness misses.

### Paths remember endpoints

A path in a topological space X is a continuous function from the closed unit interval into X. Its value at zero is the starting point, and its value at one is the endpoint. A loop based at a point p is a path starting and ending at p.

We want to compare two paths with the same endpoints. A path homotopy relative to endpoints is a continuous function of two variables: one variable moves along the path, the other runs from the original path to the final path. At deformation time zero we see the first path; at time one, the second. At every intermediate time, the path must keep its starting and ending points fixed.

That last requirement is essential. If we allowed the base point to wander freely, we could move loops into different locations and might inadvertently identify loops whose *based* behavior differs. There is a related notion of free homotopy in which endpoints are not fixed, but the group we are about to construct needs based loops.

Imagine two arcs from the same start to the same finish in a flat disk. If the disk is convex, the straight-line interpolation between corresponding points of the two arcs stays inside the disk. That interpolation is a path homotopy with fixed endpoints. So every two paths in a convex disk with the same endpoints are homotopic relative to endpoints.

An open annulus is different. A loop once around the missing center cannot be deformed to a constant loop without leaving the annulus. To prove this rather than merely draw it, we will later use a numerical winding invariant. For now the example motivates the distinction between connectedness and the ability to contract loops.

### Joining paths and reversing them

Suppose one path ends where another begins. We can concatenate them: travel along the first path during the first half of the time interval, then along the second during the second half. We can also reverse a path by traversing it backward.

At the level of parametrized paths, concatenation is not literally associative. Joining the first two paths and then the third allocates different amounts of time than joining the last two and then the first. But these two parametrizations differ by a continuous change of speed, and they are path-homotopic relative to endpoints. Similarly, walking around a loop and immediately retracing it is homotopic to staying still at the base point: the out-and-back excursion can be compressed until its distance along the original loop goes to zero.

These observations are enough to make a group out of equivalence classes. Two loops are equivalent when they are path-homotopic relative to the base point. Define multiplication by concatenation. The constant loop is the identity class; reversing a loop gives its inverse class; and associativity holds after passing to homotopy classes. The resulting group is the fundamental group of X at p, commonly written pi one of X at p.

A group has emerged from continuous deformations, not from a pre-existing arithmetic operation. That is the central idea of algebraic topology: assign an algebraic object to a topological space in a way that behaves predictably under continuous maps.

### Why the construction is well-defined

There is a hidden obligation whenever we define an operation on equivalence classes. Suppose the first loop is replaced by a homotopic loop and the second by another homotopic loop. Is the concatenation class unchanged? Yes. Apply the first homotopy on the first half of the interval and the second homotopy on the second half. The glued deformation is continuous because the loops share the base point at the joining time. This proves multiplication is well-defined on homotopy classes.

The same issue arises for inverses: reversing a path homotopy gives a path homotopy between the reversed loops. A new topological construction must survive these representative choices before it can legitimately be called a group.

### Spaces with no essential loops

A path-connected space whose fundamental group is trivial is called simply connected. In such a space, every based loop can be deformed to the constant loop. A space can be path connected and still fail this test, as a circle or a punctured plane does.

Convex subsets of Euclidean space are simply connected. In fact they are contractible: choose a center point and slide every point of the space toward it along the straight line connecting them. This contracts the identity map to a constant map. Star-shaped sets admit a similar contraction with a chosen star center. Contractibility is stronger than simple connectedness, because it concerns a deformation of the whole space, not just loops.

A useful example is a solid disk versus a circle. Both are path connected. The solid disk can be contracted to its center. A circle cannot be contracted within itself; its loops have winding information that survives deformation. Another example is a punctured plane, which can be deformed onto a circle by radially pushing each point onto the unit circle. Such a deformation retraction means the two spaces have the same homotopy behavior for loops.

We must be precise about the last statement. A deformation retraction supplies maps back and forth whose compositions are homotopic to the relevant identities, while respecting the chosen base point when appropriate. These maps induce inverse isomorphisms of fundamental groups. A deformation retraction need not preserve distances, angles, or the shapes of paths. It preserves the algebraic information encoded by their homotopy classes.

### Continuous maps carry loops into loops

Suppose f is a continuous map from X to Y, sending base point p to q. A loop in X becomes a loop in Y by applying f at every point along the route. A homotopy in X becomes a homotopy in Y after composing with f. Therefore f induces a homomorphism from the fundamental group of X at p to that of Y at q. Concatenation is preserved because applying f before or after joining the two paths produces the same parametrized route.

This is called functorial behavior. The abstract group is not merely an arbitrary label attached to a space: continuous maps induce compatible group homomorphisms, and composing maps composes the induced homomorphisms. A homeomorphism therefore induces an isomorphism of fundamental groups.

This gives a method for proving spaces are not homeomorphic. If their fundamental groups are not isomorphic, no homeomorphism can exist. The converse is false: equal fundamental groups do not guarantee equal topology, nor even equal higher-dimensional homotopy information.

### From deformation to detection

The definition of pi one is already useful, but an abstract group defined by classes of all possible loops is hard to compute directly. The next task is to make the idea numerical in a particular space. On a circle, every based loop has an integer winding number. That integer will not change under homotopy, and every integer will occur. The group of loops becomes the additive group of integers.

This is the first example of a pattern that reappears throughout mathematics: a geometric obstruction becomes an algebraic invariant. The invariant cannot capture everything about a space, but it can decisively prevent a deformation we might otherwise imagine possible.

## The Fundamental Group of the Circle and Winding Numbers

A loop that travels around a circle once can return to its starting point, as can a loop that travels twice, or once in the opposite direction. All three loops have the same endpoints and live in the same connected space. Yet they are topologically different. The distinction can be expressed by an integer: one, two, or negative one. We want to prove that this integer does not change under a deformation that keeps the base point fixed.

The fundamental group of the circle is the additive group of integers. This is not a guess suggested by pictures. We can derive it by relating the circle to the real line, where paths are easier to understand.

### Unwrapping the circle

Represent the circle by complex numbers of absolute value one. Map a real number t to the point on the circle with angle two pi times t. Increasing t by one complete unit goes once around and returns to the same point. Different real numbers can map to the same point: t, t plus one, t minus one, and every other integer translate all represent the same position on the circle.

This map from the real line onto the circle is a covering map. Each sufficiently small arc of the circle has a collection of disjoint intervals above it, each interval mapping homeomorphically onto the arc. Locally we can unwrap the circle without ambiguity. Globally, no single continuous choice of angle works for every point of the circle at once.

Now take a continuous path on the circle and choose a real number above its starting point. There is a unique continuous path on the real line beginning at that real number and projecting to the original circle path. We call this the lifted path. The idea is to follow an angle continuously rather than repeatedly resetting it whenever the circle goes through a full turn.

Why can we lift the whole path? The original path has a compact time interval as its domain. Cover its image by small arcs over which continuous angle branches exist, then divide the time interval into finitely many sufficiently short pieces that each sits in such an arc. On each piece choose the branch agreeing with the previously constructed lift at the shared endpoint. Local uniqueness makes the choices fit together. This is the path-lifting property of the covering map.

### Winding is an endpoint difference

Suppose our circle path is a loop based at the point one, and start its lift at real number zero. Because the circle path ends at the same point, the lifted endpoint must be an integer. Define the winding number of the loop to be that integer.

The loop that stays at one has winding zero. A counterclockwise traversal has winding one. A clockwise traversal has winding negative one. Twice counterclockwise has winding two. If we concatenate two based loops, their lifts concatenate after translating the second one by the integer endpoint of the first. Thus winding numbers add.

Why is this integer unchanged by path homotopy? A homotopy of loops on the circle can be lifted continuously once the starting edge is fixed at real zero. The lifted endpoints vary continuously with the deformation parameter. But each endpoint must be an integer, and a continuous map from an interval to the discrete set of integers is constant. Hence all homotopic based loops have the same winding number.

We can now prove injectivity as well as invariance. Suppose two based loops have the same winding number. Their lifts start at zero and end at the same integer. The real line is convex, so straight-line interpolation between the two lifted paths is a homotopy holding both endpoints fixed. Project that interpolation back down to the circle. This gives a based homotopy of the original loops. Thus equal winding numbers mean equal fundamental-group classes.

Surjectivity is easy: for every integer n, the loop that makes n complete signed turns has winding n. Consequently the map from the fundamental group of the circle to the integers is a bijective group homomorphism. The circle's fundamental group is the integers under addition.

### What the computation proves about holes

Consider the punctured plane, the ordinary plane with its origin deleted. Every point has a direction from the origin, and a radial deformation retract moves it to the unit circle without touching the missing point. Therefore the punctured plane has the same fundamental group as the circle: the integers. A loop winding once around the missing origin cannot shrink to a point while avoiding the origin, because such a shrinking would change its winding number from one to zero.

By contrast, a loop in the full plane can shrink linearly to its base point; the plane is contractible and has trivial fundamental group. Thus the plane and the punctured plane are not homeomorphic, even though both are path connected and locally look like ordinary planar regions away from the puncture.

An annulus, a disk with a smaller concentric disk removed, also deformation retracts to a circle and has fundamental group the integers. The exact radius of the missing region is irrelevant for this invariant. What matters is the persistent possibility of winding around it.

However, a single hole is not a universal geometric interpretation of every fundamental group element. Spaces with several punctures, knots, or more complicated identifications can have noncommutative fundamental groups. The circle is a particularly clean first example because its universal covering space is the real line and its loop classes are completely determined by a single integer.

### Maps between circles have a degree

Consider the continuous map from the circle to itself that sends a point z to z raised to the n-th power, where n is any integer. For n positive it wraps the circle around itself n times; for n negative it also reverses orientation. On fundamental groups, this map sends the integer k to n times k. In particular, it sends the generator one to n.

More generally, every continuous map from the circle to itself has an integer degree. To compute it, follow a full circuit of the source circle, lift the resulting path in the target circle, and measure the total change in angle. Homotopic maps have the same degree. In fact, for maps of circles, equal degree is enough to ensure homotopy, without insisting that a chosen base point be fixed. So the integers classify homotopy classes of maps from the circle to itself.

This degree is a first appearance of an idea that extends to spheres and manifolds: count how a map wraps an oriented space around another. It is not a notion of metric length, and it need not imply a one-to-one correspondence of points. A map can fold and reverse direction in parts while retaining a well-defined net degree.

### Why the covering space matters

On the circle itself, loops can seem hard to distinguish because every loop comes back to the same position. In the real line above it, a lifted loop becomes a path with a visible endpoint displacement. Continuous deformation cannot change which integer translate it reaches. The covering construction turns a global topological obstruction into ordinary arithmetic on the real line.

This illustrates why algebraic topology is more than a vocabulary for holes. We use a geometric construction, the covering map, to obtain an invariant, the winding number, and then prove a classification theorem. In subsequent work, covering spaces can classify subgroups of fundamental groups and connect geometry back to the subgroup machinery of algebra.

## Covering Spaces: Local Copies and Global Winding

A circle can be unwrapped onto a line. Map each real number to the point on the circle reached by turning through that many revolutions. Real numbers that differ by an integer map to the same point. Yet near any one point on the circle, we can select a small arc and find that its preimage is a disjoint collection of intervals, each of which maps perfectly onto the arc.

This is the defining idea of a covering space. Globally, the map may wrap one space around another many times. Locally, each small region downstairs has separate copies upstairs. Paths can be followed from one sheet to another, and the way they move between sheets records the global topology of the base space.

Let us call the map from the covering space E to the base space X by p. It is a covering map if every point of X has an open neighborhood U whose entire preimage is a disjoint union of open sets, each mapped homeomorphically onto U by p. We say U is evenly covered.

The requirement concerns the full preimage, not just a small neighborhood of one particular point upstairs. A map can be a local homeomorphism without satisfying the stronger global covering condition.

### Finite and infinite sheets

For a positive integer n, consider the map from the circle to itself that raises a complex number of unit magnitude to its nth power. Every point on the target has n preimages. Over a sufficiently small target arc, these preimages lie in n separate arcs, each mapped homeomorphically onto the chosen arc. We call this an n-sheeted covering.

If the starting circle winds once, its image winds n times. On fundamental groups, the induced map sends an integer k to n times k. The subgroup of winding numbers downstairs that come from closed loops upstairs is therefore the multiples of n.

The real line covering the circle has infinitely many sheets. A closed loop downstairs with winding number one lifts to a path upstairs whose endpoint is one unit away from its starting point. It does not lift to a closed loop. Only loops of winding number zero can lift to closed loops with that chosen starting point.

This gives a way to see subgroup information in a geometric picture. The circle covering itself n times corresponds to the subgroup of integers divisible by n. The real-line covering corresponds to the zero subgroup. The identity covering corresponds to all the integers.

### Uniqueness of a lifted path

Suppose a continuous path in X begins at a point x, and we choose one of the points upstairs lying over x. Can we find a path upstairs that projects to the given path and begins at our chosen point? For a covering map, yes, and the lift is unique.

Here is the argument. The path lives on a compact interval of time. Around each time, choose an evenly covered neighborhood containing the path's current position. Compactness allows us to divide the full time interval into finitely many smaller subintervals whose path images lie in such neighborhoods. Start with the chosen point upstairs. On the first subinterval, we use the unique inverse of p on its sheet. At the next endpoint, choose the sheet that contains where the previous lift arrived. Continue. The constructed segments agree at their boundaries. Local uniqueness of the inverse maps also proves that no other lift with the same initial point can diverge from it.

Now imagine continuously deforming one path into another while keeping their endpoints fixed. The covering-space homotopy-lifting property lets us lift that whole deformation once its initial lift has been selected. Because the fiber over a point is discrete, the endpoint of a lifted path cannot jump continuously from one sheet to another. Consequently homotopic based loops have lifts with the same endpoint.

This is exactly what made winding number invariant under homotopy in the previous circle calculation. Covering spaces generalize the mechanism.

### A lifting criterion

Take a continuous map from a path-connected, locally path-connected space Y into X, and choose a proposed lift of one base point. When can the whole map be lifted to E?

The answer is controlled by fundamental groups. A lift exists exactly when every loop in Y, after mapping into X, belongs to the subgroup represented by loops in E under p. In symbols, the induced image of the fundamental group of Y must be contained in the subgroup contributed by the covering map. We must use compatible base points; ignoring that choice can obscure a conjugation.

The necessity is clear. If we can lift the entire map, then the image of any closed loop in Y lifts to a closed loop in E. For sufficiency, choose a path in Y from the base point to a point y, map it into X, lift that path, and use its endpoint to define the lifted value at y. The fundamental-group condition ensures that choosing another path gives the same endpoint. Local path connectedness and the evenly covered neighborhoods then supply continuity.

For example, a continuous map from a simply connected domain into the circle has a continuous real-valued angle lift after we choose an initial angle. A map from the circle to itself of degree one cannot have such a global lift to the real line. Its fundamental group maps a generator to one, which does not belong to the zero subgroup coming from the real-line covering.

### Deck transformations

A deck transformation is a homeomorphism of the covering space to itself that leaves the projection p unchanged. For the real line over the circle, deck transformations include translations by integers. In fact those are all the deck transformations, and they form a group isomorphic to the integers.

For the n-fold circle cover, deck transformations are rotations by nth roots of unity, forming a cyclic group of order n. They permute the sheets without changing points downstairs. For more general coverings, the deck group need not act transitively on each fiber; coverings for which it does are often called regular or normal.

When X has a suitable universal cover, these symmetries are tightly connected to its fundamental group. With choices of base points, the deck group of the universal cover is naturally identifiable with the fundamental group, up to conventional choices about multiplication order. The universal cover is simply connected and serves as a reference from which other connected coverings can be constructed.

### Which subgroups correspond to coverings?

There is a beautiful classification theorem, but its hypotheses must be said aloud. If X is path-connected, locally path-connected, and semilocally simply connected, then it has a universal covering space. The connected covering spaces of X, considered up to equivalence, correspond to conjugacy classes of subgroups of its fundamental group. If we also choose base points upstairs, the correspondence becomes one with actual subgroups rather than conjugacy classes.

The subgroup records which loops downstairs close when lifted. A smaller subgroup corresponds to a covering with more sheets, where fewer loops close upstairs. For the circle, every subgroup of the integers has the form n times the integers, including the zero subgroup. We have already met all the resulting connected covering spaces: the finite-degree circle maps and the real line.

Not every topological space satisfies the local hypotheses. Spaces with loops accumulating at smaller and smaller scales can fail to admit the ordinary universal covering described here. The classification theorem is not a universal statement about arbitrary spaces.

Covering theory converts a global problem about paths into algebra about subgroups. It also illustrates a theme that will recur in geometry: local behavior can look completely standard while global gluing or winding produces structure that cannot be seen in any single small neighborhood.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Homotopy: When Paths Count as the Same Route

**Track:** Topology and Geometry. **Background:** continuous maps, connectedness, quotient spaces. **Question:** how can continuous deformation turn loops into algebra?

#### Mathematical companion (not spoken)

For \(p,q\in X\), paths \(\alpha,\beta:I\to X\) from \(p\) to \(q\) are **path-homotopic rel endpoints** if \(H:I\times I\to X\) is continuous with \(H(s,0)=\alpha(s)\), \(H(s,1)=\beta(s)\), \(H(0,t)=p\), \(H(1,t)=q\).

**Based fundamental group:** \(\pi_1(X,p)\) consists of based-loop classes under concatenation
\[
(\alpha*\beta)(t)=\begin{cases}\alpha(2t)&0\le t\le1/2,\\\beta(2t-1)&1/2\le t\le1.\end{cases}
\]
Associativity, identity, and inverses hold **up to path homotopy**, not as literal equalities of parametrized paths.

**Contraction:** A set \(X\subset\mathbb R^n\) star-shaped about \(c\) has \(H(x,t)=(1-t)x+tc\), giving a contraction to \(c\). A punctured plane deformation retracts onto the unit circle via \(H(x,t)=((1-t)+t/\lVert x\rVert)x\).

##### Exercises with answers

1. Why is every convex nonempty subset of \(\mathbb R^n\) simply connected? **Answer:** straight-line contraction makes it contractible.
2. Why does a homeomorphism induce an isomorphism of fundamental groups? **Answer:** it and its inverse induce mutually inverse maps on loop classes.
3. Is concatenation strictly associative as a path operation? **Answer:** no, only up to endpoint-preserving homotopy.
4. Why must a based loop homotopy keep the base point fixed? **Answer:** otherwise we obtain free homotopy, which does not directly define the same based-loop group operation.

##### Reading

Allen Hatcher, [Algebraic Topology, Chapter 1](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), fundamental groups and homotopy; MIT OCW, [Introduction to Topology](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/), background in quotient maps and path connectivity.

### The Fundamental Group of the Circle and Winding Numbers

**Track:** Topology and Geometry. **Background:** paths, homotopy, continuous maps, integers. **Question:** how can a loop have an integer that no continuous deformation changes?

#### Mathematical companion (not spoken)

The covering map \(p:\mathbb R\to S^1\) is \(p(t)=e^{2\pi i t}\). Let \(\gamma:I\to S^1\) be based at \(1\). There is a unique lift \(\widetilde\gamma:I\to\mathbb R\) with \(\widetilde\gamma(0)=0\). Then \(\widetilde\gamma(1)\in\mathbb Z\), and
\[
\operatorname{wind}([\gamma])=\widetilde\gamma(1),\qquad
\operatorname{wind}:\pi_1(S^1,1)\xrightarrow{\cong}(\mathbb Z,+).
\]

**Proof:** homotopy lifting makes the integer endpoint invariant under based homotopy; linear homotopy of lifts with equal endpoints proves injectivity; loops \(t\mapsto e^{2\pi int}\) give every integer. Concatenation adds integer endpoints.

**Retraction:** \(\mathbb R^2\setminus\{0\}\to S^1\), \(x\mapsto x/\lVert x\rVert\), extends to a deformation retraction.

**Degree:** \(f_n:S^1\to S^1\), \(f_n(z)=z^n\), induces \((f_n)_*(k)=nk\) on \(\pi_1(S^1)\). Homotopy classes \([S^1,S^1]\cong\mathbb Z\) are classified by degree.

##### Exercises with answers

1. What is the winding number of a loop that goes twice clockwise and once counterclockwise? **Answer:** negative one.
2. Why can no based homotopy contract a winding-one circle loop? **Answer:** it would change the integer lift endpoint from one to zero.
3. What does \(z\mapsto z^{-3}\) do to the fundamental group? **Answer:** it multiplies each integer by negative three.
4. What is \(\pi_1(\mathbb R^2\setminus\{0\})\)? **Answer:** \(\mathbb Z\), by deformation retraction onto the circle.

##### Reading

Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), Chapter 1, covering spaces, fundamental group of a circle and winding numbers.

### Covering Spaces: Local Copies and Global Winding

**Track:** Topology and Geometry. **Background:** continuous maps, path homotopy, fundamental groups, and the circle's winding number. **Question:** how can a map look like separate copies of the same space locally while recording genuinely different topology globally?

#### Mathematical companion (not spoken)

A covering \(p:E\to X\) has, for every \(x\in X\), an evenly covered open neighborhood \(U\) with
\[
p^{-1}(U)=\bigsqcup_{\alpha}V_\alpha,
\qquad p|_{V_\alpha}:V_\alpha\stackrel{\cong}{\longrightarrow}U.
\]

**Circle coverings.** For \(p_n:S^1\to S^1\), \(p_n(z)=z^n\) with \(n\ge1\), the induced homomorphism on \(\pi_1(S^1)\cong\mathbb Z\) is multiplication by \(n\), hence has image \(n\mathbb Z\). Its deck group is \(C_n\). For \(p_\infty:\mathbb R\to S^1\), \(p(t)=e^{2\pi it}\), the image of \(\pi_1(\mathbb R)\) is zero and the deck group consists of integer translations.

**Lifting criterion.** Let \(p:(E,e_0)\to(X,x_0)\) be a covering and \(f:(Y,y_0)\to(X,x_0)\) with \(Y\) path-connected and locally path-connected. A based lift \(\widetilde f:Y\to E\) exists iff
\[
f_*\pi_1(Y,y_0)\subseteq p_*\pi_1(E,e_0).
\]

**Classification.** If \(X\) is path-connected, locally path-connected, and semilocally simply connected, equivalence classes of connected pointed covers correspond to subgroups of \(\pi_1(X,x_0)\); forgetting the point upstairs quotients by conjugacy. Normal subgroups correspond to regular connected coverings; their deck groups are the corresponding quotient groups.

##### Exercises with answers

1. Which subgroup of \(\mathbb Z\) corresponds to \(z\mapsto z^4\)? **Answer:** \(4\mathbb Z\).
2. Does \(z\mapsto z^2\) admit a continuous right inverse \(S^1\to S^1\)? **No.** On \(\pi_1\), multiplication by two cannot have a right inverse homomorphism \(\mathbb Z\to\mathbb Z\).
3. What is the deck group of the real-line covering of the circle? **Answer:** integer translations, isomorphic to \(\mathbb Z\).
4. Why are free homotopy classes and based homotopy classes treated differently in the classification? **Answer:** changing a chosen lift/basepoint acts by conjugation on the subgroup.

##### Reading

Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), Chapter 1, sections on covering spaces, path lifting, universal covers, and the classification theorem.
