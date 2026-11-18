# A Forecast Begins with a Guess: Observations, Data Assimilation, and Reanalysis

<!-- BEGIN SPOKEN LECTURE -->

At this moment the atmosphere has a temperature at every point, a pressure, a wind, a humidity, and an astonishingly detailed structure of clouds and turbulence. Nobody knows that complete state. A balloon measures a thin path through the air. A satellite measures radiation received from a broad field of view. Weather stations are clustered on land and sparse in many remote regions. Aircraft follow particular routes, and ocean buoys occupy a limited set of positions. Yet a modern forecast must begin with a globally coherent set of numbers. Where do those numbers come from?

They begin with a guess informed by physics. Run the model for a few hours from the previous analysis and you have a short-range forecast of the present. This is called a background or first guess. It is not pure speculation; it contains the history of previous observations carried forward through the model's equations. But it has errors. Fresh observations also have errors. Data assimilation is the disciplined act of combining them to estimate the current state, with attention to their uncertainties and physical relationships.

Let's start with a one-number example because the logic is easier to hear. Imagine you have a short-range model estimate of a city's air temperature: nineteen degrees Celsius. You think the forecast's uncertainty is about one degree. A new thermometer says seventeen degrees, but you have reason to assign that measurement an uncertainty of about two degrees, perhaps because of poor exposure or because it samples only part of the area represented by the model. If the errors are unbiased, independent, and approximately Gaussian, the best linear variance-weighted compromise is closer to the more precise estimate. It is eighteen point six degrees, not seventeen or the simple average of eighteen. The data do not replace the model. They correct it by an amount justified by their relative precision.

That number comes from variance, not just the quoted uncertainty widths. The model variance is one squared degree. The observation variance is four squared degrees. Their inverse-variance weights give four parts to the model estimate and one part to the observation. Four times nineteen plus one times seventeen, divided by five, yields eighteen point six. If the thermometer were much more precise than the background, the result would move toward seventeen. If it were much less trustworthy, the background would barely move. Real assimilation is vastly more complicated, but this little calculation captures why there is no sensible universal rule to overwrite a simulated value whenever an instrument reports something different.

There is a second problem: the observation may not measure the model variable at all. A satellite radiometer records radiation at selected wavelengths and viewing angles. To compare its measurement with a model, scientists need an observation operator, a model of how the atmosphere's temperature, humidity, clouds, and surface properties would produce that radiance. An observing instrument may be sensitive to several atmospheric layers rather than one neat height. A model grid cell may represent an average over a large area, while an instrument samples a point. Representativeness error arises even when the instrument itself is perfectly calibrated. A direct numerical comparison without accounting for these distinctions would be misleading.

Now suppose a satellite suggests that a broad region of the upper atmosphere is warmer than the short forecast predicted. Simply raising one grid cell's temperature may leave pressure and wind fields inconsistent with the dynamical relationships. A good assimilation method uses statistical relationships among errors and variables to spread adjustments in a physically plausible way. A temperature observation may affect estimated winds, pressure, and moisture depending on how the background-error covariance is represented. The system tries to gain information from observations without breaking the evolving state into unrelated patches.

The simplest assimilation methods are not always the ones in use. An older approach called objective analysis blended nearby measurements into a background field using spatial weights. Modern operational centers employ more elaborate variational and ensemble methods. In three-dimensional variational assimilation, often abbreviated three-D var, one seeks a state that balances agreement with observations against departure from the background, weighted by assumed errors. In four-dimensional variational assimilation, four-D var, the comparison extends across a time window. The system changes the state at the window's start, runs the model forward, and evaluates agreement with observations taken at different times within that window.

The idea of four-D var is subtle but compelling. Imagine the observed position of a storm at midnight, again at three in the morning, and again at six. Adjusting the initial atmospheric state should make a single physically evolving trajectory fit all three observations better. ECMWF introduced operational four-D var in 1997 and has developed that approach further. The computation involves an optimization problem and repeated use of a forecast model and representations of how changes in the initial state affect later observations. It is not a hand adjustment of every map point after the fact.

