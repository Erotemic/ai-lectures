"""Visual, comprehensive, paper, and history track selection with isolated TTS."""
import json
from pathlib import Path
import re
import time

from starlette.testclient import TestClient
from dkvis.presentation.audio_library import AudioLectureHub, SOURCE_DIRECTORY, PAPER_DIRECTORY, HISTORY_DIRECTORY, narration_extractor
from dkvis.presentation.serve import create_app


def test_g3_syllabus_has_27_complete_spoken_lectures():
    plan = json.loads((PAPER_DIRECTORY / 'track.json').read_text())
    rows = plan['lectures']
    assert len(rows) == 27
    assert len({row['id'] for row in rows}) == 27
    assert len(list(PAPER_DIRECTORY.glob('[0-9]' * 6 + '-*.md'))) == 27
    assert rows[0]['section'] == 'orientation'
    assert [row['section'] for row in rows[-6:]] == ['section4-transport'] * 6
    assert [row['id'] for row in rows[-6:]] == [
        '017000','018000','018500','019000','024000','025000']
    assert [row['source_g2'] for row in rows[-6:]] == [
        '130000', '131000', '132000', '133000', '134000', '145000']
    for row in rows:
        path = PAPER_DIRECTORY / row['file']
        raw = path.read_text()
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        assert len(spoken.split()) >= 1150, row['file']
        assert len(spoken.split()) <= 1750, row['file']
        assert 'Source declaration excerpts' not in spoken
        assert (PAPER_DIRECTORY/'metadata'/f"{row['id']}.json").is_file()


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
        assert [r['id'] for r in tracks] == ['g1', 'g2', 'g3', 'history', 'g4']
        assert tracks[0]['url'] == '/'
        assert tracks[1]['count'] >= 154
        assert tracks[2]['count'] == 27
        assert tracks[3]['count'] == 28
        assert tracks[3]['url'] == '/audio?track=history'
        assert len(client.get('/api/audio-lectures?track=history').json()['items']) == 28
        assert len(client.get('/api/audio-lectures').json()['items']) >= 154
        assert len(client.get('/api/audio-lectures?track=g3').json()['items']) == 27
        assert client.get('/api/audio-lectures?track=g2').json()['items'][0]['id'] == '000000'
        assert client.get('/api/audio-lectures?track=g3').json()['items'][0]['id'] == '000000'
        g2 = client.get('/api/audio-lectures/000000?track=g2').json()
        g3 = client.get('/api/audio-lectures/000000?track=g3').json()
        history = client.get('/api/audio-lectures/001000?track=history').json()
        assert g2['title'] != g3['title']
        assert 'Sylvester' in history['title']
        assert history['related_resources'] and len(history['related_resources']) == 3
        for track, doc, lecture_id in (('g2', g2, '000000'), ('g3', g3, '000000'), ('history', history, '001000')):
            text_response = client.get(f'/api/audio-lectures/{lecture_id}/transcript.txt',
                                       params={'track': track})
            assert text_response.status_code == 200
            assert text_response.text == doc['transcript']
        assert client.get('/api/audio-lectures/000000/transcript.txt?track=invalid').status_code == 400
        assert 'An eigenvector can change' in g3['transcript']
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
        assert client.get('/api/audio-lectures/001000/pages/0', params={'track':'history'}).json()['state'] == 'missing'
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
    assert len(rows) == 28
    assert len({row['id'] for row in rows}) == len(rows)
    assert len({row['person'] for row in rows}) == len(rows)
    assert len(list(HISTORY_DIRECTORY.glob('[0-9]'*6 + '-*.md'))) == len(rows)
    catalog = json.loads((HISTORY_DIRECTORY / 'metadata' / 'sources.json').read_text())['sources']
    assert len(catalog) == 84
    for row in rows:
        path = HISTORY_DIRECTORY / row['file']
        raw = path.read_text(encoding='utf-8')
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        assert len(spoken.split()) >= 250, row['id']
        assert len(spoken.split()) < 700, row['id']
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
        history = client.get('/api/audio-lectures/001000?track=history').json()
        payload = dict(kind='tts_audio', track='history', lecture_id='001000',
                       page_index=0, transcript_sha256=history['transcript_sha256'],
                       profile='kokoro', voice=hub.default_voice, speed=1.0,
                       audio_key=None, playback_seconds=None,
                       text='An additional explanation of the Sylvester example would help.')
        response = client.post('/api/feedback', json=payload)
        assert response.status_code == 201, response.text
        saved = json.loads((tmp_path/'feedback'/(response.json()['id']+'.json')).read_text())
        assert saved['track'] == 'history' and saved['title'] == history['title']
        assert client.post('/api/feedback', json={**payload, 'track': 'g2'}).status_code == 409
        result = client.post('/api/audio-lectures/001000/pages/0/render',
                             json={'track':'history'})
        assert result.status_code in (200, 202), result.text
        for _ in range(50):
            status = client.get('/api/audio-lectures/001000/pages/0',
                                params={'track':'history'}).json()
            if status['state'] == 'ready':
                break
            time.sleep(.02)
        assert status['state'] == 'ready', status
        assert 'track=history' in status['url']
        assert client.get(status['url']).status_code == 200
        assert client.get('/api/audio-lectures/001000/pages/0',
                          params={'track':'g2'}).json()['state'] == 'missing'
