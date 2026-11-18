"""Storage encoding is independent of upstream transport and cache identity."""
import json
import shutil
import subprocess
import wave

import pytest

from dkvis.presentation.audio_library import AudioLectureLibrary, SpeechSettings
from ailectures.production import recording_from_engine
from ailectures.core import text_digest


@pytest.mark.skipif(not shutil.which('ffmpeg'),reason='FFmpeg unavailable')
def test_mp3_and_ogg_encode_real_audio_and_have_distinct_cache_addresses(tmp_path,monkeypatch):
    monkeypatch.delenv('DKVIS_AUDIO_OUTPUT_FORMAT',raising=False)
    document={'profile':'test','defaults':{'timeout_seconds':30,'max_chars':420,'max_words':65},
              'profiles':{'test':{'endpoint':'http://127.0.0.1:1/v1/audio/speech','model':'kokoro','voice':'af_bella','response_format':'wav'}}}
    source=tmp_path/'input.wav'
    with wave.open(str(source),'wb') as stream:
        stream.setnchannels(1);stream.setsampwidth(2);stream.setframerate(24000);stream.writeframes(b'\0\0'*48000)
    libraries=[AudioLectureLibrary(sources=tmp_path,cache=tmp_path/'cache',document=document,profile="test",output_format=fmt) for fmt in ('mp3','ogg')]
    try:
        settings=SpeechSettings('kokoro','af_bella',1)
        targets=[lib._target_from_text('000000',0,settings,'A complete sentence.') for lib in libraries]
        assert targets[0][0].suffix=='.mp3' and targets[1][0].suffix=='.ogg'
        assert targets[0][2]!=targets[1][2]
        for lib,(target,_,key) in zip(libraries,targets):
            target.parent.mkdir(parents=True,exist_ok=True)
            subprocess.run(['ffmpeg','-nostdin','-y','-loglevel','error','-i',str(source),*lib._encoding_args(target)],check=True)
            assert lib._ready(target,key)
            if lib.output_format=='ogg':assert target.read_bytes().startswith(b'OggS')
            else:assert not target.read_bytes().startswith(b'OggS')
        ogg=libraries[1];target=targets[1][0]
        row=dict(id='test:001000',spoken_sha256=text_digest('A complete sentence.'))
        ogg.detail=lambda _:dict(transcript_sha256=row['spoken_sha256'],pagination_version='test',page_chars=600,pages=['A complete sentence.'])
        ogg._target_from_text=lambda *args:(target,'A complete sentence.',targets[1][2])
        rec,files=recording_from_engine(ogg,'000000',row,variant='test')
        assert rec['segments'][0]['media_type']=='audio/ogg'
        assert rec['segments'][0]['path'].endswith('.ogg')
        assert rec['complete']
    finally:
        for lib in libraries:lib.close()


def test_invalid_output_format_is_rejected(tmp_path):
    document={'profile':'test','defaults':{},'profiles':{'test':{'endpoint':'http://127.0.0.1:1/v1/audio/speech','model':'kokoro','voice':'af_bella','response_format':'wav'}}}
    with pytest.raises(ValueError,match='output_format'):
        AudioLectureLibrary(sources=tmp_path,cache=tmp_path/'cache',document=document,profile="test",output_format='nonsense')


@pytest.mark.skipif(not shutil.which('ffmpeg'),reason='FFmpeg unavailable')
def test_web_prepare_defaults_to_real_ogg_without_output_setting(tmp_path,monkeypatch):
    import io,time,urllib.request
    from starlette.testclient import TestClient
    from ailectures.web import create_app
    from ailectures.production import GenerationManager
    from ailectures.library import Library
    from ailectures.packs import export_release
    from test_content_packs import source_pack
    monkeypatch.delenv('DKVIS_AUDIO_OUTPUT_FORMAT',raising=False)
    config=tmp_path/'tts.toml'
    config.write_text('[profiles.test]\nendpoint="http://127.0.0.1:1/v1/audio/speech"\nmodel="kokoro"\nvoice="af_bella"\nresponse_format="wav"\n')
    pack=source_pack()
    export_release(pack,tmp_path/'source')
    library=Library(tmp_path/'library');library.store.install(tmp_path/'source')
    stream=io.BytesIO()
    with wave.open(stream,'wb') as output:
        output.setnchannels(1);output.setsampwidth(2);output.setframerate(24000);output.writeframes(b'\0\0'*48000)
    class Response(io.BytesIO):pass
    def respond(request,timeout):
        result=Response(stream.getvalue());result.headers={'Content-Type':'audio/wav'};return result
    monkeypatch.setattr(urllib.request,'urlopen',respond)
    manager=GenerationManager(library,config=config)
    with TestClient(create_app(library.store.root,generation_manager=manager)) as client:
        profiles=client.get('/api/library/production?probe=0').json()['profiles']
        assert profiles[0]['output_format']=='ogg'
        response=client.post('/api/library/production/prepare',json={'lecture_id':'music:001000','profile':'test'})
        assert response.status_code==202
        job=response.json()
        deadline=time.monotonic()+8
        while time.monotonic()<deadline:
            job=client.get('/api/library/production/jobs/'+job['id']).json()
            if job['state'] in {'ready','failed','settings_changed'}:break
            time.sleep(.02)
        assert job['state']=='ready',job
        row=client.get('/api/library/lectures/music:001000').json()
        segment=row['recordings'][0]['segments'][0]
        media=client.get(segment['url'])
        assert segment['media_type']=='audio/ogg'
        assert media.headers['content-type'].startswith('audio/ogg')
        assert media.content.startswith(b'OggS')
        preview=client.get('/api/library/production/jobs/'+job['id']+'/playback').json()
        transient=client.get(preview['recordings'][0]['segments'][0]['url'])
        assert transient.headers['content-type'].startswith('audio/ogg')
        assert transient.content.startswith(b'OggS')
