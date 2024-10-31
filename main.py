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

st.title(str(최근회차))

당첨번호 = lotto_instance.check_num(최근회차)

st.markdown("""
<style>
    .lotto-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .lotto-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-around; /* 가로 정렬 */
        margin-bottom: 20px;
    }
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
    .lotto-label {
        text-align: center;
        font-size: 14px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 색상 지정 함수
def get_color(number):
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

# 타이틀 표시
st.markdown('<div class="lotto-title">로또 번호</div>', unsafe_allow_html=True)

# 로또 번호 표시
lotto_container = st.container()
with lotto_container:
    for label, value in 당첨번호.items():
        color = get_color(value)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f'<div class="lotto-ball" style="background-color: {color};">{value}</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'<div class="lotto-label">{label}<br>int<br>1<br>{value}</div>', unsafe_allow_html=True)

