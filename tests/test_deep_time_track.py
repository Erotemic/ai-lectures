"""The deep-time lecture inventory and its audio-reader route."""
import json

from starlette.testclient import TestClient

from dkvis.presentation.audio_library import AudioLectureHub, DEEP_TIME_DIRECTORY, narration_extractor
from dkvis.presentation.serve import create_app


def test_deep_time_catalog_and_sources():
    folder = DEEP_TIME_DIRECTORY
    plan = json.loads((folder / 'track.json').read_text())
    assert plan['id'] == 'deep-time'
    assert len(plan['lectures']) >= 1
    src = json.loads((folder / 'metadata' / 'sources.json').read_text())['sources']
    assert src
    for row in plan['lectures']:
        manuscript = folder / row['file']
        assert manuscript.is_file()
        assert manuscript.name.startswith(row['id'] + '-')
        spoken = narration_extractor(manuscript)
        assert len(spoken.split()) == row['spoken_words']
        metadata = json.loads((folder / 'metadata' / f"{row['id']}.json").read_text())
        assert metadata['transcript'] == row['file']
        assert metadata['related_resources']
        for item in metadata['related_resources']:
            assert item['source_id'] in src
        for item in metadata['historical_claims']:
            assert item['anchor'] in spoken
            assert all(source_id in src for source_id in item['source_ids'])


def test_deep_time_audio_reader(tmp_path):
    hub = AudioLectureHub(cache=tmp_path / 'cache', profile='kokoro')
    renders = tmp_path / 'renders'
    renders.mkdir()
    try:
        assert 'deep-time' in hub.tracks
        assert hub.engine('kokoro', 'deep-time').cache != hub.engine('kokoro', 'g2').cache
        with TestClient(create_app(renders, audio_library=hub)) as client:
            tracks = client.get('/api/audio-tracks')
            assert tracks.status_code == 200
            listing = {row['id']: row for row in tracks.json()['tracks']}
            assert listing['deep-time']['count'] >= 1
            index = client.get('/api/audio-lectures', params={'track': 'deep-time'})
            assert index.status_code == 200
            assert any(item['id'] == '001000' for item in index.json()['items'])
            detail = client.get('/api/audio-lectures/001000', params={'track': 'deep-time'})
            assert detail.status_code == 200
            assert detail.json()['words'] == len(detail.json()['transcript'].split())
            assert detail.json()['related_resources']
            text = client.get('/api/audio-lectures/001000/transcript.txt',
                              params={'track': 'deep-time'})
            assert text.status_code == 200
            assert text.text == detail.json()['transcript']
    finally:
        hub.close()
