from copy import deepcopy

from starlette.testclient import TestClient

from ailectures.core import lecture_revision
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def test_dates_transfer_without_changing_speech_and_collections_require_full_coverage(tmp_path):
    pack = source_pack("dated")
    row = pack["lectures"]["dated:001000"]
    speech = row["spoken_sha256"]
    row["metadata"]["chronology"] = {
        "work": {"start": -500, "end": -300, "approximate": True, "basis": "composition", "note": "A broad documented interval."},
        "setting": {"start": 1700, "end": 1800, "basis": "fictional setting"},
    }
    row["revision"] = lecture_revision(row)
    other = deepcopy(row)
    other.update(id="dated:002000", title="Undated lesson", metadata={})
    other["revision"] = lecture_revision(other)
    pack["lectures"][other["id"]] = other
    pack["courses"]["dated:complete"] = {"id": "dated:complete", "title": "Partly dated course", "lectures": [row["id"], other["id"]]}
    pack["courses"]["dated:explicit"] = {"id": "dated:explicit", "title": "Declared covered period", "lectures": [row["id"], other["id"]], "chronology": {"period": {"start": 1600, "end": 1900}}}
    export_release(pack, tmp_path / "pack")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "pack")
    with TestClient(app) as client:
        catalog = client.get("/api/library/catalog").json()
        lecture = next(item for item in catalog["lectures"] if item["id"] == row["id"])
        assert lecture["spoken_sha256"] == speech
        assert lecture["chronology"]["work"]["start"] == -500
        assert lecture["chronology"]["work"]["approximate"] is True
        assert lecture["chronology"]["setting"]["start"] == 1700
        courses = {item["id"]: item for item in catalog["courses"]}
        assert courses["dated:main"]["chronology"]["work"] == lecture["chronology"]["work"]
        assert "chronology" not in courses["dated:complete"]
        assert courses["dated:explicit"]["chronology"]["period"]["start"] == 1600
        assert client.get("/api/library/lectures/dated:001000").json()["chronology"] == lecture["chronology"]


def test_malformed_optional_date_fields_do_not_disable_a_lecture(tmp_path):
    pack = source_pack("dated")
    row = pack["lectures"]["dated:001000"]
    row["metadata"]["chronology"] = {"work": {"start": "ancient"}, "period": {"start": 0, "end": 100}}
    row["chronology"] = {"life": {"start": 4, "end": 2}}
    row["revision"] = lecture_revision(row)
    export_release(pack, tmp_path / "pack")
    app = create_app(tmp_path / "reader")
    app.state.library.store.install(tmp_path / "pack")
    with TestClient(app) as client:
        result = client.get("/api/library/lectures/dated:001000")
        assert result.status_code == 200
        assert result.json()["transcript"] == row["transcript"]
        assert "chronology" not in result.json()
        assert "chronology" not in client.get("/api/library/catalog").json()["lectures"][0]
