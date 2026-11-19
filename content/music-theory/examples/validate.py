#!/usr/bin/env python3
"""Validate Agent D's text-only reference scores against their lecture tables.

No dependencies, binary music assets, network access, playback, or shared repo edits.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
import re
import sys

TRACK = Path(__file__).resolve().parents[1]
DATA = Path(__file__).with_name('scores.json')
DURATION = {
    'e': Fraction(1, 2), 'q': Fraction(1), 'h': Fraction(2),
    'w': Fraction(4), 'dq': Fraction(3, 2),
    'eighth': Fraction(1, 2), 'quarter': Fraction(1),
    'half': Fraction(2), 'whole': Fraction(4),
}
PITCH = re.compile(r'^([A-G])([#b]?)(-?\d+)$')
SEMITONE = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
CHORD = {
    'C': (0, 4, 7), 'Am': (9, 0, 4), 'F': (5, 9, 0),
    'G': (7, 11, 2), 'Dm': (2, 5, 9), 'Em': (4, 7, 11),
    'D7': (2, 6, 9, 0), 'G7': (7, 11, 2, 5),
    'Fm': (5, 8, 0), 'A7': (9, 1, 4, 7),
}


def fail(message: str) -> None:
    raise ValueError(message)


def frac(value: str | int) -> Fraction:
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError, TypeError) as error:
        raise ValueError(f'Invalid rational time {value!r}') from error


def normalized(value: Fraction) -> str:
    return str(value)


def midi(pitch: str) -> int:
    match = PITCH.fullmatch(pitch)
    if not match:
        fail(f'Invalid scientific pitch spelling: {pitch!r}')
    name, accidental, octave = match.groups()
    return (int(octave) + 1) * 12 + SEMITONE[name] + {'': 0, '#': 1, 'b': -1}[accidental]


def note_events(note_text: str, default_duration: str | None = None, separator: str = ',') -> list[dict]:
    """Parse a source-table's pitch+duration cells (no instrument assumptions)."""
    result = []
    time = Fraction(0)
    for raw in note_text.split(separator):
        token = raw.strip()
        if not token:
            fail(f'Empty note token in {note_text!r}')
        parts = token.split()
        if len(parts) == 1 and default_duration is not None:
            pitch, dur_token = parts[0], default_duration
        elif len(parts) == 2:
            pitch, dur_token = parts
        else:
            fail(f'Expected pitch and duration in {token!r}')
        if dur_token not in DURATION:
            fail(f'Unsupported duration {dur_token!r} in {token!r}')
        midi(pitch)
        duration = DURATION[dur_token]
        result.append({'at': normalized(time), 'pitch': pitch, 'dur': normalized(duration)})
        time += duration
    return result


def source_table(path: Path, first_header: str) -> tuple[list[str], list[list[str]]]:
    lines = path.read_text(encoding='utf-8').splitlines()
    for n, line in enumerate(lines):
        if line.startswith('|'):
            cells = [item.strip() for item in line.strip().strip('|').split('|')]
            if cells[0] == first_header:
                if n + 1 >= len(lines) or not re.fullmatch(r'[|\s:\-]+', lines[n + 1]):
                    fail(f'No Markdown table divider after {path}:{n+1}')
                body = []
                for row in lines[n + 2:]:
                    if not row.startswith('|'):
                        break
                    items = [item.strip() for item in row.strip().strip('|').split('|')]
                    if len(items) != len(cells):
                        fail(f'Incorrect table width at {path}: {row!r}')
                    body.append(items)
                return cells, body
    fail(f'No table headed {first_header!r} in {path.name}')


def column(header: list[str], fragment: str) -> int:
    indices = [i for i, name in enumerate(header) if fragment.lower() in name.lower()]
    if len(indices) != 1:
        fail(f'Expected one column matching {fragment!r}; found {header}')
    return indices[0]


def chord_name(cell: str) -> str:
    if ':' in cell:
        cell = cell.split(':', 1)[0]
    if ' major' in cell:
        cell = cell.split(' major')[0]
    return cell.split(' (', 1)[0].strip()


def validate_events(events: list[dict], bar_length: Fraction, label: str,
                    *, filled: bool = True) -> None:
    time = Fraction(0)
    for event in events:
        if set(event) != {'at', 'pitch', 'dur'}:
            fail(f'{label}: event fields must be at, pitch, dur: {event}')
        onset, duration = frac(event['at']), frac(event['dur'])
        midi(event['pitch'])
        if duration <= 0 or onset < 0 or onset + duration > bar_length:
            fail(f'{label}: out-of-bounds event {event}')
        if onset < time:
            fail(f'{label}: overlapping notes {event}')
        if filled and onset != time:
            fail(f'{label}: unexplained gap before {event}')
        time = onset + duration
    if filled and time != bar_length:
        fail(f'{label}: part ends at {time}, expected {bar_length}')


