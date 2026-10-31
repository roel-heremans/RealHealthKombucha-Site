"""Shop and Reseller: orders-app signup links and pre-filled order emails."""
import copy
import re
from urllib.parse import parse_qs, urlsplit

from build import build
from content import CONTENT
from orders import mailto_for
from test_pages import main_of

SIGNUP = "https://roel-heremans.github.io/kombucha-orders-app/?signup"
EMAIL = "realhealthkombucha@gmail.com"


def decode(href):
    parts = urlsplit(href)
    assert parts.scheme == "mailto"
    qs = parse_qs(parts.query, keep_blank_values=True)
    return parts.path, qs["subject"][0], qs["body"][0]


def bottle(n):
    return next(p for p in CONTENT["packages_bottle"] if p["bottles"] == n)


def sub(n):
    return next(p for p in CONTENT["packages_subscription"] if p["bottles_per_week"] == n)


def test_content_values():
    assert CONTENT["orders_app_signup_url"] == SIGNUP
    assert CONTENT["order_email"] == EMAIL
    assert [(p["bottles"], p["price"], p["deposit"]) for p in CONTENT["packages_bottle"]] == [
        (2, 20, 4), (4, 36, 8), (8, 65, 16)]
    assert [(p["name"], p["bottles_per_week"], p["price_per_month"]) for p in CONTENT["packages_subscription"]] == [
        ("Single", 2, 72), ("Couple", 4, 128), ("Family", 8, 240)]
    assert "account" in CONTENT["order_button_label"].lower()
    assert "account" in CONTENT["partner_button_label"].lower()
    assert CONTENT["order_email_label"] == "or order by email"


def test_bottle_totals():
    for n, total in [(2, "€24"), (4, "€44"), (8, "€81")]:
        _, subject, body = decode(mailto_for(bottle(n), "bottle", EMAIL))
        assert total in body, (n, body)
        assert subject.endswith(f"({n} bottles)")


def test_subscription_amounts():
    for n, amount in [(2, "72€"), (4, "128€"), (8, "240€")]:
        _, subject, body = decode(mailto_for(sub(n), "subscription", EMAIL))
        assert amount in body, (n, body)
        assert subject.endswith(f"({n} bottles/week)")


def test_mailto_roundtrip():
    to, subject, body = decode(mailto_for(bottle(2), "bottle", EMAIL))
    assert to == EMAIL
    assert subject == "Kombucha Order: buy per bottle (2 bottles)"
    assert body == "\r\n".join([
        "Dear Kombucha Team,", "",
        "I want to order the 2 Bottles - buy per bottle package.", "",
        "I want to order the following flavors:", "",
        "Please let me know when the next delivery to Funchal is happening.", "",
        "I will bring the €24 (incl. deposit) to the delivery.", "",
        "Best Regards,",
    ])
    to, subject, body = decode(mailto_for(sub(4), "subscription", EMAIL))
    assert to == EMAIL
    assert subject == "Kombucha Order: subscription (4 bottles/week)"
    assert body == "\r\n".join([
        "Dear Kombucha Team,", "",
        "I want to order the 4 Bottles per week - subscription package.", "",
        "I want to order the following flavors:", "",
        "My address for delivery is:", "",
        "I will pay 128€ for the month on the first delivery.", "",
        "Best Regards,",
    ])
    # Raw form: every reserved character percent-encoded, CRLF line breaks.
    raw = mailto_for(sub(4), "subscription", EMAIL)
    assert raw.startswith(f"mailto:{EMAIL}?subject=")
    assert "%2F" in raw and "%0D%0A" in raw and "%E2%82%AC" in raw
    assert " " not in raw


def test_mailto_href_is_html_escaped(built):
    html = (built / "shop" / "index.html").read_text(encoding="utf-8")
    hrefs = re.findall(r'href="(mailto:[^"]*)"', html)
    assert len(hrefs) == 6
    for h in hrefs:
        assert "&amp;body=" in h and "&body=" not in h


def shop_links(out):
    return main_of(out / "shop" / "index.html").links


