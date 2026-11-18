import assert from 'node:assert/strict';
import { coverageModel, sectionKey } from '../ailectures/static/coverage-model.mjs';
import { libraryStats } from '../ailectures/static/stats-model.mjs';
import { tagFacet } from '../ailectures/static/tag-model.mjs';
const city=(country,name)=>['Place: Americas','Place: '+country,'Place: '+name];
const rows=[
  {id:'a:1',namespace:'a',section:'story',words:145,places:['Boston'],tag_paths:[city('United States','Boston'),city('United States','New York')]},
  {id:'a:2',namespace:'a',section:'story',words:290,places:['United States'],tag_paths:[city('United States','Boston')]},
  {id:'b:1',namespace:'b',section:'story',words:145,tag_paths:[city('United States','New York')]},
  {id:'a:3',namespace:'a',words:Infinity,tags:['Place: United States'],tag_paths:[['Place: Americas','Place: United States']]},
  {id:'a:4',namespace:'a',words:-1,tag_paths:[['Place: Americas','Place: United States']]},
  {id:'c:1',places:['Canada'],words:145},
  {id:'d:1',tags:['Geometry']},
];
const before=JSON.stringify(rows);
const model=coverageModel([...rows,rows[0]]);
assert.equal(model.rows.length,7);
assert.equal(model.tagged('Places').size,6);
const america=model.forests.get('Places').get('Place: Americas');
const us=america.children.get('Place: United States');
const stats=model.totals(us);
assert.equal(stats.lectures,5,'Multiple cities and duplicate rows count once in a parent');
assert.equal(stats.sections,4,'One declared section groups installments; different packs and unsectioned lectures remain distinct');
assert.equal(stats.atLevel,2,'Broad-only coverage does not acquire city tags');
assert.equal(stats.minutes,4,'Invalid word counts do not contaminate listening totals');
assert.equal(stats.groups[0].lectures,2);
assert.deepEqual(stats.groups[0].members.map(row=>row.id),['a:1','a:2']);
assert.equal(new Set(stats.groups.flatMap(group=>group.members.map(row=>row.id))).size,stats.lectures);
assert.equal(model.totals(america).lectures,5);
assert.equal(model.forests.get('Places').get('Place: Canada').lectures.size,1,'Unmapped labels stay visible without invented parents');
assert.notEqual(sectionKey(rows[0]),sectionKey(rows[2]));
assert.notEqual(sectionKey(rows[3]),sectionKey(rows[4]));
assert.equal(JSON.stringify(rows),before,'Coverage must not modify lecture metadata or playback ordering');
const totals=libraryStats({lectures:rows});
assert.equal(totals.places.find(row=>row.title==='United States').lectures,5);
assert.equal(totals.directPlaces.find(row=>row.title==='United States').lectures,1);
assert.equal(totals.withPlaces,6);
assert.equal(coverageModel([]).tagged('Places').size,0);
assert.equal(tagFacet('Historical setting: 17th century CE'),'Historical setting');
console.log('Coverage rolls up paths, deduplicates ancestors, preserves section provenance, and exposes broad-only and missing metadata.');
