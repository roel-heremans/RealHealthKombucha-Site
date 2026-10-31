# RealHealthKombucha-Site

Static site for realhealthkombucha.com, generated with Jinja2 (no Framer).

## Setup
    python3 -m venv .venv && . .venv/bin/activate
    pip install -r requirements.txt

## Build
    ./build-output.sh    # writes output/

Edit copy and prices in `src/content.py`, templates in `src/templates/`.

## Test
    pytest -q

## Changing content
Ask for, or make, a change in `src/content.py` (copy, prices, links, contact details) or the templates in `src/templates/`. Then rebuild and run the tests.

## Preview locally
    ./build-output.sh && python -m http.server -d output 8000    # http://localhost:8000/

## Deploy (phase 1: GitHub Pages test site)
Pushing to `main` runs `.github/workflows/deploy.yml`: install, `pytest -q` (failing tests block the deploy), build, publish `output/` to
https://roel-heremans.github.io/RealHealthKombucha-Site/ . While `CONTENT["preview"]` is True every page is noindex, `robots.txt` disallows all, and the contact form does not send.

## Visual review
    python tools/screenshots.py https://roel-heremans.github.io/RealHealthKombucha-Site/
Writes `review/new/*.png` and `review/index.html` (old vs new side by side; `review/` is gitignored) and prints pages with horizontal scroll at 390px.

## Phase 2 (go live on realhealthkombucha.com)
1. Add a deploy step that uploads `output/` to STRATO over SFTP, with host/user/password stored as GitHub repository secrets (never in the repo).
2. Set `CONTENT["preview"] = False` in `src/content.py` (removes noindex, allows robots, enables the real contact form).
3. DNS in the STRATO panel: change the `www` CNAME (currently `sites.framer.app`) and the apex A record (currently `52.223.52.2`) to the new hosting. Do NOT change the MX record `smtpin.rzone.de`.
4. Keep Framer until the new site is confirmed live.
