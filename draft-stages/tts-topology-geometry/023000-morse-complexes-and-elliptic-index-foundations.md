# Morse complexes and elliptic index foundations

<!-- BEGIN SPOKEN LECTURE -->

# Morse complexes and elliptic index foundations

## Morse Theory: Critical Points and Handle Decompositions

Imagine a smooth landscape and raise the water level from far below it. At first the land is dry. When the water reaches the bottom of a valley, a new pool appears. When it passes a saddle, two regions may join, or a tunnel may form. At a peak, a remaining boundary may close. The topology of the flooded region changes only at certain heights.

Morse theory turns that picture into a theorem about smooth manifolds. Choose a smooth real-valued function on the manifold and examine its critical points, the places where its first derivative vanishes. If these critical points are nondegenerate, their local behavior is completely controlled by a quadratic form. The number of negative directions in that form, called the Morse index, predicts the kind of topological change that occurs.

The theory is remarkable because a numerical function, which seems to throw away most of the geometry, can recover information about holes, cells, and homology.

### What nondegenerate means

At a critical point, the first derivative vanishes. The Hessian is the matrix of second derivatives in local coordinates. Nondegeneracy means that this matrix is invertible. Its numbers of positive and negative eigenvalues are independent of the coordinate system. The number of negative eigenvalues is the index.

A nondegenerate minimum has index zero. On a two-dimensional surface, a saddle has index one and a maximum has index two. In higher dimensions there are more possibilities: the index can be any integer from zero through the dimension of the manifold.

The Morse lemma states that near such a critical point there are local coordinates in which the function is exactly a constant minus a sum of squares in the negative directions plus a sum of squares in the positive directions. Not merely approximately quadratic: after a smooth change of coordinates, the higher-order terms disappear locally.

This normal form provides the model for what happens when we cross the corresponding critical value.

### Passing a critical value

For any real number a, consider the sublevel set consisting of points where the function is at most a. If we move a through an interval that contains no critical values, the sublevel set does not change its diffeomorphism type under the standard compactness hypotheses.

Cross one isolated nondegenerate critical point of index lambda. The new sublevel set is obtained from the old one by attaching a lambda-dimensional handle. At the level of homotopy type, it is like attaching a lambda-dimensional cell. A zero-handle creates a component. A one-handle can join components or create a tunnel. A top-dimensional handle can close off a cavity.

The word can matters. The effect of attaching a handle depends on where it is attached. A one-handle may connect two previously separate disks, reducing the number of connected components, or it may attach twice to the same component, increasing the number of independent cycles.

### Counting on a sphere and a torus

Take a round two-sphere and use ordinary height. There is one minimum at the south pole and one maximum at the north pole, with no saddles. As the threshold rises, a disk appears at the minimum and is eventually capped at the maximum. The alternating count of critical points is one plus one, giving Euler characteristic two.

Now picture an upright torus, a doughnut standing on its edge, with a generic height function. It has one minimum, two saddles, and one maximum. The first saddle creates a tunnel-like change, and the second changes how a boundary component connects. The alternating sum is one minus two plus one, giving zero, which is the Euler characteristic of the torus.

These examples motivate the Morse inequalities. If m sub k counts critical points of index k and b sub k is the kth Betti number over a field, then there must be at least b sub k critical points of index k. In particular, the counts of critical points constrain possible homology. Stronger alternating-sum inequalities contain additional information.

### From handles to a chain complex

There is a second step beyond counting critical points. Choose a Riemannian metric and follow negative gradient flow lines. Generically, after a Morse-Smale transversality condition, one can count flow lines connecting critical points of successive indices, with signs when orientations permit. These counts form a differential in a chain complex whose generators are the critical points.

The deep fact is that the differential squares to zero and the resulting homology agrees with ordinary homology. Critical points give the chain groups; flow trajectories tell us how the pieces attach. Betti numbers are what survive after the attachments and cancellations have been accounted for.

A simple warning illustrates the distinction. Two functions might have the same number of critical points in each index but different flow-line incidence data. Critical-point counts alone give bounds and Euler characteristics; the Morse differential is needed to recover the finer homology groups.

### The boundary of this method

A generic smooth function on a compact smooth manifold can be made Morse by a small perturbation. But not every smooth function is Morse. A whole circle of critical points, for example, violates the isolated nondegenerate condition. Morse-Bott theory addresses certain structured degeneracies, while more general singularities need other tools.

Morse theory gives a systematic bridge from calculus to topology. A local second-derivative test becomes a global handle decomposition. And once gradient trajectories are added, the same calculus produces a homology theory. That is a compelling example of differential equations, geometry, and algebra working together rather than merely borrowing terminology from each other.

## Morse Theory by Example: Critical Points Become a Chain Complex

Imagine exploring a landscape by measuring elevation. At the bottom of a valley you find a minimum. On a mountain pass you find a saddle. On the summit you find a maximum. These critical points are not only features of one particular height function. Under suitable nondegeneracy assumptions, the pattern of critical points constrains the topology of the underlying surface.

Morse theory makes that statement precise. It has two complementary sides. As we raise the elevation level, we watch how the region below it changes shape. And if we follow the downhill gradient flow, we can build a chain complex whose generators are critical points and whose differential counts special flow lines between them.

The second side is the direct ancestor of Floer homology. But the construction is easier to understand in two dimensions, where we can draw every critical-point type.

### A Hessian that counts descending directions

A critical point of a smooth function is a point where its first derivative vanishes. The Hessian measures the leading quadratic behavior near that point. For a function of two variables, a positive-definite Hessian indicates a nondegenerate minimum. A negative-definite Hessian indicates a nondegenerate maximum. A Hessian with one positive and one negative eigenvalue indicates a saddle.

The Morse index of a nondegenerate critical point is the number of negative eigenvalues of the Hessian, counted with multiplicity. It is zero for a minimum, one for a saddle on a surface, and two for a maximum on a surface.

Why does this number matter? Near a nondegenerate critical point, the Morse lemma gives coordinates in which the function is a constant minus the squares of its descending coordinates plus the squares of its ascending coordinates. The number of descending directions is therefore an intrinsic local feature of the critical point, independent of which smooth coordinates we use.

This is a bridge from calculus to topology. A quadratic approximation determines the dimension of the handle added when an elevation threshold passes through a critical point.

### Watch a sphere appear level by level

Take the ordinary height function on a round sphere. Near the south pole, the sublevel set begins as a small disk after we pass the minimum. As we raise the threshold, the region expands but remains a disk. When we pass the north-pole maximum, a two-dimensional cap is attached and the boundary closes. The completed space is a sphere.

The function has two critical points: a minimum of index zero and a maximum of index two. From the handle viewpoint we have attached one zero-handle and one two-handle, with no one-handles. The alternating count of critical points is one plus one, or two. This is the Euler characteristic of the sphere.

