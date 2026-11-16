# 006000 — Mechanical Fastening and Fatigue

**Track:** Metalworking and Fabrication. **Background:** Material behavior, cutting, forming, and welding. **Purpose:** understand reversible joints, repeated loads, and durability at stress concentrations.

<!-- BEGIN SPOKEN LECTURE -->

# Why did the bracket crack after a year?

A steel bracket supports a small machine. It survived installation and the first day of operation. The visible load never approached what someone thought the steel could carry. Yet a crack appears near a bolt hole months later. The mistake may be treating strength under one application of force as the only measure of durability. A joint that survives a large one-time load can fail after many smaller cycles if a local stress repeatedly rises and falls.

This is fatigue, and it changes how we design metal fabrications. We must ask not only how much load exists, but how it varies, how often it repeats, and where the load concentrates. A vibrating fan, a repeatedly opened gate, an engine mount, or a metal step may experience thousands or millions of cycles. A joint that flexes slightly every time can accumulate damage even though it looks rigid to the eye.

## Stress concentration begins with geometry

When a metal plate is pulled in tension, its average stress is force divided by the relevant cross-sectional area. But stress is rarely distributed perfectly evenly. A hole removes material and redirects the stress paths around its edge. A sharp interior corner or abrupt change in section can concentrate stress. A weld toe can create another local geometry where small cracks may begin.

Imagine two flat strips joined end to end. One has a smooth transition in width; the other narrows abruptly at a squared notch. Under the same average tension, the notch can experience much greater local stress. Repeated loading makes this difference especially consequential because fatigue damage often starts at such concentrated regions.

A crack is not just a line on the surface. Its tip creates an intense local stress field, and as the crack grows the remaining cross-section carries more load. The rate of growth depends on material, geometry, stress range, environment, and many other factors. A connection may therefore appear healthy for most of its service life, then deteriorate rapidly once a crack reaches a critical size.

## Bolted joints can reduce or create movement

A bolted connection can clamp two plates together, permitting friction between their faces to carry some transverse loading when properly designed and preloaded. Or the bolt shank can carry load in shear and bearing against the plate holes. In either case, the bolt size alone does not define the connection's behavior. Surface condition, hole clearance, washers, tightening procedure, plate stiffness, and thread engagement all matter.

If preload is insufficient or gradually lost, the plates may slip microscopically under repeated load. This can produce fretting wear, damage coatings, and concentrate stress around holes. Bolts can loosen under transverse vibration if the joint is not properly designed for it. Thread-locking compounds, locknuts, washers, and other retention features are tools, but none substitutes for an appropriate joint design and installation instructions.

Fastener placement affects the force route. In a lap joint, the plates are offset from each other, so the applied tension may also create a bending moment. In a symmetric double-shear arrangement, the force path can be more direct, but fabrication complexity increases. A long lever arm can amplify bolt tension even when the external force seems modest. These geometric effects matter as much as material grade.

## Welded and bolted joints answer different needs

A weld can make a compact permanent connection without drilling holes, but introduces its own considerations: heat-affected material, residual stress, possible distortion, and stress concentration at weld geometry. A bolted connection can be disassembled and inspected, but requires room for tools and suitable contact surfaces. Welding and bolting should be selected for the actual load, environment, inspection needs, and repair plan.

For a vibrating machine, a full welded frame may be stiff enough but vulnerable at a poorly designed detail. A bolted frame may allow service but create looseness if the load path is wrong. Combining connections does not automatically add their capacities; welding and tightening in the wrong sequence can change preload or introduce unintended load sharing.

Corrosion interacts with fatigue. Pitting can create tiny notches, and water trapped at a joint can degrade contact surfaces. Galvanic coupling of dissimilar metals in an electrolyte can accelerate corrosion of one member. Coatings, drainage and material choice are therefore part of mechanical durability, not merely appearance.

## Observe before reinforcing

Suppose a bracket has cracked at the same corner twice. Welding over the crack or adding a thick plate may restore short-term stiffness but move stress to another location. Instead, trace the real load. Is the attached machine unbalanced? Are fasteners loose? Does the bracket flex in bending? Is a notch or weld termination creating a concentrated stress? Has vibration increased because a bearing is worn?

A useful failure investigation records the direction of the crack, condition of the fracture surfaces, nearby corrosion, bolt-hole elongation, and evidence of rubbing. Compare the failed location with where bending and tension should peak. Avoid assuming the first visible crack is the original cause; a loose base can force an otherwise adequate bracket into an unintended cyclic load.

For critical equipment, fracture assessment and fatigue-life estimates need properly qualified engineering methods. For ordinary workshop planning, the most transferable idea is already valuable: make load paths direct, avoid unnecessary sharp geometry, support parts against unintended flexing, preserve access for inspection, and design repairs to eliminate the failure mechanism rather than conceal its symptom.

The bracket did not fail because steel became mysteriously weaker after a year. Its geometry, load history, environment, and joints created a process that was invisible in a single static test. Durable fabrication begins by seeing the process before the crack appears.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Comparisons to draw

- Smooth-radius transition versus abrupt notched section under repeated axial loading.
- Single-lap joint with eccentric load path versus symmetric double-shear clevis.
- Weld termination and bolt hole as two different stress-concentration geometries.

### Workshop diagnostic exercise

A motor mount breaks near a slotted hole. Before selecting thicker steel, check fastener preload, shaft alignment, vibration spectra if measurable, surface fretting and slot-edge condition. Which failure clues would favor progressive fatigue over a single overload?

**Review boundary:** Do not infer fatigue life from average stress or weld appearance. Qualified structural or machinery connections require applicable design rules and inspection methods.

## Selected reading and evidence records (non-spoken)

- `nasa-crews-fatigue` — [J. H. Crews Jr., The Role of Stress Concentrations in Structural Fatigue, NASA TM X-61969 (1969)](https://ntrs.nasa.gov/citations/19690031796). Fatigue cracking under cyclic loading and geometric stress concentration.
- `asm-steel` — [ASM International, Metallurgy for the Non-Metallurgist: Heat Treatment of Steel (2011)](https://dl.asminternational.org/technical-books/monograph/114/chapter-abstract/2198506/Heat-Treatment-of-Steel). Iron-carbon transformations, quenching and tempering.
