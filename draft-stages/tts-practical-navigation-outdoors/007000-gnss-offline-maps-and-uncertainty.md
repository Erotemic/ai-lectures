# 007000 — GNSS, Offline Maps, and Uncertainty

**Track:** Navigation and Outdoor Skills. **Background:** Topographic maps, compass bearings, terrain, and weather-aware planning. **Purpose:** use satellite positioning without surrendering independent navigation or mistaking a displayed dot for exact knowledge.

<!-- BEGIN SPOKEN LECTURE -->

# The blue dot is an estimate

A phone map places a blue dot beside a trail. It seems authoritative because the dot is crisp and the screen is precise. In reality, the position is an estimate with uncertainty. The device receives radio signals, interprets timing information, and solves for a location. Terrain, tree canopy, rock walls, buildings, receiver design, and satellite geometry can all degrade that solution. A map can be beautifully detailed while the position estimate is wrong by enough to put the dot on the neighboring trail.

Global Navigation Satellite Systems, or GNSS, include GPS and other satellite constellations. A receiver estimates distances using signal travel time and satellite data. It needs enough independent geometric information to solve for position and receiver clock error. Its accuracy is not the same as the precision of the displayed coordinates. Showing six decimal places does not mean the underlying estimate is accurate to centimeters.

## Offline maps and satellite position are different dependencies

An offline map is geographic data stored on the device before a trip. GNSS positioning uses radio signals from satellites, not the same data connection used to download map tiles. A phone may determine its position in airplane mode while the downloaded topographic map still displays; exact behavior depends on device settings and hardware. Conversely, a navigation app may have accurate satellite positioning yet show an empty background because the relevant map was never downloaded.

Test the system before leaving coverage. Download the intended area, including a buffer around alternative routes. Verify that the map opens with cellular and Wi-Fi data disabled. Check whether elevation, contour lines, waypoints, and track recording function without an account service. Do not discover on the trail that the application requires a login or an online license check to display stored information.

Offline availability does not guarantee map currency. Trails move, bridges wash out, access rules change, and roads close. A stored map is a snapshot. Compare it with current official route or land-management information when planning, and treat visible signs and terrain conditions as evidence during travel.

## How a fix goes wrong

Satellite geometry matters. If most visible satellites lie in a similar direction, small ranging errors can produce larger uncertainty in position. Signal blockage reduces the available measurements. Reflections from cliffs or buildings can create multipath: the receiver interprets a reflected signal as though it traveled directly. Under dense trees or deep valleys, the displayed dot can jump, drift, or lag the real path.

GPS.gov explains that smartphone accuracy under open sky can be on the order of several meters and becomes worse near buildings and trees. That is not a universal specification for every phone or location. Accuracy indicators in consumer apps vary in meaning and calibration. Treat them as cues, not as guarantees.

A more important risk is map matching. Software may snap the position estimate to a trail line it thinks you are following. If two trails run close together, a visually clean dot exactly on a path can conceal the fact that the underlying position is ambiguous. Turn-by-turn prompts may then send you along the wrong branch.

## Use independent anchors

A competent navigator connects the digital position with landscape evidence. At a junction, compare trail direction, contour shape, slope, nearby stream crossings, distance traveled, and visible landmarks. A compass bearing and a topographic map provide an independent framework. When the dot disagrees with strong terrain evidence, stop at a safe place and resolve the discrepancy rather than following the dot deeper into uncertainty.

Distance itself is not always measured in the same way. An app can report distance along a recorded track or straight-line distance to a waypoint. A steep winding trail may require much more travel than the horizontal displacement between two coordinate points. Elevation gain and descent affect time and energy. Good route planning therefore includes terrain, not just a line between coordinates.

Some devices continue estimating motion using accelerometers, gyroscopes, step counting, or cellular and Wi-Fi signals. These can help bridge short gaps, but errors can accumulate. Magnetic compasses in phones are susceptible to local magnetic interference, including metal objects and nearby electronics. A digital heading is not necessarily reliable when the device is stationary or surrounded by magnetic disturbance.

## Redundancy has to be usable

Carrying an extra battery is useful only if the charging cable works and the device can operate in wet or cold conditions. A second navigation app helps only if it does not share the same unavailable map service or account dependency. A paper map and compass help only if you know how to use them and can identify the place where you are on the paper. Redundancy must be independent enough to survive the failure being considered.

Before a trip, record the trailhead location, intended route, major junctions, expected return time, and bailout options. Share the plan with someone who can act if you do not return. Set a turnaround criterion based on daylight, weather, water, fitness, and uncertainty rather than on a single remaining-distance figure.

## A junction exercise

Imagine two paths diverging near a stream. Your phone places you on the left path, but both paths run within the indicated position-uncertainty circle. The left one climbs; the right follows the valley. Look at the contour lines, observe your actual slope and the stream's location, and verify the compass direction. If those observations support the right path, the location estimate has not earned the authority to override them. You can wait for a better fix in an open area or retrace to a known landmark.

The most important navigation tool is not the blue dot or the paper map alone. It is the habit of combining uncertain measurements with independent terrain observations and a plan for what to do when they disagree.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Three independent error sources

1. **Positioning:** GNSS geometry, blockage, multipath, receiver characteristics.
2. **Map:** stale geometry, mislocated trail, wrong datum/projection, incorrect labels.
3. **Interpretation:** wrong junction identified, snapped display, route-distance versus straight-line confusion.

### Pre-trip test

Download a topographic map and a buffer around the route; disable data connections; confirm map viewing and location fixes; save waypoints; carry another navigation method; record a return plan and offline contact instructions. For a true offline trial, verify every app feature you expect to need.

**Review boundary:** The uncertainty of any particular fix depends on conditions and receiver performance. Digital navigation does not replace terrain awareness, weather judgment, and reliable emergency planning.

## Selected reading and evidence records (non-spoken)

- `gpsgov-accuracy` — [US GPS.gov, GPS Accuracy](https://www.gps.gov/gps-accuracy). Consumer accuracy limits, multipath, blockage, receiver and map errors.
- `usgs-map-compass` — [U.S. Geological Survey, Finding Your Way with Map and Compass (2000)](https://www.usgs.gov/publications/finding-your-way-map-and-compass-0). Elevation, distance, direction and terrain reading.
