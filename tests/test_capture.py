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
    assert set(manifest["pages"]) == SLUGS
    for rel in manifest["pages"].values():
        assert (ROOT / rel).stat().st_size > 0
    urls = set()
    for page in (ORIG / "pages").glob("*.html"):
        urls |= set(IMG_RE.findall(page.read_text(encoding="utf-8")))
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
