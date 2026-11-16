# 014000 — Threaded Joints, Preload Loss, and Fastener Failure

<!-- BEGIN SPOKEN LECTURE -->

A bolt that comes loose looks like a simple failure of friction. Tighten it harder, perhaps add a locking washer, and the problem should disappear. But a bolted connection can fail for several different reasons. The bolt may stretch permanently, the mating surfaces may settle, vibration may create small relative motions, or the joint may have been asked to carry a load through the wrong path. The best way to understand a threaded joint is to imagine it as a carefully controlled spring holding two other parts together.

## Preload is the hidden force

When a bolt is tightened, its shank stretches slightly and the clamped members compress. This elastic deformation produces a tensile force in the bolt and a compressive force between the joint surfaces. That force is called preload or clamp load. In many joints, the purpose of preload is not simply to stop the nut from falling off. The normal force between members allows friction to resist sliding. If service loads are below that frictional capacity, much of the shear can pass directly through the contact surfaces instead of repeatedly bending the bolt.

Imagine two steel plates held by a bolt. If we pull them sideways, they resist movement initially because the compressed faces grip. The frictional resistance is related to clamp force and the coefficient of friction. If the plates start slipping, the bolt may begin bearing against the sides of the hole, producing bending, fretting, wear, and cyclic stress. Some joints deliberately use fitted bolts or shear pins to carry such loads, but a friction-grip joint depends on retained preload.

## Why torque does not uniquely determine tension

Applying torque with a wrench is a convenient way to stretch a bolt, but much of that torque is consumed overcoming friction in the threads and beneath the head or nut. Only a portion becomes useful bolt stretch. Changes in lubrication, plating, thread condition, washers, and surface finish can create large differences in clamp force for the same indicated torque.

An engineering approximation expresses torque as a factor multiplied by preload and nominal bolt diameter. The factor is not a universal material constant. It represents a collection of frictional and geometric effects and must come from an appropriate procedure. Taking a dry assembly torque specification and applying it after adding oil can produce a substantially different force. That is why equipment manuals sometimes specify whether threads and bearing surfaces must be dry or lubricated.

Tightening also has a sequence. On a multi-bolt flange, tightening one bolt changes the load carried by its neighbors as the joint surfaces deform. A staged pattern can help obtain a more uniform compression. Repeatedly 'making every bolt equally tight by feel' may produce very unequal clamp loads.

## How preload disappears

Suppose rough mating surfaces flatten slightly after assembly. The total thickness of the clamped stack decreases. Because bolt stretch was small to begin with, even a modest loss of stack thickness can significantly reduce preload. This is called embedment or settling. Gaskets can also creep, relax, or compress with heat, time, and load. A gasket that seals initially may leak later despite an intact bolt.

Thermal expansion can raise or lower clamp force when the bolt and the joined parts expand by different amounts. Repeated heating can relax some materials, and vibration can permit small relative movements. In a joint with inadequate frictional restraint, repeated transverse motion may rotate a nut loose; this is different from a bolt simply wearing away under steady tension.

Corrosion introduces another path. Rust can reduce thread area, make a nut seize, distort contact surfaces, and hide cracks. A corroded bolt may feel resistant to turning while carrying much less safe load than before. Never assume that difficulty turning a fastener means it is securely preloaded.

## Failure surfaces tell a story

A bolt fractured by a single overload can show a different fracture appearance from one that grew a fatigue crack over many cycles. Fatigue often begins at a stress concentration, such as the thread root or a bend, and progresses until the remaining section cannot carry the load. The visible final break may look sudden even though the damage accumulated for a long time.

Stripped threads suggest insufficient engagement, material incompatibility, damaged threads, or overloading. A sheared shank suggests forces acting across the joint. Elongated holes suggest relative sliding or bearing wear. Red-brown powder around clamped interfaces can be consistent with fretting and corrosion. No single surface mark proves the cause, but the location and pattern guide inspection.

