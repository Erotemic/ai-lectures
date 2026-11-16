# Read vibration, motion, and condition evidence

<!-- BEGIN SPOKEN LECTURE -->

# Read vibration, motion, and condition evidence

## Springs, Stored Energy, and Damping

Press down on a bicycle suspension and release it. A spring returns energy that you supplied while compressing it. If there were no dissipative mechanisms, the mass might oscillate for a long time. A damper makes that motion settle more quickly by converting some mechanical energy into heat. The spring and the damper solve different problems. Conflating them leads to poor repair decisions, uncomfortable vehicles, and vibrating equipment.

A spring is not necessarily a visible coil. A leaf spring, a thin metal strip, a flexing plastic latch, an elastic seal, and a loaded machine frame all deform and can store elastic energy. In a range of small deformations, many of them can be approximated by Hooke's law: restoring force proportional to displacement from equilibrium. More displacement means more restoring force. This is a model, not a guarantee that all real springs obey a straight line through their entire travel.

### Force is not the same as stored energy

Imagine compressing a spring gently. At first it pushes back only a little. As compression increases, the force rises. The work you do accumulates as potential energy. For a linear spring, doubling compression doubles the force but quadruples stored energy. That distinction matters because a spring can release substantial energy even if a technician has been moving it slowly.

A compressed spring in a mechanism can drive a latch, return a valve, or hold a door shut. A torsion spring stores energy through twist rather than direct extension. Gas springs and hydraulic accumulators involve pressurized fluid or gas as well as mechanical motion. A counterweight stores gravitational potential energy. There are several ways for a machine to retain energy after its power switch is off. Before disassembling a device, the question is not merely whether its motor is stopped, but what forces and pressures remain constrained.

### Motion contains mass, stiffness, and damping

Suspend a mass from a spring. Pull it down and let go. The spring pulls it toward equilibrium, but inertia carries it past. The spring pulls back in the other direction. The resulting back-and-forth motion is an oscillation. How quickly the system oscillates depends on its effective mass and stiffness. How rapidly it settles depends on damping.

An ideal mass-spring system has a natural frequency. Real machines have friction, material hysteresis, air drag and engineered dampers that remove energy. Too little damping can permit repeated bouncing, rattling or resonance. Excessive damping may prevent a device from responding as intended, turning fast motion into slow, sluggish motion. Damping is not universally 'more is better.' It must match the function.

Consider a vehicle shock absorber. It is mainly a damper, not the component that holds the vehicle's static weight. The spring supports and positions the vehicle; the damper resists movement and helps control oscillations. If a vehicle bounces repeatedly after a disturbance, inadequate damping may be one hypothesis. But tire condition, bushings, spring damage, mounting points, and suspension geometry can also cause poor behavior. The observation alone does not identify a single failed part.

### Resonance changes the stakes

A washing machine that starts to vibrate strongly at one spin speed but becomes calmer at another may be passing through a range where its forcing frequency is close to a structural natural frequency. The severity depends on imbalance, stiffness, damping and how the appliance is supported. Changing only the spin speed might move away from the bad region without correcting the imbalance. Replacing an intact damper might not correct an uneven floor or loose mounting.

The same idea applies to fans, machine-tool spindles, vehicle suspension and building components. A periodic force can repeatedly put energy into a flexible system. Near resonance, response can become much larger than expected from a static force calculation. An engineer may solve the problem by modifying stiffness, mass, excitation, isolation or damping. Those are distinct levers.

Rubber mounts make the tradeoff visible. Soft mounts can isolate high-frequency vibration, but they allow more displacement at low frequencies and during start-stop transients. Stiffer mounts constrain movement but transmit more vibration. A well-chosen mount matches the machine's mass, disturbance frequencies and allowable motion, rather than simply being the softest material available.

### Diagnose what the energy is doing

Picture a garage door that moves abruptly after a spring repair. The defect might involve spring adjustment, cable routing, damaged rollers, friction in tracks, or a failed damping and control mechanism. Because loaded springs and moving door components can retain substantial energy, dismantling them without the proper procedure is not an appropriate diagnostic experiment. The physical analysis can still begin with observation: which component stores energy, which transmits it, and which dissipates it?

