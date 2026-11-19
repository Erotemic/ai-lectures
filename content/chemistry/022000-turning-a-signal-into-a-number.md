# Turning a Signal into a Number: Calibration, Detection, and Uncertainty

<!-- BEGIN SPOKEN LECTURE -->

Imagine that a spectrometer displays an intensity of zero point two six zero. The screen is bright and the number has three decimal places. But how much substance does that represent? Without a model connecting the instrument's response to a known chemical quantity, the number is simply a signal. Analytical chemistry is the discipline of turning such signals into defensible statements about samples.

A detector responds to a physical event. Light passes through a liquid. Ions reach an electrode. A flame emits radiation. An electronic circuit collects charges. Often the detector produces a voltage, count rate, absorbance, or peak area. The quantity we want is different: concentration, mass fraction, amount of substance, or some structural property. Calibration supplies the relationship between them.

Suppose we make several solutions containing a known concentration of a colored compound. We measure their absorbances using the same optical path, wavelength and preparation as an unknown. As concentration increases, the response might increase approximately along a straight line over a useful working range. Plot detector response against known concentration, and use the resulting relationship to infer concentrations in other samples. The calibration is not an eternal property of the instrument. It depends on conditions and on the model used to connect the instrument response to the measurand.

Consider a hypothetical calibration in which response equals zero point zero one zero plus zero point zero five zero times concentration, with concentration expressed in milligrams per liter. An unknown gives a response of zero point two six zero. First subtract the intercept: zero point two five zero. Then divide by the slope, zero point zero five zero. The measured solution contains five milligrams per liter under this model. If that solution was prepared by making one volume of original sample into four volumes of diluted solution, the original concentration was twenty milligrams per liter, provided the analyte was conserved during dilution. The companion writes the calculation explicitly.

This looks almost too easy, until we ask where the line came from. The standards have uncertainties in their masses and volumes. The instrument has noise. The detector may drift while the sequence runs. The response could curve at high concentration, perhaps because absorption becomes too strong, the detector saturates, or the chemistry of the sample changes. A linear fit is not a right bestowed by a ruler laid across a graph. We use a straight line when experimental evidence supports that model over the intended range.

An intercept matters. Even a solution with no intentionally added analyte can yield a signal. There may be electronic offset, solvent absorption, reagent impurities, or contamination introduced during handling. A procedural blank follows the same chemical steps without the analyte, as far as that is possible. Measuring blanks helps expose the signal that should not be attributed to the target substance. Correcting for it can be appropriate, but the blank itself varies. Subtracting its mean does not make the uncertainty disappear.

A calibration curve can also fool us through its precision. Imagine five standards measured with a nearly perfect line, while every unknown contains a salt that suppresses detector response by a quarter. The standards are consistent. The fit is excellent. The reported unknown concentrations are still systematically low. That is a matrix effect. A method may deal with it by using matrix-matched standards, adding a known amount of analyte directly to portions of the sample, using a suitable internal standard, or separating interfering materials before detection. Each choice needs validation under the conditions of the actual measurement.

The standard-addition idea is particularly direct. Measure the sample as it is. Then measure matched portions after adding known increments of the analyte. If the original sample and the additions experience the same response suppression, the increase in signal can help infer the starting amount. But this argument depends on the added analyte behaving like what was already present and on the response model being appropriate. It is not a magical cure for every recovery problem.

An internal standard takes a different approach. A known amount of another substance is added to samples and calibration solutions. We measure the target response relative to the internal-standard response. If injection volume or instrument sensitivity fluctuates in ways that affect both similarly, the ratio can be more stable than the target response alone. But an internal standard is useful only if its behavior meaningfully tracks the sources of variation we want to correct. A chemically unrelated compound may not share an extraction loss or an ionization suppression. Isotopically labeled versions of the target are particularly useful in some mass-spectrometric methods because their chemical behavior is often closely matched, though not perfectly identical under all conditions.

Now consider the smallest amount we could detect. We measure a reagent blank repeatedly. The blank readings fluctuate because of noise and small variations. A tiny positive signal might lie within that background. We need a decision rule for separating plausible blank responses from evidence of analyte. The limit of detection is linked to a specified probability of distinguishing a sample response from a blank response under a stated procedure. A rule involving the mean blank plus a multiple of its standard deviation is a common simplification, but the multiplier and statistical assumptions matter.

Detection is not the same as reliable quantification. A feature can be distinguishable from a blank yet too variable to report a concentration with the uncertainty needed for a particular purpose. The limit of quantification is therefore tied to a fitness-for-purpose requirement, not one universal number dictated by nature. An instrument brochure that advertises an extraordinarily small detectable amount cannot by itself establish that the full field sampling method can measure environmental concentrations at that level.

It helps to distinguish precision from trueness. Precision concerns how closely repeated results agree under specified conditions. Trueness concerns closeness to a reference value in the sense of the mean systematic behavior of the method. A balance that consistently reports one hundred point five grams for a certified one-hundred-gram mass may be precise but biased. An instrument that averages correctly but swings wildly from run to run may have good average trueness and poor precision. Neither property alone guarantees a useful result.

