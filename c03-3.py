#############################################################
# chap03-3절 example
# chap03 판다스 자료구조 살펴보기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd

df = pd.read_csv('./DA/data/scientists.csv')

# print(df)
# print(df['Age'].mean())
# print(df.loc[df['Age']>df['Age'].mean()])


df1 = df2 = pd.DataFrame(data=[[1,2,3],[4,5,6],[7,8,9]])
print(df1)

print(df1.add(df2))
print(df1.add(df2, fill_value=0))