For a safe tabletop demonstration, compare an elastic band gently stretched within its working range to a strip of soft foam slowly compressed. Observe how much energy appears to return, and how much is dissipated. Then compare a ruler flexed and released with the same ruler constrained by a soft pad. The point is not precise measurement; it is to feel that stiffness, stored energy and damping have different signatures.

Once you can label those roles, many repairs become clearer. A spring can be intact while a damper fails. A damper can be healthy while an attachment loosens. A machine can vibrate because its excitation has changed even though none of its supports broke. The mechanic's task is to follow energy through the system and identify which function no longer behaves as intended.

## Failure Diagnosis from Sound, Heat, and Motion

Stored energy and damping become useful diagnostic ideas when a machine’s motion, sound, or temperature changes.

A pump that once ran quietly begins to hum, then vibrate, then trip a protection device. You may recognize the sound of a worn bearing. But it could also be a loose mounting bolt, a misaligned coupling, an imbalanced impeller, cavitation, a motor fault, or a pipe excited by changing flow. A diagnosis is stronger when it explains several independent observations, not just one familiar noise.

Machines convert energy. Motors produce rotation, transmissions change torque and speed, bearings constrain motion, seals separate fluids, and supports transfer forces into a structure. When something goes wrong, some portion of input energy may be redirected into heat, vibration, sound, deformation, or leakage. Those are signatures that an instrument and a patient observer can detect.

### Sound has frequency and timing

A squeal during startup differs from a steady rumble at constant speed. A periodic click once per revolution suggests a recurring geometric event. Rapid gear-like chatter can be tied to tooth engagement, but multiple mechanisms may overlap in the sound. The most informative question is often not 'what does it sound like?' but 'when does it appear relative to speed, temperature, load, and direction?'

A misaligned rotating assembly may generate vibration related to rotation frequency and its harmonics. A damaged bearing may generate impulsive vibration whose pattern depends on geometry and speed. A loose shield can rattle only when resonance is reached. These are tendencies, not automatic translations from one sound into one component. Without equipment geometry and measurement, saying 'a bearing frequency' is less useful than recording that the noise rises consistently with shaft speed.

An audio recording can help establish a baseline and allow comparison after repair. Yet phone microphones and automatic signal processing alter apparent loudness and frequency. Keep the recording position and operating state consistent; do not make an absolute vibration specification from a phone audio file.

### Heat is not synonymous with friction

Excessive friction creates heat, but electric motors also lose energy in windings and magnetic components. Pumps heat fluid when operating away from efficient conditions. Bearings warm during normal operation, and temperature depends on speed, preload, lubrication, load, airflow, and ambient conditions. A component that runs at 55 degrees Celsius may be normal for one machine and dangerous for another. Trends relative to a documented baseline are generally more interpretable than temperatures without context.

An infrared thermometer measures radiation from a surface within its field of view. Shiny metal can give misleading readings because emissivity is low and reflected radiation matters. Two nearby measurements with different surface finishes should not be treated as direct proof that one internal bearing is hotter. A contact sensor or other validated method may be necessary for consequential assessment.

A valuable pattern is the sequence of symptoms: vibration rises after a load change, bearing housing temperature rises, then performance falls. The sequence suggests a mechanical or lubrication problem deserving investigation, but still does not isolate the part. The observations should guide the next test.

### Motion and output reveal the load path

A fan may draw more electrical power while delivering less airflow because an inlet is obstructed or a component is rubbing. Another type of fan may respond differently depending on its performance curve. A pump may make noise at low inlet pressure because vapor bubbles form and collapse; cavitation can cause damage while appearing superficially similar to bad bearings. A gearbox with backlash may clunk on reversal even though its bearings remain smooth.

Inspecting only the rotating part is therefore insufficient. Ask what the machine is coupled to, what loads it experiences, and whether the supports are compliant. A cracked mount changes vibration transmission. A bent shaft can increase bearing load after bearings have been replaced. An impeller obstructed by debris may produce imbalance and a new noise. Replacement without cause analysis risks reproducing the same failure.

