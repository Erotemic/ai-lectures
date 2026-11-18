# A Planet in Finite Boxes: The Laws Behind an Earth System Model

<!-- BEGIN SPOKEN LECTURE -->

Stand in a room, close the door, and ask a simple question: how much warmer will this room be in an hour? You might know the heater's power and the temperature outside. You might know the thickness of the walls. But if you calculate only how much heat the heater makes, you will not know the temperature. Energy can escape through the windows and walls; air can enter under the door; sunlight can fall on the floor; a radiator can heat one corner before the others. To predict the room you need an accounting system for what crosses its boundaries and what accumulates inside.

A climate model is, in part, an extraordinarily elaborate version of that accounting system. Its subject is not a room but a planet. The walls are artificial: boundaries between neighboring pieces of atmosphere, ocean, soil, snow, and ice. Energy, water, gases, and momentum pass across them. A computer calculates what changes in each piece and passes the result to the next moment. The challenge is that the Earth has no convenient boxes. Scientists must invent them without inventing a way for matter or energy to vanish.

Begin with a single column of air above one square meter of ground. Imagine measuring the sunlight that enters at the top of the atmosphere, the fraction reflected back into space, and the thermal radiation that escapes. If the absorbed sunlight exceeds the escaping radiation, energy accumulates in the Earth system. If more energy leaves than enters, the system loses energy. The net flux is a rate, in watts per square meter, not a temperature. To get a temperature response you must also know where the energy goes and how much energy is needed to warm the materials receiving it.

For an intentionally simplified illustration, suppose the planet absorbs two hundred and forty watts per square meter and emits two hundred and thirty-nine. The difference is one watt per square meter entering storage. Over a day, that is one joule per second per square meter, multiplied by eighty-six thousand four hundred seconds. Most of the real Earth's long-term excess energy goes into the ocean, whose large heat capacity makes a given heat input produce a smaller immediate temperature change than it would in a thin layer of air. This calculation does not predict an actual warming rate; it checks the units and the direction of a budget. It is the first habit of Earth-system modeling: know what quantity you are moving, and what conserves it.

Now imagine a broad grid drawn over the planet. Each horizontal cell contains several layers, perhaps many layers, representing the vertical structure of atmosphere or ocean. In each cell the model stores a set of changing quantities. For air these include mass, pressure, temperature, humidity, and winds. For the ocean they include currents, temperature, and salinity. The model cannot know the detailed wind or temperature at every point within a cell. Its variables represent numerical approximations to what happens over a finite region, and the exact interpretation depends on the model's equations and discretization.

A useful first example is water vapor. Suppose the atmosphere over a valley contains a certain amount of water, measured as mass per unit ground area. Moist air flows in through one side, dry air exits through the other, evaporation adds water from the surface, and precipitation removes it. If more vapor enters and evaporates than leaves and rains out, the stored water must increase. In a finite-volume method, the computer sums the flux through the boundary faces and the gains and losses within the cell. Neighboring cells share a boundary. Water that leaves one through that boundary should enter its neighbor, not be counted twice and not disappear between them.

That shared-boundary idea is powerful. It turns a differential conservation law, which describes a continuously varying world, into a numerical balance among a finite number of pieces. A calculation can obey its budget while still putting a rainstorm in the wrong place. Conservation is necessary, not sufficient, for a good physical model. The model also needs accurate forces, transformations among water phases, radiative transfer, and a representation of processes smaller than its boxes. But without consistent accounting, errors can accumulate until the computer's planet warms, dries, or accelerates for no physical reason.

Air moves because forces act. Horizontal differences in pressure accelerate it, Earth's rotation alters the direction of large-scale motion in a rotating reference frame, and gravity governs the vertical balance. Temperature and moisture affect density, which affects pressure and buoyancy. Radiation heats and cools the air. Condensation releases latent heat, and turbulent motions move energy and momentum. These relationships are not a set of arrows in a diagram. They are equations which give rates of change. A model's dynamical core advances the represented winds, masses, and thermodynamic variables in time using numerical approximations to the equations of fluid motion.

