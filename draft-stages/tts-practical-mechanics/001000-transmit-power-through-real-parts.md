# Transmit power through real parts

<!-- BEGIN SPOKEN LECTURE -->

# Transmit power through real parts

## Machines Trade Force for Motion: Torque, Friction, and Wear

A machine may be as small as a door hinge or as complicated as a washing machine. What they share is not a particular motor, fuel, or housing. A machine constrains motion, transmits forces, and changes the way energy is delivered. If it works well, those interactions are controlled. When it fails, the failure often reveals which movement or load was no longer controlled.

Imagine a bicycle pedal. Your foot pushes on a crank. The crank rotates, and a chain turns the rear wheel. You get forward motion by exchanging force, distance, and time through a sequence of mechanisms. The chain does not manufacture energy. Neither does the gear ratio. It changes the balance between force and speed, with some energy lost through friction and deformation.

This is a powerful starting point for practical diagnosis, because nearly every mechanism can be examined in terms of inputs, outputs, constraints, storage, and loss.

### Force is not torque

A force can push an object in a straight line. Torque is the turning effect of a force about an axis. For a force applied perpendicular to a lever arm, torque is force multiplied by the distance from the axis. Push on a wrench ten centimeters from the bolt with a hundred newtons of force and the torque is ten newton-meters, in that ideal geometry. Move your hand twice as far from the axis and apply the same perpendicular force; the torque doubles.

But the distance is the perpendicular moment arm, not merely the length of the tool. If you push along the wrench handle, much of your force may create little torque. If you approach from an angle, only the appropriate component contributes to rotation. This is why body position matters when applying forces, and why a long handle does not magically set a known tightening torque.

Mechanical power is the rate of energy transfer. In rotating machinery, power is torque multiplied by angular speed. A slow shaft may deliver high torque while a faster shaft at the same power delivers lower torque. A gearbox can make this trade. It cannot increase power beyond its input; real gearboxes lose some to friction, churning lubricant, and deformation.

### What gears, pulleys, and screws really do

A pair of meshing gears constrains relative angular motion. In an ideal simple gear pair, the speed ratio is the inverse of the tooth-count ratio. A small gear driving a gear with twice as many teeth turns the larger gear at half its speed, while the output torque can approach twice the input torque before losses. The directions and exact relationship depend on the arrangement; compound gear trains extend the idea.

A belt drive transfers force through friction or, for toothed belts, engagement. Belts can slip, stretch, age, or lose tension. Chains engage sprocket teeth and require compatible pitch, alignment, tension and lubrication. A leadscrew trades rotation for linear movement; its pitch and friction determine the motion per turn and required torque. Every mechanism chooses a particular transformation and introduces its own failure modes.

Think about a garage-door opener. It does not simply lift a door by raw motor power. The springs, rollers, tracks, counterbalance, gears, and controls share the task. A motor that struggles may be fighting high friction, incorrect balance, damaged rollers, or another system issue. Increasing motor power without understanding stored spring energy and the door's path would be a poor diagnosis, and spring systems are particularly hazardous to improvise upon.

### Why bearings matter

A bearing constrains the position of a moving part while permitting selected motion with manageable friction. A plain bearing supports sliding motion; rolling-element bearings use balls or rollers to change the contact mechanics. They still have losses and limits. Radial loads push across a shaft; axial or thrust loads push along it. Some bearings are designed primarily for one, some for both. Mounting, preload, alignment, lubrication, temperature, contamination and load all influence life.

A noisy bearing is not automatically a bad bearing. A rumbling noise may originate in gear mesh, a loose mounting, an out-of-balance load, or a neighboring component. But sound, vibration and heat are useful clues because they tell us how mechanical energy is being dissipated. Good diagnosis compares operating conditions: unloaded and loaded, cold and warm, slow and fast, turning in either direction when applicable.

Lubrication reduces direct surface contact in many mechanisms and can carry away heat and contaminants. There are distinct regimes: full fluid-film separation, mixed lubrication and boundary lubrication, with different wear risks. More lubricant is not universally better. Excess grease can increase drag, interfere with seals, or contaminate surrounding parts. Compatibility, viscosity, service interval and manufacturer requirements matter.

### Clearance versus looseness

