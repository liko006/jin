
# 주식 데이터 불러오기
import pandas_datareader as pdr

df1 = pdr.DataReader('005930.KS', 'yahoo')
df2 = pdr.DataReader('AAPL', 'yahoo')
df3 = pdr.DataReader('LISP.SW', 'yahoo')

from datetime import datetime

start = datetime(2017,9,21)
end = datetime(2020,9,21)

df1 = pdr.DataReader('005930.KS','yahoo', start, end)
df2 = pdr.DataReader('AAPL','yahoo', start, end)
df3 = pdr.DataReader('LISP.SW','yahoo', start, end)

print(df1.head())
