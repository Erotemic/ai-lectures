#!/usr/bin/env python3
"""Validate three original forty-bar composition studies; optionally render WAVs.

This tests only source-event integrity and declared formal relationships. It does
not assess musical quality, listener response, historical style, or timbral realism.
Uses the pack's existing standard-library oscillator renderer, no plugin install.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import random
import wave
from render_listening_lab import audio, pitch_to_hz

HERE = Path(__file__).resolve().parent
SCORE = HERE / 'comparing-forms-041000.json'
IDS = ('ground_wheel', 'return_arch', 'continuous_road')


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def events(piece: dict, voice: str) -> list[dict]:
    return next(item['events'] for item in piece['voices'] if item['name'] == voice)


def signature(seq: list[dict], *, offset: float = 0) -> list[tuple]:
    return [(round(e['at'] - offset, 5), e['dur'], e['pitch']) for e in seq]


def bar_events(piece: dict, voice: str, bar: int) -> list[dict]:
    lo = (bar - 1) * 4
    return [e for e in events(piece, voice) if lo <= e['at'] < lo + 4]


def window(piece: dict, voice: str, first: int, last: int) -> list[tuple]:
    lo, hi = (first - 1)*4, last*4
    return signature([e for e in events(piece, voice) if lo <= e['at'] < hi], offset=lo)


def validate(data: dict) -> tuple[int, int]:
    require(data['schema_version'] == 1 and data['lecture_id'] == '041000', 'unexpected score identity')
    require([p['id'] for p in data['pieces']] == list(IDS), 'unexpected work IDs')
    ref = [('E4', 1), ('G4', 1), ('A4', 1), ('G4', 1)]
    require(data['reference_motif']['pitches'] == [p for p,_ in ref], 'reference motif changed')
    count = 0
    for piece in data['pieces']:
        require(piece['bars'] == 40 and piece['tempo_bpm'] == 100 and piece['beats_per_bar'] == 4,
                f"{piece['id']}: changed duration or pulse")
        require([v['name'] for v in piece['voices']] == ['lead','bass','inner'], 'unexpected voices')
        for voice in piece['voices']:
            require(voice['waveform'] in ('sine','harmonic'), 'bad wave type')
            require(0 < voice['gain'] <= .12 and -1 <= voice['pan'] <= 1, 'out of range mixing parameters')
            past = 0
            for e in voice['events']:
                require(0 <= e['at'] < 160 and e['dur'] > 0 and e['at'] + e['dur'] <= 160 + 1e-8,
                        f"{piece['id']}/{voice['name']}: off-grid event {e}")
                require(e['at'] + 1e-8 >= past, f"{piece['id']}/{voice['name']}: event overlap")
                require(20 < pitch_to_hz(e['pitch']) < 4000, 'out of range pitch')
                past = e['at'] + e['dur']
                count += 1
        require([(e['pitch'],e['dur']) for e in bar_events(piece,'lead',1)] == ref,
                f"{piece['id']}: missing exact shared opening motif")
    # Control synthesis timbres and gains, but explicitly *not* perceptual loudness.
    voice_cfg = [tuple((v['name'],v['waveform'],v['gain'],v['pan']) for v in p['voices'])
                 for p in data['pieces']]
    require(len(set(voice_cfg)) == 1, 'cross-work synthesis controls differ')
    ground, rondo, continuous = data['pieces']
    bass_four = window(ground,'bass',1,4)
    require(len(bass_four) == 8, 'ground bass needs eight notes in each cycle')
    require([p for _,_,p in bass_four[::2]] == ['C3','A2','F2','G2'], 'ground roots incorrect')
    for c in range(10):
        require(window(ground,'bass',4*c+1,4*c+4)==bass_four,
                f'ground changed at cycle {c+1}')
    require(len(ground['formal_map'])==10, 'expected ten announced ground variants')
    for first in [1,17,33]:
        require(window(rondo,'lead',first,first) == window(rondo,'lead',1,1),
                'refrain opening head changed')
    require(window(rondo,'lead',1,8)==window(rondo,'lead',17,24),
            'second refrain is not an exact melodic return')
    require(window(rondo,'lead',1,7)==window(rondo,'lead',33,39),
            'last refrain differs before the last bar')
    require(window(rondo,'lead',8,8)!=window(rondo,'lead',40,40),
            'last refrain has no changed cadence')
    require(window(rondo,'lead',9,16)!=window(rondo,'lead',25,32),
            'two contrasting episodes not contrasted')
    require([x['bars'] for x in rondo['formal_map']]==[[1,8],[9,16],[17,24],[25,32],[33,40]],
            'rondo five-part plan changed')
    # This tests absence of verbatim complete eight-bar reprise; it does not prove
    # listeners will perceive continuous development or a gradual process.
    windows = [tuple(window(continuous,'lead',i,i+7)) for i in range(1,34)]
    require(len(set(windows)) == len(windows), 'continuous work now repeats a full eight-bar lead window')
    require(len(bar_events(continuous,'lead',40))==1 and
            bar_events(continuous,'lead',40)[0]['pitch']=='C4', 'continuous close changed')
    require(len(events(continuous,'inner'))>0, 'continuous inner voice missing')
    return len(data['pieces']), count


def excerpt(piece: dict, start: int, stop: int) -> dict:
    import copy
    out = copy.deepcopy(piece)
    lo,hi=(start-1)*4,stop*4
    out['id']=f"{piece['id']}_bars{start:02d}-{stop:02d}"
    out['bars']=stop-start+1
    for voice in out['voices']:
        cropped=[]
        for e in voice['events']:
            if lo <= e['at'] < hi:
                d=min(e['dur'],hi-e['at'])
                cropped.append({**e,'at':e['at']-lo,'dur':d})
        voice['events']=cropped
    return out


def main()->None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check', action='store_true', help='inspect structural invariants only')
    p.add_argument('--output-dir',type=Path,default=Path('/tmp/music-form-comparisons-041000'))
    p.add_argument('--sample-rate',type=int,default=22050)
    p.add_argument('--only',nargs='*',help='render only these IDs')
    p.add_argument('--bar-range',nargs=2,type=int,metavar=('FIRST','LAST'),
                   help='render the same inclusive 1-indexed bar span in each work')
    p.add_argument('--anonymous',action='store_true',help='shuffle trial names, make a local answer key')
    args=p.parse_args()
    data=json.loads(SCORE.read_text(encoding='utf-8'))
    works,n=validate(data)
    print(f'Validated {works} complete original works, {n} note events and structural comparisons.')
    if args.check:return
    pieces=list(data['pieces'])
    if args.only:
        unknown=set(args.only)-{x['id'] for x in pieces}
        require(not unknown,f'unknown piece ID(s): {sorted(unknown)}')
        pieces=[x for x in pieces if x['id'] in args.only]
        require(pieces,'no selected pieces')
    if args.bar_range:
        lo,hi=args.bar_range
        require(1<=lo<=hi<=40,'bar range must lie between 1 and 40')
        pieces=[excerpt(x,lo,hi) for x in pieces]
    if args.anonymous:random.Random(41000).shuffle(pieces)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    written=[]
    for n,part in enumerate(pieces,1):
        filename=f'trial_{n:02d}.wav' if args.anonymous else part['id']+'.wav'
        destination=args.output_dir/filename
        pcm=audio(part,args.sample_rate)
        with wave.open(str(destination),'wb') as wav:
            wav.setnchannels(2);wav.setsampwidth(2);wav.setframerate(args.sample_rate);wav.writeframes(pcm)
        written.append({'file':filename,'work_id':part['id'],'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()})
        print('Rendered',destination)
    key={'schema_version':1,'label_visibility_warning':'An experimenter must conceal this answer key from listeners.',
         'trials':written}
    (args.output_dir/'answer_key.json').write_text(json.dumps(key,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__': main()
