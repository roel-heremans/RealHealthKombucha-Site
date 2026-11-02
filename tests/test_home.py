"""Home page (spec section 1), EN and PT."""
import html as H
import re

import pytest

from content import CONTENT
from i18n import eur, num, page_path

PAGES = {p["id"]: p for p in CONTENT["pages"]}
HOME = CONTENT["home"]
FLAVOUR_ORDER = ["ginger", "wild-orange", "lime", "green-mandarine", "metabolic-boost",
                 "lemon-turmeric"]
PARTNERS = ["Sun Spot", "Palm Spot", "Koa Spot", "Vegan World", "Casa Velha do Palheiro",
            "Casa Velha Tea House", "Vista Balancal", "Buddha & Sakura"]


def _home(built, lang):
    f = built / page_path(PAGES["home"], lang) / "index.html"
    return f, f.read_text()


def _section(html, cls):
    m = re.search(rf'<section[^>]*class="[^"]*\b{cls}\b[^"]*"[^>]*>(.*?)</section>', html, re.S)
    assert m, cls
    return m.group(1)


def _target(page_file, href):
    t = (page_file.parent / H.unescape(href).split("#", 1)[0]).resolve()
    return t / "index.html" if t.is_dir() else t


def _page_file(built, page_id, lang):
    return (built / page_path(PAGES[page_id], lang) / "index.html").resolve()


def _text(fragment):
    """Visible text with tags stripped and entities decoded, whitespace collapsed."""
    # Collapse ordinary whitespace only, so non-breaking spaces (U+00A0) survive.
    text = H.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"[ \t\r\n]+", " ", text).strip()


# ── eur filter (Controller Ruling C) ──

def test_eur_format_per_language():
    assert eur(20.5, "en") == "€20.50"
    assert eur(8, "en") == "€8.00"
    assert eur(3.5, "en") == "€3.50"
    # PT: decimal comma and a non-breaking space (U+00A0) before €, so it never wraps.
    assert eur(20.5, "pt") == "20,50\u00a0€"
    assert eur(8, "pt") == "8,00\u00a0€"
    assert eur(148, "en", 0) == "€148"
    assert eur(148, "pt", 0) == "148\u00a0€"
    assert eur(1, "pt", 0) == "1\u00a0€"


def test_num_format_per_language():
    assert num(5.0, "en", 1) == "5.0"
    assert num(5.0, "pt", 1) == "5,0"
    assert num(2.5, "pt", 1) == "2,5"
    assert num(37, "pt") == "37"


# ── content shape ──

def test_shared_content_lists():
    assert [f["id"] for f in CONTENT["flavours"]] == FLAVOUR_ORDER
    # Product names as printed on the labels, the same in both languages.
    assert [f["name"] for f in CONTENT["flavours"]] == [
        "Ginger", "Wild Orange", "Lime", "Green Mandarine", "Metabolic Boost", "Lemon & Turmeric"]
    assert CONTENT["partners"] == PARTNERS
    assert len(CONTENT["quotes"]) == 6
    for q in CONTENT["quotes"]:
        assert q["text"] and q["author"] and q["stars"] == 5
    assert CONTENT["quotes"][0]["text"] == (
        "Some of the best kombucha I've had anywhere … First had it at the beach cafe … "
        "and then had to buy my own bottles.")
    assert CONTENT["links"]["reviews_all"].startswith("https://www.google.com/maps/")


# ── page ──