### Turn observations into tests

Imagine a workshop belt-driven machine with increasing vibration. First establish a safe, normal operating condition. Observe whether vibration tracks motor speed, belt engagement, or load. Inspect for accessible signs of belt damage, loose external guards or supports, and heat discoloration while the system is shut down and isolated. If qualified and equipped to do so, measure alignment, belt tension, and vibration at defined points. The result of each test should make some hypotheses more plausible and others less so.

Consider a second case: a circulating pump is quiet with a cold system but noisy after heating. Thermal expansion may alter clearances or alignment. A temperature-dependent fluid condition could also matter. The contrast between cold and hot states is evidence. It is better than replacing the pump immediately because it only 'sometimes sounds bad.'

The key is a before-and-after record. Note speed, load, sound character, vibration location, temperatures, lubrication status, and performance. Compare against the machine's own baseline, manufacturer limits, and similar equipment under matched conditions. A trend matters most when measurement conditions are controlled.

Rotating equipment can injure people rapidly. Diagnosis does not justify opening a guard, touching a moving belt, or bypassing shutdown systems to obtain a closer recording. Fault isolation and controlled inspection should preserve the safeguards that separate observers from stored and moving energy.

Good mechanical diagnosis is an explanation of energy and motion. It says not only what changed, but why that change can produce the measured sound, heat, or behavior—and what independent observation would disprove the proposed explanation.

## Motors, Drives, and Mechanical Fault Isolation

An electric motor hums, the belt moves slightly, and a workshop fan turns too slowly. Replacing the motor seems like an obvious repair, but it could leave the fault untouched. Perhaps the driven bearing is seized, the belt is slipping, the supply voltage collapses under load, the fan is obstructed, or the motor is running on the wrong connection. To reason about the problem, follow the entire chain from electricity to useful motion.

A motor converts electrical energy into mechanical work. A rotating magnetic field or controlled electromagnetic interaction exerts torque on a rotor. The rotor turns a shaft, which may directly drive the load or transmit power through a belt, chain, gearbox, coupling, or pulley. Every transmission element changes how torque, speed, and losses appear at the driven machine.

### Torque and speed describe different capabilities

Torque measures a turning tendency. Rotational speed describes how quickly the shaft turns. Mechanical power equals torque multiplied by angular speed. A motor producing high torque at low speed and one producing low torque at high speed can deliver the same mechanical power, but they are not interchangeable for every load.

Consider a belt reduction with a small motor pulley driving a larger load pulley. Ignoring slippage and losses, the driven pulley turns more slowly but receives increased torque. A two-to-one diameter ratio approximately halves the driven speed and doubles the ideal torque. Real belts dissipate some energy, and their transmitted force is limited by tension, contact, and friction. Changing pulleys can therefore alter both performance and the loads borne by the motor and bearings.

A pump, fan, hoist, and grinder have different torque-versus-speed requirements. A fan's required load rises strongly with speed under many similar operating conditions; the load of a hoist depends on the lifted weight and geometry. If we choose a motor from nameplate horsepower alone without considering operating speed, starting torque, duty cycle, and ambient conditions, the selection may be poor.

### A motor can be overloaded while turning

Electrical input power is greater than shaft output because energy is lost in windings, magnetic materials, bearings, air movement, and other mechanisms. Heat is the consequence of many of those losses. Some motor types draw especially high current while starting, and prolonged stalls can produce severe overheating. Protection devices and thermal limits are therefore part of the design, not merely accessories.

A motor that repeatedly trips overload protection might be carrying excessive mechanical load, have a supply or phase problem, suffer poor ventilation, or have an internal fault. Resetting the protector repeatedly does not diagnose the cause. Measurements of current, voltage, speed, temperature, and driven-machine condition become meaningful when compared against the motor's rated operating conditions.

Different motor families require different reasoning. A brushed DC motor, a brushless motor controlled electronically, and an induction motor supplied from alternating current do not have identical speed controls or failure modes. A variable-frequency drive can control the speed of compatible AC motors, but the combination of drive, motor insulation, cooling, bearings, and load must be evaluated as a system.

