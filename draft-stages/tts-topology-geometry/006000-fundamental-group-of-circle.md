# 006000 — The Fundamental Group of the Circle and Winding Numbers

**Track:** Topology and Geometry. **Background:** paths, homotopy, continuous maps, integers. **Question:** how can a loop have an integer that no continuous deformation changes?

<!-- BEGIN SPOKEN LECTURE -->

# The Fundamental Group of the Circle and Winding Numbers

A loop that travels around a circle once can return to its starting point, as can a loop that travels twice, or once in the opposite direction. All three loops have the same endpoints and live in the same connected space. Yet they are topologically different. The distinction can be expressed by an integer: one, two, or negative one. We want to prove that this integer does not change under a deformation that keeps the base point fixed.

The fundamental group of the circle is the additive group of integers. This is not a guess suggested by pictures. We can derive it by relating the circle to the real line, where paths are easier to understand.

## Unwrapping the circle

Represent the circle by complex numbers of absolute value one. Map a real number t to the point on the circle with angle two pi times t. Increasing t by one complete unit goes once around and returns to the same point. Different real numbers can map to the same point: t, t plus one, t minus one, and every other integer translate all represent the same position on the circle.

This map from the real line onto the circle is a covering map. Each sufficiently small arc of the circle has a collection of disjoint intervals above it, each interval mapping homeomorphically onto the arc. Locally we can unwrap the circle without ambiguity. Globally, no single continuous choice of angle works for every point of the circle at once.

Now take a continuous path on the circle and choose a real number above its starting point. There is a unique continuous path on the real line beginning at that real number and projecting to the original circle path. We call this the lifted path. The idea is to follow an angle continuously rather than repeatedly resetting it whenever the circle goes through a full turn.

Why can we lift the whole path? The original path has a compact time interval as its domain. Cover its image by small arcs over which continuous angle branches exist, then divide the time interval into finitely many sufficiently short pieces that each sits in such an arc. On each piece choose the branch agreeing with the previously constructed lift at the shared endpoint. Local uniqueness makes the choices fit together. This is the path-lifting property of the covering map.

## Winding is an endpoint difference

Suppose our circle path is a loop based at the point one, and start its lift at real number zero. Because the circle path ends at the same point, the lifted endpoint must be an integer. Define the winding number of the loop to be that integer.

The loop that stays at one has winding zero. A counterclockwise traversal has winding one. A clockwise traversal has winding negative one. Twice counterclockwise has winding two. If we concatenate two based loops, their lifts concatenate after translating the second one by the integer endpoint of the first. Thus winding numbers add.

Why is this integer unchanged by path homotopy? A homotopy of loops on the circle can be lifted continuously once the starting edge is fixed at real zero. The lifted endpoints vary continuously with the deformation parameter. But each endpoint must be an integer, and a continuous map from an interval to the discrete set of integers is constant. Hence all homotopic based loops have the same winding number.

We can now prove injectivity as well as invariance. Suppose two based loops have the same winding number. Their lifts start at zero and end at the same integer. The real line is convex, so straight-line interpolation between the two lifted paths is a homotopy holding both endpoints fixed. Project that interpolation back down to the circle. This gives a based homotopy of the original loops. Thus equal winding numbers mean equal fundamental-group classes.

Surjectivity is easy: for every integer n, the loop that makes n complete signed turns has winding n. Consequently the map from the fundamental group of the circle to the integers is a bijective group homomorphism. The circle's fundamental group is the integers under addition.

## What the computation proves about holes

Consider the punctured plane, the ordinary plane with its origin deleted. Every point has a direction from the origin, and a radial deformation retract moves it to the unit circle without touching the missing point. Therefore the punctured plane has the same fundamental group as the circle: the integers. A loop winding once around the missing origin cannot shrink to a point while avoiding the origin, because such a shrinking would change its winding number from one to zero.

By contrast, a loop in the full plane can shrink linearly to its base point; the plane is contractible and has trivial fundamental group. Thus the plane and the punctured plane are not homeomorphic, even though both are path connected and locally look like ordinary planar regions away from the puncture.

