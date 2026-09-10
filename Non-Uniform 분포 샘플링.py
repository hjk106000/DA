###############################################################################
# 비균등 분포 샘를링 예제
#
# Gemini 작성코드
#
# USER:
# 숫자 1, 2, 3, 5 를 대상으로 복원추출로 샘플링 할 때 
# 각각 10%, 20%, 30%, 50%의 비율로 추출될 수 있도록 하는
# python 코드를 작성해 줄래
###############################################################################


def create_advanced_freq_table(data_list):
    from collections import Counter
    import pandas as pd

    counter = Counter(data_list)
    df = pd.DataFrame(list(counter.items()), columns=['값 (Value)', '도수 (Frequency)'])
    
    # 비율(%) 컬럼 추가
    total_count = len(data_list)
    df['비율 (%)'] = (df['도수 (Frequency)'] / total_count * 100).round(1)
    
    return df.sort_values(by='값 (Value)').reset_index(drop=True)



def main():

    # 추출 대상 및 비율 (합: 100)
    population = [1, 2, 3, 5]
    weights = [10, 20, 30, 40]

    # Cumulative weights (누적 비율): [10, 30, 60, 100]
    # 1~10: 1 선택 / 11~30: 2 선택 / 31~60: 3 선택 / 61~100: 5 선택

    sample_size = 10  # 추출할 개수
    results = []

    # 난수 생성을 위한 시드(Seed) 값 설정
    seed = 42

    for i in range(sample_size):
        # 외부 모듈 없이 난수를 생성하는 간단한 LCG 알고리즘 (1~100 사이의 정수 생성)
        seed = (seed * 1103515245 + 12345) % (2**31)
        random_val = (seed % 100) + 1  # 1부터 100 사이의 값

        # if문으로 누적 가중치 구간을 체크하여 해당하는 숫자 추출
        if random_val <= 10:
            selected = population[0]  # 1 (10% 확률)
        elif random_val <= 30:
            selected = population[1]  # 2 (20% 확률)
        elif random_val <= 60:
            selected = population[2]  # 3 (30% 확률)
        else:
            selected = population[3]  # 5 (40% 확률)

        results.append(selected)

    print("추출된 결과:", results)



    #--------------------------------------------------------------------------
    # 파이썬에서 리스트 원소의 도수 분포표(Frequency Distribution Table)를 만드는 
    # 가장 쉬운 방법은 표준 라이브러리인 collections.Counter 를 사용하는 것이다.
    #--------------------------------------------------------------------------
    # from collections import Counter
    # #data = ['A', 'B', 'A', 'C', 'B', 'A', 'D']
    # counter = Counter(results)
    # # 도수 분포 출력
    # for item, count in counter.items():
    #     print(f"{item}: {count}개")
    # print( create_advanced_freq_table(results) )


    df = create_advanced_freq_table(results)
    print("\n----- 돗수분포표 -----\n", df)



def sub1():
    import random
    import numpy as np

    # 추출 대상 숫자
    population = [1, 2, 3, 5]

    # --------------------------------------------------
    # 방법 1: 파이썬 기본 라이브러리 (random.choices)
    # --------------------------------------------------
    # weights에 상대적 가중치를 넣어주면 자동으로 비율을 계산해 복원추출합니다.
    weights = [10, 20, 30, 50]  # 상대적 비율 (1 : 2 : 3 : 5)
    sample_size = 10           # 뽑을 개수

    result_random = random.choices(population, weights=weights, k=sample_size)
    print("random 모듈 결과:", result_random)


    # --------------------------------------------------
    # 방법 2: NumPy 라이브러리 (np.random.choice)
    # --------------------------------------------------
    # NumPy는 확률(p)의 합이 정확히 1.0이어야 하므로 정규화를 수행합니다.
    p = np.array([0.1, 0.2, 0.3, 0.5])
    p_normalized = p / p.sum()  # 합이 1이 되도록 조정

    result_np = np.random.choice(population, size=sample_size, replace=True, p=p_normalized)
    print("NumPy 모듈 결과: ", result_np)



if __name__ == "__main__":
    main()
    # sub1()

