# From elimination to coordinate-free linear maps

<!-- BEGIN SPOKEN LECTURE -->

# From elimination to coordinate-free linear maps

## Solving Linear Systems: From Equations to Elimination

Imagine you need to determine two unknown prices from two shopping receipts. One receipt says that two apples and one pear cost seven units. Another says that one apple and three pears cost eleven units. Call the apple price x and the pear price y. We have two times x plus y equals seven, and x plus three times y equals eleven. The challenge is not simply to find two numbers. It is to develop a method that continues to work when there are a thousand unknowns, or when there is no solution, or infinitely many.

A linear equation says that a weighted sum of unknowns equals a specified number. The important restriction is that we never multiply unknowns together or take their squares. The unknowns enter only to the first power. For two variables, each nontrivial equation describes a line in the plane. Solving the system means finding the point, or points, common to all those lines.

### Remove a variable without changing the answers

Return to our receipts. Multiply the second equation by two. It now says two x plus six y equals twenty-two. Subtract the first equation from that, and five y equals fifteen. So y equals three, and the first equation gives x equals two. Check rather than trust the algebra: two apples at two units and one pear at three make seven; one apple and three pears make eleven.

This is elimination. We replace one equation with a combination of equations that preserves exactly the same solutions. There are three elementary operations: exchange two equations; multiply an equation by a nonzero scalar; and add a multiple of one equation to another. Each can be undone. The restriction that the multiplier be nonzero matters: replacing an equation with zero equals zero would erase information.

For our system we can also record just the coefficients and right-hand side. The first row is two, one, seven. The second is one, three, eleven. A vertical line before the last number separates coefficients from results. That rectangle is an augmented matrix. The algebraic operations on equations become row operations on the matrix. A matrix is therefore initially a compact record of a system of linear measurements, not an object that needs mystical properties.

### Pivots and free choices

Consider a different system: x plus y plus z equals four, and two x plus two y plus two z equals eight. The second statement is twice the first. It does not add an independent condition. We may choose y and z freely, then set x equal to four minus y minus z. There are infinitely many solutions. The place where a leading variable is determined is called a pivot position; a variable without a pivot can be chosen freely.

Now replace eight by nine. The equations would require the same sum to equal both four and four and a half. Row reduction produces a row of zero coefficients and a nonzero right-hand side. That row says zero equals one. No choices of the variables can satisfy it. Such a system is inconsistent.

So there are three possibilities. If all variables receive pivots and the equations are consistent, the solution is unique. If some variables are free and the equations are consistent, there are infinitely many solutions over the real numbers. If reduction produces a contradiction, there is no solution at all.

This classification gives more insight than the old rule that one needs as many equations as unknowns. Two equations can be copies of each other. Three equations can contradict one another. The meaningful quantity is the number of independent constraints, not the raw number of rows.

### A geometric interpretation

A single equation in three variables usually describes a plane. Two independent equations intersect along a line. Three independent equations can meet at a point. But planes can be parallel, or can coincide. Row reduction discovers which geometric configuration we have without asking us to draw a picture in a space of dozens of dimensions.

If the right-hand side is zero in every equation, the system is called homogeneous. It always has at least the all-zero solution. In a homogeneous system, any two solutions may be added, and any solution may be scaled, to obtain another. This closure is the beginning of the idea of a vector space: a collection where addition and scaling make sense without leaving the collection.

A nonhomogeneous system, when it has any solutions, is instead a shifted copy of the homogeneous solution set. Choose one particular solution. Add to it any homogeneous solution, and you get another solution. Subtract two particular solutions from each other, and the result solves the homogeneous equations. We will use that principle repeatedly: first solve one instance; then understand the directions in which we can move without changing the measured result.

### Elimination is a proof as well as an algorithm

Why does elimination work? Because it records logical equivalences. Every permitted operation changes the written equations but preserves the set of possible answers. When a reduced row says a variable has a certain value, that is a necessary condition. When a final choice is substituted back and works, it is sufficient. Together they certify the answer.

