"""The new question-centered lecture is registered and remains a self-contained recording."""
import json
from pathlib import Path
from starlette.testclient import TestClient
from dkvis.presentation.audio_library import (
    WORLD_RECONSIDERED_DIRECTORY, AudioLectureHub, narration_extractor,
    LECTURE_NAME,
)
from dkvis.presentation.serve import create_app


def test_world_reconsidered_manifest_and_references():
    folder = WORLD_RECONSIDERED_DIRECTORY
    manifest = json.loads((folder/'track.json').read_text())
    assert manifest['id'] == 'world-reconsidered'
    assert [row['id'] for row in manifest['lectures']] == ['001000', '002000', '003000', '004000', '005000']
    assert {row['file'] for row in manifest['lectures']} == {
        p.name for p in folder.iterdir() if p.is_file() and LECTURE_NAME.fullmatch(p.name)
    }
    sources = json.loads((folder/'metadata'/'sources.json').read_text())['sources']
    for row in manifest['lectures']:
        path = folder/row['file']
        raw = path.read_text()
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        assert len(spoken.split()) >= 4000
        assert len(spoken.split()) == row['spoken_words']
        assert 'http' not in spoken
        assert 'in the previous lecture' not in spoken.lower()
        sidecar = json.loads((folder/'metadata'/f"{row['id']}.json").read_text())
        assert sidecar['transcript'] == row['file']
        assert len(sidecar['related_resources']) >= 5
        assert all(item['source_id'] in sources for item in sidecar['related_resources'])
        assert all(source['url'].startswith('https://') for source in sources.values())
        for claim in sidecar['historical_claims']:
            assert claim['anchor'] in spoken
            assert all(source_id in sources for source_id in claim['source_ids'])


def test_world_reconsidered_reader_and_isolation(tmp_path):
    hub = AudioLectureHub(cache=tmp_path/'cache', profile='kokoro')
    render=tmp_path/'renders'
    render.mkdir()
    try:
        with TestClient(create_app(render, audio_library=hub)) as client:
            tracks=client.get('/api/audio-tracks').json()['tracks']
            pilot=next(row for row in tracks if row['id']=='world-reconsidered')
            assert pilot['count'] == 5
            assert pilot['url'] == '/audio?track=world-reconsidered'
            catalog=client.get('/api/audio-lectures?track=world-reconsidered').json()['items']
            assert [row['id'] for row in catalog] == ['001000', '002000', '003000', '004000', '005000']
            for lecture_id in ('001000', '002000', '003000', '004000', '005000'):
                detail=client.get(f'/api/audio-lectures/{lecture_id}?track=world-reconsidered').json()
                assert detail['words'] > 4000
                assert len(detail['related_resources']) >= 5
                assert client.get(f'/api/audio-lectures/{lecture_id}/transcript.txt?track=world-reconsidered').text == detail['transcript']
            assert 'worldReconsideredTrack' in client.get('/audio').text
            assert hub.engine('kokoro','world-reconsidered').cache != hub.engine('kokoro','world-history').cache
    finally:
        hub.close()
