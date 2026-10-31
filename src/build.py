"""
Generate output/ (7 pages x EN/PT, redirects for old URLs, robots.txt, sitemap.xml).
Edit src/content.py and run: python src/build.py (from project root)
SITE_ENV=production builds the live site (indexable); anything else builds the noindex test site.
"""
import datetime
import os
import shutil
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from jinja2 import Environment, FileSystemLoader, pass_context

from content import CONTENT
from i18n import LANGS, eur, num, page_path, rel, t
from orders import order_mailto

ROOT = SRC_DIR.parent
TEMPLATES_DIR = SRC_DIR / "templates"
OUT_DIR = ROOT / "output"


def _write(out_dir: Path, path: str, html: str) -> None:
    target = out_dir / path / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def build(out_dir: Path, content: dict) -> None:
    out_dir = Path(out_dir)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    pages = {p["id"]: p for p in content["pages"]}
    base = content["site_url"]

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=False)

    @pass_context
    def t_filter(ctx, value):
        return t(value, ctx["lang"])

    @pass_context
    def url(ctx, page_id, lang=None):
        return rel(ctx["path"], page_path(pages[page_id], lang or ctx["lang"]))

    @pass_context
    def eur_filter(ctx, amount, decimals=2):
        return eur(amount, ctx["lang"], decimals)

    env.filters["t"] = t_filter
    env.filters["eur"] = eur_filter

    @pass_context
    def num_filter(ctx, value, decimals=None):
        return num(value, ctx["lang"], decimals)

    env.filters["num"] = num_filter
    def mailto(lang):
        return order_mailto(lang, content)

    env.globals.update(url=url, page_path=page_path, LANGS=LANGS, order_mailto=mailto)
    year = datetime.date.today().year

    for page in content["pages"]:
        template = env.get_template(page["template"])
        for lang in LANGS:
            path = page_path(page, lang)
            other = next(l for l in LANGS if l != lang)
            html = template.render(
                content=content, page=page, lang=lang, path=path,
                root=rel(path, ""), year=year,
                switch_url=rel(path, page_path(page, other)), other_lang=other,
            )
            _write(out_dir, path, html)
            print(f"  built {path or '/'}")

    redirect = env.get_template("redirect.html.j2")
    for old, page_id in content["redirects"].items():
        path = f"{old}/"
        target = page_path(pages[page_id], "en")
        html = redirect.render(
            content=content, lang="en", path=path, root=rel(path, ""),
            target_url=rel(path, target), canonical=base + target,
        )
        _write(out_dir, path, html)
        print(f"  redirect {path} -> {target or '/'}")

    if content["preview"]:
        robots = "User-agent: *\nDisallow: /\n"
    else:
        robots = f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n"
    (out_dir / "robots.txt").write_text(robots, encoding="utf-8")

    urls = ""
    for page in content["pages"]:
        alternates = "".join(
            f'    <xhtml:link rel="alternate" hreflang="{l}" href="{base}{page_path(page, l)}"/>\n'
            for l in LANGS
        )
        for lang in LANGS:
            urls += f"  <url>\n    <loc>{base}{page_path(page, lang)}</loc>\n{alternates}  </url>\n"
    (out_dir / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{urls}</urlset>\n",
        encoding="utf-8",
    )

    assets = ROOT / "assets"
    if assets.is_dir():
        shutil.copytree(assets, out_dir / "assets")
        print("  copied assets/")

    print(f"Done. Output is in {out_dir}")


def content_for_env(environ) -> dict:
    if environ.get("SITE_ENV") == "production":
        return {**CONTENT, "preview": False}
    return CONTENT


def main():
    build(OUT_DIR, content_for_env(os.environ))


if __name__ == "__main__":
    main()
