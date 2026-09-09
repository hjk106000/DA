###############################################################################
#
# PQ_15.(참고) IRIS 붓꽃 데이터를 사용한 다양한 머신러닝 사례
# 제16강. 파이썬 응용 - 머신러닝 
# 파이썬 200제 (통계편), 위키북스, https://wikidocs.net/book/16867
#
#
# 2.3 python으로 해보는 데이터 과학
# 강의자료: Chap01. 데이터과학 소개
#
# Chap01-2.3 Python ML Preview.py 으로 배포
###############################################################################

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np


# 데이터 불러오기
iris = load_iris()
'''
꽃받침(sepal)과 꽃잎(petal)의 너비와 길이 측정값
종류(setosa, versicolor, virginica) 
'''
#print(iris.DESCR)
# print(iris.data)
#print(iris.target)  


# (1) 데이터 로드
X = iris.data
y = iris.target


# (2) 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# (3) 데이터 정규화
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


############################## KNN 모델 생성 및 훈련 ##############################
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# (4) 모델 생성 - KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train) # learning


# (5) 훈련된 mode을 가지고 예측
y_pred_knn = knn.predict(X_test)

# (6) 정확도 평가
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f'KNN 정확도: {accuracy_knn}')


'''
# knn 실제 데이티로 예측
data = np.array([[2.7, 2.4, 1.65, 0.67], 
                 [5.84, 5.48, 3, 2.16], 
                 [3.97, 4.01, 1.7, 0.67]]) 
df = pd.DataFrame(data, columns=iris.feature_names)
print(df)

pred = knn.predict(df) 
df['species'] = pred
print(df)

print(iris['target_names'])
# print(iris['target_names'][0])
'''

############################## Dection Tree 모델 생성 및 훈련 ##############################
from sklearn.tree import DecisionTreeClassifier

# (4) 모델 생성
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# (5) 예측
y_pred_dt = dt.predict(X_test)

# (6) 정확도 평가
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f'의사결정나무 정확도: {accuracy_dt}')


############################## SVM 모델 생성 및 훈련 ##############################
from sklearn.svm import SVC

# (4) 모델 생성
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)

# (5) 예측
y_pred_svm = svm.predict(X_test)

# (6) 정확도 평가
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f'SVM 정확도: {accuracy_svm}')


############################## 모형 결과 비교##############################
# 세 가지 모델의 정확도를 비교하여 어느 모델이 가장 좋은 성능을 보이는지 확인할 수 있습니다.

print(f'KNN 정확도: {accuracy_knn}')
print(f'의사결정나무 정확도: {accuracy_dt}')
print(f'SVM 정확도: {accuracy_svm:.3}')

