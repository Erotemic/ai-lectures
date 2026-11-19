# When Light Measures Matter: Absorption, Color, and Fluorescence

<!-- BEGIN SPOKEN LECTURE -->

A glass of tea looks darker when the liquid is concentrated. A thin layer looks lighter than the same tea in a deep glass. A chemist can exploit both observations, measuring the amount of light that makes it through a sample and inferring how much absorbing material is present. This is the simple idea behind absorbance spectroscopy. But it becomes a precise method only after we ask what the light is doing, which molecules interact with it, and where the simple description breaks down.

Visible light is one range of electromagnetic radiation. Its photons carry energies that depend on frequency: shorter wavelength corresponds to higher photon energy. Ultraviolet light has higher photon energies than visible light. When an atom or molecule absorbs a photon, energy is transferred into an allowed state of the material. The light does not simply vanish because the substance is 'colored.' The molecule or atom changes its energy, and what happens next can include molecular vibration, collisions, chemical change or emission of another photon.

Consider a solution that transmits only half the incoming intensity at a chosen wavelength. Its transmittance is one half. The absorbance, defined as the negative base-ten logarithm of transmittance, is about zero point three zero one. If the same solution and same optical conditions reduce transmission to a tenth, absorbance is one. If they reduce it to a hundredth, absorbance is two. Absorbance makes a multiplicative attenuation of light into an additive quantity, which is why it is so convenient for concentration measurements.

Under appropriate conditions the Beer–Lambert relation states that absorbance equals a molar absorption coefficient times path length times concentration. Keep the wavelength, solvent, chemical form and path fixed, and doubling concentration doubles absorbance within the model's applicable range. A two-centimeter cell has twice the absorbance of a one-centimeter cell for the same homogeneous solution, assuming there are no complications that violate the model. The light has twice as much absorbing material to traverse.

There is a useful intuitive derivation. Imagine a very thin slice of a uniform solution. The slice removes a fraction of the light proportional to the light entering it and the number of relevant absorbers. The next slice acts on what remains. Multiply these small losses through many slices and the transmitted fraction decreases exponentially with distance. Taking a logarithm converts that exponential attenuation into a linear dependence on path length. It does not imply that each individual molecule absorbs one photon on every pass; it is a statistical description over many photons and molecules.

An important practical detail is the blank. The container absorbs and reflects some light. The solvent may absorb too. A spectrophotometer commonly compares a sample measurement with an appropriate reference or blank so that absorbance is assigned mainly to the substances of interest. A mis-matched cell, a fingerprint on a window, bubbles in the optical path or differences in solvent composition can produce apparent changes. If a turbid sample scatters light out of the detector's collection angle, the instrument may report an apparent loss that looks like absorption. Ordinary absorption spectroscopy alone may not tell absorption from scattering.

Color emerges because different wavelengths are transmitted, reflected and absorbed differently. A solution that strongly absorbs blue wavelengths may appear yellow or orange in transmission. The perceived color also depends on illumination and the human visual response. A single 'redness' number does not specify a unique molecular identity. Different molecules can absorb in overlapping regions, and one molecule can change its spectrum when its protonation state or chemical environment changes. Chemists often choose a wavelength where the target has strong response and common interferences have weaker response, but that is an optimization rather than a guarantee of specificity.

If an unknown contains two absorbing compounds whose spectra overlap, a measurement at one wavelength may not distinguish how much of each is present. A stronger strategy is to measure several wavelengths and model the combined spectrum, ideally with known standards and a check that the chosen model is identifiable. In a simple linear approximation, each compound contributes an absorption coefficient at each wavelength, and the total absorbance is the sum. With enough independent spectral information we may be able to estimate two concentrations. If the two spectra are nearly identical, adding more decimal places does not solve the problem.

The underlying molecular transitions matter. Many organic compounds absorb ultraviolet light because their electrons can occupy excited states. Conjugated systems, in which electrons are delocalized across adjacent bonds, often have electronic transitions at lower energies than isolated saturated bonds. This is one reason a long conjugated pigment may absorb visible light while a simple colorless saturated compound does not. Yet it is not correct that all conjugated substances are visibly colored: the specific energy gaps and allowed transitions govern the wavelengths and intensities.

A metal-containing complex can acquire color through transitions involving metal and ligand orbitals, and in some cases through electron transfer between them. The surrounding ligands influence the spectrum. Analytical chemists sometimes deliberately form a colored complex with a target ion, converting a species that barely absorbs in a convenient region into one that can be measured colorimetrically. Such reactions require controlled pH, reagent excess or reaction timing. Otherwise a color change may reflect incomplete chemistry rather than concentration alone.


In very concentrated samples a second problem appears. If the sample removes nearly all the incident light, the detector may be left measuring stray light and dark background rather than the small transmitted beam the simple law expects. As absorbance rises, a tiny additive optical background can cause a large error in inferred concentration. A sensible chemist may dilute a concentrated sample rather than assume that an extremely high absorbance yields an extremely precise concentration. The dilution introduces its own uncertainty, but it can move the measurement into a reliable region of the instrument's response.

