# Plan accurate work from shared references

<!-- BEGIN SPOKEN LECTURE -->

# Plan accurate work from shared references

## Measure First, Then Shape: Error, Reference Surfaces, and Tool Choice

You want to cut a board to fit between two walls. You measure the gap: forty-eight inches. You mark forty-eight inches on the board, cut carefully, and discover the board will not fit. What went wrong? Perhaps the two walls are not parallel. Perhaps the measuring tape was hooked differently on the wall and the board. Perhaps the blade removed material on the wrong side of the pencil line. Perhaps the board is square but the corner is not. The problem is not simply that the measurement was inaccurate. It may be that the original question, "How long is the gap?" was underspecified.

Good work starts by identifying what surfaces, edges, or axes matter. Machinists call the designated references *datums*. Carpenters use a reference face and edge. Surveyors establish control points. The word changes by trade, but the habit is universal: choose what counts as fixed, and measure other things consistently from it.

### A measurement is an observation with a purpose

Suppose you are fitting a shelf into a recess. If the shelf needs to slide in, the important dimension is not necessarily the width at eye level. It is the tightest clearance along the actual insertion path, with allowance for the shelf's shape and for the finish. Measuring in one place and reporting many decimal places does not help if the gap varies by several millimeters along its depth.

Accuracy means closeness to the relevant true value. Repeatability describes how closely repeated measurements agree under similar conditions. Precision is sometimes used for the spread of repeated results, or informally for fine resolution. These ideas must not be conflated. A tape can consistently read three millimeters too long because its hook is damaged. That reading is repeatable but biased.

Resolution is merely the smallest interval the instrument can display or conveniently distinguish. A digital caliper reading to hundredths of a millimeter does not guarantee the caliper, workpiece, and operator together are accurate to that amount. Dirt on the jaws, a warm object, squeezing force, and imperfect alignment can dominate the result. The finest instrument is not always the most reliable choice for a rough surface or a large opening.

### Understand how errors accumulate

Imagine marking five equal segments along a wall, each measured from the end of the previous segment. A small error in each interval accumulates along the length. Measuring each segment from one established origin can reduce some kinds of cumulative layout error. On the other hand, a single origin can itself be wrong, so a second independent check is still useful.

The classic shop instruction, "Measure twice, cut once," is not an invitation to read the same tape twice without changing anything. Better is to verify by a different route. Measure the total and the pieces. Check a rectangle's diagonals as well as its sides. Check whether an allegedly square edge is truly square using a known reference. Make a test fit when material is costly or geometry is uncertain.

A diagonal is especially informative. If a flat quadrilateral has equal opposite side lengths yet unequal diagonals, it is not a rectangle. But equal diagonals alone do not establish the shape of an arbitrary quadrilateral; we still need appropriate constraints. Shop heuristics work best when we understand their assumptions.

### How cutting tools actually remove material

A saw blade has thickness, often called kerf, and removes that width of material. If you need a finished piece of exactly five hundred millimeters, placing the center of a three-millimeter kerf directly on the final dimension shortens the piece by roughly half the kerf. We mark the waste side deliberately. Real kerf varies with blade geometry, set, and material, so a test cut can be more informative than an assumed number.

Drills remove material differently. A twist drill uses cutting edges and flutes to create and evacuate chips. Hole size and quality depend on alignment, tool condition, speed, feed, workpiece material, and how the part is restrained. A bit that wanders at the start may never recover the desired center. A pilot or center mark can help with certain materials and geometries, but not every drill requires a smaller preliminary hole. Splintering on exit often reflects support conditions and geometry, not a defective drill.

Clamping also deserves conceptual attention. A clamp provides force, but force is not the same as location. Two boards can be clamped tightly and still be misaligned. A jig, fence, square, or stop establishes geometry; the clamp keeps the work from moving away from it. We should design the setup so that alignment does not depend entirely on how steadily a person can hold the work.

### Fastening is a mechanics problem

A screw converts turning motion into axial force, but applied torque does not translate to a single predictable clamping force without assumptions about thread friction, bearing surfaces, lubrication, and material. That is why some fasteners have specified torque procedures, and why blindly tightening until the tool feels hard to turn can strip threads, crush wood, or damage a joint.

Fasteners may resist shear, withdrawal, tension, or combinations. The correct type depends on load direction, substrate, edge distance, spacing, corrosion environment, and whether a connection can move with temperature or humidity. A screw is not inherently stronger than a nail for every framing load. Nor is a larger anchor automatically suitable for a material that may crumble around it. Rated structural connections depend on tested assemblies and applicable design rules, not anecdote.