Consider an oscillating motor mount that repeatedly loosens. Before specifying locking hardware, ask whether the mount is aligned, whether vibration creates transverse shear, whether the base is stiff, whether the bolt length and grip are appropriate, and whether a resilient layer is creeping. A locking nut might prevent rotation but cannot compensate for a joint that has lost adequate clamping force or a bracket that is fatigue-cracking.

## Choose retention appropriate to the mechanism

There are many methods of resisting unwanted rotation or maintaining a joint: prevailing-torque nuts, thread-locking compounds, tab washers, lockwire, controlled-angle tightening, and particular washer arrangements. Their effectiveness depends on environment, fastener geometry, allowable reuse, temperature, and assembly instructions. A product called 'locking' is not a substitute for correctly designed joint stiffness, clamp length, surface preparation, and load path.

For a machine, record the fastener identification, grade, engagement, intended lubrication, installation method, and condition of the mating surfaces. Where a manufacturer provides a torque-angle or stretch-based procedure, follow that rather than substituting a rough generic torque table. After assembly, inspect the joint under operating conditions for movement, leakage, heating, or recurring witness-mark shift. If a bolt keeps loosening, investigate why the preload is not surviving.

The central mechanical idea is simple: a bolted joint is a spring system. It works because the elastic stretch and compression remain large enough to keep surfaces where they belong. Understanding that model makes it easier to distinguish a loose nut from the deeper joint failure that made it loose.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Simplified models

- Clamp capacity against sliding in a simple friction joint: `F_slip ≈ μ × F_clamp`, for a single interface, before safety factors and design-specific conditions.
- Torque approximation: `T ≈ K × F_preload × d`; the empirical torque coefficient `K` varies substantially with friction, lubrication, geometry, and coating.
- Bolt spring stiffness (idealized): `k_b ≈ E A / L`; preload loss from joint settling depends on combined bolt/member stiffness, not simply the free bolt stiffness.

### Failure-analysis checklist

Inspect joint function, clamped-stack length, witness marks, thread condition, hole ovalization, fretting, gasket compression, thermal cycling, fastener grade, installation record, and whether retention hardware is appropriate. Photograph the as-found state before disassembly.

**Review boundary:** Safety-critical bolted joints, rotating equipment, vehicle suspension, lifting gear, and pressure containment require product-specific torque/stretch specifications and competent engineering evaluation. Do not infer a safe tightening torque from bolt diameter alone.

## Selected reading and evidence records (non-spoken)

- `openstax-torque` — [OpenStax College Physics 2e, The Second Condition for Equilibrium](https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium). Moment arm and torque.
- `osha-hazardous-energy` — [U.S. Occupational Safety and Health Administration, Control of Hazardous Energy (Lockout/Tagout)](https://www.osha.gov/control-hazardous-energy/). Stored pneumatic, hydraulic and mechanical energy during servicing.
- `skf-bearing-guide` — [SKF, Bearing Damage and Failure Analysis: misalignment and seal inspection excerpts](https://cdn.skfmediahub.skf.com/api/public/0901d19680c41453/pdf_preview_medium/0901d19680c41453_pdf_preview_medium.pdf). Misalignment, lubrication, seal contact pattern, locating/non-locating bearings.
- `skf-damage` — [SKF Evolution, How to Understand ISO 15243 — Bearing Damage Analysis](https://evolution.skf.com/us/bearing-damage-analysis-iso-15243-is-here-to-help-you/). Bearing removal symptoms and lubrication/contamination damage mechanisms.
- `openstax-thermal` — [OpenStax College Physics 2e, §13.2: Thermal Expansion of Solids and Liquids](https://openstax.org/books/college-physics-2e/pages/13-2-thermal-expansion-of-solids-and-liquids). Linear thermal expansion, representative material coefficients, and holes expanding with heating.
- `osha-belt-drive-guarding` — [U.S. Occupational Safety and Health Administration, Machine Guarding Introduction](https://www.osha.gov/etools/machine-guarding/introduction). Power-transmission apparatus including belts, pulleys, chains and sprockets must be appropriately guarded.
