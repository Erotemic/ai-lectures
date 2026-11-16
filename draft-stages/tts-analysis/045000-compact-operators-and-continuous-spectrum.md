# 045000 — Compact Operators and Continuous Spectrum: Two Ways Infinity Enters

**Track:** Analysis from First Principles. **Background:** Eigenvectors, spectral values, compactness, and Hilbert spaces. **Question:** When does the matrix eigenvector picture survive, and when does it fail?

<!-- BEGIN SPOKEN LECTURE -->

# Compact Operators and Continuous Spectrum: Two Ways Infinity Enters

There are two very different ways an infinite-dimensional operator can fail to behave like a finite matrix. It can have infinitely many eigenvectors with eigenvalues accumulating toward zero. Or it can have spectral values without a single nonzero eigenvector. Functional calculus must handle both.

The first situation is close to diagonalization. The second forces us to replace lists of eigenvectors by measures and spectral projections. Understanding the difference makes the general spectral theorem less mysterious.

## What compact means for an operator

In a finite-dimensional space, a bounded set has compact closure. In an infinite-dimensional Hilbert space, a bounded set can spread in infinitely many independent directions and have no convergent subsequence.

An operator T is called compact if it sends every bounded sequence to a sequence with a convergent subsequence. In particular, the image of the unit ball has compact closure. A compact operator cannot transport infinitely many orthogonal unit directions to outputs whose sizes all stay bounded away from zero; that would create a sequence of well-separated outputs with no convergent subsequence.

Finite-rank operators are compact. They send every vector into a fixed finite-dimensional space, where the ordinary finite-dimensional compactness principle applies. Norm limits of finite-rank operators are compact as well.

An example of a compact infinite-dimensional operator is diagonal multiplication on square-summable sequences by one, one half, one third, one fourth, and so on. Each coordinate is attenuated, with higher coordinates attenuated more strongly. Truncating after the first N coordinates gives a finite-rank operator, and the error in operator norm is one divided by N plus one. That error tends to zero, proving compactness.

## The compact self-adjoint spectral theorem

The diagonal example has a complete orthonormal collection of eigenvectors, one for each coordinate. The associated eigenvalues approach zero. Zero belongs to the spectrum because the inverse would need to multiply the N-th coordinate by N, which is not bounded. Yet zero is not an eigenvalue: no nonzero sequence is annihilated by the diagonal operator.

This teaches us to distinguish a spectral limit point from an eigenvalue. A compact self-adjoint operator on a Hilbert space has a particularly useful spectral theorem: its nonzero spectrum consists of eigenvalues of finite multiplicity, with no possible accumulation point other than zero. Its nonzero eigenspaces are mutually perpendicular, and together with the kernel they span the Hilbert space.

Such an operator therefore behaves like an infinite diagonal matrix, at least after choosing the right orthonormal coordinates. We can apply scalar functions by modifying the diagonal multipliers, taking care of the limit at zero.

Notice why the word compact is doing essential work. The theorem does not say that every bounded self-adjoint operator has an eigenbasis. The next example disproves that claim.

## Multiplication on an interval

Let A act on square-integrable functions between zero and one by multiplying a function at position t by t. A is bounded, self-adjoint, and positive. It has no eigenvectors, because an eigenfunction would have to live on one point of the interval, a set of measure zero.

It is also not compact. To see why, choose infinitely many disjoint small intervals within the half of the domain between one half and one. Put a normalized indicator function on each interval. These input functions have unit norm and are mutually perpendicular. After multiplying by t, their supports remain disjoint and their output norms remain at least one half. No subsequence of the outputs can converge, because every pair is separated by a definite distance.

Here the spectrum is the entire interval from zero to one. It is not a collection of isolated eigenvalues converging to zero. It is a continuous range of approximate eigenvalues, even though the operator has no actual eigenvectors.

## Why both examples are important

