# 002000 — Vectors, Linear Combinations, and Subspaces

**Track:** Linear Algebra from First Principles. **Background:** basic algebra and coordinate pairs. **Question:** what kind of objects can be added and scaled, and why does that matter?

<!-- BEGIN SPOKEN LECTURE -->

# Vectors, Linear Combinations, and Subspaces

A velocity can be represented by an arrow. A shopping list can be represented by a row of quantities. A sampled sound wave can be represented by a long list of amplitudes. A polynomial can be represented by its coefficients. These objects look different, but each permits two operations: adding two objects of the same kind, and multiplying one by a number. Linear algebra is the study of what follows from the rules connecting those operations.

## What an arrow teaches us

In the plane, write a vector as two numbers, such as three and minus one. It means move three units in the horizontal direction and one unit down. Add it to the vector minus two, four by adding coordinates: the sum is one, three. Scale the first vector by two and you get six, minus two. The geometry agrees with the arithmetic: we can place arrows head to tail to add them, or stretch and reverse them by scaling.

A linear combination is any finite sum of vectors after multiplying each by a scalar. For example, take the directions east and north. Three times east minus two times north is a linear combination. Those two directions generate every displacement in the plane. A single east-pointing arrow cannot: scaling it never produces a north component.

In three dimensions, the same arithmetic uses triples. In a dataset with a hundred measurements, it uses hundred-tuples. Nothing fundamental changes. A vector is not defined by having a visible arrow; it is defined by belonging to a collection in which addition and scalar multiplication obey certain laws.

## The laws we depend on

Addition must be associative and commutative. There must be a zero vector and additive negatives. Scaling must distribute over vector addition and scalar addition, and multiplying by one must change nothing. The scalars ordinarily come from the real or complex numbers, though other fields are possible. A vector space is a set equipped with these two operations satisfying the familiar algebraic rules.

Why list laws that seem so plain? Because we want the same arguments to work for very different objects. In the space of polynomials, adding and scaling mean adding or scaling coefficients. In the space of continuous functions on an interval, we add function values point by point. In the collection of solutions to a homogeneous linear differential equation, addition and scaling preserve solutions. We can use a single theorem for all of them if the axioms match.

There are also collections that fail. The positive real numbers are not closed under multiplying by minus one. The vectors in the plane whose length is exactly one are not closed under addition. These objects may have interesting geometry, but they are not vector spaces with the inherited operations.

## A subspace is a stable family of directions

A subspace is a smaller collection that is itself a vector space with the same operations. To check this efficiently, verify that it contains zero and that a linear combination of any two members remains inside. Consider the vectors in three-dimensional space whose coordinates satisfy x plus y plus z equals zero. The zero vector satisfies it. If two vectors each have coordinate sum zero, adding them preserves zero; scaling preserves it as well. This set is a plane through the origin, a subspace.

Contrast the parallel plane where x plus y plus z equals one. It does not contain zero. Adding two points on it gives coordinate sum two. It is an affine plane, not a vector subspace. This difference between a linear space and a translated copy is behind the shape of the solution sets of equations.

A line through the origin is a subspace. The same line shifted away from the origin generally is not. The set of all polynomials of degree at most three is a subspace of the polynomials; the set of polynomials of degree exactly three is not, because the sum of two cubics might lose the cubic term.

## Span is the smallest space containing the given vectors

Suppose you have vectors u and v. Their span consists of every combination a times u plus b times v, allowing a and b to vary. This span is a subspace, because adding combinations and scaling combinations produces another combination. It is the smallest subspace that contains u and v: any subspace containing both must contain every such combination.

Take u equal to one, two and v equal to two, four. Every combination of u and v stays on the same line: v is already twice u. Naming two vectors does not guarantee a two-dimensional span. Now replace v by two, three. The directions are not scalar multiples, and together they can make every vector in the plane. The determinant calculation comes later; at this stage we can solve a pair of linear equations to find the necessary coefficients.

A span is a description of all permitted directions, not just a count of the listed ingredients. We can add a redundant vector without changing the span. Removing a genuinely necessary vector shrinks it.

## Functions can be vectors too

Consider all real-valued continuous functions on a fixed interval. Their zero vector is the zero function. Their sum is computed point by point, and scalar multiplication likewise. If f and g are continuous, so is a f plus b g. Thus they form a vector space, but not one that can be spanned by finitely many functions. For instance, the functions one, x, x squared, and all higher powers cannot be expressed using only a fixed finite list of polynomials.

This example marks a boundary. Many definitions in linear algebra apply to infinite-dimensional spaces, but familiar finite-dimensional theorems need care. Matrix calculations, for instance, implicitly use a finite list of basis vectors. Questions about convergence and boundedness matter in function spaces. We will distinguish those settings rather than assuming every vector space behaves like the plane.

If you remember one principle, make it this: linear algebra asks which operations preserve a collection. A constraint such as x plus y plus z equals zero defines a stable family; a constraint equal to one does not. Span tells us all the directions we can build. These ideas will make basis and dimension meaningful rather than merely numerical.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A vector space \(V\) over a field \(\mathbb F\) has operations \(V\times V\to V\) and \(\mathbb F\times V\to V\) satisfying additive abelian-group and compatibility axioms. The span of \(v_1,\dots,v_k\) is
\[
\operatorname{span}\{v_i\}=\left\{\sum_{i=1}^{k}a_i v_i:a_i\in\mathbb F\right\}.
\]
The kernel of \(\ell(x,y,z)=x+y+z\) is a subspace. The affine level set \(\ell^{-1}(1)\) is not. If \(u=(1,2)\), \(v=(2,3)\), then \((x,y)=a u+b v\) has solution \(a=2y-3x\), \(b=2x-y\). The vector space of polynomials is infinite-dimensional, unlike \(\mathbb F[x]_{\le d}\).

### Exercises with answers

1. Is \(\{(x,y):y=3x\}\) a subspace? **Answer:** yes; it is the span of \((1,3)\).
2. Is the set of nonzero vectors a subspace? **Answer:** no, it does not contain zero.
3. Describe \(\operatorname{span}\{(1,0),(1,1)\}\). **Answer:** the entire plane, since \((x,y)=(x-y)(1,0)+y(1,1)\).
4. Why is the collection of even polynomials a subspace? **Answer:** sums and scalar multiples preserve the property \(p(-x)=p(x)\).

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), chapters on vector spaces and linear maps.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), subspaces and span.
- [Vector space](https://en.wikipedia.org/wiki/Vector_space).
