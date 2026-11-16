# 015000 — Diagnosing Tool Runout, Vibration, and Repeatability

<!-- BEGIN SPOKEN LECTURE -->

A drill press makes a hole that is visibly larger than the drill bit. A router leaves ripples on the edge of a board. A saw that once cut cleanly starts producing an irregular surface. Before deciding to buy a new machine, we should ask what is actually moving. The bit may not be centered; the spindle may be deflecting; the stock may be vibrating; the cutting edge may be worn; or the measurement may be inconsistent. These faults can look alike in finished work, but they require different tests.

## What runout means

Imagine rotating a perfectly straight cylinder whose centerline is offset from the machine's true rotation axis. A fixed indicator touching its surface would move in and out once each revolution. That motion is radial runout. End-face wobble is axial runout. Toolmakers commonly report the total indicated runout, abbreviated TIR, meaning the difference between the maximum and minimum dial readings over the measurement cycle. For an ideal round, rigid, off-center cylinder under simple conditions, the eccentricity is one half of the total indicator change. A real drill chuck, arbor, or workpiece may not be round or rigid, so this shortcut is not a general diagnosis.

Runout can be introduced at several interfaces. A good spindle may carry a dirty taper. A clean taper may hold a damaged chuck. A sound chuck may grip a bent drill. If we measure only at the drill tip, we have measured the combined effect of every upstream interface and the tool itself. That is a useful symptom measurement, but it does not tell us which part is responsible.

To isolate a fault, work from the reference structure outward. Check the spindle or arbor surface that the machine specification identifies as a measuring location; then check the mounted chuck or holder, and then the tool shank. Use the same indicator orientation and controlled rotation for comparisons. Unplug or isolate the machine before setup and rotate by hand only when the machine design permits it. A dial indicator should not be placed into a powered cutting operation just because we want a more realistic measurement.

## Runout is not the same as deflection

A rotating tool also bends under cutting force. Imagine a long, thin drill entering a hard surface at a shallow angle. Even with its shank centered perfectly, the tip may walk or bow. The workpiece can move if it is not clamped, and the table can move if joints are loose. That movement produces errors during cutting which are not present during a slow hand-rotation indicator test.

Think of the machine as a chain of stiffnesses: foundation, frame, table, clamp, workpiece, bearing, holder, and tool. Under load, each element deflects. The least stiff member can dominate the result. A long drill extends farther from its holder and generally bends more easily than the same diameter supported close to the work. Adding a powerful motor to a flexible setup does not improve its accuracy.

Now consider a router producing a periodic washboard finish. If the ripple spacing changes with feed speed but the spindle speed remains fixed, the pattern may follow tool rotation or tooth engagement. If the pattern occurs at a particular machine speed even while the tool is cutting lightly, structural resonance could be involved. An uneven cutting edge, chipped tooth, or poorly balanced accessory can also create forcing at rotation frequencies. We should record the circumstances rather than infer a particular cause from the appearance alone.

## Separate repeatability from accuracy

A machine might cut ten parts to the same wrong length. That is repeatable but inaccurate. It might also cut ten parts that scatter around the desired dimension. Then the variation itself is a problem. The distinction matters because the next experiment differs. A fixed offset suggests calibrating a scale, fence, or datum. Scatter suggests workholding, play, thermal effects, operator technique, material changes, or a drifting stop.

Repeated measurements should be made under comparable conditions: same reference face, similar clamping, tool temperature, measurement instrument, and feed procedure. Re-seat the tool or workpiece deliberately between trials if the question is about setup repeatability. Take a second sequence without re-seating if the question is whether the system remains stable during operation. If those two sets have very different spread, the act of locating the work may be the weak link.

We should not mistake the indicator's number of decimal places for proof of a fine result. A measurement has limits imposed by indicator resolution, contact angle, reference surface quality, operator pressure, and thermal drift. A simple repeatability study may find that the measurement method itself varies enough to hide the improvement we hoped to see. Compare several readings of a known stable reference before interpreting small differences on the machine.

## A fault-isolation sequence

Suppose a drill press makes holes about half a millimeter oversize. First confirm the hole diameter with a suitable instrument rather than relying on a nominal drill label or a visually rough exit edge. Inspect the bit for bend, chipped lips, and unequal geometry. Check the workholding and entry surface. Observe spindle, holder, and shank runout separately, using the measurement procedure appropriate to that machine. Compare a short, sound bit with the original long bit. Finally, make a controlled test hole in a representative material and document feed, speed, work support, and result.

Notice the order. We have changed one factor at a time, and every observation constrains possible causes. If the spindle's indicated motion is small but the long bit visibly wanders under load, replacing spindle bearings would be premature. If the indicator changes markedly after re-seating the chuck, an interface problem becomes more plausible. If a new bit improves the result without any machine change, cutting geometry or tool condition deserves attention.

Some vibration is an immediate stop signal: sudden shaking, a cracked abrasive wheel, a loose blade, or a damaged guard is not a data-collection opportunity. Isolate power and inspect before restarting. Diagnosis is a controlled experiment only when the setup is itself controlled.

The goal is not to make every tool metrology-grade. It is to know what accuracy the job requires, which error source is dominant, and what observation would establish that a repair worked. Good measurement avoids both needless replacement and unjustified confidence.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Diagnostic matrix

| Symptom | Candidate cause | Discriminating test |
|---|---|---|
| Dial reading changes with spindle rotation | Rotating geometry / mounting | Measure at spindle, holder, and sound reference shank separately |
| Accurate without cutting, poor under load | Bending or work motion | Shorter overhang; supported fixture; compare unloaded vs test work |
| Constant dimensional bias | Offset datum or calibration | Compare against independent traceable reference |
| Variation after every re-clamp | Re-seating / fixture locating | Alternate fixed-clamp and re-clamped batches |
| Speed-specific vibration | Resonance or rotating forcing | Record speed dependence; inspect tooling and guarding first |

### Measurement note

`TIR = max(indicator) − min(indicator)`. `eccentricity = TIR/2` applies only in an idealized rigid, round, eccentric model. It is not a general formula for bent shafts, lobing, tilted faces, or dynamic cutting error.

**Machine boundary:** Measurement points, allowable runout, bearing clearance, safe hand-rotation, and corrective methods are machine-specific. Never bypass guards or test a visibly unstable powered setup.

## Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `osha-drill-press` — [OSHA, Woodworking eTool — Drill Presses](https://www.osha.gov/etools/woodworking/production/machines-tools/drill-press). Clamping stock, twist hazards and drill press operational constraints.
