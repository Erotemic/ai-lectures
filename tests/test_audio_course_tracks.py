"""Visual, comprehensive, paper, and history track selection with isolated TTS."""
import json
from pathlib import Path
import re
import time

from starlette.testclient import TestClient
from dkvis.presentation.audio_library import (AudioLectureHub, SOURCE_DIRECTORY,
                                             PAPER_DIRECTORY, HISTORY_DIRECTORY,
                                             WORLD_HISTORY_DIRECTORY,
                                             LECTURE_NAME, narration_extractor)
from dkvis.presentation.serve import create_app


def test_g3_syllabus_has_complete_spoken_lectures():
    plan = json.loads((PAPER_DIRECTORY / 'track.json').read_text())
    rows = plan['lectures']
    assert len(rows) >= 27
    assert len({row['id'] for row in rows}) == len(rows)
    disk = {path.name for path in PAPER_DIRECTORY.iterdir()
            if path.is_file() and LECTURE_NAME.fullmatch(path.name)}
    assert {row['file'] for row in rows} == disk
    assert rows[0]['section'] == 'orientation'
    for row in rows:
        path = PAPER_DIRECTORY / row['file']
        raw = path.read_text()
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        # Long-form rewrites: every lecture must still be a complete spoken unit.
        assert len(spoken.split()) >= 1150, row['file']
        assert 'Source declaration excerpts' not in spoken
        assert (PAPER_DIRECTORY/'metadata'/f"{row['id']}.json").is_file()
        if row.get('source_g2'):
            assert re.fullmatch(r'\d{6}', row['source_g2'])


def test_course_tracks_and_track_isolation(tmp_path):
    calls = []

    def synth(text, settings, dest):
        calls.append(text)
        dest.write_bytes(b'ID3' + b'\0' * 1024)

    hub = AudioLectureHub(cache=tmp_path / 'cache', profile='kokoro', sender=synth)
    renders = tmp_path / 'renders'
    renders.mkdir()
    with TestClient(create_app(renders, audio_library=hub)) as client:
        tracks = client.get('/api/audio-tracks').json()['tracks']
        assert [r['id'] for r in tracks] == ['g1', 'g2', 'g3', 'history', 'world-history', 'world-reconsidered', 'category-theory', 'g4']
        assert tracks[0]['url'] == '/'
        assert tracks[1]['count'] >= 154
        g3_count = len(json.loads((PAPER_DIRECTORY/'track.json').read_text())['lectures'])
        assert tracks[2]['count'] == g3_count
        assert tracks[3]['count'] == len(json.loads((HISTORY_DIRECTORY/'track.json').read_text())['lectures'])
        assert tracks[3]['url'] == '/audio?track=history'
        assert len(client.get('/api/audio-lectures?track=history').json()['items']) == tracks[3]['count']
        assert len(client.get('/api/audio-lectures').json()['items']) >= 154
        assert len(client.get('/api/audio-lectures?track=g3').json()['items']) == g3_count
        assert client.get('/api/audio-lectures?track=g2').json()['items'][0]['id'] == '000000'
        assert client.get('/api/audio-lectures?track=g3').json()['items'][0]['id'] == '000000'
        g2 = client.get('/api/audio-lectures/000000?track=g2').json()
        g3 = client.get('/api/audio-lectures/000000?track=g3').json()
        history = client.get('/api/audio-lectures/018000?track=history').json()
        assert g2['title'] != g3['title']
        assert 'Chandler Davis' in history['title']
        assert history['related_resources'] and len(history['related_resources']) >= 3
        for track, doc, lecture_id in (('g2', g2, '000000'), ('g3', g3, '000000'), ('history', history, '018000')):
            text_response = client.get(f'/api/audio-lectures/{lecture_id}/transcript.txt',
                                       params={'track': track})
            assert text_response.status_code == 200
            assert text_response.text == doc['transcript']
        assert client.get('/api/audio-lectures/000000/transcript.txt?track=invalid').status_code == 400
        assert 'When a symmetric matrix or a self-adjoint operator changes a little' in g3['transcript']
        assert not any('<!-- END SPOKEN LECTURE -->' in p for p in g3['pages'])
        assert client.get('/api/audio-lectures?track=../../etc').status_code == 400
        assert client.get('/api/audio-lectures/000000?track=../../etc').status_code == 400
        assert client.post('/api/audio-lectures/000000/pages/0/render',json={'track':'../oops'}).status_code == 400
        assert client.post('/api/audio-lectures/000000/pages/0/render',json={'track':'g3','endpoint':'http://host'}).status_code == 400
        out=client.post('/api/audio-lectures/000000/pages/0/render', json={'track':'g3'})
        assert out.status_code in (200,202), out.text
        result={}
        for _ in range(50):
            result=client.get('/api/audio-lectures/000000/pages/0',params={'track':'g3'}).json()
            if result['state']=='ready': break
            time.sleep(.02)
        assert result['state']=='ready', result
        assert 'track=g3' in result['url']
        assert client.get(result['url']).status_code==200
        assert client.get('/api/audio-lectures/000000/pages/0',params={'track':'g2'}).json()['state']=='missing'
        assert client.get('/api/audio-lectures/018000/pages/0', params={'track':'history'}).json()['state'] == 'missing'
        assert 'g3' in str(hub.engine('kokoro','g3').cache)
        assert hub.engine('kokoro','g2').cache != hub.engine('kokoro','g3').cache
        assert hub.engine('kokoro','history').cache != hub.engine('kokoro','g3').cache
        assert len(calls)==1


