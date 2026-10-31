"""Build every image the site uses into assets/img/ from Roel's source folders.

Usage:  python tools/prepare_images.py [photo-target.jpg ...]
        (no arguments: build everything; with names: rebuild only those photos)

Sources (read-only, never written):
  ~/Documents/PersonalRepos/Kombucha/assets/01_images      photos
  ~/Documents/PersonalRepos/Kombucha/assets/design-logos   logo + flavour labels
  ~/Documents/PersonalRepos/Kombucha/output/qr             review QR

Uses ImageMagick `convert` via subprocess (argument lists, no shell), so file
names with spaces and commas are safe. Every output path passes through
safe_output(), which refuses anything outside assets/img/. Output is
deterministic: JPEGs are stripped, PNGs carry no date/time chunks.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = (ROOT / "assets" / "img").resolve()
KOMBUCHA = Path.home() / "Documents" / "PersonalRepos" / "Kombucha"
PHOTOS_SRC = KOMBUCHA / "assets" / "01_images"
LOGOS_SRC = KOMBUCHA / "assets" / "design-logos"
QR_SRC = KOMBUCHA / "output" / "qr" / "review_qr.svg"

OFF_WHITE = "#F8F6F3"
GREEN = "#1B3A2D"  # logo island/lettering colour
GOLD = "#C9A84C"  # logo sun colour
MAX_PHOTO_BYTES = 300 * 1024
PNG_DETERMINISTIC = ["-define", "png:exclude-chunks=date,time", "+set", "date:create", "+set", "date:modify"]

# --- Declarative mapping -----------------------------------------------------
# Photos: source file -> target name, max width, optional crop (WxH+X+Y in
# source pixels after auto-orient), starting JPEG quality.
PHOTOS = [
    # AI product scenes (Roel's own campaign images). The 04_21_06 scene has an
    # "Original" bottle on the far right; the crop keeps only the six flavours.
    ("ChatGPT Image Jun 30, 2026, 04_21_06 PM.png", "six-flavours-coast-lineup.jpg", 1190, "1190x660+0+272", 82),
    # Home hero: remake of the 04_27_12 poster without the poster logo; Roel's
    # face comes from his trained Higgsfield Soul ID (version "w4", 2026-10-31).
    # Used uncropped; Roel wanted the slogan at the bottom kept. The file name
    # changes with each new version so browsers do not show a cached copy.
    ("Hero Roel Nina tasting box w4 (Higgsfield Soul 2026-10-31).png", "roel-nina-tasting-box-coast-v3.jpg", 1535, None, 82),
    ("ChatGPT Image Jun 30, 2026, 04_43_48 PM.png", "roel-nina-six-pack-coast.jpg", 1086, None, 82),
    ("ChatGPT Image Jun 30, 2026, 04_54_14 PM.png", "six-flavours-sunset-coast.jpg", 1086, None, 82),
    # Roel & Nina portraits (2026-02-21 series, no hot-tub shots).
    ("WhatsApp Image 2026-02-21 at 20.38.14 (1).jpeg", "nina-glass-stone-wall.jpg", 1000, None, 80),
    ("WhatsApp Image 2026-02-21 at 20.38.14 (3).jpeg", "roel-drinking-fig-tree.jpg", 1000, None, 80),
    ("WhatsApp Image 2026-02-21 at 20.38.16 (3).jpeg", "roel-nina-balcony-bottles.jpg", 1000, None, 80),
    ("WhatsApp Image 2026-02-21 at 20.38.16.jpeg", "roel-glass-garden.jpg", 1000, None, 80),
    # Terrace bottle shots.
    ("Bottel01.jpeg", "bottle-in-hand-garden.jpg", 1000, None, 80),
    ("Bottel02.jpeg", "bottle-terrace-sea-view.jpg", 1000, None, 80),
    ("WhatsApp Image 2026-02-03 at 20.46.13 (3).jpeg", "three-bottles-terrace.jpg", 1000, None, 80),
    ("Leave_bottels02.jpeg", "bottles-bougainvillea.jpg", 1000, None, 80),
    # Crate / delivery.
    ("Kist01.jpeg", "crate-delivery-terrace.jpg", 1000, None, 80),
    ("WhatsApp Image 2026-02-03 at 20.43.22 (2).jpeg", "crate-top-view.jpg", 1000, None, 80),
]

# Open Graph image: 1200x630 crop of the six-flavour coast scene (no Original).
OG = ("ChatGPT Image Jun 30, 2026, 04_21_06 PM.png", "1190x625+0+278")

# Flavour labels: full wrap-around labels; the front panel is the centre
# column. Crops (WxH+X+Y) tuned per label by eye; output is 520px wide.
LABELS = [
    ("kombucha-02-ginger.png", "ginger.png", "472x787+438+0"),
    ("kombucha-03-wildorange.png", "wild-orange.png", "472x784+438+0"),
    ("kombucha-04-lime.png", "lime.png", "472x786+438+0"),
    ("kombuch-05-greenmandarine.png", "green-mandarine.png", "472x786+438+0"),
    ("kombucha-06-metabolicboost.png", "metabolic-boost.png", "472x784+438+0"),
    ("kombucha-07-lemontumeric.png", "lemon-turmeric.png", "472x785+438+0"),
]
LABEL_WIDTH = 520

LOGO = "logo_transparent_highres.png"
# Sun + island region of the trimmed logo (above the "REAL HEALTH" lettering),
# as a fraction of the trimmed height.
FAVICON_TOP_FRACTION = 0.70


# --- Helpers -------------------------------------------------------------------
def safe_output(path: Path) -> Path:
    """Return the resolved path if it lies inside assets/img/, else raise."""
    resolved = Path(path).resolve()
    if resolved != OUT and OUT not in resolved.parents:
        raise ValueError(f"refusing to write outside {OUT}: {resolved}")
    return resolved


def _convert(args: list, out: Path, fmt: str = "") -> Path:
    out = safe_output(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["convert", *[str(a) for a in args], f"{fmt}{out}"], check=True)
    return out


def _src(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path)
    return f"{path}[0]"


def _alpha_bbox(src: str) -> tuple[int, int, int, int]:
    """Bounding box (w, h, x, y) of clearly visible pixels (alpha > 10%)."""
    geo = subprocess.run(
        ["convert", src, "-alpha", "extract", "-threshold", "10%", "-format", "%@", "info:"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    wh, x, y = geo.split("+")
    w, h = wh.split("x")
    return int(w), int(h), int(x), int(y)


# --- Builders ------------------------------------------------------------------
def build_photo(src_name: str, target: str, width: int, crop: str | None, quality: int) -> Path:
    src = _src(PHOTOS_SRC / src_name)
    ops = ["-auto-orient"]
    if crop:
        ops += ["-crop", crop, "+repage"]
    ops += ["-resize", f"{width}x>", "-strip", "-sampling-factor", "4:2:0", "-interlace", "JPEG",
            "-colorspace", "sRGB"]
    out = OUT / "photos" / target
    q = quality
    while True:
        _convert([src, *ops, "-quality", q], out)
        if out.stat().st_size < MAX_PHOTO_BYTES or q <= 50:
            return out
        q -= 4


def build_og() -> Path:
    src_name, crop = OG
    return _convert(
        [_src(PHOTOS_SRC / src_name), "-auto-orient", "-crop", crop, "+repage",
         "-resize", "1200x630^", "-gravity", "center", "-extent", "1200x630",
         "-strip", "-interlace", "JPEG", "-quality", 82],
        OUT / "og.jpg",
    )


def build_label(src_name: str, target: str, crop: str) -> Path:
    return _convert(
        [_src(LOGOS_SRC / src_name), "-crop", crop, "+repage", "-resize", f"{LABEL_WIDTH}x",
         "-strip", "-dither", "FloydSteinberg", "-colors", 256, *PNG_DETERMINISTIC],
        OUT / "flavours" / target,
        fmt="PNG8:",  # 256-colour palette: ~100 KB instead of ~300 KB, no visible loss
    )


def _two_tone(alpha_src, dark_colour: str | None, bright_colour: str | None, dilate: str | None = None) -> list:
    """convert operators that recolour the current image (image 0) in two tones.

    Pixels darker than 45% grey (the green island and lettering) become
    dark_colour, the rest (the gold sun) bright_colour; None keeps a tone's
    original colours. Alpha is taken from image 0 (alpha_src "-") or from the
    file alpha_src, optionally dilated, and copied back so edges stay smooth.
    """
    keep = ["-clone", "0", "-alpha", "off"]
    bright = keep + (["-fill", bright_colour, "-colorize", "100"] if bright_colour else [])
    dark = keep + (["-fill", dark_colour, "-colorize", "100"] if dark_colour else [])
    mask = keep + ["-colorspace", "gray", "-threshold", "45%", "-negate", "-colorspace", "sRGB"]
    alpha = (["-clone", "0"] if alpha_src == "-" else [alpha_src]) + ["-alpha", "extract"]
    if dilate:
        alpha += ["-morphology", "Dilate", dilate]
    return ["(", *bright, ")", "(", *dark, ")", "(", *mask, ")", "(", *alpha, ")",
            "-delete", "0", "(", "-clone", "0-2", "-composite", ")", "-delete", "0-2", "+swap",
            "-alpha", "off", "-compose", "CopyOpacity", "-composite", "-compose", "over"]


def build_logos() -> list[Path]:
    src = _src(LOGOS_SRC / LOGO)
    w, h, x, y = _alpha_bbox(src)
    pad = 8
    crop = f"{w + 2 * pad}x{h + 2 * pad}+{x - pad}+{y - pad}"
    # The original-colour crop is only an intermediate (the site uses the light
    # logo on forest backgrounds); it is removed again so no unused file ships.
    dark = _convert([src, "-crop", crop, "+repage", "-strip", *PNG_DETERMINISTIC], OUT / "logo-dark.png")

    # Light version: dark-green island + lettering -> off-white; gold stays gold.
    light = _convert([dark, *_two_tone(dark, OFF_WHITE, None), "-strip", *PNG_DETERMINISTIC],
                     OUT / "logo-light.png")
    dark.unlink()

    # Favicon: sun + island only (logo above the lettering), centre part of the
    # sun so the island reads at 64px. Thin rays are recoloured solid gold and
    # thickened before downscaling, otherwise they fade to almost nothing.
    sun_h = int(h * FAVICON_TOP_FRACTION)
    fav = _convert(
        [src, "-crop", f"{w}x{sun_h}+{x}+{y}", "+repage", "-trim", "+repage",
         "-gravity", "south", "-crop", "62%x100%+0+0", "+repage", "-trim", "+repage",
         *_two_tone("-", GREEN, GOLD, dilate="Disk:4"),
         "-compose", "over", "-resize", "60x60", "-background", "none", "-gravity", "center",
         "-extent", "64x64", "-strip", *PNG_DETERMINISTIC],
        OUT / "favicon.png", fmt="PNG32:",
    )
    return [light, fav]


def build_qr() -> Path:
    out = safe_output(OUT / "review-qr.svg")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(QR_SRC, out)
    return out


def main(argv: list[str] | None = None) -> int:
    """Build everything, or only the photos whose target names are passed."""
    only = set(argv or [])
    if only:
        rows = [row for row in PHOTOS if row[1] in only]
        if len(rows) != len(only):
            raise SystemExit(f"unknown photo target(s): {sorted(only - {r[1] for r in rows})}")
        for p in (build_photo(*row) for row in rows):
            print(f"{p.relative_to(ROOT)}  {p.stat().st_size // 1024} KB")
        return 0
    produced = build_logos()
    produced.append(build_qr())
    produced += [build_label(*row) for row in LABELS]
    produced += [build_photo(*row) for row in PHOTOS]
    produced.append(build_og())
    for p in produced:
        print(f"{p.relative_to(ROOT)}  {p.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
