# 016000 — Machining and Welding Dissimilar Metals

<!-- BEGIN SPOKEN LECTURE -->

A steel bracket needs to attach to an aluminum frame. The two pieces fit perfectly in the workshop, but a year outdoors they show corrosion around their contact points, or a weld cracks after repeated heating and cooling. We may be tempted to blame poor workmanship alone. Yet even a neatly made joint can fail if its materials are mechanically, chemically, or metallurgically incompatible. Joining dissimilar metals begins by asking what is different about them and how those differences will matter during fabrication and service.

## Three mismatches in one joint

First, metals expand by different amounts when their temperature changes. Aluminum generally expands more per degree than carbon steel. If they are rigidly locked together across a substantial length, repeated heating can create stress, slip, or distortion. A small slot, compliant interface, or suitable connection geometry may accommodate differential movement. But those details must still carry the intended loads; movement allowance is a design feature, not permission for a loose or weak joint.

Second, metals in electrical contact can participate in galvanic corrosion when an electrolyte such as rainwater bridges them. The relative electrochemical behavior of the metals, their exposed areas, coatings, and the environment determine which part corrodes preferentially and how fast. A stainless fastener in aluminum may seem like an upgrade because the screw itself resists rust, yet the aluminum around the fastener may be more vulnerable in a wet, salty environment. The exact effect depends on alloy and geometry; a galvanic series alone is not a service-life prediction.

Third, metallurgical compatibility limits the way different alloys can be fused. Some combinations produce brittle phases at the joining interface, develop very different weld-pool behavior, or lose carefully selected base-metal properties through heat. Aluminum-to-steel fusion welding is not simply carbon-steel welding with a hotter torch. An apparently bonded interface may fail because of brittle intermetallic layers. The appropriate process may instead be a designed mechanical joint, brazing method, transition piece, or specialized joining process qualified for that combination.

## Joining is a system choice

A mechanical connection can keep base metals below their melting temperatures, but it introduces holes, stress concentrations, fastener-bearing contact, and possible corrosion paths. A brazed joint uses a filler that melts while base metals remain solid, provided wetting, gap, cleaning, and temperature compatibility are controlled. A welded joint melts and fuses material locally, potentially creating a heat-affected zone with properties different from the original stock. Adhesive bonding offers another route, but surface preparation, cure, long-term exposure, and bond-area geometry become central.

No method wins for all combinations. Consider a stainless tube joined to a carbon-steel support. A weld can be workable with the correct filler, procedure, joint details, and inspection, but the weld and heat-affected zones may have different corrosion performance than either untouched base metal. The correct filler is not determined by choosing the one whose label sounds closest to the tube. Applicable welding procedure specifications and manufacturer metallurgy guidance matter.

Machining dissimilar parts also involves different behavior. Aluminum can smear or form a built-up edge under inappropriate cutting conditions, while hard steel may require different tooling, speed, coolant, and rigidity. Clamping pressure that securely holds steel might crush a thin aluminum profile. Burrs and edge damage at a hole can concentrate stress or breach a protective finish. Tool selection should follow alloy, geometry, tolerances, and finish requirements rather than a universal speed chart.

## Design the corrosion boundary

For an outdoor bracket, sketch all electrical-contact paths and all places water can remain trapped. A polymer washer or barrier coating may break an electrical pathway, but only if the design does not reconnect the metals through another fastener or exposed edge. Coatings can be damaged during drilling or assembly. Narrow crevices may trap electrolyte. Water shedding and drainage can be as important as material selection.

Do not assume every dissimilar-metal contact is disastrous. Dry indoor contact, controlled environments, sacrificial protection, and appropriate alloy pairs can perform well. The question is the electrochemical exposure and service requirement. Likewise, designing the joint so it can be inspected and a sacrificial component replaced may be more robust than promising it will never corrode.

## Build a joining decision record

Write down the alloys and temper or heat treatment, not just 'steel' and 'aluminum.' Record expected temperature range, wet or dry exposure, load type, fatigue cycles, electrical continuity requirements, appearance, inspectability, and repair options. Then compare candidate processes. A weld procedure must address joint preparation, filler, heat input, shielding or flux, and inspection; a mechanical joint must address fastener capacity, bearing, fatigue, corrosion and movement. Many of those values require actual product data or engineering design.

Try a simple thought experiment: the bracket must survive outdoor freeze-thaw cycles and occasionally be removed. Mechanical attachment may offer easier maintenance than a permanent fusion joint. But the chosen fasteners must resist expected loads and maintain a compatible corrosion barrier. Conversely, a thin closed vessel or pressure-bearing component may have design and inspection rules that eliminate casual attachment experiments altogether.

The important move is to stop asking 'Can these metals be joined?' and ask 'By what process, with what resulting properties, under what service conditions, and how will failure be detected?' A good joint survives because its chemistry, mechanical response, and environment were considered together—not because the finished bead or screw head looked impressive.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Dissimilarity matrix:** relative thermal expansion; galvanic pairing and area ratio; strength/stiffness; melting behavior; heat-affected-zone response; possible intermetallic formation; coating compatibility; exposure; repairability.

**Joint options:** bolted with electrical isolation where appropriate; brazed with specified filler and surface preparation; fusion welded only with qualified compatible procedure; adhesive with validated surface preparation and environmental limits; specialized transition component. Exact process compatibility is alloy-, temper-, and procedure-specific.

**Illustrative differential expansion:** `ΔL_difference = L × (α_A − α_B) × ΔT`. This predicts free expansion difference, not the final stress in a constrained joint. Galvanic tables alone do not predict corrosion rates.

**Scope:** Weld process qualification, structural/pressure joint design, fume controls, and critical-component inspection require applicable standards and professional competence.

## Selected reading and source locators (non-spoken)

- `ampp-galvanic-corrosion` — [Association for Materials Protection and Performance, Galvanic Corrosion](https://www.ampp.org/technical-research/impact/corrosion-basics/group-1/galvanic-corrosion). Galvanic anode/cathode/electrolyte mechanisms and dissimilar-metal contact.
- `aws-brazing-handbook-fifth` — [American Welding Society C3 Committee on Brazing and Soldering, Brazing Handbook, Fifth Edition, preface](https://pubs.aws.org/download_pdfs/brh-2007pv.pdf). Brazing definition, capillary action and joint preparation.
- `osha-welding` — [OSHA, Welding, Cutting and Brazing: Hazards and Solutions](https://www.osha.gov/welding-cutting-brazing/hazards-solutions/). Fumes, ultraviolet radiation, burns, electric shock and protective controls.
- `asm-sheet-bending` — [ASM International, Bending of Sheet Metal, ASM Handbook Vol. 14B (Semiatin ed., 2006)](https://dl.asminternational.org/handbooks/edited-volume/35/chapter-abstract/461819/Bending-of-Sheet-Metal). Elastic-plastic bending, springback, bendability and process alternatives; abstract publicly checked.