def test_g3_learning_resources_reference_existing_catalog(tmp_path):
    hub=AudioLectureHub(cache=tmp_path/'cache')
    try:
        g3=hub.detail('025000', 'g3')
        assert g3['related_resources']
        assert all(row['url'].startswith('https://') for row in g3['related_resources'])
    finally:
        hub.close()


def test_audio_feedback_uses_selected_course_track(tmp_path):
    hub = AudioLectureHub(cache=tmp_path/'cache', profile='kokoro')
    renders = tmp_path/'renders'
    renders.mkdir()
    with TestClient(create_app(renders, audio_library=hub)) as client:
        g2 = client.get('/api/audio-lectures/000000?track=g2').json()
        g3 = client.get('/api/audio-lectures/000000?track=g3').json()
        payload = dict(kind='tts_audio', track='g3', lecture_id='000000',
                       page_index=0, transcript_sha256=g3['transcript_sha256'],
                       profile='kokoro', voice=hub.default_voice, speed=1.0,
                       audio_key=None, playback_seconds=None,
                       text='The opening of the paper track could use another example.')
        response = client.post('/api/feedback', json=payload)
        assert response.status_code == 201, response.text
        saved = json.loads((tmp_path/'feedback'/(response.json()['id']+'.json')).read_text())
        assert saved['track'] == 'g3' and saved['title'] == g3['title']
        assert saved['transcript_sha256'] == g3['transcript_sha256']
        assert client.post('/api/feedback', json={**payload, 'track': 'g2'}).status_code == 409
        assert client.post('/api/feedback', json={**payload,
            'transcript_sha256': g2['transcript_sha256']}).status_code == 409


def test_history_track_manifest_references_and_speech_extraction():
    plan = json.loads((HISTORY_DIRECTORY / 'track.json').read_text(encoding='utf-8'))
    rows = plan['lectures']
    assert len(rows) >= 4
    # A promoted history biography must be playable and no longer archived.
    assert {'009000', '011000'} <= {row['id'] for row in rows}
    assert not (HISTORY_DIRECTORY / 'stubs' / '009000-riesz.md').exists()
    assert not (HISTORY_DIRECTORY / 'stubs' / '011000-schatten.md').exists()
    assert len({row['id'] for row in rows}) == len(rows)
    assert len({row['person'] for row in rows}) == len(rows)
    assert len(list(HISTORY_DIRECTORY.glob('[0-9]'*6 + '-*.md'))) == len(rows)
    catalog = json.loads((HISTORY_DIRECTORY / 'metadata' / 'sources.json').read_text())['sources']
    archive = json.loads((HISTORY_DIRECTORY / 'stubs' / 'manifest.json').read_text())
    assert len(rows) + len(archive['lectures']) >= 28
    assert not {r['id'] for r in rows} & {r['id'] for r in archive['lectures']}
    assert all((HISTORY_DIRECTORY / 'stubs' / r['file']).is_file() for r in archive['lectures'])
    assert len(catalog) >= 84
    for row in rows:
        path = HISTORY_DIRECTORY / row['file']
        raw = path.read_text(encoding='utf-8')
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        assert len(spoken.split()) >= 3700, row['id']
        assert abs(len(spoken.split()) - row['spoken_words']) <= 3
        assert 'http' not in spoken
        metadata = json.loads((HISTORY_DIRECTORY / 'metadata' / f"{row['id']}.json").read_text())
        assert metadata['transcript'] == path.name
        for resource in metadata['related_resources']:
            assert resource['source_id'] in catalog
            assert catalog[resource['source_id']]['url'].startswith('https://')

def test_history_audio_and_feedback_are_isolated_from_math_tracks(tmp_path):
    def synth(text, settings, dest):
        dest.write_bytes(b'ID3' + b'\0' * 1024)
    hub = AudioLectureHub(cache=tmp_path / 'cache', profile='kokoro', sender=synth)
    renders = tmp_path / 'renders'
    renders.mkdir()
    with TestClient(create_app(renders, audio_library=hub)) as client:
        history = client.get('/api/audio-lectures/018000?track=history').json()
        payload = dict(kind='tts_audio', track='history', lecture_id='018000',
                       page_index=0, transcript_sha256=history['transcript_sha256'],
                       profile='kokoro', voice=hub.default_voice, speed=1.0,
                       audio_key=None, playback_seconds=None,
                       text='Another explanation of the projection example would help.')
        response = client.post('/api/feedback', json=payload)
        assert response.status_code == 201, response.text
        saved = json.loads((tmp_path/'feedback'/(response.json()['id']+'.json')).read_text())
        assert saved['track'] == 'history' and saved['title'] == history['title']
        assert client.post('/api/feedback', json={**payload, 'track': 'g2'}).status_code == 409
        result = client.post('/api/audio-lectures/018000/pages/0/render',
                             json={'track':'history'})
        assert result.status_code in (200, 202), result.text
        for _ in range(50):
            status = client.get('/api/audio-lectures/018000/pages/0',
                                params={'track':'history'}).json()
            if status['state'] == 'ready':
                break
            time.sleep(.02)
        assert status['state'] == 'ready', status
        assert 'track=history' in status['url']
        assert client.get(status['url']).status_code == 200
        assert client.get('/api/audio-lectures/018000/pages/0',
                          params={'track':'g2'}).json()['state'] == 'missing'