The Morse inequalities say more generally that the number of critical points of each index cannot be smaller than the corresponding Betti number, subject to the usual refined relations. The height function on a sphere reaches the lower bound in each degree.

### What changes on a torus?

Stand a doughnut-shaped torus upright and measure height. As we raise the water level, a component appears at a minimum. At the first saddle, a passage changes the shape of the flooded region. At a second saddle, another passage appears, creating the torus's two independent one-dimensional loop directions. At the maximum, the remaining boundary closes.

A generic vertical height function on a standard embedded torus has four nondegenerate critical points: one minimum, two saddles, and one maximum. Their Morse indices are zero, one, one, and two. The alternating critical-point count is one minus two plus one, which is zero, agreeing with the torus's Euler characteristic.

This does not mean that critical-point counts uniquely determine every homology group. To recover homology we also need to know how the handles attach, or equivalently how the corresponding Morse differential maps critical points of one index to critical points of the next lower index.

### The negative-gradient flow makes a differential

Choose a Riemannian metric so that the gradient of the function is defined. Then consider trajectories moving downhill according to the negative gradient. The function decreases along every nonconstant such trajectory because its derivative along the motion equals minus the squared norm of the gradient.

Some trajectories connect one critical point to another. Under Morse–Smale transversality, critical points whose Morse indices differ by one are connected by a finite collection of appropriate trajectories, up to time translation. Give each trajectory a sign after choosing coherent orientations, and count them. These signed counts give the coefficients of the Morse boundary operator.

The chain group in degree k is generated by critical points of Morse index k. The boundary of a generator is a signed combination of critical points of index k minus one. The central theorem is that the boundary applied twice gives zero.

Why should it? The boundary of a one-dimensional family of flow trajectories consists of broken trajectories: one path from index k to k minus one, followed by another from k minus one to k minus two. The oriented endpoints of a compact one-dimensional family cancel in pairs. This geometric cancellation becomes the algebraic identity that two consecutive Morse boundaries compose to zero.

The full proof needs compactness, transversality, and coherent orientation arguments. The slogan that 'the boundary of a boundary vanishes' is the correct organizing idea, but it is not a substitute for establishing those analytic facts.

### The circle as a signed-count example

Take the height function on a circle. There is one minimum of index zero and one maximum of index one. Exactly two downhill arcs connect the maximum to the minimum. When counted with compatible orientations, the two arcs have opposite signs. Their contributions cancel, so the Morse boundary from degree one to degree zero is zero.

The resulting homology has one integer generator in degree zero and one in degree one. That agrees with the ordinary homology of the circle.

If we work with coefficients modulo two, there are two connecting trajectories, and two is zero modulo two. The conclusion is the same, with less orientation bookkeeping. But using mod-two coefficients discards information about signs and integer torsion. It is a simplification, not a universal replacement for integral Morse theory.

### What survives beyond ordinary landscapes?

Now replace the finite-dimensional manifold by a space of paths, loops, or connections. Define a functional whose critical points represent special geometric objects: geodesics, Hamiltonian periodic orbits, or solutions of gauge equations. Try to count connecting gradient trajectories and build a chain complex.

This is the philosophy behind Floer homology and related theories. The infinite-dimensional setting creates new difficulties: compactness can fail through bubbling or escape, transversality can be hard, and orientations must be controlled. The basic algebraic target remains recognizable. Critical objects generate a complex; connecting trajectories define its boundary; the proof that the boundary squares to zero comes from the geometry of boundaries of moduli spaces.

Morse theory therefore offers more than a way to compute the Euler characteristic. It demonstrates an architecture for building topology from dynamics. Local critical-point data, global flow, compactness, and the chain-complex identity cooperate to produce homology. That architecture will be reused, with substantial extra analysis, in advanced symplectic and gauge theory.

## Weak Derivatives and Sobolev Estimates on Manifolds

Smooth functions are convenient for doing geometry, but they do not form a complete space under most of the estimates produced by differential equations. Imagine approximating a connection on a bundle by a sequence of smooth connections. Suppose their curvature energies remain bounded. The sequence need not approach a smooth connection in any naive pointwise sense. If we want to say what a limit means, we need a language for derivatives, convergence, and products that survives taking limits.

That language begins with weak derivatives and Sobolev spaces. They are not an alternative kind of calculus, restricted to pathological functions. They are the completion of ordinary calculus in the measurements that partial differential equations naturally control.

### Learning a derivative from integration

Consider a function on a line. For a smooth function, integration by parts lets us move a derivative from the function to a compactly supported test function, at the price of a minus sign. This equation still makes sense if the original function merely has a locally integrable value. We declare that it has a weak derivative if there exists another locally integrable function that satisfies the same integration-by-parts rule for every smooth test function.

Take the absolute value function. Its ordinary derivative fails to exist at zero. Its weak first derivative is minus one to the left and plus one to the right. The single troublesome point does not prevent the weak derivative from being an ordinary bounded function. But the weak derivative of a step function is different. It involves a concentrated Dirac distribution at the jump; a step function is not in the first Sobolev space based on square-integrable derivatives.

A first Sobolev space records functions whose values and first weak derivatives are both square integrable. Higher Sobolev spaces record more derivatives. It matters which integrability exponent we use, because the same derivative estimate has very different strength in different dimensions.

### Why averaging changes convergence

On a circle, imagine a smooth sine wave making more and more oscillations. Divide its amplitude by its frequency. The resulting functions approach zero uniformly, and hence in square-integrable norm. But their first derivatives still have an oscillation of fixed size. Consequently they do not approach zero in the first Sobolev norm.

This simple example separates boundedness from compactness. A sequence can be bounded in the first Sobolev norm without possessing a subsequence converging strongly in that same norm. On a compact manifold, however, the Rellich compactness theorem supplies a smaller target: a bounded first-Sobolev sequence has a subsequence that converges strongly in square-integrable norm. There are no escape-to-infinity problems because the manifold is compact, but arbitrarily rapid oscillations still prevent strong convergence at the original derivative level.

We also distinguish weak convergence from strong convergence. Weak convergence says that every continuous linear measurement of the sequence converges; strong convergence says the norm of the difference tends to zero. A bounded sequence in a Hilbert Sobolev space has a weakly convergent subsequence. Rellich often turns that weak convergence into strong convergence in a lower-order norm. Neither statement, by itself, upgrades the limit to a smooth function.

### Dimension determines which products make sense

Here is the estimate that will matter repeatedly in four-dimensional gauge theory. On a compact four-dimensional manifold, a function or section with one square-integrable derivative belongs to the fourth-power integrable space, with a bound controlled by its first Sobolev norm. The same holds componentwise in local trivializations of a vector bundle.

