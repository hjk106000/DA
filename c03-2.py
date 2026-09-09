#############################################################
# chap03-2절 example
# chap03 판다스 자료구조 살펴보기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd

# s = pd.Series(['banana', 42])
# print(s)
# print(type(s))

df = pd.read_csv('./DA/data/scientists.csv')
# print(df)

ages = df['Age']
print(ages)
# print(type(ages))

#print(ages.describe())

# broadcasting 연산 또는 vectorized 연산
print(ages[ages>ages.mean()])

