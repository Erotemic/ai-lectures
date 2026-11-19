# 018000 — Following a Circuit: Nodes, Branches, and Return Paths

**Track:** Electrical Systems: Principles, Practice, Codes, and Judgment. **Learning surface:** paper circuits, circuit simulators, and component documentation. Real installation drawings are explanatory models rather than evidence of as-built connectivity.

<!-- BEGIN SPOKEN LECTURE -->

# Following a Circuit: Nodes, Branches, and Return Paths

Suppose a lamp dims when another appliance starts. You have several plausible stories. Perhaps both loads share a supply path whose voltage falls under increased current. Perhaps the voltage dip originates farther upstream. Perhaps the lamp's driver reacts differently from other loads. Or perhaps the coincidence has nothing to do with the supply. Before choosing a story, an electrician needs a model of which components are connected to which other components.

That model is a circuit. And tracing a circuit is not chiefly following a pencil line from left to right. It is recognizing **nodes**, **branches**, **sources**, **loads**, and the paths by which charge can move in a complete system. Two pieces of metal drawn at opposite ends of a sheet might represent the same electrical node. Two symbols almost touching might be entirely unconnected. The geometry of the drawing is secondary; the topology is the thing being represented.

## The electrical meaning of a node

A node is a set of points treated as being at the same electrical potential in an ideal circuit model. If several components are joined by an ideal conductor, you can often color that connected region with one color and give it one node name. Real conductors do have resistance and inductance, so the idealization has limits; for introductory steady-state calculations, it usually gives us the right first structure.

A **branch** joins two nodes and contains an electrical element or combination of elements. A resistor, a lamp, or an ideal source can each occupy a branch. A junction is a place where multiple branches meet. If your drawing is complicated, forget the physical layout momentarily. Rewrite it as named nodes joined by named branches. That single act often makes the circuit understandable.

Voltage is the difference between the potentials of two nodes. If I say node A is eight volts, there must be an implicit or explicit reference: eight volts *relative to what*? In a worked calculation, we may choose one node as zero volts to simplify arithmetic. That mathematical reference does not necessarily mean the node is physically connected to soil, to a building's protective earth, or to the neutral conductor of a particular power system.

MIT's circuit-analysis notes by George Chaniotakis and James Cory build nodal analysis from precisely this choice of reference and the two Kirchhoff laws. The method is powerful because it converts the topology of the diagram into an organized set of equations. It does not require guessing which way an electron will go before you begin.

## Follow the complete loop, not only the supply side

Imagine a battery, a switch, and a lamp forming a closed circuit. Conventional current is represented as leaving the positive terminal, passing through the switch and lamp, and returning to the negative terminal. Electrons in a metal move in the opposite average direction. The sign convention changes the story you tell about direction, but not the circuit's physical behavior or the energy balances.

What makes the lamp work is not the presence of a wire labeled positive. The source maintains a potential difference, and the closed conducting path supports current through the lamp. Opening the path interrupts the ideal steady-state current. It does **not** erase the source voltage on the conductor connected to one side of the open switch. An open circuit can have zero current and a substantial potential difference at the same time.

The return side is not optional. In an ordinary two-wire load circuit, charge reaching the load must complete a path to the source. In a common North American branch circuit this normal return may be called neutral; in a direct-current system it may be a negative or return conductor. A protective earthing conductor has a different intended role in normal operation. The details vary with supply and earthing arrangement, but an ordinary circuit analysis always asks which complete paths exist, not merely where electrical power seems to enter.

A subtle point: a loop does not have to look like a circle. A circuit drawn in four corners of a page can still form one closed electrical path. Conversely, an apparent circle may contain an open contact or a component that blocks steady direct current. Shape is not connectivity.

## Conservation organizes the problem

Gustav Kirchhoff's circuit rules express two conservation ideas in the lumped-circuit approximation. The current law says that the algebraic sum of branch currents meeting at a node is zero. It is a bookkeeping statement about charge: current entering a junction cannot disappear there in a steady-state model. During rapid transients, charge can accumulate in capacitances, and a more complete model includes those storage effects. The simple current law remains useful when those effects are represented explicitly in circuit branches.

