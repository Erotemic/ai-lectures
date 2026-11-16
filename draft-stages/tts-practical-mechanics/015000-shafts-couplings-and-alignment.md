# 015000 — Shafts, Couplings, and Alignment

<!-- BEGIN SPOKEN LECTURE -->

A pump motor is replaced, but the new bearings run hot. The motor is new, the pump still moves water, and the installer has tightened every bolt. What could be wrong? The shafts may point in slightly different directions, their centerlines may be offset, or a coupling may be forced to accommodate motion it was not designed to carry. To diagnose this, we need to think of a drive train as a geometric system, not simply a motor attached to a load.

## What a shaft transmits

A rotating shaft transmits torque. Torque is the turning effect of force applied at a distance from the rotation axis. Power depends on both torque and rotational speed: for a given speed, more torque means more power. The shaft also experiences bending if belts pull sideways, gears transmit transverse forces, or couplings apply moments. Bearings support the shaft, constrain its position, and allow rotation with limited friction. The shaft, bearing housings, machine frame and foundation must all form a compatible load path.

A shaft can be straight but installed in a misaligned machine. Two coupled shafts can each turn smoothly when disconnected yet force their bearings sideways once joined. The coupling may be flexible enough to hide the geometry during assembly, but its flexibility has limits. Flexible does not mean it can accept any angular or parallel offset without fatigue, heating, and additional bearing load.

## Three geometries that matter

Angular misalignment means the shaft axes are tilted relative to each other. Parallel offset means the axes are parallel but do not lie on the same line. Axial position is the spacing or end-float relationship along the rotation direction. Real assemblies can have all three at once, plus runout from bent shafts, eccentric hubs, or damaged mating surfaces. The distinction matters because different measurements reveal different conditions.

Imagine two pointers with their tips facing each other. They can point in the same direction but be laterally displaced; that is offset. They can meet at a point but face different directions; that is angle. A coupling that joins the pointers may tolerate a small offset while transferring torque, but cyclic flexing can heat or damage it. If a shaft is also pushed or pulled along its own axis, the bearings or coupling may see loads that the assembly drawing did not intend.

Checking only the gap at one point of the coupling is inadequate. Rotating the shafts and measuring face variation may help reveal angular error; measuring rim or radial displacement may reveal offset. Depending on coupling design and equipment accuracy, technicians may use feeler gauges, dial indicators, straightedges, or laser alignment systems. Each technique has assumptions about the reference surfaces and whether the shafts rotate together. Indicator sag, coupling eccentricity, bracket flexure and bearing play can contaminate a reading.

## Soft foot and movement under tightening

Before precision alignment, check the machine's support. If one motor foot does not lie in the same plane as the others, tightening its bolt can distort the frame. This is called soft foot. Imagine a table with one short leg. Tightening a clamp at that leg would bend the table until the leg contacts the floor. The frame could now be under stress even if a ruler shows it is firmly bolted down. On a rotating machine, tightening a distorted frame can change shaft position and bearing geometry.

Thermal growth adds another complication. A motor and pump at operating temperature may sit at different heights than they do when cold. The housings and base expand according to material, geometry, and temperature distribution. A cold alignment that looks perfect may not be the desired operating alignment. Conversely, using a generic 'hot offset' without manufacturer data can introduce an error deliberately. The correct target belongs to the equipment and its operating conditions.

Pipe strain can also move a pump. If piping was pulled into position with flange bolts, the casing can be distorted. Disconnecting or relaxing a piping connection may cause the machine to spring out of alignment, revealing that the pipe, not the coupling, imposed a persistent load. The repair then belongs in the piping support and layout, not just a new coupling insert.

## What symptoms can and cannot prove

A misaligned drive may produce vibration, warmth near bearings, coupling wear, seal leaks, or elevated motor load. But these symptoms also have other possible causes: incorrect lubrication, unbalance, cavitation, bent shafts, loose foundations, electrical faults, or bearing contamination. Alignment is one hypothesis among several. Vibration at particular frequencies can offer clues, but a single noisy recording cannot establish alignment error by itself.

Suppose a flexible coupling insert fails repeatedly. A useful investigation compares the as-found alignment before loosening bolts, the foot support, coupling size and rating, the operating load, and the temperature change. Look for witness marks, damaged elastomer, unusual shaft-end spacing, and bearing temperatures. If alignment is corrected but the insert continues to fail, reconsider the loads and the coupling selection rather than tightening the motor harder.

Rotating equipment also stores kinetic energy and can restart unexpectedly under automatic control. Measurement and inspection occur with energy isolated and stored energy controlled. Guards remain in place during operation, and measurements requiring a running machine use procedures designed for that equipment. A vibrating exposed coupling is not something to feel with a hand while it rotates.

## Alignment as an engineering habit

The deeper idea transfers beyond pumps. A belt drive needs correct pulley alignment and tension; a lead screw needs bearings that allow intended axial and radial constraints; a sliding mechanism needs rails positioned without fighting each other. More forceful fastening rarely solves incompatible geometry.

When a machine is assembled, ask which surfaces establish its reference axes, which elements carry radial and axial loads, what movement is allowed, and what changes between cold and operating conditions. A good repair restores those relationships. Shaft alignment is not decorative precision; it prevents the coupling and bearings from being asked to solve a geometric problem every revolution.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Kinematics and inspection plan

- Power relationship: `P = T × ω` where `ω` is angular velocity in radians per second.
- Record coupling model/rating, permissible angular/parallel/axial displacement, bearing arrangement, base condition, foot shims, piping strain, and operating temperature.
- **Soft foot:** record foot gap or frame movement at each mounting point before detailed alignment.
- **Alignment:** distinguish offset, angle, shaft runout, measurement setup error, and operating thermal growth.
- **After correction:** record as-left values, torque/bolt procedure, guard reinstatement and vibration/temperature observations under authorized conditions.

**Technical boundary:** Manufacturer coupling limits and alignment procedure take precedence; no tolerance or intentional cold offset is universal. Apply lockout and stored-energy controls.

## Selected reading and source locators (non-spoken)

- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Moment arm and torque.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.
