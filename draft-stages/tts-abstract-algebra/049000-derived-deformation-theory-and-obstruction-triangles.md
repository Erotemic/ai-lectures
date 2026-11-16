# 049000 — Derived Deformation Theory: Obstructions Beyond the Tangent Space

**Track:** Abstract Algebra. **Background:** Ext, cotangent complexes, derived categories, first-order deformation theory. **Central question:** how can a deformation be possible to first order but impossible to second order?

<!-- BEGIN SPOKEN LECTURE -->

# A tangent direction that goes nowhere

Imagine drawing a tangent arrow on a surface at a point. On an ordinary smooth surface, a short curve can follow that arrow. But a space defined by equations can have tangent arrows that fail to extend to actual curves. At a crossing, a tangent space can be larger than either branch. In moduli problems, the mismatch is even richer: one might be able to change an object infinitesimally, but encounter a genuine obstruction when trying to continue the change.

The previous lecture described this phenomenon using Ext groups. Here we go inside that mechanism. The central distinction is between the *space that could hold an obstruction* and the *obstruction itself*. A nonzero second Ext group does not tell us that every attempted deformation fails. We must calculate a class and ask whether it vanishes.

Start with an elementary example. Consider the equation x squared equals zero. At the solution x equals zero, the linearization has zero derivative, so it places no restriction on an infinitesimal change. Over the dual numbers, with epsilon squared equal to zero, x equals epsilon solves the equation. But over a ring in which epsilon cubed, rather than epsilon squared, is zero, the same choice produces epsilon squared. That term is nonzero. We cannot fix it by adding a multiple of epsilon squared to x, because squaring x still produces epsilon squared at the first nonvanishing order.

This is a complete second-order obstruction in a one-equation example. It shows why a tangent direction need not arise from a genuine family. The obstruction is not a numerical error; it is a failure of an equation over a thicker infinitesimal ring.

## Organizing corrections by order

A deformation can be built order by order. At order one, solve the linearized equations. At order two, substitute the proposed solution back into the original nonlinear equations and collect the new error. If the error can be canceled by an order-two correction, move on. Otherwise the process stops. The correction problem repeats at higher orders.

For many deformation problems in characteristic zero, a differential graded Lie algebra, often shortened to a D G Lie algebra, organizes this calculation. It consists of graded vector spaces, a differential, and a bracket that remembers how two infinitesimal changes interact. A degree-one element is a candidate change. The Maurer–Cartan equation says that its differential plus half its self-bracket must vanish.

Why a bracket? A linear equation would only see independent first-order changes. The bracket records quadratic interaction. Two changes may each be allowed individually while their interaction creates a second-order error. That interaction is what our simple squared-variable example makes visible.

Consider an especially small model: one degree-one generator called e and one degree-two generator called f. Let the differential be zero, and let the bracket of e with itself be twice f. Take a candidate deformation equal to t times e. The Maurer–Cartan expression is t squared times f. It vanishes if t squared is zero, but not if t cubed is zero and t squared survives. The obstruction is the class represented by f. We have written the failure as a concrete calculation, not just named a cohomology group.

## Why triangles appear

In derived categories, a short exact sequence is expressed by a distinguished triangle. When a deformation problem is controlled by a complex, the tangent and obstruction data are not isolated spaces: they are successive cohomology groups of that complex. A map of deformation problems can therefore give a triangle of controlling complexes and a long exact sequence of tangent and obstruction groups.

Think of forgetting structure. We might deform a vector bundle together with a section, then forget the section and retain only the bundle. The relative deformation complex measures the extra conditions imposed by preserving the section. The long exact sequence compares infinitesimal automorphisms, tangent directions, and obstructions before and after forgetting.

The triangle does not mean that a derived category somehow solves every extension problem automatically. It means that the *relationship* between different extension problems is recorded without throwing away higher information. Under the relevant finiteness and perfectness assumptions, that information can be presented locally by a two-term complex and used to define virtual dimensions and virtual fundamental classes. Those are not ordinary counts of smooth parameters; they take the obstruction theory seriously.

## From calculation to geometry

The example x squared equals zero deserves a final interpretation. As a set of classical points over a field, it contains only zero. As a scheme, it still remembers the nilpotent direction. As a deformation problem, that direction is real at first order and obstructed at second order. Reducing the scheme to its underlying point would erase the entire calculation.

The lesson is not that every geometric space has hidden pathologies. It is that our mathematical description should keep exactly the information the question requires. Ordinary tangent spaces answer a linear question. Deformation complexes organize the nonlinear sequence of lifting questions. Derived objects preserve enough of the latter to compare moduli problems through maps, triangles, and cohomology.

When a proof says a moduli space is unobstructed, ask what makes the actual obstruction classes vanish. When it claims a virtual dimension, ask which complex provides it. And when a first-order solution looks convincing, check whether it survives one more power of the infinitesimal parameter.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Take `A_1=k[t]/(t^2)` and `A_2=k[t]/(t^3)` with `char(k) != 2`. For `F(x)=x^2`, `x=t` solves `F(x)=0` in `A_1`. Every lift with the same linear term in `A_2` has the form `x=t+a t^2`, so `F(x)=t^2 (mod t^3) != 0`: the lift is obstructed.

A simple dg Lie algebra model has `g^1=k e`, `g^2=k f`, `d=0`, `[e,e]=2f`, and `f` central. This satisfies graded antisymmetry (odd-degree self-brackets need not vanish) and Jacobi. For `alpha=t e`, the Maurer–Cartan equation is
\[
d\alpha+\tfrac12[\alpha,\alpha]=t^2 f=0.
\]
It holds over `A_1` but fails over `A_2`. In the standard characteristic-zero dg-Lie convention, `H^0(g)` measures infinitesimal automorphisms, `H^1(g)` the first-order tangent space and `H^2(g)` the obstruction *space*; an actual obstruction is a specific class in `H^2(g)`. The zero-bracket case illustrates unobstructed formal directions, subject to the precise deformation functor and convergence or algebraization questions.

For a distinguished triangle of complexes `A -> B -> C -> A[1]`, the cohomology sequence includes
\[
H^1(A)\to H^1(B)\to H^1(C)\xrightarrow{\delta} H^2(A)\to H^2(B).
\]
The connecting map `delta` provides a mechanism by which a deformation in `C` can fail to lift to `B`. Not every triangle is automatically a tangent-obstruction triangle: the complexes must actually control the relevant deformation problems.

### Exercises with answers

1. Over `k[t]/(t^4)`, can `x=t+a t^2+b t^3` solve `x^2=0`? **Answer:** no; its `t^2` coefficient is always one.
2. If an obstruction group is nonzero, must the deformation be obstructed? **Answer:** no; the particular obstruction class can vanish.
3. In the two-generator dg-Lie example, what is the obstruction class for `alpha=t e`? **Answer:** the coefficient `f` of `t^2`, representing a nonzero class in degree two.
4. Which map in a long exact sequence can obstruct lifting a tangent class? **Answer:** a connecting homomorphism from the relevant degree-one group to a degree-two group.

### Reading and source notes

- [The Stacks Project, Deformation Theory](https://stacks.math.columbia.edu/download/defos.pdf), deformation and obstruction calculations for algebraic objects.
- [The Stacks Project, Cotangent Complex](https://stacks.math.columbia.edu/tag/08P5), derived deformation data and comparison sequences.
- [Manetti, Lectures on Deformations of Complex Manifolds](https://arxiv.org/abs/math/0507286), differential graded Lie algebras and deformation functors.
