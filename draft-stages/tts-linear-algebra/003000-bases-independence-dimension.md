# 003000 — Independence, Bases, and Dimension: How Many Directions?

**Track:** Linear Algebra from First Principles. **Background:** vectors, span and elementary equations. **Question:** when is a description of a vector both complete and free of redundancy?

<!-- BEGIN SPOKEN LECTURE -->

# Independence, Bases, and Dimension: How Many Directions?

A map of a city may specify a position by giving a distance east and a distance north. A third instruction, such as a distance northeast, is convenient but unnecessary: northeast is already a combination of east and north. What makes the original two directions special? They can reach every position in the plane, yet neither can be built from the other. That pair of properties leads to a basis.

## Independence is the absence of a hidden cancellation

A list of vectors is linearly independent if the only way to combine them to obtain zero is to give every vector coefficient zero. If three vectors are east, north, and northeast, then east plus north minus northeast equals zero, after choosing appropriate units. That is a nontrivial cancellation: the list is dependent.

If a vector is a combination of those before it, the list is dependent. Conversely, a dependency with a nonzero coefficient tells us one vector is a combination of the others, because we can solve for it. For the two vectors one, two and two, three, suppose a times the first plus b times the second gives zero. The coordinate equations are a plus two b equals zero and two a plus three b equals zero. Substituting the first into the second forces b to vanish, then a vanishes. So the pair is independent.

Independence is a statement about uniqueness of representation. If a vector had two different coefficient lists relative to independent vectors, subtracting the descriptions would produce a nontrivial relation equal to zero. Independence rules that out.

## Spanning and independence pull in different directions

A list spans a space if every vector can be built from it. A list is independent if none of the listed vectors is redundant. A basis is a list that is both spanning and independent. The standard coordinate vectors of the plane form a basis. In three-dimensional space, the three coordinate directions form a basis. In the space of polynomials of degree at most two, the functions one, x, and x squared form a basis. None is a combination of the others, and every quadratic polynomial uses exactly those three.

Why not declare dimension to be the length of some basis? Because different bases might have different lengths, unless we prove otherwise. That is where the exchange argument enters.

## Why the number of basis vectors is fixed

Imagine a space spanned by n vectors. Can it contain more than n independent vectors? No. Express the independent candidates using the spanning list. If there were n plus one candidates, their coordinates would form an n-by-(n plus one) homogeneous system. Elimination leaves at least one free unknown, giving a nontrivial combination of the candidate vectors equal to zero. That contradicts independence.

This argument has two consequences. Every independent list has at most the number of vectors in a spanning list. If two lists are both bases, each spans and each is independent, so each has at most as many elements as the other. They must therefore have the same length. Dimension is well defined. It is not a convention about preferred coordinates but an invariant of the space.

This also explains why every sufficiently long list in a finite-dimensional space is dependent. A collection of four vectors in three-dimensional space cannot all give new directions. On the other hand, three vectors there need not form a basis; they might all lie in the same plane. The number must be right, but the independence condition matters too.

## Extend and trim

Suppose you have an independent pair in three-dimensional space. Add a vector outside their span and you obtain a basis. If you have a spanning list with redundant vectors, remove one whose deletion does not shrink the span, and continue until the remaining list is independent. Thus we can extend independent lists to bases and trim spanning lists down to bases. These facts do not demand a specific coordinate system.

Try an example. The vectors one, zero, one; zero, one, one; and one, one, two in three-dimensional space do not form a basis. The third is the sum of the first two. The span is a plane, despite the list containing three objects. Replacing the third by zero, zero, one gives a basis. To test a list algorithmically, place its vectors as matrix columns and row-reduce; the pivot columns identify an independent set that spans the same column space.

## Dimension and what it does not measure

The dimension of a subspace measures how many independent choices are needed to specify its members. A line through the origin has dimension one. A plane through the origin in three-space has dimension two. The whole three-space has dimension three. The set of all polynomials is infinite-dimensional because, no matter how many polynomial directions you list, a higher-degree monomial cannot be created by combining them.

Dimension is not length, volume, or the number of elements of a set. The real line and plane both have infinitely many points, yet dimensions one and two. A finite-dimensional real vector space and a finite-dimensional complex one may have related but different dimensions: one complex coordinate corresponds to two real coordinates. State the field whenever the distinction matters.

In geometry, a tangent space at a point of an n-dimensional smooth manifold has dimension n. In differential equations, the space of solutions of a homogeneous linear equation may have a finite or infinite dimension depending on the problem. In numerical algorithms, the number of independent directions determines how many parameters can actually be recovered from data.

A basis is an economical language for a space. It can describe everything, but nothing twice. When we change that language, coordinates change while the underlying vector remains the same. That is the next great theme of linear algebra.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A finite family \((v_i)_{i=1}^k\) is independent iff \(\sum a_i v_i=0\Rightarrow a_i=0\) for all \(i\). A basis is independent and spanning. If \(S=(s_1,\dots,s_n)\) spans \(V\), any independent family in \(V\) has at most \(n\) members by the kernel argument applied to its coordinate matrix. Therefore the length of a basis is uniquely determined, \(\dim_{\mathbb F}V\).

For \(V=\mathbb R[x]_{\le2}\), \((1,x,x^2)\) is a basis and \(\dim V=3\). In \(\mathbb R^3\), \((1,0,1),(0,1,1),(1,1,2)\) is dependent, the last being the sum of the first two.

### Exercises with answers

1. Is \((1,0),(2,0)\) independent? **Answer:** no.
2. Find a basis of \(\{(x,y,z):x+y+z=0\}\). **Answer:** \((1,0,-1),(0,1,-1)\).
3. Give the dimension of polynomials of degree at most four. **Answer:** five, with basis \(1,x,x^2,x^3,x^4\).
4. Can six vectors span \(\mathbb R^7\)? **Answer:** no; a spanning family must have at least seven members.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), finite-dimensional spaces and basis theorems.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), basis and dimension.
- [Basis (linear algebra)](https://en.wikipedia.org/wiki/Basis_(linear_algebra)).
