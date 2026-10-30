import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / "original"
IMG_RE = re.compile(r"https://framerusercontent\.com/(?:images|assets)/[A-Za-z0-9_-]+\.(?:jpe?g|png|webp|svg|gif)")
SLUGS = {"home", "about", "gut-health-101", "reseller", "contact", "shop"}


def test_manifest_complete():
    manifest_path = ORIG / "manifest.json"
    assert manifest_path.exists(), "run tools/capture.py and commit original/"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    urls = set()
    for key, folder in (("pages", "pages"), ("pages_desktop", "pages-desktop")):
        assert key in manifest, key
        assert set(manifest[key]) == SLUGS, key
        for slug, rel in manifest[key].items():
            assert rel == f"original/{folder}/{slug}.html"
            assert (ROOT / rel).stat().st_size > 1000, rel
        for page in (ORIG / folder).glob("*.html"):
            urls |= set(IMG_RE.findall(html.unescape(page.read_text(encoding="utf-8"))))
    assert urls, "no images found in captured pages"
    for url in urls:
        assert url in manifest["images"], url
        f = ROOT / manifest["images"][url]
        assert f.exists() and f.stat().st_size > 0, url
    for slug in SLUGS:
        for kind in ("desktop", "phone"):
            assert (ORIG / "screenshots" / f"{slug}-{kind}.png").stat().st_size > 0
    assert (ORIG / "fonts.txt").read_text(encoding="utf-8").strip()


def test_og_image_captured():
    manifest = json.loads((ORIG / "manifest.json").read_text(encoding="utf-8"))
    og = "https://framerusercontent.com/assets/OQTRXPkK6HaR7C9GovB4aFa7Eak.jpeg"
    assert og in manifest["images"]
    assert (ROOT / manifest["images"][og]).stat().st_size > 0


def test_desktop_dom_is_desktop_variant():
    """pages-desktop/ must hold Framer's desktop variant (long home banner)."""
    dom = (ORIG / "pages-desktop" / "home.html").read_text(encoding="utf-8")
    assert "on your next order" in dom
