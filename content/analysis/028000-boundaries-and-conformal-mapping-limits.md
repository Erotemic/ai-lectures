# 028000 — Beyond the Riemann Map: Boundaries, Corners, and the Limits of Equivalence

**Track:** Analysis from First Principles. **Background:** Riemann mapping theorem, harmonic functions, Poisson formula, conformal changes of coordinates. **Question:** When does a conformal map extend to the boundary, and what can we actually use it to compute?

<!-- BEGIN SPOKEN LECTURE -->

# Beyond the Riemann Map: Boundaries, Corners, and the Limits of Equivalence

Suppose you have a region with a jagged boundary and you want to solve a physical problem inside it. Perhaps you know the temperature along the edge of a metal plate and want the steady-state temperature at every interior point. For a circular disk, complex analysis gives an elegant formula: the value inside is a weighted average of the prescribed boundary values. For an irregular domain, there may be no equally simple-looking formula. The Riemann mapping theorem promises a conformal equivalence with the disk. Could we use that equivalence to transport the disk's solution back into the irregular region?

Yes, but only after asking a question that the mapping theorem itself did not answer. What happens to the *boundary* under that equivalence? The theorem gives a holomorphic bijection between interiors. A prescribed boundary temperature lives on the edge, not inside. If the map fails to extend appropriately, we cannot simply claim that every boundary point matches a unique point of the unit circle.

This distinction between interior and boundary is the central theme of the lecture. Along the way we will see why corners produce singular derivatives, why some domains have multiple ways to approach what looks like a single boundary point, and why conformal equivalence does not mean that all domains are interchangeable for every geometric purpose.

## The Riemann map lives in the interior

Start with a bounded simply connected domain whose boundary is a smooth, closed curve. The Riemann mapping theorem says that its interior is conformally equivalent to the unit disk. Because the boundary is smooth, one expects the correspondence to extend continuously to the edge, and in this setting it does. A continuous boundary function on the irregular region can then be transferred to the circle, solved there, and carried back inside.

Now replace the smooth boundary by a simple closed curve with corners. Intuitively, nothing catastrophic should happen to the matching of points: each boundary point is still a unique point of that one closed loop. This remains true even without smoothness. The relevant hypothesis is that the boundary is a *Jordan curve*: the continuous image of a circle under a one-to-one map. Such a curve may have many sharp corners, and it can be very rough, but it does not cross itself and it runs around the region once without retracing a boundary segment.

Carathéodory's boundary extension theorem says that a conformal equivalence between the unit disk and the interior of a Jordan curve extends continuously to a one-to-one correspondence between the closed disk and the closure of the region. Because those closures are compact, the extended map and its inverse are continuous. In other words, the extension is a homeomorphism of the two closed regions.

The theorem does not say that the derivative remains bounded at boundary points, or that the extension is differentiable there. It says the point correspondence is continuous and reversible all the way to the edge. That is precisely the additional conclusion needed to transfer continuous boundary data unambiguously.

## A slit shows why an apparent boundary point may not be one boundary direction

To see what can go wrong, imagine the open unit disk with a thin radial slit removed. Start at its center and remove the radius running to the right-hand boundary point. The remaining region is connected and simply connected: the slit has been opened from an interior point all the way to the outside edge, so it does not enclose a hole.

Now pick a point halfway along the slit. Approaching that point from above the slit and from below the slit are very different operations inside the domain. A traveler on one side cannot cross the slit to the other side without going around an endpoint. When the slit is viewed merely as a subset of the Euclidean plane, both approaches lead to the *same* geometric boundary point. But from the interior topology of the domain they represent distinct boundary approaches.

The boundary of this slit disk is not a Jordan curve. A conformal map from the disk into the slit region may extend continuously to the ordinary boundary, because this particular boundary is locally connected. Yet the extension cannot be one-to-one on the boundary circle: two different boundary directions correspond to the two sides of the slit. The same Euclidean slit point can be reached through different arcs of the unit circle.

This is not a contradiction of the Riemann mapping theorem. Its bijection was always only between interior points. The failure appears when we ask for an injective correspondence on the ordinary boundary. More complicated domains, such as carefully constructed comb-shaped regions with accumulating slits, can even obstruct continuous extension to the ordinary Euclidean boundary.

The mathematical language for handling such phenomena is the theory of prime ends. Rather than regarding the edge as only a set of Euclidean points, one records particular ways of approaching the boundary through the domain, using shrinking crosscuts. For a Jordan domain, the resulting prime-end boundary agrees with the ordinary circle-like boundary. In a slit domain, a physical point may correspond to more than one prime end. This extended viewpoint recovers a clean boundary-circle correspondence without pretending that two sides of a slit are the same approach.

