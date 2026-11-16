# 006000 — Fits, Clearances, and Thermal Expansion

**Track:** Mechanical Systems and Repair. **Background:** Bearings, friction, lubrication, and mechanical loads. **Purpose:** understand controlled gaps, interference, tolerance stacks, and thermal movement.

<!-- BEGIN SPOKEN LECTURE -->

# A gap can be a design feature

A metal shaft passes through a hole. If the hole is slightly larger, the shaft can slide or rotate. If they are nearly the same size, the result depends on manufacturing variation and temperature. If the shaft is larger, an interference fit may hold the parts tightly together. All three assemblies can be correct or incorrect depending on what the designer intended.

Mechanics is full of purposeful gaps: a bearing needs the right internal clearance, a valve stem needs space to move while remaining sealed, and two gears need backlash so their teeth do not jam. A gap is not necessarily sloppy workmanship. Conversely, two parts that feel perfectly tight on a bench can seize when they warm up or deform under load.

## Nominal dimension is not actual dimension

Suppose a drawing calls for a shaft of ten millimeters diameter and a hole of ten millimeters. These are nominal descriptions. Real parts are manufactured within tolerances. A shaft may be slightly above or below its nominal value, and the hole has its own range. The possible clearance is the hole diameter minus the shaft diameter. If the tolerance ranges overlap, some assemblies may be loose and others tight even though every individual piece passes inspection.

A fit therefore requires two compatible tolerance ranges, not merely matching nominal sizes. In a clearance fit, the smallest permitted hole still exceeds the largest permitted shaft. In an interference fit, the largest permitted hole is still smaller than the smallest permitted shaft. Transition fits occupy the territory where either outcome may occur, depending on the actual pair.

A machinist can measure one shaft and one hole, but also needs to know their shape. A slightly oval hole may admit a pin at one angle while binding at another. A tapered bore may accept an insertion and then seize. Surface roughness, burrs, and damage affect contact even if a simple caliper reading appears acceptable. Geometry and finish participate in the fit.

## Temperature moves the dimensions

Most common engineering metals expand when heated. For a sufficiently small temperature change, a useful approximation is change in length equals original length multiplied by the coefficient of thermal expansion and by the temperature change. The same principle applies approximately to diameters.

Take a steel ring with a bore diameter of fifty millimeters. If its temperature rises by fifty degrees Celsius, and we use a steel expansion coefficient of roughly twelve millionths per degree Celsius, the bore diameter increases by about thirty thousandths of a millimeter. That is a small number to the eye, but it can be important in a precision fit. Different metals have different coefficients. An aluminum housing and a steel shaft or bearing can change their relative fit as the assembly heats.

This leads to a practical surprise. Heating a ring usually enlarges its hole; it does not squeeze the hole closed. That observation underlies some controlled thermal assembly methods. But it also shows why the fit at a room-temperature inspection may not be the fit at operating temperature. Even a temporary warm spot or an uneven thermal gradient can affect clearances and alignment.

## A bearing wants the right freedom

A rolling bearing has internal clearances that change when rings are pressed into the shaft or housing. Interference can expand the inner ring or compress the outer ring, reducing some internal clearance. Running temperature, load and differential expansion change it again. Too little operating clearance can increase friction and heat; too much can reduce precision and contribute to vibration or load concentration.

It is therefore possible to damage a bearing by installing an otherwise correct bearing with an inappropriate shaft fit. The mechanic who blames the lubricant alone may miss the true cause. Likewise, a seal needs appropriate contact pressure and shaft finish. A very tight seal can overheat or wear quickly; a loose seal can leak. Mechanical quality frequently means choosing a narrow operating range between two failure modes.

The surrounding assembly must also permit expected movement. A long metal rail attached rigidly at both ends can develop force from expansion and contraction. A sliding support, expansion joint or compliant coupling may be needed. Engineers often choose one locating bearing to fix a shaft axially and another arrangement to accommodate thermal growth. Without that freedom, temperature change can preload the structure in ways nobody intended.

## Why tolerance stacks matter

Imagine a lid supported by three machined spacers. Each spacer is manufactured within an allowed range. If the critical gap depends on several dimensions added or subtracted together, their variations accumulate. A design that looks generous when every dimension takes its nominal value can become too tight in an unfavorable combination. Inspection should identify which measurements control the actual function rather than simply checking that every part is close to a printed number.

Tolerance does not mean permissible carelessness. It is a defined range that connects what can be manufactured to what will work. A sensible tolerance is tight enough to protect function and loose enough to be produced reliably. Specifying extreme precision everywhere adds cost without necessarily improving the mechanism.

## Diagnosing a fit problem

A device that binds only after warming suggests thermal expansion, loss of clearance, misalignment, or lubricant changes. A joint that rattles after a few months may have wear at a bearing or hole, or it may have had excessive clearance from the start. Measure at a controlled temperature, look for asymmetric wear, inspect surfaces for fretting, and compare with the intended arrangement. Do not file or grind away material until you know whether it was meant to provide a controlled interference.

The lesson is that an assembly is never just a collection of dimensions. It is an arrangement of freedoms and constraints that changes with load and temperature. A designed gap can be as important as a designed contact, and a fraction of a millimeter can decide which one you have.

<!-- END SPOKEN LECTURE -->

## Technical companion (non-spoken)

### Thermal expansion calculation

For `L = 50 mm`, `alpha = 12 × 10^-6 / K`, and `ΔT = 50 K`, a steel dimension changes approximately `ΔL = alpha × L × ΔT = 0.030 mm`. This is an illustrative coefficient, not a specification for all steel grades or assemblies.

### Fit exercise

Let a hole range from 10.010 to 10.030 mm and a shaft from 9.980 to 10.000 mm. The clearance ranges from 0.010 to 0.050 mm. Ask how that range changes if the shaft is steel and housing aluminum at elevated temperature.

**Review boundary:** Bearing, seal, press-fit and thermal-assembly decisions require manufacturer fit tables, material grades, temperature range, and proper measurement technique.

## Selected reading and evidence records (non-spoken)

- `openstax-thermal` — [OpenStax College Physics 2e, §13.2: Thermal Expansion of Solids and Liquids](https://openstax.org/books/college-physics-2e/pages/13-2-thermal-expansion-of-solids-and-liquids). Linear thermal expansion, representative material coefficients, and holes expanding with heating.
- `skf-highspeed-bearings` — [SKF Evolution, Bearings for High Speed Operations](https://evolution.skf.com/us/bearings-for-high-speed-operations/). Differential operating temperature, interference fit, clearance and bearing preload.
