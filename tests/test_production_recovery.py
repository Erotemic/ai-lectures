"""Preparation survives process lifecycles and reuses unchanged speech inputs."""

from copy import deepcopy
import shutil
import threading
import time

import pytest

from ailectures.core import digest, lecture_revision
from ailectures.jobs import JobStore
from ailectures.library import Library
from ailectures.packs import export_release
from ailectures.production import GenerationManager
from test_content_packs import media_for, source_pack


def setup_library(tmp_path, monkeypatch, *, text=None):
    if not shutil.which("ffprobe"):
        pytest.skip("Production audio verification needs ffprobe")
    monkeypatch.setenv("DKVIS_AUDIO_PAGE_CHARS", "250")
    pack = source_pack(text=text) if text else source_pack()
    manifest = export_release(pack, tmp_path / "source")
    library = Library(tmp_path / "library")
    library.store.install(tmp_path / "source")
    audio = next(iter(media_for(pack, tmp_path)[2].values()))
    config = tmp_path / "tts.toml"
    config.write_text(
        '[profiles.test]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="kokoro"\nvoice="af_alloy"\nresponse_format="mp3"\n'
    )
    return library, pack, manifest, audio, config


def manager_for(library, config, sender, **kwargs):
    from dkvis.presentation.audio_library import AudioLectureLibrary

    def factory(**options):
        return AudioLectureLibrary(**options, sender=sender)

    return GenerationManager(
        library, config=config, engine_factory=factory, retry_delay=0, **kwargs
    )


def finished(manager, job_id):
    deadline = time.monotonic() + 8
    while time.monotonic() < deadline:
        job = manager.status(job_id)
        if job["state"] in {"ready", "failed", "settings_changed", "cancelled"}:
            return job
        time.sleep(0.02)
    pytest.fail("Preparation did not reach a terminal state")


def test_cross_process_claim_capacity_and_expiry_fences_old_owner(
    tmp_path, monkeypatch
):
    clock = [100.0]
    monkeypatch.setattr("ailectures.jobs.time.time", lambda: clock[0])
    one, two = JobStore(tmp_path), JobStore(tmp_path)
    ids = [digest("first"), digest("second")]
    one.enqueue([(key, {"request": key}) for key in ids])
    claimed = one.claim("first-worker", limit=1, lease_seconds=30)
    assert len(claimed) == 1
    assert two.claim("second-worker", limit=1, lease_seconds=30) == []
    clock[0] = 131
    recovered = two.claim("second-worker", limit=1, lease_seconds=30)
    assert recovered[0]["id"] == claimed[0]["id"]
    assert not one.save(claimed[0]["id"], "first-worker", published=digest("stale"))
    assert two.save(recovered[0]["id"], "second-worker", published=digest("valid"))
    assert one.get(recovered[0]["id"])["published"] == digest("valid")


def test_completed_pages_publish_after_restart_without_resynthesis(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(text)
        shutil.copyfile(audio, dest)

    first = manager_for(library, config, sender)
    request = first.prepare("music:001000", "test")
    deadline = time.monotonic() + 4
    while time.monotonic() < deadline:
        active = first._jobs[request["id"]]
        if active["engine"].inventory("000000", active["settings"])["ready"] == 1:
            break
        time.sleep(0.01)
    first.close()  # Preserve intent before the coordinator observes completion.
    assert first.jobs.get(request["id"])["state"] == "queued"
    second = manager_for(library, config, sender)
    try:
        second.tick()  # No browser or reselected lecture is needed.
        result = finished(second, request["id"])
        assert result["published"] and len(calls) == 1
        assert second.list()[0]["state"] == "ready"
        assert result["created_at"] <= result["updated_at"]
        repeated = second.prepare("music:001000", "test")
        assert repeated["id"] == request["id"]
        assert len(second.list()) == 1 and len(calls) == 1
    finally:
        second.close()


def test_partial_interruption_resumes_only_missing_pages(tmp_path, monkeypatch):
    text = (
        ("First passage has a clear example. " * 5).strip()
        + "\n\n"
        + ("Second passage gives another idea. " * 5).strip()
    )
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=text
    )
    calls = []
    blocked = threading.Event()
    release = threading.Event()

    def sender(text, settings, dest):
        calls.append(text)
        if len(calls) == 2:
            blocked.set()
            release.wait(4)
        shutil.copyfile(audio, dest)

    first = manager_for(library, config, sender)
    request = first.prepare("music:001000", "test")
    assert blocked.wait(3)
    # Let the interrupted callback return after its cancellation flag is set.
    timer = threading.Timer(0.1, release.set)
    timer.start()
    first.close()
    timer.join()
    second = manager_for(library, config, sender)
    try:
        second.tick()
        result = finished(second, request["id"])
        assert result["state"] == "ready"
        assert calls.count(calls[0]) == 1
        assert len(calls) == 3
    finally:
        second.close()


