# Capacity: When a Small Set Still Has a Large Effect

**Track:** Multivariable Calculus from First Principles. **Focus:** energy capacity, condenser potentials, exact disk and ball calculations, and capacity versus ordinary measure.

<!-- BEGIN SPOKEN LECTURE -->

# Capacity: When a Small Set Still Has a Large Effect

A point has no volume. A thin metal wire occupies almost no volume in a three-dimensional room. Yet if we demand a particular electrical potential along the wire, that condition can have a measurable effect on the surrounding field. How can we distinguish sets that are negligible for a differential equation from sets that matter, even though their volume is zero?

One answer is capacity. Capacity measures the energetic cost of raising a set to a prescribed potential while keeping a larger surrounding boundary grounded. It is an idea from electrostatics, but it also tells us which boundary conditions a Sobolev function can meaningfully sense and which missing sets a weak PDE solution may ignore.

Unlike volume, capacity is tuned to derivatives. This makes it particularly natural for equations such as the Laplace and Poisson equations, whose weak solutions are controlled by the integral of the squared gradient.

## Define the experiment before naming the number

Take a bounded region D and a compact set K strictly inside it. We are allowed to choose a smooth test function that vanishes near the outer boundary of D and equals at least one near K. We interpret the function as an electric potential: the set K is maintained at potential one, and the outer wall at zero.

For each admissible function, compute its Dirichlet energy: the integral over D of the squared magnitude of its gradient. Capacity is the infimum of that energy over all admissible potentials.

The formula has an immediate physical interpretation. A sharp change of potential costs energy. If we can raise the potential to one near K while spreading the change gently through space, the energy is small. If any such change must be steep or substantial over a significant region, the energy cannot be arbitrarily small.

We are omitting the factor one half that is often placed in front of physical field energy. That is a normalization choice; it matters for exact numerical constants, so we will keep it fixed throughout this lecture.

The minimizing potential, understood in the appropriate Sobolev completion, equals one on the inner conductor, zero at the outer boundary, and is harmonic between them. Why harmonic? If we change the potential by a small function that vanishes at the prescribed boundaries, the first variation of the energy must vanish. Integration by parts then gives the Laplace equation away from K.

Already the bridge to variational calculus is clear. Capacity is an optimization problem over functions, and the capacity potential is an energy minimizer.

## A spherical conductor in three dimensions

Let D be the ball of radius R in three dimensions, and K the concentric closed ball of radius a, with a smaller than R. Symmetry suggests the optimal potential depends only on the distance r from the center.

For a radial harmonic function in three dimensions, the general form outside the inner ball is a constant plus another constant divided by r. Enforce value one at r equals a and value zero at r equals R. The result is the quantity one divided by r minus one divided by R, divided by one divided by a minus one divided by R.

The derivative has magnitude one divided by r squared, divided by the fixed denominator. To calculate energy, square that derivative and integrate over the spherical shells. Each shell has area four pi times r squared. The product is therefore proportional to one divided by r squared, which is easy to integrate.

The exact answer is four pi divided by the difference between one divided by a and one divided by R. Equivalently, it is four pi times a times R divided by R minus a.

Let the outer wall move arbitrarily far away. The capacity tends to four pi times a. Thus the Newtonian capacity of a three-dimensional ball scales with its radius, not its volume. Volume scales like the cube of the radius, and surface area scales like its square. Capacity has its own dimension and its own notion of smallness.

Take a ball of radius one hundredth, very small compared with our reference scale. Its volume is proportional to one millionth, but its capacity is proportional to one hundredth. These are different mathematical questions. Neither quantity is a substitute for the other.

## What changes in general dimension?

In spatial dimension n at least three, radial harmonic functions involve the power r to the quantity two minus n. Solving the same inner-one, outer-zero problem gives a capacity proportional to the radius a to the power n minus two, with an explicit factor involving n and the surface area of the unit sphere.

If the outer boundary goes to infinity, the result is n minus two, multiplied by the area of the unit sphere, multiplied by a to the power n minus two. The defining feature is the exponent n minus two. It comes from balancing a squared derivative, which contributes two inverse powers of length, against n-dimensional volume.

That exponent will appear again in Wiener's boundary regularity criterion. It is the natural scale for how much obstruction the complement of a domain supplies near a boundary point.

## The plane is logarithmic

Two-dimensional potential theory behaves differently. On an annulus with inner radius a and outer radius R, a radial harmonic function is a constant plus a multiple of the logarithm of radius. The function that equals one on the inner circle and zero on the outer circle is the logarithm of R divided by r, divided by the logarithm of R divided by a.

