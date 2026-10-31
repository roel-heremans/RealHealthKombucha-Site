// Stub of firebase-firestore.js: read-only snapshots of sample_data.json, writes are no-ops.
import { data, later } from "./store.js";

const collections = data.collections; // { name: { id: {...doc} } }

export function initializeFirestore() { return { type: "firestore" }; }
export function persistentLocalCache() { return {}; }
export function persistentMultipleTabManager() { return {}; }

let autoId = 0;
export function collection(db, name) { return { type: "collection", name }; }
export function doc(parent, name, id) {
  if (parent && parent.type === "collection") return { type: "doc", name: parent.name, id: "auto" + ++autoId };
  return { type: "doc", name, id };
}
export function where(field, op, value) { return { field, op, value }; }
export function query(col, ...filters) { return { type: "query", name: col.name, filters }; }

function docSnap(name, id) {
  const d = (collections[name] || {})[id];
  return { id, exists: () => d !== undefined, data: () => (d === undefined ? undefined : structuredClone(d)) };
}
function matches(d, f) {
  if (f.op === "==") return d[f.field] === f.value;
  throw new Error("stub: unsupported where op " + f.op);
}
function querySnap(ref) {
  const docs = Object.entries(collections[ref.name] || {})
    .filter(([, d]) => (ref.filters || []).every((f) => matches(d, f)))
    .map(([id]) => docSnap(ref.name, id));
  return { docs, size: docs.length, empty: docs.length === 0, forEach: (fn) => docs.forEach(fn) };
}

export function onSnapshot(ref, next) {
  later(() => next(ref.type === "doc" ? docSnap(ref.name, ref.id) : querySnap(ref)));
  return () => {};
}
export async function getDoc(ref) { return docSnap(ref.name, ref.id); }
export async function addDoc(col) { return doc(col); }
export async function setDoc() {}
export async function updateDoc() {}
export async function deleteDoc() {}
export function serverTimestamp() { return { seconds: Math.floor(Date.now() / 1000), nanoseconds: 0 }; }
export function writeBatch() {
  return { set() {}, update() {}, delete() {}, commit: async () => {} };
}
