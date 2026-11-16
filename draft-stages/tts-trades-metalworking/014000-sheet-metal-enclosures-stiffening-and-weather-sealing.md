# 014000 — Sheet-Metal Enclosures, Stiffening, and Weather Sealing

<!-- BEGIN SPOKEN LECTURE -->

A flat sheet of metal can feel flimsy between your fingers, yet the same sheet folded into a shallow box can become remarkably stiff. The change comes from geometry. The material has not become stronger; the folds have moved material away from the neutral region of bending and created sections that resist deformation. This principle lets a relatively small quantity of metal protect electrical components, tools, controls, and mechanical assemblies.

Designing an enclosure is a problem in stiffness, fabrication, sealing, and future access. A beautiful box that fills with water, rattles at a motor frequency, or cannot be opened without cutting cables is not a finished design.

## Folding changes the structure

Imagine pressing down on the middle of a thin rectangular plate. It bends readily because material is concentrated near the plane where bending strain is small. Form the edges upward into flanges, and the section resists bending more effectively in certain directions. Fold another return lip and it may resist twisting and local buckling. Ribs and beads can stiffen large panels without greatly increasing thickness.

The geometry has tradeoffs. A sharp corner concentrates strain during forming. A wide unsupported panel can still vibrate and oil-can under pressure. A narrow flange may wrinkle, and a poorly placed stiffener can interfere with screws or hinges. Plan the load path: where will someone lift the box, where will it mount, and what forces do the hinges, handles, or internal equipment impose?

A sheet enclosure frequently needs folded edges for safe handling as well as stiffness. An exposed burr can cut a gasket or cable jacket. A hem provides a safer edge, but its cavity may trap liquid, complicate coating, or create crevices in a corrosive environment. Details that improve one property may compromise another, so the intended operating environment must guide them.

## Bends consume length

If you cut a flat rectangle whose side lengths match the desired outer dimensions and bend it, the finished part may be too small or too large. Material at a bend stretches on the outside and compresses on the inside. Somewhere through the thickness is a neutral region whose length changes less. Fabricators estimate the developed blank length using bend allowance or bend deduction based on material thickness, bend radius, and tooling.

There is no universal 'subtract one thickness per bend' rule that is exact for all materials. Stainless steel, aluminum alloy, and mild steel respond differently to radius and forming tools. Springback means the bend opens slightly after force is removed; the correction depends on material yield behavior and tooling. For a repeatable part, make and measure a small sample bend before committing expensive stock.

## Water follows openings and gravity

A box under a porch roof may receive rain blown sideways, splashback, and condensation. The top surface should shed water. A door seam facing upward can become a trough. A gasket compressed unevenly by poorly located screws can leak even if the material is marketed as waterproof. A cable entering through the top without an appropriate gland or drip detail may guide water directly inside.

Sealing should be understood as a continuous boundary. Trace it around every screw, lid, hinge penetration, connector, cable entry, and joint. Ask what happens when the housing flexes or when thermal expansion changes the gap. Gaskets need an appropriate compression range and compatible contact surfaces; crushing them harder can cause permanent set or uneven gaps. The enclosure may also need provision for condensation management, pressure equalization, or drainage, depending on the equipment and its listing.

Water resistance cannot be inferred from a photograph of a gasket. An enclosure rating such as an ingress protection or NEMA type is meaningful only when the complete product, including properly installed entries, is evaluated to the relevant standard. Cutting an extra hole into a listed box can compromise the original protection if the modification is not designed accordingly.

## Corrosion hides at interfaces

A painted panel can look excellent on its face and corrode rapidly at a cut edge, crevice, or contact between dissimilar metals. Electrolyte trapped under a gasket changes the local environment. Stainless steel fasteners in aluminum may create galvanic concerns in wet exposure, depending on area ratio, coatings, and drainage. Corrosion can also seize small screws so an enclosure intended to be maintainable becomes impossible to open.

Design the coating process around edges, bends, welds, and drilled holes, not only flat faces. If an outdoor box must be serviced every season, replaceable hardware and accessible fasteners are part of durability. A nonconductive gasket may interrupt electrical continuity between panels, which is important if the enclosure participates in equipment bonding. Metalwork and electrical safety have to be coordinated at that interface.

## Design backward from maintenance

Suppose a small control box contains a power supply and two cable terminals. The internal layout needs space for terminals, cable bend radii, any heat-generating components, and tool access. The enclosure needs a mounting pattern that does not distort the base, a lid that can open without disconnecting every cable, and identification that remains readable after weather exposure.

Start with the largest internal components and the required service clearance. Place hinges, flanges, and fasteners outside that clearance where possible. Determine which seams may see standing water. Route cables so a damaged gland can be replaced without dismantling the controls. Then unfold the box into a flat pattern and verify that every bend is manufacturable with the available brake and dies.

Build a paper or inexpensive sheet mock-up. Check the enclosure after bending, not only in the flat. A flange may collide with a hinge; a screwdriver may not reach a screw; a gasket may cross an uneven weld. Prototype defects are cheap compared with twenty identical boxes that cannot be assembled.

The best sheet-metal enclosure is not the heaviest one. It uses geometry to provide stiffness, details to keep contaminants out, and a layout that lets people maintain what it protects. In that sense an enclosure is a small engineered building: it must carry forces, manage water, tolerate temperature, and preserve the services inside it.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Fabrication worksheet

- Record material alloy, thickness, grain orientation where relevant, interior bend radii, tooling, reference edges, and finish/coating process.
- Make a bend coupon; derive **observed** bend allowance/deduction and springback rather than assuming a universal number.
- For each panel: evaluate unsupported span, flange section, hinge loads, vibration, attachment and required service access.
- Trace seal continuity and water shedding across seams, cable glands, lid fasteners, and bottom edges. Document condensation strategy and protective earth/bonding where applicable.

### Failure modes

| Observation | Possible mechanism | Useful check |
|---|---|---|
| Lid rocks despite tight screws | Twisted panel / uneven flange | Check sealing land flatness |
| Rust along cut edges | Damaged coating / trapped moisture | Inspect edge finish and drainage |
| Leaks at cable entries | Incompatible gland or orientation | Verify entry system and installation |
| Rattles near motor | Panel resonance / inadequate support | Measure vibration and add suitable stiffness |

**Review boundary:** Electrical equipment enclosures and environmental ratings require the appropriate product standards, testing/listing, installed cable-entry design, and bonding practices. Generic gasket choice is not certification of ingress protection.

## Selected reading and evidence records (non-spoken)

- `asm-sheet-bending` — [ASM International, Bending of Sheet Metal, ASM Handbook Vol. 14B (Semiatin ed., 2006)](https://dl.asminternational.org/handbooks/edited-volume/35/chapter-abstract/461819/Bending-of-Sheet-Metal). Elastic-plastic bending, springback, bendability and process alternatives; abstract publicly checked.
- `asme-y145-2018` — [ASME, Y14.5-2018 (R2024): Dimensioning and Tolerancing](https://www.asme.org/codes-standards/find-codes-standards/dimensioning-and-tolerancing). Geometric specification of part size, location, form, orientation, and datum relationships.
- `ampp-galvanic-corrosion` — [Association for Materials Protection and Performance, Galvanic Corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/galvanic-corrosion). Galvanic anode/cathode/electrolyte mechanisms and dissimilar-metal contact.
- `iso-fastener-grade` — [International Organization for Standardization, ISO 898-1:2013 Mechanical Properties of Fasteners Made of Carbon Steel and Alloy Steel](https://www.iso.org/standard/60610.html). Specified fastener property classes, ambient-temperature test domain and exclusions; full standard not claimed reviewed.
