"""Foundational audio tracks: manifest-driven indexes, sources, reader routing.

Do not impose a minimum or maximum length on a spoken lecture. A transcript
is accepted when its index, extraction, and references agree; pedagogy is not
a word-count threshold. Independent track extensions may add new lectures.
"""
import json

import pytest
from starlette.testclient import TestClient

from dkvis.presentation.audio_library import AudioLectureHub, ROOT, narration_extractor
from dkvis.presentation.serve import create_app

TRACKS = {slug: ROOT / 'draft-stages' / ('tts-' + slug) for slug in (
    'modern-world', 'physical-world', 'analysis', 'numerical-analysis')}


def indexed_rows(folder):
    manifest = json.loads((folder / 'track.json').read_text(encoding='utf-8'))
    rows = manifest['lectures']
    ids = [row['id'] for row in rows]
    names = [row['file'] for row in rows]
    assert ids and ids == sorted(set(ids))
    assert len(names) == len(set(names))
    actual = {path.name for path in folder.glob('[0-9][0-9][0-9][0-9][0-9][0-9]-*.md')}
    assert set(names) == actual, (sorted(set(names) - actual), sorted(actual - set(names)))
    return manifest, rows


@pytest.mark.parametrize('track,folder', TRACKS.items())
def test_new_track_catalog_and_spoken_region(track, folder):
    manifest, rows = indexed_rows(folder)
    assert manifest['id'] == track
    sources = json.loads((folder / 'metadata' / 'sources.json').read_text())['sources']
    for row in rows:
        assert row['file'].startswith(row['id'] + '-')
        path = folder / row['file']
        source_text = path.read_text(encoding='utf-8')
        assert source_text.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert source_text.count('<!-- END SPOKEN LECTURE -->') == 1
        spoken = narration_extractor(path)
        assert spoken.strip()
        assert len(spoken.split()) == row['spoken_words']
        assert 'http' not in spoken
        meta = json.loads((folder / 'metadata' / f"{row['id']}.json").read_text())
        assert meta['transcript'] == row['file']
        for resource in meta['related_resources']:
            assert resource['source_id'] in sources
        for claim in meta['historical_claims']:
            assert claim['anchor'] in spoken
            assert all(source_id in sources for source_id in claim['source_ids'])


def test_foundational_audio_reader_retrievable_and_isolated(tmp_path):
    hub = AudioLectureHub(cache=tmp_path / 'cache', profile='kokoro')
    renders = tmp_path / 'renders'
    renders.mkdir()
    try:
        with TestClient(create_app(renders, audio_library=hub)) as client:
            response = client.get('/api/audio-tracks')
            assert response.status_code == 200
            catalog = {row['id']: row for row in response.json()['tracks']}
            html = client.get('/audio')
            assert html.status_code == 200
            assert 'courseTracks' in html.text  # shared baseline renders data-driven navigation
            caches = []
            for track, folder in TRACKS.items():
                _, rows = indexed_rows(folder)
                ids = [row['id'] for row in rows]
                assert catalog[track]['count'] == len(ids)
                assert catalog[track]['url'] == f'/audio?track={track}'
                listing = client.get('/api/audio-lectures', params={'track': track})
                assert listing.status_code == 200
                assert [item['id'] for item in listing.json()['items']] == ids
                for row in rows:
                    lecture_id = row['id']
                    detail = client.get(f'/api/audio-lectures/{lecture_id}', params={'track': track})
                    assert detail.status_code == 200
                    doc = detail.json()
                    assert doc['words'] == row['spoken_words']
                    transcript = client.get(
                        f'/api/audio-lectures/{lecture_id}/transcript.txt',
                        params={'track': track})
                    assert transcript.status_code == 200
                    assert transcript.text == doc['transcript']
                caches.append(hub.engine('kokoro', track).cache)
            assert len(set(caches)) == len(caches)
    finally:
        hub.close()
