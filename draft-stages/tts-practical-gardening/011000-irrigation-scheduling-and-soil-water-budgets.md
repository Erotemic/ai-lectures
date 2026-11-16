# 011000 — Irrigation Scheduling and Soil Water Budgets

<!-- BEGIN SPOKEN LECTURE -->

A garden may receive water every morning and still suffer from drought stress, poor root development, or fungal disease. Another garden may go several days without irrigation and remain healthy. The difference is not simply whether the plants are watered. It is how much water enters the root zone, how much can be stored there, how fast the plants and atmosphere remove it, and whether excess water can leave without depriving roots of oxygen.

Think of soil as a reservoir, not a sponge of unlimited capacity. Pores between soil particles contain air and water. After a thorough wetting, gravitational drainage removes some water from the largest pores. Plant roots can access a portion of what remains, but as the soil dries, water is held increasingly tightly by capillary and surface forces. The point at which water becomes difficult for the plant to extract depends on soil and plant characteristics, not just whether the top looks dusty.

## The budget has inputs, stores, and outputs

Water enters through rain and irrigation. It can leave by direct evaporation from soil, transpiration through plants, runoff over the surface, and drainage below the active roots. In irrigation science, evapotranspiration combines evaporation and transpiration. Weather—solar radiation, temperature, humidity, wind—changes demand. Plant size, species, growth stage, and rooting depth alter how much of that demand corresponds to the planted area.

A simplified accounting statement is that change in stored root-zone water equals rainfall plus irrigation minus evapotranspiration, runoff, and deep drainage. This is not a perfect model because water distribution is spatially variable and soil properties change with depth. Still, it prevents a common error: setting a timer without estimating how much water actually reaches the roots or how much the plants use.

## Inches of water are a depth, not a clock time

An inch of water means an equivalent layer one inch deep over an area, whether it arrives in an hour or over a day. The runtime needed to apply that depth depends on a sprinkler's precipitation rate and uniformity. A hose nozzle, drip emitter, oscillating sprinkler, and in-ground rotor do not deliver equivalent depths during equal minutes. Some locations may receive twice as much as others because of overlap, wind, pressure, or blocked emitters.

A useful observation is a catch-can test for sprinklers. Place several equal-sided containers across a zone, run the system for a measured time, and compare collected water depths. That reveals both an approximate application rate and its variation. For drip systems, emitter flow ratings and actual operating pressure require attention; checking one emitter does not establish uniform delivery over an entire long line.

## Roots, infiltration, and runoff

Water applied faster than soil can accept may run off before penetrating to the roots. Compacted soils, crusting, slope, and prior wetness all affect infiltration. Splitting an irrigation event into shorter cycles with pauses can sometimes allow water to soak in, especially on slopes or low-infiltration sites. But if the root zone is already saturated, adding more water may worsen oxygen limitation and disease risk.

Shallow frequent watering can maintain moisture near the surface while leaving deeper soil dry, depending on plant and soil. Very long watering may push water below the root zone, wasting water and potentially transporting nutrients. The best depth and interval depend on rooting conditions, recent planting, precipitation, and the species' tolerance. Newly planted trees have a different root distribution from established trees even when their canopies look similar.

## Feedback beats a fixed seasonal timer

A scheduled controller provides convenience but may keep the same pattern after a cool wet week and a hot windy week. Weather-responsive controllers adjust watering based on estimated demand; soil-moisture controllers can prevent watering when a measured threshold is already satisfied. The EPA WaterSense program describes performance criteria for soil-moisture-based control technologies. A sensor must still be placed in representative soil at a meaningful depth, and poor installation can produce misleading measurements.

A buried moisture sensor reads conditions at one location. A garden bed with different sun exposure, mulch, soils, or plant species may not share those conditions. Manual soil inspection, plant response, rain measurements, and simple observation remain useful. A wilted plant is not always thirsty: root disease, transplant shock, and waterlogged soil can also reduce effective water uptake. Watering automatically at every sign of wilting can make the problem worse.

## A practical irrigation audit

Choose a zone of the yard. Record soil texture, slope, plant type, mulch, and approximate rooting depth. Measure or estimate applied water, note recent rain, and check moisture several inches below the surface rather than judging solely by color. Compare areas that dry quickly with shaded or low spots. Record whether water ponds, runs off, or drains after a reasonable interval. Adjust schedule based on observations, then repeat after a weather change.

An irrigation plan is a feedback system: estimate demand, supply water at a rate the soil can accept, measure what happened, and revise. The goal is not to maximize gallons delivered. It is to maintain enough accessible water and air in the root zone while avoiding runoff, unnecessary evaporation, and persistent saturation. Once you understand the budget, a controller becomes a tool for expressing your judgment rather than a substitute for it.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Simplified water accounting

\[\Delta S = P + I - ET - R - D\]

where \(S\) is root-zone storage, \(P\) rainfall, \(I\) irrigation, \(ET\) evapotranspiration, \(R\) runoff, and \(D\) below-root-zone drainage, all in equivalent water-depth units over a time period. Additional lateral inflow/outflow terms may matter.

### Unit example

One inch over 100 square feet is about 62.3 US gallons (\(100 \times 1/12\) cubic feet times 7.4805 gallons/ft³). This is gross applied volume, not necessarily stored plant-available water. A sprinkler averaging 0.5 inches per hour would take roughly two hours for one nominal inch before runoff or wind losses are considered.

### Source scope

USDA NRCS soil water and root-zone resources, FAO irrigation and evapotranspiration fundamentals, EPA WaterSense soil-moisture control criteria. Agricultural ET coefficients are not universally transferable to every landscaped bed or indoor planting. Verify water restrictions and backflow protection requirements locally.

## Selected reading and evidence records (non-spoken)

- `nrcs-water` — [USDA NRCS, Soil Health for Water Quality and Quantity](https://www.nrcs.usda.gov/conservation-basics/soil/soil-health/soil-health-for-water-quality-and-quantity). Infiltration, retention and structure.
- `nrcs-agronomy-manual` — [USDA NRCS, National Agronomy Manual (Part 504: Water Management)](https://www.nrcs.usda.gov/sites/default/files/2022-10/National-Agronomy-Manual.pdf). Water potential, field capacity, and permanent wilting point.
- `usace-evapo` — [U.S. Army Corps of Engineers HEC, Evaporation and Transpiration Basic Concepts](https://www.hec.usace.army.mil/confluence/hmsdocs/hmstrm/evaporation-and-transpiration/evaporation-and-transpiration-basic-concepts). Stomata and soil-plant-atmosphere water transport.
- `epa-watersense-soil-controller` — [EPA WaterSense, Soil Moisture-Based Irrigation Controllers](https://www.epa.gov/watersense/soil-moisture-based-irrigation-controllers). Feedback irrigation controllers with soil-moisture thresholds.
