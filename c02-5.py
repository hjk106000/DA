#############################################################
# chap02-5절 example
# chap02 판다스 시작하기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./DA/data/gapminder.tsv', sep='\t')

# print( df.groupby('year')['lifeExp'].mean() )

df.groupby('year')['lifeExp'].mean().plot()
plt.show()

