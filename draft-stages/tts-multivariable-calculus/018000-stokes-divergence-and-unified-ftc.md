# 018000 — Stokes and Divergence: The Fundamental Theorem in Three Dimensions

**Track:** Multivariable Calculus from First Principles. **Background:** line integrals, surface flux, divergence and curl. **Question:** why do derivatives inside a region control integrals along its boundary?

<!-- BEGIN SPOKEN LECTURE -->

# Stokes and Divergence: The Fundamental Theorem in Three Dimensions

One-variable calculus has a remarkable theorem. Add the rate of change of a function over an interval, and the answer depends only on the function values at the endpoints. The derivative's contributions throughout the interior combine into a boundary difference. In several dimensions, two major theorems have the same structure: Stokes' theorem relates curl through a surface to circulation along its edge, and the divergence theorem relates divergence inside a solid to flux through its closed boundary.

These statements are powerful, but they become clearer if we calculate both sides of a complete example.

## Curl and circulation through a disk

Take the three-dimensional vector field F whose components are negative one half y, one half x, and zero. This field rotates around the vertical axis. Its curl is the constant vector zero comma zero comma one. The vertical component can be computed from the x derivative of the second field component minus the y derivative of the first: one half minus negative one half equals one.

Consider the flat unit disk in the horizontal plane, oriented upward. The flux of curl through this disk is the integral of one over the disk, which is pi. Stokes' theorem predicts that the circulation of F around the boundary circle, taken counterclockwise when viewed from above, is also pi.

Parametrize the boundary with x equals cosine t and y equals sine t over a full turn. The field along it is negative one half sine t comma one half cosine t comma zero. The tangent velocity is negative sine t comma cosine t comma zero. Their dot product is one half. Integrate over two pi units of parameter and obtain pi. The two sides agree exactly.

Notice the geometric role of orientation. Upward surface normal corresponds, by the right-hand rule, to counterclockwise boundary orientation as seen from above. Reverse the normal while keeping the physical field fixed, and both sides change sign when the boundary orientation is reversed consistently.

## Why surface shape can change while boundary remains fixed

Imagine replacing the flat disk by a smooth curved cap with the same circular boundary, while keeping the upward-compatible orientation. Stokes' theorem says the integral of curl over the cap is still the boundary circulation, provided the field is smooth on the relevant neighborhood. The cap may have much more area than the flat disk, but the curl flux takes the angle between curl and the normal into account. For our constant vertical curl, the total upward projected area remains pi.

This is a useful check against the mistaken belief that an integral of a vector field over a surface is simply field strength times surface area. The oriented normal matters.

## Divergence and net outflow from a ball

Now take the radial vector field G of x comma y comma z equal to x comma y comma z. Its divergence is three, because the derivative of each component with respect to its corresponding coordinate is one. Inside the unit ball, the total integral of divergence is three times the ball's volume, or three times four pi over three. The result is four pi.

On the unit sphere, the outward unit normal equals the position vector. Our field G equals that same vector, so its dot product with the unit normal is one everywhere on the sphere. Integrating one over the sphere gives surface area four pi. Again the interior calculation and boundary calculation agree.

This is the divergence theorem: the total local rate of outflow inside a solid equals the net outward flux through its enclosing surface. It is an exact mathematical identity for sufficiently regular regions and fields, not an approximation based on physical intuition.

## The cancellation mechanism

Why should either theorem be true? Divide a surface into many smaller surface patches. Their boundary curves contain many shared internal edges. A shared edge appears twice, with opposite orientation, so its two line integrals cancel. Only the outer boundary survives. At the local level, curl measures circulation per oriented area. Summing over all the patches gives the flux of curl through the surface, while the boundary sum collapses to the circulation around the outside.

For the divergence theorem, divide a solid into many small volumes. Each internal face is outward-facing for one tiny volume and inward-facing for its neighbor, so its flux contributions cancel. Only faces on the external boundary remain. Locally, divergence measures net outward flux per volume. Sum those local rates, and the net flux through the outer boundary appears.

