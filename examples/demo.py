import pyforest

df = pd.read_csv("titanic.csv")

sns.distplot(df.Age)
plt.show()


