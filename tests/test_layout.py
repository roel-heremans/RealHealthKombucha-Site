"""Site-wide layout: review banner, header (nav, Order, EN|PT), footer — EN and PT."""
import datetime
import re

import pytest

from content import CONTENT
from i18n import page_path

PAGES = {p["id"]: p for p in CONTENT["pages"]}
LINKS = CONTENT["links"]


def _file(built, page_id, lang):
    return built / page_path(PAGES[page_id], lang) / "index.html"


def _target(page_file, href):
    t = (page_file.parent / href).resolve()
    return t / "index.html" if t.is_dir() else t


def _section(html, tag, cls):
    m = re.search(rf'<{tag}[^>]*class="{cls}[^"]*"[^>]*>(.*?)</{tag}>', html, re.S)
    assert m, (tag, cls)
    return m.group(1)


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_review_banner_on_every_page(built, lang):
    text = CONTENT["review_banner"]["text"][lang]
    button = CONTENT["review_banner"]["button"][lang]
    for page_id in PAGES:
        f = _file(built, page_id, lang)
        html = f.read_text()
        banner = _section(html, "aside", "review-banner")
        assert text in banner, (page_id, lang)
        m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>\s*' + re.escape(button), banner)
        assert m, (page_id, lang)
        assert m.group(1) == LINKS["review"].replace("&", "&amp;") or m.group(1) == LINKS["review"]
        a_tag = m.group(0)
        assert 'target="_blank"' in a_tag and 'rel="noopener"' in a_tag
        # No QR code in the slim banner (it stays on the Order page).
        assert "review-qr" not in banner, (page_id, lang)
        # Banner comes before the header.
        assert html.index('class="review-banner') < html.index('class="site-header')


def test_review_banner_copy_matches_spec():
    rb = CONTENT["review_banner"]
    assert rb["text"]["en"] == ("Leave us a Google review and receive a free kombucha bottle "
                                "with your next order.")
    assert rb["text"]["pt"] == ("Deixe-nos uma avaliação no Google e receba uma garrafa de "
                                "kombucha grátis na sua próxima encomenda.")
    assert rb["button"] == {"en": "Write a review", "pt": "Escrever avaliação"}


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_nav_links_resolve_per_language(built, lang):
    root = built.resolve()
    for page_id in PAGES:
        f = _file(built, page_id, lang)
        nav = _section(f.read_text(), "nav", "site-nav")
        links = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', nav)
        by_label = {label.strip(): href for href, label in links}
        for nid in CONTENT["nav_ids"]:
            label = PAGES[nid]["nav"][lang]
            assert label in by_label, (page_id, lang, label)
            expected = root / page_path(PAGES[nid], lang) / "index.html"
            assert _target(f, by_label[label]) == expected, (page_id, lang, nid)


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_order_button_targets_order_page_same_language(built, lang):
    root = built.resolve()
    label = CONTENT["order_button"][lang]
    for page_id in PAGES:
        f = _file(built, page_id, lang)
        header = _section(f.read_text(), "header", "site-header")
        m = re.search(r'<a[^>]*class="[^"]*header-order[^"]*"[^>]*href="([^"]+)"[^>]*>\s*'
                      + re.escape(label), header)
        assert m, (page_id, lang)
        assert _target(f, m.group(1)) == root / page_path(PAGES["order"], lang) / "index.html"


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_lang_switch_marks_current_language(built, lang):
    other = "pt" if lang == "en" else "en"
    for page_id in PAGES:
        f = _file(built, page_id, lang)
        header = _section(f.read_text(), "header", "site-header")
        cur = re.search(r'<span[^>]*class="lang-current"[^>]*aria-current="true"[^>]*>([A-Z]{2})<', header)
        assert cur and cur.group(1) == lang.upper(), (page_id, lang)
        sw = re.search(r'<a[^>]*class="lang-switch"[^>]*href="([^"]+)"[^>]*>([A-Z]{2})<', header)
        assert sw and sw.group(2) == other.upper(), (page_id, lang)
        expected = built.resolve() / page_path(PAGES[page_id], other) / "index.html"
        assert _target(f, sw.group(1)) == expected


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_header_uses_light_logo_and_mobile_toggle(built, lang):
    for page_id in PAGES:
        f = _file(built, page_id, lang)
        header = _section(f.read_text(), "header", "site-header")
        logo = re.search(r'<img[^>]*src="([^"]*logo-light\.png)"', header)
        assert logo and _target(f, logo.group(1)).is_file()
        assert "logo.png" not in header
        assert re.search(r'<button[^>]*class="menu-toggle"[^>]*aria-expanded="false"'
                         r'[^>]*aria-controls="site-nav"', header)
    assert not (built / "assets" / "img" / "logo.png").exists()


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_footer_contents(built, lang):
    year = datetime.date.today().year
    for page_id in PAGES:
        f = _file(built, page_id, lang)
        footer = _section(f.read_text(), "footer", "site-footer")
        assert f'href="{LINKS["instagram"]}"' in footer
        assert f'href="{LINKS["whatsapp_chat"]}"' in footer
        assert f'href="mailto:{LINKS["email"]}"' in footer
        assert f"© {year} Real Health Kombucha" in footer
        assert CONTENT["footer_tagline"][lang] in footer
        assert CONTENT["address"] in footer
        assert 'class="lang-switch"' in footer