An annulus, a disk with a smaller concentric disk removed, also deformation retracts to a circle and has fundamental group the integers. The exact radius of the missing region is irrelevant for this invariant. What matters is the persistent possibility of winding around it.

However, a single hole is not a universal geometric interpretation of every fundamental group element. Spaces with several punctures, knots, or more complicated identifications can have noncommutative fundamental groups. The circle is a particularly clean first example because its universal covering space is the real line and its loop classes are completely determined by a single integer.

## Maps between circles have a degree

Consider the continuous map from the circle to itself that sends a point z to z raised to the n-th power, where n is any integer. For n positive it wraps the circle around itself n times; for n negative it also reverses orientation. On fundamental groups, this map sends the integer k to n times k. In particular, it sends the generator one to n.

More generally, every continuous map from the circle to itself has an integer degree. To compute it, follow a full circuit of the source circle, lift the resulting path in the target circle, and measure the total change in angle. Homotopic maps have the same degree. In fact, for maps of circles, equal degree is enough to ensure homotopy, without insisting that a chosen base point be fixed. So the integers classify homotopy classes of maps from the circle to itself.

This degree is a first appearance of an idea that extends to spheres and manifolds: count how a map wraps an oriented space around another. It is not a notion of metric length, and it need not imply a one-to-one correspondence of points. A map can fold and reverse direction in parts while retaining a well-defined net degree.

## Why the covering space matters

On the circle itself, loops can seem hard to distinguish because every loop comes back to the same position. In the real line above it, a lifted loop becomes a path with a visible endpoint displacement. Continuous deformation cannot change which integer translate it reaches. The covering construction turns a global topological obstruction into ordinary arithmetic on the real line.

This illustrates why algebraic topology is more than a vocabulary for holes. We use a geometric construction, the covering map, to obtain an invariant, the winding number, and then prove a classification theorem. In subsequent work, covering spaces can classify subgroups of fundamental groups and connect geometry back to the subgroup machinery of algebra.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The covering map \(p:\mathbb R\to S^1\) is \(p(t)=e^{2\pi i t}\). Let \(\gamma:I\to S^1\) be based at \(1\). There is a unique lift \(\widetilde\gamma:I\to\mathbb R\) with \(\widetilde\gamma(0)=0\). Then \(\widetilde\gamma(1)\in\mathbb Z\), and
\[
\operatorname{wind}([\gamma])=\widetilde\gamma(1),\qquad
\operatorname{wind}:\pi_1(S^1,1)\xrightarrow{\cong}(\mathbb Z,+).
\]

**Proof:** homotopy lifting makes the integer endpoint invariant under based homotopy; linear homotopy of lifts with equal endpoints proves injectivity; loops \(t\mapsto e^{2\pi int}\) give every integer. Concatenation adds integer endpoints.

**Retraction:** \(\mathbb R^2\setminus\{0\}\to S^1\), \(x\mapsto x/\lVert x\rVert\), extends to a deformation retraction.

**Degree:** \(f_n:S^1\to S^1\), \(f_n(z)=z^n\), induces \((f_n)_*(k)=nk\) on \(\pi_1(S^1)\). Homotopy classes \([S^1,S^1]\cong\mathbb Z\) are classified by degree.

### Exercises with answers

1. What is the winding number of a loop that goes twice clockwise and once counterclockwise? **Answer:** negative one.
2. Why can no based homotopy contract a winding-one circle loop? **Answer:** it would change the integer lift endpoint from one to zero.
3. What does \(z\mapsto z^{-3}\) do to the fundamental group? **Answer:** it multiplies each integer by negative three.
4. What is \(\pi_1(\mathbb R^2\setminus\{0\})\)? **Answer:** \(\mathbb Z\), by deformation retraction onto the circle.

### Reading

Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html), Chapter 1, covering spaces, fundamental group of a circle and winding numbers.
