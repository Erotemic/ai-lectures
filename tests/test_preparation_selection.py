from copy import deepcopy

from starlette.testclient import TestClient

from ailectures.core import lecture_revision
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def test_lecture_controls_pass_narrator_and_course_batches_skip_non_audio(tmp_path):
    class Producer:
        def __init__(self):
            self.requests = []
            self.probes = []

        def profiles(self, *, probe=False):
            self.probes.append(probe)
            return dict(profiles=[], tools_available=True)

        def prepare(self, key, profile, **settings):
            self.requests.append((key, profile, settings))
            return dict(id="requested")

        def prepare_many(self, keys, profile, **settings):
            self.requests.append((keys, profile, settings))
            return [dict(id="requested") for key in keys]

        def tick(self):
            pass

        def close(self):
            pass

    pack = source_pack()
    visual = deepcopy(pack["lectures"]["music:001000"])
    visual.update(id="music:002000", kind="presentation", title="A visual companion")
    visual["revision"] = lecture_revision(visual)
    pack["lectures"][visual["id"]] = visual
    pack["courses"]["music:main"]["lectures"] += [visual["id"], "missing:001000"]
    export_release(pack, tmp_path / "pack")
    producer = Producer()
    app = create_app(tmp_path / "library", generation_manager=producer)
    app.state.library.store.install(tmp_path / "pack")
    with TestClient(app) as client:
        assert client.get("/api/library/production?probe=0").status_code == 200
        assert producer.probes == [False]
        selection = dict(
            lecture_id="music:001000",
            revision=pack["lectures"]["music:001000"]["revision"],
            profile="narrator-b",
            voice="af_heart",
            speed=1.1,
        )
        assert (
            client.post("/api/library/production/prepare", json=selection).status_code
            == 202
        )
        assert producer.requests[-1] == (
            "music:001000",
            "narrator-b",
            dict(voice="af_heart", speed=1.1),
        )
        assert (
            client.post(
                "/api/library/production/prepare",
                json=dict(selection, revision="older"),
            ).status_code
            == 409
        )
        assert len(producer.requests) == 1
        assert (
            client.post(
                "/api/library/production/prepare",
                json=dict(
                    course_id="music:main", profile="narrator-b", voice="af_heart"
                ),
            ).status_code
            == 202
        )
        assert producer.requests[-1][0] == ["music:001000"]
