"""Checks on the production build switch and the STRATO deploy plan (no network)."""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from build import content_for_env  # noqa: E402
from content import CONTENT  # noqa: E402
from deploy_strato import MANIFEST, check_remote_path, local_manifest, plan  # noqa: E402


def test_production_env_turns_preview_off():
    assert content_for_env({"SITE_ENV": "production"})["preview"] is False
    assert CONTENT["preview"] is True  # the shared dict is not mutated


def test_default_env_keeps_preview():
    assert content_for_env({})["preview"] is True
    assert content_for_env({"SITE_ENV": "staging"})["preview"] is True


@pytest.mark.parametrize("path", ["", "/", "htdocs", "/htdocs", "/htdocs/", ".", "/htdocs/.."])
def test_refuses_webspace_root(path):
    with pytest.raises(SystemExit):
        check_remote_path(path)


def test_accepts_dedicated_folder():
    assert check_remote_path("/realhealthkombucha/") == "/realhealthkombucha"
    assert check_remote_path("/htdocs/realhealthkombucha") == "/htdocs/realhealthkombucha"


def test_refuses_foreign_folder():
    # A non-empty folder without our manifest belongs to something else (e.g. Sattva).
    with pytest.raises(SystemExit):
        plan({"index.html": "a"}, remote_manifest=None, remote_entries=["index.html", "img"])


def test_first_deploy_into_empty_folder_uploads_everything():
    uploads, deletes = plan({"index.html": "a", "pt/index.html": "b"}, None, [])
    assert uploads == ["index.html", "pt/index.html"]
    assert deletes == []


def test_only_changed_files_uploaded_and_stale_ones_deleted():
    old = {"site": "realhealthkombucha", "files": {"index.html": "a", "old/index.html": "x", "pt/index.html": "b"}}
    uploads, deletes = plan({"index.html": "a", "pt/index.html": "B"}, old, ["index.html", "old", "pt", MANIFEST])
    assert uploads == ["pt/index.html"]
    assert deletes == ["old/index.html"]


def test_manifest_of_other_site_refused():
    with pytest.raises(SystemExit):
        plan({"index.html": "a"}, {"site": "something-else", "files": {}}, ["index.html", MANIFEST])


def test_local_manifest_hashes_build(built):
    files = local_manifest(built)
    assert "index.html" in files and "pt/index.html" in files
    assert "assets/img/logo-light.png" in files
    assert all(len(h) == 64 for h in files.values())
    assert MANIFEST not in files
