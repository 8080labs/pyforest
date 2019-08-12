from ._importable import LazyModule, LazyObject, _import_statements


# ADD YOUR IMPORTS BELOW
# TODO: in this file you can add your most important modules and objects
# EXAMPLES:
# 'import os' becomes 'os = LazyModule("os")'
# 'import numpy as np' becomes 'np = LazyModule("numpy", "np")'
# 'from openpyxl import load_workbook' becomes 'LazyObject("openpyxl", "load_workbook")'
# 'from dask import dataframe as dd' becomes 'LazyObject("dask", "dataframe", "dd")'


# If you are missing an import, please contribute via creating a pull request.
# If you contribute, we can quickly collect the 80% most frequent imports
# Before you create a pull request, please read the following:

# 0) It is always best to first create a GitHub issue before creating a pull request.
# This way you can be sure that your proposal is valid and will be integrated.

# 1) The imported name should be an unambiguous standard convention and highly specific.
# Usually, you want to use the names that are proposed in the library's documentation.
# However, there should be no or little confusion with other libraries
# e.g. 'import dash_html_components as html' is a 'good' counter example
# because 'html' is not specific enough for the dash context.
# Also, it is ambiguous with e.g. IPython.display.HTML.
# A potential resolution might be 'import dash_html_components as dhc'

# 2) General imports e.g. 'from sklearn.preprocessing import *' are not allowed
# because we want to make sure that there is no accidental masking of imported names

# 3) If you disagree with the conventions, you can always adjust your local pyforest


### Data Wrangling
pd = LazyModule("pandas", "pd")

np = LazyModule("numpy", "np")

dd = LazyObject("dask", "dataframe", "dd")
SparkContext = LazyObject("pyspark", "SparkContext")

load_workbook = LazyObject("openpyxl", "load_workbook")


### Data Visualization and Plotting
mpl = LazyModule("matplotlib", "mpl")
plt = LazyModule("matplotlib.pyplot", "plt")

sns = LazyModule("seaborn", "sns")

py = LazyModule("plotly", "py")
go = LazyModule("plotly.graph_objs", "go")
px = LazyModule("plotly.express", "px")

dash = LazyModule("dash")

bokeh = LazyModule("bokeh")

alt = LazyModule("altair")

pydot = LazyModule("pydot")


### Machine Learning
sklearn = LazyModule("sklearn")
OneHotEncoder = LazyObject("sklearn.preprocessing", "OneHotEncoder")
# TODO: add all the other most important sklearn objects

# Deep Learning
tf = LazyModule("tensorflow")
keras = LazyModule("keras")

# NLP
nltk = LazyModule("nltk")
gensim = LazyModule("gensim")
spacy = LazyModule("spacy")


### Helper
sys = LazyModule("sys")
os = LazyModule("os")
re = LazyModule("re")
glob = LazyModule("glob")
Path = LazyObject("pathlib", "Path")

pickle = LazyModule("pickle")

dt = LazyModule("datetime", "dt")

tqdm = LazyModule("tqdm")


#######################################
### Complementary, optional imports ###
#######################################
# Why is this needed? Some libraries patch existing libraries
# Please note: these imports are only executed if you already have the library installed
# If you want to deactivate specific complementary imports, do the following:
# - uncomment the lines which contain `.__on_import__` and the library you want to deactivate

pandas_profiling = LazyModule("pandas_profiling")
pd.__on_import__(pandas_profiling)  # adds df.profile_report attribute to pd.DataFrame

eda = LazyModule("edaviz", "eda")
pd.__on_import__(eda)  # adds GUI to pd.DataFrame when IPython frontend can display it


##################################################
### dont make adjustments below this line ########
##################################################
def lazy_imports():
    return _import_statements(globals(), was_imported=False)


def active_imports():
    return _import_statements(globals(), was_imported=True)
