"""Behavioral evidence for personalized prerequisite planning."""

from copy import deepcopy
import random

import pytest

from ailectures.graph import build_learning_map
from ailectures.learning_plan import build_learning_plan


def graph(keys, edges=(), **extra):
    result = dict(
        generation="test-revision",
        nodes={key: dict(id=key, kind="lecture", title="Title " + key,
                         url="/lectures/" + key, available=True,
                         prerequisites_reviewed=True) for key in keys},
        relationships=[dict(from_=source, to=target, type=kind, reasons=["Authored reason"])
                       for source, target, kind in edges],
        component_lectures={},
    )
    for edge in result["relationships"]:
        edge["from"] = edge.pop("from_")
    result.update(extra)
    return result


def ids(plan):
    return [row["id"] for row in plan["steps"]]


def test_prerequisite_direction_explanations_and_goal_closure():
    data = graph(["A", "B", "C", "unrelated"], [
        ("C", "B", "hard_depends_on"), ("B", "A", "hard_depends_on")])
    plan = build_learning_plan(data, {"goals": ["C"]})
    assert plan["valid"] and ids(plan) == ["A", "B", "C"]
    assert [step["role"] for step in plan["steps"]] == ["prerequisite", "prerequisite", "goal"]
    assert plan["steps"][0]["required_by"] == ["C"]
    assert plan["steps"][1]["depends_on"] == ["A"]
    assert "Authored reason" in plan["steps"][0]["reasons"]
    assert plan["generation"] == "test-revision"


def test_known_cuts_closure_and_may_be_unavailable_background():
    data = graph(["B", "C"], [("C", "B", "hard_depends_on"),
                               ("B", "uninstalled-A", "hard_depends_on")])
    data["nodes"]["B"]["available"] = False
    unmet = build_learning_plan(data, {"goals": ["C"]})
    assert not unmet["valid"]
    assert unmet["missing"] == ["B", "uninstalled-A"]
    plan = build_learning_plan(data, {"goals": ["C"], "known": ["B"]})
    assert plan["valid"] and ids(plan) == ["C"]
    assert plan["missing"] == []
    assert plan["steps"][0]["depends_on"] == ["B"]
    assert plan["assumptions"] == [dict(id="B", basis="known", available=False,
                                        prerequisites_not_rechecked=True)]
    done = build_learning_plan(data, {"goals": ["C"], "known": ["C"]})
    assert done["valid"] and not done["steps"]


def test_uncertainty_requires_review_unless_explicitly_assumed():
    data = graph(["A", "B", "C"], [("C", "B", "hard_depends_on"),
                                    ("B", "A", "hard_depends_on")])
    request = {"goals": ["C"], "uncertain": ["B"], "known": ["B"]}
    plan = build_learning_plan(data, request)
    assert ids(plan) == ["A", "B", "C"]
    assert plan["steps"][1]["role"] == "review"
    assert plan["known"] == [] and plan["knowledge_conflicts"] == ["B"]
    assumed = build_learning_plan(data, dict(request, assume_uncertain=True))
    assert ids(assumed) == ["C"] and assumed["assumed_uncertain"] == ["B"]
    review_goal = build_learning_plan(data, {"goals": ["C"], "uncertain": ["C"]})
    assert review_goal["steps"][-1]["role"] == "review"


def test_soft_and_proof_are_independent_opt_ins_and_navigation_is_never_required():
    data = graph(["G", "H", "S", "P", "N"], [
        ("G", "H", "hard_depends_on"), ("G", "S", "soft_depends_on"),
        ("G", "P", "proof_depends_on"), ("G", "N", "listening_next"),
        ("N", "G", "historical_influence"), ("G", "N", "contains"),
        ("G", "N", "suggested_preparation"), ("G", "N", "related_to"),
    ])
    assert ids(build_learning_plan(data, {"goals": ["G"]})) == ["H", "G"]
    soft = build_learning_plan(data, {"goals": ["G"], "include_soft": True})
    assert set(ids(soft)) == {"H", "S", "G"}
    proof = build_learning_plan(data, {"goals": ["G"], "include_proof": True})
    assert set(ids(proof)) == {"H", "P", "G"}
    both = build_learning_plan(data, {"goals": ["G"], "include_soft": True, "include_proof": True})
    assert set(ids(both)) == {"H", "P", "S", "G"}
    assert "N" not in ids(both)


