# 002000 — Heat Flow, Thermal Bridges, and Whole-Assembly R-Values

**Track:** Building Science. **Background:** Introductory heat transfer and building enclosure concepts. **Purpose:** replace the idea of “insulation as a single number” with an assembly-level account of heat flow.

<!-- BEGIN SPOKEN LECTURE -->

# A Wall Is Not a Bag of Insulation

On a winter morning, touch the painted wall between two studs and then the wall where a wooden stud passes behind the drywall. One spot may be cooler. The difference is small enough that your hand may not notice it, but a thermal camera sometimes will. What you are observing is not a hole. It is a path: two different materials connecting the same warm room to the same cold outdoors.

People ask, “How much insulation is in the wall?” A better question is, “How much heat passes through the complete wall, including its interruptions?” Today we will construct that answer. We do not need an elaborate simulation to see the central problem, only a few ideas from thermal circuits.

## The resistance of a path

Heat flows from higher temperature to lower temperature. In a steady approximation, the rate of heat flow through a layer grows with the temperature difference and shrinks as thermal resistance grows. An insulating layer has a high thermal resistance; a good conductor has a low one. The thermal resistance of a homogeneous slab increases with its thickness and decreases with the material's thermal conductivity.

In North American building practice we often quote R-value. Do not mix unit systems. An R-value stated in square-foot degrees Fahrenheit hours per British thermal unit is not numerically the same as a resistance stated in square-meter kelvins per watt. The corresponding U-factor is the reciprocal of assembly resistance in the appropriate units. Higher R means less heat transfer under comparable conditions; higher U means more.

Layers in sequence act approximately like resistances in series. A wall might contain interior surface resistance, drywall, a cavity layer, sheathing, continuous exterior insulation, siding, and an exterior surface resistance. For a one-dimensional steady calculation, we add the layer resistances to get the resistance of that path. Neither insulation labels nor a material's R-value by itself accounts for gaps, metal fasteners, or air moving through the assembly.

## Two paths through the same wall

Imagine that most of a framed wall is insulated cavity, while the rest is wood framing. Suppose, for a deliberately simplified example, that the cavity path has an effective resistance of twenty in consistent R-units, and the framing path has a resistance of six. Suppose the framing occupies twenty-five percent of the wall's projected area. What is the combined resistance?

It would be wrong to average the R-values arithmetically and say sixteen and a half. Heat does not take a democratic vote among materials. The two paths experience approximately the same indoor-to-outdoor temperature difference, and their heat flows add. We must average their conductances, the reciprocals of resistance. Seventy-five percent divided by twenty, plus twenty-five percent divided by six, gives about zero point zero seven nine units of conductance. The reciprocal is approximately twelve point six. Our whole-wall resistance is much closer to twelve point six than to twenty.

This arithmetic reveals why the cavity insulation rating is not the wall rating. It also reveals why framing fraction matters. Plates, headers, studs, corners, window surrounds, and blocking all provide heat paths. Thermal bridges do not have to be wood: steel studs, metal shelf angles, fasteners, concrete balconies, and lintels can produce larger local effects.

## Continuous insulation changes the topology

Now add an uninterrupted insulating layer outside the framing and the cavities. If it adds an R-value of five to both paths, the cavity path rises from twenty to twenty-five and the framing path rises from six to eleven. The combined result is approximately nineteen, using the same area fractions. That is a larger improvement than simply adding five to the weakest part or judging by the cavity rating alone.

Why does this work? Continuous insulation forces both parallel paths to pass through another resistance in series. The framing still matters, but its bypass advantage is reduced. This is an important architectural idea: sometimes it is better to change the network of paths than to improve the best path in the network.

Real details complicate the model. Exterior insulation may be interrupted at window openings or attachments. Studs conduct heat in two and three dimensions, not only across a neat slice of wall. Surface temperatures, wind, moisture, fastener geometry, and installation quality change performance. The simple parallel-path model is for reasoning, not a claim that we have calculated the rating of a particular wall.

## Insulation quality is not the same as air sealing

A section of fluffy insulation installed with a gap around an outlet can perform worse than the nominal material rating suggests. Compression can change its effective thickness and structure. Incomplete coverage can create low-resistance routes. Moving air can carry heat through leaks without following the conduction-only paths in our calculation. For these reasons, adding up printed R-values is necessary for some questions and insufficient for others.

