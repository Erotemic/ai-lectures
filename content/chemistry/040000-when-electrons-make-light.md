# When Electrons Make Light: The Chemistry of Light-Emitting Diodes

<!-- BEGIN SPOKEN LECTURE -->

A small indicator light can stay cool enough to touch while producing a clear, intense color. It is not glowing because a metal filament has been heated until it shines. In a light-emitting diode, electrical energy is converted into electronic excitations inside a semiconductor, and some of those excitations release their energy as photons. The choice of semiconductor chemistry influences the color; the internal device structure influences the efficiency. A red indicator, a blue display pixel, and a white room lamp all illustrate the same general exchange, but not the same materials design.

Begin with a p-n junction under forward bias. Electrical contacts inject electrons from one side and holes from the other into an active region. An electron in an elevated electronic state can recombine with a hole, leaving the electronic system in a lower-energy state. The lost energy must go somewhere. Under suitable conditions, it emerges as a photon. The phenomenon is electroluminescence: light produced because an electrical input drives electronic transitions.

The emitted photon has an energy set by the particular transition, usually on the scale of the semiconductor's energy gap. Because photon energy rises with frequency, and frequency rises as wavelength shortens, a larger gap often corresponds to bluer light. A red photon near six hundred and fifty nanometers carries about one point nine electron-volts. A blue photon near four hundred and fifty nanometers carries about two point eight. These are useful reference numbers, not a claim that a device emits one perfectly sharp wavelength or that its band gap equals a measured peak photon energy exactly.

Why not use silicon as an efficient light source? Silicon is excellent for many electronic devices, but its fundamental band gap is indirect. A radiative recombination transition involving the band extrema typically also needs a change in crystal momentum supplied by a lattice vibration or another interaction. The extra condition makes that process less probable. Many injected carriers lose their energy through nonradiative channels before they emit visible light. Other semiconductor families, with more favorable direct optical transitions, are much better choices for ordinary LEDs.

Compound semiconductors are chemically interesting because we can change their composition and electronic structure. Gallium arsenide, aluminum gallium indium phosphide alloys, and gallium nitride based alloys occupy different portions of the optoelectronic design space. In an alloy, changing the proportion of constituent elements can tune band structure and wavelength, though strain, defects and lattice matching also matter. What an LED emits is partly a problem of inorganic chemistry: choosing atoms that form a useful crystalline compound and controlling how they are arranged.

A functioning LED also needs to keep electrons and holes in the same region long enough to recombine radiatively. Device engineers make heterostructures, joining layers with different electronic band structures. Some active layers form quantum wells, very thin regions that confine carriers in one direction. Confinement can raise the chance that injected electrons and holes meet in the intended optical region. It is not that the electrons are trapped forever; useful light emission depends on balancing injection, confinement, radiative recombination and escape of the photons from the device.

Escape is a problem of its own. Light produced inside a crystal can be reflected internally because of its high refractive index. Some photons travel toward absorbing contacts or other layers, and some never emerge. Surface texturing, optical structures, reflectors and package design can improve extraction. As a result, we need to distinguish internal quantum efficiency, the fraction of relevant recombination events giving photons, from external quantum efficiency, which includes whether generated photons actually leave the device. Electrical-to-optical power efficiency also depends on the operating voltage and other losses.

Defects can quietly destroy performance. An atom out of place, a dislocation, or an unwanted impurity can create electronic states in the gap. Those states can facilitate nonradiative recombination: electrical energy becomes lattice vibration, or heat, rather than useful light. At high operating current, other loss pathways and heating can reduce efficiency. Color, brightness, stability and lifetime are therefore functions of materials chemistry, interfaces and temperature, not just of the selected band gap.

The history of blue LEDs makes this concrete. By the late twentieth century, useful red and green LEDs were already available, but efficient blue emitters were far more difficult to engineer. Gallium nitride had promising optical properties but posed demanding crystal-growth and p-type doping problems. Isamu Akasaki and Hiroshi Amano, working in Japan, and Shuji Nakamura, also working in Japan during the decisive development period, helped overcome those obstacles in complementary ways. Their contributions to efficient blue light-emitting diodes were recognized with the 2014 Nobel Prize in Physics. The story is not that someone merely discovered the right blue chemical element. It is about learning to grow suitable material, control its carriers and build working structures from it.

