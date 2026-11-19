# Why Solids Have Forbidden Energies: From Atomic Orbitals to Energy Bands

<!-- BEGIN SPOKEN LECTURE -->

A copper wire and a piece of silicon can look like ordinary solid matter. Put electrodes on them, apply a small voltage, and they behave very differently. Copper carries current readily. Pure silicon, at the same temperature, is a much poorer conductor. A clean crystal of diamond is more resistant still. None of these objects contains a literal obstacle course through which electrons must squeeze. The difference is in which electronic states the solid makes available, and which of those states electrons already occupy.

Start with a single atom. Its electrons cannot have just any energy. They occupy quantum states with particular allowed energies. Chemistry gives these states names such as orbitals, and uses them to explain periodic trends and bonding. Move two atoms close together, and their electron states interact. An energy level that belonged to each isolated atom can split into two combinations. One combination may be energetically favorable, the other less so. This is already the beginning of chemical bonding.

Now imagine a hundred atoms forming a regular chain. What had been one atomic energy level can become a hundred closely spaced states. In an actual crystal, with an enormous number of atoms, those states lie so densely together that we describe them as an energy band. Between some groups of allowed states there can remain ranges of energy for which the crystal has no available electronic states. Those ranges are band gaps. A band gap is not a region of empty physical space between atoms. It is a forbidden range of electron energies in a particular solid.

Why does a crystal produce bands and gaps? Part of the answer is that electrons are waves as well as particles. In a periodic arrangement of atomic nuclei, their waves must fit the repeating environment. Some wavelengths combine consistently with that pattern; at certain boundaries, wave interference separates otherwise nearby energies and can open a gap. We do not need to solve the wave equation to grasp the consequence. The crystal's geometry and bonding alter the menu of electronic states.

The menu is only half the story. We must ask which states are filled. Electrons obey an exclusion principle: two electrons cannot occupy an identical quantum state, though states differing in spin can share a spatial orbital. In an ordinary solid near equilibrium, lower-energy available states are preferentially occupied. If the top occupied region is a partially filled band, nearby empty states are available with almost no energy cost. An electric field can slightly change how those electrons occupy states, giving rise to current. This is one reason metals conduct.

Now consider a material in which the highest relevant band is filled and a higher band is empty. We call the filled band the valence band and the higher one the conduction band. To create mobile electronic carriers at low temperature, energy must move some electrons across the gap. A filled band cannot respond like a partially filled band, because there is no nearby vacant state within it for every electron to shift into. That sentence is a simplified picture of a more detailed theory, but it explains a great deal. A semiconductor has a gap modest enough that temperature, light, or added impurities can create useful carriers. An insulator usually has a sufficiently large gap and sufficiently few accessible carriers that ordinary electric fields cannot produce much conduction.

There is no magic numerical boundary at which every material suddenly becomes a semiconductor. What counts in practice also depends on temperature, defects, impurities and the intended device. Silicon's room-temperature band gap is roughly one point one electron-volts. Diamond's is about five and a half. Both have gaps, but their ordinary electrical responses differ dramatically. Copper is a metal because its band filling and electronic structure support a high density of mobile carriers. The ordering of those examples is more informative than a rigid vocabulary rule.

An electron-volt is the amount of energy an electron gains when it moves through a potential difference of one volt. It is a convenient small unit: one electron-volt is about one point six times ten to the minus nineteen joules. To picture a one-electron-volt gap, imagine that a single electron must gain roughly that much energy to make an electronic transition across it. That does not mean one volt applied across a block automatically lifts every electron into the conduction band. Voltage, electric field, scattering, and carrier generation are different parts of the device problem.

Where do the carriers in a semiconductor come from? Some are created thermally. At finite temperature, a small fraction of electrons can be promoted into the conduction band. Each promotion leaves an unoccupied state in the valence band, called a hole. When a neighboring valence electron moves into that vacancy, the vacancy appears to move the opposite way. Rather than track the motion of every electron in an otherwise filled band, we describe the hole as a mobile positive charge carrier. It is not a missing proton and not a freely wandering positively charged atom. It is a useful description of collective electronic motion.

In a perfectly pure semiconductor in thermal equilibrium, electrons and holes created across the gap appear in pairs. Their number depends strongly on temperature and gap size. Pure silicon at room temperature is not full of conduction electrons like a copper wire; compared with the number of atoms, the intrinsic carrier concentration is tiny. Yet those few carriers matter, and semiconductor engineers can change their number by enormous factors. The ability to control that population is the foundation of electronics.

An electrical current is not determined by carrier count alone. A carrier also has to move through the solid. Crystallographic disorder, lattice vibrations, impurities and boundaries scatter carriers and limit their mobility. Two specimens with similar numbers of carriers can therefore have different conductivities. This is a direct return to our materials-chemistry theme: composition and band structure do not tell the whole story unless we also know the defects and processing history.

