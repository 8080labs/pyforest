# -*- coding: utf-8 -*-
def get_user_symbols():
    import inspect

    for index, item in enumerate(inspect.stack()):
        try:
            name = item[0].f_globals["__name__"]
            if name == "__main__":
                return item[0].f_globals
        except:  # __name__ attribute does not exist
            pass
    return {}


from ._imports import *

user_symbols = get_user_symbols()
pyforest_imports = globals().copy().keys()

for import_symbol in pyforest_imports:
    # don't overwrite symbols of the user
    if import_symbol not in user_symbols.keys():
        user_symbols[import_symbol] = eval(import_symbol)


#  set __version__ attribute
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "static",
            "dest": "pyforest",
            "require": "pyforest/nbextension",
        }
    ]


def _jupyter_labextension_paths():
    return [{"name": "pyforest", "src": "static"}]