The voltage law says that the signed sum of voltage rises and drops around a closed ideal lumped loop is zero. It is tempting to call that a universal statement about every changing electromagnetic field. It is not. A time-varying magnetic flux threading a physical loop can induce an electromotive force. In circuit engineering we include that effect as an element or source, or use a field model when the lumped description is no longer adequate. Kirchhoff's laws are excellent tools precisely because we understand the assumptions under which they work.

For a resistor under conditions where Ohm's law is a good model, the voltage across it is resistance times current. Together with the two conservation laws, this lets us predict current paths and voltage drops from a labeled diagram.

## One example with three branches

Consider an invented twelve-volt direct-current source connected through a one-hundred-ohm resistor to a junction. From that junction, one branch contains a three-hundred-ohm resistor and another contains a six-hundred-ohm resistor. Both branches return to the source's negative terminal. These are mathematical component values, not a household wiring design.

The three-hundred-ohm and six-hundred-ohm branches are in parallel, because they share the same two end nodes. Their equivalent resistance is two hundred ohms. The series resistor makes the total three hundred ohms, and the total current is forty milliamperes. The one-hundred-ohm resistor drops four volts. Therefore the junction is eight volts above the selected return node.

The three-hundred-ohm branch carries about twenty-six point seven milliamperes, and the six-hundred-ohm branch carries about thirteen point three milliamperes. Add them and you recover forty milliamperes. That is the current law visible in numbers. The resistor drop plus the junction voltage makes twelve volts. That is the voltage law, using the chosen sign conventions.

Notice what we did not do: we did not start by inventing a current path through the protective earth. We identified the branches the schematic actually specified, selected a reference, and let conservation determine the currents. A good circuit trace always starts from those connected nodes and the documented sources.

## What changes when a connection opens?

Now imagine one of those parallel branches becomes open. The effective network changes. The remaining six-hundred-ohm branch is still connected, so it can continue carrying current. The source current falls; the common resistor's voltage drop also changes, and the junction voltage rises. A disconnection in one branch changes the behavior of another branch through their shared impedance.

If instead the return connection common to both branches opens, the ideal steady-state current through the entire network can become zero. Yet the junction and parts of the load network may rise toward the source potential when measured against the original return reference. The exact potentials of floating nodes depend on leakage, capacitance and the measuring instrument. The phrase **no current** is not interchangeable with **no voltage**, and neither one by itself establishes a safe condition.

The physical analogue in a building is that a shared conductor or connection can produce symptoms in more than one load. However, the house's actual supply architecture, multiple phases, bonding arrangement, power electronics and changing loads have to be included before a simplified model becomes a diagnosis. A classroom network is a hypothesis generator, not a substitute for investigating the installation.

## Control paths and power paths

Another common source of confusion is treating a control diagram and a power diagram as the same thing. A wall switch can directly carry load current, but a thermostat or sensor may only signal a control board that energizes a relay or contactor. The small control circuit and the larger power path can use different supplies. An indicator light glowing on the control board does not prove that the contactor's power contacts are passing current. A relay coil being de-energized does not prove that every connected source has been removed.

When tracing an unfamiliar system on paper, ask two separate questions: what causes a device to change state, and what path supplies the load when the device is in that state? The answers may occupy different pages of the documentation. They may also cross boundaries between installer-provided wiring and internal manufacturer wiring.

An inverter-backed system makes this distinction especially clear. It may contain a utility source, a battery source, switching elements and internal stored energy. A block diagram can tell you the intended modes, but the real sources and transfer architecture must be resolved from product-specific information. A return conductor drawn as one line does not mean different sources can simply have their conductors joined in any configuration.

## Ideal wires hide real impedance

