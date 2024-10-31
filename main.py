# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:34:50 2024

@author: Rogio
"""

import streamlit as st
from page3.get_data import Lotto_class

import pandas as pd

# Lotto_class의 인스턴스 생성
lotto_instance = Lotto_class()


st.title('이번주 당첨번호')

최근회차 = lotto_instance.최근회차()

st.title(f'최근 회차 : {최근회차}')
# st.title(f'당첨번호 : ')

당첨번호 = lotto_instance.check_num(최근회차)


# HTML 및 CSS 스타일
st.markdown("""
<style>
    .lotto-ball {
        display: inline-block;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        color: white;
        text-align: center;
        line-height: 50px;  /* 수직 정렬 */
        font-size: 20px;
        margin: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
    .lotto-container {
        display: flex;
        justify-content: center; /* 가운데 정렬 */
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 색상 지정 함수
def get_color(number):
    number = int(number)
    if 1 <= number <= 10:
        return "#f9c74f"  # 노란색
    elif 11 <= number <= 20:
        return "#007bff"  # 파란색
    elif 21 <= number <= 30:
        return "#dc3545"  # 빨간색
    elif 31 <= number <= 40:
        return "#6c757d"  # 회색
    elif 41 <= number <= 45:
        return "#28a745"  # 녹색
    else:
        return "#000000"  # 기본 색상

def display_lotto_numbers(numbers):
    lotto_balls_html = '<div class="lotto-container">'
    for value in numbers.values():
        color = get_color(value)
        lotto_balls_html += f'<div class="lotto-ball" style="background-color: {color};">{value}</div>'
    lotto_balls_html += '</div>'
    st.markdown(lotto_balls_html, unsafe_allow_html=True)
    

# 탭 추가
tab1, tab2 = st.tabs(["현재 당첨 번호", "과거 당첨 기록"])

with tab1:
    st.header("현재 당첨 번호")    
    display_lotto_numbers(당첨번호)

with tab2:
    st.header("과거 당첨 기록")
    주차선택 = st.selectbox("주차를 선택하세요:", 
                             ["1주 전", "2주 전", "3주 전", "4주 전", 
                              "2달 전", "3달 전", "기타"])

    # 선택된 주차에 따른 데이터 출력
    if 주차선택 == "1주 전":
        과거기록 = lotto_instance.download_records(최근회차, 최근회차)
    elif 주차선택 == "2주 전":
        과거기록 = lotto_instance.download_records(최근회차-1, 최근회차)
    elif 주차선택 == "3주 전":
        과거기록 = lotto_instance.download_records(최근회차-2, 최근회차)
    elif 주차선택 == "4주 전":
        과거기록 = lotto_instance.download_records(최근회차-3, 최근회차)
    elif 주차선택 == "2달 전":
        과거기록 = lotto_instance.download_records(최근회차-7, 최근회차)
    elif 주차선택 == "3달 전":
        과거기록 = lotto_instance.download_records(최근회차-11, 최근회차)


    # 과거 기록 출력
    if 과거기록:
        
        # 과거기록 = 과거기록.iloc[::-1]
        for 회차, 번호 in 과거기록.items():
            st.subheader(f"{회차}회차")
            display_lotto_numbers(번호)
    else:
        st.write("해당 기록이 없습니다.")






















