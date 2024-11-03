# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:02:29 2024

@author: Rogio
"""


from page3.get_data import Lotto_class
from collections import Counter,defaultdict

import pandas as pd


# Lotto_class의 인스턴스 생성
lotto_instance = Lotto_class()


최근회차 = lotto_instance.최근회차()

과거기록 = lotto_instance.download_records(1, 최근회차)

과거기록 = pd.DataFrame(과거기록).transpose()


#%% 두번 연속 나온 횟수
# 연속으로 나온 횟수를 저장할 리스트
data = 과거기록
# 번호별 연속 등장 횟수를 저장할 defaultdict 초기화
연속등장_횟수 = defaultdict(lambda: {'1회연속': 0,'2회연속': 0, '3회연속': 0,'4회연속': 0,'5회연속': 0,'6회연속': 0})

# 과거기록을 순차적으로 비교
for i in range(0, len(data) - 5):
    현재회차 = data.iloc[i]
    연속2 = data.iloc[i + 1]
    연속3 = data.iloc[i + 2]
    연속4 = data.iloc[i + 3]
    연속5 = data.iloc[i + 4]
    연속6 = data.iloc[i + 5]
    
    # 현재회차의 각 번호가 다음회차와 다다음회차에 포함되는지 확인
    for 번호 in 현재회차:
        if 번호 in 연속2.values:
            연속등장_횟수[번호]['2회연속'] += 1
        
            if 번호 in 연속3.values:
                연속등장_횟수[번호]['3회연속'] += 1
                
                if 번호 in 연속4.values:
                    연속등장_횟수[번호]['4회연속'] += 1
                    
                    if 번호 in 연속5.values:
                        연속등장_횟수[번호]['5회연속'] += 1
                            
                        if 번호 in 연속6.values:
                            연속등장_횟수[번호]['6회연속'] += 1
                            print(현재회차.name,번호)
        else:
            연속등장_횟수[번호]['1회연속'] += 1
                        
연속등장_횟수 = pd.DataFrame(연속등장_횟수).transpose()
#%%



# 예시 데이터 생성
data = 과거기록  # 과거 기록 데이터프레임

# 번호별 연속 미등장 횟수를 저장할 defaultdict 초기화
연속미등장_횟수 = defaultdict(lambda: {f'{i}회연속미등장': 0 for i in range(1, 31)})

# 각 번호에 대해 연속 미등장 횟수 계산
for i in range(len(data)):
    현재회차 = data.iloc[i]

    # 현재 회차의 각 번호에 대해 연속 미등장 횟수 확인
    for 번호 in 현재회차:
        연속횟수 = 0
        
        # 다음 회차부터 시작하여 연속으로 미등장하는지 확인
        for j in range(i + 1, len(data)):
            다음회차 = data.iloc[j]
            if 번호 not in 다음회차.values:
                연속횟수 += 1
            else:
                break  # 번호가 등장하면 루프를 종료

        # 연속 미등장 횟수를 기록 (최대 30회)
        for k in range(1, 31):
            if 연속횟수 >= k:
                연속미등장_횟수[번호][f'{k}회연속미등장'] += 1

# 결과를 데이터프레임으로 변환
연속미등장_횟수 = pd.DataFrame(연속미등장_횟수).transpose()
연속미등장_횟수.reset_index(inplace=True)
연속미등장_횟수.columns = ['번호'] + [f'{i}회연속미등장' for i in range(1, 31)]

# 결과 출력
print(연속미등장_횟수)

















