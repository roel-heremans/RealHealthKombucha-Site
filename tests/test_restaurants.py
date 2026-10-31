"""For restaurants page (spec section 2), EN and PT.

The figures below are typed out from the spec tables (slides 10-12) on purpose, independent of
src/content.py and i18n.eur, so a figure retyped wrongly in content fails here in both languages.
"""
import copy
import html as H
import re

import pytest

from build import build
from content import CONTENT
from i18n import page_path

PAGES = {p["id"]: p for p in CONTENT["pages"]}
NBSP = " "
PARTNERS = ["Sun Spot", "Palm Spot", "Koa Spot", "Vegan World", "Casa Velha do Palheiro",
            "Casa Velha Tea House", "Balancal", "Buddha & Sakura"]
SIGNUP = "https://roel-heremans.github.io/kombucha-orders-app/?signup"
WHATSAPP = "https://wa.me/351913000048"   # direct chat; the group invite is Contact-only
WHATSAPP_GROUP = "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R"

# Spec section 2.3 (slide 10), EN formatting, in order.
GLASS_ROWS = [
    ["200 ml", "5", "€1.60", "€4.00", "€2.40", "60%", "€12.00"],
    ["200 ml", "5", "€1.60", "€5.70", "€4.10", "72%", "€20.50"],
    ["250 ml", "4", "€2.00", "€4.00", "€2.00", "50%", "€8.00"],
    ["250 ml", "4", "€2.00", "€5.70", "€3.70", "65%", "€14.80"],
]
# Spec section 2.4 (slide 11): menu price, profit, margin.
BOTTLE_ROWS = [
    ["€4.00", "€0.50", "13%"],
    ["€5.00", "€1.50", "30%"],
    ["€5.70", "€2.20", "39%"],
]
# Spec section 2.6 (slide 9): the five app points (EN / PT titles).
APP_POINTS = {
    "en": ["One-tap reorder", "We're notified instantly", "English or Portuguese",
           "Order history", "Recibos verdes"],
    "pt": ["Repetir com um toque", "Somos avisados de imediato", "Português ou inglês",
           "Histórico de encomendas", "Recibos verdes"],
}


def fmt(s, lang):
    """EN figure -> the same figure in `lang`: PT "€1.60" -> "1,60 €" (NBSP), "€148" -> "148 €"."""
    if lang == "en" or not s.startswith("€"):
        return s
    return s[1:].replace(".", ",") + NBSP + "€"


def _page(built, lang):
    f = built / page_path(PAGES["restaurants"], lang) / "index.html"
    return f, f.read_text()


def _section(html, cls):
    m = re.search(rf'<section[^>]*class="[^"]*\b{cls}\b[^"]*"[^>]*>(.*?)</section>', html, re.S)
    assert m, cls
    return m.group(1)


def _text(fragment):
    """Visible text, tags stripped, entities decoded; collapses ordinary whitespace only (keeps NBSP)."""
    text = H.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"[ \t\r\n]+", " ", text).strip()


def _table_rows(fragment, table_cls):
    m = re.search(rf'<table[^>]*class="[^"]*\b{table_cls}\b[^"]*"[^>]*>(.*?)</table>', fragment, re.S)
    assert m, table_cls
    body = re.search(r"<tbody>(.*?)</tbody>", m.group(1), re.S).group(1)
    return [[_text(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
            for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body, re.S)]


LANGS = pytest.mark.parametrize("lang", ["en", "pt"])


@LANGS
def test_glass_table_exact(built, lang):
    _, html = _page(built, lang)
    rows = _table_rows(_section(html, "rest-glass"), "profit-table--glass")
    assert rows == [[fmt(c, lang) for c in r] for r in GLASS_ROWS]


@LANGS
def test_glass_note_and_highlights(built, lang):
    _, html = _page(built, lang)
    text = _text(_section(html, "rest-glass"))
    assert fmt("€8.00", lang) in text           # "You pay €8.00 per 1 L bottle"
    assert "72%" in text and fmt("€5.70", lang) in text
    assert ("2.5×" if lang == "en" else "2,5×") in text
    assert ("VAT not included" if lang == "en" else "IVA não incluído") in text


@LANGS
def test_bottle_table_exact(built, lang):
    _, html = _page(built, lang)
    sec = _section(html, "rest-bottles")
    rows = _table_rows(sec, "profit-table--bottles")
    assert rows == [[fmt(c, lang) for c in r] for r in BOTTLE_ROWS]
    text = _text(sec)
    assert fmt("€3.50", lang) in text and fmt("€1", lang) in text   # €3.50 + €1 deposit
    assert f"{fmt('€5.00', lang)}–{fmt('€5.70', lang)}" in text      # price it at €5.00–€5.70
    heading = _text(re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S).group(1))
    assert fmt("€5.00", lang) in heading, heading                     # two decimals, like the rest


