# Removable Singularities: When a Missing Set Can Be Filled In

**Track:** Multivariable Calculus from First Principles. **Focus:** bounded harmonic removability, an exact point-removal proof, polar sets, capacity-zero cutoffs, and point-source counterexamples.

<!-- BEGIN SPOKEN LECTURE -->

# Removable Singularities: When a Missing Set Can Be Filled In

Suppose a harmonic function is defined everywhere inside a ball except at its center. We know the function is bounded as we approach that missing point. Can the hole conceal a genuine mathematical singularity, or is the missing value merely an omission that can be repaired?

For harmonic functions in dimension at least two, boundedness is enough to repair a single isolated point. We can extend the function to the missing point so that it is harmonic throughout the ball. The proof is short enough to understand directly and powerful enough to suggest what happens for far more complicated missing sets.

The general answer is connected to capacity. Sets of zero harmonic capacity are removable for bounded harmonic functions; sets of positive capacity can support nontrivial boundary influence. But we will first prove the one-point theorem, because it shows exactly how a singularity can be ruled out without presuming a derivative at the missing point.

## The point-removal problem

Let u be harmonic in the unit ball with its center deleted. Assume the absolute value of u never exceeds a fixed number M there. We do not know a value for u at the origin, and we are not assuming that u has a limit there.

Look at the outer sphere instead. The values of u there define ordinary continuous boundary data, if we take the unit ball slightly inside the region where u is given. Solve the standard harmonic Dirichlet problem on that full ball with those boundary data. Call the resulting function v. We know v is harmonic across the center because it was constructed on the whole ball.

Now subtract v from u. The difference, w, is harmonic on the punctured ball, bounded, and zero on the outer sphere. If we prove w vanishes everywhere away from the center, then u agrees there with the globally harmonic function v. We can define u at the center by v's value, and the hole disappears.

So the problem is reduced to a question that sounds simpler but needs care: can a bounded harmonic function on a punctured ball be zero on the outer sphere yet remain nonzero inside?

Ordinary maximum principles do not answer immediately. The punctured domain has an extra boundary component at the missing point. We cannot apply the maximum principle and silently ignore that component, because w might not have a prescribed value there.

## Build a barrier that explodes at the hole

We need a positive harmonic function that vanishes on the outer sphere and grows without bound as we approach the missing center. In three dimensions, take one divided by the distance to the center, minus one. In any dimension n greater than two, take distance to the power two minus n, minus one. In two dimensions, take the logarithm of one divided by the distance.

Each of these is harmonic away from the origin. Each equals zero when the radius equals one and tends to positive infinity when radius approaches zero.

Call the chosen function H. Fix a small positive number epsilon. Because w is bounded while epsilon times H diverges at the origin, there is a sufficiently small inner sphere on which epsilon H dominates the absolute value of w.

Now examine the annular region between that tiny inner sphere and the fixed outer sphere. On the outer boundary w is zero and H is zero. On the inner boundary, we arranged that epsilon H is at least as large as the absolute value of w. Therefore epsilon H minus w is nonnegative on both boundary spheres. It is harmonic in the intervening annulus. By the minimum principle, epsilon H minus w is nonnegative everywhere in that annulus. Apply the same argument to epsilon H plus w.

The result is that the absolute value of w is at most epsilon H at any fixed point away from the origin. The chosen inner sphere can be taken as small as needed; the inequality survives as it moves inward. And now comes the decisive step: epsilon was arbitrary. At a fixed point, H is finite. Let epsilon tend to zero. We obtain w equals zero.

That proves the removable point theorem. No guessed limit was needed. We constructed a harmonic replacement and proved that the original bounded function had to agree with it.

## Why boundedness cannot be discarded

The barrier we used is also our simplest counterexample. In three dimensions, one divided by radius is harmonic everywhere except at the center, but it diverges there. It cannot be extended to a harmonic function on the whole ball. In two dimensions, the logarithm of one divided by radius plays the analogous role.

Far from being a mathematical inconvenience, these singular functions describe point sources. With the proper constant, the three-dimensional function one over radius is the fundamental solution of the negative Laplacian. In the sense of distributions, applying the negative Laplacian produces a Dirac delta concentrated at the origin. Away from that point the equation looks homogeneous; at the point a source is hidden.

If we forgot the boundedness assumption, we would mistakenly declare a genuine point charge removable. That would erase the physical and mathematical feature we were trying to describe.

Notice how energy distinguishes the cases. The gradient of one over radius in three dimensions has magnitude proportional to one over radius squared. Its squared gradient, integrated over a small ball around zero, diverges. The singular point source is not an ordinary finite-energy H-one solution there. A bounded harmonic function, by contrast, can be shown to extend with the regularity required by the equation.

