import datetime

def parse(year, month, day):
    return datetime.datetime(int(year), int(month), int(day))

dta = pd.read_csv("../data/NationalFoodSurvey/NFS_1974.csv",
                  parse_dates={'date': ['styr', 'stmth', 'logday']},
                  date_parser=parse)
