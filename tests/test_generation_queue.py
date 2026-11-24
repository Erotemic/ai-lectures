"""Durable declaration-based queues pin each voice and never synthesize in the CLI."""
from copy import deepcopy
import json
import shutil
import sqlite3
import os
from pathlib import Path
import subprocess
import sys
import time

import pytest
from starlette.testclient import TestClient

from ailectures.__main__ import main
from ailectures.core import lecture_revision
from ailectures.generation_queue import queue_audio
from ailectures.jobs import JobStore
from ailectures.packs import export_release
from ailectures.web import create_app
from test_production_recovery import setup_library, manager_for, finished


def fixture(tmp_path, monkeypatch):
    library, pack, manifest, audio, config = setup_library(tmp_path, monkeypatch)
    row = deepcopy(pack['lectures']['music:001000'])
    row['id'] = 'music:002000'
    row['revision'] = lecture_revision(row)
    pack['lectures'][row['id']] = row
    pack['courses']['music:main']['lectures'].append(row['id'])
    export_release(pack, tmp_path / 'two')
    library.store.install(tmp_path / 'two', expected=manifest['release'])
    calls = []
    def sender(text, settings, dest):
        calls.append(settings.voice)
        shutil.copyfile(audio, dest)
    manager = manager_for(library, config, sender)
    first = manager.profile_catalog()['profiles'][0]
    manager.register_voice('test', 'am_echo')
    second = manager.save_profile(dict(duplicate_of=first['id'], label='Second voice', voice='am_echo'))
    return library, manager, first, second, config, calls


def test_dry_run_multiple_profiles_and_repeated_queue_start_no_synthesis(tmp_path, monkeypatch):
    library, manager, first, second, config, calls = fixture(tmp_path, monkeypatch)
    try:
        def no_start(*args, **kwargs):
            pytest.fail('Queue operation started an engine or network probe')
        monkeypatch.setattr(manager, 'tick', no_start)
        monkeypatch.setattr(manager, '_open', no_start)
        monkeypatch.setattr(manager, 'speech_workers', no_start)
        selectors = [first['label'].upper(), second['id'], first['id']]
        preview = queue_audio(manager, {'packs':['music']}, selectors, dry_run=True)
        assert preview['lectures'] == 2 and preview['voices'] == 2 and preview['requested'] == 4
        assert not manager.jobs.list() and not calls
        actual = queue_audio(manager, {'packs':['music']}, selectors)
        assert actual['new'] == 4 and actual['complete'] == 0
        assert len(manager.jobs.list()) == 4 and JobStore.has_pending(library.store.state)
        claimed = manager.jobs.claim('other-worker', limit=1, lease_seconds=60)
        assert len(claimed) == 1
        repeated = queue_audio(manager, {'packs':['music']}, selectors)
        assert repeated['new'] == 0 and repeated['reused'] == 4
        assert len(manager.jobs.list()) == 4 and not calls
        for record in manager.jobs.list():
            saved = record['specification']['voice_profile']
            assert saved['revision'] in {first['revision'], second['revision']}
            assert saved['recipe']['config']['voice'] in {'af_alloy', 'am_echo'}
    finally:
        manager.close()
    # Closing the short-lived queue manager leaves work for another process.
    assert len(JobStore(library.store.state).list()) == 4
    assert manager.jobs.get(claimed[0]['id'])['owner'] == 'other-worker'
    assert not calls


def test_skip_is_per_profile_revision_and_declared_membership(tmp_path, monkeypatch):
    library, manager, first, second, config, calls = fixture(tmp_path, monkeypatch)
    try:
        prepared = manager.prepare_saved(['music:001000'], first['id'])[0]
        assert finished(manager, prepared['id'])['published']
        report = queue_audio(manager, {'lectures':['music:001000']}, [first['id'], second['id']])
        assert report['lectures'] == 1 and report['complete'] == 1 and report['requested'] == 1
        assert report['jobs'][0]['profile'] == second['id']
        assert all(job['specification']['row']['id'] == 'music:001000' for job in manager.jobs.list())
        updated = manager.save_profile(dict(id=first['id'], expected_revision=first['revision'],
                                            label=first['label'], settings={'title_pause_after':1.2}))
        revised = queue_audio(manager, {'lectures':['music:001000']}, [first['id']])
        assert revised['complete'] == 0 and revised['requested'] == 1
        assert revised['jobs'][0]['profile_revision'] == updated['revision']
    finally:
        manager.close()


def test_invalid_profiles_or_declarations_never_partially_enqueue(tmp_path, monkeypatch):
    library, manager, first, second, config, calls = fixture(tmp_path, monkeypatch)
    try:
        for selection, voices, all_audio in [({'packs':['music']},[first['id'],'unknown'],False),
                                             ({'lectures':['missing:item']},[first['id']],False),
                                             ({'packs':['music']},[first['id']],True)]:
            with pytest.raises((ValueError, KeyError)):
                queue_audio(manager, selection, voices, all_audio=all_audio)
            assert not manager.jobs.list() and not calls
        manager.save_profile(dict(id=second['id'], expected_revision=second['revision'], label=first['label']))
        with pytest.raises(ValueError, match='ambiguous'):
            queue_audio(manager, {'packs':['music']}, [first['label']])
        assert not manager.jobs.list()
        # A late invalid recipe also leaves the earlier valid recipe unqueued.
        original = manager.saved_requests
        def invalid(keys, profile, **kwargs):
            if profile == second['id']:
                raise ValueError('Invalid second recipe')
            return original(keys, profile, **kwargs)
        monkeypatch.setattr(manager, 'saved_requests', invalid)
        with pytest.raises(ValueError):
            queue_audio(manager, {'packs':['music']}, [first['id'], second['id']])
        assert not manager.jobs.list()
    finally:
        manager.close()


