# 003000 — Precision, Repeatability, and Calibration

**Track:** Tools, Measurement, and Workmanship. **Background:** Reference faces and layout. **Purpose:** distinguish an apparently exact number from a trustworthy measurement.

<!-- BEGIN SPOKEN LECTURE -->

# The Number on the Tool Is Not the Whole Measurement

Suppose you measure the thickness of a board with a digital caliper. The display reads nineteen point nine eight millimeters. You measure again: nineteen point nine eight. A third time: nineteen point nine eight. It is tempting to conclude that you know the thickness to one hundredth of a millimeter. But what if the jaws contain a tiny chip? What if the caliper reads two hundredths too high at every position? What if the board is compressed by the measuring force? Repetition has answered one question and left others open.

This is where the language of metrology, the study of measurement, becomes useful in ordinary workshop practice. Accuracy, precision, repeatability, resolution, calibration, and uncertainty are related, but they are not synonyms.

## Repeatability is agreement, not truth

Repeatability asks how closely successive measurements agree when the conditions are kept substantially the same: same object, procedure, instrument, operator, and short time interval. If the caliper reports almost the same result every time, it has good repeatability in those conditions. That tells us about spread. It does not tell us whether all the readings have a common error.

Precision is a broader idea about how closely results agree, with repeatability describing one specific condition. Accuracy concerns closeness to the quantity we intend to measure, but metrologists generally express accuracy qualitatively and quantify specific errors or uncertainties rather than promising an 'accuracy number' without context.

Resolution is different again. A display that changes in steps of one hundredth of a millimeter has fine resolution. It does not follow that the device's mechanical jaws, alignment, calibration, and user technique can support a decision at that scale. Additional digits can make a measurement look authoritative without reducing uncertainty.

## Errors have different personalities

Imagine cutting ten equal wooden spacers. Each should be thirty millimeters long. If the measured lengths scatter around thirty with a spread of half a millimeter, you have a repeatability problem in cutting or measuring. If every spacer is about thirty point five millimeters, you may have a consistent offset: the stop is misplaced, the reference edge is wrong, or the rule's zero is damaged. In the first case, you investigate variation. In the second, you investigate bias.

The distinction changes the remedy. Taking more readings can help estimate an average and reveal scatter. It cannot, by itself, remove a shared calibration error. Likewise, adjusting a stop can remove an offset while leaving a wandering saw fence or a flexing workpiece unchanged.

Error can enter at every stage: the reference surface, the fixture, the tool, the observer, the temperature, and the interpretation of the reading. For a long metal part, thermal expansion may be consequential when temperature differs substantially from the reference condition. For wood, moisture and grain can matter more. The tool is part of a measurement system; the object is not a perfectly inert number waiting to be displayed.

## What calibration actually provides

Calibration establishes a relationship between indications of an instrument and reference values, with stated conditions and associated uncertainties. It need not be a magic adjustment that makes a device perfect. A calibration may reveal that the caliper reads consistently high. That information can support correction, acceptance, or rejection for a particular task.

Traceability describes an unbroken, documented chain connecting a measurement result to an appropriate reference, with uncertainty contributions along the way. A calibrated instrument is not automatically suitable for every job. The required tolerance must be compared with the measurement process's uncertainty, which includes more than a manufacturer's display resolution.

For household layout, elaborate metrology may be unnecessary. A good reference square, a verified tape measure, and a stable setup are often appropriate. For machining a close fit or checking an engineered dimension, more careful control may be warranted. The point is to spend measurement effort in proportion to the consequences of getting the dimension wrong.

## Think in terms of a decision

Consider a part meant to fit within a slot that is ten millimeters wide. If the part measures nine point nine nine millimeters and your method has uncertainty of several tenths of a millimeter, the display does not establish that it will fit. A decision near the boundary is exactly where uncertainty matters most.

You could improve the method: clean the jaws, check the zero, use a known reference, measure at several points, reduce the applied force, control temperature, or use a different instrument. Sometimes the better solution is not a more accurate number but a trial assembly with enough clearance for real movement and manufacturing variation.

The same principle applies when a wall is out of square, a door rubs, or a pipe must pass through a tight opening. Measure the real condition at relevant locations. Do not let a single measurement stand in for an object that may be bowed, tapered, twisted, or moving.

## A field exercise in honest reporting

Choose a safe, simple object such as a stack of paper, a metal washer, or a piece of scrap wood. Measure it five times, removing and replacing the tool each time. Note the spread. Rotate the object and measure elsewhere. Check the instrument's zero and, if available, a known reference. Then describe the result without claiming more certainty than the setup earns.

You may find that the important variability is not in the display at all. It may be the object's shape or the force of your hand. This is the central lesson: a measurement is an interaction between a quantity, a reference, a method, and a purpose. The experienced craftsperson is not the one who always gives the most digits. It is the one who knows which digits deserve belief and what decision those digits can safely support.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Vocabulary and example

- **Repeatability:** agreement under specified repeatability conditions.
- **Bias:** systematic component of measurement error; not estimated by repeated readings alone.
- **Resolution:** smallest displayed increment; not a complete uncertainty budget.
- **Calibration:** documented relation of instrument indications to reference quantity values.
- **Traceability:** linked chain to references with uncertainty at each step.
- **Uncertainty:** parameter describing dispersion of values attributable to a measurand, given a model and observations.

An illustrative set of readings `30.2, 30.0, 30.1, 29.9, 30.3 mm` has mean `30.1 mm` and sample standard deviation about `0.16 mm`. Neither result proves the absence of a `+0.5 mm` systematic offset. This is an example of repeatability assessment, **not** a complete calibration or valid task-specific acceptance rule.

### Source and practice distinctions

NIST's technical terminology distinguishes repeatability, calibration, and measurement uncertainty. Ordinary shop references have varying quality and need not be compared using one universal uncertainty ratio. Any dimensional acceptance rule must account for fit, function, the actual tolerance specification, and measurement risk.

## Selected reading and claim sources (non-spoken)

- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
