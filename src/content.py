# Editable content for the site. Change these and run build.py to regenerate output.

CONTENT = {
    "preview": True,
    "site_name": "Real Health Kombucha",
    "site_url": "https://www.realhealthkombucha.com/",
    "pages": [
        {"slug": "", "template": "home.html.j2", "title": "HOME - Real Health Kombucha Madeira", "nav_label": "Home"},
        {"slug": "about", "template": "about.html.j2", "title": "About - Real Health Kombucha Madeira", "nav_label": "About"},
        {"slug": "gut-health-101", "template": "gut-health-101.html.j2", "title": "Gut Health 101 - Real Health Kombucha Madeira", "nav_label": "Gut Health 101"},
        {"slug": "reseller", "template": "reseller.html.j2", "title": "Reseller Program - Real Health Kombucha Madeira", "nav_label": "Reseller"},
        {"slug": "contact", "template": "contact.html.j2", "title": "Contact - Real Health Kombucha Madeira", "nav_label": "Contact"},
        {"slug": "shop", "template": "shop.html.j2", "title": "Shop - Real Health Kombucha Madeira", "nav_label": "Shop"},
    ],
    # Top banner. The word "here" is appended by the template; it is highlighted,
    # and wrapped in a link only when the *_link slug is non-empty ("" = no link).
    # Home banner wording differs per breakpoint on the live site (verbatim):
    # phone/tablet (<960px) uses banner_home_text, desktop uses banner_home_text_desktop.
    "banner_home_text": "Exciting News! 📣 - Get a free 1 Liter Kombucha Bottle",
    "banner_home_text_desktop": "Exciting News!📣 - Get a free 1 Liter Kombucha Bottle on your next order click",
    "banner_home_link": "",
    "banner_default_text": "For Hotels & Restaurants - Become a Partner",
    "banner_default_link": "reseller",
    # Header navigation (page slugs, in order; "" = Home). "shop" is shown as a button.
    "nav": ["", "about", "gut-health-101", "reseller", "contact", "shop"],
    # Footer link column order (as on the live site).
    "footer_nav": ["", "about", "shop", "reseller", "gut-health-101", "contact"],
    "footer_tagline": (
        "Real Health Kombucha, crafted with care from the finest natural ingredients. "
        "Join us on our journey to better well-being\u2014one sip at a time."
    ),
    "socials": {
        "instagram": "https://www.instagram.com/realhealthkombucha/",
        "telegram": "http://t.me/RealHealthKombucha",
        "whatsapp": "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R",
    },
    "google_reviews_url": (
        "https://www.google.de/search?sca_esv=bb6fb22019ea88f6&tbm=lcl&q=Real+Health+Kombucha+Reviews"
        "&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDQ3MbQwMTcwszA2N7c0MLU038DI-IpRJig1MUfBA0iUZCh45-cmlSZnJCoEpZZlppYXL2LFKw0A0qUfvFgAAAA"
        "&rldimm=8174184706837790597&hl=en-PT#lkt=LocalPoiReviews"
    ),
    # Footer "Follow Us On Instagram" grid (files in assets/img/).
    "footer_instagram_images": [
        "footer-instagram-1.jpg",
        "footer-instagram-2.jpg",
        "footer-instagram-3.jpg",
        "footer-instagram-4.jpg",
    ],
}
