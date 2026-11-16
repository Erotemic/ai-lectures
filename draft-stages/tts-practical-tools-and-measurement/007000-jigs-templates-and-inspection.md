# 007000 — Jigs, Templates, and Inspection

**Track:** Tools and Measurement. **Background:** Layout, repeatability, uncertainty, drilling, fastening, and cutting. **Purpose:** explain how to transfer design intent into repeated work without accumulating hidden error.

<!-- BEGIN SPOKEN LECTURE -->

# Make the work repeatable

Imagine drilling matching mounting holes through twelve wooden panels. Measuring from a rough edge, marking two dots with a pencil, and aiming the drill at those dots may produce twelve pieces that look nearly identical. Yet a bracket may fit the first and bind against the last. The problem is not necessarily that the worker lacks dexterity. The process does not adequately constrain the relationship between the holes and the reference surfaces.

A jig or fixture exists to make a desired relationship repeatable. A template carries a shape or position. A jig may guide a tool, such as a drill bushing directing a bit. A fixture holds and locates a workpiece so the operation happens in a controlled position. Everyday workshop language sometimes blends these words, but their distinct jobs are useful: one tells you where the operation belongs, another controls where the material sits, and another may guide how the tool travels.

## Choose a datum

Before designing a jig, decide what the result must fit. If a cabinet drawer rides on slides referenced to the sides of the opening, those sides are meaningful datums. Measuring every hole from a wavy decorative face may produce precise distances from the wrong feature. A datum is a chosen reference for relating geometry. In practical fabrication it is often a flat face, straight edge, or centerline that is stable enough for the task.

A good locating fixture removes the degrees of freedom that would otherwise vary. For a rectangular board resting on a flat bench, a base supports it vertically. A straight fence constrains one sideways motion and a rotation. An end stop constrains movement along the fence. A clamp maintains contact while the operation takes place. The fixture need not be complicated. Its virtue is a clear mechanical relationship between each part and the tool.

But constraints can fight. If the stock varies in width and the fixture attempts to force both long edges into hard stops, boards may rock, bend, or fail to seat consistently. A functional datum arrangement often constrains the essential directions and leaves room for harmless variation elsewhere. Repeatability is not the same as making every surface immovable.

## The difference between consistent and correct

Suppose a drill jig places two holes precisely 80 millimeters apart on every board. If the mating bracket requires 82 millimeters, the jig is excellent at producing the wrong part. This is systematic error. Repeatedly checking with the same incorrect template can provide false reassurance.

There are at least three distinct questions. Is the setup accurate relative to the intended dimension? Is the output repeatable across pieces? And is the result functionally acceptable when assembled with its mate? A useful first-article inspection answers all three before committing an entire batch. The first article should be fitted against a known mating piece or checked with an independent reference, not only with the jig used to make it.

Another issue is tolerance accumulation. Suppose a spacer strip is meant to set a panel offset. If successive parts are located from the previously cut edge, every small error in length, angle, or surface condition can move the next reference. Whenever possible, locate repeated features from a common, stable datum instead of passing an uncertain measurement down a chain. When cumulative dimensions are unavoidable, explicitly budget the variation.

## Design for wear and mistakes

A wooden drill template may be sufficient for a handful of holes. Repeated contact with a spinning drill can enlarge its holes and allow positional drift. A replaceable metal drill bushing helps guide the bit and resist wear when the job demands it. A fence that accumulates sawdust stops locating material reliably. A stop that flexes under clamping load changes the geometry between setup and operation. A jig is a measurement and restraint system; it needs inspection and maintenance.

An easy-to-use fixture should also make incorrect setup visible. Shape a stop so the workpiece cannot seat backward, add a clear index mark, and provide access for chips to escape. But do not let a clever constraint become a trap for hands near moving cutters. A jig is not automatically a machine guard. Tool-specific guards, clamp clearance, safe workholding, and manufacturer limits remain essential.

## Inspect the output, not just the setup

Choose inspection tools in proportion to the functional requirement. For a fence post, a tape and square may suffice. For a machined bearing seat, material, temperature, gauge uncertainty, and calibrated dimensional measurement become central. Even when a part measures correctly at one point, flatness, squareness, surface finish, and hole alignment can determine whether it works.

Inspection has its own failure modes. A caliper jaw held at an angle reports a misleading dimension. A ruler pressed against a rough, bowed edge creates an unstable zero. A gauge that has not been checked may be repeatably biased. The measurement process should be specified well enough that a second person can reproduce it: what was touched, where, with which instrument, under which conditions?

An effective practical sequence is simple. Define the assembly requirement. Identify the datum that controls it. Make a fixture that constrains the important geometry without distortion. Produce one trial part. Check it against an independent standard and the mating assembly. Record the result. Only then make the batch, periodically verifying that the fixture has not shifted or worn.

The larger principle is that workmanship is designed into a process. Skill still matters, but the best use of skill is often to build a setup that makes good results easier to repeat, easier to inspect, and harder to accidentally corrupt.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Fixture drawing exercise

Sketch a flat base, long fence, one end stop, two clamps, and a drill bushing. Mark the reference surfaces and the motions each feature constrains. Then draw a slightly warped board and explain whether the fixture still locates it correctly.

### Measurement exercise

Target hole spacing: `82.0 ± 0.5 mm` (illustrative, not a design specification). A jig produces `80.0 mm` on every piece. Variation may be nearly zero while the batch fails the specification: distinguish bias from scatter. Perform an independent first-article check rather than measuring only against the original template.

**Review boundary:** Jigs and fixtures do not replace certified machine guarding, appropriate workholding, or instrument calibration. Select tolerances from the actual assembly, not from this illustration.

## Selected reading and evidence records (non-spoken)

- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `osha-hand-power-tools` — [OSHA, Hand and Power Tools (OSHA 3080)](https://www.osha.gov/sites/default/files/publications/OSHA3080.pdf). Tool guarding, securing work with clamps and correct tool operation.
