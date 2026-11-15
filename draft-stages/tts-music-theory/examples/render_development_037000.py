#!/usr/bin/env python3
"""Validate and optionally synthesize eight *original* 037000 development studies.

Text-only content-pack companion. WAVs are generated only on local invocation,
never bundled. Uses the existing same-pack standard-library reference oscillator
from render_listening_lab.py; production-quality timbres can instead be realized
with DawDreamer, and comparisons assembled in Ardour.

The checks verify score arithmetic and stipulated transformation rules; they
cannot validate aesthetic preference, the perception of a response, or cultural
performance authenticity.
"""
from __future__ import annotations

import argparse
from array import array
import hashlib
import json
from pathlib import Path
import random
import sys
import wave

from render_listening_lab import audio, pitch_to_hz

HERE = Path(__file__).resolve().parent
DATA = HERE / 'development-lab-037000.json'
IDS = ('dialogue', 'sentence_inspired', 'sequence', 'variation', 'ostinato_layers',
       'octave_canon', 'additive_process', 'contrast_return')
NOTE_NAMES = ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')


def midi(pitch: str) -> int:
    import re
    m = re.fullmatch(r'([A-G])([#b]?)(-?\d+)', pitch)
    if not m:
        raise ValueError(f'Bad written pitch: {pitch!r}')
    letter,acc,octave=m.groups()
    semi={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}[letter]
    semi += {'':0,'#':1,'b':-1}[acc]
    return 12*(int(octave)+1)+semi