There is also a practical lesson. A pivot may be zero, so we sometimes exchange rows to find a nonzero coefficient. On computers, a pivot can be nonzero but dangerously small; choosing a better pivot often makes a floating-point computation much more reliable. That numerical issue is separate from the exact algebra taught here. It is a reason to understand the algebra before treating a solver as a black box.

Linear algebra starts with the ability to transform simultaneous constraints into a readable form. From elimination we will acquire the ideas of independent information, free directions, dimension, and invertibility. The goal is not to memorize a collection of elimination tricks. It is to learn to recognize exactly what a system of linear observations does and does not determine.

## Vectors, Linear Combinations, and Subspaces

A velocity can be represented by an arrow. A shopping list can be represented by a row of quantities. A sampled sound wave can be represented by a long list of amplitudes. A polynomial can be represented by its coefficients. These objects look different, but each permits two operations: adding two objects of the same kind, and multiplying one by a number. Linear algebra is the study of what follows from the rules connecting those operations.

### What an arrow teaches us

In the plane, write a vector as two numbers, such as three and minus one. It means move three units in the horizontal direction and one unit down. Add it to the vector minus two, four by adding coordinates: the sum is one, three. Scale the first vector by two and you get six, minus two. The geometry agrees with the arithmetic: we can place arrows head to tail to add them, or stretch and reverse them by scaling.

A linear combination is any finite sum of vectors after multiplying each by a scalar. For example, take the directions east and north. Three times east minus two times north is a linear combination. Those two directions generate every displacement in the plane. A single east-pointing arrow cannot: scaling it never produces a north component.

In three dimensions, the same arithmetic uses triples. In a dataset with a hundred measurements, it uses hundred-tuples. Nothing fundamental changes. A vector is not defined by having a visible arrow; it is defined by belonging to a collection in which addition and scalar multiplication obey certain laws.

### The laws we depend on

Addition must be associative and commutative. There must be a zero vector and additive negatives. Scaling must distribute over vector addition and scalar addition, and multiplying by one must change nothing. The scalars ordinarily come from the real or complex numbers, though other fields are possible. A vector space is a set equipped with these two operations satisfying the familiar algebraic rules.

Why list laws that seem so plain? Because we want the same arguments to work for very different objects. In the space of polynomials, adding and scaling mean adding or scaling coefficients. In the space of continuous functions on an interval, we add function values point by point. In the collection of solutions to a homogeneous linear differential equation, addition and scaling preserve solutions. We can use a single theorem for all of them if the axioms match.

There are also collections that fail. The positive real numbers are not closed under multiplying by minus one. The vectors in the plane whose length is exactly one are not closed under addition. These objects may have interesting geometry, but they are not vector spaces with the inherited operations.

### A subspace is a stable family of directions

A subspace is a smaller collection that is itself a vector space with the same operations. To check this efficiently, verify that it contains zero and that a linear combination of any two members remains inside. Consider the vectors in three-dimensional space whose coordinates satisfy x plus y plus z equals zero. The zero vector satisfies it. If two vectors each have coordinate sum zero, adding them preserves zero; scaling preserves it as well. This set is a plane through the origin, a subspace.

Contrast the parallel plane where x plus y plus z equals one. It does not contain zero. Adding two points on it gives coordinate sum two. It is an affine plane, not a vector subspace. This difference between a linear space and a translated copy is behind the shape of the solution sets of equations.

A line through the origin is a subspace. The same line shifted away from the origin generally is not. The set of all polynomials of degree at most three is a subspace of the polynomials; the set of polynomials of degree exactly three is not, because the sum of two cubics might lose the cubic term.

### Span is the smallest space containing the given vectors

Suppose you have vectors u and v. Their span consists of every combination a times u plus b times v, allowing a and b to vary. This span is a subspace, because adding combinations and scaling combinations produces another combination. It is the smallest subspace that contains u and v: any subspace containing both must contain every such combination.