Light provides another way of probing the allowed energies. A photon carries energy proportional to its frequency and inversely proportional to wavelength. A photon with too little energy may pass through a semiconductor without being absorbed by a transition across its fundamental gap. A photon with enough energy can, if the transition is allowed and absorption occurs, generate an electron-hole pair. Light does not have to raise one electron exactly to the top of a band diagram; actual absorption involves available states, transition probabilities and sometimes the assistance of lattice vibrations.

This explains a familiar contrast: some solids are transparent to visible light, some absorb it, and some absorb different portions of the spectrum. The band gap is a powerful clue, but color also depends on other electronic transitions, defects, thickness, scattering and reflection. We should never infer the full optical behavior of a complex material from one band-gap number alone.

There is a further wrinkle. A band diagram often shows just the energy axis, but electrons in crystals also have crystal momentum, a quantity describing their wave pattern in the periodic lattice. In a direct-gap semiconductor, the conduction-band minimum and valence-band maximum occur at compatible crystal momenta; an electron and hole can recombine to emit a photon relatively readily. In an indirect-gap material such as silicon, a lattice vibration often has to participate to conserve momentum. This makes light emission less probable, even though silicon is excellent for many electronic devices. The distinction becomes crucial when we build light-emitting diodes.

How can scientists tell whether this picture is more than a drawing? Electrical conductivity versus temperature helps reveal carrier activation and scattering. Optical absorption identifies thresholds and transition features. Photoemission experiments can examine occupied electronic states. Hall measurements can help estimate the sign and density of mobile carriers, though several simultaneous carrier types complicate simple interpretations. No single experiment outputs a universal band diagram without assumptions; several kinds of evidence are brought together.

Return to the copper wire, the silicon wafer and the diamond. The periodic table explains which atoms they contain, and chemical bonding explains why their structures are stable. Band theory adds another level: it describes the electronic possibilities of an entire solid. We can now ask not just how atoms join, but which states electrons can occupy and how easily charge can respond. What looks like passive matter begins to resemble an adjustable electrical material. The next conceptual step is to adjust it deliberately, one impurity at a time.

<!-- END SPOKEN LECTURE -->

## Scientific companion: bands, gaps, and carriers

The electronic energy structure of a periodic crystal is conveniently described by Bloch states $\psi_{n\mathbf{k}}(\mathbf{r})$ with energies $E_n(\mathbf{k})$. A *band gap* is an energy interval with no allowed bulk one-electron states in the idealized band picture. Band gaps, measured optical gaps and transport activation energies need not coincide exactly in defective or strongly interacting materials.

For an intrinsic semiconductor in a simple equilibrium model, $n=p=n_i$. A useful nondegenerate approximation is $n_i\propto T^{3/2}\exp[-E_g/(2k_BT)]$, with material-dependent effective-mass factors. This relation illustrates sensitivity to temperature, not a precise formula over all temperature ranges.

Conductivity for two carrier types is $\sigma=q(n\mu_n+p\mu_p)$, where $n,p$ are carrier number densities and $\mu_n,\mu_p$ their mobilities. Increasing carrier number does not necessarily improve mobility. For light of wavelength $\lambda$, $E_\gamma=hc/\lambda\approx(1240\,\mathrm{eV\,nm})/\lambda_{\mathrm{nm}}$. A silicon-gap-scale energy of $1.1$ eV corresponds to a wavelength of roughly $1127$ nm, but the spectral absorption edge is not determined solely by this arithmetic because silicon has an indirect band gap.

**Worked comparison.** A direct-gap material with $E_g=2.0$ eV has a photon-energy threshold corresponding to about $620$ nm. A $700$ nm photon has energy about $1.77$ eV, below that nominal interband threshold. Whether other sub-gap absorption processes occur must be measured rather than inferred away.

### Evidence and further reading

- OpenStax, *University Physics*, Volume 3, 9.5, Band Theory of Solids: https://openstax.org/books/university-physics-volume-3/pages/9-5-band-theory-of-solids
- OpenStax, *University Physics*, Volume 3, 9.6, Semiconductors and Doping: https://openstax.org/books/university-physics-volume-3/pages/9-6-semiconductors-and-doping
- U.S. Department of Energy, *Solar Photovoltaic Performance and Efficiency Basics*: https://www.energy.gov/cmei/systems/solar-photovoltaic-performance-and-efficiency-basics

### Questions to reason through

1. Why do densely spaced electronic states form bands when isolated atoms form a crystal?
2. Why is a filled valence band not as readily conducting as a partially filled band?
3. Why does an electron promoted across a gap also create a mobile hole?
4. What does a band-gap value tell you about optical absorption, and what does it not tell you?
5. How could two wafers with similar electronic gaps nevertheless have different conductivities?
