import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from build import build  # noqa: E402
from content import CONTENT  # noqa: E402


@pytest.fixture
def built(tmp_path):
    out = tmp_path / "out"
    build(out, CONTENT)
    return out


@pytest.fixture
def built_preview_off(tmp_path):
    out = tmp_path / "out_off"
    content = copy.deepcopy(CONTENT)
    content["preview"] = False
    build(out, content)
    return out
