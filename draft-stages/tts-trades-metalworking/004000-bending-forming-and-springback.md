# 004000 — Bending, Forming, and Springback

**Track:** Metalworking and Fabrication. **Background:** Alloys, heat treatment, and subtractive processes. **Purpose:** explain how a sheet or bar can take a permanent new shape yet still elastically recover after forming.

<!-- BEGIN SPOKEN LECTURE -->

# Why the Metal Doesn't Stay at Ninety Degrees

A maker bends a strip of sheet metal in a brake until it looks like a right angle. The brake opens, the force comes off, and the part springs back a few degrees. They bend it farther, release it again, and finally reach the angle they want. Is the metal being stubborn? The behavior is a direct consequence of how solids respond to stress: part of their deformation is elastic, and part may be permanent.

Imagine first pulling gently on a metal spring. Release the force and it returns close to its original shape. That is elastic deformation. Now push a suitable metal strip hard enough that some material yields. After unloading, the permanently deformed part remains bent, but the elastic component recovers. The resulting change in angle is called springback. It depends on material properties, thickness, bend radius, tooling geometry, and the amount of deformation.

## Inside a bend, different regions do different things

Consider a straight sheet bent around a radius. Material toward the outside of the curve is stretched; material toward the inside is compressed. Somewhere through the thickness is a region with relatively little length change, often described using the neutral axis. In a real plastically bent section, the location and strain distribution depend on material and forming conditions. The farther a region lies from the neutral zone, the larger its bending strain, approximately speaking.

If the outside is stretched beyond what the material can accommodate, it may thin or crack. The inside may wrinkle or buckle under compression, especially in thin or unsupported sections. This is why bend radius matters. For the same sheet thickness and alloy, a very tight bend generally demands larger strains than a generous bend. But 'minimum radius' is not one constant for all metals: rolling direction, temper, surface quality, grain structure, and processing history can affect bendability.

## A bend is also an accounting problem

A bent part must have the right dimensions after forming. The length of the flat sheet is not simply the sum of the two outer flange dimensions. Some stock becomes the curved region, and the effective length along the material changes with bend geometry. Fabricators use bend allowance or bend deduction models, often calibrated for their actual tooling and material. A parameter commonly called the K factor expresses the approximate location of the neutral axis as a fraction of thickness in simplified models.

Suppose a box requires four bent flanges to meet at specified outside dimensions. If the blank is cut as if the bends occupied no material, the finished box will be wrong even when every angle is exactly ninety degrees. In production, a short test coupon can reveal the springback and blank-length correction for a particular setup. That feedback is often more reliable than treating a handbook coefficient as universally exact.

## Forming changes the metal

Plastic deformation can raise the strength of many metals locally through work hardening. The dislocation structure changes as the material is deformed; more stress may be needed to continue deforming it. The same process can reduce remaining ductility. Trying to correct a bend by repeatedly hammering the same region can produce a different response from the first bend. Work-hardened metals, heat-treated alloys, and brittle materials may crack or behave unpredictably when cold worked outside their suitable range.

Heating can change the behavior further, but it can also alter temper, coatings, corrosion resistance, and dimensional accuracy. A torch is not a generic solution to difficult bending. The correct process depends on the alloy and intended material properties. Similar reasoning applies to tubes: a bend may flatten the cross-section unless supported by appropriate dies, mandrels, or methods. A sharp bend in a tube carrying fluid can change its flow resistance as well as its mechanical durability.

## Processes solve different parts of the problem

Air bending uses a punch and die to deform a sheet without forcing it fully into the die cavity. Bottoming or coining involves a different contact and force regime, sometimes reducing springback but requiring different loads and tooling. Roll forming builds shape through repeated passes. Stretch bending deliberately places material in tension while bending. These are alternatives because the forces, strains, repeatability, and tooling economics differ.

A one-off bracket may be best made by simple bends and drilling. A long, consistent channel may justify roll forming. A shape with sharp corners, complex flanges, and tight tolerances may need a dedicated forming process or a fabricated assembly instead of one bent blank. 'Can it be bent?' is not the only question. Ask whether it can be bent repeatably without cracks, whether dimensions will be stable, and whether the result will perform in service.

The lesson is that metal forming is not merely an act of applying enough force. It is a controlled relationship between elastic recovery, permanent strain, material condition, tool geometry, and final dimension. A good fabricator anticipates springback, measures the first part, and adjusts the process without sacrificing the material.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Bend allowance and first-order strain

For a bend angle \(\theta\) in radians, inside radius \(R\), sheet thickness \(t\), and empirical K factor \(K\), a common simplified bend allowance is \(BA=\theta(R+Kt)\). The formula is a *process model*; \(K\) depends on geometry, material, and tooling, and is not always a transferable constant. Flat-pattern dimensions also depend on how flange lengths are referenced.

### Shop trial without a production assumption

Record alloy, temper, thickness, rolling direction, tooling radius, bend angle under load, relaxed angle, inside radius, crack observation and final flange lengths. Use scrap coupons of the same batch to calibrate bend allowance and springback; do not force thin metal with a hand setup that lacks appropriate guarding or rated capacity.

### Source scope

ASM Handbook's sheet-bending chapter discusses elastic-plastic behavior, springback, and bendability. It is a technical reference, not a certification of a specific tool setup or part design. Equipment manuals determine press-brake capacity, tooling limits and safe operation.

## Selected reading and claim sources (non-spoken)

- `asm-sheet-bending` — [ASM International, Bending of Sheet Metal, ASM Handbook Vol. 14B (Semiatin ed., 2006)](https://dl.asminternational.org/handbooks/edited-volume/35/chapter-abstract/461819/Bending-of-Sheet-Metal). Elastic-plastic bending, springback, bendability and process alternatives; abstract publicly checked.
