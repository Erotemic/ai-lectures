# 013000 — Sheaves: When Local Answers Become a Global Answer

**Track:** An Introduction to Category Theory. **Background:** sets, functions, open sets, contravariant functors, and compatible diagrams. **Theme:** why restriction, agreement, and unique gluing are distinct requirements.

<!-- BEGIN SPOKEN LECTURE -->

# Sheaves: When Local Answers Become a Global Answer

Suppose you have a large map divided into overlapping sheets. On each sheet a cartographer has marked the height of the terrain. The sheets overlap, and on every overlap the height measurements agree. Can we assemble them into a single height map of the entire region? If the data are continuous and the overlaps are compatible, the answer is yes. The value at a point can be taken from any sheet containing that point, and agreement ensures that the choice does not matter.

This small observation is the doorway to sheaf theory. A sheaf describes mathematical information that can be restricted to smaller regions and reconstructed from compatible local pieces. The idea begins with ordinary functions, but it eventually supports geometry, topology, algebra, logic, and the study of solutions to differential equations.

The central question is more demanding than 'can I store a value for each region?' It is: what exactly makes a family of local solutions count as one global solution? A sheaf answers that question with two mathematical guarantees, existence and uniqueness of gluing.

## Local data must first have somewhere to live

Let X be a space, such as a line, a circle, or a surface. We will talk about open subsets of X. Openness means, roughly, that every point of an open region has a small neighborhood still inside it. The precise topological definition matters later, but the immediate role is simple: open regions let us work locally and compare overlapping observations.

To every open region U, assign a set F of U, whose elements are the allowed pieces of data on that region. If our data are continuous real-valued functions, F of U is the set of all continuous functions from U to the real numbers.

Whenever V lies inside U, there is a restriction operation. It takes a function on U and forgets its values outside V, leaving a function on V. If we first restrict from U to V and then from V to W, that is the same as restricting directly from U to W. Restricting to the region we started with changes nothing.

This is the functorial part of the story. In the category whose objects are open subsets and whose arrows are inclusions, an inclusion points from a small region to a larger one. Restriction goes the opposite way: from functions on the larger region to functions on the smaller. Therefore the assignment is a contravariant functor, or equivalently a functor from the opposite category of open subsets to Set.

Such an assignment is called a presheaf. The word means we have coherent restriction maps. Nothing in that definition yet guarantees gluing. That missing guarantee will distinguish sheaves from arbitrary presheaves.

## Two weather stations and their overlap

Consider an interval from zero to three. Cover it with two overlapping open regions: one running a little past two, the other beginning a little before one. On the first region we have a continuous temperature function f. On the second region we have a continuous temperature function g.

To combine them, first check the overlap. Where both functions are defined, their values must agree. If one station reports eighteen degrees and the other twenty-three at the same place and time, no single exact function can restrict to both reports. The local data are incompatible. We would need a model of measurement uncertainty or reconciliation, which is a different mathematical problem.

But if the two continuous functions agree on their overlap, define a global function h by using f on the first region and g on the second. Because they agree where both are available, h is well defined. Because each piece is continuous and continuity can be checked locally, h is continuous.

Is h unique? Yes. Every point of the combined region belongs to at least one of the two pieces. A global function restricting to f and g must take the corresponding local value at every point. There is no room for a second different answer.

This example contains the entire sheaf condition. Given an open cover, local sections that agree on intersections must arise from exactly one section on the union.

Notice why both words matter. Existence says compatible pieces can be assembled. Uniqueness says they determine the assembled object completely. A presheaf can fail either condition, and different failures tell us different things about the information it stores.

## A calculation with real functions

Let's make the gluing concrete. Let the whole region be the open interval from negative two to two. Let the first open piece run from negative two to one, and the second from negative one to two. Their overlap is the interval from negative one to one.

On the first piece define the height as x squared. On the second piece also define the height as x squared. Their restrictions agree on the overlap, so the glued function is x squared throughout the union.

Now make the second formula x squared plus one. It is continuous on its own piece, but on the overlap it disagrees with the first formula by one everywhere. There is no global function whose restrictions are both of those exact local functions. The obstruction is neither subtle nor hidden: their demands contradict each other on points both pieces contain.

For a less trivial compatible example, suppose we define the first function as x squared and the second as x times x. The formulas look different but their values agree. A sheaf is concerned with the mathematical sections and their restrictions, not with preserving the exact syntax used to describe them. Compatible descriptions can glue even when written in distinct forms.