Consider a pressure pattern across two neighboring cells. The pressure difference produces an acceleration. As the flow changes, it redistributes mass. That redistribution changes pressure, which changes the acceleration on the next step. The model is not instructed to generate a cyclone at a designated location. Organized weather can emerge from repeated application of the rules to evolving conditions, though its quality depends strongly on grid spacing, physical parameterizations, and initial states. This is why the model is more than a map painted with climate statistics. It has dynamics: the state changes because the laws relate today's state to tomorrow's.

Even a perfectly derived continuous equation does not tell a computer how to take a step. Imagine tracking a parcel of air moving at twenty meters per second across a cell twenty kilometers wide. In a thousand seconds, it travels twenty kilometers, roughly the width of that cell. If a numerical scheme takes an excessively long step, it may skip over information needed to maintain a stable and accurate solution. For many explicit schemes, the allowed time step is constrained by the ratio between grid spacing and the speeds at which relevant disturbances or material travel. This is the Courant-Friedrichs-Lewy idea. Its exact form depends on the scheme, and not every weather model has the same restriction; semi-implicit and semi-Lagrangian schemes make different tradeoffs.

The distinction matters when people say a more detailed model is automatically better. Halve the horizontal grid spacing and the number of horizontal cells grows by about four on the same domain. If time steps must also shrink, a comparable simulation may cost substantially more than four times as much, even before increasing vertical resolution, complexity, or data movement. Computing resources therefore force a decision about which spatial and temporal variations will be represented directly and which will be approximated. The grid is a scientific choice as well as a hardware constraint.

There is no single universal map of the computational Earth. Some atmospheric models use latitude-longitude-like grids. Others use a cubed sphere, an icosahedral mesh, or spectral representations of large-scale fields. Ocean grids can bend or vary their resolution to handle coastlines, currents, and polar regions. A finite-volume cell is a helpful conceptual tool, but a real model may use spectral transforms or other numerical methods to calculate its evolution. The common principle is to represent continuous physical processes with a finite collection of numbers, preserve the essential budgets as well as possible, and quantify the errors introduced by that translation.

Grid resolution also is not the size of the smallest physical feature a model can portray faithfully. If a front or wave occupies a single grid cell, the numerical representation has too few points to resolve its structure reliably. It often takes several cells across a feature before a model can handle its shape and evolution. A grid labeled ten kilometers cannot therefore promise an accurate five-kilometer thunderstorm. The ECMWF explanation of atmospheric dynamics makes this point directly: nominal grid spacing and effective resolved scale are not identical. Unresolved effects require separate descriptions.

The vertical is another source of approximation. Near the ground, temperatures and winds can change quickly with height. A layer tens or hundreds of meters deep might contain a stable temperature inversion or vigorous daytime turbulence. Ocean temperature can change sharply across a thin thermocline. More vertical layers can help resolve these structures, but every added layer creates additional variables and numerical couplings. Models choose different coordinate systems and vertical distributions because atmospheric flow, deep-ocean circulation, and surface exchanges each pose different problems.

Now suppose we have a technically functioning global model. What should it conserve? Mass matters. Water matters across vapor, liquid, and ice. Energy matters across radiation, sensible heating, latent heating, work, and storage. Momentum matters, though the rotating Earth and surface friction complicate a simple bookkeeper's view. Carbon and other tracers matter in Earth-system versions. Some fluxes cross from one component to another; some are transformed among chemical or physical forms. An audit should ask not merely whether one field looks plausible but whether the sum of changes in stores agrees with the sum of the boundary flows and known sources and sinks.

A subtlety is that a physically conserved total can be difficult to maintain exactly with numerical approximations and separate software components. A discretization may slightly dissipate kinetic energy; a parameterization may convert it to heat in an approximate way; a remapping between grids may alter a tracer unless it is conservative. Numerical model developers monitor and improve these choices. Conservation is a target with precise mathematical tests, not a guarantee bestowed by the word 'physics'.

