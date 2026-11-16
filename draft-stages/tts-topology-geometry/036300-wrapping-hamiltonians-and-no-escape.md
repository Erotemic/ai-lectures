# 036300 — Wrapping Hamiltonians and No-Escape Estimates

**Track:** Topology and Geometry. **Background:** contact/Reeb dynamics, Liouville completions, Hamiltonian action and Floer energy. **Question:** how do periodic orbits appear at infinity, and what prevents Floer trajectories from disappearing there?

<!-- BEGIN SPOKEN LECTURE -->

# Wrapping Hamiltonians and No-Escape Estimates

Wrapped Floer homology deliberately uses Hamiltonian flows that travel far into a noncompact symplectic manifold. That is the whole point of wrapping. But to count trajectories reliably, we must also stop solutions of the Floer differential equation from escaping without control. The central idea is to choose Hamiltonians whose growth near infinity is simple enough that Reeb dynamics and a maximum principle govern what happens.

## Radial Hamiltonians see Reeb flow

Take the cylindrical end of a Liouville completion. It has a radial coordinate r, a contact form alpha on each boundary slice, and symplectic form equal to the exterior derivative of r alpha. Choose a Hamiltonian depending only on radius: H equals h of r.

Its derivative points in the radial direction. The Hamiltonian vector field must therefore point along the complementary Reeb direction. Let us check the sign rather than guessing. Our track defines the Hamiltonian vector field by inserting it into omega to obtain d H. On the cylindrical end, omega pairs the Reeb field with the outward radial direction to give minus one. Consequently, X H equals minus h prime of r times the Reeb field.

Some texts define the Hamiltonian vector field using the negative of d H and obtain the opposite Reeb orientation. Both conventions are valid when the definitions of action and Floer equations change consistently. We will keep the minus sign in this paragraph to match the earlier geometry lectures.

If a radial level is stationary under the Hamiltonian flow, its motion is a reparametrized Reeb trajectory. One-periodic Hamiltonian orbits on that level correspond to Reeb orbits whose period matches the absolute value of the slope h prime. For a slope that avoids the relevant Reeb periods, the cylindrical region has no such one-periodic Hamiltonian orbits.

## A circle example where the sign can be checked

Consider the cotangent bundle of the circle, with angle q taken modulo two pi and momentum p. Keep lambda equal to minus p d q and omega equal to d q wedge d p. On the positive-momentum end, r equals p and alpha is minus d q on the unit boundary. Its Reeb field is minus the q direction, whose closed orbits have period two pi.

Take H equal to a times p on that end, for a positive constant a. Hamilton's equations, in our convention, give q dot equals a and p dot equals zero. A trajectory closes after one unit of time only when a is an integer multiple of two pi. The cylindrical formula agrees: X H is minus a times the Reeb field, which is plus a times the q direction.

Choose a slope a that is not a multiple of two pi. Then this end has no new one-periodic Hamiltonian orbit. Increase the slope past successive multiples of two pi, and families of Reeb-related periodic trajectories appear in the unperturbed radial model. A small time-dependent perturbation is used where necessary to achieve nondegeneracy. This is how increasing Hamiltonians detect more winding classes.

## Action is a second filter

In an exact symplectic manifold, our convention for Hamiltonian action is minus the integral of lambda along the orbit, minus the time integral of H. For a radial one-periodic Hamiltonian orbit on the cylindrical end, lambda of X H equals minus r times h prime. Hence the action is r times h prime minus h, evaluated at the orbit's radius.

If h is exactly linear, with slope a and intercept b, this value is minus b. If h is convex in a transition region, the relationship between radius, slope and action can distinguish orbits arising at different levels. Action filtrations make infinite collections of generators manageable, but they do not by themselves prove all required compactness statements.

For Hamiltonian chords with Lagrangian endpoints, one also includes primitives of lambda on the exact Lagrangians and endpoint conventions. The basic radial relation still identifies wrapping chords near infinity with appropriately oriented Reeb chords. This is the geometric bridge from contact boundary dynamics to wrapped Lagrangian intersections.

## Why a maximum principle is needed

Consider a Floer cylinder solving the negative-gradient equation for Hamiltonian action. Even if its incoming and outgoing periodic orbits lie in a compact region, why must the entire connecting cylinder stay near them? In a noncompact target, there is no automatic answer. A sequence of solutions might travel arbitrarily far out before returning, preventing compactness of the moduli space.

On a cylindrical end, choose an almost-complex structure of contact type. In logarithmic radial coordinate s, the complex structure pairs the outward radial direction with the Reeb direction, and it respects the contact planes. For an unperturbed holomorphic curve, the logarithmic radius becomes a subharmonic function. Roughly, its Laplacian is a nonnegative measure of the curve's derivative in the contact planes. A nonconstant subharmonic function cannot have a strict interior maximum.

