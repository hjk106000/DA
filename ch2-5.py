###############################################################################
#
#
# Do it! 쉽게 배우는 파이썬 데이터 분석
# 김영우 저
# 이지스퍼블리싱 
# 2022
###############################################################################

import pandas as pd

# 현재 pwd 는 D:\Coding\pwork
df = pd.read_csv('./doitDA/Data/mpg.csv')
print(df)
# print(df.head())
# print(df.describe())
# print(df.info())
# print(df.columns)
# print(df.dtypes)
# print(df.shape)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum().sort_values(ascending=False))

