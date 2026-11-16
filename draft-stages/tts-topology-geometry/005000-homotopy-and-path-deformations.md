# 005000 — Homotopy: When Paths Count as the Same Route

**Track:** Topology and Geometry. **Background:** continuous maps, connectedness, quotient spaces. **Question:** how can continuous deformation turn loops into algebra?

<!-- BEGIN SPOKEN LECTURE -->

# Homotopy: When Paths Count as the Same Route

A path around a lake can be long, short, smooth, or jagged. If we can slide it continuously without ever passing through the water, we might want to regard all those versions as the same essential route. But a path that winds around the lake once cannot simply shrink to a point while remaining on dry land. The obstacle is not the path's length or shape. It is the hole in the space of allowed positions.

Topology makes the idea precise with homotopy: a continuous family of paths or maps interpolating between two choices. From this apparently geometric operation we can build a group, and the group detects something that ordinary connectedness misses.

## Paths remember endpoints

A path in a topological space X is a continuous function from the closed unit interval into X. Its value at zero is the starting point, and its value at one is the endpoint. A loop based at a point p is a path starting and ending at p.

We want to compare two paths with the same endpoints. A path homotopy relative to endpoints is a continuous function of two variables: one variable moves along the path, the other runs from the original path to the final path. At deformation time zero we see the first path; at time one, the second. At every intermediate time, the path must keep its starting and ending points fixed.

That last requirement is essential. If we allowed the base point to wander freely, we could move loops into different locations and might inadvertently identify loops whose *based* behavior differs. There is a related notion of free homotopy in which endpoints are not fixed, but the group we are about to construct needs based loops.

Imagine two arcs from the same start to the same finish in a flat disk. If the disk is convex, the straight-line interpolation between corresponding points of the two arcs stays inside the disk. That interpolation is a path homotopy with fixed endpoints. So every two paths in a convex disk with the same endpoints are homotopic relative to endpoints.

An open annulus is different. A loop once around the missing center cannot be deformed to a constant loop without leaving the annulus. To prove this rather than merely draw it, we will later use a numerical winding invariant. For now the example motivates the distinction between connectedness and the ability to contract loops.

## Joining paths and reversing them

Suppose one path ends where another begins. We can concatenate them: travel along the first path during the first half of the time interval, then along the second during the second half. We can also reverse a path by traversing it backward.

At the level of parametrized paths, concatenation is not literally associative. Joining the first two paths and then the third allocates different amounts of time than joining the last two and then the first. But these two parametrizations differ by a continuous change of speed, and they are path-homotopic relative to endpoints. Similarly, walking around a loop and immediately retracing it is homotopic to staying still at the base point: the out-and-back excursion can be compressed until its distance along the original loop goes to zero.

These observations are enough to make a group out of equivalence classes. Two loops are equivalent when they are path-homotopic relative to the base point. Define multiplication by concatenation. The constant loop is the identity class; reversing a loop gives its inverse class; and associativity holds after passing to homotopy classes. The resulting group is the fundamental group of X at p, commonly written pi one of X at p.

A group has emerged from continuous deformations, not from a pre-existing arithmetic operation. That is the central idea of algebraic topology: assign an algebraic object to a topological space in a way that behaves predictably under continuous maps.

## Why the construction is well-defined

There is a hidden obligation whenever we define an operation on equivalence classes. Suppose the first loop is replaced by a homotopic loop and the second by another homotopic loop. Is the concatenation class unchanged? Yes. Apply the first homotopy on the first half of the interval and the second homotopy on the second half. The glued deformation is continuous because the loops share the base point at the joining time. This proves multiplication is well-defined on homotopy classes.

The same issue arises for inverses: reversing a path homotopy gives a path homotopy between the reversed loops. A new topological construction must survive these representative choices before it can legitimately be called a group.

## Spaces with no essential loops

A path-connected space whose fundamental group is trivial is called simply connected. In such a space, every based loop can be deformed to the constant loop. A space can be path connected and still fail this test, as a circle or a punctured plane does.

