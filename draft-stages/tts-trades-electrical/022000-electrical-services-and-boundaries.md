# 022000 - Electrical Services: From Distribution Network to Premises

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** public service diagrams, one-line drawings, utility service manuals, and paper calculations.

<!-- BEGIN SPOKEN LECTURE -->

# Electrical Services: From Distribution Network to Premises

A house stands at the end of a long electrical network. Electricity reaches it from a neighborhood transformer, perhaps through wires overhead, perhaps through a buried cable. Between the distribution network and the first branch circuit lie several pieces of equipment that are easy to mistake for one another: the service conductors, an electric meter, a service disconnect, and a distribution panel. Their locations may overlap. Their purposes do not.

The word **service** has a more specific meaning in electrical practice than it has in ordinary conversation. It refers to the arrangement that connects a supply system to a premises installation. In one jurisdiction, the central document may call it the consumer's installation; in another, the service entrance; in another, the supply connection. Our task is to trace the energy and the responsibilities without assuming every country draws its boundaries at the same box.

## Trace the network in both directions

Start upstream. Generation and storage resources feed transmission and distribution networks. A distribution transformer changes voltage to the level expected by the local network or individual consumers. From there, service conductors deliver power to a building's supply equipment. Downstream, feeders and branch circuits distribute that power to appliances, lighting, and other loads.

The transformer may be mounted on a pole or placed in a ground-level enclosure. In a common North American residential arrangement, an individual single-phase transformer serves one or several buildings and has a center-tapped low-voltage secondary. In many European arrangements, a larger transformer feeds a low-voltage street network from which multiple properties take a supply. Schneider Electric's Electrical Installation Guide depicts these as contrasting distribution architectures, not universal descriptions of either continent. There are many exceptions.

A one-line drawing simplifies this network to a sequence of components and connections. It deliberately suppresses much of the physical route. For example, a mark representing a transformer is not a promise that it is outside the particular house being studied. An engineer may instead find an indoor substation, multiple transformers, a private distribution system, or a building supplied by a neighboring structure.

Follow the model as a chain of questions. Where is voltage transformed? Where are conductors physically joined? Where is energy metered? Where can the supply to downstream equipment be disconnected? Which protective device can clear a fault, and which conductor is protected by it? These are separate questions, and the answer to one does not settle the others.

## Service point and property line are different ideas

In United States National Electrical Code terminology, a **service point** marks the connection between the serving utility's facilities and premises wiring. The NFPA code-making process publishes the definition and records the committees' explanations. The utility normally specifies the service point as part of its conditions of service. Importantly, this is a technical and contractual boundary; it need not coincide with the property line, the meter, or the exterior wall.

An overhead connection commonly has a **service drop**, conductors extending from an overhead supply to the connection at the premises. An underground connection commonly uses a **service lateral** or an underground service arrangement. But the allocation of responsibility for the cable, conduit, meter socket, meter itself, and related structures is determined by the utility's actual published rules and local law. It is a mistake to memorize one universal ownership diagram.

Consider two utility documents from the same region. The New York State Electric and Gas glossary defines the service point in terms of company-to-customer connection. Its electric service manual separately describes overhead, underground, service equipment, meters, and customer-owned sources. The company's filed tariff then distinguishes the utility-owned meter from some customer-provided equipment associated with it. These are not contradictions: an ownership map can assign different components on either side of the metering location to different parties.

This distinction matters during a renovation. A change to an entrance cable may require coordination with a utility even when the cable is customer-owned. A service upgrade may require an equipment review, approved location, disconnection, inspection, and reconnection. Those administrative steps protect the interface between two systems whose operators do not have full control over each other's equipment. Specific permits, inspections, design submissions, and licenses depend on the location and work.

## A meter measures energy; it is not a general-purpose switch

An electricity meter typically measures quantities used for accounting, especially energy over time. Some meters also measure or report demand, voltage, current, or disturbances. That does not make every meter a protective disconnect or make a display of zero consumption proof that conductors are de-energized.

Suppose a resistive heater takes two kilowatts for half an hour. It consumes one kilowatt-hour, assuming the rating and operating power hold over that interval. The same heater drawing two kilowatts for two hours consumes four kilowatt-hours. A meter accumulates energy; a protective device responds to particular abnormal conditions; a disconnect creates a defined interruption in an electrical path. Different devices answer different questions.

The meter socket or enclosure is also not necessarily owned by the same organization that owns the meter. That can feel like administrative trivia until a damaged enclosure delays reconnection. The vocabulary tells you which equipment a repair proposal concerns and which document is needed to establish its specifications.

## The service disconnect defines a downstream boundary

A main disconnect can separate the portion of an installation downstream of it from its incoming supply path. In ordinary speech someone might say that the main breaker turns off the house. Electrically that statement is incomplete. Supply conductors and terminals upstream of that device may remain connected to the source. Equipment may also have other sources: a generator, a battery-backed inverter, an on-site photovoltaic system, or an additional service. The actual isolation boundary depends on the topology and the equipment.