In a neat schematic, a wire has zero resistance. In a real installation, a conductor has resistance, a termination has contact resistance, and alternating current also encounters inductive and capacitive effects. A long path carrying more current develops a larger voltage drop. A small resistance can dissipate significant heat if the current is high enough, because resistive heating is proportional to current squared times resistance.

This is a powerful connection between circuit tracing and real maintenance. A deteriorating connection can affect the voltage available downstream even while the current remains within a breaker rating. But the symptom alone does not locate the connection. Another load switching, source impedance, and the behavior of electronic drivers can create similar observations.

To understand a report of dimming or flicker, first ask which devices share a source or circuit path, whether the symptom occurs together in different rooms, whether it coincides with another load starting, and whether there is a pattern of duration or recurrence. Those are observations that help distinguish topologies without assuming a cause.

## What the schematic cannot tell you

A schematic may omit cable length, conductor material, enclosure location, environmental conditions and manufacturer-required installation details. A one-line may omit conductors by design. A floor plan may show where equipment is intended rather than where hidden cable was actually installed. A circuit model can predict behavior only for the conditions and component values it includes.

The useful habit is to keep a small separation between **observed fact**, **documented connectivity**, and **assumed connectivity**. If a drawing says two nodes connect, that is a statement about the drawing. If a qualified field examination verifies that connection, it becomes evidence about the installation. If you only infer it from wire color or the position of a switch, it remains a hypothesis.

A skilled circuit tracer can say, “Given these connections and this source, here is the current path,” and also, “I do not yet know whether the actual wiring matches that model.” That combination of analytical confidence and evidence discipline is the foundation of useful electrical diagnosis.

<!-- END SPOKEN LECTURE -->

## Non-spoken technical companion

### Circuit reconstruction and units

Choose a reference node `R` at `0 V`. A source makes `P = 12 V`; resistor `R_s = 100 Ω` connects P to A. The two return branches are `R_1 = 300 Ω` and `R_2 = 600 Ω` from A to R.

```text
P (+12 V) -- [R_s = 100 Ω] -- A -- [R_1 = 300 Ω] -- R (0 V)
                              |
                              +-- [R_2 = 600 Ω] -- R
```

- `R_parallel = (300*600)/(300+600) = 200 Ω`.
- `I_total = 12 V / (100+200) Ω = 0.040 A`.
- `V_A = 12 - 0.040*100 = 8 V`.
- `I_1 = 8/300 = 0.026667 A`, `I_2 = 8/600 = 0.013333 A`, and the node currents sum to `0.040 A`.
- `P_Rs = (0.040)^2 * 100 = 0.16 W`; `P_R1 = 8^2/300 ≈ 0.2133 W`; `P_R2 = 8^2/600 ≈ 0.1067 W`; total `0.480 W = 12*0.040 W`.
- With `R_1` open, `I = 12/700 ≈ 0.01714 A`, `V_A ≈ 10.286 V`. The surviving branch voltage rises; the current is lower.

This schematic is an analytical network, not a verified power-system design. Ratings and source behavior are assumed ideal.

### Worked trace questions

1. **Why are two parts joined by an ideal wire normally one node?** The model assigns the same potential throughout an ideal zero-impedance connection; the model ceases to be exact when conductor impedance matters.
2. **If a switch is open, what can be said about its voltage?** It may support nearly the entire source potential; open-circuit current alone does not specify its terminal voltage.
3. **If the common return is opened, what must be recalculated?** The topology and possible node potentials, including floating-node behavior and the measuring circuit. Do not declare all visible conductors at zero potential.
4. **What is a loop in Kirchhoff analysis?** Any closed traversal of the circuit graph, not a circular physical route; include modeled sources of induced electromotive force when needed.
5. **A lamp dims only when an appliance starts. Is a loose neutral proven?** No. Several source, conductor, driver, and load mechanisms fit the observation; a differential diagnostic needs additional evidence.

### Attribution and limits