Convex subsets of Euclidean space are simply connected. In fact they are contractible: choose a center point and slide every point of the space toward it along the straight line connecting them. This contracts the identity map to a constant map. Star-shaped sets admit a similar contraction with a chosen star center. Contractibility is stronger than simple connectedness, because it concerns a deformation of the whole space, not just loops.

A useful example is a solid disk versus a circle. Both are path connected. The solid disk can be contracted to its center. A circle cannot be contracted within itself; its loops have winding information that survives deformation. Another example is a punctured plane, which can be deformed onto a circle by radially pushing each point onto the unit circle. Such a deformation retraction means the two spaces have the same homotopy behavior for loops.

We must be precise about the last statement. A deformation retraction supplies maps back and forth whose compositions are homotopic to the relevant identities, while respecting the chosen base point when appropriate. These maps induce inverse isomorphisms of fundamental groups. A deformation retraction need not preserve distances, angles, or the shapes of paths. It preserves the algebraic information encoded by their homotopy classes.

## Continuous maps carry loops into loops

Suppose f is a continuous map from X to Y, sending base point p to q. A loop in X becomes a loop in Y by applying f at every point along the route. A homotopy in X becomes a homotopy in Y after composing with f. Therefore f induces a homomorphism from the fundamental group of X at p to that of Y at q. Concatenation is preserved because applying f before or after joining the two paths produces the same parametrized route.

This is called functorial behavior. The abstract group is not merely an arbitrary label attached to a space: continuous maps induce compatible group homomorphisms, and composing maps composes the induced homomorphisms. A homeomorphism therefore induces an isomorphism of fundamental groups.

This gives a method for proving spaces are not homeomorphic. If their fundamental groups are not isomorphic, no homeomorphism can exist. The converse is false: equal fundamental groups do not guarantee equal topology, nor even equal higher-dimensional homotopy information.

## From deformation to detection

The definition of pi one is already useful, but an abstract group defined by classes of all possible loops is hard to compute directly. The next task is to make the idea numerical in a particular space. On a circle, every based loop has an integer winding number. That integer will not change under homotopy, and every integer will occur. The group of loops becomes the additive group of integers.

This is the first example of a pattern that reappears throughout mathematics: a geometric obstruction becomes an algebraic invariant. The invariant cannot capture everything about a space, but it can decisively prevent a deformation we might otherwise imagine possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(p,q\in X\), paths \(\alpha,\beta:I\to X\) from \(p\) to \(q\) are **path-homotopic rel endpoints** if \(H:I\times I\to X\) is continuous with \(H(s,0)=\alpha(s)\), \(H(s,1)=\beta(s)\), \(H(0,t)=p\), \(H(1,t)=q\).

**Based fundamental group:** \(\pi_1(X,p)\) consists of based-loop classes under concatenation
\[
(\alpha*\beta)(t)=\begin{cases}\alpha(2t)&0\le t\le1/2,\\\beta(2t-1)&1/2\le t\le1.\end{cases}
\]
Associativity, identity, and inverses hold **up to path homotopy**, not as literal equalities of parametrized paths.

**Contraction:** A set \(X\subset\mathbb R^n\) star-shaped about \(c\) has \(H(x,t)=(1-t)x+tc\), giving a contraction to \(c\). A punctured plane deformation retracts onto the unit circle via \(H(x,t)=((1-t)+t/\lVert x\rVert)x\).

### Exercises with answers

1. Why is every convex nonempty subset of \(\mathbb R^n\) simply connected? **Answer:** straight-line contraction makes it contractible.
2. Why does a homeomorphism induce an isomorphism of fundamental groups? **Answer:** it and its inverse induce mutually inverse maps on loop classes.
3. Is concatenation strictly associative as a path operation? **Answer:** no, only up to endpoint-preserving homotopy.
4. Why must a based loop homotopy keep the base point fixed? **Answer:** otherwise we obtain free homotopy, which does not directly define the same based-loop group operation.

### Reading

Allen Hatcher, [Algebraic Topology, Chapter 1](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), fundamental groups and homotopy; MIT OCW, [Introduction to Topology](https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/), background in quotient maps and path connectivity.
