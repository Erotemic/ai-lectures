# A Pinch of Impurity Changes Everything: Doping, Carriers, and the Semiconductor

<!-- BEGIN SPOKEN LECTURE -->

In most branches of chemistry, a contaminant is something you try to keep out. Semiconductor fabrication turns that instinct inside out. Engineers may go to extraordinary lengths to purify silicon, grow a highly ordered crystal, and then deliberately add a tiny measured quantity of atoms that do not belong to the original lattice. The added atoms can transform how the crystal conducts electricity. A part-per-million-scale change in composition can matter far more than it would in a bag of sand or a metal bar.

The reason is that electronic properties depend on a special kind of scarcity. A clean semiconductor can have very few mobile carriers compared with its enormous population of atoms. If we can introduce new electrons or holes without destroying the crystal's structure, we gain control over the current. This procedure is called doping. It is not a seasoning of conductivity poured over the surface. It is an atomic-scale modification of the possible electronic states and the position of the electronic chemical potential.

Silicon provides an accessible example. A neutral silicon atom has four valence electrons, and the crystalline silicon network uses covalent bonds extending through the solid. Substitute a phosphorus atom for one silicon atom. Phosphorus ordinarily has five valence electrons. In a simple bonding picture, four contribute to the local network and one remains comparatively weakly bound. Because the surrounding material screens electric charge, the energy needed to free that extra electron into a mobile state can be small compared with the fundamental gap of silicon. The dopant acts as an electron donor.

Call the result n-type silicon. The letter n refers to negative carriers, electrons, becoming the majority mobile charge carriers under ordinary operating conditions. It does not mean the entire piece of silicon has acquired a large net negative charge. The donor atom, after giving up its extra mobile electron, is an ionized positive center in the lattice. Its charge is balanced by the mobile electronic charge and other carriers and defects. The material remains approximately electrically neutral away from interfaces and externally imposed space-charge regions.

Now substitute a boron atom, which has only three valence electrons. It can create an acceptor state. An electron from the surrounding valence band can fill that state, leaving behind a mobile hole in the valence band. The resulting p-type material conducts predominantly through holes. Again the bulk need not have a net positive charge: ionized acceptors are negatively charged and balance the positively charged mobile holes. The letters p and n name the majority carriers, not unbalanced electrostatic charge in the entire crystal.

A hole is worth considering carefully. If we imagine a row of seats with every seat occupied except one, a person can shift into the empty seat. Repeated shifts carry the vacancy down the row in the opposite direction. In a semiconductor the analogy is not a literal queue of jumping electrons, but it captures the bookkeeping. Instead of describing the tiny changes of all the filled electronic states, physicists describe the motion of a missing electron as that of a positively charged quasiparticle.

The energy-band picture adds precision. A shallow donor introduces an occupied state energetically close to the conduction band in a lightly doped semiconductor. A shallow acceptor introduces a state close to the valence band. The electron or hole can become mobile with much less thermal energy than it would take to create a fresh electron-hole pair across the entire semiconductor gap. This is why intentional impurities can dominate conductivity at room temperature. At very low temperatures, many dopants can remain un-ionized; at sufficiently high temperatures, thermally generated intrinsic carriers may again become important. The familiar statement that an n-type wafer contains mainly electrons is therefore conditional, not timeless.

How little doping is little? Imagine ten billion silicon atoms and only one of them is a useful donor. Even that ratio can produce a substantial increase in the available mobile electron population compared with an extremely pure semiconductor. Device designers specify dopant concentration per volume rather than using an informal phrase such as lightly contaminated. In practice the relevant concentrations vary widely across materials, devices and fabrication stages. A transistor channel, an electrical contact region and a high-voltage device may require very different profiles.

Doping also changes the Fermi level. Informally, this is an energy that helps describe the statistical occupancy of available electronic states at equilibrium. In nondegenerate n-type material it tends to move closer to the conduction band; in p-type material, toward the valence band. But the Fermi level is not an extra physical band occupied by a layer of electrons. It is a thermodynamic bookkeeping quantity related to how many states are occupied. At high doping, more complex effects such as band-gap narrowing and degenerate statistics can arise; the simple pictures need refinement.

A crucial distinction follows. Doping creates carriers, but it does not give them unlimited speed. Ionized dopants scatter other carriers. Increasing dopant concentration can raise the number of mobile charges and at the same time reduce mobility. This produces competing effects in conductivity. Lattice vibrations, dislocations, grain boundaries and surfaces also scatter carriers. Good semiconductor engineering is not a contest to add the maximum number of impurities; it is a controlled compromise among conductivity, switching behavior, breakdown voltage, optical response, and manufacturability.