def test_world_history_manifest_and_spoken_lectures():
    plan = json.loads((WORLD_HISTORY_DIRECTORY / 'track.json').read_text())
    rows = plan['lectures']
    assert plan['id'] == 'world-history'
    # The two founding lectures keep their stable identifiers at the front.
    assert [row['id'] for row in rows][:2] == ['001000', '002000']
    assert len(rows) >= 2
    assert len({row['id'] for row in rows}) == len(rows)
    assert {row['file'] for row in rows} == {
        path.name for path in WORLD_HISTORY_DIRECTORY.iterdir()
        if path.is_file() and LECTURE_NAME.fullmatch(path.name)
    }
    sources = json.loads((WORLD_HISTORY_DIRECTORY / 'metadata' / 'sources.json').read_text())['sources']
    for row in rows:
        path = WORLD_HISTORY_DIRECTORY / row['file']
        raw = path.read_text(encoding='utf-8')
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        assert 3400 <= len(spoken.split()) <= 6500
        assert len(spoken.split()) == row['spoken_words']
        assert 'http' not in spoken  # reading references stay outside the audio
        metadata = json.loads((WORLD_HISTORY_DIRECTORY / 'metadata' / f"{row['id']}.json").read_text())
        assert metadata['transcript'] == row['file']
        assert len(metadata['related_resources']) >= 3
        for resource in metadata['related_resources']:
            assert resource['source_id'] in sources
            assert sources[resource['source_id']]['url'].startswith('https://')


def test_world_history_reader_api_and_isolated_audio(tmp_path):
    def synth(text, settings, dest):
        dest.write_bytes(b'ID3' + b'\0' * 1024)

    hub = AudioLectureHub(cache=tmp_path / 'cache', profile='kokoro', sender=synth)
    renders = tmp_path / 'renders'
    renders.mkdir()
    with TestClient(create_app(renders, audio_library=hub)) as client:
        tracks = client.get('/api/audio-tracks').json()['tracks']
        world = next(row for row in tracks if row['id'] == 'world-history')
        world_count = len(json.loads(
            (WORLD_HISTORY_DIRECTORY / 'track.json').read_text())['lectures'])
        assert world['count'] == world_count
        assert world['url'] == '/audio?track=world-history'
        catalog = client.get('/api/audio-lectures?track=world-history').json()['items']
        assert [row['id'] for row in catalog] == [
            row['id'] for row in json.loads(
                (WORLD_HISTORY_DIRECTORY / 'track.json').read_text())['lectures']]
        assert [row['id'] for row in catalog][:2] == ['001000', '002000']
        gilgamesh = client.get('/api/audio-lectures/001000?track=world-history').json()
        mary = client.get('/api/audio-lectures/002000?track=world-history').json()
        assert gilgamesh['page_count'] > 20 and mary['page_count'] > 20
        assert len(gilgamesh['related_resources']) >= 3
        assert len(mary['related_resources']) >= 3
        assert client.get('/api/audio-lectures/001000/transcript.txt?track=world-history').text == gilgamesh['transcript']
        assert client.get('/api/audio-lectures/002000/transcript.txt?track=world-history').text == mary['transcript']
        assert client.get('/api/audio-lectures?track=world-history/../../').status_code == 400
        assert hub.engine('kokoro', 'world-history').cache != hub.engine('kokoro', 'history').cache
        assert hub.engine('kokoro', 'world-history').cache != hub.engine('kokoro', 'g2').cache
        assert hub.engine('kokoro', 'world-history').cache != hub.engine('kokoro', 'g3').cache
        result = client.post('/api/audio-lectures/001000/pages/0/render', json={'track': 'world-history'})
        assert result.status_code in (200, 202), result.text
        for _ in range(50):
            state = client.get('/api/audio-lectures/001000/pages/0', params={'track': 'world-history'}).json()
            if state['state'] == 'ready':
                break
            time.sleep(.02)
        assert state['state'] == 'ready'
        assert 'track=world-history' in state['url']
        assert client.get(state['url']).status_code == 200
        for other in ['g2', 'g3', 'history']:
            response = client.get('/api/audio-lectures/001000/pages/0', params={'track': other})
            if response.status_code == 200:
                assert response.json()['state'] == 'missing'
            else:
                assert response.status_code == 404  # this track has no lecture 001000
