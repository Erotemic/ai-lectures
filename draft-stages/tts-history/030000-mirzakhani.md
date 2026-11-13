# 030000 — Maryam Mirzakhani: How can we count the paths through every possible surface?

**Track:** History · People and ideas. **Theme:** Hyperbolic geometry, geodesic counting, moduli spaces, and dynamics. **Background:** a circle, a torus, and elementary plane geometry; the necessary differential geometry is built locally.

<!-- BEGIN SPOKEN LECTURE -->

# Maryam Mirzakhani: How can we count the paths through every possible surface?

Imagine walking on the surface of a doughnut. You set off in a straight direction, as straight as walking on that curved surface allows. If your path eventually returns to its starting point, it might go once around the central hole. Or it might travel through the hole and around the body of the doughnut in a more complicated combination. Some returning paths cross themselves. Others close into a loop without any self-intersection.

How many simple returning paths can there be? If we place a limit on their length, can we count them? What happens if we change the shape of the surface while keeping its fundamental pattern of holes the same? What does the answer tell us about the collection of every possible geometry that the surface could carry?

These questions sound like an invitation to draw endlessly complicated curves. Maryam Mirzakhani found that they lead to extraordinarily precise mathematics. She connected the counting of closed geodesics to the geometry and volume of spaces whose individual points represent entire curved surfaces. Later, working with collaborators, she helped establish rigidity results for flows on these spaces that had been thought too irregular for such classification.

Mirzakhani was born in Tehran in nineteen seventy-seven and died in twenty seventeen, at forty. In twenty fourteen she became the first woman and the first Iranian mathematician to receive a Fields Medal. The International Mathematical Union honored her contributions to the dynamics and geometry of Riemann surfaces and their moduli spaces. Those words are technically accurate, but they conceal the experience of the mathematics. To understand her work we need to build the picture from a few elementary pieces: a curve, a surface, a way to measure length, and an entire space of possible surfaces.

The Fields Medal changed her public life in a way she had not sought. When she first received the email saying she had won, she reportedly suspected that it was a hoax. She had a reputation for ambitious mathematical projects and for modesty when discussing her own work. These traits can coexist. Colleagues recalled that she was willing to attempt problems others regarded as forbiddingly difficult, yet she often described her own progress with caution. She became an inspiration to many young people, especially girls interested in mathematics, while remaining protective of her private life. The distinction is important because her work was the achievement of an individual with relationships and responsibilities, not simply a symbol produced by an award.

## Tehran, stories, and mathematical problems

Mirzakhani grew up in Tehran during the Iran–Iraq War and attended Farzanegan, a school for academically talented girls. She spoke about wanting to be a writer when she was young. The connection between writing and mathematics remained a way she described research: mathematical problems developed like stories whose characters only gradually became familiar.

In an interview years later, Mirzakhani remembered that her childhood ambition was to write stories. She read novels voraciously, including biographies and stories about people who had accomplished difficult things. Her older brother delighted her with the story of how the young Gauss had summed the numbers from one to a hundred. She liked the unexpectedness of the solution, although she could not reproduce it herself at the time. Her parents encouraged meaningful work without treating prizes as the purpose of education. These memories make the later Fields Medal more interesting. Mathematics did not arrive as a destiny she recognized at age five. It gradually won her attention through books, friendship, and the pleasure of a problem suddenly becoming clear.

A friend and fellow mathematician, Roya Beheshti, recalled studying and solving problems with her during their school years. Mirzakhani represented Iran at the International Mathematical Olympiad and won gold medals in nineteen ninety-four and nineteen ninety-five, with a perfect score on the second occasion. These are remarkable achievements, but Olympiad mathematics and research mathematics reward different abilities. A competition asks for a complete solution within hours. A research question might resist definition, let alone solution, for years. Mirzakhani's later career illustrates the importance of sustained attention to a difficult problem without knowing in advance what techniques will work.

