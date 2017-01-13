import pandas as pd

def read_desc(file_name):
    fname = "../data/NationalFoodSurvey/{}".format(file_name)
    return pd.read_csv(fname, sep="\t")

food_groups = read_desc("Ref_ food groups.txt")
food_groups.loc[food_groups['fd gp description'].str.contains('MILK')]
