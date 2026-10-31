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
