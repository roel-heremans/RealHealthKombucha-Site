# Real Health Kombucha website redesign — Design

Date: 2026-10-31
Status: draft, awaiting approval
Builds on: `2026-10-30-website-off-framer-design.md` (phase 1: static Jinja2 site, preview on GitHub Pages, STRATO go-live later). The build pipeline, preview flag, deploy workflow and phase-2 plan stay as they are; this document replaces the *look, structure and content*.

## Intent

Roel is unhappy with the old Framer design and copy, which phase 1 reproduced faithfully. The site should now look like sattva-reset.com (Roel & Nina's retreat site) and carry new content built from the restaurant pitch deck. Restaurants are the most important audience (they buy in volume); home customers matter too.

Success: a restaurant owner landing on the site understands within a minute why kombucha pays off on their menu and how easy ordering is, and can start the partnership; a home customer can see flavours, prices and how to order; everything exists in English and European Portuguese.

## Goals

- Sattva-style visual design (direction "A — Forest", chosen by Roel in mockups).
- New page structure and copy derived from the pitch deck, page by page.
- English + Portuguese with a language switch.
- New logo, flavour labels and photos from Roel's own assets; none of the old Framer images.
- Google-review banner with a direct link and QR code.
- Real screens of the orders app on the restaurant page.

## Non-goals

- No online payment or cart; ordering stays in the orders app (with email/WhatsApp as fallback).
- No blog/CMS.
- No change to hosting plan, deploy workflow or the phase-2 go-live steps.
- No changes to the orders app itself.

## Anti-goals

- **The flavouring supplier/brand must never appear** anywhere: page text, alt text, file names, code, commit messages, or the public GitHub repo. Flavours are described only as "Flavoured with: <ingredients>".
- No health claims beyond modest, honest wording (see Flavours and Gut health). No disease, weight-loss, detox or anti-inflammatory promises.
- No old Framer photos, logo or copy carried over unless listed here.
- Restaurant numbers must not be wrong: every price/margin figure comes from the pitch deck exactly.

## Inputs (source material)

- Pitch deck: `~/Documents/PersonalRepos/Kombucha/output/presentations/Real_Health_Kombucha_Restaurant_Pitch.pptx` (13 slides; text and figures quoted below are from it). Its embedded images may be reused where useful.
- Logo: `~/Documents/PersonalRepos/Kombucha/assets/design-logos/logo_transparent_highres.png` (dark-green Madeira island under a gold sun, "REAL HEALTH"). A light/white version for the dark header is derived from it.
- Flavour labels: same folder — `kombucha-02-ginger.png`, `kombucha-03-wildorange.png`, `kombucha-04-lime.png`, `kombuch-05-greenmandarine.png`, `kombucha-06-metabolicboost.png`, `kombucha-07-lemontumeric.png`. Each is a full wrap-around label; the front panel is the centre third. **Original is left out everywhere.**
- Photos: `~/Documents/PersonalRepos/Kombucha/assets/01_images/` (55 images).
- Review QR: `~/Documents/PersonalRepos/Kombucha/output/qr/review_qr.png` / `.svg`; review URL `https://search.google.com/local/writereview?placeid=ChIJtYnk8XlZYAwRhT9_o66JcHE`.
- Orders app: `~/Documents/PersonalRepos/kombucha-orders-app` (single `index.html` + `lib.js`, Firebase). Signup URL `https://roel-heremans.github.io/kombucha-orders-app/?signup`.
- Contact: Instagram `https://www.instagram.com/realhealthkombucha/`, WhatsApp group `https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R`, email `realhealthkombucha@gmail.com`, phone `+351 913 000 048`, address Caminho do Jangão 154, 9360-523 Ponta do Sol, Madeira.
- Style reference: `~/Documents/PersonalRepos/SattvaReset` (`output/styles.css`, templates).

## Visual design (direction A — Forest)

- Palette from Sattva: forest `#1E3526`, gold `#C9AA49`, off-white `#F8F6F3`, stone `#E8E4DE`, text `#1A1A18`, muted `#6B6460`.
- Type: Cormorant Garamond (headings, large numbers), Inter (body, UI); small uppercase letter-spaced nav and eyebrow labels, as on Sattva.
- Header: forest background, white logo, uppercase nav, outlined "Order" button, EN | PT switch.
- Hero sections: forest background with photo beside the text (as in the approved mockup). Content sections alternate off-white and stone; at least one full-width sunny photo band per long page (the bright product/terrace shots) to keep it warm.
- Generous whitespace, calm layout, thin gold accents; works at phone width (≥ 360px) with no horizontal scroll.
- Approved direction (option A): `docs/design/direction-a-forest.png` (committed). It is the reference for the header, hero (photo beside text), eyebrow, buttons and flavour row; Sattva's `output/styles.css` is the authority for everything it doesn't show. Mockup copy (e.g. "real fruit") is placeholder — this document's copy wins.
- Logo on the dark header: keep the gold sun as is, render the island and "REAL HEALTH" lettering in off-white (a two-tone derived version, not a flat white silhouette), and make it noticeably larger than in the mockup (the mockup's tiny white logo is not the target). The header "Order" button copies Sattva's outlined "Apply now" button.

## Site-wide elements

- **Review banner** (top of every page, both languages):
  EN "Leave us a Google review and receive a free kombucha bottle with your next order." + button "Write a review" → review URL (new tab).
  PT "Deixe-nos uma avaliação no Google e receba uma garrafa de kombucha grátis na sua próxima encomenda." + "Escrever avaliação".
  On desktop a small QR (review_qr.svg) next to it; on phone the button only.
- **Navigation** (EN / PT): Home / Início · For restaurants / Para restaurantes · Flavours / Sabores · Our story / A nossa história · Gut health / Saúde intestinal · Contact / Contacto · button Order / Encomendar (→ Order page).
- **Footer**: logo, one-line tagline, nav, Instagram, WhatsApp, email, address, "© {year} Real Health Kombucha", language switch.
- **Language**: English at `/…`, Portuguese at `/pt/…` with translated slugs (e.g. `/for-restaurants/` ↔ `/pt/para-restaurantes/`). The switch links to the same page in the other language; `<html lang>` and `hreflang` alternates set. All copy for both languages lives in the content file side by side. Portuguese is European Portuguese, written by Claude; Nina or a native speaker should proofread before go-live.

## Pages and sections

Copy below is the substance; final wording is the builder's within these facts. Figures are exact.

### 1. Home
1. Hero: eyebrow "Raw · Vegan · Probiotic"; heading "Handcrafted kombucha from Madeira"; line: brewed in small batches in Ponta do Sol by Roel & Nina with pure water, green tea and real flavour; already served in 8 restaurants and cafés. Buttons: "For restaurants" (primary) and "Order for home". Photo: Roel & Nina product scene.
2. Proof strip: 5.0 ★ from 37 Google reviews · 8 restaurants & cafés · brewed & delivered by hand.
3. Two paths: card "For restaurants" (up to €20.50 profit per 1 L bottle → For restaurants page) and card "For home" (1 L €8.00, 270 ml €3.50 → Order page).
4. Flavours row: six label fronts → Flavours page.
5. Full-width photo band.
6. Three or four Google quotes from slide 8 (author + stars) with link to all reviews.
7. "Already on the menu at": Sun Spot, Palm Spot, Koa Spot, Vegan World, Casa Velha do Palheiro, Casa Velha Tea House, Balancal, Buddha & Sakura (names as text).
8. Closing CTA: "Put Real Health Kombucha on your menu" → For restaurants.

### 2. For restaurants (most important)
1. Hero: "Kombucha that pays off on your menu"; short pitch; button "Become a partner" → orders-app signup; secondary "Talk to us on WhatsApp".
2. Why your guests will love it (slide 5 condensed): live cultures, less sugar, alcohol-free (< 0.5% vol), clean & vegan.
3. **By the glass** (slide 10) — table exactly:
   | Glass | Glasses per bottle | Cost per glass | Menu price | Profit per glass | Margin | Profit per bottle |
   |---|---|---|---|---|---|---|
   | 200 ml | 5 | €1.60 | €4.00 | €2.40 | 60% | €12.00 |
   | 200 ml | 5 | €1.60 | €5.70 | €4.10 | 72% | €20.50 |
   | 250 ml | 4 | €2.00 | €4.00 | €2.00 | 50% | €8.00 |
   | 250 ml | 4 | €2.00 | €5.70 | €3.70 | 65% | €14.80 |
   Note: "You pay €8.00 per 1 L bottle. Margin = profit ÷ menu price. VAT not included." Highlights: "72% margin at €5.70 per 200 ml glass", "2.5× your money back on every bottle". Tip: serve 200 ml over ice with a slice of fruit — five glasses per bottle.
4. **Small bottles** (slide 11): menu price €4.00 → profit €0.50 (13%); €5.00 → €1.50 (30%); €5.70 → €2.20 (39%). "You pay €3.50 per bottle plus a €1 deposit you get back when you return the empty. Price it at €5.00–€5.70."
5. **A typical month** (slide 12): 8 × 1 L in 200 ml glasses at €5.70 + 24 × 270 ml at €5.70. You spend €148 (8 × €8.00 + 24 × €3.50); guests spend €365 (40 glasses + 24 bottles at €5.70); extra profit €217 every month, from one fridge shelf. Deposit note (24 × €1 = €24 returned, not counted as cost).
6. **Ordering in 30 seconds** (slide 9) with real app screens (see below): one-tap reorder (last order pre-filled), we're notified instantly by WhatsApp and email, English or Portuguese, order history, recibos verdes downloadable. Steps: Scan/click to sign up → we activate your account → order anytime; works on any phone, add to home screen.
7. **Delivery & service** (slide 13): personal delivery across the island; we collect your empties and refund the deposit; table QR cards for reviews and bottle returns.
8. Already on the menu at (8 names) + 2–3 Google quotes.
9. CTA "Become a partner" (signup) + WhatsApp + email.

### 3. Flavours
Intro: six flavours, two sizes, all brewed with pure water, green tea, raw cane sugar and kombucha culture.
One card per flavour: label front, name, taste line, benefit, "Flavoured with: …", base ingredients line.

| Flavour | Taste | Benefit | Flavoured with |
|---|---|---|---|
| Ginger | Warming with a zesty bite | Warming ginger, traditionally used for digestive comfort | ginger |
| Wild Orange | Sunny, juicy and smooth | Bright, sweet orange — uplifting and cheerful | wild orange |
| Green Mandarine | Fresh, aromatic island citrus | Fresh, soft citrus — calming, a lovely evening drink | green mandarine |
| Lime | Crisp and thirst-quenching | Crisp and invigorating — the most refreshing of the six | lime |
| Metabolic Boost | Spicy-fresh and zesty | An energising, spicy-fresh blend | grapefruit, lemon, peppermint, ginger, cinnamon |
| Lemon & Turmeric | Golden, tangy and earthy | Golden and earthy, with lemon's zing and turmeric's warmth | lemon, turmeric |

Base ingredients (all flavours): water, green tea (Camellia sinensis), raw cane sugar, kombucha culture (SCOBY). Badges: raw & unpasteurised, live cultures, naturally sparkling, vegan, < 0.5% vol.
Sizes & prices: 1 L bottle €8.00 (for serving by the glass); 270 ml bottle €3.50 + €1 deposit, refunded on return. Most-loved: Ginger, Wild Orange, Metabolic Boost.
Footnote: "Based on published research on kombucha and fermented foods. Not a medical claim."

### 4. Our story
1. Meet Roel & Nina (slide 2): couple in Ponta do Sol; home experiment grew into a small-batch brewery; every bottle brewed, flavoured, bottled and delivered by the two of them.
2. It all started with our water (slide 3): drinking-water filter with a UMH Pure Gold device; tasted the difference; kombucha is > 95% water; friends kept asking for bottles.
3. From pure water to living drink (slide 4): four steps — pure water, green tea brew, fermentation, flavour & bottle (second fermentation makes it naturally sparkling). "Flavour & bottle" says natural flavours are added — no juice, no brand.
4. Ponta do Sol: brewed locally, small batches by hand, delivered personally.
Photos: portraits of Roel & Nina, terrace bottles.

### 5. Gut health
1. Intro: kombucha is fermented tea, raw and full of live cultures.
2. Six benefits (slide 5): live cultures; antioxidants (green tea polyphenols linked by research to protection against cell damage); gut friendly (fermented drinks associated with a more diverse gut flora); less sugar; alcohol-free choice (< 0.5% vol); clean & vegan.
3. Note: "Based on published research on kombucha and fermented foods. Not a medical claim."
4. CTA to Flavours and Order.

### 6. Order (home customers and anyone)
1. Prices: 1 L €8.00; 270 ml €3.50 + €1 deposit.
2. How to order: create an account in our app (button → signup; new accounts are activated by us), then order anytime; or message us on WhatsApp; or email (pre-filled mailto: subject "Kombucha order", body asking for flavours, sizes and delivery address).
3. Delivery: we deliver personally; bring back your empties and we refund the deposit.
4. Review reminder (same offer as banner).

### 7. Contact
Buttons: WhatsApp, Instagram, email; phone; address with a link to Google Maps; short "We usually reply the same day" style line is the builder's call (no promises of hours — old opening hours are dropped). **No contact form** (the phase-1 form and its phase-2 PHP script are dropped).

## App screens

Real screenshots of the orders app, not drawings. The app needs a login and live Firebase data, so the builder runs the app's own `index.html` locally with the Firebase calls replaced by a local stub serving made-up sample data (a "Demo Café" customer, sample flavours/orders/recibos), in a copy outside the orders-app repo. Nothing touches the real Firebase project or customer data, and the orders-app repo is not modified. Screens (phone size, both EN and PT if the app's language toggle allows): signup/login, new order pre-filled with last order, order history, recibos. Shown in simple phone frames on the restaurant page next to the slide-9 points.

## Photos

Only from `assets/01_images/`. Use: terrace/bottle shots (Bottel0x, Bottles01, Bottels02, Leave_bottels0x), the Roel & Nina portraits (WhatsApp 2026-02-21 series, excluding hot-tub shots), crate shots (Kist01, 2026-02-03 series) for delivery/empties, AI product scenes (2026-04-22 series and the four "ChatGPT Image Jun 30" images) for heroes and flavour bands. Exclude: hot-tub photos, "Welcome to Kombucha Brewing" sign photos, the A0 board, logo_lowres. Resize to sensible widths, compress (target < 300 KB each), descriptive file names, meaningful alt text in both languages. File names and alt text must not mention the flavouring brand.

## Changes to phase-1 behaviour

- Old pages About, Gut Health 101, Reseller, Contact, Shop are replaced by the structure above. Old content keys, templates, images and page-specific tests are removed or rewritten; the integrity tests (relative URLs, no Framer refs, no unused images, link resolution, head tags) stay and now cover both languages.
- Contact form, `contact_form_endpoint`, honeypot and the phase-2 PHP script are dropped (phase-2 notes in README updated).
- `original/` (Framer capture) stays in the repo as history but is no longer the reference.
- Preview flag, noindex, sitemap (now both languages with `hreflang`), deploy workflow unchanged.
- Old URLs (`/shop/`, `/reseller/`, `/about/`, `/gut-health-101/`) — builder adds simple redirect pages to the new equivalents so existing links/QRs keep working.

## Constraints

- Never mention the flavouring brand anywhere (repo is public).
- Figures exactly as in this document.
- Relative URLs only; works under the GitHub Pages subpath.
- Restaurant page and Home must read well on a phone.

## Decisions settled after builder check (Claude's calls)

- **Brand-secret enforcement:** the brand name is never written into the repo, not even in a test. Enforcement is a local, uncommitted git `pre-push` hook (in `.git/hooks/`, outside version control) plus a check by the controller before every push, scanning tracked files, commit messages and `output/` for the name. The builder checks every label and pitch image it uses visually for any supplier brand before committing it (the Ginger label front was checked and shows none). `Kombucha-01-original.png` is not used at all.
- **UMH Pure Gold** is named on Our story exactly as in Roel's own pitch deck (slide 3).
- **Label crops:** the centre third of each label is its front panel (verified on Ginger); the builder crops per label and checks every crop visually, adjusting per label if needed.
- **Google quotes on PT pages:** shown in their original English with a small "(original em inglês)" note; headings and surrounding text translated. The review count (5.0, 37 reviews) is one content value in the content file, used everywhere, so Roel can ask for it to be updated.
- **App screens:** first try the local Firebase stub (copy of the app outside its repo, sample data, customer "Demo Café", real flavour names and prices). If the stub turns out impractical, fall back to asking Roel for 3–4 phone screenshots from a test restaurant account — not drawings. The rest of the site does not wait on this; the app section ships with whichever screens are ready.
- **Build order:** Home, For restaurants, Order and Flavours first (one preview deploy after these), then Our story, Gut health, Contact, redirects. No deadline is known.
- **Language routing:** site root `/` is English (no auto-detection); Portuguese at `/pt/`. Old-URL redirects cover the English old paths only (no Portuguese pages existed before). The review QR is the same on both languages (it opens Google, which follows the visitor's own language).

## Left to the builder

Exact copy wording within the stated facts (both languages), section layouts and spacing in the Sattva style, which specific photo goes where (within the use/exclude lists), icon choice, how the app stub is built, phone-frame styling, redirect mechanism.

## Open points for Roel (not blocking the build)

- Portuguese proofreading by Nina or a native speaker before go-live.