### Isolate the chain conceptually

Suppose a belt-driven machine is noisy and slow. Start by asking whether the noise follows motor speed, driven-shaft speed, or belt contact. A squeal during acceleration may suggest belt slip; a rhythmic sound at bearing rotation frequency suggests a different mechanism. Neither sound proves its source. Condition monitoring improves when it compares like operating conditions and uses a baseline rather than interpreting one noise in isolation.

If the mechanical load is high, shaft torque requirement can increase and the motor may draw more current. If a belt slips, the motor may reach speed while the driven shaft remains slow. If a bearing is damaged, vibration and heating may localize to that housing. If the incoming power is inadequate, the motor may fail to accelerate under an otherwise normal load. These are distinct hypotheses and call for distinct measurements.

The safest and most informative diagnostic sequence avoids forcing a stalled machine to operate just to hear it fail again. Observe the machine's history and protective devices, isolate energy before physical inspection, and use qualified procedures for electrical testing. Rotating machinery can store energy in inertia or tension even after electrical power is disconnected. A coast-down time, charged capacitor, spring, or suspended load can make a nominally stopped machine hazardous.

### Alignment is part of energy efficiency

Even a correctly sized motor can be damaged by incorrect mounting. Misaligned couplings introduce bending loads. Excessive belt tension increases radial bearing load. Insufficient tension allows slip and heat. A poor foundation can amplify vibration. Temperature rise may reflect a combination of mechanical misalignment, electrical losses, and inadequate cooling.

Good maintenance uses quantitative baselines: approximate shaft speed, normal current under a defined load, bearing temperature trend, belt condition, pulley alignment, and the sound of healthy operation. It also records changes made before a fault appeared. If a new pulley was installed immediately before the fan began overloading the motor, the changed ratio deserves examination before the motor is condemned.

There is a broader lesson here. Most machines are chains of energy conversion and constraints. Troubleshooting becomes efficient when the chain is drawn explicitly, and each suspected fault has a predicted observation that could distinguish it from its rivals. Replacing parts becomes the final step of a diagnosis rather than a substitute for one.

## Balancing, Vibration, and Resonance

A ventilation fan is quiet at low speed and rattles badly at one particular speed. When turned faster, the rattle becomes less obvious. It is tempting to decide that speed itself must be wearing out the bearings. But a system that behaves worst in a narrow band of speed may be revealing resonance: the forcing happens to match a vibration mode of the structure. The important distinction is between the source of motion and the response of everything connected to it.

### Every rotating machine gives us a frequency

A shaft rotating at eighteen hundred revolutions per minute completes thirty revolutions each second. Its one-times rotational frequency is thirty hertz. If the center of mass of a wheel lies slightly away from the rotation axis, that eccentric mass produces a rotating force whose direction changes once per revolution. For a simple model with eccentric mass times offset fixed, the force amplitude grows with the square of angular speed. Double the speed and, all else equal, the imbalance force quadruples.

That is a reason why small misalignment or weight differences can become more consequential at higher speed. It is not evidence that every vibration at rotational frequency comes from imbalance. Bent shafts, coupling issues, pulleys, fans, and structural supports can create several different excitation patterns. A two-times component can arise from certain misalignment effects, but frequency alone never proves a fault mechanism.

Now consider the machine's structure. It has masses connected by supports with stiffness and damping. Every such assembly has natural frequencies and associated mode shapes. In a simple mass-spring approximation, the undamped natural frequency increases with the square root of stiffness and decreases with the square root of mass. Adding a stiff brace may shift a resonance; adding mass may shift it the other way. Those changes can improve or worsen behavior depending on operating frequencies.

### Why one speed can be worse than another

Imagine pushing a playground swing. When your pushes are timed near the swing's natural period, energy accumulates in its motion. Push very slowly or very quickly and the same repeated effort may produce much less amplitude. Machinery can behave similarly, except its forcing comes from rotating imbalance, reciprocating parts, tooth engagement, turbulence, or electrical excitation.

