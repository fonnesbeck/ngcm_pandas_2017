import glob
import re

import pandas as pd

def read_csv(file_name):
    df = pd.read_csv(file_name, sep="\t")
    year = re.search("\d{4}", file_name).group()
    df['styr'] = int(year)
    return df

diary_files = glob.glob("../data/NationalFoodSurvey/NFS_[0-9]*/*diary*")
dta = pd.concat(map(read_csv, diary_files), axis=0, ignore_index=True)