Take u equal to one, two and v equal to two, four. Every combination of u and v stays on the same line: v is already twice u. Naming two vectors does not guarantee a two-dimensional span. Now replace v by two, three. The directions are not scalar multiples, and together they can make every vector in the plane. The determinant calculation comes later; at this stage we can solve a pair of linear equations to find the necessary coefficients.

A span is a description of all permitted directions, not just a count of the listed ingredients. We can add a redundant vector without changing the span. Removing a genuinely necessary vector shrinks it.

### Functions can be vectors too

Consider all real-valued continuous functions on a fixed interval. Their zero vector is the zero function. Their sum is computed point by point, and scalar multiplication likewise. If f and g are continuous, so is a f plus b g. Thus they form a vector space, but not one that can be spanned by finitely many functions. For instance, the functions one, x, x squared, and all higher powers cannot be expressed using only a fixed finite list of polynomials.

This example marks a boundary. Many definitions in linear algebra apply to infinite-dimensional spaces, but familiar finite-dimensional theorems need care. Matrix calculations, for instance, implicitly use a finite list of basis vectors. Questions about convergence and boundedness matter in function spaces. We will distinguish those settings rather than assuming every vector space behaves like the plane.

If you remember one principle, make it this: linear algebra asks which operations preserve a collection. A constraint such as x plus y plus z equals zero defines a stable family; a constraint equal to one does not. Span tells us all the directions we can build. These ideas will make basis and dimension meaningful rather than merely numerical.

## Independence, Bases, and Dimension: How Many Directions?

A map of a city may specify a position by giving a distance east and a distance north. A third instruction, such as a distance northeast, is convenient but unnecessary: northeast is already a combination of east and north. What makes the original two directions special? They can reach every position in the plane, yet neither can be built from the other. That pair of properties leads to a basis.

### Independence is the absence of a hidden cancellation

A list of vectors is linearly independent if the only way to combine them to obtain zero is to give every vector coefficient zero. If three vectors are east, north, and northeast, then east plus north minus northeast equals zero, after choosing appropriate units. That is a nontrivial cancellation: the list is dependent.

If a vector is a combination of those before it, the list is dependent. Conversely, a dependency with a nonzero coefficient tells us one vector is a combination of the others, because we can solve for it. For the two vectors one, two and two, three, suppose a times the first plus b times the second gives zero. The coordinate equations are a plus two b equals zero and two a plus three b equals zero. Substituting the first into the second forces b to vanish, then a vanishes. So the pair is independent.

Independence is a statement about uniqueness of representation. If a vector had two different coefficient lists relative to independent vectors, subtracting the descriptions would produce a nontrivial relation equal to zero. Independence rules that out.

### Spanning and independence pull in different directions

A list spans a space if every vector can be built from it. A list is independent if none of the listed vectors is redundant. A basis is a list that is both spanning and independent. The standard coordinate vectors of the plane form a basis. In three-dimensional space, the three coordinate directions form a basis. In the space of polynomials of degree at most two, the functions one, x, and x squared form a basis. None is a combination of the others, and every quadratic polynomial uses exactly those three.

Why not declare dimension to be the length of some basis? Because different bases might have different lengths, unless we prove otherwise. That is where the exchange argument enters.

### Why the number of basis vectors is fixed

Imagine a space spanned by n vectors. Can it contain more than n independent vectors? No. Express the independent candidates using the spanning list. If there were n plus one candidates, their coordinates would form an n-by-(n plus one) homogeneous system. Elimination leaves at least one free unknown, giving a nontrivial combination of the candidate vectors equal to zero. That contradicts independence.

This argument has two consequences. Every independent list has at most the number of vectors in a spanning list. If two lists are both bases, each spans and each is independent, so each has at most as many elements as the other. They must therefore have the same length. Dimension is well defined. It is not a convention about preferred coordinates but an invariant of the space.