## Replace the point by a compact set

Now remove a compact set K from the interior of a domain. We ask whether every bounded harmonic function on the remaining domain has a unique harmonic extension across K.

A central theorem of classical potential theory says that this is true when K has zero harmonic capacity. In the dimensions and normalization of our previous calculation, this is equivalent locally to zero quadratic Dirichlet capacity. In the plane, the corresponding classical language is that K is polar, or has zero logarithmic capacity; care is needed with capacity normalizations, but the zero-set notion agrees locally.

A polar set can be quite complicated. A single point is polar. A countable collection of points is polar, and there are more intricate polar sets. The theorem says that their geometry does not provide enough potential-theoretic size to carry a nontrivial obstruction for bounded harmonic functions.

This is stronger than a statement about Lebesgue measure. Every polar set has area or volume zero, but a set of zero volume need not be polar. A smooth internal surface in three dimensions, for example, has zero three-dimensional volume and positive capacity. It can separate regions and carry genuine boundary effects.

## How the energy proof works

The capacity definition provides an important technical tool. If K has zero quadratic capacity, we can choose smooth cutoff functions that equal one near K and whose gradient energies tend to zero. These cutoffs let us test the PDE almost everywhere while progressively removing the special treatment of the hole.

A typical proof begins with a bounded harmonic u on the complement of K. Insert a test function that vanishes near K, and use a local Caccioppoli estimate to control the energy of u away from K. When the cutoff's gradient energy tends to zero, the extra terms involving that cutoff vanish. We can then pass to the limit in the weak harmonic equation.

Under the theorem's precise local hypotheses, the bounded function extends as a weakly harmonic H-one function across K. Interior elliptic regularity upgrades that weak solution to a smooth harmonic function. This is how a condition about the existence of low-energy cutoffs becomes a statement about removable singularities.

That is a proof strategy, not a substitute for the estimates. One must establish that the gradient of u is locally square integrable before passing to the limit; boundedness and Caccioppoli provide that missing control. Skipping that step would make the argument circular.

## A positive-capacity counterexample with zero volume

Take a solid ball inside a larger ball in three dimensions. Delete only the spherical surface of the smaller ball, leaving the inner and outer open regions. The deleted surface has zero volume, but positive capacity.

Define a bounded function to equal one throughout the inner ball. In the annular outer region, let it solve the radial harmonic problem with value one on the inner sphere and zero on the larger outer sphere. We computed that solution in the capacity lecture. The resulting function is harmonic everywhere except on the deleted spherical surface; it is even continuous across the surface if we fill in its pointwise values there.

But the radial derivative outside the inner sphere is nonzero, while the radial derivative inside is zero. This is not a harmonic function across the surface. Indeed, if it had a harmonic extension to the full outer ball with zero value on the outer sphere, the maximum principle would force the extension to be zero everywhere, contradicting its positive values inside.

This example separates continuity from harmonic removability. The function has a perfectly sensible continuous extension across the missing surface, yet that extension is not harmonic. An interface can conceal a distributional surface charge even when it does not produce a jump in the potential itself.

## What counts as a singularity depends on the class of functions

We have been precise about the class: bounded harmonic functions. If we allow unbounded harmonic functions, a single point can support a fundamental-solution singularity. If we demand a different regularity, such as Lipschitz continuity, the right notion of removable set can involve different analytic capacity conditions. For nonlinear elliptic equations, p-capacity and other capacities enter, depending on the equation and growth class.

One should therefore resist the slogan that small sets never matter. The correct statement is conditional: capacity measures smallness relative to a chosen energy and function class.

For bounded harmonic functions, the point theorem and its capacity-zero extension give a striking conclusion. A missing set can be invisible, not because it has no points, but because it cannot sustain the kind of potential-theoretic obstruction that the equation recognizes.

We are now ready to reverse the question. Instead of removing a small set from the *interior*, imagine that a tiny piece of the *complement* approaches a boundary point. Will the domain actually enforce a Dirichlet value there? The answer, again, depends on capacity—but this time on capacity at every scale.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not narrated)

### A rigorous proof for one point

Let \(n\ge2\), \(u\in C^2(B_1\setminus\{0\})\cap C(\overline{B_1}\setminus\{0\})\), with \(\Delta u=0\) and \(\|u\|_\infty\le M\). Let \(v\) solve the Dirichlet problem in \(B_1\) with boundary values \(u|_{\partial B_1}\), and put \(w=u-v\), so \(w=0\) on \(\partial B_1\) and \(|w|\le2M\).

