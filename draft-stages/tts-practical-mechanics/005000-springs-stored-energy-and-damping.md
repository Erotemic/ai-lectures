# 005000 — Springs, Stored Energy, and Damping

**Track:** Mechanical Systems and Repair. **Background:** force, torque, friction and bearings. **Purpose:** distinguish compliance, stored energy, damping, and failure in moving systems.

<!-- BEGIN SPOKEN LECTURE -->

# Why a machine keeps moving after you stop pushing

Press down on a bicycle suspension and release it. A spring returns energy that you supplied while compressing it. If there were no dissipative mechanisms, the mass might oscillate for a long time. A damper makes that motion settle more quickly by converting some mechanical energy into heat. The spring and the damper solve different problems. Conflating them leads to poor repair decisions, uncomfortable vehicles, and vibrating equipment.

A spring is not necessarily a visible coil. A leaf spring, a thin metal strip, a flexing plastic latch, an elastic seal, and a loaded machine frame all deform and can store elastic energy. In a range of small deformations, many of them can be approximated by Hooke's law: restoring force proportional to displacement from equilibrium. More displacement means more restoring force. This is a model, not a guarantee that all real springs obey a straight line through their entire travel.

## Force is not the same as stored energy

Imagine compressing a spring gently. At first it pushes back only a little. As compression increases, the force rises. The work you do accumulates as potential energy. For a linear spring, doubling compression doubles the force but quadruples stored energy. That distinction matters because a spring can release substantial energy even if a technician has been moving it slowly.

A compressed spring in a mechanism can drive a latch, return a valve, or hold a door shut. A torsion spring stores energy through twist rather than direct extension. Gas springs and hydraulic accumulators involve pressurized fluid or gas as well as mechanical motion. A counterweight stores gravitational potential energy. There are several ways for a machine to retain energy after its power switch is off. Before disassembling a device, the question is not merely whether its motor is stopped, but what forces and pressures remain constrained.

## Motion contains mass, stiffness, and damping

Suspend a mass from a spring. Pull it down and let go. The spring pulls it toward equilibrium, but inertia carries it past. The spring pulls back in the other direction. The resulting back-and-forth motion is an oscillation. How quickly the system oscillates depends on its effective mass and stiffness. How rapidly it settles depends on damping.

An ideal mass-spring system has a natural frequency. Real machines have friction, material hysteresis, air drag and engineered dampers that remove energy. Too little damping can permit repeated bouncing, rattling or resonance. Excessive damping may prevent a device from responding as intended, turning fast motion into slow, sluggish motion. Damping is not universally 'more is better.' It must match the function.

Consider a vehicle shock absorber. It is mainly a damper, not the component that holds the vehicle's static weight. The spring supports and positions the vehicle; the damper resists movement and helps control oscillations. If a vehicle bounces repeatedly after a disturbance, inadequate damping may be one hypothesis. But tire condition, bushings, spring damage, mounting points, and suspension geometry can also cause poor behavior. The observation alone does not identify a single failed part.

## Resonance changes the stakes

A washing machine that starts to vibrate strongly at one spin speed but becomes calmer at another may be passing through a range where its forcing frequency is close to a structural natural frequency. The severity depends on imbalance, stiffness, damping and how the appliance is supported. Changing only the spin speed might move away from the bad region without correcting the imbalance. Replacing an intact damper might not correct an uneven floor or loose mounting.

The same idea applies to fans, machine-tool spindles, vehicle suspension and building components. A periodic force can repeatedly put energy into a flexible system. Near resonance, response can become much larger than expected from a static force calculation. An engineer may solve the problem by modifying stiffness, mass, excitation, isolation or damping. Those are distinct levers.

Rubber mounts make the tradeoff visible. Soft mounts can isolate high-frequency vibration, but they allow more displacement at low frequencies and during start-stop transients. Stiffer mounts constrain movement but transmit more vibration. A well-chosen mount matches the machine's mass, disturbance frequencies and allowable motion, rather than simply being the softest material available.

## Diagnose what the energy is doing

Picture a garage door that moves abruptly after a spring repair. The defect might involve spring adjustment, cable routing, damaged rollers, friction in tracks, or a failed damping and control mechanism. Because loaded springs and moving door components can retain substantial energy, dismantling them without the proper procedure is not an appropriate diagnostic experiment. The physical analysis can still begin with observation: which component stores energy, which transmits it, and which dissipates it?

For a safe tabletop demonstration, compare an elastic band gently stretched within its working range to a strip of soft foam slowly compressed. Observe how much energy appears to return, and how much is dissipated. Then compare a ruler flexed and released with the same ruler constrained by a soft pad. The point is not precise measurement; it is to feel that stiffness, stored energy and damping have different signatures.

Once you can label those roles, many repairs become clearer. A spring can be intact while a damper fails. A damper can be healthy while an attachment loosens. A machine can vibrate because its excitation has changed even though none of its supports broke. The mechanic's task is to follow energy through the system and identify which function no longer behaves as intended.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Ideal model

For a linear spring, `F = -kx` and stored elastic energy `U = 1/2 kx^2`. For a viscously damped, forced single-degree-of-freedom model: `m x'' + c x' + kx = F(t)`. Undamped natural angular frequency: `omega_n = sqrt(k/m)`; damping ratio: `zeta = c/(2 sqrt(km))`. Real elastomers, friction dampers, gas struts, and nonlinear linkages may not obey these idealizations.

### Failure-mode distinctions

List stored energy sources separately: compressed springs, torsion springs, raised masses, gas pressure, hydraulic accumulators, spinning rotors and capacitors. Isolation of electrical power does not discharge them. Do not disassemble loaded garage-door springs, pressurized suspensions or similar mechanisms merely to reproduce a classroom example; use equipment-specific procedures and qualified service.

## Selected reading and claim sources (non-spoken)

- `openstax-spring-oscillation` — [OpenStax College Physics, Hooke’s Law: Stress and Strain Revisited](https://openstax.org/books/college-physics/pages/16-1-hookes-law-stress-and-strain-revisited). Linear restoring force, oscillation and damping as physical mechanisms.
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
