# 010000 — Navigation in Poor Visibility and Decision Thresholds

<!-- BEGIN SPOKEN LECTURE -->

A group hikes along a clear ridge toward a marked trail junction. The map looks straightforward. Then fog rolls in, turning a distant summit into a pale silhouette and hiding the next trail marker. The trail underfoot still exists, but the visual landmarks that connected it to the map have disappeared. This is a different navigation problem from following a sunny-day route. The question is no longer only where to go. It is whether the group has enough reliable information to continue at all.

## Visibility is part of the navigation system

On a clear day, terrain association uses the relationship between mapped ridges, streams, slopes, and visible landmarks to determine position. In fog, snow, smoke, or heavy rain, that feedback weakens. A map can remain accurate while the person using it loses the ability to confirm their location. This matters because small directional errors compound with distance traveled.

Suppose a hiker leaves a known point intending to walk due north. A heading error of five degrees creates a cross-track offset of roughly eighty-seven meters over a kilometer in an idealized straight-line model. Real walking adds deviations around rocks, trees, and terrain. Even a good compass heading cannot ensure a person will land precisely at a narrow trail junction without intermediate checks.

A map and compass offer independent information from a battery-powered navigation device, but both require skill and context. A compass points toward local magnetic north, not necessarily geographic north. The angular difference is magnetic declination, which varies by location and changes over time. Local magnetic interference from metal objects or equipment can also deflect a compass. A map's printed declination diagram must be interpreted for its map date and current location rather than blindly reused forever.

## Treat position as a region, not a dot

A phone or satellite receiver may show a dot on a digital map. That dot is an estimate. Error can arise from satellite geometry, signal reflections, canopy cover, antenna quality, filtering, and the accuracy of the underlying map. A GPS position estimate and a drawn trail line may each have uncertainty, so their apparent alignment should not be treated as centimeter precision.

The navigation question is often whether a set of possible positions is contained within safe terrain. If the estimated location could be either side of a hazardous ridge or stream crossing, the uncertainty is operationally important. A position fix with small reported error can still be wrong because of map datum mismatch, delayed updates, or device faults. Independent features, when available, help confirm it.

A bearing, distance estimate, and known start point create a dead-reckoning prediction. Every step carries uncertainty, so use intermediate catching features: a road, stream, broad ridge, or obvious terrain boundary that tells you when you have gone far enough. A handrail feature, such as a stream or ridge line, can constrain motion. In poor visibility, robust features are more useful than relying on sighting one isolated rock or sign.

## Choose the kind of destination you can reliably find

A broad trail crossing a slope can be easier to intercept than a single small trail marker. One navigation technique deliberately aims slightly to one side of a linear feature, then follows it toward the target once found. This technique, often called aiming off, reduces ambiguity about which direction to search after reaching the feature. It works only when the feature is identifiable and safe to follow. A stream is not a safe handrail when it leads toward a waterfall or hazardous gorge.

In winter, apparent flatness is particularly deceptive. Snow can conceal trails and cover small depressions. A whiteout can remove visual contrast needed to judge slope and distance. Wind, cold, and fatigue also erode the ability to perform careful navigation. A line drawn across a map may cross avalanche terrain, unstable ice, or other hazards not captured by a generic shortest-path calculation.

## Decide thresholds before losing options

A turnaround rule is easiest to follow when defined before the group is tired. It may include a latest time to reverse course, a weather condition that ends an exposed ascent, a minimum remaining battery reserve, or the loss of a required location confirmation. These are examples of decision thresholds rather than universal numbers. They should be matched to route, terrain, group ability, daylight, and rescue access.

Imagine two choices in fog. One is to continue another kilometer toward a summit whose descent route is unfamiliar. The other is to return along a known ridge to a confirmed trail junction. If daylight is falling and the group's position estimate is broad, the second may carry less uncertainty even if it feels disappointing. Continuing has an opportunity cost: each step can increase the distance from known terrain and reduce the time available to reverse.

A group can use a preplanned decision point: if visibility is below what is needed to identify the next safe feature, or if the location cannot be confirmed independently, stop and reconsider. That does not always mean immediately walking back along a guessed direction. Sometimes holding position in a safe area, rechecking navigation sources, adding layers, or seeking assistance is better than moving while uncertain. The danger of standing still must also be considered in exposure, weather, and terrain context.

## Protect the information that survives

Before departure, download maps for offline use and verify that they open without connectivity. Carry a means of navigation that does not rely exclusively on a phone battery, and learn to use it. Note intended route, turnaround points, water sources, major terrain features, and emergency exits. Share the plan and expected return with someone who can act if the group does not arrive. Weather forecasts help plan, but they are not a guarantee of visibility on the ground.

If visibility deteriorates, record the last confirmed point. A confirmed point is a location supported by evidence, not merely the most recent GPS dot. Note direction and elapsed travel since it, distinguish estimated from verified positions, and reassess the route before moving farther. When using a compass, move away from large metal items to check the needle, and convert between true and magnetic bearings correctly for the area.

In a poor-visibility emergency, the decision to request help should not wait until every resource is exhausted. Communicating location, coordinates with datum if known, terrain, weather, injuries, and plans gives responders useful information. An emergency locator or satellite messenger can improve communication where cell service is absent, but signal access and device condition remain dependencies.

Navigation competence is partly the ability to find a route, and partly the ability to recognize when the evidence no longer supports continuing it. Fog changes not just the scenery but the structure of the decision. The skilled traveler maintains a chain of confirmed positions and chooses route and timing so that uncertainty does not silently grow beyond the terrain's margin for error.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Geometry

- Approximate lateral offset from heading error: `x = L sin(θ)`. At `L = 1000 m` and `θ = 5°`, `x ≈ 87.2 m` under ideal straight-line conditions.
- Magnetic bearing conversion requires location- and date-specific declination. A map's historic printed value can be stale.
- GNSS position uncertainty, digital basemap alignment, recorded tracks, and position-fix timing are distinct uncertainties.

### Decision exercise

A route crosses an open plateau with no visual markers for 1.2 km. Fog limits visibility to tens of meters, the phone has limited battery, and the group knows the last confirmed point. Compare (a) continuing on a magnetic bearing, (b) returning to a broad known terrain feature, and (c) pausing safely to restore navigation evidence. Define what observation would justify each option.

### Limits

Terrain hazard, weather, avalanche exposure, navigation training, and group condition change the safe decision. USGS map-and-compass guidance and GPS.gov accuracy notes explain measurement limits; local land-manager and weather alerts may control the actual trip.

## Selected reading and evidence records (non-spoken)

- `usgs-map-compass-guide` — [U.S. Geological Survey, Finding Your Way with Map and Compass](https://www.usgs.gov/educational-resources/finding-your-way-map-and-compass). Map scale, contour terrain interpretation and compass use
- `gpsgov-accuracy` — [US GPS.gov, GPS Accuracy](https://www.gps.gov/gps-accuracy). Consumer accuracy limits, multipath, blockage, receiver and map errors
- `noaa-declination` — [NOAA NCEI, Magnetic Declination](https://www.ncei.noaa.gov/products/magnetic-declination). Signed east-positive declination; magnetic-to-true bearing conversion
- `nysdec-hike-smart` — [New York State Department of Environmental Conservation, Hike Smart NY](https://dec.ny.gov/things-to-do/hiking/hike-smart-ny). Layering, shelter, water, weather and planning for exposure
