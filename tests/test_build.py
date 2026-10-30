import re

SLUGS = ["about", "gut-health-101", "reseller", "contact", "shop"]


def all_pages(root):
    return [root / "index.html"] + [root / s / "index.html" for s in SLUGS]


def test_six_pages_written(built):
    for p in all_pages(built):
        assert p.exists(), p
    assert not (built / "blog").exists()


def test_preview_noindex(built):
    for p in all_pages(built):
        assert '<meta name="robots" content="noindex">' in p.read_text()
    assert (built / "robots.txt").read_text() == "User-agent: *\nDisallow: /\n"


def test_preview_off_indexable(built_preview_off):
    for p in all_pages(built_preview_off):
        assert "noindex" not in p.read_text()
    assert "Sitemap:" in (built_preview_off / "robots.txt").read_text()


def test_sitemap_lists_six_pages(built):
    locs = re.findall(r"<loc>(.*?)</loc>", (built / "sitemap.xml").read_text())
    assert len(locs) == 6
    assert not any("blog" in l for l in locs)


def test_titles(built):
    html = (built / "reseller" / "index.html").read_text()
    assert "<title>Reseller Program - Real Health Kombucha Madeira</title>" in html
