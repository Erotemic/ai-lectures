# Match a pump to its inlet, network, and seal

<!-- BEGIN SPOKEN LECTURE -->

# Match a pump to its inlet, network, and seal

## Pumps, Fans, and Performance Curves

Imagine two identical water pumps installed in different circuits. One moves water freely through a short, wide pipe. The other pushes through a tall rise, narrow pipes, several valves, and a clogged strainer. A catalog may give each pump the same nominal capacity, yet their measured flow rates differ. The pump is not behaving mysteriously. Its performance is coupled to the resistance imposed by the rest of the system.

A pump adds mechanical energy to a liquid. A fan adds it to a gas. In both cases a rotating impeller can create a pressure difference and sustain flow, but the outcome depends on the machine's geometry, speed, fluid properties, and connected system. A performance curve represents this interaction more usefully than a single advertised flow number.

### What head means

For a liquid pump, head describes energy imparted per unit weight of fluid and is often expressed in meters or feet of liquid. It is closely related to pressure but not identical in every context, because elevation and velocity contributions can matter. The system must overcome static head, if any, plus frictional losses through pipes, fittings, and components. The static contribution can remain even at zero flow; friction generally increases as flow rises.

A centrifugal pump typically has a pump curve where available head declines as flow increases at a fixed speed and impeller diameter. The system curve often rises with flow because losses increase. Draw both on the same axes. Their intersection is the operating point. A valve partly closed downstream raises resistance and moves the operating point toward less flow. Replacing a clogged filter can reduce resistance and change operating flow without touching the pump.

Suppose a pump is said to deliver fifty liters per minute. Does that number apply against a two-meter lift or a twenty-meter lift? Is it for clean water or a viscous fluid? At what speed? The stated quantity is incomplete without a test condition. The same caution applies to fans rated in cubic feet per minute. A free-air rating may say little about delivery through restrictive ducts and filters.

### The efficiency island

A pump converts electrical input through motor and shaft into useful hydraulic power, but some energy becomes heat, turbulence, and friction. Its efficiency changes with operating point. A best-efficiency point, or BEP, is a region where a given centrifugal pump often runs with relatively favorable hydraulic behavior. Far from that region, recirculation, vibration, noise, and component wear may increase. The correct operating point still needs to satisfy the actual duty; maximizing theoretical efficiency while failing to deliver required flow is not a successful design.

For water, useful hydraulic power can be estimated from density multiplied by gravity, flow rate, and developed head. The input mechanical or electrical power must exceed the useful output when losses are present. If a motor draws large power yet produces little useful flow, the system may be badly matched, obstructed, or mechanically defective. Power alone does not identify the cause, but it belongs in the evidence.

### Speed changes everything, but conditionally

For a geometrically unchanged centrifugal machine operating in comparable conditions, approximate affinity relationships say flow varies with rotational speed, head with the square of speed, and power with its cube. These are scaling relations for corresponding operating states, not guaranteed predictions for every installed system. A large static head, changing efficiency, cavitation, or a controller that changes the operating point can make naive scaling misleading.

That qualification explains a common energy-saving idea. Reducing fan or pump speed can reduce power substantially when the application permits lower flow. Throttling flow with a restrictive damper or valve may waste energy as pressure loss. But a variable-speed drive must still keep the process within required flow, minimum speed, cooling, and safety limits.

### Cavitation and the suction side

A pump also depends on the pressure available at its inlet. If local pressure falls sufficiently for vapor bubbles to form, the bubbles can collapse as they move to higher-pressure regions. Cavitation can cause noise, vibration, erosion, and lost performance. The concept of net positive suction head distinguishes the margin available in the installation from what the pump requires. It is not enough to calculate discharge pressure while ignoring a long, undersized suction line or elevated liquid temperature.

Fans have their own unstable regions, and filters become more restrictive as they collect dust. A whining motor, rattling housing, rising operating temperature, or declining flow may indicate mechanical wear, but it may also reflect a changed system curve. Diagnose both sides of the coupling.

### A curve is a conversation between components

The most productive troubleshooting sequence records the intended flow and pressure or head; collects the measured duty under known conditions; inspects filters, valves, air paths, and inlet conditions; and compares the observations with a credible machine curve. If an impeller is damaged, the machine curve itself may have changed. If a valve is partly shut, the system curve has changed. Those hypotheses point to different repairs.