This gives a way to multiply two rough fields. If each is fourth-power integrable, their product is square integrable, by the Holder inequality. So the quadratic part of curvature, a wedge product of two connection perturbations, makes sense at the integrability level supplied by first Sobolev regularity. The linear part of curvature involves one derivative and is also square integrable.

But do not infer that a first-Sobolev section in four dimensions is continuous. It need not be. Continuity requires stronger conditions, such as one derivative in an integrability power strictly larger than four, or enough additional derivative regularity. This failure of automatic continuity is one reason gauge transformations and nonlinear equations need carefully selected function spaces.

### From a coordinate chart to a manifold

The definitions begin on Euclidean space, but a compact smooth manifold can be covered by finitely many coordinate charts. Choose a partition of unity, multiply by its cutoff functions, and measure derivatives in each chart. Different smooth coordinate systems give equivalent Sobolev norms. On a vector bundle, choose local frames and use a connection to define covariant derivatives. Different smooth choices again lead to equivalent norms on a compact manifold.

These equivalences are essential. They show that the Sobolev space is geometric even though we use coordinates to estimate its elements. The metric and connection influence the norm, but on a fixed compact manifold they do not change which sections belong to the space.

On noncompact spaces the story needs additional hypotheses. Uniform geometric control, support conditions, and weights can affect embedding and compactness. We must not transport every compact-manifold theorem to an arbitrary open manifold without checking those conditions.

### Why the distinction matters in gauge theory

A connection can be written locally as a fixed smooth reference connection plus a Lie-algebra-valued one-form. In four dimensions, if that perturbation has one square-integrable derivative, its curvature is square integrable. The estimate tells us the nonlinear expression is defined. It does not say a bounded sequence of such connections is compact before allowing gauge transformations, nor does it say that a limit solves the same nonlinear equation.

That is the road ahead. First establish useful function spaces. Then obtain elliptic estimates for equations in those spaces. Finally, understand the additional symmetry and concentration phenomena that obstruct ordinary compactness.

The crucial lesson is that a bound is informative only when we know which topology it controls. Square-integrable curvature energy, weak convergence of connections, strong convergence of lower derivatives, and smooth convergence away from singularities are different statements. The advanced theorems work because they keep those statements separate and prove the steps connecting them.

## Elliptic Regularity: From Weak Solutions to Smooth Fields

The Sobolev bounds just described let us define limits, but they did not make those limits smooth. Advanced geometry often begins with weak solutions because weak limits are available; it then ends by proving that those solutions were smooth after all. What closes that gap?

The answer is elliptic regularity. An elliptic differential operator cannot ignore oscillations in one spatial direction while controlling another. Its leading symbol is invertible at every nonzero frequency. That condition turns a differential equation into an estimate for all derivatives of the unknown, up to some finite-dimensional obstruction.

### A circle where we can see every frequency

Work first on a circle with angular coordinate theta. Let the operator be minus the second derivative. Suppose the forcing term is a sine wave with frequency ten. A solution is the same sine wave divided by one hundred. More generally, at frequency k, solving the equation divides the Fourier coefficient by k squared.

That is two derivatives of improvement. High-frequency oscillations become progressively smaller in the solution than they were in the forcing term. If the forcing term has square-integrable size, the nonconstant part of the solution has two square-integrable derivatives. If the forcing term is smoother, the solution becomes smoother still.

There is a catch: constants are killed by the second derivative. The equation has a solution on the circle only if the forcing term has average zero, and solutions are then determined only up to an additive constant. This is a tiny example of Fredholm theory. We do not need the operator to be invertible to control all the components perpendicular to its kernel.

### An estimate is not an inverse formula

On a compact closed manifold, an elliptic operator of order m gives an estimate of the following shape: the Sobolev norm of a section with s plus m derivatives is bounded by a constant times the Sobolev norm of the operator applied to that section with s derivatives, plus a lower-order norm of the section itself.

That extra lower-order term is not mere bookkeeping. It prevents us from claiming that a kernel element has to vanish. The constants on the circle are the simplest example. More complicated elliptic operators have finite-dimensional kernels corresponding to harmonic forms, spinors, or infinitesimal deformations.

To derive such an estimate, one freezes coefficients at a point, uses the inverse of the principal symbol for high frequencies, and then repairs the lower-order error. On a manifold, local constructions are patched with a partition of unity. A full proof requires pseudodifferential or carefully organized energy-estimate methods. The geometric insight is that nonzero frequencies are uniformly controlled, while zero modes and global topology survive as finite-dimensional data.

### Bootstrapping a nonlinear equation

Now suppose the equation is nonlinear. Write it schematically as an elliptic operator on a field equals a product of fields and their lower derivatives. We can start with a weak solution whose derivatives lie in a Sobolev space. Sobolev multiplication may place the right-hand side in a better integrability space. An elliptic estimate can then give the solution additional derivatives. Repeat, and under suitable smoothness and dimensional hypotheses the solution becomes smooth.

But the words 'under suitable hypotheses' carry serious weight. At a critical exponent, a quadratic term may not improve the integrability enough for a naive iteration. There may also be gauge redundancy, meaning the ungauged differential operator is not elliptic. In gauge theory one first imposes a slice or gauge condition and then proves the regularity statement for the resulting elliptic system.

A common mistake is to see the word elliptic in a theorem about one operator and silently transfer every regularity result to a nonlinear gauge-invariant equation. We have to identify the operator, its domain, the chosen gauge, the regularity of coefficients, and the source term.

### Hodge theory as a regularity machine

Recall the Laplacian on differential forms. It is elliptic. A harmonic form solves the equation with zero forcing. Initially we can interpret that equation weakly in a Sobolev space. Elliptic regularity says a weak harmonic form on a closed smooth manifold is in fact smooth.

That is one reason Hodge theory can compare analytic objects with classical de Rham cohomology. We need not assume that every object in a Hilbert-space kernel was smooth to begin with. The equation makes it smooth. This also justifies speaking of a finite-dimensional space of smooth harmonic representatives after defining a self-adjoint elliptic operator using functional analysis.

### Two kinds of compactness

We can now distinguish two steps in a standard existence argument. Functional analysis may produce a weakly convergent subsequence of approximate solutions. The equation and elliptic estimates may upgrade regularity of the limit. If the estimates are uniform on the whole family, compact Sobolev embeddings can yield strong convergence in a lower norm, and sometimes smooth convergence after bootstrapping.

But curvature concentrations in four dimensions can prevent uniform estimates in the needed gauges. Then elliptic regularity is still available on regions where curvature stays controlled, while small balls around concentration points require separate treatment. This is the beginning of the Uhlenbeck compactness story, not a failure of elliptic regularity itself.