def test_preferences_break_ties_without_creating_prerequisites():
    data = graph(["A", "B", "Z", "outside"], [("Z", "A", "hard_depends_on")])
    request = {"goals": ["Z", "B"], "order_hint": ["Z", "B", "A", "outside"]}
    assert ids(build_learning_plan(data, request)) == ["B", "A", "Z"]
    assert ids(build_learning_plan(data, dict(request, start="Z"))) == ["B", "A", "Z"]
    assert ids(build_learning_plan(data, dict(request, start="A"))) == ["A", "Z", "B"]
    assert "outside" not in ids(build_learning_plan(data, request))
    ignored = build_learning_plan(data, dict(request, start="unknown", order_hint=["unknown"]))
    assert ignored["valid"] and ignored["ignored_preferences"] == ["unknown"]


def test_missing_cycles_and_blocked_dependants_do_not_disappear():
    data = graph(["A", "B", "D", "G", "R"], [
        ("A", "B", "hard_depends_on"), ("B", "A", "hard_depends_on"),
        ("D", "M", "hard_depends_on"), ("G", "A", "hard_depends_on"),
        ("G", "D", "hard_depends_on"),
    ])
    plan = build_learning_plan(data, {"goals": ["G", "R"]})
    assert not plan["valid"] and ids(plan) == ["R"]
    assert plan["missing"] == ["M"]
    assert plan["cycles"] == [["A", "B"]]
    assert plan["blocked"] == ["A", "B", "D", "G"]
    assert plan["blocked_by"]["G"] == ["A", "B", "M"]
    assert plan["blocked_by"]["D"] == ["M"]
    assert "G" not in plan["cycles"][0], "a dependant is not a member of the SCC"
    unknown_goal = build_learning_plan(data, {"goals": ["not-installed"]})
    assert unknown_goal["missing"] == ["not-installed"] and not unknown_goal["valid"]


def test_real_self_cycle_is_distinct_from_combined_internal_evidence():
    data = graph(["A"], [("A", "A", "hard_depends_on")])
    assert build_learning_plan(data, {"goals": ["A"]})["cycles"] == [["A"]]
    data["relationships"][0]["internal"] = True
    assert build_learning_plan(data, {"goals": ["A"]})["valid"]


def test_separate_sccs_are_reported_without_tail_nodes_and_known_can_cut_a_cycle():
    data = graph(["A", "B", "C", "D", "G"], [
        ("A", "B", "hard_depends_on"), ("B", "A", "hard_depends_on"),
        ("C", "D", "hard_depends_on"), ("D", "C", "hard_depends_on"),
        ("G", "A", "hard_depends_on"), ("G", "C", "hard_depends_on"),
    ])
    plan = build_learning_plan(data, {"goals": ["G"]})
    assert plan["cycles"] == [["A", "B"], ["C", "D"]]
    assert plan["blocked_by"]["G"] == ["A", "B", "C", "D"]
    cut = build_learning_plan(data, {"goals": ["G"], "known": ["B", "D"]})
    assert cut["valid"] and ids(cut) == ["A", "C", "G"]


def test_aliases_resolve_goals_and_edges_but_not_component_mastery():
    snapshot = dict(generation="composed", lectures={
        "course:combined": dict(id="course:combined", title="Combined lecture", metadata=dict(
            consolidation=dict(sources=[dict(id="course:first", metadata={}),
                                        dict(id="course:second", metadata={})]))),
        "course:goal": dict(id="course:goal", title="Goal", metadata={}),
    }, courses={}, relationships=[
        {"from": "course:goal", "to": "course:second", "type": "hard_depends_on"},
        {"from": "course:second", "to": "course:first", "type": "hard_depends_on"},
    ])
    mapped = build_learning_map(snapshot)
    plan = build_learning_plan(mapped, {"goals": ["course:goal"], "known": ["course:first"]})
    assert ids(plan) == ["course:combined", "course:goal"]
    assert plan["unknown_knowledge"] == ["course:first"]
    assert not plan["cycles"] and not plan["known"]
    aliased_goal = build_learning_plan(mapped, {"goals": ["course:second"]})
    assert aliased_goal["goals"] == ["course:combined"]
    assert ids(aliased_goal) == ["course:combined"]
    assumed = build_learning_plan(mapped, {"goals": ["course:goal"],
                                         "uncertain": ["course:second"], "assume_uncertain": True})
    assert ids(assumed) == ["course:combined", "course:goal"]
    assert assumed["unknown_knowledge"] == ["course:second"]
    exact = build_learning_plan(mapped, {"goals": ["course:goal"], "known": ["course:combined"]})
    assert ids(exact) == ["course:goal"]


