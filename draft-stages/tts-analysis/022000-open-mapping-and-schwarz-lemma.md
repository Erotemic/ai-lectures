# 022000 — The Open Mapping Theorem and Schwarz's Lemma: Two Forms of Rigidity

**Track:** Analysis from First Principles. **Background:** local factorization of zeros, Rouché's theorem, the maximum modulus principle. **Question:** Why must a nonconstant holomorphic map fill out neighborhoods, and how much can it compress the unit disk?

<!-- BEGIN SPOKEN LECTURE -->

# The Open Mapping Theorem and Schwarz's Lemma: Two Forms of Rigidity

Imagine making a tiny rubber stamp of a region in the complex plane and applying a function to it. A continuous function can crush that region into a line, or even into a single point. A real differentiable function with a degenerate derivative might flatten an entire direction. What if we demand complex differentiability at every point of an open, connected region? A nonconstant holomorphic function cannot flatten an open patch into something with no interior. It must send open sets to open sets.

This is the open mapping theorem. It is closely related to the maximum modulus principle, but it says something geometrically different. The maximum modulus principle rules out an interior magnitude peak; the open mapping theorem insists that a small neighborhood in the input produces a genuine neighborhood in the output. We'll develop the theorem using an example that first appears to violate it, then use the resulting geometric control to derive a precise bound for holomorphic self-maps of the unit disk.

## A derivative can vanish without collapsing a neighborhood

Start with f of z equal to z squared. Its derivative at the origin is zero. If we remembered only the real inverse-function theorem, we might expect trouble. At a point where the derivative vanishes, the map is not locally one-to-one. In fact, z and negative z produce the same square.

Yet look at what the function does to a small disk around zero. A disk of radius one tenth maps onto a disk of radius one hundredth. Every angle in the output is achieved, though the input angles get doubled and different inputs collide. The image has shrunk, but it has not lost its two-dimensional interior.

Contrast this with the map that sends z to its real part, regarded as a complex number with zero imaginary part. That map is continuous and differentiable as a real map on the plane. It sends a disk to an interval on the real axis, which is not open in the complex plane. But it is not holomorphic, because changes in the imaginary input direction are treated differently from changes in the real input direction.

The difference is not merely that z squared has a derivative and the real-part map does not. It is the stronger constraint of complex differentiation at *every nearby point*. Even a critical point of a nonconstant holomorphic function retains a well-defined order of vanishing, and this is what keeps open neighborhoods from collapsing.

## How a small circle proves an open mapping

Let f be nonconstant and holomorphic on a connected open set. Fix an interior point a and write w zero for the output f of a. We want to show that outputs sufficiently close to w zero are all produced by inputs sufficiently close to a. In other words, the image contains a small disk around w zero.

Consider the function obtained by subtracting w zero from f. It vanishes at a. Because f is not constant, zeros of this new function are isolated. We can choose a small closed disk around a, lying inside the domain, with no other zero of f minus w zero and no zero along the boundary circle.

On that boundary circle, the magnitude of f minus w zero is positive and continuous. Compactness gives a *positive minimum*. Call that minimum delta. Imagine now choosing a target output w whose distance from w zero is less than delta. Compare two functions on the input circle: f minus w zero, and the small constant shift w zero minus w. The magnitude of the shift is strictly less than the magnitude of f minus w zero at every boundary point.

This is exactly the situation Rouché's theorem was designed for. Adding the small constant shift does not change the number of zeros inside the circle, counted with multiplicity. The unshifted function has a zero at a, so the shifted function must have at least one zero too. A zero of the shifted function means f of some input equals w. And w was any output inside a whole small disk around w zero.

Thus a neighborhood of a maps onto a set containing a neighborhood of f of a. The image of every open subset is open. The proof is worth remembering because of its shape: isolate the known solution, separate its boundary values from zero by compactness, then perturb the output and use a zero-counting theorem to show a nearby solution still exists.

This does *not* prove local injectivity at critical points. For z squared, most small nonzero outputs have two preimages. Open mapping means the output contains an open neighborhood, not that the function has a single-valued local inverse. At points where the derivative is nonzero, the stronger holomorphic inverse-function theorem gives a local inverse. At a zero derivative, branching may occur.

## Why this theorem excludes a constant-magnitude circle image

Suppose someone proposes a nonconstant holomorphic function defined on a disk whose values all lie on the unit circle in the output plane. The unit circle has no interior. The open mapping theorem says the image of the input disk must be open, so such a function cannot exist. The only holomorphic functions whose images lie entirely in a circle are constant ones.

This immediately provides another route to the maximum modulus principle. If the magnitude of a holomorphic function reached a local maximum at an interior point and the function were nonconstant, open mapping would put a full output neighborhood around that value. Every neighborhood of a nonzero complex number contains values of strictly larger magnitude. That contradicts maximality. If the center value were zero and the local maximum magnitude were zero, the function would vanish locally and hence everywhere on the connected domain.