At Farzanegan, the decisive friendship with Roya Beheshti developed among the bookstores near their school. Mirzakhani recalled that customers were discouraged from browsing for long, so the two girls sometimes bought books almost at random. The friendship lasted into their adult mathematical careers. Her first year at the new school was not a triumph. According to Mirzakhani and Beheshti, a teacher considered her mediocre at mathematics, and her confidence suffered. The next year a more encouraging teacher changed the atmosphere. The contrast is instructive: an eventual mathematical pioneer had firsthand experience of being judged too quickly by a teacher. Mirzakhani later emphasized the importance of other people believing that a child can learn.

She studied at Sharif University of Technology in Tehran, completing her undergraduate degree in nineteen ninety-nine. At Harvard she pursued doctoral work under Curtis McMullen, himself a Fields Medalist, and completed her doctorate in two thousand four. Her thesis already contained major advances concerning simple geodesics and the volumes of moduli spaces. She then held a Clay Mathematics Institute research fellowship while working at Princeton. In two thousand eight she moved to Stanford as a professor.

Before university, Mirzakhani and Beheshti pursued competition problems with growing intensity. Mirzakhani won International Mathematical Olympiad gold medals in nineteen ninety-four and nineteen ninety-five, the second with a perfect score. In her own account those achievements also meant meeting other mathematically curious teenagers and finding a larger community. She later spoke about the principal of her girls' school as someone willing to press for the same opportunities available to boys. Her success was made by her own sustained work, but the surrounding teachers, friends, family, and school administrators played real roles. She was keenly aware that the timing of her adolescence, as the Iran–Iraq War ended, had helped make those opportunities possible.

Drawings are particularly apt for the surfaces she studied, but geometry research must move between the picture and a proof. A sketch can suggest what happens to a curve when a surface is stretched. It cannot, by itself, establish how many curves of every possible type exist or classify the closure of a dynamical orbit.

The way she worked as an adult could look bewildering to visitors. Large sheets of paper covered the floor of her home office. She drew shapes again and again, tracing loops, cuts, and relationships that were difficult to hold in a purely verbal argument. Her husband, Jan Vondrák, described a daughter who thought the sketches looked like painting. Mirzakhani herself compared mathematical research to slowly developing a story: one follows characters, discovers how they are related, and sometimes finds that an earlier impression was mistaken. That comparison helps explain the pace of her work. She could stay with a question for years, testing paths that did not immediately lead to a theorem.

## A line that stays straight on a curved surface

On a plane, the shortest path between nearby points is a straight line. On a curved surface there is an analogous concept: a geodesic. A geodesic moves forward without turning within the surface, even though it may appear curved to an observer looking from outside. A great circle on a sphere, such as the equator, provides a familiar example. Travel along the equator and your path never turns left or right within the sphere.

When a geodesic returns to its starting point with the same direction, it is closed. When the curve has no self-crossings, it is simple. These properties need to be distinguished. Some closed geodesics wind into complicated networks of crossings; simplicity rules those out. Repeating the same closed route several times also does not produce a new simple curve in the sense used in the counting theorem.

For a concrete picture, think of the ordinary flat square with its opposite edges identified. Step out through the right edge and reappear at the left. Step out through the top edge and reappear at the bottom. The result is a flat torus, a mathematical doughnut whose local measurements come from the plane, though it cannot be embedded in ordinary three-dimensional space with that flat metric everywhere.

A straight path on this torus can be described by two whole numbers, a and b, giving how many times it wraps horizontally and vertically. If the two numbers have no common factor greater than one, the path closes without traversing a shorter primitive route repeatedly. The pair one, zero goes once around horizontally. The pair one, one travels diagonally and closes after one horizontal and one vertical wrap. The pair two, one has a different slope and again defines a simple primitive loop.

With a unit square metric, the length of the primitive route is the square root of a squared plus b squared. So counting simple routes of length at most L becomes a lattice-point problem: count integer pairs in a disk of radius L whose coordinates are coprime. Roughly speaking, the number grows as the area of that disk, which is proportional to L squared. One must account for primitive pairs and whether reversing the direction counts as the same route, but the exponent two is robust.

