import re
from pathlib import Path
from urllib.parse import unquote

TEXT_EXT = {".html", ".css", ".js", ".xml", ".txt"}
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "//", "data:", "javascript:")

ATTR_RE = re.compile(r"""\b(?:href|src)\s*=\s*(["'])(.*?)\1""", re.I | re.S)
SRCSET_RE = re.compile(r"""\bsrcset\s*=\s*(["'])(.*?)\1""", re.I | re.S)
URL_RE = re.compile(r"""url\(\s*(["']?)(.*?)\1\s*\)""", re.I | re.S)


def _read(p):
    return p.read_text(encoding="utf-8")


def _text_files(out, exts=TEXT_EXT):
    return [p for p in sorted(out.rglob("*")) if p.is_file() and p.suffix in exts]


def _refs(path):
    """Return raw reference strings found in a file."""
    text = _read(path)
    refs = []
    if path.suffix == ".html":
        refs += [m.group(2) for m in ATTR_RE.finditer(text)]
        for m in SRCSET_RE.finditer(text):
            for part in m.group(2).split(","):
                part = part.strip()
                if part:
                    refs.append(part.split()[0])
    if path.suffix in (".html", ".css"):
        refs += [m.group(2) for m in URL_RE.finditer(text)]
    return refs


def _resolve(base_file, ref):
    ref = ref.strip()
    if not ref or ref.startswith("#") or ref.startswith(SKIP_PREFIXES):
        return None
    ref = ref.split("#", 1)[0].split("?", 1)[0]
    if not ref:
        return None
    target = (base_file.parent / unquote(ref)).resolve()
    if target.is_dir():
        target = target / "index.html"
    return target


def test_no_framer_references(built):
    bad = []
    for p in _text_files(built):
        t = _read(p).lower()
        for needle in ("framerusercontent", "framer.com", "framer.app", "framer"):
            if needle in t:
                bad.append((p.name, needle))
                break
    assert not bad, bad


def test_no_root_absolute_urls(built):
    pat = re.compile(r"""(?:href|src)\s*=\s*["']/(?!/)|url\(\s*["']?/(?!/)""", re.I)
    bad = [p for p in _text_files(built, {".html", ".css"}) if pat.search(_read(p))]
    assert not bad, bad


def test_internal_links_resolve(built):
    root = built.resolve()
    missing = []
    count = 0
    for p in _text_files(built, {".html", ".css"}):
        for ref in _refs(p):
            target = _resolve(p, ref)
            if target is None:
                continue
            count += 1
            if not target.exists() or root not in target.parents:
                missing.append((str(p.relative_to(built)), ref))
    assert count > 0
    assert not missing, missing


def test_no_unused_large_assets(built):
    img_dir = (built / "assets" / "img").resolve()
    used = set()
    for p in _text_files(built, {".html", ".css"}):
        for ref in _refs(p):
            t = _resolve(p, ref)
            if t is not None:
                used.add(t)
    unused = [
        str(f.relative_to(built))
        for f in sorted(img_dir.rglob("*"))
        if f.is_file() and f.resolve() not in used
    ]
    assert not unused, unused
