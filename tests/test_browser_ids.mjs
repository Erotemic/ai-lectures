import assert from 'node:assert/strict';
import {randomId} from '../ailectures/static/api.mjs';
const original=Object.getOwnPropertyDescriptor(globalThis,'crypto');
const native=globalThis.crypto;
const uuid=/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
try {
  // Match an ordinary HTTP origin: getRandomValues exists, randomUUID does not.
  Object.defineProperty(globalThis,'crypto',{configurable:true,value:{getRandomValues:native.getRandomValues.bind(native)}});
  const values=Array.from({length:100},()=>randomId());
  assert.equal(new Set(values).size,values.length);
  for(const value of values) assert.match(value,uuid);
  Object.defineProperty(globalThis,'crypto',{configurable:true,value:undefined});
  assert.match(randomId(),uuid);
} finally {
  Object.defineProperty(globalThis,'crypto',original);
}
assert.match(randomId(),uuid);
console.log('Device and event IDs work on localhost and plain HTTP origins');