The word "level" means aligned with the local gravitational horizontal, while "plumb" means vertical. "Square" usually refers to ninety-degree geometry. They are different targets. A cabinet may need to be level even when an old floor is not. A trim piece may need to follow a visibly crooked wall while preserving a straight visual line. Successful workmanship begins by deciding which reference matters for the finished function.

### An actual layout problem

Suppose a cabinet opening measures six hundred and one millimeters at the top, five hundred and ninety-eight at the middle, and six hundred at the bottom. The shelf you want to install is six hundred millimeters wide and twenty millimeters deep. What should you cut?

We cannot answer from those three numbers alone. We need the depth and orientation of the shelf, the width at the exact level where it will sit, whether the walls are straight along the insertion path, and how much clearance the installation needs. If it is an adjustable shelf that will be inserted at an angle, access geometry also matters. A measured minimum of five hundred and ninety-eight is a constraint, not a complete design. The wise worker makes a cardboard or scrap-wood template before committing expensive finish material.

This is also how professionals manage uncertainty: they use a cheap experiment to reduce the cost of a wrong assumption. We can test blade kerf on scrap, measure whether a square is truly square, compare a digital gauge against a known reference, and dry-fit an assembly before gluing. We should record the direction of a failure as well as its magnitude. Too short requires a different remedy from too long; a skewed hole is not merely a hole of the wrong diameter.

### Selection follows the operation

A tool is good when it applies the required force or measurement with useful control and without exceeding the limits of the material, person, or environment. A hand tool may offer more control and less setup for one cut. A powered tool may offer repeatable geometry for a long sequence. A specialist instrument may be necessary when the required tolerance is smaller than the uncertainty of a general-purpose one. Good technique is choosing the reference, geometry, setup, verification, and tool in that order, rather than expecting the most expensive tool to make those decisions for us.

The underlying skill is not remembering fifty tool names. It is learning how to ask: What is the desired geometry? What is the load or motion? Which errors matter? What is an acceptable tolerance? How will I know the finished piece meets it? Once those questions are clear, tool choice becomes a much more tractable decision.

## Reference Faces, Datums, and Practical Layout

The reference chosen for a measurement determines how that measurement can be used in the later operations.

Consider cutting six boards to make a rectangular cabinet. Every board has a length, but the cabinet has additional demands: corners must be square, opposite faces parallel, shelves level relative to one another, and the opening large enough for a door. If the boards are measured carefully but from inconsistent reference edges, the assembly may still twist into a shape no one intended.

The missing idea is a datum. A datum is an agreed reference from which positions, dimensions or orientations are defined. In a machine shop it may be a plane or axis represented by a fixture or set of contact points. In woodworking it may be one straight, flat face and one square adjacent edge. In layout on a building site it may be a benchmark elevation and a set of control lines. The common principle is to stop treating every measurement as an independent guess.

### A measurement needs a question

Suppose a plank is twenty millimeters thick on average, but it is slightly twisted. Which number do you want? The thickness at a particular location, the largest local thickness, or a reference plane from which to mill the other side? A caliper can report a local distance without telling you whether the surfaces are parallel. A tape measure can tell you that the far corner is two meters from a mark without telling you whether the mark belongs to a square rectangle.

Before measuring, decide what property makes the part fit its intended system. Length, squareness, flatness, parallelism, straightness and location are not the same property. They require different checks. For a shelf, the important tolerance may be clear width between supports. For a sliding drawer, parallel guide faces may matter more than the nominal length of the outer box.

### Establish a hierarchy of references

A practical sequence for a rectangular board is to establish a flat reference face, then make an adjacent edge square to it. Mark those two surfaces clearly. Other dimensions can now be defined relative to that pair. If you flip to an unverified opposite edge for half your marks, error can accumulate or reverse unpredictably.

This is why makers put a small face mark on the reference side and an edge mark on the reference edge. The symbols themselves are conventional; their function is architectural. They tell every later operation which surfaces are trusted. A story stick does something similar when many repeated dimensions are needed: one physical reference carries positions directly, avoiding repeated tape readings and transcription error.

### Why repeatedly measuring from the last mark drifts

