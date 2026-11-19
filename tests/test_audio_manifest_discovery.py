"""New, independently authored tracks must require no shared reader edits."""
import json

from dkvis.presentation import audio_library


def test_reader_discovers_every_existing_track(tmp_path):
    hub = audio_library.AudioLectureHub(cache=tmp_path / 'audio', profile='kokoro')
    try:
        tracks = {row['id']: row for row in hub.course_tracks() if row['kind'] == 'audio'}
        expected = {}
        for directory in (audio_library.ROOT / 'content').glob('*/track.json'):
            plan = json.loads(directory.read_text(encoding='utf-8'))
            expected[plan['id']] = len(plan['lectures'])
        expected['g2'] = len(hub.engine('kokoro', 'g2')._files())
        assert {name: row['count'] for name, row in tracks.items()} == expected
        for track_id in expected:
            assert len(hub.catalog(track_id)) == expected[track_id]
    finally:
        hub.close()


def test_new_track_does_not_need_registration(monkeypatch, tmp_path):
    drafts = tmp_path / 'draft-stages'
    g2 = drafts / 'tts-lectures'
    g2.mkdir(parents=True)
    music = drafts / 'tts-music-theory'
    music.mkdir(parents=True)
    (music / '001000-musical-intervals.md').write_text(
        '# Musical intervals\n<!-- BEGIN SPOKEN LECTURE -->\n'
        'An interval measures the distance between two pitches.\n'
        '<!-- END SPOKEN LECTURE -->\n', encoding='utf-8')
    (music / 'track.json').write_text(json.dumps({
        'id': 'music-theory', 'title': 'Music Theory and Composition',
        'summary': 'Listening, harmony, and form',
        'lectures': [{'id': '001000', 'file': '001000-musical-intervals.md'}],
    }), encoding='utf-8')
    monkeypatch.setattr(audio_library, 'ROOT', tmp_path)
    monkeypatch.setattr(audio_library, 'SOURCE_DIRECTORY', g2)
    hub = audio_library.AudioLectureHub(sources=g2, cache=tmp_path / 'audio', profile='kokoro')
    try:
        found = next(row for row in hub.course_tracks() if row['id'] == 'music-theory')
        assert found['count'] == 1
        assert hub.detail('001000', 'music-theory')['title'] == 'Musical intervals'
    finally:
        hub.close()
