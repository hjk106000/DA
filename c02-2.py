#############################################################
# chap02-2절 example
# chap02 판다스 시작하기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd

df = pd.read_csv('./DA/data/gapminder.tsv', sep='\t')

# print(df)
# print(type(df))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.describe(percentiles=[0.25, 0.5, 0.75]))
# print(df.describe(include='all'))   


# country_col = df['country']
# print(country_col)
# print(type(country_col))

# print(df.loc[[0,99,999]])
# print(df.iloc[-1])

print(df.loc[:, ['year', 'lifeExp']])


