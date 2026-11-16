# 004000 — Linear Maps, Kernels, and Rank–Nullity

**Track:** Linear Algebra from First Principles. **Background:** bases, vector spaces, elimination. **Question:** what information does a linear transformation preserve, erase, or create?

<!-- BEGIN SPOKEN LECTURE -->

# Linear Maps, Kernels, and Rank–Nullity

A camera takes a three-dimensional scene and records a two-dimensional picture. The resulting image loses depth. A laboratory instrument converts several physical quantities into a few measured numbers. Different states can yield the same readings. Both are examples of a map that can erase distinctions. Linear maps give us a precise way to measure how many distinctions have been lost.

## What makes a map linear?

A map from one vector space to another is linear if it respects addition and scaling. It must send the sum of two vectors to the sum of their images and send a scaled vector to the same scaling of its image. In one equation, the image of a times u plus b times v equals a times the image of u plus b times the image of v.

The map sending a point with coordinates x, y, z to x plus y is linear. Doubling every input doubles the output; adding inputs adds outputs. The map that adds one to x plus y is not linear, because it sends zero to one. A rotation about the origin is linear; a translation is generally not. The word linear describes how a map interacts with operations, not merely whether its graph looks like a straight line.

If we know a linear map on a basis, we know it everywhere. Suppose the plane has basis east and north, and a transformation sends east to the vector one, one and north to the vector one, minus one. Then it must send the vector three east plus two north to three times one, one plus two times one, minus one, giving five, one. There is no other answer consistent with linearity. That is why matrices record the images of basis vectors.

## The kernel is what becomes invisible

The kernel of a linear map is the set of inputs mapped to zero. In the measurement sending x, y, z to x plus y, the vectors whose first two coordinates sum to zero are invisible. The z coordinate can be anything. These form a plane through the origin.

Two inputs have the same image exactly when their difference lies in the kernel. If one input is u and another is v, linearity says the image of u minus v equals the image of u minus the image of v. Thus equality of measurements is the same as the lost difference lying in the kernel. That is a concrete meaning for the statement that the kernel measures ambiguity.

A linear map is injective, or one-to-one, precisely when its kernel contains only zero. If nothing nonzero is invisible, two different inputs cannot produce the same output. If there is an invisible direction, moving along it does not affect the measurement.

## The image is what can actually be produced

The image, also called the range, is the collection of possible outputs. For the map from three coordinates to the single number x plus y, every real number can occur, so the image is the whole real line. For a map from the plane to three-space sending x, y to x, y, zero, the image is only the horizontal plane. No choice of input gives an output with nonzero third coordinate.

Kernel and image are subspaces, not arbitrary collections. A sum of invisible vectors is invisible; scaling one leaves it invisible. A sum of attainable outputs is attainable, because we can add their inputs.

A map can be injective without being surjective. The embedding of a plane into three-space loses no information but cannot reach the whole target. A map can be surjective without being injective. Our three-to-one measurement reaches every output but forgets an entire plane of inputs.

## Counting information: the rank–nullity theorem

For a linear map from a finite-dimensional space, there is an exact counting law: the dimension of the domain equals the dimension of the kernel plus the dimension of the image. We call the latter the rank and the former the domain dimension. The kernel dimension is the nullity.

Why does this work? First take a basis of the kernel, listing all independent invisible directions. Extend that list to a basis of the entire input space. Apply the map to the added basis vectors. Their images span the image, because the original whole basis spans the domain and the kernel basis maps to zero. They are independent too: if a combination of them maps to zero, that combination is in the kernel and can be written using the kernel basis, contradicting independence of the full list unless all coefficients vanish. The added vectors therefore give a basis of the image.

We have divided a basis of the domain into two groups: directions that vanish, and directions that survive as independent output directions. Their counts add. That is rank–nullity.

Take the map from three-space to two-space given by x plus y for the first output and y plus z for the second. You can choose any pair of output values: set y to zero, then choose x and z to match them. So the rank is two. Its kernel consists of vectors with x equal to minus y and z equal to minus y. There is one free parameter, and the nullity is one. Three equals two plus one.

## Why this matters outside matrices

A derivative at a point is a linear map between tangent spaces. If that derivative is invertible, the inverse function theorem says the original nonlinear map is locally invertible, under suitable smoothness hypotheses. If a differential operator has nonzero kernel, there may be nontrivial solutions to its homogeneous equation. In cohomology, a chain boundary map has a kernel of cycles and an image of boundaries. In all these contexts, rank and nullity measure surviving versus lost directions.

The theorem is elementary but its viewpoint is far-reaching. Every linear transformation has a part it forgets and a part it reaches. Dimension tells us how much is in each part. That simple conservation law is one of the most reusable tools in advanced mathematics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A linear map \(T:V\to W\) satisfies \(T(au+bv)=aT(u)+bT(v)\). Its kernel and image are subspaces. \(T\) is injective iff \(\ker T=\{0\}\), and surjective iff \(\operatorname{im}T=W\). For finite-dimensional \(V\),
\[
\dim V=\dim\ker T+\dim\operatorname{im}T.
\]
Proof: choose \(k_1,\dots,k_r\) a basis of \(\ker T\); extend to \(k_1,\dots,k_r,v_1,\dots,v_s\) of \(V\). Then \(Tv_1,\dots,Tv_s\) is a basis of \(\operatorname{im}T\).
For \(T(x,y,z)=(x+y,y+z)\), \(\ker T=\operatorname{span}\{(-1,1,-1)\}\) and \(\operatorname{rank}T=2\).

### Exercises with answers

1. Find \(\ker T\) for \(T(x,y)=(x,0)\). **Answer:** \(\{(0,y)\}\).
2. Is the map \(T(x,y)=(x,y,0)\) injective? Surjective onto \(\mathbb R^3\)? **Answer:** injective, not surjective.
3. If \(\dim V=8\) and \(\operatorname{rank}T=5\), find nullity. **Answer:** three.
4. Show \(\ker T\) is a subspace. **Answer:** zero maps to zero and \(T(au+bv)=0\) when both inputs lie in the kernel.

### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), linear maps and fundamental theorem of linear maps.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), nullspaces and images.
- [Rank–nullity theorem](https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem).