Differentiate, square, and integrate over circular shells. The circumference of radius r is two pi r. The radial derivative has magnitude one divided by r, divided by the logarithm of R over a. The integral produces the exact capacity: two pi divided by the logarithm of R over a.

As the inner radius approaches zero with R fixed, this capacity tends to zero. But it does so logarithmically, much more slowly than a positive power of a.

Here is a warning about terminology. The two-dimensional *relative Dirichlet capacity* we have calculated is not the same numerical object as the classical *logarithmic capacity* often defined using potentials with a different normalization at infinity. Both belong to planar potential theory. We should not use their formulas interchangeably without defining which capacity we mean.

## Does a single point matter?

Imagine shrinking the inner ball all the way to its center point. In three dimensions, the capacity goes to zero linearly with a. In higher dimensions it goes to zero as a to the power n minus two. In two dimensions the relative capacity still tends to zero, by the logarithmic formula.

Thus a single interior point has zero Dirichlet capacity in every dimension at least two. We can build functions that equal one near the point while their gradient energy becomes arbitrarily small. That sounds paradoxical only if we expect a pointwise constraint to behave like a volume constraint.

It explains something important about the Sobolev space H one. An H-one function is an equivalence class determined almost everywhere and controlled by its square-integrable gradient. In dimensions at least two, specifying its value at a single point is not a continuous constraint in the H-one norm. The function can change near that point at an arbitrarily small energy cost.

Contrast one dimension. On an interval from negative R to R, demand potential one at the origin and zero at both endpoints. The least-energy function is a triangular tent with slopes of magnitude one over R. Its total energy is two divided by R, which is strictly positive. In one dimension, H-one functions have continuous representatives and evaluation at a point is controlled by their energy and boundary values.

The dimensional distinction is not an abstract technicality. It follows from the exact calculation we have just made.

## Zero area does not mean zero capacity

Now suppose instead of deleting a point, we delete a line segment in the plane. The segment has area zero, but it has positive relative capacity in a bounded surrounding domain. An imposed boundary value on that slit can affect a harmonic function. Similarly, an internal smooth surface in three dimensions has zero volume but can carry a meaningful Dirichlet boundary condition.

For a smooth surface, a trace inequality makes this plausible: restricting an H-one function to that surface is meaningful in an appropriate trace space. A point in dimension three, by contrast, cannot be sampled by a continuous H-one evaluation map. Volume does not distinguish those cases, but capacity does.

A useful rule is that sets of capacity zero are invisible to many energy-space constraints, while positive-capacity sets may obstruct extension or carry boundary data. The word *many* matters. The exact claim depends on the function space and the differential equation. For nonlinear problems, for example, p-capacity based on the p-th power of the gradient may be the relevant object instead of the quadratic capacity we study here.

## Capacity also predicts hitting probabilities

Consider Brownian motion inside our spherical shell. Let h at radius r be the probability that a particle starting there hits the inner sphere before reaching the outer sphere. The function h is harmonic in the shell, equals one on the inner boundary, and zero on the outer boundary. It is exactly the same radial potential used in the capacity calculation.

This is a direct bridge from variational energy to probability. The potential records how likely the inner conductor is to be hit; its integrated gradient energy records the conductor's capacity. The two quantities are closely connected, but capacity is not simply a probability. Capacity depends on the scale and normalization of the experiment, while a hitting probability is a number between zero and one attached to a starting point.

In three dimensions with no outer wall, the probability of ever hitting a ball of radius a from distance r greater than a is a divided by r. This decays with the target's radius. In two dimensions, unconstrained Brownian motion has a different recurrence behavior, so the bounded-annulus experiment is the safe comparison for the logarithmic capacity formula.

## What will capacity tell us next?

The practical insight is that some sets are too small, in the energy sense, to sustain a boundary obstruction, even if we can name every point in them. Such sets may be removable for bounded harmonic functions. Others are thin in volume but large enough in capacity to change a solution.

Capacity will also let us investigate irregular boundaries. If the complement of a domain becomes extremely thin near a boundary point, that point may fail to enforce its prescribed Dirichlet value. The capacity of the complement, measured at successively smaller scales, decides whether it is thick enough.

We began with a question about the effect of a small piece of material. We have replaced the vague word small with a variational measurement: the least gradient energy needed to establish a potential difference. That measurement explains why points, wires, surfaces, and holes can matter so differently to elliptic equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### Relative quadratic capacity and minimizers

