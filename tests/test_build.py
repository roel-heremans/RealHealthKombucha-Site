import re
from pathlib import Path

from content import CONTENT

EN_PATHS = ["", "for-restaurants/", "flavours/", "our-story/", "gut-health/", "order/", "contact/"]
PT_PATHS = ["pt/", "pt/para-restaurantes/", "pt/sabores/", "pt/a-nossa-historia/",
            "pt/saude-intestinal/", "pt/encomendar/", "pt/contacto/"]


def all_pages(root):
    return [root / p / "index.html" for p in EN_PATHS + PT_PATHS]


def test_fourteen_pages_written(built):
    for p in all_pages(built):
        assert p.exists(), p
    assert not (built / "blog").exists()


def test_preview_noindex(built):
    for p in all_pages(built):
        assert '<meta name="robots" content="noindex">' in p.read_text()
    assert (built / "robots.txt").read_text() == "User-agent: *\nDisallow: /\n"


def test_preview_off_indexable(built_preview_off):
    for p in all_pages(built_preview_off):
        assert "noindex" not in p.read_text()
    assert "Sitemap:" in (built_preview_off / "robots.txt").read_text()


def test_sitemap_hreflang(built):
    xml = (built / "sitemap.xml").read_text()
    entries = re.findall(r"<url>(.*?)</url>", xml, re.S)
    assert len(re.findall(r"<loc>", xml)) == 14
    assert len(entries) == 14
    for e in entries:
        assert 'rel="alternate" hreflang="en"' in e, e
        assert 'rel="alternate" hreflang="pt"' in e, e
    assert not any("blog" in e for e in entries)


def test_html_lang(built):
    for p in EN_PATHS:
        assert '<html lang="en"' in (built / p / "index.html").read_text(), p
    for p in PT_PATHS:
        assert '<html lang="pt"' in (built / p / "index.html").read_text(), p


def _switch_target(page_file):
    html = page_file.read_text()
    m = re.search(r'<a[^>]*class="lang-switch"[^>]*href="([^"]+)"', html) or \
        re.search(r'<a[^>]*href="([^"]+)"[^>]*class="lang-switch"', html)
    assert m, page_file
    target = (page_file.parent / m.group(1)).resolve()
    return target / "index.html" if target.is_dir() else target


def test_lang_switch_targets_same_page(built):
    root = built.resolve()
    assert _switch_target(built / "for-restaurants/index.html") == root / "pt/para-restaurantes/index.html"
    assert _switch_target(built / "pt/para-restaurantes/index.html") == root / "for-restaurants/index.html"
    assert _switch_target(built / "index.html") == root / "pt/index.html"
    assert _switch_target(built / "pt/index.html") == root / "index.html"


def _walk(node, found):
    if isinstance(node, dict):
        keys = set(node)
        if keys == {"en", "pt"}:
            found.append(node)
        else:
            assert not ({"en", "pt"} & keys and len({"en", "pt"} & keys) == 1), node
        for k, v in node.items():
            if k != "slug":  # URL slugs are not visible text; home's slug is "" in both
                _walk(v, found)
    elif isinstance(node, (list, tuple)):
        for v in node:
            _walk(v, found)


def test_every_translatable_has_both_langs():
    found = []
    _walk(CONTENT, found)
    assert found
    for d in found:
        for lang in ("en", "pt"):
            assert isinstance(d[lang], str) and d[lang].strip(), d


def test_old_urls_redirect(built):
    root = built.resolve()
    pages = {p["id"]: p for p in CONTENT["pages"]}
    assert CONTENT["redirects"] == {"shop": "order", "reseller": "restaurants",
                                    "about": "story", "gut-health-101": "gut-health"}
    for old, target_id in CONTENT["redirects"].items():
        f = built / old / "index.html"
        html = f.read_text()
        m = re.search(r'http-equiv="refresh" content="0;\s*url=([^"]+)"', html)
        assert m, old
        target = (f.parent / m.group(1)).resolve()
        if target.is_dir():
            target = target / "index.html"
        slug = pages[target_id]["slug"]["en"]
        assert target == root / slug / "index.html", (old, target)
        assert 'rel="canonical"' in html
        assert f'href="{m.group(1)}"' in html.split("<body", 1)[1]
