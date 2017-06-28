import pandas as pd
import dask.dataframe as dd

df = dd.read_csv("../data/NationalFoodSurvey/NFS*.csv")
food_mapping = pd.read_csv("../data/NationalFoodSurvey/food_mapping.csv")

df1974 = df.get_division(0)
minfd74 = (df1974.groupby('minfd')
                  .apply(len, columns='size')
                  .compute()
                  .idxmax())

# alternatively, use the category type
# you first have to materialize the categorical
# though this should work with fixes in pandas 0.18.2

df1974.minfd.astype('category').compute().describe()['top']