This little experiment is valuable because it makes the connection between geometry and counting visible. A geometric object becomes an arithmetic pair. A length bound becomes a disk. And an infinite family of curves becomes a countable collection with a predictable growth law. The challenge is to do something comparably precise on curved surfaces that are far more complicated than the flat torus.

## How many winding directions fit inside a circle?

The flat torus calculation can be pushed a little further, because it gives a small but authentic example of an asymptotic counting theorem. Draw a disk of radius ten in the ordinary plane. There are only finitely many integer lattice points inside it. Some points, such as two and four, correspond to pairs with a common factor. That pair describes the same geometric direction as one and two but runs around the route twice. To count simple primitive curves, we discard such repeated pairs.

A child who wanted to write stories might have found this kind of problem appealing for a particular reason. A closed geodesic has a recognizable identity, yet it changes when the surface is deformed. Counting all such curves is like asking how many distinct journeys can be taken through the same landscape while keeping the rule against retracing or self-crossing. Mirzakhani's drawing habit was therefore part of a serious mathematical method. The images let her reason about many possible surfaces before the equations were settled. Colleagues who saw the paper-strewn office sometimes could not tell what each diagram meant; she could use those diagrams as a private language for discovery.

The proportion of large integer pairs that are coprime approaches six divided by pi squared. One can understand why a constant of this form arises by considering divisibility one prime at a time. For a prime r, roughly one out of every r squared pairs has both coordinates divisible by r. Thus the fraction surviving the r test is one minus one over r squared. Multiplying these factors over the primes produces a convergent infinite product, equal to six over pi squared. This argument requires a limiting justification, but its arithmetic meaning is accessible.

The disk itself contains approximately pi times L squared integer lattice points when the radius is L. Retaining only primitive pairs multiplies the leading count by six over pi squared. If direction reversal describes the same unoriented closed route, we divide by two. In that convention, the leading count is approximately three over pi times L squared. The exact coefficient is less important here than the mechanism: a geometric cutoff becomes a region in a vector space, and arithmetic restrictions modify its volume by a calculable density.

This is the kind of relationship Mirzakhani sought in a vastly richer setting. For a hyperbolic surface we cannot label every simple curve by one pair of integers. We can, however, organize families of curves using coordinates related to the topology and measure the regions corresponding to bounded length. The flat torus example therefore predicts the shape of the answer without pretending that the full proof is an elementary lattice count.

## Why a hyperbolic surface is different

Mirzakhani's most celebrated early counting theorem concerns hyperbolic surfaces. A hyperbolic surface has constant negative curvature. To visualize negative curvature, think of a saddle: it bends one way along one direction and the opposite way across it. A complete hyperbolic surface may be constructed by fitting together pieces of a mathematical space with this uniform negative curvature.

A sphere has positive curvature. An ideal flat torus has zero curvature. A closed oriented surface with two or more handles can carry a hyperbolic metric. The number of handles is called its genus. Genus two means a double-handled surface. The exact geometry can change even while the number of handles remains fixed.

One striking constraint comes from Gauss–Bonnet. For a closed hyperbolic surface of genus g, with curvature normalized to minus one, its area is four times pi times g minus one. A genus-two surface has area four pi. So when we vary the geometry of a genus-two hyperbolic surface, the total area remains constant. We can make certain closed loops long or short, but we cannot arbitrarily change the total area.

If every genus-two hyperbolic surface has the same area, are they all the same? Far from it. The ways the handles stretch, pinch, and twist can differ enormously. One surface might contain a short loop separating its two handles; another might have no correspondingly short separating loop. These are different geometric structures on the same topological kind of surface.

Negative curvature also changes the path-counting problem. The total number of closed geodesics of length at most L on a compact hyperbolic surface grows approximately exponentially with L, when counted in the standard primitive-geodesic sense. But Mirzakhani examined the far smaller collection of **simple** closed geodesics, those with no self-intersections. Their number grows polynomially. That difference between exponential growth and polynomial growth is already a clue: the no-crossing requirement imposes enormous geometric structure.

## Cutting a surface into pairs of pants