Imagine drilling five holes in a line, each nominally one hundred millimeters apart. A tempting method is to place the first mark, measure one hundred from it, then another hundred from the second, and so on. Each step includes a small measurement and marking error. If those errors happen to have the same sign, the last hole can drift several times the individual error.

A better method for many layouts is to measure each hole from the same datum: one hundred, two hundred, three hundred, four hundred, five hundred. It avoids error accumulation from previous marks, though it still depends on the measuring instrument and datum being valid. In some tasks a single carefully manufactured template is better still, because it establishes the whole pattern at once.

Tolerance is not the same as carelessness. It is an explicit range within which a part still meets a functional requirement. A board meant to cover a broad gap may tolerate a few millimeters of variation. A shaft bearing fit may demand far tighter control and a different measuring process. Measuring every household cut to a thousandth of a millimeter is not excellence; it is confusing display resolution with needed accuracy.

### A square can be wrong

A combination square, framing square or machinist's square looks authoritative, but the tool itself has error. A useful field check for a square is to mark a line along a reference edge, flip the tool against the same edge, and compare the two lines. A disagreement reveals an angular error, although the test also depends on the reference edge and the fineness of your mark. It is a comparison, not a calibration certificate.

Similarly, a level is not a machine that magically creates a horizontal surface. A spirit level compares its body to gravity. Reverse it end for end on the same surface and compare readings. If they differ, investigate the tool or the contact surfaces. For large layouts, reference elevations can be transferred using a water level, laser level or optical instrument, but each introduces its own setup and alignment uncertainties.

### Marking itself changes the geometry

A pencil line has thickness. If a saw cuts directly through its middle, removes material on the wrong side, or wanders, the resulting part changes. Saw kerf is the width of material removed by the teeth, not the drawn line. A knife line may offer a sharper reference in wood, while a scriber may suit metal. A center punch gives a drill bit a starting location on some materials, but excessive punching can deform thin stock.

Think of a practical tolerance stack. A cut depends on the datum, the measured mark, the mark width, the location of the cutting edge relative to the mark, the tool's path, and the material's response. You can work carefully at every step yet miss your target if you never decide which side of the line is waste.

### Square is a relationship

To lay out a rectangle, equal opposite lengths are necessary but not sufficient for squareness. You can make a parallelogram with equal opposite sides. One quick check is to compare its diagonals. For a true rectangle the diagonals are equal; for a general parallelogram they are not. In a planar four-sided layout with opposite sides constrained appropriately, matching diagonals is useful evidence of squareness, but in irregular or warped assemblies it does not establish every geometric property.

For a small rectangular frame, you can also verify a right angle using a square. For a large site layout, the familiar three-four-five right triangle is a useful geometric construction: three units along one leg, four along the other, five between their endpoints. The construction follows the Pythagorean theorem. The precision depends on the actual measuring procedure, not on the elegance of the integers.

### Practice the disciplined sequence

Before you make a cut or drill, answer five questions. Which surface or line is the datum? What geometric relationship must the finished feature satisfy? Which tool can reveal that relationship to the accuracy required? Which direction is material removed or added? And what will you measure afterward to confirm the outcome?

Those questions change the work. You do not merely create individual dimensions; you build a connected geometry. And once the geometry has explicit references, errors become diagnosable. A crooked assembly is no longer “somehow off.” It has a misaligned datum, a measurement that was transferred from the wrong edge, a warped reference face, or a cutting process that failed to respect its intended boundary. Good layout turns guesswork into testable steps.

## Precision, Repeatability, and Calibration

Suppose you measure the thickness of a board with a digital caliper. The display reads nineteen point nine eight millimeters. You measure again: nineteen point nine eight. A third time: nineteen point nine eight. It is tempting to conclude that you know the thickness to one hundredth of a millimeter. But what if the jaws contain a tiny chip? What if the caliper reads two hundredths too high at every position? What if the board is compressed by the measuring force? Repetition has answered one question and left others open.

This is where the language of metrology, the study of measurement, becomes useful in ordinary workshop practice. Accuracy, precision, repeatability, resolution, calibration, and uncertainty are related, but they are not synonyms.

### Repeatability is agreement, not truth

Repeatability asks how closely successive measurements agree when the conditions are kept substantially the same: same object, procedure, instrument, operator, and short time interval. If the caliper reports almost the same result every time, it has good repeatability in those conditions. That tells us about spread. It does not tell us whether all the readings have a common error.

