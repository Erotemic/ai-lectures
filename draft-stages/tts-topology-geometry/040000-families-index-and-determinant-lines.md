# 040000 - Families Index Theory and Determinant Line Bundles

**Track:** Topology and Geometry. **Background:** Fredholm operators, vector bundles, elliptic index theory, and characteristic classes. **Central question:** how can the index of a smoothly varying differential operator remain meaningful when kernels suddenly change dimension?

<!-- BEGIN SPOKEN LECTURE -->

# A number can stay constant while the spaces jump

The index of a Fredholm operator is the dimension of its kernel minus the dimension of its cokernel. For a single elliptic operator, the Atiyah–Singer index theorem relates this analytic number to topological characteristic classes.

But differential operators often come in families. Imagine changing a metric, a connection, or a parameter on which a geometric problem depends. The dimension of the kernel can jump at special parameter values. If we tried to assemble the kernels into one vector bundle over the parameter space, the varying dimensions could make that impossible.

The families index theorem resolves this by using a virtual vector bundle. Instead of demanding a kernel bundle and a cokernel bundle separately, it constructs their formal difference in K-theory. That difference can vary continuously in the correct topological sense even when the two dimensions jump together.

# The smallest family has a singular-looking point

Consider the family of linear maps from the real line to itself that multiply by a real parameter t. For every nonzero t, the map is invertible. Its kernel and cokernel both have dimension zero. At t equal to zero, the map is the zero map. Its kernel and cokernel both have dimension one.

If we recorded only the kernel dimension, we would see a sudden jump. Yet the index is zero for every t. The kernel and cokernel jump by the same amount. A virtual difference captures the information that stays stable.

A single constant index is still not the whole families theory. Over a parameter space with nontrivial topology, a family of Fredholm operators can carry a nontrivial K-theory class even if its numerical index is zero at every point. How the operators vary around loops and higher-dimensional cycles contains information that cannot be read from any one operator in isolation.

# The index bundle

For a well-behaved continuous family of Fredholm operators over a compact parameter space, one can choose finite-dimensional auxiliary data that stabilize the family. The resulting virtual bundle class is independent of these choices. It is the index bundle.

The families Atiyah–Singer theorem computes its Chern character using the geometry of the fibers. When the operators are, for example, spin-c Dirac operators along the fibers of a smooth proper family, a fiber-integration formula involves the characteristic class of the vertical tangent bundle and the Chern character of the twisting bundle.

This is a stronger statement than the ordinary index theorem. The ordinary theorem recovers one integer on each connected component of the parameter space. The families theorem can recover cohomology classes of several degrees on the entire base.

The word “families” does not mean merely repeating the ordinary index calculation for many parameter choices. It means retaining the topology of how those choices fit together.

# A determinant line from kernel and cokernel

There is a particularly concrete one-dimensional shadow of the index bundle: the determinant line. At an operator D, form the top exterior power of the kernel and tensor it with the dual of the top exterior power of the cokernel.

At a point where the dimensions jump, this construction may look as though its rank-one factors have changed. Yet through the determinant-line formalism the resulting one-dimensional lines glue into a line bundle over the parameter space.

A line bundle can have nontrivial holonomy or first Chern class. In geometric families, natural metrics and connections on determinant lines allow local curvature formulas. Thus the determinant line packages not only the integer index but also how the family twists over the base.

One should distinguish the determinant line from choosing a nonzero numerical determinant of each operator. Differential operators are infinite dimensional, and eigenvalues can pass through zero. Analytic determinant constructions require regularization and choices; the determinant line is the geometric home in which those constructions live.

# A family of Dolbeault operators

Consider a fixed elliptic curve, now meaning a smooth complex curve of genus one, and degree-zero holomorphic line bundles on it. Each line bundle defines a Dolbeault operator. Its index is the holomorphic Euler characteristic, the dimension of holomorphic sections minus the dimension of the first cohomology group.

For any degree-zero line bundle on this elliptic curve, the index is zero. For a nontrivial degree-zero line bundle, both cohomology groups vanish. For the trivial line bundle, the constant functions give one holomorphic section, and the first cohomology group also has dimension one.

