# 005000 — Drilling and Hole Geometry

**Track:** Tools, Measurement, and Workmanship. **Background:** layout, cutting, and workholding. **Purpose:** treat a hole as a designed geometry with an entry, axis, depth, and exit.

<!-- BEGIN SPOKEN LECTURE -->

# A drilled hole is more than a missing circle

You mark a dot on a board, put a drill bit on the dot, pull the trigger, and find that the hole emerges a centimeter away from where you expected on the other face. The entry point was correct. The hole was wrong. What failed was not necessarily the mark: it might have been the angle of the drill, the way the bit followed the wood grain, or the force used as the tool broke through. A hole has position, diameter, depth, direction, surface quality, and an exit condition. Every one of those can matter.

Before choosing a drill, ask what the hole is for. A screw pilot hole, a clearance hole, a dowel hole, a countersink, a plumbing penetration, and a threaded hole are different geometric problems. Their apparent similarity can conceal major differences in accuracy and behavior.

## Locate the axis, not merely the center

Imagine placing a long dowel through the desired hole. The dowel shows you that a circular mark is only the intersection of a three-dimensional axis with the work surface. If the axis needs to be square to the face, you must control the drill's orientation. If it must meet another hole inside a thick piece, small angular errors accumulate with depth. A one-degree tilt over a hundred millimeters produces roughly one-point-seven millimeters of lateral displacement. That may be tolerable for a loose cable passage but unacceptable for a locating pin.

A drill press constrains an axis relative to a table more consistently than freehand operation, but it does not make the setup automatically correct. The table might be tilted. The workpiece might rock on a chip. A curved surface may move when the bit first engages. A machine vise, clamping fixture, drill guide, or sacrificial support can be more important than buying a more expensive bit. A long slender bit can deflect under side force even when the spindle starts true.

On a portable drill, posture and sightlines matter. Looking from only one direction can conceal angular error in the perpendicular plane. For a critical bore, establish a guide or a reliable reference, rather than trusting that the bit appears straight from one viewpoint.

## Bits make different holes

A twist drill has helical flutes that form and remove chips. In metal, the cutting edges need appropriate feed and cutting speed, and chips must have somewhere to go. In wood, common twist drills work, but brad-point bits can locate more predictably on the fibers and produce cleaner entry geometry. Spade bits are fast for comparatively coarse holes; augers remove larger volumes of wood and tend to pull into it; Forstner bits make controlled flat-bottomed recesses in suitable setups. A hole saw removes a ring, leaving a core, and introduces different chip-clearing and torque demands.

In masonry, the material is brittle and abrasive. Rotary hammer bits break material by impact combined with rotation rather than shearing it like an ordinary metal drill. The correct bit and machine depend on brick, mortar, concrete, reinforcement, and the required anchor system. A nominal hole diameter may be only one part of an anchor's specification: depth, cleaning procedure, substrate condition and edge distance can determine whether the installed fastening works.

A drill can also make a hole larger than its own nominal diameter. Runout, chatter, motion of the workpiece, and damage at the entrance can all enlarge it. A high-quality bearing fit or dowel hole may require boring or reaming after drilling. A tap drill is intentionally smaller than the nominal screw thread so the thread has material to form into. Clearance holes intentionally permit a bolt shank to pass without engaging the material. Those choices belong to the joint design rather than a single universal drill chart.

## What happens at the far side

Breakthrough is a change in cutting conditions. The last thin web of material may tear rather than cut, especially in wood and laminates. A backer board supports it. Reduced feed near exit can help, as can drilling from a controlled pilot or from both faces when accurate references are available. In thin metal, the drill can grab when the point breaks through. A handheld workpiece may spin with substantial torque; the correct response is to restrain the work mechanically, not to grip it harder.

Deburring matters. A sharp metal burr can damage a cable sheath, cut skin, prevent parts from seating, or give a false impression of thickness when measuring. A countersink may create a recess for a fastener head, but removing too much can weaken the joint or split thin material. A cable hole through an edge may need a protective bushing, grommet, or other approved protection; smooth visual appearance is not enough if the service condition can abrade the cable later.

## Design a hole-making sequence

Suppose a bracket must be attached with two bolts. First identify the mating surfaces and their location tolerances. Mark from a consistent datum, and decide whether both parts can be held together and transfer-punched. Plan how to restrain the work and keep the bit away from hidden services. Choose a pilot, clearance, counterbore, or threaded geometry as required. Keep drilling chips from building up in the hole. Finish the opening, remove burrs, and test alignment before the whole assembly is installed.

This sequence explains why poor holes create assembly problems later. A bolt forced through offset holes bends the joint into compliance; it is not evidence that the holes were correct. A screw that wedges in an undersized clearance hole may pull one member away rather than clamp two surfaces together. A mounting hole drilled through a water-control layer introduces a new sealing obligation that should have been considered before the drill touched the surface.

The best hole is not the most precise hole possible. It is the hole whose size, axis, finish, and location suit the job, produced with a setup that controls the relevant sources of error. Good drilling begins with geometric intent and ends with an inspected result.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Geometry and tolerance

For an axis with angular deviation `theta`, approximate lateral displacement after depth `L` is `L tan(theta)`. At `L = 100 mm`, `theta = 1 degree`, displacement is approximately `1.75 mm`.

Distinguish nominal bit diameter, actual finished bore diameter, positional tolerance, perpendicularity, and surface finish. Consult specific hardware standards or manufacturer installation instructions for fastener clearance, tap drill sizing, anchor hole cleaning and embedment.

### Observation exercise

Use scrap material and suitable restraint to compare clean entry, exit, and sidewall for several bit types. Record whether a backed-up exit is cleaner and whether the hole axis meets a marked target. Rotating stock must be clamped; do not hold a workpiece in the hand under a drill press. Check hidden wiring, plumbing and structural restrictions before making building penetrations.

## Selected reading and claim sources (non-spoken)

- `osha-drill-press` — [OSHA, Woodworking eTool — Drill Presses](https://www.osha.gov/etools/woodworking/production/machines-tools/drill-press). Clamping stock, twist hazards and drill press operational constraints.
- `osha-hand-power-tools` — [OSHA, Hand and Power Tools (OSHA 3080)](https://www.osha.gov/sites/default/files/publications/OSHA3080.pdf). Tool guarding, securing work with clamps and correct tool operation.
