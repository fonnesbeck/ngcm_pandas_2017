import pandas as pd

dta = pd.read_csv("../data/NationalFoodSurvey/NFS_1974.csv")
dta['fditemno'] = dta['fditemno'].astype("category")
dta.fditemno.describe()
