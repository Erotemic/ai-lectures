"""Modern-literature transcript, citations, and reader registration."""
import json
from starlette.testclient import TestClient
from dkvis.presentation.audio_library import (
    AudioLectureHub, MODERN_LITERATURE_DIRECTORY, narration_extractor
)
from dkvis.presentation.serve import create_app


def test_modern_literature_metadata_and_narration():
    root = MODERN_LITERATURE_DIRECTORY
    manifest = json.loads((root / 'track.json').read_text())
    assert manifest['id'] == 'modern-literature'
    assert manifest['title'].startswith('20th-Century Literature')
    catalog = json.loads((root/'metadata/sources.json').read_text())['sources']
    ids = set()
    for row in manifest['lectures']:
        assert row['id'] not in ids
        ids.add(row['id'])
        path = root / row['file']
        raw = path.read_text()
        assert raw.count('<!-- BEGIN SPOKEN LECTURE -->') == 1
        assert raw.count('<!-- END SPOKEN LECTURE -->') == 1
        speech = narration_extractor(path)
        assert len(speech.split()) == row['spoken_words']
        assert len(speech.split()) >= 4000
        assert 'http' not in speech
        metadata = json.loads((root/'metadata'/(row['id']+'.json')).read_text())
        assert metadata['transcript'] == row['file']
        assert metadata['related_resources']
        for resource in metadata['related_resources']:
            assert resource['source_id'] in catalog
        for claim in metadata['historical_claims']:
            assert speech.count(claim['anchor']) == 1
            assert all(id in catalog for id in claim['source_ids'])


def test_modern_literature_reader(tmp_path):
    hub = AudioLectureHub(cache=tmp_path/'cache', profile='kokoro')
    renders = tmp_path/'renders'
    renders.mkdir()
    try:
        with TestClient(create_app(renders, audio_library=hub)) as client:
            tracks = client.get('/api/audio-tracks').json()['tracks']
            catalog = {item['id']:item for item in tracks}
            assert catalog['modern-literature']['count'] == 9
            assert catalog['modern-literature']['url'] == '/audio?track=modern-literature'
            assert catalog['modern-literature']['label'] == '20th-Century Literature'
            listing = client.get('/api/audio-lectures',params={'track':'modern-literature'})
            assert listing.status_code == 200
            assert [item['id'] for item in listing.json()['items']] == ['001000', '002000', '003000', '004000', '005000', '006000', '007000', '008000', '009000']
            detail = client.get('/api/audio-lectures/001000',params={'track':'modern-literature'})
            assert detail.status_code == 200
            doc = detail.json()
            assert doc['words'] >= 4000
            assert len(doc['related_resources']) >= 5
            txt = client.get('/api/audio-lectures/001000/transcript.txt',params={'track':'modern-literature'})
            assert txt.status_code == 200
            assert txt.text == doc['transcript']
            assert hub.engine('kokoro','modern-literature').cache != hub.engine('kokoro','history').cache
            assert 'modernLiteratureTrack' in client.get('/audio').text
    finally:
        hub.close()


def test_literature_time_period_and_source_anchors():
    import re
    root = MODERN_LITERATURE_DIRECTORY
    manifest = json.loads((root/'track.json').read_text())
    catalog = json.loads((root/'metadata/sources.json').read_text())['sources']
    assert [int(row['id']) for row in manifest['lectures']] == list(range(1000, 10000, 1000))
    for row in manifest['lectures']:
        assert row['draft_status'] == 'substantive'
        assert 20 <= row['estimated_minutes_at_145_wpm'] <= 70
        text = (root/row['file']).read_text()
        assert '<!-- END SPOKEN LECTURE -->' in text and len(text.split('<!-- END SPOKEN LECTURE -->')[1].split()) >= 100
        assert not re.search(r'\b(previous|next) lecture\b', narration_extractor(root/row['file']), re.I)
    assert all(key in catalog for key in ('ml-solitude-ransom','ml-kindred-interview','ml-invisible-loc','ml-dispossessed-interview'))