This becomes easier to reason about when we draw the disconnect as one open switch in a network. An open switch only interrupts the edges it actually opens. It does not make every upstream node disappear. If a separate source is connected on the load side, that portion of the network may remain energized. If a transformer or inverter establishes a separately derived system, its own grounding and disconnect arrangement introduces further design questions. The underlying circuit logic stays the same even though the installation requirements change.

A service panel and a meter-main assembly can combine functions in one physical enclosure. The enclosure is not the function. To understand what it does, identify the actual conductors, buses, disconnects, protective devices, and source connections shown on its accepted drawings and markings.

## What does a two-hundred-ampere service tell you?

The phrase **two-hundred-amp service** is common in the United States. It is useful, but incomplete. It might refer to the rating of a service disconnect, the service equipment, or another aspect of the installation. Equipment ratings, conductor ampacity after applicable adjustments, the design load, the utility's supply limitations, and the available fault current are different quantities.

Take an idealized North American single-phase, three-wire supply, with two hundred forty volts between the outer conductors and a two-hundred-ampere current magnitude at its stated maximum. Multiplying gives forty-eight kilovolt-amperes of apparent power for that ideal balanced or line-to-line calculation. The multiplication is not a prediction that the utility promises forty-eight kilowatts at every moment, nor an independent sizing rule for a real installation. Real and apparent power differ for non-unity power factor; conductors, terminals, protective devices, ambient conditions, continuous load requirements, and calculated demand all matter.

The rating does not describe the prospective short-circuit current either. A stiff utility supply can drive a fault current far larger than ordinary load current. Protection must be suited both to carry expected loads and to interrupt the fault energy available at its location. This is why an electrical service specification may call for a short-circuit current calculation or a minimum interrupting rating even though the customer only asked for more appliance capacity.

## The boundary is also a document set

A useful service study starts with a one-line diagram, but it rarely ends there. Compare the diagram with the utility's current service requirements, the equipment's listings and instructions, a panel schedule, the accepted design, and the jurisdiction's adopted code. A drawing can show that the service equipment is rated at a certain current. A utility document can explain who provides a socket or entrance conductor. A code can specify protective objectives and installation rules. A commissioning record can establish what was actually inspected or tested.

No one document does the others' jobs. A billing statement does not prove conductor sizing; a panel label does not reveal available fault current; a utility meter reading does not prove an isolating state. A formal approval establishes that a particular submission satisfied a particular process, not that every conceivable fault has been eliminated.

A homeowner who can use this vocabulary can ask a far better question than 'Can I upgrade my electrical?' They can describe the present supply arrangement, service equipment, desired load changes, source configurations, utility handoff, and evidence needed to accept a design. Those questions translate well across overhead and underground networks, utility companies, and different national codes.

The first essential skill in distribution work is not memorizing the location of the main panel. It is identifying the boundaries of the system, the job of each component, and the documents that define what is actually connected.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### A generic supply one-line

```text
[distribution network] -- [distribution transformer]
             |                   |
       utility network     low-voltage secondary
                                 |
                          service conductors
                                 |
                 [service point -- location varies]
                                 |
                     [metering arrangement]
                                 |
                        [service disconnect]
                                 |
                         [distribution bus]
                           /             \
                       feeder       branch circuit
                         |                 |
                    subpanel           final load
```

This is an abstraction, **not** a universal connection order. For example, meter-main assemblies, multiple sources, service disconnect placement, CT metering and utility-owned equipment vary. The service point is not necessarily between the transformer and meter at the schematic location shown.

### Classroom calculations

1. A 2.0 kW resistive load operates for 0.5 h: `E=Pt=1.0 kWh`.
2. For a nominal 240 V source and assumed 200 A magnitude: `|S|=|V_rms I_rms|=48 kVA` if the model is single-phase and the current is the appropriate line current. This is *not* a service-sizing result or a utility guarantee.
3. A 5.0 kW resistive load on an ideal 240 V circuit would draw about 20.8 A at its rated voltage. Start-up, temperature, duty cycle, equipment instructions and conductor selection are omitted by that simple equation.

### Exercises (paper only)

- Draw a tree separating service point, meter, disconnect, overcurrent protection and branch loads. Explain why a component might serve two functions without those functions becoming identical.
- Compare an overhead and an underground service document. List whose responsibilities the document actually identifies. **Answer:** do not assume a common ownership boundary; identify each separately.
- Does an open main disconnect prove a meter enclosure is de-energized? **Answer:** no; supply-side conductors may remain energized and additional sources may exist.
- Does a 200 A rating specify available fault current? **Answer:** no; source impedance and upstream network govern that distinct quantity.

### Attribution and jurisdiction

The *service point* language is attributed to NFPA's collective National Electrical Code process and utility service documents, not to a named individual. The contrasting American and European low-voltage network illustrations are Schneider Electric's engineering-guide synthesis, not an original discovery by this manuscript. NYSEG is cited only as a specific example of utility documents; its rules do not govern other utilities.

## Claim-level source map

