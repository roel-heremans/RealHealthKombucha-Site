"""Flavours (spec section 3) and Order (spec section 6) pages, EN and PT.

The English flavour texts and the figures are typed out from the spec on purpose, independent of
src/content.py and i18n.eur, so a text or figure retyped wrongly in content fails here.
"""
import html as H
import re
import urllib.parse

import pytest

from content import CONTENT
from i18n import page_path
from orders import order_mailto

PAGES = {p["id"]: p for p in CONTENT["pages"]}
NBSP = " "
SIGNUP = "https://roel-heremans.github.io/kombucha-orders-app/?signup"
WHATSAPP = "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R"
REVIEW = "https://search.google.com/local/writereview?placeid=ChIJtYnk8XlZYAwRhT9_o66JcHE"
LANGS = pytest.mark.parametrize("lang", ["en", "pt"])

# Spec section 3 table: id, name, taste, benefit, flavoured with (EN), in display order.
FLAVOURS = [
    ("ginger", "Ginger", "Warming with a zesty bite",
     "Warming ginger, traditionally used for digestive comfort", "ginger"),
    ("wild-orange", "Wild Orange", "Sunny, juicy and smooth",
     "Bright, sweet orange — uplifting and cheerful", "wild orange"),
    ("lime", "Lime", "Crisp and thirst-quenching",
     "Crisp and invigorating — the most refreshing of the six", "lime"),
    ("green-mandarine", "Green Mandarine", "Fresh, aromatic island citrus",
     "Fresh, soft citrus — calming, a lovely evening drink", "green mandarine"),
    ("metabolic-boost", "Metabolic Boost", "Spicy-fresh and zesty",
     "An energising, spicy-fresh blend", "grapefruit, lemon, peppermint, ginger, cinnamon"),
    ("lemon-turmeric", "Lemon & Turmeric", "Golden, tangy and earthy",
     "Golden and earthy, with lemon's zing and turmeric's warmth", "lemon, turmeric"),
]
FLAVOURED_WITH = {"en": "Flavoured with:", "pt": "Aromatizado com:"}
HEALTH_NOTE = {
    "en": "Based on published research on kombucha and fermented foods. Not a medical claim.",
    "pt": "Com base em investigação publicada sobre kombucha e alimentos fermentados. "
          "Não é uma alegação médica.",
}
SUBJECT = {"en": "Kombucha order", "pt": "Encomenda de kombucha"}


def fmt(s, lang):
    """EN figure -> the same figure in `lang`: PT "€3.50" -> "3,50 €" (NBSP), "€1" -> "1 €"."""
    if lang == "en":
        return s
    return s[1:].replace(".", ",") + NBSP + "€"


def _page(built, page_id, lang):
    return (built / page_path(PAGES[page_id], lang) / "index.html").read_text()


def _section(html, cls):
    m = re.search(rf'<section[^>]*class="[^"]*\b{cls}\b[^"]*"[^>]*>(.*?)</section>', html, re.S)
    assert m, cls
    return m.group(1)


def _main(html):
    return re.search(r"<main[^>]*>(.*?)</main>", html, re.S).group(1)


def _text(fragment):
    """Visible text, tags stripped, entities decoded; collapses ordinary whitespace only (keeps NBSP)."""
    text = H.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"[ \t\r\n]+", " ", text).strip()


def _cards(html):
    """[(id, inner html)] of the flavour cards, in page order."""
    return re.findall(r'<article[^>]*class="[^"]*\bflavour-card\b[^"]*"[^>]*id="([^"]+)"[^>]*>(.*?)</article>',
                      html, re.S)


def _field(card, cls):
    m = re.search(rf'<(\w+)[^>]*class="[^"]*\b{cls}\b[^"]*"[^>]*>(.*?)</\1>', card, re.S)
    assert m, cls
    return _text(m.group(2))


# ── Flavours ──

@LANGS
def test_six_flavour_cards_in_order(built, lang):
    cards = _cards(_page(built, "flavours", lang))
    assert [c[0] for c in cards] == [f[0] for f in FLAVOURS]
    for (fid, card), (_, name, *_rest) in zip(cards, FLAVOURS):
        assert _field(card, "flavour-card__name") == name


def test_flavour_texts_en_exact(built):
    cards = dict(_cards(_page(built, "flavours", "en")))
    for fid, _, taste, benefit, flavoured in FLAVOURS:
        card = cards[fid]
        assert _field(card, "flavour-card__taste") == taste
        assert _field(card, "flavour-card__benefit") == benefit
        assert _field(card, "flavour-card__with") == f"Flavoured with: {flavoured}"


def test_flavour_texts_pt_translated(built):
    cards = dict(_cards(_page(built, "flavours", "pt")))
    for fid, _, taste, benefit, flavoured in FLAVOURS:
        card = cards[fid]
        pt_taste = _field(card, "flavour-card__taste")
        pt_benefit = _field(card, "flavour-card__benefit")
        pt_with = _field(card, "flavour-card__with")
        assert pt_taste and pt_taste != taste
        assert pt_benefit and pt_benefit != benefit
        assert pt_with.startswith("Aromatizado com: ") and len(pt_with) > len("Aromatizado com: ")
    assert _field(cards["metabolic-boost"], "flavour-card__with") != "Aromatizado com: " + FLAVOURS[4][4]


