# 003000 — Air Leakage, Pressure Differences, and Stack Effect

**Track:** Building Science. **Background:** Elementary heat flow and enclosure concepts. **Purpose:** explain why the same gap behaves differently with wind, weather, and mechanical equipment.

<!-- BEGIN SPOKEN LECTURE -->

# A House Breathes Through Its Leaks

Imagine a cold morning in a two-story house. A narrow crack at the attic hatch blows warm air into the attic. A nearly identical crack beside a basement window admits cold air. Neither crack contains a fan. The air moves because the pressure on one side differs from the pressure on the other. To understand the building, we need to understand where those differences come from.

A gap does not generate airflow on its own. It provides a path. Pressure supplies the push. The size and shape of the gap resist that push. Airflow depends on both. A large, unobstructed gap under a modest pressure difference may move more air than a tiny gap under a stronger one. That is why counting visible cracks is not a reliable measure of a building's leakage.

## The pressure map is not uniform

Start with warm indoor air. Heating generally makes a given volume of air less dense than the same volume of colder outdoor air, at comparable pressure and composition. A column of warm air therefore weighs less than a column of cold air of the same height. As elevation changes, pressure falls in each column, but the rates differ. Over the height of a house that difference matters.

In a typical cold-weather stack-effect pattern, indoor pressure relative to outdoors is negative near the bottom of the building and positive near the top. Air enters through available lower openings and leaves through upper openings. Somewhere between those regions is a neutral pressure level: at that particular height, the inside-outside pressure difference is zero, for the simplified case. The location is not automatically the middle of the building. The amount and distribution of leakage at different heights affect it.

Temperature difference and height matter. A taller, warmer building generally develops a stronger stack pressure pattern than a shorter building under otherwise similar conditions. But a building is not an isolated laboratory column. Doors, stairwells, ducts, chimneys, and room partitions change how well interior spaces communicate. A closed interior door can help create a local pressure relationship that differs from the simple whole-house picture.

## Wind adds a second pressure field

On a windy day, air piles up against the windward side of a house and flows around the edges and over the roof. Some exterior surfaces experience higher pressure; others experience suction. The actual pattern depends on wind speed, direction, nearby buildings, and the house's geometry. Consequently, wind may reinforce the stack effect at one opening and oppose it at another.

That is why one drafty window can seem quiet on Tuesday and troublesome on Wednesday. The opening has not changed. The conditions that drive it have. A tissue near a gap can indicate the direction of local air movement at that moment, but it cannot tell you the home's total leakage or identify the complete path.

## Fans can rearrange the entire map

Now turn on a kitchen exhaust hood. It sends indoor air outdoors. Unless another source supplies replacement air, the house tends to become more negative relative to outside. Replacement air enters through whatever paths offer the least resistance: a designed make-up-air opening, an open window, a building leak, or potentially an inappropriate route through a chimney or combustion appliance.

A forced-air heating system can also change local pressures. A supply duct leaking into an attic carries conditioned air outside the enclosure. A return duct leaking in a crawlspace can draw unconditioned air toward the system. The effects depend on where the leaks occur and whether those spaces are inside or outside the intended pressure boundary. Calling a duct leak 'inside the house' is not enough; one must know the boundary.

This matters because air can transport moisture, odors, particles, and combustion products along with heat. A cold-weather exfiltration leak near a roof is more than an energy concern. Warm indoor air moving into cold assemblies may cool below its dew point and deposit moisture there. A vapor-control material does not necessarily stop this flow: controlling diffusion through a material and controlling bulk air movement through a hole are different jobs.

## Follow the continuous boundary

An air barrier is best understood as a continuous system, not one magical product. Drywall, sheathing, membranes, sealants, and transitions may all help form it. The important question is whether the chosen boundary connects across floors, walls, roofs, openings, and penetrations. Where does it turn around a rim joist? How does it meet a window? Does the attic hatch join that boundary, or interrupt it?

Suppose you seal a visible crack around a window but leave a plumbing chase open from the basement to the attic. The large vertical pathway may continue to dominate the stack-driven flow. Conversely, a deliberate, well-connected air boundary can lower uncontrolled leakage even if the walls contain many different layers of material. Air tightness does not mean eliminating planned ventilation. It means separating accidental exchange from ventilation that can be measured and controlled.

## Testing separates stories from measurements

A blower door uses a calibrated fan to create a controlled pressure difference between a building and outdoors. With suitable instruments, it measures airflow needed to maintain that difference. A common diagnostic value is air changes per hour at fifty pascals, often called A C H fifty. It is a test quantity, not a claim that the house changes all its air at that rate during ordinary weather. Natural exchange depends on wind, temperature, and the actual pressure differences occurring over time.

A blower-door test tells you something about aggregate leakage. Smoke pencils, pressure measurements, and systematic investigation help locate particular paths. Thermal cameras can suggest where cold air may be entering, but a cool surface can also result from thermal bridging rather than airflow. The best diagnosis uses observations that distinguish explanations instead of treating every cold patch as the same defect.

Return to the basement crack and the attic hatch. Their behavior now has a causal account. They lie at different heights in a building with warmer indoor air; wind and fans modify the pressure field; the cracks supply paths. Repair is not a contest to apply sealant to the greatest number of spots. It is the work of identifying a continuous pressure boundary, finding consequential breaks, and preserving deliberate pathways for ventilation and safe equipment operation.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### A simplified stack-pressure relation

For two approximately isothermal columns, the difference in inside-outside pressure change over height \(H\) is approximately \(\Delta p(H)=gH(\rho_{out}-\rho_{in})\). Location of the neutral pressure level determines the sign at a given elevation; real assemblies require a leakage-network model and may have multiple interacting zones. For fixed pressure, leakage flow through an opening is often approximated empirically as \(Q=C |\Delta p|^n\), with the exponent dependent on leakage geometry. Do not use a universal exponent or infer natural infiltration directly from ACH50.

### Observation exercise

Sketch the intended air barrier in a vertical house section. Trace continuity through the attic access, top plates, wall-to-foundation junction, window perimeter, and service penetrations. Separately mark the paths for planned ventilation, drainage, and combustion exhaust. For a draft near a window, record outdoor temperature, wind direction, and active exhaust devices rather than assuming the cause from touch alone.

### Scope and review

The qualitative stack-effect model is established building physics. Diagnostic thresholds, exhaust make-up air, and safe combustion venting depend on actual appliances, configuration, local adopted codes, and professional testing. This lecture provides no combustion-appliance commissioning protocol. No field design has been verified.

## Selected reading and claim sources (non-spoken)

- `pnnl-air-flow` — [PNNL Building America Solution Center: Building Science Introduction — Air Flow](https://basc.pnnl.gov/information/building-science-introduction-air-flow). Stack effect, neutral pressure plane, wind and duct leakage.
- `doe-air-vapor` — [DOE Building Science Education, Air Barriers vs Vapor Barriers](https://bsesc.energy.gov/energy-basics/building-enclosure-air-barriers-vs-vapor-barriers-continuous-sealed-wrb-walls). Separate air leakage, vapor diffusion and water-management functions.