Mechanical parts need controlled clearances. Two pieces designed to slide must not be assembled as if both occupied exactly the same space. Yet too much clearance can produce backlash, vibration, leaks, poor alignment or impact loads. The correct fit depends on thermal expansion, operating speed, lubrication, load, and manufacturing tolerances.

An example is a rotating shaft inside a bearing. If a shaft expands as it warms but the housing and bearing arrangement do not accommodate that expansion, internal loading may rise. Conversely, if a wheel hub has excessive play, loads may no longer travel through the intended contact surfaces. The same principle appears in a drawer slide, door hinge, printer mechanism, and vehicle suspension.

### Stored energy changes repair work

A system that is switched off can still contain energy. Springs may be compressed or stretched, rotating parts may coast, a hydraulic accumulator may hold pressure, heavy equipment may remain elevated, and a hot surface can retain heat. Before studying a failed mechanism closely, identify what can move and why. Electrical isolation alone may not release mechanical, fluid, gravitational or thermal energy.

Take a hydraulic jack. In idealized terms, pressure applied to a confined fluid can transmit force to another piston. A small input piston driving a larger output piston multiplies force according to area ratio, at the cost of moving the small piston farther. Real systems have leakage, friction and compliance. A supported load must never be entrusted only to a hydraulic mechanism that could lose pressure. The engineering distinction between a lifting mechanism and an independently rated support is fundamental.

### The diagnostic tree

Suppose a belt-driven fan turns slowly and makes an intermittent squeal. Possibilities include an overloaded fan, insufficient belt tension, misalignment, worn bearings, a slipping belt, or a motor control problem. Instead of replacing the loudest component, observe whether the squeal appears at startup, under load, or with changes in speed. Compare input shaft rotation with output rotation. Inspect visible wear, alignment and available maintenance records using the correct shutdown and guarding practices. Each observation changes the likelihood of particular causes.

Mechanical troubleshooting is a process of localizing where energy and motion stop following the intended path. Start at the source, trace the transmission, identify the load, check constraints, and ask where extra loss might be occurring. The goal is to replace guesswork with causal explanations. Once we know how a machine trades force for motion, its symptoms become a kind of language.

## Gear Ratios and Transmission Layouts

The power-path picture lets us examine ratios in more detail, including several stages between the input and the load.

Take two gearwheels. One has twelve teeth; the other has thirty-six. Mesh them so the teeth remain engaged. Turn the small gear one full revolution. The large gear turns only one third of a revolution. The motion looks like a trade: we surrender angular speed and gain turning force. That intuition is correct, within the limits imposed by losses. But it is useful to derive it rather than memorize a phrase.

A gear transfers tangential force at the point where its teeth meet. For two externally meshing gears, the tangential velocity at the pitch circles must match in magnitude when there is no slip at the idealized pitch contact. A larger pitch circle covers more distance per revolution, so it rotates more slowly for the same contact speed. If the tooth spacing, or module, is compatible, the ratio of pitch diameters equals the ratio of tooth counts.

### Count teeth, not wishful turns

Let the input gear have twelve teeth and the output gear thirty-six. The output speed is the input speed multiplied by twelve divided by thirty-six. Thus it rotates one third as fast. An external gear pair also reverses the direction of rotation. A small gear driving a large gear is a speed reduction; the reverse is a speed increase.

Now think about torque. Torque is a moment: force multiplied by the perpendicular lever arm. The same tangential tooth force acting at the larger gear's pitch radius produces greater output torque. For an ideal lossless mesh, output torque is three times input torque in our twelve-to-thirty-six example. The product of torque and angular speed is power, so tripling torque while dividing speed by three preserves transmitted power.

An actual mechanism has friction, deformation, lubricant churning, bearing losses and sometimes backlash or sliding contact. Output power is less than input power. If efficiency is ninety percent in this example, ideal three-times torque gain becomes approximately two point seven times at the same speed reduction. Efficiency depends on operating conditions and configuration; ninety percent is an illustrative assumption, not a universal gear rating.

### Compound stages make ratios multiply

Put a twelve-to-thirty-six stage on a shaft that also carries a second small gear. That second gear drives another large gear of the same ratio. There are now two three-to-one reductions, for nine to one overall. An input shaft spinning nine turns drives the final shaft through one turn. If all stages were lossless, final torque could be nine times input torque. With ninety percent efficiency in each stage, overall efficiency is eighty-one percent, not ninety percent. Energy losses compound along with the ratio.