def test_ready_scope_and_unreviewed_mapping_are_not_completion_claims():
    data = graph(["A", "B", "C", "unavailable"], [
        ("B", "A", "hard_depends_on"), ("C", "B", "hard_depends_on")])
    data["nodes"]["A"].pop("prerequisites_reviewed")
    data["nodes"]["unavailable"]["available"] = False
    plan = build_learning_plan(data, {"known": ["A"], "uncertain": ["B"],
                                      "scope": ["A", "B", "C", "unknown", "unavailable"]})
    assert plan["valid"] and not plan["steps"]
    assert plan["ready"] == ["B"] and plan["unmapped"] == ["A"]
    assert plan["unknown_scope"] == ["unknown"]
    assert plan["limitations"]
    assumed = build_learning_plan(data, {"known": ["A"], "uncertain": ["B"], "assume_uncertain": True})
    assert assumed["ready"] == ["C"]


def test_every_enabled_constraint_is_respected_with_shared_prerequisites():
    rng = random.Random(31)
    keys = [f"N{i:02}" for i in range(35)]
    edges = [(keys[i], keys[j], rng.choice(["hard_depends_on", "soft_depends_on", "proof_depends_on"]))
             for i in range(35) for j in range(i) if rng.random() < .15]
    data = graph(keys, edges)
    request = dict(goals=keys[-8:], known=keys[:2], include_soft=True, include_proof=True,
                   order_hint=list(reversed(keys)), start=keys[-1])
    plan = build_learning_plan(data, request)
    order = {key: index for index, key in enumerate(ids(plan))}
    assert plan["valid"]
    for source, target, _ in edges:
        if source in order:
            assert target in request["known"] or order[target] < order[source]
    reversed_graph = deepcopy(data)
    reversed_graph["relationships"].reverse()
    reversed_graph["nodes"] = dict(reversed(list(data["nodes"].items())))
    assert build_learning_plan(reversed_graph, request) == plan


def test_iterative_planning_handles_long_chains_without_recursion():
    keys = [f"N{i:04}" for i in range(1400)]
    data = graph(keys, [(keys[i], keys[i - 1], "hard_depends_on") for i in range(1, len(keys))])
    plan = build_learning_plan(data, {"goals": [keys[-1]]})
    assert plan["valid"] and ids(plan) == keys


def test_inputs_and_returned_optional_metadata_are_independent():
    data = graph(["A"])
    data["nodes"]["A"].update(background="Some background", estimated_minutes=22.5,
                               readiness_checks=[{"question": "Can you explain it?"}])
    request = {"goals": ["A", "A"], "known": []}
    before = deepcopy((data, request))
    plan = build_learning_plan(data, request)
    assert (data, request) == before
    assert plan["steps"][0]["background"] == "Some background"
    plan["steps"][0]["readiness_checks"][0]["question"] = "Changed locally"
    assert (data, request) == before


@pytest.mark.parametrize("payload", [
    None, [], {"goals": "A"}, {"goals": [None]}, {"known": [True]},
    {"uncertain": [""]}, {"scope": None}, {"order_hint": [" A"]},
    {"include_soft": 1}, {"include_proof": "true"}, {"assume_uncertain": None},
    {"start": []}, {"start": ""}, {"goals": ["x" * 257]},
    {"goals": ["A"] * 5001}, {"goals": ["A"] * 5000, "known": ["A"] * 5000, "uncertain": ["A"]},
    {"unexpected_option": True},
])
def test_malformed_or_excessive_requests_are_rejected(payload):
    with pytest.raises(ValueError):
        build_learning_plan(graph(["A"]), payload)


def test_collection_goal_is_rejected_instead_of_expanding_contains():
    data = graph(["A"])
    data["nodes"]["collection:course"] = dict(id="collection:course", kind="collection", available=True)
    data["relationships"].append({"from": "collection:course", "to": "A", "type": "contains"})
    with pytest.raises(ValueError, match="collection"):
        build_learning_plan(data, {"goals": ["collection:course"]})
    data["relationships"].append({"from": "A", "to": "collection:course", "type": "hard_depends_on"})
    plan = build_learning_plan(data, {"goals": ["A"]})
    assert not plan["valid"] and plan["missing"] == ["collection:course"]
    assert plan["blocked"] == ["A"]
