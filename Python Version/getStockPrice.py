import pandas_datareader as web
import datetime

start = datetime.datetime(2017, 9, 1)
end = datetime.datetime(2017, 12, 31)

df = web.DataReader("nvda", 'yahoo', start, end)

print(df.head())