This is why multi-stage transmissions can create high torque reduction in a compact volume, but adding gears is not free. Every stage adds components, alignment requirements, noise sources and possible failures. A design should choose gear sizes and stages by needed speed, torque, packaging, strength and duty cycle.

### An idler changes direction, not the simple overall ratio

Insert a third, intermediate gear between two external gears. It is called an idler when its main purpose is to transfer motion or adjust direction/spacing without creating an additional net speed ratio. The idler's tooth count cancels from the overall ideal ratio between the first and last gears, though it affects layout and tooth contact. Each external mesh reverses direction, so adding an idler changes the final rotation direction compared with a direct mesh.

Do not generalize this cancellation to arbitrary gearboxes. When gears share compound shafts or use internal teeth, the connection topology changes the equations. Planetary gearsets have sun, planet and ring gears; the relationship between their speeds depends on which member is held, driven or used as output. Counting two visible gears without understanding the carrier can produce the wrong answer.

### Gear shape matters as much as ratio

Spur gears have teeth parallel to their shafts. Helical gears have angled teeth and can engage progressively, often changing noise and load distribution, but they create axial forces that bearings must handle. Bevel gears transmit rotation between intersecting axes. Worm gearing may provide large reductions in compact geometry, but it introduces substantial sliding contact and efficiency consequences. The best selection depends on geometry and service conditions.

Backlash is the clearance between mating teeth needed for manufacturing tolerances, lubrication and thermal effects. Too little may bind under operating temperature or deflection; too much can cause lost motion, impacts and positioning error. Wear changes tooth shape, and misalignment moves load toward tooth edges. A gear that looks intact can still function poorly if shafts, housings and bearings no longer hold the correct geometry.

### Read a failure by the way power flows

Suppose a small electric motor drives a heavy load through a gearbox. The output stalls. Does that mean the motor is weak? Perhaps. But the gear train may be binding because of damaged bearings, inappropriate preload, contamination, distorted housing or excessive load. Current draw, motor temperature, output motion, noise and mechanical play help separate cases. A gearbox can also develop noise from pitted teeth or lubrication failure while still transmitting torque.

A diagnostic approach follows the power path. Where does torque enter? Which shafts must move together? Which gears rotate relative to each other? Which parts support the tooth forces? If you disconnect a load, does the upstream system behave differently? These are reasoning questions; procedures for physically testing energized or moving machinery need equipment-specific controls.

### Gearboxes teach a broader engineering habit

A transmission does not create power. It trades angular speed for torque and sometimes reverses or redirects rotation. Its ratios are defined by tooth counts and topology; its losses and failures depend on contact mechanics, lubrication and structure. Once you think in terms of power paths, the same framework applies to bicycle drivetrains, winches, clocks, automotive transmissions, robot joints and industrial reducers.

Next time you see a machine that moves something heavy and slowly, ask how fast the driving motor turns and how many stages of ratio sit between the motor and the load. The machine will begin to reveal its logic, one shaft at a time.

## Friction, Lubrication, and Heat

A small fan starts quietly, runs for a while, and begins to squeal. You touch the outside of its bearing housing after it is safely stopped and find it much warmer than before. A common first guess is that the machine needs more grease. Sometimes it does. Sometimes adding grease would make the problem worse. The useful question is not 'What substance stops squeaks?' It is 'What contact is producing resistance, and why has its condition changed?'

Friction is a force associated with relative motion or the tendency to move between contacting surfaces. It can be useful: shoes grip a floor, a brake slows a wheel, and a screw holds because surfaces resist sliding. In bearings and gears, however, friction consumes part of the input mechanical energy and often contributes to heat and wear.

### Friction is not one constant

In a simple classroom model, the maximum static friction force is approximately the normal force multiplied by a coefficient. The corresponding sliding model uses a different coefficient. These are helpful first approximations, not universal laws for every material or speed. Real friction depends on surface roughness, material pairing, load, temperature, lubrication, contamination, and operating conditions.

Consider pushing a heavy crate across a floor. It may resist the start of motion more strongly than steady sliding. As the crate moves, you are doing work against friction; if nothing else stores that energy, much of it becomes heat. In a rotating machine, this process repeats continuously at contact points. A small frictional torque multiplied by a high rotational speed can represent substantial power dissipation.

