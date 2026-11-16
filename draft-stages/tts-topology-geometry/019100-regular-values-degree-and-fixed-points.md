# 019100 — Regular Values and Degree: Counting Solutions with Signs

**Track:** Topology and Geometry. **Background:** derivatives and Jacobian determinants, orientation, homology of spheres, smooth maps. **Central question:** how can counting the preimages of one ordinary point reveal a global property of a map?

<!-- BEGIN SPOKEN LECTURE -->

# Regular Values and Degree: Counting Solutions with Signs

Consider the map that takes a point on a circle and winds it around the circle three times. Most people can see that it has degree three. But what does that phrase mean if the map is distorted, if its speed varies, or if its formula is written in coordinates that hide the winding?

Degree theory gives a robust way to count. Choose a target point and ask how many source points map to it. Count with signs determined by whether the map preserves or reverses local orientation. Under suitable compactness and smoothness hypotheses, this signed total is independent of the ordinary target point chosen. It is an integer that survives continuous deformation.

## What makes a target value regular?

Start with a smooth function of two real variables: x squared plus y squared. The set on which this function equals one is a circle. At every point of that circle, the gradient is nonzero. The implicit function theorem then tells us that the level set locally looks like a smooth curve.

At level zero, the set has collapsed to one point, the origin. There the gradient vanishes. The implicit-function argument does not apply. This does not prove that every singular level set is badly behaved, but it explains why a nonvanishing derivative is an effective condition for predictable geometry.

For a smooth map between manifolds, a target value is called regular when the derivative is surjective at every source point mapping to it. The regular-value theorem says that the inverse image is a submanifold of the expected dimension, assuming the usual smoothness hypotheses. If source and target have the same dimension, that inverse image is discrete. If the source manifold is compact, a discrete closed subset is finite.

Regular values therefore allow us to replace an infinite geometric object with a finite list of points.

## Count each point with the right sign

Let source and target be connected, closed, oriented manifolds of the same dimension. At a preimage of a regular value, the derivative is an invertible linear map between oriented tangent spaces. It either preserves orientation or reverses it. Assign plus one in the first case and minus one in the second.

Add those local signs. The result is the degree of the map. Why should it not change when we move the target point a little? The inverse function theorem makes the preimages move smoothly nearby, and their signs stay constant until a critical value is crossed. At crossings, preimages can appear or disappear in opposite-sign pairs. The signed count stays unchanged.

A complete proof uses homology or a regular-value argument supported by Sard's theorem, which says smooth maps have regular values densely and in fact outside a set of measure zero in the target. Smoothness and compactness prevent the kinds of uncontrolled behavior that would defeat our count.

## Winding the circle by an integer

Write a point of the circle as a complex number of modulus one. Map it to its mth power, where m is a nonzero integer. A generic target point has the absolute value of m distinct preimages. If m is positive, the map preserves the orientation at each of them. If m is negative, it reverses orientation at each. The signed count is exactly m.

When m is two, the target point one has two preimages. Each contributes plus one. When m is negative two, each contributes minus one. A direct counting of points would give two in both cases; signed counting distinguishes the direction of winding.

This example is easy because the map is explicit. The power of degree theory is that the integer remains meaningful even after a complicated deformation of the formula, as long as the map remains continuous between the appropriate compact oriented spaces.

## Why nonzero degree forces a solution

Suppose a smooth map has nonzero degree. It must be onto. If some target point were missed, choose that point as a regular value: its preimage is empty, so the signed sum would be zero. That contradicts nonzero degree.

This turns a calculation into an existence theorem. You may not know where a solution of the equation f of x equals y lies. But if the map has nonzero degree, a solution must exist for every y in the target.

Degree also behaves well under composition. The degree of a composition is the product of the degrees. An orientation-preserving homeomorphism of a connected oriented closed manifold has degree plus one; an orientation-reversing one has degree minus one. On a two-dimensional sphere, the antipodal map has degree minus one. On a circle, the antipodal map has degree plus one: turning a circle by half a revolution preserves its orientation.

## From degree to the fixed-point theorem

The Brouwer fixed-point theorem says that every continuous map from a closed disk to itself has a fixed point. The classic proof is indirect. Assume a map has no fixed points. From each point of the disk, draw a ray starting at its image and passing through the original point. Extend the ray to the boundary. This assigns each disk point a boundary point continuously, and on the boundary it acts as the identity.

We would have constructed a retraction of the disk onto its boundary circle. But such a retraction cannot exist. Passing to first homology, the identity on the circle would have to factor through the disk's first homology, which is zero. The identity map on the integers cannot factor through the zero group.

Here the fixed-point theorem emerges not from an inequality or a contraction estimate but from a topological obstruction. Degree and homology provide a global reason a solution must exist.

## A reusable method

When a later theorem asks for existence of a zero, a fixed point, or a critical solution, it may be worth looking for a degree. Identify an oriented domain, locate regular values, determine signs, and check that solutions cannot escape through a boundary or to infinity. If the domain is noncompact, extra properness hypotheses are needed; if it has boundary, one must prevent the target value from appearing on the boundary during a homotopy.

The basic idea is already present on the circle. Count solutions with orientation. The count is stable even when individual solutions move or cancel. That is how local derivatives produce a global integer, and how a global integer can force the existence of a solution.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a smooth map \(f:M^n\to N^n\) between connected closed oriented smooth n-manifolds and a regular value \(y\in N\),
\[\deg(f)=\sum_{x\in f^{-1}(y)}\operatorname{sgn}\det(Df_x).\]
The sum is finite by compactness. The equivalent homological definition is \(f_*[M]=\deg(f)[N]\). Hence degree is homotopy invariant and \(\deg(g\circ f)=\deg(g)\deg(f)\). Nonzero degree implies surjectivity. Smooth maps have sufficiently many regular values by Sard's theorem; for the degree count, smoothness avoids technical differentiability thresholds.

For \(f_m:S^1\to S^1\), \(z\mapsto z^m\), \(m\in\mathbf Z\setminus\{0\}\), every target has \(|m|\) preimages, each with local degree \(\operatorname{sgn}(m)\); thus \(\deg f_m=m\). For a smooth function \(h(x,y)=x^2+y^2\), \(1\) is a regular value and \(h^{-1}(1)=S^1\), while \(0\) is critical. Brouwer's theorem follows because a retraction \(r:D^2\to S^1\) would induce \(r_*\circ i_*=\mathrm{id}\) on \(H_1(S^1)=\mathbf Z\), yet \(H_1(D^2)=0\).

### Exercises with answers

1. **Power map.** Compute the degree of \(z\mapsto z^{-3}\) on \(S^1\). **Answer:** \(-3\).
2. **Regular value.** Is zero a regular value of \(x^2+y^2\)? **Answer:** No; the gradient vanishes at its only preimage.
3. **Existence.** If \(\deg f=5\) for a map of connected closed oriented n-manifolds, may f omit a target point? **Answer:** No, because degree is nonzero.
4. **Fixed points.** Which homology group obstructs a retraction of the disk onto its circle boundary? **Answer:** \(H_1(S^1)=\mathbf Z\), since \(H_1(D^2)=0\).

### Sources and further reading

- Allen Hatcher, [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf), degree and homological fixed-point obstructions.
- MIT OpenCourseWare, [18.965 Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), regular values and Sard's theorem.
- Overviews: [Degree of a continuous mapping](https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping), [Regular value theorem](https://en.wikipedia.org/wiki/Preimage_theorem).
