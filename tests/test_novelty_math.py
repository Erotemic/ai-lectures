"""Numerical transport examples and shared notation regression checks."""
import math
import pytest
from dkvis.novelty_math import optimal_phase_three_halves

def _phase_power(theta: float, delta: float) -> float:
    return (2.0 * math.sin((theta + delta) / 2)) ** 1.5 + (
        2.0 * math.sin((theta - delta) / 2)
    ) ** 1.5


def test_three_halves_phase_avoids_out_of_domain_acos():
    for degrees in (0, 25, 45, 65, math.degrees(math.acos(1 / 3))):
        assert optimal_phase_three_halves(math.radians(degrees)) == 0.0


def test_three_halves_phase_supercritical_is_global_scalar_minimum():
    theta = math.radians(80.0)
    minimum_phase = optimal_phase_three_halves(theta)
    assert 0 < minimum_phase < theta
    cost = _phase_power(theta, minimum_phase)
    for i in range(1001):
        assert cost <= _phase_power(theta, theta * i / 1000) + 1e-9


def test_three_halves_phase_rejects_invalid_angles():
    for theta in (-0.1, math.pi, math.nan, math.inf):
        with pytest.raises(ValueError):
            optimal_phase_three_halves(theta)


def test_smoothed_two_by_two_example_matches_exact_formula():
    from dkvis.novelty_math import (
        canonical_smoothed_cost, optimal_smoothed_cost,
        optimal_smoothed_phase, smoothed_cutoff, smoothing_radius,
    )

    tau = 1.0
    eta = smoothing_radius(tau)
    threshold = smoothed_cutoff(tau)
    assert math.isclose(eta, (1 + math.sqrt(5)) / 2, abs_tol=1e-12)
    assert math.isclose(math.degrees(threshold), 67.54448480141833, abs_tol=1e-8)
    low = math.radians(45)
    high = math.radians(80)
    assert low < threshold < high
    assert optimal_smoothed_phase(tau, low) == 0
    assert math.isclose(math.degrees(optimal_smoothed_phase(tau, high)), 62.95971681332988, abs_tol=1e-8)
    assert math.isclose(optimal_smoothed_cost(tau, low), canonical_smoothed_cost(tau, low), abs_tol=1e-10)
    assert math.isclose(optimal_smoothed_cost(tau, low), 0.5185602534995306, abs_tol=1e-8)
    assert math.isclose(optimal_smoothed_cost(tau, high), 1.1869048335163286, abs_tol=1e-8)
    assert math.isclose(canonical_smoothed_cost(tau, high), 1.257424531537846, abs_tol=1e-8)
    assert optimal_smoothed_cost(tau, high) < canonical_smoothed_cost(tau, high)
    assert math.sin(low) < math.sqrt(1 - eta ** -4) < math.sin(high)


def test_critical_phase_gap_is_fourth_order_not_second():
    from dkvis.novelty_math import critical_phase_excess

    tau = 1.0
    q1, q2, q3 = (critical_phase_excess(tau, t) for t in (0.2, 0.1, 0.05))
    assert q1 > q2 > q3 > 0
    # Halving the phase asymptotically divides the excess by sixteen.
    assert abs(q1 / q2 - 16) < 0.1
    assert abs(q2 / q3 - 16) < 0.1
    assert q3 / 0.05 ** 2 < q2 / 0.1 ** 2


def test_smoothed_scalar_illustrations_reject_bad_inputs():
    from dkvis.novelty_math import (
        canonical_smoothed_cost, optimal_smoothed_cost,
        optimal_smoothed_phase, smoothing_radius,
    )

    for tau in (-1, 0, float('nan'), float('inf')):
        with pytest.raises(ValueError):
            smoothing_radius(tau)
    for theta in (-0.1, math.pi, float('nan'), float('inf')):
        with pytest.raises(ValueError):
            canonical_smoothed_cost(1, theta)
        with pytest.raises(ValueError):
            optimal_smoothed_cost(1, theta)
        with pytest.raises(ValueError):
            optimal_smoothed_phase(1, theta)


def test_transport_roles_match_manuscript_without_changing_legacy_keys():
    from dkvis.notation import SYMBOLS, concept_color
    from dkvis.palette import PALETTE

    assert SYMBOLS["Usource"] == (r"U", "trial")
    assert SYMBOLS["Vtarget"] == (r"V", "wanted")
    assert SYMBOLS["ProjSource"] == (r"P_U", "trial")
    assert SYMBOLS["ProjTarget"] == (r"P_V", "wanted")
    assert concept_color("Usource") == PALETTE["TRIAL"]
    assert concept_color("Vtarget") == PALETTE["WANTED"]
    # Historical sine-theta slides use U exact and V trial; keep them stable.
    assert SYMBOLS["U"][1] == "wanted"
    assert SYMBOLS["V"][1] == "trial"


def test_unrestricted_schatten_two_angle_example_matches_verified_formula():
    from dkvis.novelty_math import (
        schatten_two_angle_example_three_halves,
        schatten_phase_power_three_halves,
    )
    z = schatten_two_angle_example_three_halves()
    assert math.isclose(z["cutoff_deg"], 70.52877936550931, abs_tol=1e-8)
    assert z["low_phase_deg"] == 0.0
    assert math.isclose(z["high_phase_deg"], 74.57097698955464, abs_tol=1e-8)
    assert math.isclose(z["canonical_sum"], 4.254419090242005, abs_tol=1e-8)
    assert math.isclose(z["global_sum"], 4.093350305605767, abs_tol=1e-8)
    assert z["global_sum"] < z["canonical_sum"]
    theta = math.radians(80)
    attained = schatten_phase_power_three_halves(theta, math.radians(z["high_phase_deg"]))
    for k in range(501):
        assert attained <= schatten_phase_power_three_halves(theta, theta * k / 500) + 1e-9
    for theta, delta in [(-1, 0), (math.pi, 0), (0.5, -0.1), (0.5, 0.6)]:
        with pytest.raises(ValueError):
            schatten_phase_power_three_halves(theta, delta)


def test_simple_active_schatten_sign_families():
    from dkvis.novelty_math import (
        schatten_simple_active_signs_three_halves,
        schatten_signed_phase_power_three_halves,
    )
    z = schatten_simple_active_signs_three_halves()
    assert z["angles_deg"] == (75.0, 80.0)
    assert len(z["choices"]) == 4
    assert len(set(z["choices"])) == 4
    assert min(z["phases_deg"]) > 0
    assert max(z["costs"]) - min(z["costs"]) < 1e-12
    assert math.isclose(z["costs"][0], 5.398844412803351, abs_tol=1e-10)
    for (a, b), cost in zip(z["choices"], z["costs"]):
        assert math.isclose(cost,
            schatten_signed_phase_power_three_halves(math.radians(75), a)
            + schatten_signed_phase_power_three_halves(math.radians(80), b),
            abs_tol=1e-12)
    for phase in (-math.pi, math.pi, float('nan'), float('inf')):
        with pytest.raises(ValueError):
            schatten_signed_phase_power_three_halves(math.radians(80), phase)
