import pandas as pd

diary = pd.read_csv("../data/NationalFoodSurvey/NFS_1974/1974 diary data.txt",
                    sep="\t")
hhold = pd.read_csv("../data/NationalFoodSurvey/NFS_1974/1974 household data.txt",
                    sep="\t")

dta = diary.merge(hhold)
