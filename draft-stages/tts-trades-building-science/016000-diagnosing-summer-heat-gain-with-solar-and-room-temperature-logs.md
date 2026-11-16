# 016000 — Diagnosing Summer Heat Gain with Solar and Room Temperature Logs

<!-- BEGIN SPOKEN LECTURE -->

One room becomes unbearably hot at four in the afternoon. Another room, supplied by the same air conditioner, stays comfortable. The thermostat in the hallway declares success. What exactly would convince us that the first room has a solar-gain problem rather than a supply-air problem? We need observations that separate the explanations. A room-temperature log is useful, but a temperature curve by itself does not reveal where the heat came from.

## A room is an energy balance, not just a thermometer

At any moment, energy enters through sunlight, warm surfaces, ventilation and leakage, occupants, lights, and equipment. The cooling system removes some of it. The room and its contents store the difference for a time. That storage matters because rooms do not respond instantaneously. Sun warms a floor, a couch, and the inside of a wall; those objects then warm the surrounding air. By the time the air thermometer reaches its maximum, the strongest solar exposure may already be over.

Sunlight arriving through a window is not the same thing as conduction through its glazing. Conductive heat transfer depends on the temperature difference, area, and whole-window U-factor. Solar gain depends on incident solar power, orientation, shading, and solar heat-gain coefficient. Picture three square meters of sunlit glass receiving six hundred watts per square meter. At an illustrative solar heat-gain coefficient of one half, about nine hundred watts of solar gain enters at that instant. That is a substantial load even if the outside air is cooler than the inside air. But it is a snapshot calculation, not an hourly or seasonal forecast.

A temperature sensor in the room also has its own environment. Place it in direct sun and you may be measuring a sun-warmed sensor body. Place it beside a supply vent and it may report a temperature no occupant experiences. A useful log needs a repeatable location away from radiators, supply jets, windows, appliances, and direct solar exposure. If possible, add a second measurement of relative humidity and record the thermostat setting and operating mode. Consistent sensor placement matters more than collecting dozens of uncalibrated numbers.

## Build a timeline of competing explanations

Suppose the room heats sharply on clear afternoons and remains closer to the rest of the house on overcast days with similar outdoor temperatures. That favors solar gain. If it becomes hot in late afternoon even on cloudy days, attic heat flow or an undersupplied room becomes more plausible. If it warms abruptly whenever the outdoor air handler turns off, controls and delivery may be involved. If it never recovers overnight, investigate stored heat, inadequate night cooling, or insufficient cooling capacity. None of those patterns proves the cause; they guide the next test.

Record time, room temperature, a nearby comparison room, outdoor shade temperature, sun or cloud conditions, window-covering position, and whether cooling is running. A ten- or fifteen-minute interval is often enough to show residential trends without creating a mountain of data. Note door positions and unusual internal loads. A family gathering, active oven, gaming computer, or closed return-air path can contaminate a comparison more than another decimal place of thermometer precision could help.

The comparison-room measurement is especially valuable. If both rooms rise together, a whole-house condition is likely. If only the west room climbs as the sun reaches it, its orientation deserves attention. A useful plot shows both temperatures on the same axes, with the periods of solar exposure and cooling operation marked. Look at the *difference* between the rooms. It can remove some common influence from outdoor weather, although it cannot eliminate all differences in ventilation, thermal mass, and internal use.

## Use controlled changes instead of guessing

Try one reversible change and keep the others as stable as practical. On a sunny day, deploy an exterior shade before the sun strikes the window. On another comparable day, do not. Compare the room-to-room temperature difference, not merely the daily maximum. If weather differs, say so; this is an observation, not a laboratory randomized trial. Interior blinds are useful to test too, but their optical and thermal behavior differs from exterior shade. A window film may have tradeoffs in winter solar gain and glazing compatibility that must be assessed separately.