Software encounters the same gluing problem. Two computational regions may carry data through different representations or coordinate systems. To glue them, we need a specified notion of compatibility, often involving changes of coordinates. Merely checking that their file names or formulas match would be too restrictive, while ignoring the overlap would be too permissive.

## A presheaf that fails to glue

The easiest failure can be constructed from constant functions. Take a disconnected space consisting of two separate open pieces, call them left and right. Let F of any nonempty open region be the two-element set of choices red and blue. Restrictions between nonempty regions keep the same choice. On the empty region, give the presheaf exactly one section, as ordinary sheaf conventions require.

Locally, choose red on the left and blue on the right. The overlap is empty, so there is no point on which the two choices disagree. The data are compatible. Yet a global section of this presheaf must be either red everywhere or blue everywhere. Neither global choice restricts to red on the left and blue on the right. Gluing fails.

This is the *constant presheaf* of two labels, and on a disconnected space it is not a sheaf. It becomes easy to confuse it with the constant sheaf, but those are different constructions.

The constant sheaf associated with a discrete set of labels consists of locally constant functions. On a disconnected space a locally constant function may take red on one component and blue on another. That is exactly the glued section our example needs. Making the presheaf into a sheaf requires admitting those locally assembled assignments.

This example shows that local-to-global reasoning is about permitted global objects, not only about compatible data. You can choose a perfectly sensible restriction rule that is too rigid to represent the local configurations that should assemble.

## Uniqueness can fail separately

Imagine a data system that attaches a hidden global label to a section but discards that label whenever you restrict to a proper open subset. Different global sections could have identical restrictions on every member of a cover. Even if local pieces glue, they would not determine *which* global section we started with. Uniqueness would fail.

In the language of sheaf theory, the uniqueness condition is sometimes called separatedness. The existence condition is the other half of the sheaf axiom. Together they ensure that a section is determined by what it does locally and that every compatible local family has a global representative.

This distinction is useful because many mathematical problems concern extension. You might know local solutions and ask whether any global solution exists. Other problems concern identification. You might have two global solutions and ask whether agreement on a cover forces them to be equal. Keeping these questions separate makes failures diagnosable.

In everyday language, a pile of fragments is not automatically a complete object. For a genuine reconstruction we need rules for comparing fragments, a theorem asserting the existence of an assembly, and assurance that the assembly is the one dictated by those fragments.

## Why intersections are more informative than isolated charts

Imagine a survey team measuring elevations in three overlapping districts. If each district reports a perfectly smooth map but the maps disagree along their common boundaries, local smoothness cannot save the global reconstruction. Pairwise overlap agreement is the indispensable test. For three districts, the agreement must hold for every pair on its intersection. On a triple overlap, the pairwise agreements then force all three local values to coincide there.

One might try to avoid overlaps altogether by dividing the region into nonoverlapping cells. But boundaries create their own problem. A discontinuity can hide at a boundary unless the cells are related through an appropriate matching rule, and open covers are especially convenient because continuity is local on open neighborhoods. The topology determines which neighborhoods we can use and how covers are allowed to combine.

In practice a coordinate chart on a manifold might describe a point by one pair of numbers, while another chart uses a different pair. The charts need not report identical coordinates. They need to be related by specified transition functions on overlaps. The sheaf of scalar-valued functions then glues because the functions represent the same underlying values after the coordinate changes are taken into account. This separates the geometric object from the notation used in each patch.

A sheaf makes a promise about mathematical sections, not about raw strings or files. Before applying its gluing condition to software data, we need to specify what counts as equality on an overlap. Otherwise a system can falsely reject compatible representations or falsely accept incompatible physical values.

## The sheaf condition as a diagram

We can express the condition using a diagram of sets. Suppose U is covered by open regions U one, U two, and so forth. Restrict a global section on U to every piece. We obtain a family of sections, one for each member of the cover. Restrict each pair further to their intersection. Those two ways of reaching the overlap must give the same result.

A sheaf says that global sections correspond exactly to these compatible families. More formally, the set of sections over U is an equalizer of two maps: one map compares all local pieces to overlaps by restricting from the first index, and the other uses the second index. Their equality encodes pairwise agreement.

The word equalizer may sound abstract, but we have already used the idea. An equalizer collects the inputs on which two maps agree. Here the inputs are tuples of local sections, and the two maps list their values when restricted to every overlap. Compatible tuples are precisely those lying in the equalizer. The sheaf condition says the restriction map from global sections to that equalizer is a bijection.

