"""Selected audio libraries move intact; cleanup is explicit and reference-aware."""
from copy import deepcopy
import json
import os
from pathlib import Path
import time
from zipfile import ZipFile

import pytest
from starlette.testclient import TestClient

from ailectures.core import digest, canonical
from ailectures.deployment import export_deployment, deployment_plan
from ailectures.garbage import garbage_plan, collect_garbage
from ailectures.jobs import JobStore
from ailectures.library import Library
from ailectures.packs import export_release
from ailectures.source_snapshots import save_snapshot
from ailectures.state import ListenerState
from ailectures.storage import restore_library
from ailectures.web import create_app
from test_content_packs import source_pack, media_for


def install(library, tmp_path, namespace='music', text='Hear the interval.', media=True, kind='source'):
    pack=source_pack(namespace,text)
    folder=tmp_path/(namespace+'-'+digest(text+str(time.time_ns()))[:10])
    folder.mkdir()
    recording=media_for(pack,folder) if media else None
    release=export_release(pack,folder/'release',media=[recording] if recording else [],kind=kind)
    previous=next((r for r in library.store.active() if r['pack_id']==namespace),None)
    library.store.install(folder/'release',expected=previous['release'] if previous else None)
    return release,pack


def test_multi_pack_bundle_restores_only_selected_content_and_audio(tmp_path):
    library=Library(tmp_path/'original')
    first,_=install(library,tmp_path)
    install(library,tmp_path,'stories','A second story.')
    install(library,tmp_path,'private','An omitted lecture.')
    ListenerState(library.store.state).create_profile('Do not transfer')
    out=tmp_path/'deployment.zip'
    report=export_deployment(library,{'packs':['music','stories']},out,require_complete=True)
    assert report['lectures']==report['complete']==2
    with ZipFile(out) as archive:
        assert not any('listeners.sqlite3' in key or 'production.sqlite3' in key or '/private/' in key for key in archive.namelist())
    restored=restore_library(out,tmp_path/'restored')
    # Move the source away so absolute paths cannot rescue a broken export.
    (tmp_path/'original').rename(tmp_path/'retired')
    with TestClient(create_app(restored)) as client:
        rows=client.get('/api/library/catalog').json()['lectures']
        assert {r['id'] for r in rows}=={'music:001000','stories:001000'}
        for row in rows:
            row=client.get('/api/library/lectures/'+row['id']).json()
            assert row['recordings'][0]['complete']
            assert client.get(row['recordings'][0]['segments'][0]['url']).content.startswith(b'RIFF')
        assert client.get('/api/listeners').json()['profiles']==[]


def test_collection_selection_trims_order_without_changing_lecture_ids(tmp_path):
    library=Library(tmp_path/'library')
    _,pack=install(library,tmp_path)
    row=deepcopy(pack['lectures']['music:001000']);row['id']='music:002000'
    from ailectures.core import lecture_revision
    row['revision']=lecture_revision(row)
    pack['lectures'][row['id']]=row
    pack['courses']['music:main']['lectures'].append(row['id'])
    pack['courses']['music:one']=dict(id='music:one',title='First only',lectures=['music:001000'],parent='music:main')
    previous=library.store.active()[0]
    export_release(pack,tmp_path/'two')
    library.store.install(tmp_path/'two',expected=previous['release'])
    out=tmp_path/'subset.zip';export_deployment(library,{'collections':['music:one']},out)
    moved=Library(restore_library(out,tmp_path/'new'))
    snapshot=moved.snapshot()
    assert set(snapshot['lectures'])=={'music:001000'}
    assert snapshot['courses']['music:main']['lectures']==['music:001000']
    with pytest.raises(ValueError):deployment_plan(library,{})
    with pytest.raises(ValueError):deployment_plan(library,{'packs':['missing']})


def stale_library(tmp_path):
    library=Library(tmp_path/'library')
    old,pack=install(library,tmp_path,'audio-test','Old spoken text.',kind='media')
    # A current source snapshot supersedes the old media without deleting history.
    row=deepcopy(pack['lectures']['audio-test:001000'])
    from ailectures.core import text_digest, lecture_revision
    row['transcript']='New spoken text.';row['spoken_sha256']=text_digest(row['transcript']);row['source']=row['transcript'];row['revision']=lecture_revision(row)
    pack.update(id='authored-source',lectures={row['id']:row})
    export_release(pack,tmp_path/'current')
    library.store.install(tmp_path/'current')
    path=library.store.packs/'audio-test'/old['release']
    past=time.time()-90*86400
    for item in [*path.rglob('*'),path]: os.utime(item,(past,past))
    return library,old,path


