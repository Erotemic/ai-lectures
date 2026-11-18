/** Keep the next two immutable blocks in memory before a slow link needs them. */
export class AudioBlockCache {
  constructor({fetch: fetcher=globalThis.window?.fetch?.bind(window),urls=globalThis.URL,maxBytes=24*1024*1024}={}) {
    this.fetcher=fetcher; this.urls=urls; this.maxBytes=maxBytes; this.entries=new Map(); this.recording=null;
  }
  reset(recording) {
    if(this.recording===recording) return;
    this.close(); this.recording=recording;
  }
  close() {
    for(const entry of this.entries.values()) { entry.abort.abort(); if(entry.url) this.urls.revokeObjectURL(entry.url); }
    this.entries.clear(); this.recording=null;
  }
  cached(url) { return this.entries.get(url)?.url; }
  pending(url) { return this.entries.get(url)?.promise; }
  prefetch(recording,index) {
    if(!this.fetcher || !this.urls?.createObjectURL) return;
    this.reset(recording.id);
    const upcoming=recording.segments.filter(s=>s.index>index&&s.index<=index+2).sort((a,b)=>a.index-b.index);
    const wanted=new Set([...upcoming.map(s=>s.url),recording.segments.find(s=>s.index===index)?.url]);
    for(const [key,entry] of this.entries) if(!wanted.has(key)) {
      entry.abort.abort(); if(entry.url) this.urls.revokeObjectURL(entry.url); this.entries.delete(key);
    }
    let previous=Promise.resolve();
    for(const segment of upcoming) {
      if(this.entries.has(segment.url)) { previous=this.entries.get(segment.url).promise; continue; }
      const entry={abort:new AbortController()};
      entry.promise=previous.catch(()=>{}).then(async()=>{
        const response=await this.fetcher(segment.url,{cache:"force-cache",credentials:"same-origin",signal:entry.abort.signal});
        if(!response.ok) throw Error("Audio prefetch failed");
        if(Number(response.headers.get("Content-Length"))>this.maxBytes) throw Error("Audio block exceeds prefetch budget");
        const blob=await response.blob();
        if(blob.size>this.maxBytes || entry.abort.signal.aborted) return null;
        if(this.entries.get(segment.url)!==entry) return null;
        entry.url=this.urls.createObjectURL(blob); return entry.url;
      }).catch(()=>null);
      this.entries.set(segment.url,entry); previous=entry.promise;
    }
  }
}
