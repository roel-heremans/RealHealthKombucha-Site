"""Capture the live Framer site into original/ (reference for the rebuild).

Usage: python tools/capture.py                     # full capture
       python tools/capture.py --desktop-dom-only  # only (re)dump pages-desktop/,
                                                   # keep pages/ and screenshots/
original/pages/ holds the DOM at Chrome's default (~800px) window, i.e. Framer's
phone/tablet variant; original/pages-desktop/ holds the DOM at 1440px (desktop variant).
Standard library only; needs google-chrome.
"""
import html
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / "original"
BASE = "https://www.realhealthkombucha.com/"
CHROME = "/usr/bin/google-chrome"
SLUGS = ["", "about", "gut-health-101", "reseller", "contact", "shop"]
IMG_RE = re.compile(r"https://framerusercontent\.com/(?:images|assets)/[A-Za-z0-9_-]+\.(?:jpe?g|png|webp|svg|gif)")
FONT_RE = re.compile(r"font-family:\s*([^;}]+)")


def name(slug):
    return slug or "home"


def chrome(*args):
    r = subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", *args],
        capture_output=True, text=True, timeout=180,
    )
    if r.returncode != 0:
        raise SystemExit(f"chrome failed ({r.returncode}): {r.stderr}")
    return r


PAGE_SETS = (("pages", "pages", ()), ("pages_desktop", "pages-desktop", ("--window-size=1440,9000",)))


def dump_dom(url, folder, extra):
    dom = chrome("--virtual-time-budget=8000", *extra, "--dump-dom", url).stdout
    if len(dom.strip()) < 1000:
        raise SystemExit(f"empty DOM for {url} ({folder})")
    return dom


def main():
    desktop_only = "--desktop-dom-only" in sys.argv[1:]
    for d in ("pages", "pages-desktop", "assets", "screenshots"):
        (ORIG / d).mkdir(parents=True, exist_ok=True)
    manifest = {"images": {}}
    for key, folder, extra in PAGE_SETS:
        manifest[key] = {}
        for slug in SLUGS:
            url = BASE + slug
            dest = ORIG / folder / f"{name(slug)}.html"
            if not (desktop_only and folder == "pages"):
                dest.write_text(dump_dom(url, folder, extra), encoding="utf-8")
                print("dumped", folder, url)
            manifest[key][name(slug)] = f"original/{folder}/{name(slug)}.html"
    if not desktop_only:
        for slug in SLUGS:
            url = BASE + slug
            for size, shot in (("1440,9000", "desktop"), ("390,12000", "phone")):
                chrome("--hide-scrollbars", "--virtual-time-budget=15000",
                       f"--window-size={size}",
                       f"--screenshot={ORIG / 'screenshots' / f'{name(slug)}-{shot}.png'}", url)
            print("screenshots", url)
    fonts = {}
    page_files = [p for _, folder, _ in PAGE_SETS for p in sorted((ORIG / folder).glob("*.html"))]
    for p in page_files:
        for m in FONT_RE.findall(html.unescape(p.read_text(encoding="utf-8"))):
            fam = m.split(",")[0].strip().strip("'\"")
            if fam and not fam.startswith("var("):
                fonts[fam] = fonts.get(fam, 0) + 1
    for p in page_files:
        for img in sorted(set(IMG_RE.findall(html.unescape(p.read_text(encoding="utf-8"))))):
            if img in manifest["images"]:
                continue
            dest = ORIG / "assets" / img.rsplit("/", 1)[1]
            if not dest.exists():
                req = urllib.request.Request(img, headers={"User-Agent": "Mozilla/5.0"})
                dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
            manifest["images"][img] = f"original/assets/{dest.name}"
    manifest["images"] = dict(sorted(manifest["images"].items()))
    (ORIG / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    lines = ["Font families seen in rendered DOM (name: occurrences)"]
    lines += [f"{k}: {v}" for k, v in sorted(fonts.items(), key=lambda kv: -kv[1])]
    (ORIG / "fonts.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(len(manifest["images"]), "images")


if __name__ == "__main__":
    main()