Kirchhoff's named laws are credited to **Gustav Kirchhoff**, not to MIT course authors. The pedagogical nodal-analysis procedure, named variables and reference selection used here follow lecture notes by **George Chaniotakis and James Cory** in MIT's 6.071 course. Modern field implications are an editorial synthesis, not historical quotations from Kirchhoff. Separate model assumptions from installation or legal requirements.

## Claim-level source map

| Claim ID | Consequential claim | Evidence location and role | Limitations / pending checks |
|---|---|---|---|
| E018000-01 | Voltage is a potential difference between specified nodes (physics) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (p.1, node-method introduction; main); [`electrical-nist-dmm-1988`](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir88-4021.pdf) (§3.1, voltage input behavior; independent_measurement_context) | Reference node selected mathematically is not an installation protective earth. |
| E018000-02 | An ideal node may contain multiple physically separated points connected by zero-impedance model wires (engineering) | [`electrical-mit-node-2023`](https://circuits.mit.edu/_static/S23/handouts/lec04a/lecture_04a.pdf) (node definition and reference note; main); [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (pp. 1–3, nodal representation; related_MIT_context) | Both notes from MIT; real conductors have finite impedance. |
| E018000-03 | KCL balances algebraic currents at a node and KVL signed loop voltages under a lumped model (physics) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (pp. 1–4, KCL/KVL nodal equations; main) | Time varying flux and capacitance must be represented appropriately; unmodeled field phenomena can defeat naive KVL. |
| E018000-04 | Circuit reference zero is not proof of physical connection to soil (engineering) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (p.1, arbitrary reference node; main) | Conceptual ground and equipment protective earth are distinct. |
| E018000-05 | Series and parallel branch model gives node eight volts in illustrated network (derived_calculation) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (nodal method / Ohm law, method only; method) | Arithmetic independently computed from hypothetical values; not a field circuit. |
| E018000-06 | Opening a switch can leave potential on its supply side (safety) | [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b)(2)(iv), de-energized verification; regulatory_example); [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (p.1, potential difference and source model; independent_physics) | Workplace regulation not direct household code; model omits possible alternative sources. |
| E018000-07 | Opening one branch changes equivalent load, common-node voltage, and surviving current (derived_calculation) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (pp.1–4 KCL/Ohm method; method) | Result depends on fixed source and ideal resistor values. |
| E018000-08 | Return path must be accounted for in normal load current rather than assumed via soil (engineering) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (circuit current closure in models; conceptual); [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b), sources and voltage verification; field_boundary) | Earthing arrangements differ; grounding conductor design not specified. |
| E018000-09 | Real source/connection impedance creates load-dependent voltage drop and I-squared-R heating (physics) | [`electrical-mit-node-2006`](https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/9d19116cbabeada1c98004a4367a0ee0_nodal_mesh_methd.pdf) (Ohm law and branch currents; main) | No application-specific temperature or conductor sizing claim. |
| E018000-10 | A schematic, control circuit and actual wiring may differ in detail (engineering) | [`electrical-doe-prints-v1`](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1016-93_VOL1.pdf) (Module 3 schematics and one-lines; main) | No manufacturer control terminal arrangement inferred. |
| E018000-11 | Multiple sources and backfeed require full system topology before isolation is understood (safety) | [`electrical-osha333`](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333) (§1910.333(b)(2)(iv)(B), induced/backfed conditions; main) | The cited obligation is for covered U.S. workplaces, not an installation recipe. |
| E018000-12 | Symptoms shared across loads help locate a common hypothesis but do not confirm a fault (engineering) | [`electrical-doe-causal-2024`](https://www.energy.gov/documents/doe-std-1197-2024-finalpdf) (§5 evidence, causal analysis; method_context) | Deductive inference and observational association; not a claim of a specific defect. |
| E018000-13 | Revisions and as-built discrepancies limit what a drawing proves (engineering) | [`electrical-doe-prints-v1`](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1016-93_VOL1.pdf) (Modules 1 and 3, document types and revision; main) | Physical site verification may be needed before repair decisions. |

