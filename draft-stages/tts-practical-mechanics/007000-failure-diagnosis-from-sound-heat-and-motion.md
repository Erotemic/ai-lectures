# 007000 — Failure Diagnosis from Sound, Heat, and Motion

**Track:** Mechanical Systems. **Background:** Bearings, gears, friction, lubrication, fits, and fatigue. **Purpose:** infer failure mechanisms from measured changes rather than changing parts by intuition.

<!-- BEGIN SPOKEN LECTURE -->

# A machine tells a story in motion

A pump that once ran quietly begins to hum, then vibrate, then trip a protection device. You may recognize the sound of a worn bearing. But it could also be a loose mounting bolt, a misaligned coupling, an imbalanced impeller, cavitation, a motor fault, or a pipe excited by changing flow. A diagnosis is stronger when it explains several independent observations, not just one familiar noise.

Machines convert energy. Motors produce rotation, transmissions change torque and speed, bearings constrain motion, seals separate fluids, and supports transfer forces into a structure. When something goes wrong, some portion of input energy may be redirected into heat, vibration, sound, deformation, or leakage. Those are signatures that an instrument and a patient observer can detect.

## Sound has frequency and timing

A squeal during startup differs from a steady rumble at constant speed. A periodic click once per revolution suggests a recurring geometric event. Rapid gear-like chatter can be tied to tooth engagement, but multiple mechanisms may overlap in the sound. The most informative question is often not 'what does it sound like?' but 'when does it appear relative to speed, temperature, load, and direction?'

A misaligned rotating assembly may generate vibration related to rotation frequency and its harmonics. A damaged bearing may generate impulsive vibration whose pattern depends on geometry and speed. A loose shield can rattle only when resonance is reached. These are tendencies, not automatic translations from one sound into one component. Without equipment geometry and measurement, saying 'a bearing frequency' is less useful than recording that the noise rises consistently with shaft speed.

An audio recording can help establish a baseline and allow comparison after repair. Yet phone microphones and automatic signal processing alter apparent loudness and frequency. Keep the recording position and operating state consistent; do not make an absolute vibration specification from a phone audio file.

## Heat is not synonymous with friction

Excessive friction creates heat, but electric motors also lose energy in windings and magnetic components. Pumps heat fluid when operating away from efficient conditions. Bearings warm during normal operation, and temperature depends on speed, preload, lubrication, load, airflow, and ambient conditions. A component that runs at 55 degrees Celsius may be normal for one machine and dangerous for another. Trends relative to a documented baseline are generally more interpretable than temperatures without context.

An infrared thermometer measures radiation from a surface within its field of view. Shiny metal can give misleading readings because emissivity is low and reflected radiation matters. Two nearby measurements with different surface finishes should not be treated as direct proof that one internal bearing is hotter. A contact sensor or other validated method may be necessary for consequential assessment.

A valuable pattern is the sequence of symptoms: vibration rises after a load change, bearing housing temperature rises, then performance falls. The sequence suggests a mechanical or lubrication problem deserving investigation, but still does not isolate the part. The observations should guide the next test.

## Motion and output reveal the load path

A fan may draw more electrical power while delivering less airflow because an inlet is obstructed or a component is rubbing. Another type of fan may respond differently depending on its performance curve. A pump may make noise at low inlet pressure because vapor bubbles form and collapse; cavitation can cause damage while appearing superficially similar to bad bearings. A gearbox with backlash may clunk on reversal even though its bearings remain smooth.

Inspecting only the rotating part is therefore insufficient. Ask what the machine is coupled to, what loads it experiences, and whether the supports are compliant. A cracked mount changes vibration transmission. A bent shaft can increase bearing load after bearings have been replaced. An impeller obstructed by debris may produce imbalance and a new noise. Replacement without cause analysis risks reproducing the same failure.

## Turn observations into tests

Imagine a workshop belt-driven machine with increasing vibration. First establish a safe, normal operating condition. Observe whether vibration tracks motor speed, belt engagement, or load. Inspect for accessible signs of belt damage, loose external guards or supports, and heat discoloration while the system is shut down and isolated. If qualified and equipped to do so, measure alignment, belt tension, and vibration at defined points. The result of each test should make some hypotheses more plausible and others less so.

Consider a second case: a circulating pump is quiet with a cold system but noisy after heating. Thermal expansion may alter clearances or alignment. A temperature-dependent fluid condition could also matter. The contrast between cold and hot states is evidence. It is better than replacing the pump immediately because it only 'sometimes sounds bad.'

The key is a before-and-after record. Note speed, load, sound character, vibration location, temperatures, lubrication status, and performance. Compare against the machine's own baseline, manufacturer limits, and similar equipment under matched conditions. A trend matters most when measurement conditions are controlled.

Rotating equipment can injure people rapidly. Diagnosis does not justify opening a guard, touching a moving belt, or bypassing shutdown systems to obtain a closer recording. Fault isolation and controlled inspection should preserve the safeguards that separate observers from stored and moving energy.

Good mechanical diagnosis is an explanation of energy and motion. It says not only what changed, but why that change can produce the measured sound, heat, or behavior—and what independent observation would disprove the proposed explanation.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Pattern-to-test table

| Pattern | Candidate mechanism | Evidence that discriminates |
|---|---|---|
| One impulse per shaft turn | Rub, damaged feature, eccentricity | Confirm speed synchrony and location |
| Vibration appears under load | Misalignment, support flexibility, process force | Compare known load states and operating limits |
| Pump crackling at low inlet pressure | Cavitation or entrained gas | Suction conditions, fluid temperature, performance curve |
| Warm casing with no output | Friction or internal energy loss | Input power, shaft/output motion, control state |

### Data record

Keep measured variables with units and operating state: RPM, load, current or power, input/output flow if relevant, temperature sensor type and position, vibration sensor placement, and maintenance history. Use manufacturer acceptance limits for judgments.

**Review boundary:** Examples are hypothesis-generating, not component diagnoses. Never bypass guards, remove interlocks, or measure near exposed moving machinery without suitable procedures and qualifications.

## Selected reading and evidence records (non-spoken)

- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `skf-grease` — [SKF Evolution, Grease Lubrication Mechanisms in Rolling Bearing Systems](https://evolution.skf.com/us/grease-lubrication-mechanisms-in-rolling-bearing-systems/). Grease churning, replenishment, starvation and film breakdown.
