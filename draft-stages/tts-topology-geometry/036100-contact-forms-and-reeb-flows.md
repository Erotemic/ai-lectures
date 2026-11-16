# 036100 — Contact Forms and Reeb Flows: Dynamics on an Odd-Dimensional Boundary

**Track:** Topology and Geometry. **Background:** vector fields, differential forms, exterior derivatives and symplectic geometry. **Question:** what geometry remains on the boundary of a symplectic region, and how does it determine distinguished trajectories?

<!-- BEGIN SPOKEN LECTURE -->

# Contact Forms and Reeb Flows: Dynamics on an Odd-Dimensional Boundary

A symplectic manifold has even dimension because its defining nondegenerate two-form pairs directions in twos. But the boundary of a compact symplectic region has odd dimension. What geometry can survive there? In many important cases, the answer is contact geometry: a maximally twisting family of hyperplanes, together with a distinguished direction of motion called the Reeb field.

This is the language of characteristic trajectories on energy surfaces, of symplectic filling problems, and of the periodic orbits counted by embedded contact homology.

## Start with planes that cannot fit together into surfaces

In ordinary three-space, imagine assigning a two-dimensional plane of permitted directions at every point. If those planes were horizontal everywhere, we could stack them into ordinary surfaces of constant height. Contact geometry begins with a different possibility: the planes twist as we move, so they cannot locally be the tangent planes of a family of surfaces.

A one-form alpha can describe a plane at each point by declaring that its kernel consists of the permitted directions. For a concrete model use coordinates x, y, z and define alpha to be d z minus y times d x. The permitted vectors have z component equal to y times their x component. The plane tips as y changes. Its two convenient spanning directions are the x direction plus y times the z direction, and the y direction.

Take the exterior derivative of alpha. It is d x wedge d y. This form measures area in the x-y directions. The three-form alpha wedge d alpha is d z wedge d x wedge d y, a nonzero volume form. Therefore this one-form defines a contact structure.

In general, on a manifold of dimension two n plus one, the contact condition says alpha wedged with n copies of d alpha is nowhere zero. It ensures that d alpha is nondegenerate when restricted to the hyperplane distribution given by the kernel of alpha. The form alpha is a contact form, and the hyperplane field is the underlying cooriented contact structure.

Contrast alpha equals d z. Its exterior derivative is zero. The kernel consists of horizontal planes that really do fit together into surfaces. It is not a contact form. The distinction is not whether a plane field exists; it is how strongly it twists.

## Find the direction that contact planes do not determine

A contact form determines a unique vector field R called the Reeb field. It satisfies two equations. First alpha of R equals one. Second, inserting R into d alpha gives zero in every direction. These conditions pick the motion direction left over after the contact planes have been equipped with their nondegenerate two-form.

For our model alpha equals d z minus y d x, the z coordinate vector field is the Reeb field. The contact form evaluates it to one, and d alpha, which uses only d x and d y, evaluates it to zero against any other vector. Thus Reeb trajectories are lines moving straight in the z direction.

On all of three-space those lines do not close. If the z coordinate is instead periodic, they become closed loops. The example shows why local differential equations alone do not decide whether a Reeb trajectory is periodic. Global topology matters.

## Periods become integrals

Consider a Reeb trajectory that closes after time T, where Reeb time is normalized by alpha of R equals one. Integrating alpha along the trajectory gives the integral over time of alpha evaluated on R. That integrand is one, so the result is T. The action of a closed Reeb orbit, measured by the contact form, equals its period.

This relation provides an action scale for dynamics on contact manifolds. When we later build Hamiltonians near a cylindrical symplectic end, the slopes of those Hamiltonians interact with these Reeb periods. New periodic orbits can appear precisely when the radial Hamiltonian motion matches an appropriate Reeb period.

Rescaling the contact form can change the Reeb field and the periods. If we multiply alpha by a positive constant, the Reeb field scales by the reciprocal constant. For a nonconstant positive rescaling, the new Reeb field generally acquires a component inside the contact planes as well. The hyperplane distribution stays the same, but the parametrized dynamics need not.

## Contact geometry is not just lower-dimensional symplectic geometry

A contact structure does not possess a nondegenerate two-form on its whole odd-dimensional tangent space. Instead, d alpha is nondegenerate only on the contact hyperplanes. The Reeb direction is singled out by its complementary role. This is why a contact manifold naturally couples a plane distribution with a flow, whereas a symplectic manifold starts from a nondegenerate two-form on every tangent direction.

Contact geometry also carries local flexibility. Darboux's theorem for contact manifolds says contact structures have a standard local model, just as symplectic forms do. Yet the global Reeb dynamics can be highly constrained and can distinguish contact manifolds, contact forms, and their fillings.

A Reeb orbit is not the same thing as an arbitrary closed curve. It must solve the Reeb ordinary differential equation. In three dimensions, embedded contact homology builds algebraic generators from appropriate collections of Reeb orbits, with multiplicities and admissibility conditions. The index and holomorphic-curve counts belong to the later theory. Before encountering them, it matters to understand exactly where those orbit generators come from.

Our concrete contact form has shown every essential local ingredient: a twisting plane field, a nondegenerate area form on those planes, and a uniquely normalized transverse flow. The next question is how a contact manifold arises as the boundary of a symplectic domain and how the boundary can be stretched into a noncompact end.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(Y^{2n+1}\), \(\alpha\) is a contact form iff \(\alpha\wedge(d\alpha)^n\) is nowhere vanishing; \(\xi=\ker\alpha\), and \(d\alpha|_\xi\) is symplectic. The Reeb field satisfies \(\alpha(R_\alpha)=1\), \(\iota_{R_\alpha}d\alpha=0\). For \(\alpha=dz-y\,dx\) on \(\mathbb R^3\), \(d\alpha=dx\wedge dy\), \(\alpha\wedge d\alpha=dz\wedge dx\wedge dy\), and \(R_\alpha=\partial_z\). A Reeb orbit \(\gamma:[0,T]\to Y\) satisfies \(\dot\gamma=R_\alpha\), \(\gamma(0)=\gamma(T)\), hence \(\int_\gamma\alpha=T\). If \(\alpha'=c\alpha\), \(c>0\) constant, then \(R_{\alpha'}=R_\alpha/c\). A nonconstant factor does not generally give the same simple formula.

### Exercises with answers

1. Test \(\alpha=dz\) for contactness on \(\mathbb R^3\). **Answer:** not contact, since \(d\alpha=0\).
2. Find the Reeb field for \(dz-y\,dx\). **Answer:** \(\partial_z\).
3. What is the alpha-action of a closed Reeb orbit of period seven? **Answer:** seven.
4. Does multiplying a contact form by a positive function preserve its kernel? **Answer:** yes, though not generally its Reeb flow.

### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), contact models and Reeb fields.
- Michael Hutchings, [Lecture Notes on Embedded Contact Homology](https://arxiv.org/abs/1303.5789), Reeb orbits, actions and the ECH setting.
- [Contact geometry](https://en.wikipedia.org/wiki/Contact_geometry).
