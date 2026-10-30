# realhealthkombucha.com off Framer — Design

Date: 2026-10-30
Status: draft, awaiting approval

## Intent

Roel wants to stop editing realhealthkombucha.com in Framer. Changes should be
made by asking Claude in plain words ("new flavour", "summer prices"), after
which Claude edits, commits, pushes, and the change goes live automatically.
This copies the approach already used for sattva-reset.com
(`~/Documents/PersonalRepos/SattvaReset`): Jinja2 templates + one content file
+ a build script that writes a static site into `output/`.

Success: the site looks the same as today, Roel never opens Framer again, and a
requested change is live within minutes of a push.

## Goals

- Reproduce the current Framer site's look faithfully in a new repo,
  `RealHealthKombucha-Site`, as plain static HTML/CSS/JS.
- All editable text, prices, links and package data live in one content file
  so that routine changes never touch layout code.
- Every push to `main` builds and publishes automatically.
- Shop ordering sends people to the orders app, with email as a fallback.

## Non-goals

- No redesign. Visual fidelity to the current site is the bar.
- No online payments, cart, or stock tracking on the website.
- No CMS or blog.
- No multilingual site (current site is English only).

## Anti-goals (failure even if it "works")

- Anything that requires Roel to open an editor or a web builder for routine
  changes.
- Touching the live domain, DNS, email (MX) or Framer before Roel approves the
  test site.
- STRATO credentials or other secrets committed to the repo.
- The test site being indexed by Google.

## Phases

### Phase 1 — test site (this design)

- New GitHub repo `roel-heremans/RealHealthKombucha-Site`.
- GitHub Action on push to `main`: build, then publish `output/` to GitHub
  Pages (e.g. `roel-heremans.github.io/RealHealthKombucha-Site/`), same host
  as the orders app.
- Test site carries `<meta name="robots" content="noindex">` and a
  `robots.txt` disallowing all, controlled by a build flag so phase 2 can
  turn it off.
- realhealthkombucha.com stays on Framer, untouched.

### Phase 2 — go live (only after Roel approves phase 1; decided then)

- Pick the STRATO package (same as Sattva or separate — open question).
- Switch the Action's deploy target to STRATO via SFTP (credentials as GitHub
  secrets), add the contact-form mail script, remove the noindex flag.
- Change two DNS records in STRATO's panel: `www` (now CNAME
  `sites.framer.app`) and the apex A record (now `52.223.52.2`, Framer). DNS
  is already at STRATO (`rzone.de`); MX (`smtpin.rzone.de`) must not change.
- Keep Framer running until the new site is confirmed live, then cancel.

## Site content (from the live site, rendered 2026-10-30)

Pages to reproduce: Home (`/`), About, Gut Health 101, Reseller, Contact,
Shop. Shared header (announcement banner + nav: Home, About, Gut Health 101,
Reseller, Contact, Shop) and footer (tagline, nav, Instagram, Telegram
`t.me/RealHealthKombucha`, WhatsApp group
`chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R`).

- Banner: Home says "Exciting News! 📣 - Get a free 1 Liter Kombucha Bottle
  [here]"; other pages say "For Hotels & Restaurants - Become a Partner
  [here]". Keep both as they are; text and link target live in the content file.
  Today the Home banner's "here" is not a link (the other pages' banner links
  to `./reseller`). Claude's call: keep it unlinked, with an empty link field in
  the content file ready to fill.
- Visual tokens observed: fonts Inter / Inter Display (body), Playfair Display
  (headings), plus Lato, Figtree, Alegreya, DM Sans in places; colours
  `rgb(44,47,36)` dark olive, `rgb(238,141,8)` and `rgb(236,86,0)` oranges,
  `rgb(249,249,247)` and `rgb(219,223,208)` light neutrals. The builder
  should confirm these against the rendered pages and use Google Fonts.
- About 60 images, currently on `framerusercontent.com`. Download them into
  the repo (`assets/`) so nothing depends on Framer. Prefer full-resolution
  originals, then size/compress sensibly for the web.
- Framer animations (scroll reveals, hover effects) are reproduced only where
  simple CSS/JS does it; exact motion matching is not required.

## Shop and ordering

Each package card keeps its current look and prices:

- Buy per bottle: 2 bottles 20€ + 4€ deposit; 4 bottles 36€ + 8€; 8 bottles
  65€ + 16€.
- Subscription: Single 2/week 72€/month; Couple 4/week 128€/month; Family
  8/week 240€/month.

Packages are data in the content file (name, price, deposit, email subject and
body), so price changes are one-line edits.

- Primary button on each card → orders-app self-signup:
  `https://roel-heremans.github.io/kombucha-orders-app/?signup` (same link as
  the A6 invite card; signup is bilingual and supports private customers).
  The URL is a single content value.
- Secondary small link "or order by email" under each button → the same
  pre-filled `mailto:realhealthkombucha@gmail.com` as today (subject + body
  with package, flavours placeholder, total incl. deposit), generated from the
  package data so totals stay correct.
- Button wording should tell people what happens next (account creation),
  since a new signup is reviewed before ordering — exact wording is the
  builder's call, kept in the content file.
- Reseller page "Contact" buttons: primary → orders-app signup, with the email
  link alongside.

## Contact form

Fields Name, Email, Message (as today). Phase 1: the form renders identically
but submitting shows a "Preview — message not sent" notice (build flag). Phase
2: posts to a small PHP mail script on STRATO sending to
realhealthkombucha@gmail.com, with a basic honeypot against spam.

## Small fixes during the move (Claude's calls — Roel to confirm)

- Drop the Framer template blog (`/blog` and its five placeholder posts: sushi,
  air fryer, etc.) and its sitemap entries.
- Footer "© 2024" → current year, generated at build time.
- Tab title "Reseller Programm" → "Reseller Program".
- Generate `sitemap.xml` for the six pages.
- Left unchanged pending Roel: opening hours on Contact ("Mon-Fri: 11am -
  8pm, Sat, Sun: 9am - 10pm"), the "free 1 Liter bottle" banner, About stats
  ("5 Flavours", "10 Years experience").

## Repo shape (mirrors SattvaReset)

- `original/` — captured Framer pages (rendered DOM) and downloaded assets,
  kept as reference.
- `src/content.py` — all text, prices, links, packages, banner, flags.
- `src/templates/*.j2` — a base layout plus one template per page.
- `build-output.sh` → `output/`; `requirements.txt` (Jinja2); `.venv` local.
- `.github/workflows/deploy.yml` — build + publish to GitHub Pages.
- `README.md` — how to change content, build, preview locally, and how deploy
  works.
- Copy of this design into `docs/superpowers/specs/`.

Repo is public (needed for free GitHub Pages; content is public anyway) —
Claude's call.

## Verification before handing phase 1 to Roel

- Build runs clean locally and in the Action.
- Side-by-side screenshots (desktop and phone width) of every page, Framer vs
  new, shared with Roel for sign-off.
- All internal links, orders-app links, mailto links and social links work;
  no requests to `framerusercontent.com` or `framer` domains remain.

## Left to the builder

Template structure, CSS organisation, image sizing/format, how closely to
mimic each Framer animation, the exact wording of the order buttons and the
"preview" notice, and how the noindex/preview flags are wired.

## Open questions (phase 2, not blocking phase 1)

- Which STRATO package hosts the site (same as sattva-reset.com or its own)?
