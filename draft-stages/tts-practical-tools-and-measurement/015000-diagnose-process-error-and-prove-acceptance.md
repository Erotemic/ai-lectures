# Diagnose process error and prove acceptance

<!-- BEGIN SPOKEN LECTURE -->

# Diagnose process error and prove acceptance

## Diagnosing Tool Runout, Vibration, and Repeatability

A drill press makes a hole that is visibly larger than the drill bit. A router leaves ripples on the edge of a board. A saw that once cut cleanly starts producing an irregular surface. Before deciding to buy a new machine, we should ask what is actually moving. The bit may not be centered; the spindle may be deflecting; the stock may be vibrating; the cutting edge may be worn; or the measurement may be inconsistent. These faults can look alike in finished work, but they require different tests.

### What runout means

Imagine rotating a perfectly straight cylinder whose centerline is offset from the machine's true rotation axis. A fixed indicator touching its surface would move in and out once each revolution. That motion is radial runout. End-face wobble is axial runout. Toolmakers commonly report the total indicated runout, abbreviated TIR, meaning the difference between the maximum and minimum dial readings over the measurement cycle. For an ideal round, rigid, off-center cylinder under simple conditions, the eccentricity is one half of the total indicator change. A real drill chuck, arbor, or workpiece may not be round or rigid, so this shortcut is not a general diagnosis.

Runout can be introduced at several interfaces. A good spindle may carry a dirty taper. A clean taper may hold a damaged chuck. A sound chuck may grip a bent drill. If we measure only at the drill tip, we have measured the combined effect of every upstream interface and the tool itself. That is a useful symptom measurement, but it does not tell us which part is responsible.

To isolate a fault, work from the reference structure outward. Check the spindle or arbor surface that the machine specification identifies as a measuring location; then check the mounted chuck or holder, and then the tool shank. Use the same indicator orientation and controlled rotation for comparisons. Unplug or isolate the machine before setup and rotate by hand only when the machine design permits it. A dial indicator should not be placed into a powered cutting operation just because we want a more realistic measurement.

### Runout is not the same as deflection

A rotating tool also bends under cutting force. Imagine a long, thin drill entering a hard surface at a shallow angle. Even with its shank centered perfectly, the tip may walk or bow. The workpiece can move if it is not clamped, and the table can move if joints are loose. That movement produces errors during cutting which are not present during a slow hand-rotation indicator test.

Think of the machine as a chain of stiffnesses: foundation, frame, table, clamp, workpiece, bearing, holder, and tool. Under load, each element deflects. The least stiff member can dominate the result. A long drill extends farther from its holder and generally bends more easily than the same diameter supported close to the work. Adding a powerful motor to a flexible setup does not improve its accuracy.

Now consider a router producing a periodic washboard finish. If the ripple spacing changes with feed speed but the spindle speed remains fixed, the pattern may follow tool rotation or tooth engagement. If the pattern occurs at a particular machine speed even while the tool is cutting lightly, structural resonance could be involved. An uneven cutting edge, chipped tooth, or poorly balanced accessory can also create forcing at rotation frequencies. We should record the circumstances rather than infer a particular cause from the appearance alone.

### Separate repeatability from accuracy

A machine might cut ten parts to the same wrong length. That is repeatable but inaccurate. It might also cut ten parts that scatter around the desired dimension. Then the variation itself is a problem. The distinction matters because the next experiment differs. A fixed offset suggests calibrating a scale, fence, or datum. Scatter suggests workholding, play, thermal effects, operator technique, material changes, or a drifting stop.

Repeated measurements should be made under comparable conditions: same reference face, similar clamping, tool temperature, measurement instrument, and feed procedure. Re-seat the tool or workpiece deliberately between trials if the question is about setup repeatability. Take a second sequence without re-seating if the question is whether the system remains stable during operation. If those two sets have very different spread, the act of locating the work may be the weak link.

We should not mistake the indicator's number of decimal places for proof of a fine result. A measurement has limits imposed by indicator resolution, contact angle, reference surface quality, operator pressure, and thermal drift. A simple repeatability study may find that the measurement method itself varies enough to hide the improvement we hoped to see. Compare several readings of a known stable reference before interpreting small differences on the machine.

