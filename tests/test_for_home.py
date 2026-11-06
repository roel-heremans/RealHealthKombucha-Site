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
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {p["id"]: p for p in CONTENT["pages"]}
NBSP = " "
WHATSAPP = "https://wa.me/351913000048"
SIGNUP = "https://roel-heremans.github.io/kombucha-orders-app/?signup"
AJUDA_MAP = "https://www.google.com/maps/search/?api=1&query=32.6383957%2C-16.943107"
LEROY_MAP = "https://www.google.com/maps/search/?api=1&query=32.6463146%2C-16.9391991"
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
    assert "Leroy Merlin, São Martinho" in text
    assert "17:00–17:30" in text and "11:00–13:00" in text and "20:00" in text
    assert H.escape(LEROY_MAP) in html
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
def test_small_bottle_on_for_home(built, lang):
    text = _text(_section(_file(built, "for-home", lang).read_text(), "home-options"))
    assert "270 ml" in text and fmt("€4.50", lang) in text and fmt("€1", lang) in text


@LANGS
def test_home_prices_on_order_and_home_card(built, lang):
    """Order and the home-page card show home prices: 1 L €9.00 + €2, 270 ml €4.50 + €1."""
    for page_id, cls in (("order", "order-prices"), ("home", "home-paths")):
        sec = _section(_file(built, page_id, lang).read_text(), cls)
        if page_id == "home":   # only the "For home" card, not the restaurant card
            sec = re.findall(r"<article.*?</article>", sec, re.S)[1]
        text = _text(sec)
        for figure in ("€9.00", "€2", "€4.50", "€1"):
            assert fmt(figure, lang) in text, (page_id, figure)
        assert fmt("€3.50", lang) not in text, page_id


@LANGS
def test_restaurant_prices_section(built, lang):
    text = _text(_section(_file(built, "restaurants", lang).read_text(), "rest-prices"))
    for figure in ("€8.00", "€2", "€3.50", "€1"):
        assert fmt(figure, lang) in text, figure
    assert fmt("€9.00", lang) not in text and fmt("€4.50", lang) not in text


@LANGS
def test_flavours_price_table(built, lang):
    """Rows 1 L and 270 ml; columns at home, home subscription, restaurants & cafés."""
    table = re.search(r'<table class="price-table">(.*?)</table>',
                      _file(built, "flavours", lang).read_text(), re.S).group(1)
    rows = [[_text(c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
            for r in re.findall(r"<tr>(.*?)</tr>", table.split("<tbody>")[1], re.S)]
    none = "– not offered" if lang == "en" else "– não disponível"
    assert rows == [[fmt("€9.00", lang), fmt("€8.00", lang), fmt("€8.00", lang)],
                    [fmt("€4.50", lang), none, fmt("€3.50", lang)]]
    heads = _text(table.split("<tbody>")[0])
    for h in ({"en": ("At home", "Home subscription", "Restaurants & cafés"),
               "pt": ("Em casa", "Assinatura", "Restaurantes e cafés")}[lang]):
        assert h in heads, h
    text = _text(table)
    assert fmt("€2", lang) in text and fmt("€1", lang) in text


@LANGS
def test_hero_lead_any_amount_and_subscription(built, lang):
    """Lead: any number without subscription; subscription from 4/week at €8 (restaurant price),
    one bottle free every new month above 4 a week."""
    html = _file(built, "for-home", lang).read_text()
    lead = _text(re.search(r'<p class="lead">(.*?)</p>', html, re.S).group(1))
    words = {"en": ("without a subscription", "from 4 bottles a week", "restaurants pay",
                    "more than 4", "one bottle free every new month"),
             "pt": ("sem assinatura", "a partir de 4 garrafas por semana", "restaurantes pagam",
                    "mais de 4", "uma garrafa grátis em cada novo mês")}[lang]
    for w in words:
        assert w in lead.lower(), w
    assert fmt("€8", lang) in lead and "{sub}" not in lead


# Bottles a week -> (first, regular, last) month, typed out by hand:
# first = n × €10 + 3n × €8, regular = 4n × €8, last = regular − n × €2,
# and above 4 a week one bottle (€8) is free every month.
MONTHS = {4: (136, 128, 120), 5: (162, 152, 142), 6: (196, 184, 172),
          7: (230, 216, 202), 8: (264, 248, 232), 9: (298, 280, 262)}


@LANGS
def test_week_picker_dropdown(built, lang):
    """A <select> 4-9 (4 selected); only the 4-bottle card set is shown before any choice."""
    sec = _section(_file(built, "for-home", lang).read_text(), "home-month")
    sel = re.search(r'<select[^>]*id="per-week"[^>]*>(.*?)</select>', sec, re.S)
    assert sel and re.search(r'<label[^>]*for="per-week"', sec)
    opts = re.findall(r'<option value="(\d+)"( selected)?>\s*(\d+)', sel.group(1))
    assert [o[0] for o in opts] == [str(n) for n in MONTHS] == [o[2] for o in opts]
    assert [bool(o[1]) for o in opts] == [True] + [False] * 5
    assert "type=\"radio\"" not in sec
    variants = re.findall(r'<div class="month-variant mv-(\d+)( is-active)?"', sec)
    assert [v for v, a in variants if a] == ["4"] and len(variants) == 6


def test_picker_script_and_css():
    js = (ROOT / "assets/js/site.js").read_text()
    assert "per-week" in js and "is-active" in js
    css = (ROOT / "assets/css/styles.css").read_text()
    assert re.search(r"\.month-variant\s*\{\s*display:\s*none", css)
    assert re.search(r"\.month-variant\.is-active\s*\{\s*display:\s*block", css)


def test_css_js_links_are_versioned(built):
    """Browsers must refetch styles.css / site.js after a deploy (cache-busting query)."""
    html = _file(built, "for-home", "en").read_text()
    assert re.search(r'assets/css/styles\.css\?v=[0-9a-f]{8,}"', html)
    assert re.search(r'assets/js/site\.js\?v=[0-9a-f]{8,}"', html)


@LANGS
@pytest.mark.parametrize("n", list(MONTHS))
def test_month_variant_totals(built, lang, n):
    sec = _section(_file(built, "for-home", lang).read_text(), "home-month")
    m = re.search(rf'<div class="month-variant mv-{n}(?: is-active)?"[^>]*>(.*?)<!-- /mv -->', sec, re.S)
    assert m, n
    nums = [_text(x).strip() for x in re.findall(r'<span class="month__num">(.*?)</span>', m.group(1))]
    assert nums == [fmt(f"€{x}", lang) for x in MONTHS[n]]
    text = _text(m.group(1))
    assert f"{n * 4} " in text
    free = "free" if lang == "en" else "grátis"
    assert (free in text) == (n > 4)