@LANGS
def test_month_example_exact(built, lang):
    _, html = _page(built, lang)
    text = _text(_section(html, "rest-month"))
    for figure in ("€148", "€365", "€217"):
        assert fmt(figure, lang) in text, figure
    assert f"8 × {fmt('€8.00', lang)} + 24 × {fmt('€3.50', lang)}" in text
    # Deposit note: 24 × €1 = €24 comes back, not counted as a cost.
    assert f"24 × {fmt('€1', lang)}" in text and fmt("€24", lang) in text
    assert ("not included as a cost" if lang == "en" else "não é contabilizado como custo") in text


@LANGS
def test_hero_ctas(built, lang):
    _, html = _page(built, lang)
    hero = _section(html, "rest-hero")
    assert re.search(r"<h1", hero)
    primary = re.search(r'<a class="btn btn--gold"[^>]*href="([^"]+)"', hero)
    assert primary and H.unescape(primary.group(1)) == SIGNUP
    assert f'href="{WHATSAPP}"' in hero
    assert WHATSAPP_GROUP not in hero
    head = _text(re.search(r"<h1[^>]*>(.*?)</h1>", hero, re.S).group(1))
    assert head == ("Kombucha that pays off on your menu" if lang == "en"
                    else "Kombucha que compensa no seu menu")


@LANGS
def test_closing_cta_signup_whatsapp_email(built, lang):
    _, html = _page(built, lang)
    cta = _section(html, "rest-cta")
    assert f'href="{H.escape(SIGNUP)}"' in cta or f'href="{SIGNUP}"' in cta
    assert f'href="{WHATSAPP}"' in cta
    assert WHATSAPP_GROUP not in cta
    assert 'href="mailto:realhealthkombucha@gmail.com' in cta


@LANGS
def test_partners_and_quotes(built, lang):
    _, html = _page(built, lang)
    text = _text(_section(html, "rest-partners"))
    for name in PARTNERS:
        assert name in text
    quotes = re.findall(r'<blockquote class="quote"', _section(html, "rest-partners"))
    assert 2 <= len(quotes) <= 3
    if lang == "pt":
        assert "(original em inglês)" in text


@LANGS
def test_why_guests_love_it(built, lang):
    _, html = _page(built, lang)
    text = _text(_section(html, "rest-why"))
    assert "< 0.5% vol" in text or "< 0,5% vol" in text
    note = ("Based on published research on kombucha and fermented foods. Not a medical claim."
            if lang == "en" else
            "Com base em investigação publicada sobre kombucha e alimentos fermentados. "
            "Não é uma alegação médica.")
    assert note in text


@LANGS
def test_app_section_points_and_steps(built, lang):
    _, html = _page(built, lang)
    sec = _section(html, "rest-app")
    text = _text(sec)
    for point in APP_POINTS[lang]:
        assert point in text, point
    assert len(re.findall(r'class="step"', sec)) == 3
    assert SIGNUP in H.unescape(sec)


def test_app_screens_render_when_present(tmp_path):
    content = copy.deepcopy(CONTENT)
    content["restaurants"]["app_screens"] = [
        {"image": {"en": "assets/img/photos/crate-top-view.jpg", "pt": "assets/img/photos/crate-top-view.jpg"},
         "caption": {"en": "New order, pre-filled", "pt": "Nova encomenda, pré-preenchida"}},
    ]
    build(tmp_path / "o", content)
    for lang, caption in (("en", "New order, pre-filled"), ("pt", "Nova encomenda, pré-preenchida")):
        html = (tmp_path / "o" / page_path(PAGES["restaurants"], lang) / "index.html").read_text()
        sec = _section(html, "rest-app")
        assert sec.count('class="phone-frame"') == 1
        assert caption in _text(sec)


@LANGS
def test_app_screens_shown(built, lang):
    """Real orders-app screens (Task 8): one phone frame per screen, the image for the page
    language (the app itself in EN or PT), caption in the page language, files exist and are small."""
    f, html = _page(built, lang)
    sec = _section(html, "rest-app")
    screens = CONTENT["restaurants"]["app_screens"]
    assert len(screens) >= 3
    frames = re.findall(r'<figure class="phone-frame">(.*?)</figure>', sec, re.S)
    assert len(frames) == len(screens)
    other = "pt" if lang == "en" else "en"
    for s, fr in zip(screens, frames):
        img = s["image"][lang]
        assert img.startswith("assets/img/app/") and img.endswith(".png")
        assert img != s["image"][other]
        src = H.unescape(re.search(r'<img [^>]*src="([^"]+)"', fr).group(1))
        assert src.endswith(img), src
        target = (f.parent / src).resolve()
        assert target.is_file(), src
        assert target.stat().st_size < 250_000, src
        assert s["caption"][lang] in _text(fr)
        assert H.unescape(re.search(r'alt="([^"]*)"', fr).group(1)) == s["caption"][lang]


