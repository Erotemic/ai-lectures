# 021200 — Almost-Complex Structures: Turning Symplectic Area into Length

**Track:** Topology and Geometry. **Background:** tangent vectors, differential forms, linear maps, symplectic two-forms. **Central question:** how can an antisymmetric area measurement be combined with a complex structure to define a positive metric?

<!-- BEGIN SPOKEN LECTURE -->

# Almost-Complex Structures: Turning Symplectic Area into Length

Imagine that someone gives you a map of a city that records the signed area of every tiny parallelogram, but supplies no rulers and no way to measure angles. That is roughly the information carried by a symplectic form. It compares two directions at a time, changes sign when we exchange them, and assigns zero when both directions are the same.

To talk about the length of a curve, or the energy of a map from a surface, we need something more. An almost-complex structure supplies a consistent way to turn a tangent direction through a quarter turn. Combining this rotation with symplectic area produces a metric. This is the bridge that lets methods from complex analysis and partial differential equations enter symplectic geometry.

## A quarter turn in the plane

Take the ordinary position-momentum plane with coordinates q and p. Its symplectic form is d q wedge d p. It reports positive area on the ordered pair consisting of the q direction followed by the p direction.

Define an operation J that sends the q direction to the p direction and the p direction to minus the q direction. Apply J twice and every vector changes sign. This is the equation J squared equals minus the identity. Multiplication by the imaginary number i has exactly the same property, which is why we use the word complex.

Now take any vector v. Pair v with J of v using symplectic area. In the standard plane the answer is the ordinary squared length of v. For two potentially different vectors v and w, pairing v with J of w gives their usual dot product. A quantity that was originally antisymmetric has become a symmetric positive metric, because the quarter turn makes the second argument different.

That construction has three requirements. J squared must be minus the identity. The symplectic form must remain unchanged if we rotate both inputs by J. And the pairing of a nonzero vector with its J rotation must be strictly positive. When all three hold, we call J compatible with the symplectic form.

## More than one useful choice

The standard quarter turn is not forced. Suppose that one unit along q should have length different from one unit along p. Choose a positive number a. Define J to send the unit q direction to a times the p direction, and send the unit p direction to minus one over a times the q direction. Two applications of J still reverse every vector. The resulting metric measures q displacements with squared scale a and p displacements with squared scale one over a.

Every choice of positive a gives a legitimate compatible complex structure. The symplectic area d q wedge d p has not changed; only the associated metric has. So a symplectic manifold does not single out one metric. Instead it permits a large family of metrics tied to choices of compatible J.

This flexibility matters later. A well-chosen J can simplify a differential equation, make a geometric symmetry visible, or help make a moduli space of solutions regular. Yet changing J does not mean changing the underlying symplectic form.

## From one plane to a manifold

At each point of a symplectic manifold, the tangent space is an even-dimensional symplectic vector space. Linear algebra produces compatible complex structures on such spaces. More importantly, these choices can be made smoothly as we move from point to point. Every symplectic manifold therefore admits compatible almost-complex structures.

Why 'almost'? Because each tangent space separately looks like a complex vector space, but that does not guarantee complex coordinates that fit together on neighborhoods. The integrability condition asks whether we can choose genuine complex charts whose derivatives agree with J. A complex manifold has such charts; a general almost-complex manifold need not.

In real dimension two, every smooth almost-complex structure is integrable. On surfaces, the analytic and almost-complex pictures coincide locally. In four or more real dimensions, the integrability obstruction can be nonzero. That is precisely why studying curves that respect J is more flexible than requiring the entire target to be a complex manifold.

## Compatible versus merely tame

Another word appears often in the advanced literature: tame. A symplectic form tames J if the area pairing of v with J of v is positive for every nonzero v. Compatibility demands more, including preservation of the symplectic form under J on both arguments. Taming is the weaker condition.

