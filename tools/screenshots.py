#!/usr/bin/env python3
"""Screenshot every page of a deployed site at 1440 and 390 width and build
review/index.html (old | new side by side).

Usage: python tools/screenshots.py <base_url>

Method: headless Chrome `--screenshot` for images (same tall windows as the
originals: 1440x9000, 390x12000). For the horizontal-scroll check, the page is
fetched, a tiny script is injected that writes scrollWidth/innerWidth into a
<body> attribute, written to a temp file next to nothing else (base href set to
the live URL so assets load), embedded in a 390px-wide srcdoc iframe (Chrome headless
windows cannot be narrower than 500px) and read via `--dump-dom`.
"""
import re, subprocess, sys, tempfile, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [("home", ""), ("about", "about/"), ("gut-health-101", "gut-health-101/"),
         ("reseller", "reseller/"), ("contact", "contact/"), ("shop", "shop/")]
SIZES = {"desktop": (1440, 9000), "phone": (390, 12000)}
CHROME = "google-chrome"
INJECT = ("<script>window.addEventListener('load',function(){setTimeout(function(){"
          "document.body.setAttribute('data-sw',document.documentElement.scrollWidth"
          "+','+innerWidth)},500)})</script>")


def chrome(*args):
    return subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                           "--hide-scrollbars", *args], capture_output=True, text=True, timeout=120)


def main(base):
    base = base.rstrip("/") + "/"
    out = ROOT / "review" / "new"
    out.mkdir(parents=True, exist_ok=True)
    for slug, path in PAGES:
        for name, (w, h) in SIZES.items():
            chrome(f"--window-size={w},{h}", "--virtual-time-budget=5000",
                   f"--screenshot={out / f'{slug}-{name}.png'}", base + path)
    print("Horizontal-scroll check at 390px:")
    bad = False
    for slug, path in PAGES:
        import html as H
        page = urllib.request.urlopen(base + path).read().decode()
        page = page.replace("<head>", f'<head><base href="{base + path}">', 1)
        host = ('<body><iframe id=f style="width:390px;height:900px;border:0" srcdoc="' + H.escape(page, quote=True) + '"></iframe>'
                '<script>document.getElementById("f").onload=function(){setTimeout(function(){var d=document.getElementById("f").contentDocument.documentElement;'
                'document.body.setAttribute("data-sw",d.scrollWidth+",390")},800)}</script></body>')
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
            f.write(host)
        r = chrome("--window-size=500,900", "--virtual-time-budget=8000", "--dump-dom", "file://" + f.name)
        m = re.search(r'data-sw="(\d+),(\d+)"', r.stdout)
        if not m:
            print(f"  {slug}: could not measure"); bad = True
        elif int(m[1]) > int(m[2]):
            print(f"  {slug}: OVERFLOW scrollWidth={m[1]} > innerWidth={m[2]}"); bad = True
        else:
            print(f"  {slug}: ok ({m[1]}<={m[2]})")
    rows = "".join(
        f"<h2>{s} / {n}</h2><div class=r><figure><figcaption>old</figcaption><img src='../original/screenshots/{s}-{n}.png'></figure>"
        f"<figure><figcaption>new</figcaption><img src='new/{s}-{n}.png'></figure></div>"
        for s, _ in PAGES for n in SIZES)
    (ROOT / "review" / "index.html").write_text(
        "<!doctype html><meta charset=utf-8><title>Old vs new</title><style>body{font:14px sans-serif}"
        ".r{display:flex;gap:12px;align-items:flex-start}figure{margin:0;flex:1;min-width:0}"
        "img{width:100%;border:1px solid #ccc}</style><h1>Old vs new</h1>" + rows)
    print("Wrote", ROOT / "review" / "index.html")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
