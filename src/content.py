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
        # Direct chat with Roel's number: every "order" / "talk to us" / "message us" button.
        "whatsapp_chat": "https://wa.me/351913000048",
        # Group invite: news & new batches only (Contact page and footer).
        "whatsapp": "https://chat.whatsapp.com/HFERsCciyntHTvYT8nuv6R",
        "instagram": "https://www.instagram.com/realhealthkombucha/",
        "email": "realhealthkombucha@gmail.com",
        "phone": "+351 913 000 048",
        "maps": "https://www.google.com/maps/search/?api=1&query=32.693336%2C-17.083575",  # the house
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
        "Casa Velha Tea House", "Vista Balancal", "Buddha & Sakura",
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
    # the same in both languages. taste / benefit / flavoured_with: spec section 3 table (EN
    # verbatim). Never "juice"/"sumo"; flavours are described only as "Flavoured with: ...".
    # most_loved: the three most-loved flavours (spec).
    "flavours": [
        {"id": "ginger", "name": "Ginger",
         "image": "assets/img/flavours/ginger.png",
         "alt": {"en": "Ginger kombucha label with a drawing of ginger root and a red ginger flower",
                 "pt": "Rótulo da kombucha Ginger com um desenho de raiz de gengibre e uma flor vermelha"},
         "taste": {"en": "Warming with a zesty bite", "pt": "Aconchegante, com um toque vivo e picante"},
         "benefit": {"en": "Warming ginger, traditionally used for digestive comfort",
                     "pt": "Gengibre aconchegante, tradicionalmente usado para o conforto digestivo"},
         "flavoured_with": {"en": "ginger", "pt": "gengibre"},
         "most_loved": True},
        {"id": "wild-orange", "name": "Wild Orange",
         "image": "assets/img/flavours/wild-orange.png",
         "alt": {"en": "Wild Orange kombucha label with a drawing of ripe oranges on a leafy branch",
                 "pt": "Rótulo da kombucha Wild Orange com um desenho de laranjas maduras num ramo"},
         "taste": {"en": "Sunny, juicy and smooth", "pt": "Solarenga, suculenta e suave"},
         "benefit": {"en": "Bright, sweet orange — uplifting and cheerful",
                     "pt": "Laranja doce e luminosa — anima e alegra"},
         "flavoured_with": {"en": "wild orange", "pt": "laranja selvagem"},
         "most_loved": True},
        {"id": "lime", "name": "Lime",
         "image": "assets/img/flavours/lime.png",
         "alt": {"en": "Lime kombucha label with a drawing of whole and sliced limes",
                 "pt": "Rótulo da kombucha Lime com um desenho de limas inteiras e cortadas"},
         "taste": {"en": "Crisp and thirst-quenching", "pt": "Fresca e vibrante, mata a sede"},
         "benefit": {"en": "Crisp and invigorating — the most refreshing of the six",
                     "pt": "Viva e revigorante — a mais refrescante das seis"},
         "flavoured_with": {"en": "lime", "pt": "lima"},
         "most_loved": False},
        {"id": "green-mandarine", "name": "Green Mandarine",
         "image": "assets/img/flavours/green-mandarine.png",
         "alt": {"en": "Green Mandarine kombucha label with a drawing of green mandarins and blossom",
                 "pt": "Rótulo da kombucha Green Mandarine com um desenho de tangerinas verdes e flores"},
         "taste": {"en": "Fresh, aromatic island citrus", "pt": "Citrino fresco e aromático da ilha"},
         "benefit": {"en": "Fresh, soft citrus — calming, a lovely evening drink",
                     "pt": "Citrino fresco e suave — calmante, uma ótima bebida para o fim do dia"},
         "flavoured_with": {"en": "green mandarine", "pt": "tangerina verde"},
         "most_loved": False},
        {"id": "metabolic-boost", "name": "Metabolic Boost",
         "image": "assets/img/flavours/metabolic-boost.png",
         "alt": {"en": "Metabolic Boost kombucha label with a drawing of grapefruit, lemon, mint, ginger and cinnamon",
                 "pt": "Rótulo da kombucha Metabolic Boost com um desenho de toranja, limão, hortelã, gengibre e canela"},
         "taste": {"en": "Spicy-fresh and zesty", "pt": "Picante, fresca e vibrante"},
         "benefit": {"en": "An energising, spicy-fresh blend",
                     "pt": "Uma mistura energizante, picante e fresca"},
         "flavoured_with": {"en": "grapefruit, lemon, peppermint, ginger, cinnamon",
                            "pt": "toranja, limão, hortelã-pimenta, gengibre, canela"},
         "most_loved": True},
        {"id": "lemon-turmeric", "name": "Lemon & Turmeric",
         "image": "assets/img/flavours/lemon-turmeric.png",
         "alt": {"en": "Lemon & Turmeric kombucha label with a drawing of lemons and turmeric root",
                 "pt": "Rótulo da kombucha Lemon & Turmeric com um desenho de limões e raiz de curcuma"},
         "taste": {"en": "Golden, tangy and earthy", "pt": "Dourada, acidulada e terrosa"},
         "benefit": {"en": "Golden and earthy, with lemon's zing and turmeric's warmth",
                     "pt": "Dourada e terrosa, com a vivacidade do limão e o calor da curcuma"},
         "flavoured_with": {"en": "lemon, turmeric", "pt": "limão, curcuma"},
         "most_loved": False},
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
            "image": "assets/img/photos/roel-nina-tasting-box-coast-v4.jpg",
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
                 "label": {"en": "your money back per bottle, at {price} per 200 ml glass",
                           "pt": "o seu investimento de volta por garrafa, a {price} por copo de 200 ml"}},
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
    # For restaurants page (spec section 2; pitch slides 5, 9-13). Money values are numbers
    # in euros, formatted per language by the `eur` filter; margins are whole percents.
    # Placeholders in copy ("{price}", "{max}", ...) are filled in by the template.
    "restaurants": {
        "hero": {
            "eyebrow": {"en": "For restaurants & cafés", "pt": "Para restaurantes e cafés"},
            "heading": {"en": "Kombucha that pays off", "pt": "Kombucha que compensa"},
            "heading_accent": {"en": "on your menu", "pt": "no seu menu"},
            "lead": {
                "en": "A raw, sparkling, alcohol-free drink your guests order again, with a margin "
                      "that works for you. Brewed in small batches in Ponta do Sol, delivered by us "
                      "and reordered in seconds from your phone.",
                "pt": "Uma bebida crua, efervescente e sem álcool que os seus clientes voltam a "
                      "pedir, com uma margem que compensa. Produzida em pequenos lotes na Ponta do "
                      "Sol, entregue por nós e encomendada em segundos pelo telemóvel.",
            },
            "primary": {"en": "Become a partner", "pt": "Torne-se parceiro"},
            "up_to": {"en": "up to", "pt": "até"},
            "whatsapp": {"en": "Talk to us on WhatsApp", "pt": "Fale connosco no WhatsApp"},
            # Key figures under the buttons. "{max}" = prices.max_profit_per_bottle,
            # "{partners}" = number of partners.
            "facts": [
                # "up_to" marks a best-case figure (200 ml glasses at glass_menu_price).
                {"num": "{max}", "up_to": True,
                 "label": {"en": "profit per 1 L bottle", "pt": "de lucro por garrafa de 1 L"}},
                {"num": "72%", "up_to": True,
                 "label": {"en": "margin by the glass", "pt": "de margem a copo"}},
                {"num": "{partners}",
                 "label": {"en": "restaurants & cafés already serve it",
                           "pt": "restaurantes e cafés já a servem"}},
            ],
            "image": "assets/img/photos/roel-glass-garden.jpg",
            "alt": {
                "en": "Roel handing a guest a glass of kombucha in a sunny garden",
                "pt": "O Roel a servir um copo de kombucha a um cliente num jardim soalheiro",
            },
        },
        # Slide 5, condensed to the four points that matter at the table.
        "why": {
            "eyebrow": {"en": "Why your guests will love it", "pt": "Porque os seus clientes vão gostar"},
            "heading": {"en": "A drink your guests", "pt": "Uma bebida que os seus clientes"},
            "heading_accent": {"en": "feel good about", "pt": "bebem com gosto"},
            "items": [
                {"title": {"en": "Live cultures", "pt": "Culturas vivas"},
                 "tag": {"en": "Raw · unpasteurised", "pt": "Crua · não pasteurizada"},
                 "text": {"en": "Full of the living bacteria and yeasts from fermentation.",
                          "pt": "Cheia das bactérias e leveduras vivas da fermentação."}},
                {"title": {"en": "Less sugar", "pt": "Menos açúcar"},
                 "tag": {"en": "Lighter than soft drinks", "pt": "Mais leve que um refrigerante"},
                 "text": {"en": "Most of the sugar is consumed during fermentation.",
                          "pt": "A maior parte do açúcar é consumida durante a fermentação."}},
                {"title": {"en": "Alcohol-free", "pt": "Sem álcool"},
                 "tag": {"en": "< 0.5% vol", "pt": "< 0,5% vol"},
                 "text": {"en": "An adult drink for guests who skip alcohol.",
                          "pt": "Uma bebida adulta para quem não bebe álcool."}},
                {"title": {"en": "Clean & vegan", "pt": "Simples e vegana"},
                 "tag": {"en": "Nothing artificial", "pt": "Nada de artificial"},
                 "text": {"en": "Only water, green tea, cane sugar, kombucha culture and "
                                "natural flavours.",
                          "pt": "Apenas água, chá verde, açúcar de cana, cultura de kombucha e "
                                "aromas naturais."}},
            ],
        },
        # Slide 10. Columns: glass size (ml), glasses per bottle, cost per glass, menu price,
        # profit per glass, margin (%), profit per bottle. Exactly as in the spec.
        "glass_rows": [
            {"ml": 200, "glasses": 5, "cost": 1.60, "menu": 4.00, "profit": 2.40, "margin": 60, "per_bottle": 12.00},
            {"ml": 200, "glasses": 5, "cost": 1.60, "menu": 5.70, "profit": 4.10, "margin": 72, "per_bottle": 20.50},
            {"ml": 250, "glasses": 4, "cost": 2.00, "menu": 4.00, "profit": 2.00, "margin": 50, "per_bottle": 8.00},
            {"ml": 250, "glasses": 4, "cost": 2.00, "menu": 5.70, "profit": 3.70, "margin": 65, "per_bottle": 14.80},
        ],
        "glass_highlight": 1,  # index of the highlighted row (200 ml at €5.70)
        "money_back_multiple": 2.5,  # slide 10: "2.5× your money back on every bottle"
        "glass": {
            "eyebrow": {"en": "By the glass", "pt": "A copo"},
            "heading": {"en": "One 1 L bottle earns you", "pt": "Uma garrafa de 1 L rende-lhe"},
            "heading_accent": {"en": "up to {max}", "pt": "até {max}"},
            "intro": {
                "en": "Served by the glass, every litre goes a long way. This is what one bottle "
                      "earns you at two glass sizes and two menu prices.",
                "pt": "Servida a copo, cada litro rende muito. Veja quanto ganha com uma garrafa "
                      "em dois tamanhos de copo e dois preços de menu.",
            },
            "cols": {
                "glass": {"en": "Glass", "pt": "Copo"},
                "glasses": {"en": "Glasses per bottle", "pt": "Copos por garrafa"},
                "cost": {"en": "Cost per glass", "pt": "Custo por copo"},
                "menu": {"en": "Menu price", "pt": "Preço no menu"},
                "profit": {"en": "Profit per glass", "pt": "Lucro por copo"},
                "margin": {"en": "Margin", "pt": "Margem"},
                "per_bottle": {"en": "Profit per bottle", "pt": "Lucro por garrafa"},
            },
            "note": {
                "en": "You pay {price} per 1 L bottle. Margin = profit ÷ menu price. VAT not included.",
                "pt": "Paga {price} por garrafa de 1 L. Margem = lucro ÷ preço no menu. IVA não incluído.",
            },
            # "{price}" = prices.glass_menu_price; "{multiple}" = money_back_multiple.
            "highlights": [
                {"num": "72%",
                 "label": {"en": "margin at {price} per 200 ml glass",
                           "pt": "de margem a {price} por copo de 200 ml"}},
                {"num": "{multiple}×",
                 "label": {"en": "your money back per bottle, at {price} per 200 ml glass",
                           "pt": "o seu investimento de volta por garrafa, a {price} por copo de 200 ml"}},
            ],
            "tip_label": {"en": "Tip", "pt": "Dica"},
            "tip": {
                "en": "Serve it in 200 ml glasses over ice with a slice of fruit. It looks premium "
                      "and gets you five glasses from every bottle.",
                "pt": "Sirva-a em copos de 200 ml, com gelo e uma rodela de fruta. Tem um ar "
                      "premium e rende cinco copos de cada garrafa.",
            },
        },
        # Slide 11: the 270 ml bottle at three menu prices. Exactly as in the spec.
        "bottle_rows": [
            {"menu": 4.00, "profit": 0.50, "margin": 13},
            {"menu": 5.00, "profit": 1.50, "margin": 30},
            {"menu": 5.70, "profit": 2.20, "margin": 39},
        ],
        "bottle_highlight": 2,
        "bottle_price_range": [5.00, 5.70],
        "bottles": {
            "eyebrow": {"en": "Small bottles", "pt": "Garrafas pequenas"},
            "heading": {"en": "Small bottles pay off", "pt": "As garrafas pequenas compensam"},
            "heading_accent": {"en": "from {price} on the menu", "pt": "a partir de {price} no menu"},
            "pay": {"en": "You pay {price} per 270 ml bottle",
                    "pt": "Paga {price} por garrafa de 270 ml"},
            "deposit": {
                "en": "plus a {deposit} deposit that you get back when you return the empty.",
                "pt": "mais {deposit} de depósito, que lhe devolvemos quando nos entrega a garrafa vazia.",
            },
            "advice_title": {"en": "Price it at {range}", "pt": "Ponha-a no menu a {range}"},
            "advice": {"en": "At {low} there is only {profit} left per bottle.",
                       "pt": "A {low} sobram apenas {profit} por garrafa."},
            "cols": {
                "menu": {"en": "Menu price", "pt": "Preço no menu"},
                "profit": {"en": "Profit", "pt": "Lucro"},
                "margin": {"en": "Margin", "pt": "Margem"},
            },
            "caption": {"en": "Per 270 ml bottle. VAT not included.",
                        "pt": "Por garrafa de 270 ml. IVA não incluído."},
        },
        # Slide 12. Totals exactly as in the spec.
        "month_example": {
            "bottles_1l": 8, "glasses": 40, "bottles_270": 24, "menu_price": 5.70,
            "you_spend": 148, "guests_spend": 365, "extra_profit": 217, "deposit_total": 24,
        },
        "month": {
            "eyebrow": {"en": "A typical month", "pt": "Um mês típico"},
            "heading": {"en": "What a typical month", "pt": "Como pode ser"},
            "heading_accent": {"en": "could look like", "pt": "um mês típico"},
            "example": {
                "en": "Example order: {n1l} × 1 L bottles served in 200 ml glasses at {price}, "
                      "plus {n270} × 270 ml bottles at {price}.",
                "pt": "Exemplo de encomenda: {n1l} garrafas de 1 L servidas em copos de 200 ml a "
                      "{price}, mais {n270} garrafas de 270 ml a {price}.",
            },
            "spend": {"en": "You spend", "pt": "O seu custo"},
            "spend_calc": "{n1l} × {p1l} + {n270} × {p270}",
            "guests": {"en": "Your guests spend", "pt": "Os seus clientes gastam"},
            "guests_calc": {"en": "{glasses} glasses + {n270} bottles at {price}",
                            "pt": "{glasses} copos + {n270} garrafas a {price}"},
            "profit": {"en": "Your extra profit", "pt": "O seu lucro extra"},
            "profit_calc": {"en": "every month, from one fridge shelf",
                            "pt": "todos os meses, com uma só prateleira do frigorífico"},
            "deposit_note": {
                "en": "The {n270} × {deposit} deposit ({total}) comes back to you when the empties "
                      "are returned, so it's not included as a cost. VAT not included.",
                "pt": "O depósito de {n270} × {deposit} ({total}) é-lhe devolvido quando entrega as "
                      "garrafas vazias, por isso não é contabilizado como custo. IVA não incluído.",
            },
        },
        # Slide 9.
        "app": {
            "eyebrow": {"en": "Ordering in 30 seconds", "pt": "Encomendar em 30 segundos"},
            "heading": {"en": "Reordering takes 30 seconds", "pt": "Repetir uma encomenda demora"},
            "heading_accent": {"en": "in our app", "pt": "30 segundos na nossa app"},
            "points": [
                {"title": {"en": "One-tap reorder", "pt": "Repetir com um toque"},
                 "text": {"en": "Your last order is pre-filled; adjust and send.",
                          "pt": "A sua última encomenda já vem preenchida; ajuste e envie."}},
                {"title": {"en": "We're notified instantly", "pt": "Somos avisados de imediato"},
                 "text": {"en": "Every order reaches us by WhatsApp and email.",
                          "pt": "Cada encomenda chega-nos por WhatsApp e por email."}},
                {"title": {"en": "English or Portuguese", "pt": "Português ou inglês"},
                 "text": {"en": "Your staff use whichever language they prefer.",
                          "pt": "A sua equipa usa a língua que preferir."}},
                {"title": {"en": "Order history", "pt": "Histórico de encomendas"},
                 "text": {"en": "See what you ordered and when it was delivered.",
                          "pt": "Veja o que encomendou e quando foi entregue."}},
                {"title": {"en": "Recibos verdes", "pt": "Recibos verdes"},
                 "text": {"en": "Download your recibos verdes straight from the app.",
                          "pt": "Descarregue os seus recibos verdes diretamente na app."}},
            ],
            "steps_title": {"en": "How to start", "pt": "Como começar"},
            "steps": [
                {"title": {"en": "Sign up", "pt": "Registe-se"},
                 "text": {"en": "Scan our QR code or tap the button below to create your account.",
                          "pt": "Leia o nosso código QR ou toque no botão abaixo para criar a conta."}},
                {"title": {"en": "We activate it", "pt": "Nós ativamos a conta"},
                 "text": {"en": "We check your details and switch your account on.",
                          "pt": "Confirmamos os seus dados e ativamos a sua conta."}},
                {"title": {"en": "Order anytime", "pt": "Encomende quando quiser"},
                 "text": {"en": "Send an order whenever you need one, day or night.",
                          "pt": "Envie uma encomenda sempre que precisar, a qualquer hora."}},
            ],
            "any_phone": {"en": "Works on any phone: add it to your home screen.",
                          "pt": "Funciona em qualquer telemóvel: adicione-a ao ecrã principal."},
            "button": {"en": "Create your account", "pt": "Criar conta"},
        },
        # Real orders-app screenshots (tools/app_screens/make_screens.py: the app's own code with
        # sample data, no real customers), the app shown in the page language.
        "app_screens": [
            {"image": {"en": "assets/img/app/signup-en.png", "pt": "assets/img/app/signup-pt.png"},
             "caption": {"en": "Create your account",
                         "pt": "Crie a sua conta"}},
            {"image": {"en": "assets/img/app/new-order-en.png", "pt": "assets/img/app/new-order-pt.png"},
             "caption": {"en": "New order, pre-filled with your last one",
                         "pt": "Última encomenda já preenchida"}},
            {"image": {"en": "assets/img/app/history-en.png", "pt": "assets/img/app/history-pt.png"},
             "caption": {"en": "Your orders and recibos verdes",
                         "pt": "As suas encomendas e recibos verdes"}},
        ],
        # Slide 13.
        "delivery": {
            "eyebrow": {"en": "Delivery & service", "pt": "Entrega e serviço"},
            "heading": {"en": "We deliver,", "pt": "Nós entregamos,"},
            "heading_accent": {"en": "you simply serve", "pt": "só tem de servir"},
            "lead": {
                "en": "No wholesaler in between. We bring every order ourselves and take care of "
                      "the rest.",
                "pt": "Sem intermediários. Levamos cada encomenda pessoalmente e tratamos do resto.",
            },
            "items": [
                {"title": {"en": "Personal delivery across the island",
                           "pt": "Entrega pessoal em toda a ilha"},
                 "text": {"en": "Roel or Nina bring your order to your door themselves.",
                          "pt": "O Roel ou a Nina levam a encomenda até à sua porta."}},
                {"title": {"en": "We collect your empties", "pt": "Recolhemos as garrafas vazias"},
                 "text": {"en": "Hand us the empty bottles at the next delivery and we refund the deposit.",
                          "pt": "Entregue-nos as garrafas vazias na entrega seguinte e devolvemos o depósito."}},
                {"title": {"en": "Table QR cards", "pt": "Cartões QR para as mesas"},
                 "text": {"en": "Cards for your tables, so guests can leave a review or return "
                                "their bottle.",
                          "pt": "Cartões para as mesas, para os clientes deixarem uma avaliação "
                                "ou devolverem a garrafa."}},
            ],
            "image": "assets/img/photos/crate-delivery-terrace.jpg",
            "alt": {
                "en": "A wooden crate full of tagged kombucha bottles, ready for delivery on a "
                      "sunny terrace",
                "pt": "Uma caixa de madeira cheia de garrafas de kombucha etiquetadas, pronta "
                      "para entrega num terraço soalheiro",
            },
        },
        "band": {
            "image": "assets/img/photos/bottles-on-ice.jpg",
            "alt": {
                "en": "Bottles of Real Health kombucha scattered over sparkling ice",
                "pt": "Garrafas de kombucha Real Health espalhadas sobre gelo cintilante",
            },
        },
        "partners": {
            "eyebrow": {"en": "Google reviews", "pt": "Avaliações no Google"},
            "heading": {"en": "What guests say", "pt": "O que dizem os clientes"},
            "pick": [0, 4, 5],  # quotes shown on this page (indexes into CONTENT["quotes"])
        },
        "cta": {
            "eyebrow": {"en": "Become a partner", "pt": "Torne-se parceiro"},
            "heading": {"en": "Let's put Real Health Kombucha on your menu",
                        "pt": "Vamos colocar a Real Health Kombucha no seu menu"},
            "lead": {
                "en": "Create your account and we'll get in touch about your first "
                      "delivery. Prefer to talk first? Message us on WhatsApp or send us an email.",
                "pt": "Crie a sua conta e entramos em contacto para combinar a "
                      "primeira entrega. Prefere falar primeiro? Envie-nos uma mensagem no WhatsApp "
                      "ou um email.",
            },
            "button": {"en": "Become a partner", "pt": "Torne-se parceiro"},
            "whatsapp": {"en": "WhatsApp", "pt": "WhatsApp"},
            "email": {"en": "Or email us at", "pt": "Ou envie-nos um email para"},
            "email_subject": {"en": "Kombucha for our restaurant",
                              "pt": "Kombucha para o nosso restaurante"},
            "image": "assets/img/photos/roel-nina-six-pack-coast.jpg",
            "alt": {
                "en": "Roel and Nina smiling behind a box of six kombucha bottles on the Madeira coast",
                "pt": "O Roel e a Nina a sorrir atrás de uma caixa com seis garrafas de kombucha, "
                      "na costa da Madeira",
            },
        },
    },
    # Flavours page (spec section 3). The per-flavour texts live in CONTENT["flavours"].
    "flavours_page": {
        "hero": {
            "eyebrow": {"en": "Our flavours", "pt": "Os nossos sabores"},
            "heading": {"en": "Six flavours,", "pt": "Seis sabores,"},
            "heading_accent": {"en": "two sizes", "pt": "dois tamanhos"},
            "lead": {
                "en": "Six flavours, two sizes, all brewed with pure water, green tea, raw cane sugar "
                      "and kombucha culture.",
                "pt": "Seis sabores, dois tamanhos, todos produzidos com água pura, chá verde, açúcar "
                      "de cana em bruto e cultura de kombucha.",
            },
            "image": "assets/img/photos/six-flavours-sunset-coast.jpg",
            "alt": {
                "en": "The six Real Health Kombucha bottles in a row on a table above the sea at sunset, "
                      "with ginger, oranges, limes and turmeric in front",
                "pt": "As seis garrafas de Real Health Kombucha em fila numa mesa sobre o mar ao pôr do sol, "
                      "com gengibre, laranjas, limas e curcuma à frente",
            },
        },
        # Badges (all flavours), spec section 3.
        "badges": [
            {"en": "Raw & unpasteurised", "pt": "Crua e não pasteurizada"},
            {"en": "Live cultures", "pt": "Culturas vivas"},
            {"en": "Naturally sparkling", "pt": "Naturalmente efervescente"},
            {"en": "Vegan", "pt": "Vegana"},
            {"en": "< 0.5% vol", "pt": "< 0,5% vol"},
        ],
        "list": {
            "eyebrow": {"en": "The range", "pt": "A gama"},
            "heading": {"en": "Find your", "pt": "Encontre o seu"},
            "heading_accent": {"en": "favourite", "pt": "favorito"},
        },
        "most_loved": {"en": "Most loved", "pt": "Um dos favoritos"},
        "flavoured_with": {"en": "Flavoured with:", "pt": "Aromatizado com:"},
        "base_label": {"en": "Base ingredients:", "pt": "Ingredientes base:"},
        "base_ingredients": {
            "en": "water, green tea (Camellia sinensis), raw cane sugar, kombucha culture (SCOBY)",
            "pt": "água, chá verde (Camellia sinensis), açúcar de cana em bruto, cultura de kombucha (SCOBY)",
        },
        # Sizes & prices (spec section 3). "{deposit}" = prices.deposit.
        "sizes": {
            "eyebrow": {"en": "Sizes & prices", "pt": "Tamanhos e preços"},
            "heading": {"en": "Two sizes,", "pt": "Dois tamanhos,"},
            "heading_accent": {"en": "every flavour", "pt": "todos os sabores"},
            "bottle_1l": {"en": "1 L bottle", "pt": "Garrafa de 1 L"},
            "bottle_1l_note": {"en": "For serving by the glass", "pt": "Para servir ao copo"},
            # Order page wording for the same bottle (home customers, not restaurants).
            "bottle_1l_note_order": {"en": "Great for sharing", "pt": "Ideal para partilhar"},
            "bottle_270": {"en": "270 ml bottle", "pt": "Garrafa de 270 ml"},
            "bottle_270_note": {"en": "+ {deposit} deposit, refunded when you return the bottle",
                                "pt": "+ {deposit} de depósito, reembolsado quando devolver a garrafa"},
            "image": "assets/img/photos/bottles-bougainvillea.jpg",
            "alt": {
                "en": "Two swing-top bottles of golden kombucha on palm leaves next to pink bougainvillea",
                "pt": "Duas garrafas de kombucha dourada com tampa mecânica sobre folhas de palmeira, "
                      "ao lado de buganvílias cor-de-rosa",
            },
            "order": {"en": "Order now", "pt": "Encomendar agora"},
            "restaurants": {"en": "For restaurants", "pt": "Para restaurantes"},
        },
    },
    # Order page (spec section 6).
    "order": {
        "hero": {
            "eyebrow": {"en": "Order", "pt": "Encomendar"},
            "heading": {"en": "Fresh kombucha,", "pt": "Kombucha fresca,"},
            "heading_accent": {"en": "delivered by us", "pt": "entregue por nós"},
            "lead": {
                "en": "For your home, your office or your café. Choose your flavours and sizes, "
                      "and Roel or Nina bring them to you.",
                "pt": "Para a sua casa, o seu escritório ou o seu café. Escolha os sabores e os "
                      "tamanhos, e o Roel ou a Nina entregam-lhe a encomenda em mão.",
            },
            "image": "assets/img/photos/bottle-in-hand-garden.jpg",
            "alt": {
                "en": "A hand holding up a bottle of golden kombucha in a sunny garden above the sea",
                "pt": "Uma mão a segurar uma garrafa de kombucha dourada num jardim soalheiro sobre o mar",
            },
        },
        "prices": {
            "eyebrow": {"en": "Prices", "pt": "Preços"},
            "heading": {"en": "Simple", "pt": "Preços"},
            "heading_accent": {"en": "prices", "pt": "simples"},
            "text": {
                "en": "Every flavour costs the same. Mix and match as you like.",
                "pt": "Todos os sabores têm o mesmo preço. Combine como quiser.",
            },
            "flavours_link": {"en": "See the six flavours", "pt": "Ver os seis sabores"},
        },
        "how": {
            "eyebrow": {"en": "How to order", "pt": "Como encomendar"},
            "heading": {"en": "Three ways", "pt": "Três formas"},
            "heading_accent": {"en": "to order", "pt": "de encomendar"},
            "app": {
                "title": {"en": "Order in our app", "pt": "Encomende na nossa app"},
                "text": {
                    "en": "Create an account in our app. We activate new accounts ourselves; "
                          "after that you can order anytime, straight from your phone.",
                    "pt": "Crie uma conta na nossa app. Somos nós que ativamos as contas novas; "
                          "depois disso pode encomendar quando quiser, diretamente no telemóvel.",
                },
                "button": {"en": "Create your account", "pt": "Criar conta"},
            },
            "whatsapp": {
                "title": {"en": "Message us on WhatsApp", "pt": "Escreva-nos no WhatsApp"},
                "text": {
                    "en": "Tell us which flavours and sizes you would like, and where to deliver.",
                    "pt": "Diga-nos que sabores e tamanhos quer, e onde devemos entregar.",
                },
                "button": {"en": "Open WhatsApp", "pt": "Abrir o WhatsApp"},
            },
            "email": {
                "title": {"en": "Send us an email", "pt": "Envie-nos um email"},
                "text": {
                    "en": "The button opens a ready-made email: just fill in your flavours, sizes "
                          "and delivery address.",
                    "pt": "O botão abre um email já preparado: basta indicar os sabores, os tamanhos "
                          "e a morada de entrega.",
                },
                "button": {"en": "Email your order", "pt": "Encomendar por email"},
            },
        },
        # Pre-filled email (order_mailto in src/orders.py).
        "email_subject": {"en": "Kombucha order", "pt": "Encomenda de kombucha"},
        "email_body": {
            "en": "Hello Roel and Nina,\n\nI would like to order:\n\n"
                  "Flavours:\nSizes (1 L / 270 ml) and quantities:\nDelivery address:\n\nThank you!",
            "pt": "Olá Roel e Nina,\n\nGostaria de encomendar:\n\n"
                  "Sabores:\nTamanhos (1 L / 270 ml) e quantidades:\nMorada de entrega:\n\nObrigado!",
        },
        # "{deposit}" = prices.deposit.
        "delivery": {
            "eyebrow": {"en": "Delivery & empties", "pt": "Entrega e garrafas vazias"},
            "heading": {"en": "We deliver", "pt": "Entregamos"},
            "heading_accent": {"en": "personally", "pt": "pessoalmente"},
            "items": [
                {"title": {"en": "Brought to you by us", "pt": "Entregue por nós, em mão"},
                 "text": {"en": "We brew in Ponta do Sol and deliver every order ourselves.",
                          "pt": "Produzimos na Ponta do Sol e entregamos nós próprios cada encomenda."}},
                {"title": {"en": "Bring back your empties", "pt": "Devolva as garrafas vazias"},
                 "text": {"en": "Give us your empty 270 ml bottles at the next delivery and we refund "
                                "the {deposit} deposit per bottle.",
                          "pt": "Entregue-nos as garrafas vazias de 270 ml na entrega seguinte e "
                                "reembolsamos o depósito de {deposit} por garrafa."}},
            ],
            "image": "assets/img/photos/crate-top-view.jpg",
            "alt": {
                "en": "A wooden crate full of kombucha bottles seen from above, ready for delivery",
                "pt": "Uma caixa de madeira cheia de garrafas de kombucha vista de cima, pronta para entrega",
            },
        },
        "review": {
            "eyebrow": {"en": "A thank-you", "pt": "Um agradecimento"},
            "heading": {"en": "Enjoyed it?", "pt": "Gostou?"},
        },
    },
    # Our story page (spec section 4; pitch slides 2-4). Step 4 says natural flavours are
    # added: never "juice"/"sumo" and never the flavouring brand. "UMH Pure Gold" as in slide 3.
    "story": {
        "hero": {
            "eyebrow": {"en": "Our story", "pt": "A nossa história"},
            "heading": {"en": "Meet", "pt": "Conheça o"},
            "heading_accent": {"en": "Roel & Nina", "pt": "Roel e a Nina"},
            "lead": {
                "en": "We are a couple living in Ponta do Sol, Madeira, who believe that what you "
                      "drink every day should make you feel good.",
                "pt": "Somos um casal que vive na Ponta do Sol, na Madeira, e acreditamos que aquilo "
                      "que bebemos todos os dias nos deve fazer sentir bem.",
            },
            "image": "assets/img/photos/roel-nina-balcony-bottles.jpg",
            "alt": {
                "en": "Roel and Nina smiling on a sunny balcony, each holding a bottle of kombucha",
                "pt": "O Roel e a Nina a sorrir numa varanda soalheira, cada um com uma garrafa de kombucha",
            },
        },
        "meet": {
            "eyebrow": {"en": "Two of us", "pt": "Nós os dois"},
            "heading": {"en": "From our kitchen", "pt": "Da nossa cozinha"},
            "heading_accent": {"en": "to your table", "pt": "para a sua mesa"},
            "paragraphs": [
                {"en": "What started as a home experiment in our kitchen grew into a small-batch "
                       "kombucha brewery.",
                 "pt": "O que começou como uma experiência caseira na nossa cozinha transformou-se "
                       "numa pequena produção artesanal de kombucha."},
                {"en": "Every bottle is still brewed, flavoured and bottled by the two of us, and "
                       "delivered personally.",
                 "pt": "Cada garrafa continua a ser produzida, aromatizada e engarrafada por nós os "
                       "dois, e entregue pessoalmente."},
            ],
            "portraits": [
                {"image": "assets/img/photos/nina-glass-stone-wall.jpg", "name": "Nina",
                 "alt": {"en": "Nina smiling with a glass of kombucha in front of a stone wall",
                         "pt": "A Nina a sorrir com um copo de kombucha junto a um muro de pedra"}},
                {"image": "assets/img/photos/roel-drinking-fig-tree.jpg", "name": "Roel",
                 "alt": {"en": "Roel drinking a glass of kombucha under a fig tree",
                         "pt": "O Roel a beber um copo de kombucha debaixo de uma figueira"}},
            ],
        },
        # Slide 3, three parts.
        "water": {
            "eyebrow": {"en": "Where it began", "pt": "Onde tudo começou"},
            "heading": {"en": "It all started", "pt": "Tudo começou"},
            "heading_accent": {"en": "with our water", "pt": "com a nossa água"},
            "items": [
                {"title": {"en": "We changed our drinking water", "pt": "Mudámos a nossa água"},
                 "text": {"en": "We installed a drinking-water filter at home, with a UMH Pure Gold "
                                "fitted after the last filter stage: a gold-plated device with a "
                                "rock crystal inside. No power, no magnets.",
                          "pt": "Instalámos um filtro de água em casa, com um UMH Pure Gold "
                                "colocado depois da última etapa de filtragem: um dispositivo "
                                "banhado a ouro com um cristal de rocha no interior. Sem "
                                "eletricidade, sem ímanes."}},
                {"title": {"en": "We tasted the difference", "pt": "Sentimos a diferença"},
                 "text": {"en": "Softer, cleaner and fresher. Our tea, coffee and everything we "
                                "made with it tasted better.",
                          "pt": "Mais suave, mais limpa e mais fresca. O nosso chá, o café e tudo "
                                "o que fazíamos com ela ficou com melhor sabor."}},
                {"title": {"en": "Then came kombucha", "pt": "Depois veio a kombucha"},
                 "text": {"en": "Kombucha is more than 95% water, so great water makes great "
                                "kombucha. Friends kept asking for bottles, and Real Health "
                                "Kombucha was born.",
                          "pt": "A kombucha tem mais de 95% de água, por isso uma boa água faz uma "
                                "boa kombucha. Os amigos não paravam de nos pedir garrafas, e "
                                "assim nasceu a Real Health Kombucha."}},
            ],
        },
        # Slide 4, the four steps.
        "process": {
            "eyebrow": {"en": "How we make it", "pt": "Como a fazemos"},
            "heading": {"en": "From pure water", "pt": "Da água pura"},
            "heading_accent": {"en": "to living drink", "pt": "à bebida viva"},
            "steps": [
                {"title": {"en": "Pure water", "pt": "Água pura"},
                 "text": {"en": "Filtered drinking water, passed through our UMH Pure Gold device.",
                          "pt": "Água potável filtrada, que passa pelo nosso dispositivo UMH Pure Gold."}},
                {"title": {"en": "Green tea brew", "pt": "Infusão de chá verde"},
                 "text": {"en": "Green tea (Camellia sinensis) steeped and sweetened with raw cane sugar.",
                          "pt": "Chá verde (Camellia sinensis) em infusão, adoçado com açúcar de cana "
                                "em bruto."}},
                {"title": {"en": "Fermentation", "pt": "Fermentação"},
                 "text": {"en": "The SCOBY culture ferments the tea in glass jars and eats most of the sugar.",
                          "pt": "A cultura SCOBY fermenta o chá em frascos de vidro e consome a maior "
                                "parte do açúcar."}},
                {"title": {"en": "Flavour & bottle", "pt": "Aroma e engarrafamento"},
                 "text": {"en": "Natural flavours are added, then a second fermentation in the bottle "
                                "makes it naturally sparkling.",
                          "pt": "Juntamos aromas naturais e uma segunda fermentação na garrafa "
                                "torna-a naturalmente efervescente."}},
            ],
        },
        # Slide 2, the four facts.
        "place": {
            "eyebrow": {"en": "Ponta do Sol, Madeira", "pt": "Ponta do Sol, Madeira"},
            "heading": {"en": "Made on the island,", "pt": "Feita na ilha,"},
            "heading_accent": {"en": "by hand", "pt": "à mão"},
            "items": [
                {"title": {"en": "Brewed locally", "pt": "Produzida localmente"},
                 "text": {"en": "Brewed on the island, in Ponta do Sol.",
                          "pt": "Produzida na ilha, na Ponta do Sol."}},
                {"title": {"en": "Small batches, by hand", "pt": "Pequenos lotes, à mão"},
                 "text": {"en": "Brewed and bottled by Roel & Nina.",
                          "pt": "Produzida e engarrafada pelo Roel e pela Nina."}},
                {"title": {"en": "Delivered personally", "pt": "Entregue pessoalmente"},
                 "text": {"en": "We bring it, and collect your empties.",
                          "pt": "Somos nós que a levamos, e recolhemos as garrafas vazias."}},
            ],
            "image": "assets/img/photos/ponta-do-sol-kombucha-sea-v2.jpg",
            "alt": {
                "en": "A bottle and glasses of golden kombucha on a dark rock by the sea, looking across "
                      "the bay to the village of Ponta do Sol and the cliff with the Estalagem on top",
                "pt": "Uma garrafa e copos de kombucha dourada numa rocha escura junto ao mar, com vista "
                      "sobre a baía para a vila da Ponta do Sol e a falésia com a Estalagem no topo",
            },
            "flavours": {"en": "Discover our flavours", "pt": "Conheça os nossos sabores"},
            "order": {"en": "Order", "pt": "Encomendar"},
        },
    },
    # Gut health page (spec section 5; slide 5). Wording only as in the spec; footnote = ui.health_note.
    "gut_health": {
        "hero": {
            "eyebrow": {"en": "Gut health", "pt": "Saúde intestinal"},
            "heading": {"en": "Fermented tea,", "pt": "Chá fermentado,"},
            "heading_accent": {"en": "full of life", "pt": "cheio de vida"},
            "lead": {
                "en": "Kombucha is fermented tea: raw, unpasteurised and full of live cultures.",
                "pt": "A kombucha é chá fermentado: crua, não pasteurizada e cheia de culturas vivas.",
            },
            "image": "assets/img/photos/gut-health-fermentation-jar.jpg",
            "alt": {
                "en": "A glass jar of brewing kombucha with its live culture on top, next to a glass of "
                      "sparkling kombucha, ginger, green tea, lemon and mint",
                "pt": "Um frasco de vidro com kombucha a fermentar e a sua cultura viva por cima, ao lado "
                      "de um copo de kombucha efervescente, gengibre, chá verde, limão e hortelã",
            },
        },
        "benefits": {
            "eyebrow": {"en": "Why it feels good", "pt": "Porque faz bem"},
            "heading": {"en": "Six reasons", "pt": "Seis razões"},
            "heading_accent": {"en": "to drink it", "pt": "para a beber"},
            "items": [
                {"title": {"en": "Live cultures", "pt": "Culturas vivas"},
                 "text": {"en": "Raw and unpasteurised, full of the living bacteria and yeasts from "
                                "fermentation.",
                          "pt": "Crua e não pasteurizada, cheia das bactérias e leveduras vivas da "
                                "fermentação."}},
                {"title": {"en": "Antioxidants", "pt": "Antioxidantes"},
                 "text": {"en": "Green tea polyphenols, which research links to protection against "
                                "cell damage.",
                          "pt": "Polifenóis do chá verde, que a investigação associa à proteção "
                                "contra os danos celulares."}},
                {"title": {"en": "Gut friendly", "pt": "Amiga do intestino"},
                 "text": {"en": "Studies associate fermented drinks with a more diverse gut flora.",
                          "pt": "Os estudos associam as bebidas fermentadas a uma flora intestinal "
                                "mais diversificada."}},
                {"title": {"en": "Less sugar", "pt": "Menos açúcar"},
                 "text": {"en": "Most of the sugar is consumed during fermentation. A lighter "
                                "alternative to soft drinks.",
                          "pt": "A maior parte do açúcar é consumida durante a fermentação. Uma "
                                "alternativa mais leve aos refrigerantes."}},
                {"title": {"en": "Alcohol-free choice", "pt": "Opção sem álcool"},
                 "text": {"en": "Naturally below 0.5% vol, an adult drink for when you skip "
                                "alcohol.",
                          "pt": "Naturalmente abaixo de 0,5% vol, uma bebida adulta para quando "
                                "não quer álcool."}},
                {"title": {"en": "Clean & vegan", "pt": "Simples e vegana"},
                 "text": {"en": "Only water, green tea, cane sugar, kombucha culture and natural "
                                "flavours.",
                          "pt": "Apenas água, chá verde, açúcar de cana, cultura de kombucha e "
                                "aromas naturais."}},
            ],
        },
        "cta": {
            "eyebrow": {"en": "Taste it", "pt": "Prove"},
            "heading": {"en": "Find your", "pt": "Encontre o seu"},
            "heading_accent": {"en": "favourite", "pt": "favorito"},
            "text": {"en": "Six flavours, brewed in small batches and delivered by us personally.",
                     "pt": "Seis sabores, produzidos em pequenos lotes e entregues pessoalmente por nós."},
            "flavours": {"en": "See the flavours", "pt": "Ver os sabores"},
            "order": {"en": "Order", "pt": "Encomendar"},
        },
    },
    # Contact page (spec section 7). No form and no opening hours.
    "contact_page": {
        "hero": {
            "eyebrow": {"en": "Contact", "pt": "Contacto"},
            "heading": {"en": "Say", "pt": "Diga"},
            "heading_accent": {"en": "hello", "pt": "olá"},
            "lead": {
                "en": "Questions, an order, or a tasting for your restaurant? Message us the way "
                      "you like best and we'll get back to you.",
                "pt": "Dúvidas, uma encomenda ou uma prova para o seu restaurante? Fale connosco "
                      "como preferir e respondemos assim que possível.",
            },
            "image": "assets/img/photos/crate-delivery-terrace.jpg",
            "alt": {
                "en": "A wooden crate of kombucha bottles on a sunny terrace, with greenery behind",
                "pt": "Uma caixa de madeira com garrafas de kombucha num terraço soalheiro, com vegetação ao fundo",
            },
        },
        "ways": {
            "eyebrow": {"en": "Get in touch", "pt": "Fale connosco"},
            "heading": {"en": "Message us,", "pt": "Escreva-nos,"},
            # U+2011 (non-breaking hyphen): "visite-nos" never breaks at the hyphen.
            "heading_accent": {"en": "call or visit", "pt": "ligue ou visite\u2011nos"},
            "whatsapp": {
                "title": {"en": "WhatsApp", "pt": "WhatsApp"},
                "text": {"en": "The quickest way to reach us: message us directly.",
                         "pt": "A forma mais rápida de nos contactar: escreva-nos diretamente."},
                "button": {"en": "Open WhatsApp", "pt": "Abrir o WhatsApp"},
                "group": {"en": "WhatsApp group: news & new batches",
                          "pt": "Grupo WhatsApp: novidades e novos lotes"},
            },
            "instagram": {
                "title": {"en": "Instagram", "pt": "Instagram"},
                "text": {"en": "Follow us for news, new flavours and life in Ponta do Sol.",
                         "pt": "Siga-nos para novidades, novos sabores e a vida na Ponta do Sol."},
                "button": {"en": "Follow us", "pt": "Seguir-nos"},
            },
            "email": {
                "title": {"en": "Email", "pt": "Email"},
                "text": {"en": "For anything longer, write to us.",
                         "pt": "Para algo mais longo, escreva-nos."},
                "button": {"en": "Send an email", "pt": "Enviar email"},
            },
            "phone": {"en": "Phone", "pt": "Telefone"},
            "address": {"en": "Address", "pt": "Morada"},
            "maps": {"en": "Open in Google Maps", "pt": "Abrir no Google Maps"},
        },
    },
    # Shared interface labels.
    "ui": {
        "health_note": {
            "en": "Based on published research on kombucha and fermented foods. Not a medical claim.",
            "pt": "Com base em investigação publicada sobre kombucha e alimentos fermentados. "
                  "Não é uma alegação médica.",
        },
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