One might respond by saying that continuous spectrum is just a defect of our notation. Could we choose a different kind of basis? The useful answer is yes, but not by pretending that point masses are ordinary L-two eigenvectors. We can instead describe the operator as multiplication by a measurable function, sometimes after a unitary change of representation. In that description, scalar functional calculus is simply multiplication by a scalar function composed with that measurable multiplier.

The compact diagonal example is multiplication by a function on a discrete measure space. The interval example is multiplication by a function on a continuous measure space. The same general principle handles both: each spectral region carries some component of the vector, and a scalar function changes the multiplier on that region.

This is the conceptual content of the spectral theorem for bounded self-adjoint operators. The theorem can be presented as a multiplication-operator representation or as a projection-valued measure. The two formulations encode the same spectral action in different languages.

## The distinction from ordinary approximation

Compactness is not merely a statement that an operator can be computed accurately on every fixed input. Recall projections that keep the first N coordinates of a sequence. These projections converge strongly to the identity, meaning they approximate every fixed vector. But they do not converge to the identity in operator norm, because a unit vector can always sit entirely in a coordinate beyond N.

The identity operator on an infinite-dimensional Hilbert space is not compact. Its unit-ball image is still the whole unit ball. Thus a sequence of compact operators can converge strongly to a noncompact operator; compactness is preserved by operator-norm limits, not by arbitrary strong limits.

These distinctions between norm convergence, strong convergence, and spectral structure appear again in functional calculus. Uniform approximation of scalar functions will produce operator-norm approximation. More general measurable approximations often produce only strong convergence. We should not confuse the two.

## The lesson about infinity

Finite-dimensional spectral theory asks for eigenvalues and eigenvectors. Infinite-dimensional spectral theory asks a broader question: how is a vector's squared magnitude distributed across spectral values, and what happens when we multiply that distribution by a scalar function?

Compact self-adjoint operators supply the reassuring case where an orthonormal eigenbasis still works. Multiplication on an interval supplies the reason a full spectral calculus is necessary. A satisfactory theory must embrace both without changing its basic rules.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (not spoken)

A bounded operator \(K:H\to H\) is compact if it maps the unit ball to a relatively compact set. For \(D:\ell^2\to\ell^2\), \((Dx)_n=x_n/n\), let \(D_N\) retain only the first \(N\) weighted coordinates. Then \(D_N\) has finite rank and \(\|D-D_N\|=1/(N+1)\to0\). Its spectrum is \(\{1/n:n\in\mathbb N\}\cup\{0\}\), while \(\ker D=0\).

For a compact self-adjoint \(K\), the nonzero spectral points are real eigenvalues of finite multiplicity and can accumulate only at zero. There is an orthonormal basis of eigenvectors after including a basis of \(\ker K\). This does not imply zero must be an eigenvalue.

For \(M_t\) on \(L^2[0,1]\), select disjoint measurable positive-measure subsets \(I_n\subset[1/2,1]\) and \(e_n=\mathbf1_{I_n}/\sqrt{|I_n|}\). Then \(\|M_te_n\|\ge1/2\) and the outputs are orthogonal, so no subsequence converges. Thus \(M_t\) is not compact.

### Exercises with answers

1. **Compact diagonal.** Is \(\operatorname{diag}(1,1/2,1/3,\ldots)\) invertible as a bounded operator on \(\ell^2\)? **Answer:** No; its coordinatewise inverse would be unbounded and zero belongs to its spectrum.
2. **Zero eigenvalue.** Does zero belong to the point spectrum of that diagonal operator? **Answer:** No; the kernel is trivial.
3. **Identity.** Why is the identity not compact on an infinite-dimensional Hilbert space? **Answer:** An orthonormal sequence lies in its unit-ball image and has no convergent subsequence.
4. **Strong approximation.** Does strong convergence of finite-rank projections to I imply I is compact? **Answer:** No; compactness is closed under operator-norm limits, not arbitrary strong limits.

### Reading and source notes

- [MIT OpenCourseWare, Introduction to Functional Analysis, Lectures 20–22 on compact operators and spectral theory](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/).
- [Sheldon Axler, Measure, Integration & Real Analysis](https://measure.axler.net/).