The key arithmetic is that power equals torque times angular speed. A shaft can feel easy to turn by hand and still waste noticeable power when spinning rapidly. Conversely, a heavy load can produce substantial bearing stress even at low speed. Friction and wear require understanding both load and motion.

### What lubricant is supposed to accomplish

Oil or grease does more than make parts slippery. Under suitable conditions, a lubricant can help form a film separating opposing surface asperities, the microscopic high points that would otherwise touch. It can also carry away heat, inhibit corrosion, and transport or isolate contaminants depending on the system. The ability to form an adequate film depends on viscosity, speed, geometry, load, and temperature.

Engineers distinguish operating regimes. In boundary lubrication, much of the load is transmitted at or through very thin films near solid-surface contact, so surface chemistry and additives matter. In mixed lubrication, both the fluid film and interacting surface peaks carry load. In full-film regimes, the surfaces can be substantially separated by the fluid, though fluid shear still consumes energy. In rolling bearings, elastohydrodynamic effects can create a pressurized lubricant film in very small rolling contacts.

These descriptions matter because 'more lubricant' is not synonymous with 'better lubrication.' Grease consists of a base oil held in a thickener system, often with additives. It supplies oil to the contact over time. Overfilling can cause churning and higher temperatures; the wrong viscosity or incompatible grease can disrupt lubrication. Manufacturers specify quantities and service intervals because the bearing geometry and operating regime set the needs.

### Viscosity links temperature to behavior

Viscosity describes resistance to flow and shear. Many lubricating oils become less viscous as temperature increases. A lubricant that forms a useful film during a cool start may become too thin at high operating temperature for a particular load. A very thick oil can also create excessive drag or fail to reach a component as intended. The correct choice is a system property, not a universal number.

This leads to feedback loops. Suppose bearing friction increases because lubrication degrades. More energy becomes heat. The lubricant temperature rises, changing viscosity and sometimes chemistry. That may further reduce film quality, accelerating wear. But the reverse can also occur: an overloaded or overgreased bearing runs hot because the lubricant itself is being churned, even when there is plenty of material present.

### Wear leaves diagnostic signatures

Wear can result from abrasive particles, adhesive contact, fatigue under repeated stress, corrosion, fretting from tiny oscillations, or combinations of mechanisms. Different failures leave different evidence. A bearing with gritty contamination may feel rough. A belt misalignment can create heat and wear on one edge. A failing seal may allow lubricant to escape or contaminants to enter. A slightly misaligned shaft can repeatedly load a bearing in an unintended direction.

Noise and temperature alone rarely prove a single cause. A useful diagnosis records when the symptom occurs: immediately at startup, after warming, only under load, or only at a certain speed. Has lubricant been changed recently? Did the machine receive a different belt tension, heavier load, or new alignment? Is the housing hot because of an adjacent motor or heater rather than friction within the bearing? A trend often tells more than one alarming temperature.

### An energy audit for a simple machine

Imagine a motor driving a pulley and a fan. Electrical input becomes mechanical shaft power, with losses in the motor. The belt transmits some power and loses some through flexing and friction. Bearings resist rotation and dissipate heat. The fan transfers mechanical energy to air, but the system also makes noise, turbulence, and heat. If the fan moves less air while input power stays similar, do not assume all missing output was caused by bearing friction. A blocked duct, blade contamination, belt slip, or changed control setting can also matter.

The repair-minded approach is to identify the energy path, then localize the changed loss or load. A targeted lubrication change may be appropriate once the bearing type, lubricant, quantity, and service method are known. But replacing a damaged bearing without correcting shaft misalignment or contamination can simply reset the clock on the same failure.

The squealing fan has taught us a larger lesson. Machines transform energy, and every contact is a possible site of loss. Heat, noise, and vibration are evidence of what that transformation is doing. Learn to read those signs before reaching for a can of grease.

## Bearings, Seals, and Alignment

Losses and wear also depend on the contacts that support motion, so bearings and alignment belong inside the same power path.

A small electric motor drives a fan. After a few months, it becomes louder, runs hotter, and develops vibration. Someone replaces the bearing. For a few weeks the machine sounds better, then the noise returns. Perhaps the bearing was defective. But perhaps the bearing was carrying a load it was not meant to carry because the shaft was misaligned, the belt tension was wrong, a seal admitted contamination, or the installation damaged the bearing before it even began operating.