The two theorems illuminate each other. One is a statement about attainable output values; the other is a statement about forbidden extremal behavior.

## Normalize to a disk and ask a sharper question

Now consider a holomorphic function that takes the open unit disk into itself, fixes the origin, and is not assumed to be one-to-one. We know its outputs have magnitude less than one whenever its inputs have magnitude less than one. But that is just the definition of mapping the disk to itself. Can holomorphicity force a more informative relationship between input distance from the center and output distance from the center?

Yes. Schwarz's lemma says that for every point z in the unit disk, the output magnitude is at most the input magnitude. The derivative at the origin also has magnitude at most one. Equality is remarkably rigid: equality at one nonzero input, or equality in the derivative bound, forces the entire map to be a rotation of the disk around its center.

We should test the statement before proving it. The identity map preserves distances from the origin and attains equality everywhere. Multiplication by a complex number of unit magnitude is a rotation; it also attains equality. But z squared sends an input of magnitude one half to an output of magnitude one quarter. The output is strictly closer to the center. So the inequality captures an important distinction between rotations and other disk-preserving holomorphic maps.

A quick warning: this is a claim about distance *from the origin*, under a normalization that f of zero equals zero. It does not yet say that every holomorphic disk map contracts the ordinary Euclidean distance between arbitrary pairs of points. More precise statements use a geometry intrinsic to the disk.

## The quotient that reveals the hidden contraction

Here is the proof of Schwarz's lemma. Since f of zero is zero, write f of z as z times another function g. Away from zero, g is simply f of z divided by z. At zero, that quotient appears undefined, but the zero of f makes the singularity removable. The value of g at zero is f prime of zero. Thus g is holomorphic throughout the disk.

Fix a circle centered at zero with radius r strictly less than one. Along the circle, the output magnitude of f is less than one, and the input magnitude is exactly r. Therefore the magnitude of g on that circle is at most one divided by r. By the maximum modulus principle, the same bound holds inside the circle.

Now fix an arbitrary input z in the open unit disk. We can choose circles whose radii r are larger than the magnitude of z but approach one. On each such circle the bound on g at z is one divided by r. Let r approach one. We conclude that the magnitude of g at z is at most one.

Multiplying by the magnitude of z gives the promised bound: the magnitude of f at z is at most the magnitude of z. At the origin, evaluating g gives the derivative bound: the magnitude of f prime of zero is at most one.

The proof has an elegant tension. We deliberately divide by z to remove the one known zero, then make a boundary estimate on a smaller circle. Even though the original function is only defined in the *open* unit disk and may have no boundary values at all, the circles remain strictly inside, where everything is legal. Only at the end do we let their radii approach one.

## Equality is not a small exception

Suppose the magnitude of f at some nonzero point equals the magnitude of that point. Then g has magnitude one at an interior point. We already know g has magnitude at most one everywhere, so it has an interior maximum. By the maximum modulus principle, g must be constant. Since its constant magnitude is one, f is a rotation of the form a unit complex constant times z.

The derivative equality case is similar. If the magnitude of f prime of zero is one, then g has magnitude one at the origin. Again the maximum modulus principle makes g constant. Notice that we did not need to assume f is one-to-one or that it extends to the closed disk. The equality statement follows just from holomorphicity and the disk-preserving hypotheses.

There is a useful converse interpretation: among all holomorphic disk self-maps fixing zero, only the rotations preserve the maximum possible first-order motion at the center. All other such maps move each nonzero point strictly closer to the center in the radial sense.

## Moving the center: Schwarz–Pick

What if the holomorphic self-map does not fix zero? We can move its input and output centers to zero using special fractional linear transformations of the disk. For each point a inside the unit disk, there is a map that takes a to zero and carries the disk onto itself, with a holomorphic inverse. One convenient formula is z minus a divided by one minus the complex conjugate of a times z.

Given a holomorphic map f from the disk to itself, first transport an input point a to zero. Then transport its output f of a to zero. The conjugated map fixes zero, so Schwarz's lemma applies. Undoing the coordinate changes produces the Schwarz–Pick inequality. It says that a certain normalized distance between f of z and f of a cannot exceed the corresponding normalized distance between z and a.

That normalized distance is the magnitude of the disk automorphism sending the chosen base point to zero. It is sometimes called the pseudohyperbolic distance. Its formula corrects ordinary Euclidean separation by how close the points are to the rim. Near the boundary, the disk's intrinsic geometry treats small Euclidean movements differently from similar movements near the center.

Differentiating the Schwarz–Pick inequality at z equal to a yields a local derivative bound. The derivative magnitude at a is at most the ratio of one minus the squared magnitude of f of a to one minus the squared magnitude of a. When a is zero and f of zero is zero, this reduces to Schwarz's original bound. At other points it explains why a disk automorphism can have Euclidean derivative magnitude larger than one without violating its intrinsic distance constraint.