This formulation explains why sheaves fit so naturally into category theory. The condition is a universal characterization of global data using a diagram of local data and their restrictions. It can be generalized to more elaborate sites where 'cover' means something other than an ordinary open cover of a topological space.

## What is a stalk?

Suppose we care about data near one particular point x rather than on an entire region. Two sections defined on different neighborhoods of x may represent the same *germ* if they agree on some smaller neighborhood of x. A germ forgets details far away and remembers only what a section does sufficiently close to the point.

Collect all such germs at x. The resulting set is called a stalk. You can think of it as a microscope: it examines all available local descriptions near x and identifies descriptions that become equal when we zoom in enough.

For continuous real-valued functions, a stalk contains much more information than the function's single value at x. Two continuous functions can take the same value at x and differ arbitrarily close to x. They then determine different germs, even though a single point measurement could not distinguish them.

Stalks are powerful because many claims about maps between sheaves can be tested locally. For sheaves of sets on a topological space, a morphism is an isomorphism if and only if it induces bijections on all stalks. The phrase 'on a topological space' is important; general sites may require a different account of points.

A stalk therefore supplies another bridge between global categorical constructions and the local behavior of actual functions. It tells us which information remains when we examine smaller and smaller neighborhoods, while the sheaf condition tells us when neighborhoods can be assembled back into a global section.

## A global obstacle: locally easy does not mean globally possible

We must distinguish the sheaf property from the claim that every locally solvable problem has a global solution. These are different assertions. A sheaf glues local sections that are *compatible on overlaps*. It does not promise that arbitrary local solutions can be adjusted into a compatible family.

Consider trying to choose a continuous angle for every point on a circle in a way that increases continuously as we go once around and returns to its starting value. On each short arc we can choose a sensible angle coordinate. But along a full circuit the angle increases by one complete turn. A single globally continuous real-valued angle whose exponential reproduces every point of the circle cannot exist.

The local angle descriptions can disagree by whole turns on overlaps. Some can be adjusted locally, but there remains a global obstruction to choosing one compatible real-valued lift on the entire circle. This is a classic reason local data can be abundant while globally consistent sections are constrained.

The correct takeaway is that a sheaf provides the *rules* for gluing. Geometry and topology still determine whether the necessary compatible pieces exist for the problem under study. This distinction is the beginning of cohomological thinking, where obstructions to gluing can themselves be studied mathematically.

## Continuity makes a good first sheaf

Return to the sheaf of continuous real-valued functions. Restriction clearly sends continuous functions to continuous functions. If a family of continuous functions agrees on pairwise overlaps of an open cover, it determines one well-defined function on the union. Since every point has a neighborhood on which the glued function is one of the original continuous functions, the global function is continuous. And uniqueness is immediate because the cover contains every point.

The proof is simple, but its structure is general. The data are assigned to regions; restriction respects inclusions; compatible local assignments determine a unique global assignment. Whenever a new mathematical situation has those properties, we can look for a sheaf or a sheaf-like framework.

Smooth functions form a sheaf on a smooth manifold. Solutions of certain local equations may form a sheaf, although a particular global solution may not exist. Holomorphic functions on a complex manifold also form a sheaf. In algebraic geometry, sheaves allow rings and modules to be studied locally on spaces whose open sets are defined in an algebraic way.

The details differ, and the gluing proof must be justified in the relevant setting. But the organizational idea is portable. We can analyze a complicated object by examining simpler regions, then state precisely which relationships allow reconstruction.

## Sheafification changes the permitted global data

The constant-presheaf example gives a glimpse of another important construction. If a presheaf does not satisfy the gluing rule, one can build an associated sheaf. Informally, sheafification adds the locally determined sections needed for gluing and identifies descriptions that agree sufficiently locally. The result is not an arbitrary repair selected by hand; it has a universal property.

Every map from the original presheaf into a sheaf factors uniquely through its sheafification, in the appropriate category of presheaves. Thus sheafification is left adjoint to the inclusion of sheaves into presheaves. This means that the associated sheaf is the most economical recipient for the original local information when our target must obey the sheaf axiom.

For the presheaf with two constant labels, sheafification permits assignments that are locally constant, including different labels on disconnected components. The transformation does not demand that two conflicting labels on a nonempty overlap suddenly become compatible. It allows new global sections only when the local restrictions genuinely match.

This is a beautiful example of several categorical ideas working together. We start with a functor, impose a gluing condition expressed by an equalizer, and obtain a universal correction through an adjunction. The abstract definitions are serving a precise practical problem: turning coherent local information into objects that can be reconstructed globally.

## Why category theory helps here