def test_queue_cli_accepts_labels_all_and_json_and_voices_is_local(tmp_path, monkeypatch, capsys):
    import ailectures.production as production
    library, manager, first, second, config, calls = fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(production, 'GenerationManager', lambda *args, **kwargs: manager)
    monkeypatch.chdir(tmp_path)
    selection = tmp_path / 'selection.json'
    selection.write_text(json.dumps({'packs':['music']}))
    main(['--library',str(library.store.root),'voices','--tts-config',str(config),'--json'])
    profiles = json.loads(capsys.readouterr().out)
    assert {p['id'] for p in profiles} == {first['id'], second['id']}
    main(['--library',str(library.store.root),'queue','--all','--saved-profile',first['id'],'--dry-run','--json'])
    preview = json.loads(capsys.readouterr().out)
    assert preview['requested'] == 2 and not manager.jobs.list()
    main(['--library',str(library.store.root),'queue','--selection',str(selection),
          '--saved-profile',first['id'],'--saved-profile',second['label'],'--json'])
    report = json.loads(capsys.readouterr().out)
    assert report['requested'] == 4 and not calls


def test_running_server_notices_new_cli_jobs_without_restart_and_playback_only_does_not(tmp_path, monkeypatch):
    import ailectures.production as production
    for playback_only in (False, True):
        folder = tmp_path / str(playback_only)
        folder.mkdir()
        library, manager, first, second, config, calls = fixture(folder, monkeypatch)
        # No manager is supplied to the app. It starts without any pending work.
        monkeypatch.setattr(production, 'GenerationManager', lambda *args, **kwargs: manager)
        try:
            with TestClient(create_app(library.store.root, tts_config=config, interval=0.05, playback_only=playback_only)) as client:
                assert not manager.jobs.list()
                report = queue_audio(manager, {'lectures':['music:001000']}, [first['id']])
                job = report['jobs'][0]['id']
                deadline = time.monotonic() + (4 if not playback_only else 0.3)
                while time.monotonic() < deadline:
                    state = manager.jobs.get(job)
                    if state['published']:
                        break
                    time.sleep(0.03)
                if playback_only:
                    assert state['state'] == 'queued' and not calls
                else:
                    assert state['published'] and calls == ['af_alloy']
                    assert client.get('/api/library/catalog').json()['lectures'][0]['recordings']
        finally:
            manager.close()


def test_pending_check_handles_uninitialized_queue_and_uses_state_without_decoding_specs(tmp_path, monkeypatch):
    assert not JobStore.has_pending(tmp_path)
    with sqlite3.connect(tmp_path / 'production.sqlite3'):
        pass
    assert not JobStore.has_pending(tmp_path)
    store = JobStore(tmp_path)
    from ailectures.core import digest
    store.enqueue([(digest('fixture'), {'request':'fixture'})])
    monkeypatch.setattr(JobStore, 'decode', lambda *args: pytest.fail('Decoded transcript for pending check'))
    assert JobStore.has_pending(tmp_path)
    assert store.states() == {digest('fixture'):'queued'}


def test_real_cli_process_exits_with_unclaimed_jobs_and_no_generation_cache(tmp_path, monkeypatch):
    library, manager, first, second, config, calls = fixture(tmp_path, monkeypatch)
    selection = tmp_path / 'selection.json'
    selection.write_text(json.dumps({'packs':['music']}))
    try:
        result = subprocess.run([sys.executable, '-m', 'ailectures', '--library', str(library.store.root),
            'queue', '--selection', str(selection), '--saved-profile', first['label'],
            '--saved-profile', second['id'], '--tts-config', str(config), '--json'],
            cwd=tmp_path, env={**os.environ, 'PYTHONPATH': str(Path(__file__).resolve().parents[1])},
            capture_output=True, text=True, timeout=15)
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout)['new'] == 4
        assert all(job['state']=='queued' and job['attempts']==0 and job['owner'] is None
                   for job in manager.jobs.list())
        assert not (library.store.root / 'build-cache').exists()
        assert not calls
    finally:
        manager.close()


def test_absent_published_recording_can_be_restored_from_cached_completed_job(tmp_path, monkeypatch):
    from ailectures.core import digest
    library, manager, first, second, config, calls = fixture(tmp_path, monkeypatch)
    try:
        job = manager.prepare_saved(['music:001000'], first['id'])[0]
        assert finished(manager, job['id'])['published']
        library.store.remove('audio-' + digest('music:001000')[:24])
        report = queue_audio(manager, {'lectures':['music:001000']}, [first['id']])
        assert report['retried'] == report['requested'] == 1
        assert report['jobs'][0]['id'] == job['id']
        assert manager.jobs.get(job['id'])['state'] == 'queued'
        assert finished(manager, job['id'])['published']
        assert calls == ['af_alloy']
    finally:
        manager.close()
