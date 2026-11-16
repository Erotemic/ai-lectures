# 009200 - Partitions of Unity and Global Integration

**Track:** Topology and Geometry. **Background:** charts, smooth functions, differential forms. **Question:** how can local computations be assembled into constructions on an entire manifold?

<!-- BEGIN SPOKEN LECTURE -->

# Partitions of Unity and Global Integration

A sphere cannot be covered by one ordinary smooth coordinate chart that behaves like a plane everywhere. Nevertheless, we can integrate a smooth area form over the entire sphere. We can define metrics and connections globally, even when we construct them one chart at a time. How can local formulas produce a single global mathematical object without requiring a global system of coordinates?

The device that makes this possible is a partition of unity. Its ingredients are smooth functions that act as carefully arranged weights. Each weight is supported in a local region where we can work in coordinates. The weights sum to one, so their local contributions combine without changing the quantity we mean to describe.

## A weight that vanishes smoothly

Begin on the real line. We want a smooth bump that is positive near zero and exactly zero outside a bounded interval. There is a difference between being zero and smoothly becoming zero. A triangular tent has corners; if we take derivatives, the corners cause trouble. A true smooth bump flattens out to all orders at its boundary.

One standard construction uses an exponential that decays faster than any power as we approach the endpoint of an interval. The formula matters less than the property it establishes: smooth functions need not be analytic. A nonzero smooth function can vanish identically outside a compact region. That gives us local weights we can extend by zero beyond the chart without introducing seams.

Imagine covering a circle by several overlapping arcs. On each arc choose a bump that becomes zero before reaching the edge of that arc. Arrange for the positive parts of these bumps to cover the whole circle. At each point add up their values, then divide each bump by that sum. The new weights still vanish outside their assigned arcs, but now add to exactly one at every point.

The sum in the denominator must be positive. That is why we arranged for at least one bump to be positive at every point. In a compact space we can often perform this with finitely many bumps. On a noncompact manifold we may need infinitely many. We then require a locally finite family: every point has a neighborhood meeting the supports of only finitely many weights. All the sums we use are locally finite smooth sums, not uncontrolled infinite series.

## What a partition actually promises

A smooth partition of unity subordinate to an open cover consists of nonnegative smooth functions, each supported inside an appropriate member of the cover, whose sum is one. The standard existence theorem assumes a smooth, Hausdorff, second-countable manifold, or more generally the appropriate paracompact conditions. That hypothesis is not decorative. Without enough topological control, a locally finite refinement need not exist.

These weights do not magically make incompatible local data agree. Suppose two coordinate patches both describe the same geometric one-form. On their overlap, the component expressions must transform correctly. Once we know they agree as forms, multiplying by partition weights and summing recovers that form. If the two local definitions genuinely conflict, their weighted average is a new object, not proof that they were the same object all along.

There are, however, geometric structures that can be assembled by averaging. In each chart, construct a positive-definite metric. A weighted sum of positive-definite metrics remains positive definite, provided at least one positive weight is present. Thus partitions of unity help show that every ordinary smooth manifold admits a Riemannian metric. This is one concrete reason the existence theorem is so powerful.

## How global integration is defined

Suppose M is an oriented smooth surface and omega is a smooth two-form with compact support. Choose oriented coordinate charts and a partition of unity subordinate to those charts. Multiply omega by each weight. Each weighted form can be integrated by ordinary calculus after translating it into the local coordinates. Then add those local integrals.

Because the weights sum to one, the result should represent the integral of omega over the whole surface. But why is it independent of the chosen cover? If we use another partition, we can refine both decompositions together. The double weights still sum to one, and ordinary change-of-variables in overlapping charts shows that the same geometric two-form receives the same oriented integral. Orientation is what makes the Jacobian signs match consistently across patches.

