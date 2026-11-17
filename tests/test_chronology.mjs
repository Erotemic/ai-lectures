import assert from "node:assert/strict";
import { dateOrder, chronologyRecord, sortChronologically } from "../ailectures/static/chronology.mjs";

const rows = [
  {id:"later-first",chronology:{work:{start:2000,end:2000},setting:{start:1700,end:1800}}},
  {id:"later-second",chronology:{work:{start:2000,end:2000},setting:{start:1700,end:1800}}},
  {id:"early-first",chronology:{work:{start:-500,end:-300},setting:{start:1990,end:2000}}},
  {id:"early-second",chronology:{work:{start:-500,end:-300},setting:{start:1990,end:2000}}},
  {id:"unknown"},
];
const before=JSON.stringify(rows);
assert.deepEqual(sortChronologically(rows,'date-work').map(row=>row.id),['early-first','early-second','later-first','later-second','unknown']);
assert.deepEqual(sortChronologically(rows,'date-work-desc').map(row=>row.id),['later-first','later-second','early-first','early-second','unknown']);
assert.deepEqual(sortChronologically(rows,'date-setting').map(row=>row.id),['later-first','later-second','early-first','early-second','unknown']);
assert.deepEqual(sortChronologically(rows,'date-period').map(row=>row.id),rows.map(row=>row.id));
assert.equal(JSON.stringify(rows),before);
assert.equal(dateOrder('short'),null);
assert.deepEqual(dateOrder('date-life-desc'),{axis:'life',descending:true});
assert.equal(chronologyRecord({chronology:{work:{start:0,end:1}}},'work'),null);
assert.equal(chronologyRecord({chronology:{work:{start:5,end:1}}},'work'),null);
assert.equal(chronologyRecord({chronology:{work:{start:1e14,end:1e14}}},'work'),null);
assert.equal(chronologyRecord({metadata:{year:1851}},'work'),null);
console.log('Chronological views retain equal-date authored order, distinguish date axes and leave undated items last');