### A fault-isolation sequence

Suppose a drill press makes holes about half a millimeter oversize. First confirm the hole diameter with a suitable instrument rather than relying on a nominal drill label or a visually rough exit edge. Inspect the bit for bend, chipped lips, and unequal geometry. Check the workholding and entry surface. Observe spindle, holder, and shank runout separately, using the measurement procedure appropriate to that machine. Compare a short, sound bit with the original long bit. Finally, make a controlled test hole in a representative material and document feed, speed, work support, and result.

Notice the order. We have changed one factor at a time, and every observation constrains possible causes. If the spindle's indicated motion is small but the long bit visibly wanders under load, replacing spindle bearings would be premature. If the indicator changes markedly after re-seating the chuck, an interface problem becomes more plausible. If a new bit improves the result without any machine change, cutting geometry or tool condition deserves attention.

Some vibration is an immediate stop signal: sudden shaking, a cracked abrasive wheel, a loose blade, or a damaged guard is not a data-collection opportunity. Isolate power and inspect before restarting. Diagnosis is a controlled experiment only when the setup is itself controlled.

The goal is not to make every tool metrology-grade. It is to know what accuracy the job requires, which error source is dominant, and what observation would establish that a repair worked. Good measurement avoids both needless replacement and unjustified confidence.

## Quality Control and Reference Standards for Home Workshops

A repeatability problem needs a reference against which both the tool and the measurement process can be judged.

A shelf bracket looks square. You cut four identical spacers, and all four appear to measure the same. Yet the shelf tilts when installed. A workshop needs a way to separate a single mistake from a repeated mistake built into the measuring method. That is the purpose of quality control. It is not a certificate hanging over the bench. It is the practice of deciding which features matter, measuring them consistently, and knowing how trustworthy the result is.

### Three things a measurement can do wrong

First, a result can scatter. Measure the same board five times, with the same ruler and nominal method, and you may get slightly different readings. That is limited repeatability. Second, results can be consistently offset: a tape hook is bent, the rule's zero edge is worn, or the square is not truly square. Repeating the error ten times will not remove that bias. Third, you may be measuring the wrong feature. The inside width of a cabinet opening can change with height; a single reading at the bottom does not represent the space where a shelf must slide.

These are different failures. Better technique can reduce scatter. A check against a reliable reference can reveal bias. A better measurement plan can catch differences across the actual object. Buying a more expensive digital instrument is often not the first repair. A digital caliper reporting hundredths of a millimeter does not guarantee hundredth-millimeter accuracy on a rough, compressible, warm piece of timber.

A reference standard is an object or instrument against which a measurement system can be checked. In a professional metrology laboratory, calibrations and uncertainty are connected to traceable reference chains. In a home workshop, we may not need that level of formality, but we still need honest language: a shop-made gauge can confirm that parts agree with one another; it does not automatically establish their absolute dimension. A known reference block, a verified rule, or a certified square has a different evidentiary role from a plywood offcut that happens to fit.

### Design a check that reveals the error

Take a carpenter's square and place its stock against the straight edge of a board. Draw a line along its blade. Flip the square over against the same edge and draw a second line from the same origin. If the lines diverge, the square or reference edge deserves investigation. The comparison amplifies angular error. It does not measure exact angular deviation until the geometry and line widths are accounted for, but it is far more informative than looking at the tool.

For a repetitive operation, build a go/no-go gauge. Suppose ten shelves must fit between two faces. Rather than dial a measuring tool for each shelf and accumulate marking errors, make a gauge that embodies the maximum permitted length and another that embodies the minimum. A shelf that violates either bound is rejected or reworked. The critical step is establishing those bounds from the actual assembly, allowing for finish, movement, and clearance. Precision in production without a correct target is simply consistent wrongness.

If the project uses parts that must interchange, do not compare each new part against the previous part. That creates a chain in which errors accumulate. Return every part to the same reference face, stop block, or master. Periodically check the master itself. A stop block can loosen during repeated cuts; a bit can shift; sawdust under a workpiece can change the cut. The very consistency that makes a jig effective also allows a moved jig to spoil many parts before anyone notices.

