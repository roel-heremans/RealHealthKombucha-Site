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
        "maps": "https://maps.google.com/?q=Caminho+do+Jang%C3%A3o+154,+9360-523+Ponta+do+Sol",
        # All Google reviews (business listing on Google Maps).
        "reviews_all": "https://www.google.com/maps/search/?api=1&query=Real+Health+Kombucha"
                       "&query_place_id=ChIJtYnk8XlZYAwRhT9_o66JcHE",
    },
    "address": "Caminho do Jangão 154, 9360-523 Ponta do Sol, Madeira",
    "review_stats": {"rating": 5.0, "count": 37},  # rating shown with the `num(1)` filter
    # Header navigation (page ids). Home is reached via the logo on desktop and is
    # listed in the phone menu only.
    "nav_ids": ["home", "restaurants", "flavours", "story", "gut-health", "contact"],
    "order_button": {"en": "Order", "pt": "Encomendar"},
    "review_banner": {
        "text": {
            "en": "Leave us a Google review and receive a free kombucha bottle with your next order.",
            "pt": "Deixe-nos uma avaliação no Google e receba uma garrafa de kombucha grátis na sua próxima encomenda.",
        },
        "button": {"en": "Write a review", "pt": "Escrever avaliação"},
        "qr_alt": {
            "en": "QR code to write a Google review",
            "pt": "Código QR para escrever uma avaliação no Google",
        },
    },
    "footer_tagline": {
        "en": "Raw, vegan, probiotic kombucha, handcrafted in Ponta do Sol, Madeira.",
        "pt": "Kombucha crua, vegana e probiótica, feita à mão na Ponta do Sol, Madeira.",
    },
    # Default <meta name="description"> / og:description; a page may override with "description".
    "meta_description": {
        "en": "Raw, vegan, probiotic kombucha brewed in small batches in Ponta do Sol, Madeira. "
              "Six flavours for restaurants, cafés and home delivery.",
        "pt": "Kombucha crua, vegana e probiótica, produzida em pequenos lotes na Ponta do Sol, Madeira. "
              "Seis sabores para restaurantes, cafés e entrega em casa.",
    },
    # Prices in euros as numbers; templates format them per language with the `eur` filter.
    "prices": {
        "bottle_1l": 8.00,
        "bottle_270": 3.50,
        "deposit": 1.00,
        "max_profit_per_bottle": 20.50,  # 1 L in five 200 ml glasses at €5.70 (slide 10)
        "glass_menu_price": 5.70,         # suggested menu price per 200 ml glass (slide 10)
    },
    # Restaurants and cafés already serving it (names as text, not translated).
    "partners": [
        "Sun Spot", "Palm Spot", "Koa Spot", "Vegan World", "Casa Velha do Palheiro",
        "Casa Velha Tea House", "Balancal", "Buddha & Sakura",
    ],
    # Google reviews (slide 8), verbatim in their original English on both languages.
    "quotes": [
        {"text": "Some of the best kombucha I've had anywhere … First had it at the beach cafe … "
                 "and then had to buy my own bottles.", "author": "David W.", "stars": 5},
        {"text": "Absolutely delicious, authentic and raw (by FAR the best kombucha we have ever had).",
         "author": "Hannah R.", "stars": 5},
        {"text": "Super refreshing, lightly fizzy, and incredibly delicious. "
                 "You can immediately taste the superior quality.", "author": "Julia C.", "stars": 5},
        {"text": "Well-balanced, sweet, and surprisingly bubbly!", "author": "Theresa", "stars": 5},
        {"text": "I regularly get Metabolic Boost and Wild Orange ones but they're all top notch. "
                 "Perfect balance of sparkle too.", "author": "Stevie Z.", "stars": 5},
        {"text": "Best Kombucha not only on Madeira but all of Portugal, maybe even the world.",
         "author": "Annika F.", "stars": 5},
    ],
    # The six flavours, in display order. `name` is the product name printed on the label,
    # the same in both languages. Task 6 (Flavours page) adds taste, benefit, etc.
    "flavours": [
        {"id": "ginger", "name": "Ginger",
         "image": "assets/img/flavours/ginger.png",
         "alt": {"en": "Ginger kombucha label with a drawing of ginger root and a red ginger flower",
                 "pt": "Rótulo da kombucha Ginger com um desenho de raiz de gengibre e uma flor vermelha"}},
        {"id": "wild-orange", "name": "Wild Orange",
         "image": "assets/img/flavours/wild-orange.png",
         "alt": {"en": "Wild Orange kombucha label with a drawing of ripe oranges on a leafy branch",
                 "pt": "Rótulo da kombucha Wild Orange com um desenho de laranjas maduras num ramo"}},
        {"id": "lime", "name": "Lime",
         "image": "assets/img/flavours/lime.png",
         "alt": {"en": "Lime kombucha label with a drawing of whole and sliced limes",
                 "pt": "Rótulo da kombucha Lime com um desenho de limas inteiras e cortadas"}},
        {"id": "green-mandarine", "name": "Green Mandarine",
         "image": "assets/img/flavours/green-mandarine.png",
         "alt": {"en": "Green Mandarine kombucha label with a drawing of green mandarins and blossom",
                 "pt": "Rótulo da kombucha Green Mandarine com um desenho de tangerinas verdes e flores"}},
        {"id": "metabolic-boost", "name": "Metabolic Boost",
         "image": "assets/img/flavours/metabolic-boost.png",
         "alt": {"en": "Metabolic Boost kombucha label with a drawing of grapefruit, lemon, mint, ginger and cinnamon",
                 "pt": "Rótulo da kombucha Metabolic Boost com um desenho de toranja, limão, hortelã, gengibre e canela"}},
        {"id": "lemon-turmeric", "name": "Lemon & Turmeric",
         "image": "assets/img/flavours/lemon-turmeric.png",
         "alt": {"en": "Lemon & Turmeric kombucha label with a drawing of lemons and turmeric root",
                 "pt": "Rótulo da kombucha Lemon & Turmeric com um desenho de limões e raiz de curcuma"}},
    ],
    # Home page (spec section 1). "{partners}" / "{count}" are filled in by the template.
    "home": {
        "hero": {
            "eyebrow": {"en": "Raw · Vegan · Probiotic", "pt": "Crua · Vegana · Probiótica"},
            "heading": {"en": "Handcrafted kombucha", "pt": "Kombucha artesanal"},
            "heading_accent": {"en": "from Madeira", "pt": "da Madeira"},
            "lead": {
                "en": "Brewed in small batches in Ponta do Sol by Roel & Nina, with pure water, "
                      "green tea and natural flavours. Already served in {partners} restaurants "
                      "and cafés across the island.",
                "pt": "Produzida em pequenos lotes na Ponta do Sol pelo Roel e pela Nina, com água "
                      "pura, chá verde e aromas naturais. Já é servida em {partners} restaurantes "
                      "e cafés por toda a ilha.",
            },
            "primary": {"en": "For restaurants", "pt": "Para restaurantes"},
            "secondary": {"en": "Order for home", "pt": "Encomendar para casa"},
            "image": "assets/img/photos/roel-nina-tasting-box-coast.jpg",
            "alt": {
                "en": "Roel and Nina raising glasses of kombucha behind a box of six bottles, "
                      "on a sunny terrace above the sea",
                "pt": "O Roel e a Nina a brindar com kombucha atrás de uma caixa com seis garrafas, "
                      "num terraço soalheiro sobre o mar",
            },
        },
        "proof": {
            "reviews": {"en": "from {count} Google reviews", "pt": "em {count} avaliações no Google"},
            "partners": {"en": "restaurants & cafés serving it", "pt": "restaurantes e cafés já a servem"},
            "hand": {"en": "By hand", "pt": "À mão"},
            "hand_label": {"en": "brewed & delivered in Ponta do Sol",
                           "pt": "produzida e entregue a partir da Ponta do Sol"},
        },
        "paths": {
            "restaurants_eyebrow": {"en": "For restaurants", "pt": "Para restaurantes"},
            "restaurants_title": {"en": "Kombucha that pays off on your menu",
                                  "pt": "Kombucha que compensa no seu menu"},
            "up_to": {"en": "up to", "pt": "até"},
            "restaurants_price_note": {"en": "profit per 1 L bottle, served by the glass",
                                       "pt": "de lucro por garrafa de 1 L, servida a copo"},
            # Slide 10 highlights. "{price}" = glass_menu_price, formatted per language.
            "highlights": [
                {"num": {"en": "72%", "pt": "72%"},
                 "label": {"en": "margin on a 200 ml glass at {price}",
                           "pt": "de margem num copo de 200 ml a {price}"}},
                {"num": {"en": "2.5×", "pt": "2,5×"},
                 "label": {"en": "your money back on every bottle",
                           "pt": "o seu investimento de volta, em cada garrafa"}},
            ],
            "restaurants_text": {
                "en": "Five glasses from every bottle, reordering in one tap, and personal "
                      "delivery across the island.",
                "pt": "Cinco copos por garrafa, novas encomendas com um só toque e entrega "
                      "pessoal em toda a ilha.",
            },
            "restaurants_button": {"en": "See the numbers", "pt": "Ver os números"},
            "home_eyebrow": {"en": "For home", "pt": "Para casa"},
            "home_title": {"en": "Fresh kombucha, delivered to your door",
                           "pt": "Kombucha fresca, entregue à sua porta"},
            "bottle_1l": {"en": "1 L bottle", "pt": "Garrafa de 1 L"},
            "bottle_270": {"en": "270 ml bottle", "pt": "Garrafa de 270 ml"},
            "deposit_note": {"en": "+ {deposit} deposit, refunded when you return the bottle",
                             "pt": "+ {deposit} de depósito, devolvido quando nos entregar a garrafa"},
            "home_text": {
                "en": "Six flavours, brewed in small batches and delivered by us personally.",
                "pt": "Seis sabores, produzidos em pequenos lotes e entregues pessoalmente por nós.",
            },
            "home_button": {"en": "How to order", "pt": "Como encomendar"},
        },
        "flavours": {
            "eyebrow": {"en": "Our flavours", "pt": "Os nossos sabores"},
            "heading": {"en": "Six flavours,", "pt": "Seis sabores,"},
            "heading_accent": {"en": "naturally sparkling", "pt": "naturalmente efervescentes"},
            "link": {"en": "Discover all six", "pt": "Conheça os seis sabores"},
        },
        "band": {
            "image": "assets/img/photos/six-flavours-coast-lineup.jpg",
            "alt": {
                "en": "Six kombucha bottles, one of each flavour, lined up in the sun with fresh "
                      "citrus, ginger and the Madeira coast behind",
                "pt": "Seis garrafas de kombucha, uma de cada sabor, alinhadas ao sol com citrinos, "
                      "gengibre e a costa da Madeira ao fundo",
            },
        },
        "quotes": {
            "eyebrow": {"en": "Google reviews", "pt": "Avaliações no Google"},
            "heading": {"en": "What our guests say", "pt": "O que dizem os nossos clientes"},
            "pick": [0, 1, 2, 5],  # indexes into CONTENT["quotes"] shown on the home page
        },
        "cta": {
            "image": "assets/img/photos/roel-nina-balcony-bottles.jpg",
            "alt": {
                "en": "Roel and Nina smiling on a sunny balcony, each holding a bottle of kombucha",
                "pt": "O Roel e a Nina a sorrir numa varanda soalheira, cada um com uma garrafa de kombucha",
            },
            "eyebrow": {"en": "For restaurants & cafés", "pt": "Para restaurantes e cafés"},
            "heading": {"en": "Put Real Health Kombucha on your menu",
                        "pt": "Coloque a Real Health Kombucha no seu menu"},
            "lead": {
                "en": "Serve it by the glass or by the bottle. We deliver personally, collect your "
                      "empties, and you reorder in seconds from your phone.",
                "pt": "Sirva-a a copo ou à garrafa. Entregamos pessoalmente, recolhemos as garrafas "
                      "vazias e volta a encomendar em segundos pelo telemóvel.",
            },
            "button": {"en": "For restaurants", "pt": "Para restaurantes"},
            "whatsapp": {"en": "Talk to us on WhatsApp", "pt": "Fale connosco no WhatsApp"},
        },
    },
    # Shared interface labels.
    "ui": {
        "switch_title": {"en": "Ver em português", "pt": "View in English"},
        "menu": {"en": "Menu", "pt": "Menu"},
        "skip": {"en": "Skip to content", "pt": "Saltar para o conteúdo"},
        "menu_open": {"en": "Open menu", "pt": "Abrir menu"},
        "menu_close": {"en": "Close menu", "pt": "Fechar menu"},
        "review_label": {"en": "Google review", "pt": "Avaliação no Google"},
        "footer_nav": {"en": "Footer", "pt": "Rodapé"},
        "language": {"en": "Language", "pt": "Idioma"},
        "redirect_text": {"en": "This page has moved to", "pt": "Esta página mudou para"},
        "rights": {"en": "All rights reserved.", "pt": "Todos os direitos reservados."},
        "stars": {"en": "{n} out of 5 stars", "pt": "{n} de 5 estrelas"},
        # Shown after a quote whose language differs from the page (quotes are English).
        "original_language": {"en": "(original in English)", "pt": "(original em inglês)"},
        "all_reviews": {"en": "Read all our Google reviews", "pt": "Ver todas as avaliações no Google"},
        "partners_heading": {"en": "Already on the menu at", "pt": "Já está no menu de"},
    },
}
