# Editable content for the site. Change these and run build.py to regenerate output.
#
# Every value shown to visitors is a {"en": ..., "pt": ...} dict (European Portuguese);
# templates pick the page language with the `t` filter. Plain strings/numbers (URLs,
# phone numbers, figures) are the same in both languages.

CONTENT = {
    "preview": True,
    "site_name": "Real Health Kombucha",
    "site_url": "https://www.realhealthkombucha.com/",
    # Pages, in navigation order. Slugs: EN lives at /<en>/, PT at /pt/<pt>/ ("" = home).
    "pages": [
        {
            "id": "home",
            "template": "home.html.j2",
            "slug": {"en": "", "pt": ""},
            "title": {"en": "Real Health Kombucha Madeira", "pt": "Real Health Kombucha Madeira"},
            "nav": {"en": "Home", "pt": "Início"},
        },
        {
            "id": "restaurants",
            "template": "restaurants.html.j2",
            "slug": {"en": "for-restaurants", "pt": "para-restaurantes"},
            "title": {"en": "For Restaurants", "pt": "Para Restaurantes"},
            "nav": {"en": "For Restaurants", "pt": "Para Restaurantes"},
        },
        {
            "id": "flavours",
            "template": "flavours.html.j2",
            "slug": {"en": "flavours", "pt": "sabores"},
            "title": {"en": "Flavours", "pt": "Sabores"},
            "nav": {"en": "Flavours", "pt": "Sabores"},
        },
        {
            "id": "story",
            "template": "story.html.j2",
            "slug": {"en": "our-story", "pt": "a-nossa-historia"},
            "title": {"en": "Our Story", "pt": "A Nossa História"},
            "nav": {"en": "Our Story", "pt": "A Nossa História"},
        },
        {
            "id": "gut-health",
            "template": "gut-health.html.j2",
            "slug": {"en": "gut-health", "pt": "saude-intestinal"},
            "title": {"en": "Gut Health", "pt": "Saúde Intestinal"},
            "nav": {"en": "Gut Health", "pt": "Saúde Intestinal"},
        },
        {
            "id": "order",
            "template": "order.html.j2",
            "slug": {"en": "order", "pt": "encomendar"},
            "title": {"en": "Order", "pt": "Encomendar"},
            "nav": {"en": "Order", "pt": "Encomendar"},
        },
        {
            "id": "contact",
            "template": "contact.html.j2",
            "slug": {"en": "contact", "pt": "contacto"},
            "title": {"en": "Contact", "pt": "Contacto"},
            "nav": {"en": "Contact", "pt": "Contacto"},
        },
    ],
    # Old EN paths (phase-1 site, printed QR codes) -> page id they now redirect to.
    "redirects": {
        "shop": "order",
        "reseller": "restaurants",
        "about": "story",
        "gut-health-101": "gut-health",
    },
    "links": {
        "review": "https://search.google.com/local/writereview?placeid=ChIJtYnk8XlZYAwRhT9_o66JcHE",
        "signup": "https://roel-heremans.github.io/kombucha-orders-app/?signup",
        "whatsapp": "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R",
        "instagram": "https://www.instagram.com/realhealthkombucha/",
        "email": "realhealthkombucha@gmail.com",
        "phone": "+351 913 000 048",
    },
    "review_stats": {"rating": "5.0", "count": 37},
    # Shared interface labels.
    "ui": {
        "switch_title": {"en": "Ver em português", "pt": "View in English"},
        "menu": {"en": "Menu", "pt": "Menu"},
        "redirect_text": {"en": "This page has moved to", "pt": "Esta página mudou para"},
        "rights": {"en": "All rights reserved.", "pt": "Todos os direitos reservados."},
    },
}
