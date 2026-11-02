import re
from pathlib import Path
from urllib.parse import unquote

import pytest

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
        # Absolute og:image URLs (site_url + path) also count as a use.
        if p.suffix == ".html":
            for m in re.finditer(r'content="https://www\.realhealthkombucha\.com/(assets/[^"]+)"', _read(p)):
                used.add((built / m.group(1)).resolve())
    unused = [
        str(f.relative_to(built))
        for f in sorted(img_dir.rglob("*"))
        if f.is_file() and f.resolve() not in used
    ]
    assert not unused, unused


def test_head_has_favicon_description_and_og(built):
    from content import CONTENT
    from i18n import LANGS, page_path
    for page in CONTENT["pages"]:
        for lang in LANGS:
            f = built / page_path(page, lang) / "index.html"
            text = _read(f)
            m = re.search(r'<link rel="icon"[^>]*href="([^"]+)"', text)
            assert m, f
            assert m.group(1).endswith("favicon.png")
            assert _resolve(f, m.group(1)).is_file(), (f, m.group(1))
            d = re.search(r'<meta name="description" content="([^"]+)"', text)
            assert d and d.group(1).strip(), f
            want = page.get("description", CONTENT["meta_description"])[lang]
            assert d.group(1) == want.replace("&", "&amp;"), (f, lang)
            assert re.search(r'<meta property="og:title" content="[^"]+"', text), f
            assert re.search(r'<meta property="og:description" content="[^"]+"', text), f
            o = re.search(r'<meta property="og:image" content="([^"]+)"', text)
            assert o and o.group(1).startswith("https://"), f
            assert o.group(1).endswith("og.jpg"), f
            rel = o.group(1).split("realhealthkombucha.com/", 1)[1]
            assert (built / rel).is_file(), (f, rel)


def test_integrity_scan_covers_all_pages_and_redirects(built):
    """The scans above walk every built page: 16 pages (EN + PT) and the redirect pages."""
    from content import CONTENT
    from i18n import LANGS, page_path
    scanned = {p.resolve() for p in _text_files(built, {".html"})}
    want = {(built / page_path(p, l) / "index.html").resolve() for p in CONTENT["pages"] for l in LANGS}
    want |= {(built / old / "index.html").resolve() for old in CONTENT["redirects"]}
    assert len(want) == 16 + 4
    assert want <= scanned, want - scanned


def test_whatsapp_group_only_on_contact(built):
    """Order / talk-to-us buttons open a direct chat (wa.me); the group invite is
    linked only from the Contact pages, labelled as news & new batches."""
    group = "chat.whatsapp.com"
    pages_with_group = []
    for page in sorted(built.rglob("index.html")):
        html = _read(page)
        for tag in re.findall(r'<a\b[^>]*class="btn[^"]*"[^>]*>', html):
            assert group not in tag, (page, tag)
        if group in html:
            pages_with_group.append(page.relative_to(built).as_posix())
    assert sorted(pages_with_group) == ["contact/index.html", "pt/contacto/index.html"], pages_with_group
    assert any("wa.me/351913000048" in _read(p) for p in built.rglob("order/index.html"))
