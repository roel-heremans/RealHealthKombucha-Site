// Shared in-memory state for the Firebase stubs. Sample data comes from
// sample_data.json, which make_screens.py copies next to these modules.
// It is a static JSON-module import (part of the module graph), so the app's
// module script still runs before DOMContentLoaded, as it does with real Firebase.
import data from "./sample_data.json" with { type: "json" };

export { data };
const params = new URLSearchParams(location.search);

// ?signup -> nobody signed in (the self-signup screen); otherwise the demo restaurant user.
export const signedIn = !params.has("signup");

// Fire callbacks the way Firebase does: asynchronously, after the page's
// DOMContentLoaded handlers (which install the real render functions) have run.
export function later(fn) {
  const go = () => setTimeout(fn, 0);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", go);
  else go();
}
