# 018100 — Characteristic Classes by Example: Gluing Lines over a Sphere

**Track:** Topology and Geometry. **Background:** vector bundles, transition functions, winding numbers, de Rham cohomology, basic curvature. **Central question:** how can local triviality hide a global twist, and how do we measure it?

<!-- BEGIN SPOKEN LECTURE -->

# Characteristic Classes by Example: Gluing Lines over a Sphere

Picture two smooth disks, one covering the northern hemisphere of a sphere and the other covering the southern hemisphere. Over each disk, place a copy of the complex plane at every point. Locally, everything looks like an ordinary product: a disk times a complex line.

To make one line bundle over the entire sphere, we must identify the fibers where the two disks overlap. We are free to rotate a complex fiber by a phase before gluing it to the fiber described in the other chart. If that phase winds as we go around the equator, the resulting bundle may be globally twisted even though it looks trivial from either hemisphere.

This construction makes the first Chern class tangible. Instead of beginning with an abstract characteristic class, we will build a family of bundles and ask what integer distinguishes them.

## Gluing by an angle-dependent rotation

On the equatorial circle, choose an angle that increases once around the circle. Define the gluing rule to rotate each complex line through an angle equal to k times the equatorial angle. Here k is an integer.

Why must k be an integer for this simple rule? Returning to the same equatorial point must give the same rotation. If the angle increases by one full turn, the fiber rotation changes by k full turns. That is the identity exactly when k is integral.

For k equal to zero, gluing uses the identity rotation. We recover the product bundle: every fiber can be identified with one fixed complex line globally. For k equal to one, the fiber undergoes one turn around the equator. For k equal to two, it undergoes two. Each choice has a winding number.

One can change the trivializations on the northern and southern disks. Doing so changes the formula for the transition function, but not its winding number. A phase defined throughout a disk cannot acquire nonzero boundary winding without becoming singular or discontinuous somewhere. Therefore the integer survives changes of local description.

## A characteristic class records the obstruction

For a complex line bundle over the sphere, the first Chern number equals the winding integer, after fixing compatible sphere orientation and gluing conventions. More generally, the first Chern class is an integral cohomology class in degree two. Its evaluation on an oriented closed surface gives an integer.

The word integral here is important. A characteristic class belongs to cohomology with integer coefficients. A differential form representing its image in real cohomology may reveal the same integer after integration, but real forms cannot see torsion classes. These are two related descriptions, not identical stores of information.

For complex line bundles over suitable spaces, including smooth manifolds, the first Chern class actually classifies the isomorphism class of the bundle. For higher-rank bundles, characteristic classes are powerful invariants but need not determine the bundle completely.

## Why a nowhere-vanishing section matters

A section chooses one vector from each fiber, continuously. If a complex line bundle has a nowhere-zero section, that section gives a global way to identify every fiber with the complex line: multiply the chosen vector by arbitrary complex numbers. The bundle must therefore be trivial.

Consequently, a line bundle with nonzero first Chern class cannot have a section that avoids zero everywhere. This obstruction is visible in the hemisphere construction. A proposed section would have to agree with itself after being rotated by a nonzero winding along the equator. Something must give: the section cannot remain globally continuous and nonvanishing.

For a real oriented rank-two bundle, rotation of each fiber makes it into a complex line bundle. In that case the Euler class agrees with the first Chern class under the induced orientation convention. The tangent bundle of the two-sphere is the standard example. Its Euler number is two, matching the sphere's Euler characteristic. That is one reason the hairy-ball theorem is true: a continuous tangent vector field on the sphere cannot be everywhere nonzero.

## Curvature finds the same integer

Now equip the bundle with a unitary connection. Locally it is represented by an imaginary-valued one-form. Its curvature is an imaginary-valued two-form. The local curvature expressions agree across charts in the abelian case, even though the connection one-forms themselves differ by derivatives of the transition phases.