A pump and a fan are excellent lessons in systems thinking. Neither supplies an independent fixed flow just because a nameplate says it can. Performance emerges from a machine pushing against a network, and proper diagnosis asks what changed in the machine, the network, or both.

## Pump Cavitation, Inlet Conditions, and Impeller Wear

The pump-and-network model has an inlet boundary as well as an outlet demand. That boundary becomes central when cavitation appears.

A pump that once ran quietly now sounds as though small stones are bouncing inside it. The flow may be low and the housing warmer than before. One possibility is cavitation: vapor bubbles form in a low-pressure region of the liquid and collapse as pressure rises. But not every rattling pump cavitates. Bearings, air ingestion, loose mounts, a damaged impeller, and operating far from the intended flow can sound similar. Understanding the inlet is the first step toward separating those causes.

### A pump does not create water at its inlet

A centrifugal pump uses a rotating impeller to add energy to liquid. The impeller accelerates and redirects the liquid, and the pump casing helps convert part of that energy into pressure. For the pump to operate reliably, water must reach its inlet at a pressure and flow compatible with the impeller's demands. A clogged suction strainer, a long narrow inlet, a partially closed valve, or excessive lift can reduce the available inlet pressure while the pump is trying to draw more liquid.

Every liquid has a vapor pressure that depends on temperature. If local absolute pressure falls sufficiently near that value, some liquid flashes into vapor. The bubbles then move toward higher-pressure regions and collapse. Repeated collapse can produce noise, vibration, performance loss, and pitted metal surfaces. The damage is not just from bubbles being visible in a pipe; it comes from their violent collapse and the localized stresses they create.

An important subtlety is that the ordinary gauge on a pump may read pressure relative to atmosphere. Cavitation depends on absolute pressure relative to the liquid's vapor pressure. A reading of minus a few pounds per square inch on a suction gauge is not directly the value to compare with vapor pressure without accounting for atmospheric pressure and measurement elevation. Temperature matters too: warmer water has a higher vapor pressure and a smaller margin against boiling under reduced pressure.

### Available head versus required head

Pump engineers express inlet margin with net positive suction head, or NPSH. The available NPSH comes from the actual installation: ambient pressure, elevation of the supply, suction losses, and liquid vapor pressure. Required NPSH is associated with a pump's behavior at a particular operating flow, obtained from appropriate manufacturer data. A real installation needs sufficient margin between them, not merely equality in an oversimplified calculation.

Consider two tanks. In the first, the pump sits below the tank's water surface, giving the inlet a favorable hydrostatic head. In the second, the pump stands above the water and must lift it through a long suction line with several elbows. All else equal, the second arrangement has less available inlet head. If a filter clogs or the water gets hotter, its margin may shrink further. This does not prove it is cavitating, but it gives an explanation for why symptoms appear after a change in conditions.

The pump curve tells another story. For a centrifugal pump, head developed typically varies with flow. The system curve describes how the piping and static elevations resist flow. Their intersection determines the operating point. A restriction downstream usually reduces flow; a restriction upstream can both change flow and depress inlet pressure. Throttling a discharge valve and throttling a suction valve are therefore not equivalent, even if both reduce measured delivery. Manufacturer recommendations govern the safe operating range and whether any throttling is permitted.

### Distinguish vapor cavitation from air ingestion

A suction-line leak may admit outside air when the line is below atmospheric pressure. Bubbles can then enter the pump without the local liquid pressure dropping to vapor pressure. The symptom may include loss of prime, unstable flow, air collecting at high points, or visible bubbles where a safe observation point exists. Entrained air can disrupt a pump and may accompany cavitation, but its remedy targets sealing, venting, and inlet arrangement rather than just raising inlet pressure.

A blocked discharge, worn impeller, failing bearing, or poorly aligned coupling can also give low output and vibration. Therefore, build evidence. Record pump speed, inlet and discharge conditions, water temperature, tank level, valve positions, filter condition, flow, motor current when appropriate, and the timing of the noise. Compare with the manufacturer curve. If the sound changes predictably as suction strainer loss increases or tank level falls, that pattern supports an inlet-related hypothesis. It remains a hypothesis until measured conditions and inspection corroborate it.