### Decide what tolerance actually matters

A cabinet door may care about the gap at its visible edges, the position of a hinge cup, and the amount of clearance for movement. It may not care whether a hidden blocking piece is one millimeter longer than nominal. A tolerance is not an ornament attached to every dimension. It is an allowance chosen from function, material behavior, and the ability to manufacture and inspect reliably.

Consider a box made from four cut panels. If each panel length is independently high by a small amount, the final outside dimension may be wrong even though no individual panel looks defective. Conversely, deliberate matching or trimming at assembly can absorb some variation. The important question is which dimensions stack through the geometry and which are controlled by fitting during assembly. Write down the critical dimension chain before making parts.

Temperature and humidity can matter. Steel rules change length slightly with temperature; wooden components can change much more with moisture, and differently along different grain directions. If you measure a shelf blank on a damp day and later fit it into a very dry cabinet, the material behavior may dominate your caliper's display resolution. Control conditions where practical, or allow movement by design.

### Make evidence easy to reproduce

For a recurring job, record the datum, gauge or tool used, nominal value, allowable range, and measurement point. Write down the date and conditions when they could change the interpretation. Use a simple check sheet: first part, representative middle part, final part. When a process drifts, those samples help identify when it began. A photograph can show a layout but should include a visible reference and avoid misleading perspective.

Quality control also means refusing false certainty. A level can establish orientation relative to gravity, not whether a wall is geometrically straight. A laser can give a stable plane, but its mounting can move. A temperature sensor can be consistent while reading the temperature of the surface it is touching rather than the air we care about. Choosing the correct measurement model is a form of workmanship.

The workshop is most reliable when every operation has a reference and every important result has a way to be checked independently. The goal is not to collect the most digits. It is to make errors visible early enough that they are still cheap to correct.

## Diagnostic Measurements Under Load and Over Time

A machine starts perfectly on a workbench and stops as soon as it is asked to do real work. A pump hums when its switch is thrown but produces little water. A battery reports a healthy voltage until a motor tries to start. The measurement that matters is often not the one that is easiest to take. We need to observe a system under the conditions that make its defect appear, and sometimes over enough time to capture an intermittent event.

### No-load readings do not measure capacity

Think of a battery connected to a motor. An open-circuit voltmeter draws very little current. A weak connection or depleted battery may therefore show a familiar voltage. When the motor starts, the current demand rises. The internal resistance of the battery and the resistance of cable contacts produce voltage drops. The motor sees less voltage than expected and may stall. The important observation is the voltage at the load *while* the load attempts to run, interpreted using the manufacturer's expected range and the circuit's ratings.

The same distinction appears in fluid systems. A pressure gauge connected to a closed outlet may read normal, but flow through a restriction can cause a large pressure difference once the valve opens. In air systems, a fan may generate pressure without delivering the intended flow through a clogged filter. In mechanics, a shaft can turn freely without a workpiece yet vibrate or slip when torque is applied. Measurements under realistic operating conditions reveal the resistance and energy losses that static inspection misses.

This does not mean making the system work at any cost. A load test must be designed around known ratings, guarding, safe fixtures, and stable conditions. Do not use a jammed workpiece as a substitute for a calibrated brake, or short a battery to 'see if it has power.' A useful diagnostic load resembles normal service without inviting a new failure.

### Measure the right quantity at the right location

A meter placed across a motor's terminals answers a different question from a meter placed across the battery. If the motor terminal voltage collapses but the source voltage remains stable, the wiring or connections between them deserve inspection. Similarly, measuring pressure before and after a filter distinguishes filter restriction from low inlet supply better than a single reading. Measuring temperature at the motor housing alone does not tell you whether the source is bearing friction, winding losses, poor cooling, or a nearby heater.

Every instrument also changes or filters what it reports. A digital multimeter may update only a few times per second and miss a brief starting transient. A cheap temperature logger may have a large response delay. A clamp meter may have an accuracy range that excludes the small current you are trying to measure. An infrared thermometer observes emitted radiation and can be badly misled by a reflective metal surface. The useful question is not just 'What number did I read?' but 'What did the sensor actually measure, with what bandwidth and uncertainty?'

