"""Isolated title delivery and lossless assembly of existing reader audio pages."""
import json
from pathlib import Path
import subprocess
import tempfile
import urllib.request
import wave

from ailectures.narration import TITLE_INSTRUCTION, TITLE_POLICY
from .media import duration

RATE = 24000


def _decode(source, destination, speed=1):
    command = ['ffmpeg','-nostdin','-y','-loglevel','error','-i',str(source),'-vn']
    if speed != 1: command += ['-filter:a',f'atempo={speed:g}']
    subprocess.run(command+['-ar',str(RATE),'-ac','1','-codec:a','pcm_s16le','-f','wav',str(destination)],
                   check=True,capture_output=True,timeout=180)


def _join(entries, destination):
    """Use sample counts, so silence changes neither speech nor word alignment."""
    with wave.open(str(destination),'wb') as output:
        output.setparams((1,2,RATE,0,'NONE','not compressed'))
        for path,before,after in entries:
            output.writeframesraw(b'\0\0'*round(before*RATE))
            with wave.open(str(path),'rb') as source:
                if source.getparams()[:3] != (1,2,RATE): raise ValueError('Title assembly requires mono PCM')
                while data := source.readframes(RATE): output.writeframesraw(data)
            output.writeframesraw(b'\0\0'*round(after*RATE))


def _title(engine, text, settings, destination, task):
    from .audio import text_chunks, check_audio_limit, check_audio_minimum
    from .pronunciation import speech_text
    from .audio_library import SpeechServiceError
    entries = []
    with tempfile.TemporaryDirectory(prefix='.title-',dir=destination.parent) as folder:
        for index,piece in enumerate(text_chunks(text,engine.speech_max_chars,engine.speech_max_words)):
            task.check_cancelled()
            payload = {k:v for k,v in engine.request_settings.items()
                       if k not in {'instruction','instructions','voice_direction','direction','long_form'}}
            payload.update(model=settings.model,voice=settings.voice,input=speech_text(piece,engine.pronunciation_replacements),
                           response_format=engine.response_format)
            if engine.model.lower() == 'kokoro': payload.update(speed=settings.speed,stream=False)
            if engine.language: payload['language'] = engine.language
            if engine.title_instruction_field:
                payload[engine.title_instruction_field] = engine.title_instruction or TITLE_INSTRUCTION
            if engine.model.lower() == 'breeze-tts2': payload['cfg_scale'] = 4.0 if engine.title_instruction_field else 1.0
            source = Path(folder)/f'{index}.source.{engine.response_format}'
            request = urllib.request.Request(engine.endpoint,data=json.dumps(payload).encode(),
                                             headers={'Content-Type':'application/json'},method='POST')
            with urllib.request.urlopen(request,timeout=min(180,engine.timeout)) as response:
                content_type = response.headers.get('Content-Type','').lower()
                if 'json' in content_type or 'text/' in content_type: raise SpeechServiceError('Title request returned text instead of audio')
                data = response.read(16*1024*1024+1)
                if not 256 <= len(data) <= 16*1024*1024: raise SpeechServiceError('Title response is empty or oversized')
                source.write_bytes(data)
            task.check_cancelled()
            seconds = duration(source)
            check_audio_limit(seconds,engine.max_audio_seconds)
            check_audio_minimum(piece,seconds,engine.max_speech_words_per_second,min_words=8)
            decoded = Path(folder)/f'{index}.wav'
            _decode(source,decoded,settings.speed if engine.model.lower() != 'kokoro' else 1)
            entries.append((decoded,0,0))
        _join(entries,destination)


def render_title_page(engine, parts, settings, destination, task):
    """Titles use short requests; body keeps its normal model/policy/instructions."""
    with tempfile.TemporaryDirectory(prefix='.page-delivery-',dir=destination.parent) as folder:
        entries, chunks, cursor = [], [], 0.0
        for index,part in enumerate(parts):
            task.check_cancelled()
            output = Path(folder)/f'{index}.wav'
            title = part['role'] == 'title'
            if title: _title(engine,part['text'],settings,output,task)
            elif engine.server_long_form:
                engine._send_server_paragraph_speech(part['text'],settings,output,task=task,output_format='wav')
            else: engine._send_speech(part['text'],settings,output,output_format='wav')
            canonical = Path(folder)/f'{index}.pcm.wav'
            _decode(output,canonical)
            seconds = duration(canonical)
            before,after = (engine.title_pause_before,engine.title_pause_after) if title else (0,0)
            entries.append((canonical,before,after))
            timing = output.with_name(output.name+'.timings.json')
            marks = json.loads(timing.read_text()).get('chunks',[]) if timing.exists() else []
            words = len(part['text'].split())
            if not marks: marks = [dict(words=words,start=0,end=seconds)]
            total = sum(mark['words'] for mark in marks)
            # Pronunciation aliases can expand words. Keep canonical anchors.
            counted = assigned = 0
            for mark in marks:
                counted += mark['words']
                end_word = round(counted*words/total)
                if end_word > assigned:
                    chunks.append(dict(words=end_word-assigned,start=cursor+before+mark['start'],
                                       end=cursor+before+mark['end'],role=part['role']))
                assigned = end_word
            cursor += before+seconds+after
        joined = Path(folder)/'joined.wav'
        _join(entries,joined)
        subprocess.run(['ffmpeg','-nostdin','-y','-loglevel','error','-i',str(joined),
                        *engine._encoding_args(destination)],check=True,capture_output=True,timeout=180)
        seconds = duration(destination)
        scale = seconds/cursor
        for chunk in chunks:
            chunk['start'] = round(chunk['start']*scale,4)
            chunk['end'] = round(chunk['end']*scale,4)
        destination.with_name(destination.name+'.timings.json').write_text(json.dumps(
            dict(version=1,policy=TITLE_POLICY,duration=seconds,chunks=chunks))+'\n')