Measurement uncertainty is not the same as having made a mistake. It is a quantified description of how uncertain the measurand value remains given the information and measurement model. Random variation contributes, but so can uncertainties in a calibration standard, incomplete recovery, a correction factor, a sample volume, or the sampling design. Depending on the problem, uncertainties can be combined using a model and, where justified, methods such as standard uncertainty propagation or simulation. Sources of uncertainty may be correlated, and treating them as independent when they are not can give the wrong result.

Imagine a solution concentration computed by dividing an estimated mass by a measured volume. If the mass and volume are independent, each with a small relative standard uncertainty, the relative uncertainty of the ratio is approximately the square root of the sum of their squared relative uncertainties. If each is two percent, the combined value is about two point eight percent. We do not add the two percentages mechanically, and we do not take the square root of squares if the errors are strongly correlated without including covariance.

Calibration also has a domain. A method validated between one and ten milligrams per liter has not automatically established accuracy at one thousand. Even when the curve extrapolates smoothly, the chemistry, detector response and interferences may not. Sometimes the correct move is to dilute the unknown into the calibrated range, then account for the dilution uncertainty. Sometimes dilution changes chemical equilibria or makes an analyte adsorb to the container, and that issue requires its own check.

Why measure a quality-control standard that is not used to construct the calibration line? Because an independent check can reveal a failure that an internally consistent calibration cannot. Why run a continuing calibration check halfway through a long sequence? Because instrument response can drift. Why include duplicate preparations and blanks? Because different parts of the procedure can go wrong in different ways. The goal is not to produce a ceremonial stack of checks. It is to make specific failure modes visible before we trust the number.

When a laboratory reports a result near a regulatory threshold, uncertainty becomes particularly consequential. Suppose the threshold is ten units and a measurement is ten point one with a relatively large uncertainty. It does not follow that the true value is definitely above ten, nor that the measurement is useless. A decision rule must specify how uncertainty enters compliance or classification. Different purposes can justify different rules, but the rule should be stated rather than smuggled into the number of decimal places printed in the report.

Return to the instrument displaying zero point two six zero. The signal becomes chemical evidence only after we know the calibration materials, blank behavior, applicable concentration range, matrix, sample preparation and uncertainty. The quality of the answer comes not from the apparent precision of the screen but from how well the entire inferential chain has been examined. The next question is what kinds of physical signals chemical instruments can produce, and why light is such a rich source of those signals.

<!-- END SPOKEN LECTURE -->

## Scientific companion: a small calibration model

A hypothetical response curve, valid for the stated range and matrix, is

$$S=a+bc,\qquad a=0.010,\quad b=0.050\ \mathrm{L/mg}.$$

If $S=0.260$, then $c=(0.260-0.010)/0.050=5.0\ \mathrm{mg/L}$. If the analyzed solution was diluted fourfold in a way that conserved analyte, the original contains $20\ \mathrm{mg/L}$. This is an illustrative dataset, not a real certified response curve.

**Basic uncertainty propagation.** For independent mass and volume measurements in $c=m/V$, with small relative standard uncertainties $u_m/m$ and $u_V/V$,

$$\left(\frac{u_c}{c}\right)^2\simeq\left(\frac{u_m}{m}\right)^2+\left(\frac{u_V}{V}\right)^2.$$

Two independent 2% components yield $\sqrt{0.02^2+0.02^2}=0.0283$ (2.83%). With correlated input uncertainties the covariance terms cannot be omitted.

**Detection versus quantification.** A simplified detection-threshold construction is $S_\mathrm{crit}=\bar S_\mathrm{blank}+k\,s_\mathrm{blank}$, but the distinction between a decision threshold, detection capability and acceptable quantification requires explicit statistical probabilities and method definition. Avoid presenting a universal three-sigma or ten-sigma rule as a law of nature.

**Recovery and matrix checks.** If a spike of 100 ng yields an incremental reported amount of 85 ng, apparent recovery is 85%; that result is evidence about the tested matrix and procedure, not proof that every native analyte has equal recovery.

### Evidence and further reading

- IUPAC Gold Book, *Limit of detection*: https://goldbook.iupac.org/terms/view/L03540
- IUPAC Gold Book, *Limit of quantification*: https://goldbook.iupac.org/terms/view/08022
- IUPAC Gold Book, *Performance characteristic of a measurement procedure*: https://goldbook.iupac.org/terms/view/08094
- Eurachem/CITAC, *Evaluation of Measurement Uncertainty from In-house Precision and Recovery Data* (2026): https://eurachem.org/index.php/publications/guides/gd-mupr
- NIST, *Metrological Traceability*: https://www.nist.gov/metrology/metrological-traceability

### Questions to reason through

1. Why does a visually perfect calibration line not guarantee an unbiased unknown result?
2. What distinguishes a blank, an external calibration standard, an internal standard and a spike?
3. How can a compound be detected but not acceptably quantified?
4. Why does reporting three decimal places not create three-decimal-place accuracy?
5. What changes when two uncertainty sources are correlated?
