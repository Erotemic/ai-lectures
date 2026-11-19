# The Weather Inside a Grid Cell: Clouds, Turbulence, and Tuning

<!-- BEGIN SPOKEN LECTURE -->

Imagine a summer afternoon over a broad plain. The ground is warm; moist air rises in small pockets; some pockets collapse before reaching a cloud base. One grows into a tall convective cloud and produces rain. Meanwhile, neighboring fields have different soil moisture and crops, and a town warms the air differently from the surrounding countryside. If your Earth-system model has an atmospheric cell fifty kilometers across, much of this activity is smaller than the cell. Yet those small processes decide how much water falls, how much sunlight is reflected, and how quickly heat reaches higher layers of air. What should the model do with weather it cannot see?

This problem is called parameterization. The word can sound like an admission that scientists have replaced physics with guessed numbers. What they have actually done is confront a mathematical fact: the average of a nonlinear process is generally not what you get by applying that process to the average conditions. A cell with half its area occupied by vigorous rain clouds is not physically equivalent to a cell filled everywhere with a weak drizzle. Both might have the same mean moisture, but their vertical heat transport, precipitation, and radiation can be very different.

A model must represent these differences somehow. Its dynamical core moves mass, energy, and momentum across the resolved grid. A parameterization estimates the net influence of smaller-scale processes on that resolved state. It might calculate how strongly clouds heat their environment through condensation, how turbulence mixes momentum near the surface, or how droplets and ice crystals convert into rain and snow. The parameterization is not necessarily a separate law of nature. It is an approximation to the consequences of laws playing out at scales not directly calculated.

Consider a parcel of moist air that rises. Pressure decreases with height, the air expands and cools, and vapor may condense. Condensation releases latent heat, helping the parcel remain buoyant. The ascending cloud can carry heat and moisture upward, while surrounding air slowly sinks. The temperature and humidity of the entire cell can change even if the model does not resolve the individual ascending towers. An early influential attempt to describe the interaction of ensembles of cumulus clouds with their large-scale environment was developed by Akio Arakawa and Wayne Schubert at the University of California, Los Angeles, and published in 1974. Their framework mattered because it treated convection as coupled to the surrounding column's heat and moisture budgets, rather than as isolated cloud objects pasted onto a forecast.

Different convective schemes make different assumptions about the state of the cloud population and how it responds to instability. Some use quantities related to buoyant energy available to convection; others focus on moisture convergence, entrainment, mass flux, or convective organization. There is no universally reliable shortcut. A cloud entrains surrounding air, which may dilute its buoyancy. It detrains some of its contents into the environment. It converts vapor to liquid and ice and eventually precipitation, perhaps evaporating rain on the way down. The combined effects feed back into the atmosphere that produced the clouds. A responsible scheme must return those transfers to the resolved budgets in a consistent way.

There is a second cloud problem: the radiative effect. A low, bright cloud can reflect incoming sunlight and cool the surface below. A high, thin cloud can have a different balance of shortwave reflection and infrared trapping. Even the shape and arrangement of clouds matter because radiation travels through a three-dimensional world. Model radiation calculations often describe the vertical optical properties of fractions of a grid cell; they cannot usually trace every photon through the exact cloud geometry. Cloud coverage, droplet sizes, ice habits, and overlap among layers become approximations. Small errors in these choices can affect the planetary energy budget and the response of clouds to warming.

Now take a completely different subgrid phenomenon: turbulence above the land. On a sunny afternoon the air close to the ground may be heated and mixed vigorously. At night it can become stably stratified, with cooler air trapped below warmer air. The mixing rate controls how rapidly the surface exchanges heat, vapor, and momentum with the atmosphere. A model with a layer thicker than the actual turbulent structures needs closure relationships for that transport. In effect it needs a rule for how unresolved eddies move things across the boundaries of the resolved layer.

These approximations are unavoidable in many present-day global models, but they are not all the same kind. Some processes have strong physical constraints that can be written into a scheme. Others require empirical coefficients estimated from field experiments, satellite observations, laboratory measurements, or high-resolution simulations. A modeler may know the direction of a transfer well but have difficulty estimating its size. The scientific work is to combine conservation, theory, observations, and independent tests—not merely to turn a dial until the final map looks pleasing.

That raises the sensitive word tuning. Suppose a model produces too much reflected sunlight in the tropics because its low clouds are too extensive or too bright. The modeler can investigate the cloud scheme and adjust parameters controlling droplet properties or turbulent mixing within physically defensible ranges. This may reduce the top-of-atmosphere radiation bias. But a change that improves one diagnostic can worsen precipitation, boundary-layer structure, or regional temperature. Two compensating errors can even give an apparently excellent global energy balance: too many bright clouds in one region may offset too few in another. A single good average cannot establish that the underlying processes are right.

In 2017, Frédéric Hourdin and a large group of colleagues published a review titled The Art and Science of Climate Model Tuning. Their discussion is helpful because it refuses two simplistic views. Tuning is neither inherently illegitimate nor a magical method that validates a climate model. Scientists must make choices about uncertain parameters. The credibility of those choices depends on transparent targets, physically plausible parameter ranges, documentation, and evaluation on evidence that was not simply used to set the parameters in the first place.

Think of tuning a violin. A well-tuned string does not guarantee that the instrument will sound good in every hall, and tightening one string will not repair a broken bridge. A climate model calibrated to reproduce global radiation balance has not thereby demonstrated skill at regional monsoon rainfall, cloud feedback, or the extremes of precipitation. Yet uncertain physical coefficients still need to be estimated. Estimating uncertain coefficients is part of modeling, but independent tests must then establish whether the tuned model can explain phenomena it was not calibrated to reproduce.

