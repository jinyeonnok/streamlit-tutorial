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

# st.title(str(lotto_instance.check_num(최근회차)))

# HTML 및 CSS 스타일
st.markdown("""
<style>
    .lotto-ball {
        display: inline-block;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: #f9c74f;  /* 공의 색상 */
        color: white;
        text-align: center;
        line-height: 50px;  /* 수직 정렬 */
        font-size: 20px;
        margin: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# 로또 번호 표시
st.write("로또 번호:")
for key, value in 최근회차.items():
    st.markdown(f'<div class="lotto-ball">{value}</div>', unsafe_allow_html=True)

# 빈도 = lotto_instance.빈도추출(최근회차-5,최근회차)


