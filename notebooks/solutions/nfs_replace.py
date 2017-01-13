import pandas as pd

def read_desc(file_name):
    fname = "../data/NationalFoodSurvey/{}".format(file_name)
    return pd.read_csv(fname, sep="\t")

food_groups = read_desc("Ref_ food groups.txt")

# get the replacement dictionary
# a mapping of key to value with which to replace it
to_replace = food_groups.set_index('fdgp').to_dict()['fd gp description']

food_groups.fdgp.replace(to_replace)
