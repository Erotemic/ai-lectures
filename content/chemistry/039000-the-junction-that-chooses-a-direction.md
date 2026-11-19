# The Junction That Chooses a Direction: Diodes, Barriers, and Transistors

<!-- BEGIN SPOKEN LECTURE -->

Here is a question that seems to demand a mechanical answer: how can an electrical component allow current to flow easily in one direction, but strongly resist it in the other? A one-way valve in a pipe can do that with a moving flap. A semiconductor diode has no moving flap. It uses a carefully arranged boundary between regions containing different charge carriers. Understanding that boundary requires chemical doping, electrical forces and thermodynamic equilibrium, not an imaginary gate that swings open.

Begin with silicon that has been doped in two neighboring regions. On one side, electrons are the majority mobile carriers. We call it n-type. On the other, holes are the majority carriers: p-type. These regions may be formed in the same continuous piece of crystal. There need not be a visible seam or adhesive. Yet at their interface the distribution of mobile charge is not initially at equilibrium.

Concentration differences drive diffusion. Some electrons spread from the n-type side toward the p-type side, where holes are available. Some holes diffuse the other way. When an electron meets a hole, they may recombine. As mobile charge leaves the immediate neighborhood of the interface, the dopant ions fixed in the lattice become important. Donor ions left on the n-side are positively charged; ionized acceptors on the p-side are negatively charged. They do not drift out of the crystal like electrons. The resulting region of fixed space charge creates an electric field.

That electric field pushes mobile carriers in directions that oppose their original diffusion. Diffusion tries to smooth out a carrier concentration difference; electrical drift responds to the charge-separated field. At thermal equilibrium the opposing flows balance so that the net current vanishes. A built-in electrostatic potential difference has developed, even though no battery is attached. The region near the junction in which mobile carriers are depleted relative to the bulk is called the depletion region.

Depleted does not mean empty of all electrical charge. It contains charged dopant ions and therefore an electric field. Nor can we extract unlimited power by simply connecting a wire across an isolated junction at equilibrium. Contact potentials elsewhere in the complete circuit and thermodynamic balance prevent a perpetually powered load. The internal field matters enormously for controlling currents and separating photogenerated charge, but it is not an independent source of energy.

Now connect an external voltage. In what is called forward bias, the applied voltage lowers the effective barrier opposing majority-carrier injection across the junction. Electrons from the n-region and holes from the p-region can cross the interface more readily; injected carriers then diffuse and recombine in the neighboring material. Current can rise very rapidly with applied voltage. In reverse bias, the applied voltage increases the barrier to majority carriers. Only a much smaller current, associated with minority carriers and leakage mechanisms, typically flows until breakdown or another nonideal effect becomes important.

A real diode is not a perfectly sharp switch that passes everything in one direction and absolutely nothing in the other. Its current depends on temperature and voltage. The characteristic curve can have an approximately exponential region; resistance in contacts and neutral regions matters at high current; defects, surface paths and tunneling can affect reverse leakage. Under sufficiently large reverse voltage, avalanche multiplication or tunneling can produce substantial current. Some devices deliberately exploit breakdown, but this should not be confused with normal forward conduction.

A practical rectifier uses diodes to change an alternating electrical signal into a predominantly one-directional flow. The analogy to a valve is serviceable at the circuit level, provided we remember that actual operation is about carrier distributions and fields. The same physics forms the basis of light-emitting diodes and many solar cells, though they run the exchange between carriers and photons in different directions.

What if instead of one p-n boundary, we arrange several regions? This creates possibilities for transistors. A bipolar junction transistor uses two junctions and minority-carrier injection to control a much larger current through a device with three terminals. A small input can influence a substantial collector current, subject to device limitations and a supplied power source. The name amplifier should not mislead us into thinking that a transistor manufactures energy. The extra output power comes from the circuit's power supply; the input signal controls it.

Modern integrated circuits also rely heavily on a different family, field-effect transistors. The metal-oxide-semiconductor field-effect transistor, often called a MOSFET, does not operate simply as a pair of p-n junctions. A gate electrode, separated from a semiconductor by a very thin insulating layer, establishes an electric field. That field changes the carrier distribution in a channel between source and drain. In an enhancement-mode device, sufficient gate voltage can induce a conducting channel that was absent or weakly conducting at smaller voltage. We can modulate the channel without moving a mechanical contact.

