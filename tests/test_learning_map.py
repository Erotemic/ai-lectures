"""Native maps preserve typed evidence in both source and portable catalogs."""
from copy import deepcopy
import json

from ailectures.graph import learning_map


def snapshot():
    return {
        "generation": "example-generation",
        "lectures": {
            "math:001000": {"id": "math:001000", "title": "Combined foundations", "metadata": {
                "consolidation": {"sources": [
                    {"id": "math:001000"},
                    {"id": "math:003000", "metadata": {"consolidation": {"sources": [{"id": "math:002000"}]}}},
                ]},
            }},
            "math:004000": {"id": "math:004000", "title": "Application", "metadata": {}},
            "g1:example": {"id": "g1:example", "title": "Visual example", "kind": "presentation", "deck": "example", "aliases": ["g1:000010_example"]},
        },
        "courses": {
            "math:main": {"id": "math:main", "title": "Main", "lectures": ["math:001000", "math:004000", "optional:001000"], "preparation_collections": ["other:main"]},
            "math:deep": {"id": "math:deep", "title": "Deep", "parent_id": "math:main", "lectures": ["math:004000"], "related_collections": ["math:main"]},
        },
        "relationships": [
            {"from": "math:004000", "type": "proof_depends_on", "to": "math:002000", "why": "Uses the original lemma."},
            {"from": "math:004000", "type": "proof_depends_on", "to": "math:003000", "why": "Uses its second construction."},
            {"from": "math:003000", "type": "proof_depends_on", "to": "math:002000", "why": "A relation internal to the combined manuscript."},
            {"from": "math:004000", "type": "historical_influence", "to": "optional:001000", "why": "An explicit source claim."},
            {"from": "g1:000010_example", "type": "alternative_presentation", "to": "math:001000"},
        ],
    }


def test_nested_components_contract_without_losing_claims_or_mutating_input():
    source = snapshot()
    before = deepcopy(source)
    graph = learning_map(source)
    assert source == before
    assert graph["component_lectures"]["math:002000"] == "math:001000"
    assert "math:002000" not in graph["nodes"]
    proofs = [edge for edge in graph["relationships"] if edge["type"] == "proof_depends_on"]
    assert len(proofs) == 2
    external = next(edge for edge in proofs if not edge["internal"])
    assert external["to"] == "math:001000"
    assert external["reasons"] == ["Uses the original lemma.", "Uses its second construction."]
    assert {claim["to"] for claim in external["evidence"]} == {"math:002000", "math:003000"}
    internal = next(edge for edge in proofs if edge["internal"])
    assert internal["from"] == internal["to"] == "math:001000"
    assert internal["evidence"][0]["from"] == "math:003000"
    json.dumps(graph)
    assert graph == learning_map(source)


def test_listening_preparation_history_and_organization_are_distinct():
    graph = learning_map(snapshot())
    kinds = {edge["type"]: edge["category"] for edge in graph["relationships"]}
    assert kinds["listening_next"] == "listening"
    assert kinds["proof_depends_on"] == "proof"
    assert kinds["historical_influence"] == "history"
    assert kinds["suggested_preparation"] == "preparation"
    assert kinds["contains"] == kinds["collection_parent"] == "organization"
    assert not any(edge["type"] == "hard_depends_on" for edge in graph["relationships"])
    unknown = graph["nodes"]["optional:001000"]
    assert unknown["available"] is False and unknown["url"] is None
    assert graph["nodes"]["collection:other:main"]["available"] is False
    assert graph["nodes"]["g1:example"]["url"] == "/presentations?deck=example"
    assert graph["nodes"]["math:004000"]["url"] == "/lectures/math/004000"


def test_transferred_component_evidence_and_duplicate_routes_remain_exact():
    source = snapshot()
    source["relationships"].append({"from": "g1:example", "type": "related_to", "to": "math:001000", "component_relations": [
        {"from": "g1:000010_example", "to": "math:002000", "why": "Original evidence before alias normalization."},
    ]})
    source["courses"]["math:also"] = {"id": "math:also", "title": "Also", "lectures": ["math:001000", "math:004000"]}
    graph = learning_map(source)
    relation = next(edge for edge in graph["relationships"] if edge["type"] == "related_to" and edge["from"] == "g1:example")
    assert relation["evidence"][0]["from"] == "g1:000010_example"
    assert relation["reasons"] == ["Original evidence before alias normalization."]
    order = next(edge for edge in graph["relationships"] if edge["type"] == "listening_next" and edge["from"] == "math:001000")
    assert order["collections"] == ["math:main", "math:also"]
    assert len(order["evidence"]) == 2


def test_a_portable_pack_needs_no_repository_or_presentation_runtime(tmp_path):
    from ailectures.library import Library
    from ailectures.packs import export_release
    from test_content_packs import source_pack
    pack = source_pack()
    pack["relationships"] = [{"from": "music:001000", "type": "soft_depends_on", "to": "optional:001000", "why": "An optional background lesson."}]
    export_release(pack, tmp_path / "export")
    library = Library(tmp_path / "library")
    library.store.install(tmp_path / "export")
    graph = learning_map(library.snapshot())
    assert graph["nodes"]["music:001000"]["available"]
    assert graph["nodes"]["optional:001000"]["url"] is None
    assert graph["counts"]["lectures"] == 1


def test_native_map_api_keeps_library_snapshot_immutable(tmp_path):
    from starlette.testclient import TestClient
    from ailectures.packs import export_release
    from ailectures.web import create_app
    from test_content_packs import source_pack
    pack = source_pack()
    pack["relationships"] = [
        {"from": "music:001000", "type": "proof_depends_on", "to": "optional:001000", "why": "Explicit proof use."},
        {"from": "music:001000", "type": "historical_influence", "to": "optional:001000", "why": "A separately supplied historical claim."},
    ]
    export_release(pack, tmp_path / "export")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "export")
    original = app.state.library.snapshot()
    with TestClient(app) as client:
        first = client.get("/api/library/learning-map")
        assert first.status_code == 200
        graph = first.json()
        assert {edge["category"] for edge in graph["relationships"] if edge["to"] == "optional:001000"} == {"proof", "history"}
        assert graph["nodes"]["optional:001000"]["url"] is None
        assert client.get("/api/library/learning-map").json() == graph
    assert app.state.library.snapshot() == original


def test_malformed_optional_composition_does_not_disable_usable_map():
    source = snapshot()
    source["lectures"]["math:001000"]["metadata"]["consolidation"]["sources"] = None
    source["lectures"]["math:004000"]["aliases"] = "not-a-list"
    source["courses"]["math:main"]["preparation_collections"] = [None, "other:main"]
    source["courses"]["math:main"]["chapters"] = None
    source["relationships"].append({"from": None, "type": "related_to", "to": "math:004000"})
    graph = learning_map(source)
    assert graph["nodes"]["math:001000"]["available"]
    assert graph["diagnostics"] == ["Ignored a relationship with missing endpoints or type."]
    assert graph["nodes"]["collection:other:main"]["url"] is None