The simplest protection against a misleading measurement is to record location, time, operating condition, instrument, units, and a reference value. 'Voltage 11.1' is incomplete. '11.1 volts at motor terminals during a normal start attempt, measured on this meter, while the supply was 12.3 volts' is evidence that can be acted upon.

### Intermittent faults require time as an axis

Imagine a pump that trips after twenty minutes, cools, and starts again. A single measurement taken during its first minute may be completely normal. You need a timeline of current, temperature, inlet or outlet condition, duty cycle, and any trip signal. Samples every five minutes might show gradual heating but miss a one-second pressure surge. High-frequency capture is not always necessary; select a sampling interval that can reveal the hypothesized phenomenon.

Event logs can provide another view. A controller reporting overcurrent at a precise time does not prove the motor is defective. The event could follow a jam, poor lubrication, mechanical binding, a voltage sag, or faulty sensing. Correlate the fault timestamp with what the equipment was doing and what other measurements changed. A clock that drifts across devices can make an apparently causal sequence impossible to trust, so synchronize time or explicitly record timing uncertainty.

Repeating the same test is powerful only if conditions are comparable. Ambient temperature, workpiece mass, fluid level, battery state, and operator technique may all change. A test repeated after the machine cools cannot automatically be compared to one performed immediately following sustained operation.

### Design a discriminating test

Suppose a drill makes an oversize hole. Three competing hypotheses are tool runout, a worn bit, and the workpiece shifting. An unloaded indicator measurement at the spindle may help test runout. Inspecting the bit and checking fixture movement under cutting force test the others. An unloaded spindle number alone does not establish the actual hole diameter; cutting forces, material, feed, and fixture stiffness matter. A good sequence targets the hypothesis most likely to explain the observed failure and controls the other variables.

Now consider a hose that delivers a trickle despite a normal static gauge reading. If you can make a safe rated test, measure flow and dynamic pressure before and after the suspected restriction. The change in pressure with flow can reveal where resistance concentrates. Again, a static measurement is part of the picture but not a verdict.

The craft is to treat a number as an observation with boundaries, not as a diagnosis. Ask what changes when the equipment is working, where energy is lost, how long the failure takes to emerge, and what measurement would separate competing explanations. The best measurement is often the one collected at the precise instant and location where the defect affects performance.

## Go/No-Go Fixtures and Repeatable Acceptance Tests

Acceptance fixtures turn that reference into a repeatable decision about the finished result.

A measurement can look impressively precise and still fail to answer the important question. Suppose you are building six wooden drawer fronts. A digital caliper reports the first one as 149.86 millimeters wide. That number tells you something about one place on one part under one measuring condition. What you actually need to know is whether every drawer front fits its opening, clears its neighbors, and stays aligned when the hardware is installed. Sometimes the best measurement instrument for that question is a carefully made object that simply fits or does not fit.

### From nominal dimension to acceptance condition

A drawing might specify a width of one hundred fifty millimeters, plus or minus half a millimeter. The nominal width is not the only acceptable width. The interval from one hundred forty-nine point five to one hundred fifty point five is the stated range. Two different parts inside that range may still behave differently when combined with errors in their mating parts. This is why tolerances have to be considered as an assembly, not only as isolated dimensions.

A go gauge tests whether a feature meets the side of a tolerance that matters for passage or fit. A no-go gauge tests whether it has crossed the other limit. For a hole, a go pin represents the minimum acceptable opening: it should enter under the specified test conditions. A no-go pin represents an excessive opening: it should not enter. For a shaft, the mating ideas reverse. The details of accepted gauging practice depend on the geometry, standard, and whether form errors must be evaluated, but the reasoning is transferable. Instead of repeatedly reading a display, you test a boundary of acceptability.

Think of a plywood template used to confirm the location of bolt holes. If the template is dimensionally stable and referenced to the same datum surfaces as the real assembly, it can expose a hole-location error quickly. But if you place it by eye against a rough edge, the test is not repeatable. The definition of where the measurement begins matters as much as the shape of the gauge.

