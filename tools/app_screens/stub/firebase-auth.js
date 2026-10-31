// Stub of firebase-auth.js: a fixed demo restaurant login, no network.
import { data, signedIn, later } from "./store.js";

const auth = { currentUser: signedIn ? { ...data.user } : null };
const listeners = [];
const notify = () => listeners.forEach((cb) => later(() => cb(auth.currentUser)));
const fail = (code) => Promise.reject(Object.assign(new Error(code), { code }));

export function getAuth() { return auth; }
export function onAuthStateChanged(a, cb) {
  listeners.push(cb);
  later(() => cb(auth.currentUser));
  return () => listeners.splice(listeners.indexOf(cb), 1);
}
export function signInWithEmailAndPassword() { return fail("auth/demo-only"); }
export function createUserWithEmailAndPassword() { return fail("auth/demo-only"); }
export function sendPasswordResetEmail() { return fail("auth/demo-only"); }
export async function signOut() { auth.currentUser = null; notify(); }
