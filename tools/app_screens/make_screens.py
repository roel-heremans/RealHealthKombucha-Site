#!/usr/bin/env python3
"""Real screenshots of the kombucha orders app, rendered offline with sample data.

Usage: python tools/app_screens/make_screens.py [--app ~/Documents/PersonalRepos/kombucha-orders-app]
(needs Pillow and google-chrome; the system python3 has Pillow, the .venv does not)

How it works (the orders-app repo is only read, never written):
1. Copy the app's files (index.html, lib.js, sw.js, manifest, icons/) into a temp dir.
2. In the COPY: point the three Firebase CDN imports at local stub modules (stub/*.js, which serve
   sample_data.json: a "Demo Café" restaurant login, the six flavours, a few orders and recibos),
   switch off the service-worker registration, and add a small head script that sets the app
   language (localStorage `ko_lang`, from ?lang=) and scrolls to the wanted card (?shot=).
3. Serve the temp dir on 127.0.0.1 and screenshot with headless Chrome at 390x844, DPR 2, through
   a 390px iframe (headless windows cannot be narrower than 500px), then crop.
   Chrome cannot reach Firebase (or anything else): every host except 127.0.0.1 fails to resolve.
   A net-log of every run is scanned afterwards; the script fails if the app tried any Firebase,
   EmailJS or CallMeBot URL, and lists Chrome's own (blocked) background requests.
   The browser locale follows the language (date field), and a temporary fontconfig maps the
   app's `system-ui` font to Roboto, as on an Android phone; the app's CSS is not touched.
4. Write assets/img/app/<screen>-<lang>.png, quantised to 256 colours.
"""
import argparse, functools, os, re, shutil, subprocess, sys, tempfile, threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "img" / "app"
APP_FILES = ["index.html", "lib.js", "sw.js", "manifest.webmanifest", "icons"]
FIREBASE = "https://www.gstatic.com/firebasejs/10.12.0/firebase-{}.js"
RESOLVER_RULES = "MAP * ~NOTFOUND, EXCLUDE 127.0.0.1"   # nothing but the local server resolves
APP_BACKENDS = re.compile(r"firebase|firestore|identitytoolkit|securetoken|emailjs|callmebot", re.I)
LOCALES = {"en": "en-GB", "pt": "pt-PT"}
FONTS_CONF = """<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig>
<include ignore_missing="yes">/etc/fonts/fonts.conf</include>
<alias binding="strong"><family>system-ui</family><prefer><family>Roboto</family></prefer></alias>
<alias binding="strong"><family>sans-serif</family><prefer><family>Roboto</family></prefer></alias>
</fontconfig>"""
W, H, DPR = 390, 844, 2
# name -> query string for the app copy (lang is added per language). The restaurant view is one
# page (new order / your orders / my recibos); "history" scrolls to "Your orders", which with the
# sample data ends at the bottom of the page, so history and recibos share one screen.
SCREENS = {
    "signup": "signup&fill=signup",
    "new-order": "shot=top",
    "history": "shot=your_orders",
}

# Added to the <head> of the COPY only. Sets the language before the app renders; after the
# stubbed snapshots have rendered, scrolls the card whose title is the app's own string for
# `shot` to the top, or pre-selects "Restaurant / café" on the signup form.
HEAD_SCRIPT = """<script>
(function () {
  var q = new URLSearchParams(location.search);
  try { localStorage.setItem("ko_lang", q.get("lang") || "en"); } catch (e) {}
  window.addEventListener("load", function () { setTimeout(function () {
    var shot = q.get("shot");
    if (shot && shot !== "top") {
      var want = window.KO.t(q.get("lang") || "en", shot);
      var h = Array.prototype.find.call(document.querySelectorAll("#restaurantBody .card h3"),
        function (x) { return x.textContent.trim() === want; });
      if (h) window.scrollTo(0, h.closest(".card").getBoundingClientRect().top + window.scrollY - 12);
    }
    if (q.get("fill") === "signup") {
      var set = function (id, v) { var el = document.getElementById(id); el.value = v;
        el.dispatchEvent(new Event("input", { bubbles: true })); };
      set("suType", "restaurant");
      set("suName", "Demo Café");
    }
    document.documentElement.setAttribute("data-shot-ready", "1");
  }, 300); });
})();
</script>"""