Precision is a broader idea about how closely results agree, with repeatability describing one specific condition. Accuracy concerns closeness to the quantity we intend to measure, but metrologists generally express accuracy qualitatively and quantify specific errors or uncertainties rather than promising an 'accuracy number' without context.

Resolution is different again. A display that changes in steps of one hundredth of a millimeter has fine resolution. It does not follow that the device's mechanical jaws, alignment, calibration, and user technique can support a decision at that scale. Additional digits can make a measurement look authoritative without reducing uncertainty.

### Errors have different personalities

Imagine cutting ten equal wooden spacers. Each should be thirty millimeters long. If the measured lengths scatter around thirty with a spread of half a millimeter, you have a repeatability problem in cutting or measuring. If every spacer is about thirty point five millimeters, you may have a consistent offset: the stop is misplaced, the reference edge is wrong, or the rule's zero is damaged. In the first case, you investigate variation. In the second, you investigate bias.

The distinction changes the remedy. Taking more readings can help estimate an average and reveal scatter. It cannot, by itself, remove a shared calibration error. Likewise, adjusting a stop can remove an offset while leaving a wandering saw fence or a flexing workpiece unchanged.

Error can enter at every stage: the reference surface, the fixture, the tool, the observer, the temperature, and the interpretation of the reading. For a long metal part, thermal expansion may be consequential when temperature differs substantially from the reference condition. For wood, moisture and grain can matter more. The tool is part of a measurement system; the object is not a perfectly inert number waiting to be displayed.

### What calibration actually provides

Calibration establishes a relationship between indications of an instrument and reference values, with stated conditions and associated uncertainties. It need not be a magic adjustment that makes a device perfect. A calibration may reveal that the caliper reads consistently high. That information can support correction, acceptance, or rejection for a particular task.

Traceability describes an unbroken, documented chain connecting a measurement result to an appropriate reference, with uncertainty contributions along the way. A calibrated instrument is not automatically suitable for every job. The required tolerance must be compared with the measurement process's uncertainty, which includes more than a manufacturer's display resolution.

For household layout, elaborate metrology may be unnecessary. A good reference square, a verified tape measure, and a stable setup are often appropriate. For machining a close fit or checking an engineered dimension, more careful control may be warranted. The point is to spend measurement effort in proportion to the consequences of getting the dimension wrong.

### Think in terms of a decision

Consider a part meant to fit within a slot that is ten millimeters wide. If the part measures nine point nine nine millimeters and your method has uncertainty of several tenths of a millimeter, the display does not establish that it will fit. A decision near the boundary is exactly where uncertainty matters most.

You could improve the method: clean the jaws, check the zero, use a known reference, measure at several points, reduce the applied force, control temperature, or use a different instrument. Sometimes the better solution is not a more accurate number but a trial assembly with enough clearance for real movement and manufacturing variation.

The same principle applies when a wall is out of square, a door rubs, or a pipe must pass through a tight opening. Measure the real condition at relevant locations. Do not let a single measurement stand in for an object that may be bowed, tapered, twisted, or moving.

### A field exercise in honest reporting

Choose a safe, simple object such as a stack of paper, a metal washer, or a piece of scrap wood. Measure it five times, removing and replacing the tool each time. Note the spread. Rotate the object and measure elsewhere. Check the instrument's zero and, if available, a known reference. Then describe the result without claiming more certainty than the setup earns.

You may find that the important variability is not in the display at all. It may be the object's shape or the force of your hand. This is the central lesson: a measurement is an interaction between a quantity, a reference, a method, and a purpose. The experienced craftsperson is not the one who always gives the most digits. It is the one who knows which digits deserve belief and what decision those digits can safely support.

## Measurement and Setup Plans for Multi-Step Repairs

Those references have to remain consistent across a repair containing several operations.

Picture a repair that requires drilling four mounting holes, trimming a panel, and aligning a new bracket to an old opening. Every individual cut may be accurate, yet the assembly can still fail to fit. The problem is not necessarily a poor ruler. It may be that the measurements came from different reference points, were taken under different conditions, or accumulated error in a chain.

A measurement plan starts by asking what must be true at the end. Does the bracket need to be centered visually, clear a moving part, line up with threaded holes, or hold a seal against a surface? Each is a different functional requirement. The useful tolerance may be generous in one direction and tight in another. You cannot choose a measuring method intelligently until you know what the measurement must accomplish.

### Establish a datum before taking dimensions