A bearing's fundamental task is to support relative motion while constraining unwanted motion. A plain bearing permits sliding with an appropriate lubrication regime. A rolling-element bearing places balls or rollers between raceways, converting much of that sliding contact into rolling contact. Neither type eliminates force or friction. The design chooses how those forces are carried, what motion is allowed, and what lubrication and cleanliness are needed.

### The load has a direction

Bearings are not interchangeable circles of metal. Some are mainly intended to support *radial* loads, perpendicular to a shaft's axis. Others handle substantial *axial* or thrust loads along the shaft. Many designs carry combinations, but capacity depends on geometry and application. Consider a fan shaft with a belt pulley. Belt tension creates a radial load. A propeller or screw mechanism may create thrust. A shaft mounted between bearings also changes length as it warms; if both bearings rigidly prevent that expansion, extra axial load can develop.

Engineers often distinguish a locating bearing, which establishes axial position, from a nonlocating bearing arrangement that permits appropriate axial movement. The details depend on shaft geometry, bearing type, and fit. The mental model is that supports must constrain *just enough* motion. Too little restraint permits wobble. Too much can preload parts that were expected to move slightly.

### Alignment makes loads predictable

Two coupled shafts may look almost coaxial but differ in offset or angle. When rotated, a misaligned coupling transmits cyclic forces into shafts, bearings, and seals. A pulley installed crooked can increase belt edge wear, belt vibration, and bearing load. A machine supported on an uneven base may have a soft foot: one mounting point does not sit firmly, so tightening fasteners distorts the housing and changes the geometry.

Now imagine installing a bearing by hammering on the outer ring when the desired interference fit is on the inner ring. The assembly force may travel through the rolling elements and raceways. It can damage precisely finished contact surfaces. Proper installation transmits force through the fitted ring using suitable fixtures and methods. Temperature-assisted fits, where appropriate, must respect manufacturer limits. A bearing is not simply a component to be shoved onto a shaft until it fits.

### Seals defend the contact zone

A bearing may fail because dirt, water, or metal particles enter its lubricant. Hard debris can create surface damage; water can degrade lubrication and promote corrosion. Seals are not cosmetic covers. A contact lip seal relies on the correct relationship between the sealing lip and its shaft surface. Misalignment, roughness, insufficient lubrication, or excessive speed can wear it. Noncontact labyrinth-style seals use a tortuous path and small clearances rather than continuous rubbing, with different benefits and limitations.

A leaking seal and a damaged bearing may be symptoms of the same upstream problem. If a shaft runs eccentric, the seal may lose contact on one side and rub too heavily on another. Changing only the seal leaves the cause untouched. Similarly, filling a contaminated housing with extra grease does not remove abrasive particles or correct an inappropriate seal design.

### Read the failure before discarding it

A worn bearing leaves clues. Repeated marks on a raceway, discoloration, corrosion, pitting, smearing, and lubricant condition can suggest different failure mechanisms. No one symptom is a perfect signature: overheating may follow overload, lubrication starvation, excessive preload, or other faults. Noise frequencies and vibration signatures can be diagnostic, but interpretation requires knowledge of rotating speed, bearing geometry, mounting, and measurement conditions.

A useful troubleshooting sequence compares *what changed* against *what remained constant*. Did vibration appear after a belt replacement? Did the motor get moved? Was a seal replaced with a different material? Did washdown spray increase? Does the housing temperature rise only under certain loads? These questions test hypotheses instead of turning bearing replacement into a recurring maintenance ritual.

### A repair is complete when the load path is restored

When a shaft rotates smoothly after assembly, the job is not necessarily finished. Verify that supporting elements are aligned, that axial expansion has a legitimate path where required, that lubricant and seals suit the application, and that the operating load is within the intended arrangement. The right checks may include runout, shaft alignment, belt tension, mounting flatness, endplay, vibration, and temperature trends. Which checks apply depends on the machine.

The bearing is often the first damaged component you can hear. It is not always the component that caused the damage. Understanding the complete rotating assembly turns a repeated parts replacement into an engineering diagnosis.

## Fits, Clearances, and Thermal Expansion

