# 012000 — Dual Spaces and Covectors: The Objects That Measure Vectors

**Track:** Linear Algebra from First Principles. **Background:** linear maps, coordinates and basis changes. **Question:** why is a linear measurement not the same mathematical object as a direction?

<!-- BEGIN SPOKEN LECTURE -->

# Dual Spaces and Covectors: The Objects That Measure Vectors

A direction in space tells us how we might move. A thermometer reading, a height difference, or the derivative of a function tells us a number associated with that movement. The first is a vector; the second is a linear measurement of vectors. Linear algebra calls such measurements covectors, or linear functionals, and collects them into the dual space.

## Linear functionals as measurements

Take the plane with coordinates x and y. Define f of a vector to be two times x minus y. If we add two vectors, their readings add. If we scale a vector, its reading scales by the same amount. So f is a linear map from the plane to the real numbers.

A functional is not itself a direction on the plane. We can represent it by a row of coefficients, but that row is meaningful as an instruction to take a weighted sum. A column of coordinates is meaningful as a description of a vector. Their product is a scalar: evaluation. Without an inner product, there is no canonical way to turn one kind of object into the other.

The set of all linear functionals on a vector space V is itself a vector space, called V dual. We add functionals by adding their readings and scale them by scaling their readings. If V is finite-dimensional, its dual has the same dimension. But equal dimension does not mean a canonical identification of individual vectors with individual covectors.

## The dual basis is designed to evaluate coordinates

Suppose a vector space has a basis e one, e two, and so forth. There is a corresponding dual basis of functionals. The first returns the coefficient of e one; the second returns the coefficient of e two; and so forth. Applying dual basis functional i to basis vector j gives one when the indices match and zero otherwise.

The dual basis exists because any vector has a unique coordinate representation. If we know the coefficients, we can extract them linearly. Every functional can be expressed as a linear combination of these coordinate-extraction functionals.

In standard coordinates, our measurement two x minus y is the row two, minus one. If the vector is four, two, the reading is six. Now change the basis of vectors to u equal to one, one and v equal to one, minus one. The same physical vector has coefficients three and one. Evaluate f on u: the result is one. Evaluate f on v: the result is three. So f has the row one, three in this new basis, and its reading is one times three plus three times one, again six.

Vectors and covectors have changed coordinates in complementary ways. The vector coordinates changed from four, two to three, one. The covector coefficients changed from two, minus one to one, three. Their pairing did not change. This is why tensor calculus uses different coordinate-transformation rules for upper and lower indices.

## The transpose is the map on measurements

Suppose T maps one vector space V to another W. A functional on W can measure T of v. Compose that functional with T and you have a functional on V. This construction sends W dual back to V dual; it is called the dual map, or pullback. In coordinates, its matrix is the transpose of T, once the relevant dual bases are chosen.

Notice the reversal of direction. The original map goes from V to W, but measurements pull back from W dual to V dual. This is not a contradiction: a measurement on the output gives a measurement on the input by asking what output the input would produce. Differential forms are built from this same contravariant behavior.

## A derivative is a covector

Let h be a smooth real function on the plane, perhaps h of x and y equals x squared plus three y. A small displacement v with components a, b changes h to first order by two x times a plus three b. At each point, the derivative is a linear functional on tangent vectors, recorded as the differential d h. It takes a direction and returns a rate of change.

We often draw the gradient of h as a vector. Where did that vector come from if the derivative is naturally a covector? The inner product supplies the conversion: the gradient is the unique vector whose inner product with every direction reproduces the differential's value. In Euclidean coordinates they happen to share components. On a curved manifold or in nonorthogonal coordinates they transform differently. Confusing them leads to mistakes in geometry and optimization.

## Tangent and cotangent spaces

At a point of a smooth manifold, tangent vectors represent velocities of curves through that point. Covectors in the cotangent space are linear measurements of those velocities. Differentials of coordinate functions, like d x and d y, form a local basis of cotangent vectors. They evaluate tangent-coordinate directions just as the dual basis should.

A differential one-form assigns a covector smoothly to every point. Integrating one-forms along curves becomes possible because a one-form evaluates the curve's velocity to produce an ordinary scalar function of time. Two-forms and higher forms are multilinear alternating versions of the same measurement idea.

One last useful fact: any finite-dimensional vector space V maps canonically into its double dual. A vector v defines the functional on V dual that evaluates any covector at v. This map is an isomorphism in finite dimensions, but the construction is meaningful because it uses evaluation, not an arbitrary chosen basis. In infinite-dimensional functional analysis, continuous duals and double duals require extra hypotheses, and the canonical map may fail to be onto.

A vector is a possible direction. A covector is a way to read a number from a direction. The difference may seem formal in flat Cartesian coordinates, but it becomes indispensable when coordinates curve, metrics vary, and geometric objects must make sense independently of a chosen chart.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

The algebraic dual \(V^*=\operatorname{Hom}_{\mathbb F}(V,\mathbb F)\). Given a basis \((e_i)\), the dual basis satisfies \(e^i(e_j)=\delta^i_j\). For \(v\in V\) and \(\varphi\in V^*\), the pairing \(\varphi(v)\) is basis-independent. If \([v]_{\mathrm{old}}=P[v]_{\mathrm{new}}\), then \([\varphi]_{\mathrm{new}}=[\varphi]_{\mathrm{old}}P\) as row coordinates, preserving \(\varphi(v)\). For \(T:V\to W\), \(T^*:W^*\to V^*\), \(T^*\psi=\psi\circ T\), has transpose matrix in dual bases; here \(T^*\) denotes the **algebraic dual map**, distinct from the Hilbert adjoint, although their matrices are related after inner-product identifications.

For \(h(x,y)=x^2+3y\), \(dh_{(x,y)}(a,b)=2xa+3b\). A Riemannian metric \(g\) identifies \(dh\) with a gradient vector through \(g(\nabla h,v)=dh(v)\).

### Exercises with answers

1. Evaluate \(f(x,y)=2x-y\) on \((4,2)\). **Answer:** six.
2. What are its coefficients on the basis \((1,1),(1,-1)\)? **Answer:** \((1,3)\).
3. What direction does the dual map \(T^*\) go when \(T:V\to W\)? **Answer:** \(W^*\to V^*\).
4. Is the differential of a function naturally a vector? **Answer:** no; it is a covector, convertible to a gradient with a metric.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), dual spaces and linear functionals.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), dual spaces.
- [Dual space](https://en.wikipedia.org/wiki/Dual_space).
