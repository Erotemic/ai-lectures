"""Authored title roles preserve speech/pagination and get isolated synthesis."""
import io
import json
import shutil
import urllib.request
import wave

import pytest

from ailectures.core import extract_text
from ailectures.narration import page_delivery, title_spans, TITLE_POLICY
from dkvis.presentation.audio_library import AudioLectureLibrary, split_pages
from dkvis.presentation.media import duration


def manuscript(body):
    return '# Display-only title\n<!-- BEGIN SPOKEN LECTURE -->\n'+body+'\n<!-- END SPOKEN LECTURE -->\n'


def test_structural_titles_keep_occurrence_identity_and_all_canonical_words():
    source=manuscript('## First heading\n\nA paragraph with First heading in its prose.\n\n### Second heading\n\nAnother paragraph.')
    transcript=extract_text(source).strip()
    spans=title_spans(source,transcript)
    assert len(spans)==2
    assert [' '.join(transcript.split()[a:b]) for a,b in spans]==['First heading','Second heading']
    pages=split_pages(transcript,max_chars=100)
    plans=page_delivery(source,transcript,tuple(pages))
    for text,parts in zip(pages,plans):
        if parts: assert ' '.join(' '.join(part['text'] for part in parts).split())==' '.join(text.split())
    assert sum(part['role']=='title' for parts in plans for part in parts)==2
    assert not title_spans(source,'A different revision.')
    assert not title_spans(manuscript('An ordinary short paragraph.'),'An ordinary short paragraph.')


def wav_bytes():
    stream=io.BytesIO()
    with wave.open(stream,'wb') as output:
        output.setnchannels(1);output.setsampwidth(2);output.setframerate(24000)
        output.writeframes(b'\x10\x00'*24000)
    return stream.getvalue()


@pytest.mark.skipif(not shutil.which('ffmpeg'),reason='FFmpeg unavailable')
@pytest.mark.parametrize('model,instruction_field',[('breeze-tts2','instruction'),('breeze-tts2','none'),('kokoro',None),('kokoro','instructions')])
def test_title_requests_body_policy_pauses_and_ogg_word_alignment(tmp_path,monkeypatch,model,instruction_field):
    monkeypatch.setenv('DKVIS_AUDIO_BREEZE_LONG_FORM','1')
    monkeypatch.setenv('DKVIS_AUDIO_BREEZE_JOB_API','0')
    monkeypatch.delenv('DKVIS_AUDIO_OUTPUT_FORMAT',raising=False)
    source=manuscript('## First heading\n\nFirst body sentence.\n\n## Second heading\n\nSecond body sentence.')
    (tmp_path/'001000-test.md').write_text(source)
    profile=dict(endpoint='http://127.0.0.1:1/v1/audio/speech',model=model,voice='af_bella',response_format='wav')
    if instruction_field is not None: profile['title_instruction_field']=instruction_field
    document=dict(profile='test',defaults={},profiles={'test':profile})
    requests=[]
    class Response(io.BytesIO):
        pass
    def respond(request,timeout):
        payload=json.loads(request.data); requests.append(payload)
        result=Response(wav_bytes()); result.headers={'Content-Type':'audio/wav'}
        if payload.get('long_form'):
            result.headers.update({'X-Local-AI-Speech-Policy':'paragraph80-v1',
                'X-Local-AI-Speech-Timings':json.dumps(dict(version=1,policy='paragraph80-v1',duration=1,
                    chunks=[dict(words=len(payload['input'].split()),start=0,end=1)]))})
        return result
    monkeypatch.setattr(urllib.request,'urlopen',respond)
    engine=AudioLectureLibrary(sources=tmp_path,cache=tmp_path/'cache',document=document,profile="test",title_handling=True,output_format='ogg')
    try:
        settings=engine.settings()
        target,text,key=engine._target('001000',0,settings)
        engine._generate(target,text,settings)
        assert target.read_bytes().startswith(b'OggS')
        assert [request['input'] for request in requests]==['First heading','First body sentence.','Second heading','Second body sentence.']
        for index,request in enumerate(requests):
            if index%2==0:
                assert not request.get('long_form')
                if instruction_field and instruction_field != 'none': assert instruction_field in request
                else: assert not {'instruction','instructions','voice_direction','direction'} & request.keys()
            else:
                assert not {'instruction','instructions','voice_direction','direction'} & request.keys()
                if model=='breeze-tts2': assert request['long_form'] and request['cfg_scale']==1
        timing=json.loads(target.with_name(target.name+'.timings.json').read_text())
        assert timing['policy']==TITLE_POLICY
        assert sum(c['words'] for c in timing['chunks'])==len(text.split())
        assert [c['role'] for c in timing['chunks']]==['title','body','title','body']
        assert timing['chunks'][1]['start']-timing['chunks'][0]['end']>=0.49
        assert timing['chunks'][2]['start']-timing['chunks'][1]['end']>=0.24
        assert abs(duration(target)-5.5)<0.05
        plain=engine._target_from_text('missing',0,settings,text)
        assert plain[2]!=key
    finally:engine.close()


def test_delivery_policy_does_not_invalidate_unchanged_body_cache_directory():
    from ailectures.narration import speech_cache_key
    before = {'settings': {'output_format':'ogg','model':'kokoro'}}
    after = {'settings':dict(before['settings'],reader_title_policy=TITLE_POLICY)}
    assert speech_cache_key('test:001000',before)==speech_cache_key('test:001000',after)
    assert 'reader_title_policy' in after['settings']