Spectral measurements can also follow chemistry rather than merely count stable molecules. A pH indicator changes color because acid-base reactions alter the distribution among molecular forms with different electronic transitions. If we monitor an indicator, the measured absorbance depends on both its total concentration and its chemical speciation. With an appropriate model and known equilibrium behavior, that becomes useful information about pH or acidity. Without those assumptions, interpreting the color as only a concentration is misleading. This is why optics and chemical equilibrium so often appear together in practical analysis.

Now consider what happens after absorption. Some excited molecules relax without emitting visible light, transferring energy to vibrations and surroundings. Others emit a photon. If emission occurs promptly from an appropriate excited electronic state, we call it fluorescence. The emitted photon often has lower energy, and therefore longer wavelength, than the light used to excite the molecule. This separation between excitation and emission can help distinguish fluorescence from transmitted excitation light.

A fluorescence spectrometer illuminates the sample at one set of wavelengths and collects emitted light, often from a different direction. Because it is measuring light generated by the sample rather than the small difference between two large transmitted intensities, fluorescence can be extremely sensitive for suitable molecules. But it is not universally more accurate. Not every compound fluoresces; solvent, pH, oxygen and nearby molecules may change emission efficiency. Concentrated samples can absorb excitation light unevenly or reabsorb the emitted light. Detector geometry and inner-filter effects complicate a naive assumption that fluorescence intensity always scales linearly with concentration.

Quenching illustrates the difference between chemical amount and signal. Suppose a fluorescent molecule is present at the same concentration in two solutions, but one contains a quencher that promotes nonradiative deactivation. It emits less light. If we interpret fluorescence intensity using a calibration made without the quencher, we might infer too little molecule. The detector is not broken; the chemistry between excitation and emission has changed. A method must establish when its optical response is transferable between sample and standards.

A useful real-world method uses dye or complex formation to measure a particular substance in water. The procedure is not simply 'shine a lamp through the water.' It may involve taking a representative sample, adjusting conditions, adding a color-forming reagent, allowing a specified reaction time, referencing an appropriate blank, measuring absorbance at a particular wavelength, and checking that other sample constituents do not generate the same optical response. The optical law is one component of a much larger measurement procedure.

Notice how the same scientific principle supports several kinds of inference. A sharp atomic emission line can indicate the presence of an element under particular conditions. A broadband molecular absorption spectrum can reveal electronic structure. Absorbance at a chosen wavelength can estimate concentration. Fluorescence lifetime and emission shape can probe the surroundings of a molecule. These are related observations, not interchangeable claims. Each requires its own mapping from signal to chemical information.

Return to the tea. In a clear solution, light attenuation can give useful concentration information. But a darker appearance does not automatically mean more of one named compound. Color can change with composition, pH, temperature, optical path and scattering. Analytical chemistry turns a familiar visual effect into measurement by specifying wavelength, path length, chemical state, calibration and blank. It is exactly the same discipline we needed when choosing a sample and constructing a calibration curve. The next form of light spectroscopy asks a different question: not which electronic transitions a molecule absorbs, but how its atoms can vibrate together.

<!-- END SPOKEN LECTURE -->

## Scientific companion: optical measurements

For transmittance $T=I/I_0$, absorbance is $A=-\log_{10}T$. Thus $T=0.5$ gives $A=0.3010$ and $T=0.01$ gives $A=2$. A non-ideal detector, stray light, scattering or a mismatched blank can invalidate simple interpretation.

**Beer–Lambert relation:**

$$A(\lambda)=\epsilon(\lambda)\,\ell\,c.$$

$$ is not implied anywhere; $\ell$ is optical path length, $c$ is concentration and $\epsilon$ has units appropriate to both. For $\epsilon=10^4\ \mathrm{L\,mol^{-1}\,cm^{-1}}$, $\ell=1\ \mathrm{cm}$ and $c=20\ \mathrm{\mu M}$, $A=0.20$ and $T=10^{-0.2}\approx0.631$. The assumed constant-$\epsilon$ relation may fail when chemical speciation changes with concentration.

**Two absorbing species (idealized):**

$$A(\lambda_i)=\ell[\epsilon_1(\lambda_i)c_1+\epsilon_2(\lambda_i)c_2].$$

Two independent wavelengths may identify two concentrations if the sensitivity matrix has sufficient rank and data quality; highly similar spectra lead to an ill-conditioned problem.

**Fluorescence:** quantum yield is the ratio of emitted fluorescence photons to absorbed excitation photons under appropriate definitions. Fluorescence intensity depends not just on concentration but on excitation, collection optics, quantum yield, quenching and inner-filter effects.

### Evidence and further reading

- Royal Society of Chemistry, *Analytical chemistry introductions*: https://edu.rsc.org/resources/collections/analytical-chemistry-introductions
- American Chemical Society, *Principles of Analytical Chemistry*: https://institute.acs.org/principles-analytical-chemistry.html
- NIST Chemistry WebBook, gas-phase UV/Vis spectral reference data: https://webbook.nist.gov/
- OpenStax, *Chemistry 2e*, optical spectroscopy and electronic structure chapters: https://openstax.org/books/chemistry-2e/pages/preface

### Questions to reason through

1. Why does absorbance increase linearly with distance in the Beer–Lambert model while transmittance does not?
2. Why can a cloudy sample give a misleading apparent absorbance?
3. Under what conditions can two wavelengths separate two absorbing analytes?
4. How could the same fluorescent molecule give different signals in two solvents?
5. What differs between evidence for an electronic transition and evidence for concentration?
