# this is a bit slow because of the date parsing

transit = pd.read_csv("../data/AIS/transit_segments.csv", 
                      parse_dates=['st_time', 'end_time'],
                      infer_datetime_format=True)
vessels = pd.read_csv("../data/AIS/vessel_information.csv")