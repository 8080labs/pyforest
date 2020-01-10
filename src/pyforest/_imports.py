from ._importable import LazyImport, _get_import_statements
from .user_specific_imports import _load_user_specific_imports


# If you are missing an import and you think it is a common import, please contribute
# via creating a pull request.
# If you contribute, we can quickly collect the 80% most frequent imports
# Before you create a pull request, PLEASE READ THE FOLLOWING:

# 0) It is always best to first create a GitHub issue before creating a pull request.
# This way you can be sure that your proposal is valid and will be integrated.

# 1) The imported name should be an unambiguous standard convention and highly specific.
# Usually, you want to use the names that are proposed in the library's documentation.
# However, there should be no or little confusion with other libraries
# Good example:
#    'import pandas as pd'
# Bad example:
#    'import dash_html_components as html'
# because 'html' is not specific enough for the dash context.
# Also, it is ambiguous with e.g. IPython.display.HTML.
# A potential resolution might be 'import dash_html_components as dhc'

# 2) General, implicit imports e.g. 'from sklearn.preprocessing import *' are not possible
# because we want to make sure that there is no accidental masking of imported names

# 3) If you disagree with the conventions or you are using rare packages, you can save
# your user-specific imports in ~/.pyforest/user_imports.py


### Data Wrangling
pd = LazyImport("import pandas as pd")

np = LazyImport("import numpy as np")

dd = LazyImport("from dask import dataframe as dd")
SparkContext = LazyImport("from pyspark import SparkContext")

load_workbook = LazyImport("from openpyxl import load_workbook")

### Data Visualization and Plotting
mpl = LazyImport("import matplotlib as mpl")
plt = LazyImport("import matplotlib.pyplot as plt")

sns = LazyImport("import seaborn as sns")

py = LazyImport("import plotly as py")
go = LazyImport("import plotly.graph_objs as go")
px = LazyImport("import plotly.express as px")

dash = LazyImport("import dash")

bokeh = LazyImport("import bokeh")

alt = LazyImport("import altair as alt")

pydot = LazyImport("import pydot")

# statistics
statistics = LazyImport("import statistics")

### Machine Learning
sklearn = LazyImport("import sklearn")
OneHotEncoder = LazyImport("from sklearn.preprocessing import OneHotEncoder")
TSNE = LazyImport("from sklearn.manifold import TSNE")
train_test_split = LazyImport("from sklearn.model_selection import train_test_split")
svm = LazyImport("from sklearn import svm")
GradientBoostingClassifier = LazyImport(
    "from sklearn.ensemble import GradientBoostingClassifier"
)
GradientBoostingRegressor = LazyImport(
    "from sklearn.ensemble import GradientBoostingRegressor"
)
RandomForestClassifier = LazyImport(
    "from sklearn.ensemble import RandomForestClassifier"
)
RandomForestRegressor = LazyImport("from sklearn.ensemble import RandomForestRegressor")

TfidfVectorizer = LazyImport(
    "from sklearn.feature_extraction.text import TfidfVectorizer"
)

# TODO: add all the other most important sklearn objects
# TODO: add separate sections within machine learning viz. Classification, Regression, Error Functions, Clustering

# Deep Learning
tf = LazyImport("import tensorflow as tf")
keras = LazyImport("import keras")

# NLP
nltk = LazyImport("import nltk")
gensim = LazyImport("import gensim")
spacy = LazyImport("import spacy")
re = LazyImport("import re")

### Helper
sys = LazyImport("import sys")
os = LazyImport("import os")
re = LazyImport("import re")
glob = LazyImport("import glob")
Path = LazyImport("from pathlib import Path")

pickle = LazyImport("import pickle")

dt = LazyImport("import datetime as dt")

tqdm = LazyImport("import tqdm")


##################################################
### dont make adjustments below this line ########
##################################################


#############################
### User-specific imports ###
#############################
# You can save your own imports in ~/.pyforest/user_imports.py
# Please note: imports in ~/.pyforest/user_imports.py take precedence over the
# imports above.

_load_user_specific_imports(globals())
# don't want to blow up the namespace
del _load_user_specific_imports


# #######################################
# ### Complementary, optional imports ###
# #######################################
# # Why is this needed? Some libraries patch existing libraries
# # Please note: these imports are only executed if you already have the library installed
# # If you want to deactivate specific complementary imports, do the following:
# # - uncomment the lines which contain `.__on_import__` and the library you want to deactivate

# pandas_profiling = LazyImport("import pandas_profiling")
# pd.__on_import__(pandas_profiling)  # adds df.profile_report attribute to pd.DataFrame

# bam = LazyImport("import bamboolib as bam")
# pd.__on_import__(bam)  # adds GUI to pd.DataFrame when IPython frontend can display it


def lazy_imports():
    return _get_import_statements(globals(), was_imported=False)


def active_imports(print_statements=True):
    statements = _get_import_statements(globals(), was_imported=True)
    if print_statements:
        print("\n".join(statements))
    return statements
