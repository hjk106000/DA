###############################################################################
# train_model.py
#
# USER:
# python 에서 훈련된 knn 객체를 직렬화 하여 저장하고,  
# 이 객체를 이용하여 사용자 입력에 따라  예측하는 앱을 python 으로 만들어줘
#
# Gemini AI:
# 1. 모델 학습 및 직렬화 (train_model.py)
# 붓꽃(Iris) 데이터셋을 이용해 KNN 모델을 학습시키고 knn_model.pkl 파일로 저장합니다.
#
# 2. Streamlit 웹 애플리케이션 (app.py)
# 저장된 모델을 로드하여 사용자 입력 값을 바탕으로 예측을 수행합니다.
# Terminal 에서 > streamlit run d:/coding/pwork/DA/app.py 으로 실행
#
###############################################################################


import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 데이터 로드 및 분할
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# KNN 모델 학습
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 모델 직렬화 (저장)
joblib.dump(knn, "knn_model.pkl")
print("모델이 knn_model.pkl로 성공적으로 저장되었습니다.")