A useful technique is to cut a complicated surface along carefully chosen simple closed curves until it separates into simpler pieces. In hyperbolic geometry the basic piece is a pair of pants: a sphere with three holes and three geodesic boundary curves. The name is literal. Imagine two openings for legs and one at the waist.

For a hyperbolic pair of pants, the three boundary lengths determine its geometry up to isometry. There is no further continuous freedom inside the piece once those lengths are fixed. A complicated surface can be assembled by gluing several such pieces along matching boundary curves. The gluing introduces another kind of information: the amount of twist between the two pieces.

Take a closed genus-two surface. It can be divided along three suitable simple closed curves into two pairs of pants. There are three independent lengths, one for each cut. And when we glue the pairs of pants back together, there are three twist parameters. This gives six real coordinates for the possible marked hyperbolic geometries, at least relative to that choice of decomposition. They are called Fenchel–Nielsen coordinates.

We have discovered something important: to study all genus-two hyperbolic shapes, we do not need to store each surface as a complicated picture. A finite collection of lengths and twists can encode one. For genus g at least two, the number of real shape parameters is six g minus six. The exponent in Mirzakhani's counting theorem will be this very number.

But there is a subtlety. A space of coordinates for **marked** surfaces distinguishes a chosen identification between the abstract topological surface and its geometric realization. If we forget the marking, some descriptions become equivalent under twists and rearrangements of the underlying topology. The quotient is called a moduli space. Its points represent geometric structures up to the relevant equivalence. Mirzakhani's work moves between the space of marked surfaces, where coordinates are convenient, and the moduli space, where geometry can be integrated and counted.

## How can a space of surfaces have volume?

We can assign a volume to a collection of ordinary points in three-dimensional space. Length times width times height gives the volume of a box. In a space of surfaces, an individual point is already an entire geometric surface. What could volume mean there?

The answer is that a moduli space is itself a geometric object, with local coordinates and a natural measure. Certain mathematical structures specify how to measure sets of nearby shapes. For hyperbolic surfaces, the Weil–Petersson geometry provides such a structure. Its associated volume form lets one integrate functions over families of surfaces, just as one integrates ordinary functions over the plane.

Think about a family of genus-two surfaces in which three lengths and three twists are permitted to vary over some region of parameter space. That is a six-dimensional family. A six-dimensional volume is not something we can picture directly, but we can understand how one computes it: choose coordinates, identify the local density describing the measure, and integrate over the allowed region.

A very useful feature of Fenchel–Nielsen coordinates is that the Weil–Petersson symplectic form has a clean description in terms of length and twist variables, with a convention-dependent constant factor. The length of a chosen curve and its twist act as paired coordinates. This relation between geometry and integration is one of the reasons pants decompositions are so effective.

Mirzakhani's doctoral work studied moduli spaces of hyperbolic surfaces **with geodesic boundaries of prescribed lengths**. The boundary lengths become parameters in a volume function. The remarkable result is that, for fixed topological type, the Weil–Petersson volume is a polynomial in the squares of those boundary lengths, of bounded degree. This is a rigid algebraic answer to a problem about a continuum of curved objects.

Let's make that less abstract. Imagine a one-holed torus: a genus-one surface with one boundary circle. Fix the length of that boundary. There is still a family of possible internal hyperbolic shapes. The volume of that family changes with the boundary length, and in standard conventions the answer has the form a constant times the square of the boundary length plus another constant involving pi squared. The precise constant depends on the convention for orbifold volume, but the polynomial dependence is the essential discovery.

For a pair of pants, which has genus zero and three boundaries, specifying the three lengths leaves no continuous shape freedom. The corresponding volume is a zero-dimensional normalization. For more complicated surfaces the volume is not elementary, but Mirzakhani found recursions that reduce the computation to lower-complexity cases. In the mathematics, a complicated global quantity becomes computable through smaller geometric pieces.

## Turning a sum over curves into an integral

Where does the recursion come from? A key ingredient is a remarkable identity first discovered by Greg McShane, involving lengths of simple geodesics on certain hyperbolic surfaces. Schematically, infinitely many geometric terms add up to one fixed quantity. Mirzakhani generalized such identities to bordered hyperbolic surfaces, then integrated them over moduli space.