A familiar maintenance mistake is to replace a damaged impeller without correcting the inlet geometry that damaged it. A new impeller may restore performance briefly, then suffer the same wear. Another error is to oversize a pump to overcome low flow without examining the suction. A more powerful pump can demand more from an already inadequate inlet and worsen the problem.

### Diagnose without creating a hazard

Pumps may contain rotating shafts, hot liquids, pressurized lines, and stored electrical energy. Measurements should be made at designed service points with appropriate equipment; do not loosen a fitting on a running pressurized system to 'see whether there is air.' Any impeller inspection requires proper isolation, depressurization, cooling, and energy control. Do not reach through guarding or put a hand on a suspected rotating component.

Successful correction may involve a cleaned strainer, larger or shorter inlet piping, corrected tank placement, restored fluid level, proper air elimination, or selecting a pump whose operating range matches the real duty. If a damaged impeller is replaced, compare post-repair measurements at the same operating point. The goal is not merely a quieter sound, but adequate flow and inlet margin throughout expected conditions.

The pump is an effective teacher because it reveals a common engineering principle: the output is only as good as the supply conditions. Before blaming the machine that moves the fluid, understand what reaches it and at what pressure.

## Pump Selection, Efficiency, and the Cost of Moving Water

The operating-point model now becomes a selection tool. A pump that is too small may not deliver enough water. A pump that is much larger than necessary can also perform poorly, running far from its preferred operating point while throttles, bypasses and control cycles waste energy. Selection therefore has to match the pump to the pipe system rather than judge either one alone.

The pump has a performance curve. For a centrifugal pump at a particular speed and impeller size, the curve shows how much head the pump can develop at different flow rates. Head is energy per unit weight of fluid, commonly expressed as an equivalent height of liquid. It is a way to compare pressure rise and elevation change in a common unit. The system has its own curve: how much head it needs to move each flow rate through the actual pipework, valves, filters and static elevation difference.

The operating point is where those two curves intersect. If we install a different pump or change the piping resistance, the operating point changes. This is why a pump's advertised maximum flow and maximum head cannot usually be achieved simultaneously. They tend to be opposite ends of its performance curve.

### A system that changes with demand

Consider a small circulation system with a pump pushing water through several branches and a heat exchanger. The elevation changes may largely cancel around a closed loop; much of the required head comes from friction and fittings. Contrast that with a well pump lifting water to a tank above it: the elevation change is a real static component of head. In both systems, pipe friction grows with flow, but their system curves have different shapes and offsets.

Now add a filter. As it accumulates material, its pressure drop at a given flow may increase. The system curve becomes steeper; the same pump moves less water. A technician who observes low delivered flow should not conclude that the pump motor is failing without checking filters, closed valves, air pockets and suction conditions. Replacing the pump can leave the true restriction in place.

Cavitation is another limit. If liquid pressure at the pump inlet becomes too low relative to its vapor pressure, bubbles can form and collapse through the pump, damaging the impeller and reducing performance. Net positive suction head, abbreviated NPSH, describes the available and required suction conditions in a more careful way than a vague instruction to 'keep the inlet open.' Available NPSH depends on absolute inlet pressure, fluid vapor pressure, elevation and losses. Required NPSH is a pump characteristic given for stated conditions. A pump selected near the edge of adequate suction conditions may fail even if its advertised head and flow seem sufficient.

### Efficiency has more than one layer

There is hydraulic power transferred to the liquid, mechanical shaft power delivered to the pump, and electrical power consumed by the motor and drive. These are not equal because each conversion incurs losses. The useful hydraulic power is fluid density times gravitational acceleration times volume flow rate times head, in consistent units.

Suppose water flows at two liters per second through a pump delivering twenty meters of total head. Two liters per second is 0.002 cubic meters per second. With water density approximated as one thousand kilograms per cubic meter, the hydraulic power is about 392 watts. If the hypothetical combined pump-and-motor efficiency is fifty percent, electrical input would be about 784 watts. These numbers are not specifications for a real pump. They show why we must distinguish the energy delivered to water from the energy purchased at the meter.