Damping dissipates vibration energy. A vibrating structure cannot accumulate energy forever because friction, material losses, and fluid drag resist motion. But near resonance, a small periodic force may produce much larger movement than off resonance. Moving through resonance rapidly during startup is sometimes acceptable for equipment designed to do so; running continuously at a critical speed may not be. Whether a machine can safely cross or operate near a resonance depends on its design.

The word balancing describes a particular remedy. Static balance attempts to align the mass distribution so a rotor does not have a net eccentric tendency to settle heavy-side-down under gravity when supported appropriately. Dynamic balancing addresses the rotating unbalance forces and couples that can occur in different planes. A long rotor can be statically balanced and still develop a couple that excites bearings at speed. Adding random weights by feel is not the same as measuring amplitude and phase and making a controlled correction.

### Look for the route from the rotor to the room

A fan can shake a whole room because its vibration travels through the housing, brackets, ducting, joists, and walls. The loudest panel may be a resonator rather than the original source. Likewise, a washing machine with an uneven load can excite a flexible floor. Changing mounting feet or isolation elements can alter how much motion reaches the building without eliminating the imbalance in the drum.

Vibration isolators are springs with damping. They can reduce transmitted forces over suitable frequency ranges, but a soft mount introduces its own natural frequency and can allow larger low-frequency movement. The correct isolator depends on static load, operating speed, startup transients, and restraint requirements. An overly soft mount may let a machine strike nearby piping or ductwork. Rubber pads are not a universal solution.

### Listen, measure, and compare operating states

A bearing with a damaged race may produce repetitive impacts and characteristic high-frequency features. A rubbing fan might make a scraping noise whose timing follows rotation, and a loose housing may generate broad rattling. But acoustics is indirect: structure, microphones, room reflections, and the human ear change what is heard. Maintenance diagnosis becomes more reliable when a sound observation is paired with visual checks, temperature, operating speed, historical trend, and, where appropriate, vibration data from accelerometers.

A vibration sensor measures acceleration rather than directly measuring displacement. Displacement, velocity, and acceleration emphasize different frequency ranges; mathematically, differentiation multiplies a sinusoid by angular frequency. At high frequency the acceleration can be large while displacement is small. Comparing raw readings without sensor units, attachment method, sampling rate, and machine speed can be misleading.

Sampling introduces another trap. If data are recorded too slowly, high-frequency motion can appear at a lower false frequency through aliasing. A machine that shows a neat-looking graph is not necessarily well instrumented. Trends are most useful when measured under comparable loads and speeds, and when sensor locations remain consistent.

### Diagnose before adding mass or replacing bearings

Return to the fan that rattles only at one speed. First inspect guards, mounting bolts, blades, housings, contact points, and whether the driven load has changed. Then compare behavior at stable speeds, keeping clear of moving equipment. If the response peaks in a narrow speed band, investigate structural resonances and forcing frequencies. If amplitude grows steadily with speed, imbalance might deserve more attention, but other mechanisms can share that pattern. A loose fastener can make a resonant problem worse without being the initial rotating-force source.

A mechanic learns two separate questions: what force is exciting the machine, and what makes the surrounding structure respond so strongly? Balancing reduces an excitation. Stiffness, damping, isolation, and resonance management change the response. Separating these questions prevents repairing the loudest symptom while leaving the cause untouched.

## Condition Monitoring of Rotating Equipment

Those observations become more informative when their changes are tracked rather than treated as isolated readings.

A ventilation fan has always made a low hum. Recently the hum has acquired a faint rattle, and one bearing housing feels warmer than it did last month. Should the fan be replaced now, or simply watched? Condition monitoring is the practice of making changes like these measurable. It does not predict failure by magic; it helps distinguish normal operating variation from a developing physical defect.

### A rotating machine leaves several signatures

A shaft carries torque from a motor through bearings, couplings, gears, or belts to a load. Problems can appear as vibration, temperature rise, acoustic changes, power consumption, lubricant contamination, reduced throughput, or increasing time to start. Each is a symptom of how energy is being transmitted and dissipated.

