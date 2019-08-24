# -*- coding: utf-8 -*-
from ._imports import *


#  set __version__ attribute
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'pyforest',
        'require': 'pyforest/index'
    }]


def _jupyter_labextension_paths():
    return [{
        'name': 'pyforest',
        'src': 'static',
    }]