def test_cleanup_is_previewed_and_requires_matching_plan_and_stopped_reader(tmp_path):
    library,old,path=stale_library(tmp_path)
    plan=garbage_plan(library,keep_text_versions=1)
    assert len(plan['candidates'])==1 and path.exists()
    with pytest.raises(ValueError,match='stopped'):
        with TestClient(create_app(library.store.root)):
            collect_garbage(library,plan['plan_id'],keep_text_versions=1)
    with pytest.raises(ValueError,match='preview changed'):
        collect_garbage(library,'wrong',keep_text_versions=1)
    result=collect_garbage(library,plan['plan_id'],keep_text_versions=1)
    assert result['removed']==1 and not path.exists()
    assert 'audio-test:001000' in Library(library.store.root).snapshot()['lectures']
    with library.store.connect() as db:
        assert not db.execute('SELECT 1 FROM releases WHERE release=?',(old['release'],)).fetchone()


def test_cleanup_keeps_progress_references_recent_text_and_running_work(tmp_path):
    library,old,path=stale_library(tmp_path)
    state=ListenerState(library.store.state);who=state.create_profile('Listener')['id']
    with state.connect() as db:
        db.execute('INSERT INTO progress VALUES (?,?,?,?)',(who,'audio-test:001000',1,json.dumps({'release':old['release']})))
    assert not garbage_plan(library,keep_text_versions=1)['candidates']
    with state.connect() as db:db.execute('DELETE FROM progress')
    # A previous authored snapshot keeps the second-most-recent speech identity.
    old_row=json.loads(next(r for r in library.store.active() if r['release']==old['release'])['catalog'])['lectures']
    with library.store.connect() as db:db.execute('INSERT INTO source_snapshots VALUES (?,?)',(digest('old'),json.dumps(old_row)))
    assert not garbage_plan(library)['candidates']
    assert garbage_plan(library,keep_text_versions=1)['candidates']
    JobStore(library.store.state).enqueue([(digest('job'),{'row':next(iter(old_row.values()))})])
    plan=garbage_plan(library,keep_text_versions=1)
    with pytest.raises(ValueError,match='Finish or cancel'):
        collect_garbage(library,plan['plan_id'],keep_text_versions=1)
    assert path.exists()


def test_cleanup_retains_shared_snapshot_text_and_referenced_segment_releases(tmp_path):
    library, old, _ = stale_library(tmp_path)
    media = next(r for r in library.store.active() if r['release'] == old['release'])
    row = json.loads(media['catalog'])['lectures']['audio-test:001000']
    row['recordings'][0]['segments'][0]['_release'] = old['release']
    historical = digest('source snapshot with old audio')
    with library.store.connect() as db:
        save_snapshot(db, historical, {row['id']: row})

    assert not garbage_plan(library)['candidates']
    assert garbage_plan(library, keep_text_versions=1)['candidates']

    state = ListenerState(library.store.state)
    listener = state.create_profile('Listener')['id']
    with state.connect() as db:
        db.execute(
            'INSERT INTO progress VALUES (?,?,?,?)',
            (listener, row['id'], 1, json.dumps({'pack_release': historical})),
        )
    assert not garbage_plan(library, keep_text_versions=1)['candidates']


def test_replaced_release_keeps_surviving_recording_urls_and_cleanup_protection(tmp_path):
    library, replacement, path = stale_library(tmp_path)
    previous = digest('release before removing one recording')
    with library.store.connect() as db:
        db.execute('INSERT INTO release_aliases VALUES (?,?)', (previous, replacement['release']))
    lecture, directory = library.store.historical(previous, 'audio-test:001000')
    recording = lecture['recordings'][0]
    media, _ = library.store.media_file(previous, recording['id'], 0)
    assert directory == path and media.read_bytes().startswith(b'RIFF')
    with pytest.raises(KeyError, match='Unknown recording'):
        library.store.media_file(previous, digest('removed recording'), 0)

    state = ListenerState(library.store.state)
    listener = state.create_profile('Listener')['id']
    with state.connect() as db:
        db.execute(
            'INSERT INTO progress VALUES (?,?,?,?)',
            (listener, lecture['id'], 1, json.dumps({'release': previous})),
        )
    assert not garbage_plan(library, keep_text_versions=1)['candidates']


