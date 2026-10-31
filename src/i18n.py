"""Language helpers: EN at the site root, PT under pt/."""
import posixpath

LANGS = ("en", "pt")


def t(value, lang):
    """Pick the `lang` entry from a {"en": .., "pt": ..} dict; other values pass through."""
    if isinstance(value, dict):
        return value[lang]
    return value


def page_path(page, lang):
    """Output directory of `page` in `lang`, relative to the site root ("" = EN home)."""
    slug = page["slug"][lang]
    prefix = "" if lang == "en" else f"{lang}/"
    return f"{prefix}{slug}/" if slug else prefix


def rel(from_path, to_path):
    """Relative URL from directory `from_path` to `to_path` (both relative to the site root).

    Directories end with "/" ("" is the root); the result keeps that trailing slash.
    """
    is_dir = to_path == "" or to_path.endswith("/")
    r = posixpath.relpath("/" + to_path, "/" + from_path)
    if r == ".":
        return "./"
    return r + "/" if is_dir else r


def eur(amount, lang, decimals=2):
    """Format a euro amount for `lang`: EN "€20.50", PT "20,50\u00a0€" (European Portuguese,
    non-breaking space so the sign never wraps onto its own line).

    `decimals` = 0 gives whole euros ("€148" / "148 €"). Thousands: EN "€1,250.00",
    PT "1250,00 €" (no grouping; the site's amounts stay below 1000).
    """
    if lang == "pt":
        return num(amount, lang, decimals) + NBSP + "€"
    return f"€{amount:,.{decimals}f}"


NBSP = "\u00a0"


def num(value, lang, decimals=None):
    """Format a number for `lang`: EN "5.0", PT "5,0" (decimal comma).

    `decimals` = None keeps the value's own form (37 -> "37"); otherwise fixed decimals.
    """
    s = str(value) if decimals is None else f"{value:.{decimals}f}"
    return s.replace(".", ",") if lang == "pt" else s