Nor does every foreign atom serve as a useful dopant. Some impurities introduce deep energy levels and act as traps, capturing electrons or holes and enabling their recombination. A contaminant that contributes little to useful carrier density may ruin a solar cell by making newly generated electron-hole pairs disappear before they can be collected. The same chemical addition can be beneficial in one context and harmful in another. Chemical identity, lattice position, local bonding and processing conditions matter.

How are dopants introduced? Crystal growth can incorporate selected atoms from a melt or vapor. Ion implantation accelerates dopant ions into a wafer, producing a concentration profile that later thermal processing can modify and activate. Diffusion allows atoms to move at elevated temperature. Implantation also damages the lattice, so annealing may be necessary to repair defects and place dopants into electrically active configurations. This is another instance of a material remembering its manufacturing history. The dose delivered to the surface is not automatically identical to the final number of useful mobile carriers.

We need ways to check the outcome. A four-point probe measures electrical sheet resistance with reduced sensitivity to contact resistance. The Hall effect places a conducting sample in a magnetic field and detects a transverse voltage, which in a suitable one-carrier regime can indicate dominant carrier sign and estimate carrier concentration. More elaborate measurements separate carrier mobility, concentration and depth-dependent profiles. Combining chemical depth analysis with electrical tests helps establish whether the dopants are where intended and electrically active.

Consider a deliberately simplified design problem. We have two nominally identical silicon samples. Into one we introduce donor impurities; into the other, acceptors. The first tends to carry current mainly with mobile electrons, the second with holes. If their measured resistivities differ, do not conclude that the dopant giving lower resistivity was inserted in greater quantity. Differences in mobility, incomplete ionization, traps and processing damage may account for part of the difference. A single resistance measurement cannot reveal every microscopic cause.

The significance of doping goes beyond making silicon a better conductor. It enables adjacent regions of a crystal to have different electronic behavior while retaining a coherent material network. Connect n-type and p-type regions, and charge redistributes until an internal electric field emerges near their boundary. That boundary becomes a diode, a solar-cell junction or part of a transistor. Very little of the useful function comes from the impurity atoms mechanically blocking electrons. It comes from a delicate equilibrium among chemical composition, available quantum states and mobile electrical charge.

A semiconductor is powerful because it is not an ideal conductor. We can give it carriers, take them away, create barriers, shape electric fields, and cause light to make or unmake electrical charge. What seemed like an inconvenient gap in its electronic spectrum becomes the means of control. The impurity is not a flaw to tolerate. Under the right conditions, it is the chemical instruction that makes the device possible.

<!-- END SPOKEN LECTURE -->

## Scientific companion: donors, acceptors, and charge balance

For a lightly doped, nondegenerate semiconductor, $\sigma=q(n\mu_n+p\mu_p)$. In an idealized extrinsic n-type region with fully ionized donors and few acceptors, $n\approx N_D$; for p-type, $p\approx N_A$. These approximations fail with incomplete ionization, compensation, high intrinsic carrier densities or degeneracy. The mass-action approximation $np=n_i^2$ applies to nondegenerate thermal equilibrium under its normal assumptions.

**Example.** Suppose $n=10^{16}\,\mathrm{cm^{-3}}$, $\mu_n=1000\,\mathrm{cm^2/(V\,s)}$, and holes contribute negligibly. Then $\sigma\approx(1.602\times10^{-19})(10^{16})(1000)=1.602\,(\Omega\,\mathrm{cm})^{-1}$, giving resistivity $\rho\approx0.624\,\Omega\,\mathrm{cm}$. If mobility halves while $n$ is unchanged, conductivity also halves. Doping does not enter the formula directly: *mobile carriers* and *their mobility* do.

For a single-carrier Hall-effect model, $R_H\approx\pm1/(qn)$ with sign determined by the dominant carrier type. In mixed-carrier systems, Hall inference requires more care. Dopant concentration measured chemically is not necessarily the electrically active carrier concentration.

### Evidence and further reading

- OpenStax, *University Physics*, Volume 3, 9.6, Semiconductors and Doping: https://openstax.org/books/university-physics-volume-3/pages/9-6-semiconductors-and-doping
- OpenStax, *University Physics*, Volume 3, 9.7, Semiconductor Devices: https://openstax.org/books/university-physics-volume-3/pages/9-7-semiconductor-devices
- U.S. Department of Energy, *Solar Photovoltaic Performance and Efficiency Basics*: https://www.energy.gov/cmei/systems/solar-photovoltaic-performance-and-efficiency-basics

### Questions to reason through

1. Why can a small concentration of dopants change semiconductor conductivity greatly?
2. How can n-type and p-type materials remain electrically neutral overall?
3. Why is a hole a useful positively charged carrier description, rather than a proton?
4. Why might increasing dopant concentration increase conductivity and reduce mobility at the same time?
5. What different information could chemical profiling and a Hall measurement provide?
