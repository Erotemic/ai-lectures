"""Guard audio reader bootstrap when course tracks and TTS profiles change."""

from pathlib import Path
import shutil
import subprocess

import pytest

from dkvis.presentation.audio_library import AUDIO_PAGE


_BOOTSTRAP_CHECK = r'''
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync(process.argv[1], 'utf8');
const begin = html.indexOf('async function init(){');
const end = html.indexOf('\ninit();', begin);
assert(begin >= 0 && end > begin);
const source = html.slice(begin, end) + '\ninit()';
async function scenario(query, failTracks=false, failVoices=false) {
  const nodes = new Map();
  const get = id => {
    if(!nodes.has(id)) nodes.set(id, {
      value:'', textContent:'', checked:false, options:[], children:[],
      append(item){ this.options.push(item); },
      insertBefore(item){ this.children.push(item); }
    });
    return nodes.get(id);
  };
  const visited=[];
  let chosen=null;
  const tracks = [
    {id:'g2', kind:'audio', label:'G2', summary:'Comprehensive lectures'},
    {id:'music-theory', kind:'audio', label:'Music Theory', summary:'Harmony and form'},
  ];
  const ctx = {
    $:get, document:{createElement(){return {dataset:{}};}},
    saved:(_key, fallback)=>fallback,
    location:{search:query},
    window:{setInterval:()=>0},
    availableAudioTracks:new Map([['g2', tracks[0]]]),
    api:async path=>{
      if(path==='/api/audio-profiles') return {default_profile:'kokoro', profiles:[
        {id:'kokoro', label:'Kokoro'},
        {id:'private-local', label:'Local voice from tts.local.toml'},
      ]};
      if(path==='/api/audio-tracks') {
        if(failTracks) throw Error('Track discovery unavailable');
        return {tracks};
      }
      throw Error('Unexpected API: '+path);
    },
    refreshVoices:async profile=>{
      visited.push(profile);
      if(failVoices) throw Error('TTS server offline');
    },
    setStatus:message=>{get('status').textContent=message;},
    switchTrack:async track=>{chosen=track;},
    URLSearchParams,
    Map,
  };
  await vm.runInNewContext(source, ctx);
  assert.deepEqual(get('profile').options.map(x=>x.value), ['kokoro','private-local']);
  assert.equal(get('profile').value, 'kokoro');
  assert.deepEqual(visited, ['kokoro']);
  if(failTracks){
    assert.equal(chosen, null);
    assert.match(get('loading').textContent, /Track discovery unavailable/);
  }else{
    assert.equal(chosen, query.includes('music-theory') ? 'music-theory' : 'g2');
    assert.equal(get('courseTracks').children.length, 2);
    assert.equal(ctx.availableAudioTracks.has('music-theory'), true);
    assert.doesNotMatch(get('loading').textContent, /Could not load lectures/);
    if(failVoices) assert.match(get('status').textContent, /TTS server offline/);
  }
}
(async()=>{
  await scenario('?track=music-theory');
  await scenario('?track=invalid');
  await scenario('?track=music-theory', true);
  await scenario('?track=music-theory', false, true);
})().catch(err=>{console.error(err); process.exitCode=1;});
'''


def test_reader_initializes_tts_profiles_before_track_switching():
    node = shutil.which('node')
    if node is None:
        pytest.skip('Node.js is unavailable')
    result = subprocess.run(
        [node, '-e', _BOOTSTRAP_CHECK, str(AUDIO_PAGE)],
        check=False, text=True, capture_output=True, timeout=15,
    )
    assert result.returncode == 0, result.stderr