def validate_score(score: dict) -> int:
    sid = score['id']
    path = TRACK / score['source']
    if not path.is_file() or path.parent != TRACK:
        fail(f'{sid}: source manuscript must be at the track root: {path}')
    if not path.name.startswith(score['lecture_id'] + '-'):
        fail(f'{sid}: lecture_id does not match the source')
    top, bottom = [int(x) for x in score['meter'].split('/')]
    bar_len = Fraction(4 * top, bottom)
    if bar_len <= 0:
        fail(f'{sid}: invalid meter')
    header, rows = source_table(path, score.get('source_header', 'Bar'))
    if len(rows) != len(score['bars']):
        fail(f'{sid}: score has {len(score["bars"])} bars but table has {len(rows)}')
    melody_column = column(header, score.get('melody_column', 'melody'))
    harmony_column = column(header, score.get('harmony_column', 'chord'))
    bass_column = column(header, 'bass') if score.get('has_bass', False) else None
    for row, bar in zip(rows, score['bars']):
        number = int(row[0])
        if number != bar['bar']:
            fail(f'{sid}: bars are out of order, found {number} vs {bar["bar"]}')
        if chord_name(row[harmony_column]) != bar['chord']:
            fail(f'{sid}: chord mismatch at bar {number}')
        if bar['chord'] not in CHORD:
            fail(f'{sid}: unknown chord {bar["chord"]!r}')
        expected = note_events(row[melody_column])
        if bar['melody'] != expected:
            fail(f'{sid}: melody differs from source table at bar {number}:\n'
                 f'  source: {expected}\n  JSON:   {bar["melody"]}')
        validate_events(bar['melody'], bar_len, f'{sid} melody bar {number}')
        if bass_column is not None:
            expected_bass = note_events(row[bass_column], default_duration='whole')
            if bar.get('bass') != expected_bass:
                fail(f'{sid}: bass differs from source at bar {number}')
            validate_events(bar['bass'], bar_len, f'{sid} bass bar {number}')
        if 'section' in bar:
            if row[column(header, 'section')] != bar['section']:
                fail(f'{sid}: section mismatch at bar {number}')
        actual_nonchord = sorted({event['pitch'].rstrip('0123456789-') for event in bar['melody']
                                  if midi(event['pitch']) % 12 not in CHORD[bar['chord']]})
        # Compare spelled pitches, not only pitch classes; the chromatic spelling
        # communicates resolution (F# -> G, C# -> D) even in 12-TET.
        if 'nonchord' in bar and sorted(bar['nonchord']) != actual_nonchord:
            fail(f'{sid}: nonchord classification differs in bar {number}: {actual_nonchord}')
    return len(rows)


def validate_counterpoint(score: dict) -> int:
    sid = score['id']
    header, rows = source_table(TRACK / score['source'], 'Measure')
    if len(rows) != len(score['bars']):
        fail(f'{sid}: counterpoint bar count mismatch')
    for row, bar in zip(rows, score['bars']):
        if int(row[0]) != bar['bar']:
            fail(f'{sid}: bad measure number')
        upper = note_events(row[column(header, 'Upper line')], 'quarter')
        lower = note_events(row[column(header, 'Lower line')], separator=';')
        if bar['upper'] != upper or bar['lower'] != lower:
            fail(f'{sid}: two-voice source mismatch in bar {bar["bar"]}')
        validate_events(upper, Fraction(4), f'{sid} upper')
        validate_events(lower, Fraction(4), f'{sid} lower')
    return len(rows)


def validate_rhythm(score: dict) -> int:
    sid = score['id']
    path = TRACK / score['source']
    text = path.read_text(encoding='utf-8')
    header, rows = source_table(path, 'Version')
    if len(rows) != len(score['variants']):
        fail(f'{sid}: expected {len(score["variants"])} 7/8 patterns in source')
    for row, variant in zip(rows, score['variants']):
        if row[0] != variant['id'] or row[1] != variant['grouping']:
            fail(f'{sid}: 7/8 variant label/grouping differs from source')
        numbers = [int(x) for x in re.findall(r'\d+', row[2])]
        expected = note_events(row[3])
        if numbers != variant['accented_eighth_positions'] or expected != variant['melody']:
            fail(f'{sid}: variant {variant["id"]} does not match the source table')
        validate_events(expected, Fraction(7, 2), f'{sid} variant {variant["id"]}')
        if sum(map(int, variant['grouping'].split('+'))) != 7:
            fail(f'{sid}: grouping does not sum to 7 eighths')
        expected_accents = []
        pos = 1
        for g in map(int, variant['grouping'].split('+')):
            expected_accents.append(pos)
            pos += g
        if expected_accents != numbers:
            fail(f'{sid}: grouped accents do not match grouping')
    header, rows = source_table(path, 'Event line')
    if len(rows) < 2:
        fail(f'{sid}: missing three-against-two source rows')
    for name, cell, onsets in [('Three part', rows[0], score['three_against_two']['three']),
                               ('Two part', rows[1], score['three_against_two']['two'])]:
        if cell[0] != name:
            fail(f'{sid}: missing polyrhythm {name}')
        listed = [int(x) for x in re.findall(r'\d+', cell[1].split('(')[0])]
        if listed != onsets:
            fail(f'{sid}: inconsistent {name} attacks')
    group = score['three_against_two']
    n = group['cycle_units']
    if n != 6 or group['three'] != [0, 2, 4] or group['two'] != [0, 3]:
        fail(f'{sid}: six-unit 3:2 cycle is inconsistent')
    if 'Accents on 1, 4, 7' not in text:
        fail(f'{sid}: 3+3+2 textual source has changed; re-review it')
    return len(rows)


