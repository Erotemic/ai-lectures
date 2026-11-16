# 017000 — Condition Monitoring of Rotating Equipment

<!-- BEGIN SPOKEN LECTURE -->

A ventilation fan has always made a low hum. Recently the hum has acquired a faint rattle, and one bearing housing feels warmer than it did last month. Should the fan be replaced now, or simply watched? Condition monitoring is the practice of making changes like these measurable. It does not predict failure by magic; it helps distinguish normal operating variation from a developing physical defect.

## A rotating machine leaves several signatures

A shaft carries torque from a motor through bearings, couplings, gears, or belts to a load. Problems can appear as vibration, temperature rise, acoustic changes, power consumption, lubricant contamination, reduced throughput, or increasing time to start. Each is a symptom of how energy is being transmitted and dissipated.

An out-of-balance rotor often produces vibration related to its running speed. Misalignment of coupled shafts can excite other directions and harmonics. A damaged rolling bearing may produce repeated impact signatures tied to the geometry of its elements. A loose mounting may rattle at particular speeds. These are helpful physical explanations, but a single sound or frequency peak is rarely a unique diagnosis. Structural resonance, nearby machinery, and load changes may create similar observations.

Monitoring begins with a baseline measured when equipment is believed to be functioning correctly, in a known operating state. A machine at full load and high speed may vibrate more than at light load even with no defect. Comparing readings taken at different speed, temperature, mounting condition, and load without noting those differences can manufacture a false alarm.

## Temperature: useful, but ambiguous

A bearing housing warms from friction and from heat conducted through the shaft or frame. Lubricant viscosity, ambient temperature, rotational speed, alignment, and process heat all affect the number. A rise relative to an established baseline at comparable load and ambient condition deserves attention. But a housing that is 'hot to the touch' is neither a calibrated measurement nor a safe test.

Choose repeatable sensor locations and a suitable instrument. A contact probe can measure a point but may lag changes. An infrared instrument has a wider view and depends on surface emissivity. A polished steel housing can reflect another hot object and provide misleading apparent temperature. Record the surface condition, measuring distance and geometry, not just a temperature number.

Suppose the housing is eight degrees warmer than its normal value. That observation becomes more persuasive if vibration also rises, lubricant changes color, and the temperature tracks load. It remains possible that ambient cooling has changed, so inspect airflow and nearby heat sources. Monitoring is a search for corroboration, not an excuse to declare a bearing failed from one reading.

## Vibration requires both frequency and context

A handheld vibration meter may summarize overall vibration in displacement, velocity, or acceleration. More advanced instruments capture a time waveform and spectrum. These are different windows into the same motion. A large low-frequency displacement may correspond to modest acceleration, while a small high-frequency impact can create a strong acceleration signal. The appropriate measure depends on the equipment and defect under investigation.

Rotational speed is a critical reference. A shaft turning at eighteen hundred revolutions per minute completes thirty revolutions each second. A vibration component near thirty hertz may therefore be related to once-per-revolution excitation, but it is not proof of imbalance. Harmonics at multiples of running speed and components at bearing or gear frequencies require machine-specific interpretation. The same mechanical frequency can also coincide with a supporting structure's resonance.

A tachometer reading, speed log, and sensor placement help interpret spectra. Use sensors mounted in the same orientation and location on repeat visits, preferably on rigid accessible bearing housings. Readings from a flexible cover cannot be compared directly with readings on the bearing block. Do not expose rotating shafts, belts, or couplings merely to attach a probe. Guarding and lockout procedures determine when installation and inspection are permissible.

## Establish thresholds that lead to action

A good monitoring plan defines what equipment is important, which failures matter, what signals can reveal them, and how often readings should be taken. A low-consequence exhaust fan can tolerate a different response plan from a machine whose failure would cause injury or widespread damage. Trends can be more useful than a one-time pass/fail number: steadily increasing vibration over several visits may justify planned maintenance before a hard threshold is reached.

Yet trends can be noisy. A recently changed motor speed, process load, bearing type, or lubrication interval may make the old baseline obsolete. Reestablish a new baseline after documented changes. Keep a record of maintenance actions and measure again afterward. If a coupling replacement causes vibration to increase, the new data may reveal installation misalignment even though the old component was worn.

Consider a pump that starts vibrating only when a suction tank is nearly empty. The pattern may arise from cavitation or inadequate inlet conditions, not a worn rotor. A bearing replacement performed without checking suction conditions will not remove the initiating cause. The most valuable data include process state alongside machine state.

Condition monitoring does not eliminate the need for safe shutdown or direct inspection. Strong mechanical impacts, rapid heating, smoke, leakage, or signs of impending structural failure demand prompt action rather than waiting for another sample. For ordinary trends, build hypotheses, choose discriminating tests, and plan repair around both condition and consequences.

The central skill is learning what a machine's normal operating signature looks like and recognizing meaningful departures. Sound, heat, vibration, current, and process performance become informative when recorded under comparable conditions. Monitoring tells you when to investigate; thoughtful mechanical diagnosis tells you what to repair.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Speed calculation:** rpm / 60 = revolutions per second = running-speed frequency in Hz. At 1,800 rpm, 1× running speed is 30 Hz. A peak at 30 Hz is not a diagnosis by itself; identify the actual shaft speed and evaluate harmonics and load.

**Baseline record:** machine ID, operating speed, process throughput, bearing location and sensor axis, mounting method, temperature, lubricant, ambient conditions, vibration metric and units, maintenance state, date/time.

**Trend thought experiment:** Vibration grows only when a pump's inlet tank is low. Compare suction conditions, available head, noise pattern, flow and vibration before replacing bearings. Rising temperature without vibration change merits a different differential.

**Guarding:** Never reach into moving belts/couplings or remove guards for a convenient reading. Sensor mounting, lockout and plant safety procedures determine allowable access. Thresholds must be appropriate to the machine, instrument and consequence, not a universal sound/temperature limit.

## Selected reading and source locators (non-spoken)

- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `skf-grease` — [SKF Evolution, Grease Lubrication Mechanisms in Rolling Bearing Systems](https://evolution.skf.com/us/grease-lubrication-mechanisms-in-rolling-bearing-systems/). Grease churning, replenishment, starvation and film breakdown.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.