There is a further complication when the grid becomes finer. At sufficiently fine resolution, some convective systems previously represented only statistically can begin to be simulated explicitly. But a grid that captures some large convective motions might still miss smaller clouds, turbulent mixing, and droplet microphysics. In the so-called gray zone, a traditional parameterization may assume that all convection is unresolved while the numerical solver is already representing part of it. If both try to transport the same heat and moisture, the model can double-count. If the old scheme is simply removed, important smaller-scale transport may be lost. A scale-aware method adjusts the unresolved contribution as the resolved motions change.

The same principle applies to ocean eddies. A coarse ocean model cannot represent every swirling current. Such eddies transport heat and salt and help shape larger circulation. Parameterizations try to describe their aggregate effects. Higher resolution can permit more eddies to emerge, but that changes how transport should be split between resolved and unresolved motions. Land-surface models make their own choices: how plant roots take up water, how vegetation controls evaporation, how snow hides or exposes the ground, and how soil heat and moisture move among layers.

Another option is to use a hierarchy of models. A large-eddy simulation resolves energetic turbulent motions within a limited domain and models the remaining smallest scales. A cloud-resolving model can explore the structure of convection at much finer scales than a standard global climate model, though it too has unresolved physics and practical domain and duration limits. Observations can evaluate the behavior of these detailed models. Scientists may then use the resulting statistics and mechanisms to design better global parameterizations. This exchange between high-resolution process models and global models is an active area of research, not a one-way march toward replacing every approximation with brute-force computation.

What about artificial intelligence? A statistical or machine-learned surrogate can be trained to imitate expensive small-scale simulations or a conventional physical parameterization. That can save computation or discover patterns missing in older schemes. But a surrogate inherits limits from its training distribution. If it predicts transfers that violate global water or energy accounting, it can slowly distort the simulated climate. If future conditions move beyond its training experience, apparent accuracy on historical samples may not guarantee reliable behavior. Conservation constraints, stability tests, explainable diagnostics, and evaluation under shifted conditions remain important no matter how the surrogate was constructed.

A scientist assessing a cloud scheme therefore asks much richer questions than 'Does it rain enough?' Is the timing of afternoon convection correct? Does the rain come as too many weak events or too few intense ones? Is surface evaporation physically plausible? Does heating occur at the right heights? Does the model represent the broad patterns of reflected sunlight observed by satellites? Does a change in sea-surface temperature produce the expected changes in cloud organization, and which of those responses are actually well constrained? A scheme may score well on one of these and poorly on another. That is diagnostic information, not simply a pass or fail.

An important distinction is between model error and variability. On one simulated Tuesday a storm appears over the wrong valley. That alone is not necessarily a flaw in the modeled climate if the run did not start from an accurate initial state. Over many seasons, however, a persistent shift in the rain belt or systematically mistimed daily thunderstorms may reveal a structural bias. To evaluate climate, researchers compare distributions, seasonal cycles, radiation fluxes, and process relationships as well as individual weather forecasts. The relevant metric must match the scientific question.

Return to the summer plain. We cannot fit every rising bubble of warm air into a global grid. But we can ask what those bubbles accomplish together, estimate their transfers from physics and evidence, and make the model's choices inspectable. The great danger is not that climate models approximate small processes. Every quantitative science uses approximations. The danger is forgetting which processes are approximated, which observations informed those approximations, and which predictions remain genuinely independent tests. A good parameterization is a carefully defended bridge from unseen small-scale activity to visible large-scale consequences.

<!-- END SPOKEN LECTURE -->

## Scientific companion: subgrid closure and parameter estimation

### The average of a nonlinear process

For nonlinear $f$, in general $\mathbb E[f(X)]\neq f(\mathbb E[X])$. A 50% cloudy grid cell cannot in general be replaced by a uniformly half-cloudy column without assumptions about radiative transfer and subgrid heterogeneity. The required closure depends on which effects are unresolved.

### Physical bookkeeping

A convection scheme might apply linked tendencies to temperature, water vapor, cloud water, precipitation and momentum. Condensation and evaporation redistribute water between phases; latent heating must accompany the phase transitions. Global sums and conservation residuals are separate diagnostics from regional precipitation skill.

### Tuning versus evaluation

| Step | Responsible practice | Failure to avoid |
| --- | --- | --- |
| Develop scheme | Derive and justify closure assumptions | Treat free coefficients as direct observations |
| Estimate parameters | Specify observations and physically plausible priors | Choose values after inspecting every future validation target |
| Compare configurations | Check multiple fields and known tradeoffs | Improve global mean by canceling regional errors |
| Test out of sample | Try distinct years, regions, independent process observations | Rebrand calibration fit as independent forecast skill |
| Increase resolution | Re-evaluate resolved/unresolved split | Double-count or omit transport in the gray zone |

### Sources and further reading

- Arakawa & Schubert (1974), *Interaction of a Cumulus Cloud Ensemble with the Large-Scale Environment, Part I*. https://doi.org/10.1175/1520-0469(1974)031%3C0674:IOACCE%3E2.0.CO;2
- Hourdin et al. (2017), *The Art and Science of Climate Model Tuning*. https://doi.org/10.1175/BAMS-D-15-00135.1
- IPCC AR6 WGI, Chapter 1, §1.5.3 (model resolution, parameterization, structural choices). https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-1/
- Ullrich et al. (2025), *Recommendations for Comprehensive and Independent Evaluation of Machine Learning-Based Earth System Models*. https://doi.org/10.1029/2024JH000496

### Questions

1. Why would a uniform rain rate fail to mimic a cell containing occasional intense convection?
2. How can a parameter change improve the global radiation average while degrading the modeled climate?
3. What is 'gray-zone' double-counting when model resolution increases?
4. How would you construct an independent test of a cloud parameterization calibrated to satellite reflectance?
