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
