"""Short standard-library regression tests for the separate score representations."""
import copy
import json
import unittest

import validate as v


class ScoresTest(unittest.TestCase):
    def test_all_source_scores(self):
        self.assertEqual(v.main(), 0)

    def test_exact_event_timing(self):
        expected = [
            {'at': '0', 'pitch': 'D4', 'dur': '1/2'},
            {'at': '1/2', 'pitch': 'E4', 'dur': '1/2'},
            {'at': '1', 'pitch': 'F4', 'dur': '1'},
            {'at': '2', 'pitch': 'G4', 'dur': '1'},
            {'at': '3', 'pitch': 'A4', 'dur': '1'},
        ]
        self.assertEqual(v.note_events('D4 e, E4 e, F4 q, G4 q, A4 q'), expected)
        v.validate_events(expected, v.Fraction(4), 'four-beat example')

    def test_pitch_intervals_are_not_interchangeable(self):
        self.assertEqual(v.midi('E4') - v.midi('D4'), 2)
        self.assertEqual(v.midi('G4') - v.midi('D4'), 5)
        self.assertEqual(v.midi('Bb3'), v.midi('A#3'))

    def test_reject_out_of_bar_note(self):
        data = v.note_events('C4 q, D4 q, E4 q, F4 q')
        data[-1]['dur'] = '2'
        with self.assertRaisesRegex(ValueError, 'out-of-bounds'):
            v.validate_events(data, v.Fraction(4), 'overfull bar')

    def test_reject_changed_json_vs_source(self):
        data = json.loads(v.DATA.read_text(encoding='utf-8'))
        example = next(x for x in data['examples'] if x['id'] == '012000-sixteen-bar-workshop')
        damaged = copy.deepcopy(example)
        damaged['bars'][0]['melody'][0]['pitch'] = 'E4'
        with self.assertRaisesRegex(ValueError, 'melody differs from source'):
            v.validate_score(damaged)

    def test_reject_missing_beat(self):
        events = v.note_events('C4 q, D4 q, E4 q')
        with self.assertRaisesRegex(ValueError, 'part ends at'):
            v.validate_events(events, v.Fraction(4), 'incomplete bar')


if __name__ == '__main__':
    unittest.main()