We will not build the full prime-end theory here. Its purpose matters more than its machinery for this stage: the boundary must sometimes be understood from *inside the domain*, not merely as a set drawn in the plane.

## Why corners squeeze and stretch

Return to a simpler region, a polygon. Consider one corner with interior angle alpha. Near that corner the domain looks approximately like a wedge. We already know how to map a wedge to the upper half-plane: raise z, in appropriate local coordinates, to the power pi divided by alpha. Conversely, a map from the upper half-plane into that wedge behaves like a power with exponent alpha divided by pi.

The derivative of a power z to exponent p behaves like p times z to the power p minus one. If p is greater than one, its magnitude shrinks toward zero as we approach the vertex. If p is less than one, it grows without bound. The behavior depends on the direction of the conformal map and on the angle at the corner.

Imagine mapping a flat upper half-plane into a right-angle wedge. The angle at the vertex is pi over two, half the straight angle pi. The local map behaves like a square root, so its derivative becomes large near the boundary vertex. Reversing the map, from the wedge back to a half-plane, behaves like squaring, whose derivative tends to zero at that vertex. Both are perfectly conformal in their open interiors. Neither promises a well-behaved derivative *at* the corner.

For a concave corner of three pi over two, the roles reverse. The map from a half-plane into that wedge behaves like a power of three halves, so its derivative tends to zero at the corner. The inverse map behaves like a power of two thirds, with derivative that diverges.

These singular scale factors matter for computation. If you draw a uniform grid in one domain and move it through the conformal map, grid cells can become extremely small or extremely stretched near corners. The angles of tiny cells are preserved, but the sizes are not. A numerical method that samples uniformly in one coordinate system may resolve the mapped geometry very unevenly.

## The Schwarz–Christoffel idea

There is a systematic way to build conformal maps to polygonal regions, called the Schwarz–Christoffel transformation. Its central observation is that the derivative of a mapping from the upper half-plane to a polygon must turn through a prescribed angle each time the boundary passes a polygon vertex.

On the real boundary of the half-plane, choose one point for each polygon corner. These are often called prevertices. At each prevertex, include in the derivative a power of the distance from that point. The exponent is the interior angle of the corresponding polygon corner divided by pi, minus one. When we cross a prevertex along the real axis, the argument of that factor changes. The turning angle of the image boundary changes exactly as the polygon demands.

Multiplying the factors gives a candidate derivative. Integrating gives a conformal map, after choosing constants and placing the prevertices so the side lengths match. In practice, determining those prevertices is a nonlinear problem that can be quite difficult. The point of the construction is not that polygon maps are trivial to compute, but that their boundary angles constrain the analytic form of the derivative.

This is a striking connection between geometry and complex analysis. Corner angles become exponents of holomorphic factors. The local stretching we just studied is not a numerical accident; it is encoded in the analytic structure of the map.

## Bringing a harmonic problem back to the disk

Now return to our temperature problem. Let U be a bounded Jordan domain, and prescribe a continuous real-valued function along its boundary. We want a harmonic function in U that approaches that boundary value continuously. In two-dimensional steady-state heat conduction with uniform isotropic conductivity, harmonicity is the mathematical description of equilibrium temperature in the absence of internal sources.

Choose a conformal map F from U onto the unit disk. Carathéodory's theorem extends it to a homeomorphism of closures. That lets us transfer the prescribed boundary data to a continuous function on the unit circle: to find the value at a point on the circle, take the corresponding point of the original boundary and read its prescribed temperature there.

On the disk, the Poisson integral gives an explicit harmonic extension. Its value at an interior point is a weighted average of all the circle's boundary values. The weights are nonnegative, sum to one, and become concentrated near a boundary point as the interior evaluation point approaches it. At the disk center, the weights are uniform, so the temperature is the ordinary average of boundary temperatures. Near the edge, nearby boundary points have greater influence.

Compose this disk solution with F to return to U. The resulting function is harmonic in U. The reason is special to two dimensions: under a holomorphic change of coordinates with nonzero derivative, the Laplacian picks up a positive scale factor equal to the squared magnitude of the derivative. Multiplying zero by a positive factor still gives zero. So the equation saying the Laplacian vanishes survives the conformal coordinate change.

The boundary values are correct because both F and its inverse extend continuously to the corresponding boundaries. As an interior point tends to a particular original boundary point, its image tends to the matching circle point, and the Poisson solution tends to the prescribed value there. Uniqueness follows from the maximum principle for harmonic functions: if two continuous-on-the-closure harmonic solutions have the same boundary values, their difference is harmonic, vanishes at the boundary, and must vanish throughout.

