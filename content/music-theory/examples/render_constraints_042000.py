#!/usr/bin/env python3
"""Check eight original constraint-composition scores and optionally render audio.

Only validates score/source facts. It cannot certify creativity, aesthetic
quality, the salience of differences to listeners, or historical idiom.
Uses the existing standard-library oscillator from render_listening_lab.py.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import random
import wave

from render_listening_lab import audio, pitch_to_hz

HERE = Path(__file__).resolve().parent
SCORE = HERE / 'constraints-042000.json'
EXPECTED = ('palette_closed','palette_released','rhythm_grid','rhythm_shifted',
            'echo_exact','echo_broken','draw_fixed','draw_revised')


def require(truth: bool, message: str) -> None:
    if not truth:
        raise ValueError(message)


def events(piece: dict, name: str) -> list[dict]:
    return next(v['events'] for v in piece['voices'] if v['name'] == name)


def notes(piece: dict, name: str) -> list[tuple]:
    return [(n['at'],n['dur'],n['pitch']) for n in events(piece,name)]


def pitched(rows: list[list[str]]) -> list[dict]:
    return [{'at':bar*4+i,'dur':1,'pitch':p}
            for bar,row in enumerate(rows) for i,p in enumerate(row)]


def validate(data: dict) -> tuple[int,int]:
    require(data['schema_version']==1 and data['lecture_id']=='042000','wrong score schema/lecture')
    versions=data['versions']
    require(tuple(p['id'] for p in versions)==EXPECTED,'changed version IDs')
    require([p['id'] for pair in data['pairs'] for p in [versions[EXPECTED.index(i)] for i in pair['works']]]
            == list(EXPECTED), 'pair map out of order')
    total=0
    for part in versions:
        pid=part['id']
        require(part['bars']==16 and part['tempo_bpm']==100 and part['beats_per_bar']==4,
                f'{pid}: changed meter, duration or tempo')
        vv=part['voices']
        require([v['name'] for v in vv]==(['lead','bass','inner','follower'] if pid.startswith('echo_') else ['lead','bass','inner']),f'{pid}: voice schema')
        for v in vv:
            require(v['waveform'] in {'sine','harmonic'} and 0 < v['gain'] < .15 and -1<=v['pan']<=1,f'{pid}: invalid voice configuration')
            limit=-1
            for e in v['events']:
                require(0<=e['at']<64 and 0<e['dur'] and e['at']+e['dur']<=64+1e-8,f'{pid}: off-grid {e}')
                require(e['at']>=limit-1e-8,f'{pid}/{v["name"]}: overlapping or unsorted events')
                limit=e['at']+e['dur']
                require(30<=pitch_to_hz(e['pitch'])<=2500,f'{pid}: pitch invalid')
                total+=1
        first=events(part,'lead')[:4]
        require([(e['pitch'],e['at'],e['dur']) for e in first]
                == [(n,i,1) for i,n in enumerate(data['opening_motif'])],f'{pid}: opening modified')
    # All eight share literal bass and inner voice events and their synthesis settings.
    bass=events(versions[0],'bass')
    require(len(bass)==32, 'expected two bass notes per bar')
    cycle=[(x['at'],x['dur'],x['pitch']) for x in bass if x['at']<16]
    require(len(cycle)==8, 'expected 8-note four-bar ground')
    for repetition in range(4):
        window=[(x['at']-16*repetition,x['dur'],x['pitch'])
                for x in bass if 16*repetition<=x['at']<16*(repetition+1)]
        require(window==cycle, f'bass cycle changed at repetition {repetition+1}')
    for idx in (1,2):
        reference=versions[0]['voices'][idx]
        require(all(part['voices'][idx]==reference for part in versions[1:]),f'changed common accompaniment {reference["name"]}')
    for idx in (0,1,2):
        ref={k:v for k,v in versions[0]['voices'][idx].items() if k!='events'}
        require(all({k:v for k,v in p['voices'][idx].items() if k!='events'}==ref for p in versions[1:]),'synthesis setting drift')
    a,b,c,d,e,f,g,h=versions
    allowed=set(data['closed_pitch_classes'])
    require(len(events(a,'lead'))==64 and all(x['pitch'][0] in allowed for x in events(a,'lead')),'closed palette violation')
    pitch_diff=[i for i,(x,y) in enumerate(zip(events(a,'lead'),events(b,'lead'))) if x!=y]
    require(len(pitch_diff)==data['pitch_changed_events']==4,'unexpected pitch substitutions')
    require({i//4+1 for i in pitch_diff}=={10,11,14,15},'changed pitch bars differ')
    require(all(abs(abs(12*math.log2(pitch_to_hz(events(a,'lead')[i]['pitch']) /
                                     pitch_to_hz(events(b,'lead')[i]['pitch'])))-1)<1e-8
                for i in pitch_diff), 'pitch substitutions are no longer each one semitone')
    require(all(events(a,n)==events(b,n) for n in ('bass','inner')),'pitch pair accompaniment changed')
    require(all(x['at']==y['at'] and x['dur']==y['dur'] for x,y in zip(events(a,'lead'),events(b,'lead'))),'pitch pair changed note timing')
    require([x['pitch'] for x in events(c,'lead')]==[x['pitch'] for x in events(d,'lead')],'rhythm pair changed pitches')
    require(events(c,'lead')[:32]==events(d,'lead')[:32],'rhythm first half changed')
    require(all(i==int(i) for i in (x['at'] for x in events(c,'lead'))),'grid is no longer on quarters')
    for bar in range(8,16):
        seq=events(d,'lead')[bar*4:bar*4+4]
        require([(round(x['at']-bar*4,6),x['dur']) for x in seq]
                == [(0,1),(1.5,.5),(2,1),(3.5,.5)],f'shifted onset rule at bar {bar+1}')
    require([v for v in e['voices'][:3]]==[v for v in f['voices'][:3]],'imitation pair lead/accompaniment changed')
    lead=events(e,'lead')
    strict=events(e,'follower')
    expected=[{'at':x['at']+4,'dur':x['dur'],'pitch':x['pitch'][:-1]+str(int(x['pitch'][-1])-1)}
              for x in lead if x['at']<60]
    require(strict==expected,'exact echo no longer strict one-bar octave imitation')
    revised=events(f,'follower')
    old_outside=[x for x in strict if not (40<=x['at']<48)]
    new_outside=[x for x in revised if not (40<=x['at']<48)]
    require(old_outside==new_outside,'echo revision changed entries outside bars eleven and twelve')
    require([x for x in revised if 40<=x['at']<48]==[
        {'at':40,'dur':2,'pitch':'G3'}, {'at':42,'dur':2,'pitch':'A3'},
        {'at':44,'dur':2,'pitch':'C4'}, {'at':46,'dur':2,'pitch':'G3'}],
        'echo revised bars changed')
    require(events(g,'lead')[:4]==events(h,'lead')[:4],'draw comparison changed common introduction')
    bank=data['draw_candidates']
    rng=random.Random(data['draw_seed'])
    drawn=[0]+[rng.randrange(len(bank)) for _ in range(15)]
    require(drawn==data['draw_selected_indices'],'draw record does not reproduce its seed')
    require(events(g,'lead')==pitched([bank[i] for i in drawn]),'raw draw differs from recorded choices')
    swaps={int(k):int(v) for k,v in data['draw_editorial_swaps_by_bar'].items()}
    require(set(swaps)=={8,12,16},'unexplained editorial swap bars')
    require(all(0<=v<len(bank) and drawn[k-1]!=v for k,v in swaps.items()),'invalid or vacuous editorial edit')
    changed=[swaps.get(i+1,x) for i,x in enumerate(drawn)]
    require(events(h,'lead')==pitched([bank[i] for i in changed]),'edited draw differs from manifest')
    for pair in data['pairs']:
        x,y=(versions[EXPECTED.index(i)] for i in pair['works'])
        if pair['id']!='imitation':
            require(events(x,'bass')==events(y,'bass') and events(x,'inner')==events(y,'inner'),f'{pair["id"]}: accompaniment drift')
    return len(versions),total


def crop(piece: dict, first: int, last: int) -> dict:
    out=copy.deepcopy(piece)
    begin,stop=(first-1)*4,last*4
    out['id'] += f'_bars{first:02}-{last:02}'
    out['bars']=last-first+1
    for v in out['voices']:
        v['events']=[{**e,'at':e['at']-begin,'dur':min(e['dur'],stop-e['at'])}
                     for e in v['events'] if begin<=e['at']<stop]
    return out


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',action='store_true',help='check score and pair invariants only')
    ap.add_argument('--pair',choices=['pitch','rhythm','imitation','choice'],help='render one comparison pair')
    ap.add_argument('--only',nargs='*',help='optional exact version IDs')
    ap.add_argument('--bar-range',nargs=2,type=int,metavar=('FIRST','LAST'),help='1-indexed inclusive bar range, common to each version')
    ap.add_argument('--anonymous',action='store_true',help='shuffle trial order and save a separate answer key')
    ap.add_argument('--output-dir',type=Path,default=Path('/tmp/music-constraints-042000'))
    ap.add_argument('--sample-rate',type=int,default=22050)
    args=ap.parse_args()
    data=json.loads(SCORE.read_text(encoding='utf-8'))
    n,events_count=validate(data)
    print(f'Validated {n} original scores, {events_count} note events, four stated comparisons.')
    if args.check:return
    selected=list(data['versions'])
    if args.pair:
        ids=next(p['works'] for p in data['pairs'] if p['id']==args.pair)
        selected=[x for x in selected if x['id'] in ids]
    if args.only is not None:
        require(set(args.only)<=set(EXPECTED),f'unknown version IDs: {sorted(set(args.only)-set(EXPECTED))}')
        selected=[x for x in selected if x['id'] in set(args.only)]
    require(bool(selected),'no versions to render')
    if args.bar_range:
        first,last=args.bar_range
        require(1<=first<=last<=16,'bar range must lie within 1 through 16')
        selected=[crop(x,first,last) for x in selected]
    if args.anonymous:
        random.Random(42001).shuffle(selected)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    key=[]
    for idx,piece in enumerate(selected,1):
        filename=f'trial_{idx:02}.wav' if args.anonymous else f'{piece["id"]}.wav'
        path=args.output_dir/filename
        pcm=audio(piece,args.sample_rate)
        with wave.open(str(path),'wb') as wav:
            wav.setnchannels(2);wav.setsampwidth(2);wav.setframerate(args.sample_rate);wav.writeframes(pcm)
        key.append({'file':filename,'id':piece['id'],'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        print('Rendered',path)
    (args.output_dir/'answer_key.json').write_text(json.dumps({
        'schema_version':1,'warning':'Keep this file hidden from listeners in an anonymous comparison.',
        'trials':key},indent=2)+'\n',encoding='utf-8')

if __name__=='__main__': main()