An out-of-balance rotor often produces vibration related to its running speed. Misalignment of coupled shafts can excite other directions and harmonics. A damaged rolling bearing may produce repeated impact signatures tied to the geometry of its elements. A loose mounting may rattle at particular speeds. These are helpful physical explanations, but a single sound or frequency peak is rarely a unique diagnosis. Structural resonance, nearby machinery, and load changes may create similar observations.

Monitoring begins with a baseline measured when equipment is believed to be functioning correctly, in a known operating state. A machine at full load and high speed may vibrate more than at light load even with no defect. Comparing readings taken at different speed, temperature, mounting condition, and load without noting those differences can manufacture a false alarm.

### Temperature: useful, but ambiguous

A bearing housing warms from friction and from heat conducted through the shaft or frame. Lubricant viscosity, ambient temperature, rotational speed, alignment, and process heat all affect the number. A rise relative to an established baseline at comparable load and ambient condition deserves attention. But a housing that is 'hot to the touch' is neither a calibrated measurement nor a safe test.

Choose repeatable sensor locations and a suitable instrument. A contact probe can measure a point but may lag changes. An infrared instrument has a wider view and depends on surface emissivity. A polished steel housing can reflect another hot object and provide misleading apparent temperature. Record the surface condition, measuring distance and geometry, not just a temperature number.

Suppose the housing is eight degrees warmer than its normal value. That observation becomes more persuasive if vibration also rises, lubricant changes color, and the temperature tracks load. It remains possible that ambient cooling has changed, so inspect airflow and nearby heat sources. Monitoring is a search for corroboration, not an excuse to declare a bearing failed from one reading.

### Vibration requires both frequency and context

A handheld vibration meter may summarize overall vibration in displacement, velocity, or acceleration. More advanced instruments capture a time waveform and spectrum. These are different windows into the same motion. A large low-frequency displacement may correspond to modest acceleration, while a small high-frequency impact can create a strong acceleration signal. The appropriate measure depends on the equipment and defect under investigation.

Rotational speed is a critical reference. A shaft turning at eighteen hundred revolutions per minute completes thirty revolutions each second. A vibration component near thirty hertz may therefore be related to once-per-revolution excitation, but it is not proof of imbalance. Harmonics at multiples of running speed and components at bearing or gear frequencies require machine-specific interpretation. The same mechanical frequency can also coincide with a supporting structure's resonance.

A tachometer reading, speed log, and sensor placement help interpret spectra. Use sensors mounted in the same orientation and location on repeat visits, preferably on rigid accessible bearing housings. Readings from a flexible cover cannot be compared directly with readings on the bearing block. Do not expose rotating shafts, belts, or couplings merely to attach a probe. Guarding and lockout procedures determine when installation and inspection are permissible.

### Establish thresholds that lead to action

A good monitoring plan defines what equipment is important, which failures matter, what signals can reveal them, and how often readings should be taken. A low-consequence exhaust fan can tolerate a different response plan from a machine whose failure would cause injury or widespread damage. Trends can be more useful than a one-time pass/fail number: steadily increasing vibration over several visits may justify planned maintenance before a hard threshold is reached.

Yet trends can be noisy. A recently changed motor speed, process load, bearing type, or lubrication interval may make the old baseline obsolete. Reestablish a new baseline after documented changes. Keep a record of maintenance actions and measure again afterward. If a coupling replacement causes vibration to increase, the new data may reveal installation misalignment even though the old component was worn.

Consider a pump that starts vibrating only when a suction tank is nearly empty. The pattern may arise from cavitation or inadequate inlet conditions, not a worn rotor. A bearing replacement performed without checking suction conditions will not remove the initiating cause. The most valuable data include process state alongside machine state.

Condition monitoring does not eliminate the need for safe shutdown or direct inspection. Strong mechanical impacts, rapid heating, smoke, leakage, or signs of impending structural failure demand prompt action rather than waiting for another sample. For ordinary trends, build hypotheses, choose discriminating tests, and plan repair around both condition and consequences.

The central skill is learning what a machine's normal operating signature looks like and recognizing meaningful departures. Sound, heat, vibration, current, and process performance become informative when recorded under comparable conditions. Monitoring tells you when to investigate; thoughtful mechanical diagnosis tells you what to repair.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Springs, Stored Energy, and Damping