We have solved a problem on an irregular domain by moving it to a disk, solving there, and moving it back. We did not need an elementary formula for F to establish the existence and uniqueness of the harmonic solution. But to compute numerical values, we would need to approximate F or otherwise solve the original boundary problem.

## Harmonic measure as a way to remember boundary influence

The Poisson kernel also tells us which parts of the boundary have greater influence on a chosen interior point. If a particular boundary arc is assigned temperature one and the rest temperature zero, the harmonic solution at an interior point gives the harmonic measure of that arc, with the boundary values interpreted in a suitable limiting sense at the endpoints.

Conformal maps preserve this harmonic measure once arcs are transported by the boundary correspondence. For a bounded Jordan domain, we can transfer an arc to the disk, integrate the Poisson kernel over the corresponding circle arc, and obtain exactly the harmonic measure of the original arc. It is tempting to describe this as the chance that a random particle first exits through that arc. That interpretation is correct for planar Brownian motion in the appropriate probabilistic setting, though the probabilistic theory is not needed for our present harmonic calculation.

The phrase conformal invariance now has a more substantial meaning than preservation of angles alone. Holomorphic coordinate changes transport harmonic functions and harmonic measure. They carry an entire class of boundary-value problems to better-understood domains, provided the boundary correspondence is justified.

## The limits of being conformally equivalent

We should finish by making the restrictions explicit. The Riemann mapping theorem does not say all planar domains are equivalent. A region with a hole is not simply connected. An annulus cannot be transformed bijectively and holomorphically onto a disk. Even among annuli, the ratio of the outer and inner radii carries a conformal invariant. In logarithmic form it is called the modulus of the annulus. Different moduli cannot be removed by conformal reparametrization.

The theorem also does not make the whole complex plane equivalent to a disk. Liouville's theorem rules that out. It does not say that arbitrary boundary points are matched continuously unless there are additional conditions. And it does not imply a conformal map preserves Euclidean distance, area, or boundary smoothness. These distinctions matter when we use conformal mapping to understand physical shapes rather than just classify analytic interiors.

The Jordan-boundary conclusion is strong but also carefully limited. For a Jordan domain, we have a continuous, one-to-one correspondence on the closure. It need not preserve tangent directions at corners, and the derivative may diverge or vanish near the edge. For a slit region, a boundary point may have multiple interior approaches, and a continuous extension need not be injective. For more complicated boundary sets, even ordinary continuous extension can fail. Prime ends were invented to describe which boundary approaches remain meaningful.

The path from fractional linear maps to the intrinsic geometry of the disk, the existence theorem for conformal maps, and finally the structure of boundaries reveals how these ideas fit together. The strongest general result is not that every shape can be made identical in every sense. It is that simply connected proper plane domains share the same *interior conformal geometry*, while their boundaries, lengths, numerical conditioning, and global topology may demand additional information.

This difference between a theorem of existence and a theorem of controlled behavior is worth carrying into later analysis. Existence can be established by compactness. Uniqueness can follow from rigidity. But if we want stable approximation, estimates near singular corners, or reliable transport of boundary data, we must ask new questions and prove new theorems. The Riemann mapping theorem gives the coordinate system. It does not finish the analysis of everything we might do in that system.

<!-- END SPOKEN LECTURE -->

## Mathematical companion — display only

### Carathéodory's Jordan-domain extension theorem

If \(U\) is the bounded component of \(\mathbb C\setminus\Gamma\) for a Jordan curve \(\Gamma\), and \(f:\mathbb D\to U\) is conformal, then \(f\) extends to a homeomorphism \(\overline{\mathbb D}\to\overline U\). This does not guarantee nonzero finite boundary derivatives.

For the slit disk \(U=\mathbb D\setminus[0,1)\), the boundary is locally connected, and a Riemann map extends continuously to the usual closure, but it cannot extend as a homeomorphism. Points in the interior of the slit are approached from two sides; the prime-end boundary distinguishes them.

### Corner power laws

If \(W_\alpha=\{0<\arg z<\alpha\}\) with \(0<\alpha<2\pi\), then

\[
F:W_\alpha\to\mathbb H,\qquad F(z)=z^{\pi/\alpha}
\]

is conformal for the branch \(0<\arg z<\alpha\). Conversely, a local map from \(\mathbb H\) to the wedge behaves as \(w^{\alpha/\pi}\). Its derivative scales as \(|w|^{\alpha/\pi-1}\) near the vertex. The exponent is only a *local asymptotic model* for a general polygonal conformal map, not an exact global formula.