The general method is worth remembering. First choose a complete space in which limits exist. Second obtain an elliptic equation or gauge-fixed system. Third prove an estimate that gains derivatives. Fourth establish whatever compactness is needed to pass from approximations to a solution. Advanced geometry becomes more comprehensible when these steps are explicit instead of being compressed into the single phrase 'standard elliptic theory.'

## Elliptic Index and the Atiyah-Singer Perspective

A differential equation may have no solution, one solution, or a whole space of solutions. If we change the coefficients slightly, the number of solutions can jump. Yet certain differences between dimensions remain stable. The index of an elliptic operator is one of the most important of these stable quantities.

Take an operator between two spaces of sections of vector bundles on a compact manifold. Its kernel consists of solutions to the homogeneous equation. Its cokernel measures which right-hand sides cannot be achieved. When the operator is elliptic and we use suitable function spaces, both dimensions are finite. The index is the dimension of the kernel minus the dimension of the cokernel.

Why subtract the dimensions rather than count solutions alone? Because a perturbation can create or destroy matching pairs of kernel and cokernel directions while preserving the difference. The index captures a robust feature that does not depend on every analytic detail.

### Ellipticity as a condition on high frequencies

A differential operator has a principal symbol, obtained from its highest-order derivatives by replacing differentiation with multiplication by a frequency vector. For a first-order operator, the principal symbol is linear in that frequency. Ellipticity means the symbol is invertible at every nonzero cotangent vector for an operator of equal-rank bundles, or an appropriate exactness condition for elliptic complexes.

This requirement prevents solutions from oscillating arbitrarily in invisible directions. It supplies estimates that make the operator Fredholm on suitable Sobolev spaces when the manifold is compact without boundary. Boundary-value problems need boundary conditions of the proper elliptic type; we will not silently include arbitrary boundaries.

The index is insensitive to continuous deformations through Fredholm operators. That stability suggests a topological formula because homotopy-invariant data can be built from the operator's principal symbol.

### The de Rham operator as a test case

We can see the principle without invoking the full Atiyah-Singer theorem. On a closed oriented Riemannian manifold, take the exterior derivative and its formal adjoint. Combine them into an operator that maps even-degree differential forms to odd-degree forms. This is the even-to-odd part of d plus d adjoint.

Hodge theory says the harmonic forms represent de Rham cohomology. The kernel of the even-to-odd operator consists of even-degree harmonic forms. Its cokernel corresponds to the odd-degree harmonic forms. Therefore its index is the alternating sum of Betti numbers: the Euler characteristic.

On the two-sphere, the zero-degree and top-degree cohomology groups are one-dimensional and the first cohomology vanishes. The index is two. On the torus, the Betti numbers are one, two, and one; the index is zero. These are the same Euler characteristics we obtained from Morse critical points, now computed as an analytic index.

The equality reveals a deeper connection. Morse theory uses critical points and gradient flow. Hodge theory uses harmonic solutions of an elliptic equation. Both recover the Euler characteristic. They arrive by very different routes, but topology forces the same invariant to appear.

### The Atiyah-Singer theorem

The general Atiyah-Singer index theorem states that the analytic index of an elliptic operator on a closed smooth manifold equals a topological index determined by the symbol class. The topological side is expressed through K-theory and characteristic classes, with appropriate orientations and pushforwards.

The statement is broader than an equation involving only the Euler characteristic. Different operators lead to different indices. The signature operator on an oriented manifold of dimension divisible by four has index equal to the signature of the intersection pairing. On a spin manifold, the index of the spin Dirac operator is expressed by the A-hat genus.

The particular characteristic class depends on the operator. Replacing every index formula by the same Todd class would be wrong. Complex, spin, and signature orientations each carry their own structures.

A useful analogy is a balance sheet. Analysis counts actual solutions and constraints. Topology computes a net balance without solving the equations individually. The theorem says those two balances agree because they are descriptions of the same Fredholm class.

### What index theory does not tell us

A zero index does not mean the kernel is zero. It can mean kernel and cokernel have equal positive dimensions. A nonzero index gives a lower bound on at least one of those dimensions and can obstruct invertibility, but it does not list the solutions.

Similarly, index stability requires that we remain inside a Fredholm family. If ellipticity fails, the manifold becomes noncompact without control, or boundary conditions change improperly, finite-dimensional kernel and cokernel need not survive.

Index theory is therefore a theorem about robust analytic structure, not a substitute for checking hypotheses. It ties together the derived and K-theoretic ideas of algebra, the characteristic classes of geometry, and the PDE estimates of analysis. This synthesis is why an index can be computed without ever solving the operator's differential equation explicitly.

## An Index Theorem We Can Calculate: The de Rham Operator and Euler Characteristic

The Atiyah–Singer index theorem says, in great generality, that an analytic number defined by solutions of an elliptic differential equation can equal a topological number defined by geometry and characteristic classes. Its general formula requires substantial background. But one important case can be understood using tools we already know: the exterior derivative, its adjoint, Hodge theory, and the Euler characteristic.

We can now construct an elliptic operator on differential forms and compute its index for the circle, sphere, and torus. The result is a small index theorem with a complete chain of ideas: differential equations produce harmonic forms, harmonic forms represent cohomology, and an alternating count of cohomology dimensions produces the Euler characteristic.

### Even-degree forms and odd-degree forms

On an n-dimensional manifold, differential forms have degrees from zero through n. A function is a zero-form, a one-form measures directions, and a top-degree form measures oriented volume. The exterior derivative moves one degree upward. Its adjoint, the codifferential, moves one degree downward.

Now add those two operations into a single operator: exterior derivative plus codifferential. It changes parity. Even-degree forms are sent to odd-degree forms, and odd-degree forms are sent to even-degree forms. Restrict the operator to the direction from even forms to odd forms.

This parity split is what allows a nontrivial Fredholm index. We are comparing the dimensions of special even and odd solutions, rather than merely the kernel of a positive self-adjoint operator with itself.

### Why the operator is elliptic

At high frequencies, exterior differentiation acts like wedging with the frequency covector. Its adjoint acts like contraction with the same covector, with a sign. Adding them gives an algebraic operation analogous to Clifford multiplication.

The key identity is that applying this leading symbol twice gives minus the squared length of the frequency times the identity. If the frequency is nonzero, that algebraic map is invertible. Thus the de Rham operator is elliptic.

On a compact manifold without boundary, elliptic theory tells us that its even-to-odd restriction is Fredholm between suitable Sobolev spaces. Its kernel and cokernel are finite-dimensional, so the index is a well-defined integer. The analytical assumptions matter: on an open manifold or a manifold with boundary, the analogous claim requires more work and suitable domains or boundary conditions.

### What is in the kernel?

Square the full de Rham operator. Because the exterior derivative applied twice is zero, and likewise the codifferential squared is zero, the square reduces to the Hodge Laplacian.