This also explains why every sufficiently long list in a finite-dimensional space is dependent. A collection of four vectors in three-dimensional space cannot all give new directions. On the other hand, three vectors there need not form a basis; they might all lie in the same plane. The number must be right, but the independence condition matters too.

### Extend and trim

Suppose you have an independent pair in three-dimensional space. Add a vector outside their span and you obtain a basis. If you have a spanning list with redundant vectors, remove one whose deletion does not shrink the span, and continue until the remaining list is independent. Thus we can extend independent lists to bases and trim spanning lists down to bases. These facts do not demand a specific coordinate system.

Try an example. The vectors one, zero, one; zero, one, one; and one, one, two in three-dimensional space do not form a basis. The third is the sum of the first two. The span is a plane, despite the list containing three objects. Replacing the third by zero, zero, one gives a basis. To test a list algorithmically, place its vectors as matrix columns and row-reduce; the pivot columns identify an independent set that spans the same column space.

### Dimension and what it does not measure

The dimension of a subspace measures how many independent choices are needed to specify its members. A line through the origin has dimension one. A plane through the origin in three-space has dimension two. The whole three-space has dimension three. The set of all polynomials is infinite-dimensional because, no matter how many polynomial directions you list, a higher-degree monomial cannot be created by combining them.

Dimension is not length, volume, or the number of elements of a set. The real line and plane both have infinitely many points, yet dimensions one and two. A finite-dimensional real vector space and a finite-dimensional complex one may have related but different dimensions: one complex coordinate corresponds to two real coordinates. State the field whenever the distinction matters.

In geometry, a tangent space at a point of an n-dimensional smooth manifold has dimension n. In differential equations, the space of solutions of a homogeneous linear equation may have a finite or infinite dimension depending on the problem. In numerical algorithms, the number of independent directions determines how many parameters can actually be recovered from data.

A basis is an economical language for a space. It can describe everything, but nothing twice. When we change that language, coordinates change while the underlying vector remains the same. That is the next great theme of linear algebra.

## Linear Maps, Kernels, and Rank–Nullity

A camera takes a three-dimensional scene and records a two-dimensional picture. The resulting image loses depth. A laboratory instrument converts several physical quantities into a few measured numbers. Different states can yield the same readings. Both are examples of a map that can erase distinctions. Linear maps give us a precise way to measure how many distinctions have been lost.

### What makes a map linear?

A map from one vector space to another is linear if it respects addition and scaling. It must send the sum of two vectors to the sum of their images and send a scaled vector to the same scaling of its image. In one equation, the image of a times u plus b times v equals a times the image of u plus b times the image of v.

The map sending a point with coordinates x, y, z to x plus y is linear. Doubling every input doubles the output; adding inputs adds outputs. The map that adds one to x plus y is not linear, because it sends zero to one. A rotation about the origin is linear; a translation is generally not. The word linear describes how a map interacts with operations, not merely whether its graph looks like a straight line.

If we know a linear map on a basis, we know it everywhere. Suppose the plane has basis east and north, and a transformation sends east to the vector one, one and north to the vector one, minus one. Then it must send the vector three east plus two north to three times one, one plus two times one, minus one, giving five, one. There is no other answer consistent with linearity. That is why matrices record the images of basis vectors.

### The kernel is what becomes invisible

The kernel of a linear map is the set of inputs mapped to zero. In the measurement sending x, y, z to x plus y, the vectors whose first two coordinates sum to zero are invisible. The z coordinate can be anything. These form a plane through the origin.

Two inputs have the same image exactly when their difference lies in the kernel. If one input is u and another is v, linearity says the image of u minus v equals the image of u minus the image of v. Thus equality of measurements is the same as the lost difference lying in the kernel. That is a concrete meaning for the statement that the kernel measures ambiguity.

A linear map is injective, or one-to-one, precisely when its kernel contains only zero. If nothing nonzero is invisible, two different inputs cannot produce the same output. If there is an invisible direction, moving along it does not affect the measurement.

