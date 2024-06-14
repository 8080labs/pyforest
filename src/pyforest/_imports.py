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

open_workbook = LazyImport("from xlrd import open_workbook")

wr = LazyImport("import awswrangler as wr")

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

### Image processing

cv2 = LazyImport("import cv2")
skimage = LazyImport("import skimage")
Image = LazyImport("from PIL import Image")
imutils = LazyImport("import imutils")

# statistics
statistics = LazyImport("import statistics")
stats = LazyImport("from scipy import stats")
sm = LazyImport("import statsmodels.api as sm")

### Time-Series Forecasting
fbprophet = LazyImport("import fbprophet")
Prophet = LazyImport("from fbprophet import Prophet")
ARIMA = LazyImport("from statsmodels.tsa.arima_model import ARIMA")

### Machine Learning
sklearn = LazyImport("import sklearn")

LinearRegression = LazyImport("from sklearn.linear_model import LinearRegression")
LogisticRegression = LazyImport("from sklearn.linear_model import LogisticRegression")
Lasso = LazyImport("from sklearn.linear_model import Lasso")
LassoCV = LazyImport("from sklearn.linear_model import LassoCV")
Ridge = LazyImport("from sklearn.linear_model import Ridge")
RidgeCV = LazyImport("from sklearn.linear_model import RidgeCV")
ElasticNet = LazyImport("from sklearn.linear_model import ElasticNet")
ElasticNetCV = LazyImport("from sklearn.linear_model import ElasticNetCV")
PolynomialFeatures = LazyImport("from sklearn.preprocessing import PolynomialFeatures")
StandardScaler = LazyImport("from sklearn.preprocessing import StandardScaler")
MinMaxScaler = LazyImport("from sklearn.preprocessing import MinMaxScaler")
RobustScaler = LazyImport("from sklearn.preprocessing import RobustScaler")


OneHotEncoder = LazyImport("from sklearn.preprocessing import OneHotEncoder")
LabelEncoder = LazyImport("from sklearn.preprocessing import LabelEncoder")
TSNE = LazyImport("from sklearn.manifold import TSNE")
PCA = LazyImport("from sklearn.decomposition import PCA")
SimpleImputer = LazyImport("from sklearn.impute import SimpleImputer")
train_test_split = LazyImport("from sklearn.model_selection import train_test_split")
cross_val_score = LazyImport("from sklearn.model_selection import cross_val_score")
GridSearchCV = LazyImport("from sklearn.model_selection import GridSearchCV")
RandomizedSearchCV = LazyImport("from sklearn.model_selection import RandomizedSearchCV")
KFold = LazyImport("from sklearn.model_selection import KFold")
StratifiedKFold = LazyImport("from sklearn.model_selection import StratifiedKFold")

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

CountVectorizer = LazyImport(
    "from sklearn.feature_extraction.text import CountVectorizer"
)

metrics = LazyImport("from sklearn import metrics")

sg = LazyImport("from scipy import signal as sg")

# Clustering
KMeans = LazyImport ("from sklearn.cluster import KMeans")

# Gradient Boosting Decision Tree
xgb = LazyImport("import xgboost as xgb")
lgb = LazyImport("import lightgbm as lgb")

# TODO: add all the other most important sklearn objects
# TODO: add separate sections within machine learning viz. Classification, Regression, Error Functions, Clustering

# Deep Learning
tf = LazyImport("import tensorflow as tf")
keras = LazyImport("import keras")
torch = LazyImport("import torch")
fastai = LazyImport("import fastai")

# NLP
nltk = LazyImport("import nltk")
gensim = LazyImport("import gensim")
spacy = LazyImport("import spacy")
re = LazyImport("import re")
textblob = LazyImport("import textblob")

### Helper
sys = LazyImport("import sys")
os = LazyImport("import os")
re = LazyImport("import re")
glob = LazyImport("import glob")
Path = LazyImport("from pathlib import Path")
random = LazyImport("import random")

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