With a fixed conventional normalization, multiplying the curvature by the imaginary unit and dividing by two pi produces a real two-form representing the first Chern class in de Rham cohomology. Integrating it over the oriented sphere gives the same integer detected by the winding of the transition function.

There is a chain of reasoning hidden inside that conclusion. First we construct the bundle from gluing maps. Next we choose a connection. Then we prove that the resulting curvature form changes by an exact form when the connection changes, so its cohomology class does not depend on that choice. Finally an integrality theorem relates that class to the transition-map winding. One should not assume that every arbitrary real two-form integrates to an integer.

## Twisting and holonomy are different questions

Suppose we have a flat connection on a circle. Transport a vector once around the circle and it can return rotated by a phase. That is nontrivial holonomy, even though every complex line bundle over a circle is topologically trivial because the circle has no second cohomology.

Thus a curved connection need not live on a twisted bundle, and a flat connection need not have trivial parallel transport. Bundle topology, connection curvature, and holonomy are three related but distinct pieces of information.

Later gauge-theoretic lectures use this distinction constantly. An instanton is not defined only by a topological bundle class. It is a special connection, satisfying differential equations, on a bundle. Characteristic classes constrain which connections are possible and can assign topological charges to their curvature.

The sphere construction gives a complete example to keep in mind: two locally trivial pieces, an equatorial phase winding, an integer Chern number, and a curvature integral representing that integer. When a more complicated invariant appears, look for the same ingredients: local data, compatibility on overlaps, and a global obstruction that cannot be transformed away.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Write \(S^2=D_N\cup D_S\) with overlapping equatorial annulus retracting to \(S^1\). Clutch a complex line bundle with \(g_k:S^1\to U(1)\), \(g_k(e^{i\varphi})=e^{ik\varphi}\). The winding number is \(k\). With corresponding orientation and clutching conventions, \(\langle c_1(L_k),[S^2]\rangle=k\). Reversing the sphere orientation or the gluing convention reverses this signed evaluation.

For a unitary line connection written \(\nabla=d+A\), \(A\in i\Omega^1\), \(F=dA\). The adopted normalization is \(c_1(L)_{\mathbf R}=[iF/(2\pi)]\) (the real image of the integral class). Under a local gauge change \(g\), \(A'=A+g^{-1}dg\), while \(F'=F\). For a globally defined change of connection \(A\mapsto A+i\eta\) on a fixed line bundle, \(iF/(2\pi)\) changes by the exact form \(-d\eta/(2\pi)\).

An oriented rank-two real vector bundle is a complex line bundle after choosing a compatible complex structure, with \(e(E)=c_1(E_{\mathbf C})\). For \(E=TS^2\), \(\int_{S^2}e(TS^2)=\chi(S^2)=2\). Over \(S^1\), all complex line bundles have \(c_1=0\), but flat \(U(1)\) connections can have nontrivial holonomy.

### Exercises with answers

1. **Winding.** What Chern number results from a phase rotating three times around the equator? **Answer:** \(+3\) in the stated orientation and gluing convention.
2. **Section.** Could a complex line bundle with Chern number one have a global nowhere-zero section? **Answer:** No. Such a section would trivialize it.
3. **Tangent sphere.** What is the Euler number of \(TS^2\)? **Answer:** Two, so a globally nonzero tangent field does not exist.
4. **Flat transport.** Does vanishing curvature on a circle force trivial holonomy? **Answer:** No. Global transport can retain a phase.

### Sources and further reading

- Allen Hatcher, [Vector Bundles and K-Theory](https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html).
- University of Toronto, [Equivariant Cohomology lecture notes](https://www.math.toronto.edu/~jeffrey/mat1312/lec10.eqcoh.pdf).
- Overviews: [Chern class](https://en.wikipedia.org/wiki/Chern_class), [Clutching construction](https://en.wikipedia.org/wiki/Clutching_construction).
