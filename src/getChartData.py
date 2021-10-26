import pandas as pd
from datetime import datetime

print("Initalized getChartData")


def getChartData(df):

    print(df.head(1))

    df["time"] = pd.to_datetime(df["time"])
    print(df.head(1))

    # print(df["time"].dt.year.head(1))

    df["year"] = pd.DatetimeIndex(df["time"]).year
    print(df.head(1))
    print("#############################")

    print("getChartData Called!")
    return "Hello"
