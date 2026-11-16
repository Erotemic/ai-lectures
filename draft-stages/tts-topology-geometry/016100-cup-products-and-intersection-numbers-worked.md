# 016100 — Cup Products and Intersection Numbers: What Two Holes Say to Each Other

**Track:** Topology and Geometry. **Background:** cycles, cohomology, closed forms, the circle and torus. **Central question:** why do the dimensions of cohomology groups not tell the whole story?

<!-- BEGIN SPOKEN LECTURE -->

# Cup Products and Intersection Numbers: What Two Holes Say to Each Other

A torus has two independent directions in which a loop can wind: around its central hole and around the tube. We can describe those directions with two integers. But we can ask more than how many loops there are. We can ask how two loops meet, and whether two different one-dimensional measurements combine to detect the entire surface.

The mathematical tools for those questions are the cup product and intersection pairing. They are also the beginning of ideas that appear in characteristic classes, four-manifold topology, and gauge-theoretic invariants. Let us work through their meaning on the simplest nontrivial example.

## A closed form as a measurement

View a torus as a square with opposite sides identified. Choose a horizontal coordinate, x, and a vertical coordinate, y, each understood modulo one. The number x itself is not a globally single-valued real function on the torus. If you walk once around the horizontal direction, x has advanced by one even though you have returned to the same point.

Its infinitesimal differential, however, is globally well-defined. The one-form called d x assigns the horizontal component of a tiny displacement. Integrating it once around a horizontal loop gives one; integrating it around a vertical loop gives zero. Similarly, the form d y measures vertical winding.

Both forms are closed. Neither is globally exact, because the integral of an exact one-form around a closed loop would be zero. The two forms therefore represent distinct cohomology classes. They are dual measurements of the two fundamental loop directions.

What if we combine the two measurements? The wedge product d x wedge d y is an area form. Integrated over the oriented torus, it gives one when the square has unit area. Its two-dimensional cohomology class is not zero. The product of two one-dimensional classes has discovered a two-dimensional feature.

## Multiplication has orientation built in

Switch the order of the two one-forms. The wedge product changes sign: d y wedge d x is the negative of d x wedge d y. A small parallelogram oriented horizontal-then-vertical is positive, while vertical-then-horizontal is negative in our chosen orientation.

Cohomology has a corresponding multiplication, the cup product. On de Rham classes it is represented by wedge product. The rule is graded commutativity: exchanging degrees p and q introduces a sign determined by their product. For two degree-one classes the sign is negative.

This is why the two independent generators of first cohomology on a torus do not behave like ordinary commuting variables. Their product remembers orientation. Over real coefficients, a degree-one class wedged with itself is zero. The mixed product of our two generators is not.

The dimensions of the cohomology groups of a space are called its Betti numbers. Betti numbers tell us that the torus has one class in degree zero, two in degree one, and one in degree two. The cup product tells us how those classes interact. Two spaces can have the same Betti numbers yet different cohomology rings. Multiplication contains genuinely additional information.

## From products of forms to crossings of loops

Now draw one horizontal loop and one vertical loop on the torus. After choosing representatives in general position, they cross at one point. Give both loops directions, and give the torus an orientation. At each transverse crossing, we can count plus one or minus one according to whether the two tangent directions agree with the orientation of the surface.

For the standard horizontal and vertical loops, the signed intersection number is plus one. Reverse one loop and it becomes minus one. Move either loop without changing its homology class and, provided crossings are counted with signs, the total remains the same. Pairs of crossings can be created or canceled, but they appear with opposite signs.

The connection to differential forms is Poincaré duality. An oriented submanifold defines a cohomology class of complementary degree. Intersecting two suitably positioned cycles is reflected algebraically by multiplying their dual classes and integrating over the whole manifold.

There is an easy sign trap here. A one-form that integrates to one along a particular loop is not automatically the Poincaré dual of that same loop. Integrating along cycles and taking the dual class defined by intersection are related notions, but they involve a complementary direction and an orientation convention. One must write the pairing rather than guess the sign from a drawing.

## Why the pairing is nondegenerate