The compact-support assumption ensures that the contribution is finite and that we do not need a theory of improper integration at infinity. On a noncompact manifold, a non-compactly-supported form may also be integrable, but convergence requires additional work. A partition of unity does not by itself turn a divergent integral into a convergent one.

## A familiar area calculation in disguise

On a sphere of radius R, the usual latitude and longitude coordinates have an area element involving R squared times the cosine of latitude. Integrating longitude through a full turn and latitude from south to north gives four pi R squared. But longitude is undefined at the poles. How can this calculation be legitimate if there is no single smooth longitude chart on all of the sphere?

One answer is to exclude tiny polar caps, compute on the regular coordinate region, and show the cap contribution tends to zero. A second, more systematic answer is to use overlapping charts and a partition of unity. On each chart we integrate the appropriate weighted area form. The total agrees with the usual calculation. We are not pretending the coordinate singularity is a geometric singularity. We simply avoid giving one chart more responsibility than it can bear.

The same idea works for manifolds whose coordinate maps are far less explicit than a sphere's. Local integration is a definition, not just a convenient computational trick, because the partition-of-unity construction specifies how all local answers are combined.

## Boundaries and orientations

If a manifold has a boundary, charts near the boundary look like pieces of a half-space. The boundary inherits an orientation from the orientation of the interior, using the outward-normal-first convention. A partition of unity can be chosen compatible with such charts. Then the integral of a derivative over the manifold can be compared with the integral of the original form over its boundary.

That comparison will give the general Stokes theorem. The partitions ensure that local versions of the fundamental theorem of calculus can be summed into a global statement. Interior chart contributions cancel or vanish; boundary chart contributions survive, with signs fixed by orientation.

There is one further distinction worth retaining. On a nonorientable manifold, a globally consistent top-degree differential form cannot serve as a positive volume measure in the usual way. To integrate an unsigned density, one uses densities rather than oriented top-forms. A partition of unity still performs the local-to-global assembly, but it does not remove the need to choose the correct kind of object to integrate.

A partition of unity is therefore not a claim that a manifold secretly has one coordinate system. It is a way to respect the absence of one. We work in trustworthy local charts, weight the results smoothly, and combine them into objects and integrals whose definitions do not depend on the charts. This is a central bridge between local calculus and global geometry.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

For a locally finite open cover \(\{U_i\}\) of a paracompact smooth manifold, a subordinate smooth partition is \(\{\rho_i\}\) with
\[0\le\rho_i\le1,\qquad \operatorname{supp}\rho_i\subseteq U_i,\qquad \sum_i\rho_i=1,\]
where the support inclusion is achieved relative to a suitable locally finite refinement when necessary.

If \(\omega\in\Omega_c^n(M)\) on oriented \(M^n\),
\[\int_M\omega=\sum_i\int_{U_i}\rho_i\omega,\]
with each summand computed via an orientation-preserving chart and ordinary integration of its coefficient. If \(\{\sigma_j\}\) is another partition, insert \(1=\sum_j\sigma_j\) into each term to compare the definitions. For local positive-definite metrics \(g_i\), \(g=\sum_i\rho_i g_i\) is positive definite where the cover is locally finite.

### Check your understanding

1. Why must the covering family be locally finite? **Answer:** to ensure a point has only finitely many nonzero contributions nearby, so smooth sums are well defined.
2. Does a partition of unity repair contradictory local tensors on overlaps? **No:** it can average to create another tensor, but it does not make incompatible definitions identical.
3. What replaces an oriented volume form if the goal is unsigned integration on a nonorientable manifold? **Answer:** a density.

### Reading and sources

- MIT OCW, [Geometry of Manifolds](https://ocw.mit.edu/courses/18-965-geometry-of-manifolds-fall-2004/pages/lecture-notes/), lecture on connections and partitions of unity.
- Overview: [Partition of unity](https://en.wikipedia.org/wiki/Partition_of_unity), [Integration on manifolds](https://en.wikipedia.org/wiki/Integration_on_manifolds).
