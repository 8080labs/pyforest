# -*- coding: utf-8 -*-

import pytest


def test_imports():
    from pyforest import os, pd, Path, active_imports

    os.name
    assert "import os" in active_imports()

    df = pd.DataFrame()
    assert "import pandas as pd" in active_imports()

    # Path('.')
    # assert "from pathlib import Path" in active_imports()

    # TODO: add example for 'from x import y as z'


def test_lazy_imports():
    from pyforest import lazy_imports

    assert "import os" in lazy_imports()


def test_complementary_import():
    from pyforest import pd, active_imports

    df = pd.DataFrame()
    assert "import pandas-profiling" in active_imports()


def test_autocomplete():
    from pyforest import pd

    assert "DataFrame" in dir(pd)


def test_auto_import():
    from pyforest.auto_import import setup as setup_auto_import

    assert setup_auto_import()
