# 011000 — Machining Tolerances, Fits, and Surface Finish

<!-- BEGIN SPOKEN LECTURE -->

A shaft measures almost exactly ten millimeters across. A hole also measures almost exactly ten millimeters. Will the shaft slide into the hole, press in firmly, or refuse to fit? The answer depends on differences too small to see casually, on the geometry of both surfaces, and sometimes on temperature and roughness. Manufacturing is not about producing an abstract perfect dimension. It is about defining an acceptable range that makes the assembly work.

The nominal dimension is a name for the intended size family. A tolerance specifies permitted variation. If a shaft is specified as 10.000 millimeters plus or minus 0.010, acceptable shaft diameters lie within a small interval. But the fit depends on the interval specified for the hole too. A hole near the small end of its allowance and a shaft near the large end produce a different clearance than the opposite combination.

## Clearance, transition, and interference

A clearance fit has room between mating parts under the specified limits. It allows assembly or relative motion, though the clearance may be very small. An interference fit intentionally has a shaft larger than its mating hole at assembly conditions, requiring elastic deformation, press force, or thermal assembly methods. A transition fit may produce small clearance in some permitted combinations and interference in others. None of these is an intrinsic property of an exact nominal diameter.

Fit standards provide systems of tolerance zones so a designer can specify mating parts economically. The common hole-basis approach keeps a standardized hole tolerance zone while choosing a shaft zone for the desired fit. Manufacturing processes often control holes and shafts with different capabilities and costs. A practical design should not demand an extremely tight tolerance merely because the drawing software permits it. Tighter limits increase measurement demands, scrap risk, and sometimes processing cost.

## Dimensions are not geometry

Imagine a cylindrical shaft whose diameter measures correctly at one point. It might still be tapered, oval, bent, or rough enough to jam in a long bearing bore. Similarly, a hole can have the correct nominal diameter but be misaligned with another hole. Geometric tolerancing addresses form, orientation, location, and runout, beyond simple size. The specific datum system explains what the geometry is measured relative to. Without datums, terms such as "straight" or "centered" can be ambiguous.

A mating surface must satisfy the actual function. A pin that rotates needs suitable roundness, straightness, and lubrication behavior; a stationary dowel may prioritize accurate positioning. A sealing face has different demands from a decorative surface. The most valuable drawing is not the one with the greatest number of digits, but the one that names the functional relationships clearly.

## Roughness is not waviness, and neither is size

Surface roughness describes fine-scale texture left by cutting, grinding, polishing, or other processes. Waviness describes longer-scale variations. A smooth-looking surface can still be out of flat, and a flat surface can be microscopically rough. Roughness parameters, such as the arithmetic average height Ra, summarize selected texture features; a single number does not capture all aspects of a surface or guarantee sealing performance.

Tool geometry, feed, speed, vibration, workholding, and tool wear influence surface finish. A sharp, stable cutting tool under controlled conditions may leave a different surface from a dull tool rubbing and tearing material. When vibration excites the machine-workpiece system, periodic chatter marks can appear. Polishing may improve some texture measures yet alter size or edge geometry in ways that harm fit. Surface preparation must follow function.

## Measurement has its own tolerances

A caliper reads conveniently but can be misleading when used near the limits of its accuracy. Jaw pressure, part temperature, zero error, burrs, and measurement location matter. A micrometer may provide better resolution and repeatability for an external diameter, but it too requires appropriate calibration and method. Internal diameters may need bore gauges, plug gauges, or other instruments. A reading of 10.00 does not demonstrate that a part conforms to a ten-micrometer tolerance.

A gauge is especially useful when it directly tests the functional acceptance limits. In a go/no-go system, a compliant part passes the intended limit checks without requiring the inspector to infer geometry from a single casual measurement. But gauges must themselves be controlled, and form errors or surface defects may require separate inspection.

## Heat and assembly force

Steel expands with temperature. Over a short temperature change, linear thermal expansion is approximately proportional to the original dimension and the temperature change. A small shaft may expand only micrometers, but at a tightly controlled fit those micrometers matter. Heating a housing or cooling a shaft can make some interference assemblies possible without excessive force, provided the materials, heat treatment, surface finish, and safety limits permit the process. Thermal assembly is not a universal fix for a mistakenly designed joint.

When pressing parts together, alignment and support prevent damage. Force should reach the component that actually resists it: pressing a bearing into a housing through the wrong ring can transmit damaging forces through rolling elements. Manufacturer procedures matter because interference, lubricant, chamfer, and shoulder details alter the process.

The engineering question is always functional. Does the part need to rotate, locate, seal, transmit torque, or come apart for service? Define the fit for that requirement. Then specify geometry and finish, choose a feasible process, and select a measurement method capable of distinguishing acceptable from unacceptable parts. The most elegant machining tolerance is one that is neither vague nor unnecessarily restrictive.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Limit-stack example

Hole limits: 10.010 to 10.030 mm. Shaft limits: 9.990 to 10.000 mm. Minimum clearance = 10.010 − 10.000 = 0.010 mm; maximum clearance = 10.030 − 9.990 = 0.040 mm. These *hypothetical* limits are for teaching interval arithmetic, not a named ISO fit or a recommended machine design.

### Distinctions

- **Size**: permitted upper/lower dimensions.
- **Form**: roundness, flatness, straightness.
- **Location/orientation**: feature position relative to defined datums.
- **Surface texture**: fine-scale roughness, waviness, lay; functional needs dictate which parameter matters.
- **Metrology**: uncertainty, resolution and repeatability of the actual method; instrument readout precision alone is insufficient.

### Exercise

For each of a sliding hinge pin, press-fit dowel, bearing journal, and O-ring gland, list functional needs, fitting behavior, geometric controls, and a sensible inspection method. Follow ISO/ASME and manufacturer specifications for actual production designs; no unverified fits are supplied here.

## Selected reading and evidence records (non-spoken)

- `asme-y145-2018` — [ASME, Y14.5-2018 (R2024): Dimensioning and Tolerancing](https://www.asme.org/codes-standards/find-codes-standards/dimensioning-and-tolerancing). Geometric specification of part size, location, form, orientation, and datum relationships.
- `osha-mwf` — [OSHA, Metalworking Fluids: Safety and Health Best Practices Manual](https://www.osha.gov/metalworking-fluids/manual). Tool/workpiece heat, chip removal, cooling and lubrication of machining operations.
- `iso-fastener-grade` — [International Organization for Standardization, ISO 898-1:2013 Mechanical Properties of Fasteners Made of Carbon Steel and Alloy Steel](https://www.iso.org/standard/60610.html). Specified fastener property classes, ambient-temperature test domain and exclusions; full standard not claimed reviewed.