### A datum is an agreed reference

Suppose a board is slightly bowed. Measuring each hole from whichever nearest edge looks straight gives inconsistent results. Choose a designated reference edge and face, mark them clearly, and maintain that reference through layout, cutting, drilling, and inspection. This avoids a chain of accumulated measurements. It also makes a failure interpretable: when a bracket does not fit, you can tell whether the hole pattern shifted or the entire part was positioned incorrectly.

There is a difference between precision and suitability. A steel gauge may be accurate when calibrated but wrong for a soft wooden piece that compresses under a strong hand. A paper template may accurately locate holes but change size with moisture. A 3D-printed test fixture may be quick to reproduce yet shrink or warp when printed with a new material or orientation. Choose a fixture whose uncertainty is comfortably smaller than the decision boundary, and which does not damage the part during the test.

A useful shop exercise is to make two reference blocks representing the minimum and maximum acceptable shelf clearance. Test several shelves without reading any numbers. Then measure the blocks and a few shelves independently. If the two methods disagree, investigate burrs, board bow, reference choice, temperature, compression, and gauge wear rather than trusting whichever tool has more digits.

### Repeatability is part of the instrument

Imagine five people testing the same cabinet door with a feeler gauge. One presses hard; another just touches the gap. One measures at the hinge side with the door unloaded; another measures when the latch has been pulled tightly closed. The variation is not a minor inconvenience. It can determine whether a supposedly objective acceptance test passes or fails.

Define the test procedure: which reference surfaces are used, where the gauge is placed, what force or insertion behavior counts, whether the part is at room temperature, and whether the assembly is supported in its installed orientation. Record repeated results for the same operator and between operators where the decision is consequential. If the result changes when the tester changes, the procedure or gauge requires improvement.

A go/no-go result is binary, but the underlying dimensions are continuous. That has advantages and costs. It speeds production and prevents argument over harmless digit differences. Yet it hides how close a passing part is to failure. For a critical process, sample numerical measurements as well. If every part barely passes and the process is drifting, the next batch may fail. Acceptance testing and process monitoring solve related but different problems.

### Test the assembled function

Some failures cannot be reduced to one geometric width. A drawer might fit its opening yet bind when loaded because the slides are not parallel. A clamp might close without developing adequate holding force. A cabinet might be square on the bench but twist after fastening to a wall. These require functional acceptance tests under a realistic load or installed condition.

Design a test around the failure you are trying to prevent. For a removable service panel, that may mean open and close it ten times with the specified tool, check for fouling, then inspect the sealing surface for compression and damage. For a jig that drills repeated holes, it may mean drilling scrap samples and checking whether a real fastener enters without forcing. Include the likelihood of a false pass and a false fail. A gauge that is slightly loose may accept bad parts; one that is worn or bent may reject good ones.

Use known standards when applicable. A fixture should not create an excuse to improvise acceptance rules for a structural fastener, pressure connection, electrical part, or safety device. Those systems have their own certified tests, tolerances, and inspection procedures. A home-made gauge is most useful when the decision is well-defined and its limits are understood.

The central shift is from asking, 'How finely can I measure this?' to asking, 'What outcome must I distinguish reliably?' Once the acceptance condition is clear, you can select a measuring method that is fast, repeatable, and relevant to how the object will actually be used.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Diagnosing Tool Runout, Vibration, and Repeatability

### 015000 — Diagnosing Tool Runout, Vibration, and Repeatability

#### Technical companion (non-spoken)

##### Diagnostic matrix

| Symptom | Candidate cause | Discriminating test |
|---|---|---|
| Dial reading changes with spindle rotation | Rotating geometry / mounting | Measure at spindle, holder, and sound reference shank separately |
| Accurate without cutting, poor under load | Bending or work motion | Shorter overhang; supported fixture; compare unloaded vs test work |
| Constant dimensional bias | Offset datum or calibration | Compare against independent traceable reference |
| Variation after every re-clamp | Re-seating / fixture locating | Alternate fixed-clamp and re-clamped batches |
| Speed-specific vibration | Resonance or rotating forcing | Record speed dependence; inspect tooling and guarding first |

