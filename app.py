
###############################################################################
# app.py
#
# Gemini 작성코드
# 1. 모델 학습 및 직렬화 (train_model.py)
# 붓꽃(Iris) 데이터셋을 이용해 KNN 모델을 학습시키고 knn_model.pkl 파일로 저장합니다.
#
# 2. Streamlit 웹 애플리케이션 (app.py)
# 저장된 모델을 로드하여 사용자 입력 값을 바탕으로 예측을 수행합니다.
# Terminal 에서 > streamlit run d:/coding/pwork/DA/app.py 으로 실행
#
# USER:
# python 에서 훈련된 knn 객체를 직렬화 하여 저장하고,  
# 이 객체를 이용하여 사용자 입력에 따라  예측하는 앱을 python 으로 만들어줘
###############################################################################

import joblib
import numpy as np
import streamlit as st

# 저장된 KNN 모델 로드
model = joblib.load("knn_model.pkl")
target_names = ["Setosa", "Versicolor", "Virginica"]

# 웹 앱 UI 설정
st.title("🌺 Iris 꽃 종류 예측 앱 (KNN)")
st.write("꽃잎과 꽃받침의 길이를 입력하여 품종을 예측하세요.")

# 사용자 입력 받기
sepal_length = st.slider("꽃받침 길이 (Sepal Length)", 4.0, 8.0, 5.8)
sepal_width = st.slider("꽃받침 너비 (Sepal Width)", 2.0, 4.5, 3.0)
petal_length = st.slider("꽃잎 길이 (Petal Length)", 1.0, 7.0, 4.3)
petal_width = st.slider("꽃잎 너비 (Petal Width)", 0.1, 2.5, 1.3)

# 예측 버튼 클릭 시 실행
if st.button("예측하기"):
    input_data = np.array(
        [[sepal_length, sepal_width, petal_length, petal_width]]
    )
    prediction = model.predict(input_data)[0]
    predicted_class = target_names[prediction]

    st.success(f"예측 결과: **{predicted_class}**")