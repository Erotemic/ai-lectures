#!/usr/bin/env python3
"""Validate original orchestration studies and render optional stereo WAVs.

Reads only text in this Agent D pack. Uses the existing standard-library
reference synthesizer; no samples, plugins, TTS or real-time processing.
Checking a score tests event-level invariants, NOT whether a listener perceives
blending, masking, orchestral realism, artistic improvement, or formal closure.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
import wave

from render_listening_lab import audio, pitch_to_hz

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'orchestration-lab-038000.json'
IDS=('skeleton','synchronous_doubling','crowded_background','spaced_background','staged_entrances','timbral_handoff')


def require(condition,description):
    if not condition:
        raise ValueError(description)


def melodic_events():
    events=[]
    for bar in range(8):
        for off,duration,pitch in zip((0,1,1.5,2),(1,.5,.5,2),('E4','G4','A4','C5' if bar in (3,7) else 'G4')):
            events.append({'at':4*bar+off,'dur':duration,'pitch':pitch})
    return events


def validate(data):
    require(data['schema_version']==1,'unsupported schema')
    require(tuple(x['id'] for x in data['renderings'])==IDS,'expected six unique study names')
    fixed=melodic_events()
    reference=[{'at':4*bar,'dur':4,'pitch':'C2'} for bar in range(8)]
    total=0
    for study in data['renderings']:
        ident=study['id']
        require((study['tempo_bpm'],study['beats_per_bar'],study['bars'])==(96,4,8),ident+' wrong timing grid')
        require(study['voices'][0]['events']==reference,ident+' changed the reference drone')
        foreground=sorted((e for v in study['voices'] if v['name'].startswith('foreground') for e in v['events']),key=lambda e:e['at'])
        require(foreground==fixed,ident+' altered or omitted a melodic event')
        for voice in study['voices']:
            require(voice['waveform'] in ('sine','harmonic'),ident+' unsupported waveform')
            require(0<voice['gain']<=0.2 and -1<=voice['pan']<=1,ident+' unsupported gain/pan')
            end=0
            for event in voice['events']:
                at=event['at'];dur=event['dur']
                require(0<=at<32 and dur>0 and at+dur<=32,ident+' note outside score')
                require(at>=end,ident+' overlap within voice')
                require(20<pitch_to_hz(event['pitch'])<5000,ident+' unsupported note')
                end=at+dur
                total+=1
    by_id={s['id']:s for s in data['renderings']}
    doubled=by_id['synchronous_doubling']['voices']
    require(doubled[-1]['events']==fixed,'unison doubling does not match every attack')
    crowded=by_id['crowded_background']['voices'][-1]['events']
    spaced=by_id['spaced_background']['voices'][-1]['events']
    octave_map={'C4':'C3','E4':'E3','G4':'G3'}
    require(len(crowded)==len(spaced)==32,'register comparison missing events')
    require(all(a['at']==b['at'] and a['dur']==b['dur'] and octave_map[a['pitch']]==b['pitch'] for a,b in zip(crowded,spaced)), 'register comparison differs beyond octave')
    staged=by_id['staged_entrances']['voices']
    require(min(e['at'] for e in staged[2]['events'])==8,'lower layer should start bar three')
    require(min(e['at'] for e in staged[3]['events'])==16,'upper layer should start bar five')
    handoff=by_id['timbral_handoff']['voices']
    require(all(e['at']<16 for e in handoff[1]['events']) and all(e['at']>=16 for e in handoff[2]['events']),'timbre switch not at bar five')
    return len(data['renderings']),total


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--output-dir',type=Path,default=Path('/tmp/music-orchestration-038000'))
    parser.add_argument('--sample-rate',type=int,default=44100)
    parser.add_argument('--anonymous',action='store_true')
    parser.add_argument('--only',nargs='*',help='Optional subset of study IDs')
    args=parser.parse_args()
    data=json.loads(SOURCE.read_text(encoding='utf-8'))
    n,events=validate(data)
    print(f'Validated {n} original orchestration studies with {events} note events')
    if args.check:return
    studies=data['renderings']
    if args.only:
        wanted=set(args.only);require(wanted.issubset(set(IDS)),f'Unknown studies {wanted-set(IDS)}')
        studies=[s for s in studies if s['id'] in wanted]
    if args.anonymous:
        studies=list(studies);random.Random(38000).shuffle(studies)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    rows=[]
    for i,study in enumerate(studies,1):
        name=f'trial_{i:02d}.wav' if args.anonymous else study['id']+'.wav'
        out=args.output_dir/name
        payload=audio(study,args.sample_rate)
        with wave.open(str(out),'wb') as stream:
            stream.setnchannels(2);stream.setsampwidth(2);stream.setframerate(args.sample_rate)
            stream.writeframes(payload)
        rows.append({'file':name,'study_id':study['id'],'sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
    (args.output_dir/'answer_key.json').write_text(json.dumps({'schema_version':1,'sample_rate':args.sample_rate,'items':rows},indent=2)+'\n',encoding='utf-8')
    print(f'Generated {len(rows)} stereo WAVs and an answer key in {args.output_dir}')

if __name__=='__main__':main()
