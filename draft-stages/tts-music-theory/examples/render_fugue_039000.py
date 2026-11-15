#!/usr/bin/env python3
"""Validate 039000's original imitative scores; optionally render stereo WAVs.

No external audio files or score excerpts. Uses the existing local standard-library
oscillator synthesizer. Tests identity, transposition, actual interval exchanges,
entry schedules, and clipping constraints; it does NOT certify stylistic quality,
smooth harmonic voice-leading, instrument playability, or perceptual outcome.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
import re
import wave

from render_listening_lab import audio, pitch_to_hz

HERE = Path(__file__).resolve().parent
DATA = HERE / 'fugue-lab-039000.json'
EXPECTED_IDS = (
    'subject_alone','real_answer','tonal_answer','invertible_above',
    'invertible_below','exposition','episode_sequence','stretto',
    'complete_miniature',
)
# Independent canonical theme is intentionally repeated in this validator,
# so an accidental alteration to the JSON does not silently change the oracle.
SUBJECT = [('C4',0,1),('G4',1,1),('A4',2,.5),('G4',2.5,.5),('E4',3,1),
           ('F4',4,1),('E4',5,.5),('D4',5.5,.5),('G4',6,1),('C4',7,1)]
TONAL = [('G4',0,1),('C5',1,1),('D5',2,.5),('C5',2.5,.5),('B4',3,1),
         ('C5',4,1),('B4',5,.5),('A4',5.5,.5),('D5',6,1),('G4',7,1)]
PITCH = re.compile(r'^([A-G])([#b]?)(-?\d+)$')
NOTES = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}


def check(ok: bool, what: str) -> None:
    if not ok:
        raise ValueError(what)


def midi(pitch: str) -> int:
    m = PITCH.fullmatch(pitch)
    check(m is not None, f'bad pitch: {pitch}')
    letter, acc, octave = m.groups()
    return (int(octave)+1)*12+NOTES[letter]+(1 if acc=='#' else -1 if acc=='b' else 0)


def signature(events: list[dict], start: float = 0, octave: int = 0) -> list[tuple]:
    return [(float(x['at'])-start,float(x['dur']),midi(x['pitch'])-octave) for x in events]


def canonical(sequence: list[tuple]) -> list[tuple]:
    return [(float(at),float(dur),midi(pitch)) for pitch,at,dur in sequence]


def contains(voice: dict, start: float, pattern: list[tuple], semitones: int=0) -> bool:
    found=[x for x in voice['events'] if start <= x['at'] < start+8]
    return signature(found,start,semitones)==canonical(pattern)


def validate(data: dict) -> tuple[int,int]:
    check(data.get('schema_version')==1 and data.get('lecture_id')=='039000','bad schema/lecture')
    check(tuple(x['id'] for x in data['renderings'])==EXPECTED_IDS,'wrong renderings or order')
    studies={r['id']:r for r in data['renderings']}
    n=0
    for r in data['renderings']:
        check((r['tempo_bpm'],r['beats_per_bar'])==(104,4),f"{r['id']} timing mismatch")
        end=r['bars']*4
        for v in r['voices']:
            check(v['waveform'] in ('harmonic','sine'),f"{r['id']} invalid waveform")
            check(0 < v['gain'] <= .2 and -1 <= v['pan'] <= 1,'invalid gain/pan')
            last=0
            for e in v['events']:
                check(isinstance(e['at'],(int,float)) and isinstance(e['dur'],(int,float)),'invalid time')
                check(0 <= e['at'] < end and 0 < e['dur'] <= end and e['at']+e['dur']<=end+1e-9,'event beyond grid')
                check(e['at']>=last-1e-9,f"{r['id']} overlaps inside {v['name']}")
                check(20<pitch_to_hz(e['pitch'])<4000,'unrenderable pitch')
                last=e['at']+e['dur']
                n+=1
    check(signature(studies['subject_alone']['voices'][0]['events']) == canonical(SUBJECT),'subject changed')
    check(signature(studies['tonal_answer']['voices'][0]['events']) == canonical(TONAL),'tonal demonstration changed')
    sr=studies['subject_alone']['voices'][0]['events']
    real=studies['real_answer']['voices'][0]['events']
    check(all(a['at']==b['at'] and a['dur']==b['dur'] and midi(b['pitch'])-midi(a['pitch'])==7 for a,b in zip(sr,real)),
          'real answer is not exact +7 semitone transposition')
    check(len(sr)==len(real)==10,'wrong subject length')
    # Sounding lines are shifted in opposite directions without changing their internal event lists.
    upper=studies['invertible_above']['voices']
    lower=studies['invertible_below']['voices']
    check(signature(upper[0]['events'],octave=12)==signature(lower[0]['events']), 'subject inversion differs beyond octave')
    check(signature(upper[1]['events'])==signature(lower[1]['events'],octave=12),'counterline inversion differs beyond octave')
    # On all eight integer beats, the study's two lines have a consonant 3rd/6th class
    # in both registral arrangements. This is not a full strict-counterpoint proof.
    for arrangement in (upper,lower):
        for beat in range(8):
            pitches=[]
            for v in arrangement:
                active=[e for e in v['events'] if e['at']<=beat<e['at']+e['dur']]
                check(len(active)==1,'voice unavailable at structural beat')
                pitches.append(midi(active[0]['pitch']))
            semi=abs(pitches[0]-pitches[1])%12
            check(semi in (3,4,8,9), f'structural inversion makes a non-third/sixth interval: beat {beat}, {semi}')
    ex={v['name']:v for v in studies['exposition']['voices']}
    check(contains(ex['alto'],0,SUBJECT), 'exposition opening subject missing')
    check(contains(ex['soprano'],8,TONAL), 'exposition second entry not tonal answer')
    check(contains(ex['bass'],16,SUBJECT,-12), 'exposition bass entry missing')
    st={v['name']:v for v in studies['stretto']['voices']}
    check(contains(st['first_subject'],0,SUBJECT,12), 'first stretto subject missing')
    check(contains(st['second_subject'],4,SUBJECT), 'second stretto subject missing')
    check(4 < 8, 'stretto entries must overlap')
    episodes=studies['episode_sequence']['voices'][0]['events']
    check(len(episodes)==20 and [episodes[i]['at'] for i in (0,5,10,15)]==[0,4,8,12], 'head sequence grid changed')
    first=episodes[:5]
    for i,shift in enumerate((0,2,4,5)):
        block=episodes[5*i:5*(i+1)]
        check(all(x['at']-first[j]['at']==4*i and x['dur']==first[j]['dur'] and
                  midi(x['pitch'])-midi(first[j]['pitch'])==shift for j,x in enumerate(block)),
              'episode is not the declared exact head-motive sequence')
    full={v['name']:v for v in studies['complete_miniature']['voices']}
    entries={('alto',0,'S',0),('soprano',8,'T',0),('bass',16,'S',-12),('soprano',32,'S',12),
             ('alto',40,'T',0),('soprano',64,'S',12),('alto',68,'S',0),('bass',72,'T',-24),
             ('alto',96,'S',0)}
    for name,start,typ,shift in entries:
        check(contains(full[name],start,SUBJECT if typ=='S' else TONAL,shift),
              f'complete miniature missing {name} {typ} at beat {start}')
    check(data['entry_map']['stretto'][0]['beat']==64 and data['entry_map']['stretto'][1]['beat']==68 and
          data['entry_map']['stretto'][2]['beat']==72, 'stretto map changed')
    for start,end in data['episode_spans_beats']:
        for v in full.values():
            for at in range(start,end-7):
                for motif in (SUBJECT,TONAL):
                    # Every exact full 2-bar phrase must be absent, allowing fragment derivatives.
                    check(not contains(v,at,motif,0),f'full subject unexpectedly appears in episode at beat {at}')
    b=full['bass']['events']
    check(b[-2:]==data['closing_bass'],'bass does not end G2 -> C3')
    return len(studies),n


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true')
    p.add_argument('--output-dir',type=Path,default=Path('/tmp/fugue-039000'))
    p.add_argument('--sample-rate',type=int,default=44100)
    p.add_argument('--anonymous',action='store_true')
    p.add_argument('--only',nargs='*',help='Optional rendering IDs')
    args=p.parse_args()
    data=json.loads(DATA.read_text(encoding='utf-8'))
    n,events=validate(data)
    print(f'Validated {n} original studies with {events} note events; subject/answer and structural entry invariants pass.')
    if args.check:
        return
    renders=data['renderings']
    if args.only:
        unknown=set(args.only)-set(EXPECTED_IDS)
        check(not unknown,f'unknown IDs: {sorted(unknown)}')
        renders=[r for r in renders if r['id'] in args.only]
    if args.anonymous:
        renders=list(renders)
        random.Random(39000).shuffle(renders)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    answer=[]
    for i,r in enumerate(renders,1):
        name=f'trial_{i:02d}.wav' if args.anonymous else f"{r['id']}.wav"
        out=args.output_dir/name
        pcm=audio(r,args.sample_rate)
        with wave.open(str(out),'wb') as f:
            f.setnchannels(2)
            f.setsampwidth(2)
            f.setframerate(args.sample_rate)
            f.writeframes(pcm)
        answer.append({'file':name,'study_id':r['id'],'description':r['description'],
                       'sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
        print('Rendered',name)
    (args.output_dir/'answer_key.json').write_text(json.dumps({'schema_version':1,'sample_rate':args.sample_rate,
        'items':answer},indent=2)+'\n',encoding='utf-8')
    print('WAV files and answer key in',args.output_dir)

if __name__=='__main__':
    main()
