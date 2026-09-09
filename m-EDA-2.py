###############################################################################
#
# 3.3 보스턴 하우징 데이터 탐색
# 강의자료: Chap03. 탐색적 데이터 분석 EDA
#
#
# scikit-learn 의 dataset에서 제공하지 않음
# 
# 아래 사이트틀 참조하여 Boston Housing 데이터 수집, 전처리하여 csv 로 저장
# Boston Housing Data
# https://ds31x.tistory.com/242
#
# Chap03-3.3 Boston Housing Data Set.py 으로 배포
###############################################################################

'''
Boston Housing Data
https://ds31x.tistory.com/242


idx Column Name Desc.
1   CRIM	    범죄율
2	ZN          25,000 square feet 이상의 주거용 토지의 비율
3	INDUS	    비소매사업지역이 차지하는 토지의 비율
4	CHAS	    강의 경계 1, 아니면 0 (Charles River 기준)
5	NOX	        10ppm 단위의 Nitric Oxides Concentration
6	RM	        주택당 평균 방의 수
7	AGE	        1940년 이전에 건축된 자가 소유 주택의 비율
8	DIS	        다섯 개의 고용센터까지의 가중 거리.
9	RAD	        방사형 고속도로 (radial highways) 접근성 지수 (방사형)
10	TAX	        1만 달러당 재산세율
11	PTRATIO	    학생/교사 비율 (Pupil-teacher ratio)
12	B           1000(Black - 0.63)^2 : Black은 흑인을 의미함. 흑인의 비율
13	LSTAT	    하위계층의 비율 (Lower status)
14	MEDV	    주택의 median 가격 (단위: 1천달러)


다음 URL에서 얻을 수 있는 Boston Housing Data는 약간의 처리가 필요함.
url: http://lib.stat.cmu.edu/datasets/boston 
 

*** 데이터 전처리가 필요하다. ***

위의 URL은 다음과 같은 특성이 있어서 일반적인 csv 형식과 차이가 있음.
* 하나의 샘플에 대한 데이터가 연속된 2개의 라인에 기재됨:  
  때문에 하나의 라인을 하나의 샘플로 처리해선 안됨.
* 짝수행의 데이터에서는 3개 열 외는 NaN이므로 제거해야함.
* 짝수행의 3번째 열이 바로 target인 주택의 median value에 해당함.

이를 반영하여 506개의 sample을 가지며, 하나의 sample은 13개의 feature를 가지는 
input data인 x_raw 와 이에 대응하는 label 값을 가지는 y_raw를 생성하는 code는 다음과 같음.
'''

import pandas as pd
import numpy as np


data_url = 'http://lib.stat.cmu.edu/datasets/boston'

df = pd.read_csv(
    data_url,
    skiprows = 22,
    header = None,
    sep = '\s+'
)

print("------------ 원 데이터 ------------")
print(df.head())


tmp_raw = df.values
x_raw = np.concatenate([tmp_raw[::2,:], tmp_raw[1::2,:2]], axis=1)
y_raw = tmp_raw[1::2,2].reshape(-1,1)

features = [
    'CRIM',
    'ZN',
    'INDUS',
    'CHAS',
    'NOX',
    'RN',
    'AGE',
    'DIS',
    'RAD',
    'TAX',
    'PIRATIO',
    'B',
    'LSTAT',
    'MEDV'
]

df = pd.DataFrame(np.hstack([x_raw,y_raw.reshape(-1,1)]), columns=features)


print("------------ 전처리된 데이터 ------------")
print(df.head())


# csv 화일로 저장
# df.to_csv('boston.csv',index=False)