A pump can be mechanically healthy and still use excessive electricity when operated at an inefficient point. Centrifugal pump curves commonly identify a best efficiency point. That is not a guarantee that the entire installed system reaches the same efficiency. Pipework, controls, motor selection, suction conditions and operating schedules all matter. A pump that frequently runs at half the desired flow through a nearly closed throttling valve may merit a control or system redesign rather than just a new impeller.

### Choose the control method to fit the demand

For a variable-flow application, a variable-frequency drive can change pump speed and shift its performance curve. Under restricted conditions, fan and pump affinity relationships help explain how flow, head and power change with speed. They are approximations with assumptions, not an unconditional promise that reducing speed by ten percent will save an exact percentage of power in every installation. Static lift and changing system demands can defeat a simplistic scaling argument.

Other systems use on-off cycling, staging multiple pumps, a bypass or a pressure-regulating valve. The correct choice depends on required minimum flow, pressure limits, motor cooling, tank size and process needs. A domestic well system, for example, must coordinate the pump, pressure switch or controller, and pressure tank. Excessive cycling can shorten equipment life, but reducing cycle count by allowing improper pressure excursions would not be an improvement.

### Diagnose with a small set of simultaneous measurements

A useful field record includes the pump model, impeller and speed if known, electrical input, inlet and discharge pressures, flow, fluid temperature, filter condition and operating mode. Each pressure should be interpreted relative to the gauge location and elevation. A snapshot taken with the system fully open cannot be compared blindly with a later reading during throttled operation.

Imagine a pump that draws its normal motor current but delivers less flow than last month. Possibilities include a restricted suction screen, a partially closed valve, an air leak, an eroded or damaged impeller, a changed system resistance, or an instrumentation error. Head and flow measured together help distinguish these cases. A low current on some centrifugal pumps may accompany low flow, not proof that the motor has become more efficient. Electrical current by itself is not a reliable hydraulic diagnostic.

If efficiency is the question, compare measured electrical power with a carefully estimated useful hydraulic output, and account for the motor and drive. Verify that the measurement methods are appropriate before calculating a single percentage. Use the manufacturer's performance data to see whether the operating point lies in a reasonable part of the curve. Check whether the energy cost is significant enough to justify changes, and whether the process tolerates them.

Pump selection is therefore a matching problem. A good pump is not the pump with the largest number printed on its box. It is the pump whose curve meets the real system's needs over the operating range, with adequate suction margin, acceptable efficiency and controllable performance.

## Mechanical Seals and Leaks at Rotating Shafts

Performance is not the only outcome to inspect; the rotating shaft also creates a sealing interface.

A centrifugal pump has a steel shaft passing through a housing full of water. The shaft must rotate, but the housing must keep most of the water inside. This is a harder sealing problem than joining two stationary pipe flanges. A static gasket can simply be squeezed between surfaces. A seal around a moving shaft must manage friction, heat, lubrication, pressure and wear while allowing rotation.

The first useful distinction is between sealing a rotating lip against a shaft and sealing two faces that rotate relative to one another. Both are common, but they have different failure mechanisms.

### Lip seals and contact at the shaft

A radial shaft lip seal often uses a flexible lip held against a precision shaft surface, sometimes with a garter spring providing contact force. The lip controls the film of lubricant at the moving interface. It is not necessarily intended to operate completely dry. The seal material must tolerate the fluid, temperature, shaft speed and pressure for which it was selected.

A shaft with a worn groove can leak after installation of a brand-new lip seal. If the replacement lip rides in the same damaged groove, replacing only the rubber may not restore sealing. Shaft runout, misalignment, a rough or damaged installation surface, excessive pressure or a blocked vent can also shorten seal life. An oily trace near a gearbox output may be evidence of wear at the lip, but it may also be fluid migrating from another connection or overfill conditions that increase internal pressure.

The relative speed of the shaft surface rises with its diameter and rotational speed. At the same revolutions per minute, a larger diameter exposes the sealing lip to greater surface travel per unit time. That can change frictional heating and film behavior. A seal catalog therefore specifies operating limits in more than one variable; it cannot be chosen only by matching a nominal diameter.

### Mechanical face seals