A datum is a reference from which dimensions or positions are defined. On a simple plate, an accessible straight edge and a chosen corner can be suitable workshop datums. On a crooked doorway, the floor or jamb may not be straight. A plumb or level line established independently may be a better design reference than copying every irregularity.

Suppose four holes are laid out by measuring successively from one hole to the next. Each placement can introduce a small error. The final hole's location is the sum of those errors. Instead, measure the positions from a common baseline, or use a template and verify its fit. This does not eliminate measurement uncertainty, but it makes it easier to detect and correct. The choice between matching an existing irregular feature and creating a new straight reference should be explicit.

### Separate resolution, accuracy, and repeatability

A digital caliper with a display reading hundredths of a millimeter does not guarantee results accurate to a hundredth. Resolution is the smallest change shown; accuracy concerns closeness to the true value within a defined measurement model; repeatability concerns how much readings vary under similar conditions. Tool condition, zero setting, jaw alignment, operator pressure, surface dirt, and temperature all matter. A tape measure that repeats consistently from the wrong reference can still produce a consistent but incorrect installation.

A useful quick check is to measure a dimension more than once using a different approach. Measure the whole span, then verify the remaining distance after placing a component. Measure the diagonals of a rectangular frame to check for skew, while recognizing that equal diagonals alone do not establish all geometric conditions in an arbitrary shape. Dry-fit the assembly before irreversible cutting when access permits.

### Work backward from the tightest fit

Say a cover panel must clear two fixed posts by at least two millimeters on each side. The opening is measured as five hundred millimeters across, but the posts are not perfectly parallel. The narrowest actual opening governs the maximum panel width, not the widest point. If you cut the panel to four hundred ninety-six millimeters without accounting for measurement uncertainty, edge straightness, and thermal or moisture movement, the nominal four-millimeter clearance could disappear at a tight spot. The correct plan identifies the critical location and the likely variation, then chooses a clearance that still works under those conditions.

Some dimensions must be transferred directly. If existing anchor positions cannot be measured reliably from a wall corner, a rigid template or transfer punch may outperform repeated tape measurements. A template should have a defined orientation, a label for its reference face, and a way to prevent mirror reversal. For a repeating setup, a jig converts variable human positioning into a constrained operation, but the jig itself needs verification.

### Design the sequence to preserve access

Work is often made harder by measuring in the wrong order. Before removing a bracket, measure the offset that will disappear when the bracket is gone. Before cutting a wall opening, document concealed-service assumptions and establish a safe investigation plan. Before placing a sealant joint, ensure the mating surfaces have been prepared and the dry-fit is correct; a wet sealant bead is not the moment to discover the part is backwards.

An effective job sheet has five elements: the required final function, chosen datums, critical dimensions with tolerances, setup and inspection steps, and a decision point before irreversible operations. It also identifies what remains unknown. A measurement written as “about six inches” might be suitable for planning material quantities, but not for positioning a latch hole. Precision should follow consequence.

### Use checkpoints, not a long blind sequence

Make a pilot part, a test cut, or a temporary assembly where the cost of correcting an error is low. Check drilling perpendicularity if the mating hardware is sensitive to tilt. Verify the first hole before drilling the rest. Confirm that the finished part actually performs its function, rather than merely matching the drawing. A panel may fit but bind after humidity rises; a bracket may align but leave insufficient clearance for the moving load.

Measurement is not a ceremony performed before real work. It is a feedback system: define a target, observe the actual geometry, act, and verify the result. A thoughtful setup lets ordinary tools produce reliable work because each operation has a defined reference and a chance to catch mistakes before they propagate.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Measure First, Then Shape: Error, Reference Surfaces, and Tool Choice

**Track:** Tools, Measurement, and Workmanship. **Background:** Arithmetic and basic geometry. **Purpose:** explain why accurate practical work starts with references, measurement plans, and controlled error rather than a shopping list of tools.

#### Technical companion

**Worked geometry:** For an ideal rectangle with side lengths `a` and `b`, each diagonal has length `sqrt(a² + b²)`. Matching diagonals test rectangularity *when the opposite-side and planarity conditions are already established*; the test is not sufficient for every quadrilateral.

**Measurement record template:** desired dimension; selected datum; instrument and resolution; measurement locations; estimated uncertainty; fit allowance; independent check; observed finished dimension; any systematic discrepancy.

**Evidence map:** NIST's measurement-uncertainty materials distinguish measurement results from confidence and calibration; USDA's *Wood Handbook*, Chapter 8, treats fastening in wood including substrate and connector behavior. Neither source sets universal cutting clearances or universal screw torques.