@LANGS
def test_delivery_section(built, lang):
    _, html = _page(built, lang)
    text = _text(_section(html, "rest-delivery")).lower()
    assert ("deposit" if lang == "en" else "depósito") in text
    assert "qr" in text


@LANGS
def test_tables_stack_on_phone(built, lang):
    """Every glass-table cell carries its column label so the rows can stack as cards on phones."""
    _, html = _page(built, lang)
    sec = _section(html, "rest-glass")
    tbody = re.search(r"<tbody>(.*?)</tbody>", sec, re.S).group(1)
    cells = re.findall(r"<td([^>]*)>", tbody)
    assert len(cells) == 28 and all('data-label="' in c for c in cells)


@LANGS
def test_images_resolve_with_alt(built, lang):
    f, html = _page(built, lang)
    imgs = re.findall(r"<img ([^>]+)>", html.split('<main id="main"', 1)[1].split("</main>", 1)[0])
    assert len(imgs) >= 3
    for attrs in imgs:
        src = re.search(r'src="([^"]+)"', attrs).group(1)
        alt = re.search(r'alt="([^"]*)"', attrs).group(1)
        assert alt.strip(), src
        assert (f.parent / H.unescape(src)).resolve().is_file(), src


def test_pt_page_has_no_juice_and_no_english_headings(built):
    _, en = _page(built, "en")
    _, pt = _page(built, "pt")
    for html in (en, pt):
        low = _text(html).lower()
        assert "juice" not in low and "sumo" not in low and "real fruit" not in low
    for h in re.findall(r"<h2[^>]*>(.*?)</h2>", en, re.S):
        assert _text(h) not in _text(pt), h


def test_highlight_figures_tied_to_glass_table():
    """The hardcoded "72%" / "2.5×" highlights (home + restaurants) match the table they describe."""
    import math

    r = CONTENT["restaurants"]
    row = r["glass_rows"][r["glass_highlight"]]
    assert row["ml"] == 200 and row["menu"] == CONTENT["prices"]["glass_menu_price"]
    margin = f"{row['margin']}%"
    assert row["margin"] == round(row["profit"] / row["menu"] * 100)  # 4.10 / 5.70 = 71.9% -> 72%
    assert r["glass"]["highlights"][0]["num"] == margin
    assert r["hero"]["facts"][1]["num"] == margin
    home = CONTENT["home"]["paths"]["highlights"]
    assert home[0]["num"] == {"en": margin, "pt": margin}
    # Deck: "2.5× your money back" = profit per bottle / bottle price, rounded down to one decimal.
    multiple = math.floor(row["per_bottle"] / CONTENT["prices"]["bottle_1l"] * 10) / 10
    assert multiple == 2.5 == r["money_back_multiple"]
    assert home[1]["num"] == {"en": f"{multiple}×", "pt": f"{multiple}×".replace(".", ",")}
    assert row["per_bottle"] == CONTENT["prices"]["max_profit_per_bottle"]


@LANGS
def test_hero_facts_say_up_to(built, lang):
    """The best-case figures (200 ml glasses at €5.70) are never shown as unconditional."""
    _, html = _page(built, lang)
    facts = re.findall(r"<li>(.*?)</li>", _section(html, "rest-hero").split('class="rest-facts"')[1], re.S)
    facts = [_text(f) for f in facts]
    up = "up to" if lang == "en" else "até"
    assert facts[0] == f"{up} {fmt('€20.50', lang)} " + (
        "profit per 1 L bottle" if lang == "en" else "de lucro por garrafa de 1 L"), facts[0]
    assert facts[1] == f"{up} 72% " + ("margin by the glass" if lang == "en" else "de margem a copo"), facts[1]
    assert not facts[2].startswith(up)       # partner count is a plain fact
    # The money-back multiple is tied to the 200 ml glass price it assumes.
    text = _text(_section(html, "rest-glass"))
    assert (f"at {fmt('€5.70', lang)} per 200 ml glass" if lang == "en"
            else f"a {fmt('€5.70', lang)} por copo de 200 ml") in text
