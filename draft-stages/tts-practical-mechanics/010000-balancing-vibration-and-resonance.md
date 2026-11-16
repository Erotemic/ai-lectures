# 010000 — Balancing, Vibration, and Resonance

<!-- BEGIN SPOKEN LECTURE -->

A ventilation fan is quiet at low speed and rattles badly at one particular speed. When turned faster, the rattle becomes less obvious. It is tempting to decide that speed itself must be wearing out the bearings. But a system that behaves worst in a narrow band of speed may be revealing resonance: the forcing happens to match a vibration mode of the structure. The important distinction is between the source of motion and the response of everything connected to it.

## Every rotating machine gives us a frequency

A shaft rotating at eighteen hundred revolutions per minute completes thirty revolutions each second. Its one-times rotational frequency is thirty hertz. If the center of mass of a wheel lies slightly away from the rotation axis, that eccentric mass produces a rotating force whose direction changes once per revolution. For a simple model with eccentric mass times offset fixed, the force amplitude grows with the square of angular speed. Double the speed and, all else equal, the imbalance force quadruples.

That is a reason why small misalignment or weight differences can become more consequential at higher speed. It is not evidence that every vibration at rotational frequency comes from imbalance. Bent shafts, coupling issues, pulleys, fans, and structural supports can create several different excitation patterns. A two-times component can arise from certain misalignment effects, but frequency alone never proves a fault mechanism.

Now consider the machine's structure. It has masses connected by supports with stiffness and damping. Every such assembly has natural frequencies and associated mode shapes. In a simple mass-spring approximation, the undamped natural frequency increases with the square root of stiffness and decreases with the square root of mass. Adding a stiff brace may shift a resonance; adding mass may shift it the other way. Those changes can improve or worsen behavior depending on operating frequencies.

## Why one speed can be worse than another

Imagine pushing a playground swing. When your pushes are timed near the swing's natural period, energy accumulates in its motion. Push very slowly or very quickly and the same repeated effort may produce much less amplitude. Machinery can behave similarly, except its forcing comes from rotating imbalance, reciprocating parts, tooth engagement, turbulence, or electrical excitation.

Damping dissipates vibration energy. A vibrating structure cannot accumulate energy forever because friction, material losses, and fluid drag resist motion. But near resonance, a small periodic force may produce much larger movement than off resonance. Moving through resonance rapidly during startup is sometimes acceptable for equipment designed to do so; running continuously at a critical speed may not be. Whether a machine can safely cross or operate near a resonance depends on its design.

The word balancing describes a particular remedy. Static balance attempts to align the mass distribution so a rotor does not have a net eccentric tendency to settle heavy-side-down under gravity when supported appropriately. Dynamic balancing addresses the rotating unbalance forces and couples that can occur in different planes. A long rotor can be statically balanced and still develop a couple that excites bearings at speed. Adding random weights by feel is not the same as measuring amplitude and phase and making a controlled correction.

## Look for the route from the rotor to the room

A fan can shake a whole room because its vibration travels through the housing, brackets, ducting, joists, and walls. The loudest panel may be a resonator rather than the original source. Likewise, a washing machine with an uneven load can excite a flexible floor. Changing mounting feet or isolation elements can alter how much motion reaches the building without eliminating the imbalance in the drum.

Vibration isolators are springs with damping. They can reduce transmitted forces over suitable frequency ranges, but a soft mount introduces its own natural frequency and can allow larger low-frequency movement. The correct isolator depends on static load, operating speed, startup transients, and restraint requirements. An overly soft mount may let a machine strike nearby piping or ductwork. Rubber pads are not a universal solution.

## Listen, measure, and compare operating states

A bearing with a damaged race may produce repetitive impacts and characteristic high-frequency features. A rubbing fan might make a scraping noise whose timing follows rotation, and a loose housing may generate broad rattling. But acoustics is indirect: structure, microphones, room reflections, and the human ear change what is heard. Maintenance diagnosis becomes more reliable when a sound observation is paired with visual checks, temperature, operating speed, historical trend, and, where appropriate, vibration data from accelerometers.

A vibration sensor measures acceleration rather than directly measuring displacement. Displacement, velocity, and acceleration emphasize different frequency ranges; mathematically, differentiation multiplies a sinusoid by angular frequency. At high frequency the acceleration can be large while displacement is small. Comparing raw readings without sensor units, attachment method, sampling rate, and machine speed can be misleading.

Sampling introduces another trap. If data are recorded too slowly, high-frequency motion can appear at a lower false frequency through aliasing. A machine that shows a neat-looking graph is not necessarily well instrumented. Trends are most useful when measured under comparable loads and speeds, and when sensor locations remain consistent.

## Diagnose before adding mass or replacing bearings

Return to the fan that rattles only at one speed. First inspect guards, mounting bolts, blades, housings, contact points, and whether the driven load has changed. Then compare behavior at stable speeds, keeping clear of moving equipment. If the response peaks in a narrow speed band, investigate structural resonances and forcing frequencies. If amplitude grows steadily with speed, imbalance might deserve more attention, but other mechanisms can share that pattern. A loose fastener can make a resonant problem worse without being the initial rotating-force source.

A mechanic learns two separate questions: what force is exciting the machine, and what makes the surrounding structure respond so strongly? Balancing reduces an excitation. Stiffness, damping, isolation, and resonance management change the response. Separating these questions prevents repairing the loudest symptom while leaving the cause untouched.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Models and calculations

- Rotational frequency `f = RPM/60`. At `1800 RPM`, one-times forcing is `30 Hz`; distinguish one-times, harmonics, gear-mesh, and other mechanical excitation frequencies.
- Simple imbalance-force amplitude `F = m e ω²`; this is an idealized point-mass/eccentricity model, not a field-balancing procedure.
- Linear undamped natural frequency `f_n = (1 / 2π) √(k/m)`; mode shapes, damping, multiple axes, and supports make real machines more complex.
- Conversion among sinusoidal displacement, velocity, acceleration multiplies by `ω` at each derivative, affecting diagnostics.

### Diagnosis exercise

A fan has its strongest cabinet vibration at 900 RPM but strongest bearing vibration at 1800 RPM. Sketch multiple hypotheses: an enclosure resonance near 15 Hz, bearing defect, loose mount, and unbalance. Specify which additional measurements would separate them.

### Safety / interpretation

Balance changes and testing near critical speeds require appropriate equipment and precautions. Never remove guards or touch moving equipment to obtain observations. SKF bearing literature and general oscillator theory support mechanisms but not a particular machine's certified limits.

## Selected reading and evidence records (non-spoken)

- `openstax-spring-oscillation` — [OpenStax College Physics, Hooke’s Law: Stress and Strain Revisited](https://openstax.org/books/college-physics/pages/16-1-hookes-law-stress-and-strain-revisited). Linear restoring force, oscillation and damping as physical mechanisms
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms
- `doe-electric-motor-systems` — [US Department of Energy, Motor Systems (Industrial Technologies Office)](https://www.energy.gov/cmei/ito/motor-systems). Motor load, alignment, drive losses and troubleshooting; linked technical bulletins
