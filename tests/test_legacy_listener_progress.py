from starlette.testclient import TestClient

from ailectures.web import create_app


def test_unknown_legacy_revision_remains_unknown_after_history_transfer(tmp_path):
    with TestClient(create_app(tmp_path / "library")) as client:
        profile = client.post("/api/listeners", json={"name": "Listener"}).json()["id"]
        position = dict(
            lecture_id="music:001000",
            revision=None,
            spoken_sha256=None,
            release=None,
            recording_id=None,
            segment=3,
            seconds=0,
            completed=False,
            sequence=1,
            device_id="old-device",
            update_id="legacy-import",
            expected_version=0,
            legacy={"page_index": 3, "snapshots": []},
        )
        response = client.post(f"/api/listeners/{profile}/progress", json=position)
        assert response.status_code == 200
        assert response.json()["revision"] is None
        document = client.get(f"/api/listeners/{profile}/export").json()
    with TestClient(create_app(tmp_path / "receiver")) as client:
        assert client.post("/api/listeners/import", json=document).status_code == 200
        saved = client.get(f"/api/listeners/{profile}/progress").json()[
            position["lecture_id"]
        ]
        assert saved["revision"] is None and saved["recording_id"] is None
        assert saved["legacy"] == position["legacy"]
