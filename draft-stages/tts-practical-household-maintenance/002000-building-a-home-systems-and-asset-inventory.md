# 002000 — Building a Home Systems and Asset Inventory

**Track:** Household Systems and Maintenance. **Background:** Failure modes, observations and repair priorities. **Purpose:** construct a useful household asset map instead of an unmaintainable list of objects.

<!-- BEGIN SPOKEN LECTURE -->

# A House Should Have a Map of Its Own

A homeowner usually knows where the refrigerator is. But do they know which breaker protects its outlet? Where the supply line branches? Whether its water filter is still sold? Which valve stops a leak under the sink? Maintenance often becomes urgent precisely when these answers are missing. The important object is not a fancy spreadsheet. It is a map of the home's systems, dependencies and points of control.

An asset inventory sounds like bureaucracy until you discover what it enables. A water heater fails on a Saturday. You can tell a service company the model, age and location, identify the energy source, find the appropriate isolation controls and describe the symptoms. A blocked drain affects two fixtures: you already know which rooms share a branch. A smoke alarm chirps: you know its location and replacement type. Organized information reduces the uncertainty of a real decision.

## Start with systems, not purchases

A practical home inventory begins at the service boundaries: water supply, waste drainage, electrical service, heating and cooling, ventilation, fuel supply where present, network connectivity, roof drainage and building enclosure. Some houses also have wells, septic systems, sump pumps, backup generators, solar equipment, irrigation or security systems. Do not list a device without understanding which system it serves.

For each system, identify its major equipment, control points, pathways and dependencies. The furnace needs energy and airflow. A sump pump needs an electrical supply, a functioning float or sensor, a discharge route and a place where water can be expelled. A camera may need PoE, network connectivity, storage and a service that delivers notifications. A single visible device can depend on several invisible services.

## What to record for an asset

Useful fields include location, function, make and model when available, serial number when appropriate, installation or estimated age, filter and consumable specifications, manuals, warranty information, service history and any observed problem. Add a photograph of the nameplate and another showing the equipment in context. Record a service contact where one has proved useful. Not every door hinge needs a database entry; select assets whose failure, replacement or maintenance would benefit from having a record.

For a main shutoff, model numbers may matter less than a photograph of the location, a label and the boundary it controls. For an appliance, the model number may be essential for parts. For a roof, material type, installation history, repair sites and inspection photographs may be more useful than a serial number. Information should match the asset.

## Build the dependency graph

Imagine a basement dehumidifier empties into a condensate pump, which discharges through a tube to a drain. A full bucket alarm might arise from pump failure, a clogged tube, loss of power or a blocked drain. If the inventory records only “dehumidifier,” it hides the components that explain the failure.

A dependency graph can be simple text. Dehumidifier depends on outlet circuit, air circulation and condensate disposal. Condensate pump depends on power, float mechanism and discharge path. The relevant question is: if this component stops working, which other functions change? The answer can identify critical single points of failure and sensible inspection priorities.

The same method reveals dependencies across trades. A water heater may require plumbing, electricity or fuel, ventilation or combustion air, and drainage for relief or condensate depending on design. Any plan that describes it as “just plumbing” may omit important work.

## Prioritize consequences, not cosmetic drama

A little peeled paint is visible; a slowly leaking pipe behind a wall may not be. Visibility and urgency are different. For each known issue, ask about consequence if ignored, evidence of progression, likelihood of failure, and how quickly the situation can become expensive or dangerous. A roof leak above finished ceilings may deserve priority even if the surface stain is small. A squeaky door may have low consequence despite being annoying.

Use categories rather than false numerical precision. Immediate: loss of a protective function or active serious damage. Planned: significant risk but stable for the moment. Routine: predictable maintenance such as filters or inspections. Optional: comfort and cosmetic work. These labels should be revised as evidence changes. The point is not to create a perfect ranking; it is to make tradeoffs explicit.

## A maintenance history is diagnostic evidence

A log of dates, observations, photographs, work performed and outcomes can reveal patterns. Suppose a ceiling stain appears after wind-driven rain from the east but not after ordinary rain. That observation is more diagnostic than a vague note reading “roof leak.” Suppose a pump stops working only during sustained rainfall. A timeline may reveal that intermittent use concealed a marginal motor or clogged discharge path.

Records also help distinguish a repair from a temporary symptom change. If a technician resets a device and it works for a day, that is a different outcome from identifying and correcting the failure mechanism and testing it under comparable conditions. Record both the action and the verification, not merely “fixed.”

## The inventory must be usable under stress

An elaborate database can fail as an emergency tool if no one knows its password or where the file lives. Consider a compact offline copy of critical information: main water shutoff location, electrical panel labels, important contact numbers, major equipment locations and a few annotated photographs. Store more detailed manuals and service histories where they can be backed up and shared appropriately. Avoid making an internet connection a prerequisite for finding a water shutoff during an outage.

Photographs are especially useful for equipment hidden behind panels or located in similar-looking corners. Date the images so future residents can tell whether the configuration may have changed. A labeled sketch often complements photographs better than fifty unorganized phone pictures.

## Build it in layers

You need not inventory an entire building at once. First capture high-consequence controls and critical equipment. Next add major serviceable assets and their maintenance intervals. Then add system diagrams and records of recurring problems. Each layer should provide value even if the project stops there.

The test of an inventory is not how many rows it contains. Ask whether someone unfamiliar with the home could answer: where does this service enter, what stops it, which equipment depends on it, what has failed before, and what evidence should we gather next? A useful inventory turns those questions into straightforward lookups rather than desperate exploration. It makes the house more understandable, maintainable and resilient.

<!-- END SPOKEN LECTURE -->

## Technical companion: minimal data model

Suggested schema: `system_id`, `asset_id`, `location`, `function`, `upstream_dependencies`, `downstream_dependents`, `control_or_isolation`, `make`, `model`, `serial_optional`, `installed_or_estimated_date`, `maintenance_interval_source`, `last_service_date`, `manual_link`, `photo_ref`, `failure_mode`, `observed_condition`, `next_action`, `verification_note`. Store sensitive identifying service records locally or with appropriate permissions.

**Examples:** Water supply -> main shutoff -> optional PRV -> branch shutoff -> fixture. Building drainage -> gutter -> downspout -> discharge path -> grading. Network -> router -> switch -> PoE endpoint -> recording device. These are illustrative graphs, not assumptions about a given house.

**Evidence and limits:** EPA WaterSense home maintenance advice supports leak inspection and monitoring; DOE enclosure references distinguish moisture pathways; CDC mold guidance links moisture conditions to consequences. Scheduling is asset/manufacturer-specific, not a universally valid annual checklist. No application or service must be added to the repository to use this inventory.

**Exercise:** Create a one-page emergency map of a hypothetical home with water shutoff, electrical panel, heating equipment, smoke/CO alarms and one drainage path. Mark each unverified item with a question mark rather than an invented fact.

## Selected reading and evidence (non-spoken)

- `epa-maintenance` — [EPA WaterSense, Home Maintenance](https://www.epa.gov/watersense/home-maintenance). Leak monitoring and water-using systems.
- `doe-air-vapor` — [DOE Building Science Education, Air Barriers vs Vapor Barriers](https://bsesc.energy.gov/energy-basics/building-enclosure-air-barriers-vs-vapor-barriers-continuous-sealed-wrb-walls). Different enclosure moisture pathways.
- `cdc-mold` — [CDC, Mold, Testing, and Remediation](https://www.cdc.gov/niosh/mold/testing-remediation/index.html). Moisture as the major cause of indoor mold growth.
