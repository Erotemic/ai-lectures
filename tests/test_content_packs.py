"""Portable releases, live discovery, and concurrent activation invariants."""

from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

import pytest
from starlette.testclient import TestClient

from ailectures.catalog import RepositoryCatalog
from ailectures.core import Conflict, digest, lecture_revision, text_digest
from ailectures.packs import (
    PackStore,
    archive_release,
    export_release,
    load_release,
    recording_id,
)
from ailectures.state import ListenerState
from ailectures.web import create_app


def source_pack(namespace="music", text="Hear the interval. Then compare the pitches."):
    key = namespace + ":001000"
    row = dict(
        id=key,
        namespace=namespace,
        title="Intervals",
        transcript=text,
        spoken_sha256=text_digest(text),
        source="# Intervals\n" + text,
        metadata={},
        sources={},
        section="listening",
        kind="audio",
        recordings=[],
    )
    row["revision"] = lecture_revision(row)
    course = dict(
        id=namespace + ":main",
        title="Music",
        summary="Listen and compare",
        lectures=[key],
    )
    return dict(
        id=namespace,
        title="Music",
        lectures={key: row},
        courses={course["id"]: course},
        relationships=[],
    )


def media_for(pack, tmp_path, *, variant="narrator-a", complete=True):
    # Valid WAV bytes make the fixture playable without TTS, ffprobe, or a codec.
    import wave

    audio = tmp_path / (variant + ".wav")
    with wave.open(str(audio), "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(8000)
        stream.writeframes(b"\x00\x00" * 8000)
    key, row = next(iter(pack["lectures"].items()))
    path = f"artifacts/{variant}/000.wav"
    from ailectures.core import file_digest

    segments = (
        [
            dict(
                index=0,
                path=path,
                sha256=file_digest(audio),
                duration=1.0,
                media_type="audio/wav",
            )
        ]
        if complete
        else []
    )
    recording = dict(
        variant=variant,
        recipe=digest("recipe"),
        spoken_sha256=row["spoken_sha256"],
        pages=[row["transcript"]],
        segments=segments,
        complete=complete,
    )
    recording["id"] = recording_id(recording)
    return key, recording, {path: audio} if complete else {}


def test_round_trip_and_exact_playback_without_production(tmp_path):
    pack = source_pack()
    media = media_for(pack, tmp_path)
    release = tmp_path / "export"
    manifest = export_release(pack, release, media=[media])
    archive_release(release, tmp_path / "pack.zip")
    root = tmp_path / "elsewhere"
    store = PackStore(root)
    store.install(tmp_path / "pack.zip")
    source = tmp_path / "export" / "catalog.json"
    source.write_text("broken source after transfer")
    with TestClient(create_app(root, interval=0.05)) as client:
        data = client.get("/api/library/catalog").json()
        assert [r["id"] for r in data["lectures"]] == ["music:001000"]
        detail = client.get("/api/library/lectures/music:001000").json()
        segment = detail["recordings"][0]["segments"][0]
        response = client.get(segment["url"], headers={"Range": "bytes=0-31"})
        assert response.status_code == 206
        assert (
            response.content
            == media[2][media[1]["segments"][0]["path"]].read_bytes()[:32]
        )
        assert client.head(segment["url"]).status_code == 200
        assert client.get("/api/library/production").json()["profiles"] == []
        assert client.get("/").status_code == 200
        assert manifest["release"] in segment["url"]


def test_live_discovery_update_and_historical_media(tmp_path):
    incoming = tmp_path / "incoming"
    incoming.mkdir()
    first = source_pack()
    media = media_for(first, tmp_path)
    m1 = export_release(first, incoming / "one", media=[media])
    app = create_app(tmp_path / "library", discovery_roots=[incoming], interval=0)
    with TestClient(app) as client:
        a = client.get("/api/library/catalog").json()
        old = client.get("/api/library/lectures/music:001000").json()
        second = source_pack(text="The revised lecture explains the octave.")
        m2 = export_release(second, incoming / "two", parent=m1["release"])
        b = client.get("/api/library/catalog?refresh=1").json()
        assert a["generation"] != b["generation"]
        assert (
            client.get("/api/library/lectures/music:001000").json()["transcript"]
            == next(iter(second["lectures"].values()))["transcript"]
        )
        assert client.get(old["recordings"][0]["segments"][0]["url"]).status_code == 200
        assert (
            client.get(
                "/api/library/lectures/music:001000", params={"release": m1["release"]}
            ).json()["revision"]
            == old["revision"]
        )
        app.state.library.store.remove("music")
        assert not client.get("/api/library/catalog").json()["lectures"]
        assert client.get(old["recordings"][0]["segments"][0]["url"]).status_code == 200
        # Automatic discovery must not undo an explicit removal.
        assert not client.get("/api/library/catalog?refresh=1").json()["lectures"]


def test_parallel_independent_packs_and_same_base_conflict(tmp_path):
    left, right = tmp_path / "left", tmp_path / "right"
    export_release(source_pack("music"), left)
    export_release(source_pack("history"), right)
    root = tmp_path / "library"
    stores = [PackStore(root), PackStore(root)]
    with ThreadPoolExecutor(2) as pool:
        results = list(
            pool.map(lambda pair: pair[0].install(pair[1]), zip(stores, [left, right]))
        )
    assert set(stores[0].snapshot()["lectures"]) == {"music:001000", "history:001000"}
    original = results[0]["release"]
    a = export_release(
        source_pack("music", "Revision A."), tmp_path / "a", parent=original
    )
    b = export_release(
        source_pack("music", "Revision B."), tmp_path / "b", parent=original
    )

    def update(path):
        try:
            return PackStore(root).install(path)["release"]
        except Conflict:
            return "conflict"

    with ThreadPoolExecutor(2) as pool:
        results = list(pool.map(update, [tmp_path / "a", tmp_path / "b"]))
    assert results.count("conflict") == 1
    assert set(stores[0].snapshot()["lectures"]) == {"music:001000", "history:001000"}


def test_invalid_candidate_and_checksum_preserve_active(tmp_path):
    store = PackStore(tmp_path / "library")
    m1 = export_release(source_pack(), tmp_path / "one")
    store.install(tmp_path / "one")
    m2 = export_release(
        source_pack(text="Changed."), tmp_path / "two", parent=m1["release"]
    )
    (tmp_path / "two" / "catalog.json").write_text("{}")
    with pytest.raises(ValueError, match="Checksum"):
        store.install(tmp_path / "two")
    assert store.snapshot()["packs"][0]["release"] == m1["release"]


def test_archive_paths_and_duplicate_entries_are_rejected(tmp_path):
    for index, paths in enumerate([["../escape"], ["catalog.json", "catalog.json"]]):
        archive = tmp_path / f"bad{index}.zip"
        with ZipFile(archive, "w") as stream:
            for path in paths:
                stream.writestr(path, "bad")
        with pytest.raises(ValueError):
            PackStore(tmp_path / "library").install(archive)
    assert not (tmp_path / "escape").exists()


def test_competing_discovery_candidates_do_not_choose_scan_order(tmp_path):
    incoming = tmp_path / "incoming"
    incoming.mkdir()
    a = export_release(source_pack(), incoming / "a")
    export_release(
        source_pack(text="Other independent initial release."), incoming / "b"
    )
    store = PackStore(tmp_path / "library", discovery_roots=[incoming], interval=0)
    assert not store.snapshot()["lectures"]
    assert store.errors


def test_pack_dependencies_and_identity_collisions_rollback(tmp_path):
    store = PackStore(tmp_path / "library")
    export_release(source_pack(), tmp_path / "base")
    store.install(tmp_path / "base")
    colliding = source_pack(text="Different owner of same lecture.")
    colliding["id"] = "collision"
    export_release(colliding, tmp_path / "collision")
    with pytest.raises(Conflict):
        store.install(tmp_path / "collision")
    assert len(store.active()) == 1
    dependent = source_pack("another")
    export_release(
        dependent, tmp_path / "dependent", dependencies={"missing": digest("absent")}
    )
    with pytest.raises(Conflict):
        store.install(tmp_path / "dependent")
    assert len(store.active()) == 1


def test_content_revision_and_feedback_remain_bound_to_old_recording(tmp_path):
    pack = source_pack()
    manifest = export_release(pack, tmp_path / "one", media=[media_for(pack, tmp_path)])
    app = create_app(tmp_path / "library", interval=0)
    app.state.library.store.install(tmp_path / "one")
    with TestClient(app) as client:
        old = client.get("/api/library/lectures/music:001000").json()
        revised = source_pack(text="A new transcript.")
        export_release(revised, tmp_path / "two", parent=manifest["release"])
        app.state.library.store.install(tmp_path / "two")
        payload = dict(
            id="draft-1",
            created_at="2026-11-15T00:00:00Z",
            lecture_id=old["id"],
            release=manifest["release"],
            revision=old["revision"],
            text="The first comparison is confusing.",
            recording_id=old["recordings"][0]["id"],
            segment=0,
            seconds=0.5,
        )
        response = client.post("/api/library/feedback", json=payload)
        assert response.status_code == 201, response.text
        event = response.json()
        assert event["transcript_snapshot"] == old["transcript"]
        assert client.post("/api/library/feedback", json=payload).json() == event
        wrong = dict(
            payload,
            id="bad",
            revision=next(iter(revised["lectures"].values()))["revision"],
        )
        assert client.post("/api/library/feedback", json=wrong).status_code == 409
        events = client.get("/api/library/feedback").json()["events"]
        assert len(events) == 1
        assert not any(e["type"] == "status" for e in events)


def test_feedback_import_is_idempotent_and_atomic(tmp_path):
    state = ListenerState(tmp_path / "state")
    event = dict(
        id="a",
        type="submission",
        lecture_id="music:001000",
        text="Feedback",
        release=digest("release"),
        revision=digest("revision"),
        spoken_sha256=text_digest("Speech"),
        transcript_snapshot="Speech",
    )
    state.add_feedback_event(event)
    exported = state.export_feedback()
    assert state.import_feedback(exported) == 0
    with pytest.raises(Conflict):
        state.import_feedback(
            {
                "schema_version": 1,
                "events": [dict(event, id="new"), dict(event, text="clobber")],
            }
        )
    assert state.feedback() == [event]


def test_listener_progress_device_conflict_rewind_and_transfer(tmp_path):
    state = ListenerState(tmp_path / "state")
    profile = state.create_profile("Listener")
    p = dict(
        update_id="first",
        lecture_id="music:001000",
        device_id="phone",
        sequence=1,
        expected_version=0,
        seconds=40,
        revision=digest("revision"),
    )
    first = state.save_progress(profile["id"], p)
    assert state.save_progress(profile["id"], p) == first
    rewound = dict(p, update_id="rewind", sequence=2, expected_version=1, seconds=10)
    second = state.save_progress(profile["id"], rewound)
    assert second["seconds"] == 10 and second["version"] == 2
    late = dict(p, update_id="late", device_id="tablet", sequence=1, seconds=80)
    result = state.save_progress(profile["id"], late)
    assert result["conflict"] and result["alternate"] == late
    assert state.progress(profile["id"])["music:001000"]["seconds"] == 10
    export = state.export_listener(profile["id"])
    other = ListenerState(tmp_path / "other-state")
    assert other.import_listener(export) == profile
    assert other.progress(profile["id"]) == state.progress(profile["id"])


def test_repository_discovery_and_revision_without_tts(tmp_path):
    folder = tmp_path / "draft-stages" / "tts-music"
    folder.mkdir(parents=True)
    manuscript = folder / "001000-intervals.md"
    manuscript.write_text(
        "# Intervals\n<!-- BEGIN SPOKEN LECTURE -->\nHear an octave.\n<!-- END SPOKEN LECTURE -->\n"
    )
    (folder / "track.json").write_text(
        json.dumps(
            dict(
                id="music",
                title="Music",
                lectures=[dict(id="001000", file=manuscript.name)],
            )
        )
    )
    catalog = RepositoryCatalog(tmp_path)
    first = catalog.snapshot()["music"]["lectures"]["music:001000"]
    manuscript.write_text(manuscript.read_text().replace("octave", "fifth"))
    second = catalog.snapshot()["music"]["lectures"]["music:001000"]
    assert first["revision"] != second["revision"]
    manuscript.write_text("partial write")
    assert catalog.snapshot()["music"]["lectures"]["music:001000"] == second
    assert catalog.errors


def test_reader_import_boundary_in_fresh_process(tmp_path):
    code = """
import sys
from ailectures.web import create_app
app=create_app(sys.argv[1])
assert not any(name=='dkvis' or name.startswith(('dkvis.','numpy','networkx','torch','manim','vtk')) for name in sys.modules)
"""
    subprocess.run([sys.executable, "-c", code, str(tmp_path / "library")], check=True)


def test_audio_addons_survive_source_revisions_without_claiming_new_speech(tmp_path):
    pack = source_pack()
    base = export_release(pack, tmp_path / "base")
    addon = deepcopy(pack)
    addon["id"] = "music-audio"
    addon["courses"] = {}
    audio = media_for(addon, tmp_path)
    export_release(addon, tmp_path / "audio", media=[audio], kind="media")
    store = PackStore(tmp_path / "library")
    store.install(tmp_path / "base")
    store.install(tmp_path / "audio")
    assert store.snapshot()["lectures"]["music:001000"]["recordings"]
    notes = deepcopy(pack)
    notes["lectures"]["music:001000"]["metadata"] = {
        "reading_note": "Corrected bibliography"
    }
    notes["lectures"]["music:001000"]["revision"] = lecture_revision(
        notes["lectures"]["music:001000"]
    )
    revision = export_release(notes, tmp_path / "notes", parent=base["release"])
    store.install(tmp_path / "notes")
    assert store.snapshot()["lectures"]["music:001000"]["recordings"]
    changed = source_pack(text="A different spoken explanation.")
    export_release(changed, tmp_path / "changed", parent=revision["release"])
    store.install(tmp_path / "changed")
    assert not store.snapshot()["lectures"]["music:001000"]["recordings"]
    old_release = load_release(tmp_path / "audio")["manifest"]["release"]
    assert store.media_file(old_release, audio[1]["id"], 0)[0].exists()


def test_source_snapshot_adds_recording_context_without_losing_historical_feedback(
    tmp_path,
):
    folder = tmp_path / "repository" / "draft-stages" / "tts-music"
    folder.mkdir(parents=True)
    original = source_pack()
    text = original["lectures"]["music:001000"]["transcript"]
    manuscript = folder / "001000-intervals.md"
    manuscript.write_text(
        "# Intervals\n<!-- BEGIN SPOKEN LECTURE -->\n"
        + text
        + "\n<!-- END SPOKEN LECTURE -->\n"
    )
    (folder / "track.json").write_text(
        json.dumps(
            {
                "id": "music",
                "title": "Music",
                "lectures": [{"id": "001000", "file": manuscript.name}],
            }
        )
    )
    app = create_app(
        tmp_path / "library", repository=tmp_path / "repository", interval=0
    )
    with TestClient(app) as client:
        before = client.get("/api/library/lectures/music:001000").json()
        pack = app.state.library.repository.snapshot()["music"]
        pack["id"] = "music-audio"
        pack["courses"] = {}
        export_release(
            pack, tmp_path / "audio", media=[media_for(pack, tmp_path)], kind="media"
        )
        app.state.library.store.install(tmp_path / "audio")
        after = client.get("/api/library/lectures/music:001000").json()
        assert after["origin"]["release"] != before["origin"]["release"]
        assert after["revision"] == before["revision"]
        response = client.post(
            "/api/library/feedback",
            json=dict(
                lecture_id=after["id"],
                release=after["origin"]["release"],
                revision=after["revision"],
                text="A recording issue.",
                recording_id=after["recordings"][0]["id"],
                segment=0,
                seconds=0.2,
            ),
        )
        assert response.status_code == 201, response.text
        assert (
            app.state.library.historical(before["origin"]["release"], before["id"])[
                "recordings"
            ]
            == []
        )


def test_pins_exclusions_and_generated_lock_are_local_policy(tmp_path):
    incoming = tmp_path / "incoming"
    incoming.mkdir()
    first = export_release(source_pack(), incoming / "one")
    second = export_release(
        source_pack(text="Revised."), incoming / "two", parent=first["release"]
    )
    store = PackStore(
        tmp_path / "library",
        discovery_roots=[incoming],
        pins={"music": first["release"]},
        interval=0,
    )
    assert store.snapshot()["packs"][0]["release"] == first["release"]
    lock = json.loads((store.root / "library.lock.json").read_text())
    assert lock["packs"] == {"music": first["release"]}
    store.pins = {}
    assert store.snapshot()["packs"][0]["release"] == second["release"]
    store.excluded = {"music"}
    assert not store.snapshot()["lectures"]


def test_published_media_cannot_change_behind_an_immutable_url(tmp_path):
    pack = source_pack()
    media = media_for(pack, tmp_path)
    manifest = export_release(pack, tmp_path / "release", media=[media])
    store = PackStore(tmp_path / "library")
    store.install(tmp_path / "release")
    path, _ = store.media_file(manifest["release"], media[1]["id"], 0)
    path.write_bytes(b"changed")
    with pytest.raises(ValueError, match="bytes changed"):
        store.media_file(manifest["release"], media[1]["id"], 0)


def test_alias_collision_and_invalid_media_completeness_are_rejected(tmp_path):
    a = source_pack("music")
    a["lectures"]["music:001000"]["aliases"] = ["shared:one"]
    a["lectures"]["music:001000"]["revision"] = lecture_revision(
        a["lectures"]["music:001000"]
    )
    b = source_pack("history")
    b["lectures"]["history:001000"]["aliases"] = ["shared:one"]
    b["lectures"]["history:001000"]["revision"] = lecture_revision(
        b["lectures"]["history:001000"]
    )
    export_release(a, tmp_path / "a")
    export_release(b, tmp_path / "b")
    store = PackStore(tmp_path / "library")
    store.install(tmp_path / "a")
    with pytest.raises(Conflict, match="alias"):
        store.install(tmp_path / "b")
    media = media_for(source_pack(), tmp_path)
    media[1]["complete"] = False
    media[1]["id"] = recording_id(media[1])
    with pytest.raises(ValueError, match="completeness"):
        export_release(source_pack(), tmp_path / "bad", media=[media])


def test_declarative_content_folder_requires_no_shared_registry(tmp_path):
    folder = tmp_path / "content" / "independent"
    folder.mkdir(parents=True)
    filename = "001000-new.md"
    (folder / filename).write_text(
        "# New\n<!-- BEGIN SPOKEN LECTURE -->A new subject.<!-- END SPOKEN LECTURE -->"
    )
    (folder / "track.json").write_text(
        json.dumps(
            {
                "id": "independent",
                "title": "Independent",
                "lectures": [{"id": "001000", "file": filename}],
            }
        )
    )
    assert set(RepositoryCatalog(tmp_path).snapshot()) == {"independent"}


def test_generation_reuses_job_identity_and_publishes_portable_recording(tmp_path):
    import shutil
    import time

    if not shutil.which("ffprobe"):
        pytest.skip("Generation verification requires ffprobe")
    from ailectures.library import Library
    from ailectures.production import GenerationManager
    from dkvis.presentation.audio_library import AudioLectureLibrary

    pack = source_pack()
    export_release(pack, tmp_path / "pack")
    library = Library(tmp_path / "library")
    library.store.install(tmp_path / "pack")
    fake_audio = next(iter(media_for(pack, tmp_path)[2].values()))
    calls = []

    def synth(text, settings, destination):
        calls.append(text)
        shutil.copyfile(fake_audio, destination)

    def factory(**kwargs):
        return AudioLectureLibrary(**kwargs, sender=synth)

    config = tmp_path / "tts.toml"
    config.write_text("""[profiles.test]
endpoint="http://127.0.0.1:1/v1/audio/speech"
model="kokoro"
voice="af_alloy"
response_format="mp3"
[profiles.test.reference]
audio="approved-reference.wav"
transcript="approved-reference.txt"
""")
    manager = GenerationManager(library, config=config, engine_factory=factory)
    try:
        job = manager.prepare("music:001000", "test")
        for _ in range(100):
            if job["published"]:
                break
            time.sleep(0.02)
            job = manager.status(job["id"])
        assert job["published"]
        repeated = manager.prepare("music:001000", "test")
        assert repeated["id"] == job["id"]
        assert len(calls) == 1
        snapshot = library.snapshot()
        assert snapshot["lectures"]["music:001000"]["recordings"][0]["complete"]
        # The source pack remains the content authority and all playback is local.
        assert (
            snapshot["lectures"]["music:001000"]["revision"]
            == pack["lectures"]["music:001000"]["revision"]
        )
    finally:
        manager.close()


def test_device_sequence_survives_intervening_device_updates(tmp_path):
    state = ListenerState(tmp_path / "state")
    profile = state.create_profile("Listener")["id"]
    base = dict(lecture_id="music:001000", seconds=10, revision=digest("r"))
    state.save_progress(
        profile,
        dict(base, update_id="a", device_id="phone", sequence=10, expected_version=0),
    )
    state.save_progress(
        profile,
        dict(base, update_id="b", device_id="tablet", sequence=1, expected_version=1),
    )
    result = state.save_progress(
        profile,
        dict(base, update_id="c", device_id="phone", sequence=9, expected_version=2),
    )
    assert result["conflict"]
    assert state.progress(profile)["music:001000"]["device_id"] == "tablet"


def test_reexport_installed_media_pack_preserves_release_identity(
    tmp_path, monkeypatch, capsys
):
    from ailectures.__main__ import main

    pack = source_pack()
    pack["extra_files"] = {"README.md": b"Original instructional notes.\n"}
    manifest = export_release(
        pack, tmp_path / "release", media=[media_for(pack, tmp_path)], kind="media"
    )
    root = tmp_path / "library"
    PackStore(root).install(tmp_path / "release")
    monkeypatch.chdir(tmp_path)
    main(
        [
            "--library",
            str(root),
            "export",
            "--pack",
            "music",
            "--output",
            str(tmp_path / "again"),
        ]
    )
    assert (
        load_release(tmp_path / "again")["manifest"]["release"] == manifest["release"]
    )
    assert (
        tmp_path / "again" / "README.md"
    ).read_bytes() == b"Original instructional notes.\n"
