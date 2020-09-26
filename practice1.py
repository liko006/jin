
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


# 저장된 데이터 프레임에 새로운 열 추가 (주식의 중간값)

df1['kor_Mid'] = (df1['kor_High'] + df1['kor_Low'])/2
df2['usa_Mid'] = (df2['usa_High'] + df2['usa_Low'])/2
df2['eur_Mid'] = (df3['eur_High'] + df3['eur_Low'])/2

print(df1.tail())
print(df2.tail())
print(df3.tail())

# 하나의 데이터 프레임으로 합친 뒤, 최신순으로 정렬 (숙제)

import pandas as pd
mdf1 = pd.merge(df1,df2, on='Date')
mdf1.head()

mdf = pd.merge(mdf1, df3, on='Date')
mdf.head()

sort_mdf = pd.sort_index(ascending=False)

sort_mdf.head()
