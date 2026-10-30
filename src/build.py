"""
Generate output/ (six static pages, robots.txt, sitemap.xml) from templates.
Edit src/content.py and run: python src/build.py (from project root)
"""
import datetime
import shutil
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from jinja2 import Environment, FileSystemLoader

from content import CONTENT

ROOT = SRC_DIR.parent
TEMPLATES_DIR = SRC_DIR / "templates"
OUT_DIR = ROOT / "output"


def build(out_dir: Path, content: dict) -> None:
    out_dir = Path(out_dir)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), autoescape=False)
    year = datetime.date.today().year

    for page in content["pages"]:
        slug = page["slug"]
        root = "./" if slug == "" else "../"
        html = env.get_template(page["template"]).render(
            content=content, page=page, root=root, year=year
        )
        target = out_dir / slug / "index.html" if slug else out_dir / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(f"  built {slug or 'home'}")

    base = content["site_url"]
    if content["preview"]:
        robots = "User-agent: *\nDisallow: /\n"
    else:
        robots = f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n"
    (out_dir / "robots.txt").write_text(robots, encoding="utf-8")

    locs = "".join(
        f"  <url><loc>{base}{p['slug'] + '/' if p['slug'] else ''}</loc></url>\n"
        for p in content["pages"]
    )
    (out_dir / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{locs}</urlset>\n",
        encoding="utf-8",
    )

    assets = ROOT / "assets"
    if assets.is_dir():
        shutil.copytree(assets, out_dir / "assets")
        print("  copied assets/")

    print(f"Done. Output is in {out_dir}")


def main():
    build(OUT_DIR, CONTENT)


if __name__ == "__main__":
    main()
