"""New foundational mathematics audio tracks: manuscripts, references and routing."""
import json
from pathlib import Path

import pytest
from starlette.testclient import TestClient

from dkvis.presentation.audio_library import (
    AudioLectureHub, LOGIC_TYPES_DIRECTORY, OPTIMIZATION_DUALITY_DIRECTORY,
    PROBABILITY_MEASURE_DIRECTORY, narration_extractor,
)
from dkvis.presentation.serve import create_app

TRACKS = {
    'logic-types': LOGIC_TYPES_DIRECTORY,
    'optimization-duality': OPTIMIZATION_DUALITY_DIRECTORY,
    'probability-measure': PROBABILITY_MEASURE_DIRECTORY,
}


@pytest.mark.parametrize('track_id,folder', TRACKS.items())
def test_foundation_manuscript_manifest_sources(track_id, folder):
    manifest = json.loads((folder/'track.json').read_text())
    assert manifest['id'] == track_id
    rows = manifest['lectures']
    assert [row['id'] for row in rows] == ['001000']
    catalog = json.loads((folder/'metadata'/'sources.json').read_text())['sources']
    for row in rows:
        path = folder / row['file']
        assert path.is_file()
        assert path.name.startswith(row['id'] + '-')
        source = path.read_text()
        assert source.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert source.count('<!-- END SPOKEN LECTURE -->') == 1
        assert '## Mathematical companion (display only)' in source
        speech = narration_extractor(path)
        assert len(speech.split()) == row['spoken_words']
        assert len(speech.split()) >= 3000
        assert 'http' not in speech
        meta = json.loads((folder/'metadata'/(row['id']+'.json')).read_text())
        assert meta['transcript'] == path.name
        assert len(meta['related_resources']) >= 3
        assert len(meta['historical_claims']) >= 1
        for relation in meta['related_resources']:
            assert relation['source_id'] in catalog
        for claim in meta['historical_claims']:
            assert claim['anchor'] in speech
            assert all(sid in catalog for sid in claim['source_ids'])


def test_three_foundations_audio_reader_independent_tracks(tmp_path):
    hub = AudioLectureHub(cache=tmp_path/'cache', profile='kokoro')
    renders = tmp_path/'renders'
    renders.mkdir()
    try:
        with TestClient(create_app(renders, audio_library=hub)) as client:
            track_resp = client.get('/api/audio-tracks')
            assert track_resp.status_code == 200
            track_rows = {row['id']: row for row in track_resp.json()['tracks']}
            html = client.get('/audio').text
            for track_id in TRACKS:
                assert track_rows[track_id]['count'] == 1
                assert track_rows[track_id]['url'] == '/audio?track=' + track_id
                inventory = client.get('/api/audio-lectures', params={'track':track_id})
                assert inventory.status_code == 200
                assert [row['id'] for row in inventory.json()['items']] == ['001000']
                detail = client.get('/api/audio-lectures/001000', params={'track':track_id})
                assert detail.status_code == 200
                doc = detail.json()
                assert doc['words'] >= 3000
                assert len(doc['related_resources']) >= 3
                transcript = client.get('/api/audio-lectures/001000/transcript.txt',params={'track':track_id})
                assert transcript.status_code == 200
                assert transcript.text == doc['transcript']
                assert hub.engine('kokoro',track_id).cache != hub.engine('kokoro','category-theory').cache
            assert 'logicTypesTrack' in html
            assert 'optimizationDualityTrack' in html
            assert 'probabilityMeasureTrack' in html
            caches = [hub.engine('kokoro',track_id).cache for track_id in TRACKS]
            assert len(set(caches)) == len(caches)
    finally:
        hub.close()
