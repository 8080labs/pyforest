# %%
# from pyforest import *  # not needed because of auto_import

# %%
df = pd.read_csv("titanic.csv")

# %%
sns.distplot(df.Age)

# %%
active_imports()