An inexpensive surface-temperature measurement can be illuminating. If the sunlit floor gets markedly warmer than the room air, it is storing and reradiating heat. Infrared devices report surface radiance and depend on emissivity, reflection, and measurement geometry. A bright reflective surface can trick a thermal imager. Its apparent temperature is not automatically the surface's true temperature. Contact measurements, repeatable geometry, and cautious interpretation reduce that problem.

We can also test the air-distribution hypothesis. Record supply and return temperatures while the equipment runs steadily, register airflow observations, door status, and whether other rooms respond at the same time. A cold supply vent alone does not prove sufficient airflow. Closing registers in other rooms is not a reliable diagnostic shortcut: it changes system pressure and may create new delivery problems. The right comparison is the air temperature and flow delivered under ordinary operation, interpreted in the context of the room's heat load.

## Distinguish temperature from comfort

Two rooms at the same air temperature may not feel the same. A person facing a sun-warmed window or ceiling experiences additional radiant heat. Air movement, humidity, clothing, and activity also affect comfort. A simple room log might miss discomfort caused by a hot surface even when the thermostat reads normally. Ask occupants where they sit, when they feel hot, and whether moving away from the window changes the sensation. Their observations are evidence about operative conditions, not noise to ignore.

At the end of the investigation we should be able to write a concise hypothesis: on clear west-sun afternoons this room diverges from a shaded control room after solar exposure begins; shading reduces that divergence while cooling settings stay the same. Or perhaps: the divergence occurs regardless of clouds and tracks air-handler operation. Only then should we choose between shading, air sealing, attic improvement, duct balancing, or equipment work. We have converted a complaint into a testable physical story.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

**Illustrative instantaneous solar gain:** `Qdot_solar ≈ A_glass × irradiance × SHGC`. For 3 m² at 600 W/m² and SHGC 0.5, `Qdot ≈ 900 W`; actual incident angle, glazing optics, shade, and duration vary. **Conductive gain:** `Qdot_cond ≈ U × A × ΔT`, evaluated separately. Stored energy delays indoor air response.

**Measurement plan:** Log room A, room B, outdoor shaded air temperature, humidity, setpoint/mode, equipment runtime, occupied periods, blinds/shade, door position, and sky condition every 10–15 minutes over several representative days. Plot `T_A − T_B` and annotate sun exposure. Never place an air sensor in direct sun. A before/after shading comparison is suggestive but not controlled for changing weather.

**Interpretation boundaries:** Thermal imaging requires emissivity/reflection awareness; logger accuracy and placement may dominate small differences. Thermal comfort includes mean radiant temperature and airflow. HVAC performance diagnosis and glazing upgrades require equipment/window specifications and local climate context.

## Selected reading and source locators (non-spoken)

- `doe-energy-star-window-basics` — [US Department of Energy, Building Science Education: ENERGY STAR for Windows](https://bsesc.energy.gov/energy-basics/energy-star-windows). Whole-window U-factor and SHGC and their separate heat-flow functions.
- `doe-passive-solar-guide` — [U.S. Department of Energy, Consumer Guide to Passive Solar Home Design (2021)](https://www.energy.gov/sites/default/files/2021-08/ES-Passive%20Solar%20design_081321.pdf). Solar absorber, exposed thermal mass, heat distribution, and summer shading control.
- `ashrae-2025-energy-estimating` — [ASHRAE Handbook 2025 Fundamentals, Chapter 19: Energy Estimating and Modeling Methods](https://handbook.ashrae.org/Handbooks/F25/IP/F25_Ch19/F25_Ch19_ip.aspx). Degree-day and change-point regression models, base use and weather-dependent slope.
- `doe-airsealing-audit-2010` — [U.S. Department of Energy, Building America Best Practices Series: Retrofit Techniques and Technologies—Air Sealing, A Guide for Contractors to Share with Homeowners (2010)](https://www.energy.gov/sites/prod/files/2013/11/f5/ba_airsealing_report.pdf). Blower-door reference pressure and calibrated airflow; infrared thermography under controlled conditions.