On a compact closed manifold, a form is killed by the Laplacian exactly when it is both closed and co-closed. Such forms are harmonic. If an even form is in the kernel of the parity-restricted de Rham operator, the energy identity shows it is harmonic. Conversely, a harmonic even form is plainly in the kernel.

Thus the kernel is the space of harmonic even-degree forms. The formal adjoint of the even-to-odd operator is the same full de Rham operator restricted in the opposite direction. Its kernel consists of harmonic odd-degree forms. The cokernel of a Fredholm operator is represented by the kernel of its adjoint.

Therefore the index is the total dimension of harmonic even forms minus the total dimension of harmonic odd forms.

### Hodge theory turns analysis into topology

Hodge's theorem gives one and only one harmonic representative for each real de Rham cohomology class on a compact oriented Riemannian manifold without boundary. So the dimension of harmonic k-forms equals the kth Betti number.

Substitute that equality into the analytic index. What remains is an alternating sum of Betti numbers: degree zero contributes positively, degree one negatively, degree two positively, and so on. That alternating sum is the Euler characteristic.

We have proved the index formula for the de Rham operator, assuming the Hodge theorem and elliptic Fredholm facts already established: its index equals the Euler characteristic of the manifold.

The operator was built using a Riemannian metric. The Euler characteristic does not depend on the metric. This explains one form of index stability. Change the metric smoothly and the space of individual harmonic forms changes, but their alternating dimension difference remains topological. In fact, Hodge theory tells us each Betti number separately is fixed.

### Three complete examples

First, the circle. Harmonic zero-forms are constants, giving one even solution. Harmonic one-forms are constant multiples of the angle one-form, giving one odd solution. The index is one minus one, or zero. The circle's Euler characteristic is zero.

Second, the two-sphere. Harmonic zero-forms are constants. Harmonic two-forms are multiples of the oriented area class. There are no nonzero harmonic one-forms because the sphere has no first real cohomology. The even kernel has dimension two and the odd adjoint kernel has dimension zero. The index is two. The sphere's Euler characteristic is two.

Third, the flat two-torus. Constants give one harmonic zero-form, the two independent coordinate one-forms give two harmonic one-forms, and the area form gives one harmonic two-form. The even count is two, and the odd count is two. The index is zero, matching the torus's Euler characteristic.

No one needed to solve a complicated partial differential equation in coordinates for these examples. The topology supplied the dimensions through Hodge theory. But the PDE framework is still essential to know that the analytic operator has the claimed kernel and cokernel.

### What this does not prove

The full Atiyah–Singer theorem applies to broad classes of elliptic operators, not just the de Rham operator. It relates their symbol classes to characteristic-class expressions. Other operators require additional structures: spinor bundles, complex structures, twisting bundles, or specialized boundary conditions. It would be wrong to conclude that every elliptic operator has index equal to the Euler characteristic.

In particular, the spin and spin-C Dirac operators used in gauge theory are different operators, though they share the same general Dirac-type algebraic pattern. Their indices may involve the A-hat genus, Chern characters, and other characteristic-class data. The de Rham example is a foundation, not a substitute for those later formulas.

The important conceptual achievement is already here. We began with a local differential expression on forms. Ellipticity made its global kernel and cokernel finite-dimensional. Hodge theory identified them with topological cohomology. Their alternating dimension difference became the Euler characteristic. This is the analytic-to-topological bridge that an index theorem is designed to cross.

## Morse–Bott Theory and Equivariant Localization

Morse theory studies the critical points of a smooth function on a manifold. When critical points are isolated and nondegenerate, each one contributes a handle to a decomposition of the manifold. The number and indices of those handles constrain the manifold's homology.

But geometry often contains symmetry, and symmetry can make critical points appear in families. Think of a landscape that is constant along a circular ridge. Every point on the ridge is critical in the direction along the ridge, yet the function may curve sharply across the ridge. The usual Morse condition fails because the Hessian has a zero direction, but the failure is controlled.

Morse–Bott theory handles precisely this situation. Instead of requiring isolated critical points, it permits critical submanifolds. The Hessian may vanish along the tangent directions to a critical submanifold, but it must be nondegenerate in directions normal to it. This lets us describe what happens when a level set crosses an entire critical manifold.

### A product example

Take the product of a sphere and a circle. Use the height function on the sphere, ignoring the circle coordinate. On the sphere alone, height has two critical points: the north and south poles. On the product, each pole is accompanied by every point of the circle. The critical sets are two circles.

Near the southern circle, the function increases in the two sphere directions; near the northern circle, it decreases. Along the circle itself the function stays constant. The Hessian's kernel is exactly the tangent direction to the critical circle. The normal Hessian is nondegenerate, so the function is Morse–Bott.

Crossing a critical value attaches the disk bundle of the negative normal directions, rather than one ordinary disk. The topology contributed by a critical manifold is therefore related to the topology of the manifold *and* the rank and orientation behavior of its negative normal bundle.

This is already enough to explain a familiar phenomenon. The Euler characteristic of a product of a sphere and a circle is zero because the circle's Euler characteristic is zero. The two critical circles do not each contribute one the way isolated critical points would. Their contributions are weighted by the Euler characteristic of the critical submanifolds.

### Symmetry leads to localization

Now consider a compact oriented manifold with a circle action. The points fixed by the entire circle action form a collection of submanifolds, perhaps isolated points. At first it seems impossible that integrating a differential form over the full manifold could be recovered from information on just those fixed sets. Equivariant localization shows that, after introducing a formal variable recording the circle symmetry and inverting suitable weights, such a formula exists.

The idea is to extend ordinary cohomology to equivariant cohomology, which remembers both the space and the group action. The normal directions to each fixed component carry weights under the circle action. Those weights appear in an equivariant Euler class. Dividing by that Euler class compensates for restricting from the full manifold to the fixed set.

The resulting localization formula says that an equivariant integral over the whole manifold is a sum of contributions from fixed components. Each contribution restricts the class to the component, divides by the Euler class of its normal bundle, and integrates over that component.

The denominator is essential. Ignoring it would make the formula wrong even for the sphere.

### A sphere calculation

Rotate the two-sphere around its vertical axis. Only the north and south poles remain fixed. At each pole, the tangent plane rotates with a nonzero weight, but the signs of the weights depend on the orientations used. If we integrate the equivariant Euler class of the tangent bundle, each fixed point contributes one: its numerator and denominator are the same equivariant Euler class of that tangent representation.

The sum is two, agreeing with the Euler characteristic of the sphere. We have computed a global topological number from two local contributions.

If instead we try to integrate the constant class one, the two contributions have opposite terms proportional to the inverse of the equivariant variable, and they cancel. That matches the fact that integrating a degree-zero class over a two-dimensional closed manifold gives zero in ordinary cohomological grading.

Both examples show why localization is not simply 'count the fixed points.' It is a weighted statement about cohomology degrees, orientations, and normal representations.