### The image is what can actually be produced

The image, also called the range, is the collection of possible outputs. For the map from three coordinates to the single number x plus y, every real number can occur, so the image is the whole real line. For a map from the plane to three-space sending x, y to x, y, zero, the image is only the horizontal plane. No choice of input gives an output with nonzero third coordinate.

Kernel and image are subspaces, not arbitrary collections. A sum of invisible vectors is invisible; scaling one leaves it invisible. A sum of attainable outputs is attainable, because we can add their inputs.

A map can be injective without being surjective. The embedding of a plane into three-space loses no information but cannot reach the whole target. A map can be surjective without being injective. Our three-to-one measurement reaches every output but forgets an entire plane of inputs.

### Counting information: the rank–nullity theorem

For a linear map from a finite-dimensional space, there is an exact counting law: the dimension of the domain equals the dimension of the kernel plus the dimension of the image. We call the latter the rank and the former the domain dimension. The kernel dimension is the nullity.

Why does this work? First take a basis of the kernel, listing all independent invisible directions. Extend that list to a basis of the entire input space. Apply the map to the added basis vectors. Their images span the image, because the original whole basis spans the domain and the kernel basis maps to zero. They are independent too: if a combination of them maps to zero, that combination is in the kernel and can be written using the kernel basis, contradicting independence of the full list unless all coefficients vanish. The added vectors therefore give a basis of the image.

We have divided a basis of the domain into two groups: directions that vanish, and directions that survive as independent output directions. Their counts add. That is rank–nullity.

Take the map from three-space to two-space given by x plus y for the first output and y plus z for the second. You can choose any pair of output values: set y to zero, then choose x and z to match them. So the rank is two. Its kernel consists of vectors with x equal to minus y and z equal to minus y. There is one free parameter, and the nullity is one. Three equals two plus one.

### Why this matters outside matrices

A derivative at a point is a linear map between tangent spaces. If that derivative is invertible, the inverse function theorem says the original nonlinear map is locally invertible, under suitable smoothness hypotheses. If a differential operator has nonzero kernel, there may be nontrivial solutions to its homogeneous equation. In cohomology, a chain boundary map has a kernel of cycles and an image of boundaries. In all these contexts, rank and nullity measure surviving versus lost directions.

The theorem is elementary but its viewpoint is far-reaching. Every linear transformation has a part it forgets and a part it reaches. Dimension tells us how much is in each part. That simple conservation law is one of the most reusable tools in advanced mathematics.

## Matrices, Composition, and Changing Coordinates

Suppose a city uses streets running east and north, while a surveyor uses directions running northeast and southeast. Both can describe the same movement, but the pairs of numbers assigned to it differ. The movement does not change. The coordinate language changes. This distinction is the central discipline behind matrix algebra.

### Columns tell us what happens to basis directions

Choose a basis of an input vector space and a basis of an output vector space. To represent a linear map, ask where each input basis vector goes and write the coordinates of its image as a column. The resulting rectangle of columns is a matrix. Multiplying that matrix by a coordinate column gives the output coordinates.

For a simple example, let a map of the plane send the first coordinate direction to twice itself, and send the second to the sum of the two coordinate directions. Its matrix has first column two, zero and second column one, one. An input with coordinates three, four becomes ten, four, because three copies of two, zero plus four copies of one, one give ten, four.

The dimensions of a matrix tell us the types of vectors it accepts and produces. A matrix with m rows and n columns represents a map from an n-dimensional coordinate space to an m-dimensional one. A square matrix is needed to describe an endomorphism, a map from a space to itself in chosen bases, but linear maps need not be square.

### Matrix multiplication is composition

Suppose the first transformation sends a vector x to B times x. A second sends that result to A times it. Performing B and then A is the composite map: A times B times x. This fixes the order of matrix multiplication. The rightmost transformation acts first.