Define a nonnegative harmonic barrier in \(B_1\setminus\{0\}\):
\[
 H(x)=\begin{cases}
 |x|^{2-n}-1,&n\ge3,\\
 \log(1/|x|),&n=2.
 \end{cases}
\]
For every \(\varepsilon>0\), choose \(\delta>0\) with \(\varepsilon H\ge2M\) on \(\partial B_\delta\). Both \(\varepsilon H\pm w\) are harmonic and nonnegative on the two boundary spheres of \(B_1\setminus\overline{B_\delta}\). The minimum principle gives \(|w|\le\varepsilon H\) throughout that annulus. At each fixed \(x\ne0\), choose \(\delta<|x|\) and let \(\varepsilon\downarrow0\) to conclude \(w(x)=0\). Thus \(u=v\) off the origin and extends uniquely as \(v\).

### Distributional point sources

For \(n=3\), the fundamental solution of \(-\Delta\) is \(\Phi(x)=1/(4\pi|x|)\), and \(-\Delta\Phi=\delta_0\) in distributions. For \(n=2\), \(\Phi(x)=-(2\pi)^{-1}\log|x|\), with the same distributional identity. Each \(\Phi\) is harmonic off zero and unbounded at zero. In \(n=3\), \(|\nabla\Phi|^2\asymp r^{-4}\), whose radial integral \(\int_0^\varepsilon r^{-2}\,dr\) diverges.

### Capacity-zero removability and positive-capacity obstruction

For compact \(K\Subset\Omega\), vanishing harmonic capacity characterizes removability for bounded harmonic functions in the classical Euclidean setting. For \(n\ge3\), harmonic/Newtonian capacity is equivalent to the zero set of local \(\operatorname{cap}_2\). In \(n=2\), one uses logarithmic or local relative capacity carefully; both identify polar compact sets. The capacity-zero cutoff construction and Caccioppoli provide a path to a weak extension, and interior regularity upgrades it to a harmonic one.

For the nonremovable sphere \(K=\partial B_a\subset B_R\) in \(n=3\), set
\[
 u(x)=\begin{cases}
 1,&|x|<a,\\
 \displaystyle\frac{|x|^{-1}-R^{-1}}{a^{-1}-R^{-1}},&a<|x|<R.
 \end{cases}
\]
This is bounded and harmonic on \(B_R\setminus K\), but no harmonic extension with zero outer boundary values is possible by the maximum principle.

### Exercises and worked answers

1. **Barrier sign.** For \(n=3\), why is \(H(r)=r^{-1}-1\) positive on \(0<r<1\)? **Answer:** \(r^{-1}>1\).
2. **Boundedness.** Which step of the puncture proof fails for \(u=r^{-1}\)? **Answer:** no uniform bound can be dominated by arbitrarily small \(\varepsilon H\) on the tiny inner sphere, because both blow up at the same order.
3. **One-dimensional contrast.** Does every bounded solution of \(u''=0\) on \((-1,0)\cup(0,1)\) extend to a globally affine function? **Answer:** no; it can have different affine branches across 0, consistent with positive point capacity in one dimension.
4. **Internal sphere.** Is the piecewise potential in the example continuous across \(r=a\)? **Answer:** yes; both pieces equal one there, but their normal derivatives disagree.
5. **Measure versus capacity.** Can a set of Lebesgue measure zero be nonremovable for bounded harmonic functions? **Answer:** yes, for example a smooth internal spherical surface.
6. **Point source.** What is \(-\Delta(1/(4\pi r))\) in \(\mathbb R^3\) distributionally? **Answer:** the unit Dirac mass at the origin.

### Sources and further reading

- [Michael Taylor, *Harmonic Functions on Domains in Rn*, Section 8](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2021/02/dprn.pdf), a complete maximum-principle proof of isolated bounded removability.
- [Xavier Tolsa, *Analytic Capacity, the Cauchy Transform, and Non-Homogeneous Calderón–Zygmund Theory*, potential-theory notes](https://mat.uab.cat/~xtolsa/mesuraharmonica.pdf), capacity, polar sets, and the bounded-harmonic removable-set theorem.
- [Wikipedia: Polar set (potential theory)](https://en.wikipedia.org/wiki/Polar_set_%28potential_theory%29), polar sets and negligible sets in potential theory.
- [Wikipedia: Capacity of a set](https://en.wikipedia.org/wiki/Capacity_of_a_set), variational capacity and equilibrium potential.
- Library connections: `multivariable-calculus:056000` (capacity), `048000` (Green functions and distributions), `033000` (weak energy solutions).
