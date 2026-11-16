# 013000 — Thermal Imaging, Blower Doors, and Diagnosing Envelope Leaks

<!-- BEGIN SPOKEN LECTURE -->

On a cold morning, a thermal camera makes a poorly insulated corner look like a dark stain. It is tempting to call the stain a leak. But what did the camera actually measure? Not the movement of air. Not the presence of water. The camera detected infrared radiation leaving the surfaces in its field of view, and its display estimated apparent surface temperatures from that radiation. The cold patch could result from a missing piece of insulation, a framing member conducting heat, a draft cooling the surface, a wet material, or even a reflection. An instrument becomes useful when we understand both the observation and the question it can answer.

A building enclosure has several transport paths. Heat conducts through solids, moves with air, and crosses cavities by radiation. Air flows through openings when pressure differences drive it. Rain enters where water-control details fail. Vapor diffuses through materials according to vapor-pressure differences. Diagnostics should separate those processes before deciding on a repair.

## What a blower door measures

A blower door is a calibrated fan temporarily installed in an exterior doorway. It moves air until the house reaches a controlled pressure difference relative to outdoors. At a widely used reference pressure of fifty pascals, the instrument measures the airflow needed to maintain that difference. If it takes twelve hundred cubic feet per minute to keep the house depressurized by fifty pascals, the test result is twelve hundred CFM50. This is a measurement of enclosure leakage under a deliberately imposed test condition, not a statement that twelve hundred cubic feet per minute constantly enters the house in ordinary weather.

To compare houses of different size, practitioners may report air changes per hour at fifty pascals, or ACH50. Multiply CFM50 by sixty minutes and divide by the volume of the tested enclosure in cubic feet. For a twenty-thousand-cubic-foot house and twelve hundred CFM50, that is three point six ACH50. Notice the missing ingredient: the building's natural pressure history. Wind speed, indoor-outdoor temperature, height, and mechanical fans change pressures hour by hour. A measured ACH50 cannot be converted to normal ventilation by one universally valid multiplier.

The test boundary also matters. A conditioned basement, a crawlspace, and an attached garage are not interchangeable parts of the volume calculation. Open windows, intentional dampers, fireplaces, and air-handling systems must be set according to the test protocol. An apparently improved result may reflect changed test configuration rather than better workmanship.

## Use pressure to make a hidden leak visible

Consider a cold ceiling edge that shows up on a thermal camera. First observe it with the fan off. Then establish a controlled depressurization, and observe again while the indoor-outdoor temperature difference remains useful. If the cold area expands or develops a streak consistent with incoming air, that change supports an air-leak hypothesis. If the temperature pattern remains stationary along a framing member, a thermal bridge becomes more plausible. Neither conclusion is automatic. Air movement can be slow, insulation can be discontinuous, and sunlight or changing HVAC operation can distort the comparison.

A smoke pencil or other appropriate airflow indicator can supplement the image near accessible gaps. It shows local air movement in the test condition, not the hidden route through which the air entered the assembly. A draft at a baseboard may originate in an attic bypass far from the observed outlet. Sealing the visible exit without understanding the route can leave an important cavity connection unresolved.

## The limits of infrared photographs

The camera depends on surface emissivity. Most painted plaster and many building materials radiate reasonably well for ordinary comparisons. Polished metal and reflective glass are different: their apparent temperature may be dominated by reflected surroundings. Wet surfaces may cool through evaporation, but a cool region is not proof of a leak or concealed moisture. Conversely, wet materials can be close to surrounding temperature, and a camera may miss them entirely.

Thermal images also depend on timing. A sun-warmed wall retains heat after sunset. A radiator recently turned off leaves a recognizable warm patch. A heavy masonry wall reacts slowly to weather. A camera used after a stable temperature period and with the building's operating state recorded gives more interpretable evidence than a dramatic photograph taken at an arbitrary moment. Confirm suspected moisture with appropriate inspection and independent measurements, not with color alone.

## Plan the diagnostic sequence

Start with a specific question: Is this room cold because of air leakage, missing insulation, window performance, or insufficient heat delivery? Record outdoor temperature, recent weather, indoor setpoints, exhaust fans, and visible construction. Look for patterns at penetrations, top plates, rim joists, attic hatches, and transitions between assemblies. Use a blower door to quantify whole-enclosure leakage and help locate accessible paths. Use thermal imaging to compare surface patterns under known conditions. When appropriate, perform targeted pressure measurements to separate duct leakage, enclosure leakage, and room-to-room pressure imbalances.

After repair, test again using comparable settings. A reduction in measured leakage is meaningful, but it does not by itself establish adequate indoor air quality, safe combustion operation, or moisture durability. Airtightness is one part of an enclosure, and intentional ventilation is another.

The best diagnostic report contains more than a colorful thermal image. It states the hypothesis, the controlled conditions, the measurements, the competing explanations, the repair made, and the observation that would falsify the conclusion. That is how a tool becomes a method.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Quantitative example

`ACH50 = CFM50 × 60 / enclosed volume in ft³`. If `CFM50 = 1,200` and the test enclosure is `20,000 ft³`, then `ACH50 = 3.6`. This is the fan-driven 50 Pa reference result, **not** a measured natural air-change rate. Record which spaces were included, test pressure direction, and setup.

### Diagnostic worksheet

| Observation | Candidate explanation | Discriminating check |
|---|---|---|
| Cold line over studs | Conductive thermal bridging | Compare with known framing layout and fan-off pattern |
| Cold streak enlarges under depressurization | Incoming outdoor air | Controlled pressure comparison and local airflow indicator |
| Cool area below window after rain | Bulk water, air leakage, or conductive edge | Correlate with precipitation and verify moisture independently |
| Reflective surface reads wildly different | Low emissivity / reflected radiation | Compare a suitable high-emissivity reference surface |

**Review boundary:** Follow a recognized blower-door protocol and arrange combustion safety/ventilation evaluation where relevant. No single thermal image diagnoses moisture or certifies performance. Avoid interpreting one ACH50 value as natural ventilation.

## Selected reading and evidence records (non-spoken)

- `doe-airsealing-audit-2010` — [U.S. Department of Energy, Building America Best Practices Series: Retrofit Techniques and Technologies—Air Sealing, A Guide for Contractors to Share with Homeowners (2010)](https://www.energy.gov/sites/prod/files/2013/11/f5/ba_airsealing_report.pdf). Blower-door reference pressure and calibrated airflow; infrared thermography under controlled conditions.
- `pnnl-air-flow` — [PNNL Building America Solution Center: Building Science Introduction — Air Flow](https://basc.pnnl.gov/information/building-science-introduction-air-flow). Stack effect, neutral pressure plane, wind and duct leakage.
- `pnnl-cold-condensation` — [PNNL Building America Solution Center, Condensation Control for Walls in Cold Weather](https://basc.pnnl.gov/resource-guides/condensation-control-walls-cold-weather). Air leakage versus vapor diffusion; exterior insulation and assembly drying pathways.
- `doe-air-vapor` — [DOE Building Science Education, Air Barriers vs Vapor Barriers](https://bsesc.energy.gov/energy-basics/building-enclosure-air-barriers-vs-vapor-barriers-continuous-sealed-wrb-walls). Separate air leakage, vapor diffusion and water-management functions.