def test_source_revision_reuses_unchanged_pages_and_metadata_only_reuses_all(
    tmp_path, monkeypatch
):
    text = (
        ("First passage has a clear example. " * 5).strip()
        + "\n\n"
        + ("Second passage gives another idea. " * 5).strip()
    )
    library, pack, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text=text
    )
    calls = []

    def sender(text, settings, dest):
        calls.append(text)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        initial = finished(manager, manager.prepare("music:001000", "test")["id"])
        assert len(calls) == 2
        revised = source_pack(text=text.replace("First", "Third"))
        next_manifest = export_release(
            revised, tmp_path / "revised", parent=manifest["release"]
        )
        library.store.install(tmp_path / "revised")
        from starlette.testclient import TestClient
        from ailectures.web import create_app

        client = TestClient(create_app(library.store.root, generation_manager=manager))
        try:
            endpoint = "/api/library/lectures/music:001000"
            current = client.get(endpoint).json()
            assert current["recordings"] == []
            assert current["earlier_audio_release"] == initial["published"]
            old = client.get(endpoint, params={"release": initial["published"]}).json()
            assert old["transcript"] == text
            assert client.get(old["recordings"][0]["segments"][0]["url"]).status_code == 200
            retry = client.post("/api/library/production/jobs/" + initial["id"] + "/retry")
            assert retry.status_code == 409
        finally:
            client.close()
        result = finished(manager, manager.prepare("music:001000", "test")["id"])
        assert result["state"] == "ready" and len(calls) == 3
        assert calls[1] not in calls[2:]
        notes = deepcopy(revised)
        row = notes["lectures"]["music:001000"]
        row["metadata"] = {"note": "Corrected reading reference"}
        row["revision"] = lecture_revision(row)
        export_release(notes, tmp_path / "notes", parent=next_manifest["release"])
        library.store.install(tmp_path / "notes")
        bibliographic = finished(manager, manager.prepare("music:001000", "test")["id"])
        assert bibliographic["published"] == result["published"]
        assert len(calls) == 3
    finally:
        manager.close()