There is another kind of check: resolution sensitivity. Run the same model with finer cells and shorter steps, and see whether a chosen quantity approaches a stable answer. In numerical analysis this is related to convergence. For a simplified equation with a known analytic solution, one can test convergence directly. For the real climate, the atmosphere and ocean are chaotic, clouds are approximated, and changing resolution can change the unresolved-physics regime. Two runs may not follow the same weather trajectory even if both are well implemented. Researchers therefore compare budgets, process statistics, and climate distributions as well as individual trajectories. A finer grid that changes the answer is an invitation to diagnose why, not automatically proof that the finer answer is correct.

A little model can be more revealing than a giant one if the question is narrow. An energy-balance model with one global temperature can show how incoming energy, outgoing radiation, heat capacity, and feedback interact. A model with latitude bands can explain why heat must be transported from warm regions toward colder ones. A fluid-dynamics model can investigate waves and jets. A fully coupled Earth-system model can examine how changes propagate through ocean, land, ice, and living systems. They are not ranked by complexity alone. We choose a model whose assumptions match the question.

That is the conceptual foundation. The computer cannot reproduce every molecule of the atmosphere, nor does it need to. It must keep a faithful enough account of the things that cross its invented boundaries, calculate the changes that follow from the laws of motion and thermodynamics, and expose where approximations enter. On that foundation, the model can do something that a static weather map cannot: it can conduct a controlled, internally consistent experiment about the physical consequences of changing the planet's conditions. But the moment we draw boxes, we leave some of the weather inside them unresolved. That is the next major modeling problem, and one of the most scientifically consequential.

<!-- END SPOKEN LECTURE -->

## Scientific companion: budgets, grids, and time integration

### A conservative control-volume statement

For a conserved density $q$ and flux vector $\mathbf F$, a simplified budget is

$$\frac{\mathrm d}{\mathrm dt}\int_V q\,\mathrm dV = -\oint_{\partial V}\mathbf F\cdot\mathbf n\,\mathrm dA + \int_V S\,\mathrm dV.$$

The numerical scheme approximates face fluxes so that adjacent control volumes exchange equal and opposite amounts. The source term $S$ must be physically interpreted; phase changes can transfer water among reservoirs without creating total water. Global mass, water, and total-energy checks are more demanding than inspecting an isolated prognostic field.

### Worked energy-budget check

A hypothetical planet absorbs 240 W m⁻² and emits 239 W m⁻². Its net radiative gain is 1 W m⁻² = 86,400 J m⁻² per day. This is an **illustrative imposed budget**, not an estimate of present-day Earth imbalance. A temperature tendency requires a heat capacity and the destination of stored energy; a one-box model with effective heat capacity $C$ writes $C\,\mathrm dT/\mathrm dt=F-\lambda T$ near a reference state.

### Practical numerical distinctions

| Question | What to inspect |
| --- | --- |
| Does the scheme conserve water? | Global and component budgets; conservative remapping; diagnostic residuals |
| What does '10 km resolution' mean? | Nominal grid length versus effective resolvable scales, vertical spacing and numerical diffusion |
| Is a step stable? | CFL restrictions for the actual chosen explicit scheme; splitting and implicit solver tradeoffs |
| Is finer always more accurate? | Convergence in idealized tests, process statistics, changes in subgrid parameterizations |
| Does a successful forecast validate the climate? | Only some aspects; different time scales and metrics require different evaluation |

### Sources and further reading

- IPCC (2021), *Climate Change 2021: The Physical Science Basis*, Chapter 1, §1.5.3, climate models. https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-1/
- ECMWF, *Atmospheric dynamics* (dynamical cores, effective resolution, parameterizations). https://www.ecmwf.int/en/research/modelling-and-prediction/atmospheric-dynamics
- ECMWF, *Earth system data assimilation* (modeling and observational constraints). https://www.ecmwf.int/en/about/media-centre/focus/2025/fact-sheet-earth-system-data-assimilation

### Questions

1. Why does a globally conserved water budget not guarantee the correct location of rainfall?
2. What additional quantity is needed to turn a radiation imbalance into a temperature change?
3. Why can halving grid spacing increase computation by substantially more than a factor of four?
4. Why is comparing individual weather maps a poor test of numerical convergence for a chaotic climate simulation?
