#############################################################
# chap02-4절 example
# chap02 판다스 시작하기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import pandas as pd

df = pd.read_csv('./DA/data/gapminder.tsv', sep='\t')


'''
통계 처리의 예

Q1: 연도별 평균 기대수명은?
Q2: 기대 수명, 인구, GDP의 평균은?
Q3: 데이터를 대륙별로 나누어 통계를 계산하려면?
Q4: 대륙별 국가수는?
'''

# Q1: 연도별 평균 기대수명은?
# print( df.groupby('year')['lifeExp'].mean() )
# print( df.groupby('year')['lifeExp'].mean().reset_index() )

# print( df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean() )


# Q2: 기대 수명, 인구, GDP의 평균은?
# print( df[['lifeExp','pop','gdpPercap']].mean() )


# Q3: 데이터를 대륙별로 나누어 통계를 계산하려면?
print( df.groupby('continent')[['lifeExp','pop','gdpPercap']].mean() )
# print( df.groupby('continent')[['lifeExp','pop','gdpPercap']].describe() )


# Q4: 대륙별 국가수는?
# print( df.groupby('continent')['country'].nunique() )
# print( df.groupby('continent')['country'].count() )
# print( df.groupby('continent')['country'].value_counts() )