Here is the conceptual mechanism. Suppose we want the total volume of a family of surfaces. It can be hard to integrate directly over all their complicated shapes. Instead, we express a simple constant as a sum over specially chosen curves or pairs of curves on each surface. We then integrate the identity over the entire moduli space. Under the analytic conditions that justify rearranging the operations, the integral of a sum becomes a sum of integrals.

The summands distinguish curves. Cutting along one of those curves decomposes the surface into simpler pieces, where length and twist coordinates become manageable. The resulting integrals can be related to the volumes of moduli spaces of lower genus or with different numbers of boundaries. That is the source of the recursion: a difficult volume calculation is reduced to a systematic accounting of ways to cut surfaces.

This is not merely a clever computational device. It connects three kinds of structure: individual geodesics on a surface, global integration over families of surfaces, and algebraic relations among the resulting volume functions. The papers from two thousand seven show how the calculation yields polynomial volume formulas and then connects to intersection theory on moduli spaces of curves.

The intersection-theoretic connection led Mirzakhani to a new proof of the Witten–Kontsevich relations, often described through Virasoro constraints. Those identities had already been established by Maxim Kontsevich. Her achievement was to derive them through a geometric route involving hyperbolic surfaces and their volumes. She opened a bridge between seemingly distant ways of studying the same moduli space.

## From geometric volume to algebraic identities

There is another remarkable consequence of Mirzakhani's method. Algebraic geometers study moduli spaces of complex curves by introducing characteristic classes and intersection numbers. These are ways of assigning numerical invariants to families of geometric objects. Instead of counting geodesic loops directly, one intersects geometric conditions on a compactified moduli space and records the resulting number. The language can seem far removed from a hyperbolic pair of pants.

Yet both descriptions concern related moduli spaces. Hyperbolic geometry supplies boundary lengths, twists, and the Weil–Petersson volume form. Algebraic geometry supplies cohomology classes whose intersection numbers obey stringent identities. Mirzakhani connected the polynomial coefficients of the volume formulas to these intersection numbers. Consequently, a recursion discovered through cutting and integrating hyperbolic surfaces could reproduce relations that had arisen in the algebraic-geometric study of curves and mathematical physics.

A simple polynomial analogy helps. Suppose a volume depends on a boundary length L through a formula of the form A plus B times L squared. The constant A tells us the volume at zero boundary length, interpreted in the appropriate limiting geometry. The coefficient B tells us how that volume changes as the boundary begins to grow. In a more complicated surface there are several boundary lengths, and the polynomial contains mixed terms. Each coefficient can carry geometric information. Mirzakhani showed how the coefficients fit into intersection theory rather than merely forming a convenient table of computed numbers.

It was particularly significant that this route yielded a new proof of the relations associated with Witten's conjecture, originally proved by Kontsevich. Two very different forms of mathematics arrived at the same structure. This does not mean the original proof was incorrect or unnecessary. A second proof can reveal connections inaccessible from the first: a statement about abstract intersection numbers acquires a concrete interpretation through lengths, volumes, and decompositions of hyperbolic surfaces.

## Counting the simple paths

Now we can return to the original counting question. Fix a closed hyperbolic surface X with genus g at least two. Let N of L be the number of simple closed geodesics on X whose lengths are no greater than L. Mirzakhani proved that N of L behaves, as L grows, like a positive constant depending on X multiplied by L raised to the power six g minus six.

For a genus-two surface, that means sixth-power growth. If we increase a very large length cutoff by a factor of two, the leading asymptotic prediction multiplies the number of simple closed geodesics by two to the sixth power, or sixty-four. The surface can have many different hyperbolic shapes, and the leading constant depends on which one we choose, but the exponent six is determined by the topology.

Why does six appear? We just saw that the space of genus-two hyperbolic shapes has six real parameters. The deeper counting theorem requires more than the observation that two numbers are the same. It uses integration over moduli spaces, the structure of measured laminations, and ergodic methods. Still, the agreement is a guide to the proof: curves can be measured by coordinates with a scaling law, and the volume of the corresponding six-dimensional region grows like the sixth power of the scale.