For a tame J, the quantity obtained by pairing v with J of w need not itself be symmetric. It does, however, have a positive quadratic part and still gives useful positivity for J-holomorphic curves. For our first calculations, compatible J is simpler because it produces a genuine metric directly.

## Why a complex rotation helps analyze curves

Suppose a map carries a two-dimensional surface into our symplectic manifold. A small region in the surface has two coordinate directions. We can ask whether differentiating in the second direction is the same as differentiating in the first direction and then applying J. If the domain also has its own quarter-turn operation, the clean statement is that differentiation commutes with those two quarter turns.

This is the definition of a pseudoholomorphic, or J-holomorphic, map. In the ordinary complex plane it reduces to the Cauchy-Riemann equations. On an arbitrary symplectic manifold the same equation still makes sense, even when there is no complex coordinate system on the target.

For such a map, area and energy become linked. The metric constructed from the symplectic form and J measures the total squared derivative of the map. The map's adherence to the complex-rotation equation forces that energy to equal its symplectic area, with a suitable normalization. Thus area controls an analytic quantity that can constrain sequences of curves.

The relationship is powerful but should not be overread. Positive energy by itself does not establish compactness, and the existence of a compatible J does not make all maps holomorphic. What it does is turn symplectic geometry into a setting where precise elliptic equations can be posed and estimated.

When you next encounter a holomorphic curve in a symplectic manifold, remember the sequence of constructions. We begin with alternating area, choose a quarter turn on tangent vectors, obtain a positive metric, and then ask which surface maps respect the two quarter turns. The apparently abstract J is the device that makes all the later analysis possible.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Adopt the track convention \(\omega=dq\wedge dp\) and \(\iota_{X_H}\omega=dH\). On \(\mathbb R^2\), define \(J_0\partial_q=\partial_p\), \(J_0\partial_p=-\partial_q\). Then \(J_0^2=-I\), \(\omega(J_0v,J_0w)=\omega(v,w)\), and \(g(v,w)=\omega(v,J_0w)=v\cdot w\). More generally for \(a>0\), \(J_a=\begin{psmallmatrix}0&-a^{-1}\\a&0\end{psmallmatrix}\) in the ordered basis \((\partial_q,\partial_p)\), and \(g_a=\mathrm{diag}(a,a^{-1})\).

A compatible almost-complex structure satisfies \(J^2=-I\), \(\omega(Jv,Jw)=\omega(v,w)\), and \(\omega(v,Jv)>0\) for nonzero \(v\). A tame one only requires the final positivity in addition to \(J^2=-I\). A \(J\)-holomorphic map \(u:(\Sigma,j)\to(M,J)\) satisfies \(du\circ j=J\circ du\). For compatible \(J\) and a conformal metric on the domain, \(E(u)=\frac12\int_\Sigma |du|^2=\int_\Sigma u^*\omega\) for a \(J\)-holomorphic map, assuming suitable convergence if the domain is noncompact.

### Exercises with answers

1. **Quarter turn.** Compute \(J_0^2\partial_q\). **Answer:** \(-\partial_q\).
2. **Scaled lengths.** What are \(g_a(\partial_q,\partial_q)\) and \(g_a(\partial_p,\partial_p)\)? **Answer:** \(a\) and \(a^{-1}\).
3. **Symmetry.** Why is \(g(v,w)=\omega(v,Jw)\) symmetric for compatible \(J\)? **Answer:** \(g(w,v)=\omega(w,Jv)=-\omega(Jv,w)=\omega(v,Jw)\) by compatibility and alternation.
4. **Scope.** Does existence of a compatible almost-complex structure imply the target is a complex manifold? **Answer:** no; integrability is an additional condition.

### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), almost-complex geometry and compatibility.
- Dusa McDuff and Dietmar Salamon, [J-Holomorphic Curves and Symplectic Topology](https://bookstore.ams.org/coll-52), foundational monograph.
- [Almost complex manifold](https://en.wikipedia.org/wiki/Almost_complex_manifold); [Symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold).