Blue emission made new approaches to white lighting possible. One common white LED uses a blue semiconductor emitter with a phosphor coating. The phosphor absorbs some blue light and reemits a broader distribution of longer-wavelength light. The eye integrates the remaining blue and the converted light as white, with the precise appearance depending on the spectrum. This is wavelength conversion, not a hot tungsten filament and not three perfectly independent colors generated by every device. Different architectures use multiple colored emitters or other conversion materials.

A phosphor is itself a chemical and solid-state system. Its host lattice, activator ions and local environment influence which wavelengths are absorbed and emitted. Some energy is lost in converting a high-energy blue photon to a lower-energy one, often called the Stokes loss. The material must withstand heat, moisture and sustained optical excitation. Color rendering, manufacturing consistency and aging bring chemistry back into what might otherwise look like a simple electrical component.

How would we test the claim that an LED is efficient? Measuring luminous brightness alone is not enough. The human eye's sensitivity varies with wavelength, so equal radiant power at different colors produces different perceived brightness. Measure electrical power input, emitted optical power and the spectral distribution. Record temperature and drive current, because the efficiency changes with operating conditions. An integrating sphere helps capture light emitted in many directions, while spectrometers reveal how its color shifts. A device that looks brighter to the eye may not be converting a larger fraction of electrical energy into optical energy.

The distinction matters when comparing LEDs with fluorescence. A fluorescent dye also emits light after an electronic excitation, but its excitation can come from absorbed light rather than a junction's electrical current. An organic light-emitting diode employs electrically driven excited states in organic materials; its microscopic pathways and spin statistics differ from those of a typical inorganic LED. In all cases we ask the same questions: where did the excitation energy come from, what electronic states were available, and how much was emitted as light rather than dissipated?

Return to the tiny indicator light. It is a chemical crystal engineered so that mobile charge recombines in the place and manner we want. To make one color, adjust the allowed electronic energies. To make it bright, manage carrier injection and optical escape. To make it last, suppress destructive defects and manage heat. The light is not an incidental decoration on the electronics. It is a controlled consequence of how matter exchanges energy between electrons and photons.

<!-- END SPOKEN LECTURE -->

## Scientific companion: emission energy and light efficiency

Photon energy: $E_\gamma=hc/\lambda\approx1240\,\mathrm{eV\,nm}/\lambda_{\mathrm{nm}}$. A $650$ nm photon carries approximately $1.91$ eV; a $450$ nm photon approximately $2.76$ eV. Real emission peaks depend on band structure, confinement, temperature and other effects.

**External quantum efficiency** is, under a specified definition and measurement protocol, $\eta_{\mathrm{EQE}}=N_{\mathrm{photons,out}}/N_{\mathrm{electrons,in}}$. A simplified factorization is $\eta_{\mathrm{EQE}}\simeq\eta_{\mathrm{injection}}\eta_{\mathrm{internal}}\eta_{\mathrm{extraction}}$; the factors are device- and definition-dependent. For white LEDs with downconversion, distinguish radiometric, photometric and photon-counting efficiencies, including the phosphor's conversion losses.

**Worked comparison.** Suppose an electrical input drives $10^{18}$ electrons through an illustrative single-color LED and $4\times10^{17}$ photons escape. The external quantum efficiency is $40\%$. This number by itself is not the wall-plug efficiency: to compute energy efficiency we also need photon energy and electrical energy delivered per electron, including the operating voltage.

Direct versus indirect optical gaps involve conservation of crystal momentum as well as energy. This is why equating gap energy with LED usefulness is incomplete.

### Evidence and further reading

- Royal Swedish Academy of Sciences, *2014 Nobel Prize in Physics, Press Release*: https://www.nobelprize.org/prizes/physics/2014/press-release/
- Royal Swedish Academy of Sciences, *Advanced Information: Efficient Blue Light-Emitting Diodes*: https://www.nobelprize.org/uploads/2018/06/advanced-physicsprize2014.pdf
- U.S. Department of Energy, *A Practical Primer to LED Technology*: https://www.energy.gov/management/articles/practical-primer-led-technology
- OpenStax, *University Physics*, Volume 3, 9.5: https://openstax.org/books/university-physics-volume-3/pages/9-5-band-theory-of-solids

### Questions to reason through

1. Why is a direct-gap material often more useful for an LED than silicon?
2. How does an LED's semiconductor composition help determine its color?
3. Why do device engineers care about both carrier confinement and extraction of photons?
4. What chemistry and processing challenges made efficient blue LEDs difficult?
5. How can an LED have high photon quantum efficiency but lower electrical-to-optical energy efficiency?
