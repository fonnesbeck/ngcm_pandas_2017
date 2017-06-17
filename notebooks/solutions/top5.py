top5 = vessels.type.isin(vessels.type.value_counts().index[:5])
vessels5 = vessels[top5]