@pytest.mark.parametrize("lang", ["en", "pt"])
def test_hero(built, lang):
    f, html = _home(built, lang)
    hero = _section(html, "home-hero")
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", hero, re.S)
    assert h1
    want = HOME["hero"]["heading"][lang] + " " + HOME["hero"]["heading_accent"][lang]
    assert _text(h1.group(1)) == want
    if lang == "en":
        assert want == "Handcrafted kombucha from Madeira"
    text = _text(hero).lower()
    assert "real fruit" not in text and "juice" not in text and "sumo" not in text
    buttons = re.findall(r'<a[^>]*class="btn[^"]*"[^>]*href="([^"]+)"', hero)
    assert len(buttons) == 2
    assert _target(f, buttons[0]) == _page_file(built, "restaurants", lang)
    assert _target(f, buttons[1]) == _page_file(built, "order", lang)
    img = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"', hero)
    assert img and _target(f, img.group(1)).is_file() and img.group(2).strip()


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_proof_strip(built, lang):
    _, html = _home(built, lang)
    proof = _text(_section(html, "home-proof"))
    assert CONTENT["review_stats"]["rating"] == 5.0
    assert ("5.0" if lang == "en" else "5,0") in proof
    assert str(CONTENT["review_stats"]["count"]) in proof and "37" in proof
    assert re.search(r"\b8\b", proof)


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_two_paths(built, lang):
    f, html = _home(built, lang)
    paths = _section(html, "home-paths")
    cards = re.findall(r'<article[^>]*class="[^"]*path-card[^"]*"[^>]*>(.*?)</article>', paths, re.S)
    assert len(cards) == 2
    rest, home = cards
    assert eur(20.5, lang) in _text(rest)
    assert eur(9, lang) in _text(home) and eur(4.5, lang) in _text(home)
    if lang == "en":
        assert "€20.50" in _text(rest) and "€9.00" in _text(home) and "€4.50" in _text(home)
        assert "€2 deposit" in _text(home)
    else:
        nb = "\u00a0"
        assert f"20,50{nb}€" in _text(rest) and f"9,00{nb}€" in _text(home) and f"4,50{nb}€" in _text(home)
        assert f"2{nb}€ de depósito" in _text(home)
    # Slide 10 highlights on the restaurant card.
    assert "72%" in _text(rest) and eur(5.7, lang) in _text(rest)
    assert ("2.5×" if lang == "en" else "2,5×") in _text(rest)
    assert ("up to" if lang == "en" else "até") in _text(rest)
    r_href = re.search(r'<a[^>]*href="([^"]+)"', rest).group(1)
    h_href = re.search(r'<a[^>]*href="([^"]+)"', home).group(1)
    assert _target(f, r_href) == _page_file(built, "restaurants", lang)
    assert _target(f, h_href) == _page_file(built, "for-home", lang)


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_flavour_row(built, lang):
    f, html = _home(built, lang)
    row = _section(html, "home-flavours")
    items = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>\s*<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', row)
    assert [re.search(r"flavours/([\w-]+)\.png", src).group(1) for _, src, _ in items] == FLAVOUR_ORDER
    for href, src, alt in items:
        assert _target(f, href) == _page_file(built, "flavours", lang)
        assert _target(f, src).is_file()
        assert alt.strip()
    for fl in CONTENT["flavours"]:
        assert H.escape(fl["name"], quote=False) in row


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_photo_band(built, lang):
    f, html = _home(built, lang)
    band = re.search(r'<div class="photo-band[^"]*">\s*<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"', html)
    assert band and _target(f, band.group(1)).is_file() and band.group(2).strip()


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_partners(built, lang):
    _, html = _home(built, lang)
    text = _text(_section(html, "partners"))
    for name in PARTNERS:
        assert name in text, name


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_quotes(built, lang):
    _, html = _home(built, lang)
    sec = _section(html, "home-quotes")
    quotes = re.findall(r'<blockquote[^>]*class="[^"]*quote\b', sec)
    assert len(quotes) >= 3
    text = _text(sec)
    shown = [q for q in CONTENT["quotes"] if q["text"] in text]
    assert len(shown) >= 3
    for q in shown:
        assert q["author"] in text
    assert "★★★★★" in text
    assert CONTENT["links"]["reviews_all"].replace("&", "&amp;") in sec
    note = "(original em inglês)"
    if lang == "pt":
        assert text.count(note) >= len(shown)
    else:
        assert note not in text


@pytest.mark.parametrize("lang", ["en", "pt"])
def test_closing_cta(built, lang):
    f, html = _home(built, lang)
    cta = _section(html, "home-cta")
    if lang == "en":
        assert "Put Real Health Kombucha on your menu" in _text(cta)
    assert HOME["cta"]["heading"][lang] in _text(cta)
    hrefs = re.findall(r'<a[^>]*class="btn[^"]*"[^>]*href="([^"]+)"', cta)
    assert _target(f, hrefs[0]) == _page_file(built, "restaurants", lang)
    assert hrefs[1] == CONTENT["links"]["whatsapp_chat"] == "https://wa.me/351913000048"


def test_pt_home_has_no_english_section_copy(built):
    _, html = _home(built, "pt")
    for key in ("hero", "paths", "flavours", "quotes", "cta"):
        for v in HOME[key].values():
            if isinstance(v, dict) and "en" in v and v["en"] != v["pt"] and len(v["en"]) > 12:
                assert H.escape(v["en"], quote=False) not in html, v["en"]
