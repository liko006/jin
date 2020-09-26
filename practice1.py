
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

# 불러와서 저장한 데이터의 칼럼 이름 바꾸기

df1.rename(columns={'High':'kor_High','Low':'kor_Low','Open':'kor_Open',
                   'Close':'kor_Close','Adj Close':'kor_Adj Close'}, inplace=True)
df2.rename(columns={'High':'usa_High','Low':'usa_Low','Open':'usa_Open',
                   'Close':'usa_Close','Adj Close':'usa_Adj Close'}, inplace=True)
df3.rename(columns={'High':'eur_High','Low':'eur_Low','Open':'eur_Open',
                   'Close':'eur_Close','Adj Close':'eur_Adj Close'}, inplace=True)

print(df1.tail())
print(df2.tail())
print(df3.tail())