Why are the entries of the product formed from rows dotted against columns? Take a basis input. The columns of B are its outputs under the first map. Apply A to each of those output columns. Those are precisely the columns of the composite map. The usual multiplication formula is not arbitrary bookkeeping; it is forced by composition and the column convention.

Order matters. Rotate a rectangle ninety degrees and then stretch its horizontal direction. Stretch horizontally first and rotate afterward. The final shapes are generally different. Matrices therefore need not commute. A times B usually differs from B times A. Never cancel or rearrange matrix factors merely because ordinary real numbers permit it.

### One vector, two descriptions

Let the standard coordinates of the plane be x and y. The surveyor's new basis is the vector one, one followed by the vector one, minus one. Call them u and v. To represent the point with standard coordinates four, two, find coefficients a and b with a u plus b v equal to four, two. The equations are a plus b equals four and a minus b equals two. Thus a equals three and b equals one. The same vector is four, two in standard coordinates and three, one in the surveyor's basis.

Place the new basis vectors as columns in a matrix P. Then ordinary coordinates equal P times new coordinates. To go the other way, multiply by the inverse of P. For this example, the inverse takes x, y to one half of x plus y and one half of x minus y. New coordinates are not an alternative physical vector; they are an alternative list of coefficients describing it.

If a linear operator T acts on the plane, and A is its standard matrix, its new-coordinate matrix is P inverse times A times P. Read the operations from right to left: convert new coordinates into standard ones; apply the operator; convert the output back to the new basis. This is the similarity transformation. It changes the matrix but not the underlying linear operator.

### Why eigenvalues survive changing bases

Consider multiplying all horizontal coordinates by two and all vertical ones by three. Its matrix in standard coordinates is diagonal, with two and three on the diagonal. In the diagonal-and-antidiagonal surveyor basis, the matrix is no longer diagonal; each displayed coordinate mixes with the other. Yet the map still stretches one physical direction by two and another by three. Those characteristic stretch factors, the eigenvalues, do not depend on our choice of coordinate language.

This observation explains why much of linear algebra seeks invariants. A rank is the number of independent output directions, not the number of nonzero entries in one displayed matrix. An eigenvalue is a property of an operator, not of the visual position of a matrix entry. A determinant changes predictably with bases for maps between different spaces, but for a single operator the determinant is unchanged by similarity.

### Inverses and identity maps

An identity map leaves every vector fixed. Its matrix has ones on the diagonal and zeros elsewhere. If a map is invertible, there is another map that exactly undoes it. In coordinates, multiplying the two matrices in either order yields the identity. Row reduction supplies a systematic way to determine whether this is possible and, if so, to calculate the inverse.

For a linear map between finite-dimensional spaces of equal dimension, invertibility, injectivity, surjectivity, and full rank are equivalent. They are not equivalent without the equal-dimension qualification. Embedding a plane into three-space is injective, but no inverse defined on all of three-space is possible.

The main lesson is that a matrix is a coordinate account of a transformation. Choosing convenient coordinates may make a calculation much easier, but the map's mathematical content must not depend on which coordinate system we happen to write down.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Solving Linear Systems: From Equations to Elimination

**Track:** Linear Algebra from First Principles. **Background:** arithmetic, algebraic equations and coordinates. **Question:** when do several linear measurements determine an unknown uniquely?

#### Mathematical companion (not spoken)

For a system \(Ax=b\), elementary row operations are multiplication on the left by invertible elementary matrices; hence \(Ax=b\) and \(EAx=Eb\) have identical solution sets. For the receipt example,
\[
\left[\begin{array}{cc|c}2&1&7\\1&3&11\end{array}\right]
\to\left[\begin{array}{cc|c}1&3&11\\0&-5&-15\end{array}\right]
\to\left[\begin{array}{cc|c}1&0&2\\0&1&3\end{array}\right].
\]
For \(Ax=b\) consistent, the complete set of solutions is \(x_0+\ker A\). A contradiction row \([0\ \cdots\ 0\mid c]\), \(c\ne0\), rules out all solutions. Over an infinite field, a nontrivial kernel yields infinitely many solutions. Over a finite field it yields multiple but finitely many.

