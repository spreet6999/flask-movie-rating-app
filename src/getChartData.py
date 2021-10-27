from datetime import datetime
import pandas as pd
import time

print("Initalized getChartData")


def getChartData(df):
    start_time = time.time()
    # df["time"] = df["time"].apply(lambda x: datetime.fromtimestamp(x))
    df["time"] = pd.to_datetime(df["time"])
    # df["year"] = pd.DatetimeIndex(df["time"].year)
    df["year"] = df["time"].dt.year
    dfYearSales = df.groupby(['year'])['sales'].sum().reset_index()
    dfYearSales = dfYearSales[['year', 'sales']]
    end_time = time.time() 
    duration = round(end_time-start_time, 3)
    print(f'df_year_sales transformation in {duration}')

    print("getChartData Called!")
    return dfYearSales