At first, sheaves can look like a technical way to talk about functions. The category-theoretic perspective reveals a larger pattern. A presheaf is a contravariant functor on the open-set category. A sheaf satisfies an additional matching condition. Morphisms of sheaves are families of maps that commute with restriction. The category of sheaves itself has rich structure, and constructions familiar from sets can acquire local meanings there.

That last point leads to a surprising development. Instead of treating a sheaf only as an object attached to a space, we can study the entire category of sheaves over that space. It turns out to behave like a generalized universe of sets, with its own notion of truth varying over regions. This will lead to topoi and categorical logic.

But we should not race there before the gluing example is clear. The enduring insight is that agreement on overlaps converts many small explanations into one coherent global explanation. The failure to agree is itself useful information, and the failure of existence can reveal a global obstruction.

## One final map

Imagine the cartographer again. Each local map comes with its region of validity. Restriction crops a map to a smaller area. Agreement on overlaps establishes compatibility. The sheaf condition guarantees that compatible maps describe exactly one map on their union.

The powerful part is the word *exactly*. It prevents local information from producing contradictory or ambiguous global reconstructions. It provides an explicit mathematical contract for assembling data, functions, and structures across regions.

We began with overlapping sheets of paper and reached contravariant functors, equalizers, stalks, and global obstructions. All of these ideas serve the same question: when does knowing something everywhere locally amount to knowing one thing globally? Sheaf theory gives an answer precise enough to prove and flexible enough to use throughout mathematics.

<!-- END SPOKEN LECTURE -->

## Mathematical companion (display only)

**Presheaf.** For a topological space \(X\), regard \(\operatorname{Op}(X)\) as a poset category. A presheaf of sets is \(\mathcal F:\operatorname{Op}(X)^{op}\to\mathbf{Set}\). For \(V\subseteq U\), restriction \(\rho_{UV}:\mathcal F(U)\to\mathcal F(V)\) satisfies \(\rho_{UU}=\mathrm{id}\) and \(\rho_{VW}\rho_{UV}=\rho_{UW}\).

**Sheaf condition.** For an open cover \(U=\bigcup_i U_i\), the canonical map
\[\mathcal F(U)\longrightarrow\operatorname{Eq}\left(\prod_i\mathcal F(U_i)\rightrightarrows \prod_{i,j}\mathcal F(U_i\cap U_j)\right)\]
is bijective. This expresses both unique determination and existence of compatible gluing.

**Continuous-function example.** \(\mathcal F(U)=C(U,\mathbb R)\) is a sheaf. Compatible sections \(f_i\) define \(f(x)=f_i(x)\) for any \(i\) with \(x\in U_i\); the open-cover locality of continuity proves \(f\) continuous.

**Failure of constant presheaf.** On \(X=\{l,r\}\) discrete, let \(P(U)=\{0,1\}\) for nonempty \(U\), \(P(\varnothing)=\{*\}\), with identity restrictions among nonempty opens. Sections \(0\in P(\{l\})\) and \(1\in P(\{r\})\) match on empty overlap but do not glue to \(P(X)\). The associated constant sheaf is \(U\mapsto\{\text{locally constant }U\to\{0,1\}\}\).

**Stalk.** At \(x\in X\), \(\mathcal F_x=\operatorname{colim}_{x\in U}\mathcal F(U)\) over neighborhoods directed by restriction; it consists of germs \([U,s]\) modulo equality on some smaller neighborhood.

### Exercises with answers

1. **Exercise:** Give a compatible pair of functions on overlapping intervals. **Answer:** \(f(x)=x^2\) and \(g(x)=x\cdot x\), whose restrictions agree.
2. **Exercise:** What extra condition distinguishes a sheaf from a presheaf? **Answer:** Every matching family on any open cover glues uniquely.
3. **Exercise:** Is equality of function values at a point sufficient for equality of germs? **Answer:** No. For instance \(f(x)=0\) and \(g(x)=x\) agree at 0 but have distinct germs there.
4. **Exercise:** Does the sheaf axiom guarantee a global section from arbitrary local sections? **Answer:** Only when the local sections are compatible on all overlaps.

### References

- The Stacks Project, “Sheaves on Spaces,” https://stacks.math.columbia.edu/browse
- The Stacks Project, *Sites and Sheaves*, https://stacks.math.columbia.edu/download/sites.pdf
- Tom Leinster, *Basic Category Theory*, https://arxiv.org/abs/1612.09375
- Emily Riehl, *Category Theory in Context*, https://emilyriehl.github.io/books/
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic*.
