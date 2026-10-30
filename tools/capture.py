"""Capture the live Framer site into original/ (reference for the rebuild).

Usage: python tools/capture.py
Standard library only; needs google-chrome.
"""
import html
import json
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / "original"
BASE = "https://www.realhealthkombucha.com/"
CHROME = "/usr/bin/google-chrome"
SLUGS = ["", "about", "gut-health-101", "reseller", "contact", "shop"]
IMG_RE = re.compile(r"https://framerusercontent\.com/images/[A-Za-z0-9_-]+\.[A-Za-z0-9]+")
FONT_RE = re.compile(r"font-family:\s*([^;}]+)")


def name(slug):
    return slug or "home"


def chrome(*args):
    return subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", *args],
        capture_output=True, text=True, timeout=180, check=True,
    )


def main():
    for d in ("pages", "assets", "screenshots"):
        (ORIG / d).mkdir(parents=True, exist_ok=True)
    manifest = {"images": {}, "pages": {}}
    fonts = {}
    for slug in SLUGS:
        url = BASE + slug
        dom = chrome("--virtual-time-budget=8000", "--dump-dom", url).stdout
        page = ORIG / "pages" / f"{name(slug)}.html"
        page.write_text(dom, encoding="utf-8")
        manifest["pages"][name(slug)] = f"original/pages/{name(slug)}.html"
        for m in FONT_RE.findall(html.unescape(dom)):
            fam = m.split(",")[0].strip().strip("'\"")
            if fam and not fam.startswith("var("):
                fonts[fam] = fonts.get(fam, 0) + 1
        for size, shot in (("1440,9000", "desktop"), ("390,12000", "phone")):
            chrome("--hide-scrollbars", "--virtual-time-budget=15000",
                   f"--window-size={size}",
                   f"--screenshot={ORIG / 'screenshots' / f'{name(slug)}-{shot}.png'}", url)
        print("captured", url)
    for p in (ORIG / "pages").glob("*.html"):
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