On a closed oriented manifold of dimension n, Poincaré duality pairs degree k cohomology with degree n minus k cohomology. Over the real numbers, the pairing integrates the wedge product of representatives over the manifold. Nondegenerate means that a nonzero class can be detected by pairing it with some complementary class.

On our two-torus, any first-degree class can be expressed as a multiple of d x plus a multiple of d y. If the first multiple is nonzero, pairing with d y detects it. If the second is nonzero, pairing with d x detects it, with an orientation sign. No nonzero first-degree class is invisible to every complementary class.

The statement requires the hypotheses. Without compactness, orientation, or appropriate treatment of boundaries, a naive integral pairing can fail to have this property. For a manifold with boundary, absolute and relative cohomology play different roles. Over the integers, torsion also requires care: integration against real differential forms cannot detect torsion classes.

## A short look at four dimensions

For an oriented four-manifold, two-dimensional cohomology can pair with itself. The resulting intersection form is a bilinear form on the middle-degree cohomology, after treating torsion appropriately. Its signature, parity, and other properties can constrain the topology and smooth structure of the manifold.

That observation explains why later lectures about Donaldson invariants and Seiberg–Witten theory care so much about intersection forms and classes of embedded surfaces. They are not merely counting individual holes. They are studying how cycles coexist, intersect, and interact with the smooth geometry.

The torus is the small model in which the algebra can be seen completely. One-dimensional measurements multiply to give an area measurement. Oriented loop intersections give signed integers. Poincaré duality identifies these two ways of describing the same underlying interaction. Once this example is secure, advanced cohomological pairings have a concrete starting point.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For \(T^2=\mathbf R^2/\mathbf Z^2\) oriented by \(dx\wedge dy\), \(H^*(T^2;\mathbf R)\) is the exterior algebra on \(a=[dx]\), \(b=[dy]\): \(a\wedge a=b\wedge b=0\), \(a\wedge b=-b\wedge a\), and \(\int_{T^2}a\wedge b=1\). The Betti numbers are \((1,2,1)\).

For a closed oriented smooth n-manifold, the real Poincaré pairing is \(H^k_{\mathrm{dR}}(M)\times H^{n-k}_{\mathrm{dR}}(M)\to\mathbf R\), \(([\alpha],[\beta])\mapsto\int_M\alpha\wedge\beta\); Poincaré duality says it is nondegenerate. The cup product on singular cohomology corresponds to wedge product under the de Rham isomorphism. If \(A,B\) are oriented cycles meeting transversely in complementary dimensions, then \(A\cdot B=\int_M\operatorname{PD}(A)\smile\operatorname{PD}(B)\), with consistent orientation and degree conventions.

For the coordinate loops \(A\) (positive x direction) and \(B\) (positive y direction), \(A\cdot B=+1\). Under conventions where \(\int_M\operatorname{PD}(C)\wedge\beta=\int_C\beta\), the duals are \(\operatorname{PD}(A)=-[dy]\), \(\operatorname{PD}(B)=[dx]\), so \(\int_M(-dy)\wedge dx=1\). This illustrates why integration-dual and Poincaré-dual are not the same identification.

### Exercises with answers

1. **Product.** Evaluate \(\int_{T^2}dy\wedge dx\). **Answer:** \(-1\) for the orientation \(dx\wedge dy\).
2. **Detection.** If \(u=3a+2b\), compute \(\int u\wedge a\) and \(\int u\wedge b\). **Answer:** \(-2\) and \(3\), respectively.
3. **Intersection.** What is the intersection number after reversing the vertical loop's orientation? **Answer:** \(-1\).
4. **Hypotheses.** Why does real de Rham pairing not see \(H_1(\mathbf{RP}^2;\mathbf Z)=\mathbf Z/2\)? **Answer:** Torsion maps to zero with real coefficients.

### Sources and further reading

- Allen Hatcher, [Algebraic Topology, Chapter 3: Cohomology](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html).
- MIT OpenCourseWare, [18.966 Geometry of Manifolds](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/pages/lecture-notes/).
- Overviews: [Cup product](https://en.wikipedia.org/wiki/Cup_product), [Intersection theory](https://en.wikipedia.org/wiki/Intersection_theory).