**Track:** Mechanical Systems and Repair. **Background:** force, torque, friction and bearings. **Purpose:** distinguish compliance, stored energy, damping, and failure in moving systems.

#### Technical companion (non-spoken)

##### Ideal model

For a linear spring, `F = -kx` and stored elastic energy `U = 1/2 kx^2`. For a viscously damped, forced single-degree-of-freedom model: `m x'' + c x' + kx = F(t)`. Undamped natural angular frequency: `omega_n = sqrt(k/m)`; damping ratio: `zeta = c/(2 sqrt(km))`. Real elastomers, friction dampers, gas struts, and nonlinear linkages may not obey these idealizations.

##### Failure-mode distinctions

List stored energy sources separately: compressed springs, torsion springs, raised masses, gas pressure, hydraulic accumulators, spinning rotors and capacitors. Isolation of electrical power does not discharge them. Do not disassemble loaded garage-door springs, pressurized suspensions or similar mechanisms merely to reproduce a classroom example; use equipment-specific procedures and qualified service.

#### Selected reading and claim sources (non-spoken)

- `openstax-spring-oscillation` — [OpenStax College Physics, Hooke’s Law: Stress and Strain Revisited](https://openstax.org/books/college-physics/pages/16-1-hookes-law-stress-and-strain-revisited). Linear restoring force, oscillation and damping as physical mechanisms.
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.

### Failure Diagnosis from Sound, Heat, and Motion

**Track:** Mechanical Systems. **Background:** Bearings, gears, friction, lubrication, fits, and fatigue. **Purpose:** infer failure mechanisms from measured changes rather than changing parts by intuition.

#### Technical companion (non-spoken)

##### Pattern-to-test table

| Pattern | Candidate mechanism | Evidence that discriminates |
|---|---|---|
| One impulse per shaft turn | Rub, damaged feature, eccentricity | Confirm speed synchrony and location |
| Vibration appears under load | Misalignment, support flexibility, process force | Compare known load states and operating limits |
| Pump crackling at low inlet pressure | Cavitation or entrained gas | Suction conditions, fluid temperature, performance curve |
| Warm casing with no output | Friction or internal energy loss | Input power, shaft/output motion, control state |

##### Data record

Keep measured variables with units and operating state: RPM, load, current or power, input/output flow if relevant, temperature sensor type and position, vibration sensor placement, and maintenance history. Use manufacturer acceptance limits for judgments.

**Review boundary:** Examples are hypothesis-generating, not component diagnoses. Never bypass guards, remove interlocks, or measure near exposed moving machinery without suitable procedures and qualifications.

#### Selected reading and evidence records (non-spoken)

- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `skf-grease` — [SKF Evolution, Grease Lubrication Mechanisms in Rolling Bearing Systems](https://evolution.skf.com/us/grease-lubrication-mechanisms-in-rolling-bearing-systems/). Grease churning, replenishment, starvation and film breakdown.

### Motors, Drives, and Mechanical Fault Isolation

**Track:** Mechanical Systems and Repair. **Background:** gears, bearings, friction, fits, and performance curves. **Purpose:** trace energy conversion through an electric motor and its drive so that electrical, mechanical, and load faults can be distinguished.

#### Technical companion (non-spoken)

##### Equations and example

- Rotational mechanical power: `P_out = torque * angular_speed` in consistent SI units.
- For `torque = 4 N·m` at `1800 rpm`, `angular_speed ≈ 188.5 rad/s`, hence `P_out ≈ 754 W`.
- Ideal belt drive: `n_driven/n_motor = D_motor/D_driven`. Real behavior differs due to slip, compliance, and losses.
- Motor efficiency `η = P_out/P_electrical_in` under defined operating conditions.

##### Hypothesis table

| Symptom | Candidate mechanism | Discriminating evidence |
|---|---|---|
| Motor near normal speed; load slow | Belt slip or transmission | Compare shaft speeds and belt condition |
| Both shafts slow; motor high current | Excess load / electrical problem | Rated load, electrical measurements, mechanical condition |
| Bearing housing hot | Misalignment, lubrication, damage | Temperature trend, alignment and vibration assessment |
| Trips on start | Stall, start circuit, supply, protection | Fault sequence, safe qualified testing |

##### Work boundaries

Rotating equipment can start automatically. Electrical tests, guard removal, lockout/tagout, and stored energy control require applicable training and standards. Do not bypass overload protection or repeatedly energize a stalled motor as a diagnostic shortcut.

#### Selected reading and evidence records (non-spoken)

- `doe-electric-motor-systems` — [US Department of Energy, Motor Systems (Industrial Technologies Office)](https://www.energy.gov/cmei/ito/motor-systems). Motor load, alignment, drive losses and troubleshooting; linked technical bulletins
- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Moment arm and torque

### Balancing, Vibration, and Resonance

### 010000 — Balancing, Vibration, and Resonance

#### Technical companion (non-spoken)

##### Models and calculations

- Rotational frequency `f = RPM/60`. At `1800 RPM`, one-times forcing is `30 Hz`; distinguish one-times, harmonics, gear-mesh, and other mechanical excitation frequencies.
- Simple imbalance-force amplitude `F = m e ω²`; this is an idealized point-mass/eccentricity model, not a field-balancing procedure.
- Linear undamped natural frequency `f_n = (1 / 2π) √(k/m)`; mode shapes, damping, multiple axes, and supports make real machines more complex.
- Conversion among sinusoidal displacement, velocity, acceleration multiplies by `ω` at each derivative, affecting diagnostics.

##### Diagnosis exercise

A fan has its strongest cabinet vibration at 900 RPM but strongest bearing vibration at 1800 RPM. Sketch multiple hypotheses: an enclosure resonance near 15 Hz, bearing defect, loose mount, and unbalance. Specify which additional measurements would separate them.

##### Safety / interpretation

Balance changes and testing near critical speeds require appropriate equipment and precautions. Never remove guards or touch moving equipment to obtain observations. SKF bearing literature and general oscillator theory support mechanisms but not a particular machine's certified limits.

#### Selected reading and evidence records (non-spoken)

- `openstax-spring-oscillation` — [OpenStax College Physics, Hooke’s Law: Stress and Strain Revisited](https://openstax.org/books/college-physics/pages/16-1-hookes-law-stress-and-strain-revisited). Linear restoring force, oscillation and damping as physical mechanisms
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms
- `doe-electric-motor-systems` — [US Department of Energy, Motor Systems (Industrial Technologies Office)](https://www.energy.gov/cmei/ito/motor-systems). Motor load, alignment, drive losses and troubleshooting; linked technical bulletins

### Condition Monitoring of Rotating Equipment

### 017000 — Condition Monitoring of Rotating Equipment

#### Technical companion (non-spoken)

**Speed calculation:** rpm / 60 = revolutions per second = running-speed frequency in Hz. At 1,800 rpm, 1× running speed is 30 Hz. A peak at 30 Hz is not a diagnosis by itself; identify the actual shaft speed and evaluate harmonics and load.

**Baseline record:** machine ID, operating speed, process throughput, bearing location and sensor axis, mounting method, temperature, lubricant, ambient conditions, vibration metric and units, maintenance state, date/time.

**Trend thought experiment:** Vibration grows only when a pump's inlet tank is low. Compare suction conditions, available head, noise pattern, flow and vibration before replacing bearings. Rising temperature without vibration change merits a different differential.

**Guarding:** Never reach into moving belts/couplings or remove guards for a convenient reading. Sensor mounting, lockout and plant safety procedures determine allowable access. Thresholds must be appropriate to the machine, instrument and consequence, not a universal sound/temperature limit.

#### Selected reading and source locators (non-spoken)

- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `skf-grease` — [SKF Evolution, Grease Lubrication Mechanisms in Rolling Bearing Systems](https://evolution.skf.com/us/grease-lubrication-mechanisms-in-rolling-bearing-systems/). Grease churning, replenishment, starvation and film breakdown.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.