### From Morse–Bott to geometry with symmetry

The link between Morse–Bott theory and equivariant localization is not accidental. Both use the way a function or group action concentrates geometry into special loci. The critical manifold has normal directions whose Hessian determines how topology changes. A fixed component has normal directions whose group weights determine its localization contribution.

These are different theories with different hypotheses, so one should not substitute one theorem for the other. Yet both reveal global information by studying local behavior transverse to a distinguished submanifold.

Such methods are useful in symplectic geometry, representation theory, and characteristic-class calculations. A moment map for a Hamiltonian circle action can supply a Morse–Bott function. Its critical points often agree with the fixed points of the action, under suitable hypotheses. The resulting geometry connects the handle picture of Morse theory with the weighted fixed-point calculations of equivariant cohomology.

The conclusion is a useful shift in perspective. Symmetry may create degenerate critical points, but it can also make topology easier to compute. Instead of perturbing away every symmetric feature, we can keep the symmetry and learn to read the information stored in its critical sets and fixed points.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Morse Theory: Critical Points and Handle Decompositions

**Track:** Topology and Geometry. **Background:** smooth manifolds, tangent spaces, homology, Euler characteristic. **Central question:** how can the critical points of a smooth function reveal the topology of an entire manifold?

#### Mathematical companion (not spoken)

Let M be a smooth compact n-manifold and `f:M->R` a Morse function. A critical point p satisfies `df_p=0`; it is nondegenerate when its Hessian has no zero eigenvalues. Morse index `lambda(p)` is the number of negative eigenvalues. The Morse lemma gives local coordinates with
\[
f=f(p)-x_1^2-\cdots-x_\lambda^2+x_{\lambda+1}^2+\cdots+x_n^2.
\]
Under the usual isolated critical-value and compactness hypotheses, crossing one index-lambda critical point attaches a lambda-handle `D^lambda x D^{n-lambda}` and changes the sublevel-set homotopy type by a lambda-cell. With `m_k=# critical points of index k` and Betti numbers `b_k=dim H_k(M;F)`, weak Morse inequalities give `m_k >= b_k`, and
\[
\sum_k(-1)^k m_k=\chi(M)=\sum_k(-1)^k b_k.
\]
A Morse-Smale metric allows a chain differential defined by signed counts of negative gradient trajectories between critical points whose indices differ by one. Proving `d^2=0` uses compactification of one-dimensional moduli spaces of flow lines; the full argument requires transversality and orientation choices (or coefficients in `F_2`).

For height on `S^2`, critical indices are 0 and 2, giving Euler characteristic `1+1=2`. A generic vertical height on a standard torus has indices 0,1,1,2, giving `1-2+1=0`.

##### Exercises with answers

1. What is the Morse index of a nondegenerate local maximum of a three-manifold? **Answer:** three.
2. What does crossing an index-zero point attach? **Answer:** a zero-handle, creating a new component of the sublevel set.
3. Why do equal critical-point counts not necessarily determine full homology? **Answer:** attachment maps or the Morse differential may differ.
4. Calculate the alternating critical-point count for a torus height function with one minimum, two saddles, and one maximum. **Answer:** zero.

##### Reading and source notes