This is the analytic heart of a no-escape argument. With suitable radial Hamiltonians, cylindrical almost-complex structures and compatible asymptotic or Lagrangian boundary conditions, related maximum principles show that a Floer solution whose ends lie inside a certain radial level cannot push out past that level. The exact hypotheses differ between periodic-orbit Floer theory and wrapped Lagrangian Floer theory, and between Hamiltonians that are linear or more general at infinity. It would be incorrect to claim that every convex Hamiltonian and every almost-complex structure automatically gives such a bound.

## A local proof idea

For a holomorphic map into the symplectization, write the cylindrical coordinate as s and the map's contact-manifold component as v. The holomorphic equation relates the derivative of s in one domain direction to alpha of the derivative of v in the perpendicular direction. Differentiate once more and combine the identities. The resulting Laplacian of s is d alpha of a contact-plane derivative with its image under the compatible complex structure. Positivity of that pairing gives nonnegativity of the Laplacian.

The argument relies on the particular cylindrical geometry; it is not just a generic consequence of being symplectic. For Hamiltonian-perturbed equations, additional terms appear, so restrictions on the radial profile and the end structure matter. This is why serious treatments state a maximum principle as a lemma with hypotheses instead of a slogan.

## The two limiting procedures

Wrapped Floer theory uses a collection of Hamiltonians with increasingly large admissible slopes and continuation maps between the corresponding Floer complexes. At each stage, no-escape and compactness estimates keep the moduli problems under control. Then a directed limit captures information from arbitrarily large wrapping without asking us to count an uncontrolled infinite moduli space in one step.

The cotangent circle again gives the intuition. Larger slopes can see more loops with positive or negative winding. The resulting wrapped theory of a cotangent fiber has generators corresponding to all integer winding classes. Its relation to the based loop space is a global theorem requiring the appropriate Floer-theoretic hypotheses, not a mere consequence of counting slopes.

Contact geometry tells us which trajectories are available at the end. Radial Hamiltonians turn those trajectories into periodic or chord generators. Action and energy organize the counts. A maximum principle prevents loss of compactness by uncontrolled radial escape. These are the missing mechanics behind the phrase 'wrap the Lagrangian toward infinity.'

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

On \(([1,\infty)\times Y,\lambda=r\alpha)\), \(\omega=dr\wedge\alpha+r\,d\alpha\). Fix the track convention \(\iota_{X_H}\omega=dH\). For \(H=h(r)\), the Hamiltonian vector field is
\[
X_H=-h'(r)R_\alpha,
\]
because \(\iota_{R_\alpha}\omega=-dr\). A one-periodic orbit at fixed \(r\) follows (the inverse orientation of) a Reeb orbit with period \(|h'(r)|\). For exact action \(\mathcal A_H(x)=-\int_x\lambda-\int_0^1 H(x(t))dt\), such an orbit has \(\mathcal A_H=rh'(r)-h(r)\). For \(h(r)=ar+b\), this equals \(-b\).

On \(T^*S^1\), \(q\in\mathbb R/2\pi\mathbb Z\), \(\lambda=-p\,dq\), \(\omega=dq\wedge dp\); for \(p>1\), \(H=ap\), \(\dot q=a\), \(\dot p=0\), so one-periodicity occurs exactly at \(a\in2\pi\mathbb Z\). The end Reeb field at \(p=1\) is \(R_\alpha=-\partial_q\).

For cylindrical contact-type \(J\) with \(J\partial_s=R_\alpha\) and \(J|_\xi\) compatible with \(d\alpha|_\xi\), a \(J\)-holomorphic map \(u=(s,v)\) satisfies \(\Delta s=d\alpha(\pi_\xi v_\sigma,J\pi_\xi v_\sigma)\ge0\) in conformal coordinates \((\sigma,\tau)\). This is a model subharmonicity statement; Hamiltonian-perturbed maximum principles require additional assumptions on \(H,J\), and the relevant boundaries.

### Exercises with answers

1. Under \(\iota_{X_H}\omega=dH\), what is the vector field for \(H=h(r)\)? **Answer:** \(-h'(r)R_\alpha\).
2. When is \(H=ap\) on the positive cotangent-cylinder end one-periodic? **Answer:** when \(a\) is an integer multiple of \(2\pi\).
3. Compute the action of a radial orbit for \(h(r)=ar+b\). **Answer:** \(-b\) with the stated action convention.
4. Does noncompact exactness alone imply Floer compactness? **Answer:** no; radial and analytic control are also required.

### Sources and further reading

- Chris Wendl, [Lectures on Holomorphic Curves in Symplectic and Contact Geometry](https://arxiv.org/abs/1011.1690), cylindrical almost-complex structures and holomorphic curves.
- Mohammed Abouzaid, [On the Wrapped Fukaya Category and Based Loops](https://arxiv.org/abs/0907.5606), wrapped cotangent fibers and based loops.
- [Contact geometry](https://en.wikipedia.org/wiki/Contact_geometry); [Maximum principle](https://en.wikipedia.org/wiki/Maximum_principle).
