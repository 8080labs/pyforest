# -*- coding: utf-8 -*-

import pytest
from pyforest.__modules__ import *

def test_auto_import():
        pd = importable("pandas", "pd")
        assert "autoimported module of <module 'pandas' from" in f"{pd}"

def test_auto_import_function_call():
        df = pd.DataFrame([['a', 'b'], ['c', 'd']], index=['row 1', 'row 2'], columns=['col 1', 'col 2'])
        df_from_json = pd.read_json('{"col 1":{"row 1":"a","row 2":"c"},"col 2":{"row 1":"b","row 2":"d"}}')
        assert df.equals(df_from_json)

def test_setup_auto_import():
        assert setup_auto_import()