A metal shaft passes through a hole. If the hole is slightly larger, the shaft can slide or rotate. If they are nearly the same size, the result depends on manufacturing variation and temperature. If the shaft is larger, an interference fit may hold the parts tightly together. All three assemblies can be correct or incorrect depending on what the designer intended.

Mechanics is full of purposeful gaps: a bearing needs the right internal clearance, a valve stem needs space to move while remaining sealed, and two gears need backlash so their teeth do not jam. A gap is not necessarily sloppy workmanship. Conversely, two parts that feel perfectly tight on a bench can seize when they warm up or deform under load.

### Nominal dimension is not actual dimension

Suppose a drawing calls for a shaft of ten millimeters diameter and a hole of ten millimeters. These are nominal descriptions. Real parts are manufactured within tolerances. A shaft may be slightly above or below its nominal value, and the hole has its own range. The possible clearance is the hole diameter minus the shaft diameter. If the tolerance ranges overlap, some assemblies may be loose and others tight even though every individual piece passes inspection.

A fit therefore requires two compatible tolerance ranges, not merely matching nominal sizes. In a clearance fit, the smallest permitted hole still exceeds the largest permitted shaft. In an interference fit, the largest permitted hole is still smaller than the smallest permitted shaft. Transition fits occupy the territory where either outcome may occur, depending on the actual pair.

A machinist can measure one shaft and one hole, but also needs to know their shape. A slightly oval hole may admit a pin at one angle while binding at another. A tapered bore may accept an insertion and then seize. Surface roughness, burrs, and damage affect contact even if a simple caliper reading appears acceptable. Geometry and finish participate in the fit.

### Temperature moves the dimensions

Most common engineering metals expand when heated. For a sufficiently small temperature change, a useful approximation is change in length equals original length multiplied by the coefficient of thermal expansion and by the temperature change. The same principle applies approximately to diameters.

Take a steel ring with a bore diameter of fifty millimeters. If its temperature rises by fifty degrees Celsius, and we use a steel expansion coefficient of roughly twelve millionths per degree Celsius, the bore diameter increases by about thirty thousandths of a millimeter. That is a small number to the eye, but it can be important in a precision fit. Different metals have different coefficients. An aluminum housing and a steel shaft or bearing can change their relative fit as the assembly heats.

This leads to a practical surprise. Heating a ring usually enlarges its hole; it does not squeeze the hole closed. That observation underlies some controlled thermal assembly methods. But it also shows why the fit at a room-temperature inspection may not be the fit at operating temperature. Even a temporary warm spot or an uneven thermal gradient can affect clearances and alignment.

### A bearing wants the right freedom

A rolling bearing has internal clearances that change when rings are pressed into the shaft or housing. Interference can expand the inner ring or compress the outer ring, reducing some internal clearance. Running temperature, load and differential expansion change it again. Too little operating clearance can increase friction and heat; too much can reduce precision and contribute to vibration or load concentration.

It is therefore possible to damage a bearing by installing an otherwise correct bearing with an inappropriate shaft fit. The mechanic who blames the lubricant alone may miss the true cause. Likewise, a seal needs appropriate contact pressure and shaft finish. A very tight seal can overheat or wear quickly; a loose seal can leak. Mechanical quality frequently means choosing a narrow operating range between two failure modes.

The surrounding assembly must also permit expected movement. A long metal rail attached rigidly at both ends can develop force from expansion and contraction. A sliding support, expansion joint or compliant coupling may be needed. Engineers often choose one locating bearing to fix a shaft axially and another arrangement to accommodate thermal growth. Without that freedom, temperature change can preload the structure in ways nobody intended.

### Why tolerance stacks matter

Imagine a lid supported by three machined spacers. Each spacer is manufactured within an allowed range. If the critical gap depends on several dimensions added or subtracted together, their variations accumulate. A design that looks generous when every dimension takes its nominal value can become too tight in an unfavorable combination. Inspection should identify which measurements control the actual function rather than simply checking that every part is close to a printed number.

Tolerance does not mean permissible carelessness. It is a defined range that connects what can be manufactured to what will work. A sensible tolerance is tight enough to protect function and loose enough to be produced reliably. Specifying extreme precision everywhere adds cost without necessarily improving the mechanism.

### Diagnosing a fit problem

