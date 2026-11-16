# 003000 — Sawing, Drilling, Grinding, and Machining

**Track:** Metalworking and Fabrication. **Background:** Alloy families, heat treatment, and material behavior. **Purpose:** show how tools remove material and why process choice changes accuracy and finish.

<!-- BEGIN SPOKEN LECTURE -->

# Every Cut Has a Mechanism

A workshop has four ways to shorten a steel bar: a hacksaw, a powered band saw, an abrasive cutoff wheel, and a milling machine. All can remove material, but they do not do the same physical thing. The saw and milling cutter form chips with sharp edges. The abrasive wheel removes a multitude of tiny fragments through grains acting as cutting points. The finished surface, heat generated, material loss, cost, and required fixturing can differ greatly.

Understanding these differences prevents a familiar mistake: treating every cutting problem as a demand for more motor power. The shape of the tool, the material, the chip, the support, and the removal rate are often more important.

## Chips are how sharp tools make space

A cutting tooth penetrates material and forces a small region to deform until material shears away as a chip. It takes work to form that chip, and much of the work becomes heat in the chip, tool, and workpiece. A dull tool may rub and plow rather than cut efficiently. That can make the operation hotter, require greater force, and worsen the finish.

In drilling, two cutting edges near the drill's point remove metal while helical flutes carry chips away. The drill also has a central region that tends to push and deform material rather than cut as effectively as the outer lips. Material, point geometry, drill diameter, feed, and speed affect the result. If chips cannot escape from a deep hole, the cutting action deteriorates and torque may rise.

A drill press provides a more controlled spindle axis than many handheld operations, but it cannot compensate for a workpiece that is free to spin. A piece of flat metal that suddenly catches on the drill can rotate violently. Secure workholding is therefore part of the cutting method, not merely an accessory. The same principle applies to mills and lathes: the cutting forces have to close through a stiff, predictable path into a fixture and machine structure.

## Speed is measured at the cutting edge

A rotating tool has an angular speed, often stated in revolutions per minute. The outer edge travels farther per revolution than a point near the center. Surface cutting speed is proportional to diameter times rotational speed. Thus two drills turning at the same revolutions per minute do not have the same cutting speed if their diameters differ.

For a given work material and tool type, suitable cutting speed and feed must be selected together. Running a large drill as fast as a tiny one can overheat a cutting edge; feeding too lightly may cause rubbing instead of effective chip formation. Conversely, overly aggressive feed can overload a tool or workholding setup. Manufacturers' tables are starting points under specified conditions, not universal promises about every machine and alloy.

## What grinding does differently

A grinding wheel contains abrasive grains bonded into a rotating body. Each exposed grain can act as a small cutting tool. As grains dull or fracture and the bond wears, new edges may be exposed, depending on the wheel design. Grinding can produce fine finishes or shape hard materials, but it also concentrates heat near the contact.

An overheated surface may discolor, distort, change hardness, or develop residual stress. The right wheel, dressing condition, feed, cooling method, and contact geometry matter. Abrasive discs have application-specific ratings and operating limits; a cutting disc is not automatically a safe side-grinding wheel. A wheel's permitted speed, guard, and mounting instructions are part of the process definition.

## Roughing and finishing are separate goals

Suppose the job is to make a flat mounting plate with a precisely located bolt hole. A saw cut may establish the rough outline. A mill or file may refine the edge and bring it to size. A drilled hole may be sufficient for an ordinary bolt clearance; a reamed or bored hole may be appropriate where a controlled fit is needed. Deburring removes sharp projections without ideally changing the functional dimensions.

This sequence recognizes that a process often has strengths and limitations. A rough operation removes material efficiently but may leave an imperfect finish. A finishing operation can improve accuracy or surface condition when enough material remains to do so. The shop concept is an allowance: reserve material for the later operation instead of trying to make the first cut perfect.

Measurement closes the loop. If a hole is the wrong size, determine whether the cutter wandered, the part shifted, the machine deflected, the tool was unsuitable, or the reading was misleading. It is not enough to inspect only the tool after the operation.

## Heat and cutting fluid

Cutting fluids can cool, lubricate, help remove chips, and protect against corrosion. Their effectiveness depends on reaching the cutting zone and being compatible with the machine, work material, and tooling. A fluid that works for one operation may be unsuitable for another. Fluids and mists also create exposure and maintenance concerns; good control addresses delivery, ventilation, and housekeeping, not simply choosing a bottle with a familiar label.

For some materials and tooling, dry cutting may be the designed process. For others, controlled coolant delivery is important. The useful question is which mechanism limits the operation: edge temperature, chip welding, abrasion, chip evacuation, distortion, or something else.

## Choose a process by its required result

Return to the steel bar. If it only needs to be shorter, sawing may be simplest. If the end must be flat and accurately perpendicular for a mating part, a second finishing operation may be needed. If the material is hardened and a fine surface is required, grinding might be suitable with the correct wheel and setup. If many identical parts are needed, fixturing and process repeatability may dominate tool choice.

Good metalworking begins with a drawing of the result, then asks how to remove unwanted material without losing the geometry that must remain. Think of the forces, chip or abrasive contact, heat path, rigidity, and measurement. The metal does not care which machine is most impressive. It responds to the actual cutting conditions.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Calculations and method map

For a cutter diameter `D` in meters and rotational speed `N` in revolutions per minute, surface speed is `V = π D N / 60` meters per second. Actual speeds and feeds must come from appropriate cutting-tool and material data and the capabilities of a guarded, properly configured machine.

| Method | Basic removal mechanism | Typical selection question |
|---|---|---|
| Sawing | Teeth form chips along a kerf | Is efficient separation the main goal? |
| Drilling | Two cutting lips and chip evacuation | Is a round hole of suitable quality sufficient? |
| Milling/turning | Defined-edge chips with controlled tool path | Is dimensional control or finish required? |
| Grinding | Many abrasive cutting contacts | Is hardness, form, or fine finish decisive? |

### Field limits

OSHA discusses metalworking fluid cooling, lubrication, mist, and exposure-control mechanisms. Machine-specific guarding, chuck/workholding requirements, wheel ratings, applicable PPE, and operational procedures must come from equipment instructions and workplace training. No machine RPM or unsafe workholding procedure is specified here.

## Selected reading and claim sources (non-spoken)

- `osha-mwf` — [OSHA, Metalworking Fluids: Safety and Health Best Practices Manual](https://www.osha.gov/metalworking-fluids/manual). Tool/workpiece heat, chip removal, cooling and lubrication of machining operations.
- `osha-mwf-exposure` — [OSHA, Metalworking Fluids: Evaluating Exposure](https://www.osha.gov/metalworking-fluids/exposure-evaluation). Mist exposure controls and fluid delivery.
