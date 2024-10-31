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

# HTML 및 CSS 스타일
st.markdown("""
<style>
    .lotto-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .lotto-container {
        display: flex;
        flex-direction: column;
        align-items: center; /* 가운데 정렬 */
        margin-bottom: 20px;
    }
    .lotto-label {
        text-align: center;
        font-size: 14px;
        margin-top: 5px;
    }
    .number-container {
        display: flex;
        justify-content: space-around; /* 가로 정렬 */
        width: 100%; /* 전체 폭 */
    }
    .number-item {
        width: 50px; /* 각 칸의 너비 */
        display: flex;
        flex-direction: column;
        align-items: center; /* 가운데 정렬 */
    }
</style>
""", unsafe_allow_html=True)

# 타이틀 표시
st.markdown('<div class="lotto-title">로또 번호</div>', unsafe_allow_html=True)

# 로또 번호 표시
lotto_container = st.container()
with lotto_container:
    st.markdown('<div class="number-container">', unsafe_allow_html=True)
    
    for label, value in 당첨번호.items():
        st.markdown(f'<div class="number-item"><div class="lotto-label">{label}</div><div>{value}</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
