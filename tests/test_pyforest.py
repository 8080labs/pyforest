# -*- coding: utf-8 -*-

import pytest
from pathlib import Path

USER_IMPORTS_PATH = Path().home() / ".pyforest_test" / "user_imports.py"


def test_imports():
    from pyforest import os, pd, Path, active_imports

    os.name
    assert "import os" in active_imports()

    df = pd.DataFrame()
    assert "import pandas as pd" in active_imports()

    Path(".")
    assert "from pathlib import Path" in active_imports()

    # TODO: add example for 'from x import y as z'


def test_lazy_imports():
    from pyforest import lazy_imports

    # if the module e.g. "re" has been imported in test_imports() this test will fail
    assert "import re" in lazy_imports()


def test_complementary_import():
    # TODO: fix this test
    from pyforest import pd, active_imports

    df = pd.DataFrame()
    # assert "import pandas_profiling" in active_imports()


def test_autocomplete():
    from pyforest import pd

    assert "DataFrame" in dir(pd)


def test_auto_import():
    from pyforest.auto_import import setup as setup_auto_import

    assert setup_auto_import()


def setup_test_file(statement: str) -> None:
    USER_IMPORTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    USER_IMPORTS_PATH.touch()
    USER_IMPORTS_PATH.write_text(statement)


def cleanup_test_file() -> None:
    USER_IMPORTS_PATH.unlink()
    USER_IMPORTS_PATH.parent.rmdir()


def test_user_imports():
    from pyforest.user_specific_imports import _load_user_specific_imports
    from pyforest import LazyImport, active_imports

    # _load_user_specific_imports needs LazyImport in globals
    globals().update({"LazyImport": LazyImport})

    IMPORT_STATEMENT = "import pandas as test_import"

    setup_test_file(IMPORT_STATEMENT)
    assert USER_IMPORTS_PATH.exists()

    _load_user_specific_imports(globals_=globals(), user_imports_path=USER_IMPORTS_PATH)
    assert isinstance(test_import, LazyImport)

    cleanup_test_file()
    assert not USER_IMPORTS_PATH.exists()