Consider the ceiling of a house. Heat can conduct through insulation and framing. It can also leave with indoor air escaping through an attic hatch or plumbing penetration. More insulation may reduce the first flow while doing little to the second. Air sealing and thermal insulation are complementary controls, not synonyms.

## Why comfort and condensation enter the picture

Heat transfer is not only about a fuel bill. A thermal bridge can lower a room-facing surface temperature, changing radiant comfort and local condensation risk. If indoor air has a dew point above a cold spot's surface temperature, water can accumulate there. A corner that stays cold and wet may develop mold even when the surrounding wall appears dry. Indoor humidity, airflow, surface finish, and time also matter; a visible dark patch is not proof that a thermal bridge alone caused it.

Adding exterior insulation may warm structural sheathing during a cold season, but changing an assembly also changes its potential to dry. A wall that performs thermally could still fail in moisture control if water is trapped by incompatible layers. We must always ask about both thermal performance and moisture management. These are coupled systems, not interchangeable ones.

## Reading an insulation proposal

Suppose a contractor offers two upgrades. The first adds insulation in already-filled cavities. The second adds continuous insulation and details the window, door, foundation, and roof transitions. Before comparing prices, identify the existing assembly and ask how each option treats framing bridges, air leaks, moisture paths, and continuity at edges. Ask what numerical claim describes the insulation product and what claim describes the *assembly*. Ask what assumptions underlie a quoted savings estimate: climate, conditioned area, existing leakage, heating equipment, occupancy, and installation.

There is a final useful distinction. A highly insulated wall may occupy only a modest fraction of a home's thermal losses. Windows, roof, floor, foundation, air leakage, and mechanical ventilation contribute too. A whole-wall R-value is not a whole-house energy model. Our reasoning improves when we choose the system boundary explicitly.

When you inspect a wall, picture a network: layers in series and bridges in parallel. The most revealing question is not, “Is this material good insulation?” It is, “Where does heat have a connected low-resistance route, and what modification changes that route?” That is the beginning of credible building-envelope design.

<!-- END SPOKEN LECTURE -->

## Technical companion: assembly calculations and boundaries

For an ideal flat layer, `R = L/k` in SI thermal-resistance-per-area units, with `L` thickness and `k` conductivity. A steady approximation is `q'' = (T_in - T_out)/R_total`. For parallel area fractions `f_i` with paths `R_i`, `U_effective = sum(f_i / R_i)` and `R_effective = 1/U_effective`. Our illustrative example: `0.75/20 + 0.25/6 = 0.079166...`, so `R_eff ≈ 12.63`; with R-5 shared continuous insulation: `0.75/25 + 0.25/11 ≈ 0.05273`, so `R_eff ≈ 18.97`. The series/parallel approximation excludes junction losses, thermal storage and infiltration.

**Evidence and application boundaries:** Consult DOE building-envelope guidance and recognized assembly calculation methods before making quantitative performance claims. Surface temperatures and condensation require humidity, thermal-bridge geometry and boundary conditions. Adopted energy codes, climate zone, vapor-management strategy, and manufacturer assemblies can alter appropriate detailing.

**Exercise:** Draw the cavity, framing and window-header routes through an exterior wall. Mark which layers are continuous across every path. Explain why adding cavity insulation alone does not eliminate framing conduction.

**Claim map:** Parallel-path and reciprocal-U calculations: thermal conduction principles; building framing and material references in `metadata/sources.json`. Enclosure details: DOE and USDA reference records. The worked numerical model is original and illustrative.

## Selected reading and evidence (non-spoken)

- `doe-ci` — [DOE Building Science Education, Continuous Rigid Insulation on Exterior Walls](https://bsesc.energy.gov/energy-basics/continuous-rigid-insulation-exterior-walls). Framing thermal bridges and continuous insulation.
- `pnnl-ci` — [PNNL Building America Solution Center, Continuous Rigid Insulation Sheathing](https://basc.pnnl.gov/resource-guides/continuous-rigid-insulation-sheathing). Assembly details, moisture/climate and thermal bridging.
- `doe-air-vapor` — [DOE Building Science Education, Air Barriers vs Vapor Barriers](https://bsesc.energy.gov/energy-basics/building-enclosure-air-barriers-vs-vapor-barriers-continuous-sealed-wrb-walls). Separate air leakage, vapor diffusion and water-management functions.
