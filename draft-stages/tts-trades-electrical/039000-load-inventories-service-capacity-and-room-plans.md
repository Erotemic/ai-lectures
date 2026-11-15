# 039000 - From an Appliance List to a Load Hypothesis

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** source and load inventories, annotated one-line drawings, room plans, hypothetical demand profiles, and uncertainty ledgers.

<!-- BEGIN SPOKEN LECTURE -->

# From an Appliance List to a Load Hypothesis

There is a deceptively simple question behind almost every electrical renovation: can the existing system support what we intend to connect? It sounds like a question about one number on a breaker handle. In reality it is a question about topology, equipment ratings, timing, protective constraints, future changes and the quality of the information available.

Suppose someone is planning to replace an old water heater, install a heat pump and make room for electric-vehicle charging. They can name the appliances. Perhaps they can find the electric bill. But neither of those is a service-load study. The bill sums energy over time. A list of appliances does not show which loads coexist. The rating on a service disconnect gives part of a supply and protection description, not a promise that any combination of loads is acceptable.

The right first product is an *inventory with evidence and uncertainty*. We are not trying to guess the breaker size from a shopping list. We are making a traceable model of what the building contains, how it is connected and what still needs to be established.

## Begin with the electrical boundary

A building may receive power through a utility service, a site transformer, a distribution board, or a more complex arrangement that includes solar generation, battery storage, a generator or transfer equipment. Start the inventory by drawing the boundary of the system under study. What is the nominal supply voltage? How many phases or line conductors are present? Where does the service or supply boundary lie? What main disconnect, distribution equipment and feeders are visible in reliable documentation?

For a common North American residential split-phase service, the two line conductors are nominally 240 volts apart, and each is nominally 120 volts from neutral. Many general-use loads use one line and neutral; larger appliances often use both lines. In a three-phase 400/230-volt system, line-to-line and line-to-neutral relationships differ, and a balanced load has a different current formula. An inventory that simply labels every device '240' or every load 'single phase' will lose information the design later needs.

The service equipment rating also does not tell the whole story. Upstream transformer capacity, utility rules, fault-current characteristics, feeder limits, equipment condition and local installation rules can matter. An apparently spacious panel does not prove that the supply has enough capacity for new loads. Empty breaker spaces describe physical real estate. They do not themselves represent unused electrical demand capacity.

At this stage, an annotated one-line diagram is more helpful than a photograph album without labels. A one-line gives us source, service equipment, feeders, major panels, disconnects and identified large loads. It does not need to draw every receptacle yet. Its job is to establish the hierarchy into which the finer room plan will fit.

## Inventory connected equipment, not guessed lifestyles

Walk through an imagined house room by room, using existing plans, accessible nameplates and product literature as sources. The kitchen has a range, perhaps induction, a dishwasher, refrigerator, ventilation and general-purpose outlets. The laundry area has a dryer and washer. Mechanical space contains the air handler, compressor supply, water heater, pumps and perhaps controls. Outside are receptacles, a possible EVSE, well equipment or a workshop outbuilding.

Create a row for each load with an identifying tag, location, supply voltage, phase or line allocation, published electrical ratings, current protective device, known feeder or branch circuit, duty pattern and source of evidence. Some products state watts. Others state input current, full-load amperes, minimum circuit ampacity, or maximum overcurrent protection. Those labels serve different purposes. The presence of a manufacturer-provided minimum circuit ampacity should not tempt us to treat it as the device's measured running draw. Likewise, a motor's mechanical horsepower is not its electrical input in watts.

A helpful inventory keeps an explicit 'unknown' cell. If the air handler's supplemental heater configuration has not been established, record that. If a feeder has no dependable circuit identification, do not infer it from a label that was written decades ago. If two pieces of equipment share a circuit according to an old drawing but the site has been remodeled, record that the drawing is unverified. Unknown is a valid and often valuable engineering conclusion.

There is a second inventory for *proposed* loads. Do not silently combine planned equipment with what is already installed. A tentative EVSE might be described as twenty-four, thirty-two or forty amperes depending on operating needs and available capacity. These are planning scenarios, not interchangeable electrical installations. Keeping a proposed-options column allows capacity planning to explore alternatives before equipment is selected.

## Connected load, diversified load and measured demand

Three concepts tend to get collapsed into one.

*Connected load* is a sum or inventory of ratings associated with equipment. It may be deliberately conservative, and a code's calculation often assigns specific values rather than using ordinary operating draw. *Diversified demand* recognizes that different loads do not necessarily operate at their maxima at the same time, with factors and procedures defined for a particular calculation purpose. *Measured demand* is an observation over a stated interval with a specified meter and method.

A measured fifteen-minute peak does not capture the highest current in a motor's first fraction of a second. An average annual energy figure cannot reconstruct the worst winter morning. And last year's observation cannot prove what next year's building will draw after an equipment change. Each quantity is evidence for a different question.

