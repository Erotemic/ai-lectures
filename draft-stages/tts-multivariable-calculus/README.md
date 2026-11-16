# Multivariable Calculus from First Principles — new core mathematics track

**Created:** 2026-11-16, Mathematics Continuation 31. **Status:** 18 complete, standalone narrations with non-spoken mathematical companions, exercises and answers, source records, and relevant Wikipedia links. Lecture length is governed by subject matter, not a time target.

## Why this exists

The existing Analysis course begins with one-variable calculus and proceeds directly into complex analysis, measure, functional analysis and PDEs. Topology/Geometry introduces manifolds and differential forms. The older repository lacked a dedicated, continuous bridge teaching multivariable limits, differentiability, integration and vector calculus at the appropriate introductory level. This new track fills that prerequisite rather than expanding advanced theory.

## Lecture sequence and advanced-course connections

| ID | Lecture | Core idea | Useful later |
| --- | --- | --- | --- |
| 001000 | Points, Vectors, and Nearness in Several Dimensions | Euclidean space, norms and open sets | metric foundations; Topology 001000 and Analysis 009000 |
| 002000 | Multivariable Limits: Why Paths Can Deceive | limits, continuity, path counterexamples | differentiability, Analysis 003000 |
| 003000 | Partial and Directional Derivatives: The Information They Miss | partial slopes versus the full derivative | Analysis 005000 and PDEs |
| 004000 | The Total Derivative: One Linear Map for Every Small Change | Fréchet derivative, Jacobian and tangent plane | smooth manifolds and numerical linearization |
| 005000 | The Multivariable Chain Rule: Composing Local Linear Maps | chain rule and Jacobian products | automatic differentiation, geometry charts |
| 006000 | Gradients, Level Sets, and Tangent Directions | gradients and metric dependence | optimization, gradient flow, Riemannian geometry |
| 007000 | Inverse and Implicit Functions: Solving Nearby Equations | invertible Jacobians and parameter sensitivities | Topology 008100; regular level sets |
| 008000 | Hessians and Taylor's Formula: The Shape Beyond the Tangent Plane | Hessians and quadratic Taylor models | optimization and stability |
| 009000 | Maxima, Minima, and Saddle Points in Several Variables | interior, boundary and global extrema | Optimization; variational problems |
| 010000 | Lagrange Multipliers: Optimization Along Constraints | regular constraints and sensitivity | constrained optimization and mechanics |
| 011000 | Double and Triple Integrals: Adding Values Across a Region | multi-dimensional Riemann sums | mass and probability densities |
| 012000 | Iterated Integrals: Slicing Regions and Exchanging the Order | Fubini/Tonelli and slicing | Analysis 034000; PDE integration |
| 013000 | Polar, Cylindrical, and Spherical Integrals: Coordinates Built for Shape | radial substitutions and singular coordinates | geometry; PDE symmetry reductions |
| 014000 | The Change-of-Variables Theorem: What the Jacobian Measures | Jacobian volume scaling and orientation | Topology 009000–010000 and integral geometry |
| 015000 | Curves and Line Integrals: Measuring Along a Path | arc length, work and potentials | differential forms and mechanics |
| 016000 | Green's Theorem: Circulation and Flux from Local Derivatives | Green, curl and planar divergence | Topology 010000; conservation laws |
| 017000 | Surface Integrals: Area, Normal Vectors, and Flux | parametrized surface area and oriented flux | Riemannian area and differential forms |
| 018000 | Stokes and Divergence: The Fundamental Theorem in Three Dimensions | Stokes, Gauss and generalized FTC | Topology 010000; continuum mechanics |

## Placement and reading order

Suggested prerequisites: Analysis 001000–008000 and the early Linear Algebra lectures through determinants and inner products. Take 001000–010000 for derivatives and optimization, 011000–014000 for multiple integrals and coordinate substitutions, and 015000–018000 for oriented curves, surfaces and boundary theorems. Advanced listeners can follow the dependency branches rather than the entire track.

For example, Topology/Geometry 008000–010200 becomes more accessible after 004000–007000 and 013000–018000 here. Differential Equations 010000–015000 uses multiple integrals, gradients and boundary-flux arguments. Numerical Analysis uses Jacobian linearizations and optimization Hessians.

## Authoring decisions

- Every spoken region is standalone, with concepts motivated and formulas explained in words. Exact equations and conditions appear in the non-spoken companion.
- False converses, missing hypotheses, singular coordinate sets and orientation signs are explicitly addressed rather than hidden.
- Source records include independent lecture materials (OpenStax and MIT) and relevant Wikipedia articles.
- No existing Analysis, Geometry, Differential Equations or Linear Algebra manuscript is modified.