##### Measurement note

`TIR = max(indicator) − min(indicator)`. `eccentricity = TIR/2` applies only in an idealized rigid, round, eccentric model. It is not a general formula for bent shafts, lobing, tilted faces, or dynamic cutting error.

**Machine boundary:** Measurement points, allowable runout, bearing clearance, safe hand-rotation, and corrective methods are machine-specific. Never bypass guards or test a visibly unstable powered setup.

#### Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `osha-drill-press` — [OSHA, Woodworking eTool — Drill Presses](https://www.osha.gov/etools/woodworking/production/machines-tools/drill-press). Clamping stock, twist hazards and drill press operational constraints.

### Quality Control and Reference Standards for Home Workshops

### 016000 — Quality Control and Reference Standards for Home Workshops

#### Technical companion (non-spoken)

**Measurement vocabulary:** repeatability (scatter under similar conditions), bias (systematic offset), resolution (smallest indicated increment), uncertainty (qualified range of plausible values), datum (reference feature), tolerance (allowable functional variation). No assumption that `resolution = accuracy`.

**Three checks:** (1) flip a square against a verified straightedge; (2) inspect a short reference length at several points of a tape or rule; (3) compare a first, middle, and last part to an independent master, not sequentially to each other.

**Example control plan:** shelf opening measured at front/back and top/bottom; derive a clearance allowance for hardware and wood movement; record the gauge used, target, acceptable interval, and rejected pieces. A shop gauge is a *transfer reference* unless its absolute dimension is verified.

**Scope:** Professional calibration traceability, uncertainty budgets and certified inspection require established reference procedures appropriate to the industry; the methods here illustrate workshop control, not accredited calibration.

#### Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.

### Diagnostic Measurements Under Load and Over Time

### 017000 — Diagnostic Measurements Under Load and Over Time

#### Technical companion (non-spoken)

**Electrical example:** If a source is 12.4 V under load and terminals at an intended 5 A load are 11.6 V, the total series drop is 0.8 V and effective path resistance is about 0.16 ohm at that operating point. This is a model illustration, not an acceptance limit. Confirm voltage and current concurrently; actual circuits can vary dynamically.

**Fluid example:** Compare pressure upstream and downstream of a restriction only while measurable flow exists. When flow goes to zero, friction loss often approaches zero even if the restriction remains severe.

**Logging record:** timestamp with timezone, instrument ID/calibration, units, location, ambient condition, load/duty, event notes, expected tolerance, uncertainty. A chart needs both the signal and enough event context to interpret it.

**Safety/limitations:** Work within instrument category ratings and equipment manufacturer limits. Electrical measurements near mains or exposed conductors require qualified procedures and suitable probes; load tests must not defeat guards, interlocks, relief devices, or overcurrent protection. Don't improvise high-energy tests.

#### Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Torque and perpendicular moment arm.

### Go/No-Go Fixtures and Repeatable Acceptance Tests

### 018000 — Go/No-Go Fixtures and Repeatable Acceptance Tests

#### Technical companion (non-spoken)

**Example tolerance.** Feature specification 150.0 ± 0.5 mm gives limits 149.5 and 150.5 mm; gauge design must account for its own tolerance, wear, temperature, and the acceptance standard. The raw drawing interval does not automatically specify exact go/no-go gauge dimensions.

**Repeatability trial.** Five operators each test three parts twice in randomized order. Record pass/fail, gauge ID, orientation, applied method, and whether part dimensions were near the threshold. Investigate disagreements rather than voting them away.

**Acceptance plan.** Define characteristic, physical failure it predicts, datum, test condition, instrument or fixture, decision limits, retest procedure, traceability, and log format. Identify false-pass consequences.

**Limitations.** Design rules differ for holes, shafts, flatness, form, and assemblies. Some features require geometric tolerancing or calibrated instruments rather than informal gauges. NIST uncertainty and repeatability guidance provide the measurement framework; safety-critical product standards take precedence.

#### Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `usda-fasteners` — [USDA Forest Service, Wood Handbook (2021)](https://research.fs.usda.gov/fpl/wood-handbook). Chapter 8: fastening; Chapters 4–5: wood properties.