Another family of methods employs ensembles. Start with several plausible background states, each a little different. Advance them with a model and see how their differences evolve. The ensemble provides information about where the background is uncertain and which variables' errors tend to move together. A Kalman-filter-style update can use that flow-dependent covariance to adjust the state. Practical ensemble Kalman filters need approximations because the atmosphere has enormously more variables than the number of ensemble members. For instance, spurious long-distance correlations can arise from small ensemble size, so methods often localize the influence of observations. Hybrid systems combine aspects of ensemble estimates with variational optimization.

This is an estimation problem, not a magic recovery of the true atmosphere. No instrument samples every turbulent eddy; some satellite channels see clouds poorly; some biases are persistent; uncertainty statistics are only approximations. The analysis is a best supported state estimate conditional on the available observations and model system. An analysis can be excellent at large-scale wind and temperature while providing a much more model-dependent estimate of precipitation, soil moisture, or cloud microphysics. The output grid is full, but that does not make the information equally observed everywhere.

This distinction becomes especially important when we look backward rather than forward. Reanalysis takes archived observations, a consistent model framework, and a data-assimilation system to reconstruct past weather and climate fields. ECMWF's ERA5 is one such global reanalysis, providing fields over decades with hourly temporal resolution. Its estimates are tremendously useful because they put scattered measurements into a dynamically connected framework and provide variables that were never observed directly everywhere. But a reanalysis temperature at a particular grid point in 1945 is not the same thing as a thermometer that sat there in 1945.

Reanalysis quality changes with the observing system. In some eras and regions, the data are abundant. In others, the model must fill more gaps. Satellite data transformed the global observing network; earlier periods lack the same satellite coverage. Changes in instruments, observing practices, and the types of assimilated data can introduce artificial changes in reanalysis estimates. Scientists therefore examine observation coverage, system details, and uncertainty when studying trends. They also compare with independent instrumental records, satellite products, and other reanalyses. A continuous-looking map is not evidence of continuous observational coverage.

Suppose you download global monthly rainfall from a reanalysis and draw a fifty-year trend. Precipitation is often a model-produced quantity influenced by the assimilated state, not a direct global sum of rain gauges. Some regions and periods may be well constrained by observations, others less so. The trend can reflect genuine climate change, changes in atmospheric circulation, numerical-model biases, or changes in the observing system. That does not mean the dataset is worthless. It means the correct interpretation depends on which field you chose and how strongly observations constrain it.

Data assimilation also helps us understand the difference between a weather forecast and a climate projection. A weather forecast depends critically on the initial state, because small errors in that state can grow. An analysis gives the model the best available starting point. Many climate-projection experiments, by contrast, ask how statistical features of climate change when external conditions change. For that question the exact phase of tomorrow's storm may matter far less than greenhouse-gas concentrations, solar forcing, land use, and the coupled model's response. Some seasonal and decadal prediction systems deliberately initialize ocean and atmosphere states because their memory can provide information on those shorter prediction horizons. The terms 'forecast' and 'projection' therefore refer to different prediction questions, not to a simple ranking of model accuracy.

What counts as a successful assimilation? One check is the innovation: observation minus background prediction, before the new observation has been incorporated. Another is the residual between observation and the resulting analysis, interpreted with appropriate dependence. Yet a tiny residual is not automatically excellent; a system that overfits measurement noise can produce an unstable or inconsistent analysis. Independent forecasts launched from the analysis offer a stronger test. If the new analysis produces better predictions of withheld observations, the assimilation has made an improvement that matters beyond fitting data already seen.

Data assimilation can introduce its own budget issues. A correction to temperature, humidity, or salinity may improve agreement with observations while creating a local or global change in an otherwise conserved quantity. Operational systems use techniques to reduce such inconsistencies, but an analysis increment is not an ordinary physical flux from one grid cell to another. In climate applications, examining the increments can help reveal persistent model biases. It is a reminder that the best estimate of the present need not be an unconstrained free-running climate solution.