With real prevertices \(x_k\), an appropriately normalized Schwarz–Christoffel map from \(\mathbb H\) to a polygon has derivative of the form

\[
f'(z)=A\prod_{k=1}^{n-1}(z-x_k)^{\alpha_k/\pi-1},
\]

where one prevertex may be placed at infinity, \(A\ne0\), and branches and prevertex positions must be chosen so the image polygon has the desired side lengths and angles. In general these parameters are not available in closed form.

### Poisson transport of the Dirichlet problem

Let \(U\) be a bounded Jordan domain, \(F:U\to\mathbb D\) conformal with a homeomorphic boundary extension, and \(g:\partial U\to\mathbb R\) continuous. Define \(\phi(e^{it})=g(F^{-1}(e^{it}))\). For \(w\in\mathbb D\),

\[
P[\phi](w)=\frac1{2\pi}\int_0^{2\pi}
\frac{1-|w|^2}{|e^{it}-w|^2}\,\phi(e^{it})\,dt.
\]

Then \(u(z)=P[\phi](F(z))\) is the unique harmonic function on \(U\), continuous on \(\overline U\), with \(u|_{\partial U}=g\). The Laplacian transformation formula is

\[
\Delta(u\circ F)(z)=|F'(z)|^2(\Delta u)(F(z))
\]

for a \(C^2\) real-valued \(u\) defined on the target of \(F\).

For a boundary arc \(A\subset\partial U\), harmonic measure transports as

\[
\omega_U(z,A)=\omega_{\mathbb D}(F(z),F(A)).
\]

### Conformal modulus of annuli

The annulus \(A_r=\{r<|z|<1\}\), \(0<r<1\), has conformal modulus

\[
\operatorname{mod}(A_r)=\frac1{2\pi}\log\frac1r.
\]

Two circular annuli are conformally equivalent iff they have equal modulus; topological non-simple-connectivity alone does not classify annular conformal type.

### Exercises and answers

1. **Corner direction.** A map from the upper half-plane into a wedge with angle \(\pi/2\) behaves like which power? **Answer:** \(w^{1/2}\); the derivative magnitude diverges like \(|w|^{-1/2}\) near 0.
2. **A concave corner.** For an angle \(3\pi/2\), how does the map from the upper half-plane behave? **Answer:** Like \(w^{3/2}\), with derivative shrinking like \(|w|^{1/2}\) near the vertex.
3. **Why Jordan matters.** Can a conformal equivalence between the unit disk and the radial slit disk extend injectively to ordinary Euclidean closures? **Answer:** No; distinct approaches to the two sides of the slit would be identified, and the slit boundary is not homeomorphic to a circle.
4. **Boundary temperature.** If continuous boundary data equal a constant seven on a bounded Jordan domain, what is the unique harmonic extension? **Answer:** The constant function seven, since the Poisson kernel integrates to one and uniqueness follows from maximum principle.
5. **Modulus.** Compare \(A_{1/2}\) and \(A_{1/4}\). **Answer:** Their moduli are \(\log2/(2\pi)\) and \(\log4/(2\pi)\), different; they are not conformally equivalent despite being homeomorphic.
6. **Where the Riemann map stops.** Which part of the Dirichlet argument cannot be obtained from the Riemann mapping theorem alone? **Answer:** The continuous one-to-one boundary correspondence used to pull back continuous data, supplied here by Carathéodory's theorem under the Jordan-boundary hypothesis.

### References

- [Boris Khoruzhenko (Queen Mary University of London), potential theory notes on harmonic measure and the Dirichlet problem](https://webspace.maths.qmul.ac.uk/b.khoruzhenko/potential_th_notes.pdf).
- [Yum-Tong Siu, *Schwarz–Christoffel Transformations* (Harvard Mathematics)](https://people.math.harvard.edu/~siu/math213a/schwarz_christoffel_transformation.pdf).
- [Wikipedia, Carathéodory's theorem (conformal mapping)](https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(conformal_mapping)).
- [Wikipedia, Schwarz–Christoffel mapping](https://en.wikipedia.org/wiki/Schwarz%E2%80%93Christoffel_mapping).
- [Wikipedia, Conformal modulus](https://en.wikipedia.org/wiki/Conformal_modulus).
- [Christopher Bishop, The Riemann Mapping Theorem (Stony Brook lecture notes)](https://www.math.stonybrook.edu/~bishop/classes/math626.F08/rmt.pdf) — Bishop, chapter 2, section 9 and chapter 4: Carathéodory theorem, prime ends, conformal modulus.
- [Robert B. Ash and W. P. Novinger, Complex Variables, 2nd ed.](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesMerged.pdf) — Ash & Novinger, boundary extension of conformal maps.