A pump mechanical seal works differently. It typically has one face associated with the rotating shaft and one stationary mating face. Springs and hydraulic forces keep the faces in an intended relationship. The opposing surfaces are finished very flat; a thin lubricating film and controlled leakage manage friction and cooling. Secondary seals close off alternate paths around components.

A well-designed mechanical seal is not an absolute zero-leak magic barrier. Controlled passage across the sealing faces can be part of lubrication. The acceptable leakage depends on seal type, service and process fluid. Some systems use single seals with process liquid as the lubricant. Others use dual arrangements with a buffer or barrier fluid and a supporting flush or quench system. That infrastructure matters when the fluid is hot, abrasive, toxic or poorly lubricating.

Imagine a pump that ran dry for several minutes. Its face seal may have lost the fluid film needed to control temperature. Restarting the pump after adding water does not repair a damaged face. Similarly, a pump carrying gritty water may scar the faces. Replacing the seal without addressing suction, filtration, alignment or process conditions can reproduce the failure.

### Diagnose location before naming the fault

A leak at the joint where the pump casing meets a cover is not the same as leakage around a rotating shaft. Nor is condensation on a cold housing. First observe where fluid actually emerges. Record when the leak appears: during startup, only at pressure, after shutdown or continuously. Note temperature, vibration, pump inlet conditions, recent maintenance and whether the leak rate changes with speed.

For a pump that leaks only while rotating, seal-face wear, shaft motion and dynamic pressure deserve consideration. Leakage visible even when stationary can suggest damage or a static sealing path, but the exact diagnosis still depends on seal design and how pressure remains in the casing. A burst of leakage after a hot start may involve thermal movement or lubrication loss. None of these patterns identifies a specific failed part without examination.

Mechanical seals also teach an important principle about tolerances. Two surfaces may appear to touch while microscopic roughness supports a thin fluid film. The wear environment is determined by that micro-scale contact, lubrication, heat extraction and contamination. Surface finishing is therefore functional geometry, not simply aesthetics.

### Replacement is a system repair

Before choosing a replacement, identify the shaft diameter, housing dimensions, pressure, rotational speed, temperature, fluid chemistry and solids content. Inspect the shaft or sleeve for grooves and runout. Inspect bearings and alignment. Verify ventilation or drainage around the seal housing and that required flushes are operating. Components should be installed with clean handling and the manufacturer's approved procedure; finger marks or scratches on precision faces matter.

Stored pressure and rotating equipment energy can make inspection consequential even when a pump is small. Isolation, draining, controlled depressurization and preventing unintended startup are part of the procedure, not separate from understanding the seal.

The durable lesson is that a seal is an interface between a machine's motion and the fluid it contains. Leakage is a symptom emerging from that entire environment. A successful repair restores the film, geometry, force and operating conditions the sealing system was designed to maintain.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Pumps, Fans, and Performance Curves

**Track:** Mechanical Systems and Repair. **Background:** friction, bearings, seals, motors, and fault diagnosis. **Purpose:** learn how a machine and its connected flow system determine one another's actual performance.

#### Technical companion (non-spoken)

##### Curve sketch and calculation

Plot **head** (vertical) versus **flow** (horizontal). Draw a falling centrifugal pump curve and a rising system curve `H_system = H_static + k Q²` (approximation for many turbulent-flow systems). Mark their intersection.

For water, hydraulic power is `P_h = ρ g Q H`. Example: `Q=0.002 m³/s` and `H=15 m` gives `1000 × 9.81 × 0.002 × 15 ≈ 294 W` of useful hydraulic power. If efficiency at that point is 60%, shaft input is about `490 W`, before motor/drive losses. This is **not** a pump or electrical-service selection specification.

##### Fault discrimination

| Symptom | Machine-side possibility | System-side possibility |
|---|---|---|
| Low flow | Worn impeller, wrong speed | Blocked filter, closed valve, excessive head |
| Cavitation-like noise | Inappropriate pump selection | Low inlet pressure, hot liquid, restricted suction |
| High vibration | Damaged bearings/imbalance | Operating far from stable region, poorly supported piping |

**Review boundary:** Use OEM curves and procedures for a real pump or fan. Fluid compatibility, electrical controls, suction conditions, and containment pressure require equipment-specific engineering review.

#### Selected reading and evidence records (non-spoken)