A final example returns us to the Pacific Ocean. The state of the equatorial thermocline matters for the development of El Niño. A forecast initialized with only sea-surface temperature may miss important subsurface heat content. Ocean profiles, satellite sea level, winds, and other measurements constrain different aspects of the evolving state. Assimilation allows an ocean model to combine them into a consistent starting estimate. If the observing network is sparse, or the model represents ocean dynamics poorly, initial uncertainty remains and forecasts must express it. This is not a weakness unique to ENSO; it is a general feature of predicting a system whose complete state can never be observed.

So the forecast begins with a guess, but it does not end with one. Physics brings the previous observations forward; new measurements correct that provisional state; uncertainty determines how far the corrections should reach. When scientists later build a reanalysis, they repeat this process through the historical record using a coherent assimilation framework. The product is neither an ordinary observation nor a free simulation. It is an interpretation of evidence through a physical model. To use it well, we must ask how the observations entered, which fields they constrain, and what independent evidence can still test the answer.

<!-- END SPOKEN LECTURE -->

## Scientific companion: estimating an atmospheric state

### Scalar variance-weighted update

Let background $x_b=19\,^{\circ}\mathrm C$ with variance $\sigma_b^2=1$ and an independent observation $y=17\,^{\circ}\mathrm C$ with variance $\sigma_o^2=4$. For unbiased Gaussian errors,

$$x_a=\frac{\sigma_o^{-2}y+\sigma_b^{-2}x_b}{\sigma_o^{-2}+\sigma_b^{-2}}=\frac{17/4+19}{1/4+1}=18.6\,^{\circ}\mathrm C.$$

Equivalently $x_a=x_b+K(y-x_b)$ with gain $K=\sigma_b^2/(\sigma_b^2+\sigma_o^2)=0.2$. The assumptions are not optional; observation error and representativeness can be correlated or biased in the real system.

### A schematic variational cost

$$J(x)=\tfrac12(x-x_b)^TB^{-1}(x-x_b)+\tfrac12[y-H(x)]^TR^{-1}[y-H(x)].$$

$B$ and $R$ represent assumed background and observation-error covariances, respectively, and $H$ maps the model state to quantities an instrument would observe. Four-dimensional variational systems introduce a model evolution mapping over the observation time window. Practical operational implementations are considerably richer, and biases and error correlations matter.

### Distinguish three data products

| Product | Primary inference | Typical limitation |
| --- | --- | --- |
| Direct observation | What an instrument sampled at a place, time and viewing geometry | Spatial coverage, instrument biases, sampling |
| Analysis / reanalysis | Model-consistent estimate conditioned on observations | Depends on forecast model, assimilation, error statistics and changing observing network |
| Free-running climate projection | Response of climate distribution to specified forcing or scenario | Not synchronized with a given day's realized weather; structural and scenario uncertainties |

### Sources and further reading

- ECMWF (2025), *Fact sheet: Earth system data assimilation*. https://www.ecmwf.int/en/about/media-centre/focus/2025/fact-sheet-earth-system-data-assimilation
- ECMWF, *Forecast User Guide, Section 2A.6: Model Data Assimilation, 4D-Var*. https://confluence.ecmwf.int/spaces/FUG/pages/673550616/Section+2A.6+Model+Data+Assimilation+4D-Var
- ECMWF, *Complete ERA5 global atmospheric reanalysis*. https://www.ecmwf.int/en/forecasts/datasets/complete-era5-global-atmospheric-reanalysis
- Copernicus C3S, *Climate reanalysis*. https://climate.copernicus.eu/climate-reanalysis

### Questions

1. Why is an instrument reading not automatically the appropriate estimate of an entire model grid cell?
2. What produces the value 18.6 degrees in the worked analysis example, and what assumptions does it require?
3. Why is an ERA5 grid cell not equivalent to a historical station measurement?
4. What kind of independent prediction test could detect an assimilation system that simply overfits observations?