Think again of primitive lattice points on the flat torus. Enlarging a disk by a factor of two multiplies its area by four, and the primitive-point count grows accordingly. On a genus-two hyperbolic surface the analogous parameter region has six dimensions. Enlarging all lengths by a factor of two multiplies the leading volume by sixty-four. This is a heuristic analogy; the mathematical theorem has additional geometry and counting arguments. But it gives a listener a reason to expect polynomial growth with an exponent tied to the dimension of a space of curves.

The result concerns **simple** closed geodesics and their primitive isotopy classes; it must not be confused with counting every closed geodesic. The two problems have completely different asymptotic scales. That distinction is central to Mirzakhani's work. By imposing a topological restriction, she found a tractable counting problem whose answer reflects global geometric structure.

## When geometry begins to move

Mirzakhani later pushed from static geometric counting into dynamical systems. The basic shift is easy to state: instead of asking what a geometric surface looks like, ask what happens when we continuously deform it according to a rule. Which shapes are visited? Do trajectories settle into manageable families? Can the closure of a trajectory be described by equations?

A useful model is a flat surface constructed by gluing polygons along matching parallel sides. A translation surface carries local flat coordinates except at a finite set of cone singularities. A straight-line path in such a surface models, among other things, a billiard path in a polygon after reflected copies are used to unfold the bounces. The geometry has become a dynamical tool.

Take a rectangle, identify opposite edges, and travel in a direction whose slope is rational. On the square torus, the path closes after finitely many wraps. For an irrational slope, the path does not close, and it winds densely through the torus. Even this simple example shows that a small change in direction can alter the qualitative behavior of an orbit. On more complicated translation surfaces the possible trajectories and orbit closures become far richer.

There is another motion we can perform. Stretch every polygon horizontally by a factor of two and compress vertically by a factor of one half. The area remains unchanged. More generally, a matrix of determinant one can act on the local coordinate charts, stretching, shearing, and rotating the geometry. The group of such real two-by-two matrices is called S L two R. It acts on the moduli space of translation surfaces.

What is the closure of the orbit of one translation surface under all those deformations? It might fill a large region of moduli space. It might be confined to a smaller geometric family. Without a theorem, there is no reason to assume the boundary of the orbit's range has a simple shape.

## The rigidity of a complicated world

Mirzakhani and Alex Eskin proved powerful classification results for invariant measures arising from this action. With Amir Mohammadi they established orbit-closure and equidistribution results, published in the Annals of Mathematics in two thousand fifteen. A common informal description is the magic-wand theorem, because orbit closures that could have seemed ragged or fractal are shown to have a strongly organized structure.

The accurate mathematical statement is subtler than saying all orbits are dense or every closure is an ordinary linear plane. The closures are affine invariant submanifolds in appropriate local period coordinates, and the theorems identify natural invariant measures and equidistribution behavior under their hypotheses. The term affine describes linear equations with constant terms in local coordinates, assembled into the moduli-space setting. The result is striking precisely because the ambient space is complicated while the orbit closures have this kind of rigidity.

Why might anyone hope for such a result? There is an older family of theorems about flows on homogeneous spaces, developed by Marina Ratner and others, where invariant measures and orbit closures can be classified in unexpectedly rigid ways. Moduli spaces of flat surfaces are not the same kind of homogeneous space. Eskin, Mirzakhani, and Mohammadi established an analogue in a much less uniform setting. The difficulty is that the space can degenerate: certain geometric features may become arbitrarily short, and the dynamics can move toward its boundary.

Mirzakhani's earlier work on earthquake flows also belongs to this evolution. An earthquake deforms a hyperbolic surface by shearing along geodesics, much as one tectonic plate slips past another. Her results relate this flow to ergodicity and mixing in an appropriate measured setting. Ergodicity is a statistical statement about the behavior of typical trajectories, not a claim that every particular path visits every point. Mixing describes an additional loss of long-time correlations for suitable observables.

These dynamical results are very far from elementary curve counting in technical appearance. Yet they return to the same concern: the apparently overwhelming possibilities for surfaces and trajectories turn out to obey deep structural laws.

