###############################################################################
#
# iris 붓꽃 dataset 의 EDA
#
# 3.1 탐색적 데이터 분석 EDA 
# 강의자료: Chap03. 탐색적 데이터 분석 EDA
#
# 참고 URL:
# iris 데이터셋을 이용한 시각화 (feat.seaborn, pandas plot)
# https://dacon.io/competitions/official/235836/codeshare/4168
#
# Chap03-3.1 iris dataset.py 으로 배포
#
###############################################################################


from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()

#--------------------------------------------------------------------------
#
# 라이브러리 가져오기: from sklearn.datasets import load_iris
# 데이터 로드: iris = load_iris()
# 데이터 확인: iris.data (특징), iris.target (정답 레이블)
#
#--------------------------------------------------------------------------

# print(iris)
# print(iris.DESCR)
# print(iris.data[0:5])    # feature 특징 
# print(iris.target[0:5])  # target 정답레이블


# --------------------------------------------------------------------------
#
# 판다스(Pandas) 데이터프레임 변환
#
#--------------------------------------------------------------------------

# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df['species'] = iris.target

# print(df.head())
# print(df.tail())


# --------------------------------------------------------------------------
#
# 붓꽃(Iris) 데이터셋의 기초 통계량
# 판다스(Pandas)의 describe() 함수를 사용하면 한 줄로 쉽게 확인할 수 있습니다.
# 데이터의 개수, 평균, 표준편차, 최솟값, 사분위수, 최댓값이 
# 데이터프레임 형태로 출력됩니다.
#
# --------------------------------------------------------------------------


'''
주요 출력 지표 설명
count: 데이터 개수 (각 특징별 150개)
mean: 산술 평균값
std: 표준편차 (데이터가 평균에서 떨어진 정도)
min / max: 최솟값과 최댓값
25% / 50% / 75%: 백분위수 (50%는 중앙값)
'''

# print(df.describe())
# print(df.var())
# print(df['sepal length (cm)'].var())
# print(df[0:4].var())
# print(df.corr())


'''
품종별 통계량 확인 (심화)붓꽃은 3개 품종(Setosa, Versicolor, Virginica)으로 나뉩니다. 
품종별 평균을 비교하면 데이터의 차이를 더 잘 이해할 수 있습니다.
'''
# print(df.groupby('species').mean())



# --------------------------------------------------------------------------
#
# 데이터 시각화 Data Visualization
#
# 붓꽃(Iris)의 "품종별 데이터 분포" 는 시본(Seaborn) 라이브러리의 
# Boxplot(상자 수염 그림)을 사용하면 한눈에 가장 잘 비교할 수 있습니다.
#
# --------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 로드 및 데이터프레임 변환
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# 숫자로 된 target을 실제 품종 이름으로 매핑
df["species"] = [iris.target_names[i] for i in iris.target]

'''
# 2. 그래프 스타일 설정
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))


# 피어슨 솽관게수
# print(df.corr())


# 3. 4개 특징별 Boxplot 그리기
for i, feature in enumerate(iris.feature_names):
    row, col = i // 2, i % 2
    sns.boxplot(
        x="species", y=feature, data=df, ax=axes[row, col], palette="Set2"
    )
    axes[row, col].set_title(f"Distribution of {feature}")
    axes[row, col].set_xlabel("Species")
    axes[row, col].set_ylabel("Value (cm)")

plt.tight_layout()
plt.show()
'''


# --------------------------------------------------------------------------
#
# 데이터 시각화 Data Visualization
#
# 붓꽃(Iris) 데이터셋의 모든 변수 간 상관관계와 품종별 분포를 한눈에 보려면
# 시본(Seaborn)의 pairplot() 함수가 가장 효과적입니다. 
# 이 함수는 모든 변수 조합에 대한 산점도(Scatter plot)와 
# 대각선 상의 히스토그램을 격자 형태로 한 번에 그려줍니다.
# 
# --------------------------------------------------------------------------

# 2. Pairplot 생성
# hue='species' 옵션으로 품종별 색상을 다르게 지정합니다.
sns.pairplot(df, hue="species", palette="Set2", diag_kind="kde")

# 3. 그래프 출력
plt.show()