Consider a hypothetical home with a three-kilowatt electric water-heating load, a four-kilowatt cooking load, a five-kilowatt heating-related load in one operating mode and a roughly six-kilowatt EV charging input. The arithmetic sum is eighteen kilowatts. That number could be much higher than typical overnight demand if cooking and hot-water recovery rarely overlap EV charging. But in an intentionally constructed worst-case time window, all could overlap. We cannot simply pronounce either eighteen kilowatts or six kilowatts the 'right' service load. The code calculation method, real operating configuration and any approved load management determine what conclusion is supported.

Regional context is useful for anticipating scenarios, but not for substituting national averages for a particular house. The U.S. Energy Information Administration's Residential Energy Consumption Survey documents major end uses and geographic variation. It shows why heating and cooling can dominate annual energy. It does not tell us the service's peak line current on a specific January morning. The local climate, envelope, installed fuel mix and occupants' actual equipment govern that question.

## Turn the inventory into a small time model

A time-based sketch is an excellent design aid. Give each load a row and put time of day along the horizontal axis. Represent the refrigerator and electronics as a relatively small, variable background. Add a morning water-heating recovery, a possible high heating stage during a cold spell, a brief well-pump cycle, cooking in the evening and vehicle charging overnight.

Now ask what produces a high continuous interval. Ask what creates a short startup disturbance. Ask which loads operate by design in mutually exclusive modes. A heat-pump water heater can have hybrid and resistance-only modes; a control schedule may reduce EV power when other loads are elevated. Do not assume control exclusivity unless the product's actual configuration and failure behavior establish it.

A rough calculation can uncover where the unknowns matter. Suppose the nominal service is a hypothetical 120/240-volt split-phase supply with a two-hundred-ampere service rating. Multiplying 240 volts by 200 amperes gives forty-eight kilovolt-amperes, an *illustrative nominal upper apparent-power figure for a balanced 240-volt load at the equipment rating*. It is not an authorized design load or a code-approved capacity claim. The two line currents, the size of any neutral current, continuous-load rules, conductor and breaker ratings and the adopted service-load calculation all need separate consideration. A five-kilowatt 120-volt load on only one leg is not balanced simply because the main service is described as 240 volts.

The simple multiplication still serves a purpose: it teaches what the nameplate number means dimensionally, and why the correct analysis needs more than that multiplication.

## The room plan connects electrical behavior to people and architecture

Now change scale from the one-line to a room plan. The circuit drawing describes electrical connectivity. The room plan describes equipment location, routes, spaces and likely use. Mark large fixed appliances, control locations, lighting zones, switches, outlets, service access and possible future equipment.

Layout decisions can reveal electrical choices. A kitchen has clustered high-power appliances, general-use receptacles, moisture exposure and dedicated equipment needs. A mechanical room combines motors, controls, temperature and plumbing. A garage may have a high-duration charging load and outdoor-rated or damp-location details. A long run to an outbuilding introduces voltage drop, protective-conductor considerations and possible supply architecture choices. None of these can be answered by placing an icon in a room alone, but the room plan makes their relationships visible.

This is also where a design becomes maintainable. Label a planned circuit by meaningful function, not only by where the first outlet happens to be. Distinguish equipment that should remain powered from equipment that could be shed by an energy-management system. Note which devices require specific isolation, access or control arrangements. Show expected future modifications without treating every imagined future appliance as already installed.

## Build a capacity *hypothesis*, not a premature verdict

At the end of the first pass, write a short statement: based on the available inventory, we think the proposed equipment may fit under one or more demand-management options; or we suspect a service or feeder change might be needed. Then list the evidence that could change that conclusion.

For example: the proposed EV load can be scheduled and perhaps controlled; the space-heating system may have an auxiliary electric stage of unknown capacity; the water heater's resistance backup needs verification; the existing service load requires calculation under the adopted rules; and the supply company's requirements must be checked. A good hypothesis is specific enough to be tested. 'The house has 200 amps, so it must be fine' cannot be tested because it never states which loads, which assumptions or which limits were considered.

The inventory becomes more reliable each time an unknown is resolved. An actual manufacturer document can replace a guess. An updated one-line can replace an obsolete panel label. A documented demand history can inform an engineering estimate, while still preserving the distinction from the normative load method. The point is not to collect paper for its own sake. It is to make every consequential decision traceable to a fact, an assumption, or a clearly identified governing requirement.

A sound electrical plan begins before a cable is chosen or a breaker is selected. It begins when the building is represented accurately enough that its electrical requirements can be reasoned about, and its remaining uncertainties can be named.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Example inventory schema

| Field | Meaning | Evidence hierarchy |
|---|---|---|
| Tag / location | Identifies the load on plans and in schedule | As-built documentation, observed label, proposed equipment record |
| Supply / phase / line | Voltage and conductor arrangement | Utility/service specification and equipment data |
| Input / MCA / MOCP | Different published electrical quantities, where supplied | Model-specific nameplate/manual, not guesses from generic appliance type |
| Operating modes | What can run together, what is controlled | Product wiring/control documentation and witnessed history |
| Duration / transient | Sustained current and starts | Model data and appropriately obtained measurements |
| Source / confidence | What establishes the row | Exact dated evidence, status and unresolved discrepancies |
| Proposed changes | New loads separate from installed loads | Design alternatives and decisions still pending |

