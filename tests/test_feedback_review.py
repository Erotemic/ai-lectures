from starlette.testclient import TestClient

from ailectures.packs import export_release
from ailectures.state import ListenerState
from ailectures.web import create_app
from test_content_packs import source_pack


def test_editorial_resolution_preserves_original_context_and_transfers(tmp_path):
    pack = source_pack()
    export_release(pack, tmp_path / "source")
    app = create_app(tmp_path / "library")
    app.state.library.store.install(tmp_path / "source")
    with TestClient(app) as client:
        assert client.get("/feedback").status_code == 200
        row = client.get("/api/library/lectures/music:001000").json()
        submission = client.post(
            "/api/library/feedback",
            json={
                "lecture_id": row["id"],
                "release": row["origin"]["release"],
                "revision": row["revision"],
                "text": "Explain the interval more clearly.",
            },
        ).json()
        change = dict(
            id="editorial-change",
            created_at="2026-11-15T00:00:00+00:00",
            lecture_id=row["id"],
            feedback_id=submission["id"],
            status="triaged",
            note="Rework the comparison in the next draft.",
        )
        result = client.post("/api/library/feedback/status", json=change)
        assert result.status_code == 201
        assert (
            client.post("/api/library/feedback/status", json=change).json()
            == result.json()
        )
        assert (
            client.post(
                "/api/library/feedback/status", json=dict(change, note="different")
            ).status_code
            == 409
        )
        app.state.library.store.remove("music")
        exported = client.get("/api/library/feedback").json()
        assert exported["events"][0]["transcript_snapshot"] == row["transcript"]
        assert exported["events"][1]["note"] == change["note"]
        receiver = ListenerState(tmp_path / "receiver")
        assert receiver.import_feedback(exported) == 2
        assert receiver.import_feedback(exported) == 0
        assert receiver.feedback() == exported["events"]