## A way of working, and a community

The story of Mirzakhani's mathematics also includes the people with whom she worked. Her Harvard adviser Curtis McMullen had contributed to the geometry and dynamics of Riemann surfaces. The generalized identities used in her volume calculations grew from McShane's earlier work. Her analysis of moduli spaces intersected the work of Scott Wolpert and others on Weil–Petersson geometry. Her later breakthroughs depended on long collaborations with Alex Eskin and Amir Mohammadi. A full account should credit this intellectual network without diminishing the originality of her own results.

Mirzakhani preferred to think over problems for long periods, often drawing pictures whose importance was not immediately clear to an observer. This is sometimes described as a mysterious style of genius. A more practical description is that she invested in finding the correct representations of a problem. The representations had to be strong enough for an exact proof: pants decompositions, geodesic-length identities, volume recursions, and coordinates for dynamics all served distinct logical purposes.

Her achievements were recognized before the Fields Medal. She received the Ruth Lyttle Satter Prize of the American Mathematical Society in two thousand thirteen and a Clay Research Award in two thousand fourteen. She was elected to important scientific academies. When she received the Fields Medal in Seoul in August two thousand fourteen, the recognition was historic because no woman had previously won it in the prize's history. The mathematical citation itself recognized work that had transformed geometry and dynamics.

Public accounts sometimes present her life as if the Fields Medal were the beginning of her mathematical significance. By the time of that award, the thesis results on volume recursion and curve counting were already influential, and the Eskin–Mirzakhani program was a major development in progress. The medal was recognition of a substantial body of research, not the source of its value.

She died in July two thousand seventeen after cancer, leaving a daughter and her husband, mathematician Jan Vondrák. The loss was deeply felt by collaborators, students, and the broader mathematical community. The later history of the subject is full of work building on the tools and questions she developed. None of that continuation changes the fact that her own published results were complete mathematical achievements.

## An unexpected answer to a counting question

Let's collect the ideas without turning them into a list of theorems. We began with a person walking along a closed path on a curved surface. To count the simple closed routes, Mirzakhani first needed ways to describe the surface itself. Cutting into pairs of pants supplied lengths and twists. These parameters made the space of all shapes accessible to geometry and integration. Identities involving geodesic lengths provided recursions for its Weil–Petersson volumes. Those volumes, combined with further geometric and dynamical ideas, led to precise asymptotic counts of simple closed geodesics.

Later, the same habit of looking for structure in the space of surfaces allowed her and her collaborators to classify dynamical orbit closures that at first seemed resistant to any tidy description. In both research programs, the object being studied was not one particular surface, but the mathematical space of all surfaces of a given kind and the laws governing movements within that space.

The most useful lesson from this portrait is perhaps a method of mathematical imagination. A hard problem on one object may become clearer after we build a space whose points are entire objects like it. We can then ask new questions: what are the coordinates of that space, what does it mean to measure a region inside it, and which transformations preserve its structure? For Maryam Mirzakhani, those questions turned a problem about counting curves into new mathematics about the geometry and dynamics of worlds of possible surfaces.

<!-- END SPOKEN LECTURE -->

---

## Mathematical and historical companion (display only)

### 1. Flat torus as a counting analogy

Identify \(\mathbb R^2/\mathbb Z^2\). Primitive integer vectors \((a,b)\) with \(\gcd(|a|,|b|)=1\) parametrize unoriented simple closed geodesic *classes* up to \((a,b)\sim(-a,-b)\). In the unit flat metric their lengths are \(\sqrt{a^2+b^2}\). The count grows on the order of \(L^2\). This is a flat genus-one analogy, **not** the hyperbolic genus-\(g\) theorem.

### 2. Hyperbolic area, pants coordinates, dimension