For \(K\Subset D\subset\mathbb R^n\), define
\[
 \operatorname{cap}_2(K,D)
 =\inf\left\{\int_D|\nabla\phi|^2\,dx:
 \phi\in C_c^\infty(D),\ \phi\ge1\text{ on a neighborhood of }K\right\}.
\]
For regular inner and outer boundaries the minimizer in the relaxed \(H_0^1(D)\) class is 1 on \(K\), 0 on \(\partial D\), and harmonic in \(D\setminus K\). If \(h\) is this minimizer and \(w=0\) on both interfaces, integration by parts gives \(\int\nabla h\cdot\nabla w=0\), so
\[
E[h+w]=E[h]+E[w].
\]

### Exact concentric-ball capacity

Write \(\sigma_{n-1}=|S^{n-1}|\), \(0<a<R\). For \(n\ge3\),
\[
 h(r)=\frac{r^{2-n}-R^{2-n}}{a^{2-n}-R^{2-n}},\quad
 \operatorname{cap}_2(\overline B_a,B_R)
 =\frac{(n-2)\sigma_{n-1}}{a^{2-n}-R^{2-n}}
 =\frac{(n-2)\sigma_{n-1}a^{n-2}}{1-(a/R)^{n-2}}.
\]
For \(n=3\), this becomes \(4\pi aR/(R-a)\). Sending \(R\to\infty\) gives absolute Newtonian capacity \((n-2)\sigma_{n-1}a^{n-2}\).

For \(n=2\),
\[
 h(r)=\frac{\log(R/r)}{\log(R/a)},\qquad
 \operatorname{cap}_2(\overline B_a,B_R)=\frac{2\pi}{\log(R/a)}.
\]
These are **Dirichlet energy capacity** normalizations, not logarithmic capacity defined via transfinite diameter or equilibrium logarithmic energy.

### A point in one dimension

In \(D=(-R,R)\), require \(h(0)=1\) and \(h(\pm R)=0\). By Cauchy–Schwarz, \(1=|h(0)-h(R)|\le \sqrt R\|h'\|_{L^2(0,R)}\), and similarly on \((-R,0)\). Hence \(E[h]\ge2/R\), attained by \(h(x)=1-|x|/R\). In contrast, the ball formulas prove \(\operatorname{cap}_2(\{0\},B_R)=0\) for \(n\ge2\) by shrinking \(a\downarrow0\).

### Brownian hitting probability

For standard Brownian motion \(B_t\) started at \(x\) with \(|x|=r\in(a,R)\), the probability of hitting the inner sphere before the outer sphere solves the same harmonic Dirichlet problem. For \(n=3\),
\[
\mathbb P^x(\tau_a<\tau_R)=\frac{r^{-1}-R^{-1}}{a^{-1}-R^{-1}}.
\]
In \(n=3\), sending \(R\to\infty\) gives \(a/r\).

### Exercises and worked answers

1. **Three-dimensional shell.** Compute \(\operatorname{cap}_2(\overline B_{1/2},B_2)\). **Answer:** \(4\pi/\bigl(2-1/2\bigr)=8\pi/3\).
2. **Planar annulus.** Set \(a=1/4,R=1\). **Answer:** capacity \(2\pi/\log 4\).
3. **Higher-dimensional scaling.** Replace a ball of radius \(a\) by radius \(3a\) in \(n=5\), with the outer wall at infinity. **Answer:** capacity multiplies by \(3^3=27\).
4. **Why not volume?** Does a line segment in the plane have positive area? Does it necessarily have zero quadratic capacity? **Answer:** area zero, but a nondegenerate segment has positive relative capacity.
5. **Point constraint.** Why is evaluation at a point not continuous in \(H^1_0(B_1)\) for \(n\ge2\)? **Answer:** there are cutoffs equal to one near the point whose gradient energy tends to zero.
6. **Brownian interpretation.** What is the probability of hitting a ball of radius \(a\) from radius \(4a\) in \(\mathbb R^3\), without an outer wall? **Answer:** \(1/4\).

### Sources and further reading

- [Kondrat'ev and Shubin, capacity and Dirichlet energy calculation, Section 3](https://citeseerx.ist.psu.edu/document?doi=6532463137de37aee82ea4a48b31edf56c2e56c6&repid=rep1&type=pdf), explicit relative ball capacity in \(n\ge2\).
- [Wikipedia: Capacity of a set](https://en.wikipedia.org/wiki/Capacity_of_a_set), definitions, electrostatic language, and capacity potential.
- [Wikipedia: Potential theory](https://en.wikipedia.org/wiki/Potential_theory), Laplace and Poisson equations as potential theory.
- [Wikipedia: Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), weak derivatives and trace/evaluation distinctions.
- Library connections: `multivariable-calculus:033000` (energy spaces), `037000` (direct method), `052000` (Brownian boundary exit).
