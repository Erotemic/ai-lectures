# 013200 - Covariant Derivatives and Parallel Transport

**Track:** Topology and Geometry. **Background:** vector bundles, tensor fields, differential equations. **Question:** how can vectors in different fibers be compared along a path?

<!-- BEGIN SPOKEN LECTURE -->

# Covariant Derivatives and Parallel Transport

Picture a small arrow drawn on the surface of a sphere. Move it along a path, always trying to keep it parallel. If the path is a loop, the arrow may return rotated. What did it mean to keep it parallel in the first place? The arrow at the beginning lives in one tangent plane, while the arrow at a later point lives in another. We cannot simply subtract them as vectors in one shared plane without making an additional choice.

That missing choice is a connection. A connection specifies a rule for differentiating a section of a bundle in a direction tangent to the base. Once we have that rule, we can define parallel transport along a curve by demanding that the covariant derivative of the moving vector vanish. This turns the geometric idea of maintaining direction into a differential equation.

## Ordinary derivatives assume a fixed vector space

In a trivial bundle over the real line, every fiber is a copy of the same vector space. A section is an ordinary vector-valued function. Differentiating it component by component makes sense because the product structure has identified all fibers in advance. But choose a different smoothly varying basis along the line. A constant geometric vector will generally acquire changing components. The ordinary derivative of those new components need not vanish.

We need a derivative that compensates for the changing basis. Locally a connection does this by adding a matrix-valued one-form A to the ordinary differential. When the section has component column v, its covariant derivative has components d v plus A times v. The one-form A tells us how the chosen frame itself varies relative to the connection.

A connection must satisfy a product rule. If f is a scalar function and s is a section, the covariant derivative of f times s is d f times s plus f times the covariant derivative of s. This resembles the ordinary Leibniz rule, but the output now carries a cotangent direction as well as a fiber component.

## Parallel transport becomes an initial-value problem

Give a smooth curve gamma and a vector in the fiber at its starting point. Parallel transport asks for a section along the curve whose covariant derivative in the direction of the curve's velocity is zero and whose starting value is the given vector. In a local frame, if v of t is the component column, the equation says the ordinary derivative of v plus A evaluated on the curve's velocity, multiplied by v, equals zero.

This is a linear ordinary differential equation. On a finite interval with a smooth connection and smooth path, it has a unique solution for each initial vector. The final vector depends linearly and invertibly on the initial vector. Traversing the path backward gives the inverse transport map; following two paths in sequence composes their transport maps.

What happens when the curve crosses a chart boundary? We switch local frames and transform the components. The differential equation changes in a compatible way. The resulting geometric transport map is independent of the local frames used to calculate it.

## A connection that rotates phases

For a complex line bundle, each fiber is one-dimensional over the complex numbers. Choose a unitary frame over the plane. Then a metric-compatible connection can be expressed as the ordinary differential plus i times a real one-form, where i is the imaginary unit. The parallel transport equation changes only the phase of a vector; its magnitude stays constant.

Take the simple connection given by d plus i times x d y. If a path moves horizontally, d y along its velocity is zero, so there is no phase change on that segment. If it moves vertically at fixed x, the phase change is proportional to x times the vertical displacement. Travel counterclockwise around a rectangle. The four segments together change a unit vector by the complex phase whose exponent is negative i times the enclosed area.

This is a valuable example because the underlying line bundle is completely trivial. Every fiber can be globally identified with the complex numbers. Yet our chosen connection has nonzero curvature and produces nontrivial transport around loops. Topological twisting of the bundle and geometric bending of the connection are distinct.

## How local connection forms change

If we replace a local frame by one related through an invertible matrix g, a section's component column changes by the inverse matrix. To keep the covariant derivative geometric, the connection matrix cannot transform by simple conjugation alone. There is an extra term involving the derivative of g. In the language of gauge theory, that is the inhomogeneous gauge transformation law.