| Claim ID | Consequential claim | Source and exact support role | Limits / review |
|---|---|---|---|
| E022000-01 | Low-voltage supply can use different transformer-to-premises architectures | [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (North and Central American versus European network discussion; primary_explanation); [electrical-nyseg-service-manual](https://www.nyseg.com/w/esm-manual) (Service connection index; regional_utility_example) | Guide gives examples, not a census of national practice. |
| E022000-02 | Service point is defined as the connection of serving utility facilities to premises wiring | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Service point definition; public_us_regulation); [electrical-nyseg-glossary](https://www.nyseg.com/w/glossary) (Electricity Service definition; independent_utility_usage); [electrical-nfpa-service-point-record](https://docinfofiles.nfpa.org/files/AboutTheCodes/70/70_A2018_NEC_P01_SD_pcsubmittals.pdf) (Article 100 Service Point definition; standards_development_history) | OSHA applies to occupational installations; NFPA record not a final locally adopted code. |
| E022000-03 | Service point may differ from property line, meter location or exterior wall | [electrical-nyseg-glossary](https://www.nyseg.com/w/glossary) (Service point and installation terms; utility_context); [electrical-nyseg-service-manual](https://www.nyseg.com/w/esm-manual) (Service Connections section index; utility_context); [electrical-nfpa-service-point-record](https://docinfofiles.nfpa.org/files/AboutTheCodes/70/70_A2018_NEC_P01_SD_pcsubmittals.pdf) (Service Point informational note; standards_development_context) | Actual utility service point must be confirmed for particular premises. |
| E022000-04 | Service drop and service lateral describe distinct supply approaches | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Service drop and service conductors definitions; public_us_regulation); [electrical-nfpa-service-point-record](https://docinfofiles.nfpa.org/files/AboutTheCodes/70/70_A2018_NEC_P01_SD_pcsubmittals.pdf) (Article 100 definitions; standards_development_context) | Exact terms and ownership vary across countries and editions. |
| E022000-05 | Utility equipment ownership and customer responsibility differ by component | [electrical-nyseg-tariff-meter](https://www.nyseg.com/documents/d/nyseg/psc119_section-3) (Section 3 Service Connections and Meters; utility_tariff_context); [electrical-nyseg-service-manual](https://www.nyseg.com/w/esm-manual) (Sections 4, 5 and 7 public index; supporting_context) | Tariff excerpt reviewed, not full tariff for any property; other utilities differ. |
| E022000-06 | Utility rules and local approvals can both affect a service change | [electrical-nyseg-service-manual](https://www.nyseg.com/w/esm-manual) (Introduction and service approval index; utility_requirements); [electrical-nfpa70](https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70) (official NEC development and scope; separate_code_framework) | Exact permits, inspectors and adopted code must be verified locally. |
| E022000-07 | An energy meter measures consumption, not necessarily disconnect or protective function | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Section 9.5 energy versus power; physics); [electrical-nyseg-tariff-meter](https://www.nyseg.com/documents/d/nyseg/psc119_section-3) (Section 3 meter and metering context; utility_function) | Smart meters may have switching capabilities; model and utility practices vary. |
| E022000-08 | Service disconnect opens the defined downstream path, but upstream conductors can remain supplied | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Service conductors and service equipment definitions; primary_workplace_definitions); [electrical-osha304](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (Grounding connections on supply side of service disconnect; regulatory_context) | Other source, transfer and equipment topology must be considered for any real isolation. |
| E022000-09 | Multiple supplies can change energized boundaries in premises | [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Premises wiring definition includes distributed generation; public_us_regulation); [electrical-doe-solar-design](https://www.energy.gov/cmei/systems/solar-photovoltaic-system-design-basics) (System components and inverter functions; general_source_context) | Product-specific transfer and neutral switching not validated. |
| E022000-10 | Two kilowatts for 0.5 hour uses one kilowatt-hour in constant-power model | [electrical-openstax-power](https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power) (Section 9.5 electric power and energy; textbook_physics) | Ideal constant-power example. |
| E022000-11 | 240 V times 200 A equals 48 kVA apparent power for ideal single-phase model | [electrical-openstax-acpower](https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit) (Section 15.4 power and power factor; textbook_physics); [electrical-se-lv-networks](https://www.electrical-installation.org/enwiki/Low-voltage_distribution_networks) (Nominal 120/240 center-tapped secondary; network_example) | Does not assert legal service ampacity or continuous power availability. |
| E022000-12 | Maximum ordinary load current differs from prospective short-circuit current and interrupting capacity | [electrical-osha304](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.304) (1910.304(f) overcurrent protection and breaker ratings; workplace_regulation); [electrical-nfpa70](https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70) (NFPA 70 scope and development; standards_framework) | Actual available fault current and device ratings require site data and product-specific study. |
| E022000-13 | Drawings, utility service instructions and adopted code address different properties | [electrical-nyseg-service-manual](https://www.nyseg.com/w/esm-manual) (Manual sections 2-7 and section 13; utility_documents); [electrical-osha399](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.399) (Definitions of premises wiring and service equipment; terminology) | Site-specific legal obligations not certified by these general sources. |
