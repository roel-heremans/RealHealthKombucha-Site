"""Content pages: Home, About, Gut Health 101 (verbatim copy from the live site)."""
import html as htmllib
import re
from html.parser import HTMLParser

HOME_BENEFITS = ["Handmade", "Living Culture", "Energizing", "Bio & Vegan", "Healthy", "Spring Water"]
FLAVOURS = ["Metabolic Power", "Green Mandarine", "Wild Orange", "Lemon", "Ginger"]
GUT_BENEFITS = [
    "Detoxification",
    "Increased Energy",
    "Joint Health",
    "Antioxidants",
    "Probiotics",
    "Improved Digestion",
    "Immune Support",
]
TESTIMONIALS = ["“absolutely delicious!!”", "“Your Kombucha is amazing”", "“my favorite drink in the world”", "Dara", "Magda", "Sylvia"]


class TextAndLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text, self.links, self.imgs, self._skip = [], [], [], 0
        self._a = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "a":
            self._a = [a.get("href"), ""]
            self.links.append(self._a)
        if tag == "img":
            self.imgs.append(a.get("src"))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1
        if tag == "a":
            self._a = None

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)
            if self._a is not None:
                self._a[1] += data


def parse(path):
    p = TextAndLinks()
    p.feed(path.read_text(encoding="utf-8"))
    p.flat = re.sub(r"\s+", " ", htmllib.unescape(" ".join(p.text)))
    p.links = [(h, re.sub(r"\s+", " ", t).strip()) for h, t in p.links]
    return p


def main_of(path):
    """Only the <main> part of the page (excludes shared header/footer)."""
    html = path.read_text(encoding="utf-8")
    start, end = html.index("<main>"), html.index("</main>")
    p = TextAndLinks()
    p.feed(html[start:end])
    p.flat = re.sub(r"\s+", " ", htmllib.unescape(" ".join(p.text)))
    p.links = [(h, re.sub(r"\s+", " ", t).strip()) for h, t in p.links]
    return p


def assert_all(p, strings):
    missing = [s for s in strings if s not in p.flat]
    assert not missing, missing


def test_home_page(built):
    p = main_of(built / "index.html")
    assert_all(p, ["Delicious and Nutritious", "Benefits", "Explore our Flavours", "Taste the difference",
                   "Experience the Kombucha Magic", "What Our Customers Say", "frequently asked questions"])
    assert_all(p, HOME_BENEFITS + FLAVOURS + TESTIMONIALS)
    assert_all(p, ["Pure Source", "Natural Wellness", "Authentic", "Local Product"])
    assert_all(p, [
        "At Real Health Kombucha, we're revolutionizing Madeira's beverage market with pure, organic, and delicious Kombucha.",
        "What is Kombucha?",
        "Can Kombucha go bad? How do I know if it’s spoiled?",
        "Kombucha is a fermented tea beverage made by fermenting sweetened tea with a symbiotic culture of bacteria and yeast (SCOBY).",
    ])
    assert ("./shop/", "Shop Now") in p.links
    assert ("./about/", "Explore our Story") in p.links
    assert ("./about/", "Discover our Story") in p.links


def test_about_page(built):
    p = main_of(built / "about" / "index.html")
    assert_all(p, ["Real Health Kombucha", "Our Mission", "Our Story", "Our Values", "Made in Ponta do Sol",
                   "What Our Customers Say", "Real & Healthy", "non - Artificial", "Authentic"])
    assert_all(p, TESTIMONIALS)
    flat = p.flat
    for number, label in [("5", "Flavours"), ("2022", "Founded"), ("10", "Years experience"), ("100%", "Satisfied Customers")]:
        assert re.search(rf"\b{re.escape(number)} {label}\b", flat), (number, label)
    assert_all(p, ["Nina discovered kombucha in 2002 while living in New Mexico",
                   "Welcome to Real Health Kombucha, a small brewery dedicated to crafting premium kombucha on the beautiful island of Madeira."])
    assert ("../shop/", "Real Health Kombucha Shop") in p.links


def test_gut_health_page(built):
    p = main_of(built / "gut-health-101" / "index.html")
    assert_all(p, ["Gut Health 101", "Build a healthy gut with Kombucha every Day",
                   "Health Benefits of Real Health Kombucha", "WHY GUT HEALTH MATTERS", "What Our Customers Say"])
    assert_all(p, GUT_BENEFITS + TESTIMONIALS)
    assert_all(p, ["Cleanse Your Body Naturally", "Strengthen Your Immune System",
                   "Kombucha contains glucosamine, which supports joint health and can help reduce joint pain."])
    assert ("../shop/", "Shop Now") in p.links
    assert ("../about/", "Explore our Story") in p.links
    assert ("../about/", "Discover our Story") in p.links


def test_page_images_local(built):
    for path, root in [(built / "index.html", "./"),
                       (built / "about" / "index.html", "../"),
                       (built / "gut-health-101" / "index.html", "../")]:
        imgs = parse(path).imgs
        main_imgs = main_of(path).imgs
        assert main_imgs, f"no images in <main> of {path}"
        for src in imgs:
            assert src.startswith(root + "assets/"), (path, src)
            assert (path.parent / src).resolve().is_file(), (path, src)