MCA means *minimum circuit ampacity*; MOCP denotes *maximum overcurrent protection* as labeled on some equipment. Neither is automatically equivalent to actual running current. Exact terms and calculations vary by product and national standard.

### Hypothetical capacity exercise

For a nominal balanced single-phase `240 V x 200 A = 48 kVA` at the stated current rating. **Do not** treat this as a permitted service design load, an allowance for continuous loads or a finding of spare capacity. An unbalanced split-phase system requires considering each line and neutral where relevant. Actual equipment and jurisdictional criteria govern sizing.

Hypothetical time-slice A: `P_water=3 kW`, `P_heat=5 kW`, `P_EV=0 kW`, `P_cook=0 kW`, total `8 kW` before unrelated loads. Slice B: `P_water=0`, `P_heat=3 kW`, `P_EV=5.7 kW`, `P_cook=4 kW`, total `12.7 kW`. These are scenario inputs, **not** an NEC or IEC load calculation. The real power sum assumes known contemporaneous real power; phase currents still require voltage, power factor and circuit allocation.

### Exercises

1. Draw a room plan with fictional equipment labels and a matching one-line. Connect every named circuit to its source, identifying ambiguities instead of inventing routes.
2. Build separate current-condition and proposed-condition inventories; mark which rows came from a nameplate, a plan or a hypothesis.
3. Make three time slices: cold-morning heating, summer cooling plus cooking, overnight EV charging. State which mode-coincidence claims are confirmed versus guessed.
4. Write a capacity hypothesis and the minimum additional documents or measurements needed to assess it under a chosen edition and jurisdiction.

### Distinctions to retain

- Annual kilowatt-hours do not define the maximum supply current.
- Panel space, main-breaker label, feeder ampacity and permissible calculated load are distinct.
- A nameplate's electrical minimum circuit ampacity can exceed normal draw by design; do not substitute it for measured demand.
- A historic meter trace does not prove future equipment behavior.
- U.S. load calculations moved in the 2026 NEC edition; a prior-edition article number is not a timeless citation.

## Claim-level source map

| Claim ID | Consequential statement | Source and location | Boundaries |
|---|---|---|---|
| E039000-01 | Annual end-use energy and momentary electrical demand serve different analytical purposes | [electrical-eia-home-electricity](https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php) (end-use annual electricity); [electrical-openstax-acpower](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (AC power/energy relationships) | National averages do not produce a particular home's demand maximum |
| E039000-02 | The RECS program describes household end-use and geographic variation | [electrical-eia-recs](https://www.eia.gov/consumption/residential/) (survey scope, state and end-use data) | Survey results are not site measurements or adopted load factors |
| E039000-03 | Electrical equipment labels and specific use conditions matter to installation design | [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (§1910.303(b),(e),(f), U.S. workplace); [electrical-osha-approval-interpretation](https://www.osha.gov/laws-regs/standardinterpretations/2003-05-27-0) (listing and instructions interpretation) | Workplace scope; not direct proof of private residential rules or product suitability |
| E039000-04 | Load-calculation requirements are edition-structured and may apply differently to branch, feeder and service design | [electrical-nfpa-2026-loads](https://www.nfpa.org/news-blogs-and-articles/nfpa-journal/2025/04/29/2026-nec-changes) (2026 Article 120 restructuring); [electrical-iec60364](https://webstore.iec.ch/en/publication/63699) (installation scope and general characteristics) | Publisher scope only for IEC, not full normative clauses; adoption and edition control |
| E039000-05 | EVSE power and proposed charging rate depend on configured equipment and vehicle | [electrical-afdc-home](https://afdc.energy.gov/fuels/electricity-charging-home) (home charging choice); [electrical-afdc-charging](https://afdc.energy.gov/fuels/electricity-stations) (AC Level 1/2 supply and charging limits) | Equipment-specific current and circuit design are not established |
| E039000-06 | Space-conditioning and water-heating loads depend strongly on climate, mode and equipment | [electrical-eia-recs](https://www.eia.gov/consumption/residential/) (monthly/end-use variation); [electrical-doe-hpwh-femp](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-residential-water-heaters) (water-heater modes) | Model-specific simultaneous operation and auxiliary heat not established |
| E039000-07 | 120/240 split-phase and 400/230 three-phase require different phase/line current treatment | [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (regional network layouts and 120/240 supply); [electrical-se-voltage-ranges](https://www.electrical-installation.org/enwiki/Definition_of_voltage_ranges) (230/400 supply and line/neutral examples); [electrical-openstax-acpower](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (independent physical power relationship) | Two system-layout references are from the same publisher; utility voltage and exact connection must be verified |
| E039000-08 | A documented electrical one-line and circuit identification help connect inventory to system topology | [electrical-osha303](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.303) (§1910.303(f) identification in workplace); [electrical-nfpa70](https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70) (NEC scope) | Diagram is an engineering planning tool; sources do not prescribe one universal residential drawing format |

