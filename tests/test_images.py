"""Checks on the generated image set in assets/img (produced by tools/prepare_images.py)."""
import struct
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
sys.path.insert(0, str(ROOT / "tools"))

FIXED = [
    "logo-dark.png",
    "logo-light.png",
    "favicon.png",
    "review-qr.svg",
    "og.jpg",
]
FLAVOURS = ["ginger", "wild-orange", "lime", "green-mandarine", "metabolic-boost", "lemon-turmeric"]
EXCLUDED_STEMS = ["original", "a0_board", "logo_lowres", "hot-tub", "hottub", "welcome", "20260117"]


def _png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", path
    return struct.unpack(">II", head[16:24])


def _jpeg_size(path):
    data = path.read_bytes()
    assert data[:2] == b"\xff\xd8", path
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        (seglen,) = struct.unpack(">H", data[i + 2 : i + 4])
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", data[i + 5 : i + 9])
            return w, h
        i += 2 + seglen
    raise AssertionError(f"no SOF marker in {path}")


@pytest.mark.parametrize("name", FIXED)
def test_fixed_names_exist(name):
    assert (IMG / name).is_file(), name


def test_exactly_six_flavour_labels():
    names = sorted(p.name for p in (IMG / "flavours").iterdir())
    assert names == sorted(f"{f}.png" for f in FLAVOURS)


@pytest.mark.parametrize("flavour", FLAVOURS)
def test_flavour_label_width(flavour):
    w, h = _png_size(IMG / "flavours" / f"{flavour}.png")
    assert w == 520 and h > w


def test_favicon_is_64px():
    assert _png_size(IMG / "favicon.png") == (64, 64)


def test_og_is_1200x630():
    assert _jpeg_size(IMG / "og.jpg") == (1200, 630)


def test_photo_count_and_limits():
    photos = sorted((IMG / "photos").glob("*.jpg"))
    assert 12 <= len(photos) <= 20, len(photos)
    for p in photos:
        assert p.stat().st_size < 300 * 1024, (p.name, p.stat().st_size)
        w, _ = _jpeg_size(p)
        assert w <= 1600, (p.name, w)


def test_no_excluded_names():
    for p in IMG.rglob("*"):
        low = p.name.lower()
        for stem in EXCLUDED_STEMS:
            assert stem not in low, p


def test_output_guard_refuses_paths_outside_assets_img(tmp_path):
    import prepare_images

    with pytest.raises(ValueError):
        prepare_images.safe_output(tmp_path / "x.jpg")
    with pytest.raises(ValueError):
        prepare_images.safe_output(IMG / ".." / "evil.jpg")
    with pytest.raises(ValueError):
        prepare_images.safe_output(Path.home() / "Documents" / "PersonalRepos" / "Kombucha" / "assets" / "x.jpg")
    assert prepare_images.safe_output(IMG / "photos" / "ok.jpg") == (IMG / "photos" / "ok.jpg").resolve()