def prepare_copy(app_dir, dest):
    for name in APP_FILES:
        src = app_dir / name
        (shutil.copytree if src.is_dir() else shutil.copy2)(src, dest / name)
    shutil.copytree(HERE / "stub", dest / "stub")
    shutil.copy2(HERE / "sample_data.json", dest / "stub" / "sample_data.json")
    html = (dest / "index.html").read_text()
    for mod in ("app", "auth", "firestore"):
        url = FIREBASE.format(mod)
        assert url in html, f"import not found: {url}"
        html = html.replace(url, f"./stub/firebase-{mod}.js")
    sw = 'if ("serviceWorker" in navigator) {'
    assert html.count(sw) == 1, "service worker registration not found"
    html = html.replace(sw, "if (false) { // service worker off in the screenshot copy")
    html = html.replace("<head>", "<head>\n" + HEAD_SCRIPT, 1)
    assert not re.search(r"gstatic|firebaseio|googleapis", html.split("const FIREBASE_CONFIG")[0]), \
        "a Firebase URL survived the rewrite"
    (dest / "index.html").write_text(html)


def serve(directory):
    class Quiet(SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(directory)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def shoot(url, png, profile, netlog, lang, env):
    cmd = ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           "--no-first-run", "--no-default-browser-check", "--disable-sync",
           "--disable-background-networking", "--disable-component-update",
           f"--host-resolver-rules={RESOLVER_RULES}", f"--user-data-dir={profile}",
           f"--lang={LOCALES[lang]}", f"--accept-lang={LOCALES[lang]}",
           f"--log-net-log={netlog}", "--net-log-capture-mode=Default",
           f"--force-device-scale-factor={DPR}", f"--window-size=500,{H}",
           "--virtual-time-budget=6000", f"--screenshot={png}", url]
    loc = LOCALES[lang].replace("-", "_")
    env = dict(env, LANG=f"{loc}.UTF-8", LANGUAGE=loc, LC_ALL=f"{loc}.UTF-8")
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120, env=env)
    if not png.exists():
        sys.exit(f"chrome produced no screenshot for {url}:\n{r.stderr[-2000:]}")


def requests_in(netlog):
    """(local, external) http(s) URLs Chrome attempted, from its net-log."""
    urls = set(re.findall(r'"url":"(https?://[^"]+)"', netlog.read_text(errors="replace")))
    local = {u for u in urls if u.startswith("http://127.0.0.1:")}
    return local, urls - local


def save(raw, out):
    im = Image.open(raw).convert("RGB")
    assert im.size[0] >= W * DPR and im.size[1] >= H * DPR, im.size
    im = im.crop((0, 0, W * DPR, H * DPR))
    im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(out, optimize=True)
    return out.stat().st_size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", type=Path, default=Path.home() / "Documents/PersonalRepos/kombucha-orders-app")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="app-screens-") as tmp:
        tmp = Path(tmp)
        site = tmp / "site"
        (site / "app").mkdir(parents=True)
        prepare_copy(args.app.expanduser(), site / "app")
        (tmp / "fonts.conf").write_text(FONTS_CONF)
        env = dict(os.environ, FONTCONFIG_FILE=str(tmp / "fonts.conf"))
        httpd = serve(site)
        base = f"http://127.0.0.1:{httpd.server_address[1]}/"
        external = set()
        try:
            for lang in ("en", "pt"):
                for name, qs in SCREENS.items():
                    frame = site / f"{name}-{lang}.html"
                    frame.write_text(
                        "<!doctype html><meta charset=utf-8><style>html,body{margin:0;background:#fff}"
                        f"iframe{{display:block;width:{W}px;height:{H}px;border:0}}</style>"
                        f'<iframe src="app/index.html?{qs}&lang={lang}"></iframe>')
                    raw, netlog = tmp / f"{name}-{lang}.raw.png", tmp / f"{name}-{lang}.netlog.json"
                    shoot(base + frame.name, raw, tmp / f"profile-{name}-{lang}", netlog, lang, env)
                    local, ext = requests_in(netlog)
                    assert any("/app/stub/sample_data.json" in u for u in local), "net-log not recording?"
                    external |= ext
                    out = OUT / f"{name}-{lang}.png"
                    print(f"  {out.relative_to(ROOT)}  {save(raw, out) // 1024} KB")
        finally:
            httpd.shutdown()
    backend = sorted(u for u in external if APP_BACKENDS.search(u))
    if backend:
        sys.exit("the app tried to reach a backend:\n  " + "\n  ".join(backend))
    print("net-log check: the app made no Firebase/EmailJS/CallMeBot request.")
    if external:
        hosts = sorted({re.sub(r"^https?://([^/]+).*", r"\1", u) for u in external})
        print("Chrome's own background requests (blocked, nothing resolves but 127.0.0.1):",
              ", ".join(hosts))


if __name__ == "__main__":
    main()