@LANGS
def test_flavour_card_image_and_base_ingredients(built, lang):
    html = _page(built, "flavours", lang)
    page_dir = built / page_path(PAGES["flavours"], lang)
    base = "Base ingredients" if lang == "en" else "Ingredientes base"
    for fid, card in _cards(html):
        img = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]+)"', card)
        assert img and (page_dir / img.group(1)).resolve().is_file(), fid
        assert f"flavours/{fid}.png" in img.group(1)
        text = _text(card)
        assert base in text and "Camellia sinensis" in text and "SCOBY" in text
        assert FLAVOURED_WITH[lang] in text


@LANGS
def test_no_juice_on_flavours_and_order(built, lang):
    for page_id in ("flavours", "order"):
        text = _text(_main(_page(built, page_id, lang))).lower()
        assert not re.search(r"\bjuice\b|\bsumo\b|real fruit", text), page_id


@LANGS
def test_flavours_badges_sizes_and_footnote(built, lang):
    html = _page(built, "flavours", lang)
    text = _text(_main(html))
    assert ("< 0.5% vol" if lang == "en" else "< 0,5% vol") in text
    assert ("Vegan" if lang == "en" else "Vegana") in text
    sizes = _text(_section(html, "flavours-sizes"))
    assert fmt("€8.00", lang) in sizes and fmt("€3.50", lang) in sizes and fmt("€1", lang) in sizes
    assert "1 L" in sizes and "270 ml" in sizes
    assert HEALTH_NOTE[lang] in text


@LANGS
def test_most_loved_marked(built, lang):
    cards = dict(_cards(_page(built, "flavours", lang)))
    loved = {fid for fid, card in cards.items() if "flavour-card__loved" in card}
    assert loved == {"ginger", "wild-orange", "metabolic-boost"}


def test_flavour_content_has_both_langs():
    for f in CONTENT["flavours"]:
        for key in ("taste", "benefit", "flavoured_with", "alt"):
            assert f[key]["en"].strip() and f[key]["pt"].strip(), (f["id"], key)


# ── Order ──

@LANGS
def test_order_mailto_round_trips(lang):
    link = order_mailto(lang)
    assert link.startswith("mailto:realhealthkombucha@gmail.com?")
    query = urllib.parse.parse_qs(urllib.parse.urlsplit(link).query)
    assert query["subject"] == [SUBJECT[lang]]
    body = query["body"][0].lower()
    words = {"en": ("flavour", "size", "delivery address"),
             "pt": ("sabor", "tamanho", "morada de entrega")}[lang]
    for w in words:
        assert w in body, w
    assert " " not in link and "\n" not in link


@LANGS
def test_order_prices(built, lang):
    text = _text(_section(_page(built, "order", lang), "order-prices"))
    assert fmt("€8.00", lang) in text and fmt("€3.50", lang) in text and fmt("€1", lang) in text
    assert "1 L" in text and "270 ml" in text


@LANGS
def test_order_how_to(built, lang):
    sec = _section(_page(built, "order", lang), "order-how")
    hrefs = [H.unescape(h) for h in re.findall(r'href="([^"]+)"', sec)]
    assert SIGNUP in hrefs
    assert WHATSAPP in hrefs
    assert order_mailto(lang) in hrefs
    mail = next(h for h in hrefs if h.startswith("mailto:"))
    subject = urllib.parse.parse_qs(urllib.parse.urlsplit(mail).query)["subject"][0]
    assert subject == SUBJECT[lang]
    assert "&body=" not in sec      # the & in the mailto is escaped in the attribute


@LANGS
def test_order_delivery_and_empties(built, lang):
    text = _text(_section(_page(built, "order", lang), "order-delivery")).lower()
    if lang == "en":
        assert "empties" in text and "deposit" in text and "deliver" in text
    else:
        assert "vazias" in text and "depósito" in text and "entreg" in text


@LANGS
def test_order_review_reminder(built, lang):
    sec = _section(_page(built, "order", lang), "order-review")
    assert CONTENT["review_banner"]["text"][lang] in _text(sec)
    assert f'href="{H.escape(REVIEW)}"' in sec or f'href="{REVIEW}"' in sec


@LANGS
def test_images_resolve_with_alt(built, lang):
    for page_id in ("order", "flavours"):
        main = _main(_page(built, page_id, lang))
        page_dir = built / page_path(PAGES[page_id], lang)
        for tag in re.findall(r"<img[^>]*>", main):
            src = re.search(r'src="([^"]+)"', tag).group(1)
            assert (page_dir / src).resolve().is_file(), src
            assert re.search(r'alt="[^"]+"', tag), tag


def test_pt_pages_have_no_english_headings(built):
    en_heads = set()
    for page_id in ("flavours", "order"):
        en_heads |= set(_text(h) for h in re.findall(r"<h[12][^>]*>(.*?)</h[12]>",
                                                     _main(_page(built, page_id, "en")), re.S))
    names = {f[1] for f in FLAVOURS}
    for page_id in ("flavours", "order"):
        for h in re.findall(r"<h[12][^>]*>(.*?)</h[12]>", _main(_page(built, page_id, "pt")), re.S):
            h = _text(h)
            assert h in names or h not in en_heads, h


@LANGS
def test_order_mailto_uses_built_content(tmp_path, lang):
    import copy

    from build import build

    content = copy.deepcopy(CONTENT)
    content["links"]["email"] = "orders@example.test"
    out = tmp_path / "out"
    build(out, content)
    html = (out / page_path(PAGES["order"], lang) / "index.html").read_text()
    hrefs = [H.unescape(h) for h in re.findall(r'href="(mailto:[^"]+)"', html)]
    assert order_mailto(lang, content) in hrefs
    assert any(h.startswith("mailto:orders@example.test?subject=") for h in hrefs)