These cancellation arguments are the higher-dimensional relatives of the fundamental theorem of calculus on an interval. The interior pieces disappear in pairs because shared boundaries inherit opposite orientations.

## Conservation laws and what theorems do not claim

Suppose G represents fluid velocity and the fluid is incompressible, so divergence is zero in a region. The divergence theorem says the net outward flux through any suitable closed surface in that region is zero. It does not say the velocity is zero on the surface. Fluid may enter one side and leave the other in equal amounts.

Similarly, zero curl need not mean a vector field vanishes. It says the local circulation density vanishes. In a simply connected region this condition helps characterize gradient fields, but domains with holes need special care. Local derivative data and global topology are connected, not interchangeable.

In physical applications there may be sources, singularities, or discontinuities. The classical theorems require appropriate smoothness of the field and regularity of the domain. Distributional and weak versions extend them to rougher settings, and additional terms may appear when singularities are present. It is better to state the conditions than to apply a beautiful formula outside its domain of validity.

## The unifying formula

The later language of differential forms expresses these results in one compact pattern: integrate the exterior derivative of a form over an oriented region, and obtain the integral of the original form over its oriented boundary. In one dimension this is the fundamental theorem of calculus. On a planar region it becomes Green's theorem. On an oriented surface in three dimensions it becomes Stokes' theorem. On a solid it gives the divergence theorem after the appropriate identification of forms with vector fields and volume elements.

You do not need differential forms to verify the examples we just computed. But after seeing the same boundary-cancellation mechanism three times, the abstract formulation is no longer an arbitrary generalization. It is a way of preserving the common idea while removing dependence on the coordinates chosen for each special case.

The core lesson is simple but deep: derivatives describe local change, while integrals accumulate change. Under the right hypotheses, accumulation over an interior can be measured entirely at the boundary. That principle connects elementary calculus to geometry, topology, physics and partial differential equations.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(F\in C^1\) on a neighborhood of an oriented smooth surface \(S\) with piecewise smooth boundary, with compatible right-hand-rule boundary orientation,
\[
\oint_{\partial S}F\cdot dr=\iint_S(\nabla\times F)\cdot n\,dS.
\]
For \(F=(-y/2,x/2,0)\), \(\nabla\times F=(0,0,1)\); on the upward unit disk, both sides equal \(\pi\).

For \(G\in C^1\) on a neighborhood of a suitable bounded solid \(V\) with outward-oriented piecewise smooth boundary,
\[
\iiint_V\nabla\cdot G\,dV=\iint_{\partial V}G\cdot n\,dS.
\]
For \(G=(x,y,z)\) and the unit ball, \(\nabla\cdot G=3\), so \(3(4\pi/3)=4\pi\), while \(G\cdot n=1\) on the unit sphere with area \(4\pi\).

The generalized Stokes theorem, \(\int_M d\omega=\int_{\partial M}\omega\), requires consistent orientations and hypotheses ensuring both integrals are defined; the classical theorems are special coordinate incarnations.

### Exercises with answers

1. Compute \(\nabla\times(-y,x,0)\). **Answer:** \((0,0,2)\).
2. Find flux of \(G=(x,y,z)\) through the outward sphere of radius \(R\). **Answer:** \(3(4\pi R^3/3)=4\pi R^3\).
3. Does \(\nabla\cdot G=0\) force \(G=0\)? **Answer:** no, e.g. a constant nonzero vector field has divergence zero.
4. What determines boundary orientation for Stokes? **Answer:** the chosen oriented surface normal via the right-hand rule.

### Sources and further reading

- MIT OpenCourseWare, [18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/), Stokes and divergence theorems.
- MIT OpenCourseWare, [18.022 Calculus of Several Variables](https://ocw.mit.edu/courses/18-022-calculus-of-several-variables-fall-2010/pages/syllabus/), forms and generalized Stokes.
- [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem); [Divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem).
