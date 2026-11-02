"""For home page (private customers), EN and PT.

Prices and subscription totals are typed out here on purpose, independent of src/content.py:
single 1 L bottle €9 + €2 deposit; subscription €8 + €2 deposit, 4 bottles a week, 4 weeks a month.
First month 4 × €10 + 12 × €8 = €136, then 16 × €8 = €128, last month €128 − €8 deposit back = €120.
"""
import html as H
import re

import pytest

from content import CONTENT
from i18n import page_path

PAGES = {p["id"]: p for p in CONTENT["pages"]}
NBSP = " "
WHATSAPP = "https://wa.me/351913000048"
SIGNUP = "https://roel-heremans.github.io/kombucha-orders-app/?signup"
AJUDA_MAP = "https://www.google.com/maps/search/?api=1&query=32.6383957%2C-16.943107"
LANGS = pytest.mark.parametrize("lang", ["en", "pt"])


def fmt(s, lang):
    """EN figure -> `lang`: PT "€9.00" -> "9,00 €" (NBSP), "€136" -> "136 €"."""
    if lang == "en":
        return s
    return s[1:].replace(".", ",") + NBSP + "€"


def _file(built, page_id, lang):
    return built / page_path(PAGES[page_id], lang) / "index.html"


def _section(html, cls):
    m = re.search(rf'<section[^>]*class="[^"]*\b{cls}\b[^"]*"[^>]*>(.*?)</section>', html, re.S)
    assert m, cls
    return m.group(1)


def _text(html):
    return re.sub(r"[ \t\r\n]+", " ", H.unescape(re.sub(r"<[^>]+>", " ", html)))


def test_page_and_slugs():
    page = PAGES["for-home"]
    assert page["slug"] == {"en": "for-home", "pt": "para-casa"}
    assert page["nav"] == {"en": "For Home", "pt": "Para Casa"}
    ids = [p["id"] for p in CONTENT["pages"]]
    assert ids.index("for-home") == ids.index("restaurants") + 1
    nav = CONTENT["nav_ids"]
    assert nav.index("for-home") == nav.index("restaurants") + 1


@LANGS
def test_page_built(built, lang):
    assert _file(built, "for-home", lang).is_file()


@LANGS
def test_two_options(built, lang):
    text = _text(_section(_file(built, "for-home", lang).read_text(), "home-options"))
    assert fmt("€9.00", lang) in text and fmt("€8.00", lang) in text
    assert fmt("€2", lang) in text
    assert "1 L" in text
    assert ("4 bottles" if lang == "en" else "4 garrafas") in text


@LANGS
def test_subscription_month_totals(built, lang):
    text = _text(_section(_file(built, "for-home", lang).read_text(), "home-month"))
    for total in ("€136", "€128", "€120"):
        assert fmt(total, lang) in text, total
    assert f"4 × {fmt('€10.00', lang)} + 12 × {fmt('€8.00', lang)}" in text
    assert f"16 × {fmt('€8.00', lang)}" in text


@LANGS
def test_delivery_and_pickups(built, lang):
    html = _section(_file(built, "for-home", lang).read_text(), "home-delivery")
    text = _text(html)
    assert "Funchal" in text
    assert "São Martinho" in text
    assert "17:00–17:30" in text and "11:00–13:00" in text
    assert ("Wednesday" if lang == "en" else "Quarta") in text
    assert ("Sunday" if lang == "en" else "Domingo") in text
    assert ("Ajuda Public Garden" if lang == "en" else "Jardim Público da Ajuda") in text
    assert H.escape(AJUDA_MAP) in html


@LANGS
def test_buttons(built, lang):
    html = _file(built, "for-home", lang).read_text()
    assert f'href="{WHATSAPP}"' in html
    assert f'href="{SIGNUP}"' in html


@LANGS
def test_home_price_on_other_pages(built, lang):
    """Order, Flavours and the home-page card show the 1 L home price with its €2 deposit;
    the restaurant price (€8.00) stays on For Restaurants."""
    for page_id, cls in (("order", "order-prices"), ("flavours", "flavours-sizes"),
                         ("home", "home-paths")):
        text = _text(_section(_file(built, page_id, lang).read_text(), cls))
        assert fmt("€9.00", lang) in text, page_id
        assert fmt("€2", lang) in text, page_id
        assert fmt("€3.50", lang) in text, page_id
    rest = _text(_file(built, "restaurants", lang).read_text())
    assert fmt("€8.00", lang) in rest
