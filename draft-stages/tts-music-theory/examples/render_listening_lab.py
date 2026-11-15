#!/usr/bin/env python3
"""Render original lecture 033000-036000 listening exercises to WAV.

Only source text is checked into the content pack. This standalone renderer uses
Python's standard library, not a bundled instrument or third-party recording.
The generated WAVs are deliberately plain, and can be imported into Ardour or
processed via DawDreamer. No generated sound is considered an empirical result.
"""
from __future__ import annotations

import argparse
from array import array
import hashlib
import json
import math
from pathlib import Path
import random
import re
import sys
import wave

HERE = Path(__file__).resolve().parent
SCORES = HERE / 'listening-lab-033000-036000.json'
PITCH_RE = re.compile(r'^([A-G])([#b]?)(-?\d+)$')
SEMITONES = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def pitch_to_hz(pitch: str) -> float:
    match = PITCH_RE.fullmatch(pitch)
    if not match:
        raise ValueError(f'Invalid written pitch: {pitch!r}')
    letter, accidental, octave_s = match.groups()
    semitone = SEMITONES[letter] + (1 if accidental == '#' else -1 if accidental == 'b' else 0)
    midi = 12 * (int(octave_s) + 1) + semitone
    return 440.0 * (2.0 ** ((midi - 69) / 12.0))


def validate(data: dict) -> int:
    if data.get('schema_version') != 1:
        raise ValueError('Unrecognized score schema')
    ids = set()
    count = 0
    for part in data['renderings']:
        identity = part['id']
        if not re.fullmatch(r'[a-z0-9_]+', identity) or identity in ids:
            raise ValueError(f'Duplicate/invalid rendering id {identity}')
        ids.add(identity)
        tempo = float(part['tempo_bpm'])
        if tempo <= 0 or tempo > 400:
            raise ValueError(f'Invalid tempo for {identity}')
        total = float(part['beats_per_bar'] * part['bars'])
        for voice in part['voices']:
            if voice['waveform'] not in ('sine', 'harmonic'):
                raise ValueError('Only sine and harmonic waveforms supported')
            if not (0 < voice['gain'] <= 0.5 and -1 <= voice['pan'] <= 1):
                raise ValueError('Gain/pan out of bounds')
            for note in voice['events']:
                begin = float(note['at'])
                dur = float(note['dur'])
                if begin < 0 or dur <= 0 or begin + dur > total + 1e-7:
                    raise ValueError(f'{identity}: event outside bar grid: {note}')
                hz = float(note['frequency_hz']) if 'frequency_hz' in note else pitch_to_hz(note['pitch'])
                if not 20 <= hz <= 16000:
                    raise ValueError(f'{identity}: unsupported pitch frequency {hz}')
                count += 1
    # A small, content-specific invariant: only bar 7's upper notes change.
    choices = {part['id']: part for part in data['renderings']}
    a, b = choices['transcription_original']['voices'], choices['transcription_revision_b']['voices']
    if a[0] != b[0]:
        raise ValueError('Revision unexpectedly changed bass')
    differences = [i for i, (x, y) in enumerate(zip(a[1]['events'], b[1]['events'])) if x != y]
    if differences != [25, 26, 27]:
        # The first note, D4, remains the same; only beats 2,3,4 change.
        raise ValueError(f'Unexpected revision event positions: {differences}')
    return count


def audio(part: dict, sample_rate: int) -> bytes:
    if sample_rate < 8000 or sample_rate > 192000:
        raise ValueError('Sample rate must be between 8000 and 192000')
    sec_per_beat = 60.0 / float(part['tempo_bpm'])
    frames = round(part['beats_per_bar'] * part['bars'] * sec_per_beat * sample_rate)
    left = array('f', [0.0]) * frames
    right = array('f', [0.0]) * frames
    for voice in part['voices']:
        pan = float(voice['pan'])
        left_gain = float(voice['gain']) * math.cos((pan + 1) * math.pi / 4)
        right_gain = float(voice['gain']) * math.sin((pan + 1) * math.pi / 4)
        partials = 1 if voice['waveform'] == 'sine' else 5
        normalizer = sum(1.0 / k for k in range(1, partials + 1))
        for note in voice['events']:
            hz = float(note['frequency_hz']) if 'frequency_hz' in note else pitch_to_hz(note['pitch'])
            if hz * partials >= 0.48 * sample_rate:
                raise ValueError(f'{part["id"]}: sample rate {sample_rate} too low for {hz:.1f} Hz with {partials} harmonics')
            start = round(float(note['at']) * sec_per_beat * sample_rate)
            length = round(float(note['dur']) * sec_per_beat * sample_rate)
            end = min(frames, start + length)
            edge = max(1, min(round(0.012 * sample_rate), length // 4))
            omega = 2.0 * math.pi * hz / sample_rate
            for i in range(start, end):
                j = i - start
                fade = min(1.0, j / edge, (end - i - 1) / edge)
                phase = j * omega
                sample = sum(math.sin(phase * k) / k for k in range(1, partials + 1)) / normalizer
                left[i] += left_gain * fade * sample
                right[i] += right_gain * fade * sample
    peak = max(max(abs(s) for s in left), max(abs(s) for s in right)) if frames else 0
    if peak >= 0.99:
        raise ValueError(f'{part["id"]}: peak {peak:.3f}; reduce source gains instead of silently normalizing')
    # Explicit fixed master scale; never independently normalize examples.
    pcm = array('h')
    for l, r in zip(left, right):
        pcm.append(int(round(32767 * 0.78 * l)))
        pcm.append(int(round(32767 * 0.78 * r)))
    if sys.byteorder != 'little':
        pcm.byteswap()
    return pcm.tobytes()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output-dir', type=Path, default=Path('/tmp/music-listening-lab'))
    ap.add_argument('--sample-rate', type=int, default=44100)
    ap.add_argument('--check', action='store_true', help='Check scores without synthesizing audio')
    ap.add_argument('--only', nargs='*', default=None, help='Optional list of rendering IDs')
    ap.add_argument('--anonymous', action='store_true', help='Shuffle deterministic trial filenames and write an answer key')
    args = ap.parse_args()
    data = json.loads(SCORES.read_text(encoding='utf-8'))
    notes = validate(data)
    parts = data['renderings']
    if args.only:
        chosen = set(args.only)
        unknown = chosen.difference(p['id'] for p in parts)
        if unknown:
            raise ValueError(f'Unknown rendering ids: {sorted(unknown)}')
        parts = [p for p in parts if p['id'] in chosen]
    print(f'Score OK: {len(data["renderings"])} original renderings; {notes} declared pitch events')
    if args.check:
        return
    if args.anonymous:
        parts = list(parts)
        random.Random(33036).shuffle(parts)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for i, part in enumerate(parts, 1):
        name = f'trial_{i:03d}' if args.anonymous else part['id']
        path = args.output_dir / f'{name}.wav'
        rendered = audio(part, args.sample_rate)
        with wave.open(str(path), 'wb') as wav:
            wav.setnchannels(2)
            wav.setsampwidth(2)
            wav.setframerate(args.sample_rate)
            wav.writeframes(rendered)
        records.append({'file': path.name, 'exercise': part['id'],
                        'description': part['description'],
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    key = args.output_dir / 'answer_key.json'
    key.write_text(json.dumps({'schema_version': 1, 'sample_rate': args.sample_rate,
                               'rendering_tool': 'render_listening_lab.py',
                               'items': records}, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {len(records)} stereo WAVs and an answer key under {args.output_dir}')


if __name__ == '__main__':
    main()
