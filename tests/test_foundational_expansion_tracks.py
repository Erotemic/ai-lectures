"""Four independent opening lecture tracks, source records, and reader routing."""
import json
from pathlib import Path

import pytest
from starlette.testclient import TestClient

from dkvis.presentation.audio_library import (
    AudioLectureHub, MODERN_WORLD_DIRECTORY, PHYSICAL_WORLD_DIRECTORY,
    ANALYSIS_DIRECTORY, NUMERICAL_ANALYSIS_DIRECTORY, narration_extractor,
)
from dkvis.presentation.serve import create_app

TRACKS = {
    'modern-world': MODERN_WORLD_DIRECTORY,
    'physical-world': PHYSICAL_WORLD_DIRECTORY,
    'analysis': ANALYSIS_DIRECTORY,
    'numerical-analysis': NUMERICAL_ANALYSIS_DIRECTORY,
}


@pytest.mark.parametrize('track,folder', TRACKS.items())
def test_new_track_catalog_and_spoken_region(track, folder):
    manifest = json.loads((folder/'track.json').read_text())
    assert manifest['id'] == track
    assert [r['id'] for r in manifest['lectures']] == ['001000', '002000']
    catalog = json.loads((folder/'metadata'/'sources.json').read_text())['sources']
    for row in manifest['lectures']:
        path = folder / row['file']
        speech = narration_extractor(path)
        assert len(speech.split()) == row['spoken_words']
        assert len(speech.split()) >= 3000
        assert 'http' not in speech
        meta = json.loads((folder/'metadata'/f"{row['id']}.json").read_text())
        assert meta['transcript'] == row['file']
        assert len(meta['related_resources']) >= 3
        for res in meta['related_resources']:
            assert res['source_id'] in catalog
        for claim in meta['historical_claims']:
            assert claim['anchor'] in speech
            assert all(sid in catalog for sid in claim['source_ids'])


def test_new_lecture_tracks_are_retrievable_and_isolated(tmp_path):
    hub = AudioLectureHub(cache=tmp_path/'cache',profile='kokoro')
    renders = tmp_path/'renders'
    renders.mkdir()
    try:
        with TestClient(create_app(renders, audio_library=hub)) as client:
            response = client.get('/api/audio-tracks')
            assert response.status_code == 200
            catalog = {t['id']: t for t in response.json()['tracks']}
            html = client.get('/audio').text
            caches = []
            for track in TRACKS:
                assert catalog[track]['count'] == 2
                assert catalog[track]['url'] == f'/audio?track={track}'
                listing = client.get('/api/audio-lectures',params={'track':track})
                assert listing.status_code == 200
                assert [i['id'] for i in listing.json()['items']] == ['001000', '002000']
                for lecture_id in ('001000', '002000'):
                    doc = client.get(f'/api/audio-lectures/{lecture_id}',params={'track':track})
                    assert doc.status_code == 200
                    assert doc.json()['words'] >= 3000
                    transcript = client.get(f'/api/audio-lectures/{lecture_id}/transcript.txt',params={'track':track})
                    assert transcript.status_code == 200
                    assert transcript.text == doc.json()['transcript']
                caches.append(hub.engine('kokoro',track).cache)
            assert len(set(caches)) == len(caches)
            for id_ in ['modernWorldTrack','physicalWorldTrack','analysisTrack','numericalAnalysisTrack']:
                assert id_ in html
    finally:
        hub.close()
