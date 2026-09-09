#############################################################
# chap03-4절 example
# chap03 판다스 자료구조 살펴보기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd

df = pd.read_csv('./DA/data/scientists.csv')
print(df)
print(df.dtypes)