Think carefully about the chemistry in that sentence. An oxide interface must be electrically insulating enough to limit leakage and chemically well controlled enough to avoid too many trapped charges. The semiconductor beneath it needs the right dopants. Source and drain regions require low-resistance connections. Fabrication must pattern structures across a wafer, and heating steps must not spread impurities into unwanted locations. A transistor is an electrical circuit element manufactured by a sequence of chemical and materials-processing operations.

The ability to pattern a dense population of transistors depends not only on lithographic precision but on surface preparation, dielectric growth, deposition, etching, defect control and metrology. Silicon became an important platform partly because it can form an oxide that supports useful electrical interfaces. Other semiconductors offer advantages for light emission, high-frequency operation or high-voltage power switching, but their material processing and interfaces can present different challenges. There is no single material that is best at every device function.

Consider a simple thought experiment involving two diodes made from the same semiconductor. One has heavily doped regions immediately adjacent to a narrow junction. The other has a more lightly doped region and a broader depletion zone. Even if both are called silicon p-n diodes, their capacitance, leakage, breakdown and switching behavior may differ. The word diode specifies a kind of electrical function, not a complete engineering specification. Doping profiles and interfaces turn a chemical material into a device with quantitative performance.

How might we establish that such a junction is functioning? Measure current at a series of forward and reverse voltages, taking care not to overheat the sample. Vary temperature and see whether the change agrees with carrier and leakage models. Measure capacitance versus bias to learn something about depletion width and doping profile. Illuminate the junction and test whether light generates current. Compare electrical measurements with microscopy or impurity-depth data if manufacturing defects are suspected. Device physics becomes a conversation between models and observations.

The underlying logic is a balance of tendencies. Diffusion redistributes carriers. The resulting field opposes that redistribution. An external voltage alters the balance. Light or injected carriers can disturb it further. A diode and transistor are therefore not departures from ordinary chemistry; they are consequences of chemical control precise enough to shape electronic thermodynamics in space. When atoms are placed in the right pattern and at the right concentrations, solid matter becomes a controllable electrical process.

<!-- END SPOKEN LECTURE -->

## Scientific companion: the junction as a carrier-transport problem

For an ideal abrupt junction at equilibrium in a nondegenerate semiconductor, a common approximation is

$$V_{\mathrm{bi}}=\frac{k_BT}{q}\ln\!\left(\frac{N_AN_D}{n_i^2}\right).$$

Here $N_A,N_D$ are ionized acceptor and donor concentrations under the approximation, $n_i$ the intrinsic carrier concentration, and $q$ the elementary charge. This *built-in potential* is not a freely extractable battery voltage at equilibrium.

A simplified diode law is $I=I_S\{\exp[qV/(nk_BT)]-1\}$, with ideality factor $n$ representing a fitted departure from a particularly ideal model. Real devices depart through series resistance, recombination, tunneling, surface leakage, breakdown, and self-heating.

**Example.** At $T\approx300$ K, $k_BT/q\approx25.9$ mV. With $n=1$, increasing forward bias by about $60$ mV multiplies the exponential part of ideal current by roughly a factor of ten. That does **not** mean every practical diode always has a fixed 0.60 V threshold or that its current can rise without series-resistance limits.

The depletion region has fixed ionized dopant charges and low mobile carrier concentration; it is not free of all charge. A MOSFET uses gate-field control of channel charge, which is distinct from describing every transistor as two diodes.

### Evidence and further reading

- OpenStax, *University Physics*, Volume 3, 9.7, Semiconductor Devices: https://openstax.org/books/university-physics-volume-3/pages/9-7-semiconductor-devices
- OpenStax, *University Physics*, Volume 3, 9.6, Semiconductors and Doping: https://openstax.org/books/university-physics-volume-3/pages/9-6-semiconductors-and-doping
- U.S. Department of Energy, *Solar Photovoltaic Cell Basics*: https://www.energy.gov/cmei/systems/solar-photovoltaic-cell-basics

### Questions to reason through

1. What prevents diffusion at a p-n junction from continuing without limit?
2. Why does the depletion region carry fixed ionic charge despite its name?
3. What does forward bias change, and why does current increase nonlinearly?
4. Why is the built-in field not an independent energy source at equilibrium?
5. In what fundamental way does a MOSFET control current differently from a simple p-n diode?
