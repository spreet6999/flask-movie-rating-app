from datetime import datetime, timedelta
from random import randrange
import pandas as pd

date = datetime(1900, 1, 1)

time_list = []
sales = []

for i in range(0, 1000000):
    new_ts = date + timedelta(hours=i)
    sales.append(randrange(10))
    time_list.append(new_ts)

print(time_list[-1], sales[0])

time_sales_dict = {"time": time_list, "sales": sales}

# Create DataFrame
df = pd.DataFrame(time_sales_dict)

df.to_csv("sales_data.csv", index=False)
df.to_json("sales_data.json", orient="records")

# Creating subset of df
df_subset = df.head(10)

df_subset.to_csv("sales_subset_data.csv", index=False)
df_subset.to_json("sales_subset_data.json", orient="records")

print(df.shape)
