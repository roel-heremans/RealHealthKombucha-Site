import re
from datetime import date
from html.parser import HTMLParser

SUBPAGES = ["about", "gut-health-101", "reseller", "contact", "shop"]
NAV_ORDER = [
    ("Home", ""),
    ("About", "about/"),
    ("Gut Health 101", "gut-health-101/"),
    ("Reseller", "reseller/"),
    ("Contact", "contact/"),
    ("Shop", "shop/"),
]
SOCIALS = [
    "https://www.instagram.com/realhealthkombucha/",
    "http://t.me/RealHealthKombucha",
    "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R",
]


def pages(root):
    """(path, root-prefix) for every page."""
    return [(root / "index.html", "./")] + [
        (root / s / "index.html", "../") for s in SUBPAGES
    ]


class RegionParser(HTMLParser):
    """Collects text and links inside the first element with a given class."""

    def __init__(self, tag, cls):
        super().__init__()
        self.tag, self.cls = tag, cls
        self.depth = 0
        self.links = []  # [href, text]
        self.text = []
        self.in_a = False
        self.found = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.depth == 0 and not self.found and tag == self.tag and self.cls in (a.get("class") or "").split():
            self.depth = 1
            self.found = True
            return
        if self.depth:
            if tag == self.tag:
                self.depth += 1
            if tag == "a":
                self.links.append([a.get("href"), ""])
                self.in_a = True

    def handle_endtag(self, tag):
        if not self.depth:
            return
        if tag == "a":
            self.in_a = False
        if tag == self.tag:
            self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.text.append(data)
            if self.in_a:
                self.links[-1][1] += data


def region(html, tag, cls):
    p = RegionParser(tag, cls)
    p.feed(html)
    assert p.found, f"<{tag} class={cls}> not found"
    return p


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def test_nav_on_every_page(built):
    for path, prefix in pages(built):
        html = path.read_text(encoding="utf-8")
        nav = region(html, "nav", "site-nav")
        got = [(norm(t), h) for h, t in nav.links]
        want = [(label, prefix + rel) for label, rel in NAV_ORDER]
        assert got == want, path


def test_banners(built):
    home = (built / "index.html").read_text(encoding="utf-8")
    b = region(home, "div", "banner")
    assert not any("here" in t for _, t in b.links), "home banner 'here' must not be a link"
    assert not any("Kombucha Bottle" in t for _, t in b.links)
    # Live site: long wording on desktop, short wording on phone (verbatim, incl. spacing).
    desktop = norm("".join(region(home, "span", "banner-desktop").text))
    phone = norm("".join(region(home, "span", "banner-phone").text))
    assert desktop + " here" == "Exciting News!📣 - Get a free 1 Liter Kombucha Bottle on your next order click here"
    assert phone + " here" == "Exciting News! 📣 - Get a free 1 Liter Kombucha Bottle here"

    for path, prefix in pages(built)[1:]:
        b = region(path.read_text(encoding="utf-8"), "div", "banner")
        assert "For Hotels & Restaurants - Become a Partner here" in norm("".join(b.text)), path
        assert any(h == prefix + "reseller/" and "here" in t for h, t in b.links), path


def test_footer(built):
    year = date.today().year
    for path, _ in pages(built):
        html = path.read_text(encoding="utf-8")
        f = region(html, "footer", "site-footer")
        hrefs = [h for h, _ in f.links]
        for url in SOCIALS:
            assert url in hrefs, (path, url)
        assert f"© {year} Real Health Kombucha. All rights reserved." in norm("".join(f.text)), path


def test_layout_assets_linked_relative(built):
    for path, prefix in pages(built):
        html = path.read_text(encoding="utf-8")
        assert f'href="{prefix}assets/css/styles.css"' in html
        assert f'src="{prefix}assets/js/site.js"' in html
        assert f'src="{prefix}assets/img/logo.png"' in html
    assert (built / "assets" / "css" / "styles.css").exists()
    assert (built / "assets" / "js" / "site.js").exists()


def test_menu_toggle_present(built):
    html = (built / "index.html").read_text(encoding="utf-8")
    assert re.search(r'<button[^>]*class="menu-toggle"[^>]*aria-controls="site-nav"', html)
    assert 'id="site-nav"' in html