def fail_unless(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def notes_at(events: list[dict], bar: int) -> list[dict]:
    return [e for e in events if 4*bar <= e['at'] < 4*(bar+1)]


def motif_events(data: dict, shift: float=0) -> list[dict]:
    at=shift
    output=[]
    for pitch, duration in zip(data['source_motif']['pitches'], data['source_motif']['durations_beats']):
        output.append({'at':at,'dur':duration,'pitch':pitch}); at+=duration
    return output


def validate(data: dict) -> tuple[int, int]:
    fail_unless(data['schema_version'] == 1, 'Unknown score schema')
    context=data['fixed_context']
    fail_unless((context['tempo_bpm'],context['bars'],context['beats_per_bar'])==(96,8,4), 'Wrong fixed grid')
    renderings=data['renderings']
    fail_unless(tuple(r['id'] for r in renderings)==IDS,'Missing or reordered study identifiers')
    motif=motif_events(data)
    count=0
    for rendering in renderings:
        identity=rendering['id']
        fail_unless((rendering['bars'],rendering['beats_per_bar'],rendering['tempo_bpm'])==(8,4,96), f'{identity}: unequal grid')
        fail_unless(rendering['voices'],f'{identity}: no voices')
        drone=rendering['voices'][0]
        fail_unless(drone['name']=='quiet C2 reference drone',f'{identity}: drone missing')
        fail_unless(drone['events']==[{'at':float(4*b),'dur':4.0,'pitch':'C2'} for b in range(8)],f'{identity}: drone changed')
        fail_unless(len(rendering['voices']) in (2,3),f'{identity}: bad voice count')
        for v in rendering['voices']:
            fail_unless(v['waveform'] in ('sine','harmonic'), f'{identity}: invalid waveform')
            fail_unless(0<v['gain']<=0.3 and -1<=v['pan']<=1, f'{identity}: invalid gain/pan')
            previous_end=0
            for e in v['events']:
                start=float(e['at']); duration=float(e['dur']); end=start+duration
                fail_unless(0<=start<32 and duration>0 and end<=32+1e-8, f'{identity}: event outside duration')
                fail_unless(start+1e-8>=previous_end,f'{identity}: overlapping events within voice {v["name"]}')
                fail_unless(20<pitch_to_hz(e['pitch'])<5000,f'{identity}: unsupported pitch')
                previous_end=end
                count+=1
    by_id={r['id']:r for r in renderings}
    dialogue=by_id['dialogue']['voices']
    fail_unless(set(int(e['at']//4) for e in dialogue[1]['events'])=={0,2,4,6},'Calls not in alternating bars')
    fail_unless(set(int(e['at']//4) for e in dialogue[2]['events'])=={1,3,5,7},'Answers not in alternating bars')
    sent=by_id['sentence_inspired']['voices'][1]['events']
    fail_unless(notes_at(sent,0)==motif,'Sentence basic idea changed')
    fail_unless([{**e, 'at':e['at']-8} for e in notes_at(sent,2)]==motif,'Sentence restatement changed')
    fail_unless(notes_at(sent,7)==[{'at':28,'dur':4,'pitch':'C4'}],'Sentence close changed')
    seq=by_id['sequence']['voices'][1]['events']
    for bar,step in enumerate((0,2,4,5,7,5,2,0)):
        notes=notes_at(seq,bar)
        fail_unless(len(notes)==4,f'Sequence: bar {bar+1} wrong event count')
        for base,e in zip(motif,notes):
            fail_unless(midi(e['pitch'])-midi(base['pitch'])==step and e['dur']==base['dur'] and e['at']==base['at']+4*bar,
                        f'Sequence bar {bar+1} is not an exact transposition')
    var=by_id['variation']['voices'][1]['events']
    fail_unless(notes_at(var,0)==motif and [{**e,'at':e['at']-28} for e in notes_at(var,7)]==motif,
                'Variation source motif does not return')
    fail_unless([midi(e['pitch']) for e in notes_at(var,2)]==[64,61,59,61], 'Incorrect chromatic inversion about E4')
    fail_unless(len(notes_at(var,3))==8,'Diminution should repeat twice in one bar')
    ost=by_id['ostinato_layers']['voices'][1]['events']
    for b in range(8):
        group=notes_at(ost,b)
        fail_unless([e['pitch'] for e in group]==['E3','G3','A3','G3'],f'Ostinato bar {b+1} changed')
    leader=by_id['octave_canon']['voices'][1]['events']
    follower=by_id['octave_canon']['voices'][2]['events']
    fail_unless(len(leader)==len(follower),'Canon missing imitation events')
    for l,f in zip(leader,follower):
        fail_unless(f['at']==l['at']+8 and f['dur']==l['dur'] and midi(f['pitch'])==midi(l['pitch'])-12,
                    'Canon must be exact octave-lower copy at +8 beats')
    additive=by_id['additive_process']['voices'][1]['events']
    fail_unless([len(notes_at(additive,b)) for b in range(8)]==[1,2,3,4,4,4,4,4], 'Wrong additive schedule')
    contrast=by_id['contrast_return']['voices'][1]['events']
    fail_unless(len(notes_at(contrast,5))==0, 'Contrasting middle must leave melodic silence in bar six')
    fail_unless(notes_at(contrast,0)==motif and notes_at(contrast,6)==[{**e,'at':e['at']+24} for e in motif],
                'Contrast and return missing recognizable restatement')
    return len(renderings),count


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',action='store_true', help='Validate scores without writing WAV files')
    ap.add_argument('--sample-rate',type=int,default=44100)
    ap.add_argument('--output-dir',type=Path,default=Path('/tmp/music-development-037000'))
    ap.add_argument('--anonymous',action='store_true',help='Deterministic anonymous order with mapping in answer_key.json')
    ap.add_argument('--only',nargs='*',default=None,help='Optional subset of the eight rendering identifiers')
    args=ap.parse_args()
    data=json.loads(DATA.read_text(encoding='utf-8'))
    count,events=validate(data)
    print(f'Validated {count} original 037000 variants and {events} pitched events')
    if args.check:
        return
    renderings=data['renderings']
    if args.only:
        requested=set(args.only)
        fail_unless(requested.issubset(set(IDS)), f'Unknown IDs: {requested - set(IDS)}')
        renderings=[r for r in renderings if r['id'] in requested]
    if args.anonymous:
        renderings=list(renderings)
        random.Random(37000).shuffle(renderings)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    rows=[]
    for idx,rendering in enumerate(renderings,1):
        output_name=f'trial_{idx:02d}.wav' if args.anonymous else rendering['id']+'.wav'
        filepath=args.output_dir/output_name
        payload=audio(rendering,args.sample_rate)
        with wave.open(str(filepath),'wb') as stream:
            stream.setnchannels(2); stream.setsampwidth(2); stream.setframerate(args.sample_rate)
            stream.writeframes(payload)
        rows.append({'file':output_name,'id':rendering['id'],'sha256':hashlib.sha256(filepath.read_bytes()).hexdigest()})
    (args.output_dir/'answer_key.json').write_text(json.dumps({'schema_version':1,'sample_rate':args.sample_rate,
      'items':rows},indent=2)+'\n',encoding='utf-8')
    print(f'Generated {len(rows)} stereo WAV comparisons and the mapping at {args.output_dir}')


if __name__=='__main__':
    main()
