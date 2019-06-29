import datetime
import pandas_datareader as web
import os

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime.now()
df = web.get_data_yahoo("AAPL", start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())