A device that binds only after warming suggests thermal expansion, loss of clearance, misalignment, or lubricant changes. A joint that rattles after a few months may have wear at a bearing or hole, or it may have had excessive clearance from the start. Measure at a controlled temperature, look for asymmetric wear, inspect surfaces for fretting, and compare with the intended arrangement. Do not file or grind away material until you know whether it was meant to provide a controlled interference.

The lesson is that an assembly is never just a collection of dimensions. It is an arrangement of freedoms and constraints that changes with load and temperature. A designed gap can be as important as a designed contact, and a fraction of a millimeter can decide which one you have.

<!-- END SPOKEN LECTURE -->

## Companions, sources, and study material (not spoken)

### Machines Trade Force for Motion: Torque, Friction, and Wear

**Track:** Mechanical Systems and Repair. **Background:** Arithmetic and basic force concepts. **Purpose:** establish a transferable mechanical model for household machines and workshop mechanisms.

#### Technical companion

For perpendicular force, `τ = rF`. Rotational mechanical power `P = τω`. For an ideal external simple gear pair with tooth counts `N1` and `N2`, `ω2/ω1 = -N1/N2`; ignoring losses, torque magnitudes vary inversely with speed. Real mechanical transmissions include losses, dynamic loads, and product-specific limitations.

**Evidence map:** OpenStax's simple-machines treatment supports force-distance tradeoffs and conservation of energy. Its rotational-dynamics chapters support torque and angular motion. Machinery maintenance guidance must be tied to the actual manufacturer and equipment type; an introductory explanation does not establish safe disassembly or load-bearing arrangements.

**Exercise:** Sketch a hand-cranked winch. Label the input force, input distance per revolution, rotational speed, output load and output travel. Explain why a higher mechanical advantage does not provide free energy.

### Gear Ratios and Transmission Layouts

**Track:** Mechanical Systems and Repair. **Background:** Torque, force, motion and mechanical advantage. **Purpose:** teach gear ratios as conservation of motion and energy, then connect them to layout and failure modes.

#### Technical companion: ratio and power accounting

For ideal external gears with teeth `z1` (driving) and `z2` (driven): `ω2/ω1 = -z1/z2`, `|τ2/τ1| = z2/z1` for zero losses; `P = τ ω`. With efficiency `η`, output torque magnitude is `η*(z2/z1)*input torque` under suitable steady operation. For compound stages, multiply speed ratios and efficiencies separately. Illustration: two 3:1 stages each at 90% efficiency yield 9:1 reduction and 81% net efficiency.

**Cautions of scope:** An idler cancels from an uncomplicated simple external gear train's overall magnitude ratio, not from every multi-shaft or planetary configuration. Real teeth transmit nontrivial radial/axial forces; shaft and bearing design is not determined by tooth count alone.

**Reading:** OpenStax mechanics chapters on rotational motion, work and simple machines provide the underlying moment and power framework. Gear type and rating details depend on manufacturer data and technical gear standards; this introduction is conceptual, not a design standard.

**Exercise:** Draw a three-gear simple train with 12, 18 and 36 teeth. Find the last shaft's speed ratio and direction. Then replace the middle gear with a compound shaft containing a second gear, and explain why the calculation must change.

#### Selected reading and evidence (non-spoken)

