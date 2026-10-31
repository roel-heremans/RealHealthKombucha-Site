"""
Pre-filled order e-mails (mailto: links) for the Shop and Reseller pages.

Subject and body are percent-encoded with urllib.parse.quote(safe="") so "€",
"/", spaces and line breaks survive every mail client. In templates, output the
result with `| e` so the "&" before "body=" becomes "&amp;" in the HTML.
"""
from typing import Iterable, Literal
from urllib.parse import quote


def mailto(email: str, subject: str, body_lines: Iterable[str] = ()) -> str:
    href = f"mailto:{email}?subject={quote(subject, safe='')}"
    body = "\r\n".join(body_lines)
    if body:
        href += f"&body={quote(body, safe='')}"
    return href


def mailto_for(package: dict, kind: Literal["bottle", "subscription"], email: str) -> str:
    if kind == "bottle":
        n = package["bottles"]
        total = package["price"] + package["deposit"]
        subject = f"Kombucha Order: buy per bottle ({n} bottles)"
        lines = [
            "Dear Kombucha Team,", "",
            f"I want to order the {n} Bottles - buy per bottle package.", "",
            "I want to order the following flavors:", "",
            "Please let me know when the next delivery to Funchal is happening.", "",
            f"I will bring the €{total} (incl. deposit) to the delivery.", "",
            "Best Regards,",
        ]
    elif kind == "subscription":
        n = package["bottles_per_week"]
        subject = f"Kombucha Order: subscription ({n} bottles/week)"
        lines = [
            "Dear Kombucha Team,", "",
            f"I want to order the {n} Bottles per week - subscription package.", "",
            "I want to order the following flavors:", "",
            "My address for delivery is:", "",
            f"I will pay {package['price_per_month']}€ for the month on the first delivery.", "",
            "Best Regards,",
        ]
    else:
        raise ValueError(f"unknown package kind: {kind!r}")
    return mailto(email, subject, lines)
