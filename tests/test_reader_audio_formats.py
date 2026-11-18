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
    libraries=[AudioLectureLibrary(sources=tmp_path,cache=tmp_path/'cache',document=document,output_format=fmt) for fmt in ('mp3','ogg')]
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
        AudioLectureLibrary(sources=tmp_path,cache=tmp_path/'cache',document=document,output_format='nonsense')