- `mit-gear-ratios` — [Martin Culpepper, MIT OpenCourseWare 2.72 Elements of Mechanical Design, Lecture 12: Transmission Ratios for Serial Gears](https://ocw.mit.edu/courses/2-72-elements-of-mechanical-design-spring-2009/83d81a6f63d1c6f0fb775c08b207bc51_MIT2_72s09_lec12.pdf). Tooth-count and series gearing ratio derivations.
- `mit-gear-trains` — [MIT OpenCourseWare 2.00AJ, Gears and Linkages (2009)](https://ocw.mit.edu/courses/2-00aj-exploring-sea-space-earth-fundamentals-of-engineering-design-spring-2009/e8c25391a19f4a1ef3c427017307f509_MIT2_00AJs09_lec07.pdf). Gear trains, ideal power, efficiency and torque.
- `openstax-machines` — [OpenStax College Physics 2e, Simple Machines](https://openstax.org/books/college-physics-2e/pages/9-5-simple-machines). Mechanical advantage and energy conservation.

### Friction, Lubrication, and Heat

**Track:** Mechanical Systems and Repair. **Background:** Force, motion, and gear ratios. **Purpose:** connect contact forces to energy losses, wear, and maintenance.

#### Technical companion (non-spoken)

##### Relations and distinctions

- Simple dry-contact model: `F_f ≈ μN` under appropriate assumptions; `μ` is not a universal constant.
- Rotating loss: `P_loss = τ_friction × ω`, with torque in `N·m` and angular speed in `rad/s`.
- Lubricant film depends on operating viscosity, load, speed, geometry, and surface condition.
- Heat generated by a frictional loss is not identical to the measured housing temperature, which also depends on heat flow to surroundings.

##### Fault tree exercise

For a hot bearing housing, separate: (a) lubrication quantity or type, (b) contamination or seal defects, (c) load/alignment, (d) excessive speed or belt tension, and (e) heat entering from another component. Compare observations at consistent operating points before attributing cause.

##### Scope

SKF's published troubleshooting guides describe inadequate lubrication, inappropriate lubrication, overgreasing, and related mechanisms. Service quantities, compatibility, temperatures, and teardown steps must follow the specific equipment manual; rotating machinery must be isolated and secured before physical inspection.

#### Selected reading and claim sources (non-spoken)

- `skf-grease` — [SKF Evolution, Grease Lubrication Mechanisms in Rolling Bearing Systems](https://evolution.skf.com/us/grease-lubrication-mechanisms-in-rolling-bearing-systems/). Grease churning, replenishment, starvation and film breakdown.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.

### Bearings, Seals, and Alignment

**Track:** Mechanical Systems and Repair. **Background:** Gears, friction, lubrication, and heat. **Purpose:** see the bearing-and-shaft assembly as a controlled contact and contamination system.

#### Technical companion (non-spoken)

##### Diagnostic matrix

| Observation | Competing explanations to evaluate |
|---|---|
| Rising housing temperature | Load, preload, lubricant quantity/condition, contamination, alignment |
| Cyclic vibration after belt service | Tension, pulley runout, angular/parallel misalignment, foundation |
| Seal lip wear on one side | Shaft eccentricity, alignment, housing distortion, sealing-surface wear |
| Corrosion or debris in grease | Water ingress, cleaning process, damaged housing or seals |

A failure image or frequency signature alone does not establish causation. Save removed components and baseline operating measurements when possible.

##### Terms and review

*Radial load* acts perpendicular to the shaft; *axial load* acts along it. *Endplay* is permitted axial movement, whereas *preload* is intended internal load applied to eliminate or control clearance. Fits and bearing life calculations are equipment-specific. Rotating machinery and stored tension can be hazardous; follow lockout and manufacturer disassembly procedures. SKF's failure taxonomy and application guides support the conceptual mechanisms, not a universal repair prescription.

#### Selected reading and claim sources (non-spoken)

- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.

### Fits, Clearances, and Thermal Expansion

**Track:** Mechanical Systems and Repair. **Background:** Bearings, friction, lubrication, and mechanical loads. **Purpose:** understand controlled gaps, interference, tolerance stacks, and thermal movement.

#### Technical companion (non-spoken)

##### Thermal expansion calculation

For `L = 50 mm`, `alpha = 12 × 10^-6 / K`, and `ΔT = 50 K`, a steel dimension changes approximately `ΔL = alpha × L × ΔT = 0.030 mm`. This is an illustrative coefficient, not a specification for all steel grades or assemblies.

##### Fit exercise

Let a hole range from 10.010 to 10.030 mm and a shaft from 9.980 to 10.000 mm. The clearance ranges from 0.010 to 0.050 mm. Ask how that range changes if the shaft is steel and housing aluminum at elevated temperature.

**Review boundary:** Bearing, seal, press-fit and thermal-assembly decisions require manufacturer fit tables, material grades, temperature range, and proper measurement technique.

#### Selected reading and evidence records (non-spoken)

- `openstax-thermal` — [OpenStax College Physics 2e, §13.2: Thermal Expansion of Solids and Liquids](https://openstax.org/books/college-physics-2e/pages/13-2-thermal-expansion-of-solids-and-liquids). Linear thermal expansion, representative material coefficients, and holes expanding with heating.
- `skf-highspeed-bearings` — [SKF Evolution, Bearings for High Speed Operations](https://evolution.skf.com/us/bearings-for-high-speed-operations/). Differential operating temperature, interference fit, clearance and bearing preload.