For a complex line with a unitary change of frame by the phase exponential of i times a local function chi, the real potential a changes to a plus d chi, with our choice of connection sign. The local potential therefore depends on the frame. But its exterior derivative does not change, since differentiating d chi once more gives zero. We will call that exterior derivative the curvature in the line-bundle case.

This is an important distinction for physical interpretations: one must not treat the entries of a local connection matrix as direct frame-independent observables. Parallel transport around a closed loop and curvature transform in controlled ways; the matrix of connection coefficients depends on the chosen local basis.

## Parallel along a circle

There is an even simpler global example. On the trivial complex line bundle over a circle, let the connection be d plus i times a constant real number a times the global angular one-form. The curvature is zero because every two-form on a circle vanishes. Nonetheless, parallel transport around one full positively oriented turn multiplies a vector by the phase exponential of negative two pi i a. For many values of a this phase is not one.

So flatness does not imply trivial holonomy. A flat connection is locally equivalent to an ordinary derivative on a small simply connected patch, but going around a noncontractible loop can still accumulate phase. If we change the frame by a globally defined phase that winds an integer number of times around the circle, the coefficient a changes by that integer while the full-turn holonomy stays the same.

## The Levi-Civita connection is a special case

On a Riemannian manifold we can ask for a connection on the tangent bundle that preserves the metric under transport and has no torsion. These requirements single out the Levi-Civita connection. Its parallel transport preserves lengths and angles. For the sphere, such transport around a closed path can rotate a tangent arrow even when the path ends where it began. The rotation is related to the sphere's intrinsic curvature.

But it would be a mistake to infer that every vector bundle comes with a canonical connection or that every connection is Levi-Civita. A general vector bundle admits many connections, and the geometry under study determines which properties we require. The connection supplies a rule for comparison that the bare bundle does not provide.

Covariant derivatives, parallel transport, and curvature are successive aspects of one construction. The connection tells us how to differentiate sections. Its differential equation tells us how to carry vectors along paths. Comparing transport around different routes reveals geometric information that ordinary pointwise fiber coordinates cannot see.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A connection \(\nabla:\Gamma(E)\to\Omega^1(M;E)\) satisfies \(\nabla(fs)=df\otimes s+f\nabla s\). In a local frame \(e\), \(\nabla=d+A\). For \(e'=eg\), \(v'=g^{-1}v\), and
\[A'=g^{-1}Ag+g^{-1}dg.\]
Along a smooth path \(\gamma:[0,1]\to M\), parallel transport solves
\[\dot v(t)+A_{\gamma(t)}(\dot\gamma(t))v(t)=0.\]

For a unitary complex line connection \(\nabla=d+ia\) with real \(a\), the transport factor is \(\exp(-i\int_\gamma a)\). If \(a=x\,dy\), then on a counterclockwise rectangle of area \(S\), the factor is \(e^{-iS}\). On \(S^1\) with \(a=c\,d\theta\), \(F=0\) and the full-turn factor is \(e^{-2\pi ic}\). A gauge \(g=e^{ik\theta}\) for \(k\in\mathbb Z\) changes \(c\mapsto c+k\) without changing holonomy.

### Check your understanding

1. Does parallel transport on a line bundle preserve lengths automatically? **No:** only if the connection is compatible with a chosen Hermitian or Euclidean fiber metric.
2. Can a trivial bundle carry a curved connection? **Yes:** \(d+i x\,dy\) on \(\mathbb R^2\times\mathbb C\).
3. Does zero curvature on a circle force full-turn holonomy one? **No:** \(d+ic\,d\theta\) provides counterexamples.

### Reading and sources

- John Baez and Javier P. Muniain, [Gauge Fields, Knots and Gravity](https://pages.jh.edu/rrynasi1/FoundationsOFMath/Literature/PhilPhysics/Baez%2BMuniain1994GaugeFieldsKnots%2BGravity.pdf), connections and transport.
- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overview: [Connection (vector bundle)](https://en.wikipedia.org/wiki/Connection_(vector_bundle)), [Parallel transport](https://en.wikipedia.org/wiki/Parallel_transport).
