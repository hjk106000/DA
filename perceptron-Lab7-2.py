###############################################################################
#
# **생능 출판사 "으뜸 머신러닝"(1판) 교재의 소스 코드**
# *7장 인공신경망기초 코드*
# * 출판사 : 생능 출판사( http://www.booksr.co.kr/ )
# * 으뜸 머신러닝 저자 : 강영민, 박동규, 김성수
# * 소스코드 저장소 : https://github.com/dknife/ML
# * 저작권 : 본 주피터 노트북 코드는 자유롭게 배포가능하지만 
#           위의 출판사, 저서, 저자표기와 함께 배포해 주십시오.
#
###############################################################################

### LAB 7-2: 논리합을 수행하는 퍼셉트론 만들기
### W 와 b 를 학습함


import numpy as np

W, b = np.array([0, 0]), 0.0
learning_rate = 0.01  

def activation(s):
    if s > 0: return 1
    elif s < 0: return -1
    return 0

def out(x) :
    return activation (W.dot(x) + b)

def train(x0, x1, target):
    global W, b
    X = np.array([x0, x1])
    y = out(X)

    ### 예측이 맞으면 아무것도 하지 않음-------------------------------------
    if target == y: return False         # 가중치가 변경되지 않았음을 반환

    ### 예측이 틀리면 학습 실시---------------------------------------------
    print('가중치 수정전 target :{} y:{} b:{} W:{}'.format(target, y, b, W))
    W = W + learning_rate * X * target   # 입력x출력 비례하여 가중치 변경
    b = b + learning_rate * 1 * target   # 편향: 입력이 1이라고 볼 수 있음
    print('가중치 수정후 target :{} y:{} b:{} W:{}'.format(target, y, b, W))
    return True 

def predict(inputs):
    outputs = []
    for x in inputs:
        outputs.append (out(x))
    return outputs


adjusted = 0
for i in range(100):
    adjusted += train(-1,-1, -1)    # 훈련 데이터 1
    adjusted += train(-1, 1,  1)    # 훈련 데이터 2
    adjusted += train( 1,-1,  1)    # 훈련 데이터 3
    adjusted += train( 1, 1,  1)    # 훈련 데이터 4
    print("iteration -------------", i)
    if not adjusted: break  # 모든 훈련에 대해 가중치 변화 없으면 학습종료
    adjusted = 0

X = [[-1, -1], [-1, 1], [1, -1], [1,1]]
yhat = predict(X)
print('x0 x1  y')
for i in range(len(X)):
    print('{0:2d} {1:2d} {2:2d}'.format(X[i][0], X[i][1], yhat[i]))