##### Exercises with answers

1. Solve \(x+y=5\), \(2x-y=1\). **Answer:** \(x=2,y=3\).
2. Does \(x+y=1,2x+2y=3\) have a solution? **Answer:** no; doubling the first equation contradicts the second.
3. Solve \(x+2y+z=0\). **Answer:** \((x,y,z)=(-2s-t,s,t)\) for arbitrary real \(s,t\).
4. Why are row swaps reversible? **Answer:** exchanging the same pair a second time restores the original system.

##### Sources and further reading

- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), systems and Gauss's method.
- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), lectures on elimination and nullspaces.
- [System of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations).

### Vectors, Linear Combinations, and Subspaces

**Track:** Linear Algebra from First Principles. **Background:** basic algebra and coordinate pairs. **Question:** what kind of objects can be added and scaled, and why does that matter?

#### Mathematical companion (not spoken)

A vector space \(V\) over a field \(\mathbb F\) has operations \(V\times V\to V\) and \(\mathbb F\times V\to V\) satisfying additive abelian-group and compatibility axioms. The span of \(v_1,\dots,v_k\) is
\[
\operatorname{span}\{v_i\}=\left\{\sum_{i=1}^{k}a_i v_i:a_i\in\mathbb F\right\}.
\]
The kernel of \(\ell(x,y,z)=x+y+z\) is a subspace. The affine level set \(\ell^{-1}(1)\) is not. If \(u=(1,2)\), \(v=(2,3)\), then \((x,y)=a u+b v\) has solution \(a=2y-3x\), \(b=2x-y\). The vector space of polynomials is infinite-dimensional, unlike \(\mathbb F[x]_{\le d}\).

##### Exercises with answers

