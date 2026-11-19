#!/usr/bin/env python3
"""Validate 040000's original complete-work study; optionally render WAVs.

All music is newly authored for this lecture. This validator checks timing,
notated motifs, explicitly documented revisions and version isolation. It does
not measure perceptual clarity, composition quality, historical style, or
whether any arrangement would be playable by particular human musicians.
Pure Python standard library, using the existing music-pack oscillator synth.
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

HERE=Path(__file__).resolve().parent
DATA=HERE/'complete-work-040000.json'
IDs=('motif_seed','lead_only','dense_first_draft','texture_revision',
     'revised_score','alternate_mix')
PITCH=re.compile(r'^([A-G])([#b]?)(-?\d+)$')
PC={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise ValueError(msg)


def midi(p: str) -> int:
    match=PITCH.fullmatch(p)
    require(match is not None,f'invalid note name {p}')
    note,acc,octave=match.groups()
    return (int(octave)+1)*12+PC[note]+(1 if acc=='#' else -1 if acc=='b' else 0)


def notes(rendering: dict, name: str) -> list[dict]:
    return next(v for v in rendering['voices'] if v['name']==name)['events']


def signature(seq: list[dict]) -> list[tuple]:
    return [(e['at'],e['dur'],e['pitch']) for e in seq]


def validate(data: dict) -> tuple[int,int]:
    require(data['schema_version']==1 and data['lecture_id']=='040000','wrong schema')
    rows=data['bar_harmonies']
    require(len(rows)==40 and [r['bar'] for r in rows]==list(range(1,41)),'forty consecutive bars required')
    require([x['bars'] for x in data['formal_sections']]==[[1,8],[9,16],[17,24],[25,32],[33,40]],'sections differ')
    require([r['chord'] for r in rows[0:8]]==['C','Am','F','G7','C','F','G7','C'],'opening harmonic plan changed')
    require(rows[19]['chord']=='D7' and rows[39]['chord']=='C','revisions no longer in expected harmonic context')
    for r in rows:
        at=0
        for e in r['melody']:
            require(e['beat']==at and e['dur']>0,f"bar {r['bar']} gap/overlap")
            require(30<=midi(e['pitch'])<=100,'unrenderable melody register')
            at+=e['dur']
        require(at==4,f"bar {r['bar']} sums to {at}, not four beats")
    # The exact original seed is repeated over two harmonic contexts. The B entry is a +7 shift.
    def pitches(b): return [e['pitch'] for e in rows[b-1]['melody']]
    require(pitches(1)==pitches(9)==pitches(25)==['E4','G4','A4','G4'],'return motif no longer exact')
    require([midi(x)-midi(y) for x,y in zip(pitches(17),pitches(1))]==[7]*4,
            'contrasting B theme is not +7 semitone transposition')
    require([r['id'] for r in data['renderings']]==list(IDs),'version lineup changed')
    R={r['id']:r for r in data['renderings']}
    total=0
    for rid,r in R.items():
        require(r['tempo_bpm']==104 and r['beats_per_bar']==4,'tempo/meter mismatch')
        require((rid=='motif_seed')==(r['bars']==2),'bad seed extent')
        if rid!='motif_seed':require(r['bars']==40,'full work must be 40 bars')
        end=4*r['bars']
        require(len({v['name'] for v in r['voices']})==len(r['voices']),f'{rid} voice names repeated')
        for v in r['voices']:
            require(0<v['gain']<=.2 and -1<=v['pan']<=1 and v['waveform'] in ('sine','harmonic'),
                    f'{rid} bad voice configuration')
            last=0
            for e in v['events']:
                require(0<=e['at']<end and 0<e['dur']<=end and e['at']+e['dur']<=end,
                        f'{rid}/{v["name"]} note off grid')
                require(e['at']>=last,f'{rid}/{v["name"]} overlaps itself')
                require(20<pitch_to_hz(e['pitch'])<4000,f'{rid} unreasonable register')
                last=e['at']+e['dur']
                total+=1
    # Full lead is the notated bar plan in the final arrangement.
    planned=[(4*(r['bar']-1)+e['beat'],e['dur'],e['pitch']) for r in rows for e in r['melody']]
    require(signature(notes(R['revised_score'],'lead'))==planned,'final lead differs from bar chart')
    require(signature(notes(R['lead_only'],'lead'))==planned,'lead-only version differs')
    require(signature(notes(R['motif_seed'],'lead'))==planned[:8],'motif seed differs')
    draft=notes(R['dense_first_draft'],'lead'); texture=notes(R['texture_revision'],'lead')
    revised=notes(R['revised_score'],'lead')
    require(signature(draft)==signature(texture),'texture-only revision changes lead pitches')
    changes=[]
    for before,after in zip(draft,revised):
        require((before['at'],before['dur'])==(after['at'],after['dur']),'lead timing changed between drafts')
        if before['pitch']!=after['pitch']:
            changes.append((before['at']//4+1,before['at']%4,before['pitch'],after['pitch']))
    expected=[(20,3,'F5','F#5'),(40,3,'G4','C5')]
    require(changes==expected,'two specific compositional edits changed')
    assert [(x['bar'],x['beat'],x['before'],x['after']) for x in data['documented_revisions']]==expected
    for name in ('bass','inner_third','inner_upper'):
        require(signature(notes(R['dense_first_draft'],name))!=[],'draft missing accompaniment')
    require(len(notes(R['dense_first_draft'],'inner_third'))==40,'draft should pad every bar')
    require(len(notes(R['texture_revision'],'inner_third'))==20,'revised texture should pad first four bars of each section')
    require(len(notes(R['texture_revision'],'secondary_fragment'))==32,'secondary fragments wrong')
    for name in ('bass','inner_third','inner_upper','secondary_fragment'):
        require(signature(notes(R['texture_revision'],name))==signature(notes(R['revised_score'],name)),
                f'{name} differs between arrangement and composition edit')
    for va,vb in zip(R['revised_score']['voices'],R['alternate_mix']['voices']):
        require(va['name']==vb['name'] and signature(va['events'])==signature(vb['events']),
                'mix-only comparison changes actual notes')
    require(any((a['gain'],a['pan'])!=(b['gain'],b['pan']) for a,b in zip(
        R['revised_score']['voices'],R['alternate_mix']['voices'])), 'mix comparison has no change')
    return len(R),total


def excerpt(r: dict, start: int, stop: int) -> dict:
    """Select inclusive 1-indexed bars, retaining all stems and event boundaries."""
    lo=(start-1)*4;hi=stop*4
    import copy
    part=copy.deepcopy(r)
    part['id']=f"{r['id']}_bars{start:02d}-{stop:02d}"
    part['bars']=stop-start+1
    for v in part['voices']:
        v['events']=[{**e,'at':e['at']-lo} for e in v['events'] if lo<=e['at']<hi]
    return part


def main()->None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',action='store_true',help='validate score without making sound')
    ap.add_argument('--output-dir',type=Path,default=Path('/tmp/music-complete-work-040000'))
    ap.add_argument('--sample-rate',type=int,default=44100)
    ap.add_argument('--anonymous',action='store_true')
    ap.add_argument('--only',nargs='*')
    ap.add_argument('--bar-range',nargs=2,type=int,metavar=('START','END'),help='render just an inclusive bar range')
    args=ap.parse_args()
    data=json.loads(DATA.read_text(encoding='utf-8'))
    n,total=validate(data)
    print(f'Validated {n} versions, {total} authored note events; 40-bar form and isolated edits agree.')
    if args.check:return
    selected=data['renderings']
    if args.only:
        diff=set(args.only)-{r['id'] for r in selected}
        require(not diff,f'unknown version ids: {sorted(diff)}')
        selected=[r for r in selected if r['id'] in args.only]
    if args.bar_range:
        start,stop=args.bar_range
        require(1<=start<=stop<=40,'invalid bar range')
        require(all(stop<=r['bars'] for r in selected),'bar range exceeds a selected rendering')
        selected=[excerpt(r,start,stop) for r in selected]
    if args.anonymous:random.Random(40000).shuffle(selected)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    out=[]
    for j,r in enumerate(selected,1):
        filename=f'trial_{j:02d}.wav' if args.anonymous else f"{r['id']}.wav"
        p=args.output_dir/filename
        pcm=audio(r,args.sample_rate)
        with wave.open(str(p),'wb') as wav:
            wav.setnchannels(2);wav.setsampwidth(2);wav.setframerate(args.sample_rate);wav.writeframes(pcm)
        out.append({'file':filename,'id':r['id'],'description':r['description'],'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
        print('Rendered',p.name)
    (args.output_dir/'answer_key.json').write_text(json.dumps({'schema_version':1,'items':out},indent=2)+'\n',encoding='utf-8')
    print('Completed',len(out),'renderings in',args.output_dir)


if __name__=='__main__':main()