The dimensions therefore jump from zero and zero to one and one. The numerical index stays zero. This is the geometric counterpart of the elementary multiplication-by-t family, with a far richer parameter space: the degree-zero Picard variety of the elliptic curve.

Such families show why it is dangerous to identify the families index with the collection of individual kernels. A stable virtual class survives precisely where a naive vector bundle of kernels fails.

# Curvature and anomalies

Determinant lines also occur in mathematical physics, where phases of fermionic partition functions can behave as sections of a line bundle rather than as globally defined complex numbers. A nontrivial determinant line can obstruct choosing phases consistently around a parameter loop.

The relevant curvature and holonomy are governed by geometric data of a family of Dirac operators. Depending on the problem, this is described by Quillen metrics, Bismut–Freed connections, or related constructions. Those theories require precise analytic assumptions and regularization; a formal infinite product of eigenvalues is not a substitute.

The same mathematics therefore explains an abstract K-theory index, a concrete line-bundle obstruction, and the failure of a naive determinant to be globally single-valued. It is a good example of topology arising not from the space on which one operator acts, but from the whole collection of operators.

# The lesson of a jumping kernel

A kernel jump may signal special geometry: an extra holomorphic section, a zero mode, or a symmetry appearing at one parameter. The jump should not be erased. But it also should not lead us to conclude that no continuous invariant can be built.

Families index theory records exactly the information that remains invariant when dimensions rearrange. The determinant line distills part of it into a bundle whose twisting can be observed geometrically. A single index integer cannot see that twisting; a family K-theory class can.

The important conceptual move is to stop asking for each changing solution space to form an ordinary bundle. Instead, encode the balance between solutions and obstructions. That balance can remain geometrically coherent across the very parameter values where individual dimensions fail to behave continuously.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a family `D_b:E_b->F_b` of Fredholm operators over compact base `B`, the index defines `[ker D]-[coker D] in K^0(B)` after finite-dimensional stabilization; kernels need not individually be vector bundles. For the family `D_t:R->R`, `D_t(x)=tx`, both dimensions equal zero for `t !=0` and both equal one for `t=0`, so `ind D_t=0` throughout.

The determinant line, with a consistent dual convention, is
\[
\det D_b=\Lambda^{\max}\ker D_b\otimes\left(\Lambda^{\max}\operatorname{coker}D_b\right)^*.
\]
For a family of spin-c Dirac operators on fibers of `pi:M->B`, the cohomological families index formula is schematically
\[
\operatorname{ch}(\operatorname{Ind}D)=\pi_*\!\left(\widehat A(T^vM)e^{c_1(L)/2}\operatorname{ch}(E)\right),
\]
with the standard orientation/spin-c and twisting assumptions. For `L` of degree zero on an elliptic curve, `h^0(L)=h^1(L)=0` unless `L` is trivial, when both are one. Thus `chi(L)=0` regardless, but individual kernel and cokernel dimensions jump.

### Exercises with answers

1. What is the index of `D_0:R->R` given by multiplication by zero? **Answer:** `dim ker - dim coker=1-1=0`.
2. Do constant numerical indices imply the family index class in `K^0(B)` is trivial? **Answer:** No; higher topological classes may remain.
3. What is the determinant line fiber of an invertible operator? **Answer:** canonically the one-dimensional scalar line, since kernel and cokernel are zero.
4. Why is a family of kernel spaces not always a vector bundle? **Answer:** kernel dimension can jump with the parameter.

### Reading and source notes

- [Atiyah and Singer, The Index of Elliptic Operators: IV](https://doi.org/10.2307/1970756), the families index theorem.
- [Bismut and Freed, The Analysis of Elliptic Families: Metrics and Connections on Determinant Bundles](https://doi.org/10.1007/BF01210930), determinant-line geometry.
- [Freed, On Determinant Line Bundles](https://abel.math.harvard.edu/~dafr/detsur.pdf), detailed exposition of determinants and families.