These formulas are not only pretty. They are tools for showing that certain interpolation data are impossible. If someone claims to have a holomorphic self-map of the unit disk sending two specified inputs too far apart in the disk's intrinsic metric, Schwarz–Pick disproves the claim without requiring us to solve for the function.

## What these results actually guarantee

The open mapping theorem tells us that a nonconstant holomorphic map never squeezes an open region into a lower-dimensional set. Schwarz's lemma tells us that when the function maps the unit disk to itself and fixes its center, it cannot push a point farther out from that center. The first statement is about *noncollapse* of open neighborhoods; the second is about a precise kind of *contraction* imposed by normalization.

There is no contradiction between them. The map z squared takes open sets to open sets while pulling each nonzero point of the disk toward the origin. It is open without being locally one-to-one at zero. It is contracting in Schwarz's radial sense without being a strict Euclidean contraction on every pair of points.

The strongest lesson is that holomorphicity supplies geometric restrictions not visible from ordinary continuity. Even when derivatives vanish and functions branch, they cannot flatten a region. And when a holomorphic function is confined to the disk, its freedom is limited enough for one equality case to force an exact rotation. That is the distinctive rigidity of complex analysis: a local analytic condition constrains the global shape of the map.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

### Open mapping theorem

If \(\Omega\subset\mathbb C\) is a domain and \(f\in\mathcal O(\Omega)\) is nonconstant, then \(f(U)\) is open for every open \(U\subset\Omega\).

Fix \(a\in U\), \(w_0=f(a)\). Choose \(r>0\) with \(\overline{D(a,r)}\subset U\), and \(f(z)-w_0\ne0\) on \(|z-a|=r\). Set
\[m=\min_{|z-a|=r}|f(z)-w_0|>0.\]
For \(|w-w_0|<m\), Rouché applied to \(f(z)-w_0\) and \((w_0-w)\) shows that \(f(z)-w\) has the same positive number of zeros in \(D(a,r)\) as \(f(z)-w_0\). Thus \(D(w_0,m)\subset f(U)\).

The hypothesis of nonconstancy on the **connected domain** ensures \(f-w_0\) does not vanish identically on a component and its zeros are isolated.

### Schwarz lemma and equality

If \(f:\mathbb D\to\mathbb D\) is holomorphic and \(f(0)=0\), then
\[|f(z)|\le |z|,\qquad |f'(0)|\le1.\]
If equality holds for any \(z\ne0\) in the first inequality, or in the second inequality, then \(f(z)=e^{i\theta}z\) on the disk. Proof: define \(g(z)=f(z)/z\) for \(z\ne0\), and \(g(0)=f'(0)\). On \(|z|=r<1\), \(|g(z)|\le1/r\). Maximum modulus and \(r\uparrow1\) imply \(|g|\le1\); equality implies constant \(g\).

### Schwarz–Pick inequality

Define \(\phi_a(z)=(z-a)/(1-\overline a z)\). For \(f:\mathbb D\to\mathbb D\),
\[
\left|\frac{f(z)-f(a)}{1-\overline{f(a)} f(z)}\right|
\le\left|\frac{z-a}{1-\overline a z}\right|,
\qquad
|f'(a)|\le\frac{1-|f(a)|^2}{1-|a|^2}.
\]
The derivative bound is pointwise Euclidean and need **not** be \(\le1\) for arbitrary \(a\). Equality for two distinct points in the distance inequality, or for the derivative inequality at one point, forces \(f\) to be a disk automorphism.

### Examples and exercises

1. **Critical but open:** \(z\mapsto z^m\), integer \(m\ge2\), sends \(D(0,r)\) onto \(D(0,r^m)\), though \(f'(0)=0\).
2. **Not holomorphic:** \(z\mapsto\operatorname{Re}z\) sends a planar disk to a real interval, not open in \(\mathbb C\).
3. **Strict radial contraction:** \(f(z)=z^2\) maps \(\mathbb D\) to itself and \(|f(z)|=|z|^2<|z|\) for \(0<|z|<1\).
4. Let \(f:\mathbb D\to\mathbb D\) satisfy \(f(0)=0\) and \(f'(0)=i\). What is \(f\)? **Answer:** \(f(z)=iz\) by equality in Schwarz's lemma.
5. Can a nonconstant holomorphic map on a domain have image entirely within a smooth curve? **Answer:** No, because the image must be open in \(\mathbb C\).
6. Does Schwarz–Pick imply \(|f(z)-f(w)|\le |z-w|\) for all disk self-maps? **Answer:** No in general; it contracts the pseudohyperbolic metric, not ordinary Euclidean distance between arbitrary points.

### Sources and further reading

- MIT OCW, *18.112 Functions of a Complex Variable*, Lecture 12: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/pages/lecture-notes/.
- University of Jyväskylä, *Complex Analysis 2*, normal families and disk maps: https://users.jyu.fi/~salomi/teaching/ca2_2024/Lecture_notes_eng.pdf.