def test_revision_changed_during_staging_retires_in_flight_and_queued_work(
    tmp_path, monkeypatch
):
    from contextlib import contextmanager
    from concurrent.futures import ThreadPoolExecutor
    from ailectures.packs import PackStore

    library, _, manifest, audio, config = setup_library(
        tmp_path, monkeypatch, text="The original dialogue."
    )
    calls = []
    sending, release_sender = threading.Event(), threading.Event()

    def sender(text, settings, dest):
        calls.append(text)
        sending.set()
        release_sender.wait(8)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender, max_active_jobs=1)
    revised = source_pack(text="The revised dialogue.")
    export_release(revised, tmp_path / "revised", parent=manifest["release"])
    staged, release_stage = threading.Event(), threading.Event()
    original = library.store.stage_install

    @contextmanager
    def stage(*args, **kwargs):
        with original(*args, **kwargs) as prepared:
            staged.set()
            release_stage.wait(8)
            yield prepared

    try:
        first = manager.prepare("music:001000", "test")
        assert sending.wait(3)
        queued = manager.prepare("music:001000", "test", speed=1.2)
        assert queued["state"] == "queued"
        release_sender.set()
        live = manager._jobs[first["id"]]
        deadline = time.monotonic() + 5
        while not live["engine"].inventory("000000", live["settings"])["ready"]:
            assert time.monotonic() < deadline
            time.sleep(0.01)
        monkeypatch.setattr(library.store, "stage_install", stage)
        with ThreadPoolExecutor(max_workers=1) as pool:
            publishing = pool.submit(manager.tick)
            try:
                assert staged.wait(5)
                # Install through a separate client while the old worker is
                # still staging the media for the previous transcript.
                PackStore(library.store.root).install(tmp_path / "revised")
            finally:
                release_stage.set()
            publishing.result(timeout=5)
        result = manager.jobs.get(first["id"])
        assert result["state"] == "settings_changed"
        assert result["published"] is None
        assert manager.jobs.get(queued["id"])["state"] == "settings_changed"
        assert library.snapshot()["lectures"]["music:001000"]["recordings"] == []
        assert calls == ["The original dialogue."]
    finally:
        release_sender.set()
        manager.close()