- [University of Toronto, Morse Theory notes](https://www.math.utoronto.ca/mgualt/Morse%20Theory/Notes12-13.pdf), handles and critical values.
- [Arun Debray, Morse Theory lecture notes](https://adebray.github.io/lecture_notes/m392c_Morse_notes.pdf), local model and handle attachment.
- [Milnor, Morse Theory](https://press.princeton.edu/books/paperback/9780691080086/morse-theory), classical treatment.

### Morse Theory by Example: Critical Points Become a Chain Complex

**Track:** Topology and Geometry. **Background:** derivatives, Hessians, gradient flow, chain complexes, homology. **Central question:** how can a smooth function's critical points describe the topology of the space on which it lives?

#### Mathematical companion (not spoken)

For a Morse function \(f:M\to\mathbf R\) (all critical points nondegenerate), the Morse index \(\lambda(p)\) is the number of negative eigenvalues of \(\operatorname{Hess}_p f\). By the Morse lemma, near \(p\) suitable coordinates give \(f=f(p)-\sum_{i=1}^{\lambda}x_i^2+\sum_{i=\lambda+1}^n x_i^2\). Passing a single index-\(\lambda\) critical value attaches a \(\lambda\)-handle under the standard handle-attachment hypotheses.

With a Morse–Smale gradient and coherent orientations, \(C_k^{\mathrm{Morse}}\) is freely generated over \(\mathbf Z\) by index-k critical points and \(\partial p=\sum_{\lambda(q)=k-1}n(p,q)q\), where \(n(p,q)\) counts signed unparameterized negative-gradient trajectories. Compactified one-dimensional moduli spaces provide \(\partial^2=0\). For closed M, Morse homology is naturally isomorphic to singular homology; the Euler characteristic is \(\chi(M)=\sum_k(-1)^k c_k\), where \(c_k\) counts index-k critical points. Morse inequalities give \(c_k\ge b_k\) over a chosen field.

For the sphere's height function, \((c_0,c_1,c_2)=(1,0,1)\); for the standard upright torus, \((1,2,1)\); for the circle, the two oriented downhill arcs between maximum and minimum cancel in the Morse differential, giving \(H_0\cong H_1\cong\mathbf Z\).

##### Exercises with answers

1. **Index.** What is the Morse index of \(f(x,y)=-x^2+y^2\) at zero? **Answer:** One.
2. **Sphere.** Compute the alternating critical-point count for the height function on \(S^2\). **Answer:** \(1+1=2\).
3. **Torus.** Compute \(c_0-c_1+c_2\) for \((1,2,1)\). **Answer:** Zero.
4. **Why a complex?** What geometric structure explains \(\partial^2=0\)? **Answer:** Oriented endpoints of compactified one-dimensional moduli spaces of trajectories, corresponding to pairs of broken trajectories, cancel.

##### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds, lectures 23–28](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- University of Toronto, [Morse Theory lecture notes](https://www.math.utoronto.ca/mgualt/Morse%20Theory/Notes12-13.pdf).
- Overviews: [Morse theory](https://en.wikipedia.org/wiki/Morse_theory), [Morse homology](https://en.wikipedia.org/wiki/Morse_homology).

### Weak Derivatives and Sobolev Estimates on Manifolds

**Track:** Topology and Geometry. **Background:** multivariable calculus, integration by parts, vector bundles, compactness. **Central question:** what kind of convergence and multiplication can we expect from fields whose derivatives are controlled only on average?

#### Mathematical companion (not spoken)

For an open set \(\Omega\subset\mathbb R^n\), \(u\in W^{k,p}(\Omega)\) iff all distributional derivatives \(\partial^\alpha u\) with \(|\alpha|\leq k\) belong to \(L^p\). For a weak first derivative \(v_i\),
\[\int_\Omega u\,\partial_i\varphi\,dx=-\int_\Omega v_i\varphi\,dx\qquad(\varphi\in C_c^\infty(\Omega)).\]
On \(S^1\), \(u_m(\theta)=\sin(m\theta)/m\) satisfies \(u_m\to0\) in \(L^2\), but \(\|u_m'\|_{L^2}=\sqrt{\pi}\), so it does not converge in \(H^1=W^{1,2}\).

For a closed smooth four-manifold \(X\), \(W^{1,2}(X)\hookrightarrow L^4(X)\) continuously, but not generally into \(C^0(X)\). Rellich gives \(W^{1,2}(X)\hookrightarrow L^2(X)\) compactly. For bundle-valued one-forms \(a,b\),
\[\|a\wedge b\|_{L^2}\leq C\|a\|_{L^4}\|b\|_{L^4}\leq C'\|a\|_{W^{1,2}}\|b\|_{W^{1,2}}.\]
With smooth reference connection \(A_0\), \(F_{A_0+a}=F_{A_0}+d_{A_0}a+a\wedge a\), using a consistent Lie-algebra bracket convention. This establishes \(F_{A_0+a}\in L^2\) when \(a\in W^{1,2}\), without asserting compactness of connection moduli.

##### Exercises with answers

1. **Weak derivative.** What is the first weak derivative of \(|x|\) on a bounded interval containing zero? **Answer:** \(\operatorname{sgn}(x)\) almost everywhere; its value at zero does not matter.
2. **Oscillation.** Why do \(\sin(m\theta)/m\) fail to converge to zero in \(H^1(S^1)\)? **Answer:** the derivative has constant nonzero \(L^2\) norm.
3. **Four-dimensional product.** Which exponents make \(a\wedge b\in L^2\) if \(a,b\in L^4\)? **Answer:** Holder with \(1/4+1/4=1/2\).
4. **Limit.** Does boundedness in \(H^1\) guarantee strongly convergent \(H^1\) subsequences? **Answer:** no; on compact manifolds it gives weak \(H^1\), and a strong \(L^2\) subsequence.

##### Sources and further reading

- Harvard Math 212b, [Elliptic Engineering: Sobolev spaces and elliptic estimates](https://people.math.harvard.edu/archive/212_spring01/lectures/ellipticity.pdf).
- Emmanuel Hebey, [Nonlinear Analysis on Manifolds: Sobolev Spaces and Inequalities](https://doi.org/10.1090/cln/005) (book; publisher access may apply).
- Overviews: [Sobolev space](https://en.wikipedia.org/wiki/Sobolev_space), [Rellich-Kondrachov theorem](https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem).

### Elliptic Regularity: From Weak Solutions to Smooth Fields

**Track:** Topology and Geometry. **Background:** weak derivatives, Sobolev spaces, principal symbols, Hodge Laplacian. **Central question:** why does an elliptic differential equation often improve a rough solution's regularity?

#### Mathematical companion (not spoken)

For \(L=-\partial_\theta^2\) on \(S^1\), write \(f=\sum_k f_ke^{ik\theta}\), \(u=\sum_k u_ke^{ik\theta}\). The equation \(Lu=f\) is solvable iff \(f_0=0\); then \(u_k=f_k/k^2\) for \(k\ne0\), while \(u_0\) is arbitrary. For \(s\in\mathbb R\), \(\|u-u_0\|_{H^{s+2}}\le C\|f\|_{H^s}\).

For a smooth elliptic differential operator \(P\) of order \(m\) on a closed manifold,
\[\|u\|_{H^{s+m}}\le C_s(\|Pu\|_{H^s}+\|u\|_{H^s}).\]
For suitable distributional solutions \(Pu=f\), this estimate plus localization and approximation yields \(f\in H^s\Rightarrow u\in H^{s+m}\) locally (and globally on a closed manifold), provided the coefficients are smooth. Elliptic regularity is distinct from invertibility: \(\ker P\) may be nonzero.

For the Hodge Laplacian \(\Delta=d\delta+\delta d\), \(\sigma_2(\Delta)(x,\xi)=|\xi|^2\operatorname{id}\) up to Fourier-sign convention. Weak harmonic forms therefore are smooth.

##### Exercises with answers

1. **Fourier solution.** Solve \(-u''=\sin(3\theta)\). **Answer:** \(u=\sin(3\theta)/9+C\).
2. **Compatibility.** Can \(-u''=1\) have a periodic solution? **Answer:** no; the right side has nonzero average.
3. **Kernel.** Does ellipticity force an operator to have trivial kernel? **Answer:** no; constants lie in the kernel of the circle Laplacian.
4. **Gauge.** Why can a gauge-invariant curvature equation fail to be elliptic before choosing a slice? **Answer:** variations along gauge orbits are redundant directions in the principal symbol of the naive linearization.

##### Sources and further reading

- Harvard Math 212b, [Elliptic Engineering](https://people.math.harvard.edu/archive/212_spring01/lectures/ellipticity.pdf), including estimates and interior regularity.
- MIT OpenCourseWare, [Geometry of Manifolds lecture notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- Overviews: [Elliptic partial differential equation](https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation), [Elliptic regularity](https://en.wikipedia.org/wiki/Elliptic_operator).

### Elliptic Index and the Atiyah-Singer Perspective

**Track:** Topology and Geometry. **Background:** Hodge theory, de Rham cohomology, elliptic operators, characteristic classes. **Central question:** why can the difference between dimensions of solution spaces be computed using topology?

#### Mathematical companion (not spoken)

For a Fredholm operator `D:H_1->H_2` between Hilbert spaces, `ind(D)=dim ker(D)-dim coker(D)`. On a closed smooth manifold, an elliptic differential operator between smooth vector bundles gives a Fredholm map between appropriate Sobolev spaces. Its index depends only on its elliptic symbol class under continuous homotopy. The Atiyah-Singer theorem equates this analytic index with a topological pushforward in K-theory.

For a closed oriented Riemannian manifold M, define `D_even=(d+d^*)|_{Omega^even}:Omega^even->Omega^odd`. It is elliptic. Its adjoint is the odd-to-even restriction. By Hodge theory,
\[
\operatorname{ind}(D_{even})=\sum_{k=0}^{\dim M}(-1)^k\dim H^k_{dR}(M)=\chi(M).
\]
For `S^2` the Betti numbers are `(1,0,1)` and index is 2. For `T^2` they are `(1,2,1)` and index is 0. The standard self-adjoint scalar Laplacian, viewed as an operator from a Sobolev space to a lower-order Sobolev space, has index zero; it is not the even-to-odd de Rham operator.

The index of a spin Dirac operator on a closed spin manifold is the A-hat genus, while the signature operator gives the signature on closed oriented manifolds of dimension divisible by four. These require distinct geometric hypotheses and symbol classes. Index zero does not imply invertibility.

##### Exercises with answers

1. An operator has a two-dimensional kernel and five-dimensional cokernel. What is its index? **Answer:** minus three.
2. What is the de Rham operator's index on a genus-g closed oriented surface? **Answer:** Euler characteristic `2-2g`.
3. Does an index-zero elliptic operator have to be invertible? **Answer:** no; both kernel and cokernel may be nonzero and equal-dimensional.
4. Why are boundary conditions relevant? **Answer:** ellipticity of the interior symbol alone does not guarantee a Fredholm boundary-value problem.

##### Reading and source notes

- [Atiyah and Singer, The Index of Elliptic Operators I](https://doi.org/10.2307/1970715), original theorem.
- [Berline, Getzler and Vergne, Heat Kernels and Dirac Operators](https://link.springer.com/book/10.1007/978-3-642-58088-8), analytic index methods.
- [University of Cologne, Introduction to the Atiyah-Singer Index Theorem](https://www.mi.uni-koeln.de/~bxliu/Lecture2025IndexTheory/IndexTheory2025UzK.pdf), background on elliptic operators and K-theory.

### An Index Theorem We Can Calculate: The de Rham Operator and Euler Characteristic

**Track:** Topology and Geometry. **Background:** Hodge star and codifferential, ellipticity, Fredholm index, de Rham cohomology. **Central question:** can we prove one analytic index equals one topological invariant without hiding all the steps?

#### Mathematical companion (not spoken)

Let \(M\) be compact, oriented, Riemannian and boundaryless. Let \(D=d+\delta:\Omega^*(M)\to\Omega^*(M)\). Since \(d^2=\delta^2=0\), \(D^2=\Delta\). Separate parity, \(D^+:\Omega^{\mathrm{even}}\to\Omega^{\mathrm{odd}}\), \(D^-:\Omega^{\mathrm{odd}}\to\Omega^{\mathrm{even}}\), with \((D^+)^*=D^-\).

The principal Clifford symbol (suppressing the harmless Fourier factor i) is \(c(\xi)=\varepsilon(\xi)-\iota_{\xi^\sharp}\). The identity \(c(\xi)^2=-|\xi|^2\operatorname{id}\) follows from the exterior algebra anticommutation relations, so \(D\) is elliptic. On a compact closed M, elliptic Fredholm theory applies. The Hodge energy identity gives \(\ker D^+=\mathcal H^{\mathrm{even}}\), \(\ker D^-=\mathcal H^{\mathrm{odd}}\). Hence
\[\operatorname{ind}D^+=\sum_{k\ \mathrm{even}}\dim\mathcal H^k-\sum_{k\ \mathrm{odd}}\dim\mathcal H^k=\sum_{k=0}^n(-1)^kb_k(M)=\chi(M).\]
For \(S^1\), \((b_0,b_1)=(1,1)\) and index zero; for \(S^2\), \((1,0,1)\) and index two; for \(T^2\), \((1,2,1)\) and index zero. This is the de Rham or Euler operator index formula, one special case in the general framework of Atiyah–Singer. The spin or spin-C Dirac operator has a different associated bundle and index formula; it is not identified with \(D\).

##### Exercises with answers

1. **Parity.** Does d preserve parity of form degree? **Answer:** No. It raises degree by one and exchanges even with odd.
2. **Square.** Why is \((d+\delta)^2=d\delta+\delta d\)? **Answer:** The terms \(d^2\) and \(\delta^2\) vanish.
3. **Sphere.** Compute the index of \(D^+\) on \(S^2\). **Answer:** \(1+1-0=2\).
4. **Scope.** Must the spin-C Dirac operator on an arbitrary four-manifold have index equal to \(\chi(M)\)? **Answer:** No. Its index is governed by different characteristic data.

##### Sources and further reading

- MIT OpenCourseWare, [18.965 Geometry of Manifolds, Fredholm notes](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/).
- University of Notre Dame, [Elliptic operators on compact manifolds](https://academicweb.nd.edu/~lnicolae/Pseudo.pdf).
- Overviews: [Atiyah–Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem), [Hodge theory](https://en.wikipedia.org/wiki/Hodge_theory).

### Morse–Bott Theory and Equivariant Localization

**Track:** Topology and Geometry. **Background:** Morse theory, homology, Lie group actions, characteristic classes. **Central question:** how can fixed points and critical manifolds reveal global topology?

#### Mathematical companion (not spoken)

A smooth `f:M -> R` is Morse–Bott if its critical set is a disjoint union of smooth submanifolds C and `ker Hess_p f = T_p C` for all `p in C`. The normal Hessian splits the normal bundle into positive and negative bundles; attachment across a critical value is modeled by the negative normal disk bundle, with caveats concerning completeness and compactness.

For `M=S^2 x S^1`, `f(p,theta)=height(p)`, the critical components are `C_N={N} x S^1` and `C_S={S} x S^1`. The normal indices are 2 and 0 respectively. Since `chi(S^1)=0`, their Euler-characteristic contributions vanish, compatible with `chi(M)=chi(S^2)chi(S^1)=0`.

For a torus T action on a compact oriented M and a suitable equivariant cohomology class `alpha`, the Atiyah–Bott/Berline–Vergne localization formula is, after localization at the nonzero weights,
\[
\int_M \alpha=\sum_{F\subset M^T}\int_F \frac{i_F^*\alpha}{e_T(N_F)}.
\]
For the standard circle rotation of `S^2`, the two isolated fixed components contribute 1 each to `int_{S^2} e_T(TS^2)=chi(S^2)=2`. For `alpha=1`, the formal contributions are `1/u` and `-1/u` in consistent orientation conventions, summing to zero.

##### Exercises with answers

1. Why is `height` on `S^2 x S^1` not Morse? **Answer:** its critical points occur in circles, and the Hessian vanishes along each tangent circle.
2. Why is it Morse–Bott? **Answer:** the Hessian is nondegenerate on the normal sphere directions, with kernel exactly tangent to each critical circle.
3. What appears in the denominator of the localization formula? **Answer:** the equivariant Euler class of the normal bundle to a fixed component.
4. What global number results from integrating the tangent Euler class of the two-sphere? **Answer:** 2, its Euler characteristic.

##### Reading and source notes

- [Bott, Nondegenerate Critical Manifolds](https://doi.org/10.2307/1970034), the Morse–Bott viewpoint.
- [Atiyah and Bott, The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1), localization and moment-map geometry.
- [Guillemin and Sternberg, Supersymmetry and Equivariant de Rham Theory](https://doi.org/10.1007/978-3-662-03992-7), equivariant cohomology and fixed-point formulas.