def test_live_sources_pick_up_published_media_and_http_bundle_restores(tmp_path):
    repo=tmp_path/'repo';source=repo/'draft-stages/tts-music';source.mkdir(parents=True)
    (source/'001000-song.md').write_text('# Intervals\n<!-- BEGIN SPOKEN LECTURE -->\nHear the interval.\n<!-- END SPOKEN LECTURE -->\n')
    (source/'track.json').write_text(json.dumps(dict(id='music',title='Music',lectures=[dict(id='001000',file='001000-song.md')])))
    library=Library(tmp_path/'library',repository=repo)
    pack=source_pack(text='Hear the interval.')
    pack['id']='audio-'+digest('music:001000')[:24]
    recording=media_for(pack,tmp_path)
    export_release(pack,tmp_path/'audio',media=[recording],kind='media')
    library.store.install(tmp_path/'audio')
    with TestClient(create_app(library.store.root,repository=repo)) as client:
        preview=client.post('/api/library/deployment',json=dict(selection={'packs':['music']},preview=True))
        assert preview.status_code==200 and preview.json()['complete']==1
        response=client.post('/api/library/deployment',json=dict(selection={'packs':['music']}))
        assert response.status_code==200
        archive=tmp_path/'download.zip';archive.write_bytes(client.get(response.json()['url']).content)
    repo.rename(tmp_path/'gone')
    new=Library(restore_library(archive,tmp_path/'new'))
    row=new.snapshot()['lectures']['music:001000']
    assert row['recordings'][0]['complete']
    assert row['recordings'][0]['id']==recording[1]['id']


def test_interrupted_cleanup_restores_moves_before_commit_and_finishes_after_commit(tmp_path):
    from ailectures.garbage import recover_garbage
    from ailectures.core import write_json
    library,old,path=stale_library(tmp_path)
    ticket='a'*32;trash=library.store.root/('.gc-'+ticket);trash.mkdir()
    relative=path.relative_to(library.store.root).as_posix()
    write_json(library.store.state/'gc-receipts'/f'{ticket}.json',dict(id=ticket,paths=[relative]))
    path.rename(trash/'0')
    assert recover_garbage(library)==[dict(id=ticket,action='restored')]
    assert path.exists()
    trash.mkdir();path.rename(trash/'0')
    with library.store.connect() as db:
        db.execute('INSERT INTO gc_runs VALUES (?)',(ticket,))
        db.execute('DELETE FROM selections WHERE release=?',(old['release'],))
        db.execute('DELETE FROM releases WHERE release=?',(old['release'],))
    assert recover_garbage(library)==[dict(id=ticket,action='deleted')]
    assert not path.exists() and not trash.exists()


def test_profile_speech_cleanup_keeps_caches_shared_with_current_text(tmp_path):
    from ailectures.voice_profiles import profile_cache_key

    library = Library(tmp_path / "library")
    install(library, tmp_path, media=False)
    current = library.snapshot()["lectures"]["music:001000"]
    profile = dict(id="voice-fixture", revision=digest("recipe"))
    spec = dict(
        row={**current, "spoken_sha256": digest("old text")},
        configuration={},
        voice_profile=profile,
        cache_epoch="reset-fixture",
    )
    jobs = JobStore(library.store.state)
    jobs.clear_voice(jobs.cache_scope(spec), spec["cache_epoch"], lambda: None)
    old_id = digest("old job")
    jobs.enqueue([(old_id, spec)])
    jobs.cancel(old_id)
    cache = (
        library.store.root
        / "build-cache/speech"
        / profile_cache_key(current["id"], profile, spec["cache_epoch"])
    )
    cache.mkdir(parents=True)
    (cache / "page.ogg").write_bytes(b"fixture")
    paths = lambda: {
        row["path"]
        for row in garbage_plan(library, keep_days=0, keep_text_versions=1)[
            "candidates"
        ]
    }
    relative = cache.relative_to(library.store.root).as_posix()
    assert relative in paths()
    jobs.enqueue([(digest("current job"), {**spec, "row": current})])
    assert relative not in paths()
