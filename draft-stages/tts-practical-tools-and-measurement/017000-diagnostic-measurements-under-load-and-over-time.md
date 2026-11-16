# 017000 — Diagnostic Measurements Under Load and Over Time

<!-- BEGIN SPOKEN LECTURE -->

A machine starts perfectly on a workbench and stops as soon as it is asked to do real work. A pump hums when its switch is thrown but produces little water. A battery reports a healthy voltage until a motor tries to start. The measurement that matters is often not the one that is easiest to take. We need to observe a system under the conditions that make its defect appear, and sometimes over enough time to capture an intermittent event.

## No-load readings do not measure capacity

Think of a battery connected to a motor. An open-circuit voltmeter draws very little current. A weak connection or depleted battery may therefore show a familiar voltage. When the motor starts, the current demand rises. The internal resistance of the battery and the resistance of cable contacts produce voltage drops. The motor sees less voltage than expected and may stall. The important observation is the voltage at the load *while* the load attempts to run, interpreted using the manufacturer's expected range and the circuit's ratings.

The same distinction appears in fluid systems. A pressure gauge connected to a closed outlet may read normal, but flow through a restriction can cause a large pressure difference once the valve opens. In air systems, a fan may generate pressure without delivering the intended flow through a clogged filter. In mechanics, a shaft can turn freely without a workpiece yet vibrate or slip when torque is applied. Measurements under realistic operating conditions reveal the resistance and energy losses that static inspection misses.

This does not mean making the system work at any cost. A load test must be designed around known ratings, guarding, safe fixtures, and stable conditions. Do not use a jammed workpiece as a substitute for a calibrated brake, or short a battery to 'see if it has power.' A useful diagnostic load resembles normal service without inviting a new failure.

## Measure the right quantity at the right location

A meter placed across a motor's terminals answers a different question from a meter placed across the battery. If the motor terminal voltage collapses but the source voltage remains stable, the wiring or connections between them deserve inspection. Similarly, measuring pressure before and after a filter distinguishes filter restriction from low inlet supply better than a single reading. Measuring temperature at the motor housing alone does not tell you whether the source is bearing friction, winding losses, poor cooling, or a nearby heater.

Every instrument also changes or filters what it reports. A digital multimeter may update only a few times per second and miss a brief starting transient. A cheap temperature logger may have a large response delay. A clamp meter may have an accuracy range that excludes the small current you are trying to measure. An infrared thermometer observes emitted radiation and can be badly misled by a reflective metal surface. The useful question is not just 'What number did I read?' but 'What did the sensor actually measure, with what bandwidth and uncertainty?'

The simplest protection against a misleading measurement is to record location, time, operating condition, instrument, units, and a reference value. 'Voltage 11.1' is incomplete. '11.1 volts at motor terminals during a normal start attempt, measured on this meter, while the supply was 12.3 volts' is evidence that can be acted upon.

## Intermittent faults require time as an axis

Imagine a pump that trips after twenty minutes, cools, and starts again. A single measurement taken during its first minute may be completely normal. You need a timeline of current, temperature, inlet or outlet condition, duty cycle, and any trip signal. Samples every five minutes might show gradual heating but miss a one-second pressure surge. High-frequency capture is not always necessary; select a sampling interval that can reveal the hypothesized phenomenon.

Event logs can provide another view. A controller reporting overcurrent at a precise time does not prove the motor is defective. The event could follow a jam, poor lubrication, mechanical binding, a voltage sag, or faulty sensing. Correlate the fault timestamp with what the equipment was doing and what other measurements changed. A clock that drifts across devices can make an apparently causal sequence impossible to trust, so synchronize time or explicitly record timing uncertainty.

Repeating the same test is powerful only if conditions are comparable. Ambient temperature, workpiece mass, fluid level, battery state, and operator technique may all change. A test repeated after the machine cools cannot automatically be compared to one performed immediately following sustained operation.

## Design a discriminating test

Suppose a drill makes an oversize hole. Three competing hypotheses are tool runout, a worn bit, and the workpiece shifting. An unloaded indicator measurement at the spindle may help test runout. Inspecting the bit and checking fixture movement under cutting force test the others. An unloaded spindle number alone does not establish the actual hole diameter; cutting forces, material, feed, and fixture stiffness matter. A good sequence targets the hypothesis most likely to explain the observed failure and controls the other variables.

Now consider a hose that delivers a trickle despite a normal static gauge reading. If you can make a safe rated test, measure flow and dynamic pressure before and after the suspected restriction. The change in pressure with flow can reveal where resistance concentrates. Again, a static measurement is part of the picture but not a verdict.

The craft is to treat a number as an observation with boundaries, not as a diagnosis. Ask what changes when the equipment is working, where energy is lost, how long the failure takes to emerge, and what measurement would separate competing explanations. The best measurement is often the one collected at the precise instant and location where the defect affects performance.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Electrical example:** If a source is 12.4 V under load and terminals at an intended 5 A load are 11.6 V, the total series drop is 0.8 V and effective path resistance is about 0.16 ohm at that operating point. This is a model illustration, not an acceptance limit. Confirm voltage and current concurrently; actual circuits can vary dynamically.

**Fluid example:** Compare pressure upstream and downstream of a restriction only while measurable flow exists. When flow goes to zero, friction loss often approaches zero even if the restriction remains severe.

**Logging record:** timestamp with timezone, instrument ID/calibration, units, location, ambient condition, load/duty, event notes, expected tolerance, uncertainty. A chart needs both the signal and enough event context to interpret it.

**Safety/limitations:** Work within instrument category ratings and equipment manufacturer limits. Electrical measurements near mains or exposed conductors require qualified procedures and suitable probes; load tests must not defeat guards, interlocks, relief devices, or overcurrent protection. Don't improvise high-energy tests.

## Selected reading and source locators (non-spoken)

- `nist-uncertainty` — [NIST, Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty). Measurement values, standards and uncertainty.
- `nist-repeatability` — [NIST Technical Note 1297, Appendix D.1: Terminology](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology). Definition and conditions for repeatability.
- `nist-calibration` — [NIST Engineering Statistics Handbook, Calibration Pitfalls](https://itl.nist.gov/div898/handbook/mpc/section3/mpc364.htm). Calibration limitations; precision, bias, operator changes.
- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Torque and perpendicular moment arm.
