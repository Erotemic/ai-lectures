"""Deck integrity and authored lecture production contracts."""
import ast
from pathlib import Path
from dkvis.decks import DECKS, get_deck


def test_registered_decks_have_indexed_authored_narration():
    from dkvis.lectures import lecture_decks
    from dkvis.presentation.narration import read_deck_narration

    assert set(DECKS) == set(lecture_decks())
    for deck in DECKS.values():
        assert deck.narration
        assert list(read_deck_narration(deck.name)) == deck.scene_names


def test_decks_have_unique_scene_names_and_real_source_modules():
    root = Path(__file__).resolve().parents[1]
    for deck in DECKS.values():
        assert len(deck.scene_names) == len(set(deck.scene_names))
        for slide in deck.slides:
            source = root / (slide.module.replace(".", "/") + ".py")
            assert source.is_file(), (deck.name, slide.scene, source)
            classes = {node.name for node in ast.parse(source.read_text()).body if isinstance(node, ast.ClassDef)}
            assert slide.scene in classes, (deck.name, slide.scene, source)


def test_indexed_lectures_have_answerable_review_scenes_and_thinking_time():
    from dkvis.lectures import lecture_decks
    from dkvis.presentation.narration import read_deck_narration
    from dkvis.quiz import REVIEW_SCENES, questions
    for name in lecture_decks():
        rows = questions(name)
        scenes = REVIEW_SCENES[:len(rows)]
        assert get_deck(name).scene_names[-len(rows):] == list(scenes)
        scripts = read_deck_narration(name)
        for scene, question in zip(scenes, rows):
            script = scripts[scene]
            assert len(script.beats) == 2
            assert script.pauses == (question['think_seconds'], 0)
            assert 3 <= len(question['choices']) <= 4
            assert 0 <= question['correct'] < len(question['choices'])
            assert question['explanation'].strip()


def test_numbered_public_names_leave_deck_and_cache_names_stable():
    from dkvis.lectures import lecture_decks, lecture_number, lecture_output_name
    from dkvis.presentation.build import output_name
    for name in lecture_decks():
        number = lecture_number(name)
        assert len(number) == 6 and number.isdigit()
        assert lecture_output_name(name) == f'{number}_{name}'
        assert not output_name(name).startswith(number)
    assert lecture_output_name('unindexed-example') == 'unindexed-example'


def test_existing_public_exports_are_numbered_without_moving_caches(tmp_path):
    from dkvis.lectures import lecture_output_name, number_outputs
    deck = 'prereq-projections'
    files = [f'{deck}.kokoro.narrated.mp4', f'{deck}-light.handout.pdf',
             f'999999_{deck}.standalone.html']
    for name in files:
        (tmp_path/name).write_bytes(name.encode())
    metadata = tmp_path/(files[0]+'.metadata.json')
    metadata.write_text('generation provenance')
    cache = tmp_path/f'{deck}-narrated'
    cache.mkdir()
    (cache/'speech.wav').write_bytes(b'cached speech')
    rows = {'projections': {'deck': deck}}
    number_outputs(rows, tmp_path)
    for name in files:
        bare = name.removeprefix('999999_')
        target = tmp_path/(lecture_output_name(deck)+bare[len(deck):])
        assert target.read_bytes() == name.encode()
        assert not (tmp_path/name).exists()
    assert (tmp_path/(lecture_output_name(deck)+'.kokoro.narrated.mp4.metadata.json')).read_text() == 'generation provenance'
    number_outputs(rows, tmp_path)  # Reapplying preserves outputs and caches.
    assert (cache/'speech.wav').read_bytes() == b'cached speech'


def test_native_lessons_introduce_local_objects_and_separate_numerics():
    from dkvis.lectures import lecture_decks
    from dkvis.quiz import questions
    for name in lecture_decks():
        slides = get_deck(name).slides
        setups = [i for i, s in enumerate(slides) if s.module == 'dkvis.learning.orientation']
        # History has local orientation, and no numerical bonus or formal facts.
        # Imported reference compositions retain their existing local setup.
        if name == 'sine-theta-lecture' or name in lecture_decks('history'):
            continue
        # A factual preview may precede the notation setup. The setup still
        # belongs after the cover and before the formal/numerical companions.
        assert len(setups) == 1 and setups[0] > 0
        bonus = [i for i, s in enumerate(slides) if s.scene.endswith('Computation')]
        assert bonus == [len(slides)-len(questions(name))-1]
        assert slides[bonus[0]].depth == '*'
        assert setups[0] < bonus[0]
        assert all(setups[0] < i < bonus[0] for i, s in enumerate(slides) if 'Lean' in s.scene)


def test_sine_theta_lecture_preserves_its_authored_sequence():
    from dkvis.quiz import SCENES
    from dkvis.lectures import lecture_decks,lecture_number
    from dkvis.presentation.narration import read_deck_narration
    lecture=get_deck('sine-theta-lecture')
    assert lecture.scene_names == [
        'S00TitleShort',
        'S00bSetting',
        'S01Ellipse',
        'S02Perturb',
        'S03bWanted',
        'S03NoGap',
        'S03cUnstable',
        'S04Angle',
        'S05Residual',
        'S06Gap',
        'S07Theorem',
        'S08Why',
        'S11Payoff',
        'D01Planes',
        'S12Lean',
        'P01Claim',
        'P02Counterexample',
        'S14Summary',
    ] + list(SCENES)
    assert 'sine-theta-lecture' in lecture_decks()
    assert lecture_number('sine-theta-lecture')=='003750'
    assert list(read_deck_narration(lecture.name))==lecture.scene_names
