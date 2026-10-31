import re

import html as htmllib


class _Main:
    def __init__(self, path):
        html = path.read_text(encoding="utf-8")
        main = html[html.index("<main>"):html.index("</main>")]
        text = re.sub(r"<[^>]+>", " ", main)
        self.flat = re.sub(r"\s+", " ", htmllib.unescape(text))


def main_of(path):
    return _Main(path)


def _form(path):
    html = (path / "contact" / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<form\b[^>]*>", html)
    assert m, "no form"
    return m.group(0), html


def test_contact_details(built):
    p = main_of(built / "contact" / "index.html")
    for s in ["Contact Us", "We are looking forward hearing from you.", "Call Us:", "+351 913 000 048",
              "Hours:", "Mon-Fri: 11am - 8pm Sat, Sun: 9am - 10pm", "Our Location:",
              "Caminho do Jangão 154, 9360-523 Ponta do Sol", "Name", "Email", "Message", "Submit"]:
        assert s in p.flat, s


def test_preview_form_has_no_action(built):
    tag, html = _form(built)
    assert "action" not in tag
    assert 'data-preview="true"' in tag
    assert 'aria-live="polite"' in html
    assert "Preview — message not sent" in html


def test_live_form_posts(built_preview_off):
    tag, html = _form(built_preview_off)
    assert 'action="contact.php"' in tag and 'method="post"' in tag
    assert "data-preview" not in tag
    assert 'name="website"' in html and 'aria-hidden="true"' in html
    for n in ("name", "email", "message"):
        assert f'name="{n}"' in html