def validate_special_cases(data: dict) -> None:
    by_id = {item['id']: item for item in data['examples']}
    # Catch the historical prose mistake: E4 over D4 is a *major* second.
    score = by_id['008000-form-arrangement']
    bar7 = score['bars'][6]
    if bar7['bar'] != 7 or [(event['pitch'], event['at']) for event in bar7['reply']] != [
        ('E4', '2'), ('G4', '3')]:
        fail('008000: the optional reply is no longer the documented bar-7 answer')
    if midi('E4') - midi('D4') != 2 or midi('G4') - midi('D4') != 5:
        fail('008000: bar 7 intervals no longer match documented major second/fourth')
    text = (TRACK / score['source']).read_text(encoding='utf-8')
    if 'a major second on beat 3' not in text or 'a minor second on beat 3' in text:
        fail('008000: prose must identify E4 above D4 as a major second')
    # A spelled V-I progression by itself is not enough for a perfect authentic
    # cadence; this particular miniature additionally specifies root bass and
    # a tonic soprano arrival in its eighth bar.
    period = by_id['006000-eight-bar-period']
    v, i = period['bars'][-2:]
    if (v['chord'], i['chord']) != ('G', 'C'):
        fail('006000: final harmony is not V to I')
    if (v['bass'][0]['pitch'], i['bass'][0]['pitch']) != ('G2', 'C3'):
        fail('006000: missing root-position basses')
    if i['melody'][-1]['pitch'] != 'C5' or frac(i['melody'][-1]['dur']) != 4:
        fail('006000: missing soprano tonic arrival')
    # The workshop explicitly identifies outside-chord tones rather than
    # giving them unsupported passing/neighbor classifications.
    workshop = by_id['012000-sixteen-bar-workshop']
    allowed = {1: ['G'], 2: ['E', 'F'], 5: ['E', 'G'], 6: ['E', 'F'],
               7: ['A'], 8: ['E'], 12: ['B'], 13: ['G'],
               14: ['E', 'F'], 15: ['D']}
    actual = {bar['bar']: bar['nonchord'] for bar in workshop['bars'] if bar.get('nonchord')}
    if {k: sorted(v) for k, v in allowed.items()} != {k: sorted(v) for k, v in actual.items()}:
        fail(f'012000: non-chord notes differ from the text analysis: {actual}')
    # Chromatic pitches are spelled, not collapsed to semitone classes.
    if workshop['bars'][8]['melody'][0]['pitch'] != 'F#4':
        fail('012000: V/V setup lost F#4')
    if workshop['bars'][11]['melody'][-1]['pitch'] != 'C#5' or workshop['bars'][12]['melody'][0]['pitch'] != 'D5':
        fail('012000: leading-tone return C#5 to D5 missing')


def main() -> int:
    data = json.loads(DATA.read_text(encoding='utf-8'))
    if data.get('version') != 1 or data.get('unit') != 'quarter_note':
        fail('Unsupported score data version or time unit')
    ids = [item['id'] for item in data['examples']]
    if len(ids) != len(set(ids)):
        fail('Duplicate score IDs')
    total = 0
    for entry in data['examples']:
        if entry['kind'] == 'pitched_score':
            total += validate_score(entry)
        elif entry['kind'] == 'counterpoint':
            total += validate_counterpoint(entry)
        elif entry['kind'] == 'rhythm_grid':
            total += validate_rhythm(entry)
        else:
            fail(f'Unknown score kind {entry["kind"]}')
        print(f"OK: {entry['id']}")
    validate_special_cases(data)
    print(f"PASS: {len(data['examples'])} examples; {total} verified source rows; "
          "no audio or external packages required")
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