**Hands-on practice:** Measure a piece of scrap from two different datums, mark a waste side, make a controlled cut, and measure the finished piece. Document error instead of judging by appearance alone. Appropriate tool guards, stable work holding, and manufacturer instructions remain part of the actual operation.

### Reference Faces, Datums, and Practical Layout

**Track:** Tools and Measurement. **Background:** Measurement error and tool choice. **Purpose:** develop a systematic approach to transferring dimensions into accurate physical work.

#### Technical companion: reference chain and checks

**Layout model:** Nominal feature positions `x_i = x_datum + i*pitch`. Incremental method `x_i = x_{i-1}+pitch+e_i` can accumulate systematic errors. Datum-referenced positions `x_i = x_datum+i*pitch+e_i` still share a datum error but do not cumulatively depend on previous mark errors. For a rectangular frame with sides `a,b`, diagonal length should approximate `sqrt(a²+b²)` under planar, right-angle assumptions.

**Distinctions:** Repeatability is not accuracy; resolution is not calibration; flatness is not parallelism; square-to-a-face is not square-to-the-universe. Formal metrology uses traceability, uncertainty and specified tolerances; field layout uses the same underlying ideas at a different precision.

**Exercise:** On paper, dimension a five-hole pattern two ways: as chained spacings and from one datum. List which errors affect one hole and which affect all holes. Then design a physical template or story stick to transfer the pattern.

**References:** NIST guidance on uncertainty and geometric measurement; shop practice examples are illustrative, not prescribed by NIST. Consult tool manufacturer's documented accuracy and calibration method before claiming quantitative precision.

#### Selected reading and evidence (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Torque and perpendicular moment arm.

### Precision, Repeatability, and Calibration

**Track:** Tools, Measurement, and Workmanship. **Background:** Reference faces and layout. **Purpose:** distinguish an apparently exact number from a trustworthy measurement.

#### Technical companion (non-spoken)

##### Vocabulary and example

- **Repeatability:** agreement under specified repeatability conditions.
- **Bias:** systematic component of measurement error; not estimated by repeated readings alone.
- **Resolution:** smallest displayed increment; not a complete uncertainty budget.
- **Calibration:** documented relation of instrument indications to reference quantity values.
- **Traceability:** linked chain to references with uncertainty at each step.
- **Uncertainty:** parameter describing dispersion of values attributable to a measurand, given a model and observations.

An illustrative set of readings `30.2, 30.0, 30.1, 29.9, 30.3 mm` has mean `30.1 mm` and sample standard deviation about `0.16 mm`. Neither result proves the absence of a `+0.5 mm` systematic offset. This is an example of repeatability assessment, **not** a complete calibration or valid task-specific acceptance rule.

##### Source and practice distinctions

NIST's technical terminology distinguishes repeatability, calibration, and measurement uncertainty. Ordinary shop references have varying quality and need not be compared using one universal uncertainty ratio. Any dimensional acceptance rule must account for fit, function, the actual tolerance specification, and measurement risk.

#### Selected reading and claim sources (non-spoken)

- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.

### Measurement and Setup Plans for Multi-Step Repairs

### 012000 — Measurement and Setup Plans for Multi-Step Repairs

#### Technical companion (non-spoken)

##### Example plan: four-hole mounting plate

| Step | Datum / tool | Acceptance observation |
|---|---|---|
| Establish horizontal reference | Verified level or laser plus reference mark | Independent line retained after hardware removal |
| Record existing anchor positions | Tape, combination square, transfer method | Duplicate measurements agree within planned tolerance |
| Prepare template | Rigid stock labeled FRONT and TOP | Dry-fit reproduces all four target positions |
| Make pilot holes | Center punch and pilot drill | Pilot locations check against template |
| Fit assembly | Temporary fasteners | Clearance, load direction and moving components verified |

**Uncertainty example:** If two independent position errors are each bounded by ±1 mm, a worst-case relative separation error can be ±2 mm. Root-sum-square combinations require an uncertainty model and assumptions; do not blindly substitute them for worst-case fit decisions.

**Editorial boundary:** Measurement practice is separate from determining structural capacity, electrical clearances, pressure ratings or other application-specific acceptability. Hold points before cutting and drilling must include identification of concealed utilities and required protective measures.

#### Selected reading and evidence records (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
