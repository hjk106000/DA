#############################################################
# chap04-2절 example
# chap04 그래프 그리기
# Do it! 데이터 분석을 위한 판다스 입문
#############################################################

import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd

ans = sns.load_dataset('anscombe')
# print(ans)
# print(type(ans))


'''
# 데이터셋 별로 기술통계

# 평균 mean, 표준편차 std, 공분산 cov, 상관계수 corr 가 같다.
# print(ans.groupby('dataset').describe())
# print(ans.groupby('dataset')['x'].describe())
# print(ans.groupby('dataset')['y'].describe())

# cov(x,y) = E[(x-E[x])(y-E[y])] = E[xy] - E[x]E[y]
# print("공분산", ans.groupby('dataset')[['x', 'y']].cov())
# # corr(x,y) = E[(x-E[x])(y-E[y])] / sqrt(E[x]E[y])
# print("상관계수", ans.groupby('dataset')[['x','y']].corr())

# 위의 두 개 출력 결과를 잘 살펴 볼 것
'''


# 데이터 분포를 잘 살펴보기 위해 그래프로 보여주기

ds1 = ans[ans['dataset'] == 'I']
# # print(ds1)
# # plt.plot(ds1['x'], ds1['y'], 'o')
# # plt.show() 

ds2 = ans[ans['dataset'] == 'II']
ds3 = ans[ans['dataset'] == 'III']
ds4 = ans[ans['dataset'] == 'IV']

fig = plt.figure()
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

axes1.plot(ds1['x'], ds1['y'], 'o')
axes2.plot(ds2['x'], ds2['y'], 'o')
axes3.plot(ds3['x'], ds3['y'], 'o')
axes4.plot(ds4['x'], ds4['y'], 'o')

axes1.set_title('Anscombe I')
axes2.set_title('Anscombe II')
axes3.set_title('Anscombe III')
axes4.set_title('Anscombe IV')

fig.suptitle('Anscombe')
fig.set_tight_layout(True)

plt.show()