1. Is \(\{(x,y):y=3x\}\) a subspace? **Answer:** yes; it is the span of \((1,3)\).
2. Is the set of nonzero vectors a subspace? **Answer:** no, it does not contain zero.
3. Describe \(\operatorname{span}\{(1,0),(1,1)\}\). **Answer:** the entire plane, since \((x,y)=(x-y)(1,0)+y(1,1)\).
4. Why is the collection of even polynomials a subspace? **Answer:** sums and scalar multiples preserve the property \(p(-x)=p(x)\).

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), chapters on vector spaces and linear maps.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), subspaces and span.
- [Vector space](https://en.wikipedia.org/wiki/Vector_space).

### Independence, Bases, and Dimension: How Many Directions?

**Track:** Linear Algebra from First Principles. **Background:** vectors, span and elementary equations. **Question:** when is a description of a vector both complete and free of redundancy?

#### Mathematical companion (not spoken)

A finite family \((v_i)_{i=1}^k\) is independent iff \(\sum a_i v_i=0\Rightarrow a_i=0\) for all \(i\). A basis is independent and spanning. If \(S=(s_1,\dots,s_n)\) spans \(V\), any independent family in \(V\) has at most \(n\) members by the kernel argument applied to its coordinate matrix. Therefore the length of a basis is uniquely determined, \(\dim_{\mathbb F}V\).

For \(V=\mathbb R[x]_{\le2}\), \((1,x,x^2)\) is a basis and \(\dim V=3\). In \(\mathbb R^3\), \((1,0,1),(0,1,1),(1,1,2)\) is dependent, the last being the sum of the first two.

##### Exercises with answers

1. Is \((1,0),(2,0)\) independent? **Answer:** no.
2. Find a basis of \(\{(x,y,z):x+y+z=0\}\). **Answer:** \((1,0,-1),(0,1,-1)\).
3. Give the dimension of polynomials of degree at most four. **Answer:** five, with basis \(1,x,x^2,x^3,x^4\).
4. Can six vectors span \(\mathbb R^7\)? **Answer:** no; a spanning family must have at least seven members.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), finite-dimensional spaces and basis theorems.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), basis and dimension.
- [Basis (linear algebra)](https://en.wikipedia.org/wiki/Basis_(linear_algebra)).

### Linear Maps, Kernels, and Rank–Nullity

**Track:** Linear Algebra from First Principles. **Background:** bases, vector spaces, elimination. **Question:** what information does a linear transformation preserve, erase, or create?

#### Mathematical companion (not spoken)

A linear map \(T:V\to W\) satisfies \(T(au+bv)=aT(u)+bT(v)\). Its kernel and image are subspaces. \(T\) is injective iff \(\ker T=\{0\}\), and surjective iff \(\operatorname{im}T=W\). For finite-dimensional \(V\),
\[
\dim V=\dim\ker T+\dim\operatorname{im}T.
\]
Proof: choose \(k_1,\dots,k_r\) a basis of \(\ker T\); extend to \(k_1,\dots,k_r,v_1,\dots,v_s\) of \(V\). Then \(Tv_1,\dots,Tv_s\) is a basis of \(\operatorname{im}T\).
For \(T(x,y,z)=(x+y,y+z)\), \(\ker T=\operatorname{span}\{(-1,1,-1)\}\) and \(\operatorname{rank}T=2\).

##### Exercises with answers

1. Find \(\ker T\) for \(T(x,y)=(x,0)\). **Answer:** \(\{(0,y)\}\).
2. Is the map \(T(x,y)=(x,y,0)\) injective? Surjective onto \(\mathbb R^3\)? **Answer:** injective, not surjective.
3. If \(\dim V=8\) and \(\operatorname{rank}T=5\), find nullity. **Answer:** three.
4. Show \(\ker T\) is a subspace. **Answer:** zero maps to zero and \(T(au+bv)=0\) when both inputs lie in the kernel.

##### Sources and further reading

- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), linear maps and fundamental theorem of linear maps.
- Jim Hefferon, [Linear Algebra](https://hefferon.net/linearalgebra/), nullspaces and images.
- [Rank–nullity theorem](https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem).

### Matrices, Composition, and Changing Coordinates

**Track:** Linear Algebra from First Principles. **Background:** bases and linear maps. **Question:** how can the same transformation have different matrices without changing its action?

#### Mathematical companion (not spoken)

Given ordered bases \(\mathcal B\) of \(V\) and \(\mathcal C\) of \(W\), \([T]_{\mathcal C\leftarrow\mathcal B}\) has columns \([T(b_j)]_{\mathcal C}\). Composition gives \([S\circ T]=[S][T]\) with bases matched. Let \(P=[u\ v]=\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}\). Then \([x]_{\mathrm{std}}=P[x]_{\mathcal B}\), \([x]_{\mathcal B}=P^{-1}[x]_{\mathrm{std}}\), and \([T]_{\mathcal B}=P^{-1}[T]_{\mathrm{std}}P\). For \(A=\operatorname{diag}(2,3)\), \(P^{-1}AP=\begin{psmallmatrix}5/2&-1/2\\-1/2&5/2\end{psmallmatrix}\).

##### Exercises with answers

1. What are the columns of the identity matrix? **Answer:** the coordinate basis vectors.
2. Express \((4,2)\) in the basis \(((1,1),(1,-1))\). **Answer:** \((3,1)\).
3. Why is \(AB\) the matrix for first \(B\), then \(A\)? **Answer:** its \(j\)-th column is \(A\) applied to the \(j\)-th column of \(B\).
4. Does changing basis change the kernel dimension? **Answer:** no, because coordinate isomorphisms do not change the underlying solution space.

##### Sources and further reading

- MIT OpenCourseWare, [18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/), matrices and coordinate systems.
- Sheldon Axler, [Linear Algebra Done Right](https://linear.axler.net/), matrices of linear maps.
- [Change of basis](https://en.wikipedia.org/wiki/Change_of_basis).
