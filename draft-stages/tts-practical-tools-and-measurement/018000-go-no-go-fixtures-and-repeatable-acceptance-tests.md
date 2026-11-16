# 018000 — Go/No-Go Fixtures and Repeatable Acceptance Tests

<!-- BEGIN SPOKEN LECTURE -->

A measurement can look impressively precise and still fail to answer the important question. Suppose you are building six wooden drawer fronts. A digital caliper reports the first one as 149.86 millimeters wide. That number tells you something about one place on one part under one measuring condition. What you actually need to know is whether every drawer front fits its opening, clears its neighbors, and stays aligned when the hardware is installed. Sometimes the best measurement instrument for that question is a carefully made object that simply fits or does not fit.

## From nominal dimension to acceptance condition

A drawing might specify a width of one hundred fifty millimeters, plus or minus half a millimeter. The nominal width is not the only acceptable width. The interval from one hundred forty-nine point five to one hundred fifty point five is the stated range. Two different parts inside that range may still behave differently when combined with errors in their mating parts. This is why tolerances have to be considered as an assembly, not only as isolated dimensions.

A go gauge tests whether a feature meets the side of a tolerance that matters for passage or fit. A no-go gauge tests whether it has crossed the other limit. For a hole, a go pin represents the minimum acceptable opening: it should enter under the specified test conditions. A no-go pin represents an excessive opening: it should not enter. For a shaft, the mating ideas reverse. The details of accepted gauging practice depend on the geometry, standard, and whether form errors must be evaluated, but the reasoning is transferable. Instead of repeatedly reading a display, you test a boundary of acceptability.

Think of a plywood template used to confirm the location of bolt holes. If the template is dimensionally stable and referenced to the same datum surfaces as the real assembly, it can expose a hole-location error quickly. But if you place it by eye against a rough edge, the test is not repeatable. The definition of where the measurement begins matters as much as the shape of the gauge.

## A datum is an agreed reference

Suppose a board is slightly bowed. Measuring each hole from whichever nearest edge looks straight gives inconsistent results. Choose a designated reference edge and face, mark them clearly, and maintain that reference through layout, cutting, drilling, and inspection. This avoids a chain of accumulated measurements. It also makes a failure interpretable: when a bracket does not fit, you can tell whether the hole pattern shifted or the entire part was positioned incorrectly.

There is a difference between precision and suitability. A steel gauge may be accurate when calibrated but wrong for a soft wooden piece that compresses under a strong hand. A paper template may accurately locate holes but change size with moisture. A 3D-printed test fixture may be quick to reproduce yet shrink or warp when printed with a new material or orientation. Choose a fixture whose uncertainty is comfortably smaller than the decision boundary, and which does not damage the part during the test.

A useful shop exercise is to make two reference blocks representing the minimum and maximum acceptable shelf clearance. Test several shelves without reading any numbers. Then measure the blocks and a few shelves independently. If the two methods disagree, investigate burrs, board bow, reference choice, temperature, compression, and gauge wear rather than trusting whichever tool has more digits.

## Repeatability is part of the instrument

Imagine five people testing the same cabinet door with a feeler gauge. One presses hard; another just touches the gap. One measures at the hinge side with the door unloaded; another measures when the latch has been pulled tightly closed. The variation is not a minor inconvenience. It can determine whether a supposedly objective acceptance test passes or fails.

Define the test procedure: which reference surfaces are used, where the gauge is placed, what force or insertion behavior counts, whether the part is at room temperature, and whether the assembly is supported in its installed orientation. Record repeated results for the same operator and between operators where the decision is consequential. If the result changes when the tester changes, the procedure or gauge requires improvement.

A go/no-go result is binary, but the underlying dimensions are continuous. That has advantages and costs. It speeds production and prevents argument over harmless digit differences. Yet it hides how close a passing part is to failure. For a critical process, sample numerical measurements as well. If every part barely passes and the process is drifting, the next batch may fail. Acceptance testing and process monitoring solve related but different problems.

## Test the assembled function

Some failures cannot be reduced to one geometric width. A drawer might fit its opening yet bind when loaded because the slides are not parallel. A clamp might close without developing adequate holding force. A cabinet might be square on the bench but twist after fastening to a wall. These require functional acceptance tests under a realistic load or installed condition.

Design a test around the failure you are trying to prevent. For a removable service panel, that may mean open and close it ten times with the specified tool, check for fouling, then inspect the sealing surface for compression and damage. For a jig that drills repeated holes, it may mean drilling scrap samples and checking whether a real fastener enters without forcing. Include the likelihood of a false pass and a false fail. A gauge that is slightly loose may accept bad parts; one that is worn or bent may reject good ones.

Use known standards when applicable. A fixture should not create an excuse to improvise acceptance rules for a structural fastener, pressure connection, electrical part, or safety device. Those systems have their own certified tests, tolerances, and inspection procedures. A home-made gauge is most useful when the decision is well-defined and its limits are understood.

The central shift is from asking, 'How finely can I measure this?' to asking, 'What outcome must I distinguish reliably?' Once the acceptance condition is clear, you can select a measuring method that is fast, repeatable, and relevant to how the object will actually be used.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Example tolerance.** Feature specification 150.0 ± 0.5 mm gives limits 149.5 and 150.5 mm; gauge design must account for its own tolerance, wear, temperature, and the acceptance standard. The raw drawing interval does not automatically specify exact go/no-go gauge dimensions.

**Repeatability trial.** Five operators each test three parts twice in randomized order. Record pass/fail, gauge ID, orientation, applied method, and whether part dimensions were near the threshold. Investigate disagreements rather than voting them away.

**Acceptance plan.** Define characteristic, physical failure it predicts, datum, test condition, instrument or fixture, decision limits, retest procedure, traceability, and log format. Identify false-pass consequences.

**Limitations.** Design rules differ for holes, shafts, flatness, form, and assemblies. Some features require geometric tolerancing or calibrated instruments rather than informal gauges. NIST uncertainty and repeatability guidance provide the measurement framework; safety-critical product standards take precedence.

## Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `usda-fasteners` — [USDA Forest Service, Wood Handbook (2021)](https://research.fs.usda.gov/fpl/wood-handbook). Chapter 8: fastening; Chapters 4–5: wood properties.
