from i18n import LANGS, page_path, rel, t


def test_t_and_rel():
    assert LANGS == ("en", "pt")
    assert t({"en": "a", "pt": "b"}, "pt") == "b"
    assert t({"en": "a", "pt": "b"}, "en") == "a"
    assert t(5, "pt") == 5
    assert t("plain", "pt") == "plain"
    assert rel("pt/sabores/", "") == "../../"
    assert rel("", "pt/") == "pt/"
    assert rel("flavours/", "pt/sabores/") == "../pt/sabores/"
    assert rel("flavours/", "flavours/") == "./"


def test_page_path():
    home = {"slug": {"en": "", "pt": ""}}
    rest = {"slug": {"en": "for-restaurants", "pt": "para-restaurantes"}}
    assert page_path(home, "en") == ""
    assert page_path(home, "pt") == "pt/"
    assert page_path(rest, "en") == "for-restaurants/"
    assert page_path(rest, "pt") == "pt/para-restaurantes/"
