import glob
import os

try:
    import feather
    has_feather = True
except ImportError:
    has_feather = False

pjoin = os.path.join

hhold_cols = [
    'hhno',  # household number
    'styr',  # year
    'stmth', # month
    'memhh', # members of hhold
    'adltm', # adult males
    'adltf', # adult females
    'child', # children
    'adltgt64', # adults > 64
    'oaps',  # number of pensioners
]


def denormalize(zip_name):
    """
    Denormalize diary and hhold NFS data.

    We do this so we don't have to do this join everytime.
    It's not that expensive to store.

    Write it to CSV and to feather format.
    """

    path, ext = os.path.splitext(zip_name)
    if not os.path.exists(path):
        zip_file = zipfile.ZipFile(zip_name)
        zip_file.extractall(path=path)

    fnames = glob.glob(pjoin(path, '*'))
    diary_name =  glob.fnmatch.filter(fnames,
                                    '*diary data.txt')[0]

    hhold_name = glob.fnmatch.filter(fnames,
                                     '*household data.txt')[0]

    diary = pd.read_csv(diary_name, sep="\t")

    hhold = pd.read_csv(hhold_name, sep="\t",
                        usecols=hhold_cols)
    dta = diary.merge(hhold)
    dta.to_csv(path.rstrip('/') + '.csv', index=False)
    if has_feather:
        feather.write_dataframe(dta, path.rstrip('/') + '.feather')


def create_denormalized():
    fnames = glob.glob('../data/NationalFoodSurvey/NFS_[0-9]*.zip')
    for fname in fnames:
        denormalize(fname)

