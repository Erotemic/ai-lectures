# 020700 — Moment-Map Measures: From Symplectic Area to Duistermaat–Heckman

**Track:** Topology and Geometry. **Background:** Hamiltonian circle actions, equivariant forms, elementary probability densities. **Central question:** how can the distribution of a conserved quantity be computed by geometry and fixed points?

<!-- BEGIN SPOKEN LECTURE -->

# Moment-Map Measures: From Symplectic Area to Duistermaat–Heckman

Suppose we place points uniformly at random on the surface of a round sphere. What is the distribution of their heights? Most people first imagine that the sphere has more surface near the equator, because those latitude circles are longer. So perhaps heights near the equator should be more likely.

That conclusion misses the width of a thin band. Near the equator, a change in height corresponds to a shorter meridional distance. Near a pole, the same change in height sweeps a longer meridional distance. These effects cancel exactly. Uniform area on a sphere gives a uniform distribution of height.

This elementary fact is an instance of the geometry behind the Duistermaat–Heckman theorem. We will prove it directly, then recover it again from equivariant localization.

## Normalize the sphere

Give the sphere total symplectic area one. Use polar angle theta measured from the north pole and azimuthal angle phi, with phi running once around from zero to two pi. The area form is sine theta divided by four pi, times d theta wedge d phi.

Let the circle parameter t run from zero to one and rotate phi by two pi t. The generating vector field is two pi times the derivative with respect to phi. Under the Hamiltonian convention used in this track, contracting the symplectic form with the generator equals the derivative of the moment map. One convenient moment map is one-half cosine theta.

Its value at north is plus one-half and at south minus one-half. Call that value m. When theta increases, m decreases. Differentiating gives minus one-half sine theta times d theta. Substitute this into the area form. The measure becomes d t times d m, with the correct orientation accounting for the reversed limits.

Integrating over the circular coordinate t contributes one. What remains is ordinary Lebesgue measure in m, on the interval from minus one-half to plus one-half. Thus the moment map pushes normalized area to uniform measure on that interval.

## A physical check with bands

Consider a thin band between heights m and m plus a small change delta m. Its area is approximately delta m, independent of m, as long as the band stays away from the endpoints. Its probability under uniform surface area is the same number. The direct coordinate derivation has now become an immediately testable geometric statement.

The endpoints are special: the latitude circle collapses to a fixed point at the north or south pole. At interior values, the circle action is free on each moment level. Symplectic reduction of the two-sphere at a regular moment value produces a zero-dimensional manifold, a single point. Its symplectic volume is one under the standard zero-dimensional convention. That is another reason the pushforward density is constant.

In higher dimensions, the reduced spaces can have positive dimension and their symplectic volumes vary with the moment value. The Duistermaat–Heckman theorem says that, under its Hamiltonian torus-action hypotheses, the resulting density is piecewise polynomial. The sphere is the degree-zero case.

## Derive the exponential integral

A useful way to package the entire height distribution is its moment-generating integral. Multiply the area form by the exponential of a parameter times the height and integrate over the sphere. With the normalized uniform distribution, this is simply the integral of the exponential from minus one-half to plus one-half. Elementary calculus gives the hyperbolic sine expression: two times sinh of half the parameter, divided by the parameter.

Now let the parameter be t times the equivariant variable u, but use a different spoken name for the circle coordinate to avoid confusion. The equivariantly closed form omega plus u mu can be exponentiated formally. Integrating its exponential after multiplying by an auxiliary parameter a produces two times sinh of a u over two, divided by u. For u approaching zero, the expression approaches a, the integral of a omega, exactly as expected from the first-degree term of the exponential.

## Recover the same expression at fixed points

At the north pole, the equivariant symplectic form restricts to plus u over two. At the south pole it restricts to minus u over two. Their tangent Euler classes are plus u and minus u.

Localization says the integral of the exponential of a times the equivariant symplectic form is the north exponential divided by u, minus the south exponential divided by u. This is the hyperbolic sine expression we obtained by ordinary integration.

The equality is stronger than the single identity that area equals one. As a formal power series in a and u, it equates all the moments of the height distribution with fixed-point information. Expanding the hyperbolic sine, we see that the mean height is zero, the second moment is one-twelfth, and higher even moments follow similarly. Odd moments vanish by symmetry.

The calculation is exact because the sphere is compact, the circle action is Hamiltonian, and our normalization was specified. Change the total area or the period of the generating circle, and the numerical coefficients change accordingly. The conceptual theorem does not change, but a careless mixture of conventions would make the fixed-point and coordinate calculations disagree.

## Why this matters beyond spheres

In symplectic reduction, the moment map assigns conserved quantities to points of a symplectic manifold. The pushforward of Liouville measure describes how much phase-space volume lies near each value. Duistermaat and Heckman's result connects this measure with reduced spaces and, through equivariant localization, with fixed-point geometry.

This is the foundational bridge between moment maps, equivariant cohomology, and localization. We began with an intuitive probability question, derived the answer using coordinates, reinterpreted it using reduced spaces, and finally recovered the full generating function using two fixed points. The abstract theory earns its place because all four descriptions agree.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

Use `φ∈[0,2π)`, `t=φ/(2π)`, `ω=(1/(4π))sinθ dθ∧dφ`, `X=2π∂_φ`, `μ=cosθ/2`; then `∫_{S²}ω=1`, `ι_Xω=dμ` and `μ_*(ω)` is Lebesgue measure on `[-1/2,1/2]`. For formal parameter a,

\[
\int_{S^2}e^{a(\omega+u\mu)}
=\frac{e^{au/2}-e^{-au/2}}{u}
=\frac{2\sinh(au/2)}{u}.
\]

On the left, the cohomological integral extracts only form degree 2. The same result comes from integrating `a e^{auμ} ω` over S², or from ABBV at the two fixed points. Expanding about `u=0` gives `a+a³u²/24+...`, so for the uniform variable μ, `E[μ]=0`, `E[μ²]=1/12`. Duistermaat–Heckman generalizes this to piecewise-polynomial densities under appropriate compactness/properness and torus-action assumptions.

### Exercises with answers

1. What is the total area of a moment-map band with m between 0 and 1/4? **Answer:** 1/4.
2. What is the expectation of μ under normalized area? **Answer:** zero.
3. What is the second moment of μ? **Answer:** `∫_{-1/2}^{1/2}m² dm=1/12`.
4. What is the symplectic quotient at a regular moment value for this sphere action? **Answer:** a point (zero-dimensional reduced space).

### Sources and further reading

- J. J. Duistermaat and G. J. Heckman, [On the Variation in the Cohomology of the Symplectic Form of the Reduced Phase Space](https://doi.org/10.1007/BF01399506), Inventiones Mathematicae 69 (1982), 259–268.
- M. Atiyah and R. Bott, [The Moment Map and Equivariant Cohomology](https://doi.org/10.1016/0040-9383(84)90021-1) (1984).
- [Duistermaat–Heckman formula](https://en.wikipedia.org/wiki/Duistermaat%E2%80%93Heckman_formula); [Moment map](https://en.wikipedia.org/wiki/Moment_map).