For a closed oriented surface of genus \(g\ge2\) with curvature \(K=-1\), Gauss–Bonnet gives
\[
\operatorname{Area}(X)= -2\pi\chi(X)=4\pi(g-1).
\]
For a chosen pants decomposition, there are \(3g-3\) independent length parameters and \(3g-3\) twists, so \(\dim_\mathbb R\mathcal T_g=6g-6\). A genus-two closed hyperbolic surface has area \(4\pi\), and its marked Teichmüller space has real dimension 6. The Weil–Petersson symplectic form pairs length and twist differentials, with normalization depending on the twist convention.

### 3. Weil–Petersson volume polynomial

For stable \((g,n)\) with \(2g-2+n>0\), fixed geodesic boundary lengths \(L_1,\ldots,L_n\), and the conventions of Mirzakhani, the Weil–Petersson volume is a polynomial in \(L_1^2,\ldots,L_n^2\), of total degree at most \(3g-3+n\) in those squares. Her 2007 *Inventiones* paper develops a recursion using generalized McShane identities and integration over moduli space. Be attentive to orbifold volume conventions when quoting individual low-genus constants (a factor of two occurs between some references for \(V_{1,1}\)).

### 4. Simple geodesic counting

For a closed oriented genus \(g\ge2\) hyperbolic surface \(X\), Mirzakhani's theorem gives
\[
N_X(L)\sim c(X)L^{6g-6},\qquad c(X)>0,
\]
where \(N_X(L)\) counts simple closed geodesics (unoriented, by distinct primitive free-homotopy classes) with length at most \(L\). More refined results count mapping-class-group orbits and allow finite-area cusped surfaces, with exponent \(6g-6+2n\) in the appropriate setting. For genus two, \(N_X(2L)/N_X(L)\to64\). This should not be confused with the exponentially growing total count of primitive closed hyperbolic geodesics.

### 5. \(SL(2,\mathbb R)\) action on translation surfaces

If a translation structure is locally represented by polygon coordinates, applying \(A\in SL(2,\mathbb R)\) to those coordinates preserves area. For example, \(A=\operatorname{diag}(2,1/2)\) doubles horizontal lengths and halves vertical lengths. In the strata of translation surfaces, the Eskin–Mirzakhani measure classification and Eskin–Mirzakhani–Mohammadi orbit-closure results describe affine invariant submanifolds in period coordinates. The theorem **does not** claim all orbits are dense in their entire stratum, nor that all orbit closures are linear subspaces globally.

### 6. Chronology and source guidance

- 1977: born in Tehran. 1994 and 1995: International Mathematical Olympiad gold medals, perfect score in 1995. 1999: bachelor's degree from Sharif University of Technology.
- 2004: Harvard doctorate under Curtis McMullen; Clay Research Fellowship and Princeton appointment. 2007: volume papers in *Inventiones* and *JAMS*. 2008: simple-geodesic counting paper in *Annals*; Stanford appointment.
- 2013: AMS Ruth Lyttle Satter Prize. 2014: Fields Medal and Clay Research Award. 2015: Eskin–Mirzakhani–Mohammadi *Annals* orbit-closure theorem; IAS visit. 2017: died in California.

Source URLs and individual historical claim anchors are recorded in `metadata/030000.json` and `metadata/sources.json`. The distinction between the 2007 volume papers, 2008 geodesic count, and 2015 joint dynamical results is central.

### Historical source notes: human-portrait revision

The additional biographical scenes in the spoken lecture are grounded in the following documentary records. They concern historical context; the mathematical calculations and theorem hypotheses are unchanged.

- `history-mirzakhani-2014-interview` — Maryam Mirzakhani interview, The Guardian (August 13, 2014). https://www.theguardian.com/science/2014/aug/13/interview-maryam-mirzakhani-fields-medal-winner-mathematician
- `history-mirzakhani-2014-profile` — Erica Klarreich, A Tenacious Explorer of Abstract Surfaces (2014), Quanta. https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/
- `history-mirzakhani-vondrak-2020` — Jan Vondrák, In Memoriam: Maryam Mirzakhani, Bulletin AMS (2020). https://www.ams.org/journals/bull/2020-57-03/S0273-0979-2020-01695-2/supplementary-information/S0273-0979-2020-01695-2-original-version.pdf

Source claims are indexed by exact spoken anchors in `metadata/030000.json`.
