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

    # ------------------------------------------------------------------ shared
    # Testimonials (Home, About and Gut Health 101). Images in assets/img/.
    "testimonials": [
        {
            "title": "“absolutely delicious!!”",
            "quote": (
                "“Real Health Kombucha has been the only Kombucha that I actually feel gives me life and has "
                "all the possible healing benefits. On top of that it tastes absolutely delicious!! It’s become "
                "a staple in our household. I highly recommend it!”"
            ),
            "name": "Dara",
            "image": "testimonial-dara.jpg",
        },
        {
            "title": "“Your Kombucha is amazing”",
            "quote": (
                "“Your Kombucha is amazing. I am drinking it now, we are your loyal customers. None of the "
                "supermarket Kombucha taste like yours.”"
            ),
            "name": "Magda",
            "image": "testimonial-magda.jpg",
        },
        {
            "title": "“my favorite drink in the world”",
            "quote": (
                "“It is my favorite drink in the world but only when I buy it from Roel and Nina because "
                "it’s got unique flavors. I highly recommend it to anybody who wants a healthy and tasty "
                "homemade drink.”"
            ),
            "name": "Sylvia",
            "image": "testimonial-sylvia.jpg",
        },
    ],
    "testimonials_title": "What Our Customers Say",
    # ------------------------------------------------------------------ home
    "home": {
        "hero_title": "Delicious and Nutritious",
        "hero_text": (
            "At Real Health Kombucha, we're revolutionizing Madeira's beverage market with pure, organic, and "
            "delicious Kombucha. Our mission? To promote gut health and overall well-being by offering a healthy, "
            "tasty alternative to sugary, artificial drinks. Join us in embracing a healthier lifestyle, one sip at a time."
        ),
        "hero_image": "home-hero.jpg",
        "benefits_title": "Benefits",
        # icon = name in partials/page-icons.html.j2
        "benefits": [
            {"icon": "hand", "title": "Handmade", "text": (
                "Our kombucha is carefully handcrafted in small batches, ensuring the highest quality in every "
                "bottle. Each sip reflects our commitment to artisanal brewing, with attention to detail in every "
                "step of the process.")},
            {"icon": "infinity", "title": "Living Culture", "text": (
                "Real Health Kombucha is alive with beneficial probiotics, thanks to our authentic fermentation "
                "process. These living cultures support your gut health, bringing vitality and balance to your "
                "digestive system.")},
            {"icon": "run", "title": "Energizing", "text": (
                "Packed with natural B vitamins, our kombucha provides a gentle yet powerful energy boost to keep "
                "you feeling refreshed and revitalized throughout the day. Say goodbye to the afternoon slump and "
                "hello to sustained, natural energy.")},
            {"icon": "lotus", "title": "Bio & Vegan", "text": (
                "Made from 100% organic ingredients, our kombucha is both bio and vegan-friendly, offering a clean, "
                "pure beverage option for health-conscious individuals. We believe in nourishing your body with the "
                "best that nature has to offer.")},
            {"icon": "heart", "title": "Healthy", "text": (
                "Our kombucha is more than just a drink – it’s a health tonic packed with antioxidants, "
                "probiotics, and essential nutrients that promote overall well-being. Enjoy a delicious way to "
                "support your body’s natural defenses and maintain a healthy lifestyle.")},
            {"icon": "drop", "title": "Spring Water", "text": (
                "We brew our kombucha using pure, crystal-clear spring water, enhancing the natural flavors and "
                "health benefits of each bottle. This pristine water source ensures a clean, refreshing taste that "
                "hydrates and nourishes your body.")},
        ],
        "taste_title": "Taste the difference",
        "taste_text": (
            "Our premium kombucha products are designed to offer a nutritious alternative to the synthetic, "
            "sugar-laden drinks that currently dominate the market. Join us on our mission to promote a healthier "
            "lifestyle through accessible, delicious, and sustainable beverage choices."
        ),
        "taste_image": "scoby-jar.jpg",
        "flavours_title": "Explore our Flavours",
        "flavours_text": (
            "Experience a world of flavors with our diverse Kombucha selection. Enjoy the perfect harmony of taste "
            "and health in every bottle."
        ),
        # light = white title text (dark photo)
        "flavours": [
            {"name": "Metabolic Power", "image": "flavour-metabolic-power.jpg", "light": False},
            {"name": "Green Mandarine", "image": "flavour-green-mandarine.jpg", "light": True},
            {"name": "Wild Orange", "image": "flavour-wild-orange.jpg", "light": True},
            {"name": "Lemon", "image": "flavour-lemon.jpg", "light": False},
            {"name": "Ginger", "image": "flavour-ginger.jpg", "light": False},
        ],
        "magic_title": "Experience the Kombucha Magic",
        # focus: CSS object-position of the image (as on the live site; default centre).
        # phone_order: the live site shows these in a different order on phones.
        "magic": [
            {"title": "Pure Source", "image": "magic-pure-source.jpg", "phone_order": 1, "text": (
                "We believe in the power of authenticity and health. Our kombucha is crafted with the purest, natural "
                "spring water sourced from the pristine springs of Madeira Island. This life-giving water, rich in "
                "essential minerals, forms the foundation of our refreshing and delicious beverage. By using such "
                "high-quality water from Madeira, we ensure that every sip of our kombucha nourishes your body and "
                "supports your overall well-being.")},
            {"title": "Natural Wellness", "image": "magic-natural-wellness.jpg", "phone_order": 2, "text": (
                "Our kombucha is packed with probiotics and nutrients, promoting better digestion and overall "
                "wellness. It is crafted without any artificial flavors, colors, or sweeteners. We take pride in "
                "offering a product that is wholesome and true to its natural roots.")},
            {"title": "Authentic", "image": "magic-authentic.jpg", "focus": "73.6% 56.5%", "phone_order": 4, "text": (
                "Our kombucha is a reflection of our genuine love and dedication to this craft. We stay true to "
                "traditional brewing methods, ensuring each batch retains the authentic flavors and health benefits "
                "that kombucha is known for.")},
            {"title": "Local Product", "image": "magic-local-product.jpg", "focus": "17.6% 53.9%", "phone_order": 3, "text": (
                "Crafted with love in Madeira, our kombucha supports local farmers and the community. By choosing "
                "Real Health Kombucha, you’re contributing to the local economy and enjoying a product made with "
                "fresh, locally sourced ingredients.")},
        ],
        "faq_title": "frequently asked questions",
        # Answers 2-5 are collapsed on the live site; text taken from its page bundle.
        "faq": [
            {"q": "What is Kombucha?", "a": (
                "Kombucha is a fermented tea beverage made by fermenting sweetened tea with a symbiotic culture of "
                "bacteria and yeast (SCOBY). The fermentation process produces probiotics, enzymes, and organic "
                "acids, which contribute to its unique flavor and health benefits.")},
            {"q": "What are the health benefits of drinking Kombucha?", "a": (
                "Kombucha is known for containing probiotics, which can support gut health. It also provides "
                "antioxidants, vitamins (like B vitamins), and may aid digestion, boost immunity, and increase energy "
                "levels. However, it's important to note that individual results may vary, and more research is ongoing.")},
            {"q": "Is Kombucha safe for everyone?", "a": (
                "Kombucha is generally safe for most people, but those with compromised immune systems, pregnant or "
                "breastfeeding women, and individuals sensitive to caffeine or alcohol should consult with a "
                "healthcare provider before drinking it. Due to the fermentation process, Kombucha contains a small "
                "amount of alcohol (usually less than 0.5%).")},
            {"q": "How should I store Kombucha, and how long does it last?", "a": (
                "Kombucha should be refrigerated to slow the fermentation process and maintain freshness. It can "
                "typically last 3-6 months when stored properly. However, even after this period, the drink may "
                "become more acidic but is usually still safe to consume.")},
            {"q": "Can Kombucha go bad? How do I know if it’s spoiled?", "a": (
                "While Kombucha continues to ferment over time, it rarely spoils. Signs of spoilage include mold "
                "growth, off smells (like vinegar or rotten eggs), or an unusually sharp taste. If any of these signs "
                "are present, it’s best to discard the bottle.")},
        ],
    },
    # ------------------------------------------------------------------ about
    "about": {
        "hero_title": "Real Health Kombucha",
        "hero_text": (
            "Welcome to Real Health Kombucha, a small brewery dedicated to crafting premium kombucha on the "
            "beautiful island of Madeira."
        ),
        "hero_image": "about-hero.jpg",
        "hero_image_focus": "center top",
        "mission_title": "Our Mission",
        "mission_text": (
            "At Real Health Kombucha, our mission is to lovingly craft a positive health transformation on Madeira "
            "Island. We use only the purest ingredients and natural spring water to create our nutritious, natural "
            "kombucha. By offering a healthier alternative to sugar-laden drinks, we aim to inspire a wellness "
            "lifestyle and contribute to the well-being of Madeira's community. Together, we can make Madeira "
            "healthier and happier, one sip at a time."
        ),
        "mission_image": "about-mission.jpg",
        "stats": [
            {"number": "5", "label": "Flavours"},
            {"number": "2022", "label": "Founded"},
            {"number": "10", "label": "Years experience"},
            {"number": "100%", "label": "Satisfied Customers"},
        ],
        "story_title": "Our Story",
        "story_paragraphs": [
            "Real Health Kombucha began with a shared love for this fermented tea. Nina discovered kombucha in 2002 "
            "while living in New Mexico, where a neighbor introduced her to its benefits after yoga sessions.",
            "The good energy from kombucha inspired Nina and her husband to start brewing their own in 2014. When "
            "they moved to Madeira and couldn't find quality kombucha, they decided to share their homemade brew "
            "with friends.",
            "The positive feedback encouraged them to bring Real Health Kombucha to the island, aiming to provide a "
            "delicious and healthy alternative to sugary supermarket options.",
        ],
        "story_image": "scoby-jar.jpg",
        "story_button": "Real Health Kombucha Shop",
        "values_title": "Our Values",
        "values_text": (
            "Our kombucha is non-artificial, high quality, natural, and authentic, ensuring it is beneficial to the "
            "body. These values guide every step of our brewing process, from selecting ingredients to the final product."
        ),
        "values": [
            {"title": "Real & Healthy", "image": "home-hero.jpg", "text": (
                "We believe in the power of authenticity and health. Our kombucha is made with real, natural "
                "ingredients that promote overall well-being, providing you with a beverage that is as beneficial "
                "as it is delicious.")},
            {"title": "non - Artificial", "image": "values-non-artificial.jpg", "focus": "52.2% 0%", "text": (
                "Our kombucha is crafted without any artificial flavors, colors, or sweeteners. We take pride in "
                "offering a product that is wholesome and true to its natural roots, delivering a pure taste in "
                "every sip.")},
            {"title": "Authentic", "image": "values-authentic.jpg", "text": (
                "Our kombucha is a reflection of our genuine love and dedication to this craft. We stay true to "
                "traditional brewing methods, ensuring each batch retains the authentic flavors and health benefits "
                "that kombucha is known for.")},
        ],
        "place_title": "Made in Ponta do Sol",
        "place_text": (
            "Nestled in the scenic island of Madeira, Real Health Kombucha is a local gem committed to enhancing the "
            "health and well-being of our community. Come visit us and experience the unique taste of our "
            "handcrafted kombucha, made with love and the finest natural ingredients."
        ),
        "place_image": "ponta-do-sol.jpg",
    },
    # ------------------------------------------------------------------ gut health 101
    "gut_health": {
        "hero_title": "Gut Health 101",
        "hero_subtitle": "Build a healthy gut with Kombucha every Day",
        "hero_text": "Dive into the world of kombucha and discover the many ways it can benefit your health.",
        "hero_image": "gut-health-hero.jpg",
        "benefits_title": "Health Benefits of Real Health Kombucha",
        "benefits_text": (
            "By incorporating Real Health Kombucha into your daily routine, you can experience these health benefits "
            "firsthand. Our kombucha is crafted with love and the highest quality ingredients to ensure you receive "
            "the best possible product. Cheers to a healthier, happier you!"
        ),
        "benefits": [
            {"icon": "flower", "title": "Detoxification", "subtitle": "Cleanse Your Body Naturally", "text": (
                "Kombucha is packed with antioxidants and enzymes that may aid in the body’s natural "
                "detoxification process. By helping to remove harmful toxins, kombucha supports your liver and "
                "promotes overall health.")},
            {"icon": "lightning", "title": "Increased Energy", "subtitle": "Boost Your Energy and Mood", "text": (
                "Our kombucha contains B vitamins, known for their role in enhancing energy levels and improving "
                "mood. Enjoy a natural energy boost without the crash that often comes with sugary drinks or caffeine.")},
            {"icon": "run-duotone", "title": "Joint Health", "subtitle": "Support Your Joints", "text": (
                "Kombucha contains glucosamine, which supports joint health and can help reduce joint pain. This "
                "makes it a great addition to your diet if you are looking to maintain healthy and flexible joints.")},
            {"icon": "orange", "title": "Antioxidants", "subtitle": "Fight Oxidative Stress", "text": (
                "Rich in antioxidants, kombucha combats oxidative stress by reducing cell damage caused by free "
                "radicals. Regular consumption can help protect your cells and support overall longevity.")},
            {"icon": "plant", "title": "Probiotics", "subtitle": "Promote a Healthy Gut", "text": (
                "Kombucha is a fermented drink made using bacteria and yeast, resulting in a beverage rich in "
                "probiotics. These beneficial bacteria help maintain a healthy gut flora, essential for good "
                "digestion and overall health.")},
            {"icon": "intersect", "title": "Improved Digestion", "subtitle": "Aid Digestion and Nutrient Absorption", "text": (
                "The probiotics in kombucha not only promote a healthy gut but also aid in better digestion and "
                "nutrient absorption. This can help reduce issues like bloating and indigestion, making you feel "
                "more comfortable and energized.")},
            {"icon": "person", "title": "Immune Support", "subtitle": "Strengthen Your Immune System", "text": (
                "Probiotics found in kombucha support a healthy immune system by enhancing the body’s natural "
                "defenses. Regular consumption may help your body fight off infections and illnesses more effectively.")},
        ],
        "why_title": "WHY GUT HEALTH MATTERS",
        "why_text": (
            "Maintaining a healthy gut is crucial for overall health.  A well-functioning digestive system ensures "
            "that your body absorbs nutrients efficiently, supports your immune system, and contributes to your "
            "overall well-being. At Real Health Kombucha, we are dedicated to providing a beverage that not only "
            "tastes great but also supports your health goals."
        ),
    },
    # Button labels used on several pages.
    "btn_shop_now": "Shop Now",
    "btn_explore_story": "Explore our Story",
    "btn_discover_story": "Discover our Story",

    # ------------------------------------------------------------------ ordering
    # Ordering happens in the orders app. Its signup screen serves private customers and
    # restaurants; a new account is reviewed by us before the first order.
    "orders_app_signup_url": "https://roel-heremans.github.io/kombucha-orders-app/?signup",
    # Pre-filled order e-mails (see src/orders.py) go to this address.
    "order_email": "realhealthkombucha@gmail.com",
    # Prices in whole euros. A price edit here updates the card and the e-mail total.
    "packages_bottle": [
        {"bottles": 2, "price": 20, "deposit": 4},
        {"bottles": 4, "price": 36, "deposit": 8},
        {"bottles": 8, "price": 65, "deposit": 16},
    ],
    "packages_subscription": [
        {"name": "Single", "bottles_per_week": 2, "price_per_month": 72},
        {"name": "Couple", "bottles_per_week": 4, "price_per_month": 128},
        {"name": "Family", "bottles_per_week": 8, "price_per_month": 240},
    ],
    "order_button_label": "Create account to order",
    "order_email_label": "or order by email",
    "order_note": "New accounts are reviewed by us before your first order.",
    "partner_button_label": "Create partner account",
    "partner_email_label": "or email us",
    "partner_email_subject": "Partner enquiry: Real Health Kombucha",
    "partner_email_body": [
        "Dear Kombucha Team,", "",
        "We would like to become a partner.", "",
        "Our business (name, type, location):", "",
        "Best Regards,",
    ],
    # ------------------------------------------------------------------ shop
    "shop": {
        "hero_title": "REAL HEALTH SHOP",
        "hero_text": (
            "At Real Health Kombucha, we offer a variety of package options to suit your needs. Whether you are a "
            "new customer looking to try our kombucha or a loyal fan stocking up, we have the perfect package for you."
        ),
        "hero_image": "magic-authentic.jpg",
        "hero_image_focus": "center top",
        # Hero "tab" buttons jump to the two sections below (both always visible).
        "tab_bottle": "Buy per Bottle",
        "tab_subscription": "Subscription",
        "bottle_title": "Buy per Bottle",
        "bottle_text": (
            "Choose from our set of 2, 4, or 8 bottles and enjoy the delicious benefits of our premium kombucha. "
            "Ideal for those new to kombucha or looking to sample different flavors. This set allows you to "
            "experience the health benefits of our kombucha without committing to a larger quantity."
        ),
        "bottle_points": ["Delivery to Funchal", "Perfect for Tourists", "Choose your Flavours"],
        "subscription_title": "Subscription",
        "subscription_text": (
            "Enjoy regular deliveries of your favorite kombucha and save with our subscription plans."
        ),
        "subscription_points": [
            "Regular deliveries to your doorstep.",
            "Enjoy discounts on all subscription plans.",
            "Maintain a consistent supply of your favorite health-boosting kombucha.",
            "Free Home Delivery (Calheta - PdS - Rib. Brava - Funchal - Canico)",
        ],
    },
    # ------------------------------------------------------------------ reseller
    "reseller": {
        "hero_title": "Partner with Real Health Kombucha",
        "hero_kicker": "FOR RESTAURANTS & HOTELS",
        "hero_text": (
            "Our goal is to help you elevate your beverage offerings with a healthy, delicious, and locally crafted "
            "alternative that your guests will love."
        ),
        "hero_image": "about-hero.jpg",
        "hero_image_focus": "center top",
        # Scrolling logo band (files in assets/img/).
        "partners": [
            {"name": "Ponta do Sol Sun Spot Cafe", "image": "partner-ponta-do-sol.svg"},
            {"name": "Jin Garden", "image": "partner-jin-garden.png"},
            {"name": "Mundo Vegan", "image": "partner-mundo-vegan.png"},
        ],
        # icon = name in partials/page-icons.html.j2
        "features": [
            {"icon": "tablet", "title": "Enhance Your menu", "text": (
                "Stand out by offering a unique, health-focused beverage that caters to the growing demand for "
                "nutritious options.")},
            {"icon": "tulip", "title": "Health Benefits", "text": (
                "Attract health-conscious customers who seek quality and natural ingredients in their drinks.")},
            {"icon": "hand-heart", "title": "Promote", "text": (
                "By serving kombucha, you contribute to your guests' health, enhancing their dining or stay experience.")},
            {"icon": "globe", "title": "Eco Friendly", "text": (
                "We are committed to sustainable practices, using eco-friendly packaging and locally sourced ingredients.")},
            {"icon": "note-pencil", "title": "Tailored to Your Needs", "text": (
                "We offer flexible packages to suit your establishment’s size and needs, ensuring you have the right "
                "amount of stock at all times.")},
            {"icon": "van", "title": "Fast Delivery", "text": (
                "Our kombucha is brewed right here in Madeira, helping you support local businesses and the community.")},
        ],
        "become_title": "Become a Partner",
        "become_text": (
            "Getting started with Real Health Kombucha is easy and seamless. Once you’re ready, we’ll create a "
            "customized supply plan tailored to your establishment’s requirements."
        ),
        "become_image": "become-partner.jpg",
        "steps": [
            {"icon": "number-1", "title": "Contact Us", "text": (
                "Reach out to us through our contact form or call us directly to discuss your needs.")},
            {"icon": "number-2", "title": "Sample Package", "text": (
                "We offer a sample package so you can experience the quality and taste of our kombucha firsthand.")},
            {"icon": "number-3", "title": "Tailored Solutions", "text": (
                "We create a customized supply plan that fits your establishment’s requirements.")},
        ],
    },
}

# The Reseller page repeats About's Mission / stats / Values / "Made in Ponta do Sol"
# sections. As on the live site it uses another mission photo, capitalises
# "Non - Artificial" and shows a different "Authentic" photo; all text is shared.
_about_values = CONTENT["about"]["values"]
CONTENT["reseller"]["about_sections"] = {
    **CONTENT["about"],
    "mission_image": "reseller-mission.jpg",
    "values": [
        _about_values[0],
        {**_about_values[1], "title": "Non - Artificial", "focus": None},
        {**_about_values[2], "image": "magic-authentic.jpg", "focus": "75.3% 54.6%"},
    ],
}
