# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:07:42 2024

@author: Rogio
"""



import pandas as pd





기초통계 = './통계자료/기초통계.xlsx'


전체기록 = pd.read_excel(기초통계, sheet_name= 'Sheet1', index_col= 0)
전체기록.index = 전체기록.index.str.replace('회차', '').astype(int)


기록_100 = 전체기록[0:100].drop(columns = '보너스')


# 13.00%	2.49%	0.43%	0.06%	0.01%	0.00%
연속등장확률 = { '1' : 13.00,
            '2' : 2.49,
            '3' : 0.43,
            '4' : 0.06,
            '5' : 0.01
        }

# 13.04%	10.91%	9.31%	7.92%	6.68%	5.67%	4.77%	3.99%	3.36%	2.87%
연속미등장확률 = { '1' : 13.04,
                '2' : 10.91,
                '3' : 9.31,
                '4' : 7.92,
                '5' : 6.68,
                '6' : 5.67,
                '7' : 4.77,
                '8' : 3.99,
                '9' : 3.36,
                '10' : 2.87,
                '11' : 2.4,
                '12' : 2.01,
                '13' : 1.71,
                '14' : 1.46,
                '15' : 1.24,
                '16' : 1.04,
                '17' : 0.85
            }



# 각 통계는 특별한 언급 없으면 100번을 기준으로 한다.
#%% 필요변수 1, 이번에 나오면 몇 번째 연속으로 나온건지 

# 번호 1부터 45까지를 컬럼으로 가지는 DataFrame 생성
df = pd.DataFrame( columns=range(1, 46))


for i in range(0,len(전체기록)):
        
    당첨번호 = pd.DataFrame(전체기록.iloc[i])
    
    회차 = 당첨번호.columns[0]
    # 추출된 번호에 해당하는 컬럼 값에 1 할당
    
    df.loc[회차, ] = 0
    for num in 당첨번호.values:
        print(num[0])
        df.loc[회차, num[0]] = 1
    
df = df.astype(int)


#%%
# 특정 번호를 추출하는 함수
def analyze_number(df, draw_number, number):
    
    '''
    df = 전체기록
    draw_number = 1136
    number = 13
    '''
    
    
    # 분석할 회차
    current_draw_index = draw_number
    
    # 1. 연속 출현 횟수
    consecutive_count = 0
    for i in range(current_draw_index - 1, 0, -1):  # 0보다 클 때까지
        if number in df.loc[i].values:
            consecutive_count += 1
        else:
            break

    # 2. 연속 미출현 횟수
    consecutive_non_appearance = 0
    for i in range(current_draw_index - 1, 0, -1):  # 0보다 클 때까지
        if number not in df.loc[i].values:
            consecutive_non_appearance += 1
        else:
            break

    # 3. 최근 100회차 출현 횟수
    start_index = draw_number - 1
    end_index = draw_number - 101
    recent_100_count = df.loc[start_index : end_index].isin([number]).sum().sum()
    # 4. 최근 4회차 출현 횟수
    start_index = draw_number - 1
    end_index = draw_number - 5
    
    recent_4_count = df.loc[start_index : end_index].isin([number]).sum().sum()
    return {
        "연속 출현 횟수": consecutive_count,
        "연속 미출현 횟수": consecutive_non_appearance,
        "최근 100회차 출현 횟수": recent_100_count,
        "최근 4회차 출현 횟수": recent_4_count,
    }

# 예시: 1143회차의 첫번째 번호인 10을 분석
result = analyze_number(전체기록, 1136, 13)
print(result)



