def test_failures_retry_but_cancellation_is_durable(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(text)
        if len(calls) == 1:
            raise OSError("backend unavailable")
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        result = finished(manager, manager.prepare("music:001000", "test")["id"])
        assert result["state"] == "ready" and result["attempts"] == 2
        alternate = manager.prepare("music:001000", "test", voice="am_echo")
        manager.cancel(alternate["id"])
        assert manager.status(alternate["id"])["state"] == "cancelled"
    finally:
        manager.close()
    restarted = manager_for(library, config, sender)
    try:
        restarted.tick()
        assert restarted.jobs.get(alternate["id"])["state"] == "cancelled"
    finally:
        restarted.close()


def test_changed_backend_configuration_cannot_resume_under_old_recipe(
    tmp_path, monkeypatch
):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    release = threading.Event()

    def sender(text, settings, dest):
        release.wait(0.2)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    request = manager.prepare("music:001000", "test")
    manager.close()
    config.write_text(config.read_text().replace("af_alloy", "am_echo"))
    next_manager = manager_for(library, config, sender)
    try:
        next_manager.tick()
        assert next_manager.jobs.get(request["id"])["state"] == "settings_changed"
        new = next_manager.prepare("music:001000", "test")
        assert new["id"] != request["id"]
        assert finished(next_manager, new["id"])["state"] == "ready"
    finally:
        release.set()
        next_manager.close()


@pytest.mark.parametrize("model", ["kokoro", "breeze-tts2"])
def test_native_remote_protocol_produces_seekable_timed_pack(
    tmp_path, monkeypatch, model
):
    import io, json, wave
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    if not shutil.which("ffmpeg"):
        pytest.skip("Native conversion needs ffmpeg")
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    monkeypatch.setenv("DKVIS_AUDIO_BREEZE_LONG_FORM", "1")
    monkeypatch.setenv("DKVIS_AUDIO_BREEZE_JOB_API", "1")
    output = io.BytesIO()
    with wave.open(output, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(8000)
        wav.writeframes(b"\0\0" * 40000)
    speech = output.getvalue()
    requests = []
    payload = {}

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def json(self, value):
            data = json.dumps(value).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def audio(self):
            self.send_response(200)
            self.send_header("Content-Type", "audio/wav")
            self.send_header("Content-Length", str(len(speech)))
            self.send_header("X-Local-AI-Speech-Policy", "paragraph80-v1")
            self.send_header(
                "X-Local-AI-Speech-Timings",
                json.dumps(
                    {
                        "version": 1,
                        "policy": "paragraph80-v1",
                        "duration": 5,
                        "chunks": [
                            {
                                "start": 0,
                                "end": 5,
                                "words": len(payload["input"].split()),
                            }
                        ],
                    }
                ),
            )
            self.end_headers()
            self.wfile.write(speech)

        def do_POST(self):
            payload.update(
                json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            )
            requests.append((self.path, dict(payload)))
            if self.path == "/v1/audio/jobs":
                self.json({"id": "1" * 32})
            else:
                self.audio()

        def do_GET(self):
            if self.path.endswith("/audio"):
                self.audio()
            else:
                self.json(
                    {"state": "ready", "completed_passages": 1, "total_passages": 1}
                )

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    config.write_text(
        f'[profiles.test]\nendpoint="http://127.0.0.1:{server.server_port}/v1/audio/speech"\nmodel="{model}"\nvoice="af_alloy"\nresponse_format="wav"\n'
    )
    manager = GenerationManager(library, config=config, retry_delay=0)
    try:
        result = finished(manager, manager.prepare("music:001000", "test")["id"])
        assert result["state"] == "ready", result
        row = library.snapshot()["lectures"]["music:001000"]
        recording = row["recordings"][0]
        assert recording["complete"]
        assert recording["segments"][0]["duration"] > 4.8
        if model == "breeze-tts2":
            assert requests[0][0] == "/v1/audio/jobs"
            assert requests[0][1]["long_form"] is True
            assert recording["segments"][0]["timings"]["chunks"][0]["words"] == len(
                row["transcript"].split()
            )
        else:
            assert requests[0][0] == "/v1/audio/speech"
    finally:
        manager.close()
        server.shutdown()
        thread.join()
        server.server_close()


def test_feedback_revision_two_narrators_transfer_and_resume_roundtrip(
    tmp_path, monkeypatch
):
    from starlette.testclient import TestClient
    from ailectures.web import create_app
    from ailectures.core import file_digest

    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append((text, settings.voice))
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    first = finished(manager, manager.prepare("music:001000", "test")["id"])
    alternate = finished(
        manager, manager.prepare("music:001000", "test", voice="am_echo")["id"]
    )
    assert len(calls) == 2
    app = create_app(library.store.root, interval=0)
    with TestClient(app) as client:
        row = client.get("/api/library/lectures/music:001000").json()
        assert len(row["recordings"]) == 2
        assert {first["variant"], alternate["variant"]} == {
            recording["variant"] for recording in row["recordings"]
        }
        profile = client.post("/api/listeners", json={"name": "Listener"}).json()
        progress = {
            "lecture_id": row["id"],
            "revision": row["revision"],
            "release": row["origin"]["release"],
            "spoken_sha256": row["spoken_sha256"],
            "recording_id": row["recordings"][0]["id"],
            "device_id": "phone",
            "sequence": 1,
            "expected_version": 0,
            "update_id": "saved-position",
            "segment": 0,
            "seconds": 0.4,
            "anchor_word": 3,
            "completed": False,
        }
        assert (
            client.post(
                f'/api/listeners/{profile["id"]}/progress', json=progress
            ).status_code
            == 200
        )
        feedback = client.post(
            "/api/library/feedback",
            json={
                "lecture_id": row["id"],
                "release": row["origin"]["release"],
                "revision": row["revision"],
                "recording_id": row["recordings"][0]["id"],
                "segment": 0,
                "seconds": 0.4,
                "text": "Clarify the comparison.",
            },
        )
        assert feedback.status_code == 201, feedback.text
        old_url = row["recordings"][0]["segments"][0]["url"]
        revised = source_pack(
            text="Hear the interval. Then compare a clear second example."
        )
        export_release(revised, tmp_path / "revision", parent=manifest["release"])
        library.store.install(tmp_path / "revision")
        # New text is never described by the old narration.
        current = client.get("/api/library/lectures/music:001000").json()
        assert current["recordings"] == []
        updated = finished(manager, manager.prepare("music:001000", "test")["id"])
        current = client.get("/api/library/lectures/music:001000").json()
        assert current["recordings"] and len(calls) == 3
        status = client.post(
            "/api/library/feedback/status",
            json={
                "lecture_id": row["id"],
                "feedback_id": feedback.json()["id"],
                "status": "resolved",
                "addressed_revision": current["revision"],
            },
        )
        assert status.status_code == 201
        assert client.get(old_url).status_code == 200
        exported_feedback = client.get("/api/library/feedback").json()
        exported_listener = client.get(f'/api/listeners/{profile["id"]}/export').json()
        # Transfer a current source release and its independently generated audio.
        from ailectures.packs import load_release

        target = Library(tmp_path / "playback")
        target.store.install(tmp_path / "revision")
        active = next(
            item
            for item in library.store.active()
            if item["release"] == updated["published"]
        )
        target.store.install(active["directory"])
    manager.close()
    receiver = create_app(target.store.root)
    with TestClient(receiver) as client:
        assert (
            client.post(
                "/api/library/feedback/import", json=exported_feedback
            ).status_code
            == 200
        )
        assert (
            client.post("/api/listeners/import", json=exported_listener).status_code
            == 200
        )
        history = client.get(f'/api/listeners/{profile["id"]}/progress').json()[
            row["id"]
        ]
        assert history["revision"] == row["revision"] and history["seconds"] == 0.4
        fresh = client.get("/api/library/lectures/music:001000").json()
        assert fresh["revision"] != history["revision"]
        events = client.get("/api/library/feedback").json()["events"]
        assert events[0]["transcript_snapshot"] == row["transcript"]
        assert events[1]["addressed_revision"] == fresh["revision"]
        assert (
            client.get(fresh["recordings"][0]["segments"][0]["url"]).status_code == 200
        )


def test_legacy_queued_requests_keep_mp3_while_new_requests_default_to_ogg(tmp_path, monkeypatch):
    from dkvis.presentation.tts import load_profiles
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    _, configuration = GenerationManager._configuration(load_profiles(config),'test',None,None)
    configuration['settings'].pop('output_format')
    configuration['settings'].pop('reader_title_policy')
    row=deepcopy(library.snapshot()['lectures']['music:001000']);row.pop('origin');row['recordings']=[]
    specification=dict(row=row,configuration=configuration,profile='test',voice=None,speed=1)
    job_id=digest('pre-reader-delivery-defaults')
    JobStore(library.store.state).enqueue([(job_id,specification)])
    manager=manager_for(library,config,lambda text,settings,dest:shutil.copyfile(audio,dest))
    try:
        manager.tick()
        assert finished(manager,job_id)['state']=='ready'
        old=library.snapshot()['lectures']['music:001000']['recordings'][0]
        assert old['generator']['output_format']=='mp3'
        assert old['generator']['title_policy'] is None
        monkeypatch.setattr(manager, 'voices', lambda profile:dict(voices=['af_alloy'],registered=[]))
        choice=manager.narrators(library.snapshot()['lectures']['music:001000'])['choices'][0]
        assert choice['recording_id']==old['id']  # Existing playback does not trigger regeneration.
        assert choice['output_format']=='ogg'  # New generation still uses the reader default.
        request=manager.prepare('music:001000','test')
        assert finished(manager,request['id'])['state']=='ready'
        recordings=library.snapshot()['lectures']['music:001000']['recordings']
        assert any(rec['generator']['output_format']=='ogg' and rec['generator']['title_policy'] for rec in recordings)
    finally:manager.close()


def test_clear_voice_forces_fresh_synthesis_and_preserves_other_voices(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    calls = []

    def sender(text, settings, dest):
        calls.append(settings.voice)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        original = finished(manager, manager.prepare('music:001000', 'test')['id'])
        alternate = finished(manager, manager.prepare('music:001000', 'test', voice='am_echo')['id'])
        fast = finished(manager, manager.prepare('music:001000', 'test', speed=1.1)['id'])
        other_pack = source_pack(namespace='other')
        export_release(other_pack, tmp_path / 'other')
        library.store.install(tmp_path / 'other')
        other = finished(manager, manager.prepare('other:001000', 'test')['id'])
        row = library.snapshot()['lectures']['music:001000']
        manager.clear_voice_cache(row['id'], 'test', 'af_alloy', revision=row['revision'])
        recordings = Library(library.store.root).snapshot()['lectures'][row['id']]['recordings']
        assert len(recordings) == 1 and recordings[0]['variant'] == alternate['variant']
        with pytest.raises(ValueError, match='cleared'):
            manager.retry(original['id'])
        assert library.snapshot()['lectures']['other:001000']['recordings'][0]['variant'] == other['variant']
        manager.close()
        manager = manager_for(library, config, sender)
        request = manager.prepare(row['id'], 'test')
        assert request['id'] != original['id'] and request['variant'] != original['variant']
        finished(manager, request['id'])
        assert calls == ['af_alloy', 'am_echo', 'af_alloy', 'af_alloy', 'af_alloy']
        recordings = library.snapshot()['lectures'][row['id']]['recordings']
        assert len(recordings) == 2
        # Cleared jobs cannot become the inventory for the fresh narrator choice.
        assert {original['id'], fast['id']}.isdisjoint(job['id'] for job in manager.list())
        assert manager.narrators(library.snapshot()['lectures'][row['id']])['choices'][0]['variant'] == request['variant']
    finally:
        manager.close()


def test_clear_voice_rejects_active_generation_and_stale_lecture(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    release = threading.Event()

    def sender(text, settings, dest):
        release.wait(3)
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    try:
        manager.prepare('music:001000', 'test')
        row = library.snapshot()['lectures']['music:001000']
        with pytest.raises(ValueError, match='Stop generation'):
            manager.clear_voice_cache(row['id'], 'test', 'af_alloy', revision=row['revision'])
        with pytest.raises(ValueError, match='changed'):
            manager.clear_voice_cache(row['id'], 'test', 'af_alloy', revision=digest('old'))
    finally:
        release.set()
        manager.close()


def test_playback_only_server_keeps_audio_and_does_not_resume_jobs(tmp_path, monkeypatch):
    from starlette.testclient import TestClient
    from ailectures.web import create_app
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)

    def sender(text, settings, dest):
        shutil.copyfile(audio, dest)

    manager = manager_for(library, config, sender)
    finished(manager, manager.prepare('music:001000', 'test')['id'])
    manager.close()
    # A queued job from a prior server must remain idle in playback-only mode.
    old = manager.jobs.list()[0]
    manager.jobs.enqueue([(digest('queued'), {**old['specification'], 'speed': 1.1})])
    with TestClient(create_app(library.store.root, playback_only=True, tts_config=config)) as client:
        profiles = client.get('/api/library/production').json()
        assert profiles['playback_only'] and not profiles['profiles']
        row = client.get('/api/library/lectures/music:001000').json()
        assert client.get(row['recordings'][0]['segments'][0]['url']).status_code == 200
        choices = client.get('/api/library/production/narrators', params={'lecture_id': row['id']}).json()
        assert len(choices['choices']) == 1 and 'profile' not in choices['choices'][0]
        for path in ['prepare', 'clear-cache', 'voices/register', 'jobs/'+old['id']+'/retry']:
            assert client.post('/api/library/production/'+path, json={}).status_code == 403
        assert client.get('/api/library/production/jobs').json() == {'jobs': []}
    assert manager.jobs.get(digest('queued'))['state'] == 'queued'
