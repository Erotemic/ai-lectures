from copy import deepcopy
from starlette.testclient import TestClient

from ailectures.graph import build_learning_map
from ailectures.core import lecture_revision
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def test_learning_notes_transfer_and_plan_without_a_source_checkout(tmp_path):
    pack = source_pack("math")
    original = pack["lectures"]["math:001000"]["spoken_sha256"]
    pack["lectures"]["math:001000"]["metadata"]["learning"] = {
        "reviewed": True,
        "prerequisites": [{"lecture_id": "other:001000", "reason": "Uses linear maps."}],
        "readiness_checks": ["Can you compute a kernel?"],
        "background": ["Elementary algebra"],
    }
    pack["lectures"]["math:001000"]["revision"] = lecture_revision(pack["lectures"]["math:001000"])
    export_release(pack, tmp_path / "pack")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "pack")
    with TestClient(app) as client:
        graph = client.get("/api/library/learning-map").json()
        assert graph["nodes"]["math:001000"]["prerequisites_reviewed"] is True
        assert graph["nodes"]["math:001000"]["readiness_checks"] == ["Can you compute a kernel?"]
        assert client.get("/learning-plan").status_code == 200
        plan = client.post("/api/library/learning-plan", json={"goals": ["math:001000"]}).json()
        assert plan["valid"] is False
        assert plan["missing"] == ["other:001000"]
        known = client.post("/api/library/learning-plan", json={"goals": ["math:001000"], "known": ["other:001000"]}).json()
        assert known["valid"] is True
        assert [row["id"] for row in known["steps"]] == ["math:001000"]
        assert client.post("/api/library/learning-plan", json={"include_proof": "yes"}).status_code == 400
        assert client.post("/api/library/learning-plan", json={"goals": ["math:001000"], "generation": "a-stale-map"}).status_code == 409
        assert client.post("/api/library/learning-plan", json={"goals": ["math:001000"], "generation": graph["generation"]}).status_code == 200
        assert client.get("/api/library/lectures/math:001000").json()["spoken_sha256"] == original


def test_named_listener_learning_api_is_private_state_not_pack_content(tmp_path):
    with TestClient(create_app(tmp_path / "reader")) as client:
        profile = client.post("/api/listeners", json={"name": "Learner"}).json()["id"]
        path = f"/api/listeners/{profile}/learning"
        event = {"id": "change-one", "lecture_id": "math:001000", "status": "uncertain", "revision": None}
        assert client.get(path).json() == {"knowledge": {}}
        assert client.post(path, json=event, headers={"Origin": "https://elsewhere.example"}).status_code == 403
        saved = client.post(path, json=event).json()
        assert saved["status"] == "uncertain"
        assert client.post(path, json=event).json() == saved
        assert client.get(path).json()["knowledge"]["math:001000"] == saved
        assert client.get("/api/listeners/missing/learning").status_code == 404
        assert client.post(path, json={**event, "id": "invalid", "status": "mastered-automatically"}).status_code == 400
        exported = client.get(f"/api/listeners/{profile}/export").json()
        assert exported["knowledge"]["math:001000"]["status"] == "uncertain"


def test_malformed_optional_learning_notes_do_not_hide_the_lecture():
    pack = source_pack("math")
    row = pack["lectures"]["math:001000"]
    row["metadata"]["learning"] = {"reviewed": True, "prerequisites": [{"lecture_id": "../bad"}]}
    snapshot = {**pack, "generation": "example"}
    before = deepcopy(snapshot)
    graph = build_learning_map(snapshot)
    assert graph["nodes"]["math:001000"]["available"] is True
    assert graph["nodes"]["math:001000"]["prerequisites_reviewed"] is False
    assert graph["diagnostics"]
    assert snapshot == before


def test_a_genuine_self_prerequisite_is_not_mistaken_for_combined_components():
    from ailectures.learning_plan import build_learning_plan
    pack = source_pack("math")
    pack["lectures"]["math:001000"]["metadata"]["learning"] = {
        "reviewed": True,
        "prerequisites": [{"lecture_id": "math:001000", "reason": "An erroneous self-requirement."}],
    }
    graph = build_learning_map(pack)
    edge = next(row for row in graph["relationships"] if row["type"] == "hard_depends_on")
    assert edge["internal"] is False
    plan = build_learning_plan(graph, {"goals": ["math:001000"]})
    assert plan["valid"] is False
    assert plan["cycles"] == [["math:001000"]]


def test_familiarity_tracks_manuscript_content_including_the_written_companion():
    pack = source_pack("math")
    original = build_learning_map(pack)["nodes"]["math:001000"]["knowledge_revision"]
    row = pack["lectures"]["math:001000"]
    row["metadata"]["learning"] = {"reviewed": True, "prerequisites": []}
    row["revision"] = lecture_revision(row)
    assert build_learning_map(pack)["nodes"]["math:001000"]["knowledge_revision"] == original
    row["source"] += "\nAn expanded written mathematical companion.\n"
    assert build_learning_map(pack)["nodes"]["math:001000"]["knowledge_revision"] != original
