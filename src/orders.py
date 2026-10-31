"""Order links: the pre-filled order email used on the Order page."""
import urllib.parse

from content import CONTENT


def order_mailto(lang, content=None):
    """mailto: link to the order address with the subject and body in `lang`.

    `content` defaults to CONTENT; build() binds it to the content it was given.

    Subject and body are percent-encoded with quote(safe="") (spaces as %20, newlines as %0A),
    so mail clients show them as written. Render it in templates with `| e` (escapes the &).
    """
    content = CONTENT if content is None else content
    order = content["order"]
    subject = urllib.parse.quote(order["email_subject"][lang], safe="")
    body = urllib.parse.quote(order["email_body"][lang], safe="")
    return f"mailto:{content['links']['email']}?subject={subject}&body={body}"
