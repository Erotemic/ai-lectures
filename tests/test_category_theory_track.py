"""Check the category-theory audio track's integrity and reader integration."""
import json
from pathlib import Path
from starlette.testclient import TestClient
from dkvis.presentation.audio_library import (
    CATEGORY_THEORY_DIRECTORY, LECTURE_NAME, AudioLectureHub, narration_extractor,
)
from dkvis.presentation.serve import create_app


def test_category_theory_manuscripts_and_references():
    root = CATEGORY_THEORY_DIRECTORY
    manifest = json.loads((root / 'track.json').read_text())
    rows = manifest['lectures']
    assert manifest['id'] == 'category-theory'
    assert [row['id'] for row in rows] == [f'{n:03d}000' for n in range(1, 9)]
    actual = {p.name for p in root.iterdir() if p.is_file() and LECTURE_NAME.fullmatch(p.name)}
    assert {row['file'] for row in rows} == actual
    catalog = json.loads((root/'metadata'/'sources.json').read_text())['sources']
    for row in rows:
        path = root/row['file']
        raw = path.read_text()
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        speech = narration_extractor(path)
        assert len(speech.split()) >= 3000, path.name
        assert len(speech.split()) == row['spoken_words']
        assert 'http' not in speech
        sidecar = json.loads((root/'metadata'/f"{row['id']}.json").read_text())
        assert sidecar['transcript'] == path.name
        assert len(sidecar['related_resources']) >= 3
        for reading in sidecar['related_resources']:
            assert reading['source_id'] in catalog
        for claim in sidecar['historical_claims']:
            assert claim['anchor'] in speech
            assert all(ref in catalog for ref in claim['source_ids'])


def test_category_theory_in_reader(tmp_path):
    hub = AudioLectureHub(cache=tmp_path/'cache', profile='kokoro')
    renders = tmp_path/'renders'
    renders.mkdir()
    try:
        with TestClient(create_app(renders, audio_library=hub)) as client:
            tracks = client.get('/api/audio-tracks').json()['tracks']
            category = next(row for row in tracks if row['id'] == 'category-theory')
            assert category['count'] == 8
            assert category['url'] == '/audio?track=category-theory'
            rows = client.get('/api/audio-lectures?track=category-theory').json()['items']
            assert [row['id'] for row in rows] == [f'{n:03d}000' for n in range(1, 9)]
            for row in rows:
                lecture_id=row['id']
                detail=client.get(f'/api/audio-lectures/{lecture_id}?track=category-theory').json()
                assert detail['words'] >= 3000
                assert len(detail['related_resources']) >= 3
                assert (client.get(f'/api/audio-lectures/{lecture_id}/transcript.txt',
                                   params={'track':'category-theory'}).text == detail['transcript'])
            assert 'categoryTheoryTrack' in client.get('/audio').text
            assert hub.engine('kokoro','category-theory').cache != hub.engine('kokoro','world-reconsidered').cache
    finally:
        hub.close()
