# 003000 — Compass Bearings, True and Magnetic North

**Track:** Navigation and Outdoor Skills. **Background:** Topographic maps, contour lines, and map scale. **Purpose:** connect bearings on a map to directions shown by a magnetic compass.

<!-- BEGIN SPOKEN LECTURE -->

# North Is a Question With More Than One Answer

Imagine standing at a trail junction with a map in one hand and a magnetic compass in the other. The map says the next ridge lies northeast. You align the compass and head away, but later the ridge appears farther to your right than expected. Perhaps you followed the wrong spur. Perhaps your map and compass used different definitions of north. Before either explanation can be tested, we need to understand what a bearing actually measures.

A bearing is a direction expressed as an angle, often clockwise from a chosen north reference. Zero degrees points north, ninety east, one hundred eighty south, and two hundred seventy west. But the reference word 'north' hides several possibilities.

## True north and magnetic north

True north is the direction along Earth's surface toward the geographic North Pole, as defined by the local meridian. Magnetic north, for a compass, is the direction of the horizontal component of Earth's magnetic field at that location. It does not necessarily point exactly toward the moving north magnetic pole, and it does not generally match true north.

The angular difference between the local magnetic direction and true north is magnetic declination. Under the convention used by NOAA, east declination is positive and west declination is negative. The value depends on location and changes with time. A diagram printed on an old map therefore describes its survey or publication context; it may need updating for present-day navigation.

There is also grid north, the direction of a map's chosen north-south coordinate grid. On many map projections, grid north differs slightly from true north except along selected lines. A topographic map may show a declination diagram with true, magnetic, and grid north distinguished. Those arrows are not decorative. They tell you how to translate between two different coordinate systems.

## A conversion that can be checked

Suppose the local magnetic declination is twelve degrees east. You take a magnetic bearing of seventy degrees with a correctly used compass. Under NOAA's signed convention, the true bearing is seventy plus twelve, or eighty-two degrees. Now reverse the question. If the map indicates a true bearing of eighty-two degrees, you would subtract the twelve-degree east declination to obtain a magnetic bearing of seventy degrees.

For a west declination, use a negative number. If the declination were eight degrees west, a magnetic bearing of seventy degrees would correspond to a true bearing of sixty-two degrees. That is much safer than memorizing an ambiguous phrase like 'add east, subtract west' without knowing which direction the conversion is going.

Different compass designs allow different workflows. With an adjustable-declination compass, you may set the correct local declination and work directly in true bearings according to its instructions. With a non-adjustable compass, you may convert map bearings before setting the dial. Be consistent about the reference used by GPS, map, and compass. Do not apply the declination correction twice.

## Orienting the map

In simple terms, orienting a map means rotating it so features on paper correspond to directions in the terrain. A compass can assist, but first you must know what its north arrow and the map's north reference represent. Metallic objects, electronic devices, power lines, and nearby magnetic materials can distort a compass reading. If the needle behaves erratically, move away from the source and repeat the observation.

You can also orient by recognizable terrain. If two distinctive ridgelines or a visible road junction align with known map features, that provides an independent check. A compass heading that contradicts every clear terrain feature deserves investigation, not automatic obedience.

## Follow a bearing as a path, not a spell

Suppose a hilltop lies somewhere ahead on a given bearing. You set the bearing, then select a visible landmark on that line: a tree, boulder, or terrain notch. Walk toward it while observing ground conditions, then repeat. This is more reliable than staring continuously at the compass and drifting around obstacles without tracking the original direction.

When detouring around a pond or steep slope, the direction of travel temporarily changes. The navigation task is to recover your intended route using terrain, map features, or a planned offset. 'Keep walking northeast' is not enough because terrain is not a frictionless plane. Distance, elevation, and identifiable features are as important as azimuth.

A bearing is one constraint on position, not a complete location. If you know neither your starting location nor distance traveled, a perfect bearing still leaves many possible places on the map. Conversely, two well-identified landmarks and their bearings can help narrow location when geometry permits. Accuracy depends on landmark identification, declination, compass handling, and the map's own precision.

## The compass works only inside its assumptions

Near certain polar regions, the horizontal magnetic field can be weak enough that magnetic-compass directions become unreliable. More commonly, local magnetic interference and user error dominate. A compass tilted far from level, held near steel, or read with the wrong end of the needle can lead to substantial errors. The compass responds to a real field, not to your intention.

Today's phones and GPS devices can display true or magnetic courses, sometimes with their own conversion settings. Their electronic compasses may require calibration, and a displayed heading can differ from direction of travel when the device is stationary. The ability to read a topographic map and compare multiple observations remains useful when electronics fail or disagree.

## A small field exercise

In an open, familiar area, identify a distinctive landmark whose position is clear on a map. Record the map's north reference and the date of its declination information. Obtain a suitable current declination for your location, then take a magnetic bearing to the landmark. Convert it to true, and compare with the map bearing. Repeat the observation after moving away from cars, metal railings, and other potential interference.

The value of the exercise is not merely getting close to the right number. It is learning to state which north you used, how you converted, and how you checked the result. Navigation improves when directions become documented measurements rather than instincts dressed in degrees.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Signed declination convention

Using NOAA's convention, **true bearing = magnetic bearing + signed declination** (modulo `360°`), with east positive and west negative. The reverse is `magnetic = true − signed declination`. Example: `magnetic 70° + east 12° = true 82°`; `magnetic 70° + west 8° = true 62°`.

Grid bearings need separate **grid convergence** corrections based on map projection and location; do not silently equate true north with grid north. Device software may already have corrected heading and must not be corrected again.

### Evidence and application

NOAA NCEI's magnetic declination pages explain signed conversion, variation by location/time, and local disturbances. The USGS 'How Should I Set My GPS and Compass?' provides a practical example of adjustable and non-adjustable compass workflows. Obtain a current location-specific value before real navigation. This narrated lesson is not a substitute for a current map, route plan, and field skill.

## Selected reading and claim sources (non-spoken)

- `noaa-declination` — [NOAA NCEI, Magnetic Declination](https://www.ncei.noaa.gov/products/magnetic-declination). Signed east-positive declination; magnetic-to-true bearing conversion.
- `usgs-gps-compass` — [USGS, How Should I Set My GPS and Compass?](https://www.usgs.gov/educational-resources/how-should-i-set-my-gps-and-compass). Practical examples converting GPS/map references and compass settings.
- `nps-compass` — [National Park Service, Compass—Great Smoky Mountains National Park](https://www.nps.gov/grsm/planyourvisit/compass.htm). Magnetic declination and north reference.