- `doe-hi-pumping-sourcebook` — [US Department of Energy and Hydraulic Institute, Improving Pumping System Performance: A Sourcebook for Industry, Second Edition (2006)](https://www.energy.gov/sites/prod/files/2014/05/f16/pump.pdf). Pump and system curves, BEP, NPSH, pump selection and maintenance.

### Pump Cavitation, Inlet Conditions, and Impeller Wear

### 018000 — Pump Cavitation, Inlet Conditions, and Impeller Wear

#### Technical companion (non-spoken)

**Key distinction.** Vapor cavitation involves local pressure below vapor pressure; air ingestion involves external gas entering the suction. They can coexist. Do not diagnose either from a recording of the noise alone.

**Illustrative NPSH balance.** NPSH_available ≈ (P_surface,absolute − P_vapor)/(ρg) + static liquid elevation above inlet − suction friction losses. Conventions, velocity head, and reference datum depend on the pump calculation. Use manufacturer required-NPSH data and safety margin.

**Trend log.** Flow, speed, temperature, tank level, suction absolute pressure, discharge pressure, strainer differential pressure, vibration, and noise chronology. Compare at consistent operating states.

**Safety and review.** Never open a pressurized or energized pump for a diagnostic shortcut. Pump configuration, margins, material choice, and operating point require model-specific engineering review.

#### Selected reading and source locators (non-spoken)

- `doe-hi-pumping-sourcebook` — [US Department of Energy and Hydraulic Institute, Improving Pumping System Performance: A Sourcebook for Industry, Second Edition (2006)](https://www.energy.gov/sites/prod/files/2014/05/f16/pump.pdf). Pump and system curves, BEP, NPSH, pump selection and maintenance.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `openstax-thermal` — [OpenStax College Physics 2e, §13.2: Thermal Expansion of Solids and Liquids](https://openstax.org/books/college-physics-2e/pages/13-2-thermal-expansion-of-solids-and-liquids). Linear thermal expansion, representative material coefficients, and holes expanding with heating.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.

### Pump Selection, Efficiency, and the Cost of Moving Water

### 019000 — Pump Selection, Efficiency, and the Cost of Moving Water

#### Technical companion (non-spoken)

**Power calculation.** `P_hydraulic = rho * g * Q * H`; for water at 1000 kg/m³, `Q=0.002 m³/s`, `H=20 m`, `P≈392 W`. At an illustrative 0.50 combined efficiency, `P_electrical≈784 W`. Include realistic fluid properties, gauge elevations, motor/drive losses and test uncertainty before using this on real equipment.

**Curve exercise.** Sketch a falling centrifugal pump head curve and a rising system curve. Show how a clogged filter moves the intersection to lower flow, how increased static lift offsets the system curve, and how a pump speed change shifts the pump curve.

**Safety/limits.** Pressure systems and rotating equipment carry stored-energy, injection, electrical and entanglement hazards. Use rated ports and suitable instruments. NPSH and efficiency must come from manufacturer curves or validated tests; do not infer from motor current alone.

**References.** U.S. DOE, *Improving Pumping System Performance: A Sourcebook for Industry*; DOE Better Plants, *Pumps*; Hydraulic Institute system-curve and pump-performance methods.

### Mechanical Seals and Leaks at Rotating Shafts

### 020000 — Mechanical Seals and Leaks at Rotating Shafts

#### Non-spoken technical companion

**Surface-speed relation.** Shaft surface speed equals circumference times rotational speed: `v = π D n`, where diameter and turns-per-second must use compatible units. This supports reasoning about lip-seal heat; it is not a substitute for catalog pressure-velocity ratings.

**Failure tree.** Leak at casing joint -> static gasket/fastener/casing hypothesis. Leak at shaft -> lip, packing, mechanical face, sleeve or secondary gasket. Look for damaged shafts, vibration, pressure excursions, dry running, incorrect material compatibility and process solids. Document whether the pump is pressurized while stopped.

**Sources.** John Crane, *What Is a Mechanical Seal?* and *Common Causes of Seal Leakage and Failure* (manufacturer technical explanation); SKF radial-shaft seal engineering and damage guides. Applicable equipment and manufacturer specifications are necessary for selection, pressure relief, flush design, removal and installation.
