import { el, post } from "./api.mjs";
import { bytes } from "./storage.mjs";

export function deploymentControls(catalog) {
  const root=el("section",{class:"section deployment-export"},el("h2",{text:"Deploy selected content on another machine"}),
    el("p",{text:"Choose any combination of packs, categories, and collections. The bundle includes their current transcripts, references, companion files, and published complete or partial audio. Personal history, TTS settings, voice references, and pending jobs stay here."}));
  const inputs={};
  const options={packs:catalog.packs.filter(p=>!p.id.startsWith("audio-")).map(p=>[p.id,p.title]),
    categories:[...new Set(catalog.lectures.flatMap(r=>r.categories||[]))].sort().map(v=>[v,v]),
    collections:catalog.courses.map(c=>[c.id,c.title])};
  const filters=el("div",{class:"grid"});
  for(const [field,rows] of Object.entries(options)) {
    const select=el("select",{multiple:true,size:6,"aria-label":"Export "+field},...rows.map(([value,text])=>el("option",{value,text})));
    inputs[field]=select;
    filters.append(el("label",{},field[0].toUpperCase()+field.slice(1),select));
  }
  const status=el("p",{role:"status",class:"muted"});
  const preview=el("button",{type:"button",text:"Preview selection"});
  const download=el("button",{type:"button",text:"Build transfer bundle"});
  const result=el("div");
  async function run(onlyPreview) {
    preview.disabled=download.disabled=true; result.replaceChildren();
    status.textContent=onlyPreview?"Checking content and published recordings…":"Copying selected content and recordings. Large bundles can take several minutes…";
    try {
      const selection=Object.fromEntries(Object.entries(inputs).map(([field,input])=>[field,[...input.selectedOptions].map(o=>o.value)]));
      const data=await post("/api/library/deployment",{selection,preview:onlyPreview});
      status.textContent=`${data.lectures} lectures · ${data.complete} with complete audio · ${data.partial} with partial audio · ${data.missing} without audio · ${data.recordings} recordings`;
      if(data.url) result.append(el("a",{href:data.url,download:"",text:`Download bundle (${bytes(data.bytes)})`}),
        el("p",{text:"Copy the ZIP to the new machine. Install the standalone reader, then restore into a new library directory and serve it without --repository:"}),
        el("pre",{text:"python -m ailectures --library /path/to/new-library restore BUNDLE.zip\npython -m ailectures --library /path/to/new-library serve --installed-only --host 0.0.0.0 --port 8001"}));
    } catch(error){status.textContent=error.message;}
    finally{preview.disabled=download.disabled=false;}
  }
  preview.onclick=()=>run(true); download.onclick=()=>run(false);
  root.append(filters,el("div",{class:"actions"},preview,download),status,result);
  return root;
}
