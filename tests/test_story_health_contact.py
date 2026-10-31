"""Our story (spec 4), Gut health (spec 5) and Contact (spec 7) pages, EN and PT.

Expected EN titles, links and the footnote are typed out from the spec/deck on purpose,
independent of src/content.py.
"""
import html as H
import re

import pytest

from content import CONTENT
from i18n import page_path

PAGES = {p["id"]: p for p in CONTENT["pages"]}
LANGS = pytest.mark.parametrize("lang", ["en", "pt"])

STEPS_EN = ["Pure water", "Green tea brew", "Fermentation", "Flavour & bottle"]
BENEFITS_EN = ["Live cultures", "Antioxidants", "Gut friendly", "Less sugar",
               "Alcohol-free choice", "Clean & vegan"]
HEALTH_NOTE = {
    "en": "Based on published research on kombucha and fermented foods. Not a medical claim.",
    "pt": "Com base em investigação publicada sobre kombucha e alimentos fermentados. "
          "Não é uma alegação médica.",
}
CONTACT_HREFS = [
    "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R",
    "https://www.instagram.com/realhealthkombucha/",
    "mailto:realhealthkombucha@gmail.com",
    "tel:+351913000048",
    "https://maps.google.com/?q=Caminho+do+Jang%C3%A3o+154,+9360-523+Ponta+do+Sol",
]


def _page(built, page_id, lang):
    return (built / page_path(PAGES[page_id], lang) / "index.html").read_text()


def _main(html):
    return re.search(r"<main[^>]*>(.*?)</main>", html, re.S).group(1)


def _text(fragment):
    text = H.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"\s+", " ", text).strip()


def _items(html, cls):
    """Inner html of every element with class `cls` (li/article/div), in page order."""
    return re.findall(rf'<(li|article|div)[^>]*class="[^"]*\b{cls}\b[^"]*"[^>]*>(.*?)</\1>', html, re.S)


def _titles(html, cls):
    out = []
    for _, inner in _items(html, cls):
        m = re.search(r"<h3[^>]*>(.*?)</h3>", inner, re.S)
        assert m, f"{cls} item without h3"
        out.append(_text(m.group(1)))
    return out


def _hrefs(fragment):
    return [H.unescape(h) for h in re.findall(r'href="([^"]*)"', fragment)]


# ── Our story ──

@LANGS
def test_story_four_steps(built, lang):
    main = _main(_page(built, "story", lang))
    titles = _titles(main, "story-step")
    assert len(titles) == 4
    if lang == "en":
        assert titles == STEPS_EN
    else:
        assert all(titles) and titles != STEPS_EN
        assert "Fermentação" in titles


@LANGS
def test_story_names_umh_pure_gold(built, lang):
    assert "UMH Pure Gold" in _text(_main(_page(built, "story", lang)))


@LANGS
def test_story_step4_natural_flavours_second_fermentation(built, lang):
    step4 = _text(_items(_main(_page(built, "story", lang)), "story-step")[3][1]).lower()
    if lang == "en":
        assert "natural flavours" in step4 and "second fermentation" in step4
        assert "naturally sparkling" in step4
    else:
        assert "aromas naturais" in step4 and "segunda fermentação" in step4


@LANGS
def test_story_people_and_place(built, lang):
    text = _text(_main(_page(built, "story", lang)))
    assert "Roel" in text and "Nina" in text and "Ponta do Sol" in text
    assert ("95%" in text) if lang == "en" else ("95 %" in text or "95%" in text)


@LANGS
def test_story_uses_portraits(built, lang):
    main = _main(_page(built, "story", lang))
    srcs = re.findall(r'<img[^>]*src="[^"]*photos/([^"]+)"', main)
    assert any(s.startswith(("roel-", "nina-")) for s in srcs)


# ── Gut health ──

@LANGS
def test_gut_health_six_benefits(built, lang):
    main = _main(_page(built, "gut-health", lang))
    titles = _titles(main, "benefit")
    assert len(titles) == 6
    if lang == "en":
        assert titles == BENEFITS_EN
    else:
        assert all(titles) and titles != BENEFITS_EN


@LANGS
def test_gut_health_footnote_and_figures(built, lang):
    text = _text(_main(_page(built, "gut-health", lang)))
    assert HEALTH_NOTE[lang] in text
    assert ("below 0.5% vol" if lang == "en" else "abaixo de 0,5% vol") in text
    assert ("live cultures" if lang == "en" else "culturas vivas") in text.lower()


@LANGS
def test_gut_health_cta_links(built, lang):
    """The CTA links resolve to the Flavours and Order pages in the same language."""
    base = (built / page_path(PAGES["gut-health"], lang)).resolve()
    targets = {(base / h).resolve() for h in _hrefs(_main(_page(built, "gut-health", lang)))
               if not h.startswith(("http", "mailto:", "tel:"))}
    for pid in ("flavours", "order"):
        assert (built / page_path(PAGES[pid], lang)).resolve() in targets, pid


# ── Contact ──

@LANGS
def test_contact_five_links(built, lang):
    hrefs = _hrefs(_main(_page(built, "contact", lang)))
    for href in CONTACT_HREFS:
        assert href in hrefs, href


@LANGS
def test_contact_shows_details(built, lang):
    text = _text(_main(_page(built, "contact", lang)))
    assert "+351 913 000 048" in text
    assert "realhealthkombucha@gmail.com" in text
    assert "Caminho do Jangão 154, 9360-523 Ponta do Sol" in text


@LANGS
def test_contact_has_no_form_or_hours(built, lang):
    html = _page(built, "contact", lang)
    assert "<form" not in html.lower()
    text = _text(_main(html)).lower()
    for word in (["opening hours", "mon", "tue"] if lang == "en" else ["horário", "segunda-feira"]):
        assert not re.search(rf"\b{word}\b", text), word


@LANGS
def test_contact_external_links_open_new_tab(built, lang):
    main = _main(_page(built, "contact", lang))
    for href in CONTACT_HREFS:
        if href.startswith("http"):
            tags = re.findall(rf'<a[^>]*href="{re.escape(H.escape(href))}"[^>]*>', main)
            assert tags and all('target="_blank"' in a and 'rel="noopener"' in a for a in tags), href


# ── All three ──

@LANGS
@pytest.mark.parametrize("page_id", ["story", "gut-health", "contact"])
def test_images_resolve_with_alt(built, lang, page_id):
    page = PAGES[page_id]
    html = _page(built, page_id, lang)
    imgs = re.findall(r"<img[^>]*>", _main(html))
    assert imgs
    base = built / page_path(page, lang)
    for img in imgs:
        src = re.search(r'src="([^"]+)"', img).group(1)
        assert (base / src).resolve().is_file(), src
        assert re.search(r'alt="[^"]+"', img), img


@pytest.mark.parametrize("page_id", ["story", "gut-health", "contact"])
def test_pt_page_differs_from_en(built, page_id):
    en = _text(_main(_page(built, page_id, "en")))
    pt = _text(_main(_page(built, page_id, "pt")))
    h1_en = re.search(r"<h1[^>]*>(.*?)</h1>", _page(built, page_id, "en"), re.S).group(1)
    h1_pt = re.search(r"<h1[^>]*>(.*?)</h1>", _page(built, page_id, "pt"), re.S).group(1)
    assert en != pt and h1_en != h1_pt


@LANGS
def test_no_page_mentions_juice(built, lang):
    for page in CONTENT["pages"]:
        html = _page(built, page["id"], lang).lower()
        assert not re.search(r"\bjuices?\b|\bsumos?\b", html), page["id"]