def test_shop_cards(built):
    p = main_of(built / "shop" / "index.html")
    signup = [h for h, _ in p.links if h == SIGNUP]
    assert len(signup) == 6
    assert all(t == CONTENT["order_button_label"] for h, t in p.links if h == SIGNUP)
    mails = [(h, t) for h, t in p.links if h.startswith(f"mailto:{EMAIL}?subject=")]
    assert len(mails) == 6
    assert all(t == "or order by email" for _, t in mails)
    for text in ["20€ + 4€ deposit", "36€ + 8€ deposit", "65€ + 16€ deposit",
                 "72€ per month", "128€ per month", "240€ per month",
                 "2 Bottles", "4 Bottles", "8 Bottles", "Single", "Couple", "Family",
                 "2 Bottles a week", "4 Bottles a week", "8 Bottles a week"]:
        assert text in p.flat, text
    # Each card: signup button immediately followed by its email link.
    hrefs = [h for h, _ in p.links]
    for i, h in enumerate(hrefs):
        if h == SIGNUP:
            assert hrefs[i + 1].startswith("mailto:"), hrefs[i + 1]


def test_shop_page_copy(built):
    p = main_of(built / "shop" / "index.html")
    for text in ["REAL HEALTH SHOP", "Buy per Bottle", "Subscription", "Delivery to Funchal",
                 "Perfect for Tourists", "Choose your Flavours",
                 "Free Home Delivery (Calheta - PdS - Rib. Brava - Funchal - Canico)",
                 "Taste the difference", "What Our Customers Say", "Dara", "Magda", "Sylvia",
                 "Enjoy regular deliveries of your favorite kombucha and save with our subscription plans."]:
        assert text in p.flat, text
    assert ("#buyperbottle", "Buy per Bottle") in p.links
    assert ("#subscription", "Subscription") in p.links
    html = (built / "shop" / "index.html").read_text(encoding="utf-8")
    assert 'id="buyperbottle"' in html and 'id="subscription"' in html
    assert ("../about/", "Discover our Story") in p.links


def test_mailto_total_follows_price(tmp_path):
    content = copy.deepcopy(CONTENT)
    content["packages_bottle"][0]["price"] = 22
    _, _, body = decode(mailto_for(content["packages_bottle"][0], "bottle", EMAIL))
    assert "€26" in body
    build(tmp_path / "out", content)
    p = main_of(tmp_path / "out" / "shop" / "index.html")
    assert "22€ + 4€ deposit" in p.flat
    assert "20€ + 4€ deposit" not in p.flat
    first_mail = next(h for h, _ in p.links if h.startswith("mailto:"))
    assert "€26 (incl. deposit)" in decode(first_mail)[2]
    # Other cards unchanged.
    assert "36€ + 8€ deposit" in p.flat and "72€ per month" in p.flat


def test_reseller_buttons(built):
    p = main_of(built / "reseller" / "index.html")
    label = CONTENT["partner_button_label"]
    ctas = [(i, h) for i, (h, t) in enumerate(p.links) if t == label]
    assert len(ctas) == 2
    for i, h in ctas:
        assert h == SIGNUP
        nxt = p.links[i + 1][0]
        assert nxt.startswith(f"mailto:{EMAIL}?subject="), nxt
    assert not [h for h, t in p.links if t == "Contact"], "old Contact CTA left over"


def test_reseller_page_copy(built):
    p = main_of(built / "reseller" / "index.html")
    for text in ["Partner with Real Health Kombucha", "FOR RESTAURANTS & HOTELS", "Enhance Your menu",
                 "Health Benefits", "Promote", "Eco Friendly", "Tailored to Your Needs", "Fast Delivery",
                 "Become a Partner", "Contact Us", "Sample Package", "Tailored Solutions",
                 "Our Mission", "Our Values", "Real & Healthy", "Non - Artificial", "Authentic",
                 "Made in Ponta do Sol", "What Our Customers Say",
                 "We offer flexible packages to suit your establishment’s size and needs"]:
        assert text in p.flat, text
    for number, label in [("5", "Flavours"), ("2022", "Founded"), ("10", "Years experience"),
                          ("100%", "Satisfied Customers")]:
        assert re.search(rf"\b{re.escape(number)} {label}\b", p.flat), (number, label)


def test_shop_reseller_images_local(built):
    for slug in ("shop", "reseller"):
        path = built / slug / "index.html"
        imgs = main_of(path).imgs
        assert imgs
        for src in imgs:
            assert src.startswith("../assets/img/"), src
            assert (path.parent / src).resolve().is_file(), src
